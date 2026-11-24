"""Canonical build plus two relocated minimal-input rebuilds; no acceptance labels."""
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
from build_source import ROOT,WB,S,P,read,dump

def inventory(base):
 return {p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(base.rglob('*'))if p.is_file()and'__pycache__'not in p.parts and p.suffix not in ('.pyc','.pyo')}
def run(root,app_root):
 wb=root/'work/nam-8227-nsscas-2026/workbench';a=wb/'authoring';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
 commands=[[sys.executable,str(a/'build_source.py')],[sys.executable,str(a/'check_source.py')],[sys.executable,str(a/'check_notation.py')],['node',str(a/'check_notation.mjs'),str(app_root/'apps/web')],[sys.executable,str(a/'check_ids.py')],[sys.executable,str(a/'check_wording.py')],[sys.executable,str(a/'check_e1_runtime.py')],[sys.executable,str(a/'check_e1_preservation.py')],[sys.executable,str(a/'verify_candidate.py'),'--app-root',str(app_root)]]
 for cmd in commands:
  start=time.monotonic();r=subprocess.run(cmd,cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  print(json.dumps({'location':'canonical'if root==ROOT else'relocated','command':Path(cmd[1]).name,'exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-start,2)}),flush=True)
  if r.returncode:raise RuntimeError(r.stdout+'\n'+r.stderr)
 source=inventory(wb/'source')
 reports={name:hashlib.sha256((wb/'checks/stage-e'/name).read_bytes()).hexdigest()for name in ('source-build.json','integration.json','notation.json','candidate.json','identity.json','wording.json','e1-runtime.json','e1-preservation.json')}
 return dict(source=source,reports=reports,candidate=read(wb/'checks/stage-e/candidate.json')['manifest_sha256'])
def rebuild(app_root):
 canonical=run(ROOT,app_root);locations=[]
 for index in (1,2):
  with tempfile.TemporaryDirectory(prefix='wb8227-e-relocated-')as temp:
   root=Path(temp);wb=root/WB.relative_to(ROOT);wb.mkdir(parents=True)
   for directory in ('source','authoring'):
    shutil.copytree(WB/directory,wb/directory,ignore=shutil.ignore_patterns('__pycache__','*.pyc','candidate-audit-*'))
   for rel in ('planning/calculus-design.json','planning/trig-model-design.json','planning/visual-design.json','planning/part-evidence-register.json','planning/pilot-design.json','planning/d4/deck-compositions.json','planning/approvals/stage-d-4a054832/approval.json','subject-rules.md','planning/plan-manifest.json','analysis/cambridge-evidence.json'):
    target=wb/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(WB/rel,target)
   extracted=wb/'analysis/extracted';extracted.mkdir(parents=True,exist_ok=True)
   for source in sorted((WB/'analysis/extracted').glob('*.txt')):
    if source.name.endswith('-questions.txt')or source.name.startswith('report-')and source.name.endswith('-mathematics.txt'):
     shutil.copyfile(source,extracted/source.name)
   shutil.copytree(ROOT/'yyeni_workbench_tools',root/'yyeni_workbench_tools',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
   actual=run(root,app_root);assert actual==canonical,'Relocated output differs'
   locations.append({'copy':index,'status':'pass','source_files_compared':len(actual['source']),'report_files_compared':len(actual['reports']),'normalisation':'none','candidate_manifest_sha256':actual['candidate']})
 result=dict(status='pass',scope='Canonical plus two relocated minimal-input Stage-E rebuilds; original Stage-D pins verified separately',source_files_compared=len(canonical['source']),reports_compared=canonical['reports'],candidate_manifest_sha256=canonical['candidate'],relocated_rebuilds=locations,source_hashes=canonical['source'],path_normalisation=False)
 dump(WB/'checks/stage-e/rebuild-proof.json',result)
 print(json.dumps({k:v for k,v in result.items()if k!='source_hashes'},indent=2),flush=True)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--app-root',type=Path,required=True);rebuild(parser.parse_args().app_root.resolve())
