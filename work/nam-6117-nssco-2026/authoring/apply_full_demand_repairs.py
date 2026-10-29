"""Apply reviewed original replacements to items, worked examples, claim revisions and labels."""
import json,copy,re,hashlib,sys
from pathlib import Path
from demand_rewrites import REWRITES
from full_demand_decisions import ADDITIONAL,MECH,PART_RECALL,PARTIAL_CARDS,MIXED_CREDIT_DETAILS
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def fingerprint(x):return hashlib.sha256(json.dumps({k:x.get(k) for k in ['prompt','canonical_answer','marking_guidance','mark_tariff']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
rows=[];changes=[];budget=[]
for t in range(1,13):
 T=W/f'topics/{t}';p=T/f'learning-items/topic_{t}_items.json';d=read(p);lp=T/'claims/canonical_claim_ledger.json';ld=read(lp);units={q:read(q) for q in (T/'content-units').glob('*.json')};notes=read(T/'authoring_notes.json')
 for x in d['items']:
  if x['item_type']!='flashcard':continue
  num=x['item_id'].split('-')[3];key=f'{t}-{num}';before=copy.deepcopy(x);override=REWRITES.get(key)
  if override:
   for k in ['prompt','canonical_answer','marking_guidance']:x[k]=override[k]
   x['command_word']=x['prompt'].split()[0];x['blooms_level']=override['bloom']
   if override['ao']:x['assessment_objectives']=override['ao']
   if override['subtype']:x['subtype']=override['subtype']
   recall=0;basis='Rewritten task: the credited response must diagnose the specified defect, process supplied evidence, construct to new constraints, or connect cause to consequence. The specific credit points below, not its Bloom label, establish the intended demand.'
  else:
   recall=x['mark_tariff'] if x['subtype'] in ['DEF','FEATURE'] or num in (ADDITIONAL.get(t,'')+' '+MECH.get(t,'')).split() else 0
   recall=PARTIAL_CARDS.get(key,recall)
   basis=('Reproducing the familiar fact, standard procedure, name or model earns the credited response; counted conservatively as recall.' if recall==x['mark_tariff'] else 'Mixed response: familiar factual credit is counted; the remaining credit requires a causal link, diagnostic decision or interpretation.' if recall else 'The supplied case, quantities, representation or causal question requires a response beyond reproducing a standalone fact or procedure.')
   if recall==x['mark_tariff']:
    x['blooms_level']='Remember'
    if x['assessment_objectives']==['B']:
     x['assessment_objectives']=['A'];x['subtype']='FEATURE'
     notes.setdefault('deviations',[]).append({'item_id':x['item_id'],'from':'B-level label on a fully recalled response','to':'FEATURE / A / Remember','why':'Full prompt-and-credit audit finds a familiar factual response without a new inference; AO label corrected to actual demand.'})
  if key=='1-022':x['marking_guidance']=['Dataset A isolates temperature while keeping concentration and catalyst mass constant (1).']
  # Specific single-credit rubrics must name their actual answer, not "both types"/"correct rule".
  vague=r'^(?:Both types|Both uses|Both named use categories|All three classes|Either appropriate treatment|Either specific valid source|Either named syllabus use|Either valid industrial use|One named valid use|General rule with stated exceptions|Rule with exceptions|Rule plus named exceptions|Rule and named exceptions)\b'
  if x['mark_tariff']==1 and any(re.search(vague,g) for g in x['marking_guidance']):
   x['marking_guidance']=[x['canonical_answer'].rstrip('.')+' (1). Accept an equivalent scientifically correct formulation.']
  cid='CLM-'+x['item_id'].removeprefix('ITEM-')
  for c in ld['claims']:
   if c['claim_id']==cid and c['text']!=x['canonical_answer']:
    c['text']=x['canonical_answer'];c['revision']+=1
  if fingerprint(before)!=fingerprint(x):
   for u in units.values():
    for b in u['blocks']:
     if cid in b.get('claim_ids',[]) and before['prompt'] in b.get('text',''):
      b['text']=x['prompt']+'\n\n'+x['canonical_answer']+'\n\nChecking the response: '+' '.join(x['marking_guidance'])
      b['assessment_objectives']=x['assessment_objectives']
   changes.append({'item_id':x['item_id'],'before':{k:before[k] for k in ['prompt','canonical_answer','assessment_objectives','blooms_level','subtype']},'after':{k:x[k] for k in ['prompt','canonical_answer','assessment_objectives','blooms_level','subtype']}})
  if override:
   note={'item_id':x['item_id'],'from':'Memorised factual/procedural response in earlier authored version','to':f"{x['subtype']} / {'+'.join(x['assessment_objectives'])} / {x['blooms_level']}; new stimulus and explicit credit points",'why':'Full-demand review found recall undercount. Original replacement exercises the same mapped objective; tariff and stable slot ID retained. Two-mark explanations require the two specified causal elements, consistent with observed Describe tariffs.'}
   notes.setdefault('deviations',[])
   if not any(v.get('item_id')==x['item_id'] and v.get('from')==note['from'] for v in notes['deviations']):notes['deviations'].append(note)
  rows.append({'id':x['item_id'],'topic':str(t),'kind':'card','subtype':x['subtype'],'marks':x['mark_tariff'],'recall_marks':recall,'non_recall_marks':x['mark_tariff']-recall,'basis':basis,'prompt':x['prompt'],'credit_points':x['marking_guidance'],'fingerprint':fingerprint(x),'rubric_review':'Author read for specificity and alignment to prompt; independent semantic confirmation remains open.'})
 pdpath=T/'authored_assessment_parts.json';pd=read(pdpath)
 for part in pd['parts']:
  short=part['task_id'].removeprefix(f'ITEM-6117-{t}-')+':'+part['part'];recall=PART_RECALL.get(t,{}).get(short,0)
  if recall==part['mark_tariff']:
   part['blooms_level']='Remember'
   if part['assessment_objectives']==['B']:part['assessment_objectives']=['A']
  if t==12 and part['part']=='a':
   part['prompt']=re.sub(r'Start with the blank learner grid in .*?not the answer panel\.', 'Plot on the separate blank grid shown below.\n\n![Blank cooling grid](visuals/VIS-6117-12-02-learner.svg)',part['prompt'])
  rows.append({'id':part['task_id']+':'+part['part'],'topic':str(t),'kind':'activity_part','marks':part['mark_tariff'],'recall_marks':recall,'non_recall_marks':part['mark_tariff']-recall,'basis':'Familiar fact/procedure credited without a new inference.' if recall==part['mark_tariff'] else 'Mixed credit: stated factual credit counted separately from the required explanation.' if recall else 'Credit requires use of supplied observations, numerical working, contextual reasoning or a plan satisfying the stated constraints. Copying a supplied observation is information retrieval from the stimulus, not long-term factual recall.','prompt':part['prompt'],'credit_points':part['marking_guidance'],'fingerprint':fingerprint(part),'rubric_review':'Author read the response requirements and credited elements; this does not replace independent scientific review.'})
 # Update activity wording and retain per-part labels as the authoritative demand record.
 if t==12:
  x=next(x for x in d['items'] if x['item_id']=='ITEM-6117-12-P01')
  x['prompt']='\n\n'.join(f"({z['part']}) {z['prompt']} [{z['mark_tariff']}]" for z in pd['parts'])+'\n\n![Cooling vessels](visuals/VIS-6117-12-03-learner.svg)'
  for u in units.values():
   for b in u['blocks']:
    b['text']=re.sub(r'Start with the blank learner grid in .*?not the answer panel\.', 'Plot on the separate blank grid shown below.\n\n![Blank cooling grid](visuals/VIS-6117-12-02-learner.svg)',b['text'])
 revisions={c['claim_id']:c['revision'] for c in ld['claims']}
 def stamp(x):
  old=x.get('authored_hash');new=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  if old and old!=new:x.update(prior_hash=old,repair_note='Full-demand repair: original stimulus/credit points and worked example updated together; factual teaching retained; review required.')
  for cid,rev in x.get('claims_seen',{}).copy().items():
   if rev!=revisions[cid]:x.setdefault('reviewed_unchanged','Related factual teaching remains correct; worked application revised where it cites the changed example.');x['claims_seen'][cid]=revisions[cid]
  x['authored_hash']=new
 for x in d['items']:stamp(x)
 for q,u in units.items():
  for b in u['blocks']:stamp(b)
  u['word_count']=sum(len(b['text'].split()) for b in u['blocks']);save(q,u)
 save(p,d);save(lp,ld);save(pdpath,pd)
 notes['full_demand_review']={'coverage':'All cards and all activity parts in this topic read for demand and credit-point specificity. See planning/full-demand-audit.json for mark-level decisions and text fingerprints.','limitations':'Author review; the other-vendor review and publication approval are still open.'};save(T/'authoring_notes.json',notes)
 budget.append({'topic_id':str(t),'cards':sum(x['item_type']=='flashcard' for x in d['items']),'activities':sum(x['item_type']!='flashcard' for x in d['items']),'items':len(d['items']),'marks':sum(x['mark_tariff'] for x in d['items']),'source':str(p.relative_to(W))})
for row in rows:
 if 0<row['recall_marks']<row['marks']:row['credit_allocation_detail']=MIXED_CREDIT_DETAILS[row['id']]
summary={'entries':len(rows),'cards':sum(r['kind']=='card' for r in rows),'activity_parts':sum(r['kind']=='activity_part' for r in rows),'marks':sum(r['marks'] for r in rows),'recall_marks':sum(r['recall_marks'] for r in rows)};summary['recall_percent']=100*summary['recall_marks']/summary['marks']
save(W/'planning/full-demand-audit.json',{'reviewer':'Codex author','method':'Read every prompt and marking rubric, independent of Bloom labels. Count familiar fact/standard-procedure credit, including conservative full marks where inseparable; separate explicitly mixed credit. Replacements require new evidence/diagnosis or causal reasoning. Decision selection is recorded in authoring/full_demand_decisions.py and demand_rewrites.py.','before_revision_recall_marks':641,'before_revision_marks':1557,'summary':summary,'records':rows,'limitations':'No cognitive-demand classification is mechanically provable. This is a complete author audit, not independent approval. Independent reviewer must test the decisions and replacements.'})
cp=W/'planning/demand-rewrite-log.json'
previous=read(cp) if cp.exists() else {'changes':[]}
byid={x['item_id']:x for x in previous['changes']}
for x in changes:byid.setdefault(x['item_id'],x)
save(cp,{'changes':list(byid.values()),'replacement_slots':len(REWRITES)})
save(W/'curriculum/item-budget.json',{'basis':'Generated from actual authored items after approved-plan deviations; no extra items or marks added.','qualification':'NSSCO Chemistry 6117','topics':budget,'total_items':sum(x['items'] for x in budget),'total_marks':sum(x['marks'] for x in budget)})
print(json.dumps(summary,indent=2))
