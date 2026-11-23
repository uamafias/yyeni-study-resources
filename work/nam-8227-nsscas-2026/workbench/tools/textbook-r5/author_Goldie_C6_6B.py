"""Every6Bresponse,with source recurrence traces and independent root references."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
from source_iteration_trace_r5 import trace
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';SEQUENCE='8227:2020:M2:T6:O02:D01';RELATE='8227:2020:M2:T6:O03:D01';REARRANGE='8227:2020:M2:T6:O03:D02';ITERATE='8227:2020:M2:T6:O04:D01';STOP='8227:2020:M2:T6:O04:D02'
STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';PARAM='8227:2020:M2:T4:O03:D02';GEOM='8227:2020:M2:T4:O03:D03';EXPINT='8227:2020:M2:T5:O01:D01';DEF='8227:2020:M1:T9:O03:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01';PRODUCT='8227:2020:M2:T4:O02:D01'
ATTR={8:'9709 Paper21 Q5 June2015',9:'9709 Paper2 Q2 November2007',10:'9709 Paper2 Q7 November2008',11:'9709 Paper22 Q7 November2009',12:'9709 Paper2 Q7 June2009',13:'9709 Paper22 Q6 June2010',14:'9709 Paper32 Q2 November2009',15:'9709 Paper3 Q4 June2009',16:'9709 Paper21 Q6 June2012'}
def ev(page):
 name='Goldie-C6-170'if page<174 else'Goldie-C6-174'if page<347 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,sketch=False,rep='text'):
 for p in parts:
  kp=p.pop('key_page_override',348);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 348),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[347,348])
 row={'item_id':f'8227:TB:Goldie:C6:Exercise-6B:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Keep graph/root-count,sign bracket,supplied rearrangement,iteration,conditional limit and precision decisions distinct. Explicit curves remain explicit;only16is parametric. Author-selected starts are labelled where the source leaves them open.',
  'representation':rep,'sketch_response_required':sketch,'exam_style':n in ATTR,'exam_style_basis':'Printed attribution '+ATTR[n]+'. Internal lead only;original examination not newly verified.'if n in ATTR else'Ordinary exercise without examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT08','status':'within','quoted_value':note,'reason':'Execute/interpret the supplied formulas and understand failure;formal derivative convergence conditions are not imposed.'}],
  'precision_angle_check':{'source':'Preserve the explicitly requested final2/3/5decimal places and the4/5decimal intermediate displays. Trig arguments/inverse tangent are radians. Full internal iterates remain unrounded.',
   'comparison':'Each numeric answer has an independent original-equation root reference. Recorded actual iterations terminate only after an original-equation rounding-cell sign certificate;source-specific uniqueness remains a separate argument.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row

def bracket(label,f,a,b,page):
 p=reasoning(label,f'A root lies in({a},{b}).','The original equation residual is continuous on this interval and has opposite endpoint signs. This proves existence;uniqueness needs its separate graph/monotonicity argument.',page,'show/prove')
 p['additional_operations']={'endpoint_signs':{'kind':'identity','operands':[f'Tuple(sign(({f}).subs(x,{a})),sign(({f}).subs(x,{b})))']}}
 got=compute(p['additional_operations']['endpoint_signs']);assert got[0]*got[1]==-1;p['additional_operation_expected']={'endpoint_signs':str(got)};return p

def iteration(label,f,F,start,a,b,key,answer_dp,display_dp=4,kp=348):
 p=value(label,'0',key,kp,'Run the source recurrence from the stated start,or an explicitly labelled author start if unspecified. Retain each unrounded state and required display;certify the final decimal cell against the original continuous equation and compare an independently bracketed reference.')
 p['operation']={'kind':'bracketed-source-root','operands':[f,str(a),str(b)],'rounding':{'decimal_places':answer_dp}}
 p['iteration_trace']=trace(F,start,f,a,b,answer_dp,display_dp);assert expression(p['iteration_trace']['answer'])==expression(key)
 return p

def fixed_proof(label,F,residual,page,domain):
 p=reasoning(label,'If the supplied iteration converges in its retained real domain,its limit solves the original equation.',
  'Pass to the limit only where the supplied map is continuous and defined. Substitute a common limit on both sides,retain the stated branch/domain,and rearrange to the original residual0. This conditional statement is not a proof that every start converges. '+domain,page,'show/prove')
 p['supplied_formula']=F;p['original_equation']=residual;p['original_common_domain']=domain;return p
add(1,171,'Bracketx³−x−2between1and2;use suppliedxₙ₊₁=∛(xₙ+2)to3dp. The source leaves the initial value open;the author trace starts1.5.',[
 bracket('i','x**3-x-2',1,2,171),iteration('ii','x**3-x-2','real_root(x+2,3)','3/2',1,2,'1.521',3)],[BRACKET,RELATE,ITERATE,STOP])
parts=[]
for label,conclusion,domain in [
 ('i','x=e^x−x⁴is exactly the original equation rearranged.','All realx;no division or inverse branch introduced.'),
 ('ii','x=ln(x⁴+x)is equivalent onx⁴+x>0.','Every original solution hasx⁴+x=e^x>0;conversely exponentiating the logarithmic equation recovers the original.'),
 ('iii','x=(e^x−x)^(1/4)selects nonnegativex.','It is not equivalent for the original negative root. The radicand is positive for realx,but a principal fourth root is nonnegative.'),
 ('iv','x=√((e^x−x)/x²)selects positivex and excludes0.','Original0isnotaroot,but its negative root is lost by the principal square-root branch;the quotient is undefined at0.')]:
 p=reasoning(label,conclusion,'Forx⁴+x−e^x=0,use real algebra and preserve every inverse-operation condition. '+domain,171,'key incomplete'if label in['iii','iv']else'show/prove');p['original_common_domain']=domain
 if label in ['iii','iv']:
  p['additional_operations']={'negative_original_root_signs':{'kind':'identity','operands':['Tuple(sign(16-2-exp(-2)),sign(1-1-exp(-1)))']}}
  p['additional_operation_expected']={'negative_original_root_signs':'Tuple(1,-1)'}
 parts.append(p)
row=add(2,171,'Show four proposed rearrangements ofx⁴+x−e^x=0. The two principal even-root forms lose the negative original root,so the unqualified source equivalence claim needs a branch qualification.',parts,[REARRANGE])
row['source_interpretation']={'real_domain':'The original has negative and positive roots;iii/ivare only nonnegative/positive branches.','warning':'Preserve the existing source caution on principal fourth/square roots;do not silently call them all globally equivalent.'}
add(3,171,'Brackete^(−x)−x+2on[2,3];execute suppliedxₙ₊₁=e^(−xₙ)+2to3dp. Author start2is explicit.',[
 bracket('i','exp(-x)-x+2',2,3,171),iteration('ii','exp(-x)-x+2','exp(-x)+2',2,2,3,'2.120',3)],[BRACKET,RELATE,ITERATE,STOP])
p=reasoning('ii','x=ln(6−x),withx<6,has the same real solutions ase^x+x−6=0.',
 'The original equation givese^x=6−x>0,so the natural log is legitimate. Conversely exponentiate the rearrangement. A denominator or lost branch is not introduced;the positive log argument is essential.',171,'show/prove')
add(4,171,'Brackete^x+x−6on[1,2],prove its supplied logarithmic rearrangement,and iterate from author-chosen1.5to3dp.',[
 bracket('i','exp(x)+x-6',1,2,171),p,iteration('iii','exp(x)+x-6','log(6-x)','3/2',1,2,'1.503',3)],[BRACKET,REARRANGE,ITERATE,STOP])
p=reasoning('i','Sketchy=e^xandy=x²+2on shared axes with a single positive intersection.',
 'The exponential lies below the parabola at0and eventually above it. Forx≤0,e^x≤1<x²+2. The difference derivativee^x−2xis positive everywhere:its minimum is2−2ln2>0. Thus exactly one crossing occurs.',348,'sketch')
p2=reasoning('ii','There is exactly one real root.',
 'The original differencee^x−x²−2is strictly increasing and has opposite signs at1and2;its negative-xvalues are negative. The graph and monotonicity prove uniqueness,not just one plotted intersection.',348,'matches')
p3=reasoning('iii','One usable rearrangement isx=ln(x²+2),with positive logarithm argument for every realx.',
 'Exponentiation recovers the original equation. Choosing a new rearrangement is the source’s open construction request;the syllabus specifically requires supplied formulas/rearrangements,so this choice is marked as extension while the subsequent execution still practises the supplied-form skill.',348,'matches')
row=add(5,171,'Sketch and justify unique intersectione^x=x²+2,choose a rearrangement,then iterate to3dp. Use the valid author choiceln(x²+2),start1.3;the construction part exceeds merely interpreting a supplied form.',[p,p2,p3,iteration('iv','exp(x)-x**2-2','log(x**2+2)','13/10',1,2,'1.319',3)],[ROOTG,RELATE,ITERATE,STOP],sketch=True)
row['scope_check']={'status':'in-scope-parts-only','basis':'i/ii assess graphical root reasoning. iii requires an invented map. iv is retained only as an internal benchmark for an adaptation that supplies the author map explicitly.','excluded_or_qualified_parts':['iii:open choice of rearrangement is extension','iv:execution depends on the excluded open choice; an in-scope adaptation must supply its map']}
row['value_level_scope_decisions']=[
 {'rule_id':'8227:LIMIT08','status':'within','applies_to':'i/ii; iv only with an explicitly supplied map adaptation','quoted_value':'e^x = x^2 + 2','reason':'Graphical root reasoning is prescribed. The recorded iv trace is an internal author-map benchmark, not evidence that the original supplies a map.'},
 {'rule_id':'8227:LIMIT08','status':'outside','applies_to':'iii only','quoted_value':'Rearrange this equation in the form x = F(x).','reason':'The original freely asks the learner to invent the rearrangement; LIMIT08 concerns supplied formulae/rearrangements.'}]
p=reasoning('i','One root is0and there is exactly one further positive root.',
 'At0both sides are0. For−1<x<0,ln(1+x)<0<x²,so none occur. Forx>0,the residualx²−ln(1+x)initially decreases then increases,because its derivative2x−1/(1+x)strictly increases. Its value at1is positive,so one further positive root lies in(0,1).',348,'show/prove')
p['additional_operations']={'zero_and_upper_sign':{'kind':'identity','operands':['Tuple((x**2-log(1+x)).subs(x,0),sign((x**2-log(1+x)).subs(x,1)))']}}
p['additional_operation_expected']={'zero_and_upper_sign':'Tuple(0,1)'}
row=add(6,171,'Showx²=ln(x+1)has0and one other root;find the second to3dpby iteration. Author choiceF=√ln(1+x),start0.5,keeps the positive branch;start0would stay at the already given root.',[p,iteration('ii','x**2-log(1+x)','sqrt(log(1+x))','1/2','1/2',1,'0.747',3)],[ROOTG])
row['scope_check']={'status':'in-scope-parts-only','basis':'Only i is retained as original prescribed-demand coverage. ii supplies no map; its numerical solution remains internal benchmark evidence for an adaptation that explicitly supplies the map.','excluded_or_qualified_parts':['ii:original supplies no map; author-chosen formula must be supplied in any prescribed-demand adaptation']}
row['value_level_scope_decisions']=[
 {'rule_id':'8227:LIMIT08','status':'within','applies_to':'i only','quoted_value':'x^2 = ln(x + 1)','reason':'Root existence/count on the actual log domain is prescribed; the second part does not add direct supplied-map iteration coverage.'},
 {'rule_id':'8227:LIMIT08','status':'outside','applies_to':'ii only','quoted_value':'Use the method of fixed-point iteration to find the second value to 3 decimal places.','reason':'The original gives no iteration map. Keep the independently verified author trace internal; a future in-scope adaptation must supply its map.'}]
p=reasoning('i','Sketchy=xincreasing from(0,0)andcosxdecreasing from(0,1)to(π/2,0);they intersect once.',
 'On[0,π/2],the differencecosx−xis strictly decreasing with opposite endpoint signs. The unique intersection lies in(0,1). This is a radian graph,not a degree-mode cosine curve.',348,'sketch')
add(7,172,'Sketchliney=xandcosxon[0,π/2],then use iteration to obtain the solution to5dp. Author start1and supplied cosine map are explicit.',[p,iteration('ii','cos(x)-x','cos(x)',1,0,1,'0.73909',5,5)],[ROOTG,ITERATE,STOP],sketch=True)
p=reasoning('i','The positive constant satisfiesa=2ln((16−a)/6).',
 'The original integral is6(e^(a/2)−1)+a. Set it equal10to get6e^(a/2)=16−a>0,so taking natural logs is valid and gives the stated rearrangement. Conversely it restores the integral condition;the originala>0andlogargument must be retained.',172,'show/prove')
p['additional_operations']={'integral_expression':{'kind':'identity','operands':['integrate(3*exp(x/2)+1,(x,0,a))']}}
p['additional_operation_expected']={'integral_expression':'6*exp(a/2)+a-6'}
add(8,172,'From∫₀ᵃ(3e^(x/2)+1)dx=10,a>0,derive the given logarithmic recurrence;starta₁=2,report every iteration to5dpandfinalato3dp.',[p,iteration('ii','6*exp(x/2)+x-16','2*log((16-x)/6)',2,1,2,'1.732',3,5)],[EXPINT,DEF,REARRANGE,ITERATE,STOP])
p=reasoning('iii','α³=12,and the real limit isα=∛12.',
 'The supplied recurrence isα=2α/3+4/α²at a finite nonzero limit. A limit0cannot satisfy the recurrence because4/x²would diverge. Multiply by3α²to obtainα³=12;the real cube root is unique. This is a conditional fixed-point interpretation,not a separate proof of convergence from all starts.',348,'matches')
p['additional_operations']={'fixed_point_equation_residual':{'kind':'identity','operands':['factor(3*x**2*(x-(2*x/3+4/x**2)))']}}
p['additional_operation_expected']={'fixed_point_equation_residual':'x**3-12'}
row=add(9,172,'The supplied recurrencexₙ₊₁=2xₙ/3+4/xₙ²,x₁=2,is stated to converge toα. Calculateαto2dpwith4dpsteps,then derive its equation and exact value. Source(i)is given setup,not an extra requested response.',[iteration('ii','x**3-12','2*x/3+4/x**2',2,2,3,'2.29',2,4),p],[SEQUENCE,RELATE,ITERATE,STOP])
row['source_interpretation']={'non_assessed_given_part':'(i)defines the recurrence,initial value and convergence;responses are(ii)and(iii).','domain':'Every evaluated iterate is nonzero;finite fixed limit cannot be0.'}
p=reasoning('i','Sketchcosxand2−2xon[0,π/2];the first decreases more slowly,so there is exactly one intersection.',
 'The differencecosx−2+2xhas derivative2−sinx>0and opposite endpoint signs. This supplies uniqueness beyond merely seeing a plotted crossing.',348,'sketch')
p3=fixed_proof('iii','1-cos(x)/2','cos(x)-2+2*x',172,'Cosine is continuous everywhere;the target root is in[0.5,1].')
add(10,172,'Use graphs to prove uniqueness ofcosx=2−2x,bracket the root on[0.5,1],prove the conditional fixed-point relation,and iterate from0.6to2dpwith4dpsteps.',[p,bracket('ii','cos(x)-2+2*x','1/2',1,172),p3,iteration('iv','cos(x)-2+2*x','1-cos(x)/2','3/5','1/2',1,'0.58',2,4)],[ROOTG,BRACKET,RELATE,ITERATE,STOP],sketch=True)
p=reasoning('i','At the interior maximum,tanx=2/x.',
 'Differentiatex²cosxto getx(2cosx−xsinx). The named maximum is interior,so0<x<π/2andcosx>0;only on that branch may we divide byxcosx. The endpoint stationary valuex=0is not the named interior maximum.',173,'show/prove')
p['additional_operations']={'derivative':{'kind':'identity','operands':['diff(x**2*cos(x),x)']}}
p['additional_operation_expected']={'derivative':'2*x*cos(x)-x**2*sin(x)'}
add(11,173,'Giveny=x²cosxon[0,π/2]with maximumM,derive tanx=2/x,bracket its radian root on[1,1.2],then usexₙ₊₁=atan(2/xₙ)to2dpwith4dpsteps. Author start1.1is explicit.',[p,bracket('ii','tan(x)-2/x',1,'6/5',173),iteration('iii','tan(x)-2/x','atan(2/x)','11/10',1,'6/5','1.08',2,4)],[STATIONARY,BRACKET,REARRANGE,ITERATE,STOP],[ELEMENTARY,PRODUCT],rep='graph')
p=value('i','Tuple(-1/2,(x*exp(2*x)).subs(x,-1/2))','Tuple(-1/2,-1/(2*E))',348,'The original derivativee^(2x)(1+2x)has exactly one zeroat−½;it changes negative to positive. Substitute in the original curve for the exact minimum ordinate.')
p['assertions']=[{'expression':'diff(x*exp(2*x),x).subs(x,-1/2)','expected':'0'}]
p2=reasoning('ii','The intersection withy=20satisfiesx=½ln(20/x),onx>0.',
 'The original equationxe^(2x)=20requires positivex. Divide byxand take natural logs to obtain2x=ln(20/x). Conversely exponentiating withx>0recovers the original. The positive branch is strictly increasing and has a unique intersection.',173,'show/prove')
add(12,173,'Giveny=xe^(2x),find exact minimumM;derive the logarithmic iteration for itsy=20intersection;start1.3,show4dpstepsandfind the root to2dp.',[p,p2,iteration('iii','x*exp(2*x)-20','log(20/x)/2','13/10',1,2,'1.35',2,4)],[STATIONARY,CLASSIFY,REARRANGE,ITERATE,STOP],[ELEMENTARY,PRODUCT],rep='graph')
p=reasoning('i','Sketchlnxincreasing and2−x²decreasing onx>0;they meet exactly once.',
 'The residuallnx+x²−2has derivative1/x+2x>0on the original log domain,with negative limit near0and positive values eventually. Therefore exactly one real-domain solution exists.',348,'sketch')
p3=fixed_proof('iii','sqrt(2-log(x))','log(x)+x**2-2',174,'x>0and2−lnx≥0;the principal square root enforces a nonnegative finite limit,which cannot be0because the logarithm then diverges.')
add(13,174,'Showuniquelnx=2−x²intersection graphically,bracket on[1.3,1.4],prove the supplied principal-square-root fixed-point implication,and iterate from1.3to2dpwith4dpsteps.',[p,bracket('ii','log(x)+x**2-2','13/10','7/5',174),p3,iteration('iv','log(x)+x**2-2','sqrt(2-log(x))','13/10','13/10','7/5','1.31',2,4)],[ROOTG,BRACKET,RELATE,ITERATE,STOP],sketch=True)
p=value('i','Tuple(3,4)','Tuple(3,4)',348,'The original cubic values at3and4are−10and19,respectively;it is continuous and the question supplies a unique real root.')
p['assertions']=[{'expression':'Tuple((x**3-8*x-13).subs(x,3),(x**3-8*x-13).subs(x,4))','expected':'Tuple(-10,19)'}]
add(14,174,'Forx³−8x−13=0,find consecutive-integer bounds and use supplied real cube-root iterationto2dpwith4dpsteps. Author start3is explicit.',[p,iteration('ii','x**3-8*x-13','real_root(8*x+13,3)',3,3,4,'3.43',2,4)],[BRACKET,ITERATE,STOP])
p2=fixed_proof('ii','(2*x**3+2)/(3*x**2-2)','x**3-2*x-2',174,'3α²−2must remain nonzero at a finite limit;at either denominator zero the numerator is nonzero,so a finite convergent sequence cannot have that limit. Multiplication then recoversα³−2α−2=0.')
add(15,174,'Bracketx³−2x−2on[1,2],prove the rational recurrence’s conditional fixed-point implication,and calculate to2dpwith4dpsteps. Author start2is explicit;avoid denominator zeros.',[bracket('i','x**3-2*x-2',1,2,174),p2,iteration('iii','x**3-2*x-2','(2*x**3+2)/(3*x**2-2)',2,1,2,'1.77',2,4)],[BRACKET,RELATE,ITERATE,STOP])
p=reasoning('i','p=(p+2)^(1/6)−½,on the branchp>−½.',
 'Fromx=(2t+1)^(−2),y=√(t+2),derive dy/dx=−(2t+1)³/[8√(t+2)]. Finite gradient−1requires t>−2andt≠−½,and its sign forces2p+1>0. Thus(2p+1)³=8√(p+2),so p+½=(p+2)^(1/6)with the positive branch. Raising powers without this sign check could add invalid roots.',174,'show/prove')
p['additional_operations']={'original_parametric_derivative':{'kind':'parametric-derivative','variable':'t','operands':['1/(2*t+1)**2','sqrt(t+2)']}}
p['additional_operation_expected']={'original_parametric_derivative':'-(2*t+1)**3/(8*sqrt(t+2))'}
row=add(16,174,'Parametricx=1/(2t+1)²,y=√(t+2)has gradient−1at parameterp. Derive the supplied sixth-root relation with its sign/domain constraints;start0.7,show5dpstepsandfindpto3dp.',[p,iteration('ii','(2*x+1)**3-8*sqrt(x+2)','(x+2)**(1/6)-1/2','7/10','3/5','4/5','0.678',3,5)],[PARAM,GEOM,REARRANGE,ITERATE,STOP])
row['source_interpretation']={'original_parameter_domain':'t≥−2,t≠−½;finite slope requires t>−2. Gradient−1forcesp>−½.','key_label_check':'Scale4 confirms the key prints16(ii),matching the exercise. The suspected(iii)label was a small-contact reading error and is cleared.'}
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,label,note,parent in [(18,'6B11given polynomial-cosine hump','Graphx²cosxon[0,π/2]has endpoint zeros and one named interior maximum;the endpointx=0isnot the maximum being solved.','Exercise-6B:11'),(19,'6B12given exponential-product curve','Graphxe^(2x)has minimum(−½,−1/(2e)),crossesO,andapproaches0frombelow asx→−∞. The later y=20intersection is on its positive branch.','Exercise-6B:12')]:
 fig(n,173,label,note,[STATIONARY,ROOTG],'graph',parent=parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C6:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C6:');f['source_evidence']=ev(173)
pages=[]
for page in range(171,175):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==171:ids+=['8227:TB:Goldie:C6:Activity:2']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':6,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every6Bquestion and actual requested response enumerated;source9(i)is given setup. Page171includes the previously missingActivity6.2. Both given graphs on173have separate records.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C6-6B.json',{'scope':'All16questions,every actual requested response,and every performed iteration display;author start choices explicit.','items':answers}),('census-Goldie-C6-6B.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':6,'source_path':SRC,'source_sha256':SHA,'scope':'Complete171–174includingActivity6.2andboth given graphs.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',sum(len(p.get('iteration_trace',{}).get('records',[]))for r in answers for p in r['subparts']),'recorded iteration states;two given graphs')
