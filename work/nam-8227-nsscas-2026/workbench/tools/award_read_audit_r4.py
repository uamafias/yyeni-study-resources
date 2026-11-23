"""Record an explicit author second-read; never infer a read from extraction."""
import argparse,hashlib,json
from analysis_sources import A,ROOT,WB,write,digest

def fingerprint(row):
 return hashlib.sha256(json.dumps({k:v for k,v in row.items()if k not in ['first_read','second_read']},sort_keys=True).encode()).hexdigest()

def rows_for(year,page):
 d=json.loads((A/'award-register-r4-draft.json').read_text())
 return [r for t in d['award_tables']for r in t['rows']if r['source_locator']['report_year']==year and r['source_locator']['pdf_page']==page]

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('year',type=int);p.add_argument('page',type=int);p.add_argument('--confirm',action='store_true');p.add_argument('--notes',default='')
 args=p.parse_args();rr=rows_for(args.year,args.page)
 if not args.confirm:
  for r in rr:print(r['criterion_id'],r['part'],r['exclusive_method_path'],r['source_mark_type'],r['value'],r['what_earns_it'],'; CONDITION:',r['condition'],'; ALT:',r['accepted_alternatives'],'; DERIVED:',r['derived_additions'])
 else:
  assert rr,'No award rows on this page'
  f=A/'award-second-read-r4.json';log=json.loads(f.read_text())if f.exists()else {'status':'author second-read; not independent review','rows':{}}
  for r in rr:
   image=ROOT/r['first_read']['evidence_path'];assert image.is_file();assert digest(image)==r['first_read']['evidence_sha256']
   log['rows'][r['criterion_id']]={'status':'author second-read against rendered award table','reviewer':'Codex author','date':'2026-11-17',
    'evidence_path':r['first_read']['evidence_path'],'evidence_sha256':digest(image),'row_fingerprint':fingerprint(r),'notes':args.notes}
  write(f,log);print(f'Second-read recorded for {len(rr)} rows, {args.year} PDF {args.page}')
