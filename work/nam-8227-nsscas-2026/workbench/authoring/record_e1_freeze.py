"""Record an executed freeze check outside its own input graph."""
import hashlib,json,os,subprocess,sys
from build_source import ROOT,WB,read,dump
result=subprocess.run([sys.executable,str(WB/'authoring/freeze_stage_e.py'),'--check'],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
if result.returncode:raise RuntimeError(result.stdout+'\n'+result.stderr)
receipt=json.loads(result.stdout.splitlines()[-1]);assert receipt['status']=='pass'
manifest=WB/'authoring/stage-e-manifest.json';assert receipt['manifest_sha256']==hashlib.sha256(manifest.read_bytes()).hexdigest()
receipt.update(scope='E1 exact-byte freeze, not independent content acceptance',candidate_manifest_sha256=read(WB/'checks/stage-e/candidate.json')['manifest_sha256'],self_reference_note='Receipt intentionally outside manifest input set; verify its claimed hash against actual manifest and rerun --check.')
dump(WB/'checks/stage-e-repair-e1-freeze.json',receipt);print(json.dumps(receipt,indent=2))
