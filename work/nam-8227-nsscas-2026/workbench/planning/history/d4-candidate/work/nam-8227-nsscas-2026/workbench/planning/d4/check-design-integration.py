"""Cross-file consistency receipt for D4; educational review remains independent."""
import json,hashlib,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=read(P/'pilot-design.json');reg=read(P/'part-evidence-register.json');by={x['qualified_part_id']:x for x in reg['parts']};seen=[];classification=[]
def visit(o):
 if isinstance(o,dict):
  for k,v in o.items():
   if k=='classification_version':classification.append(v)
   else:visit(v)
 elif isinstance(o,list):
  for v in o:visit(v)
for n in ['visual-design.json','calculus-design.json','trig-model-design.json']:
 assert m['inputs'][n]==sha(P/n),('stale merge input',n)
 for r in read(P/n)['recipes']:
  rid=r['recipe_id'];mr=next(x for x in m['recipes']if x['recipe_id']==rid);assert mr['version']==r.get('version',r.get('proposed_version'))=='0.1.4'
  for b in r['branches']:
   slug=b['branch_id'].split(':')[-1];mb=next(x for x in mr['branches']if x['branch_id'].split(':')[-1]==slug)
   for q in b['part_specs']:
    local=q.get('local_part_id',q['part_id'].split(':')[-1]);qid=rid+':'+slug+':'+local;rr=by[qid];mq=next(x for x in mb['part_specs']if x['qualified_part_id']==qid)
    for k in ['directly_assessed_demand_ids','prerequisite_demand_ids','marks','response_format','misread_policy']:assert rr[k]==mq[k]==q.get(k,[]),(qid,k)
    for k in ['conditional_directly_assessed_demand_ids','conditional_other_directly_assessed_objective_ids']:assert rr.get(k,{})==mq.get(k,{})==q.get(k,{}),(qid,k)
    primary=q.get('primary_objective_id',q.get('primary_assessed_objective_id'));assert rr['primary_objective_id']==mq['primary_objective_id']==primary
    assert set(rr['other_directly_assessed_objective_ids'])==set(q['directly_assessed_objective_ids'])-{primary}
    level=q['bloom']['level']if isinstance(q['bloom'],dict)else q['bloom'];assert rr['proposed_bloom_level']==level==mq['proposed_bloom_level']
    bl=q['bloom'];cr=q.get('bloom_criterion_ids',q.get('fully_qualified_criterion_ids',q.get('criterion_ids',bl.get('criterion_ids',[])if isinstance(bl,dict)else [])));why=q.get('bloom_rationale',bl.get('rationale')if isinstance(bl,dict)else None)
    assert rr['criterion_ids']==cr and rr['rationale']==why,(qid,'stale part evidence')
    if n=='visual-design.json':assert any(k.startswith('answer_only')for k in q),(qid,'missing visual answer-only fields')
    assert ((q['misread_policy'].get('policy_id')=='MR03-D4') if isinstance(q['misread_policy'],dict) else ('OD-6' in q['misread_policy'])),(qid,'missing OD-6')
    seen.append(qid)
   assert mb['marks_total']==sum(q['marks']for q in b['part_specs'])
 visit(read(P/n))
visit(m);visit(reg);assert set(classification)=={'8227-pilot-design-0.1.1'}
assert len(seen)==len(set(seen))==len(reg['parts'])==27
assert m['counts']['whole_choice_bloom_counts']=={'3':13,'4':1}
assert m['counts']['objectives_with_unconditional_facets']==25 and m['counts']['objectives_with_conditional_only_facets']==1
trap=next(r for r in m['recipes']if r['recipe_id']=='WB8227-trapezium-sketch-estimate')['branches'][0];assert trap['capacity_record']['strict_wholly_fresh_upper_bound']==2
policy=trap['original_subtask_policy'];assert policy['examination_reference']['relation']=='original'and policy['whole_question_is_original']is False
source=read(P/'d4/coverage-check.json');assert source['result']=='pass'and source['all138_agree']
inputs=[P/n for n in ['visual-design.json','calculus-design.json','trig-model-design.json','pilot-design.json','part-evidence-register.json','coverage-plan.json','d4/coverage-check.json','OWNER-CHECKPOINT.md']]+[W/'app-change-handoff.md',W/'subject-rules.md',W/'recipe-contract.md']
result=dict(status='pass',parts_compared=27,choices_compared=14,recipes_compared=9,classification_versions=sorted(set(classification)),counts=m['counts'],original_subtask_guard='h2sketch original-part only; mathematical packing3, generated-fresh2',inputs={str(p.relative_to(W)):sha(p)for p in inputs},scope='All parts compared canonical→merge→register; active input hashes refreshed after final app handoff. This is structural author audit, not independent educational/runtime acceptance.')
(W/'checks/plan-repair-d4-part-register-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ['inputs','counts']},indent=2))
