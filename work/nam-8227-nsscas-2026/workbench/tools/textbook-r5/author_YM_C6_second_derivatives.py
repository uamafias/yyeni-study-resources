"""YM294–297: inverse connected rates,second derivatives,and first stationary sketch."""
import json
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;NOTATION=h.NOTATION;CHAIN='8227:2020:M1:T8:O02:D02';RATE='8227:2020:M1:T8:O03:D03';POINT='8227:2020:M1:T8:O04:D01';NATURE='8227:2020:M1:T8:O04:D02';extra=h.extra
def add(kind,n,page,note,parts,direct,components,powers,rep='text'):
 r=h.add(kind,n,page,note,parts,direct,components,powers=powers);r['representation']=rep
 r['mapping_rationale']='Inverse connected-rate problems solve for a coordinate or inputrate and require nonzero cancellation conditions. First and second derivatives remain separately requested outputs. Locating stationary points,justifying their nature,and sketching the curve are distinct evidence requirements; a stationary point neednotturn.'
 for p in parts:p['given_representation']=rep
 return r
def part(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[]);return p
def derivative(label,fn,key,order,kp,chain=False):
 p=part(label,f'diff({fn},x,{order})',key,kp,[NOTATION,CHAIN if chain else POWER],f'Use the ORIGINAL function and compute its requested derivative order{order}with respect tox. Each differentiation acts on the previous result;retain coefficients,minus signs,and the original domain. Square roots require interior positive arguments for finite derivatives;reciprocals exclude their zeros. Odd-root powers use real roots,not principal complex values.',[POWER]if chain else[])
 p.update(original_function=fn,derivative_order=order);return p

p=part('dA-dt','(2*pi*50)*3','300*pi',621,[RATE],'Original circular oil patch has radius50m increasing3m/h. Use dA/dt=(2pi r)(dr/dt),giving300pi m²/h. Midday identifies the current radius/rate;it isnotanother differentiationvariable.',[POWER]);p.update(units='m^2/h',printed_key_units='m^2/h')
add('Try-Now-23',4,294,'Find area rate of an expanding radius50m circular patch at3m/h,retaining square-metres per hour.',[p],[RATE],[POWER],['2'])
p=part('x-values','FiniteSet(1,Rational(9,4))','FiniteSet(1,Rational(9,4))',294,[RATE],'Original y=x²−(10/3)x^(3/2)+5xwithx>=0. For NONZERO inputrate,dx/dt=(1/2)dy/dtandthechainrelationgive dy/dx2. Letu=sqrtx>=0;2u²−5u+3=0givesu1,3/2andx1,9/4. If both rates are0,the ratio cancellation is invalid and this instantaneous relation alone doesnotdeterminex. Retain this nonzero-rate condition before variation.',[POWER])
# Avoid binding a key to its own expected value: solve the ORIGINAL root-basis equation.
# SymPy expressions deliberately avoid Python comprehensions.
p['operation']={'kind':'identity','operands':['FiniteSet(solve(2*a**2-5*a+3,a)[0]**2,solve(2*a**2-5*a+3,a)[1]**2)']}
extra(p,'both-original-gradients','Tuple((2*x-5*sqrt(x)+5).subs(x,1),(2*x-5*sqrt(x)+5).subs(x,Rational(9,4)))','Tuple(2,2)')
p['nonzero_rate_condition']='dx/dt≠0(andthereforedy/dt≠0)when forming the ratio.'
add('Example',24,294,'Use a nonzero connected-rate ratio to find both xvalues of a curve involvingx^(3/2);record the cancellation qualification.',[p],[RATE],[POWER],['2','3/2','1'])
p=part('x-values','FiniteSet(*solve(24-Rational(8,3)*(3-2*x)**2,x))','FiniteSet(0,3)',621,[RATE],'Original y12/(3−2x),dx/dt0.15anddy/dt0.4are BOTHpositive. Theirratiois8/3. Original derivative24/(3−2x)²gives(3−2x)²9,sox0or3. Both avoid the original pole3/2andbothgive the required positive gradient.',[CHAIN]);extra(p,'both-input-output-rates','Tuple((24/(3-2*x)**2).subs(x,0)*Rational(3,20),(24/(3-2*x)**2).subs(x,3)*Rational(3,20))','Tuple(Rational(2,5),Rational(2,5))')
add('Try-Now-24',1,294,'Infer two possible positions from supplied x/y rates on a rational curve,retaining both pole-separated valid branches.',[p],[RATE],[CHAIN],['−1'])
p=part('dr-dt','50/(4*pi*10**2)','1/(8*pi)',621,[RATE],'Original spherevolumeV=(4/3)pi r³givesdV/dr4pi r². Given dV/dt50cm³/satr10cm,solve dr/dt=(dV/dt)/(dV/dr),not its reciprocal. Radiuspositive makes the divisor nonzero.',[POWER]);p.update(units='cm/s',printed_key_units='cm/s')
add('Try-Now-24',2,294,'Infer radialrate from a supplied sphere-volume rate,with the current positive radius10cm.',[p],[RATE],[POWER],['3'])
ps=[derivative('a-first','x**3+2*x**2-3*x+2','3*x**2+4*x-3',1,295),derivative('a-second','x**3+2*x**2-3*x+2','6*x+4',2,295),derivative('b-second','-4/(3*x-2)**3','-432/(3*x-2)**5',2,295,True)]
add('Example',25,295,'Find first/second derivatives of a cubic and the requested second derivative of a reciprocal cube. The unasked intermediate first derivative of(b)is working,not another response.',ps,[NOTATION,POWER,CHAIN],[],['3','2','1','−3'])
data=[('a','4*x**3','12*x**2','24*x',False),('b','6*x**3-5*x**2-7','18*x**2-10*x','36*x-10',False),('c','1/x','-1/x**2','2/x**3',False),('d','6-8/x**2','16/x**3','-48/x**4',False),('e','(x**4+x)/x**2','2*x-1/x**2','2+2/x**3',False),('f','sqrt(4*x-2)','2/sqrt(4*x-2)','-4/(4*x-2)**Rational(3,2)',True)]
ps=[]
for label,fn,key1,key2,chain in data:ps.extend([derivative(label+'-first',fn,key1,1,621,chain),derivative(label+'-second',fn,key2,2,621,chain)])
add('Try-Now-25',1,295,'Find both derivative orders for six originals,including reciprocal powers,a reducible quotient,and a square-root composite.',ps,[NOTATION,POWER,CHAIN],[],['3','2','−1','−2','1/2'])
data=[('a','sqrt(x)-1/x**2','-1/(4*x**Rational(3,2))-6/x**4',False),('b','3*x**2*(5+3*x-x**2)','30+54*x-36*x**2',False),('c','(4*x**3-x)/sqrt(x)','15*sqrt(x)+1/(4*x**Rational(3,2))',False),('d','-15*(2*x-1)**(-Rational(1,3))','-Rational(80,3)*(2*x-1)**(-Rational(7,3))',True)]
ps=[derivative(label+'-second',fn,key,2,621,chain)for label,fn,key,chain in data]
extra(ps[-1],'negative-real-root-branch','diff(15*(1-2*x)**(-Rational(1,3)),x,2).subs(x,0)','Rational(80,3)')
add('Try-Now-25',2,295,'Find only the requested second derivatives of four originals,including a REAL reciprocal cube root on both sides ofx1/2.',ps,[NOTATION,POWER,CHAIN],[],['1/2','−2','4','5/2','−1/3'])
p=part('stationary-points','0','FiniteSet(Tuple(-1,10),Tuple(3,-22))',297,[POINT],'Differentiate ORIGINAL x³−3x²−9x+5,solve3(x−3)(x+1)=0,and substitute BOTH roots into the ORIGINAL function for their ordinates. A list of xcoordinates alone is incomplete.',[POWER]);p['operation']={'kind':'stationary-points','operands':['x**3-3*x**2-9*x+5']}
ps=[p]
p=reasoning('nature','Local maximum(−1,10);local minimum(3,−22).','The ORIGINAL derivative is positivebefore−1,negativebetween−1and3,andpositiveafter3. Thus +to−gives themaximumand−to+givesminimum. Source sign-table samples±0.1aroundeachcriticalpointare checked;independent secondderivatives−12and12confirm these classifications.',297,'matches');p.update(assessed_8227_demand_ids=[NATURE],component_demand_ids=[POWER])
extra(p,'source-sign-table','Tuple((3*x**2-6*x-9).subs(x,-Rational(11,10)),(3*x**2-6*x-9).subs(x,-Rational(9,10)),(3*x**2-6*x-9).subs(x,Rational(29,10)),(3*x**2-6*x-9).subs(x,Rational(31,10)))','Tuple(Rational(123,100),-Rational(117,100),-Rational(117,100),Rational(123,100))');extra(p,'independent-second-derivatives','Tuple((6*x-6).subs(x,-1),(6*x-6).subs(x,3))','Tuple(-12,12)');ps.append(p)
p=reasoning('sketch','Positive-leading cubic,lefttaildown/righttailup,yintercept5,max(−1,10),min(3,−22),threeaxis crossings.','Read the ORIGINAL function and the two already established stationarypoints. The requested sketch preserves their relative heights,abscissas,and sign changes. Exact xintercepts are not required by this source section;independent brackets(−3,−2),(0,1),(4,5)establish three crossings. These are author-derived sketch features,not an official marking tariff.',297,'sketch');p.update(assessed_8227_demand_ids=[POINT,NATURE],response_format='sketch',credited_features=['Correct cubic tail directions','Local maximum(−1,10)','Local minimum(3,−22)','yintercept(0,5)','Three crossings positioned consistently;exactrootformnotrequired'])
extra(p,'root-bracket-signs','Tuple((x**3-3*x**2-9*x+5).subs(x,-3),(x**3-3*x**2-9*x+5).subs(x,-2),(x**3-3*x**2-9*x+5).subs(x,0),(x**3-3*x**2-9*x+5).subs(x,1),(x**3-3*x**2-9*x+5).subs(x,4),(x**3-3*x**2-9*x+5).subs(x,5))','Tuple(-22,3,5,-6,-15,10)');ps.append(p)
r=add('Example',26,297,'Locate stationarypoints,classifyeachfromderivativesignchanges,andSKETCHtheoriginal cubic. Do notcollapse thevisualresponseintojustsolving thederivativezeroequation.',ps,[POINT,NATURE],[POWER],['3','2','1'],'text');r['sketch_response_required']=True

refs=[(31,295,'Second derivative notation','Differentiate fprime(x)again to obtainfdoubleprime(x),also d²y/dx². This notation isnot(dy/dx)²anddoesnotmean the second derivative is alwaysa constant.',[NOTATION],'table',None),(32,296,'Stationary maximum/minimum schematic','The markedAandBhavezero gradient;Achanges+to−andB−to+. The source calls a stationarypointor turningpoint;in general a stationaryinflectionhasno reversal,so the terms are not interchangeable.',[POINT,NATURE],'graph',None),(33,296,'Local maximum sign diagram','Near asmoothlocalmaximum,the shown derivative changespositive→0→negative. Local compares nearbyordinates,not necessarily everypointoveranunbounded domain.',[NATURE],'graph',None),(34,296,'Local minimum sign diagram','Near asmoothlocalminimum,the shown derivative changesnegative→0→positive. A zero derivative by itselfdoesnotestablish minimum.',[NATURE],'graph',None),(35,297,'Example26 two sign tables','Source samples2.9/3.1give−1.17/+1.23aroundminimumx3;−1.1/−0.9give+1.23/−1.17aroundmaximumx−1. Horizontal tangentanddirectionchangeare separate features.',[NATURE],'table','Example:26'),(36,297,'Example26 worked cubic sketch','y=x³−3x²−9x+5,maximum(−1,10),minimum(3,−22),yintercept5,andpositiveleading cubic tails. The figure is a solution illustration linked to the actual sketch response.',[POINT,NATURE],'graph','Example:26')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:')if r['parent_item_id']else None;r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['item_kind']='teaching-figure'
 r['mathematical_feature_review']['method']='Inspect original derivative-order notation,stationarypoint labels,sign-table values,and curve tail/intercept relationships. Recompute from the original function;zero derivative alone is not a nature classification.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllTry23Q4,Examples24–26,Try24Q1/2,Try25Q1/2,and six derivative/stationary reference panels are enumerated over294–297. Example26has an explicit sketch response. The optional intermediate firstderivatives in second-only requests are working,not extra responses.',scope_screen='Prescribed inverseconnectedrates,derivative notation,power/chain rules,andstationarypoint location/nature. Keep nonzero rate ratios,realoddroots,originalpoles,and localversusglobal comparisons.')for page in range(294,298)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-second-derivatives.json',dict(scope='All294–297explicit tasks.',items=answers)),('census-YM-C6-second-derivatives.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete294–297page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
