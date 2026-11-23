"""YM330–333: initial conditions,tangent/normal constraints and two integrations."""
import json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
INT=h.INT;REV=h.REV;CONST='8227:2020:M1:T9:O02:D01';CURVE='8227:2020:M1:T9:O02:D02';TANGENT='8227:2020:M1:T8:O03:D01';COORD='8227:PRIOR:NSSCO:coordinate-geometry';POINT='8227:2020:M1:T8:O04:D01'
def val(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[],response_format='symbolic',given_representation='text');return p
def curve(label,f,x0,y0,key,kp):
 primitive=f'integrate({f},x)'
 p=val(label,f'({primitive})-({primitive}).subs(x,{x0})+({y0})',key,kp,[CURVE,CONST],
  'Integrate the ORIGINAL supplied derivative,then use the ACTUAL point to determine the constant. This fixed curve is compared exactly,not up to an arbitrary additive constant. Check its derivative and point independently. A point fixes a constant only on its connected domain component.',[INT])
 p.update(original_derivative=f,given_point=[str(x0),str(y0)])
 extra(p,'point-incidence',f'({key}).subs(x,{x0})-({y0})','0')
 extra(p,'derivative-consistency',f'simplify(diff({key},x)-({f}))','0')
 return p
def add(kind,n,page,note,parts,powers,components=None):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 component=sorted(({d for p in parts for d in p.get('component_demand_ids',[])}|set(components or[]))-set(direct))
 r=h.add(kind,n,page,note,parts,direct,component,powers=powers)
 r['mapping_rationale']='Initial-condition recovery directly tests the integration constant AND the fixed curve. Basic antiderivative work is a component of that requested reconstruction,not another independently requested output. Tangent/normal and point-location outputs are direct only where explicitly asked. Intermediate parameter calculations remain components unless requested.'
 return r
add('Example',8,330,'Given dy/dx=2x and point(1,2),find the unique curve on the real line;constant1,curve x²+1.',[
 curve('curve','2*x',1,2,'x**2+1',330)],['1'])
add('Try-Now-8',1,330,'Three independent first-order curve recoveries from supplied derivatives and ACTUAL point pairs(1,4),(−2,6),(−1,5).',[
 curve('a','6*x',1,4,'3*x**2+1',626),curve('b','3*x**2-2',-2,6,'x**3-2*x+10',626),curve('c','2*(1-x)',-1,5,'-x**2+2*x+8',626)],['1','2','0'])
add('Try-Now-8',2,330,'Recover the curve with gradient(7−5x)² through(1,7/15). Expanded key constant−328/15 equals the compact primitive constant6.',[
 curve('curve','(7-5*x)**2',1,'Rational(7,15)','49*x-35*x**2+25*x**3/3-Rational(328,15)',626)],['2','1','0'])
p=reasoning('B-y','The source value−1/2 follows if the recovered primitive uses one shared constant,or extends continuously across x=1/3. Without that connection condition the given derivative on its disconnected domain does not determine the left-component constant and hence B.',
 'For x>1/3,integrating (3x−1)^(−1/3) in the REAL cube-root convention gives (1/2)(3x−1)^(2/3)+c_right. A(3,1) fixes c_right=−1. For x<1/3,the real primitive is (1/2)(1−3x)^(2/3)+c_left. Its y-intercept is1/2+c_left,undetermined by A alone. If continuity of a single curve through the missing derivative point is assumed,c_left=c_right=−1 and the printed−1/2 follows. Do not silently transfer a constant through an original singularity.',331,'key incomplete')
p.update(assessed_8227_demand_ids=[CONST,CURVE],component_demand_ids=[INT],response_format='symbolic',given_representation='text',original_domain='x≠1/3; A is on the right component and B on the left.',printed_key_normalised='-Rational(1,2)',missing_condition='Shared constant/continuous extension across x1/3 is not explicitly supplied.')
extra(p,'right-point','(Rational(1,2)*(3*x-1)**Rational(2,3)-1).subs(x,3)','1')
extra(p,'left-source-convention','(Rational(1,2)*(1-3*x)**Rational(2,3)-1).subs(x,0)','-Rational(1,2)')
extra(p,'left-independent-constant-counterexample','(Rational(1,2)*(1-3*x)**Rational(2,3)).subs(x,0)','Rational(1,2)')
r=add('Example',9,331,'Find the y-intercept from fprime=(3x−1)^(−1/3) and A(3,1). The source transfers a constant across the derivative singularity at1/3; record its implicit continuity convention and the unconstrained alternative.',[p],['−1/3'])
r.update(original_domain='x≠1/3',source_domain_caution='The given point and requested intercept are in different derivative-domain components. The source value assumes a shared constant/continuous extension; that assumption must be explicit before this pattern is used.')
add('Try-Now-9',1,331,'Given4/√(6−2x)and P(1,8),recover y=−4√(6−2x)+16 on x<3.',[curve('curve','4/sqrt(6-2*x)',1,8,'-4*sqrt(6-2*x)+16',626)],['−1/2'])
add('Try-Now-9',2,331,'Given12/(2x+1)² and P(1,5),recover the fixed curve on the component x>−1/2. The other component constant is independent.',[curve('curve','12/(2*x+1)**2',1,5,'-6/(2*x+1)+7',626)],['−2'])
ps=[curve('a-curve','sqrt(1+2*x)',4,11,'(1+2*x)**Rational(3,2)/3+2',626),val('b-intercept','((1+2*x)**Rational(3,2)/3+2).subs(x,0)','Rational(7,3)',626,[CURVE],'Substitute x0 into the independently recovered fixed curve. The requested POINT is(0,7/3),not a new integration with a new constant.',[COORD])]
ps[-1]['author_answer_form']='Point(0,7/3).'
add('Try-Now-9',3,331,'From gradient√(1+2x) and point(4,11),recover the curve,then its y-axis intersection(0,7/3).',ps,['1/2'])
add('Try-Now-9',4,331,'Recover fprime=1/√(x+6)+6/x² with f(3)=1. Original domain x>−6,x≠0; the specified branch is x>0.',[curve('curve','1/sqrt(x+6)+6/x**2',3,1,'2*sqrt(x+6)-6/x-3',626)],['−1/2','−2'])
ps=[val('a-P','Tuple(sqrt(8/(5-3)),(17-sqrt(8/(5-3)))/3)','Tuple(2,5)',332,[TANGENT],'Normal3y+x=17has slope−1/3,so tangent slope3. Solve ORIGINAL5−8/x²=3,givingx±2; retainx2because the stem explicitly sayspositive. Then use the NORMAL LINE to find y5.',[COORD]),curve('b-curve','5-8/x**2',2,5,'5*x+8/x-9',332)]
extra(ps[0],'tangent-normal-incidence','Tuple((5-8/x**2).subs(x,2),3*5+2-17)','Tuple(3,0)')
r=add('Example',10,332,'A given normal line determines the positive contact point before curve reconstruction. Do not choose the negative derivative root or integrate the normal equation.',ps,['0','−2']);r['connected_part_structure']='Part(a) supplies P(2,5) used to fix the integration constant in(b).'
p=curve('curve','4*x+3',1,-2,'2*x**2+3*x-7',626)
p['method']='The given normal gradient−1/7 makes the tangent gradient7. ORIGINAL derivative p*x+3atx1givesp4. Then independently integrate4x+3and impose(1,−2),giving constant−7. Parameterpwas inferred;the curve is the requested output.'
extra(p,'normal-implied-parameter','solve(p+3-7,p)[0]','4')
add('Try-Now-10',1,332,'A normal gradient at the supplied point determines the derivative parameter before initial-condition recovery.',[p],['1','0'],[TANGENT])
# With positivea,sqrt(a²)=a. Do not silently retain the extraneous a−16.
ps=[val('a-tangent','3*x/a**2','3*x/a**2',626,[TANGENT],'For POSITIVEa and A(a²,3),the original derivative(2/a)x^(−1/2)+a*x^(−3/2)has slope3/a². The tangent y−3=(3/a²)(x−a²) simplifies to3x/a². The positivity condition is essential to sqrt(a²)=a.',[INT]),val('b-curve','4*sqrt(x)/a-2*a/sqrt(x)+1','4*sqrt(x)/a-2*a/sqrt(x)+1',626,[CURVE,CONST],'Direct integration gives4√x/a−2a/√x+c. At A(a²,3),a>0 gives4−2+c=3,so c1. The curve domain isx>0.',[INT]),val('c-a','FiniteSet(*solve(a**2+14*a-32,a))','FiniteSet(-16,2)',626,[CURVE,CONST],'Substitute B(16,8) into the original recovered curve to get16/a−a/2+1=8,witha>0. Clearing NONZEROa yieldsa²+14a−32=0. Both algebraic candidates are checked;only2meets the original positivity condition.',[COORD]),val('c-AB','sqrt((16-2**2)**2+(8-3)**2)','13',626,[],'Witha2,A=(4,3),B=(16,8). Euclidean distance√(12²+5²)=13. This is prerequisite coordinate geometry,not an independently prescribed8227calculus output.',[COORD])]
ps[2].update(author_answer_form='a=2 only; algebraic candidate−16 is rejected by the ORIGINAL a>0 condition.',admissible_parameter_values=['2'],rejected_parameter_values=[{'value':'-16','reason':'Source a is positive.'}],printed_key_normalisation_note='The printed key lists both a2 and rejected(a−16);the compared set preserves both algebraic candidates,not an assertion that both are admissible.')
gradient='(2/(a*sqrt(x))+a/x**Rational(3,2)).subs(x,a**2).subs(Abs(a),a)'
ps[0]['operation']={'kind':'identity','operands':[f'expand(3+({gradient})*(x-a**2))']}
ps[0]['component_demand_ids']=[COORD]
primitive='integrate(2/(a*sqrt(x))+a/x**Rational(3,2),x)'
ps[1]['operation']={'kind':'identity','operands':[f'({primitive})-({primitive}).subs(x,a**2).subs(Abs(a),a)+3']}
extra(ps[0],'positive-a-contact-check','(3*x/a**2).subs(x,a**2)','3')
extra(ps[1],'derivative-consistency','simplify(diff(4*sqrt(x)/a-2*a/sqrt(x)+1,x)-(2/(a*sqrt(x))+a/x**Rational(3,2)))','0')
extra(ps[2],'positive-candidate-in-original','16/2-Rational(2,2)+1','8')
r=add('Try-Now-10',2,333,'Positive-parameter derivative,pointA(a²,3),tangent,curve,and secondpointB(16,8). The admissiblea2givesdistance13; reject−16.',ps,['−1/2','−3/2']);r.update(physical_parameter_domain='a>0,x>0',connected_part_structure='The same positivea and same fixed curve are used in(a)–(c);B adds a second constraint rather than another arbitrary constant.')
p=val('curve','integrate(integrate(-4*x,x)+8,x)+Rational(4,3)','-2*x**3/3+8*x+Rational(4,3)',333,[CURVE,CONST],
 'Integrate ORIGINAL ysecond=−4x twice. Maximum at(2,12) imposes yprime(2)=0,givingc1=8,and y(2)=12,givingc2=4/3. Verify ysecond(2)=−8<0,so the stated maximum is consistent. A worked substitution line prints +16/3 instead of−16/3,but its final curve and constants are correct.',[INT,POINT])
extra(p,'maximum-condition','Tuple(diff(-2*x**3/3+8*x+Rational(4,3),x).subs(x,2),(-2*x**3/3+8*x+Rational(4,3)).subs(x,2),diff(-2*x**3/3+8*x+Rational(4,3),x,2).subs(x,2))','Tuple(0,12,-8)')
add('Example',11,333,'Recover a curve from its second derivative and a maximum point;two distinct integration constants and two conditions are required.',[p],['1','2','0'])

fig(8,330,'Family y=x²+c','Three displayed curves y=x²+5,x²,x²−4 share derivative2x and have y-intercepts5,0,−4. They are teaching SOLUTIONS,not a graph given in Example8 or an asked sketch.',[CONST,CURVE],'graph',[('Tuple(diff(x**2+5,x),diff(x**2,x),diff(x**2-4,x))','Tuple(2*x,2*x,2*x)')],None)
figures[-1].update(item_id='8227:TB:YM:C7:Teaching-figure:8',printed_page=pp(330),source_evidence=ev(330),value_level_scope_decisions=[],item_kind='teaching-figure')
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='Every Example8–11,Try8Q1–2/9Q1–4/10Q1–2,and the family reference graph enumerated. Try10Q2starts333,not332. Handwritten annotations in the source scan are not official source statements.',scope_screen='Rational-power initial-condition recovery and tangent/normal constraints. Preserve original real components,positivea,second-derivative maximum condition,and two constants for two integrations.')for page in range(330,334)]
h.pages=pages
if __name__=='__main__':h.save('constants','Complete rendered330–333initial-condition census; mathematical answers independently derived,source defects/cautions explicit.')
