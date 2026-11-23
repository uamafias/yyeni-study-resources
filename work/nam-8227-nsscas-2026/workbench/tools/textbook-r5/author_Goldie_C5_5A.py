"""Every fixed-source Exercise5A response and its two given diagrams."""
import json
from author_Goldie_C5_opening import W,SRC,SHA,ev,value,reasoning,indefinite,definite,EXPINT,DEF,AREA,DOMAIN,compute,expression,equivalent
POWER='8227:2020:M1:T8:O02:D01';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';EXPLICIT='8227:2020:M1:T8:O03:D01'
ELEMENTARY='8227:2020:M2:T4:O01:D01';CONSTANT='8227:2020:M1:T9:O02:D01';CURVE='8227:2020:M1:T9:O02:D02';INVERSE='8227:2020:M1:T3:O01:D03'
DIVISION='8227:2020:M2:T1:O03:D01';QUOTIENT='8227:2020:M2:T1:O03:D03';LOGDEF='8227:2020:M2:T2:O02:D01';LOGLAW='8227:2020:M2:T2:O01:D02'
ATTR={6:'9709 Paper2 Q7 June2006',7:'9709 Paper2 Q6 November2005',8:'9709 Paper2 Q8 June2009',9:'9709 Paper3 Q1 November2007'}
answers=[]
def add(n,page,note,parts,direct,components=None,rep='text'):
    for p in parts:
        kp=p.pop('key_page_override',345);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C5:Exercise-5A:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
     'mapping_rationale':'Map the integral, geometric area, explicit derivative/tangent or deliberately requested algebraic decomposition separately. Do not label an explicit curve as implicit/parametric merely because its geometry follows calculus.',
     'representation':rep,'sketch_response_required':False,'exam_style':n in ATTR,'exam_style_basis':'Printed attribution '+ATTR[n]+'. Internal lead only; original exam source not newly checked.'if n in ATTR else'Ordinary exercise without examination attribution.',
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL04','status':'not applicable','quoted_value':note,'reason':'All definite integrals stay inside a single continuous component. No improper integral or pole crossing is asked.'},
      {'rule_id':'8227:QUAL06','status':'not applicable','quoted_value':note,'reason':'Planar area/line calculations, not solids of revolution.'}],
     'precision_angle_check':{'source':'Q3 asks 3 significant figures where appropriate; Q4 source key displays its two areas to 3 significant figures; Q7 stationary x is displayed to 3 decimals. Other outputs retain exact values.',
      'comparison':'Keep exact values and domains internally, then compare the source display at its stated precision. Area below the axis is positive; its signed integral is negative.'},
     'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
parts=[indefinite(label,f,key,345)for label,f,key in [('i','3/x','3*log(Abs(x))'),('ii','1/(4*x)','log(Abs(x))/4'),('iii','1/(x-5)','log(Abs(x-5))'),('iv','1/(2*x-9)','log(Abs(2*x-9))/2')]]
add(1,139,'Four real indefinite reciprocal integrals:3/x,1/(4x),1/(x−5),1/(2x−9). Each original denominator excludes its zero; use ln absolute value and an arbitrary constant per connected component.',parts,[EXPINT])
parts=[indefinite(label,f,key,345)for label,f,key in [('i','exp(3*x)','exp(3*x)/3'),('ii','exp(-4*x)','-exp(-4*x)/4'),('iii','exp(-x/3)','-3*exp(-x/3)'),('iv','10/exp(5*x)','-2/exp(5*x)'),('v','(exp(3*x)+4)/exp(2*x)','exp(x)-2*exp(-2*x)')]]
add(2,139,'Five exponential indefinite integrals:e^(3x),e^(−4x),e^(−x/3),10/e^(5x),(e^(3x)+4)/e^(2x). Simplify the last integrand into a sum before reverse differentiation.',parts,[EXPINT])
parts=[definite(label,f,lo,hi,key,345,3)for label,f,lo,hi,key in [('i','4*exp(2*x)',0,4,'5960'),('ii','4/(2*x+1)',1,3,'1.69'),('iii','exp(x)+exp(-x)',-1,1,'4.70'),('iv','exp(3*x-2)',-2,1,'0.906')]]
add(3,139,'Evaluate four proper definite integrals:4e^(2x) on[0,4],4/(2x+1) on[1,3],e^x+e^(−x) on[−1,1],e^(3x−2) on[−2,1]. Give 3 significant figures where appropriate.',parts,[EXPINT,DEF])
f='x+4/x'
p=value('i-points','0','FiniteSet(Tuple(2,4),Tuple(-2,-4))',345,'Solve the derivative of the original function on x≠0. Retain both real regular points.')
p['operation']={'kind':'stationary-points','operands':[f]}
p2=reasoning('i-natures','P=(2,4) is a minimum and Q=(−2,−4) is a maximum.',
 'f′=1−4/x² vanishes at±2. f″=8/x³ is positive at2 and negative at−2. The pole0 separates the branches and is not a stationary point.',345,'matches')
p2['additional_operations']={'second_derivatives':{'kind':'identity','operands':['Tuple(diff(x+4/x,x,2).subs(x,2),diff(x+4/x,x,2).subs(x,-2))']}};p2['additional_operation_expected']={'second_derivatives':'Tuple(1,-1)'}
p3=definite('ii-right-area',f,2,5,'14.2',345,3)
p4=value('ii-left-area','-integrate(x+4/x,(x,-4,-2))','8.77',345,'The entire left shaded branch is below the x-axis, so negate its signed integral on[−4,−2]. Round only the positive area to the written 3 significant figures.')
p4['operation']={'kind':'rounded','operands':['-integrate(x+4/x,(x,-4,-2))'],'significant_figures':3}
add(4,140,'Given y=x+4/x with two shaded branches:find minimumP and maximumQ, then the positive shaded areas on[2,5]and[−4,−2]. The disconnected pole and the left-area sign must be preserved.',[p,p2,p3,p4],[STATIONARY,CLASSIFY,AREA],[ELEMENTARY,EXPINT,DEF],rep='graph')
p=definite('i-under-curve','exp(x)',0,'log(5)','4',345)
p2=value('i-shaded-area','5*log(5)-integrate(exp(x),(x,0,log(5)))','5*log(5)-4',345,'Subtract the area under e^x from the rectangle width ln5,height5. Both given geometric bounds are essential.')
p3=reasoning('ii','Reflection in y=x transforms y=e^x into y=ln x.',
 'Exponential is one-to-one on R with positive range; its inverse logarithm has positive domain and real range. Swapping each point coordinate reflects the graph in y=x.',345,'matches')
p4=definite('iii','log(x)',1,5,'5*log(5)-4',140)
p4['check_mode']='show/prove';p4['method']='Use the preceding inverse-graph area result as requested, or independently integrate ln x for QA. The independently computed x ln x−x endpoint difference agrees with the given target; an integration-by-parts method is not imposed on the learner.'
p5=definite('iv-a','log(x**3)',1,5,'3*(5*log(5)-4)',345)
p6=definite('iv-b','log(3*x)',1,5,'4*log(3)+5*log(5)-4',345)
row=add(5,140,'From the e^x graph with A=(ln5,0),B=(ln5,5),C=(0,5):find under-curve and shaded rectangle areas, describe reflection to ln x, prove ∫₁⁵lnx=5ln5−4, and deduce integrals of ln(x³) and ln(3x). The task scaffolds the log integral geometrically.',[p,p2,p3,p4,p5,p6],[AREA,INVERSE,LOGLAW],[EXPINT,DEF],rep='graph')
# The extra definite-integral checks are independent QA, not a claim that the learner must know integration by parts.
p=value('i','diff(log(2*x+3),x)','2/(2*x+3)',345)
p2=definite('ii','1/(2*x+3)',-1,3,'log(3)',141);p2['check_mode']='show/prove'
p3=value('iii','Tuple(*div(4*x**2+8*x,2*x+3,x))','Tuple(2*x+1,-3)',345,'Perform polynomial division of the original numerator by the original linear denominator and reconstruct numerator=divisor×quotient+remainder.')
p3['assertions']=[{'expression':'expand((2*x+3)*(2*x+1)-3)-(4*x**2+8*x)','expected':'0'}]
p4=definite('iv','(4*x**2+8*x)/(2*x+3)',-1,3,'12-3*log(3)',141);p4['check_mode']='show/prove'
add(6,141,'Differentiate ln(2x+3);hence show its reciprocal integral on[−1,3]is ln3;divide4x²+8x by2x+3;hence prove the rational integral is12−3ln3. Both requested links and the remainder matter.',[p,p2,p3,p4],[ELEMENTARY,EXPINT,DEF,DIVISION,QUOTIENT])
f='exp(2*x)/2+2*exp(-x)-3/2'
p=value('i',f'integrate(exp(2*x)-2*exp(-x),x)+1-integrate(exp(2*x)-2*exp(-x),x).subs(x,0)',f,345,'Independently integrate the given derivative and solve the constant using the original point(0,1). Verify both derivative and point.')
p['assertions']=[{'expression':f'diff({f},x)-(exp(2*x)-2*exp(-x))','expected':'0'},{'expression':f'({f}).subs(x,0)','expected':'1'}]
p2=value('ii-x','solve(exp(2*x)-2*exp(-x),x)[0]','log(2)/3',345)
p2['additional_comparisons']=[{'label':'printed stationary x','operation':{'kind':'rounded','operands':['log(2)/3'],'decimal_places':3},'printed_key_normalised':'0.231'}]
p2['key_normalisation_note']='The key gives a decimal x; its exact form is independently derived, with the written decimal compared separately.'
p3=reasoning('ii-nature','The stationary point is a minimum.',
 'The second derivative is2e^(2x)+2e^(−x)>0 for every real x. The stationary equation e^(3x)=2 has exactly one real solution because exponential is strictly increasing.',345,'matches')
p3['additional_operations']={'second_derivative':{'kind':'identity','operands':[f'diff({f},x,2)']}};p3['additional_operation_expected']={'second_derivative':'2*exp(2*x)+2*exp(-x)'}
add(7,141,'Recover the curve from dy/dx=e^(2x)−2e^(−x) and point(0,1), then find its stationary abscissa and classify it. Preserve the initial condition and the uniqueness argument.',[p,p2,p3],[EXPINT,CONSTANT,CURVE,STATIONARY,CLASSIFY],[ELEMENTARY])
p=value('i','log(3*1-2)+diff(log(3*x-2),x).subs(x,1)*(x-1)','3*x-3',345)
p2=value('ii-a','expand(6*x-2*(3*x-2))','4',345)
p3=definite('ii-b','6*x/(3*x-2)',2,6,'8+8*log(2)/3',141);p3['check_mode']='show/prove'
add(8,141,'For y=ln(3x−2),find the tangent at x=1;decompose6x/(3x−2)=2+A/(3x−2),then prove the integral on[2,6]. Original log curve needs x>2/3;the rational integral also stays clear of its pole.',[p,p2,p3],[EXPLICIT,ELEMENTARY,EXPINT,DEF],[DIVISION])
p=value('k','solve(log(2*x-1)/2-1,x)[0]','(exp(2)+1)/2',345,'The positive integrand from1 to k has integral½ln(2k−1). On k>1/2 the logarithm is strictly increasing; setting it equal1 gives a unique k>1. The entire interval is therefore regular.')
add(9,141,'Find exact k such that ∫₁ᵏ1/(2x−1)dx=1. The lower endpoint is1;the solution must remain above the pole1/2 and the positive integral forces k>1.',[p],[EXPINT,DEF,LOGDEF])
# Reuse figure assembly without mutating another builder's output.
from author_Goldie_C5_opening import fig,figures
figures.clear()
fig(7,140,'Exercise5A4 given two-branch area graph','Graph y=x+4/x has pole0,minimumP=(2,4),maximumQ=(−2,−4),positive region[2,5]and below-axis region[−4,−2]. The diagram defines the integration bounds.',[AREA,STATIONARY],'graph',[('Tuple((x+4/x).subs(x,2),(x+4/x).subs(x,-2))','Tuple(4,-4)')],parent='Exercise-5A:4')
fig(8,140,'Exercise5A5 inverse-graph area scaffold','Given e^x graph marksA=(ln5,0),B=(ln5,5),C=(0,5),E=(0,1);shadedEBC is the rectangle area5ln5 minus the under-curve area4. This geometry is the scaffold for the subsequent log integral.',[AREA,INVERSE],'graph',[('exp(log(5))','5'),('exp(0)','1')],parent='Exercise-5A:5')
corrections=[{'item_id':'8227:TB:Goldie:C5:Exercise-5A:5','continuation_pdf_pages':[141]}]
pages=[]
for page in range(139,142):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==139:ids+=['8227:TB:Goldie:C5:Prompt:2','8227:TB:Goldie:C5:Teaching-figure:6']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':ids,
  'continuation_item_ids':['8227:TB:Goldie:C5:Exercise-5A:5']if page==141 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
  'non_item_content':'All5A questions and connected subparts recorded. Page139 includes the pole warning/discontinuity prompt;5A5 continues on141. Both given diagrams have their own records.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-5A.json',{'scope':'All9questions and every requested5A response.','items':answers}),('census-Goldie-C5-5A.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete139–141 with5A5continuation.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
