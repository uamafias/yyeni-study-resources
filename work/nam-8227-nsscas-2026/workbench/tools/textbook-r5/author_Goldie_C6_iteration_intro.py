"""Iteration investigation,all boxed prompts,worked sequences and new Activity6.2."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';SEQUENCE='8227:2020:M2:T6:O02:D01';FAIL='8227:2020:M2:T6:O02:D02';RELATE='8227:2020:M2:T6:O03:D01';REARRANGE='8227:2020:M2:T6:O03:D02';ITERATE='8227:2020:M2:T6:O04:D01';STOP='8227:2020:M2:T6:O04:D02'
def ev(page):
 name='Goldie-C6-166'if page<170 else'Goldie-C6-170'if page<347 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,teaches=None,new_kind=None):
 for p in parts:
  kp=p.pop('key_page_override',347);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 347),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[347,348])
 row={'item_id':f'8227:TB:Goldie:C6:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],'teaches_8227_demand_ids':teaches or[],
  'mapping_rationale':'Supplied iteration,its fixed-point relation,observed convergence/failure and accuracy are distinct decisions. Unprompted examples teach rather than count as extra assessed questions. Formal derivative convergence conditions are author explanations only,not required8227knowledge.',
  'representation':'text','sketch_response_required':False,'exam_style':False,'exam_style_basis':'Ordinary source investigation,prompt,activity or worked exposition.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT08','status':'within','quoted_value':note,'reason':'Interpret supplied sequences and understand possible failure;do not require a formal derivative convergence condition. The open-ended invention prompt has a separate out-of-scope disposition.'}],
  'precision_angle_check':{'source':'Cosine iteration explicitly uses radians. Printed finite decimal sequences keep full calculator values internally;ellipses are decimal prefixes. No inference of a guaranteed root bound from stabilising digits alone.',
   'comparison':'Compare explicit finite iterates at their written precision and verify true roots independently from original equations. Odd fifth roots use the real branch,including negative arguments.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row)
 if new_kind:new.append({'item_id':row['item_id'],'item_kind':new_kind,'exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],'teaches_8227_demand_ids':teaches or[],'representation':'text','source_evidence':ev(page),'learner_display':False})
 return row

def iterate(label,F,start,steps,key,page,dp=4,prefix=False):
 p=value(label,'0',key,page,'Apply the source formula repeatedly from its stated initial value using80-digit internal arithmetic;do not feed rounded displayed iterates back into the recurrence. x₁is the supplied start,so stepscounts actual formula applications.')
 raw={'kind':'supplied-source-iteration','operands':[F,str(start)],'steps':steps}
 p['operation']=({**raw,'rounding':{'decimal_places':dp}}if not prefix else{'kind':'decimal-prefix','operands':[str(compute(raw))],'decimal_places':dp})
 p['additional_operations']={'unrounded_supplied_iterate':raw}
 return p
p=reasoning('i','Starting0and repeatedly applying cosine in radians converges to0.739085…with alternating errors.',
 'After the first step,the sequence lies in[cos1,1]. Cosine reverses ordering there and has absolute derivative at mostsin1<1,which supplies an author justification of contraction. The learner’s required explanation can be qualitative from the decreasing graph. Independently solve cosx−x=0on[0,1].',347,'matches')
p['additional_operations']={'independent_root':{'kind':'bracketed-source-root','operands':['cos(x)-x','0','1'],'rounding':{'decimal_places':4}},'iterate_30':{'kind':'supplied-source-iteration','operands':['cos(x)','0'],'steps':30}}
p['additional_operation_expected']={'independent_root':'0.7391'}
p2=reasoning('ii','Every positive starting value under repeated square root converges to1;starts above1decrease and those below1increase.',
 'Afterksteps the value isa^(1/2^k). Its logarithm is(loga)/2^k→0,so the limit is1. Ifa=1the sequence is constant. The source explicitly says positive;0would instead remain0and negative real starts are undefined.',347,'matches')
p2['additional_operations']={'above_one_example':{'kind':'supplied-source-iteration','operands':['sqrt(x)','16'],'steps':2},'below_one_example':{'kind':'supplied-source-iteration','operands':['sqrt(x)','1/16'],'steps':2}}
p2['additional_operation_expected']={'above_one_example':'2','below_one_example':'1/2'}
p3=reasoning('iii','Repeated x↦√(1+x)from a positive start converges toφ=(1+√5)/2.',
 'The positive limit must satisfyL²−L−1=0andL≥0,selectingφrather than the negative quadratic root. Values aboveφdecrease while positive values belowφincrease,remaining on their side. A bounded monotone argument justifies the limit;formal derivative criteria are not required of the learner.',347,'matches')
p3['additional_operations']={'fixed_point_residual':{'kind':'identity','operands':['((1+sqrt(5))/2)**2-(1+sqrt(5))/2-1']}}
p3['additional_operation_expected']={'fixed_point_residual':'0'}
add('Investigation',1,166,'Run and explain three supplied calculator processes:cosine from0in radian mode,repeated square root from any positive value,and repeated√(1+x)from a positive value. Record special starts and preserve real-domain restrictions.',[p,p2,p3],[SEQUENCE,RELATE,ITERATE])
p=reasoning('relation','x²−x−2=0andx=x²−2have identical real solutions−1and2.',
 'Subtractxfrom both sides of the fixed-point equation to recover the original polynomial. The first graph hasx-axis roots−1,2;the second shows intersections ofy=xandy=x²−2at(−1,−1),(2,2). These are different coordinate representations of the same root values.',166,'matches')
p['additional_operations']={'relation_residual':{'kind':'identity','operands':['(x**2-2)-x-(x**2-x-2)']}}
p['additional_operation_expected']={'relation_residual':'0'}
row=add('Worked-illustration',4,166,'Unprompted quadratic example relates polynomial zeros to intersections withy=xafter rearrangement. Both Figure6.6panels have separate figure records.',[p],[],[RELATE,REARRANGE],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting fixed-point representation illustration'
parts=[iterate(f'x{j}','(x**5+3)/5',1,j-1,key,167)for j,key in enumerate(['1','0.8','0.6655','0.6261','0.6192','0.6182','0.6181','0.6180','0.6180'],1)]
row=add('Worked-illustration',5,167,'Unprompted quintic iterationxₙ₊₁=(xₙ⁵+3)/5fromx₁=1. Check all nine printed values,using full internal values before four-decimal display. The attracting middle root is exactly(√5−1)/2despite the earlier false impossibility claim.',parts,[],[RELATE,ITERATE,STOP],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting supplied-iteration worked sequence';corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[169]})
p=reasoning('family','For every nonzero realn,x=[x⁵+(n−5)x+3]/nis equivalent to the original quintic,and there are infinitely many distinct rearrangements.',
 'Multiply byn≠0and move all terms to one side to recoverx⁵−5x+3=0. Distinct positive integersnproduce distinct polynomial maps because their difference is a nonzero multiple of the original nonzero polynomial. The source also gives the real odd-fifth-root rearrangement;negative arguments require its real branch. Inventing an unbounded family is enrichment beyond interpreting a supplied rearrangement.',347,'matches')
p['additional_operations']={'general_relation':{'kind':'identity','operands':['(x**5+(n-5)*x+3)-n*x']}}
p['additional_operation_expected']={'general_relation':'x**5-5*x+3'}
row=add('Prompt',2,167,'Find further rearrangements ofx⁵−5x+3=0and decide how many exist. Give a proved infinite family with nonzerondenominator,rather than guessing a finite list.',[p],[])
row['scope_check']={'status':'out-of-scope','basis':'Open invention of arbitrary rearrangements is extension;8227requires relating a given formula or supplied rearrangement to its equation.','excluded_or_qualified_parts':['whole open-ended invention task']};row['evidence_role']='prerequisite/supporting open rearrangement extension;no direct8227coverage'
p=reasoning('certainty','The sign bracket[0.61,0.62]certifies a root there;the earlier finite list of iterates alone did not.',
 'For continuous f=x⁵−5x+3,f(0.61)>0andf(0.62)<0. This supplies an existence interval independently of apparent stabilisation. A separate graph/count argument identifies which root is being bracketed. Do not infer an error bound just from five printed iterates.',347,'matches')
p['additional_operations']={'exact_endpoint_signs':{'kind':'identity','operands':['Tuple(sign((x**5-5*x+3).subs(x,61/100)),sign((x**5-5*x+3).subs(x,62/100)))']}}
p['additional_operation_expected']={'exact_endpoint_signs':'Tuple(1,-1)'}
add('Prompt',3,169,'Explain why the new endpoint sign check now makes the root-location judgement certain,unlike the finite iteration values alone.',[p],[BRACKET,STOP])
parts=[iterate(f'x{j}','real_root(5*x-3,5)',1,j-1,key,169,prefix=True)for j,key in enumerate(['1','1.1486','1.2236','1.2554','1.2679','1.2727','1.2745','1.2752','1.2755','1.2756','1.2756','1.2756'],1)]
p=reasoning('negative-start','With the alternative real-fifth-root formula andx₁=0,the sequence tends to the negative root−1.6180…;from1it tends to the positive outer root1.2756….',
 'The source uses an odd real fifth root. A complex principal-power implementation is inappropriate for negative arguments. Verify the two reference roots independently in[−2,−1]and[1,2];a finite numerical sequence is additional evidence,not the proof of a universal basin boundary.',170,'matches')
p['additional_operations']={'negative_root':{'kind':'bracketed-source-root','operands':['x**5-5*x+3','-2','-1'],'rounding':{'decimal_places':4}},'positive_root':{'kind':'bracketed-source-root','operands':['x**5-5*x+3','1','2'],'rounding':{'decimal_places':4}}}
p['additional_operation_expected']={'negative_root':'-1.6180','positive_root':'1.2757'}
# The printed prose gives a prefix1.2756…,not a nearest4dp claim.
p['source_precision_note']='Positive root1.275682…has prefix1.2756but rounds to1.2757at4dp.';parts.append(p)
row=add('Worked-illustration',6,169,'Alternative quintic real-fifth-root iteration from1:check all twelve printed prefixes and the different attracting root. The continuation170discusses start0and the negative root.',parts,[],[RELATE,ITERATE,FAIL],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting alternative-iteration worked sequence';corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[170]})
p=reasoning('target','It solves the equation,but fails the task if a specified root or interval was required.',
 'A numerical method can converge successfully to a different root. The original target interval,initial value and rearrangement remain part of the problem. Report that distinction and choose a suitable start/rearrangement rather than calling every converged value the intended answer. The source key explicitly discusses appropriate starting points and rearrangements.',348,'matches')
add('Prompt',4,170,'If an iteration finds a root but not the requested root,is it a failure? Distinguish equation validity from satisfying the selected interval/target.',[p],[SEQUENCE,FAIL])
parts=[iterate(f'x{j}','(1-x*exp(x))/x','1/2',j-1,key,170,dp=2)for j,key in enumerate(['0.50','0.35','1.43','-3.46'],1)]
row=add('Worked-illustration',7,170,'The source rearrangesxe^x+x²−1=0asx=(1−xe^x)/xand starts at½. Check its first four rounded iterates;after becoming negative,the sequence cannot approach the positive root.',parts,[],[RELATE,ITERATE,FAIL],new_kind='worked-illustration');row['evidence_role']='prerequisite/supporting divergent-iteration illustration'
p=reasoning('curve-feature','Near the fixed point,the decreasing iteration curve is much steeper in magnitude than the liney=x,so the cobweb jumps expand rather than contract.',
 'Read the supplied cobweb asx₁→F(x₁)→F(F(x₁)). Author checkF′=−1/x²−e^xhas large negative magnitude near the positive fixed point. Formal derivative convergence conditions remain excluded knowledge;the learner need only interpret the supplied failure qualitatively. Once a term becomes negative,Fkeeps it negative,so it cannot converge to the requested positive root.',348,'matches')
p['additional_operations']={'iteration_curve_derivative':{'kind':'identity','operands':['diff((1-x*exp(x))/x,x)']}}
p['additional_operation_expected']={'iteration_curve_derivative':'-1/x**2-exp(x)'}
row=add('Prompt',5,170,'Use Figure6.10to identify the curve feature causing divergence of the supplied iteration. Preserve qualitative graph interpretation without turning it into a required formal convergence theorem.',[p],[FAIL])
row['scope_check']={'status':'in-scope-parts-only','basis':'Recognising that iteration can fail is prescribed;formal derivative convergence conditions in surrounding prose remain extension.','excluded_or_qualified_parts':['formal convergence-condition theorem not required']}
parts=[]
for label,start,conclusion in [('start-minus2',-2,'Diverges toward−∞.'),('start-minus1',-1,'Converges to(√5−1)/2≈0.618.'),('start-plus1',1,'Converges to(√5−1)/2≈0.618.'),('start-plus2',2,'Diverges toward+∞.')]:
 p=reasoning(label,conclusion,
  'For starts±2,the graph ofF=(x⁵+3)/5lies beyondy=xin the outward direction and there is no further fixed point on that tail. Starts−1and1enter[0,1],then[0.6,0.8],where graph steps approach the middle fixed point. The source key reports the same four cases. Author contraction arguments can justify them but are not added to the learner’s required knowledge.',348,'matches')
 p['additional_operations']={'first_three_applications':{'kind':'supplied-source-iteration','operands':['(x**5+3)/5',str(start)],'steps':3,'return_sequence':True}}
 parts.append(p)
row=add('Activity',2,171,'Try the supplied quintic iteration from each endpoint of[−2,−1]and[1,2],and explain the four outcomes using a sketch. This Activity6.2was absent from the previous item population.',parts,[ROOTG,SEQUENCE,FAIL,ITERATE],new_kind='activity');row['sketch_response_required']=True
row['source_interpretation']={'visual_requirement':'Explain all four outcomes by reference to a sketch of F=(x^5+3)/5, as the source explicitly asks. Figure6.7on167already supplies this curve; a correctly annotated fresh sketch or a clear reference to that supplied map can support the explanation.',
    'credited_features':['The map is increasing and meets y=x at approximately−1.618,.618,1.276.',
        'From−2 successive steps move further left;from2 they move further right, away from the requested outer fixed points.',
        'From−1 and1 the staircase approaches the middle fixed point.618, which is not either target interval root.'],
    'not_sufficient':'Four numerical outcome labels alone omit the source requested visual explanation.',
    'criterion_basis':'Author-derived from the supplied map and source activity, not an official award table.'}
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,page,label,note,rep,checks,parent in [
 (10,166,'Figure6.6 polynomial zeros','Graphx²−x−2has roots−1,2and vertex(½,−9/4). Root values arex-coordinates,not points on the fixed-point diagonal.','graph',[('(x**2-x-2).subs(x,1/2)','-9/4')],'Worked-illustration:4'),
 (11,166,'Figure6.6 fixed-point intersections','Graphsy=xandy=x²−2intersect at(−1,−1),(2,2). Lower parabola vertex is(0,−2),different from the upper polynomial graph.','graph',[('Tuple((x**2-2).subs(x,-1),(x**2-2).subs(x,2))','Tuple(-1,2)')],'Worked-illustration:4'),
 (12,167,'Figure6.7 quintic iteration map','F=(x⁵+3)/5andy=xintersect at the three original quintic roots. The map is increasing;its staircase for the middle root is not the decreasing generic cobweb shown later.','graph',[],'Worked-illustration:5'),
 (13,168,'Iteration-to-graph procedure table','Choosex₁,move vertically toF,then horizontally toy=xand repeat. These correspondences define the supplied graphical iteration procedure.','table',[],None),
 (14,168,'Figure6.8 staircase','A generic increasing iteration curve approaches its diagonal fixed point from one side. The picture illustrates convergence;it is not a proof for every possibleF.','graph',[],None),
 (15,168,'Figure6.9 cobweb','A different decreasing genericFproduces alternating values around its fixed point. It is not the increasing quintic map from Figure6.7. A finite oscillating picture alone does not prove all future brackets.','graph',[],None),
 (16,170,'Figure6.10 divergent cobweb','The given mapF=1/x−e^xisundefined at0. Its displayed initial terms½,0.35,1.43jump away from the positive fixed point;subsequent terms become negative.','graph',[],'Worked-illustration:7')]:
 fig(n,page,label,note,[RELATE,ITERATE,FAIL],rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C6:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C6:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(166,171):
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':6,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
  'non_item_content':'All investigation processes,boxed prompts,unprompted numerical sequences,procedure table and teaching graphs enumerated. Formal derivative convergence conditions are extension. Activity6.2on171awaits the combined6Bcensus.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C6-iteration-intro.json',{'scope':'Investigation,allfourboxedprompts,worked sequences,andnewActivity6.2complete.','items':answers}),('census-Goldie-C6-iteration-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':6,'source_path':SRC,'source_sha256':SHA,'scope':'Complete166–170;Activity6.2on171awaits6Bcensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;newActivity6.2')
