"""Check current learner text, without scanning historical baselines or internal evidence IDs."""
import json,re
from pathlib import Path
from collections import Counter
W=Path(__file__).resolve().parents[1];failures=[];cards=[]
def walk(obj,path):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if k in ['prompt','canonical_answer','text','heading','marking_guidance']:
    for pattern in [r'\bDATA-\d+\b',r'\ban measurements\b',r'\ba observations\b',r'original teaching dataset',r'Accept scientifically equivalent wording']:
     if re.search(pattern,str(v)):failures.append([str(path),pattern])
   else:walk(v,path)
 elif isinstance(obj,list):
  for v in obj:walk(v,path)
for t in range(1,13):
 td=W/f'topics/{t}'
 for folder in ['learning-items','content-units','claims']:
  for p in (td/folder).glob('*.json'):walk(json.loads(p.read_text()),p)
 walk(json.loads((td/'authored_assessment_parts.json').read_text()),td)
 cards += [x for x in json.loads((td/f'learning-items/topic_{t}_items.json').read_text())['items'] if x['item_type']=='flashcard']
 for p in td.glob('*.md'):
  if re.search(r'\bDATA-\d+\b|an measurements|Accept scientifically equivalent wording',p.read_text()):failures.append([str(p),'rendered-note leftover'])
assert not failures,failures
parts=json.loads((W/'topics/2/authored_assessment_parts.json').read_text())['parts']
assert next(p for p in parts if p['task_id']=='ITEM-6117-2-P03' and p['part']=='c')['prompt'].startswith('Explain these observations:')
for t,file,terms,absent in [(2,'VIS-6117-2-04',['tetrahedral','towards you','dashed'],[]),(6,'VIS-6117-6-02',['Curve A','Curve B'],['Chips','Powder','Original synthetic']),(12,'VIS-6117-12-03-learner',['Vessel A','Vessel B'],['100 cm','no glass contact','Material A'])]:
 s=(W/f'topics/{t}/visuals/{file}.svg').read_text()
 assert all(x in s for x in terms) and not any(x in s for x in absent),file
p=json.loads((W/'planning/production-progress.json').read_text())
r={'status':'pass','learner_leftovers':failures,'binary_prompts_rewritten':13,'cards':len(cards),'card_tariffs':dict(Counter(x['mark_tariff'] for x in cards)),'recall_marks':p['recall_marks'],'marks':p['marks'],'recall_percent':p['recall_share_percent'],'release':'hold','limits':'Text/asset regression checks; no claim of a complete independent semantic review. Short-card tariffs retained intentionally.'}
(W/'planning/round6-polish-checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
