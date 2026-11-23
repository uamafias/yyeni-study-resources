"""Render every Mathematics examiner-report page; never infer table absence from text."""
import json,shutil
from pypdf import PdfReader
from analysis_sources import A,WB,ROOT,write,digest,render_page
RANGES={2021:(231,243),2022:(301,316),2023:(321,339),2024:(325,343),2025:(345,364)}

def build():
 old=json.loads((A/'report-reading-8227-r3.json').read_text());sources={p['year']:p['source_path'] for p in old['pages']};rows=[]
 target=WB/'checks/r4';target.mkdir(exist_ok=True)
 for year,(start,end) in RANGES.items():
  source=sources[year];doc=PdfReader(ROOT/source)
  for n in range(start,end+1):
   rendered=render_page(source,n);out=target/f'report-{year}-{n:03}.png'
   if not out.exists() or digest(out)!=digest(rendered):shutil.copyfile(rendered,out)
   rows.append({'year':year,'source_path':source,'source_sha256':digest(ROOT/source),'pdf_page':n,
       'printed_page_candidate':n-2,'render_path':str(out.relative_to(ROOT)),'render_sha256':digest(out),
       'renderer':'macOS PDFKit144dpi; full page','text_discovery_only':doc.pages[n-1].extract_text() or ''})
 write(A/'report-page-index-r4.json',{'scope':'All87 Mathematics report pages, including general comments and blank pages; visual census required',
    'ranges':{str(y):list(v) for y,v in RANGES.items()},'pages':rows})
 print('Rendered',len(rows),'report pages')
if __name__=='__main__':build()
