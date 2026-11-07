"""Serialize original authored material with the approved metadata interfaces."""
import hashlib
import json
import sys
from pathlib import Path
WS=Path(__file__).resolve().parents[2];ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p):return json.loads(p.read_text())
def save(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def stamp(x):
    x['claims_seen']={c:1 for c in x['claim_ids']}
    x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x

class Topic:
    def __init__(self,tid):
        self.tid=tid;self.td=WS/'topics'/tid
        self.wo=read(self.td/'work_order.json');self.contract=read(self.td/'contract.json')
        self.claims=[];self.blocks=[];self.items=[];self.claim_map={}
        self.registry={o['objective_id']:o for o in read(WS/'curriculum/objective_registry.json')['objectives']}
    def oid(self,local):return 'OBJ-6145-'+self.tid+'-'+local
    def claim(self,local,text,kind='factual'):
        oid=self.oid(local);cid=f'CLM-6145-{self.tid}-{len(self.claims)+1:03}'
        self.claims.append({'claim_id':cid,'objective_ids':[oid],'text':text,'claim_type':kind,
          'provenance':'generated_quality','evidence':[{'source_id':'NIED-6145-2018',
          'locator':f"PDF page {self.registry[oid]['syllabus_page']}, topic {self.tid}; original teaching derivation",'support_type':'derivation'}],
          'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Original author statement; independent semantic review pending.','reviewer_id':None,'reviewed_at':None,'confidence':0.9},
          'publishable':False,'revision':1})
        self.claim_map.setdefault(local,[]).append(cid)
        return cid
    def block(self,locals,kind,heading,text,scope=None):
        cids=list(dict.fromkeys(c for local in locals.split() for c in self.claim_map[local]))
        self.blocks.append(stamp({'block_id':f'B-6145-{self.tid}-{len(self.blocks)+1:03}',
          'block_type':kind,'heading':heading,'text':text.strip(),'claim_ids':cids,
          'context_tags':['Namibia','original invented teaching data'],'assessment_objectives':['A','B','C']}))
        if scope:self.blocks[-1]['generalisation_scope']=[self.oid(o) for o in scope.split()]
    def card(self,slot,locals,prompt,answer,guidance,facts=None):
        if isinstance(slot,str):
            hits=[s for s in self.wo['item_slots'] if s['slot']==slot or s['subtype']==slot]
            if len(hits)!=1:raise ValueError((slot,'specify the exact slot ID',len(hits)))
            slot=hits[0]
        oids=[self.oid(o) for o in locals.split()]
        cids=list(dict.fromkeys(c for o in locals.split() for c in self.claim_map[o]))
        perf='item_type' in slot
        assert (set(oids)==set(slot['objective_ids'])) if perf else oids==[slot['objective_id']]
        x={'item_id':slot['slot'],'objective_ids':oids,'claim_ids':cids,
          'item_type':slot['item_type'] if perf else 'flashcard','subtype':None if perf else slot['subtype'],
          'assessment_objectives':slot['assessment_objectives'],'difficulty':slot.get('difficulty',3),
          'prompt':prompt.strip(),'canonical_answer':answer.strip(),'marking_guidance':guidance,
          'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original Namibian teaching example','facts':facts or []},
          'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,
          'provenance':'original_codex_authorship','qa_status':'review_required',
          'blooms_level':slot['blooms_level'],'command_word':slot['command_word'],'mark_tariff':slot['mark_tariff']}
        if slot.get('misconception_entry'):x['misconception_entry']=slot['misconception_entry']
        self.items.append(stamp(x))
    def finish(self,deviations=None):
        note_path=self.td/'authoring_notes.json'
        if note_path.exists() and read(note_path).get('post_review_locked'):
            raise RuntimeError('This initial authoring snapshot would overwrite reviewed repairs. Maintain the canonical JSON, then run restamp.py, render_notes.py and run_checks.py as the playbook requires.')
        expected={s['slot'] for s in self.wo['item_slots']+self.wo['performance_tasks']}
        assert {i['item_id'] for i in self.items}==expected
        assert len(self.items)==len(expected)
        required={self.oid(o) for o in self.claim_map}
        assert required==set(self.contract['scope']['included_objective_ids'])
        assert all(2<=len(v)<=4 for v in self.claim_map.values())
        u=self.wo['content_units'][0];lo,hi=u['word_budget'];n=sum(len(b['text'].split()) for b in self.blocks)
        assert lo<=n<=hi,(self.tid,n,lo,hi)
        save(self.td/'claims/canonical_claim_ledger.json',{'ledger_id':'LEDGER-6145-'+self.tid,'claims':self.claims})
        save(self.td/u['file'],{'unit_id':u['unit_id'],'title':self.wo['topic_title'],
          'objective_ids':u['objective_ids'],'level':'NSSCO','core_status':'core','objective_type':'economics_concept',
          'depth_tier':max(o['depth_tier'] for o in u['objectives']),
          'word_budget':{'min':lo,'target':round((lo+hi)/2),'max':hi},'word_count':n,'blocks':self.blocks,'qa_status':'review_required'})
        save(self.td/self.wo['output_files']['learning_items'],{'dataset_id':'ITEMS-6145-'+self.tid,'topic_id':self.tid,'items':self.items})
        save(self.td/'authoring_notes.json',{'topic_id':self.tid,'author':'Codex','deviations':deviations or [],
          'judgements':['Examples and rubrics are original teaching applications, not reproduced examination material.','Marks are allocated to the actual requested economic elements; semantic review remains pending.'],
          'counts':{'claims':len(self.claims),'units':1,'items':len(self.items),'notes_words':n}})
        print(self.tid,len(self.claims),'claims',len(self.items),'items',n,'note words')
