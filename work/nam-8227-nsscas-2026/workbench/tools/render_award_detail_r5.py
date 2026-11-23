"""Scale-4 PDFKit source details; source PDFs are read only."""
import argparse,json,subprocess
from pathlib import Path
from PIL import Image
from analysis_sources import ROOT,WB,A,digest,write

def render(year,page,box,name):
 idx=json.loads((A/'report-page-index-r4.json').read_text())['pages'];row=next(r for r in idx if r['year']==year and r['pdf_page']==page)
 out=WB/'checks/r5';out.mkdir(exist_ok=True);cache=out/'scale4';cache.mkdir(exist_ok=True)
 swift=WB/'tools/render_pdf_detail_r5.swift';binary=cache/('render-'+digest(swift)[:12])
 if not binary.exists():subprocess.run(['swiftc',str(swift),'-o',str(binary)],check=True,capture_output=True)
 directory=cache/str(year);target=directory/f'page-{page:04}.png'
 if not target.exists():subprocess.run([str(binary),str(ROOT/row['source_path']),str(directory),str(page)],check=True,capture_output=True)
 with Image.open(target)as image:
  if box is None:box=[0,0,image.width/4,image.height/4]
  crop=image.crop(tuple(round(v*4)for v in box));dest=out/(name+'.png');crop.save(dest)
 record={'year':year,'pdf_page':page,'printed_page':page-2,'source_path':row['source_path'],'source_sha256':row['source_sha256'],'render_scale':4,'crop_box_pdf_points':box,'path':str(dest.relative_to(ROOT)),'sha256':digest(dest),'inspection':'pending; rendering is not reading'}
 write(out/(name+'.json'),record);return record
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('year',type=int);p.add_argument('page',type=int);p.add_argument('name');p.add_argument('--box',nargs=4,type=float);a=p.parse_args();print(json.dumps(render(a.year,a.page,a.box,a.name)))
