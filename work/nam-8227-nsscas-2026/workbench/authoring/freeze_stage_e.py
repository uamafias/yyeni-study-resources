"""Freeze the authored scope; approval/release states are deliberately separate."""
import hashlib,json,sys
from pathlib import Path
from build_source import ROOT,WB,S,P,read,dump
from approval_snapshot import verify as verify_approval
TARGET=WB/'authoring/stage-e-manifest.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def paths():
 result=set()
 for base in (S,WB/'authoring',WB/'checks/stage-e'):
  result.update(p for p in base.rglob('*')if p.is_file()and'__pycache__'not in p.parts and p.suffix not in ('.pyc','.pyo')and p!=TARGET)
 result.update(WB/p for p in ('STATUS.md','HANDOVER.md','PLAN.md','subject-rules.md','recipe-contract.md','app-change-handoff.md','checks/author-report.md','checks/stage-e-repair-e1-report.md','package-definition.json','planning/OWNER-CHECKPOINT.md','planning/approvals/stage-d-4a054832/approval.json','planning/approvals/stage-d-4a054832/manifest.json'))
 result.add(WB.parent/'STATUS.md');result.update((WB/'work-orders').glob('*.md'))
 c=ROOT/read(WB/'checks/stage-e/candidate.json')['candidate'];result.update(p for p in c.rglob('*')if p.is_file()and'__pycache__'not in p.parts and p.suffix not in ('.pyc','.pyo'))
 return sorted(result)
def freeze():
 verify_approval();candidate=read(WB/'checks/stage-e/candidate.json');integration=read(WB/'checks/stage-e/integration.json');build=read(WB/'checks/stage-e/source-build.json')
 assert integration['status']=='pass'and candidate['status']=='pass'
 manifest={'schema':'8227-stage-e-authoring-manifest-v1','subject':'NSSCAS Mathematics 8227','syllabus_edition':'NIED December 2020','grade':'12','owner':'Vitalis','date':'2026-11-24','authors':'Codex AUTHOR plus three parallel same-vendor assistants','status':'E1 repair authored; cross-vendor diff-only confirmation pending','native_version':'0.1.5','design_rubric_version':'0.1.4','reviewed_stage_e_manifest_sha256':'22cd1799146ce1d07c25c837f7078b6bb0f717d0e5b9985d57f4371f2ec87025','owner_design_manifest_sha256':'4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec','owner_design_content_digest':'e9cd8f58345364e7b3bb45fadf2bab162571cc4c101df5beff2189a514fd8780','candidate':candidate['candidate'],'candidate_manifest_sha256':candidate['manifest_sha256'],'counts':{k:build[k]for k in ('recipes','choices','assessed_part_slots','branch_marks','generated_parameter_rows','prepared_assets')},'frozen_runtime_examples':integration['frozen_examples'],'files':{str(p.relative_to(ROOT)):sha(p)for p in paths()},'guideline_authority':{str(p.relative_to(ROOT)):sha(p)for p in sorted((ROOT/'workbench/playbook/guidelines').glob('*'))if p.is_file()},'cross_vendor_review_evidence':{str(p.relative_to(ROOT)):sha(p)for folder in ('opus-5-5-d4-1-check','opus-stage-e')for p in sorted((WB/'review'/folder).rglob('*'))if p.is_file()},'release_approved':False,'registry_activated':False,'website_or_response_marker_accepted':False,'not_done':['app edits','installation','MCP import','school/classroom/learner assignment','commit','push']}
 manifest['content_digest']=hashlib.sha256(json.dumps(manifest['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest();dump(TARGET,manifest);print(json.dumps({'status':'frozen','files':len(manifest['files']),'manifest_sha256':sha(TARGET),'candidate_manifest_sha256':candidate['manifest_sha256']}))
def check():
 verify_approval();d=read(TARGET)
 assert set(d['files'])==set(str(p.relative_to(ROOT))for p in paths()),'Unfrozen or removed live Stage-E path'
 for kind in ('files','cross_vendor_review_evidence','guideline_authority'):
  for rel,h in d[kind].items():assert sha(ROOT/rel)==h,rel
 assert hashlib.sha256(json.dumps(d['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==d['content_digest']
 print(json.dumps({'status':'pass','files':len(d['files']),'manifest_sha256':sha(TARGET),'release_approved':False}))
if __name__=='__main__':check()if'--check'in sys.argv else freeze()
