"""Regression audit of the substantive omissions identified in Claude review r1."""
import collections
import json
import re
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
def read(p):return json.loads((WS/p).read_text())
reg=read('curriculum/objective_registry.json')['objectives']
work={p.parent.name:json.loads(p.read_text()) for p in (WS/'topics').glob('*/work_order.json')}
allslots=[s for w in work.values() for s in w['item_slots']]
by_object=collections.defaultdict(set)
for s in allslots:by_object[s['objective_id']].add(s['subtype'])
def oid(local):
    tid,number=local.rsplit('.',1)
    return f'OBJ-6145-{tid}-{int(number):02}'
def family(root):return [o['objective_id'] for o in reg if o['objective_id']==root or o['objective_id'].startswith(root+'-M')]
checks=[]
for local in ['1.2.2','1.3.3','2.3.5','4.3.1','6.2.2','6.2.3','8.1.1','9.1.1']:
    fs=family(oid(local));assert any(by_object[o]&{'MECH','EVAL'} for o in fs),local
checks.append('Lost list demands restored to explanatory/evaluative slots on parent or explicit members.')
for n in reg:
    if n['parent_id'] and n['parent_id'].count('-')==2 and re.search(r'\bevaluate\b',n['syllabus_text'],re.I):
        assert any('EVAL' in by_object[o] for o in family(n['objective_id'])),n['objective_id']
checks.append('Every original explicitly evaluative bullet has C evaluation practice, including all three financial-institution members.')
for local in ['5.3.1','5.3.2','5.3.3','8.2.1']:
    assert 'CALC' in by_object[oid(local)],local
assert 'DEF' in by_object[oid('7.1.1')]
assert 'DIAGRAM' in by_object[oid('1.1.2')]
assert sum(s['subtype']=='CALC' for s in work['3.3']['item_slots'])==2
checks.append('Cost/revenue/output, income-per-person, RPI definition and opportunity-cost illustration restored; exactly two elasticity calculations remain.')
for s in allslots:
    if s['subtype']=='DEF':
        title=s['objective_title'].lower()
        assert not any(x in title for x in ['functions of money','qualities of money','types of money','income-group','government as','changes in demand conditions','changes in supply conditions','aims of trade unions']),s['slot']
checks.append('No reviewed non-term objective retains a DEF slot.')
for tid in ['3.1','3.4','6.1','7.3']:
    assert len(work[tid]['performance_tasks'])==2
    assert work[tid]['performance_tasks'][1]['item_type']=='case_analysis'
    required=work[tid]['performance_tasks'][1]['marking_guidance_must_name']
    assert not any('judgement' in x or 'both sides' in x for x in required)
    assert all('C' not in s['assessment_objectives'] for s in work[tid]['performance_tasks'])
for tid,w in work.items():
    ps=w['performance_tasks'];assert len({p['command_word'] for p in ps[0]['part_specs']})>1
    for p in ps:
        assert p['objective_ids'] and p['objective_selection_note'].startswith('Demand-led')
        for part in p['part_specs']:assert part['demand'] and part['objective_ids']
assert 'OBJ-6145-6.2-05' in work['6.2']['performance_tasks'][1]['objective_ids']
assert 'OBJ-6145-6.2-06' in work['6.2']['performance_tasks'][1]['objective_ids']
checks.append('Composite anchors and short-part content are explicit; no evaluation is forced on the four descriptive topics; taxes/budget and interest rate are included.')
ex=read('exemplar/topics/1.1/learning-items/topic_1.1_items.json')['items']
assert all(i['context']['facts'] for i in ex)
assert all('credit a relevant, distinct element' not in ' '.join(i['marking_guidance']) for i in ex)
for p in work['1.1']['performance_tasks']:
    item=next(i for i in ex if i['item_id']==p['slot'])
    assert item['objective_ids']==p['objective_ids']
    assert item['mark_tariff']==p['mark_tariff'] and item['command_word']==p['command_word']
assert read('exemplar/shape-slices/validation.json')['result']=='PASS'
checks.append('Exemplar guidance is concrete, context is present, performance metadata agrees and risky shape slices pass their independent numeric/schema checks.')
terms={t['term'] for t in read('curriculum/glossary.json')['terms']}
assert {'complementary goods','substitute goods','production possibility frontier','short run','long run','law of diminishing returns','normal profit','abnormal profit'}<=terms
assert 'price discrimination' not in terms
assert read('curriculum/jurisdiction-sources.json')['sources']
assert len(read('curriculum/topic-ownership.json')['entries'])>=7
for entry in read('curriculum/scope-scan.json')['entries']:
    assert all(re.search(entry['pattern'],x,re.I) for x in entry['controls']['must_catch'])
    assert not any(re.search(entry['pattern'],x,re.I) for x in entry['controls']['must_allow'])
checks.append('Glossary gaps/rulings, verified jurisdiction constraints, semantic ownership and tested level boundaries are present.')
out={'result':'PASS','checks':checks,'limits':['Semantic adequacy of the actual economics remains a reviewer judgement; these controls establish that the specific structural omissions do not recur.','No full-topic publication claim is made for thin shape slices.']}
(WS/'review/plan-claude-r1/repair-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
