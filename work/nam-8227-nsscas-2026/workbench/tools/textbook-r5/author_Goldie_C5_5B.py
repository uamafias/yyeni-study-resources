"""All fixed-source Exercise5B identities, primitives and definite integrals."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,indefinite,definite,compute,expression,equivalent
from author_YM_C4_composite_equations import roots,transform
TRIGINT='8227:2020:M2:T5:O01:D02';EXPINT='8227:2020:M2:T5:O01:D01';IDENTINT='8227:2020:M2:T5:O02:D01';SQUARED='8227:2020:M2:T5:O02:D02';DEF='8227:2020:M1:T9:O03:D01'
DOUBLE='8227:2020:M2:T3:O02:D03';RFORM='8227:2020:M2:T3:O02:D04';REC='8227:2020:M2:T3:O01:D01';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
ATTR={5:'9709 Paper33 Q4 June2013',6:'9709 Paper21 Q5 June2014',7:'9709 Paper2 Q6 June2007',8:'9709 Paper2 Q7 November2007',9:'9709 Paper22 Q4 June2010',10:'9709 Paper21 Q6 June2011',11:'9709 Paper31 Q9 June2011',12:'9709 Paper21 Q8 November2011',13:'9709 Paper21 Q3 November2014'}
# Read the page boundary again on2026-11-22: these printed entries begin on346.
KEY_PAGE_R6={(6,'ii-a'):346,(6,'ii-b'):346,(7,'i'):346,(7,'iii'):346,(8,'ii'):346,(9,'ii'):346,(10,'i'):346,(11,'ii-a'):346,(11,'ii-b'):346,(13,'i'):346,(13,'ii'):346}
def ev(page):
 if page==346:
  p=W/'checks/r6/parallel-notes/answer-tops/Goldie-346-full.png'
  return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 name='Goldie-C5-142'if page<146 else'Goldie-C5-146'if page<345 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None):
 for p in parts:
  kp=KEY_PAGE_R6.get((n,p['subpart']),p.pop('key_page_override',345));p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C5:Exercise-5B:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Keep explicitly requested identity/R-form proofs distinct from the following integrals. An identity used only as working is a component; choosing a representation that makes the integral possible is the integration demand. Bounded equations retain all roots.',
  'representation':'text','sketch_response_required':False,'exam_style':n in ATTR,'exam_style_basis':'Printed attribution '+ATTR[n]+'. Internal lead only; original examination not newly verified.'if n in ATTR else'Unattributed ordinary exercise.',
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if n==11 else'not applicable','quoted_value':note,
   'reason':'11(ii)(a) has multipliers4and2, both small integers, and a finite interval. It reduces to a polynomial in cosθ using the requested identity. QUAL03 does not specify a maximum multiplier of2.'if n==11 else'Trig identities/primitives are not bounded trig-equation asks.'},
   {'rule_id':'8227:QUAL04','status':'within'if n==6 else'not applicable','quoted_value':'6(ii)(b):∫₀^(π/2)6/(tanθ+cotθ)dθ, with removable endpoint exclusions.'if n==6 else note,
    'reason':'The original integrand is undefined at the endpoints but equals3sin2θ in the interior; its one-sided limits are0. The integral is evaluated by the continuous extension, not by crossing a pole.'if n==6 else'All other finite integral intervals are proper and avoid original poles.'}],
  'precision_angle_check':{'source':'Exact radian results throughout except11(ii)(a),whose key gives±0.572. There the original exact roots are retained and the printed3decimal-place values compared separately.',
   'comparison':'Do not confuse sin²x with sin2x, or lose the linear-argument factor. Endpoint holes in6(ii)(b) require explicit limiting treatment.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
parts=[indefinite(label,f,key,345)for label,f,key in [
 ('i','sin(x)-2*cos(x)','-cos(x)-2*sin(x)'),('ii','3*cos(x)+2*sin(x)','3*sin(x)-2*cos(x)'),('iii','5*sin(x)+4*cos(x)','-5*cos(x)+4*sin(x)'),
 ('iv','4*sec(x)**2','4*tan(x)'),('v','sin(2*x+1)','-cos(2*x+1)/2'),('vi','cos(5*x-pi)','sin(5*x-pi)/5'),
 ('vii','6*sec(2*x)**2','3*tan(2*x)'),('viii','3*sec(3*x)**2-sin(2*x)','tan(3*x)+cos(2*x)/2'),('ix','4*sec(x)**2-cos(2*x)','4*tan(x)-sin(2*x)/2')]]
add(1,145,'Nine indefinite integrals of sine/cosine sums and secant squares, including shifted2x+1and5x−π arguments and2x/3xscale factors. Preserve original tangent poles.',parts,[TRIGINT])
parts=[definite(label,f,lo,hi,key,345)for label,f,lo,hi,key in [
 ('i','sin(x)',0,'pi/3','1/2'),('ii','sec(x)**2',0,'pi/4','1'),('iii','cos(x)','pi/6','pi/3','(sqrt(3)-1)/2'),
 ('iv','sin(2*x)',0,'2*pi/3','3/4'),('v','cos(3*x)',0,'5*pi/6','1/3'),('vi','sec(2*x)**2','pi/8','pi/6','(sqrt(3)-1)/2'),
 ('vii','cos(2*x+pi/2)',0,'pi','0'),('viii','sec(x)**2+cos(4*x)',0,'pi/4','1'),('ix','cos(x)+sin(2*x)',0,'pi/6','3/4')]]
add(2,145,'Nine exact proper trig integrals with stated radian bounds. The cosine3x interval passes several sign regions but no singularity;the secant-square intervals remain strictly within regular components.',parts,[TRIGINT,DEF])
add(3,145,'Show sinxcosx=½sin2x, then use it to integrate sinxcosx on[0,π/3]. The proof is a requested result, not merely hidden working.',[
 transform('i','sin(x)*cos(x)','sin(2*x)/2',['sin(2*x)/2'],'All real radians.',145),definite('ii','sin(x)*cos(x)',0,'pi/3','3/8',345)],[DOUBLE,IDENTINT,DEF],[TRIGINT])
add(4,145,'Choose suitable identities to integrate cos²x and sin²x indefinitely and on[0,π/2]and[0,π/3]respectively. Keep each indefinite and definite output separate.',[
 indefinite('i-a','cos(x)**2','x/2+sin(2*x)/4',345),definite('i-b','cos(x)**2',0,'pi/2','pi/4',345),
 indefinite('ii-a','sin(x)**2','x/2-sin(2*x)/4',345),definite('ii-b','sin(x)**2',0,'pi/3','pi/6-sqrt(3)/8',345)],[IDENTINT,SQUARED,DEF],[TRIGINT])
p=value('i','0','Tuple(2,pi/6)',345,'Match Rcosα=√3,Rsinα=1 with R>0and0<α<π/2. The original coefficient pair fixes the quadrant and exact phase.')
p['operation']={'kind':'r-form-coefficients','operands':['1','sqrt(3)'],'target':'cos-minus','angle_unit':'radian'}
p2=definite('ii','1/(sqrt(3)*cos(x)+sin(x))**2','pi/6','pi/2','sqrt(3)/4',145);p2['check_mode']='show/prove'
add(5,145,'Express √3cosx+sinx as Rcos(x−α),with R>0and0<α<π/2,then show the reciprocal-square integral on[π/6,π/2]is√3/4. The transformed denominator2cos(x−π/6)does not vanish on these bounds.',[p,p2],[RFORM,TRIGINT,DEF])
p=transform('i','tan(x)+cot(x)','2/sin(2*x)',['1/(sin(x)*cos(x))'],'Original sinx≠0andcosx≠0.',145)
p2=value('ii-a','tan(pi/8)+cot(pi/8)','2*sqrt(2)',345)
p3=value('ii-b','integrate(3*sin(2*x),(x,0,pi/2))','3',345,'Inside the original interval,6/(tanx+cotx)=3sin2x. Both one-sided endpoint limits are0, so the removable-endpoint improper integral equals the proper integral of this continuous extension. The original expression is not falsely declared defined at either endpoint.')
p3['original_integrand']='6/(tan(x)+cot(x))';p3['original_common_domain']='0<x<π/2; endpoint values supplied only by limits.'
p3['additional_operations']={'interior_identity':{'kind':'trig-identity-residual','operands':['6/(tan(x)+cot(x))','3*sin(2*x)']},'endpoint_limits':{'kind':'identity','operands':['Tuple(limit(6/(tan(x)+cot(x)),x,0,dir="+"),limit(6/(tan(x)+cot(x)),x,pi/2,dir="-"))']},'continuous_extension_integral':{'kind':'proper-definite-integral','operands':['3*sin(2*x)','0','pi/2']}}
p3['additional_operation_expected']={'interior_identity':'0','endpoint_limits':'Tuple(0,0)','continuous_extension_integral':'3'}
add(6,145,'Prove tanθ+cotθ=2/sin2θ on its original domain;evaluate its sum atπ/8;hence integrate6/(tanθ+cotθ)on[0,π/2]. The last integrand has removable endpoint exclusions,treated explicitly by limits.',[p,p2,p3],[REC,DOUBLE,IDENTINT,DEF],[TRIGINT])
p=transform('i','cos(x)**2','(1+cos(2*x))/2',['(1+cos(2*x))/2'],'All real radians.',146)
p2=definite('ii','cos(x)**2',0,'pi/3','pi/6+sqrt(3)/8',146);p2['check_mode']='show/prove'
p3=definite('iii','sin(x)**2',0,'pi/3','pi/6-sqrt(3)/8',345)
add(7,146,'Express cos²x in terms of cos2x;hence prove its exact integral on[0,π/3];deduce the sine-square integral with the complementary identity.',[p,p2,p3],[DOUBLE,IDENTINT,SQUARED,DEF],[TRIGINT])
p=transform('i','(cos(x)+3*sin(x))**2','5-4*cos(2*x)+3*sin(2*x)',
 ['cos(x)**2+6*sin(x)*cos(x)+9*sin(x)**2','(1+cos(2*x))/2+3*sin(2*x)+9*(1-cos(2*x))/2'],'All real radians.',146)
p2=definite('ii','(cos(x)+3*sin(x))**2',0,'pi/4','(5*pi-2)/4',345)
add(8,146,'Prove(cosx+3sinx)²=5−4cos2x+3sin2x,then use the identity or another valid method to integrate the square on[0,π/4]. Expansion and power reduction preserve every cross term.',[p,p2],[DOUBLE,IDENTINT,SQUARED,DEF],[TRIGINT])
p=definite('i','cos(2*x)',0,'pi/4','1/2',146);p['check_mode']='show/prove'
p2=definite('ii','3*tan(x)**2','pi/6','pi/3','2*sqrt(3)-pi/2',345)
add(9,146,'Show the cosine2x integral on[0,π/4]is½;then use a suitable identity to integrate3tan²x on[π/6,π/3]. The latter uses tan²x=sec²x−1 and avoids tangent poles.',[p,p2],[TRIGINT,IDENTINT,DEF])
p=indefinite('i','4*exp(x)*(3+exp(2*x))','12*exp(x)+4*exp(3*x)/3',345)
p2=definite('ii','3+2*tan(x)**2','-pi/4','pi/4','(8+pi)/2',146);p2['check_mode']='show/prove'
add(10,146,'Integrate4e^x(3+e^(2x))indefinitely;show the exact integral of3+2tan²θ on[−π/4,π/4]. The two parts use distinct exponential simplification and trig-identity structures.',[p,p2],[EXPINT,TRIGINT,IDENTINT,DEF])
p=transform('i','cos(4*x)+4*cos(2*x)','8*cos(x)**4-3',['2*(2*cos(x)**2-1)**2-1+4*(2*cos(x)**2-1)'],'All real radians.',146)
p2=roots('ii-a','cos(4*x)+4*cos(2*x)-1',['-0.572','0.572'],345,[('cos','x','2**(-1/4)',1),('cos','x','-2**(-1/4)',1)],unit='radian',lo='-pi/2',hi='pi/2',approx=True)
p3=definite('ii-b','cos(x)**4',0,'pi/4','3*pi/32+1/4',345)
p2['key_page_override']=346;p3['key_page_override']=346
add(11,146,'Prove cos4θ+4cos2θ=8cos⁴θ−3;hence solve its equation equal to1 on[−π/2,π/2],and integrate cos⁴θ on[0,π/4]. The finite equation has two real roots;small integer4is not excluded by QUAL03.',[p,p2,p3],[DOUBLE,BND,ALL,IDENTINT,SQUARED,DEF],[TRIGINT])
p=transform('i','cos(3*x)','4*cos(x)**3-3*cos(x)',
 ['cos(2*x)*cos(x)-sin(2*x)*sin(x)','(2*cos(x)**2-1)*cos(x)-2*sin(x)**2*cos(x)'],'All real radians;expand cos(2x+x)as explicitly requested.',147)
p['method_requirement']='Start by expanding cos(2x+x), as the source requires.'
p2=definite('ii','2*cos(x)**3-cos(x)',0,'pi/6','5/12',147);p2['check_mode']='show/prove'
add(12,147,'By first expanding cos(2x+x),prove cos3x=4cos³x−3cosx;hence integrate2cos³x−cosx on[0,π/6]. The required expansion is an assessed method,not an optional model-solution embellishment.',[p,p2],[DOUBLE,IDENTINT,DEF],[TRIGINT])
add(13,147,'Integrate4cos²(θ/2)indefinitely,then evaluate the exact reciprocal-linear integral1/(2x+3)on[−1,6]. The half-angle power reduction is separate from the logarithmic proper integral.',[
 indefinite('i','4*cos(x/2)**2','2*sin(x)+2*x',345),definite('ii','1/(2*x+3)',-1,6,'log(15)/2',345)],[IDENTINT,SQUARED,EXPINT,DEF],[TRIGINT])
pages=[]
for page in [145,146]:
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page],
  'continuation_item_ids':['8227:TB:Goldie:C5:Example:8']if page==145 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every5B question/part on the page recorded. No given diagram or additional task;the Example8solution continuation is explicitly linked on145. Page147also starts numerical integration and awaits its combined census.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-5B.json',{'scope':'All13questions and every stated primitive,proof,exact integral and bounded root set.','items':answers}),('census-Goldie-C5-5B.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete145–146;5B12/13on147await numerical-opening census.','new_items':[],'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation'])
    if 'printed_key_normalised'in p:assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs')
