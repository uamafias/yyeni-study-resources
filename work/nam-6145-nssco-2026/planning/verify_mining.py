"""Independent aggregation and provenance audit for step 3, not a publication gate."""
import collections
import importlib.util
import json
import re
from pathlib import Path
from types import SimpleNamespace

WS = Path(__file__).resolve().parents[1]
ROOT = WS.parents[1]
def read(p): return json.loads((WS/p).read_text())
evidence = read('assessment-evidence/assessment_evidence.json')
records = evidence['records']
exposure = read('curriculum/exam-exposure.json')
assert len(records)==271 and len({r['evidence_id'] for r in records})==271
assert all(r['year'] in range(2020,2025) for r in records)
checks=[]
for year in range(2020,2025):
    p1=[r for r in records if r['year']==year and r['paper_id']=='P1']
    p2=[r for r in records if r['year']==year and r['paper_id']=='P2']
    assert sum(r['mark_tariff'] for r in p1)==80
    assert all(sum(r['mark_tariff'] for r in p1 if r['section']==s)==40 for s in ('A','B'))
    for q in range(1,7):
        assert sum(r['mark_tariff'] for r in p2 if int(re.match(r'\d+',r['question_ref'])[0])==q)==20
checks.append('All 10 papers reconcile; P1 sections are 40/40 and all six offered P2 questions are 20 each.')

spec=importlib.util.spec_from_file_location('economics_checks',ROOT/'standard/v0.2.0-draft/checks/yyeni_checks.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
branch={x['objective_id']:x for x in exposure['objectives']}
c39=module.c39(SimpleNamespace(evidence=evidence,exposure=exposure,branch=branch))
assert c39[0]=='pass', c39
checks.append(c39[1])

for word in read('assessment-evidence/command-word-counts.json')['commands']:
    rows=[r for r in records if r['command_word']==word['word']]
    assert len(rows)==word['count']
    assert dict(collections.Counter(str(r['mark_tariff']) for r in rows))==word['tariff_counts']
assert sum(r['count'] for r in read('assessment-evidence/command-word-counts.json')['commands'])==271
checks.append('Primary command counts and tariff distributions independently recompute to 271 parts.')

def norm(t):return re.sub(r'\s+',' ',t).strip()
for finding in read('assessment-evidence/examiner_findings.json')['findings']:
    loc=finding['source_locator']
    text=(WS/loc['extraction']).read_text().split(f"=== PDF PAGE {loc['pdf_page']} ===",1)[1].split('=== PDF PAGE',1)[0]
    assert norm(finding['statement']) in norm(text),finding['finding_id']
for shape in read('curriculum/answer-shapes.json')['shapes']:
    for source in shape['support']:
        text=(WS/source['extraction']).read_text().split(f"=== PDF PAGE {source['pdf_page']} ===",1)[1].split('=== PDF PAGE',1)[0]
        assert norm(source['verbatim']) in norm(text)
checks.append('Every retained error-comment quotation and answer-shape support re-found on its cited source page.')

candidate_ids={r['finding_id'] for r in read('assessment-evidence/report-comment-candidates.json')}
miscon=read('curriculum/misconceptions.json')['entries']
assert len({r['entry_id'] for r in miscon})==len(miscon)
for entry in miscon:
    assert entry['objective_id'] in branch and entry['discriminating_test']
    assert all(r['finding_id'] in candidate_ids for r in entry['source_evidence'])
checks.append(f'{len(miscon)} curated conceptual confusions carry existing report evidence and valid syllabus references.')

for entry in read('curriculum/scope-scan.json')['entries']:
    assert all(re.search(entry['pattern'],s,re.I) for s in entry['controls']['must_catch'])
    assert all(not re.search(entry['pattern'],s,re.I) for s in entry['controls']['must_allow'])
checks.append('All scope-regex catch/allow controls pass; positive depth limits remain manual-review constraints.')
assert sum(r['marks'] for r in read('assessment-evidence/topic-mark-shares.json')['topics'])==1000
checks.append('One-primary-topic marks total 1,000; optional offered marks are kept separate from 800 candidate-route marks.')
report={'result':'PASS','checks':checks,'publication_status':'Full subject publication not assessed. Main topics have no authored learner resources; any plan/exemplar is separately validated.',
        'limitations':['No standalone mark schemes or 2025 QPs; examiner-report mining is an extraction/curation, not a claim that every sentence is a distinct error.',
                       '28 primary mappings are explicitly flagged as contextual or overlapping; decomposition status is recorded in the step-4 plan.',
                       'C-39 is run directly over the mining references; the full publication suite is not applicable yet.']}
(WS/'planning/corpus-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
