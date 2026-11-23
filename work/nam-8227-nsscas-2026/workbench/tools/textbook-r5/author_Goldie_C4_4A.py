"""Every connected task of Goldie Exercise4A2–8, PDF102–104."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_Goldie_C4_opening import derivative
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02';CHAIN='8227:2020:M1:T8:O02:D02';POWER='8227:2020:M1:T8:O02:D01'
TANGENT='8227:2020:M1:T8:O03:D01';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02'
GRADIENT='8227:2020:M1:T8:O01:D01';SKETCH='8227:2020:M1:T3:O05:D01'
def ev(page):
    name='Goldie-key-C3-341'if page==342 else'Goldie-C4-102'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(n,page,note,parts,direct,components=None,sketch=False,rep='text'):
    for p in parts:
        kp=p.pop('key_page_override',342);pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Exercise-4A:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Map the explicitly requested derivative,tangent/normal,stationary point/classification and sketch. All curves here are explicit; geometric follow-up doesnot create an implicit/parametric derivative demand. Supporting coordinate geometry/area remains a separate component or cross-cutting decision.',
      'representation':rep,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within','quoted_value':note,
        'reason':'All actual powers are integer or1/2; real-domain restrictions/poles/endpoints are retained.'},
       {'rule_id':'8227:LIMIT04','status':'within'if n in[2,4,5,6,7,8]else'not applicable','quoted_value':note,
        'reason':'Any product/quotient rule is inMathematics2; the task is not reassigned toMathematics1only. Expansion remains a valid alternative for the cubicQ3.'},
       {'rule_id':'8227:QUAL09','status':'not applicable','quoted_value':note,
        'reason':'The tangents/normals are obtained by calculus at specified or stationary points,not a new quadratic-discriminant tangency task.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Exercise4Awithout an examination attribution or explicit exam-style label.',
      'precision_angle_check':{'source':'Exact algebraic coordinates/equations; no angle unit or rounding required.',
        'comparison':'Source unsigned∞inQ8is treated as vertical-tangent shorthand; finite endpoint derivative is undefined and the relevant left slope tends−∞. Equivalent line equations/derivative forms are retained.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

def stat(label,f,key,kp=342):
    p=value(label,'0',key,kp,'Solvef′(x)=0in the original real domain,then substitute each root into the original function. This gives every stationary coordinate,not every zero of the original function.')
    p['operation']={'kind':'stationary-points','operands':[f]};return p

def at_deriv(f,point,order=1):return f'(diff({f},x,{order})).subs(x,{point})'
def at(f,point):return f'({f}).subs(x,{point})'
def tangent(f,point):return f'({at_deriv(f,point)})*(x-({point}))+({at(f,point)})'
def normal(f,point):return f'(-1/({at_deriv(f,point)}))*(x-({point}))+({at(f,point)})'

f='x/(x-1)'
p=reasoning('iv','The two tangents are parallel.',
 'The independently derived tangent slopes atx=0andx=2are both−1. The linesy=−xandy=−x+4are distinct and therefore parallel.',342,'matches')
p['additional_operations']={'slope_difference':{'kind':'identity','operands':[f'{at_deriv(f,"0")}-({at_deriv(f,"2")})']}}
add(2,102,'Giveny=x/(x−1)andits hyperbola sketch:find derivative;gradient/tangent at(0,0);gradient/tangent at(2,2);deduce the relationship between the tangents. Keepx≠1.',[
 derivative('i',f,'-1/(x-1)**2',342,'x≠1.'),
 value('ii',f'Tuple({at_deriv(f,"0")},{tangent(f,"0")})','Tuple(-1,-x)',342),
 value('iii',f'Tuple({at_deriv(f,"2")},{tangent(f,"2")})','Tuple(-1,-x+4)',342),p],
 [QUOTIENT,TANGENT],[POWER],rep='graph')
f='(x+1)*(x-2)**2'
p=reasoning('ii-classification','(0,4)is a local maximum and(2,0)is a local minimum.',
 'f′=3x(x−2),so the only stationary abscissae are0,2. The second derivative is6x−6,negative at0andpositive at2. A derivative-sign test gives the same classification.',342,'matches')
p['additional_operations']={'second_derivatives':{'kind':'identity','operands':[f'Tuple({at_deriv(f,"0",2)},{at_deriv(f,"2",2)})']}}
p['additional_operation_expected']={'second_derivatives':'Tuple(-6,6)'}
p2=reasoning('iii','Cubic sketch:crosses(−1,0),passes(0,4)at its local maximum,touches(2,0)at its local minimum,andhas opposite unbounded end behaviour with positive leading coefficient.',
 'Factorisation gives a simple root−1anddouble root2. Independent derivative/classification supplies both turns;the y-intercept is4. The supplied key graph has these features. A correct sketch joins them continuously with cubic end behaviour; its drawing neednot match a pixel template.',342,'sketch')
p2['additional_operations']={'function_roots':{'kind':'real-roots','operands':[f]},'y_intercept':{'kind':'identity','operands':[at(f,'0')]},
 'end_signs':{'kind':'identity','operands':[f'Tuple(limit({f},x,-oo),limit({f},x,oo))']}}
add(3,102,'Fory=(x+1)(x−2)²:find derivative,all stationary coordinates/classifications,and sketch the cubic. Expansion is a valid independent route; no implicit or parametric curve is involved.',[
 derivative('i',f,'3*x*(x-2)',342),stat('ii-points',f,'FiniteSet(Tuple(0,4),Tuple(2,0))'),p,p2],
 [POWER,STATIONARY,CLASSIFY,SKETCH],[PRODUCT,CHAIN],True)
f='(x-3)/(x-4)'
p=reasoning('iv-no-stationary','There are no stationary points onx≠4.',
 'The derivative is−1/(x−4)²,strictly negative everywhere the function is defined. It never equalszero. The polex=4is outside the domain and isnot a stationary point.',342,'matches')
p['additional_operations']={'stationary_set':{'kind':'stationary-points','operands':[f]}}
p2=reasoning('iv-sketch','Hyperbola y=1+1/(x−4):vertical asymptotex=4,horizontal asymptotey=1,intercepts(3,0),(0,3/4);both branches decrease.',
 'Algebraic division gives1+1/(x−4). Limits fix both asymptotes and their sidedness;the derivative is negative on each connected domain interval. The source key graph depicts these branches and asymptotes. No stationary point is introduced at the pole.',342,'sketch')
p2['additional_operations']={'translation_identity':{'kind':'identity','operands':[f'cancel(({f})-(1+1/(x-4)))']},
 'intercepts':{'kind':'identity','operands':[f'Tuple(solve({f},x)[0],{at(f,"0")})']},
 'pole_limits':{'kind':'identity','operands':[f'Tuple(limit({f},x,4,dir="-"),limit({f},x,4,dir="+"))']}}
add(4,102,'Fory=(x−3)/(x−4):differentiate;find tangent at(6,1.5);normal at(5,2);use derivative to deduce no stationary points and sketch. The polex=4remains outside its domain.',[
 derivative('i',f,'-1/(x-4)**2',342,'x≠4.'),value('ii',tangent(f,'6'),'(12-x)/4',342),value('iii',normal(f,'5'),'x-3',342),p,p2],
 [QUOTIENT,TANGENT,STATIONARY,SKETCH],[POWER],True)
f='2*x/(sqrt(x)-1)'
p=reasoning('iii-classification','P=(4,8)is a local minimum.',
 'Within the original domainx≥0,x≠1,the derivative is(√x−2)/(√x−1)². For1<x<4it is negative,andforx>4it is positive. Hence the stationary point4is a local minimum. The computed second derivative there is1/4>0,an alternative justification. The endpoint0is not a stationary point.',342,'matches')
p['additional_operations']={'second_derivative_at_P':{'kind':'identity','operands':[at_deriv(f,'4',2)]}}
p['additional_operation_expected']={'second_derivative_at_P':'1/4'}
p4=reasoning('iv-normal','The normal atP=(4,8)isx=4.',
 'AtPthe tangent gradient iszero,sothe tangent isy=8andthe normal is vertical. Do not apply−1/0as a finite slope.',342,'matches')
n9=normal(f,'9');q_x=f'solve(({n9})-({at(f,"4")}),x)[0]';r_y=f'({n9}).subs(x,4)'
p6=value('vi',f'Abs((({q_x})-4)*(({r_y})-({at(f,"4")})))/2','441/8',103,
 'P,Qshare the horizontal tangent y=8,andP,Rshare the verticalnormalx=4. Independently deriveQfrom its intersection with the original normal at(9,9),deriveRbyx=4,anduse half the product of these perpendicular side lengths. The stated result is in the task; no separate official working is claimed.')
p6['check_mode']='show/prove'
row=add(5,102,'Giveny=2x/(√x−1),undefinedx<0andx=1,andaminimumP:derive gradient;normal at(9,9);locate/classifyP;its tangent/normal;intersectionsQ,Rwith the first normal;showtrianglePQRarea441/8. The denominator is√x−1,not√(x−1). Parts continuePDF103.',[
 derivative('i',f,'(sqrt(x)-2)/(sqrt(x)-1)**2',342,'x>0,x≠1for the symbolic differentiation; a right derivative exists at0.'),
 value('ii-gradient',at_deriv(f,'9'),'1/4',342),{**value('ii-normal',n9,'-4*x+45',103),'check_mode':'show/prove'},
 stat('iii-points',f,'FiniteSet(Tuple(4,8))'),p,
 value('iv-tangent',tangent(f,'4'),'8',342),p4,
 value('v-a-Q',f'Tuple({q_x},{at(f,"4")})','Tuple(37/4,8)',342),
 value('v-b-R',f'Tuple(4,{r_y})','Tuple(4,29)',342),p6],
 [QUOTIENT,TANGENT,STATIONARY,CLASSIFY],[CHAIN,POWER],rep='graph')
for part in row['subparts']:
 if part['subpart']!='i':part['source_pdf_page']=103;part['source_evidence']=ev(103)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[103]})
f='(x**2-2*x-5)/(2*x+3)'
p=reasoning('iii','(−1,−2)is a local minimum;(−2,−3)is a local maximum.',
 'The only stationary x-values are−1,−2;the pole−3/2is excluded. The second derivative is2/(2x+3)³,positive at−1andnegative at−2. Alternatively use the sign of2(x+1)(x+2)/(2x+3)²on the connected intervals,keeping the pole separate.',342,'matches')
p['additional_operations']={'second_derivatives':{'kind':'identity','operands':[f'Tuple({at_deriv(f,"-1",2)},{at_deriv(f,"-2",2)})']}}
p['additional_operation_expected']={'second_derivatives':'Tuple(2,-2)'}
add(6,103,'Giveny=(x²−2x−5)/(2x+3)andits two-branch sketch:find derivative;hence all stationary coordinates;classify each using calculus. Keepx≠−3/2separate from the two stationary points.',[
 derivative('i',f,'2*(x+1)*(x+2)/(2*x+3)**2',342,'x≠−3/2.'),stat('ii',f,'FiniteSet(Tuple(-1,-2),Tuple(-2,-3))'),p],
 [QUOTIENT,STATIONARY,CLASSIFY],[POWER],rep='graph')
f='x**2/(2*x+1)'
p=reasoning('classification','Local maximum at(−1,−1);local minimum at(0,0).',
 'Differentiate to2x(x+1)/(2x+1)². Its only zero abscissae are−1,0;the pole−1/2is excluded. The second derivative is2/(2x+1)³,negative at−1andpositive at0;this gives the two classifications.',342,'matches')
p['additional_operations']={'derivative':{'kind':'identity','operands':[f'diff({f},x)']},
 'second_derivatives':{'kind':'identity','operands':[f'Tuple({at_deriv(f,"-1",2)},{at_deriv(f,"0",2)})']}}
p['additional_operation_expected']={'second_derivatives':'Tuple(-2,2)'}
add(7,103,'Fory=x²/(2x+1),find every stationary point and identify its nature. Derivative is supporting working,not an extra numbered output;the polex=−1/2is never included as a stationary point.',[
 stat('points',f,'FiniteSet(Tuple(-1,-1),Tuple(0,0))'),p],[STATIONARY,CLASSIFY],[QUOTIENT,POWER])
f='x*sqrt(9-2*x**2)'
p=derivative('ii-inner','sqrt(9-2*x**2)','-2*x/sqrt(9-2*x**2)',104,'−3/√2<x<3/√2for finite derivative.')
p['check_mode']='show/prove'
p2=derivative('ii-hence',f,'(9-4*x**2)/sqrt(9-2*x**2)',104,'Originalfunction−3/√2≤x≤3/√2;finite derivative on the interior.')
p2['check_mode']='show/prove'
p3=value('iii-maximum-x','solve(9-4*x**2,x)[1]','3/2',342,
 'Stationarity requires9−4x²=0inside the original positive displayed arc. The positive root is3/2;the derivative changes from positive to negative there,so it is the required maximum. The negative root belongs to the other arc,not the pictured maximum.')
p3['assertions']=[{'expression':'sign((9-4*(1)**2)/sqrt(9-2*(1)**2))','expected':'1'},
 {'expression':'sign((9-4*(2)**2)/sqrt(9-2*(2)**2))','expected':'-1'}]
p4=reasoning('iii-endpoint-gradient','At the positive endpointa=3√2/2there is a vertical tangent and no finite derivative;the left-hand slope tends−∞.',
 'The numerator9−4x²tends−9whilethe positive denominator√(9−2x²)tends0asx→a−. The source key says gradient=∞without a plus sign;this is read as vertical-tangent shorthand,not a correct signed positive limit. The drawing also approaches the endpoint vertically downwards.',342,'matches')
p4['source_interpretation']='Unsigned∞is a qualitative vertical-tangent convention here. The finite derivative is undefined; for directional limits use−∞.'
p4['additional_operations']={'left_slope_limit':{'kind':'identity','operands':[f'limit(diff({f},x),x,3*sqrt(2)/2,dir="-")']}}
add(8,104,'The positive arc ofy=x√(9−2x²)crosses at(a,0):find positivea;show derivative ofthe square-root factor;hence differentiate the product;find maximumx,origin gradient,andinterpret the endpoint gradient. The displayed arc is0≤x≤a;the full function has a larger symmetric real domain.',[
 value('i','solve(9-2*x**2,x)[1]','3*sqrt(2)/2',342),p,p2,p3,
 value('iii-origin-gradient',at_deriv(f,'0'),'3',342),p4],
 [PRODUCT,CHAIN,STATIONARY,CLASSIFY,GRADIENT],[POWER],rep='graph')

figures=[]
for n,page,parent,label,note,method,teaches in[
 (5,102,2,'Exercise4A2 rational graph','y=x/(x−1)hasverticalasymptotex=1,horizontalasymptotey=1,andpasses(0,0),(2,2). Thetwo branches are separately decreasing.',
 'Rewrite1+1/(x−1);limits give theasymptotes,andderivative−1/(x−1)²fixes monotonicity. Source given graph is checked qualitatively,not measured for an exact slope.',[QUOTIENT,TANGENT]),
 (6,102,5,'Exercise4A5 square-root denominator graph','y=2x/(√x−1)hasdomainx≥0,x≠1,verticalasymptotex=1,andpositive-branchminimumP=(4,8). Leftbranchpasses theoriginandfalls to−∞;rightbranchfallsfrom+∞thenrises.',
 'Read the radical extent from the rendered formula;differentiate original function. The parent independently locates/classifiesP;limits at1check thetwo vertical branches. This is not2x/√(x−1).',[QUOTIENT,STATIONARY,CLASSIFY]),
 (7,103,6,'Exercise4A6 stationary rational branches','y=(x²−2x−5)/(2x+3),polex=−1.5,leftbranchmaximum(−2,−3),rightbranchminimum(−1,−2). The source graph is qualitative with the polelabel−1.5.',
 'Original derivative is2(x+1)(x+2)/(2x+3)²;second derivative2/(2x+3)³classifiesbothturns. Polynomial division gives obliqueasymptotey=x/2−7/4. The pole is not a stationary point.',[QUOTIENT,STATIONARY,CLASSIFY]),
 (8,104,8,'Exercise4A8 restricted positive radical arc','Positivearc y=x√(9−2x²)fromorigin to(a,0),a=3√2/2,withmaximumatx=3/2andverticaldownwardendpointtangent. The graph is onlypart ofthe full real curve.',
 'Original square-root domain is[−3/√2,3/√2]. On the shownpositiveinterval,the computed derivative changes+to−at3/2,hasvalue3at0,andtends−∞at the rightendpoint. No continuation beyond the radical domain is permitted.',[PRODUCT,CHAIN,STATIONARY,CLASSIFY])]:
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure','exercise':'Given figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
     'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':'graph','source_evidence':ev(page),
     'parent_item_id':f'8227:TB:Goldie:C4:Exercise-4A:{parent}','learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within','quoted_value':note,'reason':'Integer/rational powers only;original poles/radical domain preserved.'}],
     'value_level_scope_review_status_r5':'author actual curve/domain/turning evidence checked2026-11-18;independent check pending',
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
       'relation':'Internal textbook given graph;no claim ofexamination frequency orofficialmarking.'},
     'mathematical_feature_review':{'status':'author rendered source graph compared with original-function analysis;independentacceptancepending','method':method}})
# Page104 also contains a polynomial prompt and the log/exponential exposition.
# It is NOT declared fully censused by this segment; the following segment owns104.
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'Every Exercise4A2–7task/given graph andconnected continuation is recorded;4A8starts104andwillbe includedin that page census with thefollowinglog/exponential material.',
 'reader':'Codex author','date':'2026-11-18'}for page in[102,103]]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-4A.json',{'scope':'Every4A2–8subtask,includingallcalculus,geometry,sketchandshow-thatoutputs.','items':answers}),
     ('census-Goldie-C4-4A.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages102–103;4A8/givengraph104recordedbutpage104censusawaitsitsremainingexposition/prompt.',
      'new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
