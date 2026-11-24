"""Second planner's independent fixed-domain/motion arithmetic and rubric audit.

Uses exact Simpson integration of quadratic legs rather than the author's cubic
primitive routine. Does not import the motion builder or shared ledger engine.
Same-vendor author-team evidence, not cross-vendor acceptance or a runtime marker.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_HALF_UP
from collections import Counter,defaultdict
from itertools import product,combinations
import json,hashlib
import sympy as S
H=Path(__file__).resolve().parent;P=H.parent;W=P.parent
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def sf(value):
 with localcontext()as c:
  c.prec=80;d=Decimal(value.numerator)/Decimal(value.denominator)if isinstance(value,F)else Decimal(str(value))
  if not d:return '0'
  return str(d.quantize(Decimal(1).scaleb(d.adjusted()-2),rounding=ROUND_HALF_UP).normalize())
def main():
 design=read(P/'calculus-design.json');motion=next(r for r in design['recipes']if r['recipe_id']=='WB8227-motion-integration');b=motion['branches'][-1]
 expected=[(k,r,c,T)for k,r,c,T in product([-3,-2,-1,1,2,3],range(1,5),range(1,4),[3,4,5])if r<T and 2*r!=T]
 expected +=[(k,r,c,T)for k in [-3,-2,-1,1,2,3]for r,c,T in[(4,1,3),(4,3,3),(5,2,4),(6,3,5)]]
 actual=[tuple(map(int,x))for x in b['accepted_tuple_keys']];assert set(actual)==set(expected)and len(actual)==168
 vals=[];answers=[];collisions=defaultdict(list);models=set()
 def simpson(k,r,c,left,right):
  v=lambda u:k*(u-r)*(u+c)
  return F(right-left,6)*(v(F(left))+4*v(F(left+right,2))+v(F(right)))
 for row in expected:
  k,r,c,T=row;aa,bb,dd=k,k*(c-r),-k*r*c;models.add((bb//aa,dd//aa))
  v=lambda u:k*(u-r)*(u+c);bounded=[0,r,T]if r<T else[0,T]
  legs=[simpson(k,r,c,l,u)for l,u in zip(bounded,bounded[1:])];distance=sum(map(abs,legs));net=simpson(k,r,c,0,T)
  interior=F(T,2);vertex=F(r-c,2)
  triangle=F(abs(v(0))*r+abs(v(T))*(T-r),2)if r<T else F(T*(abs(v(0))+abs(v(T))),2)
  split=lambda q:abs(simpson(k,r,c,0,q))+abs(simpson(k,r,c,q,T))
  errors={'linear-triangle-or-trapezium':triangle,'signed-area-without-decision':net,'absolute-net-without-decision':abs(net),'always-split-at-r':split(r),'never-split':abs(net),'wrong-positive-root-c':split(c),'coherent-linear-sign-root-slip':split(c),'harmless-interior-split':split(interior)}
  if 0<vertex<T:errors['vertex-zero-acceleration-split']=split(vertex)
  for name,wrong in errors.items():
   if sf(wrong)==sf(distance):collisions[name].append(row)
  feature=dict(a=aa,b=bb,d=dd,T=T,abs_a=abs(aa),abs_b=abs(bb),abs_d=abs(dd),sum_roots=F(-bb,aa),abs_b_over_a=abs(F(bb,aa)),d_over_a=F(dd,aa),sum_roots_minus_T=F(-bb,aa)-T,sum_roots_ge_T=F(-bb,aa)>=T,endpoint_values_equal=v(0)==v(T),vertex_ge_half_T=vertex>=F(T,2))
  for threshold in range(5):feature[f'abs_b_over_a_ge_{threshold}']=abs(F(bb,aa))>=threshold
  vals.append((feature,r<T));answers.append(dict(tuple=list(row),distance=str(distance),displacement=str(net),signed_legs=[str(z)for z in legs]))
 assert Counter(outcome for _,outcome in vals)=={True:144,False:24}
 assert len({(r,c,T)for k,r,c,T in expected})==28 and len(models)==14
 assert Counter(k>0 for k,r,c,T in expected)=={True:84,False:84}
 sep=read(H/'motion-separation.json');tests=[]
 def lookup(names):
  groups=defaultdict(Counter)
  for f,label in vals:groups[tuple(f[n]for n in names)][label]+=1
  return sum(max(x.values())for x in groups.values()),sum(len(x)==2 for x in groups.values())
 for group in [sep['tests'],sep['triples_containing_T'],sep['derived_feature_tests']]:
  for claim in group:
   correct,ambiguous=lookup(claim['features']);assert correct==claim['best_lookup_correct']and correct<168,(claim,correct)
   if 'ambiguous_signatures'in claim:assert ambiguous==claim['ambiguous_signatures']
   tests.append(dict(features=claim['features'],best_lookup_correct=correct,total=168,ambiguous_signatures=ambiguous))
 assert max(x['best_lookup_correct']for x in sep['tests'])==156 and max(x['best_lookup_correct']for x in sep['triples_containing_T'])==166
 old_shortcut=lookup(['abs_b_over_a_ge_4']);assert old_shortcut[0]==144
 sweeps=read(H/'motion-design-check.json')['branches'][-1]['disclosed_value_coincidences'];sweep_checks=[]
 for name in ['linear-triangle-or-trapezium','signed-area-without-decision','absolute-net-without-decision','always-split-at-r','never-split','wrong-positive-root-c','coherent-linear-sign-root-slip','vertex-zero-acceleration-split','harmless-interior-split']:
  actual_set=set(collisions[name]);claim=sweeps.get(name,{'count':0,'tuples':[]})
  assert actual_set=={tuple(map(int,r))for r in claim['tuples']}and len(actual_set)==claim['count'],name
  sweep_checks.append(dict(strategy=name,coincidences=len(actual_set),tested_precision='3sf decimal half-up',tuple_sets_match=True))
 # Nine finite examples: independent moment formula, differentiation and leg Simpson.
 t=S.symbols('t',real=True);examples=[]
 for case in read(H/'motion-cases.json'):
  p=case['parameters'];a=case['expected_answers'];slug=case['branch_id'].split(':')[-1]
  if slug=='polynomial-chain':
   v=p['A']*t*t+p['B']*t+p['u'];exact=S.Rational(p['A']*p['T']**3,3)+S.Rational(p['B']*p['T']**2,2)+p['u']*p['T'];assert S.simplify(v-S.sympify(a['velocity'],locals={'t':t}))==0;assert exact==S.Rational(a['distance'])
  elif slug=='exponential-positive':
   kk=S.Rational(p['k']);v=p['V']*S.exp(-kk*t);acc=S.diff(v,t);exact=S.Rational(p['V'])/kk*(1-S.exp(-kk*p['T']));assert S.simplify(acc-S.sympify(a['acceleration'],locals={'t':t}))==0;assert S.simplify(exact-S.sympify(a['distance_exact']))==0
  else:
   k,r,c,T=[p[key]for key in ['k','r','c','T']];cuts=[0,r,T]if r<T else[0,T];legs=[simpson(k,r,c,l,u)for l,u in zip(cuts,cuts[1:])];exact=sum(abs(x)for x in legs);net=simpson(k,r,c,0,T)
   assert exact==F(a['distance'])and net==F(a['displacement'])and [str(z)for z in legs]==a['signed_legs']
   assert S.diff(S.sympify(a['primitive'],locals={'t':t}),t).expand()==(k*(t-r)*(t+c)).expand()
  examples.append(dict(case_id=case['case_id'],computed_distance=str(exact),status='pass'))
 assert len(examples)==9
 # Independently authored expected gross evidence and an independent net allocation.
 mr=read(H/'misread-policy-check.json')['motion_cases'];misreads=[]
 gross_expected={
 'exponential-12-read-21':dict(zip(['E1','E2','E3','E4','E5'],[1,1,1,1,1])),
 'exponential-18-read-81':dict(zip(['E1','E2','E3','E4','E5'],[1,1,1,1,1])),
 'exponential-30-read-36':dict(zip(['E1','E2','E3','E4','E5'],[1,1,1,1,1])),
 'exponential-misread-plus-wrong-reciprocal-derivative':dict(zip(['E1','E2','E3','E4','E5'],[0,0,1,1,1])),
 'mixed-R2-net-deduction-keeps-R4-gross-dependency':dict(zip(['R1','R2','R3','R4','R5','R6'],[1]*6)),
 'polynomial-S2-net-deduction-keeps-S3-gross-dependency':dict(zip(['V1','V2','V3','S1','S2','S3'],[1]*6)),
 'mixed-outcome-flipping-T-ineligible-canonical-throughout':dict(zip(['R1','R2','R3','R4','R5','R6'],[0,1,0,0,1,0])),
 'no-AB-anywhere-no-negative-deduction':dict(zip(['E1','E2','E3','E4','E5'],[0,0,0,1,0]))}
 ab={'E1','E2','E3','E5','R2','R4','R6','V2','V3','S2','S3'}
 for row in mr:
  cid=row['case_id'];gross=gross_expected[cid];assert gross==row['gross_awards'];eligible='outcome-flipping'not in cid;net=gross.copy();deduct=None
  allowed=set(gross)-{'V1','V2','V3'}if cid.startswith('polynomial-S2')else set(gross)
  if eligible:
   for key,value in gross.items():
    if value and key in ab and key in allowed:net[key]-=1;deduct=key;break
  assert net==row['net_awards']and sum(net.values())==row['net_total']and row['ledger'][0]['deducted_criterion']==deduct
  work=row.get('work',{});computed={}
  if cid.startswith('exponential-'):
   if 'plus-wrong'in cid:V,kk,T=21,S.Rational(1,2),2
   else:
    canonical,V=map(int,cid.removeprefix('exponential-').split('-read-'));kk,T={12:(S.Rational(1,2),2),18:(S.Rational(1,3),3),30:(S.Rational(1,4),4)}[canonical]
   v=V*S.exp(-kk*t);acc=S.diff(v,t);integral=S.integrate(v,(t,0,T));primitive=S.integrate(v,t)
   for field,value in [('acceleration',acc),('primitive',primitive),('distance',integral),('correct_misread_primitive',primitive),('correct_misread_distance',integral)]:
    if field in work:assert S.simplify(S.sympify(work[field],locals={'t':t})-value)==0,(cid,field)
   if 'wrong_acceleration'in work:assert S.sympify(work['wrong_acceleration'],locals={'t':t})==primitive
   computed=dict(acceleration=str(acc),primitive=str(primitive),distance=str(integral))
  elif cid.startswith('mixed-R2'):
   d=abs(simpson(2,2,2,0,2))+abs(simpson(2,2,2,2,3));net_distance=simpson(2,2,2,0,3);assert d==F(46,3)and net_distance==-6;assert F(work['distance'])==d and F(work['displacement'])==net_distance
   assert row['dependency_evidence']['R4']['R2']==1;computed=dict(distance=str(d),displacement=str(net_distance),R2_gross=1,R2_net=0,R4_net=1)
  elif cid.startswith('polynomial-S2'):
   d=F(2*3**3,3)+F(3**2,2)+3*3;assert d==F(63,2)and F(work['distance'])==d;assert row['dependency_evidence']['S3']['S2']==1;computed=dict(distance=str(d),S2_gross=1,S2_net=0,S3_net=1)
  elif cid.startswith('mixed-outcome'):
   canonical=simpson(-1,4,3,0,3);legs=[simpson(-1,4,3,0,4),simpson(-1,4,3,4,5)];d=sum(map(abs,legs));net_dist=sum(legs)
   assert canonical==F(63,2)and d==F(77,2)and net_dist==F(185,6)
   assert all(F(work[k])==v for k,v in [('canonical_distance',canonical),('misread_distance',d),('misread_displacement',net_dist)])
   assert row['ledger'][0]['eligible']is False and row['net_total']==2;computed=dict(canonical_distance=str(canonical),misread_distance=str(d),misread_displacement=str(net_dist),canonical_score='2/6')
  misreads.append(dict(case_id=cid,net_score=sum(net.values()),tariff=row['tariff'],deducted_criterion=deduct,computed=computed,status='pass'))
 # Seven displayed R1/sample-credit examples, manually judged independent of helper.
 marking=read(H/'motion-marking-check.json');wanted=[1,4,4,3,3,1,0]
 assert [x['net_total']for x in marking['fixed_distance_cases']]==wanted
 vel=-t*t+t+12;assert vel.subs(t,0)==12 and vel.subs(t,3)==6 and vel.subs(t,S.Rational(1,2))==S.Rational(49,4)and S.diff(vel,t,2)==-2
 nc=[row for row in expected if row[1]>row[3]]
 assert all(0<F(r-c,2)<T for k,r,c,T in nc)
 assert all(k*(F(r-c,2)-r)*(F(r-c,2)+c)*k<0 for k,r,c,T in nc)
 assert 'or a vertex bound'not in b['official_qualifiers']['R1']and'earns no R1'in b['official_qualifiers']['R1']
 assert 'attempted primitive with both bounds'in b['official_qualifiers']['R5']
 assert 'gross dependencies'in b['official_qualifiers']['R4']
 old=read(P/'history/d3-candidate/work/nam-8227-nsscas-2026/workbench/planning/calculus-design.json')['recipes'][2]['branches'][-1]['accepted_tuple_keys'];old={tuple(map(int,r))for r in old};new=set(expected)
 assert (len(old&new),len(old-new),len(new-old))==(150,18,18)
 assert len({(k,k*(c-r),-k*r*c,T)for k,r,c,T in expected})==168
 inputs=[P/'calculus-design.json']+[H/n for n in ['motion-cases.json','motion-design-check.json','motion-separation.json','misread-policy-check.json','motion-marking-check.json']]+[W/'work-orders/WB8227-motion-integration.md',W/'exemplars/WB8227-motion-integration.md']
 result=dict(status='pass',audit_role='Second planner assistant; independently implemented arithmetic and expected gross/net evidence. Same vendor as author, not independent acceptance.',input_hashes={str(p.relative_to(W)):sha(p)for p in inputs},counts=dict(total=168,sign_change=144,no_change=24,minority='1/7',shapes=28,normalised_polynomials=14,directions=[84,84],key_retained=150,key_removed=18,key_added=18,legacy_calculus_sum=438),extended_separation_checks=tests,old_abs_ratio_ge4_lookup=dict(best_lookup_correct=old_shortcut[0],total=168,interpretation='This former shortcut never occurs in D4; majority baseline only.'),nine_marked_precision_sweeps=sweep_checks,exemplar_checks=examples,misread_checks=misreads,R1_fixture_credits=wanted,vertex_value_only_rejected_in_all_no_change_cases=True,all_tuple_answers=answers,limits=__doc__.strip())
 (H/'motion-independent-audit.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(status='pass',tuples=168,separation_tests=len(tests),sweeps=9,paper_cases=9,misread_fixtures=8,R1_fixed_cases=7),indent=2))
if __name__=='__main__':main()
