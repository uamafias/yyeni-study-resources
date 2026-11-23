import json,re,pymupdf,sys
from pathlib import Path

from analysis_sources import A,write
ym=[]
for n in range(12,587):
 d=json.loads((A/f'ocr/ymxc/page-{n:04}.json').read_text());lines=[x['text'] for x in d['lines']]
 leads=[]
 for i,t in enumerate(lines):
  if re.match(r'^(?:Example|Try Now|Lry Now|Exercise|Revision Exercise)\s*[-:]?\s*\d',t,re.I):leads.append({'line':i,'heading':t,'context':' '.join(lines[i:i+5])})
 ym.append({'pdf_page':n,'heading_leads':leads,'text':'\n'.join(lines)})
write(A/'textbook-ymxc-discovery.json',{'status':'OCR discovery only, not item verification','pages':ym})
g=pymupdf.open('sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf');pages=[]
for n,p in enumerate(g,1):
 t=p.get_text();leads=re.findall(r'(?:Example|EXERCISE|REVISION EXERCISE)\s*\d+(?:\.\d+)?',t)
 pages.append({'pdf_page':n,'printed_page_candidate':n-14 if n>=15 else None,'heading_leads':leads,'text':t})
write(A/'textbook-goldie-discovery.json',{'status':'Native text discovery only; maths and diagrams need rendered checks','pages':pages})
print('Goldie exercise/REVISION headings in scope:')
for p in pages:
 if p['pdf_page']<176 or 248<=p['pdf_page']<=272:
  h=[s for s in p['heading_leads'] if 'EXERCISE' in s];
  if h:print(p['pdf_page'],h)
print('YM revision headings')
for p in ym:
 for h in p['heading_leads']:
  if h['heading'].lower().startswith('revision'):print(p['pdf_page'],h['heading'])
