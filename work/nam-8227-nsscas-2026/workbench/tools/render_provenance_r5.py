"""Pair-image evidence for R5; no source mutation or downloading."""
import sys,json
from PIL import Image,ImageDraw
from analysis_sources import A,WB,ROOT,render_page,write,digest
from provenance_inputs import SPEC,PAIR_PART_MAP

def render(n):
 line=SPEC.strip().splitlines()[n-1];key,stem,num,pgs,*_=line.split('|');q=next(q for q in json.loads((A/'question-analysis.json').read_text())['questions']if q['source_key']==key);cb=json.loads(next((A/'cambridge-discovery').glob(stem+'-*.json')).read_text())
 nspages=q['pdf_pages']
 if n in[34,35]:nspages=[q['pdf_pages'][0]]
 sources=[('NSSCAS',q['question_source_path'],p)for p in nspages]+[('Cambridge',cb['path'],int(p))for p in pgs.split(',')]
 sheet=Image.new('RGB',(850*len(sources),1240),'white');draw=ImageDraw.Draw(sheet)
 for i,(board,path,pg)in enumerate(sources):
  im=Image.open(render_page(path,pg)).convert('RGB');im.thumbnail((840,1200));sheet.paste(im,(850*i,25));draw.text((850*i+5,5),f'{board} {key if board=="NSSCAS"else stem} PDF{pg}',fill='red')
 out=WB/f'checks/r5/provenance-{n:03}.png';sheet.save(out)
 rec={'pair_id':n,'input_sha256':__import__('hashlib').sha256(line.encode()).hexdigest(),'image_path':str(out.relative_to(ROOT)),'image_sha256':digest(out),'source_pages':[{'board':board,'path':path,'pdf_page':pg,'source_sha256':digest(ROOT/path)}for board,path,pg in sources],'status':'pending image reading'};write(WB/f'checks/r5/provenance-{n:03}.json',rec);print(n,flush=True)
if __name__=='__main__':
 for n in map(int,sys.argv[1:]):render(n)
