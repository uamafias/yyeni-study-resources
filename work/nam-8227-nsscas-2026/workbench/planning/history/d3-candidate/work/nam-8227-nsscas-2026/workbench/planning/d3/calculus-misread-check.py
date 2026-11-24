"""Independent D3 paper-design recomputation and manual evidence fixtures.

This audits the eight-part contract and works twelve data misreads algebraically.
It is not a runtime marker: award vectors are explicit planner expectations.
"""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction
import argparse, json, hashlib
import sympy as S
H=Path(__file__).resolve().parent;W=H.parent.parent
read=lambda p:json.loads(p.read_text())
write=lambda p,d:p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['missing-policy','double-deduction','no-accuracy-negative-total','proof-target-follow-through','back-substitution-in-S3','normal-positive-reciprocal','invalid-log-full-credit']);a=parser.parse_args()
 design=read(W/'planning/calculus-design.json'); recipes=[r for r in design['recipes']if r['recipe_id']in ['WB8227-implicit-normal','WB8227-stationary-inflexion']]
 parts=[(r,b,p)for r in recipes for b in r['branches']for p in b['part_specs']];assert len(parts)==8
 if a.negative_fixture=='missing-policy':parts[0][2].pop('misread_policy')
 for r,b,p in parts:
  assert r['version']=='0.1.3'
  assert p['classification_version']=='8227-pilot-design-0.1.1'
  assert p['answer_only_credit']==0 and p['bloom']==3
  m=p['misread_policy'];assert m['policy_id']=='OD-6','OD-6 policy absent'
  ab=[c['suffix']for c in p['criteria']if c['mark_type']in ['A','B']]
  assert m['follow_through_award_suffixes']==ab
  assert m['deduction']['amount']==1 and m['deduction']['mark_types']==['A','B']
  assert 'Earliest earned'in m['deduction']['selection'] and 'Deduct zero'in m['deduction']['if_none']
  assert all('@0.1.3:'in c['criterion_id']for c in p['criteria'])
  assert all(c in p['bloom_rationale']for c in p['bloom_criterion_ids'])
 proof=next(p for r,b,p in parts if p['part_id']=='show-derivative')
 if a.negative_fixture=='back-substitution-in-S3':proof['alternative_criterion_mapping']['S3']='Include back-substitution here.'
 assert 'No back-substitution'in proof['alternative_criterion_mapping']['S3'],'Back-substitution moved out of S4'
 assert 'back-substitution'in proof['alternative_criterion_mapping']['S4']
 x,y=S.symbols('x y',real=True);samples=[]
 for c in read(H/'calculus-case-inputs.json')['cases']:
  p=c['parameters'];branch=c['branch_id'].rsplit(':',1)[1];cid=c['case_id']
  if c['recipe_id']=='WB8227-implicit-normal':
   aa,k,q=p['a'],p['k'],p['q'];C=q*(q+aa)
   if branch=='gradient':
    kk=5-k;eq=aa*S.exp(kk*x)*y+y*y-C
    assert eq.subs({x:0,y:q})==0
    mm=S.simplify((-S.diff(eq,x)/S.diff(eq,y)).subs({x:0,y:q}));canonical=S.Rational(-aa*k*q,aa+2*q)
    assert mm!=canonical and mm!=0
    sigma=S.sign(aa+2*q);local=(-aa*S.exp(kk*x)+sigma*S.sqrt(aa*aa*S.exp(2*kk*x)+4*C))/2
    assert S.simplify(S.diff(local,x).subs(x,0)-mm)==0
    sample=dict(case_id=cid,datum='question exponent coefficient k',canonical_value=k,misread_value=kk,first_use_part_id='gradient',eligibility='Curve point remains valid; nonzero finite exponential-chain/implicit gradient task, unchanged difficulty and object.',computed=dict(gradient=str(mm),independent_local_root_derivative=str(S.diff(local,x).subs(x,0))),earned_before={'G1':1,'G2':1,'G3':1,'G4':1,'G5':1},deducted_criterion='G2',deduction=1,expected_credit=4,total=5,later_deduction=0)
   else:
    numerator=aa*k;misread=numerator+2
    # Correct proof is untouched; this later read error is isolated to the given formula.
    substituted=S.Rational(-misread*q,aa+2*q);normal=-1/substituted
    assert substituted!=S.Rational(-aa*k*q,aa+2*q) and substituted*normal==-1
    sample=dict(case_id=cid,datum='displayed derivative numerator coefficient, first misread only when applying part (b)',canonical_value=numerator,misread_value=misread,first_use_part_id='gradient',eligibility='The actual supplied proof was correctly read and proved; later numeric substitution and perpendicular-line task unchanged.',computed=dict(gradient=str(substituted),normal_slope=str(normal),normal_equation='y-('+str(q)+')=('+str(normal)+')*x'),earned_before={'S1':1,'S2':1,'S3':1,'S4':1,'H1':1,'H2':1,'N1':1,'N2':1,'N3':1},deducted_criterion='H2',deduction=1,expected_credit=8,total=9,later_deduction=0)
  else:
   aa,h,cc=p['a'],p['h'],p['c']
   f=S.expand(aa*((x-h)**3-3*p['r']**2*(x-h))+cc)if branch=='two-extrema'else S.expand(aa*(x-h)**p['power']+cc)
   # A genuine printed constant-term reading error shifts f by one, not any derivative.
   wrong=f+1;df=S.diff(wrong,x);roots=S.solve(df,x)
   points=[[int(z),int(wrong.subs(x,z))]for z in roots];types=[]
   for z in roots:
    for order in range(2,S.degree(wrong,x)+1):
     term=S.diff(wrong,x,order).subs(x,z)
     if term!=0:
      types.append('stationary inflexion'if order%2 else'minimum'if term>0 else'maximum');break
   assert S.diff(wrong,x)==S.diff(f,x)
   data=dict(points=points,classifications=types,derivative=str(df))
   if branch=='two-extrema':earned={'P1':1,'P2':1,'P3':1,'P4':1,'C1':1,'C2':1};first='points';slot='P2'
   else:earned={'I1':1,'I2':1,'I3':1,'I4':1,'I5':1,'I6':1};first='point';slot='I1'
   sample=dict(case_id=cid,datum='printed expanded polynomial constant term',canonical_value=int(f.subs(x,0)),misread_value=int(wrong.subs(x,0)),first_use_part_id=first,eligibility='Vertical constant changes by one; derivative solving and nature demands unchanged.',computed=data,earned_before=earned,deducted_criterion=slot,deduction=1,expected_credit=5,total=6,later_deduction=0)
  assert sum(sample['earned_before'].values())-sample['deduction']==sample['expected_credit']
  samples.append(sample)
 # Negative fixture targets the explicit continuation ledger, without implementing an app marker.
 if a.negative_fixture=='double-deduction':samples[0]['later_deduction']=1
 assert len(samples)==12 and all(s['later_deduction']==0 for s in samples),'A datum was charged again in a later part'
 edge=[dict(sample='no-earned-A-or-B',earned_before={'G1':1,'G2':0,'G3':0,'G4':0,'G5':0},earned_A_B=[],deduction=0,expected_credit=1,reason='One method mark; nothing eligible to deduct. No charge transferred to later parts.'),dict(sample='bare-correct-misread-gradient',earned_before={'G1':0,'G2':0,'G3':0,'G4':0,'G5':0},deduction=0,expected_credit=0,reason='OD-1: a bare answer earns no awards and MR does not create working.'),dict(sample='proof-target-inconsistent-with-misread-curve',MR_eligible=False,terminal_S4=0,reason='Changing the supplied proof target changes the object; mark the actual target canonically.'),dict(sample='divided-proof-failed-back-substitution',awards={'S1':1,'S2':1,'S3':1,'S4':0},expected_credit=3,total=4),dict(sample='wrong-index-coincidence-in-extended-gradient',awards={'H1':1,'H2':1},expected_credit=2,total=2,proof_S2=0,proof_S4=0,reason='Credible own expression at x=0 yields the canonical value. H2 has no www gate; G5 has its separate gate.'),dict(sample='negative-y-log-without-moduli',awards={'S1':0,'S2':0,'S3':1,'S4':0},expected_credit=1,total=4,reason='Invalid real equivalent relation; only separately correct S3 evidence survives.'),dict(sample='positive-reciprocal-or-just-negation',N1=0,N2=0,reason='N1 needs labelled value equal to -1/(their m); dependent N2 cannot be inferred.'),dict(sample='own-figure-error',MR_eligible=False,reason='Ordinary canonical accuracy and existing limited method F.T., no OD-6.'),dict(sample='misread-point-off-curve',MR_eligible=False,reason='No gradient at a point absent from the curve; changed object/no-solution case, ordinary canonical marking.'),dict(sample='misread-degree-simplifies-classification',MR_eligible=False,reason='Changed difficulty/object receives ordinary canonical marking.'),dict(sample='named-e-index-differentiation-error',MR_eligible=False,gradient_G5=0,reason='Method error, not a genuine question-data misread; www cannot be rescued.')]
 if a.negative_fixture=='no-accuracy-negative-total':edge[0]['deduction']=1
 assert edge[0]['deduction']==0,'No A/B earned but MR deducted a mark'
 if a.negative_fixture=='proof-target-follow-through':edge[2]['terminal_S4']=1
 assert edge[2]['terminal_S4']==0,'Misread proof target received S4'
 if a.negative_fixture=='normal-positive-reciprocal':edge[6]['N1']=1
 assert edge[6]['N1']==0,'Invalid perpendicular gradient earned N1'
 if a.negative_fixture=='invalid-log-full-credit':edge[5]['expected_credit']=4
 assert edge[5]['expected_credit']==1,'Invalid logarithm route received full credit'
 original_text=(W/'work-orders/WB8227-stationary-inflexion.md').read_text()
 assert 'G1/G4'not in original_text and 'G2 or final accuracy G5'not in original_text
 write(H/'calculus-misread-oracle.json',dict(status='pass',scope='Stage-D manual expected awards plus independently recomputed misread mathematics; not a marker implementation or independent content acceptance.',policy_parts_checked=8,retained_case_misreads_checked=12,samples=samples,edge_expectations=edge,source_checks=['Syllabus PDF14/printed11 native image reread for division and quotient prerequisites.','OD-6 source pages independently read by root D3 source audit; Cambridge is comparable, not NSSCAS.']))
 print(json.dumps(dict(status='pass',policy_parts=8,misread_math_samples=len(samples),edge_cases=len(edge)),indent=2))
if __name__=='__main__':main()
