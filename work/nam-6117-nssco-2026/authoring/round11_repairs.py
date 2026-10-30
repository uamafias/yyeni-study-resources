"""Repairs following independent full-bank review, 30 October 2026."""
import copy,re
from final_method_examples import EXTRA4
DATA3='''Two cleaning products are tested: S is soap and D is a soapless detergent. Equal water portions at the same temperature are used, with a fixed cleaning endpoint and unchanged product concentrations. S forms scum in hard water; D forms no visible precipitate in this trial.

| Product | Volume needed in soft water / cm³ | Volume needed in hard water / cm³ |
|---|---:|---:|
| S | 2 | 8 |
| D | 2 | 2 |

A separate seven-day microbial breakdown test uses the same controlled conditions for both products. No toxicity measurements are available.

| Product | Initial mass / g | Mass remaining after seven days / g |
|---|---:|---:|
| S | 5.0 | 1.0 |
| D | 5.0 | 4.0 |'''
DATA6='''Two samples of the same carbonate react with excess acid at the same temperature and acid concentration. The limiting carbonate masses are equal. The curves are labelled A and B; no particle-size identity is assigned to either curve.

| Time / s | 0 | 20 | 40 | 60 | 80 | 100 | 120 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Curve A: CO2 volume / cm³ | 0 | 18 | 30 | 38 | 43 | 46 | 48 |
| Curve B: CO2 volume / cm³ | 0 | 28 | 41 | 47 | 48 | 48 | 48 |

Later readings confirm that both volumes remain at 48 cm³.'''
FRACTION=['The molecules in a fraction do not all have identical chain lengths.','Different refinery operations can produce somewhat different mixtures while retaining the same broad fraction name.']
SHAPES=['A correct formula does not by itself guarantee a correct shape drawing.','Use an explicit legend for a three-dimensional drawing.','Bond angles need not be invented when the task asks only for the shape name.']

def clean_text(s):
 replacements={'this original supplied record':'this record','these original results':'these results','these original data':'these data','original synthetic dataset':'dataset','Original synthetic gas data:':'Gas measurements:','an original synthetic classroom dataset':'a classroom observation record','synthetic practice data, not universal values':'results for these test conditions, not universal values','its original teaching box':'the relevant practical method','The original equation C6H12O6':'The equation C6H12O6','after after':'after','10⁻9':'10⁻⁹','used for a chemical feedstock':'used as a chemical feedstock','used for fuel for':'used as fuel for'}
 for a,b in replacements.items():s=s.replace(a,b)
 s=s.replace('These labelled diagrams are answer and teaching references; attempt drawing tasks before consulting them.','')
 s=s.replace('This consolidation chapter organises the syllabus practical skills rather than adding a twelfth content topic to the official eleven; the linked practical index points back to all 55 suggested experiences in their teaching contexts.','Use the practical index to find a method, its measurements and the evidence needed for a conclusion.')
 return s.strip()

def card(x,key):
 for field in ['prompt','canonical_answer']:x[field]=clean_text(x[field])
 x['marking_guidance']=[clean_text(g) for g in x['marking_guidance']]
 if key=='6-017':
  x['prompt']='State the name of the sugar produced during photosynthesis.';x['canonical_answer']='Glucose.';x['marking_guidance']=['Glucose (1).'];x['command_word']='State'
 if key=='9-044':
  x['prompt']='Name one use of copper that depends on its electrical conductivity.';x['canonical_answer']='Electrical wiring.';x['marking_guidance']=['Electrical wiring or another specific copper conductor, such as an electrical contact (1).']
 if key=='9-023':x['canonical_answer']='X fits oxygen blowing into molten iron: oxidation removes excess carbon and releases heat. Y fits the electric-arc furnace: the available electrical supply melts its solid scrap.'
 if key=='10-082':
  x['canonical_answer']='Reducing friction between moving machine parts; making waxes or surface polishes.'
  x['marking_guidance']=['First distinct use: reducing friction between moving parts, making waxes, or making surface polishes (1).','Second different use from reducing friction between moving parts, making waxes, or making surface polishes; do not credit the same use twice (1).']
 if key=='10-033':x['prompt']=x['prompt'].replace('Describe what follows','Deduce what follows',1);x['command_word']='Deduce'
 if key=='6-002':x['marking_guidance']=['Physical change, justified by H2O remaining the same substance with no new substance formed; both classification and evidence required (1).']
 for pair,group in [(('6-053','6-054'),'CHEM-hydration-reversibility'),(('7-021','7-022'),'CHEM-weak-acid-conduction'),(('7-043','7-044'),'CHEM-carbon-dioxide-limewater')]:
  if key in pair:x['intentional_duplicate_group']=group
 if key.startswith('1-') and re.search(r'offset|zero error|zero-error',x['prompt'],re.I):x['intentional_duplicate_group']='CHEM-additive-offset-transfer'

def part(p,t):
 for f in ['prompt','canonical_answer']:p[f]=clean_text(p[f])
 p['marking_guidance']=[clean_text(g) for g in p['marking_guidance']]
 task=p['task_id'];label=p['part']
 if task in ['ITEM-6117-3-P02','ITEM-6117-7-P02','ITEM-6117-11-P02']:
  p['part']=chr(ord('a')+int(label.rsplit('-',1)[1])-1)
 if task=='ITEM-6117-11-P02' and p['part']=='b':
  p['canonical_answer']='Remove the suspended calcium carbonate by filtration to obtain clear treated water rather than leaving solid particles in it. Before precipitation, dissolved calcium ions pass through ordinary filter paper, so filtration alone does not soften the water.'
  p['marking_guidance']=['Remove the suspended calcium carbonate so the treated water is free of that solid precipitate (1).','Before precipitation, dissolved calcium ions pass through filter paper, so filtration alone leaves the hardness ions in solution (1).']
 if task=='ITEM-6117-6-P02':
  if label=='b':p['prompt']='Describe two shared features of Curve A and Curve B in the table and graph.'
  if label=='d':
   p['prompt']='Compare the average gas-production rates of Curve B and Curve A during the first 20 s.'
   p['canonical_answer']='Curve B is faster over the first 20 s: 28/20 = 1.4 cm³/s, compared with 18/20 = 0.9 cm³/s for Curve A.'
   p['marking_guidance']=['Curve B faster, justified by 28 versus 18 cm³ in the same 20 s or 1.4 versus 0.9 cm³/s (1).']
 if task=='ITEM-6117-6-P03' and label=='c':p['canonical_answer']='A gas syringe with a freely moving plunger. Alternatively, collect the gas over water in an inverted, water-filled graduated cylinder using a suitable delivery tube; carbon dioxide dissolves partly in water, so this alternative can underestimate the collected volume.'
 if task=='ITEM-6117-8-P03':
  if label=='a':p['prompt']='Complete the table for portion A.\n\n| Feature | Result |\n|---|---|\n| Initial appearance after adding NaOH | ______ |\n| Behaviour after adding excess NaOH | ______ |\n| Physical state of the coloured material | ______ |'
  if label=='e':p['prompt']='Explain why the tests do not establish that X contains only the ions you identified, and give one improvement to the strength of the identification evidence.'
 if task=='ITEM-6117-12-P01' and label=='a':p['canonical_answer']=p['canonical_answer'].replace(' The answer panel is separate from the blank learner grid.','')
 if task=='ITEM-6117-12-P01' and label=='d':
  p['canonical_answer']='Use identical vessels with equal water volumes and the same starting temperature. Fit equal-thickness jackets of the two materials with the same covered area and identical lids. Keep ambient conditions the same, including draught exposure. Position thermometer bulbs in the water without touching glass and record temperatures at fixed time intervals. Repeat each arrangement and compare mean cooling curves or temperature drops over the same interval; the smaller drop indicates better insulation under these conditions.\n\nPractical safety advice (unassessed): the teacher supplies the hot water; place vessels on heatproof mats and handle them to avoid burns.'
  p['prompt']=p['prompt'].replace(' Include safe handling of hot water.','')
  p['marking_guidance']=[g.replace('Safety and a sensible prediction are expected supporting plan details; no invented extra marks.','The safe handling described in the model answer is unassessed practical advice; the six marks above exhaust the allocation.') for g in p['marking_guidance']]

def whole(x,t):
 if x['item_id']=='ITEM-6117-3-P02':x['prompt']=DATA3+'\n\n'+x['prompt'];x['context']['facts']=['S: soft 2 cm³; hard 8 cm³; scum forms.','D: soft 2 cm³; hard 2 cm³; no precipitate.','Microbial test, seven days: S 5.0 g to 1.0 g; D 5.0 g to 4.0 g.']
 if x['item_id']=='ITEM-6117-6-P02':x['prompt']=DATA6+'\n\n'+x['prompt']+'\n\n![Gas-production curves](visuals/VIS-6117-6-02.svg)'


def notes(t,units):
 seen=set();conn_seen=False
 for u in sorted(units,key=lambda u:tuple(map(int,u['unit_id'].removeprefix('CU-6117-').split('.')))):
  kept=[]
  for b in u['blocks']:
   b['text']=clean_text(b['text'])
   if t in [2,10]:
    for sentence in (SHAPES if t==2 else FRACTION):
     if sentence in b['text']:
      if sentence in seen:b['text']=b['text'].replace(sentence,'').replace('  ',' ')
      seen.add(sentence)
   if t==3 and b['heading']=='Connections':
    if conn_seen:
     assert not b['claim_ids'];continue
    conn_seen=True
   if t==9 and b['heading']=='Connections':
    if conn_seen:
     assert not b['claim_ids'];continue
    conn_seen=True;b['heading']='Linking properties, structure and reactions'
   b['text']=re.sub(r'[ \t]+(?=\n\n|$)','',b['text']).strip()
   kept.append(b)
  u['blocks']=kept
 if t==2:
  source=next(b for u in units for b in u['blocks'] if b['heading']=='Atoms, ionic diagrams and isotope calculations')
  paras=source['text'].split('\n\n');group=[p for p in paras if p.startswith('Group I metals react')]
  assert len(group)==1
  source['text']='\n\n'.join(p for p in paras if p not in group)
  destination=next(b for u in units for b in u['blocks'] if b['heading']=='Soluble Group I hydroxides')
  destination['text']+='\n\n'+group[0]
 if t==9:
  u=next(u for u in units if u['unit_id']=='CU-6117-9.3');b=next(b for b in u['blocks'] if b['heading']=='Blast furnace chemistry');u['blocks'].remove(b)
  i=next(i for i,z in enumerate(u['blocks']) if z['heading']=='Iron in the blast furnace');u['blocks'].insert(i+1,b)
 if t==4:
  u=next(u for u in units if u['unit_id']=='CU-6117-4.2');model=next(b for b in u['blocks'] if b['block_id'].endswith('FINAL-METHOD'))
  # The titration method stays by solution stoichiometry; other examples follow their concepts.
  paragraphs=model['text'].split('\n\n');assert len(paragraphs)==4
  model['text']='\n\n'.join(paragraphs[:2])
  chunks=[('BURETTE','Reading a titre and controlling the endpoint','Titration apparatus reference','\n\n'.join(paragraphs[2:]))]
  for ident,title,anchor,text in zip(['LIMIT','FORMULA','YIELD'],['Limiting reagent, excess metal and gas volume','Empirical and molecular formulae','Percentage yield'],['Gas volume at room conditions','Molecular formula from an empirical formula','Percentage yield'],EXTRA4.split('\n\n')):chunks.append((ident,title,anchor,text))
  for ident,title,anchor,text in chunks:
   b=copy.deepcopy(model);b.update(block_id=model['block_id']+'-'+ident,heading='Worked example: '+title[0].lower()+title[1:],text=text)
   i=next(i for i,z in enumerate(u['blocks']) if z['heading']==anchor);u['blocks'].insert(i+1,b)
