"""Enforce the repair write boundary against every reviewed baseline file."""
import hashlib
from build_source import ROOT,WB,read,dump
BASE=WB/'authoring/history/stage-e-0'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def check():
 m=read(BASE/'manifest.json');changed=[];removed=[];unchanged=0
 allowed=('source/','authoring/','checks/stage-e/','checks/author-report.md','STATUS.md','HANDOVER.md','app-change-handoff.md','package-definition.json')
 for rel,before in m['files'].items():
  p=ROOT/rel
  if p.is_file()and sha(p)==before:unchanged+=1;continue
  if p==WB.parent/'STATUS.md':local='../STATUS.md'
  else:
   assert p.is_relative_to(WB),rel
   local=p.relative_to(WB).as_posix()
   assert any(local==rule or local.startswith(rule)for rule in allowed),('out-of-scope change',rel)
  if not p.exists():
   assert local.startswith('source/assets/'),('unexpected removal',rel)
   removed.append({'path':rel,'before':before,'meaning':'live derived SVG replaced; reviewed original bytes remain in archive and immutable candidate'})
  else:changed.append({'path':rel,'before':before,'after':sha(p)})
 for rel,h in m['cross_vendor_review_evidence'].items():assert sha(ROOT/rel)==h,rel
 inputs=read(WB/'review/opus-stage-e/inputs.json')
 result={'status':'pass','scope':'Every existing reviewed file compared; only named E1 namespaces changed, plus explicit subject-status update','baseline_files':len(m['files']),'unchanged_files':unchanged,'changed_files':changed,'replaced_live_assets':removed,'old_review_hashes_unchanged':True,'reviewed_candidate_unchanged':'checked exhaustively by check_e1_preservation.py','new_files':'new E1 scripts/render evidence/report/prompt, formatter, generated assets/candidate and exact recovery copies; indexed by current freeze'}
 dump(WB/'checks/stage-e/e1-delta.json',result);print({'status':'pass','baseline':len(m['files']),'unchanged':unchanged,'changed':len(changed),'replaced_live_assets':len(removed)})
if __name__=='__main__':check()
