"""Attach explicit author render-reading notes to local screen leads; never infer reads."""
import json
from analysis_sources import A,WB,ROOT,digest,evidence_path,write
from provenance_inputs import SPEC

def build():
    p=A/'provenance-full-screen-r5.json';screen=json.loads(p.read_text())
    images=json.loads((A/'provenance-screen-images-r5.json').read_text())['images']
    notes=json.loads((WB/'tools/provenance_screen_readings_r5.json').read_text())['batches']
    lookup={}
    for image in images:
        reading=notes.get(str(image['batch']))
        if not reading:continue
        assert len(reading)==len(image['pages'])
        assert digest(evidence_path(image['path']))==image['sha256']
        for page,note in zip(image['pages'],reading):
            assert note
            for link in page['candidate_links']:
                lookup[link['candidate_id']]={'image_path':image['path'],'image_sha256':image['sha256'],
                  'note':note,'reader':'Codex author','date':'2026-11-17',
                  'scope':'Rendered Cambridge candidate page read against NSSCAS records. Preceding/following pages not claimed unless explicitly identified in paired evidence.'}
        image['reading_status']='author read; independent review pending'
    confirmed={};possible={}
    audit=json.loads((A/'provenance-reading-r5.json').read_text())['entries']
    for n,line in enumerate(SPEC.strip().splitlines(),1):
        key,stem,num,pgs,confidence,*_=line.split('|')
        cb=json.loads(next((A/'cambridge-discovery').glob(stem+'-*.json')).read_text())
        if n==4 or confidence.startswith('structurally'):continue
        store=possible if confidence.startswith('possible')else confirmed
        for pg in map(int,pgs.split(',')):
            store[(key,cb['sha256'],pg)]=f'8227:PROVENANCE:{n:03}'
    count=0
    for result in screen['results']:
        for c in result['candidates']:
            read=lookup.get(c['candidate_id'])
            if not read:continue
            k=(result['source_key'],c['source_sha256'],c['pdf_page'])
            c['render_reading']=read
            m=confirmed.get(k);lead=possible.get(k)
            c['disposition']='confirmed paired-page correspondence'if m else 'wording-only possible source; hidden'if lead else 'read; no specific source established'
            c['reason']=read['note'];c['match_ids']=[m or lead]if m or lead else[]
            count+=1
    screen['rendered_candidates_read']=count
    screen['unread_above_threshold']=screen['candidates_above_threshold']-count
    candidate_keys={(r['source_key'],c['source_sha256'],c['pdf_page'])
        for r in screen['results']for c in r['candidates']}
    population=set(confirmed.values())
    hits={mid for key,mid in confirmed.items()if key in candidate_keys}
    screen['measured_recall_on_confirmed_pairs']=dict(
        numerator=len(hits),denominator=len(population),
        match_ids_found=sorted(hits),match_ids_missed=sorted(population-hits),
        baseline_r5=dict(numerator=16,denominator=31),
        limitation='Recall on the confirmed-pair register only, not on all real adaptations. Duplicate variants are not separate breadth. The new pair037 changes the denominator.')
    base=screen['limitations'].split(' Measured recall on')[0]
    screen['limitations']=base+f' Measured recall on current confirmed pairs: {len(hits)}/{len(population)}; frozen R5 baseline16/31. This is not corpus-wide adaptation recall.'
    screen['independent_review']='pending'
    write(p,screen)
    write(A/'provenance-screen-images-r5.json',{'images':images,'scope':'Explicit source-page read notes in tools/provenance_screen_readings_r5.json; rendering alone does not establish reading.'})
    print(count,'candidates explicitly read;',screen['unread_above_threshold'],'unread')
if __name__=='__main__':build()
