"""Final reviewer follow-up: literal source fixes with regression assertions."""
import re
from mc_distractor_reasons import apply as mc_feedback

def card(x,key):
 if key in ['10-028','10-045']:x['prompt']=re.sub(r'^Suggest ', 'State ',x['prompt']);x['command_word']='State'
 if key=='11-003':
  x['prompt']='Discuss whether these records are sufficient to choose a secure water source: dam X loses 25% of storage each dry season with no dry-season inflow; aquifer Y has annual recharge 4 million m³ and proposed abstraction 6 million m³. Identify the risk for each source and the further evidence needed.'
 if key=='9-015':
  x['prompt']='A zinc-oxide feed can be processed in a thermal-reduction plant costing N$8 per kg of zinc or an electrolysis plant costing N$20 per kg. Explain which chemically suitable route you would select on these processing costs.'
  x['canonical_answer']='Choose thermal reduction with carbon: zinc can be reduced from its oxide by carbon, and the stated processing cost is N$12 per kg lower than electrolysis.'
  x['marking_guidance']=['Thermal/carbon reduction, justified both by carbon being able to reduce zinc oxide and by its lower stated cost (N$8 versus N$20 per kg, or N$12 per kg less); all links required (1).']

def part(p,t):
 if p['task_id'].endswith('P01') and t<12:
  if t==11 and p['part']=='3':p['prompt']=p['prompt'].replace('D. Calcium ions become removable by filtration','D. Dissolved calcium ions are trapped directly by filter paper')
  mc_feedback(p,t)

ANCHORS={1:'Measurement precision and significant figures',2:'The ionic lattice and conduction',3:'Selecting by properties',4:'Solutions and reacting amounts',5:'Copper sulfate: active and inert anodes',6:'Interpreting rate data',7:'Selecting starting materials',8:'Zinc ions',9:'Reactivity determines extraction route',10:'Chromatography of hydrolysis products',11:'Boiling and scale',12:'Planning a fair investigation'}
FRACTION_SENTENCES=['To answer a one-mark use question, give one precise accepted use, then stop.','Compare neighbouring fractions by their broad boiling ranges and molecule sizes without inventing fixed values.']
def notes(t,units):
 counts={s:0 for s in FRACTION_SENTENCES}
 for u in sorted(units,key=lambda u:tuple(map(int,u['unit_id'].removeprefix('CU-6117-').split('.')))):
  for b in u['blocks']:
   # Only authoring labels; retain chemically meaningful 'original sample/mixture'.
   b['text']=re.sub(r'\boriginal (?=(?:practice|illustrative|example|results|cooling results|timed gas data|data|chip and powder data)\b)','',b['text'],flags=re.I)
   b['text']=b['text'].replace('An practice','A practice').replace('an practice','a practice')
   b['text']=re.sub(r'(^|(?<=[.!?])\s+)(practice data|illustrative data|example volumes|results|cooling results|timed gas data|data|chip and powder data)',lambda m:m[1]+m[2][0].upper()+m[2][1:],b['text'])
   if t==10:
    for sentence in FRACTION_SENTENCES:
     if sentence in b['text']:
      counts[sentence]+=1
      if counts[sentence]>1:b['text']=b['text'].replace(sentence,'').replace('  ',' ')
  # Supplemental teaching precedes exercises and Connections, never trails the summary.
  supplements=[b for b in u['blocks'] if b['block_id'].endswith('-R5')]
  for b in supplements:
   u['blocks'].remove(b)
   pos=next((i for i,z in enumerate(u['blocks']) if z['block_type'] in ['practice_guidance','cross_link']),len(u['blocks']))
   if t==4:pos=0
   u['blocks'].insert(pos,b)
  methods=[b for b in u['blocks'] if b['block_id'].endswith('FINAL-METHOD')]
  for b in methods:
   u['blocks'].remove(b);b['heading']='Worked example: '+b['heading'][0].lower()+b['heading'][1:]
   pos=next(i for i,z in enumerate(u['blocks']) if z['heading']==ANCHORS[t]);u['blocks'].insert(pos+1,b)
 return counts
