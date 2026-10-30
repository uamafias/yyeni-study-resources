"""Remove answer-only blocks and build real teaching examples and traceable claims."""
import copy,re
from final_method_examples import EXAMPLES,EXTRA4
from round10_repairs import notes as round10_notes
from round11_repairs import notes as round11_notes
PRINCIPLES={
'12.1-01':'Read a scale at eye level using its divisions; a meniscus reading describes the liquid level, and reported precision must match the instrument.',
'12.2-01':'Choose the operation and instrument to match the measured quantity; keep sample identity clear and use separate clean portions when reagents could interfere.',
'12.2-02':'Record quantities and units in table headings and calculate changes by final reading minus initial reading before calculating a rate or ratio.',
'12.2-03':'An apparatus diagram needs labelled components, correct connections and the positions that affect the measurement; artistic perspective is unnecessary.',
'12.3-01':'A conclusion should name the observed change and its comparison or control, rather than substituting a remembered expectation for evidence.',
'12.3-02':'An observation can support an identification without proving purity; shared observations require another discriminating test.',
'12.3-03':'Label graph axes with quantities and units, plot measured points on suitable scales, and distinguish an interval gradient from an instantaneous tangent gradient.',
'12.4-01':'An improvement must identify the source of error and explain how the change reduces it; repeats estimate variation but do not automatically remove a persistent bias.',
'12.5-01':'A fair investigation specifies the changed variable, measured outcome, controls, repeats, relevant precautions and the comparison used for its conclusion.'}
def rebuild(t,d,ld,units,notes,registry):
 old=[c for c in ld['claims'] if re.match(r'CLM-6117-\d+-P',c['claim_id'])];obsolete={c['claim_id'] for c in old}
 removed=0
 for u in units:
  before=len(u['blocks']);u['blocks']=[b for b in u['blocks'] if not b['heading'].startswith(('Activity feedback','Activity worked example'))];removed+=before-len(u['blocks'])
  for b in u['blocks']:
   b['claim_ids']=[cid for cid in b['claim_ids'] if cid not in obsolete]
 # Activity evidence remains in item/part answer fields. It is not duplicated in learner notes.
 ld['claims']=[c for c in ld['claims'] if c['claim_id'] not in obsolete]
 sample=copy.deepcopy(ld['claims'][0]);missing=sorted({oid for x in d['items'] for oid in x['objective_ids'] if not any(oid in c['objective_ids'] for c in ld['claims'])})
 headings={o['sub_topic']:o['sub_topic_heading'] for o in registry['objectives'] if o.get('sub_topic')}
 headings.update({'12.1':'Reading scales and recording precision','12.2':'Apparatus and processing data','12.3':'Interpreting results and graphs','12.4':'Errors and improvements','12.5':'Planning investigations','12.6':'Drawing conclusions from chemical tests'})
 for u in units:
  section=u['unit_id'].removeprefix('CU-6117-');u['title']=section+' — '+headings[section]
 method_section={1:'1.4',2:'2.4.2',3:'3.2',4:'4.2',5:'5.1',6:'6.4',7:'7.4',8:'8.1',9:'9.3',10:'10.8.2',11:'11.1.2',12:'12.5'}[t]
 target=next(u for u in units if u['unit_id']=='CU-6117-'+method_section)
 overview_section={1:'1.4',2:'2.2',4:'4.2',5:'5.1',6:'6.2',7:'7.4',8:'8.1',9:'9.2',10:'10.2.1',11:'11.1.1',12:'12.4'}.get(t)
 if overview_section:
  destination=next(u for u in units if u['unit_id']=='CU-6117-'+overview_section)
  moved=[]
  for u in units:
   if u is destination:continue
   moved += [b for b in u['blocks'] if b['block_id'].endswith('-R5')]
   u['blocks']=[b for b in u['blocks'] if not b['block_id'].endswith('-R5')]
  destination['blocks']+=moved
 newclaims=[]
 for i,oid in enumerate(missing,1):
  short=oid.removeprefix('OBJ-6117-');assert short in PRINCIPLES,oid
  c=copy.deepcopy(sample);c.update(claim_id=f'CLM-6117-FINAL-{t}-{i}',objective_ids=[oid],text=PRINCIPLES[short],revision=1);ld['claims'].append(c);newclaims.append(c)
 heading,text=EXAMPLES[t]
 factual=[c for c in ld['claims'] if any(oid in target['objective_ids'] for oid in c['objective_ids'])]
 claimids=[c['claim_id'] for c in newclaims]+[c['claim_id'] for c in factual[:2]]
 target['blocks'].append({'block_id':target['unit_id']+'-FINAL-METHOD','block_type':'worked_application','heading':heading,'text':text,'claim_ids':claimids,'context_tags':[],'assessment_objectives':['A','B','C'],'claims_seen':{}})
 for c in newclaims:
  for oid in c['objective_ids']:
   if oid not in target['objective_ids']:target['objective_ids'].append(oid)
 for x in d['items']:
  if x['item_type']!='flashcard':
   x['claim_ids']=list(dict.fromkeys(c['claim_id'] for oid in x['objective_ids'] for c in ld['claims'] if oid in c['objective_ids']))
  else:x['claim_ids']=[cid for cid in x['claim_ids'] if cid not in obsolete]
 # Remove repeated long sentences, including stock exam-advice embedded inside otherwise unique paragraphs.
 seen=set();removed_sentences=0
 for u in sorted(units,key=lambda u:tuple(int(n) for n in re.findall(r'\d+',u['unit_id']))):
  for b in u['blocks']:
   if b['block_type']=='learner_objective' or '![' in b['text'] or b['block_id'].endswith('FINAL-METHOD'):continue
   paragraphs=[]
   for para in b['text'].split('\n\n'):
    keep=[]
    for sentence in re.split(r'(?<=[.!?])\s+(?=[A-Z])',para):
     norm=' '.join(sentence.split())
     if len(norm.split())>=16 and norm in seen:removed_sentences+=1;continue
     if len(norm.split())>=16:seen.add(norm)
     keep.append(sentence)
    if keep:paragraphs.append(' '.join(keep))
   b['text']='\n\n'.join(paragraphs)
 for u in units:
  for b in u['blocks']:
   if not b['text']:assert not b['claim_ids'],b['block_id']
  u['blocks']=[b for b in u['blocks'] if b['text']]
 round10_notes(t,units)
 round11_notes(t,units)
 notes.setdefault('deviations',[]).append({'from':'Answer-only activity feedback in learner notes','to':'Independent method examples, de-duplicated prose, and activity claims linked to factual teaching','why':'User instructed completion of all remaining editorial work; answer keys remain in activity records, not in the notes.'})
 return {'topic':t,'answer_blocks_removed':removed,'repeated_long_sentences_removed':removed_sentences,'new_method_claims':len(newclaims)}
