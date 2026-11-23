"""Discover report wording, including raster-table text preserved by visual transcription.
A scan finds leads; it cannot certify their educational interpretation.
"""
import json,re,hashlib
from analysis_sources import A,clean,write

def build():
 pages=json.loads((A/'report-page-index-r4.json').read_text())['pages']
 register=json.loads((A/'marking-conventions.json').read_text())
 dispositions_path=A/'convention-context-dispositions-r4.json'
 decisions={}
 for line in (A.parent/'tools/convention_context_decisions_r4.txt').read_text().splitlines():
  if not line or line.startswith('#'):continue
  prefix,status,refs,reason=line.split('|');stem,nums=prefix.split(':')
  for n in nums.split(','):
   key=f'{stem}-H{int(n):02}';assert key not in decisions,key
   decisions[key]={'status':status,'convention_rule_ids':[f'8227:CONVENTION:{int(x):03}'for x in refs.split(',')if x],'reason':reason,'author':'Codex','date':'2026-11-17'}
 write(dispositions_path,decisions)
 items=[]
 pattern=r'\bmust\b|\bno marks\b|\bnot accepted\b|\blose\b|\blost\b|\bcondone\b|\baccept\w*\b'
 for page in pages:
  text=clean(page['text_discovery_only'])
  for n,m in enumerate(re.finditer(pattern,text,re.I),1):
   key=f'{page["year"]}-{page["pdf_page"]}-H{n:02}'
   context=text[max(0,m.start()-180):m.end()+200]
   links=[r['rule_id']for r in register['rules']if any(e['source_locator']['report_year']==page['year']and e['source_locator']['pdf_page']==page['pdf_page']and e['verbatim_excerpt'].lower()in context.lower()for e in r['evidence'])]
   decision=decisions.get(key)
   if decision and decision['status']=='registered in award':
    m=re.search(r'(202[1-5]) P([12]) Q(\d+)(?:\(([^)]+)\))?',decision['reason']);assert m,(key,'local award locator missing')
    source_key=f'{m[1]}-{m[2]}-Q{m[3]}'
    table=next(t for t in register['award_tables']if t['source_key']==source_key)
    decision['local_award_record_links']=[r['criterion_id']for r in table['rows']if not m[4]or r['part']==m[4]]
    assert decision['local_award_record_links'],(key,m[0])
    decision['award_link_basis']='Question/part locator in the author disposition; scoped source rows, not a new universal penalty.'

   items.append({'hit_id':key,'year':page['year'],'pdf_page':page['pdf_page'],'printed_page':page['pdf_page']-2,
     'keyword':m[0],'context':context,'source_path':page['source_path'],'source_sha256':page['source_sha256'],
     'render_path':page['render_path'],'render_sha256':page['render_sha256'],'matched_rule_leads':links,
     'disposition':decision or {'status':'pending author disposition'}})
 # Award conditions are visually transcribed, so image-only hits are not silently omitted.
 raster=[]
 for t in register['award_tables']:
  for r in t['rows']:
   if r['evidence_kind']!='official award table':continue
   text=r['what_earns_it']+' '+r['condition']+' '+' '.join(r['accepted_alternatives'])
   if re.search(pattern,text,re.I):raster.append({'criterion_id':r['criterion_id'],'source_locator':r['source_locator'],
      'condition':r['condition'],'accepted_alternatives':r['accepted_alternatives'],
      'disposition':'registered in the second-read official award row; local condition, not a universal penalty'})
 result={'status':'context scan; completion requires every native hit disposition','native_hits':items,'visually_transcribed_award_condition_hits':raster,
    'counts':{'native_hits':len(items),'pending_author_disposition':sum(i['disposition']['status'].startswith('pending')for i in items),'award_rows_with_keywords':len(raster)},
    'limits':'Native text is a discovery aid; raster award conditions are independently scanned from the author visual transcription. Performance and teaching comments need explicit dispositions, not automatic marking policies.'}
 write(A/'convention-context-scan-r4.json',result)
 print(json.dumps(result['counts']))
if __name__=='__main__':build()
