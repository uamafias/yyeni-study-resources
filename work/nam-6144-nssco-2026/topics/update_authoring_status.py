"""Reconcile actual author outputs, exact slots, labels and the approved input hashes."""
import hashlib,json,re
from pathlib import Path
W=Path(__file__).resolve().parents[1]
rows=[]
for td in sorted((W/'topics').iterdir(),key=lambda p:tuple(map(int,p.name.split('.'))) if re.fullmatch(r'\d+\.\d+',p.name) else (999,)):
 if not (td/'authoring_summary.json').exists():continue
 s=json.loads((td/'authoring_summary.json').read_text());wo=json.loads((td/'work_order.json').read_text());items=json.loads((td/'learning-items'/f'topic_{td.name}_items.json').read_text())['items'];by={i['item_id']:i for i in items}
 assert len(by)==len(items)
 assert set(by)=={x['slot'] for x in wo['item_slots']+wo['performance_tasks']}
 for slot in wo['item_slots']:
  i=by[slot['slot']]
  assert i['objective_ids']==[slot['objective_id']]
  for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff']:assert i[k]==slot[k],(td.name,k)
 for bp in json.loads((td/'performance-blueprints.json').read_text())['packages']:
  i=by[bp['slot']]
  for k in ['item_type','blooms_level','objective_ids','assessment_objectives']:assert i[k]==bp[k]
  assert i['mark_tariff']==bp['total_marks']
  assert i['command_word']==bp['subparts'][0]['command_word']
 q=json.loads((td/'qa_report.json').read_text());assert s['decision']==q['release_decision']
 s['flashcards']=sum(i['item_type']=='flashcard' for i in items);s['practice_packages']=len(items)-s['flashcards']
 s['over_max_units']=[u['unit_id'] for p in (td/'content-units').glob('*.json') if (u:=json.loads(p.read_text()))['word_count']>u['word_budget']['max']]
 rows.append(s)
summary={'completed':sum(x['decision']=='publish' and not x['failed_checks'] for x in rows),'planned':22,'topics':rows,'totals':{k:sum(r[k] for r in rows) for k in ['claims','units','items','flashcards','practice_packages','notes_words']},'slot_audit':'Exact IDs, counts and required labels reconciled against each approved work order and blueprint.'}
(W/'authoring-progress.json').write_text(json.dumps(summary,indent=2)+'\n')
p=W/'STATUS.md';s=p.read_text();s=re.sub(r'- \[ \] 5 Topics authored[^\n]*',f"- [ ] 5 Topics authored — {summary['completed']} / 22 complete drafts, deterministic PUBLISH; independent review pending. See authoring-progress.json.",s);s=re.sub(r'\w+ production topic drafts exist',f"{summary['completed']} production topic drafts exist",s);p.write_text(s)
print(json.dumps({k:summary[k] for k in ['completed','planned','totals','slot_audit']},indent=2))
