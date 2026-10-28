"""6145 corpus extraction and aggregation. Human semantic mappings are separate inputs."""
import collections
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence'
TEXT = OUT / 'extracted'
RANGES = {2020: (141, 154), 2021: (131, 144), 2022: (159, 176),
          2023: (173, 193), 2024: (171, 187)}


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def extract():
    TEXT.mkdir(parents=True, exist_ok=True)
    sources = []
    for path in sorted((ROOT / 'Question Banks/Namibian Curricula/NSSCO (New)/Economics').rglob('*.pdf')):
        reader = PdfReader(path)
        cover = norm(reader.pages[0].extract_text())
        paper = re.search(r'6145\s*[/\-]\s*([12])', cover)[1]
        year = int(path.parent.name)
        sid = f'{year}-P{paper}'
        for mode in ('plain', 'layout'):
            data = '\n'.join(f'\n=== PDF PAGE {i + 1} ===\n' + pg.extract_text(extraction_mode=mode)
                             for i, pg in enumerate(reader.pages))
            (TEXT / f'{sid}-{mode}.txt').write_text(data)
        sources.append({'source_id': sid, 'kind': 'question_paper', 'year': year,
                        'paper_id': paper, 'path': str(path.relative_to(ROOT)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'pages': len(reader.pages), 'series': f'{year} annual; month not stated on cover',
                        'first_proof_filename': 'Proof' in path.name,
                        'cover_verbatim': cover})
    for year, (first, last) in RANGES.items():
        path = next((ROOT / 'Question Banks/Namibian Examiner Reports/NSSCO (New) ' / str(year)).glob('*.pdf'))
        reader = PdfReader(path)
        for mode in ('plain', 'layout'):
            data = '\n'.join(f'\n=== SOURCE PDF PAGE {n} ===\n' + reader.pages[n - 1].extract_text(extraction_mode=mode)
                             for n in range(first, last + 1))
            (TEXT / f'{year}-ER-{mode}.txt').write_text(data)
        sources.append({'source_id': f'{year}-ER', 'kind': 'examiner_report', 'year': year,
                        'path': str(path.relative_to(ROOT)), 'pdf_pages': [first, last],
                        'printed_pages': [first - 2, last - 2],
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'scope': 'Economics 6145 Paper 1 and Paper 2 only; other subjects excluded'})
    (OUT / 'sources.json').write_text(json.dumps({'sources': sources,
        'extraction': 'pypdf plain and layout, compared during reading. pdftotext unavailable on PATH; selected diagrams rendered separately. No OCR needed.'}, indent=2) + '\n')


def clean_lines(text):
    page = None
    for line in text.splitlines():
        m = re.match(r'=== PDF PAGE (\d+) ===', line)
        if m:
            page = int(m[1])
            continue
        line = norm(line)
        if not line or re.fullmatch(r'(For|Examiner’s|Use|\d+|6145/\d/\d+|\[Turn over)', line):
            continue
        if '6145/' in line or line == 'BLANK PAGE':
            continue
        if 'The DNEA acknowledges' in line:
            continue
        # Answer dotted lines carry tariff tokens but no question content.
        if re.search(r'\.{5,}', line):
            mark = re.search(r'\[(\d+)\]', line)
            if mark:
                yield page, mark[0]
            continue
        yield page, line


def parse():
    records = []
    for path in sorted(TEXT.glob('*-P?-plain.txt')):
        sid = path.name.split('-plain')[0]
        year, paper = int(sid[:4]), sid[6]
        active = False
        section = 'A'
        pending = []
        main = 0
        letter = ''
        roman = ''
        for page, line in clean_lines(path.read_text()):
            if page == 1:
                continue
            if line.upper() == 'SECTION A':
                active = True
                section = 'A'
                pending = []
                continue
            if not active:
                continue
            if line.upper() == 'SECTION B':
                section = 'B'
                pending = []
                letter = roman = ''
                if paper == '1':
                    main += 1
                continue
            pending.append((page, line))
            mark = re.search(r'\[(\d+)\]', line)
            if not mark:
                continue
            tariff = int(mark[1])
            if tariff > 10:
                pending = []
                continue
            chunk = pending
            pending = []
            last_label = None
            for k, (_, l) in enumerate(chunk):
                # Printed page numbers and numbered answer spaces are excluded.
                m = re.match(r'^(\d{1,2})\s+(?=[A-Z(])', l)
                if m:
                    main = int(m[1])
                    letter = roman = ''
                    last_label = k
                sub = re.match(r'^(?:\d+\s+)?\(([a-h])\)(?:\s+\(([ivx]+)\))?', l)
                if sub:
                    letter = sub[1]
                    roman = sub[2] or ''
                    last_label = k
                else:
                    sub = re.match(r'^\(([ivx]+)\)', l)
                    if sub:
                        roman = sub[1]
                        last_label = k
            # Q22 in 2023 P1 is drawn into a table; its number is not extractable.
            if sid == '2023-P1' and main == 21 and any('highest standard of living' in l for _, l in chunk):
                main, last_label = 22, 0
            # The first Q23/Q25 labels on 2020/2022 P1 are embedded in graphics.
            ref = str(main) + (f'({letter})' if letter else '') + (f'({roman})' if roman else '')
            start = last_label if last_label is not None else 0
            stem = norm(' '.join(l for _, l in chunk[start:]))
            stem = re.sub(r'^\d+\s+', '', stem)
            stem = re.sub(r'^(?:\([a-z]+\)\s*)+', '', stem)
            stem = re.sub(r'\[\d+\]', '', stem).strip()
            # Unnumbered direct question in the short-answer section.
            if section == 'A' and paper == '1' and last_label is None:
                main += 1
                ref = str(main)
            records.append({'evidence_id': f'EV-6145-{sid}-{ref}', 'source_id': sid,
                            'exam_series': str(year), 'year': year, 'paper_id': paper,
                            'variant': None, 'section': section, 'question_ref': ref,
                            'mark_tariff': tariff, 'stem_internal': stem,
                            'source_locator': {'source_id': sid, 'pdf_page': chunk[start][0],
                                               'tariff_pdf_page': page},
                            'source_provenance': 'corpus'})
    (OUT / 'question-parts-draft.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    for r in records:
        print(f"{r['source_id']} {r['question_ref']:10s} {r['mark_tariff']}m p{r['source_locator']['pdf_page']}: {r['stem_internal']}")
    print('COUNTS', collections.Counter(r['source_id'] for r in records))
    print('MARKS', {s: sum(r['mark_tariff'] for r in records if r['source_id'] == s)
                    for s in sorted({r['source_id'] for r in records})})


if __name__ == '__main__':
    import sys
    if '--extract' in sys.argv:
        extract()
    parse()
