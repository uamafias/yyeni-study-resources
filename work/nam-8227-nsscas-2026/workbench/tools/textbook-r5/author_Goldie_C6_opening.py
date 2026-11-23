"""Full fixed-source C6 opening census and source QA, PDF158–163."""
import hashlib,json
from fractions import Fraction
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';STOP='8227:2020:M2:T6:O04:D02'
QUADRATIC='8227:2020:M1:T1:O01:D01';FACTOR='8227:2020:M2:T1:O04:D02'
def ev(page):
 name='Goldie-C6-158'if page<162 else'Goldie-C6-162'if page<347 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,teaches=None,new_kind=None):
 for p in parts:
  kp=p.pop('key_page_override',347)
  p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 347),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[347,348])
 row={'item_id':f'8227:TB:Goldie:C6:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'teaches_8227_demand_ids':teaches or[],
  'mapping_rationale':'Actual requested roots or sign brackets are assessed. Unprompted numerical tables and warning examples teach but do not add separately assessed source coverage. Decimal/bisection implementation details are supporting extension rather than a newly prescribed numerical algorithm.',
  'representation':'text','sketch_response_required':False,'exam_style':False,'exam_style_basis':'Unattributed boxed prompt,activity,example or teaching illustration.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT08','status':'not applicable','quoted_value':note,'reason':'No formal fixed-point convergence condition requested in this opening. Interval continuity and sign changes are distinct from a derivative convergence criterion.'}],
  'precision_angle_check':{'source':'Opening equations ask an accurate or approximate solution without a fixed decimal requirement. Printed graphs have rounded labels;worked sign-search tables display2decimal places.',
   'comparison':'Do not infer root accuracy from all displayed calculator digits. A bracket gives existence and an error interval;it does not establish uniqueness without a separate argument.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row)
 if new_kind:
  new.append({'item_id':row['item_id'],'item_kind':new_kind,'exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'teaches_8227_demand_ids':teaches or[],'representation':'text','source_evidence':ev(page),'learner_display':False})
 return row

def derived(label,expr,target,method):
 p=value(label,expr,target,None,method);p.pop('printed_key_normalised');p['author_check_target_normalised']=target;p['check_mode']='no key';return p
p=reasoning('context','Examples include refining a measurement estimate or adjusting a trial numerical solution using feedback.',
 'The opening asks for other situations analogous to successive golf attempts. These are possible author examples,not a printed model answer,and do not automatically assess a numerical-equation objective.',None,'no key')
p1=derived('i','FiniteSet(*solve(x**2-4*x+3,x))','FiniteSet(1,3)','Factor(x−1)(x−3)=0. Exact polynomial algebra is available;the prompt requires only a valid solution,not necessarily every root.')
p2=derived('ii','FiniteSet(*solve(x**2+10*x+8,x))','FiniteSet(-5-sqrt(17),-5+sqrt(17))','Complete the square or use the quadratic formula. The discriminant68is positive;both exact roots are shown for author QA,though one solution satisfies the prompt.')
p3=reasoning('iii-algebraic-claim','This quintic does admit algebraic solutions:its factorisation is(x²+x−1)(x³−x²+2x−3),so(−1±√5)/2are exact roots.',
 'Expand the proposed integer-coefficient factors and substitute both quadratic roots into the originalx⁵−5x+3. This directly contradicts the printed statement on159that this particular quintic cannot be solved algebraically. A general quintic has no general radical formula,but that fact does not apply to every particular quintic. The remaining cubic can be treated numerically within learner scope;no cubic radical formula is imposed.',159,'key wrong')
p3['additional_operations']={'factorisation_residual':{'kind':'identity','operands':['expand((x**2+x-1)*(x**3-x**2+2*x-3))-(x**5-5*x+3)']},'two_exact_roots':{'kind':'identity','operands':['Tuple((x**5-5*x+3).subs(x,(-1+sqrt(5))/2),(x**5-5*x+3).subs(x,(-1-sqrt(5))/2))']}}
p3['additional_operation_expected']={'factorisation_residual':'0','two_exact_roots':'Tuple(0,0)'}
p4=derived('iv','FiniteSet(*solve(x**3-x,x))','FiniteSet(-1,0,1)','Factorx(x−1)(x+1). Each root is exact;the full set is author breadth evidence,not an extra learner demand.')
p5=value('v','0','0.357',159,'Use the continuous differencee^x−4x on[0,1],with opposite endpoint signs. Independent bisection gives the lower root;round to the source graph label’s3significant figures. Other roots exist,so this does not claim uniqueness.')
p5['operation']={'kind':'bracketed-source-root','operands':['exp(x)-4*x','0','1'],'rounding':{'significant_figures':3}}
row=add('Prompt',1,158,'Suggest other iterative-approximation situations,then decide algebraic versus numerical methods and find a solution of five equations:x²−4x+3,x²+10x+8,x⁵−5x+3,x³−x,e^x−4x. The source’s blanket quintic claim is false;one valid solution per equation is sufficient.',[p,p1,p2,p3,p4,p5],[],[FACTOR],teaches=[ROOTG])
row['evidence_role']='prerequisite/supporting algebraic-versus-numerical method exploration; no prescribed method-specific coverage'
row['mapping_rationale']='Rendered158 asks which equations admit algebraic solutions and asks for an accurate or approximate solution. It does not require completing the square, a graphical root estimate or any particular numerical method. Those chosen author methods do not become directly assessed8227demands; the following159graphs supply teaching support only.'
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[159]})
p=reasoning('proof','There is at least one root ofe^x−x=x²+2between2and3.',
 'Letg=e^x−x²−x−2,continuous on[2,3]. g(2)=e²−8<0andg(3)=e³−14>0,so the intermediate-value argument gives a root. Equivalently compare the original LHSandRHSat both endpoints:the ordering reverses. Neither method by itself claims a unique root.',161,'show/prove')
p['additional_operations']={'endpoint_signs':{'kind':'identity','operands':['Tuple(sign(exp(2)-8),sign(exp(3)-14))']}}
p['additional_operation_expected']={'endpoint_signs':'Tuple(-1,1)'}
p['valid_alternative_methods']=['Compare original left/right side endpoint ordering.','Rearrange to a continuous difference and show its sign change.']
row=add('Example',1,160,'Showe^x−x=x²+2has a root between2and3. The worked source gives two valid endpoint-comparison methods,continued161;continuity is necessary in either interpretation.',[p],[BRACKET])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[161]})
# The decimal-step prompt is headingless and was missing from the earlier population.
parts=[]
for label,root,key in [('0.012','0.012','5'),('0.385','0.385','18'),('0.989','0.989','28')]:
 r=Fraction(root);left=Fraction(0);step=Fraction(1,10);evaluations=[]
 while left!=r:
  candidate=left+step;evaluations.append(str(candidate))
  if candidate>r:step/=10
  else:left=candidate
 assert len(evaluations)==int(key)
 p=value(label,str(sum(map(int,root.split('.')[1])))+'+2',key,347,'Under the source decimal-search convention,start0is known;count every positive trial,including the two overshoots at coarser decimal levels. Three-place targetabcwith nonzero final digit requiresa+b+c+2trials. The explicit generated trial list separately verifies that count for these three targets.')
 p['decimal_trial_points']=evaluations;p['source_interpretation']='Illustrates an isolated monotone crossing,with exact hits and no cached duplicate trials. Trailing-zero targets can terminate earlier;the generic digit formula is not extended to them.';parts.append(p)
row=add('Prompt',6,162,'How many decimal-search steps from0reach0.012,0.385and0.989? The search convention and counted trial lists are explicit. This headingless prompt was absent from the prior inventory.',parts,[],teaches=[BRACKET],new_kind='prompt')
row['evidence_role']='prerequisite/supporting decimal-search extension;no separately prescribed algorithm coverage'
p=reasoning('absolute-error-model','Afterkhalvings of an interval of length1,the midpoint error is at most2^(−k−1). For tolerance½×10^(−d),k≥ceil(dlog₂10):4,7,10for d=1,2,3.',
 'Each bisection divides width by2. Using the midpoint gives half that width as a worst-case absolute error bound. This answers an absolute-error interpretation. It is different from requiring every number in the bracket to round to the same d-decimal display. The source answer itself notes dependence on endpoints and gives examples where four rather than five steps suffice for one decimal.',347,'matches')
p['additional_operations']={'midpoint_step_counts':{'kind':'identity','operands':['Tuple(ceiling(log(10)/log(2)),ceiling(2*log(10)/log(2)),ceiling(3*log(10)/log(2)))']}}
p['additional_operation_expected']={'midpoint_step_counts':'Tuple(4,7,10)'}
p2=reasoning('rounded-display-model','No finite uniform step count alone guarantees that an arbitrary root’s entire bracket rounds to one d-decimal value;check the actual bracket relative to rounding boundaries.',
 'A bracket can remain arbitrarily close to or straddle a half-unit rounding boundary even when very narrow. The source describes this endpoint dependence,including[0.3125,0.375]being inconclusive at one decimal. For a particular root continue until the bracket lies in one rounding cell,or explicitly report a midpoint with its absolute error. Formal bisection step-count analysis is supporting enrichment,not a newly required8227algorithm.',347,'matches')
row=add('Activity',1,162,'Investigate bisection counts for1,2,3andndecimal accuracy from a unit interval. Separate absolute-error guarantees from identical rounding of bracket endpoints;no universal digit-count guarantee is inferred from interval width alone.',[p,p2],[])
row['evidence_role']='prerequisite/supporting bisection step-count investigation;no prescribed algorithm demand'
row['scope_check']={'status':'out-of-scope','basis':'The syllabus requires locating roots and supplied iteration,but not a formal bisection step-count algorithm. Retain the investigation internally as accuracy support.','excluded_or_qualified_parts':['whole formal step-count investigation']}
# Unprompted tables and failure warnings remain teaching evidence.
parts=[]
for label,points,keys,kp in [('tenths',[f'{j}/10'for j in range(8)],['3.00','2.50','2.00','1.50','1.01','0.53','0.08','-0.33'],161),('hundredths',['60/100','61/100','62/100'],['0.08','0.03','-0.01'],162)]:
 for j,(point,key)in enumerate(zip(points,keys)):
  p=value(f'{label}-{j}',f'(x**5-5*x+3).subs(x,{point})',key,kp,'Evaluate the original quintic exactly at this source grid node,then compare the printed2decimal-place table entry.')
  p['operation']={'kind':'rounded','operands':[f'(x**5-5*x+3).subs(x,{point})'],'decimal_places':2};parts.append(p)
p=reasoning('bracket-and-midpoint','The relevant root lies in[0.61,0.62];the midpoint0.615has absolute error at most0.005.',
 'The original polynomial is continuous;the endpoint signs are positive and negative. Every point in the bracket lies within half its width of the midpoint. The root’s one-decimal display is0.6;the midpoint’s three written decimals do not themselves mean three-decimal accuracy.',162,'matches');parts.append(p)
row=add('Worked-illustration',1,161,'Unprompted decimal search for the middle root ofx⁵−5x+3:all eight tenths and three hundredths table entries,sign bracket and midpoint/error interpretation. This is teaching support rather than another posed problem.',parts,[],teaches=[BRACKET,STOP],new_kind='worked-illustration')
row['evidence_role']='prerequisite/supporting decimal-search worked illustration';corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[162]})
parts=[]
for label,point,key,bracket in [('first','1/2','0.53',['1/2','1']),('second','3/4','-0.51',['1/2','3/4']),('third','5/8','-0.03',['1/2','5/8'])]:
 p=value(label,f'(x**5-5*x+3).subs(x,{point})',key,162,'Evaluate the true midpoint value without rounding the decision sign;retain the half interval where the continuous original function changes sign.')
 p['operation']={'kind':'rounded','operands':[f'(x**5-5*x+3).subs(x,{point})'],'decimal_places':2};p['resulting_bracket']=bracket;parts.append(p)
row=add('Worked-illustration',2,162,'Unprompted first three bisection trials for the quintic:½,¾,⅝and the resulting nested brackets. Signs are decided before rounded table display.',parts,[],teaches=[BRACKET],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting bisection worked illustration'
p=reasoning('touching-root','A tangent/even-multiplicity root need not change sign.',
 'For example(x−1)²has a root1but is positive on either side. Figure6.3shows an x-axis touch followed by a later crossing. A sign-change search can miss the touching root. The graph is illustrative,not enough information to recover its exact equation.',163,'matches')
p['additional_operations']={'touch_counterexample':{'kind':'identity','operands':['Tuple(((x-1)**2).subs(x,0),((x-1)**2).subs(x,1),((x-1)**2).subs(x,2))']}}
p['additional_operation_expected']={'touch_counterexample':'Tuple(1,0,1)'}
p2=reasoning('clustered-roots','The cubic has roots0.3,0.7,0.9;one sign bracket[0,1]does not prove there is only one root.',
 'Factor the originalx³−1.9x²+1.11x−0.189=(x−0.3)(x−0.7)(x−0.9). f(0)<0,f(1)>0andf(0.5)>0,so bisection can settle on the first root while missing the later pair. A separate graph/root-count argument is needed.',163,'matches')
p2['additional_operations']={'factorisation':{'kind':'identity','operands':['expand((x-3/10)*(x-7/10)*(x-9/10))-(x**3-19*x**2/10+111*x/100-189/1000)']},'signs':{'kind':'identity','operands':['Tuple(sign((x**3-19*x**2/10+111*x/100-189/1000).subs(x,0)),sign((x**3-19*x**2/10+111*x/100-189/1000).subs(x,1)),sign((x**3-19*x**2/10+111*x/100-189/1000).subs(x,1/2)))']}}
p2['additional_operation_expected']={'factorisation':'0','signs':'Tuple(-1,1,1)'}
p3=reasoning('discontinuity','1/(x−2.7)has no root;an apparent opposite-sign bracket across2.7violates continuity.',
 'The reciprocal numerator is1and never zero. At2.7the function is undefined,and its opposite one-sided infinities explain the sign reversal. Blind interval subdivision can converge to this pole. Never promote a pole to a root.',164,'matches')
p3['additional_operations']={'pole_limits':{'kind':'identity','operands':['Tuple(limit(1/(x-27/10),x,27/10,dir="-"),limit(1/(x-27/10),x,27/10,dir="+"))']}}
p3['additional_operation_expected']={'pole_limits':'Tuple(-oo,oo)'}
row=add('Worked-illustration',3,163,'Three unprompted sign-search failure warnings:an even/touching root,three close cubic roots,and the reciprocal discontinuity at2.7continued164. Graphs warn why sign change alone is neither a full root count nor a substitute for continuity.',[p,p2,p3],[],teaches=[ROOTG,BRACKET],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting sign-search warning illustrations';corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[164]})
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,page,label,note,rep,checks,parent in [
 (1,159,'Figure6.1 quintic graph','x⁵−5x+3has stationarypoints(−1,7),(1,−1),three real crossings,and no further real turning points. The graph is valid despite the surrounding false algebraic-solvability claim.','graph',[('Tuple((x**5-5*x+3).subs(x,-1),(x**5-5*x+3).subs(x,1))','Tuple(7,-1)')],'Prompt:1'),
 (2,159,'Figure6.1 exponential/line intersections','e^xand4xintersect twice,with rounded labels(0.357,1.43),(2.15,8.6). The displayed precision varies by coordinate;neither is an exact point identity.','graph',[],'Prompt:1'),
 (3,160,'Figure6.2 increasing crossing','A continuous increasing curve has opposite endpoint signs at the markedabracket. It supplies an existence argument,not numeric ordinates.','graph',[],'Example:1'),
 (4,160,'Figure6.2 decreasing crossing','A continuous decreasing curve has the opposite sign ordering but the same sign-change existence argument. Either endpoint ordering is valid.','graph',[],'Example:1'),
 (5,161,'Decimal tenths-search table','Original quintic evaluated from0to0.7at tenths;all eight2dpentries are separately recomputed.','table',[],'Worked-illustration:1'),
 (6,162,'Decimal hundredths-search table','Original quintic at0.60,0.61,0.62has printed values0.08,0.03,−0.01;do not infer the decision sign from rounded zero values on other instances.','table',[],'Worked-illustration:1'),
 (7,163,'Figure6.3 touching and crossing roots','An illustrative curve touches the axis at one root and crosses later. The exact function is not supplied;even multiplicity is the teaching feature.','graph',[],'Worked-illustration:3'),
 (8,163,'Figure6.4 three close cubic roots','Cubic crossings0.3,0.7,0.9and endpoint sign change[0,1];a search can find one and miss a pair.','graph',[],'Worked-illustration:3'),
 (9,164,'Figure6.5 discontinuity warning','y=1/(x−2.7)has vertical asymptote2.7,no root,and opposite signs on the two domain components.','graph',[],'Worked-illustration:3')]:
 fig(n,page,label,note,[ROOTG,BRACKET],rep,checks,parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C6:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C6:');f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(158,164):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 cont=[r['item_id']for r in corrections if page in r['continuation_pdf_pages']]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':6,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':cont,'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
  'non_item_content':'All posed prompts,activity,worked numerical tables and teaching warnings enumerated. Opening golf photo and quotation are decorative context,with no mathematical data to read. Page164warning continuation awaits combined6Acensus.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C6-opening.json',{'scope':'All opening tasks/tables/warnings,with author-derived answer absence and source algebraic error explicit.','items':answers}),('census-Goldie-C6-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':6,'source_path':SRC,'source_sha256':SHA,'scope':'Complete158–163;warning continuation164awaits6Acensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p.get('printed_key_normalised',p.get('author_check_target_normalised')))),(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;new headingless prompt6')
