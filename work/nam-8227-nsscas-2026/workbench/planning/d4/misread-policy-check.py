"""Independent D4 motion mathematics plus derived fixed-evidence MR ledgers.

No answer parser, production marker or runtime recipe is implemented here.
"""
import json,hashlib
from pathlib import Path
import sympy as s
from misread_ledger import settle,award
P=Path(__file__).resolve().parents[1];W=P.parent;t=s.symbols('t',real=True)
def datum(id,first,eligible=True,reason='Same object and difficulty; genuine printed datum miscopied.',**extra):return dict(datum_id=id,eligible=eligible,first_use_part=first,reason=reason,**extra)
rows=[]
for V,k,T,misV in [(12,s.Rational(1,2),2,21),(18,s.Rational(1,3),3,81),(30,s.Rational(1,4),4,36)]:
 v=misV*s.exp(-k*t);acc=s.diff(v,t);F=s.integrate(v,t);distance=s.integrate(v,(t,0,T));assert s.simplify(s.diff(F,t)-v)==0
 awards=[award(id,'acceleration'if id in ['E1','E2']else'distance',typ,datum_ids=['V'])for id,typ in [('E1','B'),('E2','B'),('E3','B'),('E4','M'),('E5','A')]]
 ledger=settle(awards,[datum('V','acceleration',canonical_value=V,misread_value=misV)])
 assert ledger['net_total']==4 and ledger['ledger'][0]['deducted_criterion']=='E1'
 rows.append(dict(case_id=f'exponential-{V}-read-{misV}',work=dict(acceleration=str(acc),primitive=str(F),distance=str(distance)),**ledger))
# The named -V/k error removes both first-part B marks. The MR penalty moves
# to the first later earned A/B on the same V, rather than disappearing.
awards=[award(id,'acceleration'if id in ['E1','E2']else'distance',typ,earned=0 if id in ['E1','E2']else 1,datum_ids=['V'])for id,typ in [('E1','B'),('E2','B'),('E3','B'),('E4','M'),('E5','A')]]
ledger=settle(awards,[datum('V','acceleration',canonical_value=12,misread_value=21)])
assert ledger['gross_total']==3 and ledger['net_total']==2 and ledger['ledger'][0]['deducted_criterion']=='E3'
rows.append(dict(case_id='exponential-misread-plus-wrong-reciprocal-derivative',work=dict(wrong_acceleration='-42*exp(-t/2)',correct_misread_primitive='-42*exp(-t/2)',correct_misread_distance='42-42/exp(1)'),reason='E1 wrong coefficient and E2 named primitive-coefficient exclusion; correct distance work earns E3/E4/E5 before MR.',**ledger))
# Same direction-change outcome: constant -2 is copied as -8.
v=2*t*t-8;F=s.integrate(v,t);legs=[s.integrate(v,(t,0,2)),s.integrate(v,(t,2,3))];distance=sum(abs(x)for x in legs);net=s.integrate(v,(t,0,3));assert distance==s.Rational(46,3)and net==-6
awards=[award('R1','distance','M',datum_ids=['constant']),award('R2','distance','B',datum_ids=['constant']),award('R3','distance','DM',datum_ids=['constant'],depends_on=['R1']),award('R4','distance','A',datum_ids=['constant'],depends_on=['R2','R3']),award('R5','displacement','M',datum_ids=['constant']),award('R6','displacement','A',datum_ids=['constant'],depends_on=['R5'])]
ledger=settle(awards,[datum('constant','distance',canonical_value=-2,misread_value=-8,reason='Both canonical and misread quadratic have one interior root and require the same two-leg decomposition.')]);assert ledger['net_total']==5 and ledger['net_awards']['R2']==0 and ledger['net_awards']['R4']==1
rows.append(dict(case_id='mixed-R2-net-deduction-keeps-R4-gross-dependency',work=dict(velocity=str(v),roots=['-2','2'],primitive=str(F),signed_legs=list(map(str,legs)),distance=str(distance),displacement=str(net)),**ledger))
# Polynomial distance T changes while the first velocity part is unaffected.
v=2*t*t+t+3;dist=s.integrate(v,(t,0,3));assert dist==s.Rational(63,2)
awards=[award('V1','velocity','M'),award('V2','velocity','A'),award('V3','velocity','A'),award('S1','distance','M',datum_ids=['T']),award('S2','distance','A',datum_ids=['T']),award('S3','distance','A',datum_ids=['T'],depends_on=['S1','S2'])]
ledger=settle(awards,[datum('T','distance',canonical_value=2,misread_value=3)]);assert ledger['net_total']==5 and ledger['net_awards']['S2']==0 and ledger['net_awards']['S3']==1
rows.append(dict(case_id='polynomial-S2-net-deduction-keeps-S3-gross-dependency',work=dict(velocity=str(v),distance=str(dist)),**ledger))
# A changed direction decision changes the object. Canonical marking persists.
v=-t*t+t+12;F=s.integrate(v,t);mislegs=[s.integrate(v,(t,0,4)),s.integrate(v,(t,4,5))];misdist=sum(abs(x)for x in mislegs);misnet=sum(mislegs);assert misdist==s.Rational(77,2)and misnet==s.Rational(185,6)
awards=[award('R1','distance','M',0,['T'],basis='canonical'),award('R2','distance','B',1,['T'],basis='canonical'),award('R3','distance','DM',0,['T'],['R1'],basis='canonical'),award('R4','distance','A',0,['T'],['R2','R3'],basis='canonical'),award('R5','displacement','M',1,['T'],basis='canonical'),award('R6','displacement','A',0,['T'],['R5'],basis='canonical')]
ledger=settle(awards,[datum('T','distance',False,'Canonical no-change interval becomes a two-leg reversal interval; object changes and eligibility stays false in displacement.',canonical_value=3,misread_value=5)]);assert ledger['net_total']==2 and ledger['ledger'][0]['amount']==0
rows.append(dict(case_id='mixed-outcome-flipping-T-ineligible-canonical-throughout',work=dict(canonical_interval=[0,3],canonical_distance='63/2',misread_interval=[0,5],misread_distance=str(misdist),misread_displacement=str(misnet)),reason='R1 misses the canonical interval decision; R2 is the correct supplied-velocity primitive; R3 dependency fails and R4 total is wrong. R5 earns an attempted definite primitive evaluation method with two bounds, R6 canonical accuracy fails:2/6, no MR concession.',**ledger))
# No A/B anywhere: retain a demonstrated method without a negative penalty.
awards=[award('E1','acceleration','B',0,['V']),award('E2','acceleration','B',0,['V']),award('E3','distance','B',0,['V']),award('E4','distance','M',1,['V']),award('E5','distance','A',0,['V'])]
ledger=settle(awards,[datum('V','acceleration')]);assert ledger['net_total']==1 and ledger['ledger'][0]['amount']==0
rows.append(dict(case_id='no-AB-anywhere-no-negative-deduction',**ledger))
negative=[]
def rejects(name,fn):
 try:fn()
 except AssertionError as e:negative.append(dict(seed=name,result='rejected',reason=str(e)))
 else:raise AssertionError('seed passed '+name)
rejects('duplicate-datum-double-charge',lambda:settle([award('B','a','B',datum_ids=['x'])],[datum('x','a'),datum('x','a')]))
rejects('dependency-cascade-counted-as-gross-evidence',lambda:settle([award('R2','a','B',0,['x']),award('R4','a','A',1,['x'],['R2'])],[datum('x','a')]))
rejects('ineligible-datum-reintroduced-as-FT',lambda:settle([award('B','b','B',datum_ids=['x'],basis='misread')],[datum('x','a',False,'Task object changes')]))
rejects('method-mark-cannot-be-MR-source',lambda:settle([award('X','a','MR',datum_ids=['x'])],[datum('x','a')]))
assert len(negative)==4
source= json.loads((P/'d3/misread-policy-check.json').read_text())['sources']
out=dict(status='pass',owner_principle='OD-6',operational_rule='MR03-OPS-D4 proposed; exact-manifest approval pending',sources=source,motion_cases=rows,negative_fixtures=negative,dependency_rule='All gross evidence, DM and www dependency tests precede the single net MR deduction.',limits='Mathematics independently differentiated/integrated; author-specified fixed gross evidence drives a derived ledger, not a learner submission marker or independent acceptance.')
(P/'d4/misread-policy-check.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(status='pass',motion_ledgers=len(rows),negative_fixtures=len(negative))))
