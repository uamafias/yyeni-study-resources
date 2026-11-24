"""Independent D3 changed-example arithmetic and synthetic credit bookkeeping.
Not a learner-response marker, runtime generator or independent content acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP
import argparse, json, hashlib, subprocess, sys
import mpmath as m
W=Path(__file__).resolve().parents[2];P=W/'planning';m.mp.dps=75

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vector(u,v,w):
 # Separate componentwise linear-system computation, angle by Euclidean cosine law.
 coefficient=sum(u[i]*w[i] for i in range(3));constant=sum(v[i]*w[i] for i in range(3))
 if not coefficient:return {'p':None,'solvable':constant==0,'equation_constant':constant}
 p=F(constant,coefficient);resultant=[p*u[i]-v[i]for i in range(3)];assert dot(resultant,w)==0
 a,b=dot(u,u),dot(v,v);distance=dot([x-y for x,y in zip(u,v)],[x-y for x,y in zip(u,v)])
 theta=m.acos(m.mpf(a+b-distance)/(2*m.sqrt(a*b)))*180/m.pi
 return dict(p=str(p),angle_degrees=str(theta),angle_1dp=str(Decimal(str(theta)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP)),residual=str(dot(resultant,w)))
def sig3(x):
 d=Decimal(str(x));return str(d.quantize(Decimal(1).scaleb(d.adjusted()-2),rounding=ROUND_HALF_UP))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
 doc=json.loads((P/'visual-design.json').read_text());assert sum(len(b['part_specs'])for r in doc['recipes']for b in r['branches'])==7
 assert all('OD-6'in q['misread_policy']for r in doc['recipes']for b in r['branches']for q in b['part_specs'])
 assert all(r['proposed_version']=='0.1.3'for r in doc['recipes'])
 assert all(q['bloom']['classification_version']=='8227-pilot-design-0.1.1'for r in doc['recipes']for b in r['branches']for q in b['part_specs'])
 old=json.loads((P/'d2/visual-domain-checks.json').read_text());new=json.loads((P/'d3/visual-domain-checks.json').read_text())
 for a,b in zip(old['branches'],new['branches']):assert a['admitted']==b['admitted']and a['removed']==b['removed']
 v=vector([1,1,1],[-2,1,-1],[1,2,1]);assert v['p']=='-1/4'and v['angle_1dp']=='118.1'
 impossible=vector([1,-2,1],[-3,1,-1],[1,1,1]);assert impossible==dict(p=None,solvable=False,equation_constant=-3)
 width=m.mpf(4)/2;nodes=[2,4,6];T=m.fsum([(nodes[i+1]-nodes[i])*(m.log(nodes[i]-1)+m.log(nodes[i+1]-1))/2 for i in range(2)])
 J=m.fsum([(nodes[i+1]-nodes[i])*(3*m.log((nodes[i]-1)**2)+3*m.log((nodes[i+1]-1)**2))/2 for i in range(2)])
 assert abs(J-6*T)<m.mpf('1e-70')and sig3(J)=='22.8';assert Decimal('3.81')*6==Decimal('22.86')
 # These credit ledgers are synthetic facts of fully specified work, not recognition tests.
 credits=[
 dict(case='vector genuine question OB sign misread, fully correct misread work',pre_deduction={'a:B1':1,'a:M1':1,'a:A1':1,'b:B1':1,'b:M1':1,'b:M2':1,'b:A1':1},deduct_from='a:B1',deduction=1,total=6,part_totals={'a':2,'b':4},same_datum_later_part_deduction=0),
 dict(case='vector learner own dot misread as -2 after correct question data and a',pre_deduction={'a:B1':1,'a:M1':1,'a:A1':1,'b:B1':0,'b:M1':1,'b:M2':1,'b:A1':0},deduction=0,total=5,reason='Own figures: ordinary accuracy marking, not MR.'),
 dict(case='vector OA sign misread leaves no p; a zero-dot setup only',pre_deduction={'a:B1':0,'a:M1':1,'a:A1':0},deduction=0,total=1,reason='No solution changes object: normal canonical marking.'),
 dict(case='eligible genuine misread, only method earned and no A/B in first-use part',pre_deduction={'a:B1':0,'a:M1':1,'a:A1':0},deduction=0,total=1,later_deferred_penalty=0),
 dict(case='misread makes requested work easier; wrong resultant p(OA-OB) is not a copied datum',pre_deduction={'a:B1':0,'a:M1':1,'a:A1':0},deduction=0,total=1,reason='Named wrong method uses normal canonical marking; no MR rescue.'),
 dict(case='trapezium k2 read as k3, correct log derivation and product, other parts complete',pre_deduction={'a':3,'b:B1':1,'b:B2':1,'c':3,'d':2},deduct_from='b:B1',deduction=1,total=9),
 dict(case='trapezium changed bare J=6T=6(11.5), no visible log-law reasoning',pre_deduction={'b:B1':0,'b:B2':1},deduction=0,total=1,reason='B2 scale product is shown; B1 log law is absent.'),
 dict(case='eligible datum also used later, full first-use A/B and full later work',pre_deduction={'a:B1':1,'a:M1':1,'a:A1':1,'b:B1':1,'b:B2':1},deduct_from='a:B1',deduction=1,total=4,same_datum_later_part_deduction=0),
 dict(case='eligible misread with named erroneous working and unsupported final only',pre_deduction={'a:B1':0,'a:M1':0,'a:A1':0},deduction=0,total=0,reason='OD-1 and www still apply; no invented A/B earned to deduct.')]
 for c in credits:assert sum(c['pre_deduction'].values())-c['deduction']==c['total']
 pool=[row for row in new['branches'][2]['admitted']if row['parameters']['h']!=2]
 # Every single generated example exposes one of the two available sketch keys.
 exposure=[]
 examples=json.loads((P/'visual-design-asset-checks.json').read_text())['exemplar_cases']
 for e in examples:
  if not e['recipe_id'].endswith('trapezium-sketch-estimate'):continue
  row=next(q for q in pool if q['parameters']==e['parameters']);remaining=[q for q in pool if all(q['part_keys'][part]!=row['part_keys'][part]for part in 'abcd')]
  assert remaining and len({r['parameters']['h']for r in remaining})==1
  exposure.append(dict(example=e['case_id'],remaining_presentations=len(remaining),strict_generated_fresh_packing_after_example=1))
 sources=[]
 for path in [Path('Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf'),next(Path('Question Banks/Cambridge Curricula/Cambridge AS and A Level/Mathematics (9709)').rglob('9709_m16_ms_12.pdf'))]:
  sources.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),page=345 if 'NSSCAS'in str(path)else 3,role='OD-6 authority; native page read is recorded by coordinating PLANNER, not newly claimed by this arithmetic check.'))
 negative=[]
 for seed in ['modulus-parabola','vector-wrong-resultant','trapezium-original','trapezium-original-part','trapezium-original-sketch','trapezium-precision-collision']:
  r=subprocess.run([sys.executable,str(P/'d3/visual-domain-checks.py'),'--negative-fixture',seed],capture_output=True,text=True);assert r.returncode!=0
  negative.append(dict(seed=seed,rejected=True,exit_code=r.returncode))
 result=dict(status='pass',limits=__doc__.strip(),visual_part_count=7,versions='0.1.3; classification 8227-pilot-design-0.1.1 unchanged',domain_unchanged=True,vector_genuine_misread_recomputation=v,vector_no_solution_recomputation=impossible,trapezium_k_misread_recomputation=dict(T=str(T),J=str(J),J_3sf=sig3(J),reported_a_product='22.86'),credit_ledgers=credits,generated_fresh_exposure_checks=exposure,sources=sources,seeded_negatives=negative)
 out=P/'d3/visual-d3-independent-checks.json';text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
 if args.check:assert out.read_text()==text
 else:out.write_text(text)
 print(json.dumps(dict(status='pass',new_math_samples=3,credit_ledgers=len(credits),negative_fixtures=len(negative),visual_parts=7)))
if __name__=='__main__':main()
