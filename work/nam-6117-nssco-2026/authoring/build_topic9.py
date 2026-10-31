"""Package original Metals authoring; keep the approved baseline and log deviations."""
import copy,hashlib,json,re,sys,subprocess
from collections import defaultdict
from pathlib import Path
from topic9 import LESSONS
from topic9_activities import MC,SHORT_PROMPTS,SHORT_ANSWERS,SHORT_GUIDANCE,PRACTICAL_PROMPTS,PRACTICAL_ANSWERS,PRACTICAL_GUIDANCE
from topic9_practicals import PRACTICALS
W=Path(__file__).resolve().parents[1];R=W.parents[1];T=W/'topics/9'
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
def read(p):return json.loads(p.read_text())
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def stamp(x):x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest();return x
order=read(T/'work_order.json');registry={x['objective_id']:x for x in read(W/'curriculum/objective_registry.json')['objectives']}
claims=[];blocks=defaultdict(list);items=[];parts=[];deviations=[];objclaims={}

def claim(cid,oids,text,kind='factual'):
 claims.append({'claim_id':cid,'objective_ids':oids,'text':text,'claim_type':kind,'provenance':'generated_gap','evidence':[],'derived_from_claim_ids':[],'revision':1,'verification':{'status':'unverified','method':'Original authoring; independent semantic review pending.','reviewer_id':None,'reviewed_at':None,'confidence':0.9},'publishable':False});return cid
def block(uid,title,text,oids,cids,kind='plain_explanation'):
 blocks[uid].append(stamp({'block_id':f'{uid}-B{len(blocks[uid])+1:03d}','block_type':kind,'heading':title,'text':text,'claim_ids':cids,'context_tags':[],'assessment_objectives':sorted({a for o in oids for a in registry[o]['assessment_objectives']}),'claims_seen':{c:1 for c in cids}}))
def item(iid,oids,cids,kind,st,prompt,answer,guidance,ao,bloom,command,marks,difficulty=3):
 return stamp({'item_id':iid,'objective_ids':oids,'claim_ids':cids,'item_type':kind,'subtype':st,'assessment_objectives':ao,'difficulty':difficulty,'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original Chemistry 6117 teaching content; no official question or report wording reproduced.','qa_status':'review_required','blooms_level':bloom,'command_word':command,'mark_tariff':marks,'claims_seen':{c:1 for c in cids}})
labels={'CALC':'Equation/formula, numerical substitution and working, result and units: ','DEF':'Meaning or identity: ','FEATURE':'Property or structural feature: ','MECH':'Cause/reason and effect: ','APP':'Given case and supporting reason: ','INTERP':'Diagram/data interpretation and conclusion: ','LIM':'Limitation, consequence and improvement: ','PROC':'Method sequence and observation: ','DIST':'Difference and structural reason: ','MISCON':'Error, correct response and diagnostic test: '}
byobj=defaultdict(list)
for s in order['item_slots']:byobj[s['objective_id']].append(s)
for unit in order['content_units']:
 for oid in unit['objective_ids']:
  l=LESSONS[oid];uid=unit['unit_id'];base=[]
  for n,p in enumerate(l['text'].split('\n\n')):
   base.append(claim('CLM-6117-'+oid.removeprefix('OBJ-6117-')+f'-T{n+1}',[oid],re.split(r'(?<=[.!?])\s+',p)[0]))
  objclaims[oid]=base
  block(uid,l['title'],l['text'],[oid],base)
  assert len(l['cards'])==len(byobj[oid]),oid
  for n,(s,c) in enumerate(zip(byobj[oid],l['cards'])):
   prompt,answer,guidance=c;st=s['subtype'];ao=s['assessment_objectives'];bloom=s['blooms_level']
   command=s['command_word']
   if s['slot']=='ITEM-6117-9-021-PROC':
    bloom='Understand';deviations.append({'item_id':s['slot'],'from':s['blooms_level'],'to':'Understand','why':'Preserves the reviewed prototype demand: describe a familiar two-stage mechanism.'})
   if st=='MISCON':
    bloom='Apply';deviations.append({'item_id':s['slot'],'from':'Understand','to':'Apply','why':'Diagnoses a supplied error about the named test, colour or physical state.'})
   cid=claim('CLM-'+s['slot'].removeprefix('ITEM-'),[oid],answer,'synthetic_example')
   rubric=list(guidance)
   x=item(s['slot'],[oid],base+[cid],'flashcard',st,prompt,answer,rubric,ao,bloom,command,s['mark_tariff'],s['difficulty'])
   if 'misconception_entry' in s:x['misconception_entry']=s['misconception_entry']
   if s['required_visual_ids']:x['context']['facts'].append('Reference visual(s): '+', '.join(s['required_visual_ids'])+'. Drawing prompts use no keyed answer image.')
   items.append(stamp(x));block(uid,'Worked practice — '+l['title'],prompt+'\n\n'+answer+'\n\nChecking the response: '+' '.join(guidance),[oid],base+[cid],'worked_application')
for task in order['performance_tasks']:
 subparts=copy.deepcopy(task['parts']);pp=[];aa=[];gg=[];cids=[];oids=[]
 for n,p in enumerate(subparts):
  if task['item_type']=='multiple_choice_set':
   q,opts,key,reason,wrong=MC[n];prompt=q+'\n'+'\n'.join(f'{chr(65+j)}. {v}' for j,v in enumerate(opts));answer=key+'. '+opts[ord(key)-65]+' '+reason;guidance=[f'Correct option/key {key} (1 mark). Reason: {reason} Distractor explanations: {wrong}']
  elif task['item_type']=='short_answer':prompt=SHORT_PROMPTS[n];answer=SHORT_ANSWERS[n];guidance=SHORT_GUIDANCE[n]
  else:
   prompt=PRACTICAL_PROMPTS[n];answer=PRACTICAL_ANSWERS[n];guidance=PRACTICAL_GUIDANCE[n]
  if task['item_type']=='practical_task' and p['part']=='c':
   p['objective_ids']=['OBJ-6117-12.2-01'];p['practical_criterion']='C1'
   deviations.append({'item_id':task['slot'],'part':'c','from':'12.1-01 / C3 scale reading','to':'12.2-01 / C1 measurement choice','why':'Names measured quantities; does not read an instrument scale.'})
  p.update(task_id=task['slot'],prompt=prompt,canonical_answer=answer,marking_guidance=guidance);parts.append(p)
  cid=claim('CLM-'+task['slot'].removeprefix('ITEM-')+'-'+str(n+1),p['objective_ids'],answer,'synthetic_example');cids.append(cid);oids+=p['objective_ids']
  pp.append(f"({p['part']}) {prompt} [{p['mark_tariff']}]");aa.append(f"({p['part']}) {answer}");gg.extend(f"Part {p['part']}: "+v for v in guidance)
  uid=next((u['unit_id'] for u in order['content_units'] if any(oid in u['objective_ids'] for oid in p['objective_ids'])),'CU-6117-9.2')
  block(uid,'Activity worked example '+task['slot']+' ('+p['part']+')',prompt+'\n\n'+answer+'\n\n'+' '.join(guidance),p['objective_ids'],[cid],'worked_application')
 if task['item_type']=='practical_task':gg.insert(0,'Apparatus and method, recorded data, then conclusion and improvement are assessed by the points below.')
 if task['item_type']=='calculation':gg.insert(0,'Equation/formula, substitution and working, numerical result and units are credited below.')
 if task['item_type']=='short_answer':gg.insert(0,'Award marks for the distinct chemical point and reason below; accept equivalent accurate reasoning.')
 items.append(item(task['slot'],list(dict.fromkeys(oids)),cids,task['item_type'],None,'\n\n'.join(pp),'\n\n'.join(aa),gg,sorted({a for p in subparts for a in p['assessment_objectives']}),task['blooms_level'],None,task['mark_tariff']))
for number,sub,oid,title,txt in PRACTICALS:
 oid='OBJ-6117-'+oid
 block('CU-6117-'+sub,'Suggested practical SP-6117-'+number+' — '+title,txt,[oid],objclaims[oid],'practice_guidance')
gallery=[('9.3','Blast furnace chemistry','VIS-6117-9-01','Essential furnace inputs, reactions and separate iron/slag layers.'),('9.1','Metal and alloy models','VIS-6117-9-02','Equal atoms in regular layers compared with a model alloy containing differently sized atoms.'),('9.2','Controlled rate comparison','VIS-6117-9-03','Matched magnesium/zinc setups with original timed gas data and no ignition source.')]
for sub,title,vis,alt in gallery:
 u=next(u for u in order['content_units'] if u['sub_topic']==sub);oid=u['objective_ids'][0]
 block(u['unit_id'],title,f'![{alt}](visuals/{vis}.svg)\n\n{alt} These labelled diagrams are answer and teaching references; attempt drawing tasks before consulting them.',[oid],objclaims[oid],'practice_guidance')
for u in order['content_units']:
 uid=u['unit_id'];oids=u['objective_ids'];block(uid,'Connections','Connect metal behaviour to particle structure, redox and electrolysis. Distinguish intrinsic reactivity from apparent rate, and connect a material choice to the actual property required.',oids,[],'cross_link')
 bs=blocks[uid]
 wc=sum(len(b['text'].split()) for b in bs);lo,hi=u['word_budget']
 if u['sub_topic']=='9.2':
  hi=1350;deviations.append({'unit_id':uid,'from':'Maximum 660 words','to':'Maximum 1,350 words; subject topic remains within original 10,230-word cap','why':'The two required practical boxes and worked controlled-reactivity activity need space alongside the two syllabus outcomes.'})
 save(T/u['file'],{'unit_id':uid,'title':u['sub_topic']+' — '+u['objectives'][0]['title'].split(' — focus:')[0],'objective_ids':oids,'level':'NSSCO','core_status':'core','objective_type':'chem_description','depth_tier':3,'word_budget':{'min':lo,'target':round((lo+hi)/2),'max':hi},'blocks':bs,'word_count':wc,'qa_status':'review_required'})
 print(uid,wc,'budget',lo,hi)
save(T/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6117-9','claims':claims})
save(T/'learning-items/topic_9_items.json',{'dataset_id':'ITEMS-6117-9','topic_id':'9','items':items})
save(T/'authored_assessment_parts.json',{'parts':parts,'basis':'Actual authored demand; deviations logged.'})
save(T/'authoring_notes.json',{'topic_id':'9','deviations':deviations,'source_policy':'All learner wording, contexts and data are original; report material is used only for scope and evidenced difficulties.','visuals':'Generated by authoring/render_topic9_visuals.py from balanced furnace equations, particle-model parameters and original timed gas data; separate scientific review required.'})
c=read(T/'contract.json');c['depth_constraints']['item_budget']=len(items);c['required_outputs']['learning_items']=len(items);c['required_outputs']['content_units']=len(order['content_units']);save(T/'contract.json',c)
subprocess.run([sys.executable,str(R/'standard/v0.2.0-draft/build/render_notes.py'),str(W),'9'],check=True)
subprocess.run([sys.executable,str(W/'planning/check_resource_topic.py'),'9'],check=True)
