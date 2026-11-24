"""Freeze/check the D3 candidate, all live plan checks and unchanged analysis."""
import argparse,json,hashlib,subprocess
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;ROOT=W.parents[2];TARGET=P/'plan-manifest.json'
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def verify(items,base=ROOT):
 for rel,h in items.items():assert sha(base/rel)==h,('hash mismatch',rel)
def digest(files):return hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def livepaths():
 paths=[]
 for folder in [P,W/'work-orders',W/'exemplars']:
  paths += [p for p in folder.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.name!='.DS_Store'and p!=TARGET]
 paths+=list((W/'checks').glob('plan-*'))
 paths +=[W/n for n in ['PLAN.md','recipe-contract.md','subject-rules.md','app-change-handoff.md','capability-gaps.md','STATUS.md','HANDOVER.md','analysis/analysis-snapshot.json','checks/repair-r7-closeout.md','checks/r7-closeout/fresh-copy-proof.json','checks/r7-closeout/final-validation.json']]+[W.parent/'STATUS.md']
 return {str(p.relative_to(ROOT)):p for p in paths if p.is_file()}
args=argparse.ArgumentParser();args.add_argument('--check',action='store_true');args=args.parse_args()
baseline=read(W/'checks/plan-repair-d3-baseline.json')
verify(baseline['protected_analysis_tools_curriculum']);verify(baseline['review_hashes'])
protected_now={str(p.relative_to(ROOT))for folder in [W/'analysis',W/'tools',W.parent/'curriculum']for p in folder.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.name!='.DS_Store'}
assert protected_now==set(baseline['protected_analysis_tools_curriculum']),('analysis/tool/curriculum inventory changed',protected_now^set(baseline['protected_analysis_tools_curriculum']))
a=read(W/'analysis/analysis-snapshot.json')
for k in ['files','source_files','review_files']:verify(a[k])
recovery={}
for n in ['d0','d1','d2']:
 mp=P/f'history/plan-manifest-{n}.json';arc=P/f'history/{n}-candidate';old=read(mp);verify(old['files'],arc)
 recovery[n+'_recovery']=dict(manifest_path=str(mp.relative_to(ROOT)),manifest_sha256=sha(mp),candidate_path=str(arc.relative_to(ROOT)),verified_files=len(old['files']))
assert recovery['d2_recovery']['manifest_sha256']==baseline['manifest_d2_sha256']
if args.check:
 d=read(TARGET);assert d['schema']=='8227-stage-d-design-manifest-v0.1.3'
 for k in ['files','source_files','review_files']:verify(d[k])
 assert set(livepaths())==set(d['files']),('uncovered or stale live Stage-D path',set(livepaths())^set(d['files']))
 assert digest(d['files'])==d['content_digest']
 assert d['analysis_snapshot_sha256']==sha(W/'analysis/analysis-snapshot.json')
 print(json.dumps(dict(status='pass',files=len(d['files']),sources=len(d['source_files']),reviews=len(d['review_files']),live_plan_checks=sum('/checks/plan-'in x for x in d['files']if '/history/'not in x),d2_recovered=809,manifest_sha256=sha(TARGET)),indent=2));raise SystemExit
preservation=dict(status='pass',analysis_snapshot_sha256=sha(W/'analysis/analysis-snapshot.json'),analysis_frozen_files=len(a['files']),protected_sources=len(a['source_files']),protected_analysis_tools_curriculum=len(baseline['protected_analysis_tools_curriculum']),unchanged_review_files=len(baseline['review_hashes']),analysis_inputs_or_tools_changed=False,source_PDFs_changed=False,all_live_plan_checks_pinned=True,recovery=recovery,scope='Exact D3 start hashes and accepted whole-workspace analysis freeze checked. D3 writes only Stage-D design/check/status namespaces. Existing R7 author+two-fresh-copy/76-negative evidence is preserved, not rerun or re-labelled as new D3 execution.')
dump(W/'checks/plan-repair-d3-preservation.json',preservation)
files={rel:sha(p)for rel,p in sorted(livepaths().items())}
counts=read(P/'pilot-design.json')['counts'];assert counts['whole_choice_bloom_counts']=={'3':13,'4':1}
d=dict(schema='8227-stage-d-design-manifest-v0.1.3',subject='NSSCAS Mathematics 8227',syllabus_edition='NIED December 2020',owner='Vitalis',date='2026-11-24',role='PLANNER',planner='Codex with three parallel same-vendor assistants',status='D3 author repair complete; Claude changed-scope confirmation then Vitalis exact-manifest approval pending',counts=counts,files=files,source_files=a['source_files'],review_files=baseline['review_hashes'],**recovery,analysis_snapshot_sha256=sha(W/'analysis/analysis-snapshot.json'),analysis_preservation=preservation,owner_checkpoint='OD-1–6 bind; exact counts/gaps/capabilities/exemplars/adaptations remain pending Vitalis approval after Claude D3 confirmation',independence='Separate-formula/CAS/quadrature and parallel-assistant checks are author evidence, not cross-vendor or owner acceptance',git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),not_created=['Runtime recipes/items','Runtime question generators','Provider install','Imports','Learner assignments','Commit','Push'],next_action='Claude planning/CLAUDE-D3-CONFIRM.md, then Vitalis exact-manifest approval',content_digest=digest(files))
dump(TARGET,d);print(json.dumps(dict(status='frozen',files=len(files),d2_recovered=809,manifest_sha256=sha(TARGET)),indent=2))
