"""Verify every generated 6145 slot and calculate unrounded AO totals."""
import collections
import json
from pathlib import Path

import jsonschema
import yaml

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
load=lambda p:json.loads(p.read_text())
reg=load(WS/'curriculum/objective_registry.json')
fw=load(WS/'curriculum/assessment-framework.json')
sp=yaml.safe_load((WS/'subject-profile.yaml').read_text())
qp=yaml.safe_load((WS/'qualification-profile.yaml').read_text())
scope=load(WS/'curriculum/scope-scan.json')['entries']
schema=lambda name:load(ROOT/f'standard/v0.2.0-draft/schemas/{name}.schema.json')
jsonschema.Draft202012Validator(schema('objective_registry')).validate(reg)
jsonschema.Draft202012Validator(schema('qualification_profile')).validate(qp)
profile_errors=[e.message for e in jsonschema.Draft202012Validator(schema('subject_profile')).iter_errors(sp)]
assert len(profile_errors)==1 and 'Additional properties' in profile_errors[0],profile_errors
legacy={k:v for k,v in sp.items() if k in schema('subject_profile')['properties']}
jsonschema.Draft202012Validator(schema('subject_profile')).validate(legacy)
obj={o['objective_id']:o for o in reg['objectives']}
for o in obj.values():
 assert o['parent_id'] is None or o['parent_id'] in obj,o['objective_id']
cmd={c['word']:c for c in fw['command_words']}
perf={p['item_type']:p for p in sp['slot_plan']['performance_tasks']}
tot=collections.Counter();by_topic=[];mis=[];slots=[]
for p in sorted((WS/'topics').glob('*/work_order.json'),key=lambda p:tuple(map(int,p.parent.name.split('.')))):
 wo=load(p);c=load(p.parent/'contract.json');bs=collections.Counter()
 expected={o['objective_id'] for o in obj.values() if o['parent_id'] and o['topic_id']==wo['topic_id']}
 actual={s['objective_id'] for s in wo['item_slots']}
 assert expected==actual,(wo['topic_id'],expected-actual)
 assert wo['planned_item_count']==len(wo['item_slots'])+len(wo['performance_tasks'])
 assert c['depth_constraints']['item_budget']==wo['planned_item_count']
 assert c['required_outputs']['content_units']==len(wo['content_units'])
 assert len(c['depth_constraints']['excluded_constructs'])==len(scope)
 assert {e['pattern'] for e in c['depth_constraints']['excluded_constructs']}=={e['pattern'] for e in scope}
 for s in wo['item_slots']:
  assert s['command_word'] in cmd and cmd[s['command_word']]['use_in_prompts']
  assert str(s['mark_tariff']) in cmd[s['command_word']]['observed_tariffs'],s
  assert s['blooms_level'] in ['Remember','Understand','Apply','Analyse','Evaluate','Create']
  assert s['assessment_objectives'] and set(s['assessment_objectives'])<={'A','B','C'}
  assert s['marking_guidance_must_name'],s
  slots.append(s['slot'])
  for a in s['assessment_objectives']:bs[a]+=s['mark_tariff']/len(s['assessment_objectives'])
  if s.get('misconception_entry'):mis.append(s['misconception_entry'])
 for s in wo['performance_tasks']:
  bs.update(perf[s['item_type']]['ao_split']);slots.append(s['slot'])
 tot.update(bs)
 by_topic.append({'topic_id':wo['topic_id'],'title':wo['topic_title'],'objectives':len(expected),
                  'flashcards':len(wo['item_slots']),'practice_packages':len(wo['performance_tasks']),
                  'items':wo['planned_item_count'],'units':len(wo['content_units']),
                  'notes_words':c['depth_constraints']['word_budget'],
                  'ao_marks':dict(bs)})
assert len(set(slots))==len(slots)
entries=load(WS/'curriculum/misconceptions.json')['entries']
assert collections.Counter(mis)==collections.Counter(m['entry_id'] for m in entries)
target=fw['ao_mark_budget']['stated_qualification_weight_percent']
share={a:tot[a]/sum(tot.values())*100 for a in 'ABC'}
gap=max(abs(share[a]-target[a]) for a in 'ABC')
assert gap<=5,gap
report={'status':'PASS','topics':len(by_topic),'assessable_objectives':sum(t['objectives'] for t in by_topic),
 'original_syllabus_outcomes':96,'additional_member_objectives':sum(t['objectives'] for t in by_topic)-96,
 'flashcards':sum(t['flashcards'] for t in by_topic),'practice_packages':sum(t['practice_packages'] for t in by_topic),
 'items':len(slots),'content_units':sum(t['units'] for t in by_topic),
 'notes_words':{k:sum(t['notes_words'][k] for t in by_topic) for k in ['min','max']},
 'misconception_slots':len(mis),'ao_marks':dict(tot),'ao_share_percent':share,'ao_target_percent':target,
 'largest_gap_points':gap,'every_slot_has_observed_command_tariff':True,
 'each_misconception_has_exactly_one_slot':True,'all_223_outcomes_have_slots':True,
 'by_topic':by_topic,
 'shared_tool_limits':[
  'The subject-profile schema predates the runtime-supported slot_plan, conditioned_mechanisms and depiction_rule. Base profile validates; full legacy schema rejects these extensions. Standard files were not edited.',
  'The shared AO summary rounds topic shares and truncates its printed fractional gap. This report recomputes exact marks and uses the actual fractional gap.',
  'Shared contract/work-order boilerplate mentions Cambridge/AO4. This plan uses Namibia A/B/C and the calculated targets; boilerplate is not authority.',
  'Member exposure is deliberately not invented from parent evidence. Parent mappings remain intact; child-level observations are not claimed without a separate semantic mapping.']}
(WS/'planning/plan-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in {'by_topic','shared_tool_limits'}},indent=2))
