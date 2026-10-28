"""Repair duplicate derived counts without rebuilding approved slots or touching content."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parents[1];R=W/'planning/revision-01'
load=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 changes=[];scope_hashes={str(p):sha(p) for root in [W,R/'candidate']for p in (root/'topics').glob('*/work_order.json')}
 for root in [W,R/'candidate']:
  for wp in sorted((root/'topics').glob('*/work_order.json')):
   wo=load(wp);n=len(wo['item_slots'])+len(wo['performance_tasks']);assert n==wo['planned_item_count'];p=wp.parent/'contract.json';c=load(p);before=sha(p);old={'item_budget':c['depth_constraints']['item_budget'],'learning_items':c['required_outputs']['learning_items']}
   if old!={'item_budget':n,'learning_items':n}:
    c['depth_constraints']['item_budget']=n;c['required_outputs']['learning_items']=n;p.write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n');changes.append({'path':str(p.relative_to(W)),'before':old,'after':{'item_budget':n,'learning_items':n},'before_sha256':before,'after_sha256':sha(p),'work_order_sha256':sha(wp)})
 assert all(sha(Path(p))==h for p,h in scope_hashes.items())
 if changes:
  (R/'contract-count-correction.json').write_text(json.dumps({'reason':'Correct the two contract count fields to the already-approved work-order count; no scope or label changes. Preserve original approval/activation hashes as historical evidence.','supersedes':'Only the contract-file hashes listed below from approval-and-activation.json; other activation hashes are unchanged.','work_orders_unchanged':True,'planned_items':sum(load(p)['planned_item_count'] for p in (W/'topics').glob('*/work_order.json')),'changes':changes},indent=2)+'\n')
 print('Contracts corrected:',len(changes),'across live/candidate; approved slots unchanged.')
if __name__=='__main__':main()
