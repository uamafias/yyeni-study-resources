"""Second planner agent's independent motion audit, not cross-vendor acceptance.

Uses Fraction polynomial integration and independent CAS differentiation for nine
paper cases. Does not call or import the root motion audit/answer implementation.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import product,combinations
from decimal import Decimal,localcontext,ROUND_HALF_UP
import json,hashlib
import sympy as S
H=Path(__file__).resolve().parent;W=H.parent.parent
read=lambda p:json.loads(p.read_text())

def sig3(f):
 with localcontext()as c:
  c.prec=70;v=Decimal(f.numerator)/Decimal(f.denominator)
  if not v:return Decimal(0)
  return v.quantize(Decimal(1).scaleb(v.copy_abs().adjusted()-2),rounding=ROUND_HALF_UP)

def main():
 paths=[W/'planning/calculus-design.json',H/'motion-design-check.json',H/'motion-cases.json',H/'misread-policy-check.json',W/'work-orders/WB8227-motion-integration.md',W/'exemplars/WB8227-motion-integration.md']
 hashes={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}
 design=read(paths[0]);rr=next(r for r in design['recipes']if r['recipe_id']=='WB8227-motion-integration');mixed=next(b for b in rr['branches']if b['branch_id'].endswith(':interior-reversal'))
 tuples=[q for q in product([-3,-2,-1,1,2,3],range(1,5),range(1,4),[3,4,5])if q[1]<q[3]and 2*q[1]!=q[3]]+[(k,r,c,T)for k in [-3,-2,-1,1,2,3]for r,c,T in [(4,1,3),(5,1,3),(5,1,4),(6,1,5)]]
 assert len(tuples)==168 and len(set(tuples))==168
 assert {tuple(map(int,row))for row in mixed['accepted_tuple_keys']}==set(tuples)
 assert mixed['capacity']==168
 outcomes=Counter(r<T for k,r,c,T in tuples);assert outcomes=={True:144,False:24}
 assert len({(r,c,T)for k,r,c,T in tuples})==28
 features=[];coinc=Counter();per_tuple=[]
 for k,r,c,T in tuples:
  aa=k;bb=k*(c-r);dd=-k*r*c
  vel=lambda z:aa*z*z+bb*z+dd
  primitive=lambda z:F(aa,3)*z**3+F(bb,2)*z**2+dd*z
  signed=primitive(T);bounds=[F(0),F(r),F(T)]if r<T else[F(0),F(T)]
  distance=sum(abs(primitive(v)-primitive(u))for u,v in zip(bounds,bounds[1:]))
  always=abs(primitive(r))+abs(primitive(T)-primitive(r))
  wrong=abs(primitive(c))+abs(primitive(T)-primitive(c))if 0<c<T else abs(signed)
  harmless=abs(primitive(F(T,2)))+abs(primitive(T)-primitive(F(T,2)))
  vertex=F(r-c,2)
  variants={'always-split-at-r':always,'wrong-positive-root-c':wrong,'coherent-linear-sign-root-slip':wrong,'signed-area-without-decision':signed,'absolute-net-without-decision':abs(signed),'never-split':abs(signed),'harmless-interior-split':harmless}
  if 0<vertex<T:variants['vertex-zero-acceleration-split']=abs(primitive(vertex))+abs(primitive(T)-primitive(vertex))
  for name,v in variants.items():
   if sig3(v)==sig3(distance):coinc[name]+=1
  # In every no-change task endpoint signs plus the appropriate concavity suffices.
  if r>T:
   assert vel(0)*vel(T)>0
   assert (aa>0 and vel(0)<0 and vel(T)<0)or(aa<0 and vel(0)>0 and vel(T)>0)
  features.append((dict(a=aa,b=bb,d=dd,T=T,abs_a=abs(aa),abs_b=abs(bb),abs_d=abs(dd)),r<T))
  per_tuple.append(dict(tuple=[k,r,c,T],distance=str(distance),displacement=str(signed),sign_change=r<T))
 root=read(H/'motion-design-check.json');rootmixed=root['branches'][2]
 assert {k:v['count']for k,v in rootmixed['disclosed_value_coincidences'].items()}==dict(coinc),(dict(coinc),{k:v['count']for k,v in rootmixed['disclosed_value_coincidences'].items()})
 names=['a','b','d','T','abs_a','abs_b','abs_d'];separation=[]
 for size in [1,2]:
  for subset in combinations(names,size):
   grouped=defaultdict(set)
   for feature,outcome in features:grouped[tuple(feature[n]for n in subset)].add(outcome)
   ambiguous=sum(len(v)>1 for v in grouped.values());assert ambiguous>0
   separation.append(dict(features=list(subset),ambiguous_signatures=ambiguous,perfect_separation=False))
 assert separation==[{k:t[k]for k in ['features','ambiguous_signatures','perfect_separation']}for t in root['separation']['tests']]
 t=S.symbols('t',real=True);cases=[]
 for case in read(H/'motion-cases.json'):
  p=case['parameters'];expected=case['expected_answers'];branch=case['branch_id'].rsplit(':',1)[1]
  if branch=='polynomial-chain':
   acceleration=2*p['A']*t+p['B'];velocity=S.integrate(acceleration,t)+p['u'];distance=S.integrate(velocity,(t,0,p['T']))
   assert S.simplify(velocity-S.sympify(expected['velocity'],locals={'t':t}))==0
  elif branch=='exponential-positive':
   velocity=p['V']*S.exp(-S.Rational(p['k'])*t);distance=S.integrate(velocity,(t,0,p['T']))
   assert S.simplify(S.diff(velocity,t)-S.sympify(expected['acceleration'],locals={'t':t}))==0
  else:
   k,r,c,TT=p['k'],p['r'],p['c'],p['T'];velocity=S.expand(k*(t-r)*(t+c));roots=S.solve(velocity,t);interior=[z for z in roots if 0<z<TT];bounds=[0]+interior+[TT]
   legs=[S.integrate(velocity,(t,u,v))for u,v in zip(bounds,bounds[1:])];distance=sum(abs(q)for q in legs);signed=S.integrate(velocity,(t,0,TT))
   assert roots==expected['roots'] and interior==expected['interior_roots']
   assert legs==list(map(S.sympify,expected['signed_legs']))
   assert S.simplify(signed-S.sympify(expected['displacement']))==0
  assert S.simplify(distance-S.sympify(expected.get('distance',expected.get('distance_exact'))))==0
  cases.append(dict(case_id=case['case_id'],distance=str(distance),status='pass'))
 misreads=[]
 for sample in read(H/'misread-policy-check.json')['motion_exemplar_misreads']:
  actual=int(sample['case'].split(' as ')[1]);k=S.Rational(sample['k']);TT=sample['T'];v=actual*S.exp(-k*t)
  derivative=S.diff(v,t);primitive=S.integrate(v,t);distance=S.integrate(v,(t,0,TT))
  for name,computed in [('acceleration',derivative),('primitive',primitive),('distance',distance)]:assert S.simplify(computed-S.sympify(sample['learner_work'][name],locals={'t':t}))==0
  assert sum(sample['gross_awards'].values())==5 and sum(sample['net_awards'].values())==4
  assert sample['deduction']=={'datum_id':'V','first_use_part':'acceleration','criterion':'E1','amount':1}
  assert sample['parts']=={'acceleration':'1/2','distance':'3/3'}
  misreads.append(dict(case=sample['case'],acceleration=str(derivative),primitive=str(primitive),distance=str(distance),credit='4/5',status='pass'))
 qualifiers=mixed['official_qualifiers']
 assert 'constant-sign argument'in qualifiers['R1'] and 'never add marks'in qualifiers['R1']
 assert 'attempted primitive with both bounds'in qualifiers['R5'] and 'calculator legs alone are insufficient'in qualifiers['R5']
 assert 'one-slip false interior root'in qualifiers['R4'] and 'giving 3/4'in qualifiers['R4']
 # Concrete arithmetic-slip case: t²−3t−4 has root4, but sqrt25 incorrectly read as1 gives2.
 # On [0,3] the primitive is decreasing, so splitting at2 leaves the exact distance unchanged.
 vf=lambda z:F(1,3)*z**3-F(3,2)*z**2-4*z
 assert abs(vf(2))+abs(vf(3)-vf(2))==abs(vf(3))==F(33,2)
 output=dict(status='pass',reviewer='Codex second planner agent; same-vendor check, not independent content acceptance',input_hashes=hashes,mixed_counts=dict(total=168,sign_change=144,no_sign_change=24,no_change_fraction='1/7',normalised_shapes=28),separation_checks=separation,marked_precision_coincidences=dict(coinc),exemplar_checks=cases,misread_checks=misreads,marking_expectations=[dict(sample='complete no-change endpoint-plus-concavity argument',R1=1,rule='Same slot and cap as the root-solving route; not additive.'),dict(sample='one-slip no-change false root2 on t²−3t−4 over[0,3]',distance='33/2',credit='3/4',rule='R1/R2/R3 earned, R4 www lost despite the canonical number.'),dict(sample='calculator-only signed sum of legs',R5=0,R6=0,rule='Attempted primitive and both bounds are mandatory for R5; accuracy depends on R5.')],limits='Mathematical formulas independently implemented here; award vectors manually checked against written contract. No app or runtime marker tested.',all_mixed_tuple_answers=per_tuple)
 (H/'motion-independent-audit.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'status':'pass','mixed':168,'separation_tests':28,'exemplars':len(cases),'misreads':len(misreads)}))
if __name__=='__main__':main()
