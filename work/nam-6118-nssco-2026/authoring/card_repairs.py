"""Per-card authored criteria and prose edits, separate from model answers."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
def records(name):
 out={};t=None
 for line in (HERE/name).read_text().splitlines():
  if line.startswith('['):t=int(line[1:-1]);out[t]={}
  elif line.strip():
   n,text=line.split(':',1);out[t][int(n)]=text.strip()
 return out
def apply(A):
 t=int(A.t);credits=records('credit-points.txt')[t];answers=records('answer-repairs.txt').get(t,{})
 for s in A.wo['item_slots']:
  n=int(s['slot'].split('-')[-2]);base=A.miscons[s['misconception_entry']] if s['subtype']=='MISCON' else A.data[s['objective_id']]
  override=getattr(A,'slot_overrides',{}).get(s['slot'])
  target=override if override is not None else base
  if n in answers:target['answer']=answers[n]
  ans=target.get('answer',base['answer'])
  if s['subtype']=='CALC':
   from review_followup import calculations
   g=calculations()[s['slot']]
  else:
   parts=credits[n].split(' | ');marks=s['mark_tariff'];assert len(parts)==marks,(t,n,marks,parts)
   g=[f'Credit {k+1} (1): '+p[0].upper()+p[1:]+'.' for k,p in enumerate(parts)]
   if marks>1:g.append(f'Maximum {marks} marks. Accept equivalent scientifically correct wording or a labelled representation of the same points. Count each distinct idea once; an unsupported keyword alone is not a causal explanation.')
  target['guidance']=g
 # Specific short prompts align one-mark method cards with a single observable outcome.
 narrowed={13:{14:'Describe the junction feature that lets a thermocouple respond rapidly.'},14:{7:'Describe the measurements and relation needed to estimate a block’s specific heat capacity.',8:'Describe the controlled comparison needed to test temperature rise against reciprocal mass.'},8:{6:'Describe the comparison that tests the principle of moments in a balanced beam.',8:'Describe how two suspension lines locate a card’s centre of mass.'},24:{25:'Describe one final safety check on the unplugged training plug model.'}}
 for n,prompt in narrowed.get(t,{}).items():
  s=next(s for s in A.wo['item_slots'] if int(s['slot'].split('-')[-2])==n);A.data[s['objective_id']]['prompt']=prompt
 # Remove copied long definition phrasing in all learner-facing prose, not only cards.
 for v in list(A.data.values())+list(A.miscons.values()):
  for key in ('core','detail','teach'):
   v[key]=v[key].replace('The total momentum of a system remains unchanged when its external resultant force is zero','A system retains its signed total momentum if the net external impulse is zero').replace('energy supplied by a source per unit charge','source energy contribution to each coulomb').replace('energy required to raise the temperature of 1 kg of a substance by one kelvin','energy for each kilogram to warm by one kelvin').replace('magnetic dipoles or dipoles','atomic magnetic effects').replace('turning effect of separated opposite forces','turning effect of opposite forces at separate positions')

def rubric_policy(sub):
 return {'DEF':'Accept an equivalent definition, equation or named relation only when its stated conditions are met.',
 'FEATURE':'Accept an equivalent scientific name, property, unit or fact answering the requested feature; do not award unrelated facts.',
 'DIST':'Credit the contrast on the same basis for both cases; repeating one side does not establish the difference.',
 'PROC':'Credit the requested action; unrelated procedural detail does not earn an extra mark.',
 'MECH':'Credit a linked physical process and its effect; a cause named without the requested consequence is incomplete.',
 'SYNTH':'The link must include a reason or result connecting the stated ideas; unrelated facts do not earn explanation credit.',
 'INTERP':'Accept an equivalent correctly labelled graph or diagram; the requested scale, point placement, direction or gradient feature must remain clear.',
 'MISCON':'Identify the error or confusion and give the correct replacement account. Do not credit agreement with the incorrect premise.',
 'CALC':'Accept an equivalent equation and numerical substitution/working. The answer must use compatible units; apply the stated method and follow-through rules.'}.get(sub,'')
