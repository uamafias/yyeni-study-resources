"""Rebuild learner-review changes from a preserved baseline; never from stale builders."""
import json,copy,re,hashlib,sys,collections
from pathlib import Path
from round5_content import CARDS,PARTS,NEW
from round5_notes import NOTES,METAL_PROPERTIES
from round5_mc import WRONG
from round6_polish import clean,card as polish_card,part as polish_part
from round7_replacements import apply as apply_round7
from round8_diversity import apply as apply_round8
from round9_repairs import apply_card as apply_round9,apply_part as part_round9,SHARED
from final_content_edits import apply_card as final_card,apply_mc as final_mc
from final_notes_rebuild import rebuild as final_notes
from round10_repairs import card as round10_card,part as round10_part
from round11_repairs import card as round11_card,part as round11_part,whole as round11_whole
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
base=json.loads((W/'planning/round5-baseline.json').read_text())
def get(p):return copy.deepcopy(base[str(p)])
def save(p,d):(W/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def fp(x):return hashlib.sha256(json.dumps({k:x.get(k) for k in ['prompt','canonical_answer','marking_guidance','mark_tariff']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def tariff(g):return sum(map(int,re.findall(r'\((\d+)\s*(?:marks?[^)]*)?\)',' '.join(g))))
reg=get('curriculum/objective_registry.json');o=copy.deepcopy(next(o for o in reg['objectives'] if o['objective_id']=='OBJ-6117-11.1.1-01'));o.update(objective_id='OBJ-6117-11.1.1-02',syllabus_text='describe a chemical test for the presence of water using (anhydrous copper(II) sulfate or cobalt(II) chloride)',learner_objective='Identify water chemically and distinguish presence from purity.',syllabus_page=37);reg['objectives'].append(o)
lube=copy.deepcopy(next(z for z in reg['objectives'] if z['objective_id']=='OBJ-6117-10.2.1-04-07'));lube.update(objective_id='OBJ-6117-10.2.1-04-08',learner_objective='name the uses of the lubricating fraction: lubricants, waxes and polishes',syllabus_page=32);reg['objectives'].append(lube)
objectives={o['objective_id']:o for o in reg['objectives']}
# Repair explicit miscitation in the new measurement slot before resolving IDs.
for n in NEW:
 if n['topic']==1:n['objectives']=['1.4-01']
 if n['topic']==1 and n['sub']=='DIST':n['sub']='INTERP'
 if n['prompt'].startswith('Classify '):n['prompt']=n['prompt'].replace('Classify ','State the classification of ',1)
 n['prompt']=n['prompt'].replace('Use the mass numbers as isotope masses.','Treat the mass numbers as isotope masses.').replace('Use a small separately collected sample.','Test a small separately collected sample.')
 if n['topic']==10 and 'lubricating fraction' in n['prompt']:n['objectives']=['10.2.1-04-08'];n['prompt']=n['prompt'].replace('State two uses','Name two uses')
 for oid in n['objectives']:assert 'OBJ-6117-'+oid in objectives,oid
save('curriculum/objective_registry.json',reg)
command_extensions=[]
oldrows={r['id']:r for r in get('planning/full-demand-audit.json')['records']};rows=[];migration={};log=[];budget=[];dropped_blocks=0;final_log=[]
for t in range(1,13):
 td=f'topics/{t}';ip=f'{td}/learning-items/topic_{t}_items.json';d=get(ip);ld=get(f'{td}/claims/canonical_claim_ledger.json');pp=get(f'{td}/authored_assessment_parts.json');order=get(f'{td}/work_order.json');contract=get(f'{td}/contract.json');notes=get(f'{td}/authoring_notes.json');units={p:get(p) for p in base if p.startswith(td+'/content-units/')};unitlist=list(units.values())
 item_recall={};new_ids=[]
 for x in d['items']:
  if x['item_type']!='flashcard':continue
  old=copy.deepcopy(x);key=f"{t}-{x['item_id'].split('-')[3]}";c=CARDS.get(key);recall=oldrows[x['item_id']]['recall_marks']
  if c:
   for f in ['prompt','canonical_answer','marking_guidance']:x[f]=c[f]
   for f,k in [('assessment_objectives','ao'),('subtype','sub'),('blooms_level','bloom'),('objective_ids','objectives')]:
    if c[k] is not None:x[f]=c[k]
   if c['recall'] is not None:recall=c['recall']
   x['mark_tariff']=tariff(x['marking_guidance'])
  # Remove directly supplied mole ratios, retain necessary reactant identities.
  if key=='4-016':x['prompt']=x['prompt'].replace('HCl + NaOH → NaCl + H2O. ','Write the neutralisation equation before calculating. ')
  if key in ['4-019','4-040']:x['prompt']=x['prompt'].replace('CaCO3:CO2 amount ratio is 1:1; ','The carbonate reacts with excess hydrochloric acid; ').replace('CaCO3:CO2 amount ratio=1:1; ','The carbonate reacts with excess hydrochloric acid; ')
  if x['prompt'].startswith('Describe why '):x['prompt']=x['prompt'].replace('Describe why ','Explain why ',1)
  if t==2 and key in ['2-113','2-115','2-117','2-119']:x['canonical_answer']+='\n\n![Model shapes — answer only](visuals/VIS-6117-2-03.svg)'
  polish_card(x,key)
  if key in ['1-051','1-066','1-070','12-014']:recall=x['mark_tariff'];x['assessment_objectives']=['A'];x['blooms_level']='Remember';x['subtype']='FEATURE'
  r7=apply_round7(x,key)
  if r7 is not None:recall=r7
  r8=apply_round8(x,key)
  if r8 is not None:recall=r8
  r9=apply_round9(x,key)
  if r9 is not None:recall=r9
  rf=final_card(x,key)
  if rf is not None:recall=rf
  round10_card(x,key)
  round11_card(x,key)
  x['command_word']=x['prompt'].split()[0]
  # IDs identify current subtype; a migration file preserves traceability to old slots.
  new_id=x['item_id'].rsplit('-',1)[0]+'-'+x['subtype']
  if new_id!=x['item_id']:migration[x['item_id']]=new_id
  item_recall[new_id]=recall;x['item_id']=new_id
  if x['subtype']=='INTERP' and x['mark_tariff']==1 and x['command_word'] in ['State','Deduce']:x['blooms_level']='Apply' if x['assessment_objectives']==['B'] else x['blooms_level']
  if fp(old)!=fp(x):log.append({'old_id':old['item_id'],'id':new_id,'change':'Prompt/answer/credit repair','old_prompt':old['prompt'],'prompt':x['prompt']})
 # Add explicit gap items to the generated order rather than hiding them in generic topic coverage.
 nextnum=max(int(x['item_id'].split('-')[3]) for x in d['items'] if x['item_type']=='flashcard')+1
 for n in [n for n in NEW if n['topic']==t]:
  x=copy.deepcopy(next(x for x in d['items'] if x['item_type']=='flashcard'));iid=f'ITEM-6117-{t}-{nextnum:03}-{n["sub"]}';nextnum+=1
  for f in ['prompt','canonical_answer','marking_guidance']:x[f]=n[f]
  oids=['OBJ-6117-'+z for z in n['objectives']];x.update(item_id=iid,objective_ids=oids,subtype=n['sub'],assessment_objectives=[n['ao']],blooms_level=n['bloom'],mark_tariff=tariff(n['marking_guidance']),command_word=n['prompt'].split()[0],claim_ids=[],claims_seen={},context={'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},difficulty=2,prerequisite_item_ids=[])
  for k in ['misconception_entry','prior_hash','repair_note','reviewed_unchanged']:x.pop(k,None)
  round11_card(x,f'{t}-{iid.split("-")[3]}')
  # One explicit teaching claim per objective, supported by the supplemental prose.
  for oid in oids:
   cid=f'CLM-6117-R5-{t}-{nextnum-1}-{len(x["claim_ids"])+1}'
   text=objectives[oid]['syllabus_text'];text=re.sub(r'^(?:describe|state|define|explain|identify|calculate|use|distinguish|deduce)\s+','',text,flags=re.I)
   claim=copy.deepcopy(ld['claims'][0]);claim.update(claim_id=cid,objective_ids=[oid],text=next((c['text'] for c in ld['claims'] if oid in c['objective_ids'] and c.get('claim_type')!='synthetic_example'), NOTES[t][1].split('\n\n')[0]),claim_type='factual',provenance='generated_gap',evidence=[],derived_from_claim_ids=[],revision=1,publishable=False)
   claim['verification'].update(status='unverified',method='Syllabus-mapped coverage repair; author checked, independent review pending.')
   ld['claims'].append(claim);x['claim_ids'].append(cid)
  if t==2 and 'Bohr shell' in x['prompt']:x['canonical_answer']+='\n\n![Bohr model — answer only](visuals/R5-bohr-answer.svg)'
  if t==2 and 'magnesium fluoride' in x['prompt']:x['canonical_answer']+='\n\n![Ionic model — answer only](visuals/R5-ionic-answer.svg)'
  if t==6 and 'forward activation energy' in x['prompt']:x['prompt']='Calculate the forward activation energy and enthalpy change from the profile. State whether the reaction is exothermic.\n\n![Energy profile](visuals/R5-profile-learner.svg)'
  if x['command_word']=='Draw':x['context']['facts']=['Draw on paper or a digital canvas, then reveal the answer and check each credited feature. This bank does not automatically mark drawings.']
  d['items'].append(x);new_ids.append(iid);item_recall[iid]=n['recall']
  slot=copy.deepcopy(order['item_slots'][0]);slot.update(slot=iid,objective_id=oids[0],objective_title=objectives[oids[0]]['syllabus_text'],syllabus_text=objectives[oids[0]]['syllabus_text'],subtype=x['subtype'],assessment_objectives=x['assessment_objectives'],blooms_level=x['blooms_level'],command_word=x['command_word'],mark_tariff=x['mark_tariff'],difficulty=2,reason='Learner-review coverage repair; specific skill previously not independently assessed.',required_visual_ids=[],variant_spec={'variant':1,'scope':oids[0],'task_distinction':x['prompt']},marking_guidance_must_name=x['marking_guidance'],answer_requirements={'canonical_answer':x['canonical_answer'],'credit_points':x['marking_guidance']},tariff_provenance={'planned_tariff':x['mark_tariff'],'reason':'Original allocation to the explicitly listed independent credit points; not an official mark scheme.'})
  order['item_slots'].append(slot)
 # Remove copied card worked-practice blocks, preserving factual teaching, not assessment keys.
 cardids={x['item_id'] for x in d['items'] if x['item_type']=='flashcard'};oldcardprompts={x['prompt'] for x in get(ip)['items'] if x['item_type']=='flashcard'};removedclaims=set();seenparagraphs=set()
 for u in unitlist:
  retained=[]
  for b in u['blocks']:
   if b['heading'].startswith('Worked practice') and any(p in b['text'] for p in oldcardprompts):removedclaims.update(b['claim_ids']);dropped_blocks+=1;continue
   paras=[]
   for para in b['text'].split('\n\n'):
    if len(para.split())>25 and para in seenparagraphs:continue
    paras.append(para)
    if len(para.split())>25:seenparagraphs.add(para)
   b['text']='\n\n'.join(paras)
   if b['text']:retained.append(b)
  u['blocks']=retained
 # Remove synthetic flashcard-example claims, retain the factual teaching claims.
 synthetic={c['claim_id'] for c in ld['claims'] if re.match(r'^CLM-6117-\d+-\d{3}-',c['claim_id'])}
 for x in d['items']:
  if x['item_type']=='flashcard':x['claim_ids']=[cid for cid in x['claim_ids'] if cid not in synthetic];x['claims_seen']={cid:v for cid,v in x['claims_seen'].items() if cid not in synthetic}
 for u in unitlist:
  for b in u['blocks']:b['claim_ids']=[cid for cid in b['claim_ids'] if cid not in synthetic];b['claims_seen']={cid:v for cid,v in b['claims_seen'].items() if cid not in synthetic}
 ld['claims']=[c for c in ld['claims'] if c['claim_id'] not in synthetic]
 if t in NOTES:
  heading,text=NOTES[t];target=unitlist[0]
  # Put expanded metal teaching in the reactivity unit; append elsewhere only once.
  if t==9:target=next((u for u in unitlist if u['unit_id'].endswith('9.2')),target)
  block={'block_id':target['unit_id']+'-R5','block_type':'plain_explanation','heading':heading,'text':text,'claim_ids':[c['claim_id'] for c in ld['claims'] if c['claim_id'].startswith(f'CLM-6117-R5-{t}-')],'context_tags':[],'assessment_objectives':['A','B','C'],'claims_seen':{}}
  target['blocks'].append(block)
  addedoids={oid for x in d['items'] if x['item_id'] in new_ids for oid in x['objective_ids']}
  # Supplemental block belongs to one existing unit but references its actual extra targets.
  target['objective_ids']=list(dict.fromkeys(target.get('objective_ids',[])+sorted(addedoids)))
 if t==9:
  u=next(u for u in unitlist if u['unit_id'].endswith('9.1'));u['blocks'].append({'block_id':u['unit_id']+'-R5-properties','block_type':'plain_explanation','heading':'Using properties and particle models','text':METAL_PROPERTIES,'claim_ids':[],'context_tags':[],'assessment_objectives':['A','B'],'claims_seen':{}})
 # Restore the syllabus position and remove the unverified external project link.
 for u in unitlist:
  for b in u['blocks']:
   if t==11:
    b['text']=re.sub(r'The 2018 syllabus emphasises.*?(?=\n\n|$)','The syllabus emphasises that seawater desalination is expensive and does not present it as the solution to Namibia’s water scarcity. Evaluate water conservation, safe supply and treatment using the stated needs and resources.',b['text'],flags=re.S)
   if t==10:b['text']=b['text'].replace('Ships or industrial furnaces.','Ships or home heating systems.').replace('ships and industrial furnaces','ships and home heating systems')
 # Activity parts and whole-task text remain aligned.
 for z in pp['parts']:
  short=f'{t}-'+z['task_id'].split('-')[-1]+':'+z['part'];c=PARTS.get(short)
  recall=oldrows[z['task_id']+':'+z['part']]['recall_marks']
  if c:
   for f in ['prompt','canonical_answer','marking_guidance']:
    if c[f] is not None:z[f]=c[f]
   for f,k in [('assessment_objectives','ao'),('blooms_level','bloom'),('objective_ids','objectives')]:
    if c[k] is not None:z[f]=c[k]
   if c['recall'] is not None:recall=c['recall']
  if z['task_id']=='ITEM-6117-2-P03':
   for f in ['prompt','canonical_answer']:
    z[f]=z[f].replace('an indicator','an ammeter').replace('indicator response','ammeter reading').replace('indicator','ammeter').replace('does not light the ammeter','gives negligible current')
   z['marking_guidance']=[g.replace('Indicator','Ammeter').replace('indicator response','ammeter reading') for g in z['marking_guidance']]
   z['objective_ids']=list(dict.fromkeys(z['objective_ids']+z.get('context_objective_ids',[])))
  if z['task_id']==f'ITEM-6117-{t}-P01' and t<12 and (t,z['part']) in WRONG:
   key=z['canonical_answer'][0];opts=dict(re.findall(r'^([A-D])\. (.+)$',z['prompt'],re.M));old_correct=opts[key];wrong=iter(WRONG[(t,z['part'])])
   for letter in 'ABCD':
    if letter!=key:opts[letter]=next(wrong)
   stem=z['prompt'].split('\nA. ')[0];z['prompt']=stem+'\n'+'\n'.join(k+'. '+v for k,v in opts.items())
   reason=z['canonical_answer'][len(key+'. '+old_correct):].strip()
   z['canonical_answer']=key+'. '+opts[key]+' '+reason
   z['marking_guidance']=[f"Correct option {key} (1). {reason} Other options reflect misconceptions about the stated process; see the answer explanation. No mark for more than one selected option."]
  if z['task_id']=='ITEM-6117-5-P01' and z['part']=='10':z['canonical_answer']+=' This applies to an active copper anode.'
  if z['task_id']=='ITEM-6117-11-P01' and z['part']=='12':z['canonical_answer']+=' This concerns the gaseous Haber equilibrium.'
  z['prompt']=re.sub(r'Original (?:synthetic observations|DATA-\d+):','Measurements:',z['prompt']).replace('original teaching dataset','measurements')
  polish_part(z)
  if z['task_id'].endswith('P01') and t<12:final_mc(z,t)
  r9=part_round9(z)
  if r9 is not None:recall=r9
  if z['task_id'].endswith('P01') and t<12:
   z['prompt']=re.sub(r'(?m)^([A-D]\. .+?)[.。]+$',r'\1',z['prompt'])
  round10_part(z,t)
  prior_part=z['part']
  round11_part(z,t)
  row=copy.deepcopy(oldrows[z['task_id']+':'+prior_part]);row.update(id=z['task_id']+':'+z['part'],marks=z['mark_tariff'],prompt=z['prompt'],credit_points=z['marking_guidance'],recall_marks=recall,non_recall_marks=z['mark_tariff']-recall,fingerprint=fp(z),basis='Author reclassification after removing learner cues; familiar observation credit counted as recall, numerical/evidence processing separately.');rows.append(row)
 for x in d['items']:
  if x['item_type']=='flashcard':continue
  ps=[p for p in pp['parts'] if p['task_id']==x['item_id']]
  if x['item_type']=='multiple_choice_set':
   x['prompt']='\n\n'.join(f"({p['part']}) {p['prompt']} [1]" for p in ps);x['canonical_answer']='\n\n'.join(f"({p['part']}) {p['canonical_answer']}" for p in ps);x['marking_guidance']=[f"Part {p['part']}: {g}" for p in ps for g in p['marking_guidance']]
   for u in unitlist:
    for b in u['blocks']:
     if any(cid in b['claim_ids'] for cid in x['claim_ids']):b['text']='\n\n'.join(p['canonical_answer'] for idx,p in enumerate(ps,1) if 'CLM-'+x['item_id'].removeprefix('ITEM-')+f'-{idx}' in b['claim_ids'])
   continue
  images=list(dict.fromkeys(re.findall(r'!\[[^\]]*\]\([^)]*\)',x['prompt'])))
  if x['item_id'] in ['ITEM-6117-2-P03','ITEM-6117-12-P01']:images=[i for i in images if 'VIS-6117-2-01' not in i and 'VIS-6117-12-03' not in i]
  prompt='\n\n'.join((f"({p['part']}) " if not p['part'].startswith('credit-group') else '')+p['prompt']+f" [{p['mark_tariff']}]" for p in ps)
  if x['item_id']=='ITEM-6117-8-P03':prompt=SHARED+'\n\n'+prompt
  x['prompt']=prompt+'\n\n'+'\n'.join(i for i in images if i not in prompt)
  round11_whole(x,t)
  x['canonical_answer']='\n\n'.join(f"({p['part']}) "+p['canonical_answer'] for p in ps)
  x['marking_guidance']=[f"Part {p['part']}: {g}" for p in ps for g in p['marking_guidance']]
  x['objective_ids']=list(dict.fromkeys(oid for p in ps for oid in p['objective_ids']))
  for idx,p in enumerate(ps,1):
   cid='CLM-'+x['item_id'].removeprefix('ITEM-')+f'-{idx}';cl=next((c for c in ld['claims'] if c['claim_id']==cid),None)
   if cl:cl['text']=p['canonical_answer'];cl['objective_ids']=p['objective_ids'];cl['revision']+=1
  # Replace the activity worked example rather than leave stale learner wording.
  for u in unitlist:
   for b in u['blocks']:
    if any(cid in b['claim_ids'] for cid in x['claim_ids']):b['text']='\n\n'.join(p['canonical_answer'] for idx,p in enumerate(ps,1) if 'CLM-'+x['item_id'].removeprefix('ITEM-')+f'-{idx}' in b['claim_ids']);b['heading']='Activity feedback — '+x['item_id'].split('-')[-1]
 if t==10:
  for cl in ld['claims']:
   changed=cl['text'].replace('ships and industrial furnaces','ships and home heating systems').replace('Ships or industrial furnaces.','Ships or home heating systems.')
   if changed!=cl['text']:cl['text']=changed;cl['revision']+=1
 # Every current slot receives current labels and explicit deviation provenance.
 actual={x['item_id']:x for x in d['items']}
 for s in order['item_slots']:
  s['slot']=migration.get(s['slot'],s['slot']);x=actual[s['slot']]
  for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff']:s[k]=x[k]
  s['answer_requirements']={'canonical_answer':x['canonical_answer'],'credit_points':x['marking_guidance']}
  s['marking_guidance_must_name']=x['marking_guidance']
  if isinstance(s.get('variant_spec'),dict):s['variant_spec']['task_distinction']=x['prompt']
 for task in order['performance_tasks']:
  x=actual[task['slot']];current=[p for p in pp['parts'] if p['task_id']==task['slot']]
  task['parts']=copy.deepcopy(current)
  for k in ['objective_ids','mark_tariff','assessment_objectives','blooms_level']:task[k]=x[k]
  task['brief']=x['prompt'];task['marking_guidance_must_name']=x['marking_guidance']
  task['ao_split']={a:sum(p['mark_tariff']/len(p['assessment_objectives']) for p in current if a in p['assessment_objectives']) for a in ['A','B','C']}
 order['planned_item_count']=len(d['items']);order['marks_equivalent_total']=sum(x['mark_tariff'] for x in d['items'])
 contract['required_outputs']['learning_items']=len(d['items']);contract['depth_constraints']['item_budget']=len(d['items'])
 extraobjs=sorted({oid for x in d['items'] for oid in x['objective_ids']}-set(contract['scope']['included_objective_ids']))
 contract['scope']['included_objective_ids']+=extraobjs;contract['scope']['included_count']=len(contract['scope']['included_objective_ids'])
 # Command extension is explicitly author judgement, never a claim about syllabus wording.
 for x in d['items']:
  if x['item_type']=='flashcard' and x['command_word']=='Explain':
   for oid in x['objective_ids']:
    obj=objectives[oid]
    if 'Describe' in obj['command_words'] and 'Explain' not in obj['command_words']:
     obj['command_words'].append('Explain');command_extensions.append({'objective_id':oid,'added':'Explain','basis':'Author judgement: causal prompt and linked credit; the original Describe command remains. Explain is observed in the held corpus.','example_item':x['item_id']})
 for obj in [d,ld,pp,order,unitlist]:clean(obj)
 if t==12:
  x=next(x for x in d['items'] if x['item_id'].startswith('ITEM-6117-12-014-'))
  cid='CLM-6117-12.2-02-T2';x['claim_ids']=[cid]
  c=next(c for c in ld['claims'] if c['claim_id']==cid)
  teaching='A measured change is found by subtracting the initial reading from the final reading. If both readings have the same additive zero offset, subtracting cancels that offset; unequal or changing offsets do not cancel.'
  c['text']+=' '+teaching;c['revision']+=1
  for u in unitlist:
   for b in u['blocks']:
    if cid in b['claim_ids']:b['text']+='\n\n'+teaching
 for x in d['items']:
  if x['item_id'] in ['ITEM-6117-3-P03','ITEM-6117-4-P03','ITEM-6117-6-P02','ITEM-6117-6-P03']:
   for path in dict.fromkeys(re.findall(r'visuals/[A-Za-z0-9_-]+\.svg',x['prompt'])):
    if ']('+path+')' not in x['prompt']:x['prompt']+='\n\n![Question stimulus]('+path+')'
 final_log.append(final_notes(t,d,ld,unitlist,notes,reg))
 # Current traceability and hashes; factual claims survive without copied Q&A blocks.
 revisions={c['claim_id']:c['revision'] for c in ld['claims']}
 def stamp(x):
  x['claims_seen']={cid:revisions[cid] for cid in x.get('claim_ids',[])};old=x.get('authored_hash');new=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  if old and new!=old:x.update(prior_hash=old,repair_note='Learner-review repair: independent stimuli, explicit coverage and de-duplicated teaching.')
  elif old:x['reviewed_unchanged']='Relevant teaching remains correct after review; claim references reconciled.'
  x['authored_hash']=new
 for x in d['items']:
  stamp(x)
  if x['item_type']=='flashcard':rows.append({'id':x['item_id'],'topic':str(t),'kind':'card','subtype':x['subtype'],'marks':x['mark_tariff'],'recall_marks':item_recall[x['item_id']],'non_recall_marks':x['mark_tariff']-item_recall[x['item_id']],'basis':'Author credit-level judgement: explicit new factual/formula/diagram reproduction counted; supplied-data processing and causal credit separate. Independent confirmation pending.','prompt':x['prompt'],'credit_points':x['marking_guidance'],'fingerprint':fp(x)})
 for p,u in units.items():
  for b in u['blocks']:stamp(b)
  u['word_count']=sum(len(b['text'].split()) for b in u['blocks']);save(p,u)
 notes.setdefault('deviations',[]).append({'from':'Copied card worked-practice blocks and incomplete independent assessment of some syllabus skills','to':'Removed verbatim card questions and scoring text; added syllabus-grounded tasks and supplemental teaching; corrected activity leaks and current subtype IDs','why':'User-directed learner review repairs. Source extraction omission for chemical water test corrected from syllabus PDF p.37.','new_item_ids':new_ids})
 for p,v in [(ip,d),(f'{td}/claims/canonical_claim_ledger.json',ld),(f'{td}/authored_assessment_parts.json',pp),(f'{td}/work_order.json',order),(f'{td}/contract.json',contract),(f'{td}/authoring_notes.json',notes)]:save(p,v)
 budget.append({'topic_id':str(t),'cards':sum(x['item_type']=='flashcard' for x in d['items']),'activities':sum(x['item_type']!='flashcard' for x in d['items']),'items':len(d['items']),'marks':sum(x['mark_tariff'] for x in d['items']),'source':ip})
summary={'entries':len(rows),'cards':sum(r['kind']=='card' for r in rows),'activity_parts':sum(r['kind']=='activity_part' for r in rows),'marks':sum(r['marks'] for r in rows),'recall_marks':sum(r['recall_marks'] for r in rows)};summary['recall_percent']=100*summary['recall_marks']/summary['marks']
save('planning/full-demand-audit.json',{'reviewer':'Codex author','method':'Explicit credit allocation under the execution-versus-recitation policy. Coverage additions include conservative factual credit. Labels do not set the count.','summary':summary,'records':rows,'limitations':'Author estimates; independent cognitive-demand review and acceptance remain open.'})
save('planning/round5-id-migration.json',migration);save('planning/round5-repair-log.json',{'card_changes':log,'added_cards':sum(len([n for n in NEW if n['topic']==t]) for t in range(1,13)),'removed_copied_practice_blocks':dropped_blocks,'summary':summary})
save('curriculum/item-budget.json',{'basis':'User-authorised learner-review coverage corrections; computed from actual authored output.','qualification':'NSSCO Chemistry 6117','topics':budget,'total_items':sum(x['items'] for x in budget),'total_marks':sum(x['marks'] for x in budget)})
reg['objectives'].sort(key=lambda o:tuple(int(n) for n in re.findall(r'\d+',o['objective_id'])))
save('curriculum/objective_registry.json',reg);save('planning/round5-command-extensions.json',command_extensions)
save('planning/final-editorial-log.json',final_log)
print(json.dumps(summary,indent=2));print('Removed copied card practice blocks:',dropped_blocks)
