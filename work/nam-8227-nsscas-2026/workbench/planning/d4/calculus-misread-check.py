"""D4 fixed-response mathematics and derived gross/net ledger audit.

All evidence vectors are authored expectations for named worked submissions.
This is not a submission recogniser, runtime marker or question generator.
"""
from pathlib import Path
import argparse,json
import sympy as S
from misread_ledger import settle,award
H=Path(__file__).resolve().parent;W=H.parent.parent
read=lambda p:json.loads(p.read_text())
write=lambda p,d:p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
DEPS={'G2':['G1'],'G5':['G2','G4'],'S2':['S1'],'S4':['S1','S2','S3'],'H2':['H1'],'N2':['N1'],'N3':['N1','N2'],'P3':['P1'],'P4':['P3'],'C2':['C1'],'I3':['I2'],'I6':['I5']}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--negative-fixture',choices=['missing-policy','no-later-deduction','gross-dependency-cascade','eligibility-reopened','proof-target-follow-through','back-substitution-in-S3','normal-positive-reciprocal','invalid-log-full-credit']);a=ap.parse_args()
 design=read(W/'planning/calculus-design.json');recipes=[r for r in design['recipes']if r['recipe_id']in ['WB8227-implicit-normal','WB8227-stationary-inflexion']]
 branches={b['branch_id']:b for r in recipes for b in r['branches']};parts=[q for r in recipes for b in r['branches']for q in b['part_specs']]
 assert len(parts)==8
 for r in recipes:assert r['version']=='0.1.4'
 for q in parts:
  assert q['bloom']==3 and q['classification_version']=='8227-pilot-design-0.1.1'
  assert all('@0.1.4:'in c['criterion_id']for c in q['criteria'])
  if q['part_id']!='show-derivative':assert all('fixed supplied proof target'not in s for c in q['criteria']for s in c['qualifiers'])
 proof=next(q for q in parts if q['part_id']=='show-derivative')
 if a.negative_fixture=='back-substitution-in-S3':proof['alternative_criterion_mapping']['S3']='Back-substitution is required here.'
 assert 'No back-substitution'in proof['alternative_criterion_mapping']['S3'],'S3 acquired back-substitution'
 assert 'back-substitution'in proof['alternative_criterion_mapping']['S4']
 shared=read(H/'shared-misread-policy.json')
 if a.negative_fixture=='missing-policy':shared.pop('operational_status')
 assert shared['owner_principle_id']=='OD-6'and'proposed'in shared['operational_status']
 for q in parts:
  m=q['misread_policy'];assert m['owner_principle_id']=='OD-6'and m['operational_policy_id']=='MR03-OPS-D4'and 'proposed'in m['operational_status']
  assert m['owner_principle']==shared['owner_principle']and m['operational_rules']==shared['operational_rules']and m['feedback']==shared['feedback']
 for rid in ['WB8227-implicit-normal','WB8227-stationary-inflexion']:
  assert shared['work_order_line']in(W/'work-orders'/f'{rid}.md').read_text()
 x,y=S.symbols('x y',real=True);samples=[];edges=[]
 def evidence(branch_id,earned=None,datum=None,using_parts=None,basis='misread'):
  rows=[];earned=earned or{}
  for q in branches[branch_id]['part_specs']:
   use=datum is not None and(using_parts is None or q['part_id']in using_parts)
   for c in q['criteria']:
    suf=c['suffix'];rows.append(award(suf,q['part_id'],c['mark_type'],earned.get(suf,1),[datum]if use else[],DEPS.get(suf,[]),basis))
  return rows
 def record(label,branch_id,earned,eligible,reason,first_use,expected,computed,datum_id='copied-datum',using_parts=None,canonical_value=None,misread_value=None):
  awards=evidence(branch_id,earned,datum_id,using_parts,'misread'if eligible else'canonical')
  datum=dict(datum_id=datum_id,eligible=eligible,first_use_part=first_use,reason=reason,canonical_value=canonical_value,misread_value=misread_value)
  result=settle(awards,[datum]);assert result['net_total']==expected,(label,result['net_total'],expected)
  return dict(case_id=label,branch_id=branch_id,computed=computed,gross_evidence_justification=reason,derived_ledger=result,expected_credit=expected,expected_tariff=result['tariff'])
 for c in read(H/'calculus-case-inputs.json')['cases']:
  p=c['parameters'];branch=c['branch_id'].rsplit(':',1)[1];cid=c['case_id']
  if c['recipe_id']=='WB8227-implicit-normal':
   aa,k,q=p['a'],p['k'],p['q'];C=q*(q+aa)
   if branch=='gradient':
    kk=5-k;eq=aa*S.exp(kk*x)*y+y*y-C;assert eq.subs({x:0,y:q})==0
    mm=S.simplify((-S.diff(eq,x)/S.diff(eq,y)).subs({x:0,y:q}));canonical=S.Rational(-aa*k*q,aa+2*q)
    assert mm!=canonical and mm!=0
    sigma=S.sign(aa+2*q);local=(-aa*S.exp(kk*x)+sigma*S.sqrt(aa*aa*S.exp(2*kk*x)+4*C))/2
    independent=S.simplify(S.diff(local,x).subs(x,0));assert independent==mm
    rec=record(cid,c['branch_id'],{},True,'The supplied point remains on the misread curve, with finite nonzero gradient and nonunit exponential-chain demand. Complete correct work on this datum earns every gross criterion. G5 www and all dependencies are checked before the net penalty.','gradient',4,dict(gradient=str(mm),independent_local_root_derivative=str(independent)),canonical_value=k,misread_value=kk)
    assert rec['derived_ledger']['ledger'][0]['deducted_criterion']=='G2'
    assert rec['derived_ledger']['dependency_evidence']['G5']['G2']==1
    samples.append(rec)
   else:
    numerator=aa*k;misread=numerator+2;mm=S.Rational(-misread*q,aa+2*q);normal=-1/mm
    assert mm!=S.Rational(-aa*k*q,aa+2*q)and mm*normal==-1
    rec=record(cid,c['branch_id'],{},True,'The correct printed proof was read and established. Only the displayed numerator is newly misread in gradient application; the substitution and normal task retain their demand. The proof is not associated with the later datum.','gradient',8,dict(gradient=str(mm),normal_slope=str(normal),normal_equation=f'y-({q})=({normal})*x'),using_parts=['gradient','normal'],canonical_value=numerator,misread_value=misread)
    assert rec['derived_ledger']['ledger'][0]['deducted_criterion']=='H2';samples.append(rec)
  else:
   aa,h,cc=p['a'],p['h'],p['c'];f=S.expand(aa*((x-h)**3-3*p['r']**2*(x-h))+cc)if branch=='two-extrema'else S.expand(aa*(x-h)**p['power']+cc)
   wrong=f+1;df=S.diff(wrong,x);roots=S.solve(df,x);types=[]
   for z in roots:
    for order in range(2,S.degree(wrong,x)+1):
     term=S.diff(wrong,x,order).subs(x,z)
     if term!=0:types.append('stationary inflexion'if order%2 else'minimum'if term>0 else'maximum');break
   assert S.diff(wrong,x)==S.diff(f,x)
   computed=dict(points=[[int(z),int(wrong.subs(x,z))]for z in roots],classifications=types,derivative=str(df))
   first='points'if branch=='two-extrema'else'point';slot='P2'if branch=='two-extrema'else'I1'
   rec=record(cid,c['branch_id'],{},True,'Printed polynomial constant changes by one. Derivative, stationary solving and nature task are unchanged; all gross evidence is correctly demonstrated on that polynomial context.',first,5,computed,canonical_value=int(f.subs(x,0)),misread_value=int(wrong.subs(x,0)))
   assert rec['derived_ledger']['ledger'][0]['deducted_criterion']==slot;samples.append(rec)
 assert len(samples)==12
 gradient='WB8227-implicit-normal:gradient';normal='WB8227-implicit-normal:normal';ext='WB8227-stationary-inflexion:two-extrema';flat='WB8227-stationary-inflexion:flat-classification'
 # No earned A/B anywhere: no penalty can be taken from M/DM.
 edges.append(record('no-earned-A-or-B-anywhere',gradient,{'G2':0,'G3':0,'G4':0,'G5':0},True,'Only a visible differentiation attempt earns G1; no accuracy award exists anywhere on this datum.','gradient',1,{}))
 edges.append(record('bare-correct-misread-gradient',gradient,{key:0 for key in ['G1','G2','G3','G4','G5']},True,'OD-1 gives zero for an unsupported final answer; MR never creates evidence.','gradient',0,{}))
 # First-use part has no A/B; later same-polynomial nature has C2.
 base=x**3-6*x*x+9*x+1;misread_poly=base+6;learner_df=6*x*x-24*x+18
 assert S.solve(learner_df,x)==[1,3]and S.solve(S.diff(base,x),x)==[1,3]
 assert [misread_poly.subs(x,z)for z in[1,3]]==[11,7]
 assert [S.diff(learner_df,x).subs(x,z)for z in[1,3]]==[-12,12]
 deferred=record('stationary-no-AB-in-first-use-part',ext,{'P2':0,'P4':0},True,'Constant-term misread plus unrelated derivative/coordinate slips leaves P1/P3 only, while valid own-root local tests and canonical types earn C1/C2. The same polynomial context is reused in nature.','points',3,dict(learner_derivative='6*x**2-24*x+18',stationary_abscissae=[1,3],nature_test='second derivative of their expression: -12,+12, maximum/minimum'),canonical_value=1,misread_value=7)
 assert deferred['derived_ledger']['gross_total']==4
 if a.negative_fixture=='no-later-deduction':deferred['derived_ledger']['ledger'][0]['deducted_criterion']=None
 assert deferred['derived_ledger']['ledger'][0]['deducted_criterion']=='C2','Misread became free because first-use part lacked A/B'
 edges.append(deferred)
 # calc-D3-02(i): C-only proof change is canonical throughout, not newly eligible.
 canonical_eq=3*S.exp(2*x)*y+y*y-4;point={x:0,y:-4};misC=canonical_eq-1
 assert canonical_eq.subs(point)==0 and misC.subs(point)!=0
 assert S.diff(canonical_eq,x)==S.diff(misC,x)and S.diff(canonical_eq,y)==S.diff(misC,y)
 canonical_m=S.simplify((-S.diff(canonical_eq,x)/S.diff(canonical_eq,y)).subs(point));assert canonical_m==S.Rational(-24,5)
 edges.append(record('implicit-C4-to5-proof-only-ineligible-once',normal,{},False,'At first use P is off the misread curve, so the datum is ineligible for the connected question. C differentiates to zero, so a complete proof nevertheless establishes the canonical target. Correct displayed-derivative substitution and normal remain canonical.','show-derivative',9,dict(canonical_gradient=str(canonical_m),normal_slope=str(-1/canonical_m),proof_part='4/4',gradient_part='2/2',normal_part='3/3'),canonical_value=4,misread_value=5))
 # calc-D3-02(ii): finite a3->4 response carried forward, still canonical.
 misA=4*S.exp(2*x)*y+y*y-4;wrong_m=S.simplify((-S.diff(misA,x)/S.diff(misA,y)).subs(point));assert misA.subs(point)!=0 and wrong_m==-8
 wrong_normal=-1/wrong_m;assert wrong_normal==S.Rational(1,8)
 vals={'S2':0,'S4':0,'H2':0,'N3':0}
 ineligible=record('implicit-a3-to4-target-ineligible-through-later-parts',normal,vals,False,'Misread curve/point and supplied target are inconsistent at first use. Canonical S1/S3 remain, H1 uses a credible own derivative, N1/N2 use the correct negative reciprocal and own line; canonical S2/S4/H2/N3 fail. Eligibility cannot reopen later.','show-derivative',5,dict(gradient=str(wrong_m),normal_slope=str(wrong_normal),normal_equation='y+4=x/8',parts=['2/4','1/2','2/3']),canonical_value=3,misread_value=4)
 if a.negative_fixture=='eligibility-reopened':
  bad=evidence(normal,vals,'a',basis='canonical');next(a for a in bad if a['id']=='H2')['basis']='misread';settle(bad,[dict(datum_id='a',eligible=False,first_use_part='show-derivative',reason='Target-ineligible')])
 if a.negative_fixture=='proof-target-follow-through':
  bad=evidence(normal,{**vals,'S4':1},'a',basis='canonical');settle(bad,[dict(datum_id='a',eligible=False,first_use_part='show-derivative',reason='Target-ineligible')])
 edges.append(ineligible)
 # A nonfinite coefficient change is not the finite response above.
 singular=8*S.exp(2*x)*y+y*y-4;assert S.diff(singular,y).subs(point)==0
 edges.append(dict(case_id='implicit-a3-to8-singular-distinct',eligible=False,computed=dict(denominator_at_P=0),treatment='No finite tangent/normal; do not reuse the finite a3-to4 response or its score. No eligibility reopening.'))
 # Canonical method-error cases are not eligible MR accuracy.
 ownfig=record('own-figure-final-gradient-error',gradient,{'G5':0},False,'The question data were read correctly; the final own numerical gradient is copied with the wrong sign. Valid preceding method survives; accuracy fails.','gradient',4,dict(canonical_gradient='-24/5',learner_own_copy='24/5'))
 edges.append(ownfig)
 eq2=2*S.exp(2*x)*y+y*y-4;mm2=S.simplify((-S.diff(eq2,x)/S.diff(eq2,y)).subs(point));assert mm2==S.Rational(-8,3)and eq2.subs(point)!=0
 edges.append(record('misread-point-off-curve-gradient',gradient,{'G2':0,'G5':0},False,'The supplied point is not on the coefficient-misread curve, so no such tangent exists; ordinary canonical marking retains G1/G3/G4, not wrong product accuracy or final accuracy.','gradient',3,dict(learner_gradient=str(mm2),canonical_gradient=str(canonical_m)),canonical_value=3,misread_value=2))
 edges.append(record('k2-to1-easier-chain-free',gradient,{'G2':0,'G5':0},False,'k=1 removes this branch’s declared nonunit chain demand; use ordinary canonical marking.','gradient',3,dict(learner_gradient='-12/5'),canonical_value=2,misread_value=1))
 wrong_named_m=S.solve(S.Eq(-9+S.Symbol('m')-6,0),S.Symbol('m'))[0];assert wrong_named_m==15
 edges.append(record('eligible-k-misread-plus-omitted-y-prime',gradient,{'G3':0,'G5':0},True,'k2→3 is eligible; the separate method error omits y-prime from the y² derivative, losing G3 and www G5. G1/G2/G4 gross remain; MR comes from G2 only.','gradient',2,dict(canonical_model='exp(2*x)*y+y**2=6; P=(0,-3)',misread_model='exp(3*x)*y+y**2=6',learner_relation='3*exp(3*x)*y+exp(3*x)*y_prime+2*y=0',learner_gradient=15),canonical_value=2,misread_value=3))
 # Fixed ordinary rubric regressions from D3, with derived totals.
 ordinary=[]
 for label,bid,vals,credit,why in [
  ('divided-proof-failed-back-substitution',normal,{'S4':0,'H1':0,'H2':0,'N1':0,'N2':0,'N3':0},3,'Correct divided-route S1/S2/S3; missing final target establishment loses only S4.'),
  ('wrong-index-coincidence-extended-gradient',normal,{'S2':0,'S4':0},7,'Known wrong e-index proof loses S2/S4; its credible x=0 application gives canonical H1/H2 and correct normal.'),
  ('negative-y-log-without-moduli',normal,{'S1':0,'S2':0,'S4':0,'H1':0,'H2':0,'N1':0,'N2':0,'N3':0},1,'Invalid real log relation; only independently correct remaining derivative evidence S3 survives under proposed DEV09.'),
  ('positive-reciprocal-or-negation',normal,{'N1':0,'N2':0,'N3':0},6,'Prior proof/gradient correct; N1 not earned, so N2 dependent method also fails and the final line is not canonical.')]:
  vector=evidence(bid,vals,basis='canonical')
  if a.negative_fixture=='invalid-log-full-credit'and label=='negative-y-log-without-moduli':next(v for v in vector if v['id']=='S4')['earned']=1
  if a.negative_fixture=='normal-positive-reciprocal'and label=='positive-reciprocal-or-negation':next(v for v in vector if v['id']=='N1')['earned']=1
  result=settle(vector,[]);assert result['net_total']==credit,(label,result['net_total'],credit);ordinary.append(dict(case_id=label,reason=why,derived_ledger=result,expected_credit=credit))
 # Concrete source-review object change: flat cubic +3x read as +2x.
 cubic=x**3-3*x**2+3*x-3;wrong=x**3-3*x**2+2*x-3;wrong_roots=S.solve(S.diff(wrong,x),x)
 assert wrong_roots==[1-S.sqrt(3)/3,1+S.sqrt(3)/3]
 wrong_points=[[str(z),str(S.simplify(wrong.subs(x,z)))]for z in wrong_roots]
 edges.append(record('misread-coefficient-changes-flat-object',flat,{'I1':0,'I3':0,'I4':0,'I6':0},False,'Reading +3x as +2x changes the stationary inflexion to two extrema. Canonical I1/I3/I4/I6 fail; ordinary credible quadratic solving and testing methods I2/I5 survive, as in the confirmed D3 review fixture.','point',2,dict(misread_polynomial=str(wrong),stationary_points=wrong_points,learner_types=['maximum','minimum'],canonical_type='stationary inflexion'),canonical_value=3,misread_value=2))
 if a.negative_fixture=='gross-dependency-cascade':
  wrong=evidence(gradient,{'G2':0},'k');settle(wrong,[dict(datum_id='k',eligible=True,first_use_part='gradient',reason='Eligible k2→3')])
 assert all(rec['derived_ledger']['ledger'][0]['amount']<=1 for rec in samples)
 write(H/'calculus-misread-oracle.json',dict(status='pass',scope=__doc__.strip(),part_policies=8,retained_case_misreads=12,samples=samples,edge_fixtures=edges,ordinary_regressions=ordinary,operational_authority=shared['operational_status'],eligibility_decisions='Planner interpretations disclosed in own WO; each datum is classified once for the connected question. calc-D3-04 coefficient eligibility remains an E/F item.',limits='CAS work independently checks fixed mathematical responses. Gross awards are explicit proposed evidence judgements; the shared helper derives net ledgers only. No runtime submission recognition or independent vendor acceptance.'))
 print(json.dumps(dict(status='pass',parts=8,misread_cases=len(samples),edge_fixtures=len(edges),ordinary_regressions=len(ordinary)),indent=2))
if __name__=='__main__':main()
