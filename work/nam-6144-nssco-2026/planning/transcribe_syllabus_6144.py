"""Subject-local Step 2 transcription. Reads only the official 6144 syllabus.

Whitespace is normalised; original page text is retained. Table columns are
isolated before transcribing learning outcomes. No assessment fact comes from
another subject or from a question paper. Run --verify to re-open the PDF.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
PDF = REPO / 'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_6144_Business_Studies_syllabus_June_2020_final.pdf'
FACTS = WS / 'curriculum/syllabus-facts.json'


def norm(text):
    return ' '.join(text.split())


def citation(page, quote, section, **extra):
    return {'page': page, 'printed_page': page - 4 if 5 <= page <= 34 else None,
            'section': section, 'verbatim': norm(quote), 'provenance': 'syllabus', **extra}


def columns(text):
    lines = text.splitlines()
    header = next(line for line in lines if 'GENERAL OBJECTIVES' in line and 'SPECIFIC OBJECTIVES' in line)
    a, b = header.index('GENERAL OBJECTIVES'), header.index('SPECIFIC OBJECTIVES')
    return a, b


def build(pages):
    def cited(page, quote, section, **extra):
        q = norm(quote)
        assert q in norm(pages[page - 1]), (page, q)
        return citation(page, quote, section, **extra)

    # Read numbers directly from the specification-grid rows, in printed column order.
    rows = []
    for line in pages[23].splitlines():
        m = re.match(r'^\s*([ABCD])\s+(.+?)\s{2,}(\d+)\s+(\d+)\s+(\d+)%\s*$', line)
        if m:
            code, name, p1, p2, overall = m.groups()
            rows.append({'code': code, 'name': norm(name), 'p1': int(p1), 'p2': int(p2),
                         'overall': int(overall), 'line': line})
    assert len(rows) == 4
    aos = []
    ao_page = pages[22]
    for row in rows:
        code, name = row['code'], row['name']
        start = re.search(r'^\s*' + code + r'\s+' + re.escape(name) + r'\s*$', ao_page, re.M)
        # The first occurrence is the summary list; the second is the full definition.
        starts = list(re.finditer(r'^\s*' + code + r'\s+' + re.escape(name) + r'\s*$', ao_page, re.M))
        assert len(starts) == 2
        body = ao_page[starts[1].end():].split('Questions', 1)[0]
        definitions = []
        for match in re.finditer(r'^\s*([12])\.\s+(.+?)(?=^\s*[12]\.\s+|\Z)', body, re.M | re.S):
            text = match.group(2).strip()
            # AO A has a concluding explanatory paragraph outside its two numbered outcomes.
            text = text.split('The curriculum objectives', 1)[0].strip()
            definitions.append({'number': int(match.group(1)), 'text': norm(text),
                                'source': cited(23, text, '6 Assessment objectives')})
        assert len(definitions) == 2
        aos.append({'code': code, 'name': name, 'can_do': [x['text'] for x in definitions],
                    'definitions': definitions,
                    'source': cited(23, f'{code} {name}', '6 Assessment objectives'),
                    'verbatim': f'{code} {name}',
                    'qualification_weight_percent': row['overall'],
                    'weight_source': cited(24, row['line'], '8 Specification grid')})

    per_paper = {f'P{n}': {r['code']: r[f'p{n}'] for r in rows} for n in [1, 2]}
    paper_records = []
    assessment = pages[23].split('8.', 1)[0]
    for n in [1, 2]:
        block = re.split(r'^Paper ' + str(n) + r'\s*$', assessment, maxsplit=1, flags=re.M)[1]
        if n == 1:
            block = block.split('Paper 2', 1)[0]
        m = re.search(r'Written\s+(\d+) hours (\d+) minutes\s+(\d+) marks\s+Weighting:\s*(\d+)\s*%', block)
        assert m
        hours, minutes, marks, weight = map(int, m.groups())
        description = norm(block[m.end():])
        assert 'five' in description and '20 marks each' in description
        paper_records.append({'paper': str(n), 'name': f'Paper {n}',
                              'duration_minutes': hours * 60 + minutes, 'marks': marks,
                              'weight_percent': weight, 'ao_split': per_paper[f'P{n}'],
                              'description': description, 'questions': 5, 'marks_per_question': 20,
                              'source': cited(24, m.group(), '7 Scheme of assessment'),
                              'structure_source': cited(24, description, '7 Scheme of assessment'),
                              'weight_provenance': 'syllabus: PDF page 24, printed page 20',
                              'verbatim': norm(m.group())})

    # Read every command-word entry. Explain deliberately occurs twice.
    commands, current, ao = [], None, None
    for page in [27, 28]:
        for line in pages[page - 1].splitlines():
            if 'NSSCO Business Studies Syllabus' in line or re.fullmatch(r'\s*\d+\s*', line):
                continue
            if 'Assessment objective ' in line:
                ao = re.search(r'Assessment objective ([ABCD]):', line).group(1)
                current = None
                continue
            if ao is None or not line.strip():
                continue
            m = re.match(r'^([A-Z][a-z]+(?: examples)?)\s{2,}(.+)$', line)
            if m:
                current = {'word': m.group(1).lower(), 'syllabus_assessment_objective': ao,
                           'meaning': m.group(2).strip(), 'quote': line.strip(), 'page': page}
                commands.append(current)
            elif current is not None and line.startswith(' '):
                current['meaning'] += ' ' + line.strip()
                current['quote'] += ' ' + line.strip()
    for command in commands:
        page = command.pop('page')
        quote = command.pop('quote')
        command['meaning'] = norm(command['meaning'])
        command['source'] = cited(page, quote, '10 Glossary of command words')
        command['verbatim'] = norm(quote)
        command['use_in_prompts'] = None
        command['prompt_use_note'] = 'Undecided until subject-specific corpus analysis; glossary membership alone does not permit use.'
    assert len(commands) == 25 and len({x['word'] for x in commands}) == 24

    topics, current_topic = {}, None
    for page in range(8, 23):
        a, b = columns(pages[page - 1])
        lines = pages[page - 1].splitlines()
        start = next(i for i, line in enumerate(lines) if 'Learners should be able to:' in line) + 1
        groups = []
        group = None
        for line in lines[start:]:
            if 'NSSCO Business Studies Syllabus' in line:
                break
            left = line[:a].strip()
            m = re.match(r'^(\d\.\d)\s+(.+)', left)
            if m:
                group = {'topic_id': m.group(1), 'title_lines': [m.group(2)], 'general': [], 'specific': []}
                groups.append(group)
            if group is None:
                continue
            if left and not m:
                group['title_lines'].append(left)
            group['general'].append(line[a:b].strip())
            group['specific'].append(line[b:].strip())
        for group in groups:
            topic_id = group['topic_id']
            title = norm(' '.join(group['title_lines']))
            title = re.sub(r'\s*\(continued\)', '', title)
            topic = topics.setdefault(topic_id, {'topic_id': topic_id, 'title': title, 'theme': topic_id[0],
                                                'title_sources': [], 'general_objectives': [], 'specific_objectives': []})
            topic['title_sources'].append(citation(page, ' '.join(group['title_lines']), '5 Learning content', column='topic'))
            for field, column in [('general_objectives', 'general'), ('specific_objectives', 'specific')]:
                chunks = re.split(r'\uf0b7', ' '.join(group[column]))
                assert not chunks[0].strip(), (page, topic_id, field, chunks[0])
                for chunk in chunks[1:]:
                    value = norm(chunk)
                    if value:
                        topic[field].append({'text': value, 'source': citation(page, value, '5 Learning content', column=column)})
    assert len(topics) == 22
    theme_records = []
    for page in range(8, 23):
        line = next(x for x in pages[page - 1].splitlines() if x.startswith('THEME '))
        m = re.match(r'THEME (\d):\s*(.+)', line)
        if m and not any(t['theme_id'] == m.group(1) for t in theme_records):
            theme_records.append({'theme_id': m.group(1), 'title': norm(m.group(2)),
                                  'source': cited(page, line, '5 Learning content')})

    scope = []
    for topic in topics.values():
        for objective in topic['specific_objectives']:
            if re.search(r'not expected|entirely descriptive|descriptively|general terms|briefly|general idea|simple ', objective['text'], re.I):
                scope.append({'topic_id': topic['topic_id'], 'kind': 'depth_or_format_limit', **objective})
    scope.extend([
        {'kind': 'application_requirement', 'text': norm('In the specific objectives in the learning content the words “…in particular circumstances” would expect application of the knowledge to circumstances given in a case study and not a general discussion. The applications are however not limited to these specific objectives.'),
         'source': cited(7, 'In the specific objectives in the learning content the words “…in particular circumstances” would expect application of the knowledge to circumstances given in a case study and not a general discussion. The applications are however not limited to these specific objectives.', '5 Learning content')},
        {'kind': 'calculation_convention', 'text': 'Calculate ratios using year-end balances where appropriate, unless the question specifies the use of average figures.',
         'source': cited(34, 'Calculate ratios using year-end balances where appropriate, unless the question specifies the use of average figures.', 'Annexe A')},
        {'kind': 'calculation_convention', 'text': 'Calculate ratios to two decimal places.',
         'source': cited(34, 'Calculate ratios to two decimal places.', 'Annexe A')},
    ])
    return {
        'facts_id': 'SYLFACTS-NAM-6144-NSSCO', 'generated_by': str(Path(__file__).relative_to(REPO)),
        'authority': 'NIED NSSCO Business Studies 6144 syllabus; publication 2019; filename June 2020 final',
        'source_document': str(PDF.relative_to(REPO)), 'source_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'pages_in_document': len(pages), 'provenance': 'syllabus',
        'quote_policy': 'Whitespace normalised only. Column citations are verified within the named layout column on the cited PDF page. PDF page is 1-based; printed page is separate.',
        'route': 'NSSCO Ordinary Level, Grades 10–11',
        'identity_sources': [cited(1, 'SYLLABUS CODE: 6144', 'Cover'), cited(1, 'GRADES 1 0 - 11', 'Cover', extraction_note='Layout extractor spaces the digits of 10; ordinary extraction reads GRADES 10 - 11.'),
                             cited(1, 'FOR IMPLEMENTATION IN 2019 FOR FIRST EXAMINATION IN 2020', 'Cover'),
                             cited(2, 'Publication date: 2019', 'Publication')],
        'validity_note': '2026 is the learner examination target, not a syllabus expiry/start date. No explicit 2026 validity statement or expiry has been transcribed.',
        'assessment_objectives': aos,
        'ao_weights': {'qualification_percent': {r['code']: r['overall'] for r in rows},
                       'per_component_marks': per_paper,
                       'per_component_percent': per_paper,
                       'percent_note': 'Each paper is explicitly 100 marks; its AO marks are numerically equal to within-paper percentages. Printed grid labels are marks.',
                       'source': {'qualification': {'page': 24, 'printed_page': 20, 'rows': [norm(r['line']) for r in rows]},
                                  'per_component': {'page': 24, 'printed_page': 20, 'rows': [norm(r['line']) for r in rows]}}},
        'weighting_caveat': cited(24, 'The assessment objectives are weighted to give an indication of their relative importance. They are not intended to provide a precise statement of the number of marks allocated to particular assessment objectives.', '8 Specification grid'),
        'papers': paper_records, 'command_words': commands,
        'command_word_table': {'pages': [27, 28], 'printed_pages': [23, 24], 'entry_count': len(commands),
                               'unique_word_count': len({x['word'] for x in commands}),
                               'note': 'Explain has distinct B and C entries. Determine occurs in section 6 examples but not section 10 glossary; it is not silently added to the glossary.'},
        'themes': theme_records, 'content_outline': list(topics.values()), 'scope_limits_and_requirements': scope,
        'annex_a': cited(34, pages[33], 'Annexe A Summary of commonly used ratios'),
        'unknowns': ['Exact per-question command-word tariffs are not stated in the glossary; await corpus analysis.',
                     'No future prompt-use verdicts or corpus frequencies are inferred in this file.'],
    }


def verify(facts, pages):
    checked = 0
    def walk(value):
        nonlocal checked
        if isinstance(value, dict):
            if 'page' in value and 'verbatim' in value:
                page, quote = value['page'], norm(value['verbatim'])
                text = pages[page - 1]
                if value.get('column'):
                    a, b = columns(text)
                    slices = {'topic': (0, a), 'general': (a, b), 'specific': (b, None)}
                    lo, hi = slices[value['column']]
                    text = '\n'.join(line[lo:hi] for line in text.splitlines())
                assert quote and quote in norm(text), (page, value.get('column'), quote)
                checked += 1
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(facts)
    rebuilt = build(pages)
    assert facts == rebuilt, 'Persisted facts differ from fresh source transcription'
    assert sum(facts['ao_weights']['qualification_percent'].values()) == 100
    for paper in facts['papers']:
        assert sum(paper['ao_split'].values()) == paper['marks'] == 100
        assert paper['questions'] * paper['marks_per_question'] == paper['marks']
    assert sum(p['weight_percent'] for p in facts['papers']) == 100
    return {'status': 'pass', 'source_sha256': facts['source_sha256'], 'verified_citations': checked,
            'assessment_objectives': len(facts['assessment_objectives']), 'papers': len(facts['papers']),
            'themes': len(facts['themes']), 'topics': len(facts['content_outline']),
            'specific_objective_bullets': sum(len(t['specific_objectives']) for t in facts['content_outline']),
            'command_word_entries': len(facts['command_words']), 'unique_command_words': len({x['word'] for x in facts['command_words']}),
            'method': 'Fresh pypdf layout extraction; every quote checked on cited PDF page and column; all structured facts regenerated and compared; grid and question arithmetic reconciled.',
            'visual_review': 'Codex inspected rendered PDF pages 23, 24, 27 and 28 (printed 19, 20, 23 and 24). Human assessment-table checkpoint remains pending.'}


def write_brief(facts):
    lines = ['# Syllabus brief — NSSCO Business Studies 6144', '',
             'Owner: Vitalis. Step 2 completed 27 October 2026; human assessment-table confirmation pending.', '',
             'Source: NIED 2019 syllabus, filename June 2020 final; implementation 2019, first examination 2020. The 2026 date is our learner examination target; the document does not state a 2026 validity window. Page references below give printed page first, then PDF page.', '',
             '## Papers — printed p.20 / PDF p.24', '',
             '| Paper | Duration | Marks | Weight | Structure |',
             '|---|---|---:|---:|---|']
    for paper in facts['papers']:
        hours, mins = divmod(paper['duration_minutes'], 60)
        structure = 'Five compulsory questions, 20 marks each'
        if paper['paper'] == '2':
            structure += ', arising from a business case study'
        lines.append(f"| {paper['paper']} | {hours} h {mins} min | {paper['marks']} | {paper['weight_percent']}% | {structure} |")
    lines += ['', 'All learners sit both papers.', '',
              '## Assessment objectives — definitions p.19 / PDF p.23; grid p.20 / PDF p.24', '',
              '| Objective | Paper 1 marks | Paper 2 marks | Overall weight |',
              '|---|---:|---:|---:|']
    for ao in facts['assessment_objectives']:
        code = ao['code']
        lines.append(f"| {code}: {ao['name']} | {facts['ao_weights']['per_component_marks']['P1'][code]} | {facts['ao_weights']['per_component_marks']['P2'][code]} | {ao['qualification_weight_percent']}% |")
    lines += ['', 'The grid indicates relative importance; the syllabus explicitly says it is not a precise statement of the marks allocated to each objective in each examination.', '',
              '## Content — printed pp.3–18 / PDF pp.7–22', '']
    for theme in facts['themes']:
        topics = [t for t in facts['content_outline'] if t['theme'] == theme['theme_id']]
        lines.append(f"- Theme {theme['theme_id']}: " + '; '.join(f"{t['topic_id']} {t['title']}" for t in topics) + '.')
    count = sum(len(t['specific_objectives']) for t in facts['content_outline'])
    lines += ['', f"Transcribed {len(facts['themes'])} themes, {len(facts['content_outline'])} topics and {count} specific-objective bullets. These are syllabus bullets, not a decomposed objective registry or an item budget.", '',
              '## Commands, limits and calculation conventions', '',
              f"The glossary, printed pp.23–24 / PDF pp.27–28, contains {len(facts['command_words'])} entries for {len(set(c['word'] for c in facts['command_words']))} distinct command expressions. Explain appears under both B and C, with different definitions. Determine appears in section 6 examples but is absent from the glossary; both facts are preserved. Actual prompt eligibility and tariffs await corpus analysis.", '',
              'Detailed ownership legal requirements/procedures are not expected (printed p.6 / PDF p.10). Social cost-benefit analysis is entirely descriptive (p.17 / PDF p.21). Other stated brief/general/simple depth requirements are retained in the facts. Application to a supplied case is expected where particular circumstances are specified (p.3 / PDF p.7).', '',
              'Annexe A (p.30 / PDF p.34): use year-end balances where appropriate unless the question specifies averages; calculate ratios to two decimal places. Topic 2.4 calls inventory turnover a liquidity ratio, while Annexe A groups it under efficiency: retain and flag the source discrepancy rather than silently rewriting it.', '',
              '## Verification and next checkpoint', '',
              'The subject-local transcriber reopens the original PDF, verifies every citation on its page/column, regenerates the structured facts and reconciles grid/question totals. Codex visually inspected the assessment and glossary pages. These checks are transcription verification, not subject-resource publication checks.', '',
              'Vitalis: open printed pp.19–20 (PDF pp.23–24), check the objective names, paper structures and weighting grid, then confirm. Corpus analysis begins after that checkpoint; no notes, flashcards, plan or work orders have been authored.', '']
    out = REPO / 'operations/analysis/6144-nssco-business-studies-syllabus-brief.md'
    out.write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    pages = [p.extract_text(extraction_mode='layout') or '' for p in PdfReader(PDF).pages]
    if args.verify:
        facts = json.loads(FACTS.read_text())
    else:
        facts = build(pages)
        FACTS.parent.mkdir(exist_ok=True)
        FACTS.write_text(json.dumps(facts, ensure_ascii=False, indent=2) + '\n')
        (WS / 'planning/syllabus-layout.txt').write_text('\n'.join(f'\n--- PDF PAGE {i} ---\n{text}' for i, text in enumerate(pages, 1)))
        write_brief(facts)
    report = verify(facts, pages)
    (WS / 'planning/syllabus-verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
