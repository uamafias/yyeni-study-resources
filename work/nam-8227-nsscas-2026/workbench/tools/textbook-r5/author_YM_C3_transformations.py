"""YM128–133: all six transformation investigations and their source graph panels.

Source enrichment, not a newly claimed examination transformation taxonomy.
Software menu actions are recorded context, not assessed mathematics.
"""
import json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,ev,reasoning,fig,figures,compute,expression,equivalent
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
SKETCH='8227:2020:M1:T3:O05:D01'

def response(label,answer,method,kp,sketch=False,checks=None):
 p=reasoning(label,answer,method+' Mathematical features are author-derived from the stated rules and compared with the rendered book graph/summary; no official award table exists for this investigation.',kp,'sketch'if sketch else'matches')
 p.update(given_representation='text',response_format='sketch'if sketch else'explanation',assessed_8227_demand_ids=[SKETCH]if sketch else[],teaches_8227_demand_ids=[]if sketch else[SKETCH])
 if sketch:p.update(credited_features=[answer],feature_basis='author-derived; textbook inline graph is comparison evidence, not official awards')
 for name,expr,target in checks or[]:
  p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=target
 return p

def add(n,page,note,parts,continuation=None):
 r=prior.add('Investigation-transformations',n,page,note,parts,[SKETCH],continuation=continuation)
 r.update(sketch_response_required=True,exam_style=False,exam_style_basis='The book explicitly labels this graph-software investigation For Enrichment; no exam attribution. Not evidence of an official transformation command or mark tariff.')
 r['mapping_rationale']='Graph outputs directly practise sketching the specified simple functions on their natural domains. Explanations of transformation rules are supporting enrichment, not a separate prescribed transformation demand or proof of examination coverage. Menu selections, QR link and partner discussion logistics are not mathematical assessed outputs.'
 r['precision_angle_check']={'source':'Exact Cartesian graph relationships; no requested numerical rounding or angle measure.','comparison':'Keep natural real domains and transformed endpoints. Output scaling changes heights; input scaling changes horizontal coordinates reciprocally. A source software screenshot is not a learner response or verified marking capability.'}
 r['software_setup_context']='Opening a new Sketchpad file, selecting the arrow tool and entering functions are procedural setup, not additional mathematical responses. The QR/video link is a source lead only; it was not opened or used as evidence.'
 return r

add(1,128,'Plot x²,x²+2,x²−3 and sqrt(x),sqrt(x)+4,sqrt(x)−5; explain upward/downward output translations without changing their input domains.',[
 response('b-quadratic-plots','Three upward parabolas with vertices (0,0),(0,2),(0,−3), all domain R; the latter two translate the original vertically by +2/−3.','For each original x, only the output constant changes. Check vertex values at0 and the unchanged x coordinate of the vertex.',128,True,[('vertices','Tuple(0**2,0**2+2,0**2-3)','Tuple(0,2,-3)')]),
 response('c-root-plots','Three increasing root curves on x>=0 with endpoints (0,0),(0,4),(0,−5); images respectively y>=0,4,−5.','The radicand x is unchanged, so all natural domains stay [0,infinity). Add the constants to each original output.',128,True,[('endpoints','Tuple(sqrt(0),sqrt(0)+4,sqrt(0)-5)','Tuple(0,4,-5)')]),
 response('c-add-output','Adding a positive constant C translates the whole graph up by C; (u,v) becomes (u,v+C).','Input coordinates do not change; the same domain is retained and the image shifts by C.',132),
 response('c-subtract-output','Subtracting a positive constant C translates the graph down by C; (u,v) becomes (u,v−C).','A downward shift is not reflection or a change in the natural input domain.',132)])
add(2,129,'Plot horizontally translated quadratic and root graphs and explain why an additive input constant moves the graph in the opposite horizontal direction.',[
 response('b-quadratic-plots','Parabola vertices (0,0),(−3,0),(2,0) for x²,(x+3)²,(x−2)²; all domains R.','Find the input making each square zero. Curvature and vertical coordinates of corresponding points are unchanged.',129,True,[('zeros','Tuple((-3+3)**2,(2-2)**2)','Tuple(0,0)')]),
 response('b-observation','(x+3)² is the original shifted left3; (x−2)² is shifted right2.','An original input u is reproduced when the new input is u−C in f(x+C), so corresponding horizontal coordinates move by−C.',132),
 response('c-root-plots','sqrt(x),sqrt(x+4),sqrt(x−5) start at (0,0),(−4,0),(5,0), with domains [0,infinity),[−4,infinity),[5,infinity).','Solve each ORIGINAL radicand inequality and retain the included zero endpoint. The curves are horizontal translations, not vertical shifts.',129,True,[('endpoints','Tuple(sqrt(-4+4),sqrt(5-5))','Tuple(0,0)')]),
 response('c-add-input','For C>0, f(x+C) translates the graph left C and its natural domain by−C.','The original argument x+C must belong to the original domain; this is why the root endpoint moves left.',132),
 response('c-subtract-input','For C>0, f(x−C) translates the graph right C and its natural domain by+C.','Set new argument x−C=u to obtain new x=u+C, rather than reading the minus sign as a left shift.',132)])
add(3,129,'Compare y=x² with−x², sqrt(x) with−sqrt(x), and2^x with−2^x; explain reflection in the horizontal axis. The source result graph continues on130.',[
 response('b-quadratic-plots','x² opens upward and−x² downward, sharing vertex(0,0) and domain R; their images are nonnegative/nonpositive.','Negate each original output; x coordinates and the domain are unchanged.',130,True,[('sample','Tuple(2**2,-2**2)','Tuple(4,-4)')]),
 response('b-observation','Multiplying all outputs by−1 reflects the graph in the x-axis.','Every point(u,v) becomes(u,−v); points on the x-axis stay fixed.',133),
 response('c-root-plots','sqrt(x) and−sqrt(x) share endpoint(0,0) and domain x>=0; one is above and one below the x-axis.','The negative sign is OUTSIDE the root; it does not reverse the input domain.',130,True,[('sample','Tuple(sqrt(4),-sqrt(4))','Tuple(2,-2)')]),
 response('c-exponential-plots','2^x and−2^x have domain R, y-intercepts1/−1 and asymptote y=0; their images are strictly positive/negative.','Negating the exponential does not change its positive-base domain or make either graph attain0.',130,True,[('intercepts','Tuple(2**0,-2**0)','Tuple(1,-1)')]),
 response('c-negative-output','The transformation y=−f(x) is reflection in the x-axis, with the same domain.','Distinguish negating the whole output from replacing the input by−x.',133)],continuation=[130])
add(4,130,'Compare sqrt(x) with sqrt(−x), and2^x with2^(−x); explain reflection in the vertical axis and the root-domain reversal.',[
 response('b-root-plots','sqrt(x) lies on x>=0; sqrt(−x) lies on x<=0. Both start at(0,0), remain nonnegative and reflect in the y-axis.','The original radicand is−x for the second graph, so its permitted inputs are nonpositive.',130,True,[('symmetric-values','Tuple(sqrt(4),sqrt(-(-4)))','Tuple(2,2)')]),
 response('b-observation','Replacing the argument x by−x sends point(u,v) to(−u,v).','This is a horizontal reflection, preserving output sign and reversing the domain horizontally.',133),
 response('c-exponential-plots','2^x increases,2^(−x) decreases; both have domain R, image(0,infinity), y-intercept1 and mirror symmetry in the y-axis.','Compare opposite inputs and retain the nonattained y0 asymptote.',130,True,[('symmetric-values','Tuple(2**2,2**(-(-2)))','Tuple(4,4)')]),
 response('c-negative-input','f(−x) reflects the graph in the y-axis; it is distinct from−f(x).','Input sign reversal can change a natural domain, as for the root, even though both exponential domains remain R.',133)])
add(5,131,'Compare cubic x³−4x with output-scaled versions2(x³−4x) and(1/2)(x³−4x); explain vertical scale factors greater than1 and between0and1.',[
 response('b-double-output','All three base/doubled cubic roots are −2,0,2; doubling outputs doubles all turning heights and every y at the same x.','Expand the original scaled cubic and preserve its roots; domain and image are R. Larger positive output factors stretch vertically.',131,True,[('expanded','expand(2*(x**3-4*x))','2*x**3-8*x'),('zero-check','Tuple((-2)**3-4*(-2),0**3-4*0,2**3-4*2)','Tuple(0,0,0)')]),
 response('b-observation','For C>1, C f(x) stretches by factor C parallel to the y-axis.','Each point(u,v) becomes(u,Cv). Nonzero y distances multiply by C; x positions stay fixed.',133),
 response('c-half-output','The half-height cubic is x³/2−2x; roots stay−2,0,2 and all heights halve.','A positive output factor between0and1 compresses vertically; it does not widen the root locations.',131,True,[('expanded','expand(Rational(1,2)*(x**3-4*x))','x**3/2-2*x')]),
 response('c-observation','For 0<C<1, C f(x) compresses by factor C parallel to the y-axis.','The factor is C itself for output scaling, with domain unchanged.',133)])
add(6,131,'Compare cubic x³−4x with input-scaled versions f(2x) and f(x/2); explain reciprocal horizontal scales and changed zeros. The result graph is on132.',[
 response('b-double-input','f(2x)=8x³−8x has roots−1,0,1. The base roots−2,0,2 halve their horizontal positions; corresponding y values stay the same.','Substitute2x into EVERY x occurrence of the original cubic. The graph is compressed horizontally by1/2, not stretched by2.',132,True,[('expanded','expand((2*x)**3-4*(2*x))','8*x**3-8*x'),('roots','solveset((2*x)**3-4*(2*x),x,domain=S.Reals)','FiniteSet(-1,0,1)')]),
 response('b-observation','For C>1, f(Cx) compresses horizontally by factor1/C.','To reproduce original argument u, the new input is u/C. Both cubic domain and image are R.',133),
 response('c-half-input','f(x/2)=x³/8−2x has roots−4,0,4. Horizontal coordinates double; corresponding output values are unchanged.','Substitute x/2 consistently in both cubic and linear terms. A factor1/2 INSIDE produces horizontal stretch2.',132,True,[('expanded','expand((x/2)**3-4*(x/2))','x**3/8-2*x'),('roots','solveset((x/2)**3-4*(x/2),x,domain=S.Reals)','FiniteSet(-4,0,4)')]),
 response('c-observation','For 0<C<1, f(Cx) stretches horizontally by factor1/C.','Input and output scaling are distinct even though both source software panels draw cubic families.',133)],continuation=[132])

refs=[
 (48,128,'Investigation1 vertical-translation plot','The source panel overlays quadratic vertical shifts0,+2,−3 androot shifts0,+4,−5. Root domains stay nonnegative; shifted endpoints differ in output only. QR code is a resource lead, not a mathematical figure.',1),
 (49,129,'Investigation2 horizontal-translation plot','Quadratic vertices shift to−3and2;root endpoints shift to−4and5. The changed radicands change input domains, unlike output shifts.',2),
 (50,130,'Investigation3 negative-output plot','The six original/negative-output quadratic,root andexponential graphs reflect in the x-axis; the root domains remain nonnegative and exponential images never include0.',3),
 (51,130,'Investigation4 negative-input plot','Root and exponential pairs reflect in the y-axis. The root branch now lies on the negative input half-line, while both exponential curves keep real domains.',4),
 (52,131,'Investigation5 cubic output-scale plot','The factors1,2,1/2 multiply y values at unchanged x positions. The three roots−2,0,2 are shared by every curve; turning heights scale.',5),
 (53,132,'Investigation6 cubic input-scale plot','Input factors1,2,1/2 correspond to horizontal factors1,1/2,2; the roots become±2,±1,±4 respectively, with corresponding heights unchanged.',6),
 (54,132,'Vertical-translation summary row','The summary sends y=f(x) to f(x)+C, translating by vector(0,C); positive C goes up and negative C down. The plot illustrates x²+2 andx²−3.',None),
 (55,132,'Horizontal-translation summary row','The summary sends y=f(x) to f(x+C), translating by vector(−C,0); positive C goes left. Domains translate with the graph.',None),
 (56,133,'Negative-output reflection summary row','y=−f(x) reflects in the x-axis. The printed root pair has unchanged nonnegative input domain and opposite output signs.',None),
 (57,133,'Negative-input reflection summary row','y=f(−x) reflects in the y-axis. The printed root pair retains nonnegative output values and reverses its input-domain sign.',None),
 (58,133,'Positive output-scale summary row','For C>1 the vertical scaleC stretches; for0<C<1 it compresses. The source describes positive factors only; zero/negative factors need separate treatment, not silent extrapolation.',None),
 (59,133,'Positive input-scale summary row','For C>1 the horizontal scale1/C compresses; for0<C<1 it stretches. This summary assumes C>0; C0 is undefined as a reciprocal scale and negative C also reflects.',None)]
for n,page,label,note,parent in refs:
 fig(n,page,label,note,[SKETCH],'graph',[],f'Investigation-transformations:{parent}'if parent else None)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
pages=[]
for page in range(128,134):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:YM:C3:Investigation-transformations:3']if page==130 else['8227:TB:YM:C3:Investigation-transformations:6']if page==132 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'All six numbered mathematical investigations, every requested graph/explanation and the six combined plot panels/six summary rows are enumerated across128–133. GUI setup, repeated part-label(b) in131 and QR link are context, not extra assessed mathematics. No separate answer-section key is claimed: the inline result graphs and132–133 summaries are the cited keys.','scope_screen':'Specific graph sketches support the prescribed simple-function sketch demand. General transformation taxonomy/software operation remains textbook enrichment, with no claim that each rule is an official separately assessed8227demand.'})

if __name__=='__main__':
 for name,data in [('answers-YM-C3-transformations.json',{'scope':'Every mathematical output of investigations1–6,including all graphs and discussions.','items':answers}),('census-YM-C3-transformations.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete128–133 investigation/summary census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
