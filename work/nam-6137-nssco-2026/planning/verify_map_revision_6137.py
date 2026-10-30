"""Read-only verification of the approved two-map delta; no content regeneration."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a=read(W/'planning/map-revision-01-approval-6137.json');p=read(W/'planning/visual-resource-plan-6137.json');old=W/'planning/revisions/map-revision-01-before-6137';base=read(old/'visual-resource-plan-6137.json');original=read(old/'plan-approval-manifest-6137.json')
 assert a['approved'] and a['approved_by']=='Vitalis P Haupindi' and a['approval_evidence']
 assert sha(W/'planning/visual-resource-plan-6137.json')==a['active_visual_plan_sha256']
 assert sha(old/'visual-resource-plan-6137.json')==a['previous_visual_plan_sha256']
 assert sha(old/'plan-approval-manifest-6137.json')==a['original_approval_manifest_sha256']
 assert sha(W/'planning/plan-approval-manifest-6137.json')==a['original_approval_manifest_sha256']
 assert p['resources'][:54]==base['resources'] and len(p['resources'])==56
 assert sum(r['kind']=='licensed_photo' for r in p['resources'])==6
 slots={};cardcount=packages=0
 for td in (W/'topics').iterdir():
  wo=read(td/'work_order.json');cardcount+=len(wo['item_slots']);packages+=len(wo['performance_tasks'])
  assert sha(td/'contract.json')==original['files'][str((td/'contract.json').relative_to(W))]
  assert sha(td/'work_order.json')==original['files'][str((td/'work_order.json').relative_to(W))]
  for s in wo['item_slots']+wo['performance_tasks']:assert s['slot'] not in slots;slots[s['slot']]=s
 assert (cardcount,packages,len(slots))==(737,64,801)
 for path,digest in a['active_document_hashes'].items():assert sha(W/path)==digest
 assert sha(W/'authoring/MAP-REPAIR-PROPOSALS-6137.md')==a['proposal_sha256']
 ids=set();bound=set()
 for r in p['resources']:
  assert r['resource_id'] not in ids;ids.add(r['resource_id']);assert r['assigned_item_id'] in slots
  if r.get('scope_revision')=='map-revision-01':
   for iid in r['approved_binding_item_ids']:assert iid in slots;bound.add(iid)
   n=read(W/'topics'/r['topic_id']/'authoring_notes.json');c=next(c for c in n['scope_concerns'] if r['assigned_item_id'] in c['affected_items'])
   assert c['resolution']['resource_id']==r['resource_id'] and c['resolution']['approved_by']==a['approved_by'] and c['resolution']['approval_evidence']==a['approval_evidence']
 assert bound==set(a['item_ids']) and len(bound)==5
 print('PASS: 56 resources; original 54 unchanged; 2 approved additions / 5 existing cards; 801 slots and all contract/work-order hashes unchanged. Assets not yet authored or accepted.')
if __name__=='__main__':main()
