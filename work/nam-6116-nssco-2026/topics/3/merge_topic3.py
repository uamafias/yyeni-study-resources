"""Merge whole-unit authoring groups without duplicate live item datasets."""
import json
from pathlib import Path

b=Path(__file__).resolve().parent
archive=b/'authoring-groups'
archive.mkdir(exist_ok=True)
claims=[]; items=[]
notes={'topic_id':'3','authoring_tool':'Codex','groups':{},
       'release_status':'Unreleased; independent review, teacher verification and visual holds outstanding.'}
for group in ('3A','3B','3C','3D'):
    cp=b/f'claims/staging/claims_{group}.json'
    ip=b/f'learning-items/topic_3_items_{group}.json'
    if not cp.exists():cp=archive/f'claims_{group}.json'
    if not ip.exists():ip=archive/f'topic_3_items_{group}.json'
    claims.extend(json.loads(cp.read_text())['claims'])
    items.extend(json.loads(ip.read_text())['items'])
    n=json.loads((b/f'authoring_notes_{group}.json').read_text())
    notes['groups'][group]=n
    for key,value in n.items():
        if isinstance(value,list): notes.setdefault(key,[]).extend(value)
    for p in (cp,ip):
        if p.parent!=archive:p.replace(archive/p.name)
assert len({c['claim_id'] for c in claims})==len(claims)
assert len({i['item_id'] for i in items})==len(items)
wo=json.loads((b/'work_order.json').read_text())
assert {i['item_id'] for i in items}=={s['slot'] for s in wo['item_slots']+wo['performance_tasks']}
(b/'claims/canonical_claim_ledger.json').write_text(json.dumps({'ledger_id':'CLM-LEDGER-6116-3','claims':claims},indent=1,ensure_ascii=False)+'\n')
(b/'learning-items/topic_3_items.json').write_text(json.dumps({'dataset_id':'ITEMS-6116-3','topic_id':'3','items':sorted(items,key=lambda i:i['item_id'])},indent=1,ensure_ascii=False)+'\n')
(b/'authoring_notes.json').write_text(json.dumps(notes,indent=2,ensure_ascii=False)+'\n')
print(f'Merged {len(claims)} claims; {len(items)} items; {len(wo["content_units"])} units')
