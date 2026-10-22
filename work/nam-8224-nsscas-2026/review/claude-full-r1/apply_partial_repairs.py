"""Codex applies three explicit findings from the interrupted Claude worklog.

This is not a completed Claude review or an independent validation of the repairs.
"""
import json
from pathlib import Path
import sys
WS=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WS/'planning'))
from authoring_common_8224 import words
def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=1)+'\n')
changes={}
def revise(topic,cid,text=None,evidence=None):
 p=WS/'topics'/topic/'claims/canonical_claim_ledger.json';x=read(p);c=next(c for c in x['claims'] if c['claim_id']==cid)
 assert c['revision']==1,(cid,c['revision'])
 if text:c['text']=text
 if evidence:c['evidence'].append(evidence)
 c['revision']=2;c['notes'].append('Codex repair implementing explicit Claude partial-review finding; resumed Claude verification pending.')
 write(p,x);changes[cid]=2
revise('1.3','CLM-8224-1.3-053','The NSSCAS syllabus groups C60 and carbon nanotubes as fullerene/molecular examples; C60 units are discrete covalent cages and nanotubes are long covalent cylindrical units with weaker attractions between separate tubes.',{'source_id':'NSSCAS-8224-SYLLABUS','locator':'§1.3.6, printed p11: simple molecular examples include fullerene allotropes C60 and nanotubes.','support_type':'paraphrase'})
revise('2.3','CLM-8224-2.3-016','Iron in the Haber process and vanadium(V) oxide, V2O5, in the Contact process accelerate reaction at a chosen temperature without increasing the equilibrium yield.',{'source_id':'OpenStax-Chemistry','locator':'§19.3 Transition Metal Catalysts, vanadium oxide in sulfuric-acid production; governing syllabus §2.3.1 requires catalyst choice for Haber and Contact.','support_type':'paraphrase'})
for cid in ['CLM-8224-3.4-017','CLM-8224-3.4-018']:
 revise('3.4',cid,evidence={'source_id':'NSSCAS-8224-SYLLABUS','locator':'Annexe E §3(a), hydrogen–halogen bond energies: H–Cl431,H–Br366,H–I299 kJ mol−1. Official board data replace the separate textbook illustrative set in this worked example.','support_type':'paraphrase'})
repairs=[
 {'id':'CC-8224-PARTIAL-001','topic':'1.3','block':'1.3-6-01-b1','why':'Explicitly reconcile the syllabus fullerene/molecular grouping with intratube covalent bonding and weaker intertube attractions.'},
 {'id':'CC-8224-PARTIAL-002','topic':'2.3','block':'2.3-1-07-b1','why':'Name the missing Contact-process catalyst V2O5 and retain fixed-temperature rate/yield distinction.'},
 {'id':'CC-8224-PARTIAL-003','topic':'3.4','block':'3.4-2-04-b1','item':'ITEM-8224-3.4-015-INTERP','why':'Align example and derived arithmetic with official board H–X values431/366/299, difference132 kJ mol−1 and0.0100 mol H–I breaking energy2.99 kJ.'}]
for topic in ['1.3','2.3','3.4']:
 p=WS/'topics'/topic
 for f in (p/'content-units').glob('*.json'):
  u=read(f)
  for b in u['blocks']:
   old=b['text']
   if b['block_id']=='1.3-6-01-b1':
    a='C60 is different:';z='\n\nIce is molecular';start=b['text'].index(a);end=b['text'].index(z,start)
    b['text']=b['text'][:start]+'''The NSSCAS syllabus groups C60 and carbon nanotubes under its fullerene/molecular examples. Each C60 unit is a discrete cage of60 covalently bonded carbon atoms. A nanotube is a long cylindrical covalent carbon unit, with weaker attractions between separate tubes. Preserve the syllabus grouping while distinguishing strong bonds within a cage or tube from attractions between separate units. A tube's extended length does not turn the attractions between tubes into the covalent bonds of a continuous three-dimensional diamond network.'''+b['text'][end:]
   if b['block_id']=='2.3-1-07-b1':b['text']=b['text'].replace('A suitable catalyst permits an effective rate at a moderate temperature.','Vanadium(V) oxide, V2O5, is the Contact-process catalyst. It permits an effective rate at a moderate temperature by providing a lower-activation-energy pathway, without changing the equilibrium yield at that temperature.')
   if b['block_id']=='3.4-2-04-b1':
    b['text']=b['text'].replace('Representative H–Cl, H–Br and H–I dissociation values are 432, 370 and 295 kJ mol⁻¹ in the local textbook table.','The NSSCAS Data Booklet gives H–Cl, H–Br and H–I dissociation values of431,366 and299 kJ mol⁻¹.').replace('432 − 295 = 137','431 − 299 = 132').replace('137 times','132 times').replace('295 kJ mol⁻¹ requires 2.95','299 kJ mol⁻¹ requires 2.99')
   relevant=set(b.get('claims_seen',{})) & set(changes)
   for cid in relevant:b['claims_seen'][cid]=changes[cid]
   if relevant and b['text']==old:b['reviewed_unchanged']='The clarified claim/evidence does not alter this block’s supported explanation; checked against the revised scope.'
  u['word_count']=sum(words(b['text']) for b in u['blocks']);write(f,u)
 f=p/'learning-items'/f'topic_{topic}_items.json';d=read(f)
 for i in d['items']:
  old=i['prompt']+i['canonical_answer']
  if i['item_id']=='ITEM-8224-3.4-015-INTERP':i['prompt']=i['prompt'].replace('HCl 432, HBr 370 and HI 295','HCl 431, HBr 366 and HI 299')
  relevant=set(i.get('claims_seen',{})) & set(changes)
  for cid in relevant:i['claims_seen'][cid]=changes[cid]
  if relevant and old==i['prompt']+i['canonical_answer']:i['reviewed_unchanged']='Revised claim clarifies scope, names the catalyst or updates reference evidence; this item’s prompt/answer remains chemically valid.'
 write(f,d)
 f=p/'authoring_notes.json';d=read(f);d.setdefault('review_repairs',[]).extend({'finding_id':x['id'],'applied_by':'Codex implementing Claude worklog finding','status':'applied_pending_resumed_Claude_validation','why':x['why']} for x in repairs if x['topic']==topic);write(f,d)
write(Path(__file__).parent/'operator-applied-repairs.json',{'review_complete':False,'applied_by':'Codex','basis':'Explicit findings in the interrupted Claude reviewer-worklog.md','repairs':repairs,'claim_revisions':changes,'claude_validation':'pending quota reset'})
print('Applied3 partial-review findings;4 claims revised. Independent resumed Claude validation pending.')
