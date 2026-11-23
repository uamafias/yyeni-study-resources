import sys,json,re,pymupdf

from analysis_sources import A,write
p=pymupdf.open('sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf')
items=[];context=None;expected=1
for n,page in enumerate(p,1):
 if not(15<=n<=175 or 248<=n<=293):continue
 text=page.get_text();h=re.search(r'(?m)^Exercise\s+(\d+[A-Z])\s*$',text)
 if h:context=h[1];expected=1
 if not context:continue
 starts=[]
 for b in page.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   for s in l['spans']:
    if s['font']=='DIN-Bold' and 9.9<s['size']<10.1 and re.fullmatch(r'\s*\d{1,2}\s*',s['text']):starts.append((round(s['bbox'][1],2),int(s['text']),s['bbox']))
 starts.sort()
 for y,num,box in starts:
  if num==expected:
   items.append({'book':'Goldie','exercise':context,'item_number':str(num),'pdf_page':n,'printed_page':n-14,'bbox':list(box),'discovery_status':'native font/sequence lead; not image verified'});expected+=1
write(A/'textbook-goldie-population-leads.json',{'items':items,'status':'Font/sequence discovery; count needs visual census reconciliation'})
from collections import defaultdict
s=defaultdict(list)
for x in items:s[x['exercise']].append(x)
for e,ls in s.items():print(e,len(ls),'pages',sorted({x['pdf_page'] for x in ls}),'last',ls[-1]['item_number'])
