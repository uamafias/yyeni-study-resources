import sys,json
from pathlib import Path
from PIL import Image,ImageDraw

from analysis_sources import A,WB,ROOT,render_page,write
from provenance_inputs import SPEC
qs={q['source_key']:q for q in json.loads((A/'question-analysis.json').read_text())['questions']}
manifest=[]
for i,line in enumerate(SPEC.strip().splitlines(),1):
 key,stem,num,pgs,*_=line.split('|');q=qs[key];cb=json.loads(next((A/'cambridge-discovery').glob(stem+'-*.json')).read_text())
 ns_pages=sorted(set(q['pdf_pages']));cb_pages=[int(p) for p in pgs.split(',')]
 sources=[('NSSCAS',q['question_source_path'],p) for p in ns_pages]+[('Cambridge',cb['path'],p) for p in cb_pages]
 # One paired evidence sheet per match, with all source pages and readable labels.
 cols=len(sources);sheet=Image.new('RGB',(700*cols,1020),'white');draw=ImageDraw.Draw(sheet)
 for j,(board,path,p) in enumerate(sources):
  im=Image.open(render_page(path,p)).convert('RGB');im.thumbnail((690,980));sheet.paste(im,(700*j,25));draw.text((700*j+4,4),f'{key if board=="NSSCAS" else stem} Q{q["question"] if board=="NSSCAS" else num} PDF {p}',fill='red')
 target=WB/'checks/r4'/f'provenance-{i:02}.png';sheet.save(target)
 manifest.append({'nsscas':key,'cambridge':stem,'question':num,'evidence_sheet':str(target.relative_to(ROOT)),'source_pages':sources})
write(WB/'checks/r4/provenance-render-manifest.json',manifest)
print(len(manifest))
