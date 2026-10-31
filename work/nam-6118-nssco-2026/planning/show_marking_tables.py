from pathlib import Path
import re,sys,json
W=Path(__file__).resolve().parents[1]
y=int(sys.argv[1]);native=(W/f'planning/extracted/{y}-report.layout.txt').read_text();ocr=(W/f'planning/extracted/{y}-report.ocr-draft.txt').read_text()
np={int(n):t for n,t in re.findall(r'=== SOURCE PDF PAGE (\d+) ===\n(.*?)(?==== SOURCE PDF PAGE|\Z)',native,re.S)}
op={int(n):t for n,t in re.findall(r'=== SOURCE PDF PAGE (\d+); OCR DRAFT, VERIFY IMAGE ===\n(.*?)(?==== SOURCE PDF PAGE|\Z)',ocr,re.S)}
inv=json.loads((W/'curriculum/source-inventory.json').read_text());r=next(x for x in inv['entries'] if x.get('year')==y and x['kind']=='combined_examiner_report');start=next(x['pdf_page'] for x in r['paper_headers'] if x['paper']==2)
for p in sorted(np):
 if p<start:continue
 text=op.get(p,np[p]);on=False;out=[]
 for l in text.splitlines():
  if re.match(r'^\s*Question\s+\d+',l,re.I) or re.match(r'^\s*\d*\.?\s*POSITIVE SUGGESTIONS',l,re.I):on=False
  if re.search(r'Mark [Ss]cheme|Expected answers',l,re.I) or re.match(r'^\s*Question\s+Answer',l) or re.match(r'^\s*\d\s+(?:\(a\)|Method)',l):on=True
  if on:out.append(l)
 if out:print(f'=== {y} PDF {p} {"OCR" if p in op else "native"} ===\n'+'\n'.join(out))
