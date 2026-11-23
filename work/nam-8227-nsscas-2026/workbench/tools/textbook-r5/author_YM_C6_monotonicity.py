"""YM286–289: derivative-sign intervals,domain qualifications,and first rate."""
import json
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;GRAD=h.GRAD;CHAIN='8227:2020:M1:T8:O02:D02';MONO='8227:2020:M1:T8:O03:D02';RATE='8227:2020:M1:T8:O03:D03';extra=h.extra
def add(kind,n,page,note,parts,direct,components=None,powers=None):
 r=h.add(kind,n,page,note,parts,direct,components or[],powers=powers or[])
 r['mapping_rationale']='The required increasing/decreasing sign set is distinct from solving fprime=0alone. Keep the original domain and pole-separated components. A derivative may vanish at isolated points of a strictly increasing function. A physical rate uses the requested variable and units,not just a polynomial derivative label.'
 return r
def interval(label,fn,sign,key,kp):
 p=v(label,'0',key,kp,'Differentiate the ORIGINAL function and solve the strict derivative-sign inequality,as the source key does. The roots split the real line into sign intervals;test the factor signs and retain every interval. These open sign sets do not assert that a stationary endpoint cannot belong to a larger monotonic interval.')
 p['operation']={'kind':'inequality','operands':[f'diff({fn},x){sign}0']}
 p.update(assessed_8227_demand_ids=[MONO],component_demand_ids=[POWER],original_function=fn,source_derivative_sign=sign);return p
def derivative(label,fn,key,kp):
 p=h.deriv(label,fn,key,kp);p.update(assessed_8227_demand_ids=[POWER],component_demand_ids=[]);return p
def explain(label,result,method,kp,prove=False):
 p=reasoning(label,result,method,kp,'show/prove'if prove else'matches');p.update(assessed_8227_demand_ids=[MONO],component_demand_ids=[POWER],response_format='explanation');return p

add('Example',16,286,'Find strict positive-gradient region forx²+10x+5andnegative-gradient region for8−6x−3x².',[
 interval('a','x**2+10*x+5','>','Interval.open(-5,oo)',286),interval('b','8-6*x-3*x**2','<','Interval.open(-1,oo)',286)],[MONO],[POWER],['2','1'])
add('Try-Now-16',1,286,'Find positive-gradient regions for two given quadratics,including reversal of a negative-coefficient inequality.',[
 interval('a','5*x**2-10*x+3','>','Interval.open(1,oo)',620),interval('b','5-7*x-2*x**2','>','Interval.open(-oo,-Rational(7,4))',620)],[MONO],[POWER],['2','1'])
add('Try-Now-16',2,287,'Find negative-gradient regions for two independently given quadratic curves.',[
 interval('a','3*x**2-12*x+7','<','Interval.open(-oo,2)',620),interval('b','8-3*x-x**2','<','Interval.open(-Rational(3,2),oo)',620)],[MONO],[POWER],['2','1'])
add('Example',17,287,'For4x³−15x²−72x+5,find both positive and negative derivative regions from roots−3/2and4.',[
 interval('a','4*x**3-15*x**2-72*x+5','>','Union(Interval.open(-oo,-Rational(3,2)),Interval.open(4,oo))',287),interval('b','4*x**3-15*x**2-72*x+5','<','Interval.open(-Rational(3,2),4)',287)],[MONO],[POWER],['3','2','1'])
add('Try-Now-17',1,288,'Forx³−12x²+45x+6,retain both exterior positive-gradient intervals and the interior negative-gradient interval.',[
 interval('a','x**3-12*x**2+45*x+6','>','Union(Interval.open(-oo,3),Interval.open(5,oo))',620),interval('b','x**3-12*x**2+45*x+6','<','Interval.open(3,5)',620)],[MONO],[POWER],['3','2','1'])
add('Try-Now-17',2,288,'Forx³+3x²−24x+11,use the two derivative roots−4and2to find both sign sets.',[
 interval('a','x**3+3*x**2-24*x+11','>','Union(Interval.open(-oo,-4),Interval.open(2,oo))',620),interval('b','x**3+3*x**2-24*x+11','<','Interval.open(-4,2)',620)],[MONO],[POWER],['3','2','1'])
add('Try-Now-17',3,288,'Find where(1/6)(2x−3)³−4xhas positive gradient,using both squared-factor branches.',[
 interval('positive-gradient','Rational(1,6)*(2*x-3)**3-4*x','>','Union(Interval.open(-oo,Rational(1,2)),Interval.open(Rational(5,2),oo))',620)],[MONO],[CHAIN],['3','1'])
ps=[derivative('a-derivative','(3*x+2)**3-5','9*(3*x+2)**2',288),explain('a-explanation','Increasing on the stated domainx>=0.','The ORIGINAL domain restrictsx>=0. Thus3x+2>=2and9(3x+2)²>=36>0. The zero of the squared derivative atx−2/3lies OUTSIDE that domain,so it cannot invalidate the strict sign statement here.',288),derivative('b-derivative','3/(2*x+5)','-6/(2*x+5)**2',288),explain('b-explanation','Decreasing separately on(−infinity,−5/2)and(−5/2,infinity).','The ORIGINAL polex−5/2is excluded. On each connected component the denominator square is positive and the derivative is negative. This is NOT a global decreasing order on the disconnected union: f(−3)=−3butf(−2)=3. Preserve the separate components before adapting the source assertion.',288)]
ps[2]['assessed_8227_demand_ids']=[CHAIN];ps[2]['component_demand_ids']=[POWER]
extra(ps[3],'cross-pole-counterexample','Tuple(3/(2*(-3)+5),3/(2*(-2)+5))','Tuple(-3,3)')
r=add('Example',18,288,'Differentiate a shifted cube onx>=0and a rational function with a pole,then justify the derivative sign. The rational monotonicity assertion must be read componentwise.',ps,[POWER,CHAIN,MONO],[],['3','−1'])
r['source_domain_caution']='Source says the rational function is decreasing without stating the connected-component qualification;keep the pole-separated intervals explicit.'
ps=[derivative('derivative','6/(2*x+3)','-12/(2*x+3)**2',621),explain('explanation','Decreasing on the stated domain[0,infinity).','For originalx>=0,the denominator2x+3>=3ispositive,so the derivative−12/(2x+3)²isstrictlynegative everywhere in the domain. The source domain has no pole or disconnected branch.',621)]
ps[0]['assessed_8227_demand_ids']=[CHAIN];ps[0]['component_demand_ids']=[POWER]
add('Try-Now-18',1,289,'Obtain the derivative of6/(2x+3)and explain decreasing behaviour on its statedx>=0domain.',ps,[CHAIN,MONO],[POWER],['−1'])
p=explain('proof','The gradient is never negative;the cubic is strictly increasing despite one zero gradient.','Original y=3x³−6x²+4x+2has derivative9x²−12x+4=(3x−2)²>=0. Equality holds only atx2/3;there is no negative-gradient interval. To justify strict increase rather than merely nondecrease,note the integral of this continuous square over ANY nonzero interval is positive,or use the positive shifted-cube form. Do not claim the derivative is strictlypositive at every point.',621,True)
extra(p,'derivative-square','diff(3*x**3-6*x**2+4*x+2,x)-(3*x-2)**2','0')
extra(p,'shifted-cube','expand((3*x-2)**3/9+Rational(26,9))-(3*x**3-6*x**2+4*x+2)','0')
add('Try-Now-18',2,289,'Show that the cubic3x³−6x²+4x+2never has negative gradient;retain its isolated zero rather than substituting a false strict-positive claim.',[p],[MONO],[POWER],['3','2','1'])
p=v('dV-dt','diff(Rational(4,3)*t**3-Rational(3,4)*t**2+2*t+3,t).subs(t,2)','15',289,'Differentiate the ORIGINAL Vpolynomial with respect tot,then substitutet2:4t²−(3/2)t+2gives15. No physical measurement units are specified for this example,so do not invent cubic-centimetres per second from the preceding illustration.')
p.update(assessed_8227_demand_ids=[RATE],component_demand_ids=[POWER],differentiation_variable='t',source_units='not stated in this example')
add('Example',19,289,'Find dV/dtatt2from V=(4/3)t³−(3/4)t²+2t+3,keeping the requested variable and unstated units.',[p],[RATE],[POWER],['3','2','1'])

refs=[
 (21,286,'Six monotonicity example curves','Three schematic increasing andthree decreasing graphs illustrate sign. Positive derivative is sufficient on an interval;strict increase doesnotrequire it to be positive at EVERY point,as laterTry18Q2shows.',[MONO],'graph',[],None),
 (22,286,'Increasing then decreasing peak','The source graphy=t(x)rises forx<aandfallsforx>a;its tangent is horizontal at the marked peak. Increasing/decreasing areintervalproperties,not assertions about the sign of the ordinate.',[MONO],'graph',[],None),
 (23,287,'Derivative quadratic sign sketch','Example17derivativeis6(2x²−5x−12),withroots−3/2and4andpositiveleadingcoefficient. Above-axis exterior regions correspond to positive original-function gradient.',[MONO],'graph',[('factor(diff(4*x**3-15*x**2-72*x+5,x))','6*(2*x+3)*(x-4)')],'Example:17'),
 (24,287,'Original-function and derivative comparison','The original cubic increases where its DERIVATIVE graph is above the axis. Original-function ysign is irrelevant;critical abscissas belong to derivative zeros,not necessarily original zeros.',[MONO],'graph',[],'Example:17'),
 (25,288,'Example18a squared derivative sketch','9(3x+2)²touches0atx−2/3,but the ORIGINAL stated domain isx>=0,where the derivative isstrictlypositive. Preserve the source domain when reusing this panel.',[MONO],'graph',[('diff((3*x+2)**3-5,x)','9*(3*x+2)**2')],'Example:18'),
 (26,288,'Example18b derivative-sign sketch','−6/(2x+5)²isnegativeonbothcomponents,butundefinedatthepole−5/2. The source schematic is derivative-sign support,not evidence of global monotonic order across a missing point.',[MONO],'graph',[('diff(3/(2*x+5),x)','-6/(2*x+5)**2')],'Example:18'),
 (27,289,'Cylinder versus cone depth/time comparison','Both containers have totalvolume100cm³,height10cm,andconstantinflow10cm³/s. Author-derived depthh=tforcylinder,andh=(100t)^(1/3)forcone,t0..10s. Both reach10cmat10s;conicaldepthrisesfastinitiallythenslows. These formulas are independent feature checks,not transcribed book answers.',[RATE],'diagram',[('10*10','100'),('100*(10/10)**3','100'),('10**3/10','100')],None)]
for n,page,label,note,teaches,rep,checks,parent in refs:
 fig(n,page,label,note,teaches,rep,checks,parent);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:')if r['parent_item_id']else None
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['item_kind']='teaching-figure'
 r['mathematical_feature_review']['method']='Inspect original curve/derivative labels,axis location,domain and quantitative depth/time labels. Recompute derivative signs or the geometric volume-depth relation independently;never measure schematic curve heights or treat a zero derivative as a sign change without checking.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllExamples16–19,Try16Q1/2,Try17Q1–3,Try18Q1/2,andsevenmonotonicity/rate reference panels are enumerated over286–289. Sign-interval and global monotonicity qualifications are explicit;the cylinder/cone formulas are author-derived feature checks.',scope_screen='Prescribed derivative-sign intervals andrates. Preservex>=0domains,polecomponents,isolatedzero-gradient behaviour,and stated versusunstatedunits. No formal first-principles proof is required.')for page in range(286,290)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-monotonicity.json',dict(scope='All286–289explicit tasks.',items=answers)),('census-YM-C6-monotonicity.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete286–289page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
