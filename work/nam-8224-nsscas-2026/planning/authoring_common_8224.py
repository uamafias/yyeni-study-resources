"""Small authoring helpers; inputs are authored content, never source prose."""
import hashlib
import json
from pathlib import Path
import re
import sys

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text


def read(path):return json.loads(Path(path).read_text())
def write(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=1,ensure_ascii=False)+'\n')
def words(text):return len(re.findall(r"\b[\w′'⁻]+\b",text))
def stamp(value):value['authored_hash']=hashlib.sha256(_artefact_text(value).encode()).hexdigest()


class Topic:
    def __init__(self,topic):
        self.topic=topic;self.dir=WS/'topics'/topic
        self.wo=read(self.dir/'work_order.json')
        self.claims=[];self.blocks={};self.items=[];self.deviations=[]

    def objective(self,short,claims,paragraphs,source,locator):
        oid=f'OBJ-8224-{self.topic}{short}' if short.startswith('-') else f'OBJ-8224-{self.topic}.{short}'
        cids=[]
        for text in claims:
            cid=f'CLM-8224-{self.topic}-{len(self.claims)+1:03}'
            self.claims.append({'claim_id':cid,'objective_ids':[oid],'text':text,'claim_type':'factual','provenance':'generated_gap','evidence':[{'source_id':source,'locator':locator,'support_type':'paraphrase'}],'derived_from_claim_ids':[],'revision':1,'verification':{'status':'unverified','method':'Authored after reading the cited local reference; independent cross-vendor semantic review remains outstanding.','reviewer_id':None,'reviewed_at':None,'confidence':0.95},'publishable':False,'notes':[]});cids.append(cid)
        self.blocks[oid]=[]
        for heading,text in paragraphs:
            b={'block_id':f'{self.topic}-{short}-b{len(self.blocks[oid])+1}','block_type':'plain_explanation','heading':heading,'text':text,'claim_ids':cids,'context_tags':[],'assessment_objectives':['A','B'],'claims_seen':dict.fromkeys(cids,1)}
            stamp(b);self.blocks[oid].append(b)

    def claims_for(self,oids):return [c['claim_id'] for c in self.claims if set(c['objective_ids']) & set(oids)]

    def item(self,slot,prompt,answer,subtype=None,guidance=None):
        oids=slot.get('objective_ids') or [slot['objective_id']]
        cids=self.claims_for(oids)
        st=subtype or slot.get('subtype')
        if guidance is None:
            parts=slot.get('marking_guidance_must_name',[])
            if subtype=='WHY':parts=['reason','because','effect']
            guidance=['Required answer parts: '+', '.join(parts)+'. Use the specific chemically correct points in the canonical answer; award no additional credit for repetition.']
        x={'item_id':slot['slot'],'objective_ids':oids,'claim_ids':cids,'item_type':slot.get('item_type','flashcard'),'subtype':st,'assessment_objectives':slot['assessment_objectives'],'blooms_level':slot['blooms_level'],'command_word':slot['command_word'],'mark_tariff':slot['mark_tariff'],'difficulty':slot.get('difficulty',3),'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original item authored from the frozen Chemistry 8224 work order and locally recorded factual references.','qa_status':'review_required','claims_seen':dict.fromkeys(cids,1)}
        if slot.get('misconception_entry'):x['misconception_entry']=slot['misconception_entry']
        stamp(x);self.items.append(x)

    def save(self):
        assert len(self.items)==self.wo['planned_item_count']
        assert len({i['item_id'] for i in self.items})==len(self.items)
        write(self.dir/'claims/canonical_claim_ledger.json',{'ledger_id':f'CLM-LEDGER-8224-{self.topic}','claims':self.claims})
        total_words=0
        for planned in self.wo['content_units']:
            blocks=[b for oid in planned['objective_ids'] for b in self.blocks[oid]]
            count=sum(words(b['text']) for b in blocks);total_words+=count
            lo,hi=planned['word_budget']
            write(self.dir/planned['file'],{'unit_id':planned['unit_id'],'title':self.wo['topic_title']+' — '+planned['sub_topic'],'objective_ids':planned['objective_ids'],'level':'NSSCAS','core_status':'core','objective_type':'integrated_teaching','depth_tier':max(o['depth_tier'] for o in planned['objectives']),'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},'blocks':blocks,'word_count':count,'qa_status':'review_required','notes':['Original teaching prose; source-backed claim ledger. Independent semantic review remains required.']})
        write(self.dir/'learning-items'/f'topic_{self.topic}_items.json',{'dataset_id':f'ITEMS-8224-{self.topic}','topic_id':self.topic,'items':self.items})
        write(self.dir/'authoring_notes.json',{'topic_id':self.topic,'deviations':self.deviations,'source_policy':'Local sources read before authoring; original prose and questions. Textbook source locators support concepts; worked data are original and transparently derived.','review_status':'Independent semantic and human visual review outstanding.'})
        print(self.topic,len(self.claims),'claims',len(self.wo['content_units']),'units',len(self.items),'items',total_words,'words')
