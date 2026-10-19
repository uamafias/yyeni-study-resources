"""Metadata/serialization helpers only; teaching content and tasks are authored explicitly."""
import hashlib
import json
from pathlib import Path
import re
import sys

WS = Path(__file__).resolve().parents[1]
ROOT = WS.parents[1]
sys.path.insert(0, str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def split_credits(guidance):
    """One list entry per stated credit: "1 mark: a. 1 mark: b." becomes two entries. Entries that state several marks at
    once ("2 marks: ..."), option rules ("1 mark each for any two of ...") and single-credit entries are left whole."""
    out = []
    for g in guidance:
        parts = re.split(r'(?<=[.;])\s+(?=1 mark\b[:\s])', g.strip())
        out.extend(p.strip() for p in parts if p.strip())
    return out

def stamp(x):
    x['qa_status'] = 'review_required'
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x

class Author:
    def __init__(self, topic, group=None):
        self.topic = str(topic)
        self.group = group
        self.base = WS/'topics'/self.topic
        self.wo = json.loads((self.base/'work_order.json').read_text())
        if group:
            selected=json.loads((WS/'planning/topic3_groups.json').read_text())['groups'][group]['units']
            self.wo['content_units']=[u for u in self.wo['content_units'] if u['sub_topic'] in selected]
            owns={o for u in self.wo['content_units'] for o in u['objective_ids']}
            self.wo['item_slots']=[s for s in self.wo['item_slots'] if s['objective_id'] in owns]
            if group!='3A':self.wo['performance_tasks']=[]
        self.reg = {o['objective_id']: o for o in json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']}
        self.claims, self.entries, self.items = [], {}, []
        self.prebuilt_units={}
        self.notes = {'topic_id': self.topic, 'authoring_tool': 'Codex', 'deviations': [],
                      'visuals_pending': [], 'ao_demand_evidence': [], 'below_budget_units': [],
                      'release_status': 'unreleased; cross-vendor review, teacher verification and unresolved visuals pending'}

    def entry(self, obj, heading, claims, explanation='', source=None, claim_type='factual'):
        oid = obj if obj.startswith('OBJ-') else 'OBJ-6116-'+obj
        assert oid in self.reg and oid not in self.entries, oid
        ids = []
        for text in claims:
            cid = f'CLM-6116-{self.group or self.topic}-{len(self.claims)+1:03d}'
            ev = [] if source is None else [{'source_id': source[0], 'locator': source[1], 'support_type': source[2]}]
            self.claims.append({'claim_id': cid, 'objective_ids': [oid], 'text': text,
                'claim_type': claim_type, 'provenance': 'generated_gap', 'evidence': ev,
                'derived_from_claim_ids': [], 'revision': 1,
                'verification': {'status': 'unverified', 'method': 'Original subject authoring; requires semantic and source verification.',
                                 'reviewer_id': None, 'reviewed_at': None, 'confidence': 0.8},
                'publishable': False, 'notes': [] if ev else ['No approved reference with a sufficiently specific locator cited. Teacher verification required; SRC-SCHOOL has not been named.']})
            ids.append(cid)
        self.entries[oid] = {'heading': heading, 'text': '\n\n'.join(claims)+ ('\n\n'+explanation if explanation else ''), 'claims': ids}
        return ids

    def card(self, obj, subtype, prompt, answer, guidance, pending=False, demand=None):
        oid = obj if obj.startswith('OBJ-') else 'OBJ-6116-'+obj
        ss = [s for s in self.wo['item_slots'] if s['objective_id']==oid and s['subtype']==subtype]
        assert len(ss)==1, (oid, subtype)
        s=ss[0]
        assert not any(i['item_id']==s['slot'] for i in self.items),s['slot']
        ids=self.entries[oid]['claims']
        i={'item_id': s['slot'], 'objective_ids': [oid], 'claim_ids': ids,
           'item_type': 'flashcard', 'subtype': subtype, 'assessment_objectives': s['assessment_objectives'],
           'blooms_level': s['blooms_level'], 'command_word': s['command_word'],
           'mark_tariff': s['mark_tariff'], 'difficulty': s['difficulty'], 'prompt': prompt,
           'canonical_answer': answer, 'marking_guidance': split_credits(guidance),
           'context': {'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
           'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None,
           'provenance': 'Original Codex authoring for Biology 6116; marking guidance proposed, not official.',
           'claims_seen': {c:1 for c in ids}}
        if s.get('misconception_entry'):i['misconception_entry']=s['misconception_entry']
        self.items.append(stamp(i))
        if pending:self.notes['visuals_pending'].append({'item_id':s['slot'],'figure':'VIS-6116-'+obj,'reason':'Required image/variant or reviewed scale/labels/delivery unresolved; activity cannot be released as complete.'})
        if demand:self.notes['ao_demand_evidence'].append({'item_id':s['slot'],**demand})

    def task(self, kind, objs, prompt, answer, guidance, marks, aos, command=None):
        p=next(p for p in self.wo['performance_tasks'] if p['item_type']==kind)
        oids=['OBJ-6116-'+o for o in objs]
        ids=list(dict.fromkeys(c for o in oids for c in self.entries[o]['claims']))
        self.items.append(stamp({'item_id':p['slot'],'objective_ids':oids,'claim_ids':ids,
            'item_type':kind,'subtype':None,'assessment_objectives':aos,'blooms_level':p['blooms_level'],
            'command_word':command,'mark_tariff':marks,'difficulty':3,'prompt':prompt,'canonical_answer':answer,
            'marking_guidance':split_credits(guidance),'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},
            'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,
            'provenance':'Original Codex activity; invented readings; proposed marking guidance.', 'claims_seen':{c:1 for c in ids}}))

    def write(self, summaries, links=None):
        links=links or {}
        for folder in ['claims','content-units','learning-items']:(self.base/folder).mkdir(exist_ok=True)
        actual={i['item_id'] for i in self.items}
        expected={s['slot'] for s in self.wo['item_slots']+self.wo['performance_tasks']}
        assert actual==expected,(sorted(expected-actual),sorted(actual-expected))
        assert len(actual)==len(self.items)
        for u in self.wo['content_units']:
            if u['unit_id'] in self.prebuilt_units:
                (self.base/'content-units'/f"{u['unit_id']}.json").write_text(json.dumps(self.prebuilt_units[u['unit_id']],indent=1,ensure_ascii=False)+'\n')
                continue
            entries=[self.entries[oid] for oid in u['objective_ids']]
            ids=[c for e in entries for c in e['claims']]
            def block(n,typ,heading,text,cids):
                value=stamp({'block_id':u['sub_topic']+f'-b{n}','block_type':typ,'heading':heading,'text':text,
                              'claim_ids':cids,'context_tags':[],'assessment_objectives':['AO1'],
                              'claims_seen':{c:1 for c in cids}})
                value.pop('qa_status')  # content-unit block schema forbids this field; unit/items carry it
                return value
            blocks=[block(0,'summary','Key points',summaries[u['sub_topic']],ids)]
            blocks += [block(n+1,'plain_explanation',e['heading'],e['text'],e['claims']) for n,e in enumerate(entries)]
            if u['sub_topic'] in links:blocks.append(block(len(blocks),'cross_link','Where this connects',links[u['sub_topic']],[]))
            count=sum(len(b['text'].split()) for b in blocks)
            lo,hi=u['word_budget']
            if count<lo:self.notes['below_budget_units'].append({'unit_id':u['unit_id'],'words':count,'minimum':lo,'why':'Objectives and original worked/task-method examples are taught together; no padding added to reach a minimum. Subject review must still confirm teaching depth.'})
            cu={'unit_id':u['unit_id'],'title':u['sub_topic']+' '+entries[0]['heading'],'objective_ids':u['objective_ids'],
                'level':'NSSCO Ordinary Level','core_status':'core','objective_type':self.reg[u['objective_ids'][0]]['objective_type'],
                'depth_tier':max(self.reg[o]['depth_tier'] for o in u['objective_ids']),
                'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},'blocks':blocks,'word_count':count,
                'qa_status':'review_required','notes':['Operative budget from the approved work order.']}
            (self.base/'content-units'/f"{u['unit_id']}.json").write_text(json.dumps(cu,indent=1,ensure_ascii=False)+'\n')
        if self.group:
            (self.base/'claims/staging').mkdir(exist_ok=True)
            cp=self.base/f'claims/staging/claims_{self.group}.json'
            ip=self.base/f'learning-items/topic_{self.topic}_items_{self.group}.json'
            np=self.base/f'authoring_notes_{self.group}.json'
        else:
            cp=self.base/'claims/canonical_claim_ledger.json'
            ip=self.base/f'learning-items/topic_{self.topic}_items.json'
            np=self.base/'authoring_notes.json'
        cp.write_text(json.dumps({'ledger_id':f'CLM-LEDGER-6116-{self.group or self.topic}','claims':self.claims},indent=1,ensure_ascii=False)+'\n')
        ip.write_text(json.dumps({'dataset_id':f'ITEMS-6116-{self.group or self.topic}','topic_id':self.topic,'items':self.items},indent=1,ensure_ascii=False)+'\n')
        np.write_text(json.dumps(self.notes,indent=2,ensure_ascii=False)+'\n')
        print(f'Topic {self.topic}: {len(self.claims)} claims; {len(self.wo["content_units"])} units; {len(self.items)} items')
