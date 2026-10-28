#!/usr/bin/env python3
"""Reconcile the completed revision against its pre-authoring snapshot and scratch export."""
import collections
import hashlib
import json
from pathlib import Path

W = Path(__file__).resolve().parents[1]
ROOT = W.parents[1]
OUT = Path('/private/tmp/6145-nonvisual-complete-review')
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')

def main():
    snap=read(W/'review/nonvisual-start-snapshot-6145.json')
    items={}; olditems={}; units={}; changed_blocks=[]; oldclaims={}; claims={}; warnings=collections.Counter(); notrun=collections.Counter()
    for rel,d in snap.items():
        for i in d.get('items',[]):olditems[i['item_id']]=i
        for c in d.get('claims',[]):oldclaims[c['claim_id']]=c
    for td in sorted(p for p in (W/'topics').iterdir() if p.is_dir() and (p/'work_order.json').exists()):
        t=td.name;wo=read(td/'work_order.json');qa=read(td/'qa_report.json')
        assert qa['release_decision']=='publish',t
        assert not any(c['status']=='fail' for c in qa['deterministic_checks']),t
        for c in qa['deterministic_checks']:
            if c['status']=='warn':warnings[c['check_id']]+=1
            if c['status']=='not_run':notrun[c['check_id']]+=1
        rows=read(td/f'learning-items/topic_{t}_items.json')['items']
        wanted={s['slot'] for s in wo['item_slots']+wo['performance_tasks']}
        assert len(rows)==len({i['item_id'] for i in rows})==len(wanted)
        assert {i['item_id'] for i in rows}==wanted
        byid={i['item_id']:i for i in rows};items.update(byid)
        for s in wo['item_slots']:
            i=byid[s['slot']]
            assert i['objective_ids']==[s['objective_id']],i['item_id']
            for k in ['subtype','assessment_objectives','difficulty','blooms_level','command_word','mark_tariff']:
                assert i[k]==s[k],(i['item_id'],k)
        for p in (td/'content-units').glob('*.json'):
            u=read(p);actual=sum(len(b['text'].split()) for b in u['blocks'])
            assert actual==u['word_count'] and u['word_budget']['min']<=actual<=u['word_budget']['max'],u['unit_id']
            units[u['unit_id']]=u
            old=snap[str(p.relative_to(W))];before={b['block_id']:b for b in old['blocks']}
            for b in u['blocks']:
                if b['text']!=before[b['block_id']]['text']:
                    changed_blocks.append({'topic_id':t,'unit_id':u['unit_id'],'block_id':b['block_id'],'before':before[b['block_id']]['text'],'after':b['text']})
        for c in read(td/'claims/canonical_claim_ledger.json')['claims']:claims[c['claim_id']]=c
    assert len(olditems)==588 and len(items)==625
    assert {i for i in olditems if olditems[i]!=items[i]}=={'ITEM-6145-5.4-013-DEF'}
    assert all(claims[cid]==c for cid,c in oldclaims.items()),'Existing claim changed'
    intended={r['slot_id'] for r in read(W/'planning/revision-01/scope.json') if r['owner']=='Codex'}
    assert set(items)-set(olditems)==intended and len(intended)==37
    visuals=read(W/'diagrams/CODEX-REVIEW-6145.json')['items'];image_count=0
    for iid,r in visuals.items():
        i=items[iid];fingerprint=hashlib.sha256(json.dumps({k:i.get(k) for k in ('prompt','canonical_answer','marking_guidance','assessment_objectives','blooms_level','command_word','mark_tariff')},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        assert fingerprint==r['learner_text_sha256'] and i==olditems[iid]
        for p,h in r['files_sha256'].items():assert sha(W/p)==h;image_count+=1
    exported={}
    for p in (OUT/'flashcards').glob('*.json'):
        for i in read(p)['items']:
            assert i['item_id'] not in exported
            exported[i['item_id']]=i
    assert set(exported)==set(items)
    for iid,i in items.items():
        e=exported[iid]
        assert {k:v for k,v in e.items() if k!='objective_titles'}==i,('export differs',iid)
    sidecar=read(OUT/'diagram-assets.json');assert set(sidecar['items'])==set(visuals)
    for iid,r in sidecar['items'].items():
        for side in ['question','answer']:
            e=r[side];assert sha(OUT/e['png'])==e['png_sha256'];assert e['yyeni_asset_id'] is None
    assert len(list((OUT/'notes/diagrams').glob('*.png')))==12
    assert len(list((OUT/'card-images').glob('*.png')))==24
    # Original live publication is still the pre-visual reviewed package.
    baseline=read(W/'planning/revision-01/baseline/preservation-hashes.json')
    published={p:h for p,h in baseline.items() if p.startswith('publish/')}
    assert published and all(sha(ROOT/p)==h for p,h in published.items()),'Live publication changed'
    budgets=[]
    for r in read(W/'planning/revision-01/notes-budget-work-order.json'):
        uid=r['unit_id'];u=units[uid];budgets.append({'unit_id':uid,'before':r['actual_words'],'after':u['word_count'],'min':u['word_budget']['min'],'max':u['word_budget']['max']})
    result={'total_items':len(items),'flashcards':sum(i['item_type']=='flashcard' for i in items.values()),'packages':sum(i['item_type']!='flashcard' for i in items.values()),'new_items':37,'preserved_existing_items':587,'approved_existing_retarget':'ITEM-6145-5.4-013-DEF','new_claims':len(set(claims)-set(oldclaims)),'all_existing_claims_unchanged':True,'content_units':len(units),'canonical_block_words':sum(u['word_count'] for u in units.values()),'all_unit_budgets_pass':True,'topics_publish':28,'warnings':dict(warnings),'not_run':dict(notrun),'accepted_visual_cards_unchanged':len(visuals),'image_and_master_hashes_unchanged':image_count,'scratch_export_equal_items':len(exported),'scratch_note_images':12,'scratch_card_images':24,'scratch_output':str(OUT),'live_publication_files_unchanged':len(published),'ten_budget_repairs':budgets,'text_changed_blocks':len(changed_blocks),'independent_nonvisual_review':'pending Claude; deterministic success is not semantic approval'}
    write(W/'review/nonvisual-completion-audit-6145.json',result)
    write(W/'review/nonvisual-notes-diff-6145.json',changed_blocks)
    packet=['# 6145 revision-01 nonvisual review packet','',
            'Generated from canonical artefacts and the pre-authoring snapshot. Independent Claude review pending.',
            '', '## New cards']
    for iid in sorted(intended):
        i=items[iid]
        packet += ['', '### '+iid, '',
                   f"Labels: {i['subtype']}; AO {i['assessment_objectives']}; Bloom {i['blooms_level']}; {i['command_word']}; {i['mark_tariff']} marks; difficulty {i['difficulty']}.",
                   '',i['prompt'],'',i['canonical_answer'],'',*i['marking_guidance'],
                   '', 'Claims: '+', '.join(i['claim_ids'])]
    iid='ITEM-6145-5.4-013-DEF'
    packet += ['', '## Approved existing-card retarget', '', iid, '',
               'Before: '+olditems[iid]['prompt']+' — '+olditems[iid]['canonical_answer'],
               '', 'After: '+items[iid]['prompt']+' — '+items[iid]['canonical_answer'],
               '',*items[iid]['marking_guidance'], '', '## New claims']
    for cid in sorted(set(claims)-set(oldclaims)):
        c=claims[cid];packet += ['',f"### {cid} (revision {c['revision']})",'',c['text'],
                                '', 'Objectives: '+', '.join(c['objective_ids'])]
    packet += ['', '## Changed notes blocks — full before and after']
    for b in changed_blocks:
        packet += ['', '### '+b['block_id'], '', '**Before**', '',b['before'],
                   '', '**After**','',b['after']]
    (W/'review/nonvisual-review-packet-6145.md').write_text('\n'.join(packet)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
