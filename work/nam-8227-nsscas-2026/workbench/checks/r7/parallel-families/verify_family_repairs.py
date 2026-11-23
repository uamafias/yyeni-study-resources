"""Run from any cwd; in-memory AUTHOR checks, never rewrite canonical outputs."""
import copy,json,sys,hashlib,gzip
from pathlib import Path
W=Path(__file__).resolve().parents[3];sys.path.insert(0,str(W/'tools'))
import apply_textbook_family_repairs_r7 as repair
families=json.loads(gzip.decompress((W/'checks/r7/parallel-families/assembled-r6-baseline.json.gz').read_bytes()))['families']
items=json.loads((W/'analysis/textbook-inventory.json').read_text())['items']
first=copy.deepcopy(families);a=repair.apply(first,items,wb=W)
second=copy.deepcopy(families);b=repair.apply(second,items,wb=W)
assert first==second and a==b
results={}
def negative(name,mutator):
 x=copy.deepcopy(first);mutator(x)
 try:repair.validate(x,items,wb=W)
 except AssertionError as e:results[name]={'result':'failed as required','message':str(e)}
 else:raise AssertionError('seed unexpectedly passed: '+name)
negative('doubled sibling prefix',lambda fs:fs[0].update(distinction_basis='Compared with x: Compared with x: bad'))
negative('empty family missing disposition reason',lambda fs:next(f for f in fs if f.get('empty_demand_disposition_r7'))['empty_demand_disposition_r7'].update(reason=''))
negative('unjustified family demand exception',lambda fs:next(m for f in fs for m in f['members'] if m.get('family_response_demand_evidence_r7')).pop('family_response_demand_evidence_r7'))
negative('lost source response',lambda fs:fs[0]['members'][0]['part_labels'].pop())
print(json.dumps({'deterministic_in_memory_double_apply':'pass','positive':repair.validate(first,items,wb=W),'negative_fixtures':results},indent=2))
