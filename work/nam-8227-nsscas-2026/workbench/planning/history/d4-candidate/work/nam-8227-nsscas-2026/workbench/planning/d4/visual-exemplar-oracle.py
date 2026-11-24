"""Independent paper-example oracle: recover from points, sum areas, cosine law.

No imports from an answer constructor or domain-check module. Not a generator.
"""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext,ROUND_HALF_UP
import argparse,json
import mpmath as mp
WB=Path(__file__).resolve().parents[2]

def sig(x,n=3):
 with localcontext()as c:
  c.prec=85;d=Decimal(str(x))
  if not d:return '0'
  return format(d.quantize(Decimal(1).scaleb(d.adjusted()-n+1),rounding=ROUND_HALF_UP),'f')

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();data=json.loads((WB/'planning/visual-design-asset-checks.json').read_text());rows=[]
 for case in data['exemplar_cases']:
  p=case['parameters'];e=case['expected_answers'];id=case['recipe_id'];proof={}
  if id.endswith('modulus-graph-recovery'):
   vx,vy=e['vertex'];zx,zy=e['zeros'][0];bb=-vx;cc=vy;aa=Fraction(zy-vy,abs(zx-vx));assert aa==e['a']and bb==e['b']and cc==e['c']
   pts=[e['vertex'],*e['zeros'],e['y_intercept']];assert all(aa*abs(x+bb)+cc==y for x,y in pts)
   proof=dict(method='Recover slope from independently supplied vertex and zero, then check every labelled point; no use of c=-ad answer builder.',coefficients=[str(aa),bb,cc],point_residuals=[str(aa*abs(x+bb)+cc-y)for x,y in pts])
  elif id.endswith('trapezium-sketch-estimate'):
   h,L,n,k=[p[x]for x in['h','L','n','k']]
   with mp.workdps(80):
    xx=[mp.mpf(h+1)+mp.mpf(L)*j/n for j in range(n+1)];areas=[(xx[j+1]-xx[j])*(mp.log(xx[j]-h)+mp.log(xx[j+1]-h))/2 for j in range(n)];T=mp.fsum(areas);J=mp.fsum([(xx[j+1]-xx[j])*(k*mp.log(xx[j]**2-2*h*xx[j]+h*h)+k*mp.log(xx[j+1]**2-2*h*xx[j+1]+h*h))/2 for j in range(n)]);truth=mp.quad(lambda x:mp.log(x-h),[h+1,h+1+L]);assert abs(T-mp.mpf(e['a_exact_log_value']))<mp.mpf('1e-70')and abs(J-2*k*T)<mp.mpf('1e-70')and truth>T
    assert sig(T)==e['a_3sf']and sig(J)==e['b_3sf'];ft=Decimal(e['a_3sf'])*(2*k);accepted={sig(J),format(ft,'f'),sig(ft)};assert accepted==set(e['b_canonical_path_fixture_strings'])
    assert e['c']['intercept']==[h+1,0]and e['c']['asymptote']=='x='+str(h)
    proof=dict(method='Independent individual trapezium-area sums for original and transformed integrands; numerical quadrature of original integral for bias.',a_3sf=sig(T),b_canonical_3sf=sig(J),b_canonical_path_fixture_strings=sorted(accepted,key=Decimal),b_FT_rule="Evaluate against learner own(a), not this fixture list",positive_bias_residual=str(truth-T),asymptote='x='+str(h),intercept=[h+1,0])
  else:
   r,s,t=[p[x]for x in['r','s','t']];u=[1,r,1];v=[s,1,-1];w=[1,t,1];coef=sum(x*y for x,y in zip(u,w));const=sum(x*y for x,y in zip(v,w));pp=Fraction(const,coef);assert str(pp)==e['a'];result=[pp*x-y for x,y in zip(u,v)];assert sum(x*y for x,y in zip(result,w))==0 and r!=t and pp!=0
   nu=sum(x*x for x in u);nv=sum(x*x for x in v);dist=sum((x-y)**2 for x,y in zip(u,v))
   with mp.workdps(80):
    angle=mp.acos(mp.mpf(nu+nv-dist)/(2*mp.sqrt(nu*nv)))*180/mp.pi
    with localcontext()as c:
     c.prec=85;ang=str(Decimal(str(angle)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP))
    assert ang==e['b_1dp']
    proof=dict(method='Solve perpendicularity by dot coefficient/constant independently; angle by Euclidean A-B distance and cosine law, not the closed dot numerator.',p=str(pp),norm_squares=[nu,nv],distance_AB_squared=dist,angle_1dp=ang,perpendicular_residual='0')
  assert sum(v for k,v in case['expected_marks'].items()if k!='total')==case['expected_marks']['total']
  rows.append(dict(recipe_id=id,branch_id=case['branch_id'],case_id=case['case_id'],result='pass',oracle=proof))
 assert len(rows)==9
 result=dict(status='pass',scope='Nine repaired paper-design examples; separate point-recovery/area-sum/numerical-integral/Euclidean-cosine-law oracle, not runtime marking acceptance.',cases=rows)
 p=WB/'planning/d4/visual-exemplar-oracle.json';text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
 if args.check:assert p.read_text()==text,'stale visual exemplar oracle report'
 else:p.write_text(text)
 print(json.dumps(dict(status='pass',cases=len(rows)),indent=2))
if __name__=='__main__':main()
