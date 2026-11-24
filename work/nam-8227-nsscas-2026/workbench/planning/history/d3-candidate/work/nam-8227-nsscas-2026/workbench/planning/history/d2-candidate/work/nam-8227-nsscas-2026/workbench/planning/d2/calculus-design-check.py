"""D2 PLANNER mathematics/discrimination audit; not a runtime generator or marker.

Reads finite design domains and twelve paper exemplar records. Produces no question
text and no learner instances. Separate symbolic/explicit-root recomputation is the
oracle; printed expected exemplar answers are inputs, not reused answer functions.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,math,hashlib
import sympy as S
HERE=Path(__file__).resolve().parent
WB=HERE.parent.parent
read=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
key=lambda x:json.dumps(x,separators=(',',':'),sort_keys=True)
x=S.symbols('x',real=True)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['implicit-chain','implicit-original','proof-given-answer-credit','index-error-accuracy-credit','classification-analyse','alternative-proof-missing-slot']);args=parser.parse_args()
 tuples=[(a,k,q)for a,k,q in product(range(1,5),[2,3],range(-5,0))if a+2*q!=0 and q!=-a and(a,k,q)!=(2,3,-5)]
 if args.negative_fixture=='implicit-chain':tuples[0]=(3,1,-1)
 if args.negative_fixture=='implicit-original':tuples[0]=(2,3,-5)
 assert len(tuples)==27 and all(k in [2,3]for a,k,q in tuples),'D1 implicit chain/domain discrimination failed'
 assert (2,3,-5)not in tuples,'D1 official original leaked into fresh pool'
 implicit=[];collisions={name:[]for name in ['omit-exponential-chain-factor','omit-y-chain-factor','differentiate-constant-as-itself','omit-product-factor-y-derivative','treat-exponential-as-constant','reverse-gradient-sign','normal-negate-instead-reciprocal','normal-positive-reciprocal','change-exponential-index']}
 for a,k,q in tuples:
  c=q*(q+a);m=F(-a*k*q,a+2*q);normal=-1/m
  # Independent implicit partial derivatives, not the displayed answer formula.
  X,Y=S.symbols('X Y');relation=a*S.exp(k*X)*Y+Y**2-c
  mm=-S.diff(relation,X).subs({X:0,Y:q})/S.diff(relation,Y).subs({X:0,Y:q});assert mm==S.Rational(m.numerator,m.denominator)
  # Independent explicit local branch derivative.
  sigma=1 if a+2*q>0 else-1;explicit=(-a*S.exp(k*x)+sigma*S.sqrt(a*a*S.exp(2*k*x)+4*c))/2
  assert S.simplify(explicit.subs(x,0))==q
  assert S.simplify(S.diff(explicit,x).subs(x,0)-mm)==0
  wrong={'omit-exponential-chain-factor':F(-a*q,a+2*q),'omit-y-chain-factor':F(-q*(a*k+2),a),'differentiate-constant-as-itself':F(c-a*k*q,a+2*q),'omit-product-factor-y-derivative':F(-a*k,2),'treat-exponential-as-constant':F(0),'reverse-gradient-sign':-m,'normal-negate-instead-reciprocal':-m,'normal-positive-reciprocal':1/m,'change-exponential-index':S.simplify((-a*k*S.exp((k-1)*x)*S.Symbol('y')/(a*S.exp(k*x)+2*S.Symbol('y'))).subs({x:0,S.Symbol('y'):q}))}
  for name,v in wrong.items():
   if v==(normal if name.startswith('normal-')else m):collisions[name].append([a,k,q])
  implicit.append(dict(parameters=dict(a=a,k=k,q=q),curve_key=key(['implicit-curve',a,k,c]),point_task_key=key(['implicit-point',a,k,c,q]),show_derivative_key=key(['implicit-show',a,k]),normal_part_key=key(['implicit-normal',a,k,c,q]),gradient=str(m),normal_slope=str(normal)))
 assert len(collisions['change-exponential-index'])==27
 assert not any(v for name,v in collisions.items()if name!='change-exponential-index'),('Undisclosed implicit answer collision',collisions)
 curves={r['curve_key']for r in implicit};points={r['point_task_key']for r in implicit};proofs={r['show_derivative_key']for r in implicit}
 assert(len(curves),len(points),len(proofs))==(23,27,8)
 # Keep the accepted two-extrema domain. Keys intentionally collapse vertical
 # translations and horizontal mirrors for classification, but not coordinates.
 extrema=[];flat=[];surface=[];factor_checks=[]
 for a,h,r,c in product([-2,-1,1,2],[-2,-1,0,1,2],[1,2,3],range(-4,5)):
  f=S.Poly(S.expand(a*((x-h)**3-3*r*r*(x-h))+c),x);df=f.diff();roots=sorted(df.ground_roots());assert roots==[h-r,h+r]
  assert all(df.eval(z)==0 for z in roots)
  # A substituted-function-for-derivative error cannot return BOTH correct stationary x values.
  f_as_zero=[z for z in roots if f.eval(z)==0]
  assert len(f_as_zero)<2
  e=dict(parameters=dict(a=a,h=h,r=r,c=c),polynomial_coefficients=[int(v)for v in f.all_coeffs()],points=[[int(z),int(f.eval(z))]for z in roots],nature=['maximum','minimum']if a>0 else['minimum','maximum'],point_task_key=key(['stationary-points',*map(int,f.all_coeffs())]),classification_key=key(['two-extrema-shape',min((a,h,r),(-a,-h,r))]),nondiagnostic_shortcuts=[])
  if h==0:e['nondiagnostic_shortcuts'].append('Dropping horizontal shift is invisible here; h0 easy tier, not a shift-error diagnostic.')
  if f_as_zero:e['nondiagnostic_shortcuts'].append('Function-zero method shares one stationary abscissa but not the complete required pair; visible solve method still required.')
  extrema.append(e)
 for n,a,h,c in product([3,4],[-2,-1,1,2],[-2,-1,1,2],[-4,-3,-2,-1,1,2,3,4]):
  f=S.Poly(S.expand(a*(x-h)**n+c),x);df=f.diff();roots=df.ground_roots();assert list(roots)==[h]and roots[h]==n-1
  left=S.sign(df.eval(h-1));right=S.sign(df.eval(h+1))
  classification='minimum'if left<0<right else'maximum'if left>0>right else'stationary inflexion'
  assert classification==('stationary inflexion'if n==3 else'minimum'if a>0 else'maximum')
  assert c!=0 and h!=0
  # Using derivative for y always returns0; c!=0 removes that accidental correct point.
  assert df.eval(h)!=f.eval(h)
  if n==4:
   quotient,remainder=S.div(df.as_expr(),x-h,x);assert remainder==0
   assert S.discriminant(quotient,x)==0 and S.solve(quotient,x)==[h]
   factor_checks.append(dict(parameters=dict(power=n,a=a,h=h,c=c),derivative=str(df.as_expr()),division_quotient=str(quotient),remainder=0,quadratic_discriminant=0,only_root=h,result='pass'))
  notes=[]
  if n==3:notes.append('f_second(h)==0 therefore inflexion reaches the correct name here, but is an invalid unsupported classification method and earns0 classification marks.')
  if n==4 and a>0:notes.append('Always call a flat point minimum reaches the correct name here, but gives no working and earns0 classification marks.')
  if n==4 and a<0:notes.append('Always call a flat point maximum reaches the correct name here, but gives no working and earns0 classification marks.')
  flat.append(dict(parameters=dict(power=n,a=a,h=h,c=c),polynomial_coefficients=[int(v)for v in f.all_coeffs()],point=[h,c],classification=classification,first_derivative_signs=[int(left),int(right)],point_task_key=key(['flat-point',*map(int,f.all_coeffs())]),classification_key=key(['flat-shape',min((n,a,h),(n,(-1)**n*a,-h))]),nondiagnostic_shortcuts=notes))
 assert len(extrema)==540 and len({r['point_task_key']for r in extrema})==540 and len({r['classification_key']for r in extrema})==30
 assert len(flat)==256 and len({r['point_task_key']for r in flat})==256 and len({r['classification_key']for r in flat})==16
 outcomes={k:sum(r['classification']==k for r in flat)for k in ['stationary inflexion','minimum','maximum']};assert outcomes=={'stationary inflexion':128,'minimum':64,'maximum':64}
 # General proof alternatives independently established from equivalent relations.
 proof_checks=[]
 Y,C=S.symbols('Y C',nonzero=True)
 for a,k in product(range(1,5),[2,3]):
  E=a*S.exp(k*x);target=-k*E*Y/(E+2*Y)
  divided=-k*E*Y**2/(Y**2+C)
  logarithmic=-k*Y*(C-Y**2)/(C+Y**2)
  for route,derived in [('divided-by-y',divided),('log-absolute',logarithmic)]:
   assert S.simplify(derived.subs(C,E*Y+Y**2)-target)==0
   proof_checks.append(dict(a=a,k=k,route=route,forward_result=str(derived),back_substitution='C=ae^(kx)y+y^2',target=str(target),result='pass'))
  simplified=S.cancel(target)
  assert S.simplify(simplified-target)==0
  proof_checks.append(dict(a=a,k=k,route='simplified-target',forward_result=str(simplified),target=str(target),result='pass'))
 design=read(WB/'planning/calculus-design.json')
 implicit_spec=next(r for r in design['recipes']if r['recipe_id']=='WB8227-implicit-normal')
 stationary_spec=next(r for r in design['recipes']if r['recipe_id']=='WB8227-stationary-inflexion')
 flat_spec=next(b for b in stationary_spec['branches']if b['branch_id'].endswith(':flat-classification'))
 proof_spec=next(q for b in implicit_spec['branches']for q in b['part_specs']if q['part_id']=='show-derivative')
 if args.negative_fixture=='classification-analyse':flat_spec['whole_bloom']=4
 if args.negative_fixture=='alternative-proof-missing-slot':proof_spec['alternative_criterion_mapping'].pop('S3')
 assert flat_spec['whole_bloom']==3 and all(q['bloom']==3 for q in flat_spec['part_specs']),'D2 stationary classification must be Apply3 under OD4'
 assert set(proof_spec['alternative_criterion_mapping'])=={'S1','S2','S3','S4'},'D2 valid alternative proof has an unmapped criterion'
 for rr in [implicit_spec,stationary_spec]:
  assert rr['version']=='0.1.2'
  for bb in rr['branches']:
   assert bb['classification_version']=='8227-pilot-design-0.1.1'
   for pp in bb['part_specs']:assert pp['classification_version']=='8227-pilot-design-0.1.1'
 gradient_spec=next(q for b in implicit_spec['branches']if b['branch_id'].endswith(':gradient')for q in b['part_specs'])
 g5=next(c for c in gradient_spec['criteria']if c['suffix']=='G5')
 assert any('www'in q for q in g5['qualifiers']),'D2 G5 missing without-wrong-working guard'
 point_spec=next(q for q in flat_spec['part_specs']if q['part_id']=='point')
 assert {p['demand_id']for p in point_spec['prerequisite_demand_ids']}=={'8227:2020:M1:T2:O01:D01','8227:2020:M2:T1:O04:D02','8227:2020:M2:T1:O04:D04'}
 assert len(factor_checks)==128
 # Paper evidence vectors make answer-only and given-answer dependencies explicit.
 examples=read(HERE/'calculus-case-inputs.json')['cases'];checks=[]
 for case in examples:
  p=case['parameters'];expected=case['expected_answers'];branch=case['branch_id'].split(':')[-1]
  if case['recipe_id']=='WB8227-implicit-normal':
   a,k,q=p['a'],p['k'],p['q'];c=q*(q+a);sgn=S.sign(a+2*q);explicit=(-a*S.exp(k*x)+sgn*S.sqrt(a*a*S.exp(2*k*x)+4*c))/2
   slope=S.simplify(S.diff(explicit,x).subs(x,0));assert slope==S.sympify(expected['gradient']);assert S.simplify(slope*S.sympify(expected['normal_slope']))==-1
   shown=S.sympify(expected['shown_derivative'],locals={'x':x,'y':S.Symbol('y')});relation=a*S.exp(k*x)*S.Symbol('y')+S.Symbol('y')**2-c
   oracle=-S.diff(relation,x)/S.diff(relation,S.Symbol('y'));assert S.simplify(shown-oracle)==0
   assert case['mark_total']==(5 if branch=='gradient'else 9)
  else:
   a,h,c=p['a'],p['h'],p['c'];f=S.expand(a*((x-h)**3-3*p['r']**2*(x-h))+c)if branch=='two-extrema'else S.expand(a*(x-h)**p['power']+c)
   rootlist=S.solve(S.diff(f,x),x);actual=[[int(z),int(f.subs(x,z))]for z in rootlist]
   assert actual==(expected['points']if branch=='two-extrema'else[expected['point']])
   kinds=[]
   for z in rootlist:
    # Independent polynomial Taylor leading nonzero derivative test, not sign-table construction.
    for order in range(2,S.degree(f,x)+1):
     term=S.diff(f,x,order).subs(x,z)
     if term!=0:
      kinds.append('stationary inflexion'if order%2 else'minimum'if term>0 else'maximum');break
   assert kinds==(expected['classifications']if branch=='two-extrema'else[expected['classification']]);assert case['mark_total']==6
  checks.append(dict(case_id=case['case_id'],result='pass',oracle='explicit local-root derivative and implicit partials'if case['recipe_id']=='WB8227-implicit-normal'else'expanded polynomial solve and first nonzero Taylor derivative',expected_answers=expected,marks=case['mark_total']))
 assert len(checks)==12
 # Not a grader: these are manually specified expected evidence/award vectors.
 marking=[dict(sample='flat-derivative-coefficient-slip',branch='flat-classification',location_credit=2,classification_credit=3,total_credit=5,evidence='I1B0,I2M1,I3A1; correct root does not restore a wrong derivative'),dict(sample='bare-gradient',branch='gradient',expected_credit=0,evidence='correct value, no derivative/substitution work'),dict(sample='bare-normal',branch='normal',expected_credit=0,evidence='correct line only; neither perpendicular step nor line-construction method seen'),dict(sample='copied-show-result',branch='normal',expected_credit=0,evidence='provided formula copied, no proof'),dict(sample='wrong-proof-then-given-result',branch='normal',show_credit=2,terminal_S4_credit=0,evidence='S1 andS3only; a slip cannot follow through into an answer supplied by the question'),dict(sample='first-derivative-only-cubic',branch='flat-classification',expected_credit=6,evidence='I1/I2/I3stationaryworking plus f_prime(h)=0 and correct same-sign neighbourhood test with inflexion conclusion; no secondderivative required'),dict(sample='first-derivative-only-quartic',branch='flat-classification',expected_credit=6,evidence='I1/I2/I3stationaryworking plus opposite first-derivative signs and justified extremum'),dict(sample='slipped-gradient-correct-perpendicular-and-line',branch='normal',normal_credit=2,evidence='N1,M1andN2,DM1seen; canonicalN3fails'),dict(sample='unsupported-stationary-coordinate-and-type',branch='flat-classification',expected_credit=0,evidence='OD1no derivative/solve/classificationmethod')]
 marking += [dict(sample='wrong-exponential-index-correct-gradient',branch='gradient',G1=1,G2=0,G3=1,G4=1,G5=0,total_credit=3,evidence='Wrong general derivative; final number coincides at x0 but cannot earn G5www'),dict(sample='valid-divided-relation-proof',branch='normal',proof_credit=4,criterion_mapping=['S1','S2','S3','S4'],evidence='Every differentiated term and the forward back-substitution shown'),dict(sample='valid-log-absolute-proof',branch='normal',proof_credit=4,criterion_mapping=['S1','S2','S3','S4'],evidence='Log absolute values on nonzero factors, correct implicit log derivatives and forward back-substitution'),dict(sample='own-wrong-derivative-substitution',branch='normal',H1=1,H2=0,evidence='Credible derivative from the proof used consistently; canonical gradient accuracy fails'),dict(sample='simplified-equivalent-target',branch='normal',proof_credit=4,evidence='Correct full derivation and explicit common-factor equivalence'),dict(sample='stated-perpendicular-gradient',branch='normal',N1=1,evidence='Labelled perpendicular-gradient value in working; bare final line remains0')]
 if args.negative_fixture=='index-error-accuracy-credit':next(m for m in marking if m['sample']=='wrong-exponential-index-correct-gradient')['G5']=1
 assert next(m for m in marking if m['sample']=='wrong-exponential-index-correct-gradient')['G5']==0,'D2 wrong e-index numerical coincidence earned G5'
 if args.negative_fixture=='proof-given-answer-credit':next(m for m in marking if m['sample']=='wrong-proof-then-given-result')['terminal_S4_credit']=1
 assert next(m for m in marking if m['sample']=='wrong-proof-then-given-result')['terminal_S4_credit']==0,'D1 no-follow-through into given proof result failed'
 for m in marking:
  if m['sample'].startswith('bare-')or m['sample']in ['copied-show-result','unsupported-stationary-coordinate-and-type']:assert m['expected_credit']==0
 domain=dict(status='pass; finite design enumeration only, not runtime questions',implicit=dict(raw_parameter_combinations=40,admitted_point_tasks=27,distinct_curves=23,show_derivative_identities=8,gradient_strict_fresh_bound=23,normal_strict_fresh_bound=8,point_part_capacity=27,normal_line_part_capacity=27,collision_tests=collisions,disclosed_nondiagnostic_error='change-exponential-index:27/27numeric collisions at x0; working G2 and G5www detect it',tuples=implicit),two_extrema=dict(admitted_polynomials=540,raw_shapes=60,mirror_pairs=270,vertical_shifts_per_shape=9,classification_semantic_capacity=30,coordinate_part_capacity=540,strict_complete_fresh_bound=30,nondiagnostic_shift_error_count=sum(any('horizontal shift'in t for t in r['nondiagnostic_shortcuts'])for r in extrema),partial_function_zero_collision_count=sum(any('Function-zero'in t for t in r['nondiagnostic_shortcuts'])for r in extrema),tuples=extrema),flat_classification=dict(before_h0_c0_exclusions=360,after_h0_exclusion=288,excluded_c0=32,admitted_polynomials=256,outcomes=outcomes,classification_semantic_capacity=16,point_part_capacity=256,strict_complete_fresh_bound=16,unsupported_inflexion_shortcut_answer_collisions=128,all_unsupported_shortcut_working_credit=0,tuples=flat),no_repeat_rule='Require every assessed part semantic key and the shared implicit curve-exposure key unseen for whollyfresh practice/test; otherwise disclose afterfeedback/repeated-component practice. Counts are separate branch packing bounds, never a summed globalbank capacity.')
 write(HERE/'calculus-domain-audit.json',domain)
 write(HERE/'calculus-exemplar-oracle.json',dict(status='pass',cases_checked=len(checks),checks=checks,proof_alternative_checks=proof_checks,quartic_factor_theorem_checks=factor_checks,marking_sample_expectations=marking,limits='Planner-side independent recomputation and manually specified evidence vectors; not vendor-independent acceptance or a runtime grading implementation.'))
 print(json.dumps(dict(status='pass',implicit_point_tasks=27,implicit_curves=23,implicit_normal_fresh_bound=8,two_extrema_raw=540,two_extrema_semantic=30,flat_raw=256,flat_semantic=16,exemplars=len(checks),flat_outcomes=outcomes),indent=2))
if __name__=='__main__':main()
