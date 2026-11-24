"""Copy one reviewed D4 policy into authored part specifications, not runtime data."""
import copy,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text())
base=read(P/'d4/shared-misread-policy.json');base.pop('work_order_line')
count=0
def ids(x):
 if isinstance(x,str):return x.replace('@0.1.3:', '@0.1.4:')
 if isinstance(x,list):return [ids(v)for v in x]
 if isinstance(x,dict):return {k:ids(v)for k,v in x.items()}
 return x
for name in ['visual-design.json','calculus-design.json','trig-model-design.json']:
 d=read(P/name)
 for r in d['recipes']:
  if 'version'in r:r['version']='0.1.4'
  if 'proposed_version'in r:r['proposed_version']='0.1.4'
  r['status']='D4 proposed paper design; Claude changed-scope confirmation then Vitalis exact-manifest approval pending'
  for b in r['branches']:
   for q in b['part_specs']:
    policy=copy.deepcopy(base)
    if r['recipe_id']=='WB8227-implicit-normal' and b['branch_id'].split(':')[-1]=='gradient':
     policy['eligibility_notes']='For this standalone gradient branch, judge the printed curve/point consistency, finite gradient and preserved implicit/exponential chain demand. There is no supplied proof target or later part. Apply connected-question MR03 eligibility and the fixed gradient-only fixtures.'
    elif r['recipe_id']=='WB8227-implicit-normal':
     policy['eligibility_notes']='Retain the proposed fixed-point/curve and supplied-target consistency guard. Once a datum is ineligible in the proof, later gradient/normal parts are marked canonically; differentiating a misread constant to zero does not create a new eligibility decision. See the 9/9 and 5/9 D4 fixed-response cases.'
    elif r['recipe_id']=='WB8227-motion-integration' and b['branch_id'].endswith('polynomial-chain'):
     policy['eligibility_notes']='Polynomial branch: preserve acceleration-to-velocity integration, the initial-condition demand and positive-velocity distance evaluation. Eligibility considers both connected parts; the first earned A/B in a using part is charged under proposed MR03 mechanics, even when its own expression is unaffected. Gross S2 remains evidence for S3 after the net deduction.'
    elif r['recipe_id']=='WB8227-motion-integration' and b['branch_id'].endswith('exponential-positive'):
     policy['eligibility_notes']='Exponential branch: preserve the nonunit exponential chain factor and positive-velocity differentiation/integration demands across both parts. A zero-rate or otherwise object-changing misread is canonical throughout; named derivative/primitive coefficient exclusions remain. The V-misread fixtures use whole-question deferred deduction when acceleration earns no A/B.'
    elif r['recipe_id']=='WB8227-motion-integration':
     policy['eligibility_notes']='A misread that changes the sign-change outcome changes the object and stays canonical throughout. A same-outcome coefficient/value misread can be eligible; use gross R2/S2 evidence for dependent accuracy before the net penalty.'
    elif r['recipe_id']=='WB8227-principal-inverse':
     policy['eligibility_notes']='A designed no-real-solution branch is not itself the no-solution exclusion. Target sign misread -3pi/4 to3pi/4 preserves that outcome/demand and earns2/3 for full misread-data work.'
    elif r['recipe_id']=='WB8227-vector-geometry':
     policy['eligibility_notes']='An OA misread that removes every p solution is ineligible in both parts: canonical a1/3+b2/4=3/7. An eligible OB sign misread plus wrong resultant retains gross5/7 and deducts the first later B1, net4/7.'
    else:policy['eligibility_notes']='Apply the once-only whole-question eligibility record and the part-specific mathematical/source constraints. Unsettled detailed edge cases remain explicit E/F acceptance fixtures.'
    q['misread_policy']=policy;count+=1
 d=ids(d)
 if 'exemplar_cases'in d:
  for c in d['exemplar_cases']:c['recipe_version']='0.1.4'
 d['d4_status']='OD-6 principle binding; MR03-OPS-D4 mechanics proposed pending exact-manifest approval.'
 (P/name).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
assert count==27
print('Copied shared MR03-D4 to all27parts; current criterion IDs use0.1.4')
