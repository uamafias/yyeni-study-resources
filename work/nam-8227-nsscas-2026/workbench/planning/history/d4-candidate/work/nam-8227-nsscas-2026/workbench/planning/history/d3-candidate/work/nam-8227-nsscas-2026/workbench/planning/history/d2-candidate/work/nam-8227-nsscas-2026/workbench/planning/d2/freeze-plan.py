"""Freeze/check D2 plus recoverable D0/D1 and the complementary analysis freeze."""
import argparse,json,hashlib,subprocess
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;ROOT=W.parents[2];TARGET=P/'plan-manifest.json';read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def verify(items,base=ROOT):
 for rel,h in items.items():assert sha(base/rel)==h,('hash mismatch',rel)
def digest(files):return hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def stage_d_excluded(path):
 if not path.is_relative_to(W.parent):return False
 if path in [W.parent/'STATUS.md',W/'STATUS.md',W/'HANDOVER.md',W/'capability-gaps.md',W/'PLAN.md',W/'recipe-contract.md',W/'subject-rules.md',W/'app-change-handoff.md']:return True
 if path.is_relative_to(W):
  rel=path.relative_to(W)
  return rel.parts[0]in ['planning','work-orders','exemplars']or(rel.parts[0]=='checks'and path.name.startswith('plan-'))
 return False
ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
if args.check:
 d=read(TARGET);assert d['schema']=='8227-stage-d-design-manifest-v0.1.2'
 for key in ['files','source_files','review_files']:verify(d[key])
 assert digest(d['files'])==d['content_digest']
 for label in ['d0_recovery','d1_recovery']:
  old=read(ROOT/d[label]['manifest_path']);verify(old['files'],ROOT/d[label]['candidate_path'])
 print(json.dumps(dict(status='pass',files=len(d['files']),sources=len(d['source_files']),reviews=len(d['review_files']),manifest_sha256=sha(TARGET)),indent=2));raise SystemExit
b=read(W/'checks/plan-repair-d2-baseline.json');verify(b['review_hashes']);old=P/'history/plan-manifest-d1.json';assert sha(old)==b['manifest_d1_sha256']
recovery={}
for label,n in [('d0_recovery','d0'),('d1_recovery','d1')]:
 path=P/f'history/plan-manifest-{n}.json';doc=read(path);arc=P/f'history/{n}-candidate';verify(doc['files'],arc)
 recovery[label]=dict(manifest_path=str(path.relative_to(ROOT)),manifest_sha256=sha(path),candidate_path=str(arc.relative_to(ROOT)),verified_files=len(doc['files']))
a=read(W/'analysis/analysis-snapshot.json');verify(a['files']);verify(a['source_files']);verify(a['review_files'])
oldanalysis=read(W/'analysis/history/analysis-snapshot-r7-closeout.json');required={rel for rel in oldanalysis['files']if not stage_d_excluded(ROOT/rel)and 'review'not in Path(rel).parts and '__pycache__'not in Path(rel).parts and Path(rel).name!='.DS_Store'and ROOT/rel!=W/'analysis/analysis-snapshot.json'}
missing=required-set(a['files']);assert not missing,('historical evidence unpinned',sorted(missing))
checks={rel for rel in required if str((W/'checks').relative_to(ROOT))+'/'in rel};assert len(checks)>5000
baseline=read(P/'stage-d-baseline.json')['preserved_analysis_curriculum_sources_reviews'];changes={rel:dict(before=h,after=sha(ROOT/rel))for rel,h in baseline.items()if sha(ROOT/rel)!=h}
expected=['history/rebuild-verification-r7-closeout-final-fresh-copy.json','objective-problem-map.json','objective-problem-map.md','textbook-completion-audit-r5.json','textbook-exam-candidates-r6.json','textbook-exam-relations-r7.json','textbook-families.json','textbook-insights.md'];assert set(changes)=={str((W/'analysis'/x).relative_to(ROOT))for x in expected}
preservation=dict(status='pass',historical_paths_required=len(required),historical_paths_pinned=len(required),historical_checks_paths_pinned=len(checks),uncovered_historical_paths=[],analysis_frozen_files=len(a['files']),protected_sources=len(a['source_files']),review_files_unchanged=len(b['review_hashes']),original_stage_d_baseline_paths=len(baseline),baseline_paths_unchanged=len(baseline)-len(changes),named_analysis_changes=changes,d0_d1_recovery=recovery,scope='Whole workspace freeze with exact Stage-D/review/cache/self exclusions; current plan pins Stage-D including all history/archive files. No item-level mapping, sourcePDF or review modification.')
dump(W/'checks/plan-repair-d2-preservation.json',preservation)
assert len(read(W/'checks/plan-repair-d2-dispositions.json')['findings'])==31
assert read(W/'checks/r7-closeout/fresh-copy-proof.json')['total_seeded_errors_rejected']==76
counts=read(P/'pilot-design.json')['counts'];assert counts['whole_choice_bloom_counts']=={'3':13,'4':1}
paths=[]
for folder in [P,W/'work-orders',W/'exemplars']:
 paths +=[p for p in folder.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.name!='.DS_Store'and p!=TARGET]
paths +=list((W/'checks').glob('plan-repair-d2*'))
paths +=[W/n for n in ['PLAN.md','recipe-contract.md','subject-rules.md','app-change-handoff.md','capability-gaps.md','STATUS.md','HANDOVER.md','analysis/analysis-snapshot.json','checks/repair-r7-closeout.md','checks/r7-closeout/fresh-copy-proof.json','checks/r7-closeout/final-validation.json']]+[W.parent/'STATUS.md']
files={str(p.relative_to(ROOT)):sha(p)for p in sorted(set(paths))if p.is_file()}
manifest=dict(schema='8227-stage-d-design-manifest-v0.1.2',subject='NSSCAS Mathematics8227',syllabus_edition='NIED December2020',owner='Vitalis',date='2026-11-23',role='PLANNER',planner='Codex with three parallel same-vendor assistants',status='D2 author repair complete; Claude changed-scope confirmation then Vitalis approval pending',counts=counts,files=files,source_files=a['source_files'],review_files=b['review_hashes'],**recovery,analysis_preservation=preservation,owner_checkpoint='OD1–5; exact active adaptation register/counts/gaps/capabilities/exemplars approved only after changed-scope confirmation',independence='Separate-formula/CAS/quadrature and parallel-assistant checks are author evidence; independent confirmation and owner acceptance pending',git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),not_created=['Runtime items/recipes','Runtime question generators','Provider install','Imports','Learner assignments','Commit','Push'],next_action='Claude planning/CLAUDE-D2-CONFIRM.md, then Vitalis exact-manifest approval',content_digest=digest(files))
dump(TARGET,manifest);print(json.dumps(dict(candidate_files=len(files),d0_recovered=recovery['d0_recovery']['verified_files'],d1_recovered=recovery['d1_recovery']['verified_files'],historical_checks_pinned=len(checks),manifest_sha256=sha(TARGET)),indent=2))
