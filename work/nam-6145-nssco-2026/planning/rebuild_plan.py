"""Rebuild and validate step 4; never commits, pushes or publishes."""
import json
import subprocess
import sys
from pathlib import Path
WS=Path(__file__).resolve().parents[1];ROOT=WS.parents[1]
def run(script,*args):
    subprocess.run([sys.executable,str(script),*map(str,args)],cwd=ROOT,check=True)
run(WS/'planning/prepare_plan.py')
run(WS/'planning/build_glossary.py')
run(ROOT/'standard/v0.2.0-draft/build/conform_registry.py',WS)
run(WS/'planning/generate_contracts.py')
run(WS/'planning/generate_work_orders.py')
run(WS/'planning/build_exemplar.py')
run(WS/'planning/build_shape_slices.py')
run(ROOT/'standard/v0.2.0-draft/build/render_notes.py',WS/'exemplar','1.1')
# The suite returns 'publish' while this wrapper's exit comparison expects 'pass'.
qa=subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS/'exemplar'),'1.1','--quiet'],cwd=ROOT)
report=json.loads((WS/'exemplar/topics/1.1/qa_report.json').read_text())
if report['release_decision']!='publish' or any(c['status']=='fail' for c in report['deterministic_checks']):
    raise SystemExit('Exemplar has unresolved failures; inspect qa_report.json.')
run(ROOT/'standard/v0.2.0-draft/checks/what_to_fix.py',WS/'exemplar','1.1')
run(WS/'planning/validate_plan.py')
run(WS/'planning/render_plan.py')
run(WS/'planning/verify_mining.py')
print('Step-4 rebuild complete. Await human plan approval; no main-topic authoring or publication performed.')
