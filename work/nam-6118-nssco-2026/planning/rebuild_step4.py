"""Rebuild Step 4 planning artifacts in dependency order; no commit or publish."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'work/nam-6118-nssco-2026';PY=sys.executable
steps=[['planning/build_planning_curriculum.py'],['@standard/conform_registry.py'],['@standard/make_contract.py','--force'],['planning/size_notes_budgets.py'],['@standard/make_work_order.py','--all'],['planning/bind_task_specs.py'],['planning/write_plan.py']]
for stage in steps:
 path,*args=stage
 if path.startswith('@standard/'):
  cmd=[PY,str(ROOT/'standard/v0.2.0-draft/build'/path.split('/',1)[1]),str(W),*args]
 else:cmd=[PY,str(W/path),*args]
 subprocess.run(cmd,cwd=ROOT,check=True)
print('Planning rebuilt. Exemplar construction/checking is separate; authoring and Git are not run.')
