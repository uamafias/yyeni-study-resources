"""Focused 12-word report-overlap check; intentionally quoted audit fields excluded."""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1]
def words(s):return re.findall(r'[a-z0-9]+',s.lower())
def grams(s):
 t=words(s);return (tuple(t[n:n+12]) for n in range(max(0,len(t)-11)))
source={}
for p in sorted((W/'planning/extracted').glob('*-report.*.txt')):
 for g in grams(p.read_text()):source.setdefault(g,p.name)
items=[]
for file in ('misconceptions.json','candidate-errors.json'):
 for e in json.loads((W/'curriculum'/file).read_text())['entries']:
  items.append((e['entry_id'],'diagnostic',e['discrimination_task']))
for e in json.loads((W/'curriculum/answer-shapes.json').read_text())['entries']:
 items.append((e['shape_id'],'interpretation',e['interpretation']))
 for i,s in enumerate(e['credit_structure']):items.append((e['shape_id'],f'credit_structure[{i}]',s))
hits=[]
for eid,field,s in items:
 for g in grams(s):
  if g in source:hits.append(dict(entry=eid,field=field,words=' '.join(g),source=source[g]))
out=dict(status='pass' if not hits else 'fail',rule='No 12 or more consecutive normalised words in diagnostic tasks or answer-shape narrative may match the held report text.',checked_text_fields=len(items),report_text_files=len(list((W/'planning/extracted').glob('*-report.*.txt'))),excluded='Intentional verbatim audit anchors, source excerpts, locators and source-derived question metadata.',matches=hits)
(W/'review/original-wording-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));raise SystemExit(bool(hits))
