"""Mechanical candidate extraction; meaning mappings are supplied separately by the miner."""
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence'
label_rx = re.compile(r'^(?:([1-5])\s+)?\(([a-d]|i{1,3}|iv|v)\)\s*(?:\((i{1,3}|iv|v)\)\s*)?(.*)$')
all_records = []
for source in sorted((OUT / 'extracted').glob('QP-*.json')):
    doc = json.loads(source.read_text())
    year, paper = re.match(r'QP-(\d+)-P(\d)', doc['source_id']).groups()
    records, current, question, letter = [], None, 0, None
    for page in doc['pages']:
        for raw_line in page['raw'].splitlines():
            line = ' '.join(raw_line.split())
            match = label_rx.match(line)
            if match:
                q, lab, roman, body = match.groups()
                if current is not None:
                    raise ValueError(('unclosed question', current, line))
                if lab in 'abcd':
                    if lab == 'a':
                        question = int(q) if q else question + 1
                    letter = lab
                else:
                    roman = lab
                ref = f'{question}({letter})' + (f'({roman})' if roman else '')
                current = {'evidence_id': f'EV-6144-{year}-P{paper}-{ref}',
                           'source_id': doc['source_id'], 'year': int(year), 'paper_id': f'P{paper}',
                           'question_ref': ref, 'question_number': question,
                           'source_locator': {'path': doc['path'], 'pdf_page': page['pdf_page']},
                           'text_lines': [body] if body else []}
            elif current is not None:
                # Remove response lines, page furniture and printed identifiers.
                if not line or re.search(r'6144/|Examiner|^For$|^Use$|Turn over|^\d{6}$',line):
                    continue
                if re.fullmatch(r'\d+', line):
                    continue
                current['text_lines'].append(line)
            if current is not None:
                marks = re.search(r'\[(\d+)\]',line)
                if marks:
                    current['mark_tariff'] = int(marks.group(1))
                    current['end_pdf_page'] = page['pdf_page']
                    clean=[]
                    for item in current.pop('text_lines'):
                        item = re.sub(r'\[\d+\]', '', item)
                        item = re.sub(r'\.{3,}|…+', '', item).strip()
                        if item and not re.fullmatch(r'\d+',item):clean.append(item)
                    current['question_text_internal_only'] = ' '.join(clean)
                    current['tariff_source'] = {'pdf_page':page['pdf_page'],'verbatim':marks.group(0),'provenance':'corpus'}
                    records.append(current)
                    current=None
    assert current is None
    assert set(r['question_number'] for r in records)==set(range(1,6)), doc['source_id']
    assert sum(r['mark_tariff'] for r in records)==100, (doc['source_id'],records)
    all_records.extend(records)
    packet = [doc['source_id'], 'COVER: ' + ' '.join(doc['pages'][0]['raw'].split())]
    packet += [f"{r['question_ref']} [{r['mark_tariff']}] p{r['source_locator']['pdf_page']}: {r['question_text_internal_only']}" for r in records]
    (OUT / 'extracted' / f"{doc['source_id']}.questions.txt").write_text('\n'.join(packet)+'\n')
    print(doc['source_id'], len(records),'parts',sum(r['mark_tariff'] for r in records),'marks')
(OUT / 'question-candidates.json').write_text(json.dumps(all_records,ensure_ascii=False,indent=2)+'\n')
