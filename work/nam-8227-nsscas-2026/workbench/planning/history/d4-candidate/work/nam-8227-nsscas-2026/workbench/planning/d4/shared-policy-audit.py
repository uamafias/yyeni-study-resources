"""Read-only D4 shared policy and fixed-ledger consistency audit.

Same-author-team inspection, not cross-vendor acceptance or runtime marking.
"""
import argparse,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
policy=read(P/'d4/shared-misread-policy.json');line=policy['work_order_line'];wos=sorted((W/'work-orders').glob('*.md'));assert len(wos)==9
wo_checks=[]
bad_phrases=['deduct nothing and do not defer','never deferred when none is earned','no deduction is made or carried into a later part','unless the actual scheme specifies an order','If the first-use part earns no A/B, deduct nothing there or later']
for p in wos:
 text=p.read_text();assert text.count(line)==1,('shared work-order line differs',p)
 assert not any(x in text for x in bad_phrases),('withdrawn no-deferral or exception text remains',p)
 wo_checks.append(dict(path=str(p.relative_to(W)),shared_line_exact=True,line=next(i for i,x in enumerate(text.splitlines(),1)if line in x)))
rules=(W/'subject-rules.md').read_text();mr=next(x for x in rules.splitlines()if x.startswith('| D1-MR03:'))
for needle in ['Binding OD-6 principle','Separate proposed operational interpretation','MR03-OPS-D4','pending Vitalis','moving to later-use parts','remains earned for every DM','canonical in every later part','designed no-real-solution','Practice feedback names the misread']:
 assert needle in mr,('MR03 missing',needle)
checks=[];sourcepaths=[]
keys=['policy_id','owner_principle_id','owner_principle','operational_policy_id','operational_status','operational_rules','feedback','ledger_fields','sources']
for name in ['visual-design.json','calculus-design.json','trig-model-design.json']:
 path=P/name;sourcepaths.append(path)
 for r in read(path)['recipes']:
  for b in r['branches']:
   for q in b['part_specs']:
    p=q['misread_policy'];assert isinstance(p,dict),(name,q['part_id'])
    for key in keys:assert p[key]==policy[key],(name,q['part_id'],key)
    assert p['owner_principle_id']=='OD-6'and p['operational_policy_id']=='MR03-OPS-D4'
    assert 'proposed'in p['operational_status']and'pending'in p['operational_status']
    checks.append(dict(recipe_id=r['recipe_id'],branch_id=b['branch_id'],part_id=q['part_id'],same_shared_policy=True))
assert len(checks)==27
examplepaths=sorted((W/'exemplars').glob('*.md'));assert len(examplepaths)==9
for p in examplepaths:
 assert not any(x in p.read_text()for x in bad_phrases),('withdrawn example operational text remains',p)
paths=[W/'subject-rules.md',P/'d4/shared-misread-policy.json',P/'d4/misread_ledger.py',*wos,*examplepaths,*sourcepaths]
result=dict(status='pass',role='Codex parallel planner audit; same author team',work_orders_checked=9,part_policies_checked=27,work_order_checks=wo_checks,part_checks=checks,manual_conclusions=['Owner principle is distinct from proposed per-datum/order/eligibility/dependency mechanics.','All nine work orders copy the same declared policy line; all 27 policy objects preserve its exact owner/operational split and feedback.','No first-part-only no-deduction exception or trig-only scheme-order override remains in the inspected live work orders/exemplars.','Eligibility is once-only, ineligible data stay canonical, and gross evidence remains earned after the net MR deduction.','Question-data no-solution exclusion preserves a designed no-real-solution outcome.'],input_hashes={str(p.relative_to(W)):sha(p)for p in paths},limits='Text and explicit fixed-fixture evidence only; does not prove marker recognition, app behaviour, educational acceptance, or undiscovered semantic edge cases. Final independent review and Vitalis approval remain pending.')
out=P/'d4/shared-policy-audit.json';text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
if args.check:assert out.read_text()==text,'shared policy audit inputs changed; re-inspect before refreshing'
else:out.write_text(text)
print(json.dumps(dict(status='pass',work_orders=9,policies=27,input_files=len(paths))))
