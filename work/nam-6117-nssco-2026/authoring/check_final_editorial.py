"""Verify final editorial invariants; this is author QA, not independent approval."""
import json,re,hashlib,math,xml.etree.ElementTree as ET
from pathlib import Path
from final_content_edits import OPTIONS
W=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((W/p).read_text())
items=[];parts=[];units=[];qa=[]
for t in range(1,13):
 d=W/f'topics/{t}'
 items+=read(f'topics/{t}/learning-items/topic_{t}_items.json')['items']
 parts+=read(f'topics/{t}/authored_assessment_parts.json')['parts']
 us=[json.loads(p.read_text()) for p in (d/'content-units').glob('*.json')];units+=us
 blocks=[b for u in us for b in u['blocks']]
 assert not any(b['heading'].startswith(('Activity feedback','Activity worked example')) for b in blocks)
 assert sum(b['block_id'].endswith('FINAL-METHOD') for b in blocks)==1
 notes=next(p for p in d.glob('*.md') if re.match(r'^\d+-',p.name)).read_text()
 nums=re.findall(r'^## (\d+(?:\.\d+)*)\s',notes,re.M)
 assert len(nums)==len(us),(t,nums)
 assert [tuple(map(int,n.split('.'))) for n in nums]==sorted(tuple(map(int,n.split('.'))) for n in nums)
 q=read(f'topics/{t}/qa_report.json');assert q['release_decision']=='hold'
 assert not any(c['status']=='fail' for c in q['deterministic_checks'])
 qa.append({'topic':t,'generated_at':q['generated_at'],'counts':{s:sum(c['status']==s for c in q['deterministic_checks']) for s in ['pass','fail','warn','not_run']}})
assert len(items)==844 and len(parts)==236 and len(units)==64
p=read('planning/production-progress.json');assert (p['recall_marks'],p['marks'])==(392,1637)
log=read('planning/final-editorial-log.json');assert sum(x['answer_blocks_removed'] for x in log)==236
manifest=read('review/copied-wording-sources.json');assert manifest['paths_scanned']==28 and manifest['distinct_file_contents']==24
visuals=read('planning/visual-delivery-audit.json')['files'];assert len(visuals)==71
for v in visuals:
 f=W/v['file'];ET.parse(f);assert f.with_suffix('.png').exists()
for ident in ['3-P03','4-P03','6-P02','6-P03']:
 x=next(x for x in items if x['item_id']=='ITEM-6117-'+ident);assert re.search(r'!\[[^\]]*\]\(',x['prompt']),ident
# Independently recompute the numerical methods newly added to the notes.
calculations=[('displaced volume',30.5-18,12.5),('density',31.5/(30.5-18),2.52),('cooling P',(70-55)/6,2.5),('cooling Q',(70-61)/6,1.5),('titre',20.10-1.50,18.60),('acid amount',.150*18.6/1000,.00279),('carbonate concentration',(.150*18.6/1000)/2/(15/1000),.093),('Mg amount',4.8/24,.2),('limiting Mg',.3/2,.15),('gas volume',(.3/2)*24,3.6),('excess Mg',(4.8/24-.3/2)*24,1.2),('C amount',2.4/12,.2),('H:C ratio',.6/(2.4/12),3),('formula multiplier',30/(12+3),2),('yield',6/7.5*100,80),('first rate',12/15,.8),('second rate',(21-12)/15,.6),('oxide oxygen mass',8-5.6,2.4),('iron percent',5.6/8*100,70),('Rf',(4-1)/(7-1),.5),('excess soap',4-1.5,2.5),('soap volume',6.1-2.1,4),('cooling A',(75-57)/8,2.25),('cooling B',(75-63)/8,1.5)]
for name,value,expected in calculations:assert math.isclose(value,expected,rel_tol=1e-10,abs_tol=1e-10),(name,value)
r={'status':'pass','scope':'Final editorial invariants and new worked-method arithmetic; author checks, not independent certification.','items':len(items),'activity_parts':len(parts),'units':len(units),'answer_only_blocks_removed':236,'worked_method_blocks':12,'additional_stoichiometry_methods':4,'repeated_long_sentences_removed':sum(x['repeated_long_sentences_removed'] for x in log),'mc_option_sets_rewritten':len(OPTIONS),'visual_assets':71,'recall_marks':392,'marks':1637,'qa':qa,'new_worked_method_calculations':[{'name':n,'actual':v,'expected':e} for n,v,e in calculations]}
(W/'planning/final-editorial-checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ['qa','new_worked_method_calculations']},indent=2))
