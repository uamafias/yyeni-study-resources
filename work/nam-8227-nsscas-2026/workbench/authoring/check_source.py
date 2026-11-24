"""Integration checks. Mathematical recomputation lives in the separate group audits."""
from copy import deepcopy
import hashlib,json,re,sys,tempfile,random
from pathlib import Path
from build_source import load_source,WB,S,dump

def must_fail(name,call,receipts):
 try:call()
 except (ValueError,AssertionError,KeyError,TypeError):receipts.append(name);return
 raise AssertionError('Negative fixture accepted: '+name)
def check():
 module=load_source();initial_random_state=random.getstate();p=module.create_provider();rows=p.list_recipes();negative=[];frozen=[];tested=0;seen=set();all_keys={};branches=[]
 assert len(rows)==14 and len({r['recipeId']for r in rows})==9
 for row in rows:
  _,c=p._choice(row['id']);keys=set();semantics=set();asset_roles=set()
  for i in range(len(c['parameters'])):
   q=p.generate_at(row['id'],i)
   assert p.validate_instance(q)['valid']
   assert q['recipe_version']=='0.1.5'and q['generator_version']==2
   assert q['proposed_total_marks']==row['marks']
   assert all(q[k]for k in ('objective_ids','demand_ids','exposure_keys'))
   assert len({x['part_id']for x in q['parts']})==len(q['parts'])
   assert all(x['part_id'].startswith(q['recipe_id']+':')for x in q['parts'])
   # Inspect strings directly; decoding JSON escapes would manufacture controls.
   def strings(v):
    if isinstance(v,str):yield v
    elif isinstance(v,dict):
     for x in v.values():yield from strings(x)
    elif isinstance(v,list):
     for x in v:yield from strings(x)
   assert not any(re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',x)for x in strings(q))
   for part in q['parts']:
    assert part['worked_steps']and all(all(step[k].strip()for k in ('action','reason','result'))for step in part['worked_steps'])
   semantics.add(q['semantic_fingerprint']);keys.update(q['exposure_keys']);tested+=1
   for a in q['assets']:
    ref=a['reference'];role=ref['role'];asset_roles.add(role)
    assert a['target_part_ids']and set(a['target_part_ids'])<=set(x['part_id']for x in q['parts'])
    assert p.resolve_asset(ref['asset_id'],ref['sha256'],role)
    assert p.asset_for_instance(q,ref['asset_id'],ref['sha256'],role,solution_revealed=role=='solution')
   pre=module.learner_projection(q,mode='practice');test=module.learner_projection(q,mode='test')
   assert 'practice_help'in pre and 'practice_help'not in test
   for public in (pre,test):
    assert not {'parameters','generator_seed','private_math','grading_contract','marking_memo','instance_hash','worked_steps','reference_answer'}&public.keys()
    assert all(a['reference']['role']=='question'for a in public['assets'])
    assert all(not {'source_path','source_sha256','verified_by'}&r.keys()for r in public['examination_references'])
    assert all(r['scope']=='part'and r['target_part_ids']and set(r['target_part_ids'])<=set(p['part_id']for p in public['parts'])for r in public['examination_references'])
   shown=module.learner_projection(q,reveal=True)
   assert len(shown['solution'])==len(q['parts'])
  assert len(semantics)==len(c['parameters'])
  all_keys[row['id']]=keys
  exhausted=p.generate_fresh(row['id'],0,keys,mode='test')
  assert exhausted['status']=='exhausted'and exhausted['question']is None
  repeated=p.generate_fresh(row['id'],0,keys,allow_repeat=True)
  assert repeated['status']=='repeated-practice'and repeated['fresh']is False
  for seed in (0,42,2**63-1):
   q=p.generate(row['id'],2,seed);assert q==p.generate(row['id'],2,seed)
   name=row['id'].replace(':','--')+'--seed-'+str(seed)+'.json';dump(S/'examples'/name,q);frozen.append(name)
  q=p.generate(row['id'],2,42);bad=deepcopy(q);bad['parts'][0]['reference_answer']='seeded corruption'
  assert not p.validate_instance(bad)['valid'];negative.append(row['id']+':altered-frozen-answer')
  bad=deepcopy(q);bad['parts'][0]['criteria'][0]['marks']+=1
  assert not p.validate_instance(bad)['valid'];negative.append(row['id']+':altered-tariff')
  must_fail(row['id']+':test-repeat',lambda:p.generate_fresh(row['id'],0,keys,mode='test',allow_repeat=True),negative)
  must_fail(row['id']+':test-early-reveal',lambda:module.learner_projection(q,mode='test',reveal=True),negative)
  branches.append(dict(selection_id=row['id'],parameter_rows=len(c['parameters']),semantic_fingerprints=len(semantics),exposure_key_count=len(keys),asset_roles=sorted(asset_roles),exhaustion='passed'))
 for seed in (-1,True,2**63,1.25,'42'):
  must_fail('invalid-seed-'+str(seed),lambda seed=seed:p.generate(rows[0]['id'],2,seed),negative)
 must_fail('unknown-selection',lambda:p.generate('not-a-reviewed-choice',2,0),negative)
 must_fail('unreviewed-transport-version',lambda:p.generate(rows[0]['id'],1,0),negative)
 for old in ('0.1.1','0.1.2','0.1.3','0.1.4','0.1.5'):
  assert module.normalized_exposure('key@'+old+':datum')=='key:datum'
 # A version/seed change cannot make an already exposed implicit curve fresh.
 grad=next(r for r in rows if r['id'].endswith(':implicit-normal:gradient'));norm=next(r for r in rows if r['id'].endswith(':implicit-normal:normal'))
 q=p.generate_at(grad['id'],0);_,nc=p._choice(norm['id'])
 common=[p.generate_at(norm['id'],i)for i in range(len(nc['parameters']))if nc['parameters'][i]==q['parameters']]
 assert common and set(q['exposure_keys'])&set(common[0]['exposure_keys'])
 # Asset role and instance binding, independently of the app's caller permissions.
 aq=next(p.generate(r['id'],2,0)for r in rows if r['id'].endswith(':logarithmic-hence-chain'))
 sol=next(a['reference']for a in aq['assets']if a['role']=='solution')
 must_fail('solution-asset-before-reveal',lambda:p.asset_for_instance(aq,sol['asset_id'],sol['sha256'],'solution'),negative)
 must_fail('solution-asset-as-question',lambda:p.resolve_asset(sol['asset_id'],sol['sha256'],'question'),negative)
 other=p.generate(grad['id'],2,0)
 must_fail('cross-instance-asset',lambda:p.asset_for_instance(other,sol['asset_id'],sol['sha256'],'solution',solution_revealed=True),negative)
 must_fail('asset-wrong-hash',lambda:p.resolve_asset(sol['asset_id'],'0'*64,'solution'),negative)
 # Conditional scope is resolved privately and never disclosed as an answer cue.
 pi=next(r for r in rows if r['id'].endswith(':solve-or-explain'));_,pc=p._choice(pi['id']);outcomes={}
 for i in range(len(pc['parameters'])):
  q=p.generate_at(pi['id'],i);kind=q['private_math']['outcome'];outcomes[kind]=outcomes.get(kind,0)+1
  assert ('8227:2020:M1:T6:O03:D01'in q['demand_ids'])==(kind=='real-solution')
  assert 'conditional_direct_demand_ids'not in module.learner_projection(q)
 assert set(outcomes)=={'real-solution','no-real-solution'}
 assert random.getstate()==initial_random_state,'Generator mutated global random state'
 result=dict(status='pass',scope='author integration; independent mathematics in group reports; not cross-vendor/app acceptance',parameter_rows_tested=tested,frozen_examples=len(frozen),negative_fixtures_rejected=len(negative),negatives=negative,branches=branches,principal_outcomes=outcomes)
 dump(WB/'checks/stage-e/integration.json',result);print(json.dumps({k:v for k,v in result.items()if k not in ('negatives','branches')},indent=2))
if __name__=='__main__':check()
