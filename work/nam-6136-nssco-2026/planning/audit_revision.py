"""Source-demand and regression audit for the Claude-reviewed plan revision.

These checks establish concrete corrections/coverage, not the educational truth
of future authored prose. Preserve the original Claude verdict unchanged.
"""
import json,re
from pathlib import Path
from collections import Counter
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads((W/p).read_text())
facts=read('curriculum/syllabus-facts.json');reg=read('curriculum/objective_registry.json')['objectives']
slots=read('curriculum/slot-demand-specs.json')['slots'];packs=read('curriculum/performance-slot-specs.json')['slots']
d=read('curriculum/objective-demand.json')['objectives'];v=read('planning/plan-validation.json')
assert len(slots)==len({x['slot'] for x in slots})
commands=Counter(x['command_word'] for x in slots)
source_checks=[]
for topic in facts['content_outline']:
 for n,b in enumerate(topic['specific_objectives'],1):
  key=f'{topic["id"]}:{n}'
  if key=='3.1:11':continue
  ss=[x for x in slots if x['source_bullet_key']==key]
  assert ss,key
  sub={x['subtype'] for x in ss}
  for pattern,needed in [(r'\bdefine\b','DEF'),(r'\b(?:assess|evaluate)\b','EVAL'),(r'\b(?:differentiate|distinguish)\b','DIST')]:
   if re.search(pattern,b['text']):assert needed in sub,(key,needed)
  source_checks.append(key)
assert commands['Define']>=30 and commands['Calculate']>=10
assert commands['Differentiate']+commands['Compare']>=10
assert commands['Discuss']<commands['Explain']
assert not any('explain and apply' in o['learner_objective'].lower() for o in reg)
for s in slots:
 if s['subtype']=='INTERP':assert 'self-contained' in s['task_requirement'] and 'inferred' in s['task_requirement']
 if s['subtype']=='CHAIN':assert 'two material facts' in s['task_requirement']
 if s['subtype']=='EVAL':assert 'criterion' in s['task_requirement'] and 'alternatives' in s['task_requirement']
 if s['subtype']=='CALC':assert s['calculation_target']
for tid in ['1.1','3.1','4.2','6.2','7.1','7.2','7.3','9.1']:
 assert any(s['subtype']=='CALC' and s['objective_id'].split('-')[2].startswith(tid+'.') for s in slots),tid
research=[p for p in packs if p['topic_id']=='10.1']
assert len(research)==4 and len({tuple((x['command_word'],x['mark_tariff']) for x in p['subparts']) for p in research})==4
community=[]
for p in research:
 assert p['section_totals']['A1']+p['section_totals']['A2']==35 and p['section_totals']['B']==15
 text=' '.join(x['purpose'] for x in p['subparts'] if x['section']=='A2').lower()
 if 'funding' in text:
  assert 'aims' in text and 'organise' in text and ('problem' in text or 'obstacle' in text)
  community.append(p['cycle'])
assert len(community)>=2
for topic in ['3.1','10.1']:
 items=read(f'exemplar/proof/work/nam-6136-nssco-2026/topics/{topic}/learning-items/topic_{topic}_items.json')['items']
 for i in items:
  guide=' '.join(i['marking_guidance']).lower()
  if topic=='3.1':assert not re.search(r'pilot|questionnaire|volunteer|water.journey',guide),i['item_id']
  else:assert not re.search(r'cloth|sewing|machine|capital good',guide),i['item_id']
byid={o['objective_id']:o for o in reg}
for o in reg:
 assert set(o['related_ids'])<=set(byid) and set(o['prerequisite_ids'])<=set(byid)
seen=set();active=set()
def visit(oid):
 assert oid not in active,oid
 if oid in seen:return
 active.add(oid)
 for prev in byid[oid]['prerequisite_ids']:visit(prev)
 active.remove(oid);seen.add(oid)
for oid in byid:visit(oid)
assert sum(bool(o['related_ids']) for o in reg)>=10
assert 'date' in byid['OBJ-6136-10.1.02-04']['learner_objective']
mis={s.get('misconception_entry'):s for s in slots if s['subtype']=='MISCON'}
assert mis['MISCON-6136-011']['assessment_objectives']==['B']
assert mis['MISCON-6136-028']['assessment_objectives']==['D']
assert len(v['relative_shortfall_percent'])==4 and v['exact_largest_gap_points']<=5
out={'status':'PASS for enumerated revision checks; not a fresh Claude verdict',
     'source_outcomes_checked':len(source_checks),'command_counts':dict(commands),
     'flashcards':len(slots),'performance_packages':len(packs),'research_packages':len(research),
     'community_project_cycles':community,'related_targets':sum(bool(o['related_ids']) for o in reg),
     'exact_ao_percent':v['exact_ao_percent'],'relative_shortfall_percent':v['relative_shortfall_percent'],
     'original_review':'FIX PLAN FIRST; retained unchanged',
     'remaining_limits':['Actual authored questions still require semantic review against their slot demand.',
                        'Standard-owner schema/runner/graph issues remain explicit.','No standalone mark schemes; no official item-level allocations invented.']}
(W/'planning/revision-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
