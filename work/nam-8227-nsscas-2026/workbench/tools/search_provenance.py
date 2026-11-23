"""Rank local PDF extraction leads; no network and no assertion of provenance."""
import json, math, re, unicodedata
from collections import Counter
from analysis_sources import A, clean, write
STOP=set('the and that this with from have find show hence given curve equation value values question paper mathematics international cambridge use examiner for which where answer correct diagram marks following point points all not are'.split())
def tokens(s):
 s=unicodedata.normalize('NFKC',s).lower();s=re.sub(r'/[a-z]+',' ',s)
 return [w for w in re.findall(r'[a-z]{2,}|\d+(?:\.\d+)?',s) if w not in STOP and (not w.isdigit() or int(w)>2)]
def build():
 pages=[]
 for f in sorted((A/'cambridge-discovery').glob('*.json')):
  d=json.loads(f.read_text())
  if d.get('kind')!='qp':continue
  for p in d['pages'][1:]:
   t=clean(p['text'])
   if len(tokens(t))<12 or 'BLANK PAGE' in t or 'Additional Page' in t:continue
   pages.append({'source_path':d['path'],'source_sha256':d['sha256'],'year':d['year'],'session_code':d['session_code'],
                 'component':d['component'],'pdf_page':p['pdf_page'],'text':t})
 bag=[Counter(tokens(x['text'])) for x in pages];df=Counter(w for c in bag for w in c)
 idf={w:math.log((len(pages)+1)/(n+1))+1 for w,n in df.items()}
 def vec(c):
  v={w:(1+math.log(n))*idf.get(w,1) for w,n in c.items()};norm=math.sqrt(sum(n*n for n in v.values()))
  return {w:n/norm for w,n in v.items()} if norm else {}
 vectors=[vec(c) for c in bag];results=[]
 for q in json.loads((A/'question-analysis.json').read_text())['questions']:
  v=vec(Counter(tokens(' '.join(p['source_segment'] for p in q['parts']))))
  scores=[sum(n*x.get(w,0) for w,n in v.items()) for x in vectors]
  best=sorted(range(len(pages)),key=lambda i:(-scores[i],pages[i]['source_path'],pages[i]['pdf_page']))[:8]
  results.append({'source_key':q['source_key'],'status':'searched local discovery text; candidates require rendered confirmation',
     'candidates':[{**{k:x for k,x in pages[i].items() if k!='text'},'similarity':round(scores[i],5),'discovery_excerpt':pages[i]['text'][:1700]} for i in best]})
 write(A/'provenance-search-leads.json',{'method':'TF-IDF lexical/numerical page ranking, eight leads per question, all 119 searched; score is not evidence of adaptation. OCR/extraction defects and diagrams can hide matches.',
  'question_count':len(results),'cambridge_search_pages':len(pages),'results':results})
 for r in results:
  c=r['candidates'][0];print(r['source_key'],f'{c["similarity"]:.2f}',c['source_path'].split('/')[-1],c['pdf_page'],c['discovery_excerpt'][:115])
if __name__=='__main__':build()
