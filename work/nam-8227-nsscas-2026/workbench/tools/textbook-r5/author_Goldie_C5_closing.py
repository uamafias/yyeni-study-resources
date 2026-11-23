"""All five reference blocks and every final numerical-investigation subtask."""
import hashlib,json
import sympy as sp
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
from author_Goldie_C5_opening import fig,figures
figures.clear()
POWERINT='8227:2020:M1:T9:O01:D02';EXPINT='8227:2020:M2:T5:O01:D01';TRIGINT='8227:2020:M2:T5:O01:D02'
TRAPSET='8227:2020:M2:T5:O03:D01';TRAP='8227:2020:M2:T5:O03:D02';SKETCH='8227:2020:M2:T5:O04:D01';BIAS='8227:2020:M2:T5:O04:D02'
def ev(page):
 name='Goldie-C5-154'if page<345 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def no_key(label,answer,why):
 p=reasoning(label,answer,why,None,'no key');p['inspected_key_pdf_pages']=[345,346]
 p.update(source_pdf_page=156,source_evidence=ev(156),answer_pdf_page=None,answer_printed_page=None,key_evidence=ev(346),review_date='2026-11-18')
 return p
parts=[]
p=no_key('left-right-claim','The claim that both endpoint-rectangle rules always underestimate is false.',
 'For increasing f=1+x on[0,1],one left rectangle has area1and one right rectangle has area2,while the integral is3/2. For decreasing f=2−x,the signs reverse. Monotonicity can justify opposite left/right bounds;an arbitrary nonmonotonic curve needs its local shape considered. The source’s provisional learner statements are the propositions to investigate,not errors in a printed answer key.')
p['additional_operations']={'increasing_example':{'kind':'identity','operands':['Tuple((1+x).subs(x,0),(1+x).subs(x,1),integrate(1+x,(x,0,1)))']},'decreasing_example':{'kind':'identity','operands':['Tuple((2-x).subs(x,0),(2-x).subs(x,1),integrate(2-x,(x,0,1)))']}}
p['additional_operation_expected']={'increasing_example':'Tuple(1,2,3/2)','decreasing_example':'Tuple(2,1,3/2)'};parts.append(p)
p=no_key('average-identity','For the same partition,the average of left and right rectangle sums equals the trapezium sum exactly.',
 'On each interval of widthhᵢ,the average is[hᵢf(xᵢ)+hᵢf(xᵢ₊₁)]/2,the area of that interpolation trapezium. Summing proves the statement,including a nonuniform common partition. For an equal grid this becomes h/2[end ordinates+twice the middle ordinates]. This is an algebraic identity,not a statement that the approximation equals the true integral.')
p['additional_operations']={'one_segment_average_residual':{'kind':'identity','operands':['(c*a+c*b)/2-c*(a+b)/2']}}
p['additional_operation_expected']={'one_segment_average_residual':'0'};parts.append(p)
p=no_key('midpoint-counterexample','Midpoint rectangles are not always more accurate than trapezia for every function and every interval count.',
 'Use f(x)=2+x⁴−(9/5)x² on[0,1],with one interval. The exact integral and trapezium sum are both8/5. The midpoint value is129/80,so its absolute error is1/80and the trapezium error is0. A linear function also makes both methods exact. This refutes the unrestricted claim without denying midpoint accuracy for many smooth convex/concave examples.')
f='2+x**4-9*x**2/5'
p['additional_operations']={'counterexample_I_T_M':{'kind':'identity','operands':[f'Tuple(integrate({f},(x,0,1)),(({f}).subs(x,0)+({f}).subs(x,1))/2,({f}).subs(x,1/2))']}}
p['additional_operation_expected']={'counterexample_I_T_M':'Tuple(8/5,8/5,129/80)'};parts.append(p)
p=no_key('specification-and-collection','Use a shared interval[0,1],counts1,2,4,8,16,and convex,concave,mixed-curvature and numerically integrated functions. Retain original formulas,node positions and all four estimates.',
 'Choose1+x²,2−x²,the counterexample polynomial,and e^(−x²). Draw each shape first and keep the same node partition for L,R,T,M. Compute signed and absolute errors where the exact integral is available. For e^(−x²),a high-precision independent quadrature supplies an author reference;learners can investigate numerically without a new special-function demand. This answers the source questions on technology,example choice,interval counts and collecting enough varied evidence.')
experiments=[]
for function in ['1+x**2','2-x**2',f,'exp(-x**2)']:
 for n in [1,2,4,8,16]:
  h=sp.Rational(1,n);F=expression(function);x=expression('x')
  L=sp.Add(*(F.subs(x,j*h)for j in range(n)))*h;R=sp.Add(*(F.subs(x,(j+1)*h)for j in range(n)))*h
  M=sp.Add(*(F.subs(x,(j+sp.Rational(1,2))*h)for j in range(n)))*h;T=(L+R)/2
  truth=sp.integrate(F,(x,0,1));assert sp.simplify(T-(L+R)/2)==0
  experiments.append({'function':function,'interval':['0','1'],'strips':n,'L':str(sp.N(L,17)),'R':str(sp.N(R,17)),'T':str(sp.N(T,17)),'M':str(sp.N(M,17)),
   'reference_integral':str(sp.N(truth,17)),'T_signed_error':str(sp.N(T-truth,17)),'M_signed_error':str(sp.N(M-truth,17)),
   'reference_kind':'author quadrature cross-check required; special-function expression not learner scope'if function=='exp(-x**2)'else'exact elementary integral'})
p['numerical_experiments']=experiments
p['additional_operations']={'Gaussian_reference_integral':{'kind':'proper-definite-integral','operands':['exp(-x**2)','0','1']}}
p['additional_operation_expected']={'Gaussian_reference_integral':'sqrt(pi)*erf(1)/2'};parts.append(p)
p=no_key('processing-sketches-and-reporting','Organise one comparison table per function,show L,R,T,M and signed/absolute error across the five grids,and sketch the corresponding interpolation shapes.',
 'For1+x²and2−x²,the curvature signs explain the opposite midpoint/trapezium biases. The mixed-curvature polynomial has a special one-strip cancellation;report it as a counterexample,not a general law. e^(−x²)changes curvature at1/√2on this interval,so a single blanket convexity claim is invalid. Preserve that source graphs illustrate an increasing curve but give no numeric formula to recover. A diagram of that curve alone does not prove a universal accuracy ordering.')
p['required_sketch_features']=['Use the original function and interval for each experiment.','Align rectangle/trapezium boundaries with the selected grid.','Mark which heights are left,right or midpoint evaluations.','Show the mixed-curvature/inflection case rather than drawing every example as globally convex.']
parts.append(p)
p=no_key('interpretation-and-other-methods','A useful rule should converge under stated regularity,be practical for available data,and support an honest accuracy estimate;no method is universally best on all finite grids.',
 'For continuous f on a closed interval,the rectangle/trapezium sums converge as the maximum strip width tends to0. Where curvature is controlled,the graph supports directional error claims. Finite agreement is not a rigorous bound:5C6already gives two agreeing coarse estimates that miss two humps. Midpoint evaluation needs values between data nodes,which may be unavailable for an experimental table. Other rules such as Simpson may be mentioned as extension,but are not added to the8227prescribed trapezium demand. This answers the source’s requests to define good,identify desirable features and conclude with other methods.')
parts.append(p)
row={'item_id':'8227:TB:Goldie:C5:Problem-solving-investigation:1','source_pdf_page':156,
 'notes':'Investigate Vesna’s three left/right-average/midpoint claims,choose varied examples and technology,collect and organise results,draw the necessary graphs,and explain what makes a numerical-integration rule useful. All source guiding subtasks on156–157are answered;rectangle/midpoint extensions remain distinct from prescribed trapezium evidence.',
 'assessed_8227_demand_ids':[TRAPSET,TRAP,SKETCH,BIAS],'component_demand_ids':[],
 'mapping_rationale':'The investigation directly compares trapezium estimates and requires graph/error reasoning. Left/right and midpoint algorithms are comparative extensions,not additional8227methods. Author counterexamples and selected data answer the open investigation;they do not define a required classroom recipe.',
 'representation':'graph','sketch_response_required':True,'exam_style':False,'exam_style_basis':'Problem-solving investigation,not an exam attribution.',
 'scope_check':{'status':'in-scope-parts-only','basis':'Trapezium and simple graph-bias reasoning prescribed;rectangle/midpoint rules and formal convergence/error theorems are comparative enrichment.','excluded_or_qualified_parts':['Do not make midpoint/rectangle algorithms or formal convergence theorems mandatory8227content.']},
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL11','status':'within','quoted_value':'Compare simple graphs and trapezium over/under bias;the source also asks broader midpoint-rule claims.','reason':'Retain graph justification without requiring a formal second-derivative/error theorem. Extension methods do not add syllabus scope.'}],
 'precision_angle_check':{'source':'No mandatory numeric precision;the task asks how outcomes and accuracy should be reported.','comparison':'Keep17-digit author experiment values with their original formulas and grid;they are numerical evidence,not exact source answers or a universal error bound.'},
 'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
answers=[row]
corrections=[{'item_id':row['item_id'],'continuation_pdf_pages':[157]}]
for n,label,note,teaches,checks in [
 (24,'Key points1 power integral','∫kxⁿdx=kx^(n+1)/(n+1)+c for n≠−1,on real branches where the original power is defined. The reciprocal case is the next logarithm block.',[POWERINT],[('diff(k*x**(n+1)/(n+1),x)','k*x**n')]),
 (25,'Key points2 exponential integrals','∫e^x=e^x+c and∫e^(ax+b)=e^(ax+b)/a+c for a≠0. A zero linear coefficient needs its separate constant-integrand case.',[EXPINT],[('diff(exp(x),x)','exp(x)'),('diff(exp(a*x+b)/a,x)','exp(a*x+b)')]),
 (26,'Key points3 logarithm integrals','∫1/x=ln|x|+c and∫1/(ax+b)=ln|ax+b|/a+c,for a≠0and on each nonzero real component. Constants may differ on disconnected components.',[EXPINT],[('diff(log(x),x)','1/x'),('diff(log(-x),x)','1/x'),('diff(log(a*x+b)/a,x)','1/(a*x+b)')]),
 (27,'Key points4 trigonometric primitives','Cosine,sine and secant-square linear-argument primitives include1/a,and use radians. Retain original poles;do not integrate across them by a formal endpoint subtraction.',[TRIGINT],[('diff(sin(a*x+b)/a,x)','cos(a*x+b)'),('diff(-cos(a*x+b)/a,x)','sin(a*x+b)'),('diff(tan(a*x+b)/a,x)','sec(a*x+b)**2')]),
 (28,'Key points5 trapezium formula','For n equal strips,widthh=(b−a)/n,the estimate is h/2[y₀+2(y₁+…+yₙ₋₁)+yₙ]. Interior endpoints belong to two adjacent strips;outer endpoints belong to one.',[TRAPSET,TRAP],[('expand((a+b)/2+(b+c)/2)','a/2+b+c/2')])]:
 fig(n,155,label,note,teaches,'table',checks)
for n,label,note in [
 (29,'Figure5.8 left-end rectangles','Given increasing curve with left-height rectangles below it on the illustrated common grid. No numeric function is specified. It illustrates one case rather than all possible curves.'),
 (30,'Figure5.9 right-end rectangles','The same increasing curve with right-height rectangles above it. Its caption explicitly calls this a high estimate,in this case;the investigation’s universal under-estimate proposition is for the learner to test.'),
 (31,'Figure5.10 midpoint rectangles','The same source curve with midpoint-height rectangles. It visually motivates a candidate method but cannot prove that every function and every grid is more accurate than trapezia.')]:
 fig(n,156,label,note,[BIAS],'graph',parent='Problem-solving-investigation:1')
for frow in figures:frow['source_evidence']=ev(frow['pdf_page'])
pages=[]
for page in [155,156,157]:
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':ids,
  'continuation_item_ids':[row['item_id']]if page==157 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
  'non_item_content':{155:'All five formula/reference blocks enumerated. Learning outcomes are a checklist,not an extra task.',156:'Every investigation claim,specification question and all three teaching diagrams are linked to the complete investigation record.',157:'Investigation continuation covers reporting,information collection,processing/sketches,interpretation,desired method properties and other methods. No new independent task or figure;C6begins158.'}[page]})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-closing.json',{'scope':'Every guiding investigation subtask answered;author-derived,no printed key.','items':answers}),('census-Goldie-C5-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete155–157including investigation continuation and all teaching/reference figures.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for part in parts:
  for name,op in part.get('additional_operations',{}).items():assert equivalent(compute(op),expression(part['additional_operation_expected'][name])),name
 print('One complete investigation;',len(parts),'subtask dispositions;20experiment rows;',len(figures),'reference/given figures')
