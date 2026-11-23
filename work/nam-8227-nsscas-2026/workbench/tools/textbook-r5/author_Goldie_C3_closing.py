"""Goldie C3 closing census, investigation and mixed practice, PDF92–96."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
COMP='8227:2020:M2:T3:O02:D02';DOUBLE='8227:2020:M2:T3:O02:D03';RFORM='8227:2020:M2:T3:O02:D04'
PYTH='8227:2020:M2:T3:O02:D01';REC='8227:2020:M2:T3:O01:D01';PRINC='8227:2020:M1:T6:O04:D01'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';TRANS='8227:2020:M1:T6:O05:D02'
PROOF='8227:2020:M1:T6:O05:D01';D='(x*pi/180)'
def ev(page):
    name='Goldie-key-C3-341'if page in[341,342]else'Goldie-C3-90'if page<=93 else'Goldie-C3-boundary-94'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[]
def add(kind,n,note,parts,direct,components=None,new_item=False):
    for p in parts:
        kp=p.pop('key_page_override',342);p.pop('source_page_override',None)
        p.update(source_pdf_page=92,source_evidence=ev(92),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C3:{kind}:{n}','source_pdf_page':92,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Classify what is explicitly simplified,proved,solved or investigated. Algebraic intermediate steps do not automatically become additional assessed syllabus demands. The general current-sum investigation requires coefficient/R-form reasoning,not an unrequested physical-circuit technique.',
      'representation':'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if kind=='Exercise-3E'and n==4 else'not applicable',
        'quoted_value':note,'reason':'Seven original finite intervals; input multipliers1or2. Identity arguments3θ/4θ/6θare not periodic-equation asks.'if kind=='Exercise-3E'and n==4 else'No bounded-equation root set requested; coefficient/identity tasks are not governed by the multiplier limit on solving.'},
       {'rule_id':'8227:LIMIT02','status':'within'if kind=='Exercise-3E'and n==4 else'not applicable',
        'quoted_value':note,'reason':'Every requested root set is bounded; the next general-solutions section is separately excluded.'if kind=='Exercise-3E'and n==4 else'No general root formula is requested.'}],
      'exam_style':False,'exam_style_basis':'Unattributed mixed Exercise3E or investigation; no exam-style heading or examination attribution.',
      'precision_angle_check':{'source':'3E4has explicit per-part degree/radian intervals; exactπanswers for(iii),(v). The currents phase is unrestricted in the question; do not silently assume an acute phase.',
       'comparison':'Retain full internal accuracy and original common domains. Degree decimal keys are compared at written precision; NSSCAS conditions remain separately recorded.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'investigation','exercise':'Investigation','item_number':str(n),'pdf_page':92,'printed_page':78,
      'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'representation':'text','source_evidence':ev(92),
      'answer_key':{'available':True,'pdf_pages':[341],'printed_pages':[327],'locator':'Investigation(Page78),answerPDF341'},'learner_display':False})
    return row

p=transform('coefficient-expansion','a*sin(x)+b*sin(x+c)','(a+b*cos(c))*sin(x)+b*sin(c)*cos(x)',
 ['a*sin(x)+b*(sin(x)*cos(c)+cos(x)*sin(c))'],'All real x,c; a,b positive source amplitudes.',341)
p['check_mode']='matches'
p['author_answer_form']='P=a+b*cos(c),Q=b*sin(c),where x=2πft.'
p2=value('amplitude-formula','expand((a+b*cos(c))**2+(b*sin(c))**2)',
 'a**2+b**2+2*a*b*cos(c)',341,
 'Derive the squared norm of the coefficient pair independently. With positive source amplitudes,the resultant amplitude is its nonnegative square root,and lies between|a−b|and a+b.')
p2['additional_operations']={'same_phase_amplitude_squared':{'kind':'identity','operands':['(a+b*cos(0))**2+(b*sin(0))**2']},
 'opposite_phase_amplitude_squared':{'kind':'identity','operands':['(a+b*cos(pi))**2+(b*sin(pi))**2']}}
p3=reasoning('greater-amplitude-claim','The resultant need not have a greater amplitude. At a=b=1,c=π,it is identicallyzero; at a=2,b=1,c=π,it has amplitude1,smaller than the first constituent.',
 'R²=a²+b²+2abcosc. For positive a,b,cosc∈[−1,1]gives|a−b|≤R≤a+b. In particular cancellation is allowed by the unrestricted question. The printed sentence claiming a greater amplitude is therefore false without additional restrictions.',341,'key wrong')
p3['additional_operations']={'cancellation_function':{'kind':'identity','operands':['sin(x)+sin(x+pi)']},
 'smaller_nonzero_result':{'kind':'trig-identity-residual','operands':['2*sin(x)+sin(x+pi)','sin(x)']}}
p4=reasoning('phase-formula','For R>0,a correct phase satisfiescosε=P/R,sinε=Q/R,so choose a quadrant-aware atan2(Q,P),modulo2π. The printedatan(Q/P)alone loses quadrants and is undefined on the vertical axis.',
 'Takea=1,b=3,c=π:thenP=−2,Q=0andI=−2sinx. A positive-amplitude sine needsεπmodulo2π,butatan(Q/P)=0. Takea=1,b=2,c=2π/3:thenP=0,Q=√3andI=√3cosx,soεπ/2;Q/Pis undefined. IfR=0,no resultant phase is defined. These cases are all permitted by the source question.',341,'key wrong')
p4['additional_operations']={'negative_axis_phase':{'kind':'r-form-coefficients','operands':['1+3*cos(pi)','3*sin(pi)'],'target':'sin-plus','angle_unit':'radian'},
 'vertical_axis_phase':{'kind':'r-form-coefficients','operands':['1+2*cos(2*pi/3)','2*sin(2*pi/3)'],'target':'sin-plus','angle_unit':'radian'}}
p5=reasoning('frequency-and-phase-between','For nonzero resultant and f>0,the fundamental frequency remainsf. A phase-between claim requires compatible representatives and a stated phase-difference convention; zero resultant has no fundamental oscillation frequency or phase.',
 'Both terms reduce toPsin(2πft)+Qcos(2πft). If(P,Q)≠(0,0),this is a nonzero sinusoid with the same angular rate. If(P,Q)=(0,0),the function is zero and every shift is a period,so it has no positive fundamental period. For positive amplitudes and a phase difference in(−π,π),the positive vector sum lies between the two rays on that chosen shorter arc. The printed question sets no such representative convention; phase comparison as an ordered interval is incomplete at the opposite-ray/zero cases and modulo2π.',341,'key incomplete')
row=add('Investigation','Currents','Investigate the sum ofa*sin(2πft)andb*sin(2πft+c),samefrequencyfand unrestricted phase differencec. Expand coefficients,derive resultant amplitude/phase,and audit cancellation,quadrants and the key frequency/amplitude/phase claims. The power-line photograph supplies context only; no geometry is read from it.',
 [p,p2,p3,p4,p5],[COMP,RFORM],new_item=True)

parts=[]
for label,expr,key,domain in[
 ('i','2*sin(3*x)*cos(3*x)','sin(6*x)','All real x.'),
 ('ii','cos(3*x)**2-sin(3*x)**2','cos(6*x)','All real x.'),
 ('iii','cos(3*x)**2+sin(3*x)**2','1','All real x.'),
 ('iv','1-2*sin(x/2)**2','cos(x)','All real x.'),
 ('v','sin(x-a)*cos(a)+cos(x-a)*sin(a)','sin(x)','All real x,a.'),
 ('vi','3*sin(x)*cos(x)','3*sin(2*x)/2','All real x.'),
 ('vii','sin(2*x)/(2*sin(x))','cos(x)','Originalsinx≠0; simplification doesnot extend the original domain.'),
 ('viii','cos(2*x)-2*cos(x)**2','-1','All real x.')]:
    p=value(label,expr,key,342,'Simplify independently using addition,double-angle or Pythagorean identities; compare the separate printed result. Preserve any original denominator exclusion.')
    p['original_common_domain']=domain;parts.append(p)
add('Exercise-3E',1,'Simplify eight expressions:2sin3θcos3θ;cos²3θ−sin²3θ;their square sum;1−2sin²(θ/2);sin(θ−α)cosα+cos(θ−α)sinα;3sinθcosθ;sin2θ/(2sinθ);cos2θ−2cos²θ. The seventh retains sinθ≠0.',parts,[DOUBLE,COMP,PYTH])
parts=[]
for label,expr,key in[
 ('i','(cos(x)-sin(x))**2','1-sin(2*x)'),('ii','cos(x)**4-sin(x)**4','cos(2*x)'),('iii','2*cos(x)**2-3*sin(x)**2','(5*cos(2*x)-1)/2')]:
    p=value(label,expr,key,342,'Expand/factor independently,then use the stated double-angle target. Algebraically equal expanded forms are checked on all real angles.');parts.append(p)
add('Exercise-3E',2,'Express(cosx−sinx)²in terms ofsin2x;cos⁴x−sin⁴xin terms ofcos2x;and2cos²x−3sin²xin terms ofcos2x. Choose the identity to match the requested representation.',parts,[DOUBLE],[PYTH])
parts=[
 transform('i','(1-cos(2*x))/(1+cos(2*x))','tan(x)**2',['2*sin(x)**2/(2*cos(x)**2)'],'cosx≠0,on both original sides.',92),
 transform('ii','csc(2*x)+cot(2*x)','cot(x)',['(1+cos(2*x))/sin(2*x)','2*cos(x)**2/(2*sin(x)*cos(x))'],'sin2x≠0; this also excludes sinx=0 andcosx=0.',92),
 transform('iii','tan(4*x)','4*tan(x)*(1-tan(x)**2)/(1-6*tan(x)**2+tan(x)**4)',
 ['sin(4*x)/cos(4*x)','4*sin(x)*cos(x)*(cos(x)**2-sin(x)**2)/(cos(x)**4-6*sin(x)**2*cos(x)**2+sin(x)**4)'],
 'cosx≠0andcos4x≠0. Do not additionallyexclude cos2x=0:the finalidentity is defined atx=π/4and3π/4even though a tan2x intermediate would be undefined.',92)]
for p in parts:p.update(key_presence='Stated result in the source task; no separate proof in the chapter answer section',inspected_key_pdf_pages=[340,341,342],
 author_proof_basis='Every transformation is author-derived; the answer page jumps from3E2to3E4. A zero residual validates the stated result,not an official proof or marking sequence.')
add('Exercise-3E',3,'Prove(1−cos2θ)/(1+cos2θ)=tan²θ;csc2θ+cot2θ=cotθ;andtan4θ=4t(1−t²)/(1−6t²+t⁴),t=tanθ. Original common domains are retained; the last proof uses sine/cosine expansions to avoid an unnecessary tan2θpole.',parts,[PROOF,DOUBLE],[REC,PYTH])
parts=[
 roots('i',f'sin({D}+2*pi/9)-7/10',['4.4','95.6'],342,[('sin','x+40','7/10',1)],approx=True),
 roots('ii',f'3*cos({D})**2+5*sin({D})-1',['199.5','340.5'],342,[('sin','x','-1/3',1),('sin','x','2',1)],approx=True),
 roots('iii','2*cos(x-pi/6)-1','FiniteSet(-pi/6,pi/2)',342,[('cos','x-pi/6','1/2',1)],unit='radian',lo='-pi',hi='pi'),
 roots('iv',f'cos(pi/4-{D})-2*sin(pi/6+{D})',['-15.9','164.1'],342,[('tan','x','(1-sqrt(2)/2)/(sqrt(2)/2-sqrt(3))',1)],lo='-180',hi='180',approx=True),
 roots('v','cos(2*x)+3*sin(x)-2','FiniteSet(pi/6,pi/2,5*pi/6)',342,[('sin','x','1/2',1),('sin','x','1',1)],unit='radian'),
 roots('vi',f'cos({D})+3*sin({D})-2',['20.8','122.3'],342,[('sin','x+180*atan(1/3)/pi','2/sqrt(10)',1)],approx=True),
 roots('vii',f'tan({D})**2-3*tan({D})-4',['76.0','135'],342,[('tan','x','4',1),('tan','x','-1',1)],hi='180',approx=True)]
add('Exercise-3E',4,'Seven bounded mixed equations:sin(θ+40°)=0.7on0..360°;3cos²θ+5sinθ−1=0on0..360°;2cos(θ−π/6)=1on−π..π;cos(45°−θ)=2sin(30°+θ)on−180..180°;cos2θ+3sinθ=2on0..2π;cosθ+3sinθ=2on0..360°;tan²θ−3tanθ−4=0on0..180°. All intervals inclusive.',parts,[BND,ALL,TRANS],[COMP,DOUBLE,RFORM,PYTH])

figures=[]
def scalar(expr,key):return {'operation':{'kind':'identity','operands':[expr]},'source_normalised':key}
def ident(left,right,domain='Original common defined domain; no new points introduced by cancellation.'):
    return {'operation':{'kind':'trig-identity-residual','operands':[left,right]},'source_normalised':'0','original_common_domain':domain}
def fig(n,page,label,note,teaches,rep,checks,scope=None):
    result=[]
    for c in checks:
        got=compute(c['operation']);assert equivalent(got,expression(c['source_normalised'])),(label,str(got),c)
        result.append({**c,'derived':str(got),'comparison':'author exact check agrees; independent acceptance pending'})
    figures.append({'item_id':f'8227:TB:Goldie:C3:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
     'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,'source_evidence':ev(page),'learner_display':False,
     'scope_check':scope or{'status':'in-scope','basis':'Required formula/principal-value support; no general root-formula demand added.','excluded_or_qualified_parts':[],'qualifier_screen':[],'limits_considered':['8227:LIMIT02']},
     'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'outside'if page in[93,94]else'not applicable','applies_to':'General-root formulas only; principal/bounded branch features retained'if page in[93,94]else'formula support','quoted_value':note,
       'reason':'Only principal branch/one-cycle features retained; surrounding general-solution formulas remain outside8227.'if page in[93,94]else'Formula support,not an unbounded general solution.'}],
     'value_level_scope_review_status_r5':'author actual formulas/principal intervals read2026-11-18; independent check pending',
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
       'relation':'Textbook formula/principal-branch teaching support,not an assessed response or exam-frequency claim.'},
     'mathematical_feature_review':{'status':'author source mathematics/labels and explicit formula/feature checks; independent acceptance pending',
       'method':'Check exact analytic values,principal intervals,branch endpoints and common domains. Excluded general-root formulas are recorded separately and never become8227coverage.',
       'checks':result}})
fig(24,93,'Principal inverse-value interval panel','atan has output(−π/2,π/2);asin has output[−π/2,π/2];acos has output[0,π]. Principal values are unique in these ranges. Surrounding infinite root lists/general formulas are excluded underLIMIT02.',[PRINC],'table',
 [scalar('Tuple(atan(-1),atan(0),atan(1))','Tuple(-pi/4,0,pi/4)'),scalar('Tuple(asin(-1),asin(0),asin(1))','Tuple(-pi/2,0,pi/2)'),
  scalar('Tuple(acos(-1),acos(0),acos(1))','Tuple(pi,pi/2,0)'),scalar('Tuple(limit(atan(x),x,-oo),limit(atan(x),x,oo))','Tuple(-pi/2,pi/2)')])
fig(25,93,'Figure3.14 tangent/principal-value branch','Tangent poles at±π/2bound the principal increasing branch;the markedatan(c)lies inside it. Repeated roots outside that branch illustrate an excluded general-solution topic,not a new required8227demand.',[PRINC],'graph',
 [scalar('tan(atan(x))','x'),scalar('Tuple(cos(-pi/2),cos(pi/2))','Tuple(0,0)')])
fig(26,94,'Figure3.15 cosine/principal-value branch','Cosine is even;the marked positiveacos(c)is the principalvalue in[0,π],with its negative reflection also on the fullgraph. Periodic/general root formulas above the graph are excluded.',[PRINC],'graph',
 [scalar('cos(acos(x))','x'),scalar('Tuple(cos(0),cos(pi))','Tuple(1,-1)'),ident('cos(-x)','cos(x)')])
fig(27,94,'Figure3.16 sine/principal-value branch','The markedasin(c)lies in[−π/2,π/2];π−asin(c)is the reflected first-cycle branch. All unbounded general-root formulas andActivity3.3are excluded; principal branch and finite-cycle reading are retained.',[PRINC,BND,ALL],'graph',
 [scalar('sin(asin(x))','x'),ident('sin(pi-x)','sin(x)'),scalar('Tuple(sin(-pi/2),sin(pi/2))','Tuple(-1,1)')])
fig(28,95,'Key points1 reciprocal definitions','secθ=1/cosθ,cscθ=1/sinθ,cotθ=1/tanθas written; original denominator exclusions remain. In particular the last writtenquotient requires bothsinθandcosθnonzero.',[REC],'table',
 [ident('sec(x)','1/cos(x)'),ident('csc(x)','1/sin(x)'),ident('cot(x)','1/tan(x)')])
fig(29,95,'Key points2 Pythagorean reciprocal identities','tan²θ+1=sec²θand1+cot²θ=csc²θon their original defined domains.',[PYTH],'table',
 [ident('tan(x)**2+1','sec(x)**2'),ident('1+cot(x)**2','csc(x)**2')])
fig(30,95,'Key points3 compound-angle formula table','Six sine/cosine/tangent sum/difference identities. The printed tangent note excludes a sum/difference of90°/270°etc; each originaltanθ/tanφmust also be defined. No additional assessment is invented.',[COMP],'table',
 [ident('sin(x+a)','sin(x)*cos(a)+cos(x)*sin(a)'),ident('sin(x-a)','sin(x)*cos(a)-cos(x)*sin(a)'),
  ident('cos(x+a)','cos(x)*cos(a)-sin(x)*sin(a)'),ident('cos(x-a)','cos(x)*cos(a)+sin(x)*sin(a)'),
  ident('tan(x+a)','(tan(x)+tan(a))/(1-tan(x)*tan(a))'),ident('tan(x-a)','(tan(x)-tan(a))/(1+tan(x)*tan(a))')])
fig(31,95,'Key points4 double-angle and power-reduction table','sin2θ,threecos2θforms,tan2θ,andtwo square-reduction formulas. The tangent formula needs the originaltanθandtan2θdefined; source lists45°/135°etc as denominator-zero cases.',[DOUBLE],'table',
 [ident('sin(2*x)','2*sin(x)*cos(x)'),ident('cos(2*x)','cos(x)**2-sin(x)**2'),ident('cos(2*x)','1-2*sin(x)**2'),
  ident('cos(2*x)','2*cos(x)**2-1'),ident('tan(2*x)','2*tan(x)/(1-tan(x)**2)'),
  ident('sin(x)**2','(1-cos(2*x))/2'),ident('cos(x)**2','(1+cos(2*x))/2')])
fig(32,95,'Key points5 R-form summary','Four sine/cosine R-forms use r=√(a²+b²),cosα=a/r,sinα=b/r. Interpret coefficient signs according to the chosen target; nonzero pair needed for the displayed phase equations. Zero-vector/phase-endpoint caveats are linked to the earlier generalisation defect.',[RFORM],'table',
 [ident('sqrt(a**2+b**2)*sin(x+atan2(b,a))','a*sin(x)+b*cos(x)'),
  ident('sqrt(a**2+b**2)*sin(x-atan2(b,a))','a*sin(x)-b*cos(x)'),
  ident('sqrt(a**2+b**2)*cos(x-atan2(b,a))','a*cos(x)+b*sin(x)'),
  ident('sqrt(a**2+b**2)*cos(x+atan2(b,a))','a*cos(x)-b*sin(x)')])
excluded={'item_id':'8227:TB:Goldie:C3:Activity:3','item_kind':'activity','exercise':'Activity','item_number':'3','pdf_page':94,'printed_page':80,
 'notes':'Activity3.3asks to prove the unbounded general sine solutionθ=nπ+(−1)^n*asin(c),ninteger. Explicitly outside8227LIMIT02; retain the source occurrence to prove the census didnot omit it.',
 'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[],'representation':'text','source_evidence':ev(94),
 'evidence_role':'excluded source occurrence; no8227assessed or teaching coverage','disposition':'exclude:general trigonometric solutions outside8227LIMIT02','learner_display':False,
 'scope_check':{'status':'out-of-scope','basis':'8227:LIMIT02excludes general trigonometric solution formulas; this is the entire task.','excluded_or_qualified_parts':['whole activity'],'qualifier_screen':[],'limits_considered':['8227:LIMIT02']},
 'answer_key':{'available':False,'pdf_pages':[],'printed_pages':[],'locator':'Excluded source task; no8227answer-accuracy claim.'},
 'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'outside','applies_to':'whole item','quoted_value':'θ=nπ+(−1)^n*asin(c),n∈Z','reason':'Unbounded general solution rather than a finite interval.'}],
 'value_level_scope_review_status_r5':'author actual general-form exclusion checked2026-11-18; independent acceptance pending'}
new.append(excluded)
pages=[]
for page in range(92,97):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]+([excluded['item_id']]if page==94 else[])
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated'if ids else'prose only',
     'item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),
     'excluded_source_elements':({'93':['Infinite example root lists andθ=atan(c)+nπgeneralformula'],
        '94':['Cosine and sine general-root formulas','Activity3.3whole task']} .get(str(page),[])),
     'non_item_content':{92:'Currents photograph is decorative/contextual; no metric data. All investigation and3Equestions recorded.',
      93:'Principal interval panel/tangent graph retained; infinite root lists andgeneral formula excluded.',
      94:'Both plots retained only for principal/bounded branch reading. General formulas andActivity3.3excluded.',
      95:'Five in-scope formula reference blocks,despite general-solutions margin label. No separately posed problem.',
      96:'Learning-outcome bullet list only; no new question,example,table or mathematical teaching figure. C4starts97.'}[page],
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C3-closing.json',{'scope':'Currents investigation and every3EsubpartPDF92; sourcekeys341–342andquestion-statedproofs.','items':answers}),
     ('census-Goldie-C3-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
      'scope':'Every mathematical source elementPDF92–96; explicit exclusion/general-branch screening retained.','new_items':new+figures,
      'corrections':[{'item_id':excluded['item_id'],'answer_accuracy_status_r5':'Excluded whole task:general-root proof outside8227; no in-scope answer accuracy claim.','design_use_status':'excluded from8227design underLIMIT02'}],
      'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'response items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;',sum(len(r['mathematical_feature_review']['checks'])for r in figures),'formula/feature checks;1excluded activity')
