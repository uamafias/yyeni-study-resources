"""Reproducible step-2 transcription; reads this subject's syllabus only."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
PDF = ROOT / 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Economics_Syllabus.pdf'


def norm(text):
    return re.sub(r'\s+', ' ', text).strip()


def extract():
    return subprocess.run(['pdftotext', '-layout', str(PDF), '-'],
                          capture_output=True, check=True, text=True).stdout.split('\f')[:-1]


pages = extract()
citations = []


def cite(page, quote, section=None):
    assert norm(quote) in norm(pages[page - 1]), (page, quote)
    result = {'page': page, 'printed_page': page - 4 if 5 <= page <= 26 else None,
              'verbatim': norm(quote), 'provenance': 'syllabus'}
    if section:
        result['section'] = section
    citations.append(result)
    return result


def fact(value, page, quote):
    return {'value': value, 'source': cite(page, quote)}


ao_page = pages[16]
ao_matches = list(re.finditer(r'^([ABC]) {2,}([^\n]+)$', ao_page, re.M))
assert len(ao_matches) == 3
aos = []
for i, m in enumerate(ao_matches):
    block = ao_page[m.end():ao_matches[i+1].start() if i+1 < 3 else len(ao_page)]
    numbered = re.findall(r'^\s*\d\.\s+(.*?)(?=^\s*\d\.\s|\n\s*\(Questions)', block, re.M | re.S)
    aos.append({'code': m[1], 'name': norm(m[2]), 'can_do': [norm(x) for x in numbered],
                'source': cite(17, m[0], '6 Assessment objectives'),
                'verbatim': norm(m[0]), 'definition_source': cite(17, block.split('(Questions')[0])})
assert [len(x['can_do']) for x in aos] == [2, 4, 3]

rows = []
splits = {'1': {}, '2': {}}
for line in pages[18].splitlines():
    m = re.match(r'\s*([ABC])\s+(.+?)\s+(\d+)\s*%\s+(\d+)\s*%', line)
    if m:
        rows.append(norm(line))
        for paper, group in [('1', 3), ('2', 4)]:
            splits[paper][m[1]] = int(m[group])
assert all(sum(x.values()) == 100 for x in splits.values())
grid_source = cite(19, '\n'.join(rows), '8 Specification grid')
grid_source['rows'] = rows
derived = {a: sum(splits[p][a] * 0.5 for p in splits) for a in 'ABC'}

papers = []
paper_page = pages[17]
headers = list(re.finditer(r'^Paper ([12])\s+(.*?)\s+(\d+) marks\s+Weighting (\d+)%', paper_page, re.M))
assert len(headers) == 2
for i, m in enumerate(headers):
    number, duration, marks, weight = m.groups()
    nums = [int(x) for x in re.findall(r'\d+', duration)]
    minutes = nums[0] * 60 + (nums[1] if len(nums) > 1 else 0)
    description = paper_page[m.end():headers[i+1].start() if i == 0 else paper_page.index('NSSCO Economics syllabus')].strip()
    papers.append({'paper': number, 'name': f'Paper {number}', 'marks': int(marks),
                   'duration_minutes': minutes, 'duration_verbatim': duration,
                   'weight_percent': int(weight), 'share_of_route': int(weight)/100,
                   'weight_provenance': 'syllabus', 'ao_split': splits[number],
                   'source': cite(18, m[0], '7 Scheme of assessment'),
                   'verbatim': norm(m[0]), 'description': norm(description),
                   'description_source': cite(18, description), 'ao_split_source': grid_source})

word_page = pages[21]
word_matches = [m for m in re.finditer(r'^([A-Z][a-z]+) {2,}(\S.*)$', word_page, re.M) if m[1] != 'Command']
commands = []
for i, m in enumerate(word_matches):
    end = word_matches[i+1].start() if i+1 < len(word_matches) else word_page.index('NSSCO Economics syllabus')
    quote = word_page[m.start():end].strip()
    commands.append({'word': m[1].lower(), 'meaning': norm(quote[len(m[1]):]),
                     'verbatim': norm(quote), 'source': cite(22, quote, '10 Command words')})
assert len(commands) == 13

# Keep complete source rows, since a table's reading order interleaves columns.
topics = []
themes = []
for pdf_page in range(8, 17):
    page = pages[pdf_page-1]
    lines = page.splitlines()
    theme = next(x.strip() for x in lines if x.startswith('THEME'))
    themes.append({'title': theme, 'source': cite(pdf_page, theme)})
    header = next(x for x in lines if 'SPECIFIC OBJECTIVES' in x)
    general_col, specific_col = header.index('GENERAL OBJECTIVES'), header.index('SPECIFIC OBJECTIVES')
    specific_col = min(m.start() for line in lines for m in re.finditer('', line)
                       if abs(m.start() - specific_col) <= 6)
    starts = [(i, re.match(r'^(\d\.\s?\d)\s+(.*)', line)) for i, line in enumerate(lines)]
    starts = [(i, m) for i, m in starts if m]
    for k, (start, match) in enumerate(starts):
        end = starts[k+1][0] if k+1 < len(starts) else next(i for i in range(start+1, len(lines)) if 'NSSCO Economics syllabus' in lines[i])
        block = lines[start:end]
        topic_edge = min([general_col] + [m.start() for line in block for m in re.finditer('', line)
                                         if m.start() < specific_col - 6])
        left = [line[:topic_edge].strip() for line in block]
        left[0] = re.sub(r'^\d\.\s?\d\s*', '', left[0])
        title = norm(' '.join(x for x in left if x and not x.startswith('*')))
        objectives = []
        for line in block:
            right = line[specific_col:].strip()
            if right.startswith(''):
                objectives.append(right[1:].strip())
            elif right and objectives:
                objectives[-1] += ' ' + right
        topics.append({'topic_id': match[1].replace(' ', ''), 'topic_title': title,
                       'theme': theme, 'specific_objectives': objectives,
                       'source': cite(pdf_page, '\n'.join(block)),
                       'extraction': {'method': 'pdftotext -layout; specific-objective column',
                                      'specific_column_zero_based': specific_col}})
assert len(topics) == 28
assert all(t['specific_objectives'] for t in topics)

limit_hits = []
limit_pattern = re.compile(r'not required|will not be assessed|not expected|not be expected|not necessary|not examin|only|simple|elementary', re.I)
for number, page in enumerate(pages, 1):
    for line in page.splitlines():
        if limit_pattern.search(line):
            limit_hits.append(cite(number, line))

facts = {
    'facts_id': 'SYLFACTS-NAM-6145-NSSCO-2026',
    'generated_by': 'planning/read_syllabus.py', 'generated_date': '2026-11-07',
    'authority': 'NIED Economics Ordinary Level Grades 10–11, publication 2018',
    'source_document': str(PDF.relative_to(ROOT)), 'source_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
    'pages_in_document': len(pages), 'page_convention': 'source.page is the 1-based PDF page; source.printed_page is the printed syllabus page',
    'qualification': {'code': fact('6145', 1, 'SYLLABUS CODE: 6145'),
                      'publication_year': fact(2018, 2, 'Publication date: 2018'),
                      'implementation_year': fact(2019, 1, 'FOR IMPLEMENTATION IN 2019'),
                      'first_examination': fact(2020, 1, 'FOR FIRST EXAMINATION IN 2020'),
                      'final_examination_year': {'value': None, 'note': 'Not stated in this syllabus.'}},
    'assessment_objectives': aos, 'route': 'NSSCO; both papers compulsory',
    'ao_weights': {'qualification_percent': None,
                   'qualification_note': 'Overall AO percentages are not explicitly stated; calculated values are stored separately.',
                   'per_component_percent': splits,
                   'source': {'per_component': grid_source},
                   'derived_qualification_percent': derived,
                   'derived_provenance': 'calculation',
                   'derived_method': 'Each paper AO percentage multiplied by its stated 50% qualification weight, then summed.',
                   'derived_inputs': [grid_source, cite(19, 'Weighting                                               50 %          50 %')]},
    'papers': papers, 'command_words': commands,
    'command_word_table': {'page': 22, 'printed_page': 18, 'count': len(commands),
                           'source': cite(22, '10.      COMMAND WORDS')},
    'command_word_caveat': 'The AO prose on printed page 13 also mentions list, comment, compare, contrast and assess. These are not entries in the printed page 18 command-word table. Actual prompt eligibility requires corpus evidence at step 3.',
    'content_outline': themes, 'topics': topics,
    'scope': {'explicit_content_exclusions': [],
              'note': 'No explicit content exclusions using not required/will not be assessed were found in the learning-content pages. Absence of exclusions does not permit material beyond the specified objectives.',
              'qualifier_scan': limit_hits,
              'glossary_caveat': 'Glossary includes cross elasticity, income elasticity, marginal quantities and diminishing returns. Their glossary presence alone does not establish an independent learning-content objective. Resolve against learning content and corpus before planning.',
              'social_costs_definition': fact('Social costs are equal to the sum of private costs and external costs', 16,
                                            '*Social costs are equal to the sum of private costs and external costs')},
}

# Re-open the PDF independently and verify every citation and grid value.
fresh = extract()
for source in citations:
    assert source['verbatim'] in norm(fresh[source['page']-1]), source
for line in rows:
    m = re.match(r'([ABC]) .+? (\d+) % (\d+) %$', line)
    assert m and all(splits[p][m[1]] == int(m[int(p)+1]) for p in ('1','2'))
assert sum(derived.values()) == 100
out = WS / 'curriculum/syllabus-facts.json'
out.write_text(json.dumps(facts, indent=2, ensure_ascii=False) + '\n')
(WS / 'planning/syllabus-layout.txt').write_text('\f'.join(pages))
report = {'result': 'PASS', 'citations_verified': len(citations), 'assessment_objectives': len(aos),
          'command_words': len(commands), 'themes': len(themes), 'topics': len(topics),
          'specific_objectives': sum(len(t['specific_objectives']) for t in topics),
          'checks': ['Every quotation re-found on its cited PDF page', 'Each paper AO column sums to 100%',
                     'Paper AO percentages match independently re-opened grid rows',
                     'Derived overall AO percentages sum to 100%', '28 topics and 13 command words extracted'],
          'human_checkpoint': 'Pending Jeremy verification of printed pages 13–15 (PDF pages 17–19)'}
(WS / 'planning/syllabus-transcription-verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
for topic in topics:
    print(topic['topic_id'], topic['topic_title'], len(topic['specific_objectives']))
