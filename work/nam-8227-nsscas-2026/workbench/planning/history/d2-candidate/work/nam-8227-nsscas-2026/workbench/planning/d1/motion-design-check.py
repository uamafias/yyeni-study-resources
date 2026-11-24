"""Stage-D finite design checks/oracle only. Does not generate runtime questions."""
import json,itertools,math
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import mpmath as mp
P=Path(__file__).resolve().parents[1];D=json.loads((P/'calculus-design.json').read_text());R=next(r for r in D['recipes']if r['recipe_id']=='WB8227-motion-integration');t=s.symbols('t',real=True)
def validate_admission(slug,raw):
 if slug=='polynomial-chain':
  A,B,u,T=map(int,raw);assert (A,B,u,T)!=(3,1,2,3),'official polynomial original admitted'
  assert A in range(1,4) and B in range(3) and u in range(1,5) and T in range(1,5)
 elif slug=='exponential-positive':
  V=int(raw[0]);k=F(raw[1]);T=int(raw[2]);assert k!=1,'unit chain-factor collision admitted'
  assert (V,k,T)!=(30,F(1,2),2),'official exponential original admitted'
  assert V in [6,12,18,24,30] and k in [F(1,4),F(1,2),F(1,3)] and T in range(1,5)
 else:
  k,r,c,tail=map(int,raw);assert r!=tail,'quadratic triangle collision admitted'
  assert k in [-3,-2,-1,1,2,3] and all(x in range(1,4)for x in [r,c,tail])
results=[]
for b in R['branches']:
 slug=b['branch_id'].split(':')[-1];tuples=b['accepted_tuple_keys'];collisions={};tests={};removed=[]
 def test(name,key,wrong,correct):
  tests[name]=tests.get(name,0)+1
  if abs(float(wrong-correct))<1e-9:collisions.setdefault(name,[]).append(key)
 for raw in tuples:
  validate_admission(slug,raw)
  if slug=='polynomial-chain':
   A,B,u,T=map(int,raw);d=F(A*T**3,3)+F(B*T*T,2)+u*T
   test('omit initial velocity constant',raw,d-u*T,d)
   test('omit lower boundary (zero primitive at zero)',raw,d,d)
   test('omit linear acceleration term B',raw,d-F(B*T*T,2),d)
  elif slug=='exponential-positive':
   V=int(raw[0]);k=F(raw[1]);T=int(raw[2]);term=1-math.exp(-float(k)*T);d=float(V/k)*term
   assert k!=1 and (V,k,T)!=(30,F(1,2),2)
   test('omit reciprocal chain factor in integral',raw,V*term,d)
   test('multiply by k instead of divide',raw,float(V*k)*term,d)
   test('omit lower boundary',raw,-float(V/k)*math.exp(-float(k)*T),d)
  else:
   k,r,c,tail=map(int,raw);T=r+tail;prim=lambda x:k*(F(x**3,3)+F((c-r)*x*x,2)-r*c*x)
   left=prim(r);right=prim(T)-left;dist=abs(left)+abs(right)
   test('absolute value of net displacement',raw,abs(prim(T)),dist)
   test('treat quadratic velocity as straight-line triangles',raw,F(abs(k*r*c)*r,2)+F(abs(k*(T-r)*(T+c))*tail,2),dist)
   test('signed integral instead of travelled length',raw,prim(T),dist)
  # Every admitted record is feasible. Disclosed answer coincidences do not imply method credit.
 nondiagnostic=[]
 for name,keys in collisions.items():
  if slug=='polynomial-chain' and name in ['omit lower boundary (zero primitive at zero)','omit linear acceleration term B']:
   nondiagnostic.append(dict(error=name,tuple_count=len(keys),tuples=keys,reason='Retained and explicitly disclosed: zero boundary/zero B may hide this isolated numeric omission. Working-required criteria still require credible integration; this instance is not a diagnostic test of the missing term/boundary.'))
  else:raise AssertionError((slug,name,len(keys)))
 results.append(dict(branch_id=b['branch_id'],raw_capacity=len(tuples),semantic_capacity=b['semantic_capacity'],errors_tested=tests,removed_original_tuples=b['domain_spec'].get('excluded_original'),disclosed_nondiagnostic_instances=nondiagnostic,undisclosed_collisions=0))
oracle=[]
for case in json.loads((P/'d1/motion-cases.json').read_text()):
 q=case['parameters'];e=case['expected_answers'];slug=case['branch_id'].split(':')[-1]
 if slug=='polynomial-chain':
  a=2*q['A']*t+q['B'];v=s.integrate(a,t)+q['u'];answer=s.integrate(v,(t,0,q['T']))
  assert s.simplify(v-s.sympify(e['velocity'],locals={'t':t}))==0
  assert answer==s.Rational(e['distance'])
  assert s.diff(v,t)==a
 elif slug=='exponential-positive':
  k=s.Rational(q['k']);v=q['V']*s.exp(-k*t);a=s.diff(v,t);answer=s.integrate(v,(t,0,q['T']))
  assert s.simplify(a-s.sympify(e['acceleration'],locals={'t':t}))==0
  assert s.simplify(answer-s.sympify(e['distance_exact']))==0
  numeric=mp.quad(lambda x:q['V']*mp.exp(-mp.mpf(str(float(k)))*x),[0,q['T']]);assert abs(float(answer)-float(numeric))<1e-10
 else:
  v=q['k']*(t-q['r'])*(t+q['c']);T=q['T'];root=q['r'];answer=s.Abs(s.integrate(v,(t,0,root)))+s.Abs(s.integrate(v,(t,root,T)))
  assert answer==s.Rational(e['distance']);assert s.integrate(v,(t,0,T))==s.Rational(e['displacement'])
  numeric=mp.quad(lambda x:abs(q['k']*(x-q['r'])*(x+q['c'])),[0,root,T]);assert abs(float(answer)-float(numeric))<1e-10
 oracle.append(dict(case_id=case['case_id'],status='pass',method='separately implemented symbolic integration/differentiation; exponential/reversal additionally checked by numerical quadrature',answer=str(answer)))
negative=[]
for slug,raw,reason in [('polynomial-chain',['3','1','2','3'],'official polynomial original admitted'),('exponential-positive',['18','1','3'],'unit chain-factor collision admitted'),('interior-reversal',['2','1','1','1'],'quadratic triangle collision admitted')]:
 try:validate_admission(slug,raw)
 except AssertionError as exc:
  assert str(exc)==reason;negative.append(dict(fixture=slug,seed=raw,result='rejected',reason=reason))
 else:raise AssertionError('negative seed passed')
report=dict(negative_fixtures=negative,status='pass' ,scope='Stage-D motion design only; no runtime generation or independent-vendor acceptance',branches=results,exemplar_oracle=oracle)
(P/'d1/motion-design-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':'pass','branches':len(results),'exemplars':len(oracle)}))
