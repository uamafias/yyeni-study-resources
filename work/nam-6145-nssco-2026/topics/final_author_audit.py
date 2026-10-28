"""Reconcile final author outputs with the frozen 6145 plan, then run required checks."""
import json,subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WS=Path(__file__).resolve().parents[1]
def run():
 rows=[];totals=Counter();issues=[];ids=set();mis=[]
 for td in sorted((WS/'topics').iterdir(),key=lambda p:[int(s) for s in p.name.split('.')] if p.is_dir() else [999]):
  if not td.is_dir() or not (td/'work_order.json').exists():continue
  for cmd in [['python3',str(WS/'topics/author_support.py'),td.name],['python3',str(ROOT/'standard/v0.2.0-draft/build/render_notes.py'),str(WS),td.name],['python3',str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),td.name,'--quiet']]:
   r=subprocess.run(cmd,capture_output=True,text=True)
   if r.returncode not in [0,1]:issues.append({'topic':td.name,'error':r.stderr})
  w=json.loads((td/'work_order.json').read_text());p=json.loads((td/'authored_packet.json').read_text());q=json.loads((td/'qa_report.json').read_text());dataset=json.loads((td/'learning-items'/('topic_'+td.name+'_items.json')).read_text())['items'];ledger=json.loads((td/'claims/canonical_claim_ledger.json').read_text())['claims'];byid={x['item_id']:x for x in dataset};counts=Counter(o for c in ledger for o in c['objective_ids']);words=0
  for u in w['content_units']:
   actual=json.loads((td/u['file']).read_text());n=sum(len(x['text'].split()) for x in actual['blocks']);words+=n
   if not u['word_budget'][0]<=n<=u['word_budget'][1]:issues.append({'topic':td.name,'budget':u['unit_id'],'words':n})
   for oid in u['objective_ids']:
    if not 2<=counts[oid]<=4:issues.append({'topic':td.name,'claim_count':oid,'count':counts[oid]})
  expected={s['slot'] for s in w['item_slots']+w['performance_tasks']}
  if set(byid)!=expected or len(dataset)!=len(expected):issues.append({'topic':td.name,'slots':'mismatch'})
  for s in w['item_slots']:
   i=byid[s['slot']]
   for field in ['subtype','assessment_objectives','command_word','mark_tariff','blooms_level','difficulty']:
    if i[field]!=s[field]:issues.append({'item':i['item_id'],'label':field})
   if i['objective_ids']!=[s['objective_id']]:issues.append({'item':i['item_id'],'objective':'mismatch'})
   if s.get('misconception_entry'):
    mis.append(i.get('misconception_entry'))
    if i.get('misconception_entry')!=s['misconception_entry']:issues.append({'item':i['item_id'],'misconception':'mismatch'})
  for i in dataset:
   if i['item_id'] in ids:issues.append({'duplicate':i['item_id']})
   ids.add(i['item_id'])
  fail=[x['check_id'] for x in q['deterministic_checks'] if x['status']=='fail'];warn=[x['check_id'] for x in q['deterministic_checks'] if x['status']=='warn'];nr=[x['check_id'] for x in q['deterministic_checks'] if x['status']=='not_run']
  if fail or q['release_decision']!='publish':issues.append({'topic':td.name,'failures':fail,'decision':q['release_decision']})
  row={'topic':td.name,'claims':len(ledger),'units':len(w['content_units']),'flashcards':len(w['item_slots']),'packages':len(w['performance_tasks']),'items':len(dataset),'content_words':words,'decision':q['release_decision'],'failures':fail,'warnings':warn,'not_run':nr,'deviations':p.get('deviations',[])};rows.append(row)
  totals.update({k:row[k] for k in ['claims','units','flashcards','packages','items','content_words']});totals['topics']+=1
 if (totals['topics'],totals['units'],totals['flashcards'],totals['packages'],totals['items'])!=(28,63,468,112,580):issues.append({'totals':'mismatch'})
 if len(mis)!=37 or len(set(mis))!=37:issues.append({'misconception_count':len(mis),'unique':len(set(mis))})
 result={'status':'PASS' if not issues else 'FAIL','totals':dict(totals),'misconception_slots':len(mis),'topics':rows,'issues':issues,'semantic_review':'not_run; independent Claude review required'}
 (WS/'topics/final-author-audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'totals':result['totals'],'issues':issues},indent=2))
 if issues:raise SystemExit(1)
if __name__=='__main__':run()
