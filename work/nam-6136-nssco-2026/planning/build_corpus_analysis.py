"""Compile explicit semantic mappings and curated evidence into Step 3 artefacts."""
import json,re
from pathlib import Path
from collections import Counter,defaultdict

WS=Path(__file__).resolve().parents[1];REPO=WS.parents[1];EV=WS/'assessment-evidence';CUR=WS/'curriculum'
def read(p):return json.loads(p.read_text())
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
records=read(EV/'question-parts-draft.json');sources=read(EV/'source-manifest.json');facts=read(CUR/'syllabus-facts.json')
maps=read(WS/'planning/semantic_mappings.json');curated=read(WS/'planning/curated_findings.json')
bullets={f'{t["id"]}:{i}':o for t in facts['content_outline'] for i,o in enumerate(t['specific_objectives'],1)}
titles={t['id']:t['title'] for t in facts['content_outline']}
def objective_id(key):
 t,b=key.split(':');return f'SB-6136-{t}-{int(b):02d}'
def decode(value):
 keys=value.split('+');assert all(k in bullets for k in keys),value
 return keys
for sid,tokens in maps.items():
 if sid.startswith('_'):continue
 rs=[r for r in records if r['source_id']==sid];tokens=tokens.split();assert len(rs)==len(tokens)
 for r,token in zip(rs,tokens):
  # Survey location is data extraction, not formulation of a study aim.
  if r['paper_id']=='P3' and r['question_ref']=='1(a)(i)':token='10.1:11'
  if r['evidence_id']=='6136-2023-P2-2(b)(ii)':token='9.1:4'
  keys=decode(token);r['syllabus_bullet_ids']=[bullets[k]['source_bullet_id'] for k in keys]
  r['objective_ids']=[objective_id(k) for k in keys];r['primary_topic_id']=keys[0].split(':')[0]
  r['secondary_topic_ids']=list(dict.fromkeys(k.split(':')[0] for k in keys[1:] if k.split(':')[0]!=r['primary_topic_id']))
  r['mapping_method']='human semantic mapping after reading question and syllabus; explicit assignment, no keyword similarity'
  r['mapping_note']='Source-bullet IDs are a Step 3 bridge, not the later decomposed objective registry. Primary topic owns marks once for topic shares; linked objectives may overlap.'
  r['context_type']='own_investigation' if r['paper_id']=='P3' and r['question_ref'].startswith('3') else 'supplied_stimulus_or_subject_context'
  r['creditworthy_points']=[];r['examiner_findings']=[];r['common_errors']=[];r['strong_response_features']=[];r['notes']=[]
byid={r['evidence_id']:r for r in records};assert len(byid)==419

# Shared parent directions that do not appear again in the child question.
overrides={
 '6136-2021-P1-2(b)(i)':'Explain','6136-2021-P1-2(b)(ii)':'Explain',
 '6136-2021-P1-4(a)(i)':'Define','6136-2021-P1-4(a)(ii)':'Define',
 **{f'6136-2024-P3-2({c})':'Describe' for c in 'abcd'}}
verbs=['Define','State','Describe','Explain','Suggest','Identify','Calculate','Compare','Differentiate','Name','Give','Discuss','Design','Draw','Outline','Indicate','Determine','Write','Choose','Mention','Use','List']
rx=re.compile(r'\b('+ '|'.join(verbs)+r')\b',re.I)
def command(r):
 s=r['stem_internal'];eid=r['evidence_id']
 if eid in overrides:return overrides[eid],'shared parent instruction'
 definition=re.search(r'\bwhat is meant by\b',s,re.I)
 directive=rx.search(s)
 interrog=None
 for candidate in re.finditer(r'\b(In which|As what|By how much|What|Which|Where|Who|How|Are|Is)\b',s,re.I):
  if candidate[1].lower() in ['is','are'] and candidate.start()>0:continue
  # Lower-case relative clauses (people who live...) are not question openings.
  if candidate[1].islower() and candidate.start()>0 and not re.match(r'Using|According|From|If\b',s,re.I):continue
  interrog=candidate;break
 if definition and (not directive or definition.start()<directive.start()):return 'Define','syllabus synonym: What is meant by'
 if interrog and (not directive or interrog.start()<directive.start()):return interrog[1][0].upper()+interrog[1][1:].lower(),'literal interrogative form'
 if directive:
  label=next(w for w in verbs if w.lower()==directive[1].lower())
  compound=re.match(r'(Name and explain|Name and describe|Describe and evaluate)',s[directive.start():],re.I)
  return (compound[1][0].upper()+compound[1][1:].lower() if compound else label),'first operative directive after context/source prefix'
 return 'unresolved','no counted command inferred'
for r in records:
 cw,basis=command(r);r['command_word']=cw;r['command_extraction_note']=basis
 # Per-item AO focus is judgement, never inferred just from which paper it is on.
 s=r['stem_internal'].lower()
 if cw=='Design':ao=['C.1'];level=6
 elif cw=='Draw':ao=['C.3'];level=3
 elif r['paper_id']=='P3':
  if '10.1-bullet-12' in r['syllabus_bullet_ids']:
   ao=['B.2'] if 'conclu' in s or 'finding' in s or 'report' in s else ['D.1'];level=4 if ao==['B.2'] else 3
  elif cw in ['Calculate','By how much'] or (re.search(r'percentage|least|highest|where|which country|which part|which.*region|which sector',s) and not r['question_ref'].startswith('3')):ao=['B.1'];level=3
  elif '10.1-bullet-11' in r['syllabus_bullet_ids']:ao=['C.3'];level=2
  else:ao=['C.1' if 'sample' in s or 'aim' in s or 'hypothesis' in s or 'topic' in s else 'C.2'];level=3 if re.search(r'used|your|how|suitable|why',s) else 2
 elif cw=='Define':ao=['A.2'];level=1
 elif re.search(r'justify|evaluate',s):ao=['B.2'];level=4
 elif cw in ['Calculate','By how much'] or re.search(r'fig\.|figs\.|photograph|pyramid|use statistics|using data|using evidence',s):ao=['B.1'];level=3
 elif cw in ['Explain','Discuss','How','Describe and evaluate']:ao=['A.3'];level=2
 else:ao=['A.1'];level=1 if cw in ['Name','State','Identify','Give','Mention','Who','Which'] else 2
 r['ao_focus']=ao;r['blooms_level_judgement']=level
 r['ao_focus_provenance']='judgement of required task; not an official item-level AO allocation'
 r['marking_basis']='question paper tariff; exact credit allocation unresolved except where report-backed shape is attached'
ao_overrides={
 '6136-2023-P1-4(e)':(['B.3'],5,'Evaluate two alternative education approaches, not just recall their names.'),
 '6136-2023-P2-2(c)(iii)':(['B.3'],5,'Choose suitable aid for three specified situations and justify choices.'),
 '6136-2024-P3-1(b)(ii)':(['C.2','B.3'],5,'Select a collection method and justify its suitability for the survey.'),
 '6136-2020-P3-1(c)(iii)':(['C.1','B.3'],5,'Choose an alternative sampling approach and justify it.')}
for eid,(ao,level,why) in ao_overrides.items():
 r=byid[eid];r['ao_focus']=ao;r['blooms_level_judgement']=level;r['notes'].append('Semantic demand judgement: '+why)

# Index report associations. Preserve original labels and record explicit source-number repairs.
comments=read(EV/'report-comments-index.json');unmatched=[]
for c in comments:
 ref=c['question_ref_candidate'];resolved=ref;association_note=None
 if c['year']==2024 and c['paper_id']=='P1' and ref and ref.startswith('4(c)'):
  resolved=ref.replace('4(c)','4(d)',1);association_note='Report uses (c); the corresponding paper labels this debt subpart (d).'
 if c['year']==2021 and c['paper_id']=='P2' and c['finding_id'].endswith(tuple(f'F{i:04d}' for i in range(146,151))):
  roman={'0146':'i','0147':'i','0148':'ii','0149':'iii','0150':'iv'}[c['finding_id'][-4:]]
  resolved=f'1(d)({roman})';association_note='Report prints a malformed (d (i) heading; following health-method subparts belong to paper 1(d), not the preceding 1(c).'
 eid=f'6136-{c["year"]}-{c["paper_id"]}-{resolved}'
 if eid not in byid and resolved and re.search(r'\([ivx]+\)$',resolved):
  shorter=re.sub(r'\([ivx]+\)$','',resolved)
  candidate=f'6136-{c["year"]}-{c["paper_id"]}-{shorter}'
  if candidate in byid:eid=candidate;resolved=shorter;association_note='Report adds a roman label absent from the corresponding un-split paper part.'
 c['question_ref_resolved']=resolved;c['association_note']=association_note
 if eid in byid:
  c['evidence_id']=eid;c['objective_ids']=byid[eid]['objective_ids']
  byid[eid]['examiner_findings'].append(c['finding_id'])
 else:
  c['evidence_id']=None;c['objective_ids']=[];unmatched.append(c['finding_id'])
 c['classification_status']='indexed commentary; conceptual entries are curated separately; no unique-error frequency inferred from overlapping comments'
dump(EV/'report-comments-index.json',comments)

mis=[]
for n,(a,b,key,year,paper,ref,page,test) in enumerate(curated['misconceptions'],1):
 keys=decode(key);eid=f'6136-{year}-{paper}-{ref}';sid=f'6136-{year}-ER'
 src=next(s for s in sources if s['source_id']==sid)
 obj={'misconception_id':f'MISCON-6136-{n:03d}','a':a,'b':b,'n':1,'series':[str(year)],'kind':'adjacent_concept',
  'objective_id':objective_id(keys[0]),'objective_ids':[objective_id(k) for k in keys],
  'topic_id':keys[0].split(':')[0],'objective_text':bullets[keys[0]]['text'],'discrimination_test':test,
  'source_locator':{'path':src['path'],'printed_page':page,'pdf_page':page+2,'paper_id':paper,'question_ref':ref},
  'evidence_id':eid,'provenance':'examiner-evidenced conceptual confusion; paraphrased human curation',
  'n_note':'One curated source occurrence is cited; n is not a claim to exhaustive recurrence counts.'}
 mis.append(obj)
 if eid in byid:byid[eid]['common_errors'].append({'type':'misconception','misconception_id':obj['misconception_id'],'summary':f'Confuses {a} with {b}.'})
dump(CUR/'misconceptions.json',{'register_id':'MISCON-NAM-6136-NSSCO-2026','authority':'6136 examiner reports, 2020–2024',
 'derivation_policy':'mine_do_not_reproduce; conceptual pairs restated independently',
 'how_to_use':'Each card must discriminate the two ideas in a new scenario, not merely repeat a definition. General answering habits are excluded.',
 'entries':mis})

shapes=[]
for shape in curated['answer_shapes']:
 y,paper,ref,page=shape['evidence'];eid=f'6136-{y}-{paper}-{ref}';assert eid in byid,eid
 rr=byid[eid];src=next(s for s in sources if s['source_id']==f'6136-{y}-ER')
 item={**shape,'command':rr['command_word'],'marks':rr['mark_tariff'],'observed_examples_cited':1,'evidence_ids':[eid],
  'source_locator':{'path':src['path'],'printed_page':page,'pdf_page':page+2},
  'provenance':'paraphrased examiner-report guidance; no standalone mark scheme available',
  'applies_to':'this cited item/demand shape; not an automatic rubric for every item with the same command and tariff'}
 shapes.append(item);rr['strong_response_features']=item['shape'];rr['creditworthy_points']=item['shape']
 rr['marking_basis']='report-backed architecture (not copied credit-point wording); see answer-shapes '+shape['id']
 rr['answer_shape_id']=shape['id']
dump(CUR/'answer-shapes.json',{'_provenance':{'source':'6136 question papers and examiner reports, 2020–2024','standalone_mark_schemes':0,
 'limit':'These are documented examples, not universal command/tariff marking rules. Some report rubrics are ambiguous or level-based.'},
 '6136':{'subject':'NSSCO Development Studies','shapes':shapes}})

# Count commands and topic marks from the evidence, never type headline statistics.
cw=[]
glossary_words=[c['word'] for c in facts['command_words']]
glossary_aliases={'Define':['Define or state the meaning of or what is meant by'],
 'Explain':['Explain or Account for/'],'Design':['Devise or plan'],
 'Name and explain':['Name','Explain or Account for/'],'Name and describe':['Name','Describe']}
for word in sorted({r['command_word'] for r in records}):
 rs=[r for r in records if r['command_word']==word];tariffs=Counter(r['mark_tariff'] for r in rs)
 # Design is semantically near Devise, but remains observed-not-listed literally.
 listed=word in glossary_words or word in ['Define','Explain']
 cw.append({'word':word,'count':len(rs),'mark_total':sum(r['mark_tariff'] for r in rs),
  'tariffs_seen':dict(sorted(tariffs.items())),'modal_tariffs':[t for t,n in sorted(tariffs.items()) if n==max(tariffs.values())],
  'papers':dict(Counter(r['paper_id'] for r in rs)),'in_syllabus_table':listed,
  'related_glossary_entries':glossary_aliases.get(word,[]),'use_in_prompts':word!='unresolved',
  'verdict':'observed_listed' if listed else 'observed_not_listed','evidence_ids':[r['evidence_id'] for r in rs]})
unobserved=[]
for label in glossary_words:
 # Compare first operative commands only, not incidental later words or teacher directions.
 aliases=[label]
 if label.startswith('Define or'):aliases=['Define']
 elif label.startswith('Explain or'):aliases=['Explain']
 elif label=='Devise or plan':aliases=['Devise','Plan']
 elif label=='Insert or label':aliases=['Insert','Label']
 elif label=='Use or using the information provided':aliases=['Use']
 if not any(c['word'] in aliases for c in cw):unobserved.append(label)
dump(EV/'command-word-counts.json',{'method':'one primary operative command per assessed part; Define includes the printed what-is-meant-by synonym; compounds kept; shared parent instructions manually recovered',
 'note':'Secondary commands are retained in internal stems but are not double-counted as question parts. This is an observed-form inventory, not the Step 4 framework.',
 'parts':len(records),'commands':cw,'listed_entries_not_observed_as_primary_commands':unobserved})

exposures=[]
for key,o in bullets.items():
 oid=objective_id(key);rs=[r for r in records if oid in r['objective_ids']];years=sorted({r['year'] for r in rs})
 tariffs=Counter(r['mark_tariff'] for r in rs)
 exposures.append({'objective_id':oid,'source_bullet_id':o['source_bullet_id'],'topic_id':key.split(':')[0],
 'syllabus_text':o['text'],'times_examined':len(rs),'marks_examined_overlap':sum(r['mark_tariff'] for r in rs),
 'distinct_years':len(years),'series_spread':len(years),'series':[str(y) for y in years],
 'maximum_tariff':max(tariffs) if tariffs else None,'tariffs':dict(sorted(tariffs.items())),
 'command_words':dict(Counter(r['command_word'] for r in rs)),'evidence_ids':[r['evidence_id'] for r in rs],
 'exposure_class':'frequent' if len(years)>=4 else 'occasional' if len(years)>=2 else 'rare' if years else 'unseen'})
topicstats=[]
for tid,title in titles.items():
 rs=[r for r in records if r['primary_topic_id']==tid]
 topicstats.append({'topic_id':tid,'title':title,'parts':len(rs),'marks':sum(r['mark_tariff'] for r in rs),
  'share_percent':sum(r['mark_tariff'] for r in rs)/10,'years':sorted({r['year'] for r in rs}),
  'marks_by_paper':{p:sum(r['mark_tariff'] for r in rs if r['paper_id']==p) for p in ['P1','P2','P3']}})
assert sum(t['marks'] for t in topicstats)==1000
dump(CUR/'exam-exposure.json',{'exposure_id':'EXPOSURE-NAM-6136-NSSCO-2026','authority':'6136 syllabus source bullets and 15 question papers, 2020–2024',
 'status':'measured_with_human_semantic_mapping','method':maps['_method'],
 'objective_id_status':'Stable source-bullet bridge IDs (SB-6136…), not a decomposed Step 4 objective registry. Recompute/bridge rather than treating 102 source bullets as unique assessable objectives.',
 'principle':'Frequency calibrates emphasis; all syllabus content remains required.',
 'class_definitions':{'frequent':'examined in 4–5 distinct years','occasional':'2–3 years','rare':'1 year','unseen':'0 years'},
 'counting_limits':'Linked objective marks overlap and cannot be summed. Topic shares assign each part once to its primary semantic topic; mixed parts are not fractionally allocated. Research skills owns P3 demand; content contexts are secondary links.',
 'question_parts':len(records),'marks':1000,'objectives':exposures,'topics':topicstats})
dump(EV/'assessment_evidence.json',{'evidence_id':'CORPUS-NAM-6136-2020-2024','derivation_policy':'Internal evidence only; question wording must never be rendered in learner resources.',
 'records':records})
dump(EV/'association-gaps.json',{'report_comments_indexed':len(comments),'not_joined_to_single_paper_part':unmatched,
 'note':'Includes general comments, teacher advice, grouped comments and unresolved report numbering; not every unjoined record is missing subject evidence.'})
print('Question parts:',len(records),'marks:',sum(r['mark_tariff'] for r in records))
print('Commands:',[(c['word'],c['count'],c['modal_tariffs']) for c in sorted(cw,key=lambda x:-x['count'])])
print('Topic shares:',[(t['topic_id'],t['marks']) for t in topicstats])
print('Report comments',len(comments),'joined',len(comments)-len(unmatched),'misconceptions',len(mis),'shapes',len(shapes))

scope=[]
limit_patterns=[
 (0,'assuming prior Development Studies study',r'\b(?:must|need to) have (?:already )?studied Development Studies (?:at|in) (?:Junior Secondary|JS)\b',
  ['You must have studied Development Studies in Junior Secondary.'],['No prior Development Studies study is assumed.']),
 (1,'claiming the investigation is formally assessed coursework',r'\b(?:research investigation|investigation report) (?:is|will be) (?:formally )?assessed as (?:a )?(?:formal )?coursework(?: assignment)?\b',
  ['The research investigation is assessed as formal coursework.'],['Paper 3 asks questions about the investigation; it is not assessed as a formal coursework assignment.']),
 (2,'recommending separate descriptions in place of a comparison',r'\b(?:comparison|compare)\b.{0,50}\b(?:just|only) describe [AB] (?:and|then) [AB] separately\b',
  ['For a comparison, just describe A then B separately.'],['Compare the two places directly using paired statements.'])]
for index,construct,pattern,catch,allow in limit_patterns:
 limit=facts['limits'][index]
 scope.append({'construct':construct,'pattern':pattern,'applies_to':'subject','controls':{'must_catch':catch,'must_allow':allow},
  'source':limit['source'],'syllabus_sentence':limit['verbatim'],'provenance':{'sentence':'syllabus','pattern':'judgement'},
  'note':'Instruction/assessment safeguard; this does not exclude any of the ten content themes.'})
dump(CUR/'scope-scan.json',{'scope_scan_id':'SCOPE-SCAN-NAM-6136','rule':'Carry the three stated preparation/assessment/answer constraints into planning; no topic exclusion is invented.',
 'entries':scope,'explicit_topic_exclusions':[],'report_scope_advice':[{'source':'2023 P3 examiner report printed p.168 / PDF p.170',
 'note':'The report advises against line graphs in presentation teaching. The syllabus does not state a blanket exclusion. Prioritise observed suitable categorical chart tasks; preserve this as report advice pending teacher judgement, not a syllabus prohibition.'}],
 'pattern_limit':'Regexes catch specific wording risks, not all conceptual violations. Contextual reading remains necessary.'})

gaps=f'''# 6136 Development Studies — corpus gaps and limits

- Accepted sources: 15 question papers and five annual examiner reports, 2020–2024. No standalone mark schemes or 2025 papers/reports are present locally. 2021–2023 papers are proof versions, including First Revised Proofs for 2023 Papers 1/2. No evidence is claimed from absent documents.
- All 419 assessed parts reconcile to the 1,000 available marks. Raw and layout extractions retain the same ordered assessed tariffs; source subtotals are not double-counted.
- All parts have an explicit semantic mapping to approved syllabus **source bullets**, using SB-6136 bridge IDs. The 102 bullets include a duplicated enterprise continuation. They are not a decomposed objective registry; Step 4 must bridge/decompose them and recompute exposure.
- Topic shares assign each whole part once to its primary semantic demand. A mixed part can cover linked objectives; its individual concepts have not been assigned guessed fractional marks. Paper 3 is counted primarily as Research skills, with contextual links retained. Counts of linked objective marks overlap.
- The report index contains {len(comments)} extracted comments, including simple performance judgements, general advice and some overlapping fragments. These are **not** {len(comments)} unique misconceptions. {len(comments)-len(unmatched)} comments join to a paper part; {len(unmatched)} general/grouped/unresolved comments remain visible in association-gaps.json. Curated claims below do not depend on treating this raw count as exhaustive error frequency.
- Thirty conceptual confusions and fifteen answer-architecture exemplars were curated separately with precise report pages and paper references. Exact credit structures remain unresolved for parts without report-backed evidence. Do not invent one-point-per-mark rules.
- Report source defects are retained: 2020 P1 Q3(b)(i) is a one-mark definition in the paper but the report prints [4]; 2021 P2 has a malformed health-group heading; 2024 P1 report debt group is (c) while the paper says (d). The latter two are explicitly resolved by question meaning and source sequence without rewriting source text.
- The 2022 P3 findings rubric has overlapping lower bands; the 2024 P3 research-obstacle rubric prints a two-mark problem-only cap on a two-mark task while rejecting solution-only answers. These are ambiguities, not licences to invent corrected official rubrics.
- Some reports use “imports” in commentary corresponding to a paper's exports calculation, or give broad teaching advice. The question paper governs the actual stem and tariff; treat contradictory report wording as a source limitation.
- This stage mines structure and failure patterns. It does not verify every statistic or statement embedded in assessment sources, nor reproduce their questions for learners. Reconstruct numerical datasets and charts independently when authoring new contexts, especially percentage-to-angle conversions and quantities presented as tally data.
- The report advice about line graphs is not transcribed as a syllabus exclusion. Named historical national plans and policy examples are not presented as current policies.
- Step 3 has not built profiles, contracts, work orders, teaching resources or import payloads. The Step 3 human checkpoint and then Step 4 plan approval remain required. No publication gate is claimed.
'''
(EV/'GAPS.md').write_text(gaps)

report=['# Corpus analysis — 6136 NSSCO Development Studies\n\nStep 3, 2026-10-19. Whole subject, Grades 10–11. Source set approved by Jeremy with gaps; syllabus checkpoint approved after Claude Code review and local corrections. Internal evidence only: mine, do not reproduce.\n\n## 1. The corpus\n\n']
report.append(f'Fifteen question papers and five examiner reports cover 2020–2024. Both layout and raw extraction modes were used. The assessment ledger has **{len(records)} question parts and 1,000 marks**; every paper reconciles exactly to its cover total and every extracted tariff agrees with the raw-mode sequence. Source paths, hashes, proof labels and report page ranges are in `work/nam-6136-nssco-2026/assessment-evidence/source-manifest.json`.\n\n')
report.append('No standalone mark schemes or 2025 material were available. 2021–2023 papers are proof versions (2023 Papers 1/2 are First Revised Proofs). Examiner reports contain marking guidance, but are not relabelled as mark schemes. No legacy syllabus, other subject or supplemental-note question is counted. The earlier retrofit is not counted as assessment evidence.\n\n## 2. What each paper looks like\n\n| Paper | Parts across five years | Marks | Structure recovered from the papers |\n|---|---:|---:|---|\n')
descriptions={'P1':'Four compulsory questions, exactly 20 marks each; definitions, source identification, calculations, comparisons and developed explanations.',
 'P2':'Two compulsory questions, exactly 35 marks each; related source material plus subject knowledge and longer reasoned responses.',
 'P3':'Research methods, data presentation/interpretation, practical problem-solving and own investigation. Section A totals 35; own-investigation Q3 totals 15 every year.'}
for p in ['P1','P2','P3']:
 rs=[r for r in records if r['paper_id']==p]
 report.append(f'| {p} | {len(rs)} | {sum(r["mark_tariff"] for r in rs)} | {descriptions[p]} |\n')
report.append('\nObserved assessed-part tariffs are 1–6 marks. Paper 3 Section A is not always split 25+10: 2022 uses 20+15 and 2023 uses 24+11. Do not turn one year’s sub-question layout into a permanent rule. Six-mark research reports and 3–5-mark chart/conclusion tasks can be **level-marked**, according to report examples; a universal one-point-per-mark template would be wrong.\n\n## 3. Command words actually used\n\nOne primary operative command is counted per assessed part. “What is meant by” is normalised to the glossary’s Define synonym; its original stem is retained internally. Compounds remain compounds. Source-prefix wording is not counted as the response command. Shared parent instructions are recovered explicitly for eight child parts. Secondary instructions remain in the evidence and do not double-count marks.\n\n| Primary form | Parts | Marks | Modal tariff(s) | Tariffs seen (tariff: count) |\n|---|---:|---:|---|---|\n')
for c in sorted(cw,key=lambda c:(-c['count'],c['word'])):
 report.append(f'| {c["word"]} | {c["count"]} | {c["mark_total"]} | '+', '.join(map(str,c['modal_tariffs']))+' | '+', '.join(f'{t}: {n}' for t,n in c['tariffs_seen'].items())+' |\n')
report.append('\nListed glossary entries not observed as a primary form under this stated counting convention: '+ '; '.join(unobserved)+'. This includes noun cues and source-reference phrases, not only imperative verbs. It does not claim these strings never occur later in a stem. Full forms and IDs are in `assessment-evidence/command-word-counts.json`.\n\nStandalone Evaluate and Analyse are not observed primary commands; one **Describe and evaluate** item occurs at four marks. Differentiate, Design and Outline occur even though those literal words are absent as separate glossary entries (Design relates to Devise/plan). Do not generate large invented Evaluate essays. Use the observed command/tariff form while setting genuine judgement and discrimination where the question demands it.\n\n## 4. What a creditable answer looks like\n\n')
for sh in shapes:
 report.append(f'- **{sh["id"]}** — {sh["evidence_ids"][0]}, report p.{sh["source_locator"]["printed_page"]}: '+ ' '.join(sh['shape'])+' '+sh['allocation']+' Guard: '+sh['guard']+'\n')
report.append('\nThese are fifteen cited exemplars, not fifteen universal rules. The 2020 P1 relationship example explicitly separates one relationship mark from two statistics marks; an Identify-three-factors item is only one mark. Conversely, the report on 2024 P3 pilot-study application gives no credit for definition alone. Exact credit-point formulas for other parts remain unverified without standalone schemes or a specific report statement. `curriculum/answer-shapes.json` preserves those distinctions.\n\n## 5. Where the marks fall\n\nThese primary-topic shares sum to the whole 1,000-mark corpus. A part is counted once by its assessed demand; incidental context is not another set of marks. Multi-objective parts are not split into invented fractional tariffs. Research owns Paper 3’s demand, with relevant content links retained separately.\n\n| Topic | Parts | Marks | Corpus share | Years represented |\n|---|---:|---:|---:|---|\n')
for t in topicstats:
 report.append(f'| {t["topic_id"]} {t["title"]} | {t["parts"]} | {t["marks"]} | {t["share_percent"]:g}% | '+', '.join(map(str,t['years']))+' |\n')
dist=Counter(x['exposure_class'] for x in exposures)
report.append('\nSource-bullet exposure classes: '+', '.join(f'{k}={v}' for k,v in sorted(dist.items()))+'. Frequent means 4–5 years; occasional 2–3; rare 1; unseen 0. The ten unassigned bullets remain compulsory. “Unseen” means no part assigned under this semantic mapping, not proof that no related idea ever appears. The 102 source bullets are not unique decomposed objectives, and enterprise appears twice across a page continuation. Step 4 must bridge these IDs rather than inflate objective counts. No token-matched first pass was used; lexical-match correction counts are not applicable.\n\n## 6. How candidates lose marks\n\n')
habits=[
 ('Naming or defining instead of applying','2020 P3 report p.136; 2023 P3 p.164; 2024 P3 pp.163,166','Use a fresh survey scenario and require the instrument, respondents, collection/recording procedure and any pilot adjustment.'),
 ('Listing instead of developing an explanation','2020 P1 report pp.124,127; 2024 P1 p.155; 2024 P2 p.158','Show a point, its mechanism and consequence at the actual tariff; do not award repeated labels as development.'),
 ('Ignoring or merely copying a source','2020 P1 report p.123; 2023 P3 p.164; 2024 P1 p.151','Require a source-supported statement and relevant figures where requested; use own words for interpretation.'),
 ('Unpaired comparisons','2020 P2 report p.129; 2021 P2 p.120; 2024 P1 p.154','Compare the same feature across both cases in each statement; a table is helpful but not a universal requirement.'),
 ('Weak numerical/graph work','2020 P1 report p.123; 2023 P1 pp.153,155–156; 2024 P1 p.154; 2024 P3 p.164','Practise units, subtraction versus percentage change, scale/key/title and pie-sector angles; match chart type to data.'),
 ('Findings, conclusions, aims and recommendations not linked','2021 P3 report p.127; 2022 P3 p.155; 2023 P3 pp.167–168; 2024 P3 pp.165–166','Build an own-study chain: question → aims → collected evidence → findings → conclusion → feasible recommendation and implementer.'),
 ('A problem without its matched response, or the wrong problem','2020 P3 report p.137; 2022 P3 p.153; 2024 P3 pp.165–166','Distinguish researcher obstacles from community issues; pair practical problems with feasible responses and keep ambiguous printed caps visible.')]
for title,cites,action in habits:report.append(f'- **{title}.** Evidence: {cites}. Resource response: {action}\n')
report.append(f'\nThe raw commentary index contains {len(comments)} records, including performance judgements, advice and overlapping fragments; {len(comments)-len(unmatched)} join to individual paper parts and {len(unmatched)} remain general/grouped/unresolved. These are not unique error counts. Conceptual pairs and the seven recurring study weaknesses above were curated by reading the reports; raw extraction/classification is not substituted for that judgement. Source numbering repairs and all unjoined comments remain inspectable.\n\n## 7. Misconceptions\n\nThirty conceptual pairs are in `curriculum/misconceptions.json`, each with a report page, paper reference, source-bullet linkage and a discrimination test. General habits such as omitting units or giving an unpaired comparison were not padded into conceptual entries. Each entry cites one occurrence; this is not an exhaustive recurrence count.\n\n')
for m in mis:report.append(f'- {m["a"]} ↔ {m["b"]}: {m["source_locator"]["paper_id"]} {m["source_locator"]["question_ref"]}, {m["series"][0]} report p.{m["source_locator"]["printed_page"]}. Test: {m["discrimination_test"]}\n')
report.append('''
## 8. Scope and limits

`curriculum/scope-scan.json` carries the syllabus’s no-assumed-prior-study, no-formal-coursework-assessment and direct-comparison constraints, with positive and negative pattern controls. No content theme is excluded. Regexes guard wording risks; they cannot judge all conceptual compliance. The own investigation and report remain required preparation for Paper 3.

The examiner report’s advice about line graphs remains report advice, not an invented “not assessed” syllabus limit. Historical plans and named examples are treated in their source context, with current claims requiring separate verification at authoring. Report tariff/numbering/rubric contradictions are recorded in `assessment-evidence/GAPS.md` rather than silently repaired into official rules.

## 9. What this means for the plan

1. Cover all ten themes and all assessable syllabus content; low exposure does not authorise removal of EU cooperation, population policies, economies of scale or other unseen bullets.
2. Give Research skills a substantial applied component, including practical community project planning, instrument design/testing, sampling application, graph work and own-investigation reporting. Definition-only revision cannot supply the observed demand.
3. Build short, targeted numerical/data tasks as well as linked explanations. Preserve observed 1–6-mark shapes and reported level-based architectures instead of assigning marks from the number of answer bullets.
4. Allocate genuine Apply/Analyse/Evaluate practice by what the answer must do. A memorised list behind Discuss is not automatically Evaluate, and genuine evaluation need not use an unobserved standalone Evaluate stem.
5. Carry the thirty evidenced concept boundaries into discriminating examples, prioritising density/distribution, urban population/urbanisation, money capital/capital goods, formal/non-formal versus traditional/modern education, and sample/sampling method.
6. Use source-bullet exposure as a bridge to a decomposed, deduplicated objective registry. Recompute all totals after that bridge; do not treat the 102 source rows as 102 final objectives or overlap-linked marks as independent totals.
7. Claude Code will author only after Jeremy reads this analysis and approves the generated plan. Codex’s later independent resource review remains separate from Claude’s earlier syllabus-transcription review. No teaching resources have been authored at this stage.

**Checkpoint: show Jeremy sections 2, 3 and 6 in short form, then stop for the Step 3 human response.**
''')
(REPO/'operations/analysis/6136-nssco-development-studies-corpus-analysis.md').write_text(''.join(report))
