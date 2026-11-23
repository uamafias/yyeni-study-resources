"""Every fixed-source question/subpart in YM Exercise 4.2, PDF 223–224."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
BASIC='8227:2020:M1:T6:O01:D01';INTERPRET='8227:2020:M1:T6:O02:D02';SKETCH='8227:2020:M1:T6:O02:D03'
PROOF='8227:2020:M1:T6:O05:D01';TRANS='8227:2020:M1:T6:O05:D02';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
ONE='8227:2020:M1:T3:O03:D01';EVAL='8227:2020:M2:T3:O02:D05';D='(x*pi/180)'
def ev(page):
    name='YM-key-614-615-full'if page==614 else'YM-C4-221'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,sketch=False,representation='text'):
    for p in parts:
        kp=p.pop('key_page_override',614);p.pop('source_page_override',None)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A28',key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:Exercise-4.2:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'Only requested results or required methods are assessed. A sketch root count does not ask for a numerical root estimate. Squared-ratio evaluation is not an identity proof. The independent solution method does not invent a separately assessed demand.',
      'representation':representation,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if n not in[5,8]else'not applicable',
        'quoted_value':note,'reason':'Actual bounded-equation argument multipliers are 1, 2, or the simple fraction 2/3; a graph-only cos3θ task is not an equation multiplier restriction.'},
       {'rule_id':'8227:LIMIT02','status':'outside'if n==3 else'within'if n not in[5,8]else'not applicable',
        'quoted_value':note,'reason':'Question 3(b) supplies neither interval nor angle unit; its finite key is conditional and does not answer an unbounded literal equation. A bounded adaptation would be a later planning proposal.'if n==3 else'The actual finite interval is retained wherever roots are requested; no general solution is introduced into a bounded task.'},
       {'rule_id':'8227:QUAL08','status':'within'if n==5 else'not applicable',
        'quoted_value':'g(x)=cosx, 0≤x≤k; largest k for an inverse'if n==5 else note,
        'reason':'The largest initial injective interval ends at the first turning point π.'if n==5 else'No inverse function is constructed; question 8 squared outputs do not assess principal-sign selection.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Exercise 4.2, with Basic/Intermediate/Advanced headings, before the separately labelled exam-style section. Difficulty labels alone do not establish examination style.',
      'precision_angle_check':{'source':'Degrees and radians are stated per question, except the missing interval/unit in 3(b). Decimal key values are compared at their written precision; exact π values remain exact.',
        'comparison':'Root-count tasks keep their graphical demand even when the author verifies algebraically. Q10 uses radian π axes; coordinate components are rounded independently.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if n==3:row['value_level_scope_decisions'][1]['part_ids']=['b']
    answers.append(row);return row

p=value('a','Tuple((3-(-1))/2,360/120,(3+(-1))/2)','Tuple(2,3,1)',614,
 'Read maximum 3, minimum −1, and positive period 120° from the given graph. The explicitly positive integers a,b,c remove the otherwise equivalent simultaneous sign reversal: a=2, b=3, c=1.')
p['assertions']=[{'expression':'2*sin(3*0*pi/180)+1','expected':'1'}]
p2=value('b','(180+asin(1/2)*180/pi)/3','70',614,
 'With 2sin3x+1=0, the first positive phase is 210°, so the first positive x is 70°. Enumerating all roots on the given interval independently confirms the minimum.')
p2['additional_operations']={'all_original_roots':{'kind':'bounded-trig-equation','operands':[f'2*sin(3*{D})+1','0','360']}}
p2['dependency']={'source_part':'a','role':'Use the graph-derived positive parameters in f(x)=0.'}
add(1,223,'Given f(x)=a sin(bx)+c on 0°≤x≤360°, maximum 3, minimum −1, period 120° and initially rising midline 1; a,b,c are positive integers. Find the parameters and the smallest positive zero.',[p,p2],[INTERPRET,BND],representation='graph')
# The actual n=3 belongs to a bounded equation derived from a graph. It is not
# silently described as n=1 or n=2; the syllabus permits small positive integers.
answers[-1]['value_level_scope_decisions'][0].update(quoted_value='2sin(3x)+1=0, 0°≤x≤360°; n=3',reason='The actual input multiplier is the small positive integer 3.')

p=graph('a:2sin','sin','2','1','0','0','pi','radian',614,
 {'sample_values':'Tuple(0,2,0)','window_range':'Interval(0,2)'},at=['0','pi/2','pi'])
p2=graph('a:cos2','cos','1','2','0','0','pi','radian',614,
 {'sample_values':'Tuple(1,-1,1)','window_range':'Interval(-1,1)'},at=['0','pi/2','pi'])
p3=reasoning('b','2 solutions',
 'The two given interval sketches cross twice. Independent completeness check: set s=sinθ on [0,π]; cos2θ=1−2s² gives 2s²+2s−1=0. Only s=(√3−1)/2 lies in [0,1], and it occurs once in each open half interval, giving exactly two intersections. Numerical roots are not requested.',614,'matches')
p3['additional_operations']={'exact_root_set':{'kind':'bounded-trig-equation','operands':['2*sin(x)-cos(2*x)','0','pi']}}
add(2,223,'Sketch 2sinθ and cos2θ on 0≤θ≤π; hence state how many solutions their equality has. Only the count, not numerical root estimates, is requested.',[p,p2,p3],[BASIC,SKETCH],True)

p=transform('a','3*cos(x)-2*sin(x)**2','2*cos(x)**2+3*cos(x)-2',[], 'all real x',614)
p2=reasoning('b','The literal task has no finite specified interval or angle unit. If one additionally imposes 0°≤x≤360°, its two roots are 60° and 300°; that condition is absent from the source stem.',
 'From (2cosx−1)(cosx+2)=0, only cosx=1/2 is admissible. The printed two angles are valid on a single degree cycle but omit infinitely many literal roots without a supplied interval. Internal diagnostic: degree solutions 60+360k and 300+360k, integer k (or the equivalent radian families). These general forms are outside the prescribed bounded demand, not candidate learner material. Preserve the missing-condition defect rather than supplying it silently.',614,'key incomplete')
p2['additional_operations']={'admissible_ratio_candidates':{'kind':'real-roots','operands':['2*x**2+3*x-2']},
 'conditional_one_cycle_only':{'kind':'bounded-trig-equation','operands':[f'3*cos({D})-2*sin({D})**2','0','360']}}
add(3,223,'(a) Show 3cosx=2sin²x reduces to 2cos²x+3cosx−2=0. (b) Hence solve the original equation: no interval or angle unit is stated, although the key silently gives one degree cycle.',[p,p2],[TRANS])
answers[-1]['source_interpretation']='Part (b) cannot establish complete bounded-equation coverage as printed. Retain only the explicit equation-transformation aspect; any bounded repair is a proposal for step 3.'

p=transform('a','4*sin(x)**4+5-7*cos(x)**2','4*sin(x)**4+7*sin(x)**2-2',[], 'all real x',614)
p2=roots('b','4*sin(x)**4+5-7*cos(x)**2','FiniteSet(pi/6,5*pi/6,7*pi/6,11*pi/6)',614,
 [('sin','x','1/2',1),('sin','x','-1/2',1)],unit='radian')
add(4,223,'Reduce 4sin⁴x+5=7cos²x to a quadratic in sin²x, then solve on 0≤x≤2π. Reject sin²x=−2; sin²x=1/4 gives all four exact radian roots.',[p,p2],[TRANS,BND,ALL])

p=graph('a:cos','cos','1','1','0','0','2*pi','radian',614,
 {'sample_values':'Tuple(1,-1,1)','window_range':'Interval(-1,1)'},at=['0','pi','2*pi'])
p2=graph('a:cos3','cos','1','3','0','0','2*pi','radian',614,
 {'sample_values':'Tuple(1,-1,1,-1,1,-1,1)','amplitude':'1','period':'2*pi/3'},
 at=['0','pi/3','2*pi/3','pi','4*pi/3','5*pi/3','2*pi'])
p2.update(question_formula_normalised='cos(3*x)',printed_key_formula_normalised='3*cos(x)',
 source_graph_comparison='The drawn high-frequency curve has amplitude 1 and three cycles, as cos3θ should. The rendered equation label incorrectly says 3cosθ; retain a label defect, not an incorrect curve-shape claim.')
p3=value('b','0','pi',614,
 'Cosine is strictly decreasing from 1 to −1 on [0,π]. Its first interior turning point to the right is π, so increasing k beyond π repeats nearby ordinates and prevents an inverse.')
p3['operation']={'kind':'first-turning-point-right','operands':['cos(x)','0','2*pi']}
add(5,223,'Sketch and label cosθ and cos3θ on 0≤θ≤2π; then find the largest k for which cosx restricted to [0,k] has an inverse. The key shape is right but its cos3θ label is printed as 3cosθ.',[p,p2,p3],[BASIC,SKETCH,ONE],True)

add(6,223,'Solve (a) 3tanx=2/cosx on −90°<x<90°; (b) tan(2y/3)+1=0 on 0°≤y≤360°. The actual second argument multiplier is the simple fraction 2/3.',[
 roots('a',f'3*tan({D})-2/cos({D})',['41.8'],614,[('sin','x','2/3',1)],lo='-90',hi='90',approx=True,opened=True),
 roots('b',f'tan(2*{D}/3)+1','FiniteSet(405/2)',614,[('tan','2*x/3','-1',1)])],[BND,ALL,TRANS])

left='(1+cos(x))/(1-cos(x))-(1-cos(x))/(1+cos(x))'
p=transform('a',left,'4/(sin(x)*tan(x))',['4*cos(x)/sin(x)**2'],
 'sin(x) != 0 and cos(x) != 0; this retains the domain of both original sides, including the defined tangent',614)
original=f'sin({D})*((1+cos({D}))/(1-cos({D}))-(1-cos({D}))/(1+cos({D})))-3'
p2=roots('b',original,['53.1','233.1'],614,[('tan','x','4/3',1)],approx=True,opened=True)
p2['dependency']={'source_part':'a','role':'Hence use the proved identity, while preserving the original equation denominator conditions.'}
add(7,224,'Prove the stated rational cosine identity, retaining its common domain; hence solve sinθ times that difference =3 on 0°<θ<360°. The original sine-zero poles cannot be solutions.',[p,p2],[PROOF,TRANS,BND,ALL])

p=value('a','1-(2/5)**2','21/25',614,
 'From x=asin(2/5), sinx=2/5. The identity cos²x=1−sin²x gives 21/25. Because the requested output is squared, no quadrant/sign decision is demonstrated.')
p2=value('b','(2/5)**2/(1-(2/5)**2)','4/21',614,
 'Divide the known sin²x by cos²x to get tan²x=4/21. This is exact identity evaluation, not a request to prove an identity.')
add(8,224,'Given x=asin(2/5), find cos²x and tan²x exactly. The squared answers do not assess principal-sign selection or a proof.',[p,p2],[EVAL])
answers[-1]['direct_demand_aspects']={EVAL:'Basic exact evaluation using sin²x+cos²x=1 and tan²x=sin²x/cos²x; this supports one elementary aspect of the broader Module 2 identity demand, not its full compound/double-angle breadth.'}

left='(sin(x)+cos(x))*(1-sin(x)*cos(x))'
p=transform('a',left,'sin(x)**3+cos(x)**3',
 ['sin(x)+cos(x)-sin(x)**2*cos(x)-sin(x)*cos(x)**2',
  'sin(x)*(1-cos(x)**2)+cos(x)*(1-sin(x)**2)'],'all real x',614)
p2=roots('b',f'(sin({D})+cos({D}))*(1-sin({D})*cos({D}))-9*sin({D})**3',
 ['26.6','206.6'],614,[('tan','x','1/2',1)],approx=True)
add(9,224,'Prove (sinx+cosx)(1−sinx cosx)=sin³x+cos³x; then solve the same left side =9sin³x on 0°≤x≤360°. The identity reduces this to cos³x=8sin³x.',[p,p2],[PROOF,TRANS,BND,ALL])

s='((sqrt(5)-1)/2)'
p=value('a',f'asin({s})','333/500',614,
 'At either intersection tanx=cosx, and cosx cannot vanish. Thus sinx=cos²x=1−sin²x. Of the two quadratic roots, only s=(√5−1)/2 is a sine value. The left point A is in (0,π/2), so xA=asin(s). Round to the key three significant figures only after deriving it.')
p['operation']={'kind':'rounded','operands':[f'asin({s})'],'significant_figures':3}
p['additional_operations']={'all_original_intersections':{'kind':'bounded-trig-equation','operands':['tan(x)-cos(x)','0','pi']}}
p2=value('b:x',f'pi-asin({s})','62/25',614,
 'The right point B is in (π/2,π), so xB=π−asin(s); round the derived value to three significant figures.')
p2['operation']={'kind':'rounded','operands':[f'pi-asin({s})'],'significant_figures':3};p2['source_assessed_part_id']='b'
p3=value('b:y',f'cos(pi-asin({s}))','-393/500',614,
 'Evaluate the original cosine at the right intersection, so yB is negative. Independently yB²=sinxB=s and yB=−√s. Round only at the end.')
p3['operation']={'kind':'rounded','operands':[f'cos(pi-asin({s}))'],'significant_figures':3};p3['source_assessed_part_id']='b'
p3['assertions']=[{'expression':f'cos(pi-asin({s}))+sqrt({s})','expected':'0'}]
add(10,224,'Given the tanx and cosx intersection diagram on 0≤x≤π, calculate the left intersection A x-coordinate and both coordinates of right intersection B. The tangent pole at π/2 is excluded.',[p,p2,p3],[INTERPRET,TRANS,BND,ALL],representation='graph')

left='(sin(x)-3*cos(x))**2+(3*sin(x)+cos(x))**2'
p=value('a',left,'10',614,
 'Expand the original two squares: cross terms cancel and the remaining 10(sin²θ+cos²θ) equals 10 for every θ. This establishes the requested invariant, not merely one numerical example.')
p['check_mode']='show/prove'
p2=roots('b',f'2*(sin({D})-3*cos({D}))-(3*sin({D})+cos({D}))',
 ['98.1','278.1'],614,[('tan','x','-7',1)],approx=True)
add(11,224,'For a=sinθ−3cosθ and b=3sinθ+cosθ on 0°≤θ≤360°, (a) show a²+b² is constant and find it; (b) solve 2a=b. Expansion gives invariant 10 and the equation sinθ+7cosθ=0.',[p,p2],[PROOF,TRANS,BND,ALL])

figures=[]
for n,page,label,note,parent in[
 (174,223,'Exercise 4.2 question 1 given sine graph','The graph has midline 1, maximum 3, minimum −1, period 120°, and rises initially. Positive integer a,b,c are explicit in the stem.','1'),
 (175,224,'Exercise 4.2 question 10 given intersections','On 0≤x≤π, tangent and cosine cross once on each side of the tangent pole π/2; A has positive y and B negative y. Axes use radian π.','10')]:
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'given-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':'8227:TB:YM:C4:Exercise-4.2:'+parent,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'teaches_8227_demand_ids':[INTERPRET],'representation':'graph','source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':note,
        'reason':'The actual equation arguments have n=3 for the sine parameter task and n=1 for tan/cos intersections; original intervals and poles are preserved.'}],
      'value_level_scope_review_status_r5':'author actual graph values read 2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Source graph interpretation, not official examination frequency or marking evidence.'},
      'mathematical_feature_review':{'status':'given graph read; original function roots and coordinate signs independently derived; independent acceptance pending',
        'method':'Read labelled scales/constraints; derive exact root sets and substitute in the source equations. Do not use the drawing as a numerical answer key.'}})
pages=[{'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'All 11 Basic/Intermediate/Advanced Exercise 4.2 questions and both given graphs enumerated. The separate exam-style section starts on PDF225.',
 'reader':'Codex author','date':'2026-11-18'}for page in[223,224]]
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-exercise-4-2.json',{'scope':'All 11 questions and every explicit response in Exercise 4.2, including source defects and no-interval restriction.','items':answers}),
      ('census-YM-C4-exercise-4-2.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF223–224; every formal exercise question and given mathematical graph.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
