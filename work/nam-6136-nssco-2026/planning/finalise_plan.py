"""Validate the concrete 6136 plan and generate the operator-facing PLAN/HANDOVER."""
import hashlib
import json
from collections import Counter
from pathlib import Path
import re
import yaml
import jsonschema

WS=Path(__file__).resolve().parents[1];REPO=WS.parents[1];STD=REPO/'standard/v0.2.0-draft';CUR=WS/'curriculum'
def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
summary=read(WS/'planning/plan-summary.json'); facts=read(CUR/'syllabus-facts.json')
reg=read(CUR/'objective_registry.json');objs={o['objective_id']:o for o in reg['objectives']}
fw=read(CUR/'assessment-framework.json');sp=yaml.safe_load((WS/'subject-profile.yaml').read_text());qp=yaml.safe_load((WS/'qualification-profile.yaml').read_text())
ev=read(WS/'assessment-evidence/assessment_evidence.json');exp=read(CUR/'exam-exposure.json')
bridge=read(CUR/'source-bullet-bridge.json')['entries'];cmds={c['word']:c for c in fw['command_words']}
mis=read(CUR/'misconceptions.json')['entries'];shapes=read(CUR/'answer-shapes.json')['6136']['shapes']
gloss=read(CUR/'glossary.json')['entries'];scope=read(CUR/'scope-scan.json')['entries']
schema_results={}
for name,data in [('objective_registry',reg),('qualification_profile',qp),('assessment_evidence',ev)]:
 errors=list(jsonschema.Draft202012Validator(read(STD/f'schemas/{name}.schema.json')).iter_errors(data))
 assert not errors,[(list(e.path),e.message) for e in errors]
 schema_results[name]='PASS'
subject_errors=list(jsonschema.Draft202012Validator(read(STD/'schemas/subject_profile.schema.json')).iter_errors(sp))
# Do not suppress stale-schema errors. Record them visibly as a standard-owner issue.
schema_results['subject_profile']=[{'path':list(e.path),'message':e.message} for e in subject_errors] or 'PASS'
assert len(ev['records'])==419 and sum(x['mark_tariff'] for x in ev['records'])==1000
assert all(set(r['objective_ids'])<=set(objs) for r in ev['records'])
assert len(bridge)==102
expected={o['source_bullet_id'] for t in facts['content_outline'] for o in t['specific_objectives']}
assert {b['source_bullet_id'] for b in bridge}==expected
assert len({b['registry_parent_id'] for b in bridge})==101
assert all(x['registry_parent_id'] in objs and set(x['registry_member_ids'])<=set(objs) for x in bridge)
wo_by_topic={}; spec=[]; exact=Counter(); total=0; slots=[]; mappedmis=[]
performance_blueprints=read(CUR/'performance-decisions.json')['topics']
for t in summary['topics']:
 tid=t['topic_id'];wo=read(WS/'topics'/tid/'work_order.json');c=read(WS/'topics'/tid/'contract.json');wo_by_topic[tid]=wo
 assert {o['objective_id'] for o in reg['objectives'] if o['topic_id']==tid and o['parent_id']}==set(c['scope']['included_objective_ids'])
 assert len(c['depth_constraints']['excluded_constructs'])==len(scope)
 assert c['depth_constraints']['excluded_constructs']==[{k:e[k] for k in ['construct','pattern','source']} for e in scope]
 for s in wo['item_slots']:
  assert s['command_word'] in cmds and cmds[s['command_word']]['use_in_prompts']
  assert s['mark_tariff'] in cmds[s['command_word']]['observed_tariffs'],s
  assert set(s['assessment_objectives'])<=set(objs[s['objective_id']]['assessment_objectives'])
  assert s['blooms_level'] in ['Remember','Understand','Apply','Analyse','Evaluate','Create']
  total+=s['mark_tariff'];slots.append(s['slot'])
  for a in s['assessment_objectives']:exact[a]+=s['mark_tariff']/len(s['assessment_objectives'])
  if s.get('misconception_entry'):mappedmis.append(s['misconception_entry'])
 for i,p in enumerate(wo['performance_tasks']):
  blueprint=performance_blueprints[tid][i]
  assert blueprint['item_type']==p['item_type']
  components=blueprint['parts'];cycle=blueprint.get('cycle')
  ao=Counter()
  for component in components:
   word=component['command_word'];n=component['mark_tariff'];alloc=component['ao_split_judgement']
   assert n in cmds[word]['observed_tariffs'],(word,n)
   assert sum(alloc.values())==n
   ao.update(alloc)
  marks=sum(x['mark_tariff'] for x in components)
  exact.update(ao);total+=marks;slots.append(p['slot'])
  entry={'slot':p['slot'],'topic_id':tid,'item_type':p['item_type'],'title':blueprint['title'],
         'blooms_level':p['blooms_level'],'command_word':components[0]['command_word'],
         'mark_tariff':marks,'assessment_objectives':list(ao),'ao_split_judgement':dict(ao),
         'cycle':cycle,'subparts':components,
         'allocation_authority':'judgement; indicative new practice rubric, not an official item allocation',
         'prompt_policy':'Every subpart and its required original data must be self-contained in the package. Supply a fictional model and transfer own-investigation parts to actual learner work.'}
  if tid=='10.1':
   sections=Counter()
   for part in components:sections[part['section']]+=part['mark_tariff']
   assert sections['A1']+sections['A2']==35 and sections['B']==15
   entry['section_totals']=dict(sections)
  spec.append(entry)
 assert len(wo['item_slots'])+len(wo['performance_tasks'])==c['required_outputs']['learning_items']==t['items']
demand=read(CUR/'objective-demand.json')['objectives']
NUMERICAL={'1.1:4':'GNP divided by population, with period/currency stated',
 '3.1:10':'sector employment as a percentage of total employment',
 '4.2:1':'urban population share or its percentage-point change',
 '6.2:2':'participation share or percentage change in a supplied gender-development dataset',
 '7.1:1':'population divided by area, in people per square kilometre',
 '7.1:3':'natural increase from crude birth/death rates, preserving per-thousand units',
 '7.1:6':'an age-group share from supplied population counts',
 '7.2:1':'service-access share or change from original health-development counts',
 '7.3:4':'literacy or enrolment share using the specified denominator',
 '9.1:3':'exports minus imports, with currency and period',
 '9.1:4':'absolute or percentage change in supplied trade values',
 '10.1:11':'survey share, absolute difference or percentage-to-angle conversion'}
slot_specs=[]
for tid,wo in wo_by_topic.items():
 for slot in wo['item_slots']:
  d=demand[slot['objective_id']];st=slot['subtype'];ao=slot['assessment_objectives']
  require={'DEF':'One precise meaning; essential terminology, without a compulsory extra boundary question.',
   'FEATURE':'Recognise or describe the specified feature/role. Do not relabel factual description as analysis.',
   'DIST':'Directly pair the same defining characteristic across the specified concepts; no unrelated lists.',
   'WHY':'Explain the relevant reason in the stated syllabus context; ordinary knowledge/application is A.',
   'APP':'Use the stated contextual constraint to select or justify an appropriate action. The contextual fact must change the answer.',
   'CHAIN':'Supply a new short case with at least two material facts/conditions. Require an inference that traces mechanism to consequence from those facts; a memorised general explanation is insufficient for B.',
   'INTERP':'Supply a self-contained original table/map specification or two contrasting sources. Require a relationship inferred from at least two relevant observations, not mere naming or copying. No mandatory extra limitation at this short tariff.',
   'EVAL':'Specify alternatives, a development criterion and original evidence/constraints. Require a justified choice or weighing. Explain must ask for that decision reasoning, not a generic advantage list. Extra counterarguments/conditions only where material to the question.',
   'PROC':'Describe the ordered procedure in this specific situation, including the relevant selection/collection/recording or construction steps. A definition alone is not application.',
   'CALC':'Provide original figures; ask for the specified calculation with working and unit. Do not tack interpretation/rounding discussion onto two marks unless explicitly asked.',
   'MISCON':'Discriminate the named misconception in a new example; error and correct distinction are required, not boilerplate about an unrelated topic.'}[st]
  if st=='APP' and ao==['D']:require='State a concrete research/community implementation obstacle, available resources and responsible actors. Require a feasible matched response and its practical reason; do not substitute recalling a method.'
  if st=='EVAL':
   from repair_review_demands import EVAL_REQUIREMENT
   require=EVAL_REQUIREMENT
  if st=='CALC':require+=' Notes must explicitly teach the formula, units, denominator and a worked example before this practice.'
  rec={'slot':slot['slot'],'objective_id':slot['objective_id'],'target':objs[slot['objective_id']]['learner_objective'],
       'subtype':st,'command_word':slot['command_word'],'mark_tariff':slot['mark_tariff'],
       'assessment_objectives':ao,'blooms_level':slot['blooms_level'],
       'task_requirement':require,'command_authority':d['command_decisions'],
       'source_bullet_key':d['source_bullet_key'],'semantic_status':'planner judgement; final reviewer must check the authored task actually meets this requirement'}
  if st=='CALC':
   assert d['source_bullet_key'] in NUMERICAL,d
   rec['calculation_target']=NUMERICAL[d['source_bullet_key']]
  if st=='MISCON':rec['misconception_entry']=slot['misconception_entry']
  slot_specs.append(rec)
dump(CUR/'slot-demand-specs.json',{'authority':'Explicit task requirements resolve Claude F-03/F-09/F-17. They do not claim that future prose is already semantically validated.','slots':slot_specs})
assert len(slots)==len(set(slots))==summary['totals']['items']
assert Counter(mappedmis)==Counter(m['entry_id'] for m in mis)
exactpct={a:round(100*exact[a]/total,4) for a in ['A','B','C','D']}
targets=fw['ao_mark_budget']['stated_qualification_weight_percent']
gap=max(abs(exactpct[a]-targets[a]) for a in targets)
assert gap<=5,(exactpct,gap)
dump(CUR/'performance-slot-specs.json',{'authority':'Generated from declared performance plans and explicit component judgements. Work order IDs remain authoritative.',
                                    'slots':spec})
# Recompute every registry exposure independently from canonical evidence.
for e in exp['objectives']:
 rs=[r for r in ev['records'] if e['objective_id'] in r['objective_ids']];v=e['evidence']
 assert v['question_parts_naming_it']==len(rs)
 assert v['distinct_series']==len({r['exam_series'] for r in rs})
 assert v['max_mark_tariff']==max([r['mark_tariff'] for r in rs] or [0])
 assert v['command_words_observed']==dict(Counter(r['command_word'] for r in rs))
 assert set(v['evidence_ids'])=={r['evidence_id'] for r in rs}
 for st in e['required_subtypes']:
  assert any(s['objective_id']==e['objective_id'] and s['subtype']==st for s in wo_by_topic[e['topic_id']]['item_slots'])
for e in scope:
 rx=re.compile(e['pattern'],re.I)
 assert all(rx.search(x) for x in e['controls']['must_catch']) and not any(rx.search(x) for x in e['controls']['must_allow'])
ex=read(WS/'exemplar/validation.json')
assert all(not x['failures'] for x in ex['slices'])
quality=read(CUR/'quality-evidence.json')
shape_ids={s['id'] for s in shapes}
for criterion in quality['criteria']:
 assert set(criterion['answer_shape_ids'])<=shape_ids
 assert len(criterion['citations'])==len(criterion['answer_shape_ids'])
 for citation in criterion['citations']:
  assert citation['source_locator'] and citation['evidence_ids']
for wo in wo_by_topic.values():
 for slot in wo['item_slots']+wo['performance_tasks']:
  assert slot['marking_guidance_must_name']==sp['answer_structures'][slot.get('subtype') or slot['item_type']]

compat=[
 {'issue':'run_checks.py exits nonzero even when JSON decision is publish',
  'evidence':'The wrapper compares release_decision to pass, while yyeni_checks.run returns publish/reject.',
  'status':'Observed on both exemplars: JSON PUBLISH, zero deterministic failures, process exit 1. No exit code is silently reclassified.',
  'action':'Standard maintainer should align the wrapper with the runner. Until resolved, report JSON decision, failure counts, no-opinion checks and exit code explicitly.'},
 {'issue':'Subject-profile schema predates the supported profile extensions',
  'evidence':'subject_profile.schema.json rejects slot_plan, conditioned_mechanisms and depictions, while the build and checks explicitly consume them (CR-006 and C-37).',
  'status':'Open standard-owner discrepancy; full subject-profile schema validation does not pass. No schema changed or error filtered.',
  'action':'Vitalis/standard maintainer should reconcile the schema with the documented supported fields before recording the NSSCO pilot as complete.'},
 {'issue':'Graph rendering/checking is limited to business break-even charts',
  'evidence':'C-35/C-41 and context.chart schema support break-even parameters, not Development Studies pie/bar graphs, maps or population pyramids.',
  'status':'No compatible graphical check; no deterministic graph PASS is claimed. Tables and learner plotting tasks use the supported no-renderer depiction policy.',
  'action':'Independently recompute original graph datasets, percentages, pie angles, scales and labels. Resolve any check that is required but inapplicable in the standard, not through a workspace bypass.'},
 {'issue':'PUBLISH is not equivalent to every check passing',
  'evidence':'The runner returns PUBLISH with no failures even when checks are not_run; TEAM-PLAYBOOK.md says not_run is never a pass.',
  'status':'Every exemplar no-opinion check is listed in validation.json and must be visible in final QA. No publication or pilot completion claimed.',
  'action':'Follow the playbook. Do not count a required missing-input check as passed; standard owner resolves actual pilot incompatibilities.'},
 {'issue':'Generated contract narrative says Cambridge and default AO commentary names AO1–AO4',
  'evidence':'The stock contract and AO commentary contain Cambridge/AO1–AO4 prose even with correct 6136 data and A/B/C/D labels.',
  'status':'Cosmetic template mismatch in internal generated text. PLAN and HANDOVER explicitly use NIED/DNEA and A/B/C/D; never copy boilerplate into learner prose.',
  'action':'Standard maintainer should generalise the narrative. Do not edit generated outputs or standard here.'}
]
dump(WS/'planning/standard-compatibility.json',compat)
validation={'status':'PASS for enumerated planning checks; standard compatibility issues remain separately open',
            'schema_checks':schema_results,'source_bullets_bridged':len(bridge),'unique_source_outcomes':101,
            'assessable_targets':sum(bool(o['parent_id']) for o in reg['objectives']),'question_parts':len(ev['records']),
            'question_marks':1000,'unique_slots':len(slots),'misconception_slots':len(mappedmis),
            'all_slot_command_tariffs_observed':True,'all_scope_controls_carried':True,
            'exact_marks_equivalent':total,'exact_ao_marks':dict(exact),'exact_ao_percent':exactpct,
            'exact_largest_gap_points':gap,
            'relative_shortfall_percent':{a:round(max(0,targets[a]-exactpct[a])/targets[a]*100,2) for a in targets},'standard_rounded_rollup':'curriculum/ao_coverage.md',
            'exemplar':ex,'quality_evidence_criteria':len(quality['criteria']),
            'generated_guidance_matches_subject_profile':True,
            'standard_compatibility':'planning/standard-compatibility.json',
            'not_a_claim':'This does not validate the truth of future resources, count not_run as pass, complete Step 4 human approval or record publication.'}
dump(WS/'planning/plan-validation.json',validation)

stem='6136-nssco-development-studies'
L=['# Plan — NSSCO Development Studies 6136','',
   'Revised 2026-10-20 after Claude Code’s FIX PLAN FIRST review. Whole subject, Grades 10–11. Jeremy approved this version conditionally on completing and validating the revisions, then explicitly authorised Codex to start building. Codex authors the final resources; Claude Code independently reviews afterwards.','',
   '## 0. What the syllabus says','',
   'NIED 2017, implementation 2019, first examination 2020, no stated terminal year. The workspace year 2026 is intended use. All ten themes and all 18 topics are covered. No previous Junior Secondary Development Studies study is assumed.','',
   '| AO | Name | Qualification | P1 marks | P2 marks | P3 marks |','|---|---|---:|---:|---:|---:|']
for a in facts['assessment_objectives']:
 L.append(f'| {a["code"]} | {a["name"]} | {targets[a["code"]]:g}% | '+ ' | '.join(str(p['ao_marks'][a['code']]) for p in facts['papers'])+' |')
L+=['','Aggregate percentages are derived from the printed sub-objective grid on p.20 / PDF23. A.1/A.2 are combined in the source and are not split here. Paper 3 guidance on p.22 mentions C/D broadly; the detailed grid additionally assigns B15, retained above.','']
for p in facts['papers']:L.append(f'- Paper {p["paper"]}: {p["marks"]} marks, {p["duration_minutes"]} minutes, {p["weight_percent"]}% of the qualification. '+{'1':'Four compulsory 20-mark questions.','2':'Two compulsory 35-mark questions.','3':'Section A supplied-investigation tasks, 35 marks; Section B own investigation, 15 marks.'}[p['paper']])
L+=['','Each learner presents their own investigation report, even when collection was in a group. It is preparation for written Paper 3 questions, not formally assessed coursework.','',
    '## 1. What the corpus says','',
    'Fifteen 2020–2024 papers: 419 assessed parts, 1,000 marks. All paper and root-question totals reconcile. Five reports support the study weaknesses, thirty conceptual confusions and fifteen answer-shape exemplars. No standalone mark schemes or 2025 sources are held; proof versions and ambiguous report rubrics remain in assessment-evidence/GAPS.md.','',
    'The source-bullet evidence is preserved in planning/source-bullet-evidence.json. The canonical assessment map now uses registry IDs, conforms to its schema, and still contains every paper part. It is labelled partial because scheme coverage and member-level mapping are incomplete. Ninety-one explicit member assignments supplement conservative parent mappings. Unassigned members are not claimed absent from examinations. No parent frequency is inherited by every child.','',
    '## 2. Command words and tariffs','',
    'One operative command per assessed part is counted. Define includes the printed what-is-meant-by synonym. Compounds remain compounds. Use each slot’s command and tariff; all selected pairs are observed. Parent task totals are packages of subparts, not invented 15- or 35-mark single commands.','',
    '| Command | Parts | Modal tariff(s) | Observed tariffs |','|---|---:|---|---|']
for c in sorted([c for c in fw['command_words'] if c['observed_count']],key=lambda c:-c['observed_count']):
 L.append(f'| {c["word"]} | {c["observed_count"]} | '+', '.join(map(str,c['modal_tariffs']))+' | '+', '.join(map(str,c['observed_tariffs']))+' |')
L+=['','Standalone Analyse, Evaluate and Assess do not open any planned prompt. Differentiate, Design and Outline are observed despite not being separate glossary entries. Syllabus glossary inclusion alone never authorises a command. The framework retains all measured verdicts, including rare interrogative forms.','',
    '## 3. Answer shapes','',
    'Use curriculum/answer-shapes.json for fifteen report-backed examples, with their specific limits. Some graphs, reports and conclusions are level-marked. Guidance requirements are minimal and tariff-scaled: short interpretations need evidence and a relationship; calculations need working and units; limits or extra counterarguments are not compulsory boilerplate. An Identify-three-factors part can be worth one mark; there is no universal one-point-per-bullet rule. New practice rubrics must fit the original task and be labelled indicative internally. Exact unseen official allocations are not invented.','']
for s in shapes:L.append(f'- {s["id"]}: {s["command"]} {s["marks"]}; '+s['allocation']+' '+s['guard'])
L+=['','## 4. Card types, assessment objectives and Bloom levels','',
    'AOs measure credited skills; Bloom labels measure the cognitive demand. They are different axes. A includes application in its syllabus wording. C labels in research practice do not create an additional general knowledge AO on Paper 3. All slot labels are planner judgements, not official item-level AO marks.','',
    '| Subtype | Required answer parts | Permitted AOs | Bloom |','|---|---|---|---|']
for s in fw['flashcard_subtype_ao_map']:L.append(f'| {s["subtype"]} | '+', '.join(sp['answer_structures'][s['subtype']])+f' | {"/".join(s["assessment_objectives"])} | {s["blooms_level"]} |')
L+=['','Performance items have explicit labels and subpart plans in curriculum/performance-slot-specs.json. There are no MCQ sets or invented extended Evaluate essays.','',
    '## 5. The topics','',
    f'{summary["totals"]["objectives"]} assessable teaching targets comprise {len({b["registry_parent_id"] for b in bridge})} canonical source outcomes and {summary["totals"]["objectives"]-len({b["registry_parent_id"] for b in bridge})} separately practised members, alongside {len(summary["topics"])} structural roots. The enterprise continuation is consolidated. Illustrative example lists are taught inside their parent lessons rather than becoming compulsory card sets. Recurring concepts have cross-links and distinct uses. Parent source verbs and member roles determine the practice, not a universal two-card template.','',
    '| Topic | Title | Targets | Items | Notes words |','|---|---|---:|---:|---:|']
for t in summary['topics']:L.append(f'| {t["topic_id"]} | {t["title"]} | {t["objectives"]} | {t["items"]} | {t["notes_words"]["min"]:,}–{t["notes_words"]["max"]:,} |')
tot=summary['totals']
L+=['',f'**{tot["topics"]} topics; {tot["objectives"]} teaching targets; {tot["flashcards"]} flashcards and {tot["performance_tasks"]} practical/structured activities = {tot["items"]} items; {tot["words_min"]:,}–{tot["words_max"]:,} notes words.** These are generated allocation ranges. Treat upper bounds as planning ceilings and lower bounds as advisory; concise complete teaching is preferable to repeated definitions or padding. Record justified shorter units and their C-26 warnings. The main plan has no authored claims, units or items yet.','',
    'Each content topic has two six-mark mini-tasks, with Calculate in numerical topics and source comparison/decision tasks elsewhere. Research has four distinct full 50-mark packages: water access, rural production, education access and community waste. Every package has two supplied-stimulus questions totalling 35 and an own-investigation section of 15. Two packages explicitly plan a small community project, including aims, organisation, funding, obstacles, responses and implementers. Fictional model enquiries teach method; learners then use their own real investigation. No fabricated fieldwork is attributed to them.','',
    '## 6. AO balance, in marks','',
    '| AO | Planned (exact recomputation) | Syllabus | Gap |','|---|---:|---:|---:|']
for a in targets:L.append(f'| {a} | {exactpct[a]:.2f}% | {targets[a]:g}% | {exactpct[a]-targets[a]:+.2f} points |')
L+=['',f'Largest exact gap: **{gap:.2f} points** across {total:,} marks-equivalent of practice. The standard rounded rollup reports largest gap 4 points, inside the playbook limit of five. Marks-equivalent is a planning estimate; it is not an official marking scheme. Item-count balance is descriptive only. No AO top-up loop or bank padding was used. This calculation does not itself prove task demand: curriculum/slot-demand-specs.json requires evidence/inference for every B-labelled interpretation or causal task and a real decision for evaluation.','',
    'Research allocations now follow the actual designed subparts rather than forcing each package to B15/C25/D10. The syllabus grid remains the target; all per-item allocations are explicit planning judgements. Absolute AO gaps and relative shortfalls are both reported in plan-validation.json. The skill balance still requires semantic review of the actual authored questions, not just arithmetic on labels.','',
    '## 7. Misconceptions, glossary and scope','',
    f'- {len(mis)} report-evidenced pairs each have exactly one named MISCON slot and an independent discrimination test.',
    f'- {len(gloss)} settled conceptual glossary entries guide consistent original authoring; they are planner definitions, not asserted official quotations.',
    f'- {len(scope)} syllabus-based scope/instruction patterns are present in every generated contract with catch/allow controls. No syllabus topic is removed.',
    '- Neighbouring-topic ownership guides depth, not passing references. Historical plans and population policies remain dated examples. Current policies, agency actions, legal or health claims require official verification before authoring.',
    '- Conditions travel with claims: wood use depends on regrowth/harvesting balance; local tourism income depends on local participation or retention. Avoid blanket claims about regions, societies, women or people living with HIV. Discuss GBV and baby dumping sensitively without blame, unsupported causal certainty or invented current statistics.','',
    '## 8. Rules particular to this subject','',
    '1. All ten themes receive teaching and practice, regardless of corpus frequency.',
    '2. No copied exam stems, report phrases or marking prose reach learners. Use original scenarios and figures.',
    '3. Explanations show a mechanism and consequence; comparisons pair the same feature; data answers use relevant figures.',
    '4. Numerical work distinguishes absolute differences, percentage changes and percentage points; show method, working, units and interpretation.',
    '5. Research notes connect topic → question/hypothesis → aims → instrument and pilot → sample → data → presentation → findings → conclusion → feasible recommendation and implementer → evaluation.',
    '6. Teach suitable bar/pie charts, divided rectangles, tables, sketch maps and flow charts from the Paper 3 guidance. Ask learners to construct representations from supplied original data. Answers specify axes, scale, labels, calculated values and shape. Do not claim an unseen visual has been checked or use an invented hand-rendered plot.',
    '7. Generate no line-graph construction exercises under the report-based practice policy. Teach random, systematic and stratified sampling, not adjacent sampling curricula. These teaching boundaries and per-theme depth ceilings are explicit in contracts; no content theme is removed.',
    '8. Claims remain unverified/non-publishable in the structured authoring model until the prescribed review process; a deterministic PUBLISH result is reported with all warnings and not_run checks.',
    '9. Structural examples are in exemplar/proof/work/nam-6136-nssco-2026/. Their reduced registry and budgets never replace the full plan. Each item now has a topic-specific rubric; C-16 checks keywords, not the truth or relevance of marking. Both examples have zero deterministic failures; C-35/C-41/C-43 have no opinion and are explicitly listed.',
    '10. planning/standard-compatibility.json records unresolved standard-level discrepancies, including stale profile schema and graph support. Nothing under standard/ was modified. Required pilot incompatibilities must be resolved by the standard owner before pilot completion is recorded.',
    '11. Codex authors after Jeremy approves and commits the plan; Claude Code independently reviews after authoring. Agents do not commit/push or import to YYeni. Comparison and import approval are later steps.','',
    'Quality requirements are linked to 6136 report examples in curriculum/quality-evidence.json. At Jeremy’s direction on 2026-10-20, reusable reasoning, fieldwork and quantitative patterns from existing subject profiles were adapted. The 6136 syllabus, papers and reports remain authoritative. There is no additional two-topic authoring trial or blanket requirement to access a subject teacher. The existing structural exemplars remain file-format demonstrations, not an extra approval stage.','',
    '**Approval recorded:** Jeremy explicitly approved the revised version once these corrections are complete and validated, and authorised starting the build. Record completion of the revision audit in STATUS.md and proceed to sequential Codex authoring. The human git commit remains a separate task and is not silently marked done; Jeremy’s explicit instruction permits building before that commit. No platform import is authorised.','']
(WS/f'PLAN-{stem}.md').write_text('\n'.join(L))

H=f'''# Handover — NSSCO Development Studies 6136

Workspace: `work/nam-6136-nssco-2026/`. Owner: Jeremy. Final author: Codex.
Independent final reviewer: Claude Code. Whole subject, Grades 10–11.

**Authoring authorisation:** Jeremy explicitly approved this revised version once the Claude-feedback corrections are complete and validated, and authorised starting the build (2026-10-20). Confirm the revision audit in STATUS.md, then begin. The human plan commit remains pending; Jeremy’s explicit instruction permits building before it. Never commit or push on his behalf.

## Start here

Read TEAM-PLAYBOOK.md, AGENTS.md, the AUTHOR role at Step 5, STATUS.md and PLAN-{stem}.md. The playbook decides sequence/checkpoints. This handover wins over conflicting generic AUTHOR defaults. Sources, corrected syllabus and corpus checkpoints are already approved; do not repeat them. Do not use the old three-theme retrofit’s process exceptions.

Jeremy rejected an additional two-topic authoring trial and a blanket teacher-access requirement on 2026-10-20. Use the approved 6136 syllabus, papers and examiner reports as the basis for quality. Read curriculum/quality-evidence.json for the specific source-backed criteria, and subject-profile.yaml for the adapted reasoning/method/answer requirements. Existing subject profiles supplied reusable patterns; their content, AO weights, tariffs and commands do not govern this subject. Keep genuine source and technical limitations explicit. Follow the existing whole-subject playbook checkpoints without adding a new trial stage.

## The job

Author all {tot['topics']} topics: {tot['flashcards']} flashcards plus {tot['performance_tasks']} structured/practical activities. The per-topic generated work order is authoritative. Treat integrated outcomes and their retained members as related teaching targets, not unrelated essays. Illustrative examples remain taught but are folded into parent lessons. Read curriculum/objective-demand.json for semantic roles and command provenance. Parent items must require a relationship or application distinct from the member items. Notes upper budgets are planning ceilings; lower allocations are advisory warnings, not a requirement to pad. Report shorter complete units and genuine duplication/depth problems.

For each topic produce its claim ledger, content-units and learning-items files, then render notes using the standard tool. Read the two thin structural examples under exemplar/proof/work/nam-6136-nssco-2026/topics/. They demonstrate structure and traceability, not volume or final prose. These are thin Codex planning examples; final resources must meet the full work orders and must not be represented as independently reviewed because the examples passed structural checks.

Codex authors topics one after another in this session, as Step 5 directs. Write only this subject’s authorised topic paths. Never commit or push. Re-run each topic’s checks and fix failures; Claude Code independently reviews the completed subject at Step 6.

## Every item carries its labels

Use each flashcard slot’s exact id as item_id, subtype, assessment_objectives, blooms_level, command_word and mark_tariff. Each flashcard’s actual demand is specified in curriculum/slot-demand-specs.json; fulfil its source/inference/decision requirement, not only the labels. Each performance slot has its full labels and subparts in curriculum/performance-slot-specs.json. Use the first subpart command as the parent item command; parent tariff is the sum of parts. The full research packages contain A1+A2=35 and B=15 marks, 50 total; these are package totals, not single-command tariffs. Keep A/B/C/D, not generic AO1–AO4. All practice AO splits are planner estimates.

Claims have revision 1 initially, verification.status unverified and publishable false; items/units use review_required. Cite claims that genuinely support each objective. Teach every cited claim in a content-unit block. Stamp each block/item with claims_seen and authored_hash after authoring; use the exact _artefact_text algorithm demonstrated in the exemplar. Preserve a proper revision trail on repairs.

## Rules that come from the syllabus and the corpus

1. Fill every slot once. Use the slot’s observed command/tariff; standalone Analyse, Evaluate and Assess do not open prompts. Syllabus glossary inclusion alone is insufficient.
2. Read answer-shapes.json and retain the limits on each exemplar. New rubrics are indicative original practice guidance, never attributed as official schemes. No universal one-mark-per-bullet rule; graphs, conclusions and reports can have bands.
3. Every MISCON slot names its register entry, distinguishes the two ideas and includes a separating test. Do not turn a study habit into an invented evidenced misconception.
4. Use glossary.json consistently; explain terms in ordinary language before asking learners to apply them.
5. Never copy assessment wording, scenarios, report phrases or answer allocations. Internal evidence and the Step 3 snapshots must not be rendered to learners.
6. Use invented organisations, Namibian/southern African settings, British English and N$. Label synthetic data as such. Do not invent current facts or claims about real people or institutions.
7. Historical NDP, population-policy and NIC examples stay in source context. Verify any current policy, agency function, health or legal statement against a primary official source and record the date/source. Prefer conceptual explanations where a current claim adds nothing.
8. Research is practical: explain instruments, sampling decisions, pilots, representation, findings, conclusions, recommendations and methodological limits with evidence. Learners may collect in groups but each presents an individual report; it is not formal assessed coursework. Fictional model enquiries must never be presented as learners’ actual work.
9. Recompute every number. Distinguish percentage points from percentage change and totals from per-person measures. No supplied value is silently invented in an answer.
10. Depictions follow the profile’s supported no-renderer policy: original tables and learner plotting/construction tasks, with explicit model coordinates, axes, scales, keys and labels. Teach the syllabus forms, including sketch maps and flow charts. No hand-authored ASCII or code-fenced plots. C-35/C-41 have no compatible general Development Studies graph model; do not claim their not_run results are passes. Graph-data correctness and suitability require independent review.
11. Keep conditions and variant distinctions with the relevant claims. Treat gender, violence, poverty, traditional societies and HIV sensitively and without stereotyping or unsupported absolutes.
12. Contracts carry the syllabus instruction/assessment safeguards plus a labelled sampling-depth policy. Every contract includes a generated per-theme teaching ceiling. No content theme is excluded. Scope patterns cannot replace semantic reading. Generate no line-graph construction tasks under the examiner-report-based practice policy.

## Voice

Direct explanatory prose for Namibian secondary learners who may be meeting the subject for the first time. Notes must stand alone offline. Use developed explanations and short original worked examples; avoid lists where learners need to see a mechanism or decision.

## The work order is a baseline, not a cage

Report a genuinely unsuitable slot and record every proposed change as {{from, to, why}} in the topic’s authoring_notes.json. Do not silently alter labels or reduce the plan to fit what was written. Planner corrections and regeneration belong to the planning role; authors do not edit curriculum, contracts or work orders. A persistent check failure after three attempts is reported with attempts/evidence, then the lead continues other topics.

## Finishing each topic

Run from the repository root, using the environment with yaml/jsonschema available:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-6136-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py work/nam-6136-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py work/nam-6136-nssco-2026 <T>
```

The current run_checks wrapper prints DECISION: PUBLISH with zero failures but exits nonzero because it compares release_decision to pass. Record the JSON decision and actual failures explicitly; do not change the standard or treat an unexplained exit as a pass. what_to_fix.py supplies the prescribed fix loop.

The lead re-runs every topic’s checks. Report warnings and not_run by id/reason. The playbook says not_run is never a pass; any required pilot-incompatible check is referred to the standard owner. Read planning/standard-compatibility.json, especially the stale subject-profile schema and graph-check limitations. Do not mark the NSSCO pilot complete while a required compatibility issue remains unresolved.

After authoring passes the applicable gates and required standard issues are resolved, use publish_subject.py as Step 5 directs. This creates repository upload output; it does not import into YYeni. Independent Claude Code review follows as Step 6, with its human commit/start checkpoint.

## Boundaries

Write only this subject’s assigned topic files, designated status and generated publish output at the authorised stage. Never edit standard/, original sources, another workspace, curriculum, the generated plan or the exemplar. No commits/pushes, no platform mutations/imports. Distinguish planning examples from completed Codex-authored topics. Claude Code is the independent resource reviewer. The cross-vendor review is required even if all deterministic checks return PUBLISH.

## Report back when the subject is finished

Under 250 words: topics completed/blocked; claims, units, items and notes words; check decision and warnings/no-opinion checks; every deviation; plan problems; unresolved standard compatibility issues. Update STATUS.md accurately. Do not label a blocked or partial subject complete.
'''
(WS/f'HANDOVER-{stem}.md').write_text(H)
(WS/'planning/README.md').write_text('''# 6136 Development Studies planning reproducibility

Step 2 and Step 3 are approved. Step 4 is drafted for approval; STATUS.md is the
current workflow record. Older corpus prose describes its own stage at creation.

The Step 3 source-bullet evidence/exposure/misconceptions are preserved unchanged
as source-bullet-*.json here. The rejected submitted plan is frozen under reviewed-plan-v1/ and the original Claude report remains unchanged. The canonical curriculum and assessment evidence now
use the Step 4 registry. verify_corpus.py checks the original snapshots, while
finalise_plan.py independently checks the canonical registry map, every slot,
performance subparts, exact AO arithmetic and all scope/coverage invariants.

Human semantic inputs: registry_decisions.json, member_evidence_decisions.json
and glossary_decisions.json. Current member-level evidence is conservative and
incomplete; zero direct assignments never implies absence from the papers.

Rebuild from repository root, in order:

```bash
python3 work/nam-6136-nssco-2026/planning/build_plan.py
python3 work/nam-6136-nssco-2026/planning/build_exemplar.py
python3 work/nam-6136-nssco-2026/planning/finalise_plan.py
python3 work/nam-6136-nssco-2026/planning/verify_corpus.py
python3 work/nam-6136-nssco-2026/planning/verify_syllabus_facts.py
```

build_plan invokes the unchanged conform_registry, make_contract and
make_work_order tools. Do not run old Step 3 miners alone over the canonical
Step 4 outputs: they produce bridge IDs. Preserve the Step 3 snapshots when
rebuilding. Final teaching prose is designated for Codex; Claude Code reviews the authored resources.

Read plan-validation.json and standard-compatibility.json together. Profile
schema incompatibility is recorded as an error, not filtered into a pass.
Exemplar no-opinion checks and the wrapper exit discrepancy are explicit.
No full-topic or publication gate has been claimed. No source or standard file
was edited, and no commit, push, publishing or platform import was performed.
''')
print(json.dumps({'totals':tot,'exact_ao_percent':exactpct,'largest_gap':gap,'schema_checks':schema_results,
                  'performance_slots':len(spec),'validation':'planning/plan-validation.json'},ensure_ascii=False))
