"""Rebuild this subject's analysis records from analyst annotations and source bytes.

Not a recipe generator, publication tool, or independent educational reviewer.
Run from the repository root. Original source PDFs are never modified.
"""
from pathlib import Path
import collections
import hashlib
import json
import re
from pypdf import PdfReader
from analysis_inputs import OBJECTIVES, FAMILIES, QUESTIONS

ROOT = Path(__file__).resolve().parents[4]
WB = Path(__file__).resolve().parents[1]
WS = WB.parent
A = WB / 'analysis'
SYLLABUS = ROOT / 'Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf'
HASH = hashlib.sha256(SYLLABUS.read_bytes()).hexdigest()
PAGES = [p.extract_text() for p in PdfReader(SYLLABUS).pages]

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def ident(short):
    theme, topic, ordinal = short.split('.')
    return f'8227:2020:{theme}:{topic}:O{int(ordinal):02d}'

def evidence(page, anchor):
    raw = PAGES[page - 1]
    # Locate a literal prose anchor, preserving original source bytes/text for checking.
    matches = list(re.finditer(re.escape(anchor), raw, re.I))
    if len(matches) != 1:
        raise ValueError(('Ambiguous/missing syllabus anchor', page, anchor, len(matches)))
    start = matches[0].start()
    end = raw.find('\uf0b7', start)
    end = len(raw) if end == -1 else end
    quote = raw[start:end].strip()
    if 'Topic ' in quote:
        quote = quote.split('Topic ')[0].strip()
    assert quote and quote in raw
    return {'document': str(SYLLABUS.relative_to(ROOT)), 'sha256': HASH,
            'pdf_page': page, 'printed_page': page - 3, 'verbatim_extracted_quote': quote,
            'mathematical_text_limit': 'Plain extraction can scramble formulae; normalized demand labels are analyst judgements.'}

objectives = []
demands = []
topic_counts = collections.Counter()
for line in OBJECTIVES.strip().splitlines():
    if re.match(r'M[12]\.T\d+\|', line):
        topic, page, title = line.split('|'); page = int(page)
        continue
    anchor, actions = line.split('|')
    topic_counts[topic] += 1
    oid = ident(f'{topic}.{topic_counts[topic]}')
    source = evidence(page, anchor)
    objective = {'objective_id': oid, 'topic_id': f'8227:2020:{topic.replace(".", ":")}',
                 'topic_title': title, 'source_kind': 'syllabus', 'source': source,
                 'syllabus_text': source['verbatim_extracted_quote'], 'screen': 'in-scope',
                 'review_status': 'author-transcribed; independent source/content review pending'}
    objectives.append(objective)
    for n, action in enumerate(actions.split('/'), 1):
        demands.append({'demand_id': f'{oid}:D{n:02d}', 'objective_id': oid,
                        'learner_action': action, 'source_kind': 'judgement',
                        'basis': 'Decomposition of directly cited syllabus bullet, not an official board demand identifier',
                        'source': source, 'screen': 'in-scope',
                        'direct_vs_prerequisite': 'direct candidate; actual assessed role determined per question part',
                        'review_status': 'proposed'})
assert len(objectives) == 60 and len(topic_counts) == 15
objective_ids = {o['objective_id'] for o in objectives}

families = {}
for line in FAMILIES.strip().splitlines():
    n, title, short = line.split('|'); oid = ident(short)
    assert oid in objective_ids
    families[n] = {'pattern_id': f'8227:PAT-{n}', 'title': title,
                   'primary_objective_id': oid, 'question_parts': [],
                   'distinction': title + '; different values alone do not justify another pattern.',
                   'recipe_status': 'not a recipe count; branch/grouping review pending',
                   'marking_status': 'use linked official excerpts where present; missing rules stay on source hold'}

REPORT_STARTS = {2021: (231,236,242), 2022:(301,307,316), 2023:(321,330,339),
                 2024:(325,335,343), 2025:(345,355,364)}
MEMO_PAGES = {
    '2021-2': {1:[237],3:[238]},
    '2023-2': {1:[331],2:[331],3:[333],4:[335],5:[336],6:[337],7:[338],8:[339],9:[339]},
    '2024-2': {1:[336],2:[336],3:[337],4:[337],5:[338],6:[339],7:[340],8:[341],9:[342],10:[342],11:[343]},
}
VISUAL = {'2021-1-Q12:c','2021-2-Q4:a','2022-1-Q6:c','2023-2-Q6:c',
          '2024-2-Q8:a','2024-2-Q11:a','2025-1-Q4:a','2025-1-Q4:b',
          '2025-2-Q4:b','2025-2-Q11:a','2025-2-Q12:a'}
EXPLICIT_DEPENDENCIES = {
    '2021-1-Q1': [('a','b')], '2021-1-Q3':[('a','b')],
    '2021-1-Q4':[('a','b')], '2021-1-Q6':[('a','b')],
    '2021-2-Q5':[('a','b')], '2021-2-Q8':[('b','c.i'),('c.i','c.ii')],
    '2021-2-Q10':[('a','b')], '2021-2-Q11':[('a','b')],
    '2022-1-Q8':[('a','b')], '2022-1-Q12':[('a','b')],
    '2022-2-Q3':[('a','b'),('a','c')], '2022-2-Q5':[('a','b'),('a','c')],
    '2022-2-Q7':[('a','b')], '2023-2-Q1':[('a','b'),('b','c')],
    '2023-2-Q3':[('b.i','b.ii'),('b.i','b.iii')],
    '2023-2-Q6':[('a','b'),('c','d')], '2023-2-Q7':[('a','b'),('a','c')],
    '2024-2-Q4':[('a','b')], '2024-2-Q5':[('a','b'),('a','c')],
    '2024-2-Q6':[('a','b')], '2024-2-Q7':[('a','b'),('b','c')],
    '2024-2-Q11':[('a','c'),('b','c')],
    '2025-1-Q4':[('a','c'),('b','c')], '2025-1-Q7':[('a','b'),('b','c'),('b','d')],
    '2025-1-Q8':[('a','b')], '2025-1-Q9':[('a','b'),('b','c')],
    '2025-1-Q11':[('a','b'),('b','c')], '2025-2-Q6':[('a','b')],
    '2025-2-Q7':[('a','b')], '2025-2-Q9':[('a','b')],
    '2025-2-Q10':[('a','b')], '2025-2-Q12':[('a','b'),('b','c'),('b','d')],
}
questions = []
totals = collections.Counter()
paper_cache = {}
pdf_cache = {}
for line in QUESTIONS.strip().splitlines():
    key, page_list, summary, encoded = line.split('|')
    paper, q = key.split(); year, component = map(int, paper.split('-')); q = int(q)
    qid = f'{paper}-Q{q}'
    sourcefile = A / 'extracted' / f'{year}-P{component}.json'
    data = paper_cache.setdefault(str(sourcefile), json.loads(sourcefile.read_text()))
    actual_source = ROOT / data['source']
    assert hashlib.sha256(actual_source.read_bytes()).hexdigest()==data['sha256'],('Source changed',actual_source)
    pdf = pdf_cache.setdefault(data['source'],PdfReader(actual_source))
    pages = list(map(int,page_list.split(',')))
    raw = '\n'.join(pdf.pages[n-1].extract_text() for n in pages)
    observed_marks = list(map(int,re.findall(r'\[\s*(\d+)\s*\]',raw)))
    memo_pages = MEMO_PAGES.get(paper,{}).get(q,[])
    report = json.loads((A/'extracted'/f'report-{year}.json').read_text())
    lo, split, hi = REPORT_STARTS[year]
    section = (lo, split-1) if component == 1 else (split, hi)
    report_hits = [x['pdf_page'] for x in report['pages'] if section[0]<=x['pdf_page']<=section[1]
                   and re.search(rf'Question\s+{q}(?!\d)',x['text'])]
    parts=[]
    for encoded_part in encoded.split(';'):
        label, fnos, mark = encoded_part.split(':'); fids = fnos.split('+'); mark=int(mark)
        part_id=f'8227:EXAM:{year}:P{component}:Q{q}:{label}'
        oids=list(dict.fromkeys(families[f]['primary_objective_id'] for f in fids))
        parts.append({'part_id':part_id,'source_label':None if label=='answer' else label,
                      'paper_locator':{'path':data['source'],'sha256':data['sha256'],
                                       'question':q,'part':label,'question_pdf_pages':pages},
                      'primary_objective_id':oids[0],'other_directly_assessed_objective_ids':oids[1:],
                      'prerequisite_context_note':'NSSCO prior knowledge prescribed by syllabus; its incidental use does not earn direct coverage.',
                      'objective_mapping_status':'analyst judgement; source/content review pending',
                      'pattern_ids':[families[f]['pattern_id'] for f in fids],
                      'printed_marks':mark,'mark_source':'question-paper tariff, not a generated memo',
                      'blooms_level':None,'bloom_status':'unclassified; reviewed criterion-linked classification deferred',
                      'response_requirement':'visual sketch plus reasoning' if f'{qid}:{label}' in VISUAL else 'inspect exact prompt; symbolic/numerical/reasoning evidence as requested',
                      'capability_hold':'CAP-8227-02' if f'{qid}:{label}' in VISUAL else None,
                      'marking_excerpt_pdf_pages':memo_pages,
                      'marking_rule_status':'official report contains linked award excerpt; transcribe/reconcile before recipe design' if memo_pages else 'no complete award schedule verified; source hold'})
        for f in fids:families[f]['question_parts'].append(part_id)
    # Reconcile curated mark sequence to literal paper brackets, including shared pages.
    sequence=[x['printed_marks'] for x in parts]
    assert any(observed_marks[i:i+len(sequence)]==sequence for i in range(len(observed_marks)-len(sequence)+1)),(qid,sequence,observed_marks)
    totals[paper]+=sum(sequence)
    labels={x['source_label'] or 'answer' for x in parts}
    dependencies=[{'from_part':a,'to_part':b,'basis':'analyst reading of connected question; award follow-through is separate'}
                  for a,b in EXPLICIT_DEPENDENCIES.get(qid,[])]
    assert all(x['from_part'] in labels and x['to_part'] in labels for x in dependencies)
    questions.append({'question_id':f'8227:EXAM:{year}:P{component}:Q{q}',
                      'year':year,'paper':component,'question':q,'pdf_pages':pages,
                      'pattern_summary':summary,'source_kind':'corpus',
                      'question_source_path':data['source'],'parts':parts,
                      'reported_question_total':sum(sequence),'dependencies':dependencies,
                      'dependency_scope':'Only explicitly annotated edges; other shared-given/part dependencies remain to review.',
                      'report_source':report['source'],'report_question_heading_pages':report_hits,
                      'report_section_pdf_pages':list(section),'marking_excerpt_pdf_pages':memo_pages,
                      'source_hold':'SRC-8227-DOMAIN-2022-P1-Q13' if qid=='2022-1-Q13' else None,
                      'inspection':'all question text structurally read; diagrams and scrambled formulae require targeted visual review; not all independently solved'})
assert len(questions)==119 and len(totals)==10
assert all(v==75 for v in totals.values()),dict(totals)

# One source-backed record for each assessment value; page text retains exact tables.
def fact(value,page):
    return {'value':value,'source_kind':'syllabus','pdf_page':page,
            'source_sha256':HASH,'verbatim_page_text':PAGES[page-1]}
facts={'schema_version':'workbench-source-transcription-8227-v1',
       'document_path':str(SYLLABUS.relative_to(ROOT)), 'document_sha256':HASH,
       'qualification':fact('NSSCAS Mathematics 8227',1),'grade':fact(12,1),
       'edition':fact('December 2020',2),'implementation_year':fact(2021,1),
       'first_examination_year':fact(2021,1),
       'assessment_area':fact('technique with application',17),
       'per_ability_weights':fact('not separately stated',17),
       'papers':[{'id':fact(n,18),'marks':fact(75,18),'duration_minutes':fact(120,18),'weight_percent':fact(50,18)} for n in [1,2]],
       'command_word_table':{'value':None,'status':'no standalone command-word table found in complete extracted syllabus; author finding, not a transcribed official list',
                             'source_kind':'judgement','inspected_pdf_pages':list(range(1,len(PAGES)+1))},
       'assessment_abilities':[], 'review_status':'author source transcription; owner verification and independent review pending'}
ability_text = '\n' + PAGES[16][PAGES[16].index('1. organise'):]
for m in re.finditer(r'\n(\d+)\.\s+(.+?)(?=\n\d+\.\s|\nThe assessment objectives)',ability_text,re.S):
    facts['assessment_abilities'].append({'id':f'8227:2020:ABILITY:{int(m[1]):02d}',
        'verbatim_quote':m[0].strip(),'source_kind':'syllabus','pdf_page':17})
assert len(facts['assessment_abilities'])==11
write(WS/'curriculum/syllabus-facts.json',facts)
write(WS/'curriculum/objective_registry.json',{'schema_version':'workbench-analysis-8227-v1','source_sha256':HASH,'objectives':objectives})
limits=[
    ('LIMIT01','M1.T2.1','Greatest binomial term and coefficient properties are not required.'),
    ('LIMIT02','M1.T6.6','General trigonometric solution forms are not included.'),
    ('LIMIT03','M1.T8.1','Differentiation from first principles is not required.'),
    ('LIMIT04','M1.T8.2','Product and quotient rules are not required in Mathematics 1; they ARE required in Mathematics 2.'),
    ('LIMIT05','M2.T1.3','Polynomial dividend degree at most four; divisor linear or quadratic.'),
    ('LIMIT06','M2.T2.1','Change of logarithm base is excluded.'),
    ('LIMIT07','M2.T5.1','General integration by substitution is not required.'),
    ('LIMIT08','M2.T6.4','Formal convergence condition is not included; possible failure to converge must be understood.')]
write(WS/'curriculum/syllabus-exclusions.json',{'limits':[{'limit_id':'8227:'+n,'objective_id':ident(o),
      'normalized_rule':s,'source_kind':'judgement-normalized-from-syllabus','source':next(x['source'] for x in objectives if x['objective_id']==ident(o))} for n,o,s in limits],
      'prior_knowledge':{'role':'prerequisite, not automatic direct AS coverage','pdf_pages':[8,14],
                        'verbatim_quote':'Knowledge of the content of NSSCO Mathematics is prescribed, and learners may be required to demonstrate such knowledge in answering questions.'}})
write(A/'demand-registry.json',{'schema_version':1,'demands':demands,'limitations':'Analysis decomposition; no recipe, implementation or curriculum-coverage acceptance.'})
write(A/'question-analysis.json',{'schema_version':1,'questions':questions})

coverage=[]
for o in objectives:
    fs=[f for f in families.values() if f['primary_objective_id']==o['objective_id']]
    links=sorted({p for f in fs for p in f['question_parts']})
    coverage.append({'objective_id':o['objective_id'],'pattern_ids':[f['pattern_id'] for f in fs],
                     'observed_part_links':links,'status':'observed candidate links; not full-demand coverage' if links else 'syllabus-required; no direct link established by this pass',
                     'recipe_ids':[],'coverage_certified':False})
write(A/'coverage-matrix.json',{'schema_version':1,'rows':coverage})
textbook_samples=json.loads((A/'textbook-samples.json').read_text())['samples'] if (A/'textbook-samples.json').exists() else []
for f in families.values():
    f['textbook_sample_ids']=[x['sample_id'] for x in textbook_samples if f['pattern_id'] in x['related_pattern_ids']]
    f['evidence_labels']=(['examination-observed'] if f['question_parts'] else ['syllabus-derived']) + (['textbook-derived'] if f['textbook_sample_ids'] else [])
write(A/'problem-patterns.json',{'schema_version':1,'patterns':list(families.values()),
                              'scope':'62 provisional families, not recipe counts; inspect structural branches and exact evidence before planning'})

lines=['# Demand registry for Mathematics 8227','',
       'Generated from `tools/analysis_inputs.py` and the exact syllabus source. Each decomposition is analyst judgement. No recipe authoring approval.',
       '', '| Demand ID | Learner action | Syllabus PDF / printed page |','|---|---|---|']
for d in demands:lines.append(f'| {d["demand_id"]} | {d["learner_action"]} | {d["source"]["pdf_page"]} / {d["source"]["printed_page"]} |')
(A/'demand-registry.md').write_text('\n'.join(lines)+'\n')
lines=['# Provisional pattern selections for Mathematics 8227','',
       'Generated analysis, not accepted recipes or work orders. Include means retain for design review. Source and capability holds still prevent affected authoring/release.',
       '', '| Pattern | Reasoning/evidence distinction | Primary objective | Observed part links | Disposition and limits |','|---|---|---|---|---|']
for f in families.values():
    status='include for analysis/design review; marking rules need linked source review' if f['question_parts'] else ('include for design review: syllabus/textbook-derived, not examination-observed; proposed marking requires review' if f['textbook_sample_ids'] else 'hold: syllabus-derived candidate; no observed part link established')
    lines.append(f'| {f["pattern_id"]} | {f["title"]} | {f["primary_objective_id"]} | {len(f["question_parts"])} | {status} |')
(A/'selection-table.md').write_text('\n'.join(lines)+'\n')
lines=['# Objective coverage matrix for Mathematics 8227','',
       'Part associations do not prove all demands/representations of an objective are covered. No recipes yet exist. Full direct/prerequisite mapping requires independent review.',
       '', '| Objective | Syllabus PDF page | Analyst demand count | Observed links | Coverage state |','|---|---|---|---|---|']
for o,c in zip(objectives,coverage):
    lines.append(f'| {o["objective_id"]} | {o["source"]["pdf_page"]} | {sum(d["objective_id"]==o["objective_id"] for d in demands)} | {len(c["observed_part_links"])} | {c["status"]} |')
(A/'coverage-matrix.md').write_text('\n'.join(lines)+'\n')
lines=['# Examination question index for Mathematics 8227','',
       'First author structural reading. Part/objective mappings and branches require review; see question-analysis.json for exact identifiers and source hashes.',
       '', '| Source question | PDF pages | Connected demand | Parts and printed marks | Official report award-excerpt pages |','|---|---|---|---|---|']
for q in questions:
    labels=', '.join(f'{p["source_label"] or "unlabelled"}: {p["printed_marks"]}' for p in q['parts'])
    lines.append(f'| {q["year"]} P{q["paper"]} Q{q["question"]} | {q["pdf_pages"]} | {q["pattern_summary"]} | {labels} | {q["marking_excerpt_pdf_pages"] or "not verified"} |')
(A/'question-index.md').write_text('\n'.join(lines)+'\n')
dispositions=[]
for d in demands:
    c=next(x for x in coverage if x['objective_id']==d['objective_id'])
    dispositions.append({'demand_id':d['demand_id'],'objective_id':d['objective_id'],
                         'disposition':'include','meaning':'Retain required syllabus demand in analysis; not permission to author/activate.',
                         'related_pattern_candidates':c['pattern_ids'],
                         'exact_demand_to_part_mapping':'requires finer review; objective association is not full-demand coverage',
                         'source_or_capability_holds':['unverified award rules where no linked memo','visual assessment if a sketch response is required'],
                         'recipe_ids':[]})
write(A/'demand-dispositions.json',{'scope':'All 138 proposed demands retained; none silently dropped or claimed implemented','rows':dispositions})
counts={'objectives':len(objectives),'demands':len(demands),'topics':len(topic_counts),'papers':len(totals),
        'connected_questions':len(questions),'assessed_parts':sum(len(q['parts']) for q in questions),
        'patterns':len(families),'observed_patterns':sum(bool(f['question_parts']) for f in families.values()),
        'paper_mark_totals':dict(totals),'visual_response_parts':len(VISUAL),
        'questions_with_embedded_marking_excerpt':sum(bool(q['marking_excerpt_pdf_pages']) for q in questions),
        'checks':{'literal_syllabus_quotes':'pass','objective_and_pattern_references':'pass','part_mark_sequence_against_paper_brackets':'pass','ten_papers_75_marks_each':'pass'},
        'does_not_certify':['mathematical solutions','complete official marking coverage','all figures visually reviewed','independent educational acceptance','complete problem universe']}
write(A/'analysis-checks.json',counts)
print(json.dumps(counts,indent=2))
