"""Flag exact 8-word overlaps with held 6116 papers and Biology report pages.

This is an overlap screen, not a copyright clearance or semantic review.
No official text is stored in the resulting report.
"""
import hashlib,json,re,subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

W=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]
def words(s): return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?",s.lower())
inv=json.loads((W/'curriculum/source-inventory.json').read_text())
spans={s['year']:s for s in json.loads((W/'assessment-evidence/examiner_evidence.json').read_text())['biology_spans']}
jobs=[(p['path'],None,None) for p in inv['question_papers']]
for r in inv['examiner_reports_distinct'].values():
 path=r['copies'][0];year=next(y for y in spans if y in path);s=spans[year]
 jobs.append((path,s['start_pdf_page'],s['end_pdf_page']))
def extract(job):
 path,first,last=job;cmd=['pdftotext','-layout']
 if first:cmd+=['-f',str(first),'-l',str(last)]
 result=subprocess.run(cmd+[str(ROOT/path),'-'],check=True,text=True,capture_output=True)
 return path,first,result.stdout.split('\f')
index={};page_count=0
with ThreadPoolExecutor(max_workers=6) as pool:
 for path,first,pages in pool.map(extract,jobs):
  for offset,page in enumerate(pages):
   ws=words(page)
   if not ws:continue
   page_count+=1
   for n in range(len(ws)-7):index.setdefault(tuple(ws[n:n+8]),(path,(first or 1)+offset))
hits=[]
for t in range(1,6):
 b=W/'topics'/str(t)
 artefacts=[]
 for p in (b/'content-units').glob('*.json'):
  for block in json.loads(p.read_text())['blocks']:artefacts.append((block['block_id'],block['text']))
 for item in json.loads((b/f'learning-items/topic_{t}_items.json').read_text())['items']:
  for field in ('prompt','canonical_answer','marking_guidance'):
   v=item[field];artefacts.append((item['item_id']+':'+field,' '.join(v) if isinstance(v,list) else v))
 for owner,text in artefacts:
  ws=words(text);matches=[]
  for n in range(len(ws)-7):
   key=tuple(ws[n:n+8])
   if key in index:
    path,page=index[key];matches.append({'token_offset':n,'ngram_sha256':hashlib.sha256(' '.join(key).encode()).hexdigest(),'source':path,'pdf_page':page})
  if matches:hits.append({'topic':str(t),'artefact':owner,'matches':matches})
out={'scope':'All 18 held papers, including Paper 1; Biology sections only of six held reports. Syllabus not reopened.',
 'normalisation':'Lowercase alphanumeric tokens; exact windows of 8 words, with no cross-page joins.',
 'documents':len(jobs),'nonempty_pages':page_count,'source_ngrams':len(index),'hits':hits,
 'limitation':'Extraction can miss image-only text and reading-order text. Shared prescribed definitions require explicit review; this cannot certify independent scenario design or semantic originality.'}
(W/'topics/wording_overlap_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'{len(jobs)} documents / {page_count} pages; {len(hits)} artefacts flagged at 8 words')
for h in hits:print(h['topic'],h['artefact'],len(h['matches']))
