"""Render all above-threshold Cambridge discovery pages; rendering is not reading."""
import json
from pathlib import Path
from PIL import Image,ImageDraw
from collections import defaultdict
from analysis_sources import A,WB,ROOT,render_page,digest,write

def build():
    screen=json.loads((A/'provenance-full-screen-r5.json').read_text());links=defaultdict(list);sources={}
    for r in screen['results']:
        for c in r['candidates']:
            key=(c['source_sha256'],c['pdf_page']);links[key].append({'nsscas_question_key':r['source_key'],'candidate_id':c['candidate_id']});sources[key]=c
    records=[];target=WB/'checks/r5/screen';target.mkdir(parents=True,exist_ok=True)
    keys=sorted(links,key=lambda k:(sources[k]['source_path'],k[1]))
    for offset in range(0,len(keys),3):
        batch=keys[offset:offset+3];tiles=[];entries=[]
        for key in batch:
            c=sources[key];img=Image.open(render_page(c['source_path'],c['pdf_page'])).convert('RGB');img.thumbnail((850,1210))
            tile=Image.new('RGB',(850,1270),'white');tile.paste(img,(0,60));d=ImageDraw.Draw(tile)
            d.text((5,3),Path(c['source_path']).name+' PDF'+str(c['pdf_page']),fill='red')
            d.text((5,18),', '.join(v['nsscas_question_key']for v in links[key]),fill='red')
            tiles.append(tile);entries.append({'source_path':c['source_path'],'source_sha256':c['source_sha256'],'pdf_page':c['pdf_page'],'candidate_links':links[key]})
        canvas=Image.new('RGB',(850*len(tiles),1270),'white')
        for i,tile in enumerate(tiles):canvas.paste(tile,(i*850,0))
        path=target/f'pages-{offset//3+1:03}.png';canvas.save(path)
        records.append({'batch':offset//3+1,'path':str(path.relative_to(ROOT)),'sha256':digest(path),'pages':entries,'reading_status':'unread'})
    write(A/'provenance-screen-images-r5.json',{'images':records,'scope':'Source-page renders for full-screen candidates. No reading status is inferred from rendering.'})
    print(len(keys),'unique pages in',len(records),'contact images')
if __name__=='__main__':build()
