import json,re
from pathlib import Path
W=Path(__file__).resolve().parents[1]
items={};parts=[];unresolved_blocks=[];orders={}
for t in range(1,13):
 td=W/f'topics/{t}'
 for x in json.loads((td/f'learning-items/topic_{t}_items.json').read_text())['items']:items[x['item_id']]=x
 parts+=json.loads((td/'authored_assessment_parts.json').read_text())['parts']
 for p in (td/'content-units').glob('*.json'):
  for b in json.loads(p.read_text())['blocks']:
   if b['heading'].startswith(('Activity feedback','Activity worked example')):unresolved_blocks.append(b['block_id'])
 notes=next(p for p in td.glob('*.md') if re.match(r'^\d+-',p.name)).read_text()
 ids=re.findall(r'^## (\d+(?:\.\d+)*)\s',notes,re.M);keys=[tuple(map(int,i.split('.'))) for i in ids]
 assert keys==sorted(keys),(t,ids)
 orders[str(t)]=ids
get=lambda prefix:next(x for k,x in items.items() if k.startswith('ITEM-6117-'+prefix+'-'))
assert 'red-brown' not in get('8-013')['prompt'] and 'green' not in get('8-013')['prompt']
assert 'readily reduced' not in get('9-015')['prompt']
assert 'reference chloride' not in get('8-029')['prompt'].lower() and 'bromide gives' not in get('8-029')['prompt']
assert get('8-023')['command_word']=='Deduce' and get('8-024')['command_word']=='Plan'
x=items['ITEM-6117-8-P03'];assert x['prompt'].count('| Portion |')==1
ps=[p for p in parts if p['task_id']==x['item_id']];assert sum(p['mark_tariff'] for p in ps)==12
assert next(p for p in ps if p['part']=='b')['mark_tariff']==2
assert all('| Portion |' not in p['prompt'] for p in ps)
assert 'original synthetic results' not in '\n'.join(x['prompt'] for x in items.values()).lower()
punctuation=[];unique=0;ties=0
for p in parts:
 if p['task_id'].endswith('P01') and not p['task_id'].startswith('ITEM-6117-12-'):
  opts=dict(re.findall(r'^([A-D])\. (.+)$',p['prompt'],re.M));key=p['canonical_answer'][0]
  assert len(opts)==4
  if any(v.endswith('.') for v in opts.values()):punctuation.append(p['task_id']+':'+p['part'])
  n={k:len(v.split()) for k,v in opts.items()};unique+=n[key]>max(v for k,v in n.items() if k!=key);ties+=n[key]==max(n.values())
assert not punctuation
progress=json.loads((W/'planning/production-progress.json').read_text());assert progress['recall_marks']==392
r={'status':'pass','activity_marks':12,'shared_record_instances':1,'cation_part_marks':2,'mc_option_terminal_full_stop_sets':punctuation,'correct_option_uniquely_longest':unique,'correct_option_longest_including_ties':ties,'unresolved_answer_only_note_blocks':len(unresolved_blocks),'numeric_section_order':orders,'recall_marks':392,'marks':1637,'limits':'Historical named-repair checks; completed editorial work is checked by check_final_editorial.py.'}
(W/'planning/round9-repair-checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
