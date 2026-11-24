"""Stage-D D3 domain/precision/decision audit. No runtime question generation."""
import json,itertools,math,hashlib
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_HALF_UP
import sympy as s
import mpmath as mp
P=Path(__file__).resolve().parents[1];D=json.loads((P/'calculus-design.json').read_text());R=next(r for r in D['recipes']if r['recipe_id']=='WB8227-motion-integration');t=s.symbols('t',real=True);mp.mp.dps=60
POLY_BAD={(3,0,2,2),(3,1,1,2),(3,2,4,1)}
def sf(x,n=3):
 with localcontext()as ctx:
  ctx.prec=60
  if isinstance(x,F):d=Decimal(x.numerator)/Decimal(x.denominator)
  else:d=Decimal(str(x))
  if not d:return '0'
  return str(d.quantize(Decimal(1).scaleb(d.adjusted()-n+1),rounding=ROUND_HALF_UP).normalize())
def admit(slug,row):
 if slug=='polynomial-chain':
  A,B,u,T=map(int,row);assert (A,B,u)!=(3,1,2),'official polynomial part(a) admitted';assert (A,B,u,T)not in POLY_BAD,'differentiate-instead collision admitted';assert A in range(1,4)and B in range(3)and u in range(1,5)and T in range(1,5)
 elif slug=='exponential-positive':
  V=int(row[0]);k=F(row[1]);T=int(row[2]);assert (V,k)!=(30,F(1,2)),'official exponential part(a) admitted';assert k!=1,'unit chain factor collision admitted';assert V in [6,12,18,24,30]and k in [F(1,4),F(1,2),F(1,3)]and T in range(1,5)
 else:
  k,r,c,T=map(int,row)
  rev=k in [-3,-2,-1,1,2,3]and r in range(1,5)and c in range(1,4)and T in [3,4,5]and 0<r<T and 2*r!=T
  no=k in [-3,-2,-1,1,2,3]and(r,c,T)in [(4,1,3),(5,1,3),(5,1,4),(6,1,5)]
  assert rev or no,'outside declared mixed motion domain'
  assert r!=T and r>0 and c>0
branches=[]
for b in R['branches']:
 slug=b['branch_id'].split(':')[-1];tuples=b['accepted_tuple_keys'];collisions={};counts={};rounding=[];outcomes={};samples=[]
 def test(name,row,wrong,correct):
  counts[name]=counts.get(name,0)+1
  if sf(wrong)==sf(correct):collisions.setdefault(name,[]).append(row)
 for row in tuples:
  admit(slug,row)
  if slug=='polynomial-chain':
   A,B,u,T=map(int,row);d=F(A*T**3,3)+F(B*T*T,2)+u*T
   for name,wrong in [('omit-initial-velocity',d-u*T),('zero-lower-bound-omission',d),('omit-B-term',d-F(B*T*T,2)),('differentiate-v-then-both-bounds',F(2*A*T)),('acceleration-at-T',F(2*A*T+B)),('integral-of-a',F(A*T*T+B*T)),('velocity-at-T',F(A*T*T+B*T+u)),('half-endpoint-velocity-times-T',F((A*T*T+B*T+u)*T,2))]:test(name,row,wrong,d)
  elif slug=='exponential-positive':
   V=int(row[0]);k=F(row[1]);T=int(row[2]);e=mp.exp(-mp.mpf(k.numerator)*T/k.denominator);d=mp.mpf(V*k.denominator)/k.numerator*(1-e)
   for name,wrong in [('omit-reciprocal-chain-factor',V*(1-e)),('differentiate-instead-of-integrate',float(V*k)*(1-e)),('omit-lower-bound',-float(V/k)*e)]:test(name,row,wrong,d)
   for prec in [3,4]:
    rounded_e=Decimal(sf(e,prec));approx=Decimal(V*k.denominator)/Decimal(k.numerator)*(1-rounded_e)
    if sf(approx)!=sf(d):rounding.append({'tuple':row,'intermediate_sf':prec,'canonical_3sf':sf(d),'premature_3sf':sf(approx)})
  else:
   k,r,c,T=map(int,row);P0=lambda x:k*(F(x**3,3)+F((c-r)*x*x,2)-r*c*x);inside=[r]if r<T else[];cuts=[0]+inside+[T];legs=[P0(b)-P0(a)for a,b in zip(cuts,cuts[1:])];distance=sum(abs(x)for x in legs);net=P0(T);outcome='sign_change'if inside else'no_sign_change';outcomes[outcome]=outcomes.get(outcome,0)+1
   triangle=(F(abs(k*r*c)*r,2)+F(abs(k*(T-r)*(T+c))*(T-r),2))if inside else F((abs(k*r*c)+abs(k*(T-r)*(T+c)))*T,2)
   for name,wrong in [('linear-triangle-or-trapezium',triangle),('signed-area-without-decision',net),('absolute-net-without-decision',abs(net)),('always-split-at-r',abs(P0(r))+abs(P0(T)-P0(r))),('never-split',abs(net)),('wrong-positive-root-c',abs(P0(c))+abs(P0(T)-P0(c))),('harmless-interior-split',abs(P0(F(T,2)))+abs(P0(T)-P0(F(T,2)))),('coherent-linear-sign-root-slip',abs(P0(c))+abs(P0(T)-P0(c)))]:test(name,row,wrong,distance)
   vertex=F(r-c,2)
   if 0<vertex<T:test('vertex-zero-acceleration-split',row,abs(P0(vertex))+abs(P0(T)-P0(vertex)),distance)
   if not inside:assert r-T in [1,2]
   # 'always split' at a true root beyond T is not an interior partition.
   # Harmless split is an identity for a constant-sign function, not root evidence.
   if len(samples)<2 or(row==['-2','3','2','1']):samples.append({'tuple':row,'outcome':outcome,'distance':str(distance),'displacement':str(net)})
 # Numeric coincidences are disclosed; full credit requires the appropriate evidence.
 forbidden=['differentiate-v-then-both-bounds']if slug=='polynomial-chain'else['omit-reciprocal-chain-factor','differentiate-instead-of-integrate','omit-lower-bound']if slug=='exponential-positive'else['linear-triangle-or-trapezium']
 assert all(not collisions.get(x)for x in forbidden),(slug,collisions)
 branches.append(dict(branch_id=b['branch_id'],admitted_raw=len(tuples),semantic_capacity=b['semantic_capacity'],marked_precision='3 significant figures, decimal half-up; exact answers also accepted',named_error_tests=counts,disclosed_value_coincidences={name:dict(count=len(rows),tuples=rows,credit_rule='Value alone is non-diagnostic. S3 needs S1/S2; mixed-distance R4 needs R2/R3 and www, R3 needs R1 root/interval or complete constant-sign decision and attempted primitive. A correct method for the no-split outcome is accepted when justified; an unchecked strategy is not fabricated as checked.')for name,rows in collisions.items()},undisclosed_collisions=0,decision_outcomes=outcomes,rounding_flip_fixtures=rounding,samples=samples))
assert [x['admitted_raw']for x in branches]==[137,56,168];assert branches[2]['decision_outcomes']=={'sign_change':144,'no_sign_change':24}
# Test each printed coefficient and interval endpoint, plus magnitudes, alone/in pairs.
# A mathematical combination that actually determines the roots/signs is valid reasoning,
# not an incidental parameter shortcut. Hidden r,c are not learner-visible parameters.
mixed=R['branches'][-1];rows=[list(map(int,r))for r in mixed['accepted_tuple_keys']]
assert len(rows)==len(set(map(tuple,rows)))==168
features=['a','b','d','T','abs_a','abs_b','abs_d']
records=[]
for k,r,c,T in rows:
 a,bb,dd=k,k*(c-r),-k*r*c
 records.append(dict(tuple=[k,r,c,T],outcome='sign_change'if r<T else'no_sign_change',values=dict(zip(features,[a,bb,dd,T,abs(a),abs(bb),abs(dd)]))))
separation=[]
for n in [1,2]:
 for names in itertools.combinations(features,n):
  groups={}
  for x in records:groups.setdefault(tuple(x['values'][name]for name in names),[]).append(x)
  ambiguous=[items for items in groups.values()if len({x['outcome']for x in items})==2]
  assert ambiguous,('visible shortcut perfectly separates',names)
  majority_hits=sum(max(sum(x['outcome']==label for x in items)for label in ['sign_change','no_sign_change'])for items in groups.values())
  witness=ambiguous[0];pair=[next(x for x in witness if x['outcome']==label)['tuple']for label in ['sign_change','no_sign_change']]
  separation.append(dict(features=list(names),perfect_separation=False,ambiguous_signatures=len(ambiguous),best_lookup_correct=majority_hits,total=168,opposite_outcome_witness=pair))
keycheck={}
for k,r,c,T in rows:
 key=(k,k*(c-r),-k*r*c,T)
 assert key not in keycheck,'different tuples alias the same expanded bounded task'
 keycheck[key]=(k,r,c,T)
separation_record=dict(status='pass',single_and_pair_tests=len(separation),tests=separation,public_title=mixed['display_title'],shape_count=len({(r,c,T)for k,r,c,T in rows}),interpretation='No tested single printed coefficient, endpoint, magnitude or pair perfectly separates outcomes. This is not a claim that algebraic/sign reasoning cannot do so; endpoint signs plus valid concavity is an accepted R1 method.',part_key_alias_audit=dict(unique_tuple_keys=168,unique_expanded_polynomial_interval_keys=len(keycheck),both_part_keys=['k','r','c','T'],model_repeats_tracked_separately=True))
(P/'d3/motion-separation.json').write_text(json.dumps(separation_record,indent=2)+'\n')
checks=[]
for case in json.loads((P/'d3/motion-cases.json').read_text()):
 p=case['parameters'];e=case['expected_answers'];slug=case['branch_id'].split(':')[-1]
 if slug=='polynomial-chain':
  a=2*p['A']*t+p['B'];v=s.integrate(a,t)+p['u'];ans=s.integrate(v,(t,0,p['T']));assert s.simplify(v-s.sympify(e['velocity'],locals={'t':t}))==0;assert ans==s.Rational(e['distance'])
 elif slug=='exponential-positive':
  k=s.Rational(p['k']);v=p['V']*s.exp(-k*t);a=s.diff(v,t);ans=s.integrate(v,(t,0,p['T']));assert s.simplify(a-s.sympify(e['acceleration'],locals={'t':t}))==0;assert s.simplify(ans-s.sympify(e['distance_exact']))==0
 else:
  v=p['k']*(t-p['r'])*(t+p['c']);roots=s.solve(v,t);inside=sorted(x for x in roots if 0<x<p['T']);cuts=[0]+inside+[p['T']];ans=sum(s.Abs(s.integrate(v,(t,x,y)))for x,y in zip(cuts,cuts[1:]));assert ans==s.Rational(e['distance']);assert s.integrate(v,(t,0,p['T']))==s.Rational(e['displacement']);assert bool(inside)==e['sign_change']
  num=mp.quad(lambda x:abs(p['k']*(x-p['r'])*(x+p['c'])),[float(x)for x in cuts]);assert abs(float(ans)-float(num))<1e-10
 checks.append(dict(case_id=case['case_id'],result='pass',oracle='Separately implemented CAS integration/differentiation and root isolation; mixed branch additionally numerical quadrature',answer=str(ans)))
negative=[]
for slug,row in [('polynomial-chain',[3,1,2,4]),('polynomial-chain',[3,0,2,2]),('exponential-positive',[30,'1/2',4]),('exponential-positive',[18,1,3]),('interior-reversal',[2,2,1,2])]:
 try:admit(slug,row)
 except AssertionError as exc:negative.append(dict(branch=slug,tuple=row,result='rejected',reason=str(exc)))
 else:raise AssertionError('seed admitted')
assert sf(F(233,2))=='117';assert sf(F(233,2),4)=='116.5'
report=dict(status='pass',version='0.1.3',classification_version='8227-pilot-design-0.1.1',branches=branches,exemplar_checks=checks,negative_fixtures=negative,separation=separation_record,half_boundary=dict(exact='233/2=116.5',correct_3sf_half_up='117',incorrect_bankers='116',tuple=['3','2','3','5']),limits='Author design verification, not runtime marker/renderer or independent acceptance. Disclosed numeric coincidences require visible criterion evidence; cannot infer root/primitive decisions from values.')
(P/'d3/motion-design-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'result':'pass','raw_counts':[137,56,168],'outcomes':branches[2]['decision_outcomes'],'exemplars':len(checks),'negatives':len(negative)}))
