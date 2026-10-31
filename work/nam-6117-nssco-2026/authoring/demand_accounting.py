"""Consume explicit reviewed credit counts; Bloom labels never determine recall."""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[1]
def fingerprint(x):
 return hashlib.sha256(json.dumps({k:x.get(k) for k in ['prompt','canonical_answer','marking_guidance','mark_tariff']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def load_decisions():return {r['id']:r for r in json.loads((W/'planning/full-demand-audit.json').read_text())['records']}
def item_key(x):return x['item_id'] if 'item_id' in x else x['task_id']+':'+x['part']
def recall_credit(x,decisions):
 key=item_key(x)
 if key not in decisions:raise ValueError('Unaudited response: '+key)
 r=decisions[key]
 if fingerprint(x)!=r['fingerprint']:raise ValueError('Demand audit is stale: '+key)
 if not 0<=r['recall_marks']<=x['mark_tariff']:raise ValueError('Invalid audited credit: '+key)
 return r['recall_marks']
