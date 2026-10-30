"""Schema assembly only: prose, facts and tasks are explicitly authored in topic files.
No generated teaching sentences, card answers, slot labels or contract counts.
"""
from pathlib import Path
import json,re,hashlib,sys
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def stamp(x,cids,block=False):
 x['claims_seen']={c:1 for c in cids}
 if not block:x['qa_status']='review_required'
 x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()

def assemble(tid,facts,cards,tasks,sources):
 td=W/'topics'/tid;wo=read(td/'work_order.json');reg={o['objective_id']:o for o in read(W/'curriculum/objective_registry.json')['objectives']};prov=read(W/'planning/registry-provenance-6137.json')['sources'];prefix='OBJ-6137-'+tid+'.';byobj={};claims=[]
 for suffix,pair in facts.items():
  oid=suffix if suffix.startswith('OBJ-') else prefix+suffix;assert oid in reg;byobj[oid]=[]
  for n,text in enumerate(pair,1):
   cid='CL-6137-'+tid+'.'+suffix+'-'+str(n);byobj[oid].append(cid)
   claims.append({'claim_id':cid,'objective_ids':[oid],'text':text,'claim_type':'factual','provenance':'source_synthesised','evidence':[{'source_id':'SCOPE-6137-'+tid,'locator':json.dumps(prov[oid]['source'],ensure_ascii=False),'support_type':'corroboration'},{'source_id':'AUTHOR-SOURCES-6137-'+tid,'locator':f'authoring/{tid}-source-register.json; scope and synthesis, not independent verification','support_type':'corroboration'}],'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Codex source-informed authoring; independent semantic review pending.','reviewer_id':None,'reviewed_at':None,'confidence':0.8},'publishable':False,'revision':1})
 assert set(byobj)==set(read(td/'contract.json')['scope']['included_objective_ids'])
 dump(td/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6137-'+tid,'claims':claims})
 sections=re.split(r'\n## \d\d ',(W/'authoring'/f'{tid}-notes.md').read_text())[1:];assert len(sections)==len(wo['content_units'])
 for up,section in zip(wo['content_units'],sections):
  title,body=section.split('\n',1);paras=[p.strip() for p in body.split('\n\n') if p.strip()];cids=[c for o in up['objective_ids'] for c in byobj[o]];blocks=[]
  for n,text in enumerate(paras,1):
   kind='definition' if n==1 else 'cross_link' if n==len(paras) else 'worked_application' if any(k in text.lower() for k in ['consider','suppose','resource','imagine','original','hypothetical','teaching record']) else 'plain_explanation'
   b={'block_id':up['unit_id'].replace('CU-','BL-')+f'-{n:02d}','block_type':kind,'heading':title if n==1 else '','text':text,'claim_ids':cids,'context_tags':['Geography','original teaching'],'assessment_objectives':sorted({a for o in up['objective_ids'] for a in reg[o]['assessment_objectives']})};stamp(b,cids,True);blocks.append(b)
  lo,hi=up['word_budget'];dump(td/up['file'],{'unit_id':up['unit_id'],'title':title,'objective_ids':up['objective_ids'],'level':'NSSCO','core_status':'core','objective_type':reg[up['objective_ids'][0]]['objective_type'],'depth_tier':max(reg[o]['depth_tier'] for o in up['objective_ids']),'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},'blocks':blocks,'word_count':sum(len(b['text'].split()) for b in blocks),'qa_status':'review_required'})
 items=[];visuals={r['assigned_item_id']:r for r in read(W/'planning/visual-resource-plan-6137.json')['resources'] if r['topic_id']==tid}
 for slot in wo['item_slots']:
  number=slot['slot'].split('-')[-2];prompt,answer,guide=cards[number];oid=slot['objective_id'];cids=byobj[oid]
  item={'item_id':slot['slot'],'objective_ids':[oid],'claim_ids':cids,'item_type':'flashcard',**{k:slot[k] for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff','difficulty']},'prompt':prompt,'canonical_answer':answer,'marking_guidance':guide,'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original self-contained Geography resource; invented numbers and scenarios are synthetic, not real-place measurements.','facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original Codex authoring; official wording is not reproduced.'}
  if slot['subtype']=='MISCON':
   m=re.search(r'MIS-6137-\d+',slot['reason']);assert m;item['misconception_entry']=m.group(0)
  if item['item_id'] in visuals:item['context']['situation']='VISUAL PENDING: '+visuals[item['item_id']]['resource_id']+'; Claude authoring and separate Codex review required before use.'
  stamp(item,cids);items.append(item)
 assert len(wo['performance_tasks'])==len(tasks)
 for slot,task in zip(wo['performance_tasks'],tasks):
  oids=[x if x.startswith('OBJ-') else prefix+x for x in task['objectives']];cids=[c for o in oids for c in byobj[o]]
  item={'item_id':slot['slot'],'objective_ids':oids,'claim_ids':cids,'item_type':slot['item_type'],'subtype':None,'assessment_objectives':list(task['split']),'blooms_level':slot['blooms_level'],'command_word':'How far do you agree' if slot['item_type']=='case_analysis' else 'Describe','mark_tariff':sum(task['split'].values()),'difficulty':3,'prompt':task['prompt'],'canonical_answer':task['answer'],'marking_guidance':task['guide'],'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original multipart Geography teaching package; part-level specifications in authoring_notes.json.','facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original Codex package, not a copied examination question.'}
  if task.get('assets_required'):item['context']['situation']='VISUAL PENDING: '+ '; '.join(task['assets_required'])
  stamp(item,cids);items.append(item)
 dump(td/wo['output_files']['learning_items'],{'dataset_id':'DATA-6137-'+tid,'topic_id':tid,'items':items})
 dump(td/'authoring_notes.json',{'topic_id':tid,'author':'Codex','deviations':[],'state':'Text draft only; mandatory visuals and independent content review pending.','visual_pending':list(visuals),'performance_parts':{s['slot']:{'ao_split':t['split'],'assets_required':t.get('assets_required',[]),'parts':[{'part':a,'command_word':b,'mark_tariff':c,'ao':d} for a,b,c,d in t['parts']]} for s,t in zip(wo['performance_tasks'],tasks)},'schema_note':'Current schema places qa_status on units/items, forbids it on blocks; blocks retain claims_seen and hashes.'})
 dump(W/'authoring'/f'{tid}-source-register.json',{'sources':[{'source_id':a,'url':b} for a,b in sources],'read_on':'2026-10-29','review_status':'Codex author synthesis, not independent semantic review','synthetic_resources':'All original grids, dimensions, velocities, sediment figures and hypothetical scenarios are teaching data, not real-place measurements.','case_policy':'Primary source accounts are dated; no unsupported current population percentages, yields or flood statistics are asserted.'})
 print(tid,len(claims),'claims;',len(wo['content_units']),'units;',len(items),'draft items; mandatory visuals pending',len(visuals))
