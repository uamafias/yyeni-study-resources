"""Render explicitly selected local book pages for author inspection; never edits PDFs."""
import argparse,json,pymupdf
from PIL import Image,ImageDraw
from analysis_sources import A,WB,ROOT,write

def render(path,pages,prefix,per_sheet=3):
 doc=pymupdf.open(ROOT/path);manifest=[]
 for off in range(0,len(pages),per_sheet):
  selected=pages[off:off+per_sheet];s=Image.new('RGB',(800*len(selected),1160),'white');d=ImageDraw.Draw(s)
  for j,n in enumerate(selected):
   pix=doc[n-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5));im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((790,1125));s.paste(im,(800*j,25));d.text((800*j+4,4),f'{prefix}: PDF {n}',fill='red')
  out=WB/'checks/r3'/f'{prefix}-{off//per_sheet:02}.png';s.save(out);manifest.append({'path':str(out.relative_to(ROOT)),'pages':selected})
 write(WB/'checks/r3'/f'{prefix}-manifest.json',manifest)
 return manifest
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('path');p.add_argument('prefix');p.add_argument('pages',help='Comma separated PDF pages');a=p.parse_args();render(a.path,[int(n) for n in a.pages.split(',')],a.prefix)
