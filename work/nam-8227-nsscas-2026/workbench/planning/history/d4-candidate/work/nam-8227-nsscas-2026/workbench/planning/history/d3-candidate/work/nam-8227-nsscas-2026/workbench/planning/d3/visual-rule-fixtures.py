"""D3 arithmetic/format and declared-credit design probes.

These are synthetic feature facts and expected rubric credits, not a visual or
learner-response marker, app grading, or independent educational acceptance.
"""
from pathlib import Path
from decimal import Decimal, localcontext, ROUND_HALF_UP
import json
W=Path(__file__).resolve().parents[2]
def round3(x):
 with localcontext()as ctx:
  ctx.prec=80;x=Decimal(str(x));return x.quantize(Decimal(1).scaleb(x.adjusted()-2),rounding=ROUND_HALF_UP)if x else Decimal(0)
def follows_own_a(own_a,k,answer):return round3(answer)==round3(Decimal(str(own_a))*2*k)
ft=[]
for a,k,answers in [('3.80666248977',2,['15.23','15.2']),('3.81',2,['15.24','15.2']),('10.84',2,['43.36','43.4']),('11.52',2,['46.08','46.1']),('11.52',3,['69.12','69.1'])]:
 for answer in answers:
  assert follows_own_a(a,k,answer);ft.append(dict(own_a=a,k=k,answer=answer,expected='b:B2 eligible with correct visible2k scale',result='pass'))
assert not follows_own_a('3.81',2,'14.5')
format_rows=[]
for canonical,rejected in [('80.0','80'),('63.0','63')]:
 # Numericallyequal but explicit requested form differs.
 assert Decimal(canonical)==Decimal(rejected)and'.'in canonical and'.'not in rejected
 format_rows.append(dict(accepted=canonical,rejected=rejected,reason='Non-exact angle requires1dp raw form',result='pass'))
# This table records expected rubric allocations from explicit synthetic work facts.
expectations=[
 dict(case='modulus correct named fields,no wrong working',criteria={'a:B1':1,'a:B2':1,'a:B3':1},total=3),
 dict(case='modulus correct formula,no wrong working',criteria={'a:B1':1,'a:B2':1,'a:B3':1},total=3),
 dict(case='modulus validb,c then wrongparabola for a',criteria={'a:B1':0,'a:B2':1,'a:B3':1},total=2),
 dict(case='trap direct2kln(x-h), correcthenceproduct',criteria={'b:B1':1,'b:B2':1},total=2),
 dict(case='trap correctlogshape,wrongshift ln(x),asymptote0/intercept1',criteria={'c:B1':1,'c:B2':0,'c:B3':0},total=1),
 dict(case='trap owncurve/chordoverlay+briefgeometricstatement',criteria={'d:B1':1,'d:DB1':1},total=2),
 dict(case='trap multipleunlabelledfunctiongraphs,noidentifiableowncurve',criteria={'c:B1':0,'c:B2':0,'c:B3':0,'d:B1':0,'d:DB1':0},total=0),
 dict(case='trap unique requestedlabel amongmultiplefunctiongraphs,correctfeatures/ownreason',criteria={'c:B1':0,'c:B2':1,'c:B3':1,'d:B1':1,'d:DB1':1},total=4),
 dict(case='vector undistributedrestatementonly parta',criteria={'a:B1':0,'a:M1':0,'a:A1':0},total=0),
 dict(case='vector distributedscaledminusonly parta',criteria={'a:B1':1,'a:M1':0,'a:A1':0},total=1),
 dict(case='vector coherent OB sign misread, OD-6 once at a:B1',criteria={'a:B1':0,'a:M1':1,'a:A1':1,'b:B1':1,'b:M1':1,'b:M2':1,'b:A1':1},total=6),
 dict(case='trap changed case bare J=6T=69.0 without logarithm-law derivation',criteria={'b:B1':0,'b:B2':1},total=1),
 dict(case='trap normal k2 misread k3, correct logarithm and hence work, OD-6 first used in b',criteria={'b:B1':0,'b:B2':1},total=1)
]
for row in expectations:assert sum(row['criteria'].values())==row['total'];row['verification']='Declared credit totals reconcile; actual submission recognition remains an E/F/app fixture.'
result=dict(status='pass',scope=__doc__.strip(),own_a_arithmetic_checks=ft,precision_form_checks=format_rows,declared_marker_expectations=expectations)
(W/'planning/d3/visual-rule-fixtures.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print(json.dumps(dict(status='pass',FT_arithmetic_cases=len(ft),format_pairs=len(format_rows),rubric_expectations=len(expectations))))
