"""Verify implemented queue, not a prospective reduction based on labels."""
import json,math
from pathlib import Path
from round7_replacements import CHANGES
W=Path(__file__).resolve().parents[1]
# Round 8 intentionally restores test recall and supersedes some round-7 assertions.
if 'State the structural feature' in (W/'topics/10/learning-items/topic_10_items.json').read_text():
 import runpy
 print('Round-7 subset superseded: checking current round-7/8 replacements together.')
 runpy.run_path(str(W/'authoring/check_round8_diversity.py'),run_name='__main__')
 raise SystemExit(0)
items={}
for t in range(1,13):
 for x in json.loads((W/f'topics/{t}/learning-items/topic_{t}_items.json').read_text())['items']:
  if x['item_type']=='flashcard':items['-'.join(x['item_id'].split('-')[2:4])]=x
rows={r['id']:r for r in json.loads((W/'planning/full-demand-audit.json').read_text())['records']}
for k,c in CHANGES.items():
 x=items[k]
 for f in ['prompt','canonical_answer','marking_guidance']:assert x[f]==c[f],(k,f)
 assert rows[x['item_id']]['recall_marks']==c['recall'],k
 assert x['item_id'].endswith(x['subtype'])
for k in ['9-007','6-002','10-032','10-076']:assert ' or ' not in items[k]['prompt'],k
assert items['1-051']['canonical_answer']=='A burette.'
assert 'offsets cancel' in items['12-014']['canonical_answer']
# Equal absolute offsets cancel in final-minus-initial volume, for several actual readings.
for a,b in [(1.2,24.8),(0,25.4),(3.15,17.65)]:assert math.isclose((b+.2)-(a+.2),b-a)
queue=['8-015','8-017','8-019','8-021','8-023','8-037','8-039','8-041','8-043','8-045','11-020']
assert sum(items[k]['mark_tariff'] for k in queue)==22
assert sum(rows[items[k]['item_id']]['recall_marks'] for k in queue)==0
p=json.loads((W/'planning/production-progress.json').read_text());assert (p['recall_marks'],p['marks'])==(373,1637)
assert 100*373/1637<23
r={'status':'pass','implemented_queue':queue,'queue_marks_rewritten':22,'recall_before':395,'recall_after':373,'marks':1637,'reconciliation':'395 - 22 queue credit - 1 burette offset application + 1 alkene factual credit = 373. Already-applied first-batch replacements earn no new savings.','recall_percent':p['recall_share_percent'],'ceiling_maximum_integer_marks':409,'additional_recall_marks_before_ceiling':36,'changed_cards':[{'id':items[k]['item_id'],'prompt':items[k]['prompt'],'answer':items[k]['canonical_answer'],'credit':items[k]['marking_guidance'],'recall_marks':rows[items[k]['item_id']]['recall_marks']} for k in CHANGES],'limitations':'Author estimate. Independent acceptance of the replacement demands and the counting policy remains open; release hold remains.'}
(W/'planning/round7-replacement-checks.json').write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print({k:v for k,v in r.items() if k!='changed_cards'})
