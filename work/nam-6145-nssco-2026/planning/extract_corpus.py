"""Extract only Economics sources; preserve page-level provenance and both reading orders."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence/extracted'
OUT.mkdir(parents=True, exist_ok=True)
manifest = []
qp_root = ROOT / 'Question Banks/Namibian Curricula/NSSCO (New)/Economics'
er_root = ROOT / 'Question Banks/Namibian Examiner Reports/NSSCO (New) '
cached = WS / 'assessment-evidence/source-cache/NSSCOExaminersReport2025.pdf'
for path in sorted(qp_root.rglob('*.pdf')) + sorted(er_root.rglob('*.pdf')) + ([cached] if cached.exists() else []):
    kind = 'QP' if qp_root in path.parents else 'ER'
    year = 2025 if path == cached else int(path.parent.name)
    layouts = {}
    for order in ('layout', 'raw'):
        result = subprocess.run(['pdftotext', '-'+order, str(path), '-'], capture_output=True, text=True, check=True)
        layouts[order] = result.stdout.split('\f')[:-1]
    if kind == 'QP':
        match = re.search(r'6145[-_ ]([12])', path.name)
        assert match, path
        paper = match[1]
        selected = list(range(len(layouts['layout'])))
        stem = f'6145-{year}-P{paper}'
    else:
        paper = None
        pgs = layouts['layout']
        starts = [i for i, p in enumerate(pgs) if re.search(r'ECONOMICS\s+6145', p) and 'GENERAL COMMENTS' in p]
        assert starts, path
        start = min(starts)
        def other_subject(text):
            match = re.search(r'^\s*(61\d\d)\s*\n\s*Paper', text[:250], re.M)
            return match and match[1] != '6145'
        end = next((i for i in range(start+1, len(pgs)) if other_subject(pgs[i])), len(pgs))
        selected = list(range(start, end))
        stem = f'6145-{year}-ER'
    outputs = {}
    for order, pages in layouts.items():
        text = '\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+pages[i] for i in selected)
        target = OUT / f'{stem}-{order}.txt'
        target.write_text(text)
        outputs[order] = str(target.relative_to(WS))
    manifest.append({'source_id': stem, 'kind': kind, 'year': year, 'paper': paper,
                     'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                     'pdf_pages': [i+1 for i in selected], 'extractions': outputs,
                     'first_proof_filename': 'First Proof' in path.name})
(WS / 'assessment-evidence/extraction-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
for item in manifest:
    print(item['source_id'], len(item['pdf_pages']), 'pages', item['pdf_pages'][0], 'to', item['pdf_pages'][-1])
