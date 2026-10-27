"""Verify persisted mining links/counts independently of report rendering."""
import collections
import hashlib
import json
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
E=WS/'assessment-evidence'
C=WS/'curriculum'
def read(path):return json.loads(path.read_text())
accepted=E/'step3-accepted'
records=read((accepted if accepted.exists() else E)/'assessment_evidence.json')
manifest=read(E/'SOURCE-MANIFEST.json')
sources={s['source_id']:s for s in manifest}
for s in manifest:
    assert hashlib.sha256((REPO/s['path']).read_bytes()).hexdigest()==s['sha256'],s['source_id']
index={o['objective_id']:o for o in read(C/'syllabus-outcome-index.json')['objectives']}
by_id={r['evidence_id']:r for r in records}
assert len(records)==len(by_id)==176
for r in records:
    assert all(key in index for key in r['objective_ids'])
    doc=read(E/'extracted'/f"{r['source_id']}.json")
    pages={p['pdf_page']:p for p in doc['pages']}
    assert r['source_locator']['pdf_page'] in pages
    assert f"[{r['mark_tariff']}]" in pages[r['tariff_source']['pdf_page']]['raw']
    report=read(E/'extracted'/f"{r['report_locator']['source_id']}.json")
    report_pages={p['pdf_page']:p for p in report['pages']}
    for n in r['report_locator']['pdf_pages']:
        assert hashlib.sha256(report_pages[n]['raw'].encode()).hexdigest()==r['report_page_text_sha256'][str(n)]
    assert sum(r['report_ao_marks'].values())==r['mark_tariff']
for source_id in [s for s in sources if s.startswith('QP-')]:
    rr=[r for r in records if r['source_id']==source_id]
    assert sum(r['mark_tariff'] for r in rr)==100
    assert all(sum(r['mark_tariff'] for r in rr if r['question_number']==q)==20 for q in range(1,6))
exposure=read((accepted if accepted.exists() else C)/'exam-exposure.json')
assert {o['objective_id'] for o in exposure['objectives']}==set(index)
for o in exposure['objectives']:
    rr=[r for r in records if o['objective_id'] in r['objective_ids']]
    assert set(o['evidence_ids'])=={r['evidence_id'] for r in rr}
    assert o['question_parts']==len(rr)
    assert o['distinct_series']==len({r['exam_series'] for r in rr})
    assert o['maximum_tariff']==max((r['mark_tariff'] for r in rr),default=0)
    assert o['command_word_mix']==dict(collections.Counter(r['command_word'] for r in rr))
words=read(E/'command-word-evidence.json')
assert sum(x['substantive_task_count'] for x in words)==176
for word in words:
    rr=[r for r in records if r['command_word']==word['word']]
    assert set(word['evidence_ids'])=={r['evidence_id'] for r in rr}
    assert {int(k):v for k,v in word['tariff_counts'].items()}==dict(collections.Counter(r['mark_tariff'] for r in rr))
    assert word['use_in_prompts']==bool(word['task_sentence_opening_count'])
findings=read(E/'examiner-findings.json')
assert len({f['finding_id'] for f in findings})==len(findings)
assert all(f['evidence_id'] in by_id for f in findings)
miscon=read((accepted if accepted.exists() else C)/'misconceptions.json')['misconceptions']
assert all(m['evidence_ids'] and all(x in by_id for x in m['evidence_ids']) for m in miscon)
numbers=read(E/'numeric-verification.json')
assert numbers['status']=='pass' and numbers['numeric_and_chart_checks']==len(numbers['checks'])
ao_totals={ao:sum(r['report_ao_marks'][ao] for r in records) for ao in 'ABCD'}
assert ao_totals=={'A':400,'B':200,'C':250,'D':150},ao_totals
summary={'status':'pass','source_hashes_verified':len(manifest),'question_parts_verified':len(records),
         'all_paper_and_main_question_totals_reconciled':True,'ao_marks':ao_totals,
         'exposure_rows_recomputed':len(exposure['objectives']),
         'command_count_and_tariff_rows_recomputed':len(words),
         'finding_links_verified':len(findings),'misconception_links_verified':len(miscon),
         'numeric_and_chart_checks':numbers['numeric_and_chart_checks'],
         'limits':'Verifies source integrity, locators, links and derivations; does not independently validate semantic mappings or learner content.'}
(E/'mining-link-verification.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
