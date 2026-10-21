"""Metadata assembly for original, explicitly written topic manuscripts.

No learning content, questions, answers, claims or rubrics are invented here.
Approved contracts and work orders are read, never changed.
"""
import hashlib
import json
import sys
from pathlib import Path

def read(p): return json.loads(p.read_text())
def dump(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + '\n')

def assemble(td, claims_by_suffix, blocks_by_unit, answers, performances, deviations=None, revision_reviews=None):
    td = Path(td); tid = td.name; ws = td.parents[1]; repo = ws.parents[1]
    sys.path.insert(0, str(repo / 'standard/v0.2.0-draft/checks'))
    from yyeni_checks import _artefact_text
    wo = read(td / 'work_order.json')
    contract = read(td / 'contract.json')
    ledger_path=td/'claims/canonical_claim_ledger.json'
    old_claims={c['claim_id']:c for c in read(ledger_path)['claims']} if ledger_path.exists() else {}
    old_artifacts={}
    for p in (td/'content-units').glob('*.json'):
        for b in read(p)['blocks']:old_artifacts[b['block_id']]=b
    items_path=td/wo['output_files']['learning_items']
    if items_path.exists():
        old_artifacts.update({i['item_id']:i for i in read(items_path)['items']})
    revisions={}; changed_claims=[]
    assert set(contract['scope']['included_objective_ids']) == {'OBJ-6136-' + tid + '.' + s for s in claims_by_suffix}
    def oid(s): return f'OBJ-6136-{tid}.{s}'
    def stamp(x):
        aid=x.get('item_id',x.get('block_id'));old=old_artifacts.get(aid)
        x['claims_seen'] = {cid: revisions[cid] for cid in x.get('claim_ids', [])}
        x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
        if old:
            advanced=any(v>old.get('claims_seen',{}).get(cid,0) for cid,v in x['claims_seen'].items())
            changed=x['authored_hash']!=old.get('authored_hash')
            if advanced or changed:
                x['prior_hash']=old['authored_hash']
                if changed:
                    x['repair_note']='Original Codex draft repair; prior text hash retained. See manuscript diff and authoring history.'
                elif advanced:
                    reason=(revision_reviews or {}).get(aid)
                    if not reason:raise ValueError('Revised claim requires explicit unchanged-text review: '+aid)
                    x['reviewed_unchanged']=reason
            else:
                for field in ['prior_hash','repair_note','reviewed_unchanged']:
                    if field in old:x[field]=old[field]
        return x
    claims=[]; refs={}
    for s, entries in claims_by_suffix.items():
        refs[s]=[]
        for n, (kind, text) in enumerate(entries, 1):
            cid=f'CLM-6136-{tid}-{s}-{n:02d}'; refs[s].append(cid)
            old=old_claims.get(cid)
            changed=bool(old and (old['text']!=text or old['claim_type']!=kind))
            revisions[cid]=(old.get('revision',1) if old else 1)+int(changed)
            if changed:changed_claims.append({'claim_id':cid,'before':old,'after_text':text,'after_revision':revisions[cid]})
            claims.append({'claim_id':cid,'objective_ids':[oid(s)],'text':text,'claim_type':kind,
                'provenance':'generated_gap','evidence':[],'derived_from_claim_ids':[],'revision':revisions[cid],
                'verification':{'status':'unverified','method':'Original Codex teaching synthesis within approved source scope; pending independent Claude Code review.',
                                'reviewer_id':None,'reviewed_at':None,'confidence':0.9},'publishable':False,'notes':[]})
    if changed_claims:
        history=td/'authoring-history/claim-repairs.json'
        prior=read(history) if history.exists() else []
        dump(history,prior+changed_claims)
    dump(ledger_path,{'ledger_id':f'LEDGER-6136-{tid}','claims':claims})
    total_words=0
    for spec in wo['content_units']:
        num=spec['sub_topic'].split('.')[-1]; blocks=[]
        for n,(kind,heading,text,suffixes) in enumerate(blocks_by_unit[num],1):
            blocks.append(stamp({'block_id':f'BLK-6136-{tid}.{num}-{n:02d}', 'block_type':kind,'heading':heading,'text':text,
                'claim_ids':list(dict.fromkeys(c for s in suffixes for c in refs[s])),
                'context_tags':['original teaching; fictional examples where stated'],
                'assessment_objectives':sorted(set(a for slot in wo['item_slots'] if slot['objective_id'] in spec['objective_ids'] for a in slot['assessment_objectives']))}))
        wc=sum(len((b['heading']+' '+b['text']).split()) for b in blocks);total_words+=wc
        lo,hi=spec['word_budget']
        dump(td/spec['file'],{'unit_id':spec['unit_id'],'title':blocks_by_unit[num][0][1], 'objective_ids':spec['objective_ids'],
            'level':'NSSCO','core_status':'core','objective_type':'integrated_subject_lesson','depth_tier':max(x['depth_tier'] for x in spec['objectives']),
            'word_budget':{'min':lo,'target':(lo+hi)//2,'max':hi},'blocks':blocks,'word_count':wc,'qa_status':'review_required',
            'notes':['Approved lower word allocations advisory; no padding of integrated parent/member explanations.']})
    ps={x['slot']:x for x in read(ws/'curriculum/performance-slot-specs.json')['slots']}
    items=[]
    for slot in wo['item_slots']+wo['performance_tasks']:
        sid=slot['slot'];perf='item_type' in slot
        if perf:
            suffixes,prompt,answer,guidance=performances[sid.rsplit('-',1)[-1]];meta=ps[sid]
        else:
            n=int(sid.split('-')[-2]);prompt,answer,guidance=answers[n];meta=slot
            suffixes=[slot['objective_id'].removeprefix(f'OBJ-6136-{tid}.')]
        item={'item_id':sid,'objective_ids':[oid(s) for s in suffixes],
            'claim_ids':list(dict.fromkeys(c for s in suffixes for c in refs[s])),
            'item_type':slot['item_type'] if perf else 'flashcard','subtype':slot.get('subtype'),
            'assessment_objectives':meta['assessment_objectives'],'blooms_level':meta['blooms_level'],'command_word':meta['command_word'],
            'mark_tariff':meta['mark_tariff'],'difficulty':slot.get('difficulty',3),'prompt':prompt,'canonical_answer':answer,
            'marking_guidance':guidance+['Original indicative practice guidance; not an official mark scheme.'],
            'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original conceptual question or explicitly fictional case.','facts':[]},
            'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,
            'provenance':'Original Codex authoring, 2026-10-20; independent Claude Code review pending.','qa_status':'review_required'}
        if slot.get('misconception_entry'):item['misconception_entry']=slot['misconception_entry']
        items.append(stamp(item))
    assert len(items)==wo['planned_item_count']
    dump(td/wo['output_files']['learning_items'],{'dataset_id':f'ITEMS-6136-{tid}','topic_id':tid,'items':items})
    dump(td/'authoring_notes.json',{'topic_id':tid,'deviations':deviations or [],
        'limits':['Claims unverified and not publishable; independent review remains required.', 'No copied assessment text; numeric cases explicitly fictional.']})
    print(json.dumps({'topic':tid,'claims':len(claims),'units':len(wo['content_units']),'items':len(items),'notes_block_words':total_words}))
