"""Source QA for every parametric Exercise 4E subpart, Goldie PDF 130–132.
This checks fixed textbook questions; it generates no learner questions.
"""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PARAM='8227:2020:M2:T4:O03:D02';GEOM='8227:2020:M2:T4:O03:D03'
POWER='8227:2020:M1:T8:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02'
STATIONARY='8227:2020:M1:T8:O04:D01';LOGDEF='8227:2020:M2:T2:O02:D01';DOUBLE='8227:2020:M2:T3:O02:D03'
COORD='8227:PRIOR:NSSCO:coordinate-geometry';SIMULT='8227:PRIOR:NSSCO:simultaneous-equations'
ATTR={9:'9709 Paper 21 Q7 November 2011',10:'9709 Paper 31 Q4 November 2013',11:'9709 Paper 2 Q3 June 2007',12:'9709 Paper 2 Q4 June 2009',13:'9709 Paper 22 Q4 November 2009',14:'9709 Paper 2 Q3 June 2006',15:'9709 Paper 3 Q6 June 2009'}
def ev(page):
    name='Goldie-key-C3-341' if page==344 else 'Goldie-key-C4-C5-345' if page==345 else 'Goldie-C4-130'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None):
    for p in parts:
        kp=p.pop('key_page_override',345)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Exercise-4E:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or [],
      'mapping_rationale':'Record the requested parametric derivative, line or geometric conclusion as direct. Intermediate elementary differentiation, identities and simultaneous equations are components unless explicitly requested. Unbounded trig solutions in 4E8(iii) are excluded rather than silently adapted.',
      'representation':'graph' if n==7 else 'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Derivatives and geometric identities are not finite trig-equation tasks. The general-root ask in 8(iii) has its separate LIMIT02 exclusion.'},
       {'rule_id':'8227:QUAL10','status':'within' if n in [1,3,4,5,7,9,11,15] else 'not applicable','quoted_value':note,
        'reason':'Actual polynomial/reciprocal powers are integers; retain the original parameter and regularity domains.' if n in [1,3,4,5,7,9,11,15] else 'Exponential/trigonometric parameter, not a constant rational-power boundary.'}],
      'exam_style':n in ATTR,'exam_style_basis':('Printed attribution: '+ATTR[n]+'. Internal source lead; original examination not newly verified here.') if n in ATTR else 'Unattributed ordinary exercise; a PS icon alone does not establish examination provenance.',
      'precision_angle_check':{'source':'Radian trigonometric parameters. Exact forms except the written four-decimal base angle in 8(iii). No general NSSCAS rounding rule is imposed on the source key.',
       'comparison':'Preserve original excluded parameters before cancellation, allow implicit vertical line forms, and distinguish signed intercept products from unsigned areas.'},
      'expected_subpart_labels':[p['subpart'] for p in parts],'subparts':parts}
    answers.append(row);return row

def pv(label,kind,X,Y,key,kp=345,at=None,proof=False):
    p=value(label,'0',key,kp,'Differentiate the original coordinate functions independently. Use Y′/X′ only on a regular finite-slope branch; line coefficients come from the tangent vector and original point. Compare with a separately transcribed key after any stated nonzero rescaling.')
    p['operation']={'kind':kind,'variable':'t','operands':[X,Y]}
    if at is not None:p['operation']['at']=at
    if proof:p['check_mode']='show/prove'
    return p
parts=[]
for label,X,Y,key,domain in [
 ('i','3*t**2','2*t**3','t','Finite ratio requires t≠0. At t=0 the parametrisation is singular; the horizontal limiting tangent needs separate analysis.'),
 ('ii','t-cos(t)','t+sin(t)','(1+cos(t))/(1+sin(t))','Radian parameter; 1+sin(t)≠0 for the ratio.'),
 ('iii','t+1/t','t-1/t','(t**2+1)/(t**2-1)','Original t≠0; finite ratio also excludes t=±1.'),
 ('iv','3*cos(t)','2*sin(t)','-2*cot(t)/3','Radian parameter; finite ratio requires sin(t)≠0.'),
 ('v','(t+1)**2','(t-1)**2','(t-1)/(t+1)','Finite ratio requires t≠−1; the tangent vector is nonzero at that vertical-tangent point.'),
 ('vi','t*sin(t)+cos(t)','t*cos(t)-sin(t)','-tan(t)','Original ratio requires t≠0 and cos(t)≠0. Cancellation does not prove regularity at the singular parameter 0.'),
 ('vii','exp(2*t)+1','exp(t)','1/(2*exp(t))','All real t; X′=2exp(2t)>0.'),
 ('viii','t/(1+t)','1/(1-t)','(1+t)**2/(1-t)**2','Original t≠−1,1. The simplified ratio does not restore t=−1.')]:
    p=pv(label,'parametric-derivative',X,Y,key,344);p['original_common_domain']=domain;parts.append(p)
add(1,130,'Eight derivative drills: (3t²,2t³), (θ−cosθ,θ+sinθ), (t+1/t,t−1/t), (3cosθ,2sinθ), ((t+1)²,(t−1)²), (θsinθ+cosθ,θcosθ−sinθ), (e^(2t)+1,e^t), and (t/(1+t),1/(1−t)). Cancel only after recording the original domains.',parts,[PARAM],[POWER,ELEMENTARY,COMPOSITE])
X='tan(t)';Y='tan(2*t)'
p=pv('i','parametric-derivative',X,Y,'6',344,'pi/6')
p2=pv('ii','parametric-tangent',X,Y,'Tuple(8,-4/3,-4*sqrt(3)/3)',344,'pi/6')
p2['normalisation_note']='Raw coefficients are (4/3) times the printed 6x−y−√3=0.'
p3=pv('iii','parametric-normal',X,Y,'Tuple(4/3,8,-76*sqrt(3)/9)',344,'pi/6')
p3['normalisation_note']='Raw coefficients are (4/9) times the printed 3x+18y−19√3=0.'
add(2,130,'For x=tanθ,y=tan2θ, evaluate the gradient and tangent/normal at θ=π/6. The original cosθ and cos2θ denominators are nonzero at the requested point.',[p,p2,p3],[PARAM,GEOM],[ELEMENTARY])
X='t**2';Y='1-1/(2*t)'
add(3,130,'For x=t²,y=1−1/(2t), t>0, find its x-axis crossing, gradient there, tangent and tangent y-intercept. The last point belongs to the extended tangent, not the positive-x curve.',[
 value('i','Tuple((solve(1-1/(2*t),t)[0])**2,0)','Tuple(1/4,0)',344),
 pv('ii','parametric-derivative',X,Y,'2',344,'1/2'),
 pv('iii','parametric-tangent',X,Y,'Tuple(2,-1,-1/2)',344,'1/2'),
 value('iv','Tuple(0,(2*x-1/2).subs(x,0))','Tuple(0,-1/2)',344)],[PARAM,GEOM],[COORD])
X='a*t**2';Y='2*a*t'
p=pv('i','parametric-tangent',X,Y,'Tuple(2*a,-2*a*t,2*a**2*t**2)');p['normalisation_note']='Divide by 2a≠0 to obtain the printed x−ty+at²=0.'
p2=pv('ii','parametric-normal',X,Y,'Tuple(2*a*t,2*a,-2*a**2*t**3-4*a**2*t)');p2['normalisation_note']='Divide by 2a≠0 to obtain tx+y=at³+2at.'
p3=value('iii','Tuple(Tuple(solve(t*x-(a*t**3+2*a*t),x)[0],0),Tuple(0,a*t**3+2*a*t))','Tuple(Tuple(a*t**2+2*a,0),Tuple(0,a*t**3+2*a*t))',345,'Derive the normal independently and intersect it with each axis. Unique x-axis intersection requires t≠0 in addition to a≠0; at t=0 the normal is the x-axis itself.')
row=add(4,130,'For x=at²,y=2at, a merely stated constant, find the general tangent, normal and the normal axis-intercepts. Nondegenerate curve requires a≠0; unique intercepts in (iii) also require t≠0. The source omits these qualifications.',[p,p2,p3],[PARAM,GEOM],[COORD])
row['source_interpretation']={'parameter_domains':{'a':'real, nonzero for the intended nondegenerate parabola','t':'real; t≠0 for two unique normal axis-intercepts'},'source_omission':'a=0 collapses the curve. At t=0 the normal y=0 coincides with an axis, so its x-axis intercept is not unique.'}
X='cos(t)';Y='cos(2*t)'
p=pv('i','parametric-derivative',X,Y,'4*cos(t)',130,proof=True)
p2=value('ii','diff(4*x,x)-4','0',130,'The requested intermediate rewrite is dy/dx=4x, using x=cosθ. Differentiating with respect to x gives d²y/dx²=4. This is not differentiation with respect to θ alone.');p2['check_mode']='show/prove'
p2['additional_operations']={'cartesian_elimination':{'kind':'trig-identity-residual','operands':['cos(2*t)','2*cos(t)**2-1']}}
p2['additional_operation_expected']={'cartesian_elimination':'0'}
row=add(5,130,'For x=cosθ,y=cos2θ, show dy/dx=4cosθ and, by rewriting it in terms of x, show d²y/dx²−4=0. Ratio derivation initially uses sinθ≠0; Cartesian y=2x²−1 explains the curve.',[p,p2],[PARAM],[DOUBLE,POWER])
X='a*t';Y='b/t'
p=pv('i','parametric-derivative',X,Y,'-b/(a*t**2)')
p2=pv('ii','parametric-tangent',X,Y,'Tuple(-b/t**2,-a,2*a*b/t)');p2['normalisation_note']='Multiply by −t²≠0 to obtain bx+at²y−2abt=0.'
p3=value('iii','Tuple(Tuple(solve((-b/t**2)*x+2*a*b/t,x)[0],0),Tuple(0,solve(-a*y+2*a*b/t,y)[0]))','Tuple(Tuple(2*a*t,0),Tuple(0,2*b/t))',345)
p4=reasoning('iv','Unsigned area is 2|ab|, independent of t. The printed 2ab requires ab>0 for a nondegenerate triangle.',
 'The intercepts are (2at,0) and (0,2b/t), so area=½|(2at)(2b/t)|=2|ab|. With a=1,b=−1,t=1 the triangle has positive area 2, whereas the printed expression is −2. Require a,b,t≠0 for the intended hyperbola and unique intercepts. Constancy is valid; the unrestricted signed key is not.',345,'key wrong')
p4['additional_operations']={'unsigned_area':{'kind':'identity','operands':['Abs((2*a*t)*(2*b/t))/2']},'negative_product_counterexample':{'kind':'identity','operands':['Tuple((Abs((2*a*t)*(2*b/t))/2).subs({a:1,b:-1,t:1}),(2*a*b).subs({a:1,b:-1}))']}}
p4['additional_operation_expected']={'unsigned_area':'2*Abs(a*b)','negative_product_counterexample':'Tuple(2,-2)'}
row=add(6,130,'For x=at,y=b/t, with unspecified constants a,b, derive gradient, tangent, both axis-intercepts and constant triangle area. Nonzero a,b,t are needed; unsigned area is 2|ab|. The printed 2ab silently assumes a positive product.',[p,p2,p3,p4],[PARAM,GEOM],[COORD])
row['source_interpretation']={'parameter_domains':{'a':'real, nonzero','b':'real, nonzero','t':'real, nonzero'},'unsigned_area':'2|ab|; unqualified 2ab is invalid for ab<0.'}
row['direct_demand_aspects']=[{'demand_id':GEOM,'assessed_facet':'Parametric tangent and its geometric intercept consequences; triangle area itself is prior mensuration, not calculus optimisation.'}]
X='4*t';Y='2*t**2'
p=pv('i','parametric-derivative',X,Y,'t',131,proof=True)
p2=pv('ii','parametric-tangent',X,Y,'Tuple(4*t,-4,-8*t**2)');p2['normalisation_note']='Divide by 4 to obtain tx−y−2t²=0.'
p3=reasoning('iii','S=(2(t₁+t₂),2t₁t₂), for distinct t₁,t₂.',
 'Subtract y=t₁x−2t₁² and y=t₂x−2t₂², then divide by t₁−t₂≠0. This gives x=2(t₁+t₂). Substitute in either original tangent to give y=2t₁t₂. If the parameters coincide, these are the same tangent and no unique intersection S is defined.',345,'matches')
p3['additional_operations']={'both_tangent_residuals':{'kind':'identity','operands':['Tuple((2*a*b)-a*(2*(a+b))+2*a**2,(2*a*b)-b*(2*(a+b))+2*b**2)']}}
p3['additional_operation_expected']={'both_tangent_residuals':'Tuple(0,0)'}
p4=value('iv','(2*(a+b)).subs(b,2-a)','4',345,'The stated sum fixes the x-coordinate of S at 4. The question asks for a containing straight line, not a complete locus, so no unrequested ordinate-range conclusion is required.');p4['author_answer_form']='x=4.'
add(7,131,'Read the given parabola x=4t,y=2t² for positive and negative t. Derive gradient and tangent, intersect tangents at distinct t₁,t₂, then use t₁+t₂=2 to identify the containing line x=4. No sketch response or complete locus is requested.',[p,p2,p3,p4],[PARAM,GEOM],[SIMULT,COORD])
X='4*cos(t)';Y='3*sin(t)'
p=pv('i','parametric-derivative',X,Y,'-3*cos(t)/(4*sin(t))')
p2=pv('ii','parametric-tangent',X,Y,'Tuple(3*cos(t),4*sin(t),-12)')
p3=reasoning('iii','t=atan(3/4)+nπ; base angle 0.6435 radians to four decimal places. This unbounded solution part is outside 8227 LIMIT02.',
 'The line x+y=0 has slope −1. Set the independently derived slope to −1, giving 3cos t=4sin t, hence tan t=3/4 on the regular branch. All solutions have the stated π-periodic form; the question gives no finite interval. Verify the base angle and periodic identity, while excluding this part from 8227 coverage. Do not invent an interval.',345,'matches')
p3['additional_operations']={'base_angle_4dp':{'kind':'rounded','operands':['atan(3/4)'],'decimal_places':4},'base_slope':{'kind':'identity','operands':['(-3*cos(t)/(4*sin(t))).subs(t,atan(3/4))']},'pi_period':{'kind':'trig-identity-residual','operands':['tan(t+pi)','tan(t)']}}
p3['additional_operation_expected']={'base_angle_4dp':'0.6435','base_slope':'-1','pi_period':'0'}
row=add(8,131,'Particle coordinates x=4cos t,y=3sin t: derive gradient and tangent, then all times when travel is parallel to x+y=0. Parts (i)–(ii) are in scope; the unbounded general trig solution in (iii) is excluded by LIMIT02.',[p,p2,p3],[PARAM,GEOM],[ELEMENTARY])
row['value_level_scope_decisions'].append({'rule_id':'8227:LIMIT02','status':'outside','applies_to':'iii only','quoted_value':'Find the values of t; no finite interval is supplied. Key t=0.6435+nπ.','reason':'Unbounded general trigonometric solutions are excluded from 8227.'})
row['scope_check']={'status':'in-scope-parts-only','basis':'8227 LIMIT02','excluded_or_qualified_parts':['iii: unbounded general trigonometric solutions']}
X='exp(3*t)';Y='t**2*exp(t)+3'
p=pv('i','parametric-derivative',X,Y,'t*(t+2)/(3*exp(2*t))',131,proof=True)
p2=pv('ii','parametric-derivative',X,Y,'0',131,'0',True)
p2['assertions']=[{'expression':'Tuple(exp(3*t),t**2*exp(t)+3).subs(t,0)','expected':'Tuple(1,3)'}]
p3=pv('iii','parametric-stationary-points',X,Y,'FiniteSet(Tuple(exp(-6),4*exp(-2)+3),Tuple(1,3))')
p3['author_answer_form']='Other point: (e^(−6),4e^(−2)+3); exclude the already supplied (1,3).'
p3['key_comparison_note']='Full derived set is compared to the printed other point together with the given point. This explicit augmentation does not claim the key prints the given point in (iii).'
add(9,131,'For x=e^(3t),y=t²e^t+3, show the slope formula and the horizontal tangent at (1,3), then find the other horizontal-tangent point. Negative t=−2 is valid: t is a real parameter, not explicitly nonnegative time.',[p,p2,p3],[PARAM,GEOM,STATIONARY],[ELEMENTARY,COMPOSITE])
p=pv('proof','parametric-derivative','exp(-t)*cos(t)','exp(-t)*sin(t)','tan(t-pi/4)',131,proof=True)
p['original_common_domain']='Radian t; sin t+cos t≠0 for finite slope.'
add(10,131,'Show the gradient of x=e^(−t)cos t,y=e^(−t)sin t is tan(t−π/4). Both exponents are negative on the enlarged render; a positive-exponent transcription would create a false defect.',[p],[PARAM],[ELEMENTARY,COMPOSITE])
X='3*t+log(t-1)';Y='t**2+1'
p=pv('i','parametric-derivative',X,Y,'2*t*(t-1)/(3*t-2)')
p2=value('ii','Tuple((3*t+log(t-1)).subs(t,2),(t**2+1).subs(t,2))','Tuple(6,5)',345,'Solve 2t(t−1)/(3t−2)=1. The algebraic candidates are 1/2 and 2; the original log domain t>1 rejects 1/2. Substitute t=2 in both original coordinates.')
p2['additional_operations']={'algebraic_candidates':{'kind':'identity','operands':['FiniteSet(*solve(2*t*(t-1)-(3*t-2),t))']}}
p2['additional_operation_expected']={'algebraic_candidates':'FiniteSet(1/2,2)'}
add(11,132,'For x=3t+ln(t−1),y=t²+1, t>1, find gradient and the unique point with gradient 1. Retain the original logarithm domain when rejecting the second algebraic candidate.',[p,p2],[PARAM,GEOM],[ELEMENTARY,COMPOSITE])
p=pv('gradient','parametric-derivative','4*sin(t)','3-2*cos(2*t)','2*sin(t)')
p['original_common_domain']='−π/2<t<π/2, so X′=4cos t>0; endpoints are excluded.'
add(12,132,'For x=4sinθ,y=3−2cos2θ on −π/2<θ<π/2, simplify dy/dx. The open branch ensures a nonzero parameter derivative; no unrestricted general root set is requested.',[p],[PARAM],[ELEMENTARY,DOUBLE])
p=pv('i','parametric-derivative','1-exp(-t)','exp(t)+exp(-t)','exp(2*t)-1',132,proof=True)
p2=value('ii','solve(exp(2*t)-1-2,t)[0]','log(3)/2',345,'Use the requested preceding slope formula, solve e^(2t)=3 by natural logarithms and retain the exact parameter. X′=e^(−t)>0 for all real t.')
add(13,132,'For x=1−e^(−t),y=e^t+e^(−t), show the slope is e^(2t)−1 and hence find exact t when it is 2. The exponential equation is explicitly requested, so its inverse-log demand is direct.',[p,p2],[PARAM,GEOM,LOGDEF],[ELEMENTARY,COMPOSITE])
p=pv('proof','parametric-derivative','2*t+sin(2*t)','1-cos(2*t)','tan(t)',132,proof=True)
p['original_common_domain']='Finite ratio requires cos t≠0. At cos t=0 both coordinate derivatives vanish; a cusp requires separate geometric treatment.'
add(14,132,'For x=2θ+sin2θ,y=1−cos2θ, prove dy/dx=tanθ on the regular branch. Do not cancel the common cosθ factor and then claim the singular cusp has a finite derivative.',[p],[PARAM],[ELEMENTARY,DOUBLE])
X='a*cos(t)**3';Y='a*sin(t)**3'
p=pv('i','parametric-derivative',X,Y,'-tan(t)')
p2=pv('ii','parametric-tangent',X,Y,'Tuple(3*a*sin(t)**2*cos(t),3*a*sin(t)*cos(t)**2,-3*a**2*sin(t)**2*cos(t)**2)',132,proof=True)
p2['normalisation_note']='Divide by 3a sin t cos t>0 under the stated a>0,0<t<π/2. This gives x sin t+y cos t−a sin t cos t=0.'
p3=reasoning('iii','The intercept distance XY is a.',
 'The nonzero sine and cosine give X=(a cos t,0), Y=(0,a sin t). Thus XY²=a²(cos²t+sin²t)=a². The given a>0 selects distance a rather than |a|. The strict angle bounds avoid the coincident-axis intercept cases.',132,'show/prove')
p3['additional_operations']={'squared_distance':{'kind':'identity','operands':['(a*cos(t))**2+(a*sin(t))**2']},'intercept_residuals':{'kind':'identity','operands':['Tuple((a*cos(t))*sin(t)-a*sin(t)*cos(t),(a*sin(t))*cos(t)-a*sin(t)*cos(t))']}}
p3['additional_operation_expected']={'squared_distance':'a**2','intercept_residuals':'Tuple(0,0)'}
row=add(15,132,'Astroid x=a cos³t,y=a sin³t, explicitly a>0 and 0<t<π/2: derive gradient, prove the tangent equation and show its axis-intercept segment has constant length a. The positive scale and open quadrant are essential.',[p,p2,p3],[PARAM,GEOM],[ELEMENTARY,COORD])
row['source_interpretation']={'parameter_domains':{'a':'positive','t':'0<t<π/2 radians'},'reason':'Unlike 4E4/6, the source explicitly supplies the conditions needed for nondegenerate intercept geometry and positive length.'}
# The only given graph in the exercise set is a source element in its own right.
p=W/'checks/r5/textbooks/Goldie-C4-130.png'
figure={'item_id':'8227:TB:Goldie:C4:Teaching-figure:45','item_kind':'given-figure','exercise':'Teaching figure','item_number':'45','pdf_page':131,'printed_page':117,
 'source_label':'Exercise 4E7 given parabola','notes':'Given full upward parabola x=4t,y=2t² for both signs of t, with origin O and coordinate axes. No extra scale or numerical point is read from the sketch.',
 'what_it_shows':'Both branches of y=x²/8, with vertex O. The parameter takes positive and negative values.',
 'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[PARAM,GEOM],'representation':'graph','source_evidence':ev(131),
 'parent_item_id':'8227:TB:Goldie:C4:Exercise-4E:7','learner_display':False,
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':'x=4t,y=2t²; both positive and negative t.','reason':'Polynomial parametric graph, not trig-equation solving.'}],
 'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],'relation':'Internal textbook given graph; not evidence of an official marking criterion.'},
 'mathematical_feature_review':{'status':'author render/identity checked; independent acceptance pending','method':'Eliminate t=x/4, giving y=x²/8 for every real x. This confirms both signs and the unlabelled origin vertex.',
 'checks':[{'operation':{'kind':'identity','operands':['(2*t**2).subs(t,x/4)']},'source_normalised':'x**2/8','derived':str(compute({'kind':'identity','operands':['(2*t**2).subs(t,x/4)']}))}]}}
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+([figure['item_id']]if page==131 else[]),
 'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
 'non_item_content':'Every question and connected subpart of Exercise 4E is listed; the only given graph has its own record. Printed examination attributions are internal discovery leads.'}for page in range(130,133)]
if __name__=='__main__':
    for name,data in [('answers-Goldie-C4-4E.json',{'scope':'All 15 questions and every connected requested response; 8(iii) solved only as excluded source evidence.','items':answers}),
      ('census-Goldie-C4-4E.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,'scope':'Complete exercise pages 130–132.','new_items':[figure],'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for row in answers:
        for part in row['subparts']:
            if 'operation'in part:
                got=compute(part['operation']);assert equivalent(got,expression(part['printed_key_normalised'])),(row['item_id'],part['subpart'],got,part['printed_key_normalised'])
            for name,op in part.get('additional_operations',{}).items():
                assert equivalent(compute(op),expression(part['additional_operation_expected'][name])),(row['item_id'],part['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs; one given figure; focused fixed-source mathematics passed')
