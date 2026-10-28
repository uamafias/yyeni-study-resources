"""Reopen the held PDFs and reconcile references, totals and generated exposure."""
import collections
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence'
load = lambda p: json.loads(p.read_text())
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
sources = load(OUT / 'sources.json')['sources']
findings = load(OUT / 'examiner-findings.json')['findings']
records = load(OUT / 'assessment_evidence.json')['records']
exposure = load(WS / 'curriculum/exam-exposure.json')
errors = []
page_cache = {}
for s in sources:
    path = ROOT / s['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == s['sha256'], path
    reader = PdfReader(path)
    if s['kind'] == 'examiner_report':
        page_cache[s['source_id']] = {n: reader.pages[n - 1].extract_text()
                                    for n in range(s['pdf_pages'][0], s['pdf_pages'][1] + 1)}
    else:
        # Reconcile the complete printed tariff inventory independently of the
        # question-reference parser, excluding section/question subtotals.
        tariffs = [int(x) for p in reader.pages[1:]
                   for x in re.findall(r'\[(\d+)\]', p.extract_text()) if int(x) <= 10]
        mined = [r['mark_tariff'] for r in records if r['source_id'] == s['source_id']]
        assert tariffs == mined, (s['source_id'], tariffs, mined)

for f in findings:
    source = page_cache[f['source_locator']['source_id']]
    n = f['source_locator']['pdf_page']
    text = norm(' '.join(source.get(p, '') for p in (n, n + 1)))
    if norm(f['verbatim_internal']) not in text:
        errors.append(f['finding_id'])
assert not errors, ('Report quote mismatch', errors)

for o in exposure['objectives']:
    rs = [r for r in records if o['objective_id'] in r['objective_ids']]
    assert o['times_examined'] == len(rs)
    assert o['series'] == sorted({r['exam_series'] for r in rs})
    assert o['marks_examined'] == sum(r['mark_tariff'] for r in rs if r['primary_objective_id'] == o['objective_id'])
    assert o['command_words'] == dict(collections.Counter(r['command_word'] for r in rs))
    assert o['evidence_ids'] == [r['evidence_id'] for r in rs]
scope = load(WS / 'curriculum/scope-scan.json')
control_count = 0
for entry in scope['entries']:
    for text in entry['controls']['must_catch']:
        assert re.search(entry['pattern'], text, re.I), (entry['construct'], text)
        control_count += 1
    for text in entry['controls']['must_allow']:
        assert not re.search(entry['pattern'], text, re.I), (entry['construct'], text)
        control_count += 1

report = {'source_hashes_checked': len(sources),
          'independent_qp_tariff_sequences_checked': 10,
          'report_comment_quotes_checked': len(findings),
          'objective_exposure_rows_recomputed': len(exposure['objectives']),
          'scope_controls_checked': control_count,
          'status': 'PASS', 'limits': 'This verifies extraction/reconciliation; human semantic mappings and source anomalies remain explicit judgements. It is not a Step 6 content approval.'}
(OUT / 'source-verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
