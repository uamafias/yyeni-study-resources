"""Build measured evidence from reconciled questions and reviewed semantic choices."""
import collections
import json
import re
from pathlib import Path
from semantic_mappings import MAPPINGS, MAPPING_NOTES

WS = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((WS/path).read_text())
def write(path, obj):
    (WS/path).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')

facts = read('curriculum/syllabus-facts.json')
parts = read('planning/question-candidates.json')
audit = read('planning/question-extraction-audit.json')
assert all(r['reconciles'] for r in audit)
assert len({r['evidence_id'] for r in parts}) == len(parts)
objectives = {}
for topic in facts['topics']:
    for number, text in enumerate(topic['specific_objectives'], 1):
        key = f"{topic['topic_id']}.{number}"
        objectives[key] = {'objective_id': f"OBJ-6145-{topic['topic_id']}-{number:02}",
                           'topic_id': topic['topic_id'], 'syllabus_text': text,
                           'source': topic['source'], 'reference_only': True}
write('planning/objective-reference.json', {'note': 'Stable syllabus-bullet references for mining; not the decomposed step-4 registry.', 'objectives': list(objectives.values())})

verbs = r'write down|explain|define|describe|discuss|evaluate|assess|calculate|outline|state|name|give|identify|consider|comment|analyse|draw|show|illustrate|indicate|mention|advise|distinguish|justify|suggest|compare|list|examine'
command_overrides = {
    '2020-P1-8': 'which', '2021-P1-24(a)(i)': 'comment', '2021-P1-24(a)(ii)': 'comment',
    '2022-P1-9': 'which', '2022-P1-13': 'what', '2022-P1-17': 'which',
    '2023-P1-11': 'what', '2023-P1-14': 'what', '2023-P1-22': 'identify',
    '2023-P1-24': 'how', '2023-P1-25(d)': 'what', '2024-P1-9': 'show', '2024-P1-17': 'how',
}
for key, mappings in MAPPINGS.items():
    year, paper = key.split('-')
    rows = [r for r in parts if r['year'] == int(year) and r['paper_id'] == paper]
    mappings = mappings.split()
    assert len(rows) == len(mappings), (key, len(rows), len(mappings))
    for row, mapping in zip(rows, mappings):
        objective = objectives[mapping]
        local = f"{key}-{row['question_ref']}"
        row['objective_ids'] = [objective['objective_id']]
        row['topic_id'] = objective['topic_id']
        row['mapping_method'] = 'Human semantic reading of the question demand and syllabus bullet; explicit per-part choices in planning/semantic_mappings.py. No token-matched first pass.'
        row['mapping_confidence'] = 'moderate' if local in MAPPING_NOTES else 'high'
        row['mapping_note'] = MAPPING_NOTES.get(local, 'Primary objective selected by meaning; marks allocated once to avoid counting a multi-construct part twice.')
        stem = row['stem']
        matches = list(re.finditer(r'\b('+verbs+r')\b', stem, re.I))
        opening = re.match(r'(What|Why|How|Who|When|Which|Is|To what|In which)\b', stem, re.I)
        command = (opening[1].lower() if opening else matches[0][1].lower() if matches else None)
        if command is None:
            interrogative = re.search(r'\b(What|Why|How|Who|When|Which|In which|To what)\b',stem)
            command = interrogative[1].lower() if interrogative else None
        command = command_overrides.get(local, command)
        assert command, local
        row['command_word'] = command
        row['command_words_present'] = sorted({m[1].lower() for m in matches} | {command})
        row['command_method'] = 'First substantive task verb; introductory use/using/with wrappers omitted. Interrogative wording retained, not silently converted into an imperative.'
        if row['paper_id'] == 'P1' and row['section'] == 'A':
            ao, provenance = ['A'], 'syllabus: Paper 1 Section A is AO A; command wording does not override it'
        else:
            evaluative = re.search(r'\b(whether|to what extent|to what|to which|agree|in favour|only benefits|always|should always)\b',stem,re.I)
            ao = ['C'] if command in ('evaluate','assess','consider','advise','justify','examine') or evaluative else ['A'] if command in ('define','name','list','state','outline','identify','write down','distinguish') else ['B']
            provenance = 'judgement: semantic demand, checked against report labels where present; not an official allocation of each mark'
        row['ao_focus'] = ao
        row['ao_focus_provenance'] = provenance
        report_ao = {'2023-P1-25(a)':'A','2023-P1-25(b)':'B','2023-P1-25(c)':'C','2023-P1-25(d)':'C',
                     '2023-P1-26(a)':'B','2023-P1-26(b)':'B','2023-P1-26(c)':'C','2023-P1-26(d)':'C',
                     '2023-P2-1(a)':'A','2023-P2-1(b)':'B','2023-P2-1(c)':'B','2023-P2-1(d)':'B','2023-P2-1(e)':'C',
                     '2023-P2-2(a)':'A','2023-P2-2(b)':'B','2023-P2-2(c)':'C',
                     '2023-P2-4(a)':'A','2023-P2-4(b)':'B','2023-P2-4(c)':'C',
                     '2023-P2-5(a)(i)':'A','2023-P2-5(a)(ii)':'A','2023-P2-5(b)':'B','2023-P2-5(c)':'C',
                     '2023-P2-6(a)':'A','2023-P2-6(b)':'A','2023-P2-6(c)':'B','2023-P2-6(d)':'C'}
        if local in report_ao:
            row['ao_focus'] = [report_ao[local]]
            row['ao_focus_provenance'] = 'corpus: 2023 examiner-report Kn / Ap / An / Ev label, mapped to syllabus A / B / C; no per-mark AO split inferred'
        if local=='2022-P1-7':
            row['command_words_present'].remove('compare')  # narrative function of money, not a task instruction
        row['context_type'] = 'data_or_scenario' if row['section'] == 'B' or row['paper_id'] == 'P2' else 'short_answer'
        row['creditworthy_points'] = []
        row['creditworthy_points_note'] = 'Not individually transcribed from a standalone mark scheme. Selected report-backed answer-shape records are attached below; absent records remain unknown.'
        row['examiner_findings'] = []
        row['common_errors'] = []
        row['strong_response_features'] = []
        row['notes'] = [row['mapping_note']]
        if row['paper_id']=='P1' and row['year'] in (2021,2022,2023):
            row['notes'].append('Question-paper filename is marked First Proof; retain provisional-source caveat.')

# Corrections after reading both extraction orders and the report page headings.
ref_corrections = {
    '2021-069':'5', '2021-072':'9', '2021-073':'11(a)',
    '2021-085':'25(a)(ii)', '2021-086':'25(b)', '2021-087':'25(c)',
    '2023-550':'3(b)', '2023-558':'3(c)', '2023-636':'6(b)',
    '2023-644':'6(c)', '2023-652':'6(d)',
}
by_question = {(r['year'],r['paper_id'],r['question_ref']): r for r in parts}
all_candidates = read('assessment-evidence/report-comment-candidates.json')
candidate_by_id = {r['finding_id']:r for r in all_candidates}
findings = []
for record in all_candidates:
    # Remove the answer/guidance text that runs on in some raw-order table rows.
    statement = re.split(r'\b(?:Define|Describe|Explain|Identify|Discuss|Evaluate|Assess|Calculate|Outline|State|Name|Give|Consider|Using|Use|Why|What|How|Write down|Distinguish|Except for|With the help)\b|•',record['statement'])[0].strip()
    statement = ' '.join(re.split(r'(?<=[.!?])\s+',statement)[:5])
    if len(statement)<30 or not re.search(r'learners|candidates',statement,re.I):
        continue
    if not re.search(r'not |fail|confus|instead|only|wrong|difficult|lost|unable|lacked|poor|listing|one.side|rather|copied',statement,re.I) and record['finding_id'] != 'ER-6145-2020-023':
        continue
    if not re.match(r'Well|Fairly|Poorly|Not well|Moderately|Most learners|Some learners|Learners|The majority|A few|Many learners',statement):
        continue
    if statement.startswith(('Learners must','Learners should')):
        continue
    if record['finding_id']=='ER-6145-2023-302':
        continue  # improvement in listing is a positive observation, not an error
    item = dict(record, statement=statement)
    suffix = record['finding_id'].removeprefix('ER-6145-')
    item['question_ref'] = ref_corrections.get(suffix, record['question_ref'])
    target = by_question.get((record['year'],record['paper_id'],item['question_ref']))
    item['objective_ids'] = target['objective_ids'] if target else []
    item['classification'] = ('shallow development' if re.search(r'one.side|listing|develop|list.*instead',statement,re.I)
                              else 'command-word miss' if re.search(r'instead|rather|question|link|referr|referred',statement,re.I)
                              else 'omission')
    item['classification_provenance'] = 'judgement; conceptual confusions are separately curated in misconceptions.json'
    item['mapping_method'] = 'Question reference with manually reviewed extraction corrections; broad/unresolved cases remain explicitly flagged.'
    item['mapping_status'] = 'question_linked' if target else 'report_only_or_unresolved'
    # Verify the quoted comment against the page extraction before accepting it.
    source_text = (WS/record['source_locator']['extraction']).read_text()
    page_text = source_text.split(f"=== PDF PAGE {record['source_locator']['pdf_page']} ===",1)[1].split('=== PDF PAGE',1)[0]
    assert re.sub(r'\s+',' ',statement).strip() in re.sub(r'\s+',' ',page_text), record['finding_id']
    if target:
        target['examiner_findings'].append(item['finding_id'])
        target['common_errors'].append({'finding_id':item['finding_id'],'classification':item['classification'], 'statement':statement})
    findings.append(item)

# A few report-only mappings require meaning because no 2025 QPs are available.
report_2025 = {
    '739':'1.1.1','741':'5.1.4','745':'3.2.2','746':'6.3.2','749':'4.3.1','750':'4.2.4',
    '751':'5.3.1','752':'6.2.3','754':'7.1.1','756':'7.2.2','757':'7.3.2','758':'7.4.2',
    '760':'8.2.1','761':'8.1.4','762':'3.5.1','764':'3.5.1','765':'6.3.2','767':'8.2.1',
    '769':'8.2.3','785':'1.1.3','811':'7.4.1','826':'5.4.2','838':'6.2.4','848':'6.2.5',
    '857':'7.3.3','869':'1.2.1','871':'1.2.1','876':'2.1.2','882':'1.2.3','901':'9.1.1',
    '909':'7.4.2','920':'9.1.1','937':'6.2.3','946':'2.3.5','957':'6.2.6',
}
for row in findings:
    last = row['finding_id'].split('-')[-1]
    if row['year']==2025 and last in report_2025:
        row['objective_ids'] = [objectives[report_2025[last]]['objective_id']]
        row['mapping_status'] = 'report_only_semantic_mapping; excluded from QP exposure counts'

write('assessment-evidence/examiner_findings.json', {'findings':findings,
    'note':'Raw candidates include positive comments, guidance and recommendations. These are extracted error comments, not 973 independently verified errors. The misconception register is a separate semantic curation. QP references and report text can disagree; source discrepancies are recorded separately.'})

def support(year, page, phrase, order='raw'):
    path = WS/f'assessment-evidence/extracted/6145-{year}-ER-{order}.txt'
    text = path.read_text().split(f'=== PDF PAGE {page} ===',1)[1].split('=== PDF PAGE',1)[0]
    assert re.sub(r'\s+',' ',phrase).strip() in re.sub(r'\s+',' ',text), (year,page,phrase)
    return {'source_id':f'6145-{year}-ER','pdf_page':page,'verbatim':phrase,'extraction':str(path.relative_to(WS))}

# Only these selected shapes are directly evidenced and attached to their parts.
shapes = [
 {'shape_id':'SH-DEF','command_words':['define','describe','what','explain'], 'tariffs':[1,2,3],
  'answer_architecture':['Give the economic meaning with each defining element; an example supports but does not replace the definition.'],
  'support':[support(2020,147,'Up to two marks for definition of GDP'),support(2021,140,'Up to two marks for description of employers’ association.')],
  'question_keys':['2020-P2-2(a)','2021-P2-3(c)']},
 {'shape_id':'SH-IDENTIFY-EXAMPLE','command_words':['identify','define'], 'tariffs':[4,6],
  'answer_architecture':['Supply each concept and the requested type/example separately; link the example to the extract when requested.'],
  'support':[support(2021,139,'Two marks for definition. Two marks for examples.')],
  'question_keys':['2021-P2-3(a)']},
 {'shape_id':'SH-DIAGRAM-4-3','command_words':['explain','illustrate','analyse'], 'tariffs':[7],
  'answer_architecture':['Draw the correct economic market with labels, equilibrium and the specified change or price control.','Explain the direction of price and quantity changes, or the surplus/shortage; the diagram alone is incomplete.'],
  'support':[support(2020,146,'Diagram (4)'),support(2020,146,'Explanation (3)'),support(2024,177,'Up to four marks for the application.'),support(2024,177,'Up to three marks for analysis.')],
  'question_keys':['2020-P2-1(b)','2024-P1-24(c)']},
 {'shape_id':'SH-EXPLAIN-DEVELOP','command_words':['explain','describe','analyse','discuss'], 'tariffs':[6,7],
  'answer_architecture':['Make a relevant point, develop its mechanism or consequence, and connect it to the named economic agent.','Do not repeat the same effect using different words or answer only with a list.'],
  'support':[support(2021,141,'Most learners were listing and could not explain the points in full.'),support(2025,168,'Point and development 3 x 2 + 1')],
  'question_keys':['2021-P2-4(c)']},
 {'shape_id':'SH-EVAL-7-2023','command_words':['evaluate','consider','assess','discuss'], 'tariffs':[7],
  'answer_architecture':['Develop relevant arguments on both sides in context.','For the cited 2023 question, one-sided work is capped at 3; both sides access 4–6 and a distinct reasoned conclusion earns the remaining mark.'],
  'support':[support(2023,185,'Ev L1 (1 - 3 marks)'),support(2023,185,'Ev L 2 (4 - 6 marks)'),support(2023,185,'Learners must reach a conclusion.')],
  'question_keys':['2023-P2-2(c)']},
 {'shape_id':'SH-EVAL-9','command_words':['evaluate','assess'], 'tariffs':[9],
  'answer_architecture':['Develop both sides of the economic issue.','Use the source-specific 1–4 versus 5–8 bands for the cited 2023 question, then add a distinct justified conclusion; do not duplicate an earlier credited point.'],
  'support':[support(2023,183,'Ev L1 (1 - 4 marks)'),support(2023,183,'Ev L 2 (5 - 8 marks)'),support(2020,147,'One mark for valid conclusion which was not already mentioned in answer.')],
  'question_keys':['2023-P2-1(e)','2020-P2-1(c)']},
 {'shape_id':'SH-EVAL-7-2024','command_words':['discuss'], 'tariffs':[7],
  'answer_architecture':['Explain why the proposed result might occur and why it might not.','The 2024 report allows a 4/3 or 3/4 split across sides; do not impose the 2023 conclusion allocation on every seven-mark question.'],
  'support':[support(2024,178,'Both sided seven marks.')],
  'question_keys':['2024-P1-24(d)']},
 {'shape_id':'SH-RPI','command_words':['describe','explain'], 'tariffs':[4,7],
  'answer_architecture':['Select a representative basket, assign expenditure weights, select the base period, collect prices and construct the weighted index.','Distinguish the index level from the percentage change between periods.'],
  'support':[support(2024,182,'Select a basket of goods and services'),support(2024,182,'Attached weight to goods and services in the basket')],
  'question_keys':['2024-P2-3(c)']},
 {'shape_id':'SH-CALCULATE','command_words':['calculate'], 'tariffs':[1,2,5],
  'answer_architecture':['State the appropriate relationship, substitute the given data, carry out the arithmetic and label the result.','A percentage-change result needs the original value as denominator; elasticity is the ratio of percentage changes, without another multiplication by 100.'],
  'support':[support(2023,177,'could not convert it to percentages.'),support(2025,156,'A few learners multiplied with 100.')],
  'question_keys':['2023-P1-25(b)']},
]
for shape in shapes:
    shape['provenance'] = 'corpus: examiner-report suggested answers and guidance; paraphrased structure, not a universal tariff rule'
    for key in shape['question_keys']:
        year,paper,ref = key.split('-',2)
        row = by_question[(int(year),paper,ref)]
        row.setdefault('answer_shape_ids',[]).append(shape['shape_id'])
        row['creditworthy_points'].extend(shape['answer_architecture'])
        row['creditworthy_points_note'] = 'Paraphrased structural credit requirements from the cited report; not verbatim answer points.'
        row['strong_response_features'].extend(shape['answer_architecture'])
write('curriculum/answer-shapes.json', {'shapes':shapes,
      'limitations':['Standalone mark schemes are absent. Report guidance is used only where directly available.',
                     'Command word alone does not determine AO or answer shape; read the whole task, tariff, context and year-specific guidance.',
                     'Some 2023 guidance labels and tariffs conflict internally and with QPs. Exact universal allocation cannot be inferred.']})

evidence = {'evidence_id':'EVIDENCE-NAM-6145-NSSCO-2026', 'derivation_policy':'mine_do_not_reproduce',
            'records':parts, 'status':'measured_with_documented_gaps',
            'notes':['Question frequency uses the ten held 2020–2024 papers only. The 2025 report supplements errors and shapes, not question counts.',
                     'Each primary objective was selected by meaning. The 96 references have not yet been decomposed into the step-4 registry.',
                     'AOs outside the syllabus-labelled Paper 1 Section A are judgements, not per-mark official splits.']}
write('assessment-evidence/assessment_evidence.json',evidence)

exposure = []
for obj in objectives.values():
    rows = [r for r in parts if obj['objective_id'] in r['objective_ids']]
    years = sorted({r['exam_series'] for r in rows})
    tariffs = collections.Counter(r['mark_tariff'] for r in rows)
    spread = len(years)
    evidence_metrics = {'question_parts_naming_it':len(rows),'marks_examined':sum(r['mark_tariff'] for r in rows),
                        'distinct_series':spread,'series':years,'max_mark_tariff':max(tariffs,default=0),
                        'tariffs':dict(tariffs),'command_words_observed':dict(collections.Counter(r['command_word'] for r in rows)),
                        'modal_tariff':min(tariffs,key=lambda t:(-tariffs[t],t)) if tariffs else None,
                        'evidence_ids':[r['evidence_id'] for r in rows]}
    exposure.append(dict(obj,evidence=evidence_metrics,
                         exam_exposure='probed_high' if max(tariffs,default=0)>=6 or spread>=3 else 'probed_low' if rows else 'unprobed_2020_2024'))
assert sum(r['evidence']['marks_examined'] for r in exposure) == 1000
write('curriculum/exam-exposure.json', {'exposure_id':'EXPOSURE-NAM-6145-NSSCO-2026', 'status':'measured',
     'method':'All primary objectives mapped by meaning; one primary assignment per tariff-bearing question part. Values recomputed from records.',
     'classes':{'probed_high':'6 marks or more, or 3 or more distinct series',
                'probed_low':'5 marks or fewer and fewer than 3 distinct series',
                'unprobed_2020_2024':'No primary mapped question part in the held 2020–2024 corpus'},
     'window':'2020–2024; five annual series, ten question papers; all offered options included',
     'caveats':['A Paper 2 offers 120 marks but each candidate attempts 80. Shares describe offered content, not a candidate route.',
                'Topic shares are approximate primary-demand allocations; contextual numeracy is explicitly flagged.',
                'Unseen means not a primary mapped demand in the held corpus, not impossible to examine or unnecessary to teach.',
                'Do not treat undecomposed bullet exposure as exposure of every member listed in that bullet.'],
     'principle':'Frequency may calibrate emphasis; it never removes syllabus coverage.',
     'unmatched_parts':0,'objectives':exposure})

table_words = {c['word'] for c in facts['command_words']}
commands = []
for word in sorted(table_words | {w for r in parts for w in r['command_words_present']}):
    rows = [r for r in parts if r['command_word']==word]
    counter = collections.Counter(r['mark_tariff'] for r in rows)
    commands.append({'word':word,'in_syllabus_table':word in table_words,
        'count':len(rows),'marks':sum(r['mark_tariff'] for r in rows),
        'embedded_only_count':sum(word in r['command_words_present'] and r['command_word']!=word for r in parts),
        'modal_tariff':min(counter,key=lambda t:(-counter[t],t)) if counter else None,
        'tariffs':sorted(counter),'tariff_counts':dict(counter),
        'per_paper':dict(collections.Counter(r['paper_id'] for r in rows)),
        'use_in_prompts':bool(rows) and word not in ('what','why','how','who','which','when','is','in which','to what'),
        'verdict':'observed_and_listed' if rows and word in table_words else 'observed_not_listed' if rows else 'embedded_only' if word not in table_words else 'listed_not_observed',
        'note':'Interrogative forms are counted as observed phrasing; prompt design should preserve their demand without assuming they are imperative command words.'})
write('assessment-evidence/command-word-counts.json',{'counting_rule':'One primary command per tariff-bearing part, based on substantive instruction. Compound verbs are preserved separately on records. Equal-frequency modal tariff ties choose the smaller tariff.', 'commands':commands})
topic_stats = []
for topic in facts['topics']:
    rows = [r for r in parts if r['topic_id']==topic['topic_id']]
    marks = sum(r['mark_tariff'] for r in rows)
    topic_stats.append({'topic_id':topic['topic_id'],'title':topic['topic_title'],'parts':len(rows),'marks':marks,
                        'share_percent':marks/10, 'series':sorted({r['year'] for r in rows})})
write('assessment-evidence/topic-mark-shares.json', {'denominator':1000,'basis':'All printed offered question marks, including unchosen Paper 2 options; one primary topic per part.','topics':topic_stats})

summary = {'question_papers':10,'annual_series':5,'question_parts':len(parts),'printed_offered_marks':sum(r['mark_tariff'] for r in parts),
           'candidate_route_marks_across_five_years':800,'examiner_reports':6,
           'report_error_comments':len(findings),'parts_with_common_errors':sum(bool(r['common_errors']) for r in parts),
           'parts_with_directly_evidenced_answer_shapes':sum(bool(r['creditworthy_points']) for r in parts),
           'primary_mapping_flags':sum(r['mapping_confidence']=='moderate' for r in parts),
           'token_matched_first_pass':False,'token_mapping_corrections':0,
           'objective_bullets':len(objectives),'exposure_classes':dict(collections.Counter(r['exam_exposure'] for r in exposure)),
           'all_paper_totals_reconcile':True,
           'paper_tariffs':{paper:dict(sorted(collections.Counter(r['mark_tariff'] for r in parts if r['paper_id']==paper).items())) for paper in ('P1','P2')}}
write('planning/corpus-summary.json',summary)
print(json.dumps(summary,indent=2))
for command in sorted(commands,key=lambda x:-x['count']):
    print(command['word'],command['count'],command['modal_tariff'],command['tariffs'],command['per_paper'])
