"""Assemble explicitly authored topic packets. No pedagogical text is templated here."""
import hashlib
import json
import sys
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def build(topic):
 td=WS/'topics'/topic
 packet=json.loads((td/'authored_packet.json').read_text())
 wo=json.loads((td/'work_order.json').read_text())
 reg={o['objective_id']:o for o in json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']}
 claims=[];ci={}
 for c in packet['claims']:
  key,objs,text,kind=c
  oid=[o if o.startswith('OBJ-') else 'OBJ-6145-'+topic+'-'+o for o in objs]
  claim={'claim_id':f'CL-6145-{topic}-{key}','objective_ids':oid,'text':text,'claim_type':kind,
   'provenance':'source_synthesised','evidence':[{'source_id':'NIED-6145-2018','locator':'PDF p.'+str(reg[oid[0]]['syllabus_page'])+'; '+oid[0],'support_type':'derivation'}],
   'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Original authoring from approved curriculum; independent review pending','reviewer_id':None,'reviewed_at':None,'confidence':0.85},'publishable':False,'revision':1}
  claim['evidence'].extend(packet.get('additional_evidence',{}).get(key,[]))
  claims.append(claim);ci[key]=claim
 assert len(ci)==len(claims)
 def cids(keys):return [ci[k]['claim_id'] for k in keys]
 def stamp(x):
  x['claims_seen']={c:1 for c in x['claim_ids']}
  x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  return x
 units=[]
 for uplan in wo['content_units']:
  body=packet['units'][uplan['unit_id']]
  blocks=[]
  for n,(kind,heading,text,keys) in enumerate(body,1):
   b={'block_id':uplan['unit_id']+'-B'+str(n).zfill(2),'block_type':kind,'heading':heading,'text':text,
      'claim_ids':cids(keys),'context_tags':['Namibia','original teaching'],'assessment_objectives':sorted({a for o in uplan['objective_ids'] for a in reg[o]['assessment_objectives']})}
   blocks.append(stamp(b))
  lo,hi=uplan['word_budget']
  unit={'unit_id':uplan['unit_id'],'title':packet.get('titles',{}).get(uplan['unit_id'],wo['topic_title']+' — '+uplan['sub_topic']),
   'objective_ids':uplan['objective_ids'],'level':'NSSCO','core_status':'core','objective_type':'economics_concept',
   'depth_tier':max(o['depth_tier'] for o in uplan['objectives']),'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},
   'blocks':blocks,'word_count':sum(len(b['text'].split()) for b in blocks),'qa_status':'review_required'}
  units.append(unit)
 cards={c[0]:c[1:] for c in packet['cards']}
 perfs={p[0]:p[1:] for p in packet['performance']}
 items=[]
 def base(slot,p,a,g,keys,oids,itemtype,subtype,aos,difficulty,bloom,command,tariff):
  return stamp({'item_id':slot,'objective_ids':oids,'claim_ids':cids(keys),'item_type':itemtype,
   'subtype':subtype,'assessment_objectives':aos,'difficulty':difficulty,'prompt':p,'canonical_answer':a,'marking_guidance':g,
   'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original case or focused retrieval','facts':[]},
   'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'original Codex authoring from approved 6145 curriculum',
   'qa_status':'review_required','blooms_level':bloom,'command_word':command,'mark_tariff':tariff})
 for s in wo['item_slots']:
  short=s['slot'].split('-')[-2]
  p,a,g,keys=cards.pop(short)
  i=base(s['slot'],p,a,g,keys,[s['objective_id']],'flashcard',s['subtype'],s['assessment_objectives'],s['difficulty'],s['blooms_level'],s['command_word'],s['mark_tariff'])
  if s.get('misconception_entry'):i['misconception_entry']=s['misconception_entry']
  items.append(i)
 for s in wo['performance_tasks']:
  p,a,g,keys,oidshort=perfs.pop(s['item_type'])
  ids=[o if o.startswith('OBJ-') else 'OBJ-6145-'+topic+'-'+o for o in oidshort]
  kind=s['item_type'];aos={'data_response':['B','C'],'short_answer':['A'],'case_analysis':['A','B','C'],'essay_plan':['C']}[kind]
  cmd={'data_response':'Describe','short_answer':'Define','case_analysis':'Define','essay_plan':'Evaluate'}[kind]
  tariff={'data_response':20,'short_answer':16,'case_analysis':20,'essay_plan':9}[kind]
  items.append(base(s['slot'],p,a,g,keys,ids,kind,None,aos,4,s['blooms_level'],cmd,tariff))
 assert not cards and not perfs
 for d in ['claims','content-units','learning-items']:(td/d).mkdir(exist_ok=True)
 for path,data in [(td/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6145-'+topic,'claims':claims}),
                   (td/'learning-items'/('topic_'+topic+'_items.json'),{'dataset_id':'ITEMS-6145-'+topic,'topic_id':topic,'items':items})]+[(td/'content-units'/(u['unit_id']+'.json'),u) for u in units]:
  path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
 (td/'authoring_notes.json').write_text(json.dumps({'topic_id':topic,'deviations':packet.get('deviations',[]),'judgements':packet.get('judgements',[]),'source_limitations':['Original authoring follows the approved glossary and source-anomaly register; independent subject review remains pending.']},indent=2)+'\n')
 print(topic,len(claims),'claims,',len(units),'units,',len(items),'items,',sum(u['word_count'] for u in units),'words')

if __name__=='__main__':build(sys.argv[1])
