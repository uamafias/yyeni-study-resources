"""Independent fixed-response OD-6 examples; not an operational marker."""
import json,hashlib
from pathlib import Path
from fractions import Fraction
import sympy as s
P=Path(__file__).resolve().parents[1];ROOT=P.parents[3]
sources=[('NSSCAS 2025 report','Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf',345,343,'item 4: no maximum after misread; allocation not stated'),('Comparable Cambridge board convention','Question Banks/Cambridge Curricula/Cambridge AS and A Level/Mathematics (9709)/Pure Mathematics 1/2016/March (Variant 2)/9709_m16_ms_12.pdf',3,3,'Penalties: genuine unchanged-difficulty question misread, MR-1 from A/B, all A/B FT; own-figure error excluded')]
t=s.symbols('t',real=True);rows=[]
for V,k,T,misV in [(12,s.Rational(1,2),2,21),(18,s.Rational(1,3),3,81),(30,s.Rational(1,4),4,36)]:
 v=misV*s.exp(-k*t);a=s.diff(v,t);primitive=s.integrate(v,t);d=s.integrate(v,(t,0,T))
 assert s.simplify(s.diff(primitive,t)-v)==0
 gross={'E1':1,'E2':1,'E3':1,'E4':1,'E5':1};net={**gross,'E1':0};assert sum(net.values())==4
 rows.append(dict(case=f'exponential V={V} misread as {misV}',k=str(k),T=T,learner_work=dict(acceleration=str(a),primitive=str(primitive),distance=str(d)),eligibility='Same positive exponential and nonunit chain factor; same object/difficulty; original question V miscopied.',gross_awards=gross,deduction=dict(datum_id='V',first_use_part='acceleration',criterion='E1',amount=1),net_awards=net,parts={'acceleration':'1/2','distance':'3/3'},total='4/5',later_use='No second deduction from E3/E5.'))
# Edge decisions are executable assertions independent of canonical design fields.
def deduct(earned,types):
 result=earned.copy()
 for key in earned:
  if earned[key]>0 and types[key]in ['A','B']:result[key]-=1;return result,key
 return result,None
for earned,types,expected in [({'M1':1,'A1':1,'B1':1},{'M1':'M','A1':'A','B1':'B'},'A1'),({'E4':1},{'E4':'M'},None),({'A1':0,'M1':1},{'A1':'A','M1':'M'},None)]:
 after,key=deduct(earned,types);assert key==expected and min(after.values())>=0
guards=[dict(case='No A/B earned in first-use part',earned={'E4':1},MR_deduction=0,total='1 method mark; no negative/borrowed deduction'),dict(case='Own-figure slip after correct derivative/integral',treatment='Ordinary accuracy error, no MR; unchanged correct awards survive'),dict(case='k misread as zero',treatment='Changes exponential calculus to constant velocity; no MR concession, normal canonical marking'),dict(case='Answer only on misread V',earned={},MR_deduction=0,total='0/5 by OD-1; FT never invents working'),dict(case='Primitive coefficient used as derivative',treatment='Named E2 exclusion survives; genuine V misread cannot rescue it'),dict(case='Several uses of one misread V',treatment='One first-use ledger entry; no later-part second deduction'),dict(case='Incorrect numerical root on no-change case',treatment='Ordinary method slip, not a datum misread: R1/R2/R3=3/4, R4 www lost despite canonical total')]
out=dict(status='pass',policy='OD-6',unit='once per misread datum in first-use part',selection='earliest eligible earned A/B in declared part/award order',sources=[dict(title=title,source_path=path,source_sha256=hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),pdf_page=pdf,printed_page=printed,authority=note,verification='Root inspected native rendered page; comparable Cambridge allocation is adopted by owner, not represented as NSSCAS published allocation')for title,path,pdf,printed,note in sources],motion_exemplar_misreads=rows,edge_fixtures=guards,independence='Separate CAS differentiation and definite integration; scoring is manual fixed-criterion evidence with a small independent deduction check, not runtime marker acceptance.')
(P/'d3/misread-policy-check.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print('OD-6: three independently recalculated exponential misreads and seven edge fixtures pass')
