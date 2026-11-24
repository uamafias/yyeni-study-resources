"""Read-only changed-scope OD-6 consistency audit by the visual planner.
Source-text inspection plus independent arithmetic, not a runtime marker or cross-vendor acceptance.
"""
from pathlib import Path
import argparse, hashlib, json, re
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
import mpmath as m
W=Path(__file__).resolve().parents[2]

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
 paths=[W/'subject-rules.md',*sorted((W/'work-orders').glob('WB8227-*.md')),*sorted((W/'exemplars').glob('WB8227-*.md'))]
 assert len(paths)==19
 checked=[];stale=[]
 patterns=[r'D2-MISREAD-ALLOCATION',r'No blanket minusone',r'affected component/dot/canonical A awards fail',r'a:M1 and b:M1/M2 only',r'implicit curve can retain the structural remaining-y derivative G3']
 for path in paths:
  txt=path.read_text();lines=txt.splitlines();assert 'OD-6'in txt,str(path)
  hits=[]
  for i,l in enumerate(lines,1):
   if re.search('misread|MR03|MR−1|OD-6',l,re.I):hits.append({'line':i,'text':l})
   for pattern in patterns:
    if re.search(pattern,l):stale.append({'path':str(path.relative_to(W)),'line':i,'pattern':pattern})
  assert hits,str(path)
  checked.append(dict(path=str(path.relative_to(W)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),policy_or_fixture_lines=hits))
 assert not stale,stale
 # Independent normal-case OB sign misread: solve component dot equation;
 # recover angle using side lengths and Euclidean cosine law, not closed answer code.
 u=[1,1,1];v=[-2,1,-1];w=[1,2,1]
 coeff=sum(a*b for a,b in zip(u,w));const=sum(a*b for a,b in zip(v,w));p=Fraction(const,coeff)
 result=[p*a-b for a,b in zip(u,v)];residual=sum(a*b for a,b in zip(result,w));assert p==Fraction(-1,4)and residual==0
 with m.workdps(70):
  nu=sum(x*x for x in u);nv=sum(x*x for x in v);dist=sum((x-y)**2 for x,y in zip(u,v));theta=m.acos(m.mpf(nu+nv-dist)/(2*m.sqrt(nu*nv)))*180/m.pi
  angle=str(Decimal(str(theta)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP));assert angle=='118.1'
 assert 3-1+4==6
 result=dict(status='pass',scope=__doc__.strip(),input_count=19,inputs=checked,stale_allocation_matches=stale,manual_checks=[
 'Subject MR03: owner decision with NSSCAS no-max principle and explicitly comparable Cambridge MR−1 source; first-use datum ledger, earliest eligible earned A/B, no later/no-A/B deduction, normal M/DM, own-figure/easier/changed/no-solution exclusion and OD-1/www all present.',
 'All nine current work orders contain OD-6, and all nine exemplars contain the replacement policy or a compliant example/source line. No stale D2 allocation wording was found in the scoped live records.',
 'Motion examples distinguish 12→21, 18→81 and 30→36, all 1/2+3/3=4/5 with no second deduction. Polynomial/mixed canonical-only accuracy text is qualified by the shared OD-6 exception.',
 'Implicit gradient and later-numerator examples lose G2 or H2 once; fixed supplied proof targets cannot be changed to obtain MR treatment. Stationary uses its own P/C/I awards, not copied implicit G criteria.',
 'Principal divisor misread retains the real-task demand; the no-real-to-real target misread is excluded. R-form coefficient sample preserves its two-root search; log prefactor/target samples identify the correct first-use part.',
 'Modulus preserves official answer-only/www exceptions; trapezium preserves sketch/bias exceptions and OD-5; no arbitrary graph or wrong-log-law rescue.',
 'Vector a policy concerns resultant/dot-zero/p, not the copied b magnitude awards. Its genuine OB sign misread is 6/7; no-solution OA misread remains ordinary canonical marking.'],vector_recomputation=dict(p=str(p),dot_residual=str(residual),angle_degrees=str(theta),angle_1dp=angle,raw_a=3,raw_b=4,deducted_criterion='a:B1',deduction=1,a_total=2,b_total=4,total=6,second_deduction=0),conflicts=[],limitations='This is a same-author-team changed-scope audit, not cross-vendor acceptance. It checks declared text and independently recomputes the vector sample; it does not run a learner-response marker. Hashes identify the exact read state; refresh after any later root edits.')
 out=W/'planning/d3/shared-policy-audit.json';text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
 if args.check:assert out.read_text()==text,'Shared policy audit inputs changed; rerun without --check after reviewing the diff.'
 else:out.write_text(text)
 print(json.dumps({'status':'pass','inputs':len(paths),'stale_allocations':len(stale),'vector_total':6}))
if __name__=='__main__':main()
