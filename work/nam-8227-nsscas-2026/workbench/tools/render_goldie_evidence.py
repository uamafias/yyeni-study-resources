import json,pymupdf,sys
from PIL import Image,ImageDraw
from pathlib import Path
from analysis_sources import A,WB,ROOT,write
items=json.load(open(A/'textbook-goldie-population-leads.json'))['items']
pages=sorted({i['pdf_page'] for i in items if int(i['exercise'][:-1])<7 or i['exercise'] in ['10A','10B','10C']})
p=pymupdf.open(ROOT/'sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf');manifest=[]
for off in range(0,len(pages),4):
 selected=pages[off:off+4];s=Image.new('RGB',(800*len(selected),1080),'white');d=ImageDraw.Draw(s)
 for j,n in enumerate(selected):
  px=p[n-1].get_pixmap(matrix=pymupdf.Matrix(1.45,1.45));im=Image.frombytes('RGB',(px.width,px.height),px.samples);im.thumbnail((790,1045));s.paste(im,(800*j,25));d.text((800*j+4,4),f'Goldie PDF {n}; printed {n-14}',fill='red')
 out=WB/'checks/r3'/f'goldie-set-{off//4:02}.png';s.save(out);manifest.append({'path':str(out.relative_to(ROOT)),'pages':selected})
write(WB/'checks/r3/goldie-render-manifest.json',manifest);print('pages',len(pages),'sheets',len(manifest))
