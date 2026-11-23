"""Render local book pages for author analysis; no acquisition or source mutation."""
import json,sys
from PIL import Image,ImageDraw
from analysis_sources import A,WB,ROOT,write,digest,render_page

def render(book,pages,name):
 inv=json.loads((A/'textbook-inventory.json').read_text());src=next(x for x in inv['books']if (x['document_id']=='8227-SRC-015')==(book=='Goldie'))
 target=WB/'checks/r4'/f'{name}.png';target.parent.mkdir(exist_ok=True)
 sheet=Image.new('RGB',(1700,1240*((len(pages)+1)//2)),'white');draw=ImageDraw.Draw(sheet)
 for n,p in enumerate(pages):
  im=Image.open(render_page(src['path'],p)).convert('RGB');im.thumbnail((845,1200));x=(n%2)*850;y=(n//2)*1240
  sheet.paste(im,(x,y+25));draw.text((x+4,y+4),f'{book} PDF {p}',fill='red')
 sheet.save(target)
 return {'book':book,'pdf_pages':pages,'path':str(target.relative_to(ROOT)),'sha256':digest(target),'source_path':src['path'],'source_sha256':src['sha256'],'inspection':'pending; rendering is not inspection'}
if __name__=='__main__':
 r=render(sys.argv[1],[int(x)for x in sys.argv[2].split(',')],sys.argv[3]);write(WB/'checks/r4'/f'{sys.argv[3]}.json',r);print(r['path'])
