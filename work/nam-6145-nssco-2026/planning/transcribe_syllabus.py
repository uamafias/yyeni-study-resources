"""6145 step 2: transcribe this syllabus; never read assessment papers here."""
import hashlib
import json
import re
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
SOURCE = Path('Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Economics_Syllabus.pdf')
reader = PdfReader(ROOT / SOURCE)
pages = [p.extract_text() for p in reader.pages]
with pdfplumber.open(ROOT / SOURCE) as verification_pdf:
    alternate_pages = [p.extract_text() or '' for p in verification_pdf.pages]


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def cite(page, quote, section):
    quote = norm(quote)
    assert any(quote in norm(text) for text in (pages[page - 1], alternate_pages[page - 1])), (page, quote)
    return {'page': page, 'pdf_page': page,
            'printed_page': page - 4 if 5 <= page <= 26 else None,
            'section': section, 'verbatim': quote, 'provenance': 'syllabus'}


def fact(value, page, quote, section):
    return {'value': value, 'source': cite(page, quote, section)}


with pdfplumber.open(ROOT / SOURCE) as pdf:
    grid = pdf.pages[18].extract_tables()[0]
    weights = {'P1': {}, 'P2': {}}
    weight_rows = []
    for row in grid[1:4]:
        code = row[0][0]
        for i, paper in enumerate(('P1', 'P2'), 1):
            weights[paper][code] = int(re.search(r'\d+', row[i]).group())
        weight_rows.append(cite(19, ' '.join(row), '8 Specification grid'))

    themes = []
    for page in range(8, 17):
        table = pdf.pages[page - 1].extract_tables()[0]
        theme_match = re.fullmatch(r'THEME (\d+):\s*(.*)', norm(table[0][0]))
        assert theme_match
        theme = {'theme_id': theme_match[1], 'title': theme_match[2],
                 'source': cite(page, table[0][0], '5 Learning content'), 'topics': []}
        for row in table[2:]:
            title = norm(row[0])
            m = re.fullmatch(r'(\d+\.\s*\d+)\s+(.*)', title)
            assert m, title
            topic = {'topic_id': m[1].replace(' ', ''), 'title': m[2],
                     'source': cite(page, title, '5 Learning content'),
                     'general_objectives': [], 'specific_objectives': []}
            for col, key in [(1, 'general_objectives'), (2, 'specific_objectives')]:
                for bullet in row[col].split('\uf0b7'):
                    if not bullet.strip():
                        continue
                    topic[key].append(cite(page, bullet, '5 Learning content'))
            theme['topics'].append(topic)
        themes.append(theme)

aos = []
ao_text = alternate_pages[16]
for code in 'ABC':
    blocks = list(re.finditer(r'^[ \t]*' + code + r' (.+)$', ao_text, re.M))
    blocks = [m for m in blocks if not m[1].startswith('description of')]
    assert len(blocks) == 2
    heading = blocks[1]
    end = next((b.start() for c in 'ABC' if c > code
                for b in re.finditer(r'^[ \t]*' + c + r' (.+)$', ao_text, re.M)
                if b.start() > heading.end()), len(ao_text))
    block = ao_text[heading.end():end]
    block = block.split('(Questions testing')[0]
    statements = re.findall(r'^\d\. (.*?)(?=^\d\. |\Z)', block, re.M | re.S)
    assert len(statements) == {'A': 2, 'B': 4, 'C': 3}[code]
    aos.append({'code': code, 'name': norm(heading[1]),
                'source': cite(17, heading[0], '6 Assessment objectives'),
                'can_do': [norm(s) for s in statements],
                'statement_sources': [cite(17, s, '6 Assessment objectives') for s in statements],
                'qualification_weight_percent': None,
                'qualification_weight_note': 'No separate qualification-level AO table is stated. See derived weights.'})

command_text = pages[21].split('Command General definition', 1)[1]
command_matches = list(re.finditer(r'^([A-Z][a-z]+) (.*?)(?=^[A-Z][a-z]+ |\Z)',
                                      command_text, re.M | re.S))
commands = [{'word': m[1].lower(), 'meaning': norm(m[2]),
             'source': cite(22, m[0], '10 Command words')}
            for m in command_matches]
assert len(commands) == 13

papers = []
for m in re.finditer(r'Paper ([12]) +(\d hours(?: 30 minutes)?) (80) marks Weighting (50)%', pages[17]):
    number, duration, marks, weight = m.groups()
    papers.append({'paper': number, 'name': 'Paper ' + number,
                   'marks': int(marks), 'duration_minutes': 150 if '30 minutes' in duration else 120,
                   'weight_percent': int(weight), 'ao_split': weights['P' + number],
                   'source': cite(18, m[0], '7 Scheme of assessment'),
                   'ao_split_source': weight_rows})
assert len(papers) == 2
papers[0]['sections'] = [
    {'section': 'A', 'marks': fact(40, 18, 'Short-answer questions.  (40 marks)', '7 Scheme of assessment'),
     'assessment_objectives': fact(['A'], 18, 'Questions in this section will be assessed by Assessment Objective A.', '7 Scheme of assessment')},
    {'section': 'B', 'marks': fact(40, 18, 'Assessment Objective B and C.  (40 marks)', '7 Scheme of assessment'),
     'assessment_objectives': fact(['B', 'C'], 18, 'Questions in this section will be assessed by Assessment Objective B and C.', '7 Scheme of assessment')}]
papers[0]['answer_rule'] = cite(18, 'Learners will be required to answer all questions in both sections.', '7 Scheme of assessment')
papers[1]['sections'] = [
    {'section': 'A', 'marks': fact(20, 18, 'Structured questions (20 marks)', '7 Scheme of assessment'),
     'diagrams': cite(18, 'Questions will include drawing and interpretation of diagrams.', '7 Scheme of assessment')},
    {'section': 'B', 'marks': fact(60, 18, '(60 marks)', '7 Scheme of assessment'),
     'answer_rule': cite(18, 'Learners will be required to answer three structured essay questions (3 x 20 marks) from the five questions available.', '7 Scheme of assessment')}]
papers[1]['answer_rule'] = cite(18, 'Learners will be required to answer all questions in Section A.  In Section B learners will choose three out of five questions available.', '7 Scheme of assessment')

derived = {a: sum(weights['P' + p['paper']][a] * p['weight_percent'] / 100 for p in papers)
           for a in 'ABC'}
assert sum(derived.values()) == 100
for split in weights.values():
    assert sum(split.values()) == 100

scope_quotes = [
    (6, 'Learners beginning this course are not expected to have studied Economics previously.'),
    (10, 'analyse simple market situations with changes in supply and demand'),
    (10, 'perform simple calculations of elasticity and inelasticity of demand and supply'),
    (14, 'define retail price index and show its simple calculation'),
    (14, 'demonstrate the simple application of absolute and comparative advantage in trade'),
    (15, 'describe simple measures and indicators of comparative living standards'),
    (16, '*Social costs are equal to the sum of private costs and external costs'),
]
negative_hits = []
for n, text in enumerate(pages, 1):
    for line in text.splitlines():
        if re.search(r'will not|not required|not expected|not be assessed|excluded|beyond the scope', line, re.I):
            negative_hits.append(cite(n, line, 'Full-document scope search'))

facts = {
    'facts_id': 'SYLFACTS-NAM-6145-NSSCO-2026',
    'generated_by': 'planning/transcribe_syllabus.py', 'generated_on': '2026-10-28',
    'authority': 'NIED NSSCO Economics syllabus 6145, publication 2018',
    'source_document': str(SOURCE), 'source_sha256': hashlib.sha256((ROOT / SOURCE).read_bytes()).hexdigest(),
    'pages_in_document': len(pages),
    'page_convention': 'source.page and source.pdf_page are one-based PDF positions; printed_page is the footer number.',
    'edition': fact(2018, 2, 'Publication date:  2018', 'Publication information'),
    'first_examination_year': fact(2020, 1, 'FOR FIRST EXAMINATION IN 2020', 'Cover'),
    'target_exam_year': {'value': 2026, 'provenance': 'judgement', 'basis': 'User-specified learner examination; user accepted this source set on 2026-10-28. No terminal year stated in this PDF.'},
    'route': 'NSSCO Ordinary Level', 'papers_in_route': ['1', '2'],
    'route_source': cite(18, 'All learners will take Paper 1 and Paper 2.', '7 Scheme of assessment'),
    'assessment_objectives': aos,
    'ao_weights': {
        'qualification_percent': None,
        'qualification_percent_status': 'Not separately stated; do not present the calculated overall percentages as a quoted syllabus table.',
        'per_component_percent': weights,
        'source': {'per_component': {'page': 19, 'printed_page': 15, 'section': '8 Specification grid', 'rows': weight_rows,
                                    'columns_source': cite(19, 'Assessment Objectives Paper 1 Paper 2', '8 Specification grid')}}},
    'derived_qualification_ao_weights': {'values_percent': derived, 'provenance': 'judgement',
        'method': 'Sum of each stated component AO percentage times its stated 50% qualification weighting; calculated, not separately stated.',
        'inputs': weight_rows + [p['source'] for p in papers]},
    'papers': papers, 'command_words': commands,
    'command_word_table': {'page': 22, 'printed_page': 18, 'count': len(commands),
        'source': cite(22, '10. COMMAND WORDS', '10 Command words'),
        'note': 'Complete section 10 table only. AO example verbs on page 13 are a separate list. Corpus use_in_prompts decisions are deferred.'},
    'content_outline': themes,
    'scope': {'stated_constraints_and_depth': [cite(p, q, 'Syllabus scope/depth') for p, q in scope_quotes],
        'explicit_negative_scope_search': negative_hits,
        'content_exclusions': [],
        'exclusion_note': 'No explicit subject-content prohibition found on full reading. Do not invent exclusions from another syllabus. Positive depth constraints and glossary context remain binding.',
        'glossary_note': {'provenance': 'judgement', 'text': 'Read section 11 (printed pages 19–22) alongside the content outline. It includes cross/income elasticity and marginal/normal-profit concepts. Do not label these automatically out of scope using Cambridge IGCSE assumptions; determine the teaching depth from this syllabus and the later 6145 corpus.'}},
    'source_limitations': ['No standalone mark schemes or 2025 material identified locally.',
                           'Annual examiner-report Economics sections have not yet been verified.'],
}

curriculum = WS / 'curriculum'
curriculum.mkdir(exist_ok=True)
(curriculum / 'syllabus-facts.json').write_text(json.dumps(facts, indent=2, ensure_ascii=False) + '\n')
topic_count = sum(len(t['topics']) for t in themes)
objectives = sum(len(t['specific_objectives']) for th in themes for t in th['topics'])
print(json.dumps({'themes': len(themes), 'topics': topic_count, 'specific_objective_bullets': objectives,
                  'command_words': len(commands), 'per_component': weights,
                  'derived_overall': derived, 'all_quotes_checked': True}, indent=2))
