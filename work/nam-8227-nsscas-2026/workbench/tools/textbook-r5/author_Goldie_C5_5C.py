"""Every numerical-integration exercise response, including all sketch copies."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,definite,compute,expression,equivalent
TRAPSET='8227:2020:M2:T5:O03:D01';TRAP='8227:2020:M2:T5:O03:D02';SKETCH='8227:2020:M2:T5:O04:D01';BIAS='8227:2020:M2:T5:O04:D02'
DEF='8227:2020:M1:T9:O03:D01';EXPINT='8227:2020:M2:T5:O01:D01';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';EXPLICIT='8227:2020:M1:T8:O03:D01'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';PRODUCT='8227:2020:M2:T4:O02:D01';MOTION='8227:2020:M1:T9:O04:D03'
ATTR={7:'9709 Paper21 Q1 November2014',8:'9709 Paper2 Q6 June2005',9:'9709 Paper2 Q7 June2007',10:'9709 Paper2 Q8 November2007',11:'9709 Paper21 Q6 June2014'}
def ev(page):
 name='Goldie-C5-150'if page<154 else'Goldie-C5-154'if page<345 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,rep='text',sketch=False):
 for p in parts:
  kp=p.pop('key_page_override',346);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C5:Exercise-5C:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'The trapezium setup,estimate,sketch or bias justification is assessed as actually requested. An explicit curve and its stationary/tangent questions remain explicit calculus. Author quadrature/exact audits do not impose out-of-syllabus antiderivatives on learners.',
  'representation':rep,'sketch_response_required':sketch,'exam_style':n in ATTR,'exam_style_basis':'Printed attribution '+ATTR[n]+'. Internal lead; original source not newly verified.'if n in ATTR else'Ordinary exercise without examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL11','status':'within'if n in[3,4,5,6,8,9]else'not applicable','quoted_value':note,
   'reason':'Specified simple graph/sketch and finite interval;where asked, justify bias from curve/chord geometry. Formal second derivatives are author support,not the only acceptable learner method.'if n in[3,4,5,6,8,9]else'No over/under sketch justification requested in this item.'},
   {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':'11(ii): log₁₀x evaluated numerically at five nodes on[1,17].'if n==11 else note,'reason':'Calculator evaluation of common logarithms in a required numerical rule is not a requested change-of-base derivation.'if n==11 else'No change-of-base question.'}],
  'precision_angle_check':{'source':'Q8–10estimates2decimal places;Q11(ii)3significant figures. Q3–5compare refining estimates and ask a justified number of decimals. Trig inputs are radians.',
   'comparison':'Use unrounded ordinates,then final requested precision. Several agreeing estimates alone are not a rigorous error bound;Q6deliberately demonstrates aliasing.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row

def trapez(label,f,lo,hi,n,key,kp=346,dp=None,sf=None):
 p=value(label,'0',key,kp,'Set h=(b−a)/n from the source bounds,calculate every original ordinate,and add the individual trapezia. Round only the final estimate. The key is not an input to the ordinate calculation.')
 p['operation']={'kind':'trapezium-rule','operands':[f,str(lo),str(hi)],'strips':n}
 if dp is not None:p['operation']['rounding']={'decimal_places':dp}
 if sf is not None:p['operation']['rounding']={'significant_figures':sf}
 p['additional_operations']={'unrounded_trapezium':{'kind':'trapezium-rule','operands':[f,str(lo),str(hi)],'strips':n}}
 return p

def manual(label,answer,why,status='matches',kp=346):return reasoning(label,answer,why,kp,status)

p=value('i','0','458',346,'Read the seven speed values at10second intervals. Sum six trapezium areas in the speed–time plane;metres/second times seconds gives metres.')
p['operation']={'kind':'tabulated-trapezium','operands':['Tuple(0,10,20,30,40,50,60)','Tuple(0,5.0,6.7,8.2,9.5,10.6,11.6)']};p['units']='m';p['printed_key_units']='m'
p2=manual('ii','A curved speed graph is replaced by straight segments;the given speeds are rounded to2significant figures.',
 'Only seven rounded measurements are supplied. Piecewise linear interpolation does not recover unknown acceleration between measurements. The source key names both straight-line curve approximation and2significant-figure input speeds.')
add(1,151,'Given train speeds0,5.0,6.7,8.2,9.5,10.6,11.6m/s at0,10,…,60s,estimate the one-minute distance and give two reasons accuracy is limited.',[p,p2],[TRAPSET,TRAP,MOTION],rep='table')
parts=[]
for label,n,prefix in [('i',4,'3.1349'),('ii-10',10,'3.1399'),('ii-20',20,'3.1411')]:
 op={'kind':'trapezium-rule','operands':['1/(1+x**2)','0','1'],'strips':n,'scale':'4'}
 exact=value(label,'0',prefix,346,'Compute four times the trapezium estimate from the original quarter-pi integral. The key uses an ellipsis: compare its literal four-decimal prefix by truncation,not by pretending it is a rounded value.')
 exact['operation']={'kind':'decimal-prefix','operands':[str(compute(op))],'decimal_places':4}
 exact['additional_operations']={'unrounded_trapezium':op}
 exact['printed_key_prefix']=prefix
 if n==4:
  exact['expected_source_key_status']='key wrong'
  exact['author_answer_form']='3.131176470588… for four strips. The printed3.1349… instead matches five strips.'
  exact['additional_operations']['five_strip_diagnostic']={'kind':'decimal-prefix','operands':[str(compute({**op,'strips':5}))],'decimal_places':4}
  exact['additional_operation_expected']={'five_strip_diagnostic':'3.1349'}
 parts.append(exact)
parts.append(manual('iii','π≈3.14 is suggested by refinement,consistent with the independently known true value.',
 'Each estimate is4times the trapezium approximation of the stated quarter-circle-arctangent integral. Refinement provides empirical decimal evidence rather than a universal error guarantee. Verify source prefixes and never claim finite agreement proves the next digit.'))
add(2,151,'Use the given ∫₀¹1/(1+x²)dx=π/4 to estimateπ with4,10and20strips,then choose a defensible decimal display. Retain the factor4 between the integral andπ.',parts,[TRAPSET,TRAP])
p=manual('i-sketch','On[0,1.6],y=√(1+x²)starts(0,1),increases and is convex;endpoint(1.6,√3.56).',
 'The derivative x/√(1+x²) is nonnegative and second derivative(1+x²)^(−3/2)>0. The source sketch has this positive increasing convex shape. These formulas support the features;the learner may use an accurate plot.',status='sketch')
parts=[p]+[trapez(label,'sqrt(1+x**2)',0,'8/5',n,key,dp=6)for label,n,key in [('ii-h0.8',2,'2.179218'),('ii-h0.4',4,'2.145242'),('ii-h0.2',8,'2.136756'),('ii-h0.1',16,'2.134635')]]
p=manual('iii','The recommended value is2.13to2decimal places.',
 'The displayed estimates decrease toward a stable value;this is the source intended numerical justification. Independently,an author-only exact audit uses[x√(1+x²)+asinhx]/2atx=1.6and0,giving2.133936…which rounds to2.13. Hyperbolic functions are not added to the learner demand. Finite estimates alone do not prove an error bound.')
p['additional_operations']={'independent_true_integral_2dp':{'kind':'rounded','operands':['(x*sqrt(1+x**2)+asinh(x)).subs(x,8/5)/2'],'decimal_places':2}};p['additional_operation_expected']={'independent_true_integral_2dp':'2.13'};parts.append(p)
add(3,151,'Sketch√(1+x²)on[0,1.6];use widths0.8,0.4,0.2,0.1for four estimates;state as many justified decimal places as the evidence allows.',parts,[SKETCH,TRAPSET,TRAP],sketch=True)
p=manual('i-sketch','On[0,1],y=√(sinx)starts at0,increases concavely downward and ends at√sin1;the initial tangent is vertical.',
 'sinx>0andcosx>0inside this radian interval. y′=cosx/(2√sinx)>0and y″=−√sinx/2−cos²x/(4sin^(3/2)x)<0. Near0,y≈√x,so the slope is unbounded. The source graph shows the concave increasing shape.',status='sketch')
parts=[p]+[trapez(label,'sqrt(sin(x))',0,1,n,key,dp=6)for label,n,key in [('ii-1',1,'0.458658'),('ii-2',2,'0.575532'),('ii-4',4,'0.618518'),('ii-8',8,'0.634173'),('ii-16',16,'0.639825')]]
for part in parts[1:]:
 part['operation'].pop('rounding')
 part['printed_approximation_check']={'absolute_error_strictly_below':'0.000001','required_rounding':None,'source_claim':'The source lists six-decimal approximations without requiring six decimal places. Two values truncate rather than round to nearest. Compare within one displayed last unit and retain exact unrounded values for canonical use.'}
parts.append(manual('iii','The source recommends0.64to2decimal places.',
 'The increasing underestimates approach a value consistent with0.64. Independent high-precision quadrature of the original√sinx supplies an author check;the finite refinement sequence alone is not a rigorous error guarantee.'))
add(4,152,'Sketch√sinx on[0,1]radians,estimate using1,2,4,8,16strips,and justify a final decimal display. The endpoint square-root slope explains slow convergence.',parts,[SKETCH,TRAPSET,TRAP],sketch=True)
p=manual('i-sketch','On[0,1],y=4/(1+x²)decreases from4to2 with horizontal tangent at0;concavity changes atx=1/√3.',
 'The derivative−8x/(1+x²)² is nonpositive. The second derivative8(3x²−1)/(1+x²)³ changes sign once. The given key graph decreases smoothly between the labelled endpoint heights;it does not require a falsely uniform concavity.',status='sketch')
parts=[p]+[trapez(label,'4/(1+x**2)',0,1,n,key,dp=6 if n>2 else 1)for label,n,key in [('ii-h1',1,'3'),('ii-h0.5',2,'3.1'),('ii-h0.25',4,'3.131176'),('ii-h0.125',8,'3.138988')]]
parts.append(manual('iii','Recommended2decimal-place value3.14.',
 'The refined trapezium estimates approach3.14. The author independently checks the known exact integralπ,whose2decimal-place display agrees. The learner is being asked for numerical refinement,not an inverse-tangent antiderivative.'))
add(5,152,'Sketch4/(1+x²)on[0,1];estimate with widths1,0.5,0.25,0.125;justify the reported decimals. Do not confuse the reciprocal denominator with√(1+x²).',parts,[SKETCH,TRAPSET,TRAP],sketch=True)
parts=[trapez(label,'2-cos(2*pi*x)',0,2,n,key)for label,n,key in [('i-a',1,'2'),('i-b',2,'2'),('i-c',4,'4'),('i-d',8,'4')]]
for label,n,description in [('ii-a',1,'One rectangle ofheight1across[0,2],area2.'),('ii-b',2,'Two unit-width rectangles eachheight1,area2.'),('ii-c',4,'Four width½trapezia with endpoint heights1,3,1,3,1,area4.'),('ii-d',8,'Eight width¼trapezia with heights1,2,3,2,1,2,3,2,1,area4.')]:
 p=manual(label,'Draw the same y=2−cos2πx curve on[0,2]and shade the requested interpolating trapezia. '+description,
  'The curve has minima1at0,1,2and maxima3at½,3/2. Each shading uses its own equally spaced node values;1and2strip grids sample only minima and miss both humps. Four and eight strips give the same exact area while representing the curve differently. The four printed key panels agree with these node sets.',status='sketch')
 p['additional_operations']={'node_heights':{'kind':'identity','operands':['Tuple('+','.join(f'(2-cos(2*pi*x)).subs(x,{2*j}/{n})'for j in range(n+1))+')']}}
 p['additional_operation_expected']={'node_heights':{1:'Tuple(1,1)',2:'Tuple(1,1,1)',4:'Tuple(1,3,1,3,1)',8:'Tuple(1,2,3,2,1,2,3,2,1)'}[n]};parts.append(p)
parts.append(definite('iii','2-cos(2*pi*x)',0,2,'4',346))
add(6,152,'Estimate∫₀²(2−cos2πx)dx with widths2,1,0.5,0.25;on four graph copies shade each interpolant;then find the exact integral. Equal coarse estimates2are both wrong:refinement can alias an oscillating curve.',parts,[TRAPSET,TRAP,SKETCH,DEF],sketch=True)
add(7,152,'Use4intervals to estimate∫₁⁵|2^x−8|dx. Read the modulus before evaluating nodes;the zero atx=3is a corner on the grid.',[
 trapez('estimate','Abs(2**x-8)',1,5,4,'27')],[TRAPSET,TRAP])
p=manual('ii-y','M has x=e and y=1/e.',
 'For f=lnx/x onx>0,f′=(1−lnx)/x²=0onlyat e. It changes positive to negative,so this is the given maximum. Substitution gives1/e. The source asks to show the abscissa and write the ordinate.')
p['additional_operations']={'stationary_condition':{'kind':'identity','operands':['diff(log(x)/x,x).subs(x,E)']},'ordinate':{'kind':'identity','operands':['(log(x)/x).subs(x,E)']}}
p['additional_operation_expected']={'stationary_condition':'0','ordinate':'1/E'}
p2=manual('iv','The trapezium estimate is an underestimate.',
 'On[1,4],the curve bends downward:each interpolation chord lies below it. Author check f″=(2lnx−3)/x³<0because2ln4<3. The interval is crucial;the full positive-domain curve is not concave down everywhere.')
row=add(8,152,'Given y=lnx/x on0<x≤4,find x-interceptA,show maximum abscissae and find its ordinate;estimate∫₁⁴lnx/x with3intervals to2dp;justify its bias on that interval.',[
 value('i','Tuple(solve(log(x),x)[0],0)','Tuple(1,0)',346),p,trapez('iii','log(x)/x',1,4,3,'0.89',dp=2),p2],[STATIONARY,CLASSIFY,TRAPSET,TRAP,BIAS],[ELEMENTARY,PRODUCT],rep='graph')
p=manual('iv','The trapezium estimate is an underestimate.',
 'On[0,π/2],the given curve bends downward,so each chord lies below it. Author check f″=−2e^xsinx≤0on the interval;the graph argument is sufficient for a learner.')
add(9,153,'Given y=e^xcosx on[0,π/2],find y-interceptA and the maximum abscissa,estimate its integral with3intervals to2dp,then justify trapezium bias.',[
 value('i','Tuple(0,(exp(x)*cos(x)).subs(x,0))','Tuple(0,1)',346),{'subpart':'ii','operation':{'kind':'bounded-trig-equation','operands':['cos(x)-sin(x)','0','pi/2']},'printed_key_normalised':'FiniteSet(pi/4)','method':'Solve the derivative-zero condition on the original finite interval after noting e^x>0. The single rootπ/4has a positive-to-negative derivative sign change.','key_page_override':346,'source_ratio_branches':[{'function':'tan','argument':'x','ratio':'1','power':1,'angle_unit':'radian'}]},trapez('iii','exp(x)*cos(x)',0,'pi/2',3,'1.77',dp=2),p],[STATIONARY,CLASSIFY,TRAPSET,TRAP,BIAS],[ELEMENTARY,PRODUCT],rep='graph')
p=value('i','solve(2*x-x**2,x)[1]','2',346,'The given maximumM is the positive stationary root2;the other root0is a local minimum,notM.')
p2=value('ii-tangent','(x**2*exp(-x)).subs(x,1)+diff(x**2*exp(-x),x).subs(x,1)*(x-1)','x/E',154,'Form the tangent through its original point atx=1;the independent result y=x/e passes through the origin.');p2['check_mode']='show/prove'
add(10,154,'Given the x²e^(−x)curve and its positive maximumM,find M’s abscissa,show the tangent atx=1passes throughO,and estimate its integral on[1,3]with2intervals to2dp.',[p,p2,trapez('iii','x**2*exp(-x)',1,3,2,'0.95',dp=2)],[STATIONARY,EXPLICIT,TRAPSET,TRAP],[ELEMENTARY,PRODUCT],rep='graph')
p=definite('i','6/(2*x-7)',6,16,'log(125)',154);p['check_mode']='show/prove';p['source_reading_note']='Scale4 confirms lower limit6,not4. The stated ln125 target is correct.'
add(11,154,'Show∫₆¹⁶6/(2x−7)dx=ln125;then estimate∫₁¹⁷log₁₀x dx with4intervals to3significant figures. The logarithm base is10only in the numerical second part.',[p,trapez('ii','log(x,10)',1,17,4,'13.5',sf=3)],[EXPINT,DEF,TRAPSET,TRAP])
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,page,label,note,parent,rep,checks in [
 (20,151,'5C1 given speed/time table','Seven speeds at ten-second spacing;ordinate unitsm/sand abscissaseconds. Integrating the interpolant gives a distance estimate,not a time average.','Exercise-5C:1','table',[('10*(0/2+5+6.7+8.2+9.5+10.6+11.6/2)','458')]),
 (21,152,'5C8 given logarithmic curve','Graph ln x/x on0<x≤4crosses atA=(1,0)and has maximumM=(e,1/e). It has no point atx=0;the integral itself begins1.','Exercise-5C:8','graph',[('(log(x)/x).subs(x,1)','0')]),
 (22,153,'5C9 given exponential-cosine hump','Graph e^xcosx on[0,π/2]startsA=(0,1),peaks atπ/4,and ends on thex-axis atπ/2.','Exercise-5C:9','graph',[('Tuple((exp(x)*cos(x)).subs(x,0),(exp(x)*cos(x)).subs(x,pi/2))','Tuple(1,0)')]),
 (23,154,'5C10 given polynomial-exponential curve','Graph x²e^(−x)touchesOat its local minimum,has positive maximum atx=2,and tends to0asx→+∞;the left negative-x branch grows positively.','Exercise-5C:10','graph',[('limit(x**2*exp(-x),x,oo)','0')])]:
 fig(n,page,label,note,[TRAPSET,TRAP],rep,checks,parent)
for f in figures:f['source_evidence']=ev(f['pdf_page'])
corrections=[{'item_id':'8227:TB:Goldie:C5:Exercise-5C:8','continuation_pdf_pages':[153]}]
pages=[]
# Page151also has Prompt4;page154is fully owned here. 151census is assembled by numerical-opening.
for page in range(152,155):
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':['8227:TB:Goldie:C5:Exercise-5C:8']if page==153 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every numerical task,graph response and given figure recorded. 5C8continues153;5C10/11end154. No additional boxed prompt is omitted.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-5C.json',{'scope':'All11questions; every required estimate,graph copy,reason and exact check.','items':answers}),('census-Goldie-C5-5C.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete152–154;151awaitsPrompt4combined census.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);same=equivalent(got,expression(p['printed_key_normalised']))
    if p.get('printed_approximation_check'):same=bool(abs((got-expression(p['printed_key_normalised'])).evalf(50))<expression(p['printed_approximation_check']['absolute_error_strictly_below']))
    assert (not same)if p.get('expected_source_key_status')=='key wrong'else same,(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'given figures')
