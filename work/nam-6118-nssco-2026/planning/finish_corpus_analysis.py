"""Derive Step 3 outputs from manual semantic annotations and located report evidence.
No objective mappings or official credit are inferred by vocabulary matching.
"""
from pathlib import Path
from collections import Counter
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[3]; W=ROOT/'work/nam-6118-nssco-2026'
def load(p):return json.loads((W/p).read_text())
def save(p,d):(W/p).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def norm(s):return ' '.join(s.split())
def obj(codes):return ['6118-'+s+'-'+f'{int(n):02}' for s,n in (v.split(':') for v in codes.split(','))]
def topic(oid):return oid.split('-')[1].split('.')[0] if 'ANNEX' not in oid else '5'
def page(y,p):
 s=(W/f'planning/extracted/{y}-report.layout.txt').read_text()
 return re.search(rf'=== SOURCE PDF PAGE {p} ===(.*?)(?==== SOURCE PDF PAGE|\Z)',s,re.S)[1]
records=load('assessment-evidence/assessment_evidence.json')['records'];byid={r['evidence_id']:r for r in records}
details=load('assessment-evidence/demand-review.json')['records'];usable={r['evidence_id'] for r in details if r['usable_for_exposure']}
comments=load('assessment-evidence/report-commentary.json')['records'];keys=load('assessment-evidence/published-mc-keys.json')['records'];facts=load('curriculum/syllabus-facts.json')
for r in records:
 for field in ('creditworthy_points','examiner_findings','common_errors','strong_response_features'):r[field]=[]
 r['notes']=[x for x in r['notes'] if not x.startswith(('report_link=','marking_coverage='))]
# Preserve every native commentary block, including general observations. Negative keyword
# flags remain triage; only the manually selected distinctions below are misconceptions.
for f in comments:
 for eid in f['linked_evidence_ids']:
  r=byid[eid];cite=f"{f['finding_id']} [commentary; report PDF {','.join(map(str,f['pdf_pages']))}; {f['link_scope']}] "
  r['examiner_findings'].append(cite+f['internal_verbatim'])
  if any(c!='performance_or_teaching_observation' for c in f['triage_categories']):
   r['common_errors'].append(cite+'Triage categories='+','.join(f['triage_categories'])+'; see located finding. Not automatically a misconception.')
# Published MC keys: separate from commentary and independently solved answers.
for k in keys:
 for q,answer in k['answers'].items():
  r=byid[f"6118-{k['year']}-P1-{int(q):03}"]
  if answer in 'ABCD' and len(answer)==1:
   r['creditworthy_points'].append(f"[key; examiner report PDF {k['pdf_page']}] Single keyed option: {answer}. This records the published key, not an independent scientific verification.")
  else:r['notes'].append(f"Published key marker {answer!r}; compensated, not a usable keyed answer.")
# Manually read, source-anchored examples of marking architecture. These are representative,
# never a claim that all image-only memo rows have been reconstructed or verified.
SHAPES=[
(2021,'2','2(e)',487,'v = u + at','calculation_chain','A three-mark calculation credits a governing relation and a valid substitution before the final result. Do not impose this exact split on every calculation.', ['Select the appropriate constant-acceleration relation.','Substitute quantities consistently.','Complete the numerical result.']),
(2021,'2','3(a)',487,'one kelvin or one degree Celsius','qualified_definition','A two-mark definition includes both the unit-mass condition and the unit temperature change; a named quantity alone is insufficient.', ['Include energy per unit mass.','Include a one-unit temperature rise.']),
(2021,'2','7(b)',489,'Two vectors drawn tip to tail','vector_construction','Four separate credits cover a valid vector arrangement, its resultant, magnitude and direction. A numerical magnitude alone cannot earn all four.', ['Construct a valid triangle or parallelogram.','Identify the resultant correctly.','Obtain its magnitude at the stated scale.','Give its direction.']),
(2021,'2','8(a)',489,'no external resultant force','conditional_law','The two-mark law statement needs the conserved total and the condition under which it is conserved.', ['State conservation of total momentum.','Specify absence of an external resultant force.']),
(2021,'2','8(b)',489,'Momentum before collision = Momentum after','multi_step_calculation','The five-mark calculation awards intermediate momentum and combined-mass work as well as the final common velocity; it is not a five-fact list.', ['Set up conservation for the interacting system.','Form the initial momentum terms.','Use the combined final mass.','Rearrange consistently.','Obtain a final velocity with appropriate precision.']),
(2024,'2','1(a)',658,'All 5 correct','banded_classification','Five classifications share three marks: all five correct earns three, three or four earns two, two earns one. This disproves a universal one-response-per-mark rule.', ['Correctly classify all five quantities for full credit; partial credit follows the printed grouped thresholds.']),
(2024,'2','1(c)',658,'Single straight line from origin','graph_motion_segment','Two graph credits distinguish the correct starting point and a line reaching the required time-speed endpoint.', ['Start the segment at the required origin.','Draw the correct straight-line endpoint and slope.']),
(2024,'2','5(d)(i)',661,'detecting broken bones','specific_application','Two medical applications must state a relevant purpose. Merely saying that an image shows the skeleton is too vague.', ['Connect X-rays to a specific diagnostic or accepted treatment purpose.','Give an accepted purpose for gamma radiation.']),
(2024,'3','1(c)(i)',666,'T remains similar','data_backed_conclusion','A two-mark conclusion combines a decision about the proposed relationship with an observation from the supplied data.', ['Give a defensible decision about the proposed effect.','Support it using the observed near-constant period as the independent variable changes.']),
(2024,'3','2(c)',666,'all six plots correct','graph_construction','Five graph marks cover labelled axes and units, useful scales, accurate points (two marks) and a best-fit line. These are features, not five prose statements.', ['Label quantities and units on the required axes.','Use suitable scales and adequate grid coverage.','Plot all six values accurately (two marks in this scheme).','Draw a thin, well-judged best-fit line.']),
(2024,'3','2(d)',666,'mm/N','gradient','Four marks cover a visible graph triangle, matching substitution, acceptable gradient and a derived axis-ratio unit. The source misnames inverse stiffness as stiffness; preserve the graph method, correct the physical interpretation.', ['Show a large triangle using the fitted line.','Substitute the corresponding axis differences.','Calculate an acceptable slope.','Use vertical-axis unit divided by horizontal-axis unit.']),
(2024,'3','3(e)',667,'temperature of the wire may vary','specific_limitation','A one-mark limitation must be a specific measurement constraint compatible with the stated careful procedure. A generic claim of carelessness misses the demand.', ['Identify a relevant physical or instrument limitation, such as variable wire temperature or contact-position uncertainty.']),
(2024,'3','3(f)',667,'correct symbol for variable resistor','circuit_change','Two marks distinguish the appropriate variable-resistor symbol from a valid series connection in the existing circuit.', ['Use the correct variable-resistor symbol.','Place it in series in a functioning arrangement.']),
(2024,'3','4',668,'Precautions for accuracy','investigation_plan','The eight marks divide into four method elements, one accuracy precaution, one table, one graph and one conclusion method. This split is specific to this investigation.', ['Specify the setup and what is varied.','Measure the initial temperature.','Measure temperature change against timed intervals.','Repeat across different water volumes.','State a concrete accuracy precaution.','Provide a table with quantities and units.','Specify a suitable labelled graph.','Explain how data or gradients will establish the conclusion.']),

(2021,'3','4',496,'Control variables','pendulum_investigation_plan','The eight-mark plan uses five operational method points, one control, one table and one data-based conclusion method. A memorised relationship is not a method for finding the relationship.', ['Set up a pendulum.','Measure its length.','Displace and release it.','Time several oscillations and obtain period.','Repeat at different lengths.','Keep a relevant variable fixed.','Specify raw and processed table columns.','Explain how the data will test the relationship.']),
(2022,'3','4',578,'Measure original length','spring_investigation_plan','Five method marks include a usable labelled setup and measurement of original and loaded lengths; table, graph and a method for reaching a conclusion provide the other three.', ['Show and label a usable spring setup (two marking elements).','Measure the original length.','Load and measure the spring.','Repeat across several loads.','Specify a suitable data table.','Specify extension against load or mass on the graph.','Explain how the graph establishes the relationship.']),
(2023,'3','4',674,'A table to show i, r, sin i, sin r','refraction_investigation_plan','The plan credits a usable ray method, measured angles and sine processing; a table, a sine-ratio graph and a gradient-based conclusion are separately credited.', ['Trace the transparent block.','Draw a normal at the entry point.','Direct a ray at a chosen incidence angle.','Measure incidence and refraction angles.','Calculate sines for the observed angles.','Tabulate both raw angles and sines.','Plot the appropriate sine quantities.','Explain how the gradient supports the conclusion.']),
(2025,'3','3(a)(i)',659,'ecf from calculations','zero_offset_correction','Three credits distinguish both instrument readings and subtraction of the zero offset. The corrected reading follows from the measured offset, rather than being copied independently.', ['Read the zero offset.','Read the loaded indication.','Subtract the offset to obtain the corrected current.']),
(2025,'3','3(a)(ii)',659,'caused by faulty instrument','error_type_justification','A two-mark response names the error type and gives a reason connected to the instrument offset; the label alone earns only part of the credit.', ['Classify the offset as systematic.','Explain that the instrument introduces the persistent offset.']),
(2025,'3','3(a)(iii)',659,'third small division','meter_pointer','One mark requires the pointer to end at the correct scale division without contradictory diagram marks.', ['Place an unambiguous pointer at the required scale division.']),
(2025,'3','3(b)(i)',659,'consistency for both values','paired_precision','The two-mark paired calculation distinguishes correct numerical results from consistent significant figures across the pair.', ['Calculate both resistance values correctly.','Present the pair with a consistent accepted precision.']),
(2025,'3','3(b)(ii)',659,'Study the shape of the graph','processing_to_relationship','Two marks require specific processing and a method to establish the relationship; a vague request for more readings does not describe the use of the data.', ['Calculate resistance from voltage and current for each wire length.','Use an appropriate resistance-length graph or comparisons to establish the trend.']),
(2025,'3','4',659,'Control variable','comparison_investigation_plan','The eight marks allocate five to method, one to a table, one to a controlled variable and one to how cooling data establish the comparison.', ['Prepare hot water.','Measure the volume.','Measure initial temperature and use the specified covered setup.','Measure temperatures over known time intervals.','Repeat with the comparison vessel.','Provide a table with measured quantities and units.','Hold a relevant comparison variable fixed.','Compare cooling rates or temperature-time gradients.']),
]
shapes=[]
for n,(year,paper,ref,pdf,anchor,name,summary,points) in enumerate(SHAPES,1):
 source_text=page(year,pdf)
 if (year,pdf)==(2025,659):
  ocr=(W/'planning/extracted/2025-report.ocr-draft.txt').read_text()
  source_text=re.search(r'=== SOURCE PDF PAGE 659; OCR DRAFT, VERIFY IMAGE ===(.*?)(?==== SOURCE PDF PAGE|\Z)',ocr,re.S)[1]
 assert norm(anchor).lower() in norm(source_text).lower(),(year,pdf,anchor)
 matches=[r for r in records if r['year']==year and r['paper_id']==paper and r['question_ref']==ref];assert len(matches)==1,(year,paper,ref)
 r=matches[0];sid=f'AS-{n:02}'
 shapes.append(dict(shape_id=sid,name=name,command_word=r['command_word'],mark_tariff=r['mark_tariff'],evidence_kind='embedded_marking_table',evidence_ids=[r['evidence_id']],source_path=next(k['source_path'] for k in keys if k['year']==year),source_pdf_page=pdf,source_read_method='source_image_checked_with_OCR_anchor' if (year,pdf)==(2025,659) else 'native_table_text',internal_verbatim_anchor=anchor,interpretation=summary,credit_structure=points,scope='Located example; do not generalise a fixed mark split to every matching verb/tariff.'))
 r['creditworthy_points'] += [f'[{sid}; embedded marking table; report PDF {pdf}] '+x for x in points]
 r['strong_response_features'].append(summary)
# The requested families are now covered in full by individually read marking rows.
family_rows=[]
for line in (W/'planning/marking-families.tsv').read_text().splitlines():
 if not line or line.startswith('#'):continue
 year,part,pdf,anchor,summary=line.split('|');year=int(year);pdf=int(pdf);eid=f'6118-{year}-{part}'
 r=byid[eid];sources={}
 for mode in ('layout','ocr-draft'):
  text=(W/f'planning/extracted/{year}-report.{mode}.txt').read_text()
  match=re.search(rf'=== SOURCE PDF PAGE {pdf}(?:; OCR DRAFT, VERIFY IMAGE)? ===\n(.*?)(?==== SOURCE PDF PAGE|\Z)',text,re.S)
  if match:sources[mode]=match[1]
 modes=[mode for mode,text in sources.items() if norm(anchor).lower() in norm(text).lower()]
 assert modes,(eid,pdf,anchor)
 mode=modes[0]
 source_path=next(x['path'] for x in load('curriculum/source-inventory.json')['entries'] if x.get('year')==year and x['kind']=='combined_examiner_report')
 shape=dict(shape_id='MF-'+eid,name=r['command_word']+'_located_marking_row',command_word=r['command_word'],mark_tariff=r['mark_tariff'],evidence_kind='embedded_marking_table',evidence_ids=[eid],source_path=source_path,source_pdf_page=pdf,source_question_ref=r['question_ref'],source_read_method='native_table_text' if mode=='layout' else 'manually_checked_OCR_table',internal_verbatim_anchor=anchor,interpretation=summary,credit_structure=[summary],scope='Part-specific marking architecture checked against the located table; no universal verb-to-mark split is inferred.',verification=dict(status='lead_agent_table_checked',method='Read the native or OCR marking row alongside its question demand and tariff; ambiguous numerical text is not adopted as an answer key.',source_mode=mode,source_page_image_checked=(year,pdf) in {(2020,467),(2021,495),(2024,658),(2024,661),(2025,659)}))
 # Replace the earlier example for this demand, rather than counting it twice.
 shapes=[old for old in shapes if eid not in old['evidence_ids']]
 shapes.append(shape);family_rows.append(shape)
 r['creditworthy_points']=[f"[{shape['shape_id']}; embedded marking table; report PDF {pdf}] "+summary]
 r['strong_response_features']=[summary]
needed={r['evidence_id'] for r in records if r['command_word'] in ('calculate','define','explain')}
assert {e for f in family_rows for e in f['evidence_ids']}==needed
save('assessment-evidence/marking-family-coverage.json',dict(status='all_requested_primary_command_families_checked',scope='Primary calculate, define and explain demands, all papers, 2020–2025.',family_counts=dict(Counter(byid[e]['command_word'] for e in needed)),three_mark_calculations=sum(byid[e]['command_word']=='calculate' and byid[e]['mark_tariff']==3 for e in needed),evidence_ids=sorted(needed),entries=family_rows,limitations='OCR/table review is a lead-agent check, not an independent review or a complete scientific audit of every numerical answer. Existing source defects and tariff disagreements remain flagged.'))
for r in records:
 r['notes'].append('marking_coverage='+('published_key_or_located_representative_shape' if r['creditworthy_points'] else 'no_verified_part_specific_credit_structure_entered; consult report/OCR and GAPS; never invent official credit'))
save('curriculum/answer-shapes.json',dict(shape_id='6118-answer-shapes',status='requested_families_covered_with_additional_located_examples',rule='Every primary calculate, define and explain demand has located marking architecture. Other task families retain selected examples. Source anchors are internal; narrative summaries are original analysis.',entries=shapes,coverage=dict(located_marking_examples=len(shapes),structured_practical_parts=382,published_usable_mc_answers=199,requested_family_demands=len(needed),requested_family_demands_covered=len(family_rows)),remaining='Unrepresented task families still require a located marking row before their part-specific architecture is used in a plan. Checked OCR rows in the requested families are explicitly identified.'))
save('assessment-evidence/assessment_evidence.json',dict(map_id='nam-6118-nssco-2026-assessment-evidence',status='partial',records=records))
# Curate genuine conceptual distinctions, not spelling, rounding or generic exam habits.
mis=[];habits=[]
for line in (W/'planning/misconception-curation.tsv').read_text().splitlines():
 if not line or line.startswith('#'):continue
 mid,dist,codes,selector,test=line.split('|');year,paper,q,phrase=selector.split(',',3)
 fs=[f for f in comments if f['year']==int(year) and f['paper_id']==paper and (f['question_ref'] or '').startswith(q) and norm(phrase).lower() in norm(f['internal_verbatim']).lower()]
 assert len(fs)==1,(mid,len(fs));f=fs[0];oids=obj(codes)
 mis.append(dict(entry_id=mid,topic_id=topic(oids[0]),objective_id=oids[0],objective_ids=oids,n=1,a=dist,discrimination_task=test,evidence_kind='commentary',finding_ids=[f['finding_id']],source_locator=f"{f['source_path']}; PDF {','.join(map(str,f['pdf_pages']))}; paper {paper}; question {q}",internal_verbatim_anchor=phrase,provenance='judgement_of_meaning_supported_by_located_examiner_commentary',qualification='One located supporting block is selected per entry; n is not a count of every recurrence. The diagnostic is an original task outline, not an authored card.'))
# Move all six challenged entries out of the conceptual misconception register.
moved_ids={'MIS-20','MIS-21','MIS-24','MIS-25','MIS-27','MIS-29'}
for entry in mis:
 if entry['entry_id'] in moved_ids:
  habit=dict(entry);habit['classification']='candidate_error_or_skill_practice';habit['reason']='Moved on operator feedback: the located report evidence does not establish a distinct conceptual belief strongly enough for a dedicated MISCON slot.';habits.append(habit)
mis=[entry for entry in mis if entry['entry_id'] not in moved_ids]
save('curriculum/candidate-errors.json',dict(register_id='6118-candidate-errors',entries=habits,rule='Retained in corpus-analysis section 6 as practice needs; these entries do not generate misconception cards.'))
save('curriculum/misconceptions.json',dict(register_id='6118-misconceptions',status='curated_step3_source_bullet_anchors',objective_id_policy='These IDs identify syllabus source bullets, not the decomposed Step 4 target registry. Step 4 must carry them through explicit semantic target mappings; no automatic one-card-per-bullet rule.',entries=mis))
# Raw census metrics retain compensated item; usable metrics exclude it. A part's
# whole tariff attached to several objectives is not an additive mark apportionment.
index=load('curriculum/source-objective-index.json')['objectives']+[dict(objective_id='6118-ANNEX-D-01',subtopic_code='ANNEX-D',text='Annexe D diode symbol; bounded observed rectification context.')]
def metrics(rs):
 c=Counter(r['command_word'] for r in rs if r['command_word']);tar=Counter(r['mark_tariff'] for r in rs)
 return dict(question_parts_naming_it=len(rs),distinct_series=len({r['year'] for r in rs}),series=sorted({r['year'] for r in rs}),max_mark_tariff=max((r['mark_tariff'] for r in rs),default=0),command_words_observed=dict(sorted(c.items())),tariffs=dict(sorted(tar.items())),linked_marks_nonadditive=sum(r['mark_tariff'] for r in rs),evidence_ids=[r['evidence_id'] for r in rs])
ex=[]
for o in index:
 rs=[r for r in records if o['objective_id'] in r['objective_ids']];us=[r for r in rs if r['evidence_id'] in usable];s=len({r['year'] for r in us})
 ex.append(dict(objective_id=o['objective_id'],topic_id=topic(o['objective_id']),syllabus_text=o['text'],evidence=metrics(rs),usable_evidence=metrics(us),exposure_class='frequent' if s>=3 else 'occasional' if s==2 else 'rare' if s==1 else 'unseen',exam_exposure='probed_high' if s>=3 else 'probed_low' if s else 'unprobed_2020_2025'))
shares=[]
for t in '123456':
 rs=[r for r in records if r['paper_id'] in ('1','2') and r['evidence_id'] in usable and topic(r['objective_ids'][0])==t]
 shares.append(dict(topic_id=t,title=next(x['title'] for x in facts['content_outline'] if x['code']==t),primary_content_marks=sum(r['mark_tariff'] for r in rs),share_percent=round(100*sum(r['mark_tariff'] for r in rs)/719,2),parts=len(rs)))
save('curriculum/exam-exposure.json',dict(exposure_id='6118-exposure-2020-2025',provenance='corpus_counts_over_manually_reviewed_semantic_mappings',classes={'frequent':'3 or more usable distinct annual series','occasional':'2 usable annual series','rare':'1 usable annual series','unseen':'0 usable annual series'},method='Counts are derived; source-bullet IDs are provisional anchors pending Step 4 decomposition. Whole question-part tariffs linked to multiple objectives are nonadditive. Raw evidence metrics retain compensated item for census reconciliation; usable_evidence and exposure classes omit it. Primary-objective content shares allocate each P1/P2 mark once, by judgement of its principal demand. They are not official blueprint weights or AO allocations. P3 is kept separately as 240 practical marks, not used to inflate content shares.',excluded_from_usable=['6118-2024-P1-009'],objectives=ex,primary_content_topic_shares=shares,denominators=dict(printed_parts=622,printed_marks=960,usable_parts=621,usable_marks=959,usable_P1_P2_marks=719,P3_marks=240)))
# One primary command per mark-bearing demand, with explicit inherited instructions.
cws=[]
for cw in sorted({r['command_word'] for r in records if r['command_word']}):
 rs=[r for r in records if r['command_word']==cw];tar=Counter(r['mark_tariff'] for r in rs);m=max(tar.values())
 cws.append(dict(word=cw,observed_count=len(rs),modal_tariffs=sorted(k for k,v in tar.items() if v==m),observed_tariffs=sorted(tar),tariff_counts=dict(sorted(tar.items())),paper_counts=dict(Counter(r['paper_id'] for r in rs)),marks=sum(r['mark_tariff'] for r in rs),paper_marks={p:sum(r['mark_tariff'] for r in rs if r['paper_id']==p) for p in ('2','3')},use_in_prompts=True,provenance='corpus'))
terms=[x['term'] for x in facts['command_words']]
# Glossary rows are preserved verbatim. A row can contain a paired instruction.
rows=[]
for term in terms:
 aliases=[x.strip().lower() for x in re.split(r'/|\bor\b|\band\b',term)]
 observed=[c['word'] for c in cws if c['word'] in aliases or c['word']==term.lower()]
 rows.append(dict(syllabus_term=term,observed_primary_commands=observed,listed_but_not_primary_observed=not observed,provenance='syllabus row with corpus observation'))
save('curriculum/command-word-census.json',dict(census_id='6118-primary-command-census',method='One primary imperative per terminal marked segment, including inherited parent instructions; MC interrogatives are null. Secondary instructions inside a segment are not separately counted. Draw includes diagrams and drawing a conclusion; subtype must be retained. Glossary row absence in this census does not prove absence as a secondary instruction.',commands=cws,syllabus_glossary_rows=rows,unlabelled_structured_practical=[r['evidence_id'] for r in records if r['paper_id']!='1' and not r['command_word']]))
# Narrow lexical checks plus explicit context gates; no global ban on nuclide equations.
limits=[x for x in facts['scope_limits_and_conditions'] if x['kind']=='explicit_limit'];assert len(limits)==3
configs=[
('Collision definitions',r'\b(?:define|definition\s+of)\s+(?:(?:an?|the)\s+)?(?:elastic|inelastic)\s+collision\b|\b(?:elastic|inelastic)\s+collision\s+(?:is\s+defined\s+as|means)\b',['Define an elastic collision.','An inelastic collision means a collision that changes kinetic energy.'],['Apply momentum conservation to an inelastic collision.','Two bodies collide along one line.'], '2.4','Definitions are not required; one-dimensional two-body momentum applications remain in scope. Do not ban the collision terms themselves.'),
('Nuclide formulae in energy-source teaching',r'\b(?:nuclear\s+energy\s+source|energy\s+from\s+nuclear\s+fuel)\b.{0,100}\b(?:write|balance|derive)\b.{0,45}\b(?:nuclide|nuclear)\s+(?:formula|equation)', ['For a nuclear energy source, write a nuclide equation for the fuel reaction.'], ['Write a decay equation for beta emission.','Explain an advantage of a nuclear energy source.','Balance a nuclear equation in radioactivity.'], '2.10.1','Requires energy-source context. Nuclear Physics decay equations remain required. A paragraph-level pattern cannot replace a contextual review of an entire energy section.'),
('Standalone diverging-lens theory',r'\b(?:derive|calculate)\b.{0,70}\b(?:diverging|concave)\s+lens\b.{0,60}\b(?:formula|magnification|image\s+distance)\b',['Calculate the diverging lens image distance using the lens formula.'],['A diverging lens corrects short sight.','Draw rays showing a diverging lens correcting short sight.','Construct an image formed by a converging lens.'], '4.3.3','Diverging lenses are limited to eye-defect correction. Lexical screen catches selected standalone depth excursions; human context review is required for other formulations.')]
scope=[]
for limit,(name,pattern,catch,allow,sub,explain) in zip(limits,configs):
 assert limit['subtopic_code']==sub
 scope.append(dict(construct=name,pattern=pattern,applies_to='subject',context_subtopic=sub,controls=dict(must_catch=catch,must_allow=allow),source=f"syllabus PDF {limit['source']['pdf_page']}; topic {sub}",syllabus_sentence=limit['text'],provenance=dict(sentence='syllabus',pattern='judgement'),interpretation=explain,automation_limit='Heuristic screen plus human context review; a passing regex check does not certify complete scope compliance.'))
 for s in catch:assert re.search(pattern,s,re.I),(name,s)
 for s in allow:assert not re.search(pattern,s,re.I),(name,s)
save('curriculum/scope-scan.json',dict(scope_scan_id='6118-scope-scan',entries=scope,depth_and_condition_checks=[x for x in facts['scope_limits_and_conditions'] if x['kind']!='explicit_limit'],rule='Three explicit exclusions have bounded patterns. Other depth/condition wording is retained for manual planning review, not converted into broad banned-word rules.'))
# Source scientific/rubric issues are distinct from candidate misconceptions.
issues=[
('SRC-01',2024,'1','9',[654],'key/commentary','No correct MC option; report compensates every candidate.','Exclude from usable exposure and diagnostics; retain census mark.'),
('SRC-02',2024,'3','2(c,d)',[666],'question_and_marking_table','Extension/load slope has units mm/N and equals reciprocal stiffness, despite source calling it k.','Teach slope from actual axes and convert to stiffness if required.'),
('SRC-03',2025,'3','1(c)',[657],'question','Volume/mass slope is reciprocal density. Introductory source sentence calls it density; following reciprocal calculation is consistent with axes.','Keep axis-ratio dimensional reasoning; do not copy erroneous interpretation.'),
('SRC-04',2020,'2','4(b)(i)',[469],'commentary','Commentary names specific heat capacity while the question and marking demand concern specific latent heat.','Use actual demand; do not curate the report label error as a learner misconception.'),
('SRC-05',2021,'3','3(d)',[495],'marking_table','Image-verified table gives d(i) one mark and d(ii) two, while the question paper gives two and one respectively.','Use question-paper tariffs in demand census; do not treat mismatching table column as settled allocations.'),
('SRC-06',2024,'2','4(d)(ii)',[661],'marking_table','Image-verified table prints 2.5 for arcsin(sin35/1.5); calculation gives approximately 22.5 degrees.','Use correct mathematics in original examples; source numeric answer is not authoritative.'),
('SRC-07',2024,'1','32',[656],'commentary','Wire-resistance commentary treats diameter as simply inverse rather than inverse-square, for fixed material and length.','Use R proportional to 1/area and hence 1/diameter squared.'),
('SRC-08',2025,'1','31',[645],'commentary','Wire-diameter reasoning needs R proportional to inverse area; any inverse-diameter shorthand is insufficient.','Derive from circular area before adapting a diagnostic; not a new exclusion.')]
save('assessment-evidence/source-issues.json',dict(entries=[dict(issue_id=i,year=y,paper_id=p,question_ref=q,report_pdf_pages=pages,evidence_kind=k,issue=s,handling=h,provenance='lead_agent_source_read_and_physics_check') for i,y,p,q,pages,k,s,h in issues],reference_repairs=load('planning/reference-corrections.json'),semantic_review_repairs=[dict(evidence_id='6118-2025-P2-027',before='relay / circuit objective',after='fuse / electrical-safety source bullet',verification='Question-paper PDF p.11 image inspected: fuse rectangle with through-line; consistent with report function.')]))
stats=dict(records=len(records),printed_marks=sum(r['mark_tariff'] for r in records),usable_records=len(usable),usable_marks=sum(r['mark_tariff'] for r in records if r['evidence_id'] in usable),commentary_blocks=len(comments),linked_blocks=sum(bool(f['linked_evidence_ids']) for f in comments),records_with_findings=sum(bool(r['examiner_findings']) for r in records),records_with_error_triage=sum(bool(r['common_errors']) for r in records),records_with_credit=sum(bool(r['creditworthy_points']) for r in records),curated_misconceptions=len(mis),marking_shape_examples=len(shapes),source_bullets=335,supplementary_anchors=1,exposure_classes=dict(Counter(x['exposure_class'] for x in ex)))
save('assessment-evidence/mining-summary.json',stats)
print(json.dumps(stats,indent=2));print('TOPIC SHARES',shares);print('COMMANDS',[(c['word'],c['observed_count'],c['modal_tariffs'],c['paper_marks']) for c in cws]);print('LISTED NOT PRIMARY',[r['syllabus_term'] for r in rows if r['listed_but_not_primary_observed']])
