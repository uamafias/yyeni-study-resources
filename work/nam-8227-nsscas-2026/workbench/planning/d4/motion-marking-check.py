"""Fixed-response D4 R1/gross-evidence checks, not learner-response assessment."""
import json,argparse
from pathlib import Path
import sympy as s
from misread_ledger import settle,award
P=Path(__file__).resolve().parents[1];t=s.symbols('t',real=True)
ap=argparse.ArgumentParser();ap.add_argument('--negative-fixture',choices=['vertex-only-R1','dependency-cascade']);args=ap.parse_args()
v=-t*t+t+12;vertex=s.solve(s.diff(v,t),t)[0]
assert vertex==s.Rational(1,2)and 0<vertex<3 and s.diff(v,t,2)==-2
endpoints=[v.subs(t,x)for x in [0,3]];extremum=v.subs(t,vertex)
assert min(endpoints)==6 and extremum>s.Max(*endpoints)
R1_vertex=1 if args.negative_fixture=='vertex-only-R1'else 0
assert R1_vertex==0,'vertex value alone is an upper bound here, not a positive lower bound'
def distance_awards(r1,r2,r3,r4):return [award('R1','distance','M',r1),award('R2','distance','B',r2),award('R3','distance','DM',r3,depends_on=['R1']),award('R4','distance','A',r4,depends_on=['R2','R3'])]
rows=[]
for label,vector,score,reason in [
 ('vertex-only-argument-with-correct-primitive',(0,1,0,0),1,'The positive interior maximum alone never establishes positive velocity across the whole interval; R1=0, dependent R3/R4=0.'),
 ('endpoints-plus-concavity-no-root-solving',(1,1,1,1),4,'v(0)=12,v(3)=6 and concavity down bound v below by its positive endpoint chord.'),
 ('correct-no-change-proof-plus-harmless-interior-partition',(1,1,1,1),4,'A correct sign argument and primitive justify nonnegative leg magnitudes; no mark is discretionary.'),
 ('one-slip-false-root-remains-outside',(1,1,1,0),3,'Method solve/check and one-leg primitive survive; R4www fails the false root unless a separate complete correct sign argument is supplied.'),
 ('one-slip-false-interior-root-canonical-total',(1,1,1,0),3,'Same-sign leg magnitudes may sum canonically; this coincidence cannot repair false root working.'),
 ('root-check-and-calculator-legs-only',(1,0,0,0),1,'No attempted primitive; only the decision method is evidenced.'),
 ('numeric-only-canonical-distance',(0,0,0,0),0,'OD-1 supplies no inferred method/accuracy evidence.')]:
  result=settle(distance_awards(*vector),[]);assert result['net_total']==score
  rows.append(dict(case_id=label,reason=reason,**result))
if args.negative_fixture=='dependency-cascade':
    from importlib.machinery import SourceFileLoader
    # Deliberately contrary to the declared net-after-evidence rule.
    gross={'R2':1,'R3':1,'R4':1};net={'R2':0,'R3':1,'R4':0}
    assert net['R4']==gross['R4'],'net MR deduction cascaded into R4'
doc=dict(status='pass',fixed_distance_cases=rows,independent_math=dict(velocity=str(v),interval=[0,3],vertex=str(vertex),vertex_value=str(extremum),endpoint_values=list(map(str,endpoints)),concavity='down; endpoint chord is a positive lower bound, vertex is an upper bound'),scope='Declared fixed response credit and separately computed geometry; no handwritten-response recognizer or operational marker.')
(P/'d4/motion-marking-check.json').write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n');print('D4 motion:7fixed-credit cases and independent endpoint/vertex geometry pass')
