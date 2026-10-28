"""Independent numeric/attachment audit for the 12 diagram cards, not a full-subject verdict.
Expected calculations below are restated from learner prompts, not the author's verifier/spec.
The recorded visual reading is separate from these mechanical assertions.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,re,subprocess
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1]
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
results=[]
def row(iid,calculation,expected,actual):
 assert actual==expected,(iid,actual,expected)
 results.append({'item_id':iid,'calculation':calculation,'result':str(actual),'pass':True})
row('ITEM-6145-1.1-011-PROC','Cattle forgone at successive 50-tonne maize increases',[5,15,25,35],[80-75,75-60,60-35,35-0])
row('ITEM-6145-3.3-019-PROC','PED initial-value percentage ratios',[F(-1,2),F(-3,2)],[(F(q-100,100)/F(30-20,20))for q in[75,25]])
row('ITEM-6145-3.3-020-PROC','PES initial-value percentage ratios',[F(8,5),F(2,5)],[(F(q-50,50)/F(600-400,400))for q in[90,60]])
row('ITEM-6145-4.2-025-PROC','D=400-10w, S=10w-100; then D increases by 100',[(25,150),(30,200)],[(F(500,20),10*F(500,20)-100),(F(600,20),10*F(600,20)-100)])
row('ITEM-6145-5.4-031-PROC','Total cost / litres',[F(17,2),6,F(9,2),4,F(9,2),6],[F(c,q)for c,q in zip([85000,120000,135000,160000,225000,360000],[10000,20000,30000,40000,50000,60000])])
row('ITEM-6145-6.3-017-PROC','Bread: Qd=1200-50p, Qs=50p-200; p=12 control',(14,500,600,400,200),(F(1400,100),50*F(1400,100)-200,1200-50*12,50*12-200,(1200-50*12)-(50*12-200)))
row('ITEM-6145-6.3-018-PROC','Mahangu: Qd=700-2p, Qs=2p-100; p=250 control',(200,300,200,400,200),(F(800,4),2*F(800,4)-100,700-2*250,2*250-100,(2*250-100)-(700-2*250)))
row('ITEM-6145-6.3-019-PROC','Guards: D=900-20w, S=20w-100; w=30 control',(25,400,300,500,200,100),(F(1000,40),900-20*F(1000,40),900-20*30,20*30-100,(20*30-100)-(900-20*30),400-(900-20*30)))
row('ITEM-6145-3.2-002-PROC','D=120-5p, S=5p; p rises 8 to 16',[(80,40),(40,80)],[(120-5*p,5*p)for p in[8,16]])
row('ITEM-6145-3.2-006-PROC','D=120-3p, S=3p; equilibrium and shortage at p=10',(20,60,60),(F(120,6),3*F(120,6),(120-3*10)-3*10))
row('ITEM-6145-3.2-010-PROC','D changes 120-3p to 150-3p, S=3p',(25,75),(F(150,6),3*F(150,6)))
row('ITEM-6145-3.2-017-PROC','D=120-3p, S changes 3p to 3p+30',(15,75),(F(90,6),3*F(90,6)+30))
manifest=load(W/'diagrams/asset-manifest.json')['items'];wo=load(W/'planning/revision-01/claude-visual-work-order.json')['cards'];assert set(manifest)=={c['slot_id']for c in wo};allitems={};missing=[];sloterrors=[]
for p in (W/'topics').glob('*/work_order.json'):
 t=p.parent.name;order=load(p);items=load(p.parent/f'learning-items/topic_{t}_items.json')['items'];counts=Counter(i['item_id']for i in items);slots=order['item_slots']+order['performance_tasks'];want={s['slot']for s in slots};c=load(p.parent/'contract.json');assert c['required_outputs']['learning_items']==c['depth_constraints']['item_budget']==len(want)
 missing+=list(want-set(counts));assert set(counts)<=want and all(n==1 for n in counts.values())
 for s in slots:
  i=next((i for i in items if i['item_id']==s['slot']),None)
  if i:
   for k in ['subtype','item_type','assessment_objectives','blooms_level','command_word','mark_tariff']:
    if k in s and s[k]!=i.get(k):sloterrors.append((s['slot'],k))
 allitems.update({i['item_id']:i for i in items})
assert not sloterrors,sloterrors;pending={s['slot_id']for s in load(W/'planning/revision-01/scope.json')if s['owner']=='Codex'};assert set(missing)==pending and len(missing)==37 and len(allitems)==588
assets=[]
for iid,e in manifest.items():
 note_text='\n'.join(b.get('text','')for p in (W/f'topics/{e["topic_id"]}/content-units').glob('*.json')for b in load(p)['blocks']);assert Path(e['answer']['png']).name in note_text
 for side in ['question','answer']:
  d=e[side];p=W/d['png'];svg=W/d['svg_master'];assert sha(p)==d['png_sha256']and sha(svg)==d['svg_sha256'];assert d['yyeni_asset_id']is None;assets.append({'item_id':iid,'side':side,'png':str(p.relative_to(W)),'png_sha256':sha(p),'svg_sha256':sha(svg)})
# The four pre-existing visual cards retain the learner text from the authored checkpoint.
existing=[]
old=json.loads(subprocess.check_output(['git','show','c7d6bb1:work/nam-6145-nssco-2026/topics/3.2/learning-items/topic_3.2_items.json']));old={i['item_id']:i for i in old['items']}
for c in wo:
 if c['existing_card']:
  iid=c['slot_id'];assert all(allitems[iid][k]==old[iid][k]for k in ['prompt','canonical_answer','marking_guidance']);existing.append(iid)
pubhash={p:h for p,h in load(W/'planning/revision-01/baseline/preservation-hashes.json').items()if p.startswith('publish/')};assert all(sha(ROOT/p)==h for p,h in pubhash.items())
report={'status':'PASS - focused diagram calculations, mappings and attachments','numeric_recomputations':results,'assets':assets,'visual_cards':12,'pngs':24,'all_625_contract_counts_correct':True,'filled_items':588,'missing_items':sorted(missing),'existing_visual_text_unchanged_since_authored_checkpoint':existing,'publication_unchanged':True,'limits':'The author verifier supplies the SVG geometry checks; Codex separately read every full-size and phone image, all 12 prompts/answers/rubrics, new/moved note blocks and 16 claims. No full-bank semantic review or live YYeni import is claimed.'}
(W/'review/codex-visual-audit-6145.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: 12 independent numerical recomputations, 24 PNG/SVG pairs, 588 exact slots filled / 37 assigned slots pending, all contract counts correct, publication unchanged.')
