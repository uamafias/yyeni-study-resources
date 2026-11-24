"""Rebuild and freeze-check D4.1 in two genuinely relocated disposable trees."""
import argparse,hashlib,json,platform,shutil,subprocess,sys,tempfile
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;ROOT=W.parents[2];H=P/'d4-1'
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def execute(command,cwd):
 r=subprocess.run(command,cwd=cwd,capture_output=True,text=True)
 assert r.returncode==0,(command,r.stdout[-3000:],r.stderr[-3000:])
 return json.loads(r.stdout)
def freeze(root):return execute([sys.executable,str(root/W.relative_to(ROOT)/'planning/d4/freeze-plan.py'),'--check'],root)
ap=argparse.ArgumentParser();ap.add_argument('--final-sync',action='store_true');ap.add_argument('--state');args=ap.parse_args()
if args.final_sync:
 state=read(Path(args.state));manifest=read(P/'plan-manifest.json');results=[]
 for label,raw in state['copies'].items():
  dest=Path(raw)
  for rel,h in manifest['files'].items():
   target=dest/rel
   if not target.exists()or sha(target)!=h:
    metadata_paths={str(x.relative_to(ROOT))for x in [W.parent/'STATUS.md',W/'STATUS.md',W/'HANDOVER.md',W/'checks/plan-errata-d4-1-report.md',W/'checks/plan-errata-d4-1-preservation.json']}
    assert rel in metadata_paths or rel.startswith(str(H.relative_to(ROOT))+'/'),('rebuilt core changed after relocation proof; refusing metadata sync',rel)
    target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,target)
  target=dest/P.relative_to(ROOT)/'plan-manifest.json';shutil.copy2(P/'plan-manifest.json',target)
  result=freeze(dest);results.append(dict(copy=label,**result))
 print(json.dumps(dict(status='pass',phase='final-manifest-check',copies=results),indent=2));raise SystemExit
temp=Path(tempfile.mkdtemp(prefix='yyeni-8227-d41-'));state=dict(copies={});results=[]
manifest=read(P/'plan-manifest.json');snapshot=read(W/'analysis/analysis-snapshot.json');external=set(manifest['source_files'])|set(snapshot['source_files'])|set(snapshot['files'])
expected=read(P/'d4/design-rebuild-proof.json')['outputs']
for i in [1,2]:
 label=f'relocated-{i}';dest=temp/label;target=dest/W.parent.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True)
 command=['cp','-cR',str(W.parent),str(target)]if platform.system()=='Darwin'else['cp','--reflink=auto','-a',str(W.parent),str(target)]
 r=subprocess.run(command,capture_output=True,text=True)
 if r.returncode:
  if target.exists():shutil.rmtree(target)
  shutil.copytree(W.parent,target,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
 linked=0
 for rel in sorted(external):
  if rel.startswith(str(W.parent.relative_to(ROOT))+'/'):continue
  source=ROOT/rel;out=dest/rel
  if not out.exists():out.parent.mkdir(parents=True,exist_ok=True);out.symlink_to(source);linked+=1
 print(label+': cloned subject and linked '+str(linked)+' immutable source paths',flush=True)
 script=dest/W.relative_to(ROOT)/'planning/d4/rebuild-design.py'
 rebuilt=execute([sys.executable,str(script)],dest)
 assert rebuilt['status']=='pass'and rebuilt['byte_identical_derived_outputs']==28
 for rel,h in expected.items():assert sha(dest/W.relative_to(ROOT)/rel)==h,(label,'derived output differs',rel)
 guard=execute([sys.executable,str(dest/W.relative_to(ROOT)/'planning/d4-1/no-score-change-check.py'),'--check'],dest);assert guard['status']=='pass'
 frozen=freeze(dest);state['copies'][label]=str(dest)
 results.append(dict(copy=label,derived_outputs_matching_author=28,rebuild=rebuilt,freeze=frozen,no_score_check=guard))
 print(label+': rebuild,28raw-byte output comparisons,no-score guard and freeze pass',flush=True)
out=dict(status='pass',scope='Two relocated physical subject copies; immutable external source files linked read-only. Every derived output compared byte-for-byte without normalisation.',copies=results,source_render_path='repo-relative; source and render hashes unchanged',limits='Author portability/rebuild evidence, not cross-vendor acceptance, runtime marker/UI or production testing. Final metadata/manifest may be synchronised without modifying the rebuilt design; --final-sync verifies those final pins separately.')
(H/'relocated-rebuild-proof.json').write_text(json.dumps(out,indent=2)+'\n');statepath=temp/'state.json';statepath.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps(dict(status='pass',state_path=str(statepath),copies=2,matching_derived_outputs_per_copy=28)))
