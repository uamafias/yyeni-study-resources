"""Recompute production progress from authored files, never from planned slots."""
import json
from pathlib import Path
from demand_accounting import load_decisions,recall_credit
demand_decisions=load_decisions()
from collections import Counter
W=Path(__file__).resolve().parents[1]
topics=[];subject_ao=Counter();subject_recall=0
for folder in sorted((W/'topics').iterdir(),key=lambda p:int(p.name)):
 f=folder/'learning-items'/f'topic_{folder.name}_items.json'
 if not f.exists():continue
 items=json.loads(f.read_text())['items'];cards=[x for x in items if x['item_type']=='flashcard'];parts=json.loads((folder/'authored_assessment_parts.json').read_text())['parts'];ao=Counter();recall=0
 for x in cards+parts:
  for a in x['assessment_objectives']:ao[a]+=x['mark_tariff']/len(x['assessment_objectives'])
  recall+=recall_credit(x,demand_decisions)
 qa=json.loads((folder/'qa_report.json').read_text());checks=Counter(x['status'] for x in qa['deterministic_checks'])
 units=[json.loads(p.read_text()) for p in (folder/'content-units').glob('*.json')];row={'topic':folder.name,'title':json.loads((folder/'work_order.json').read_text())['topic_title'],'cards':len(cards),'activities':len(items)-len(cards),'units':len(units),'notes_words':sum(x['word_count'] for x in units),'checks':dict(checks),'ao_marks':dict(ao),'recall_marks':recall,'marks':sum(ao.values()),'release_status':'review_required'};topics.append(row);subject_ao.update(ao);subject_recall+=recall
 if (folder/'author-self-review.json').exists():
  p=folder/'author-self-review.json';d=json.loads(p.read_text());d.update(structural_checks=dict(checks),ao_marks=dict(ao),recall_marks=recall,total_marks=sum(ao.values()));p.write_text(json.dumps(d,indent=2)+'\n')
total=sum(subject_ao.values());share=100*subject_recall/total if total else 0
d={'stage':'Step 5 authored; independent review pending' if len(topics)==12 else 'Step 5 in progress; independent review pending','topics':topics,'authored_cards':sum(x['cards'] for x in topics),'authored_activities':sum(x['activities'] for x in topics),'ao_marks':dict(subject_ao),'marks':total,'recall_marks':subject_recall,'recall_share_percent':share,'recall_status':'above ceiling' if share>25 else 'review trigger' if share>24 else ('below trigger' if len(topics)==12 else 'below trigger on authored subset'),'limitation':'Recall sums explicit credit-level decisions for all authored responses, independently of Bloom labels; independent semantic confirmation remains open. All authored content remains review_required.'}
(W/'planning/production-progress.json').write_text(json.dumps(d,indent=2)+'\n')
lines=['# Chemistry 6117 production progress','','All 12 topics are authored as review drafts. Plan and prototype approval are recorded; independent review of the authored bank remains open.','','| Topic | Cards | Activities | Units | Notes words | Blocking failures |','|---|---:|---:|---:|---:|---:|']
for x in topics:lines.append(f"| {x['topic']} {x['title']} | {x['cards']} | {x['activities']} | {x['units']} | {x['notes_words']:,} | {x['checks'].get('fail',0)} |")
lines+=['',f"Authored: {d['authored_cards']} cards and {d['authored_activities']} activities. Recall: {subject_recall:g}/{total:g} marks ({share:.2f}%). This is the full-bank estimate from an explicit audit of all card and activity credit; independent semantic confirmation remains required. No per-topic recall cap applies.",'','Automated checks establish structural properties, not semantic correctness. Visuals and answers require independent scientific review. See each topic’s authoring_notes.json for deviations and author-self-review.json for the scope of self-checks.','','Carry-forward: reword and recompute any reused internal report answers; no invented official allocations for the five commentary-only parts; Paper 1 syllabus duration is 45 minutes; 2022 and 2023 papers are proof versions.']
(W/'PRODUCTION-PROGRESS.md').write_text('\n'.join(lines)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='topics'},indent=2))
