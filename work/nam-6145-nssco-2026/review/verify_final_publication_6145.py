#!/usr/bin/env python3
"""Verify the published 625-item subject and Claude's bounded nonvisual repairs."""
import ast
import collections
import hashlib
import json
from pathlib import Path
import re

W=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]
PUB=ROOT/'publish'/W.name
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ah(x):
    text=(x['prompt']+'|'+x['canonical_answer']+'|'+'|'.join(x['marking_guidance'])) if 'item_id' in x else x['heading']+'|'+x['text']
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    items={};blocks={};units={};claims={};warnings=collections.Counter();notrun=collections.Counter()
    sourcefiles={};topics=[]
    for td in sorted(p for p in (W/'topics').iterdir() if p.is_dir() and (p/'work_order.json').exists()):
        t=td.name;topics.append(t);wo=read(td/'work_order.json');qa=read(td/'qa_report.json')
        assert qa['release_decision']=='publish' and not any(c['status']=='fail' for c in qa['deterministic_checks']),t
        for c in qa['deterministic_checks']:
            if c['status']=='warn':warnings[c['check_id']]+=1
            if c['status']=='not_run':notrun[c['check_id']]+=1
        p=td/f'learning-items/topic_{t}_items.json';sourcefiles[str(p.relative_to(W))]=sha(p)
        rows=read(p)['items'];byid={i['item_id']:i for i in rows};wanted={s['slot'] for s in wo['item_slots']+wo['performance_tasks']}
        assert len(rows)==len(byid)==len(wanted) and set(byid)==wanted
        for s in wo['item_slots']:
            i=byid[s['slot']];assert i['objective_ids']==[s['objective_id']]
            for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff','difficulty']:assert i[k]==s[k],(i['item_id'],k)
        items.update(byid)
        for p in (td/'content-units').glob('*.json'):
            u=read(p);count=sum(len(b['text'].split()) for b in u['blocks']);assert count==u['word_count'] and u['word_budget']['min']<=count<=u['word_budget']['max']
            units[u['unit_id']]=u;blocks.update({b['block_id']:b for b in u['blocks']});sourcefiles[str(p.relative_to(W))]=sha(p)
        p=td/'claims/canonical_claim_ledger.json';claims.update({c['claim_id']:c for c in read(p)['claims']});sourcefiles[str(p.relative_to(W))]=sha(p)
    assert len(items)==625 and len(topics)==28 and len(units)==63
    # Compare every author-changed block against the full author-checkpoint diff.
    authored_blocks={b['block_id']:b['after'] for b in read(W/'review/nonvisual-notes-diff-6145.json')}
    snapshot=read(W/'review/nonvisual-start-snapshot-6145.json')
    expected_old_claims={c['claim_id']:c for d in snapshot.values() for c in d.get('claims',[])}
    assert all(claims[cid]==c for cid,c in expected_old_claims.items())
    beforeblocks={b['block_id']:b['text'] for d in snapshot.values() for b in d.get('blocks',[])};beforeblocks.update(authored_blocks)
    changedblocks={bid for bid,b in blocks.items() if b['text']!=beforeblocks[bid]}
    # Recover new card text directly from the one-shot author's literal data table.
    module=ast.parse((W/'review/author_nonvisual_revision_6145.py').read_text())
    rows=ast.literal_eval(next(n.value for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ROWS' for t in n.targets)))
    scope={r['key']:r['slot_id'] for r in read(W/'planning/revision-01/scope.json') if r['owner']=='Codex'}
    changeditems=set()
    for key,_,prompt,answer,guidance,_ in rows:
        i=items[scope[key]]
        if (i['prompt'],i['canonical_answer'],i['marking_guidance'])!=(prompt,answer,[guidance]):changeditems.add(i['item_id'])
    assert changeditems=={'ITEM-6145-5.3-024-DEF','ITEM-6145-6.2-037-FEATURE'}
    recorded=read(W/'review/claude-nonvisual-crossreview-changes-6145.json')['artefacts']
    assert changedblocks|changeditems=={r['id'] for r in recorded} and len(recorded)==11
    for r in recorded:
        x=items.get(r['id'],blocks.get(r['id']));assert ah(x)==r['authored_hash']==x['authored_hash']
        assert x['prior_hash']==r['prior_hash']
    # Six whitespace-only blocks plus the two wording fixes and public-good fix.
    semantic_blocks={'CU-6145-3.5-B02','CU-6145-6.1.1-B01'}
    for bid in changedblocks-semantic_blocks:assert blocks[bid]['text'].split()==beforeblocks[bid].split(),bid
    packet=(W/'review/nonvisual-review-packet-6145.md').read_text().split('## New claims\n',1)[1].split('## Changed notes blocks',1)[0]
    packetclaims=re.findall(r'### (CL-[^\s]+) \(revision (\d+)\)\n\n(.*?)\n\nObjectives:',packet,re.S)
    assert len(packetclaims)==69
    for cid,revision,text in packetclaims:assert claims[cid]['text']==text and claims[cid]['revision']==int(revision),cid
    visuals=read(W/'diagrams/CODEX-REVIEW-6145.json')['items'];files={}
    for iid,r in visuals.items():
        i=items[iid];h=hashlib.sha256(json.dumps({k:i.get(k) for k in ('prompt','canonical_answer','marking_guidance','assessment_objectives','blooms_level','command_word','mark_tariff')},sort_keys=True,ensure_ascii=False).encode()).hexdigest();assert h==r['learner_text_sha256']
        for p,h in r['files_sha256'].items():assert sha(W/p)==h;files[p]=h
    exports={}
    for p in (PUB/'flashcards').glob('*.json'):
        for i in read(p)['items']:assert i['item_id'] not in exports;exports[i['item_id']]=i
    assert set(exports)==set(items)
    for iid,i in items.items():assert {k:v for k,v in exports[iid].items() if k!='objective_titles'}==i,iid
    refs=[]
    for p in (PUB/'notes').glob('*.md'):
        for rel in re.findall(r'\]\((diagrams/[^)]+)\)',p.read_text()):
            assert (p.parent/rel).is_file();refs.append(rel)
    assert len(refs)==12
    manifest=read(W/'diagrams/asset-manifest.json');sidecar=read(PUB/'diagram-assets.json')
    assert set(manifest['items'])==set(sidecar['items'])==set(visuals)
    for iid,r in sidecar['items'].items():
        assert r['status']==manifest['items'][iid]['status']=='reviewed by Codex; visual subset accepted'
        for side in ['question','answer']:
            e=r[side];m=manifest['items'][iid][side]
            assert sha(PUB/e['png'])==e['png_sha256']==m['png_sha256'] and e['yyeni_asset_id'] is None
    for rel in refs:
        name=Path(rel).name;expected=next(h for p,h in files.items() if Path(p).name==name);assert sha(PUB/'notes'/rel)==expected
    result={'scope':'Final checks and focused independent acceptance of Claude’s five repair categories; not another full-bank semantic review','items':len(items),'flashcards':sum(i['item_type']=='flashcard' for i in items.values()),'packages':sum(i['item_type']!='flashcard' for i in items.values()),'topics_publish':len(topics),'content_units_within_budget':len(units),'warnings':dict(warnings),'not_run':dict(notrun),'claude_changed_artefacts_verified':len(recorded),'all_claims_unchanged':True,'new_claims_checked_against_author_packet':len(packetclaims),'visual_cards_unchanged':len(visuals),'visual_file_hashes_unchanged':len(files),'exports_equal_canonical':len(exports),'note_image_references_resolve':len(refs),'card_image_files':len(list((PUB/'card-images').glob('*.png'))),'managed_asset_ids':'null; no upload or classroom import','source_hashes':sourcefiles,'review_report_sha256':sha(W/'review/step6-nonvisual-crossreview-6145.md'),'canonical_block_words':sum(u['word_count'] for u in units.values())}
    (W/'review/final-publication-verification-6145.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2,ensure_ascii=False))

if __name__=='__main__':main()
