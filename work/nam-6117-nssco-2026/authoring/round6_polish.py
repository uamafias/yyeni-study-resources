"""Learner wording repairs; assessment tariffs and accepted chemistry are unchanged."""
import re
from round9_repairs import learner_text
PROMPTS={
 '1-049':'State how to correct a balance that reads +0.30 g when its pan is empty, before measuring a sample.',
 '1-051':'State the apparatus suited to delivering a measured volume that must be varied drop by drop to reach a titration end-point.',
 '1-066':'State which component is collected first when a mixture of miscible liquids is fractionally distilled.',
 '1-070':'State the apparatus needed to record gas volume at timed intervals during a reaction.',
 '3-016':'Suggest an example of a synthetic polymer.',
 '3-033':'Identify the cleaning-agent class that forms insoluble scum with calcium ions in hard water.',
 '8-004':'State the ion indicated by a white precipitate that dissolves in excess NaOH but remains insoluble in excess aqueous ammonia on a fresh portion.',
 '8-006':'State the ion indicated by white precipitates that dissolve in excess NaOH and in excess aqueous ammonia on separate portions.',
 '8-008':'State the ion indicated by a brick-red flame and a white precipitate insoluble in excess NaOH.',
 '8-012':'State the iron ion indicated by a freshly formed green precipitate insoluble in excess NaOH.',
 '12-014':'State the apparatus needed to measure the variable volume of acid delivered drop by drop to an end-point.',
 '2-121':'State the relative strength of covalent bonds within small molecules and forces between the molecules.',
 '9-011':'State the usual chemical form in which metals occur in their ores.',
}
def clean_text(s):
 s=s.replace('Explain these supplied observations from an measurements:', 'Explain these observations:')
 s=s.replace('the original DATA-10 example','the chromatography example')
 s=s.replace('Original DATA-11','Soap-test diagram')
 s=s.replace('For DATA-12,','For the cooling experiment,')
 s=s.replace('original DATA-12 answer curves','cooling answer curves')
 s=s.replace('Original DATA-10 with ruler','Chromatography diagram with ruler')
 s=re.sub(r'\b(?:[Oo]riginal )?DATA-12\b','cooling measurements',s)
 s=re.sub(r'\b(?:[Oo]riginal )?DATA-10\b','chromatography measurements',s)
 s=s.replace('Accept scientifically equivalent wording.','').replace('Accept scientifically equivalent wording','')
 return learner_text(s).strip()
def clean(obj):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if k in ['prompt','canonical_answer','text','heading','brief','credit_requirement'] and isinstance(v,str):obj[k]=clean_text(v)
   elif k in ['marking_guidance','marking_guidance_must_name','credit_points'] and isinstance(v,list):obj[k]=[clean_text(x) if isinstance(x,str) else x for x in v]
   else:clean(v)
 elif isinstance(obj,list):
  for x in obj:clean(x)
def card(x,key):
 if key in PROMPTS:x['prompt']=PROMPTS[key]
 if key=='3-016':
  x['canonical_answer']='For example, nylon. Other valid examples include poly(ethene), poly(propene) and polyester.'
  x['marking_guidance']=['One valid synthetic polymer, such as nylon, poly(ethene), poly(propene) or polyester (1). Do not credit cellulose or starch.']
 clean(x)
def part(x):
 if x['task_id']=='ITEM-6117-6-P02':
  for f in ['prompt','canonical_answer']:
   if x['part']=='b':x[f]=x[f].replace('chip and powder gas-volume curves','Curve A and Curve B').replace('Chip CO2','Curve A CO2').replace('Powder CO2','Curve B CO2')
   if x['part']=='d':x[f]=x[f].replace('powder and chips','Curve B and Curve A').replace('Chip CO2','Curve A CO2').replace('Powder CO2','Curve B CO2').replace('Powder is initially faster','Curve B is initially faster')
 clean(x)
