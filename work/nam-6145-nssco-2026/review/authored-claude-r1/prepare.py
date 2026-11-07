import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
WS=HERE.parents[1];ROOT=WS.parents[1]
rows=[];frozen={}
for td in sorted((WS/'topics').iterdir(),key=lambda p:list(map(int,p.name.split('.')))):
 if not td.is_dir():continue
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),td.name,'--quiet'],cwd=ROOT,capture_output=True,text=True)
 q=json.loads((td/'qa_report.json').read_text());assert q['release_decision']=='publish'
 wo=json.loads((td/'work_order.json').read_text());c=json.loads((td/'contract.json').read_text())
 slots={s['slot']:s for s in wo['item_slots']+wo['performance_tasks']}
 items=json.loads((td/wo['output_files']['learning_items']).read_text())['items']
 assert len(items)==len(slots)
 for it in items:
  s=slots[it['item_id']]
  for k in ['assessment_objectives','blooms_level','command_word','mark_tariff']:assert it[k]==s[k]
  assert it['item_type']==s.get('item_type','flashcard')
  assert it['subtype']==s.get('subtype')
 packet=['# '+td.name+' '+wo['topic_title'],'','## Notes','']
 for b in json.loads((td/wo['content_units'][0]['file']).read_text())['blocks']:
  packet.extend(['### '+b['block_id']+' '+b['heading'],b['text'],''])
 packet.extend(['## Assigned objectives',json.dumps(wo['content_units'][0]['objectives'],ensure_ascii=False),'','## Items (original order)',''])
 for it in items:
  packet.extend(['### '+it['item_id'],json.dumps({k:it[k] for k in ['item_type','subtype','objective_ids','assessment_objectives','blooms_level','command_word','mark_tariff','prompt','canonical_answer','marking_guidance']},ensure_ascii=False),''])
 (HERE/(td.name+'-packet.md')).write_text('\n'.join(packet))
 rows.append({'topic':td.name,'items':len(items),'decision':q['release_decision'],'warnings':[x for x in q['deterministic_checks'] if x['status']=='warn'],'not_run':[x for x in q['deterministic_checks'] if x['status']=='not_run']})
 for p in [td/'contract.json',td/'work_order.json',td/'claims/canonical_claim_ledger.json',td/wo['content_units'][0]['file'],td/wo['output_files']['learning_items']]:
  frozen[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n')
(HERE/'FROZEN.json').write_text(json.dumps(frozen,indent=2)+'\n')
print(json.dumps({'topics':len(rows),'items':sum(r['items'] for r in rows),'frozen_files':len(frozen),'packet_words':sum(len(p.read_text().split()) for p in HERE.glob('*-packet.md'))}))
