"""Index examiner commentary by its printed question reference; retain provenance."""
from pathlib import Path
import re,json
WS=Path(__file__).resolve().parents[1];EV=WS/'assessment-evidence'
sources=json.loads((EV/'source-manifest.json').read_text())
rows=[]
for source in sources:
 if source['kind']!='examiner_report':continue
 paper=None;root=None;letter=None;roman=None
 pages=(EV/'extracted'/f'{source["source_id"]}-layout.txt').read_text().split('\f')
 for offset,page in enumerate(pages):
  lines=page.splitlines();pdfpage=source['pdf_page_range'][0]+offset
  covered=set()
  for i,line in enumerate(lines):
   s=re.sub(r'\s+',' ',line).strip()
   p=re.fullmatch(r'Paper\s+([123])',s,re.I)
   if p:paper='P'+p[1];root='1';letter=None;roman=None;continue
   if s.upper()=='SECTION B' and paper=='P3':root='3';letter=None;roman=None;continue
   if re.match(r'Positive suggestions?|Suggestions? to teachers',s,re.I):root=None;letter=None;roman=None
   q=re.match(r'^(?:Question\s+)([1-4])\b',s,re.I)
   if q:root=q[1];letter=None;roman=None
   q=re.match(r'^([1-4])[.]?\s*(?=\([a-z]\))',s)
   if q:root=q[1];letter=None;roman=None;s=s[q.end():].strip()
   m=re.match(r'^(\([a-z]\))?\s*(\([ivx]+\))?\s*(.*)',s)
   lm,rm=m[1],m[2]
   if lm in ['(i)','(v)','(x)'] and not rm:rm,lm=lm,None
   if lm:letter=lm[1:-1];roman=None
   if rm:roman=rm[1:-1]
   if i in covered:continue
   if not re.search(r'poorly|fairly|well.answer|could not|couldn.t|failed|unable|confus|instead|learner|candidate',s,re.I):continue
   if 'NSSCO Examiners Report' in s:continue
   # Continue the explanation, stopping before the supplied answer or next part.
   chunk=[line]
   for j,following in enumerate(lines[i+1:i+12],i+1):
    fs=following.strip()
    if not fs or re.match(r'Answers?\b|Correct answer|\([a-zivx]+\)',fs,re.I):break
    if re.search(r'poorly|fairly|well.answer',fs,re.I):break
    if re.search(r'NSSCO|^\d+$',fs):break
    chunk.append(following)
    covered.add(j)
   text=re.sub(r'\s+',' ','\n'.join(chunk)).strip()
   text=re.split(r'\bAnswers?\s*:',text,flags=re.I)[0].strip()
   if len(text)<15:continue
   ref=(root or '')+(f'({letter})' if letter else '')+(f'({roman})' if roman else '')
   rows.append({'finding_id':f'{source["source_id"]}-F{len(rows)+1:04d}',
     'source_id':source['source_id'],'year':source['year'],'paper_id':paper,'question_ref_candidate':ref or None,
     'comment_internal':text,'source_locator':{'path':source['path'],'pdf_page':pdfpage,'printed_page':pdfpage-2,'line_in_extraction':i+1},
     'kind':'performance_only' if re.fullmatch(r'.*(?:Well|Fairly|Poorly) answered[.]?',text,re.I) else 'commentary',
     'association_method':'question-reference index; associations are checked against available paper references, not inferred from topic keywords'})
(EV/'report-comments-index.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
for r in rows:
 if re.search(r'instead|could not|couldn.t|failed|unable|confus|without|only (?:list|refer|stat|defin)|did not',r['comment_internal'],re.I):
  print(r['finding_id'],r['paper_id'],r['question_ref_candidate'],'p'+str(r['source_locator']['printed_page']),r['comment_internal'])
print('INDEXED',len(rows),'comments')
