"""Pin/check the Stage-D D1 candidate independently of the analysis-content freeze."""
import argparse,hashlib,json,subprocess
from pathlib import Path
W=Path(__file__).resolve().parents[2];P=W/'planning';ROOT=W.parents[2];TARGET=P/'plan-manifest.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def check_hashes(items,base=ROOT):
 for rel,h in items.items():assert sha(base/rel)==h,('hash mismatch',rel)
parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
if args.check:
 d=read(TARGET);assert d['schema']=='8227-stage-d-design-manifest-v0.1.1'
 for key in ['files','source_files','review_files']:check_hashes(d[key])
 assert hashlib.sha256(json.dumps(d['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==d['content_digest']
 print(json.dumps({'status':'pass','candidate_files':len(d['files']),'sources':len(d['source_files']),'reviews':len(d['review_files']),'manifest_sha256':sha(TARGET)},indent=2));raise SystemExit
baseline=read(W/'checks/plan-repair-d1-baseline.json');old=P/'history/plan-manifest-d0.json';assert sha(old)==baseline['baseline_manifest_sha256'];d0=read(old);check_hashes(d0['files'],ROOT/baseline['d0_candidate']);check_hashes(baseline['review_hashes'])
analysis=read(W/'analysis/analysis-snapshot.json');check_hashes(analysis['source_files']);check_hashes(analysis['files'])
preserved=read(P/'stage-d-baseline.json')['preserved_analysis_curriculum_sources_reviews'];changed={rel:{'before':h,'after':sha(ROOT/rel)}for rel,h in preserved.items()if sha(ROOT/rel)!=h}
expected=['history/rebuild-verification-r7-closeout-final-fresh-copy.json','objective-problem-map.json','objective-problem-map.md','textbook-completion-audit-r5.json','textbook-exam-candidates-r6.json','textbook-exam-relations-r7.json','textbook-families.json','textbook-insights.md'];assert set(changed)=={str((W/'analysis'/x).relative_to(ROOT))for x in expected},('unexpected accepted-input change',list(changed))
transition=dict(status='S3-10 named residual propagation only; no item-level assessed/component retag',preserved_baseline='planning/stage-d-baseline.json',baseline_paths=len(preserved),unchanged_paths=len(preserved)-len(changed),changed_paths=changed,original_manifest_sha256=sha(old),archived_d0_files_verified=len(d0['files']),review_files_unchanged=len(baseline['review_hashes']),analysis_content_snapshot_sha256=sha(W/'analysis/analysis-snapshot.json'),analysis_content_pinned_files=len(analysis['files']),stage_transition_rule='Status/handover/Stage-D design use this separate plan manifest, not the immutable historical accepted snapshot.')
dump(W/'checks/plan-repair-d1-preservation.json',transition)
parts=read(P/'part-evidence-register.json')['parts'];merged=read(P/'pilot-design.json');counts=merged['counts'];assert counts['recipes']==9 and counts['branch_choices']==14 and len(parts)==27
assert len(read(W/'checks/plan-repair-d1-dispositions.json')['findings'])==94
assert read(W/'checks/r7-closeout/fresh-copy-proof.json')['total_seeded_errors_rejected']==75
paths=[]
for folder in [P,W/'work-orders',W/'exemplars']:
 paths +=[p for p in folder.rglob('*')if p.is_file() and 'history'not in p.relative_to(folder).parts and '__pycache__'not in p.parts and p.name!='.DS_Store' and p!=TARGET]
paths +=list((W/'checks').glob('plan-repair-d1*'))
paths +=[W/n for n in ['PLAN.md','recipe-contract.md','subject-rules.md','app-change-handoff.md','capability-gaps.md','STATUS.md','HANDOVER.md','analysis/analysis-snapshot.json','checks/repair-r7-closeout.md','checks/r7-closeout/fresh-copy-proof.json','checks/r7-closeout/final-validation.json']]
paths +=[W.parent/'STATUS.md']
files={str(p.relative_to(ROOT)):sha(p)for p in sorted(set(paths))if p.is_file()}
manifest=dict(schema='8227-stage-d-design-manifest-v0.1.1',subject='NSSCAS Mathematics8227',syllabus_edition='NIED December2020',owner='Vitalis',date='2026-11-23',planner='Codex with three parallel same-vendor assistants',status='D1 author repair complete; Claude short check then Vitalis approval pending',counts=counts,files=files,source_files=analysis['source_files'],review_files=baseline['review_hashes'],d0_recovery=dict(manifest_path=str(old.relative_to(ROOT)),manifest_sha256=sha(old),candidate_path=baseline['d0_candidate'],verified_files=len(d0['files'])),analysis_transition=transition,independence='Independent-formula/CAS/quadrature and parallel assistants are same-vendor author evidence. Claude focused check pending; owner acceptance pending.',owner_checkpoint='OD3: short check, then Vitalis approves exact plan/counts/gaps/capabilities/exemplars; no stageE until explicit approval',git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),not_created=['Runtime recipes/items','Runtime question generators','Provider package installation','Imports','Learner assignments','Commit','Push'],next_action='Focused Claude check using planning/CLAUDE-D1-SHORT-CHECK.md, then Vitalis approval of exact manifest digest',content_digest=hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest())
dump(TARGET,manifest);print(json.dumps({'candidate_files':len(files),'d0_recovered':len(d0['files']),'unchanged_accepted_inputs':transition['unchanged_paths'],'named_analysis_changes':len(changed),'manifest_sha256':sha(TARGET)},indent=2))
