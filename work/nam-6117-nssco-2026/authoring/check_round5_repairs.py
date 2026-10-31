"""Learner-leak, current coverage, arithmetic and source regressions."""
import json,re,math,sys,xml.etree.ElementTree as ET
from pathlib import Path
from round5_content import NEW
from round5_mc import WRONG
from demand_accounting import load_decisions,recall_credit
W=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text());cards=[];allitems=[];parts=[];copies=[];answercopies=[]
for t in range(1,13):
 items=read(W/f'topics/{t}/learning-items/topic_{t}_items.json')['items'];allitems+=items
 txt='\n'.join(b['text'] for p in (W/f'topics/{t}/content-units').glob('*.json') for b in read(p)['blocks'])
 for x in items:
  if x['item_type']=='flashcard':
   cards.append(x)
   if x['prompt'] in txt:copies.append(x['item_id'])
   if x['canonical_answer'] in txt:answercopies.append(x['item_id'])
   assert x['item_id'].endswith('-'+x['subtype']),x['item_id']
 parts+=read(W/f'topics/{t}/authored_assessment_parts.json')['parts']
assert not copies,copies
pmap={p['task_id']+':'+p['part']:p for p in parts};imap={x['item_id']:x for x in allitems}
assert 'DATA-12' not in pmap['ITEM-6117-12-P01:a']['prompt']
assert '80 °C' not in pmap['ITEM-6117-12-P01:d']['prompt'] and '100 cm' not in pmap['ITEM-6117-12-P01:d']['prompt']
assert 'VIS-6117-12-03' not in imap['ITEM-6117-12-P01']['prompt']
assert all(s not in pmap['ITEM-6117-7-P03:b']['prompt'] for s in ['black solid remains','blue crystals'])
assert '2.4' not in pmap['ITEM-6117-10-P03:c']['prompt'] and '8.0' not in pmap['ITEM-6117-10-P03:c']['prompt']
x=imap['ITEM-6117-2-P03'];assert 'VIS-6117-2-01' not in x['prompt'];assert 'ammeter' in x['prompt'] and 'indicator' not in x['prompt'];assert any(o.startswith('OBJ-6117-2.') for o in x['objective_ids'])
for t,f,forbidden in [(11,'VIS-6117-11-04-learner.svg',['Comparison tube','soap solution','Stand and clamp']),(12,'VIS-6117-12-03-learner.svg',['100 cm','Equal jacket','80 °C','no glass contact']),(6,'VIS-6117-6-02.svg',['Chips (slow)','Powder (fast)'])]:
 txt=' '.join(ET.parse(W/f'topics/{t}/visuals/{f}').getroot().itertext())
 assert not any(s in txt for s in forbidden),(f,forbidden)
# Independent arithmetic from new stimulus quantities, not the authoring functions.
numbers={'chlorine_mean':(35*.76+37*.24,35.48),'alumina_Mr':(2*27+3*16,102),'alumina_moles':(5.40/102,.05294117647058824),'molecules':(.0250*6.022e23,1.5055e22),'mass_concentration':(7.5/(250/1000),30),'acid_concentration':((.160*.025/2)/.020,.100),'activation_energy':(95-40,55),'enthalpy':(15-40,-25),'air_nitrogen':(.78*500,390),'air_oxygen':(.21*500,105),'air_other':(.01*500,5),'precision_mean':((12.1+12.3)/2,12.2),'systematic_offset':(6.20-6.00,.20),'water_deficit':(100-80,20),'aquifer_deficit':(6-4,2)}
for label,(a,b) in numbers.items():assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10),label
# Re-open the exact syllabus pages for the two extraction omissions and contested wording.
from pypdf import PdfReader
sy=PdfReader(W.parents[1]/'Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Chemistry_syllabus.pdf')
source_checks={37:['chemical test for the presence of water','anhydrous copper(II) sulfate'],32:['fuel for ships and home heating systems','lubricating fraction for lubricants, waxes and polishes'],38:['process of desalination of sea water is','not a solution to water scarcity problem in Namibia']}
for page,terms in source_checks.items():
 text=' '.join(sy.pages[page-1].extract_text().split())
 for term in terms:assert term in text,(page,term)
decisions=load_decisions();recall=sum(recall_credit(x,decisions) for x in cards+parts);marks=sum(x['mark_tariff'] for x in cards+parts)
assert len(cards)==808 and len(allitems)==844 and len(parts)==236
assert (recall,marks)==(392,1637)
report={'status':'pass','cards':len(cards),'activities':len(allitems)-len(cards),'new_cards':len(NEW),'mc_questions_with_revised_distractors':len(WRONG),'verbatim_card_prompts_in_notes':copies,'verbatim_answers_in_notes':len(answercopies),'answer_overlap_note':'Short factual statements may be taught in notes. Assessment prompts and scoring blocks are not reproduced.','subtype_suffix_mismatches':0,'numeric_recomputations':{k:a for k,(a,b) in numbers.items()},'syllabus_PDF_viewer_pages_verified':list(source_checks),'recall_marks':recall,'marks':marks,'recall_percent':100*recall/marks,'limits':'Author regression checks and source reads; not independent approval of every revised card, distractor, note or visual.'}
(W/'planning/round5-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
