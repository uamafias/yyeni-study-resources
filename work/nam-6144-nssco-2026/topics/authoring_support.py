"""Subject-local serialization/render/check support. Teaching and questions are authored per topic.

This helper never fabricates domain prose or changes the approved input packet.
Each topic supplies its original teaching, worked applications and item answers.
"""
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
STD=REPO/'standard/v0.2.0-draft'
REG={o['objective_id']:o for o in json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']}
MIS={m['entry_id']:m for m in json.loads((WS/'curriculum/misconceptions.json').read_text())['entries']}
REVISIONS={}
PRIOR={}
REVIEW_NOTE=None

def read(p):return json.loads(p.read_text())
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def stamp(x):
    x['claims_seen']={c:REVISIONS.get(c,1) for c in x['claim_ids']}
    text=(x['prompt']+'|'+x['canonical_answer']+'|'+'|'.join(x['marking_guidance'])) if 'item_id' in x else x['heading']+'|'+x['text']
    x['authored_hash']=hashlib.sha256(text.encode()).hexdigest()
    old=PRIOR.get(x.get('item_id') or (x.get('block_id'),tuple(x.get('claim_ids',[]))))
    if old and any(v>1 for v in x['claims_seen'].values()):
        x['prior_hash']=old.get('authored_hash')
        if x['prior_hash']==x['authored_hash']:
            assert REVIEW_NOTE,'An unchanged derivative needs an explicit author re-read decision.'
            x['reviewed_unchanged']=REVIEW_NOTE
    return x

def build(topic,lessons,members,cards,miscon_cards,performance,deviations=None,review_note=None,extra_evidence=None):
    """All prose supplied by the topic author. Dict keys are stable approved IDs/suffixes.

    lessons: bullet-number -> (heading, teaching, worked_application)
    members: exact member objective ID -> (heading, teaching, worked_application)
    cards: objective ID -> subtype -> (prompt, answer)
    miscon_cards: entry ID -> (prompt, answer)
    performance: item type -> (prompt, answer), following its approved blueprint.
    """
    global REVISIONS,PRIOR,REVIEW_NOTE
    REVISIONS={};PRIOR={};REVIEW_NOTE=review_note
    td=WS/'topics'/topic;wo=read(td/'work_order.json');blue=read(td/'performance-blueprints.json')['packages']
    old_claims={c['claim_id']:c for c in read(td/'claims/canonical_claim_ledger.json')['claims']} if (td/'claims/canonical_claim_ledger.json').exists() else {}
    for p in (td/'content-units').glob('*.json'):
        for block in read(p)['blocks']:PRIOR[(block['block_id'],tuple(block.get('claim_ids',[])))]=block
    if (td/'learning-items'/f'topic_{topic}_items.json').exists():
        for item in read(td/'learning-items'/f'topic_{topic}_items.json')['items']:PRIOR[item['item_id']]=item
    claims=[];claim_by_obj={};unit_specs={u['unit_id']:u for u in wo['content_units']};units=[]
    payload={f'OBJ-6144-{topic}.{k}':v for k,v in lessons.items()};payload.update(members)
    targets={s['objective_id'] for s in wo['item_slots']}
    assert set(payload)==targets,(topic,'missing prose',targets-set(payload),'extra',set(payload)-targets)
    def addclaim(oid,text,kind,provenance,locator):
        cid=f'CLM-6144-{topic}-{len(claims)+1:03}'
        old=old_claims.get(cid);revision=(old.get('revision',1)+(old['text']!=text)) if old else 1
        REVISIONS[cid]=revision
        claims.append({'claim_id':cid,'objective_ids':[oid],'text':text,'claim_type':kind,'provenance':provenance,
                       'evidence':[{'source_id':'NIED-6144-SYLLABUS','locator':locator,'support_type':'derivation' if provenance in ['reasoned_extension','generated_quality'] else 'paraphrase'}],
                       'derived_from_claim_ids':[],'verification':{'status':'unverified','method':'Author draft; source-linked concepts and original examples await independent subject review.','reviewer_id':None,'reviewed_at':None,'confidence':0.85},
                       'publishable':False,'revision':revision})
        claim_by_obj.setdefault(oid,[]).append(cid);return cid
    for oid,(heading,teach,example) in payload.items():
        assert teach.strip() and example.strip(),oid
        obj=REG[oid];loc=f"PDF p.{obj['syllabus_page']}; objective {oid}. Author's explanation of the cited syllabus demand, not a verbatim source quotation."
        # A concept claim and a separately identified worked application. Long claims
        # are explicit author statements rather than a false independent verification.
        addclaim(oid,teach,'factual','source_synthesised',loc)
        claims[-1]['evidence'].extend((extra_evidence or {}).get(oid,[]))
        addclaim(oid,example,'synthetic_example','generated_quality',loc+' Original illustrative reasoning/context.')
    for spec in wo['content_units']:
        blocks=[]
        for oid in spec['objective_ids']:
            heading,teach,example=payload[oid];cs=claim_by_obj[oid]
            blocks.append(stamp({'block_id':f"B{len(blocks)+1:02}",'block_type':'plain_explanation','heading':heading,'text':teach,
                                 'claim_ids':[cs[0]],'context_tags':['Namibia','NSSCO'],'assessment_objectives':REG[oid]['assessment_objectives']}))
            blocks.append(stamp({'block_id':f"B{len(blocks)+1:02}",'block_type':'worked_application','heading':'Putting the idea to work','text':example,
                                 'claim_ids':[cs[1]],'context_tags':['original teaching example'],'assessment_objectives':list('ABC')}))
        unit={'unit_id':spec['unit_id'],'title':payload[spec['objective_ids'][0]][0],'objective_ids':spec['objective_ids'],'level':'NSSCO','core_status':'core',
              'objective_type':'integrated subject teaching','depth_tier':max(REG[x]['depth_tier'] for x in spec['objective_ids']),
              'word_budget':{'min':spec['word_budget'][0],'target':sum(spec['word_budget'])//2,'max':spec['word_budget'][1]},
              'blocks':blocks,'word_count':sum(len(b['text'].split()) for b in blocks),'qa_status':'review_required'}
        units.append(unit)
    # Curated misconceptions get actual authored cases; the planner's test is not
    # passed off as an answer. They are taught next to their selected concept.
    for slot in wo['item_slots']:
        if slot['subtype']!='MISCON':continue
        prompt,answer=miscon_cards[slot['misconception_entry']]
        unit=next(u for u in units if slot['objective_id'] in u['objective_ids'])
        unit['blocks'].append(stamp({'block_id':'MIS-'+slot['misconception_entry'],'block_type':'misconception','heading':'Keeping the ideas apart',
                                     'text':prompt+'\n\n'+answer,'claim_ids':claim_by_obj[slot['objective_id']],
                                     'context_tags':['concept discrimination'],'assessment_objectives':slot['assessment_objectives']}))
    for u in units:u['word_count']=sum(len(b['text'].split()) for b in u['blocks'])
    # Every answer fact is also taught, so learners can reconstruct practice offline.
    # Integrated practice follows the teaching in a relevant unit with room within
    # its advisory allocation; it never substitutes for the explanation.
    for bp in sorted(blue,key=lambda b:len((' '.join(performance[b['item_type']])).split()),reverse=True):
        prompt,answer=performance[bp['item_type']]
        for oid in bp['objective_ids']:assert oid in payload
        cs=[c for oid in bp['objective_ids'] for c in claim_by_obj[oid]]
        block=stamp({'block_id':f"PRACTICE-{bp['item_type']}",'block_type':'worked_application',
                     'heading':'Worked practice: '+bp['title'], 'text':prompt+'\n\n'+answer,
                     'claim_ids':cs,'context_tags':['original integrated practice'],'assessment_objectives':bp['assessment_objectives']})
        related=[u for u in units if set(u['objective_ids']) & set(bp['objective_ids'])]
        needed=len(block['text'].split())
        fitting=[u for u in related if u['word_budget']['max']-u['word_count']>=needed]
        if not fitting:fitting=[u for u in units if u['word_budget']['max']-u['word_count']>=needed]
        destination=max(fitting or related,key=lambda u:u['word_budget']['max']-u['word_count'])
        destination['blocks'].append(block)
        destination['word_count']+=len(block['text'].split())
    items=[]
    structures=read_yaml(WS/'subject-profile.yaml')['answer_structures']
    for slot in wo['item_slots']:
        oid=slot['objective_id'];st=slot['subtype']
        prompt,answer=miscon_cards[slot['misconception_entry']] if st=='MISCON' else cards[oid][st]
        assert prompt.lower().startswith(slot['command_word'].lower()),(slot['slot'],prompt)
        guidance=[part.split('|')[0].capitalize()+': '+detail for part,detail in zip(structures[st],guidance_parts(st,answer))]
        # Numerical and non-prose construction guidance is authored in the topic's
        # answer; these parts identify the rubric dimensions, not an invented split.
        x={'item_id':slot['slot'],'objective_ids':[oid],'claim_ids':claim_by_obj[oid],'item_type':'flashcard','subtype':st,
           'assessment_objectives':slot['assessment_objectives'],'blooms_level':slot['blooms_level'],'command_word':slot['command_word'],'mark_tariff':slot['mark_tariff'],
           'difficulty':slot['difficulty'],'prompt':prompt+f" [{slot['mark_tariff']}]",'canonical_answer':answer,'marking_guidance':guidance,
           'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original Namibian teaching task','facts':[]},
           'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original author prose derived from the named syllabus objectives; no official question text.','qa_status':'review_required'}
        if st=='MISCON':x['misconception_entry']=slot['misconception_entry']
        items.append(stamp(x))
    for bp in blue:
        prompt,answer=performance[bp['item_type']];cs=[c for oid in bp['objective_ids'] for c in claim_by_obj[oid]]
        guidance=[f"Part {p['part']}: {p['marks']} marks; "+', '.join(f'{a}{n}' for a,n in p['ao_split'].items())+'. '+p['demand'] for p in bp['subparts']]
        guidance+=['Knowledge: precise relevant concepts, as explained in the model answer.','Context: use the stated facts, not an unsupported assumption.','Analysis: trace the requested effect or comparison.','Alternative: weigh the actual option(s) where judgement is required.','Judgement: support the decision with a decisive reason and relevant conditions.']
        x={'item_id':bp['slot'],'objective_ids':bp['objective_ids'],'claim_ids':cs,'item_type':bp['item_type'],'subtype':None,
           'assessment_objectives':bp['assessment_objectives'],'blooms_level':bp['blooms_level'],'command_word':bp['subparts'][0]['command_word'],
           'mark_tariff':bp['total_marks'],'difficulty':4,'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,
           'context':{'sector':None,'business_size':None,'ownership':None,'situation':'Original integrated case','facts':[]},
           'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original practice package; subpart AO splits follow the approved blueprint.','qa_status':'review_required'}
        items.append(stamp(x))
    for u in units:
        u['word_count']=sum(len(b['text'].split()) for b in u['blocks'])
        write(td/'content-units'/f"{u['unit_id']}.json",u)
    write(td/'claims/canonical_claim_ledger.json',{'ledger_id':f'LEDGER-6144-{topic}','claims':claims})
    write(td/'learning-items'/f'topic_{topic}_items.json',{'dataset_id':f'ITEMS-6144-{topic}','topic_id':topic,'items':items})
    assert {i['item_id'] for i in items}=={s['slot'] for s in wo['item_slots']+wo['performance_tasks']}
    write(td/'authoring_notes.json',{'topic_id':topic,'deviations':deviations or [],
                                   'notes':['Original explanations, examples and tasks; no source text copied from official assessment material.','Word minima are advisory under the approved handover. Shorter integrated teaching is not padded to reach a count.','Claims remain unverified/non-publishable pending independent review.']})
    subprocess.run([sys.executable,str(STD/'build/render_notes.py'),str(WS),topic],check=True,capture_output=True)
    result=subprocess.run([sys.executable,str(STD/'checks/run_checks.py'),str(WS),topic],capture_output=True,text=True)
    report=read(td/'qa_report.json');fail=[x for x in report['deterministic_checks'] if x['status']=='fail']
    summary={'topic':topic,'claims':len(claims),'units':len(units),'items':len(items),'notes_words':sum(u['word_count'] for u in units),
             'decision':report['release_decision'],'failed_checks':fail,'warnings':[x['check_id'] for x in report['deterministic_checks'] if x['status']=='warn'],
             'not_run':[x['check_id'] for x in report['deterministic_checks'] if x['status']=='not_run'],'runner_exit':result.returncode}
    write(td/'authoring_summary.json',summary)
    print(json.dumps(summary,indent=2))
    if fail:print(result.stdout)
    return summary

def read_yaml(path):
    import yaml
    return yaml.safe_load(path.read_text())

def guidance_parts(st,answer):
    first=re.split(r'(?<=[.!?])\s+',answer)[0]
    return [first,
            'credit the specific case link or contrast stated in the answer; a copied name alone is insufficient.',
            'credit the developed explanation or correctly executed working, rather than a repeated assertion.',
            'credit the stated result/effect with its beneficiary or units, as applicable.',
            'credit the supported judgement or interpretation and its relevant condition where this task requires it.',
            'retain the distinction and relevant limitations stated in the answer.',
            'do not credit a contradictory alternative or an invented fact.',
            'credit independently correct required elements rather than repeated wording.']
