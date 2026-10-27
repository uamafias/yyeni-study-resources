"""Generate reviewable plan/handover and audit the unchanged shared build outputs."""
import collections
import copy
import hashlib
import json
import re
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
STD=REPO/'standard/v0.2.0-draft'
def read(path):return json.loads(path.read_text())
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
REG=read(WS/'curriculum/objective_registry.json')
INDEX={o['objective_id']:o for o in REG['objectives']}
PROFILE=yaml.safe_load((WS/'subject-profile.yaml').read_text())
FW=read(WS/'curriculum/assessment-framework.json')
WO=[read(p) for p in sorted((WS/'topics').glob('*/work_order.json'),key=lambda p:[int(x) for x in p.parent.name.split('.')])]

# The planner selects the actual decision and outcomes; the author invents the prose/data.
CASES={
'1.1':('Specialisation, trade and stakeholder effects','A producer chooses how far to divide work when demand and variety change.',['07','09','10']),
'1.2':('Small-firm survival and sector/size distinctions','A small specialist enterprise compares a personal-service response with a larger-scale response.',['03','04','06']),
'2.1':('Appropriate ownership and change of form','Owners weigh a suitable ownership form and the consequences of changing it.',['02','03','05']),
'2.2':('Structure, delegation and expansion','An expanding enterprise chooses how to allocate authority and revises its reporting structure.',['02','04','05']),
'2.3':('Finance needs, sources and provider criteria','An enterprise needs equipment and working funds; the finance provider assesses risk and repayment. Keep lender and borrower perspectives explicit.',['01','02','05']),
'2.4':('Financial evidence and judgement','An original financial table supports ratio calculations and interpretation; the selected ratios must answer the stated performance/liquidity/solvency question.',['02','05','07']),
'2.5':('Coordinated management and decision levels','A manager responds to a missed objective by coordinating work and choosing a response appropriate to the managerial level.',['01','02','05']),
'2.6':('Communication and a context-dependent choice','A business changes arrangements for its workers and chooses a suitable communication way while addressing a matching barrier.',['01','03','05']),
'3.1':('How work satisfies individual needs','Management compares the implications of the taught motivation theories for a specified workforce without mixing theorists.',['01','02']),
'3.2':('Rewards and their motivational effects','A workforce faces a choice of payment/reward arrangements; the changed constraint affects which arrangement fits.',['01','02','03']),
'3.3':('Formation and importance of workplace groups','A workplace considers formal and informal groups, their formation and their contribution to work. Judge the group arrangements using only taught formation/importance content, without importing ownership forms or union law.',['01','02']),
'3.4':('Participation, conflict and representation','A workplace chooses a participation arrangement and explains its implications, distinguishing the named mechanisms and the parties affected.',['10','14','15','16']),
'3.5':('Recruitment materials and training suitability','An enterprise designs appropriate recruitment material and chooses training suited to the worker and task.',['01','02','03']),
'4.1':('Customer focus and segmentation','A business identifies customer needs and chooses a segmentation basis suitable for its products and constraints.',['02','04','05']),
'4.2':('Research evidence and a research decision','A business considers primary and secondary information, develops original questions and represents checked response data. Judge the research approach with its information limits explicit.',['01','02','03','04']),
'4.3':('Business-plan components and usefulness','A proposed business needs a coherent plan; compare which component deserves more investigation under the stated constraint without pretending required components can simply be omitted.',['01','02','03']),
'4.4':('Marketing choices in a coherent mix','A business chooses suitable pricing or promotion, using product/customer facts and original figures. Preserve the distinction between promotion type, sales-promotion method and advertising medium.',['09','10','12','17']),
'4.5':('Production method, scale and location','A manufacturer weighs production methods or location options using required variety, volume and resources; changed constraints alter the decision.',['05','06','09','11']),
'5.1':('Descriptive social effects and regulation','A community and business weigh social costs/benefits and environmental protection. The judgement remains descriptive; no discounted or monetised social-cost-benefit calculation.',['03','05','06','08']),
'5.2':('Assistance to producers and trade implications','A producer considers government assistance and regional trading opportunities/risks. Distinguish why assistance is given from how it works; no invented current tariffs.',['02','03','04','06']),
'5.3':('Government protection and its effects','A workplace assesses employee protection and the consequences for the named parties. Use conceptual/hypothetical measures, not unverified current legal rates or procedures.',['01','02','03']),
'5.4':('Consumers, capital providers and protection','An enterprise considers consumer protection and protection of lenders/capital providers, keeping rights, mechanisms and the affected group separate.',['01','02','03']),
}

KNOWLEDGE_FOCUS={
'1.1':('Define','07','specialisation'), '1.2':('Define','03','a primary-sector business'),
'2.1':('Define','02','a private limited company'), '2.2':('Define','02','delegation'),
'2.3':('State','01','two distinct needs for finance in the supplied situation'),
'2.4':('Define','02','unit cost'), '2.5':('Define','01','effective management'),
'2.6':('Define','01','effective communication'), '3.1':('State','01','two distinct reasons why individuals work'),
'3.2':('State','01','two distinct financial or non-financial rewards, as specified'),
'3.3':('Define','01','an informal workplace group'), '3.4':('Define','14','worker participation'),
'3.5':('Define','01','recruitment'), '4.1':('State','02','two ways the business can identify or meet customer needs, as specified'),
'4.2':('Define','01','market research'), '4.3':('Define','01','a business plan'),
'4.4':('Define','09','cost-plus pricing'), '4.5':('Define','05','job production'),
'5.1':('Define','03','social cost'), '5.2':('State','02','two relevant ways government can assist a producer'),
'5.3':('State','01','two relevant employee-protection measures'),
'5.4':('State','01','two mechanisms protecting the specified group of consumers or capital providers'),
}


def blueprint(wo):
    topic=wo['topic_id'];label,situation,nums=CASES[topic]
    ids=[f'OBJ-6144-{topic}.{n}' for n in nums]
    assert all(x in INDEX for x in ids)
    packets=[]
    for task in wo['performance_tasks']:
        kind=task['item_type'];spec=next(t for t in PROFILE['slot_plan']['performance_tasks'] if t['item_type']==kind)
        if kind=='short_answer':
            kcommand,knumber,kfocus=KNOWLEDGE_FOCUS[topic]
            subs=[('a(i)',kcommand,2,{'A':2},f'OBJ-6144-{topic}.{knumber}'),('a(ii)','State',2,{'A':2},ids[-1]),
                  ('b','State',2,{'A':2},ids[0]),('c','Explain',6,{'A':2,'B':2,'C':2},ids[1]),
                  ('d','Evaluate',8,{'A':2,'B':2,'C':2,'D':2},ids[-1])]
            if topic=='2.2':subs[3]=('c','Explain',6,{'A':2,'B':2,'C':2},ids[-1])
            if topic=='2.4':subs[3]=('c','Analyse',6,{'A':2,'B':2,'C':2},ids[1])
            if topic=='4.2':subs[3]=('c','Distinguish',6,{'A':2,'B':2,'C':2},ids[1])
            if topic=='4.4':subs[3]=('c','Calculate',6,{'A':2,'B':2,'C':2},ids[1])
        elif kind=='data_response':
            command='Draw' if topic in ['2.2','4.2'] else 'Explain'
            analytical=ids[-1] if topic=='4.2' else ids[0] if topic=='4.4' else ids[1]
            if topic=='2.4':command='Analyse'
            decision=ids[1] if topic=='2.4' else ids[-1]
            subs=[('a',command,8,{'A':2,'B':2,'C':4},analytical),('b','Evaluate',12,{'A':4,'B':2,'C':2,'D':4},decision)]
        elif kind=='essay_plan':subs=[('a','Evaluate',12,{'A':4,'B':2,'C':2,'D':4},ids[-1])]
        else:subs=[('a','Evaluate',12,{'A':4,'B':2,'C':2,'D':4},ids[-1]),('b','Evaluate',12,{'A':4,'B':2,'C':2,'D':4},ids[-1])]
        packet={'slot':task['slot'],'item_type':kind,'blooms_level':task['blooms_level'],
                'objective_ids':ids,'title':label,'situation':situation,
                'assessment_objectives':list(spec['ao_split']),'ao_split':spec['ao_split'],
                'total_marks':sum(spec['ao_split'].values()),
                'subparts':[{'part':part,'command_word':command,'marks':marks,'ao_split':split,'primary_objective_id':obj,
                             'demand':KNOWLEDGE_FOCUS[topic][2] if part=='a(i)' else 'A second distinct knowledge element from the indicated outcome; avoid repeating a(i).' if part=='a(ii)' else 'Two distinct relevant knowledge elements from the indicated outcome, not copies of earlier subparts.' if part=='b' and kind=='short_answer' else 'Develop the specified in-scope case relationship or construction.' if 'D' not in split else 'Weigh the specified decision or trade-off and give a supported choice; respond to the changed constraint in the second linked case part.'} for part,command,marks,split,obj in subs],
                'allocation_provenance':'Corpus part mark structures; transfer to this in-scope topic/decision is planner judgement, not a claim that this exact task appeared.',
                'demand_rules':['Treat every listed objective as content that the whole package must genuinely exercise; align each subpart to the selected demand, not just its primary ID.','Use original Namibian business facts and N$ values where a number helps.','Use a clear alternative or positive/negative trade-off and justify the choice where D is allocated.','The paired case_analysis changes one decisive stated constraint in part (b); compare why the judgement changes or holds.']}
        if topic in ['2.4','4.2','4.4']:
            packet['data_rule']='Include sufficient original checked data for the requested calculations/construction. Do not infer an unknown datum merely to make an answer possible.'
        assert sum(s['marks'] for s in packet['subparts'])==packet['total_marks']
        packets.append(packet)
    write(WS/'topics'/topic/'performance-blueprints.json',{'topic_id':topic,'packages':packets,'authority':'Supplementary generated plan specifying what the shared generator leaves as choose 2–4 objectives. Read alongside work_order.json; no official source wording may be reproduced.'})
    return packets


def audit():
    errors=[];rows=[];aos=collections.Counter();allslots=[];taskcount=0;miscon=[];blueprints=[]
    words={w['word']:w for w in FW['command_words']}
    for w in WO:
        topic=w['topic_id'];contract=read(WS/'topics'/topic/'contract.json');branch={o['objective_id'] for o in REG['objectives'] if o['topic_id']==topic and o['parent_id']}
        slots=w['item_slots'];allslots+=slots
        covered={s['objective_id'] for s in slots}
        assert covered==branch,(topic,'coverage mismatch',branch-covered)
        for s in slots:
            assert s['command_word'] in words and words[s['command_word']]['use_in_prompts'],s
            assert s['mark_tariff'] in words[s['command_word']]['observed_tariffs'],s
            assert s['blooms_level'] in ['Remember','Understand','Apply','Analyse','Evaluate','Create']
            assert s['assessment_objectives'] and set(s['assessment_objectives'])<=set('ABCD')
            assert s['marking_guidance_must_name'],s
            for ao in s['assessment_objectives']:aos[ao]+=s['mark_tariff']/len(s['assessment_objectives'])
            if s['subtype']=='MISCON':miscon.append(s['misconception_entry'])
        assert len(contract['depth_constraints']['excluded_constructs'])==2
        packages=blueprint(w);blueprints+=packages
        for p in packages:
            aos.update(p['ao_split']);taskcount+=1
            for sub in p['subparts']:
                assert sub['command_word'] in words and sub['marks'] in words[sub['command_word']]['observed_tariffs']
        budget=contract['depth_constraints']['word_budget']
        rows.append({'topic_id':topic,'title':w['topic_title'],'objectives':len(branch),'flashcards':len(slots),
                     'practice_packages':len(packages),'total_items':w['planned_item_count'],'word_min':budget['min'],'word_max':budget['max'],
                     'content_units':len(w['content_units'])})
    entries=read(WS/'curriculum/misconceptions.json')['entries']
    assert set(miscon)=={e['entry_id'] for e in entries} and len(miscon)==len(entries)
    total=sum(aos.values());shares={a:100*aos[a]/total for a in 'ABCD'};targets=FW['ao_mark_budget']['stated_qualification_weight_percent']
    worst=max(abs(shares[a]-targets[a]) for a in 'ABCD')
    assert worst<=5,(shares,worst)
    # Core schemas are checked directly. Runtime profile extensions are reported,
    # never silently removed to claim full schema compatibility.
    schema_checks={}
    for schema_name,path,parser in [('objective_registry',WS/'curriculum/objective_registry.json',read),
                                    ('qualification_profile',WS/'qualification-profile.yaml',lambda p:yaml.safe_load(p.read_text())),
                                    ('subject_profile',WS/'subject-profile.yaml',lambda p:yaml.safe_load(p.read_text())),
                                    ('assessment_evidence',WS/'assessment-evidence/assessment_evidence.json',read)]:
        schema=read(STD/'schemas'/f'{schema_name}.schema.json')
        errs=list(Draft202012Validator(schema).iter_errors(parser(path)))
        schema_checks[schema_name]=[{'path':list(e.path),'message':e.message} for e in errs]
    assert not schema_checks['objective_registry']
    assert not schema_checks['qualification_profile']
    assert not schema_checks['assessment_evidence']
    assert all(e['path']==[] and 'Additional properties' in e['message'] for e in schema_checks['subject_profile'])
    exp=read(WS/'curriculum/exam-exposure.json');recs=read(WS/'assessment-evidence/assessment_evidence.json')['records']
    for x in exp['objectives']:
        rr=[r for r in recs if x['objective_id'] in r['objective_ids']]
        assert x['evidence']['question_parts_naming_it']==x['times_examined']==len(rr)
        assert x['marks_examined']==sum(r['mark_tariff'] for r in rr)
        assert x['evidence']['max_mark_tariff']==max((r['mark_tariff'] for r in rr),default=0)
    source_rows=read(WS/'curriculum/objective-provenance.json')['sources']
    assert {o['objective_id'] for o in REG['objectives'] if o['parent_id']}=={x['objective_id'] for x in source_rows}
    assert len([x for x in source_rows if x['kind']=='syllabus bullet'])==146
    glossary=read(WS/'curriculum/glossary.json')
    assert all(len(x['term'])<45 for x in glossary['entries'])
    summary={'status':'pass with recorded shared-schema limitation','topics':len(rows),'topic_roots':22,
             'syllabus_bullets':146,'named_member_targets':234,'annex_additional_ratios':3,
             'assessable_objectives':sum(r['objectives'] for r in rows),'flashcards':len(allslots),'practice_packages':taskcount,
             'practice_subparts':sum(len(p['subparts']) for p in blueprints),
             'total_items':len(allslots)+taskcount,'content_units':sum(r['content_units'] for r in rows),
             'word_budget':{'min':sum(r['word_min'] for r in rows),'max':sum(r['word_max'] for r in rows)},
             'misconception_slots':len(miscon),'glossary_terms':len(glossary['entries']),
             'exact_ao_marks_equivalent':dict(aos),'exact_ao_share_percent':shares,'target_ao_share_percent':targets,
             'largest_exact_gap_percentage_points':worst,'schema_checks':schema_checks,
             'schema_limit':'Shared subject_profile schema predates runtime slot_plan, depictions and conditioned_mechanisms fields used by the shared build/check tools. Full subject-profile validation reports those extensions; no standard/schema file was edited. C-00 does not validate the profile. Core profile fields and all other named artifacts validate.',
             'rows':rows,'approval':'Vitalis plan approval pending. No production topic is authored.'}
    write(WS/'planning/plan-validation.json',summary)
    write(WS/'curriculum/dependency_graph.json',{'nodes':[o['objective_id'] for o in REG['objectives']],
                                               'edges':[{'from':pr,'to':o['objective_id'],'kind':'prerequisite'} for o in REG['objectives'] for pr in o['prerequisite_ids']],
                                               'note':'Declared member/container prerequisites; content units integrate related targets rather than repeat their explanations.'})
    return summary,rows,shares


def documents(summary,rows,shares):
    scope=read(WS/'curriculum/scope-scan.json');mis=read(WS/'curriculum/misconceptions.json')['entries']
    lines=['# Plan — NSSCO Business Studies 6144','',
           'Generated 27 October 2026 from the subject’s own syllabus facts, accepted corpus analysis, explicit planner decisions and shared-generator work orders. Owner: Vitalis. Status: proposed; plan approval pending.','',
           '## 0. What the syllabus says','',
           'The source is the NIED 2019 syllabus, filename June 2020 final. Both papers are 100 marks, 135 minutes and 50% of the qualification; five compulsory 20-mark questions per paper. PDF pp.23–24 / printed pp.19–20 state A Knowledge with understanding 40%, B Application 20%, C Analysis 25%, D Evaluation 15%. Paper 1’s grid is 50/20/20/10; Paper 2’s 30/20/30/20. Its AO grid indicates relative importance, not a guarantee of an exact split in every future paper.','',
           'All 146 original specific-objective bullets remain, with 234 named member targets and three additional ratios explicitly listed in Annexe A. The 22 topic roots are organisational nodes and do not count as assessable targets. No other qualification’s content or exclusions have been inherited.','',
           '## 1. What the corpus says','',
           'The accepted analysis is operations/analysis/6144-nssco-business-studies-corpus-analysis.md: ten papers, five annual report sections, 176 parts and 1,000 marks. Marking guidance in examiner reports supports the repeated answer shapes. One employer/employee question remains unresolved. Missing standalone mark schemes, 2025 material, grade thresholds and proof-version provenance remain explicit limitations.','',
           'The complete accepted Step 3 JSON files are preserved under assessment-evidence/step3-accepted/. The canonical planner evidence is a schema-shaped projection of 175 mapped records; the unresolved part is retained separately, not invented away. Parent evidence does not give every named child a frequency: only explicit semantic member links carry direct exposure.','',
           '## 2. Command words and tariffs','',
           'Use only live commands and observed tariffs in curriculum/assessment-framework.json. Every generated slot is audited against that table. Definitions use Define 2; knowledge features State 2; comparisons Distinguish 6; causal/application work Explain 6; interpretation Analyse 8; calculation Calculate 6; evaluative cards Evaluate 8. Extended performance decisions use Evaluate 12. Chart construction uses Draw 8, while the product-life-cycle construction uses Draw 6. Document-design tasks use the observed Explain 8 frame with explicit drafting output and Bloom Create; transfer of the demand to an unobserved outcome is labelled planning judgement.','',
           'Justify and Consider are observed secondary instructions but not permitted standalone openers here. Avoid the generator’s default assumption that an 8-mark task necessarily needs evaluation: Paper 2’s 8 marks are analytical.','',
           '## 3. Answer shapes','',
           'Every item’s marking guidance names the parts in subject-profile.yaml. Short knowledge is precise; six-mark applied explanation has two relevant points with distinct application and consequences. Eight-mark Paper 1 evaluation adds a supported choice. Eight-mark Paper 2 analysis develops the reasoning further without an invented evaluation allocation. Twelve-mark judgement weighs the actual alternatives/conditions and supports the decision. Numerical answers include formula, substitution, result/format and meaning.','',
           'Each topic has four practice packages: a Paper 1 20-mark question; a Paper 2 8+12 pair; a 12-mark decision plan; and two linked 12-mark case decisions with one changed constraint. The latter teaches whether and why a conclusion survives a changed situation. This supplies extended evaluation practice without multiplying definition or evaluation flashcards. Each performance-blueprints.json specifies its objectives, subparts, command words, tariffs, AO splits, case focus and boundaries; it supersedes the generic choose-2–4 placeholder in the shared work order.','',
           '## 4. Card types, assessment objectives and Bloom levels','',
           '| Subtype | AO labels | Bloom | Meaning |','|---|---|---|---|']
    meaning={'DEF':'Precise meaning','FEATURE':'Requested knowledge elements','DIST':'A meaningful comparison','APP':'In-scope business application or construction','CHAIN':'Point, mechanism and effect','EVAL':'A supported decision','PROC':'An ordered procedure or construction','CALC':'A completed calculation','INTERP':'Interpretation of supplied data','MISCON':'Discriminate a real confusion','SYNTH':'Create an original in-scope document'}
    for m in FW['flashcard_subtype_ao_map']:lines.append(f"| {m['subtype']} | {'/'.join(m['assessment_objectives'])} | {m['blooms_level']} | {meaning[m['subtype']]} |")
    lines+=['','AO and Bloom are separate axes. Knowledge points may underpin an analytical task; do not relabel its cognitive demand as recall merely because A earns some marks.','',
            '## 5. The topics','', '| Topic | Teaching targets | Flashcards | Practice packages | Items | Notes allocation |', '|---|---:|---:|---:|---:|---:|']
    for r in rows:lines.append(f"| {r['topic_id']} {r['title']} | {r['objectives']} | {r['flashcards']} | {r['practice_packages']} | {r['total_items']} | {r['word_min']:,}–{r['word_max']:,} |")
    lines+=['',f"**{summary['topics']} topics; {summary['assessable_objectives']} teaching targets; {summary['flashcards']} flashcards; {summary['practice_packages']} practice packages ({summary['practice_subparts']} subparts); {summary['total_items']} total items; {summary['word_budget']['min']:,}–{summary['word_budget']['max']:,} allocated notes words.**",'',
            'Word ranges are generated allocations, not permission to pad prose. The notes must teach every target in depth, integrating member/container explanations and avoiding repetition. Advisory lower-bound warnings remain visible if a shorter explanation fully teaches the material; upper bounds remain ceilings. This is a complete-subject plan, not merely a predicted-topic revision pack.','',
            '## 6. AO balance, in marks','', '| AO | Exact planned share | Syllabus | Gap |','|---|---:|---:|---:|']
    for a in 'ABCD':lines.append(f"| {a} | {shares[a]:.2f}% | {summary['target_ao_share_percent'][a]}% | {shares[a]-summary['target_ao_share_percent'][a]:+.2f} |")
    lines+=['',f"Largest exact gap: **{summary['largest_exact_gap_percentage_points']:.2f} percentage points**, within the five-point planning tolerance. The shared roll-up reports rounded whole-topic estimates; planning/plan-validation.json recomputes exact unrounded totals.",'',
            'This is the generator’s marks-equivalent estimate: flashcard tariff is split equally across declared AOs, whereas performance tasks use the exact source-backed split. It estimates balance, not independent proof of semantic alignment. Topic shares need not equal qualification shares. Recall anchors, real analytical demand and extended judgement remain the substantive tests.','',
            '## 7. Misconceptions, glossary and scope','',
            f"{len(mis)} curated confusions each have exactly one MISCON slot with its named register entry; linked objectives remain visible without duplicate cards. The glossary transcribes {summary['glossary_terms']} syllabus terms and flags source simplifications. Two tested scope patterns travel into every contract; all other simple/brief/general depth limits are preserved as semantic obligations. Basic liability, marginal cost, the named ratios and exchange-rate conversion remain in scope.",'',
            'Detailed registration procedures and quantitative social-cost-benefit appraisal are excluded. Source issue handling includes inconsistent employer/employee wording, time-rate phrasing, liquidity year labels, ratio truncation and conflicting theory text. No contextual rejection in one report becomes a universal business fact.','',
            '## 8. Rules particular to this subject','',
            '- Use invented Namibian businesses, N$ and British English. Official assessment sources are internal mining evidence; no question/model-answer wording reaches learners.',
            '- Introduce terms before use. Retain distinct meanings for profit/cash, capital senses, unit/marginal cost, production/productivity and the named protected parties.',
            '- Ratios use Annexe A’s formulas and two-decimal convention. Distinguish percentages from x:1 ratios. Show full working; avoid rounded equalities that are mathematically false.',
            '- Recruitment document, questionnaire, marketing-plan and chart targets require genuine outputs. A definition alone does not satisfy a creation/construction objective.',
            '- Charts must be generated from original data by reproducible subject-local code. The shared chart model is break-even only and does not verify organisation charts, product life cycles or survey/time-series charts. Preserve C35/C41 not_run and add direct data/render checks; do not invent break-even metadata to silence them.',
            '- Claim source locators and revision stamps are required. An unverified exemplar claim is not independent truth approval. Never invent current legal rules, statutory lists or rates.',
            '- Author all topics sequentially in Codex after approval. Run the unchanged checks and fix real failures. Stop after three repeated failures on one issue and report the cause; do not edit the standard.',
            '- Qualitative and quantitative reduced-scope exemplars both have zero failed shared checks. They retain AO/word-budget warnings where applicable and three inapplicable checks. The runner exits 1 even on PUBLISH because it compares the decision with pass; inspect the persisted decision and failure list. They are structural examples, not full production topics or semantic release approval.',
            '- Shared-schema limitation: the subject-profile JSON schema predates slot_plan, depictions and conditioned_mechanisms used by the runtime. Independent validation reports these extra fields; C-00 validates the registry/content/items, not this profile. Core profile fields and other named artifacts validate. No standard file was changed.',
            '', 'Plan approval checkpoint: Vitalis reviews the topic and AO tables before production authoring. The tracker claim/plan commit and push remain human steps; no remote publication is asserted.','']
    stem='6144-nssco-business-studies'
    (WS/f'PLAN-{stem}.md').write_text('\n'.join(lines))
    handover=f'''# Handover prompt — NSSCO Business Studies 6144

## Start here

Work only in work/nam-6144-nssco-2026/. Read TEAM-PLAYBOOK.md, the Author role brief when authoring begins, STATUS.md, PLAN-{stem}.md and the reduced-scope exemplars. Owner: Vitalis. Start only when the plan approval checkpoint is explicitly recorded. Plan/claim commit and push remain human steps.

## The job

Author the whole subject, 22 topics in numerical order, sequentially in Codex. Every topic reads its generated contract and work order plus performance-blueprints.json. Write claims, content units and learning items, then use the shared notes renderer. Notes are full standalone teaching, not card-answer dumps. The plan totals are {summary['flashcards']} flashcards and {summary['practice_packages']} practice packages; author each slot once.

## Every item carries its labels

Carry item ID, objective IDs, subtype/item type, AOs, Bloom level, command word and tariff. For performance items, the supplementary blueprint supplies exact objectives, task subparts and AO split that the shared work-order placeholder omits. For case_analysis the package is 24 marks: two 12-mark judgements after a changed constraint. Do not collapse them into one 12-mark task or present 24 as an observed single-part tariff.

## Rules that come from the syllabus and the corpus

Define/State short knowledge, Explain 6, Distinguish 6, Analyse 8, Evaluate 8 cards and Evaluate 12 extended decisions, Calculate 6, Draw 8 construction and Draw 6 product life cycle as specified by the slot. Both papers draw on the subject. Paper 1’s 8 marks and Paper 2’s 8 marks have different AO patterns. Never infer evaluation from tariff alone. No official question or answer wording; invent all scenarios and data.

## Voice

British English, Namibian places and invented businesses, N$, clear teaching. Explain a term before using it. Keep examples original and relevant. No learner-facing claims about examiner behaviour, question frequency, tooling or publication gates.

## The work order is a baseline, not a cage

Every generated slot is required. Do not redesign it or change labels to get an easy pass. If a slot cannot genuinely serve its objective, report the plan problem. The blueprint resolves the generic performance objective placeholder. Teach a full member list through integrated notes and individual targets; do not make one flashcard list an entire long syllabus family for two marks. Word minima are advisory; never pad or overwrite teaching with a trimmed card answer.

## Finishing each topic

Use revision 1 on initial claims and claims_seen/authored_hash stamps on derivatives. Run render_notes.py, run_checks.py and what_to_fix.py on that topic. Read the saved decision and every failed/warn/not_run result; the CLI has a known exit-code bug on PUBLISH. Fix real failures; do not edit standard/. If the same check fails after three attempts, record the issue and move to an independent topic. Preserve numerical, diagram and copied-wording checks. Full-subject Claude review remains a separate later stage explicitly started by Vitalis.

## Boundaries

Only this subject’s workspace, named analysis files and its publication folder. No Git add/commit/push or platform import. No other subject writes. No source acquisition or source-folder writes. Source issues and legal uncertainty remain explicit; no factual claim becomes verified merely because deterministic checks pass. The shared subject-profile schema/runtime extension discrepancy is reported in planning/plan-validation.json and no standard file has been changed.

## Report back when the subject is finished

In under 250 words: topics completed/blocked, counts of claims/units/items/notes words, per-topic saved decisions, deviations and retained warnings/not_run results. Publication packaging, independent review, Git push, platform import and learner assignment are distinct states. Do not infer one from another.
'''
    (WS/f'HANDOVER-{stem}.md').write_text(handover)
    (WS/'exemplar/README.md').write_text('''# Structural exemplars — NSSCO Business Studies 6144

Generated by planning/build_exemplars_6144.py. Read REDUCED-SCOPE.json in each scratch workspace. These do not replace the production contracts.

- qualitative/nam-6144-nssco-2026/: two topic 2.5 targets, two content units and two cards.
- quantitative/nam-6144-nssco-2026/: one cost-plus target, one content unit and one six-mark calculation card.

Both saved decisions are PUBLISH with zero failed checks. Warnings and three inapplicable checks remain explicit in VALIDATION.json. Neither is a full production topic or independently approved subject content. The standard runner’s exit 1 on PUBLISH is retained, not relabelled success.
''')


if __name__=='__main__':
    summary,rows,shares=audit();documents(summary,rows,shares)
    print(json.dumps({k:v for k,v in summary.items() if k not in ['rows','schema_checks']},indent=2))
