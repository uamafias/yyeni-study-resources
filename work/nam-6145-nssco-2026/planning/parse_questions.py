"""Parse tariff-bearing question parts; require total-mark reconciliation before mining."""
import collections
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
records = []
audit = []
for path in sorted((WS / 'assessment-evidence/extracted').glob('*-P*-raw.txt')):
    year, paper = re.search(r'6145-(\d+)-P(\d)', path.name).groups()
    text = path.read_text()
    if year == '2020' and paper == '1':
        text = text.replace('\n23\n', '\n23 ')
    if year == '2022' and paper == '1':
        text = text.replace('\n25\nANNUAL', '\n25 ANNUAL')
    if year == '2023' and paper == '1':
        text = text.replace('\n22\nCountry A', '\n22 Country A')
    q = 0
    letter = roman = ''
    page = start_page = 0
    buf = []
    context = []
    section = 'A'
    fresh = False
    for line in text.splitlines():
        pm = re.match(r'=== PDF PAGE (\d+) ===', line)
        if pm:
            page = int(pm[1])
            continue
        if page < 2:
            continue
        if 'SECTION B' in line:
            section = 'B'
        if re.search(r'6145/[12]/|^For$|^Use$|Examiner|Turn over|^\d{5,}$|©|^ORDINARYLEVEL$', line):
            continue
        line = re.sub(r'\.{3,}', '', line).strip()
        if not line or line in ('.', 'SECTION A', 'SECTION B'):
            continue
        main = re.match(r'^(\d{1,2})\s+([A-Za-z(].*)', line)
        if main and int(main[1]) == q + 1:
            q += 1
            letter = roman = ''
            buf, context = [], []
            line = main[2]
            start_page = page
            fresh = True
        part = re.match(r'^\(([a-h])\)\s*(?:\(([ivx]+)\))?\s*(.*)', line)
        sub = re.match(r'^\(([ivx]+)\)\s*(.*)', line)
        if part:
            if buf:
                context.extend(buf)
            letter, roman = part[1], part[2] or ''
            line = part[3]
            buf = []
            start_page = page
            fresh = True
        elif sub:
            roman, line = sub.groups()
            buf = []
            start_page = page
            fresh = True
        if not q:
            continue
        marks = re.search(r'\[(\d+)\]', line)
        if marks:
            before = line[:marks.start()].strip(' .0123456789')
            if before:
                buf.append(before)
            tariff = int(marks[1])
            # Totals follow the final part without a fresh question start.
            if not fresh:
                continue
            stem = re.sub(r'\s+', ' ', ' '.join(buf)).strip()
            ref = str(q) + (f'({letter})' if letter else '') + (f'({roman})' if roman else '')
            records.append({'evidence_id': f'EV-6145-{year}-P{paper}-{ref}',
                            'source_id': f'6145-{year}-P{paper}', 'year': int(year),
                            'exam_series': f'{year}-annual', 'paper_id': f'P{paper}', 'variant': None,
                            'section': section, 'question_ref': ref, 'mark_tariff': tariff,
                            'stem': stem, 'context': ' '.join(context),
                            'source_locator': {'pdf_pages': list(range(start_page, page+1)),
                                               'extraction': str(path.relative_to(WS))}})
            fresh = False
            buf = []
        elif not re.fullmatch(r'[.\d\s]+', line):
            buf.append(line)
    mine = [r for r in records if r['year'] == int(year) and r['paper_id'] == 'P'+paper]
    sums = collections.Counter()
    for r in mine:
        sums[re.match(r'\d+', r['question_ref'])[0]] += r['mark_tariff']
    total = sum(r['mark_tariff'] for r in mine)
    audit.append({'source_id': path.name, 'parts': len(mine), 'printed_marks': total,
                  'expected_printed_marks': 80 if paper == '1' else 120, 'question_totals': dict(sums),
                  'reconciles': total == (80 if paper == '1' else 120)})
(WS / 'planning/question-candidates.json').write_text(json.dumps(records, indent=2, ensure_ascii=False)+'\n')
(WS / 'planning/question-extraction-audit.json').write_text(json.dumps(audit, indent=2)+'\n')
for row in audit:
    print(row)
for year in range(2020, 2025):
    output = []
    for row in records:
        if row['year'] == year:
            output.append(f"{row['paper_id']} {row['question_ref']:9} [{row['mark_tariff']}] {row['stem']}")
    (WS / f'planning/questions-{year}.txt').write_text('\n'.join(output)+'\n')
