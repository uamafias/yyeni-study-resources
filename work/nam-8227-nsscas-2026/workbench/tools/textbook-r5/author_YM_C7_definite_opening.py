"""YM334–337: second-order recovery,hence reverse derivatives and definite integrals."""
import json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra,integral
from author_Goldie_C5_opening import definite
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
INT=h.INT;CONST='8227:2020:M1:T9:O02:D01';CURVE='8227:2020:M1:T9:O02:D02';CHAIN='8227:2020:M1:T8:O02:D02';REV2='8227:2020:M2:T5:O01:D03';DEF='8227:2020:M1:T9:O03:D01'
def val(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[],response_format='symbolic',given_representation='text');return p
def add(kind,n,page,note,parts,powers=None):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 comp=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 return h.add(kind,n,page,note,parts,direct,comp,powers=powers)
p=val('curve','integrate(integrate(12/x**3,x)+Rational(3,2),x)+4','6/x+3*x/2+4',626,[CURVE,CONST],'Integrate ORIGINAL fsecond12/x³. Stationary x2 imposes fprime(2)=0 and fixes c1=3/2. Integrate again and impose f(2)=10 to fix c2=4. The given point selects x>0;the negative component has independent constants.',[INT])
extra(p,'original-second-and-point','Tuple(diff(6/x+3*x/2+4,x,2)-12/x**3,diff(6/x+3*x/2+4,x).subs(x,2),(6/x+3*x/2+4).subs(x,2))','Tuple(0,0,10)')
add('Try-Now-11',1,334,'Recover f from second derivative12/x³ and stationary point(2,10),requiring TWO constants and both constraints.',[p],['−3','−2','−1'])
ps=[val('a-derivative','integrate(24/x**3-4,x)+11','-12/x**2-4*x+11',626,[CONST],'Integrate ORIGINAL ysecond24/x³−4. The supplied stationary abscissa2 gives yprime2=0,so c1=11. No original curve ordinate is given in(a).',[INT]),val('b-P','Tuple(2,(integrate(-12/x**2-4*x+11,x)-8).subs(x,2))','Tuple(2,12)',626,[CURVE,CONST],'Integrate the independently recovered first derivative. Original point(1,13)fixes c2−8. Evaluate the SAME curve at the known stationary abscissa2 to obtain P(2,12).',[INT])]
extra(ps[0],'stationary-condition','(-12/x**2-4*x+11).subs(x,2)','0')
extra(ps[1],'given-point','(12/x-2*x**2+11*x-8).subs(x,1)','13')
r=add('Try-Now-11',2,334,'Find first derivative from a second derivative and stationary abscissa,then use a separate curve point to find the stationary ordinate.',ps,['−3','0','−2','1','−1']);r['connected_part_structure']='First integration and stationary condition in(a)fix the first constant. Point(1,13)in(b)fixes the second.'

for kind,n,fn,integrand,key,kp,note in [
 ('Example',12,'1/(x**2-5)','4*x/(x**2-5)**2','-2/(x**2-5)',334,'Differentiate1/(x²−5),then HENCE integrate4x/(x²−5)²;the target integrand is−2times the obtained derivative.'),
 ('Try-Now-12',1,'1/(4-2*x**3)','3*x**2/(4-2*x**3)**2','1/(2*(4-2*x**3))',626,'Differentiate1/(4−2x³),then HENCE integrate3x²/(4−2x³)²;the derivative coefficient6requires scale1/2.'),
 ('Try-Now-12',2,'(2*x**2-1)**6','x*(2*x**2-1)**5','(2*x**2-1)**6/24',627,'Differentiate(2x²−1)^6,then HENCE integratex(2x²−1)^5;the derivative coefficient24requires scale1/24.'),
 ('Try-Now-12',3,'(x**2-4*x+5)**6','2*(2*x-4)*(x**2-4*x+5)**5','(x**2-4*x+5)**6/3',627,'Differentiate(x²−4x+5)^6,then HENCE integrate2(2x−4)(x²−4x+5)^5;the quadratic(x−2)²+1has no real zero.')]:
  # Key derivatives are independent printed transcriptions,not generated from fn.
  derivative={12:'-2*x/(x**2-5)**2',1:'6*x**2/(4-2*x**3)**2',2:'24*x*(2*x**2-1)**5',3:'6*(2*x-4)*(x**2-4*x+5)**5'}[n]
  ps=[val('a',f'diff({fn},x)',derivative,kp if kind!='Example'else 334,[CHAIN],'Differentiate the ORIGINAL given composite using the chain rule,retaining inner derivative and original denominator exclusions.'),integral('b',integrand,key,kp if kind!='Example'else 334)]
  ps[1].update(assessed_8227_demand_ids=[REV2],component_demand_ids=[CHAIN],given_derivative_function=fn,required_method='Hence:recognise a constant multiple of the derivative established in(a). No general substitution selection is required.')
  r=add(kind,n,334,note,ps)
  r.update(mapping_rationale='Part(a)directly asks chain-rule differentiation. Part(b)directly asks reverse recognition from that established derivative,not direct powers of a LINEAR inner expression. The supplied hence structure is retained.',connected_part_structure='Typed cue a→b:hence. The exact constant multiple must be reconciled.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT07',status='not applicable',quoted_value=note,reason='The source supplies the antiderivative target via an explicit derivative/hence pair;it does not require selecting a general substitution.')])

def dv(label,f,lo,hi,key,kp):
 p=definite(label,f,lo,hi,key,kp);p.update(assessed_8227_demand_ids=[DEF],component_demand_ids=[INT],given_representation='text',response_format='numeric',original_integrand=f,original_bounds=[str(lo),str(hi)])
 return p
add('Example',13,336,'Three proper finite integrals:constant3 on[1,5],6√x on[0,4],and(x³−4x)/x⁵ on[2,3]. The rational interval excludes its pole0.',[
 dv('a','3',1,5,'12',336),dv('b','6*sqrt(x)',0,4,'32',336),dv('c','(x**3-4*x)/x**5',2,3,'Rational(4,81)',336)],['0','1/2','−2','−4'])
add('Try-Now',13,336,'Six proper finite integrals,including a zero lower endpoint with finite square-root powers,nonzero denominator intervals,and2/fourthrootx on[1,16].',[
 dv('a','2',1,4,'6',627),dv('b','2*x**2',1,3,'Rational(52,3)',627),dv('c','2*x**Rational(3,2)',0,9,'Rational(972,5)',627),dv('d','3*x-1',4,6,'28',627),dv('e','2/x**Rational(1,4)',1,16,'Rational(56,3)',627),dv('f','(2*x**2-6)/x**2',2,4,'Rational(5,2)',627)],['0','2','3/2','1','−1/4','−2'])
add('Example',14,337,'Evaluate two proper integrals:combined reciprocal/root terms on[1,4],and4/√(5−2x)on[−2,2]. Its root denominator never vanishes on the interval.',[
 dv('a','(2/sqrt(x)+1/x)/x',1,4,'Rational(11,4)',337),dv('b','4/sqrt(5-2*x)',-2,2,'8',337)],['−3/2','−2','−1/2'])
ps=[dv('a','sqrt(x)*(x+2)',0,4,'Rational(352,15)',627),dv('b','(x+8)*(3-x)/x**4',1,2,'Rational(37,8)',627),dv('c','(3*x-2)**5',-1,2,'-Rational(1281,2)',627),dv('d','(x-1)**Rational(3,2)',1,2,'Rational(2,5)',627)]
p=reasoning('e','The integral diverges to positive infinity;it has no finite proper value. The printed−16/11is invalid endpoint subtraction across x=−2/3.',
 'The ORIGINAL integrand4/(3x+2)² is positive and has a second-order pole inside[−1,3]. Split at−2/3. With primitive−4/(3(3x+2)),both one-sided integrals tend to+∞ independently. Finite endpoint subtraction gives−16/11,which cannot equal the integral of a positive function and ignores the internal singularity. This source part cannot be used as an ordinary finite-integral exemplar.',627,'key wrong')
p.update(assessed_8227_demand_ids=[],component_demand_ids=[DEF],given_representation='text',response_format='numeric',printed_key_normalised='-Rational(16,11)',original_integrand='4/(3*x+2)**2',original_bounds=['-1','3'],original_domain='x≠−2/3;the specified bounds cross the pole.',source_interpretation='Defective finite-integral exercise;retain internal diagnosis,not valid task coverage.')
extra(p,'left-improper-limit','limit(-4/(3*(3*(-Rational(2,3)-a)+2))-Rational(4,3),a,0,dir="+")','oo')
extra(p,'right-improper-limit','limit(-Rational(4,33)+4/(3*(3*(-Rational(2,3)+a)+2)),a,0,dir="+")','oo')
extra(p,'invalid-endpoint-subtraction','-Rational(4,33)-Rational(4,3)','-Rational(16,11)')
ps.append(p);ps.append(dv('f','4/sqrt(1-2*x)',-4,0,'8',627))
r=add('Try-Now',14,337,'Six displayed finite integrals. Five are proper;part(e)crosses a second-order pole and its negative finite key is invalid. Preserve this source defect and both one-sided divergent limits.',ps,['3/2','1/2','−2','−3','−4','5','3/2','−1/2'])
r['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['Part(e)is defective as a finite-integral task:internal pole at−2/3. It supplies no valid ordinary definite-integral coverage.'])
r['source_domain_caution']='The key applies the fundamental theorem through a pole in(e). Both one-sided improper integrals diverge+∞;do not classify the endpoint difference as an integral.'

refs=[(9,335,'Definite-integral evaluation and constant cancellation','For∫₃⁶x²dx,the SAME primitive x³/3+c at both endpoints gives63;the same constant cancels. The theorem requires a valid common interval,not passage through a pole.',[DEF],'table',[('integrate(x**2,(x,3,6))','63')]),(10,335,'Definite-integral linearity,orientation and interval additivity','Constant multiples and sums/differences preserve proper integrability;reversing bounds changes the sign;adjacent compatible intervals add. None of these rules repairs an internal singularity. A signed integral is geometric area only with appropriate sign/region conditions.',[DEF],'table',[])]
for n,page,label,note,teaches,rep,checks in refs:
 fig(n,page,label,note,teaches,rep,checks,None);figures[-1].update(item_id=f'8227:TB:YM:C7:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All Try11Q1–2,Example12,Try12Q1–3,definite-integral reference panels,Examples13–14 andTry13–14 enumerated over334–337. Each hence pair preserves its dependency and exact multiplier. The source statement definiteintegral=area requires sign qualifications.',scope_screen='Fixed-curve reconstruction,chain/reverse-derivative pairs,and proper finite integrals. Try14(e)is explicitly excluded as a defective finite exemplar;the divergent diagnosis does not create new syllabus coverage.')for page in range(334,338)]
h.pages=pages
if __name__=='__main__':h.save('definite-opening','Complete rendered334–337census;valid integrals independently recomputed,and internal-pole defect diagnosed.')
