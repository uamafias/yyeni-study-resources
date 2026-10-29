"""Package original authored Topic 1 content with the unchanged repository schemas."""
import copy,hashlib,json,re,sys,subprocess
from pathlib import Path
from collections import defaultdict
W=Path(__file__).resolve().parents[1];R=W.parents[1];T=W/'topics/1'
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
from topic1 import LESSONS
from topic1_activities import MC,SHORT_PROMPTS,SHORT_ANSWERS,SHORT_GUIDANCE,PRACTICAL_PROMPTS,PRACTICAL_ANSWERS,PRACTICAL_GUIDANCE

def read(p):return json.loads(p.read_text())
def save(p,d):p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def stamp(a):a['authored_hash']=hashlib.sha256(_artefact_text(a).encode()).hexdigest();return a
order=read(T/'work_order.json');registry={o['objective_id']:o for o in read(W/'curriculum/objective_registry.json')['objectives']};claims=[];blocks=defaultdict(list);items=[];deviations=[];parts=[]

def claim(cid,oids,text,kind='factual'):
 claims.append({'claim_id':cid,'objective_ids':oids,'text':text,'claim_type':kind,'provenance':'generated_gap','evidence':[],'derived_from_claim_ids':[],'revision':1,'verification':{'status':'unverified','method':'New authoring; semantic review required before learner release.','reviewer_id':None,'reviewed_at':None,'confidence':0.9},'publishable':False})
 return cid

def block(uid,title,text,oids,cids,kind='plain_explanation'):
 blocks[uid].append(stamp({'block_id':f'{uid}-B{len(blocks[uid])+1:03d}','block_type':kind,'heading':title,'text':text,'claim_ids':cids,'context_tags':[],'assessment_objectives':sorted({a for oid in oids for a in registry[oid]['assessment_objectives']}),'claims_seen':{c:1 for c in cids}}))

def item(iid,oids,cids,kind,subtype,prompt,answer,guidance,ao,bloom,word,marks,difficulty=3):
 return stamp({'item_id':iid,'objective_ids':oids,'claim_ids':cids,'item_type':kind,'subtype':subtype,'assessment_objectives':ao,'difficulty':difficulty,'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original Chemistry 6117 authoring; no official question or report wording reproduced.','qa_status':'review_required','blooms_level':bloom,'command_word':word,'mark_tariff':marks,'claims_seen':{c:1 for c in cids}})

def guidance_shape(st,gs):
 # Labels describe the rubric sections, not extra credit or generic answer padding.
 labels={'CALC':'Equation/formula and working; numerical result and units: ','PROC':'Method/sequence and resulting observation: ','MECH':'Cause/reason and resulting effect: ','FEATURE':'Required feature/property: ','DEF':'Meaning or identity: ','APP':'Given case and supporting reason: ','INTERP':'Data interpretation and conclusion: '}
 return list(gs)
byobj=defaultdict(list)
for s in order['item_slots']:byobj[s['objective_id']].append(s)
for unit in order['content_units']:
 for oid in unit['objective_ids']:
  l=LESSONS[oid];uid=unit['unit_id'];paragraphs=l['text'].split('\n\n');base=[]
  for index,paragraph in enumerate(paragraphs):
   cid=claim('CLM-6117-'+oid.removeprefix('OBJ-6117-')+f'-T{index+1}',[oid],re.split(r'(?<=[.!?])\s+',paragraph)[0]);base.append(cid)
  block(uid,l['title'],l['text'],[oid],base)
  assert len(l['cards'])==len(byobj[oid]),oid
  for index,(s,card) in enumerate(zip(byobj[oid],l['cards'])):
   prompt,answer,guidance=card;st=s['subtype'];ao=s['assessment_objectives'];bloom=s['blooms_level']
   if s['slot']=='ITEM-6117-1-031-CALC':
    deviations.append({'item_id':s['slot'],'from':'CALC/B/Apply','to':'DEF/A/Remember','why':'The planned Identify command asks for the SI mass unit, not a calculation. The second slot retains conversion practice.'});st='DEF';ao=['A'];bloom='Remember'
   if oid=='OBJ-6117-1.5-03':
    bloom='Apply';ao=['B'];st='INTERP';deviations.append({'item_id':s['slot'],'from':'A/Remember','to':'INTERP/B/Apply','why':'The actual prompt identifies a sample using supplied reference melting-point data.'})
   if oid=='OBJ-6117-1.5-09':prompt=prompt.replace('Calculate','Calculate from the chromatogram distances:',1)
   cid=claim('CLM-'+s['slot'].removeprefix('ITEM-'),[oid],answer,'synthetic_example');items.append(item(s['slot'],[oid],base+[cid],'flashcard',st,prompt,answer,guidance_shape(st,guidance),ao,bloom,s['command_word'],s['mark_tariff'],s['difficulty']))
   block(uid,'Worked practice — '+l['title'],prompt+'\n\n'+answer+'\n\nChecking the response: '+' '.join(guidance),[oid],base+[cid],'worked_calculation' if st=='CALC' else 'worked_application')
# Add the three original activities and teach every answer in the corresponding notes.
for task in order['performance_tasks']:
 kind=task['item_type'];subparts=copy.deepcopy(task['parts']);prompts=[];answers=[];rubrics=[];cids=[];oids=[]
 for n,p in enumerate(subparts):
  if kind=='multiple_choice_set':
   q,options,key,reason,distractors=MC[n];prompt=q+'\n'+'\n'.join(f'{chr(65+j)}. {v}' for j,v in enumerate(options));answer=key+'. '+options[ord(key)-65]+' '+reason;guidance=['Correct option/key '+key+' (1 mark). Reason: '+reason+' Distractor explanations: '+distractors]
   if n==0:p['assessment_objectives']=['B'];p['blooms_level']='Apply';deviations.append({'item_id':task['slot']+' part 1','from':'A/Understand','to':'B/Apply','why':'The authored item subtracts supplied syringe readings to calculate collected volume.'})
  elif kind=='short_answer':prompt=SHORT_PROMPTS[n];answer=SHORT_ANSWERS[n];guidance=SHORT_GUIDANCE[n]
  else:prompt=PRACTICAL_PROMPTS[n];answer=PRACTICAL_ANSWERS[n];guidance=PRACTICAL_GUIDANCE[n]
  p.update(prompt=prompt,canonical_answer=answer,marking_guidance=guidance);p['task_id']=task['slot'];parts.append(p);cid=claim('CLM-'+task['slot'].removeprefix('ITEM-')+'-'+str(n+1),p['objective_ids'],answer,'synthetic_example');cids.append(cid);oids.extend(p['objective_ids'])
  prompts.append(f"({p['part']}) {prompt} [{p['mark_tariff']}]");answers.append(f"({p['part']}) {answer}");rubrics+= [f"Part {p['part']}: "+x for x in guidance]
  # Practical answers are co-taught in the scientific-processes notes even when a
  # performance part credits the more specific Annex A objective.
  uid=next((u['unit_id'] for u in order['content_units'] if any(o in u['objective_ids'] for o in p['objective_ids'])),'CU-6117-1.2.2' if n in [0,2,3] else 'CU-6117-1.5')
  block(uid,'Activity worked example '+task['slot']+' ('+p['part']+')',prompt+'\n\n'+answer+'\n\n'+' '.join(guidance),p['objective_ids'],[cid],'worked_application')
 if kind=='practical_task':rubrics.insert(0,'Apparatus/method, data and observations, then a supported conclusion or improvement are marked by the explicit points below.')
 if kind=='short_answer':rubrics.insert(0,'Award marks for each distinct chemical point or reason listed below; accept equivalent accurate wording.')
 ao=sorted({a for p in subparts for a in p['assessment_objectives']})
 items.append(item(task['slot'],list(dict.fromkeys(oids)),cids,kind,None,'\n\n'.join(prompts),'\n\n'.join(answers),rubrics,ao,task['blooms_level'],None,task['mark_tariff']))
# Specific suggested practical experiences retained in the notes, original wording.
practice=[('Crystallisation from solution','Under teacher supervision, gently concentrate a salt solution without boiling it dry. Allow it to cool, then separate and dry the crystals. Record when crystals first appear and compare their appearance with the starting solution. Use a small cold-solvent wash to reduce adhering impurities; explain why a large hot wash could reduce yield.'),('Distillation of a fermented sample','Use a teacher-prepared fermented sample with supervised apparatus and a suitable non-flame heating method. Record vapour temperature as distillate is collected. Explain the roles of the condenser and fractionating column where used. Do not taste the distillate or assume it is pure or safe; the task is to interpret separation by volatility.'),('Filtration of muddy water','Stir a prepared water-and-sand mixture, then filter it through paper in a funnel. Record the retained residue and clarity of the filtrate. Explain why removing suspended solid does not establish that water is safe to drink: dissolved material and microorganisms may remain.'),('Chromatography of coloured substances','Place small coloured-sample spots and a reference on a pencil baseline. Keep the starting spots above the solvent and develop the chromatogram under supervision. Mark the solvent front, count separated spots and measure their baseline distances. Calculate Rf values and compare references under the same conditions; avoid claiming that a single spot proves complete purity.')]
for title,txt in practice:block('CU-6117-1.5','Suggested practical — '+title,txt,['OBJ-6117-1.5-06'],[c['claim_id'] for c in claims if c['objective_ids']==['OBJ-6117-1.5-06']][:2],'practice_guidance')
for unit in order['content_units']:
 uid=unit['unit_id'];obs=unit['objective_ids'];bs=blocks[uid]
 block(uid,'Connections','Use these methods when calculating solution quantities in Stoichiometry, interpreting reactions in Chemical reactions, and evaluating laboratory methods in Practical skills and investigation planning.',obs,[],'cross_link')
 wc=sum(len(b['text'].split()) for b in bs);lo,hi=unit['word_budget'];save(T/unit['file'],{'unit_id':uid,'title':{'1.1':'Mathematical requirements','1.2.1':'Planning investigations','1.2.2':'Recording and presenting results','1.3':'Units and scales','1.4':'Evaluating measurements','1.5':'Apparatus, purity and separation'}[unit['sub_topic']],'objective_ids':obs,'level':'NSSCO','core_status':'core','objective_type':'chem_practical','depth_tier':3,'word_budget':{'min':lo,'target':round((lo+hi)/2),'max':hi},'blocks':bs,'word_count':wc,'qa_status':'review_required'})
 print(uid,wc,'budget',lo,hi)
save(T/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6117-1','claims':claims})
save(T/'learning-items/topic_1_items.json',{'dataset_id':'ITEMS-6117-1','topic_id':'1','items':items})
save(T/'authored_assessment_parts.json',{'parts':parts,'basis':'Actual authored prompts/answers; updated cognitive labels are recorded as deviations.'})
save(T/'authoring_notes.json',{'topic_id':'1','deviations':deviations,'source_policy':'Official sources used only for scope and demand; all prompts, prose, datasets and answers are original.','visuals':'Generated with authoring/render_topic1_visuals.py; actual figure geometry and numerical inputs are retained.'})
contract=read(T/'contract.json');contract['depth_constraints']['item_budget']=len(items);contract['required_outputs']['learning_items']=len(items);contract['required_outputs']['content_units']=len(order['content_units']);save(T/'contract.json',contract)
subprocess.run([sys.executable,str(R/'standard/v0.2.0-draft/build/render_notes.py'),str(W),'1'],check=True)
subprocess.run([sys.executable,str(W/'planning/check_resource_topic.py'),'1'],check=True)
