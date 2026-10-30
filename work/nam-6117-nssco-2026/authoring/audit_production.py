"""Whole-bank structural accounting. Does not substitute for semantic review."""
import json,re,collections
from pathlib import Path
from demand_accounting import load_decisions,recall_credit
demand_decisions=load_decisions()
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
items=[];parts=[];units=[];claims=[];differences=[];errors=[];practicals={};warnings=[];allchecks=collections.Counter();topic_rows=[]
for t in range(1,13):
 folder=W/f'topics/{t}';order=read(folder/'work_order.json');bank=read(folder/f'learning-items/topic_{t}_items.json')['items'];actual={x['item_id']:x for x in bank};pp=read(folder/'authored_assessment_parts.json')['parts'];items+=bank;parts+=pp
 planned=order['item_slots']+order['performance_tasks'];expected={x['slot'] for x in planned}
 if set(actual)!=expected:errors.append({'topic':t,'slot_mismatch':list(set(actual)^expected)})
 notes=next(folder.glob(f'{t}-*.md'));note_text=notes.read_text();un=[]
 for p in sorted((folder/'content-units').glob('*.json')):
  u=read(p);units.append(u);un.append(u)
  for b in u['blocks']:
   h=b.get('heading','');m=re.search(r'SP-6117-\d{2}',h)
   if h.startswith('Suggested practical'):
    if m:pid=m.group()
    else:
     names={'Crystallisation from solution':'01','Distillation of a fermented sample':'02','Filtration of muddy water':'03','Chromatography of coloured substances':'04'}
     pid='SP-6117-'+next(v for k,v in names.items() if k in h)
    if pid in practicals:errors.append({'duplicate_practical':pid})
    practicals[pid]={'topic':t,'file':str(notes.relative_to(W)),'heading':h,'unit_id':u['unit_id'],'block_id':b['block_id']}
 for dest in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',note_text):
  if not (notes.parent/dest).exists():errors.append({'missing_visual':str(notes.parent/dest)})
 for s in planned:
  a=actual[s['slot']];d={k:{'planned':s[k],'authored':a.get(k)} for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff'] if k in s and s[k]!=a.get(k)}
  if d:differences.append({'topic':t,'item_id':s['slot'],'differences':d,'review_record':f'topics/{t}/authoring_notes.json'})
 for x in bank:
  if x['item_type']=='flashcard':
   if not x['prompt'].lower().startswith(x['command_word'].lower()):errors.append({'command_mismatch':x['item_id']})
   nums=re.findall(r'\((\d+)\s*(?:marks?[^)]*)?\)', ' '.join(x['marking_guidance']))
   if sum(map(int,nums))!=x['mark_tariff']:errors.append({'credit_sum':x['item_id'],'tariff':x['mark_tariff'],'explicit_credits':sum(map(int,nums))})
  else:
   ps=[p for p in pp if p['task_id']==x['item_id']]
   if sum(p['mark_tariff'] for p in ps)!=x['mark_tariff']:errors.append({'part_total':x['item_id']})
 for p in pp:
  if '-P01' in p['task_id'] and t<12 and p['command_word'] is not None:errors.append({'MC_command':p['task_id'], 'part':p['part']})
 ledger=read(folder/'claims/canonical_claim_ledger.json')['claims'];claims+=ledger
 q=read(folder/'qa_report.json')['deterministic_checks'];cnt=collections.Counter(x['status'] for x in q);allchecks.update(cnt)
 for x in q:
  if x['status']=='fail':errors.append({'topic':t,'check':x})
  elif x['status']=='warn':warnings.append({'topic':t,**x})
 topic_rows.append({'topic':t,'title':order['topic_title'],'cards':sum(x['item_type']=='flashcard' for x in bank),'activities':sum(x['item_type']!='flashcard' for x in bank),'units':len(un),'claims':len(ledger),'words':sum(u['word_count'] for u in un),'checks':dict(cnt),'notes':str(notes.relative_to(W))})
ids=[x['item_id'] for x in items]
if len(ids)!=len(set(ids)):errors.append({'duplicate_item_ids':True})
expected_items=read(W/'curriculum/item-budget.json')['total_items']
if len(items)!=expected_items:errors.append({'item_count':len(items),'expected':expected_items})
if len(practicals)!=55:errors.append({'practical_count':len(practicals)})
visuals=read(W/'planning/visual-manifest.json')['visuals']
for v in visuals:
 if not (W/v['planned_file']).exists():errors.append({'missing_planned_visual':v['visual_id']})
mis=read(W/'curriculum/misconceptions.json');misitems=[x for x in items if x.get('misconception_entry')]
if len(set(x['misconception_entry'] for x in misitems))!=19:errors.append({'misconception_coverage':len(misitems)})
registry=read(W/'curriculum/objective_registry.json')['objectives'];expected_obj={x['objective_id'] for x in registry if x['objective_type']!='chem_container'};covered={o for x in items for o in x['objective_ids']}
if expected_obj-covered:errors.append({'uncovered_objectives':sorted(expected_obj-covered)})
# Exercise the pre-existing scope regression cases without editing syllabus limits.
scope=read(W/'curriculum/scope-scan.json');scope_cases=0
for guard in scope['entries']:
 for text in guard['must_catch']:
  scope_cases+=1
  if not re.search(guard['pattern'],text):errors.append({'scope_missed':text})
 for text in guard['must_allow']:
  scope_cases+=1
  if re.search(guard['pattern'],text):errors.append({'scope_false_positive':text})
cards=[x for x in items if x['item_type']=='flashcard'];ao=collections.Counter();recall=0
for x in cards+parts:
 for a in x['assessment_objectives']:ao[a]+=x['mark_tariff']/len(x['assessment_objectives'])
 recall+=recall_credit(x,demand_decisions)
total=sum(ao.values())
result={'status':'pass' if not errors else 'fail','scope':'Structural accounting plus explicit-credit arithmetic; not independent semantic review. Recall uses fingerprint-bound credit decisions for all authored responses, not Bloom labels; independent semantic confirmation remains open.','topics':topic_rows,'totals':{'items':len(items),'cards':len(cards),'activities':len(items)-len(cards),'activity_parts':len(parts),'claims':len(claims),'units':len(units),'notes_words':sum(u['word_count'] for u in units),'suggested_practicals':len(practicals),'planned_visuals_present':len(visuals),'misconceptions':len(misitems),'examiner_misconception_entries':len(set(x['misconception_entry'] for x in misitems)),'miscon_subtype_cards':sum(x.get('subtype')=='MISCON' for x in items),'activities_with_markdown_images':sum(x['item_type']!='flashcard' and '![' in x['prompt'] for x in items),'assessable_objectives':len(expected_obj),'marks':total,'ao_marks':dict(ao),'ao_percent':{k:100*v/total for k,v in ao.items()},'recall_marks':recall,'recall_percent':100*recall/total,'scope_regression_cases':scope_cases},'deterministic_checks':dict(allchecks),'warnings':warnings,'slot_label_differences':differences,'errors':errors,'release':'review_required; no claims approved for publication'}
(W/'planning/production-audit.json').write_text(json.dumps(result,indent=2)+'\n')
(W/'planning/authored-practical-index.json').write_text(json.dumps(practicals,indent=2)+'\n')
lines=['# Suggested practicals — Chemistry 6117','','All 55 experiences are taught in their content topics. Topic 12 consolidates the skills; it is our organisational addition to the eleven syllabus topics. These are supervised teaching experiences and original practice data, not official examination tasks.','','| ID | Teaching box | Location |','|---|---|---|']
for pid,x in sorted(practicals.items()):lines.append(f"| {pid} | {x['heading'].split(' — ')[-1]} | [Topic {x['topic']}]({x['file']}) — {x['unit_id']} |")
(W/'PRACTICAL-INDEX.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'status':result['status'],'totals':result['totals'],'errors':errors},indent=2))
if errors:raise SystemExit(1)
