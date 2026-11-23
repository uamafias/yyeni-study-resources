"""YM394–399: remainder constraints, factor proofs, factorisation and cubic roots."""
import author_YM_C8_opening as h
from author_YM_C8_polynomial_division import ev,division,pair
from author_YM_C8_opening import W,pp,v,fig,figures,extra,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
h.common.base.ev=ev
answers=h.answers
REM='8227:2020:M2:T1:O04:D01';FAC='8227:2020:M2:T1:O04:D02';COEFF='8227:2020:M2:T1:O04:D03';SOLVE='8227:2020:M2:T1:O04:D04';QR='8227:2020:M2:T1:O03:D03'
def coeff(label,original,conditions,unknowns,key,kp,component=REM):
 target='FiniteSet(*solve(['+','.join(conditions)+'],('+','.join(unknowns)+',),set=True)[1])'
 p=v(label,target,key,kp,'Apply the stated divisor-root/factor/remainder conditions to the ORIGINAL polynomial. Solve all resulting simultaneous conditions and retain every admissible real parameter tuple. Re-substitute each tuple into the original conditions, keeping ordered coefficient pairs together.')
 p.update(original_polynomial=original,original_parameter_conditions=conditions,unknown_order=unknowns,assessed_8227_demand_ids=[COEFF],component_demand_ids=[component],response_format='symbolic')
 return p
def factor(label,original,key,kp,variable='x'):
 p=v(label,'factor('+original+')',key,kp,'Factor the ORIGINAL polynomial, then independently expand every displayed factor to recover all original coefficients. A factor theorem proof uses an actual divisor root and zero remainder. Merely selecting a factor from its appearance is not a proof.')
 p.update(original_polynomial=original,source_variable=variable,assessed_8227_demand_ids=[FAC],response_format='symbolic')
 extra(p,'source-factor-reconstruction','expand(('+key+')-('+original+'))','0')
 return p
def proof(label,original,divisor,kp):
 p=v(label,'rem('+original+','+divisor+',x)','0',kp,'Show the actual remainder is zero, retaining the original divisor. For a nonmonic linear factor, evaluate at its exact root. For the quadratic factor in Try21(c), perform the requested long division and reconstruct the product; one zero evaluation alone cannot establish both linear factors.')
 p.update(check_mode='show/prove',original_polynomial=original,original_divisor=divisor,assessed_8227_demand_ids=[FAC],response_format='proof/show-that')
 return p
def roots(label,original,key,kp):
 p=v(label,'solveset('+original+',x,domain=S.Reals)',key,kp,'Use the actual factor theorem to find a zero, divide out that linear factor, then solve the remaining quadratic and retain ALL real roots. Substitute the complete root set into the ORIGINAL cubic. A displayed sign typo in later working must not change the original equation.')
 p.update(original_polynomial=original,assessed_8227_demand_ids=[SOLVE],component_demand_ids=[FAC],response_format='symbolic')
 return p
def add(kind,n,page,note,parts,division_request=False):
 r=h.add(kind,n,page,note,parts)
 direct=set(r['assessed_8227_demand_ids']);r['component_demand_ids']=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-direct)
 r.update(mapping_rationale='Separate the requested coefficient tuple, zero-remainder proof, full factorisation and equation roots. The theorem used as a method is a component when only a coefficient/result is requested. Connected parts remain within their original item. A general polynomial remainder theorem has no blanket degree-four restriction from the different division objective.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT05',status='within'if division_request else'not applicable',quoted_value=note,reason='The actual explicitly requested division is cubic or quartic by linear/quadratic; all supporting divisions also satisfy the bound.'if division_request else'The stated output is a theorem evaluation, coefficient condition, factorisation or cubic solution, not a separately requested long division. Example18 has degree5 but uses only the remainder theorem.')])
 return r
add('Example',18,394,'Quintic x⁵−3x⁴+px²+5x+6 has remainder2 underx+1. Evaluate at−1 to obtain p=5; the theorem task does not become a prohibited degree-five division request.',[coeff('p','x**5-3*x**4+p*x**2+5*x+6',['(x**5-3*x**4+p*x**2+5*x+6).subs(x,-1)-2'],['p'],'FiniteSet(Tuple(5))',394)])
ps=[coeff('a-m','x**3-x**2+p*x+11',['(x**3-x**2+p*x+11).subs(x,-2)-3'],['p'],'FiniteSet(Tuple(-2))',634),coeff('b-m','2*x**3+x**2+p*x-5',['(2*x**3+x**2+p*x-5).subs(x,-1)+8'],['p'],'FiniteSet(Tuple(2))',634)]
for p in ps:p['source_parameter_names']={'p':'m'}
add('Try-Now-18',1,394,'Two independent coefficient m conditions: remainders3 at root−2 and−8 at root−1. Original source m is represented by checker p without changing the polynomial.',ps)
add('Try-Now-18',2,394,'For2px²−p²x−14, remainder10 at root3 gives TWO admissible parameters p=2,4; no positive-root-only filtering is invented.',[coeff('p-values','2*p*x**2-p**2*x-14',['(2*p*x**2-p**2*x-14).subs(x,3)-10'],['p'],'FiniteSet(Tuple(2),Tuple(4))',634)])
p=coeff('m-n','x**3+2*x**2+p*x+n',['(x**3+2*x**2+p*x+n).subs(x,1)-4','(x**3+2*x**2+p*x+n).subs(x,-2)-16'],['p','n'],'FiniteSet(Tuple(-5,6))',394);p['source_parameter_names']={'p':'m','n':'n'}
add('Example',19,394,'The cubic has remainders4 underx−1 and16 underx+2. Solve the ordered pair m=−5,n=6; each remainder has its own divisor-root input.',[p])
p=v('k-n','Tuple(solve(2-k-6+7,k)[0],log(81)/log(3))','Tuple(3,4)',634,'P(1)=−7 gives k=3 because1ⁿ=1 for polynomial integer n≥0. Then P(−3)=129 gives(−3)ⁿ=81. Its sign requires even n; |−3|ⁿ=3⁴ and injectivity for positive base3 give n=4. Verify both original remainder values; do not accept a complex-log branch.')
p.update(assessed_8227_demand_ids=[COEFF],component_demand_ids=[REM],original_polynomial='2*x**n-k*x**2-6',parameter_domain='n is a nonnegative integer because the source expression is a polynomial;k real.',response_format='symbolic')
extra(p,'original-remainder-values','Tuple((2*x**4-3*x**2-6).subs(x,1),(2*x**4-3*x**2-6).subs(x,-3))','Tuple(-7,129)')
add('Try-Now-19',1,395,'Unknown coefficient k and polynomial exponent n are fixed by remainders−7 at1 and129 at−3. Preserve the integer exponent/parity reasoning, giving k3,n4.',[p])
f='2*x**4-a*x**3-8*x**2+b*x+5'
add('Try-Now-19',2,395,'Quartic remainder−4 at root3 and exact remainder17/8 at the NONMONIC divisor2x+1 root−1/2 fix a4,b3.',[coeff('a-b',f,[f'({f}).subs(x,3)+4',f'({f}).subs(x,-Rational(1,2))-Rational(17,8)'],['a','b'],'FiniteSet(Tuple(4,3))',634)])
f='x**3+a*x**2+b*x-7'
add('Try-Now-19',3,395,'The cubic has equal remainders at2 and−1, and remainder3 at−2. Keep the equal-remainder relation rather than silently setting either one to zero; obtain a2,b−5.',[coeff('a-b',f,[f'({f}).subs(x,2)-({f}).subs(x,-1)',f'({f}).subs(x,-2)-3'],['a','b'],'FiniteSet(Tuple(2,-5))',634)])
f='2*x**3-4*x**2+a*x+b'
ps=[coeff('a-coefficients',f,[f'({f}).subs(x,-1)-4',f'({f}).subs(x,3)-12'],['a','b'],'FiniteSet(Tuple(-4,6))',634)]
ps+=pair('b','2*x**3-4*x**2-4*x+6','x**2-2','2*x-4','-2',634)
for p in ps[1:]:p['depends_on_source_parts']=['a-coefficients']
add('Try-Now-19',4,395,'First determine a−4,b6 from two remainders. Then divide that same cubic byx²−2, preserving the connected quotient2x−4 and remainder−2.',ps,True)
f='x**3-5*x+b'
add('Example',20,395,'Remainder at−3 is TWICE the remainder at2, fixing b−8. The multiplier applies to the whole second remainder, including its constant.',[coeff('b',f,[f'({f}).subs(x,-3)-2*({f}).subs(x,2)'],['b'],'FiniteSet(Tuple(-8))',395)])
f='2*x**3-5*x**2+2*a*x+52';g='x**3+3*a*x**2+11*x-6'
add('Try-Now-20',1,395,'Two different polynomials have equal remainders under the SAME divisorx−2. Equate their values at2 to obtain a3.',[coeff('a',f+' ; '+g,[f'({f}).subs(x,2)-({g}).subs(x,2)'],['a'],'FiniteSet(Tuple(3))',634)])
f='x**3+3*x**2-2*x+a'
add('Try-Now-20',2,395,'The same cubic has remainder R at2 and2R at−2. Eliminate the unspecified R by retaining P(−2)=2P(2); a=−24.',[coeff('a',f,[f'({f}).subs(x,-2)-2*({f}).subs(x,2)'],['a'],'FiniteSet(Tuple(-24))',634)])
add('Example',21,396,'Show x−2 is a factor ofx³−x−6 by its zero remainder, rather than merely listing a known root.',[proof('show-factor','x**3-x-6','x-2',396)])
add('Try-Now-21',1,396,'Prove factors2x−1,x−2 and quadraticx²−4x+3 of the three original polynomials. Part(c) explicitly hints LONG DIVISION; a single linear-root substitution is insufficient for that quadratic factor.',[proof('a','2*x**3-x**2+2*x-1','2*x-1',635),proof('b','2*x**3-3*x**2+3*x-10','x-2',635),proof('c','x**4-3*x**3-x+3','x**2-4*x+3',635)],True)
add('Try-Now-21',2,396,'Two factor conditions independently fix coefficient a: root3 gives−7 in(a), root−2 gives−8 in(b).',[coeff('a','2*x**3+a*x**2+2*x+3',['(2*x**3+a*x**2+2*x+3).subs(x,3)'],['a'],'FiniteSet(Tuple(-7))',635,FAC),coeff('b','2*x**3+x**2+a*x-4',['(2*x**3+x**2+a*x-4).subs(x,-2)'],['a'],'FiniteSet(Tuple(-8))',635,FAC)])
f='2*x**3+p*x**2+n*x+5';p=coeff('m-n',f,[f'({f}).subs(x,1)',f'({f}).subs(x,-5)'],['p','n'],'FiniteSet(Tuple(7,-14))',635,FAC);p['source_parameter_names']={'p':'m'}
add('Try-Now-21',3,396,'Two distinct factorsx−1,x+5 determine m7,n−14. The source m parameter is represented by checker p.',[p])
add('Example',22,397,'Factorise2x³+3x²−3x−2 using the factor theorem. Root1 gives a zero-remainder division and the remaining quadratic splits into(x+2)(2x+1).',[factor('factors','2*x**3+3*x**2-3*x-2','(x-1)*(x+2)*(2*x+1)',397)])
data=[('a','2*x**3+5*x**2+x-2','(x+1)*(2*x-1)*(x+2)','x'),('b','2*x**3-9*x**2+7*x+6','(x-2)*(2*x+1)*(x-3)','x'),('c','a**3-1','(a-1)*(a**2+a+1)','a'),('d','x**3+2*x**2-29*x+42','(x-2)*(x+7)*(x-3)','x'),('e','5*x**3-9*x**2-17*x-3','(x+1)*(5*x+1)*(x-3)','y'),('f','2*x**3+a*x**2-8*a**2*x-4*a**3','(2*x+a)*(x-2*a)*(x+2*a)','x'),('g','2*x**3+a*x**2-13*a**2*x+6*a**3','(2*x-a)*(x+3*a)*(x-2*a)','x')]
add('Try-Now',22,397,'Seven complete factorisations include different source variables and symbolic-parameter coefficients. In(c), a²+a+1 has no real roots; in(f),(g), exact factor identities remain valid at a0 where factors coalesce.',[factor(l,f,k,635,var)for l,f,k,var in data])
f='2*x**3+a*x**2+b'
add('Example',23,398,'Combine factorx+1 (zero remainder at−1) with nonzero remainder−5 at−2. Solve a3,b−1 while preserving their different roles.',[coeff('a-b',f,[f'({f}).subs(x,-1)',f'({f}).subs(x,-2)+5'],['a','b'],'FiniteSet(Tuple(3,-1))',398)])
f='x**3-x**2+a*x+b'
ps=[coeff('a-coefficients',f,[f'({f}).subs(x,-1)',f'({f}).subs(x,2)-12'],['a','b'],'FiniteSet(Tuple(2,4))',635),factor('b-factors','x**3-x**2+2*x+4','(x+1)*(x**2-2*x+4)',635)]
ps[1]['depends_on_source_parts']=['a-coefficients']
add('Try-Now-23',1,398,'First find a2,b4 from one factor and one nonzero remainder. Then factorise the resulting SAME cubic; its quadratic factor is irreducible over the reals.',ps)
f='2*x**3-3*x**2+a*x+b';ps=[coeff('a-coefficients',f,[f'({f}).subs(x,2)',f'({f}).subs(x,-2)+20'],['a','b'],'FiniteSet(Tuple(-3,2))',635),division('b-remainder','2*x**3-3*x**2-3*x+2','x**2-4','5*x-10',635,'remainder')]
ps[1]['depends_on_source_parts']=['a-coefficients']
add('Try-Now-23',2,398,'First derive a−3,b2, then find only the remainder5x−10 underx²−4. The quotient is not asked, and is not added as a learner response.',ps,True)
f='x**3+4*x**2-a*x+b'
add('Try-Now-23',3,398,'A factorx+2 and remainder a³ underx−a give TWO admissible ordered parameter pairs: a−4/3,b−16/3 and a2,b−12. The divisor root depends on the unknown parameter itself.',[coeff('a-b',f,[f'({f}).subs(x,-2)',f'({f}).subs(x,a)-a**3'],['a','b'],'FiniteSet(Tuple(-Rational(4,3),-Rational(16,3)),Tuple(2,-12))',635)])
f='2*x**3-x**2+p*x+q'
add('Try-Now-23',4,398,'Quadratic2x²+x−1 is a factor of the cubic. Its distinct roots1/2,−1 give p−2,q1. Both root conditions establish the whole supplied quadratic factor.',[coeff('p-q',f,[f'({f}).subs(x,Rational(1,2))',f'({f}).subs(x,-1)'],['p','q'],'FiniteSet(Tuple(-2,1))',635,FAC)])
p=roots('all-roots','6*x**3-23*x**2+16*x-3','FiniteSet(3,Rational(1,3),Rational(1,2))',399)
p['source_working_warning']='The final narrative repeats the cubic with +23x², unlike the original −23x² and correct displayed factors. Solve the original, not that copied-sign typo.'
add('Example',24,399,'Solve the ORIGINAL6x³−23x²+16x−3=0 by factor theorem. Its three rational roots3,1/3,1/2 match the correct factorisation; a later copied equation changes the quadratic sign incorrectly.',[p])
data=[('a','2*x**3+3*x**2-8*x+3','FiniteSet(1,Rational(1,2),-3)'),('b','12*x**3-20*x**2+x+3','FiniteSet(Rational(1,2),Rational(3,2),-Rational(1,3))'),('c','2*x**3-7*x**2+2*x+3','FiniteSet(1,-Rational(1,2),3)'),('d','6*x**3+19*x**2+x-6','FiniteSet(1,-Rational(1,2),3)')]
parts=[roots(l,f,k,635)for l,f,k in data]
parts[-1].update(author_expected_normalised='FiniteSet(-3,-Rational(2,3),Rational(1,2))',source_interpretation='Native key repeats1,−1/2,3. None solves the original part(d); correct factorisation is(x+3)(3x+2)(2x−1).')
add('Try-Now',24,399,'Solve four cubics explicitly using the factor theorem. Retain each complete real root set; a rational candidate denominator may divide the leading coefficient, not only the constant.',parts)
refs=[(42,394,'Example18 remainder coefficient substitution','Evaluate at−1, including all odd-power signs; −3+p=2 givesp5.',[COEFF],'table','Example:18'),(43,394,'Example19 linked remainder equations','m+n=1 and−2m+n=16 form one simultaneous system for the same polynomial; two different numeric remainders are not zero-factor conditions.',[COEFF],'table','Example:19'),(44,395,'Example20 doubled-remainder relation','P(−3)=2P(2) gives b−12=2b−4 and b−8. Double the full remainder, not only its variable term.',[COEFF],'table','Example:20'),(45,396,'Factor theorem reference and nonmonic typo','Forax−b witha≠0, P(b/a)=0 proves factorax−b. The source conclusion mistakenly printsax−c, introducing an undefined constant.',[FAC],'table',None),(46,396,'Try21 quadratic-factor long-division hint','A quadratic factor requires an exact zero remainder for the whole divisor, or two distinct root conditions. The source asks long division inQ1(c).',[FAC],'table','Try-Now-21:1'),(47,397,'Example22 rational-factor trial list','Candidate rational roots come from numerator divisors of the constant and denominator divisors of the leading coefficient. Zero substitution proves the selected factor.',[FAC],'table','Example:22'),(48,397,'Example22 long/synthetic division alternatives','Dividing byx−1 gives2x²+5x+2 and zero remainder. Either displayed division method supports the same factorisation, not a new family.',[FAC],'table','Example:22'),(49,398,'Example23 simultaneous parameter equations','Factor conditiona+b2 and nonzero-remainder condition4a+b11 yielda3,b−1.',[COEFF],'table','Example:23'),(50,398,'Try23 quadratic-factor hint','Factor2x²+x−1=(2x−1)(x+1) and use BOTH root conditions to determinep,q.',[COEFF],'table','Try-Now-23:4'),(51,399,'Example24 trial factors and zero-remainder division','Root3 reduces the original cubic to6x²−5x+1=(3x−1)(2x−1). Both division layouts agree.',[SOLVE],'table','Example:24'),(52,399,'Example24 final equation sign typo','The concluding sentence prints+23x² although original/division/factors have−23x². The complete original roots remain3,1/3,1/2.',[SOLVE],'table','Example:24')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C8:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C8:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read actual theorem conditions, divisor roots and every connected coefficient system from rendered pages. Recompute original conditions and expand factored results. Keep copied source-sign/notation defects separate from correct final answers.'
h.pages=[dict(pdf_page=page,printed_page=pp(page),chapter=8,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='Every Example18–24,Try18–24 and all independently numbered questions/connected parts enumerated, with eleven theorem/method panels.',scope_screen='Polynomial theorem conditions and original rational roots preserved. Only actual requested divisions inherit LIMIT05; quintic Example18 is a theorem evaluation.')for page in range(394,400)]
if __name__=='__main__':h.save('theorems','Complete394–399 theorem, coefficient, factorisation and cubic-equation census; no extra unrequested quotient outputs.')
