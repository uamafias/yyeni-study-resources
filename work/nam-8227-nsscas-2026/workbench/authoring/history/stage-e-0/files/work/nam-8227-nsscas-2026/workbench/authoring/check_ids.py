"""Compare runtime evidence identities to the owner-approved branch specifications."""
from build_source import load_source,WB,P,dump,read
p=load_source().create_provider();receipt=[]
register={r['qualified_part_id']:r for r in read(P/'part-evidence-register.json')['parts']}
for native in p.list_native_recipes():
 q=p.generate(native['selection_id'],1,42)
 for part,spec in zip(q['parts'],native['part_specs']):
  expected=spec.get('fully_qualified_criterion_ids') or spec.get('criterion_ids') or [c['criterion_id']for c in spec.get('criteria',[])] or register[part['part_id']]['criterion_ids']
  actual=[c['criterion_id']for c in part['criteria']]
  assert expected and expected==actual,(q['selection_id'],part['part_id'],expected,actual)
  assert part['proposed_marks']==spec['marks']
  receipt.append({'part_id':part['part_id'],'criterion_ids':actual,'marks':part['proposed_marks']})
assert len(receipt)==27
result={'status':'pass','parts':receipt,'assessed_part_slots':len(receipt),'branch_marks':sum(p['marks']for p in receipt)}
dump(WB/'checks/stage-e/identity.json',result);print({'status':'pass','parts':len(receipt),'branch_marks':result['branch_marks']})
