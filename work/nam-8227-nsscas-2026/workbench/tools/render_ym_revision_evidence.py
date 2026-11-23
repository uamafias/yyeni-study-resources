import json,re,pymupdf,sys
from PIL import Image,ImageDraw
from pathlib import Path
from analysis_sources import A,WB,ROOT,write
p=pymupdf.open(ROOT/'Y=mc as textbook.pdf');groups=[[50],[105],[148],[227,228],[263,264],[318,319],[372,373],[405],[445],[480],[527,528],[556],[583,584]]
manifest=[]
for ch,ns in enumerate(groups,1):
 # Also include worked exam-style sections immediately before the revision set.
 starts=[49,103,146,225,261,314,369,403,443,479,525,554,581]
 ns=list(range(starts[ch-1],max(ns)+1))
 s=Image.new('RGB',(800*len(ns),1160),'white');d=ImageDraw.Draw(s)
 for j,n in enumerate(ns):
  pix=p[n-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5));im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((790,1125));s.paste(im,(800*j,25));d.text((800*j+4,4),f'YM chapter {ch}, PDF {n}',fill='red')
 out=WB/'checks/r3'/f'ym-revision-{ch:02}.png';s.save(out);manifest.append({'path':str(out.relative_to(ROOT)),'chapter':ch,'pdf_pages':ns})
write(WB/'checks/r3/ym-revision-render-manifest.json',manifest)
