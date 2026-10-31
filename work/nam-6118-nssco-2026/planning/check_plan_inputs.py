"""Focused Step 4 integration checks, not an independent curriculum review."""
from pathlib import Path
import json,re,collections,hashlib
import jsonschema
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'work/nam-6118-nssco-2026'
def j(p):return json.loads((W/p).read_text())
reg=j('curriculum/objective_registry.json');jsonschema.validate(reg,json.loads((ROOT/'standard/v0.2.0-draft/schemas/objective_registry.schema.json').read_text()));byid={o['objective_id']:o for o in reg['objectives']};fw=j('curriculum/assessment-framework.json');commands={x['word']:x for x in fw['command_words']};evidence=j('assessment-evidence/assessment_evidence.json');budget=j('curriculum/item-budget.json');cross=j('curriculum/source-to-registry-crosswalk.json')['entries']
assert len(cross)==335 and len({c['source_objective_id'] for c in cross})==335
assert all(o['parent_id'] is None or o['parent_id'] in byid for o in reg['objectives'])
assert all(set(r['objective_ids'])<=set(byid) for r in evidence['records'])
assert sum(not r['creditworthy_points'] for r in evidence['records'])==267
assert all('`'+r['evidence_id']+'`' in (W/'assessment-evidence/GAPS.md').read_text() for r in evidence['records'] if not r['creditworthy_points'])
counts=collections.Counter();seen=set();task_contexts=j('curriculum/topic-task-specifications.json')['specifications'];specs={x['topic_id']:x for x in task_contexts}
for d in budget['topics']:
 t=d['topic_id'];wo=j(f'topics/{t}/work_order.json');co=j(f'topics/{t}/contract.json')
 assert len(co['depth_constraints']['excluded_constructs'])==3
 assert len(wo['item_slots'])+len(wo['performance_tasks'])==d['items']==co['required_outputs']['learning_items']
 assert all(not s['reason'].startswith('added to reach') for s in wo['item_slots'])
 for s in wo['item_slots']:
  assert s['objective_id'] in byid
  c=commands[s['command_word']];assert c['use_in_prompts'] and s['mark_tariff'] in c['observed_tariffs'],s
  seen.add(s['objective_id']);counts['flashcards']+=1
 for p in wo['performance_tasks']:
  assert set(p['objective_ids'])<=set(byid)
  assert sum(p['ao_split'].values())==p['mark_tariff']
  if 'parts' in p:
   assert sum(x['marks'] for x in p['parts'])==p['mark_tariff']
   for x in p['parts']:assert x['marks'] in commands[x['command_word']]['observed_tariffs'],(t,x)
  if p['item_type']=='practical_task':
   assert specs[t]['practical_data'] is not None
  counts[p['item_type']]+=1
assert seen=={o['objective_id'] for o in reg['objectives'] if o['parent_id']}
assert sum(counts.values())==budget['totals']['items']==666
assert len(reg['objectives'])==594 and budget['totals']['leaf_objectives']==495
coverage=(W/'curriculum/ao_coverage.md').read_text();gap=int(re.search(r'largest gap (\d+) points',coverage)[1]);assert gap<=5
for a in fw['assessment_objectives']:assert a['definition']
# Original learner text only; intentionally quoted internal source metadata is excluded.
def words(s):return re.findall(r'[a-z0-9]+',s.lower())
def grams(s):
 w=words(s);return [tuple(w[i:i+12]) for i in range(max(0,len(w)-11))]
source=set()
for p in (W/'planning/extracted').glob('*.txt'):source.update(grams(p.read_text()))
text_fields=[]
for tid in ('11','3'):
 for p in (W/'exemplar'/tid/'content-units').glob('*.json'):
  for b in json.loads(p.read_text())['blocks']:text_fields.append((b['block_id'],b['text']))
 for p in (W/'exemplar'/tid/'learning-items').glob('*.json'):
  for it in json.loads(p.read_text())['items']:
   for field in ['prompt','canonical_answer']:text_fields.append((it['item_id']+':'+field,it[field]))
   text_fields.extend((it['item_id']+':guidance',g) for g in it['marking_guidance'])
hits=[(key,' '.join(g)) for key,text in text_fields for g in grams(text) if g in source]
assert not hits,hits
proof={}
for tid in ('11','3'):
 q=j(f'exemplar/{tid}/qa_report.json');assert not any(x['status']=='fail' for x in q['deterministic_checks']);proof[tid]=dict(decision=q['release_decision'],statuses=dict(collections.Counter(x['status'] for x in q['deterministic_checks'])))
result=dict(status='pass',scope='Step 4 build consistency and original-text overlap only; not independent scientific, syllabus-mapping or teaching review.',topics=28,registry_records=594,source_bullets=335,leaf_outcomes=495,source_containers=71,planned_items=666,item_types=dict(counts),notes_words=budget['totals'],largest_ao_gap_points=gap,remaining_marking_demands=267,exemplar_checks=proof,original_wording=dict(fields_checked=len(text_fields),twelve_word_matches=0),standard_wrapper_note='run_checks.py returns 1 even when release_decision is publish; compare the actual failed-check list. Standard unchanged.')
(W/'review/step4-build-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
