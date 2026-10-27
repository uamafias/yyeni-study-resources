"""Extract only NSSCO 6144 papers and report sections; retain both reading orders."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence/extracted'
OUT.mkdir(parents=True, exist_ok=True)
inventory = json.loads((WS / 'planning/source-inventory.json').read_text())
sources = []
for record in inventory['files']:
    path = record['path']
    if 'Business Studies (6144)/20' in path and 'Report' not in path:
        year = int(Path(path).parent.name)
        paper = 1 if ('_1.pdf' in path or '-1.pdf' in path or 'Paper 1' in path) else 2
        sources.append((f'QP-{year}-P{paper}', path, None, None))
for year, start, end in [(2020,65,84),(2021,65,80),(2022,75,90),(2023,79,94),(2024,79,104)]:
    path = next((REPO / f'Question Banks/Namibian Examiner Reports/NSSCO (New) /{year}').glob('*.pdf'))
    sources.append((f'ER-{year}', str(path.relative_to(REPO)), start, end))
manifest = []
for source_id, path, start, end in sources:
    reader = PdfReader(REPO / path)
    start, end = start or 1, end or len(reader.pages)
    pages = []
    for n in range(start, end + 1):
        page = reader.pages[n-1]
        pages.append({'pdf_page': n, 'raw': page.extract_text() or '',
                      'layout': page.extract_text(extraction_mode='layout') or ''})
    payload = {'source_id': source_id, 'path': path,
               'sha256': hashlib.sha256((REPO / path).read_bytes()).hexdigest(),
               'pdf_pages': [start,end], 'pages': pages}
    (OUT / f'{source_id}.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    for mode in ['raw','layout']:
        (OUT / f'{source_id}.{mode}.txt').write_text('\n'.join(f"\n--- PDF PAGE {p['pdf_page']} ---\n{p[mode]}" for p in pages))
    manifest.append({k:v for k,v in payload.items() if k != 'pages'})
    print(source_id, len(pages), 'pages', flush=True)
(OUT.parent / 'SOURCE-MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n')
