"""YM478–479: all seven Exercise10 questions and connected exam-style ratios."""
import json
from author_YM_C4_composite_equations import roots
import author_YM_C10_rform_cycles_extrema as m
import author_YM_C10_compound_sine as s
import author_YM_C10_opening as o
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
BND=m.BND;ALL=m.ALL;RFORM=m.RFORM;RANGE=m.RANGE;D=m.D
COMP=o.COMPOUND;EVAL=o.EXACT;RECIP=o.RECIP;DOUBLE='8227:2020:M2:T3:O02:D03';PYTH='8227:2020:M2:T3:O02:D01';BASIC='8227:2020:M1:T6:O05:D01'
value=m.value;form=m.form

def bounded(label,expr,key,kp,branches,direct,lo='0',hi='360'):
 p=roots(label,expr,key,kp,branches,lo=lo,hi=hi,approx=isinstance(key,list));p.update(assessed_8227_demand_ids=direct+[BND,ALL],response_format='numeric',original_equation_zero_form=expr,method='Transform the ORIGINAL equation on its own domain, retain all factor branches and original poles, solve the complete actual interval including its specified endpoints, and substitute all candidates back. An auxiliary quadratic root is not the final requested angle.');return p

def proof(label,lhs,rhs,kp,domain,method,direct):
 p=s.proof(label,lhs,rhs,kp,domain,method);p['assessed_8227_demand_ids']=direct;return p

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts)
 r.update(exam_style=page==479,exam_style_basis='Source10.5 explicitly labels these as exam-style; this is textbook classification,not original examination provenance.'if page==479 else'Ordinary Exercise10 basic/intermediate/advanced questions,not the next10.5 exam-style section.',mapping_rationale='Direct links follow requested outputs and required new trigonometric identity/representation. Auxiliary quadratic manipulation is a component,not automatic polynomial demand coverage. The basic sin²+cos² identity is separated from reciprocal Pythagorean identities. Given hence results,source duplicate tasks,and exact ratio rather than unasked angle outputs are retained.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='within'if page==478 else'not applicable',quoted_value=note,reason='Actual bounded-solve arguments have multiplier1or2,including shifts. Page479asks exact ratios and a reduction,not a bounded angle set.'),dict(rule_id='8227:LIMIT02',status='within'if page==478 else'not applicable',quoted_value=note,reason='Finite original intervals are retained. No general solution family is asked; exact ratio tasks are distinct.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03','8227:LIMIT02']),precision_angle_check=dict(source='Degree intervals on478;phase2dp explicitly inQ7. Example26/Try26 use exact acute-angle ratios without finding the angle.',comparison='Keep exact radicals and full internal root precision; compare the key at its printed last place. Do not infer a second angle quadrant from a condition imposed only on the firstangle.'))
 return r
p=bounded('roots',f'sec({D})-4+2*tan({D})**2',['48.19','120'],644,[('cos','x','2/3',1),('cos','x','-1/2',1)],[PYTH,RECIP],hi='180')
add('Exercise-10',1,478,'secx=4−2tan²x on CLOSED0..180degrees. Reciprocal Pythagorean reduction givessecx3/2or−2; requested roots48.19/120,with secant poles excluded.',[p])
p=bounded('roots',f'8+cot({D})-2*csc({D})**2',['26.57','146.3','206.6','326.3'],644,[('tan','x','1/2',1),('tan','x','-2/3',1)],[PYTH,RECIP])
add('Exercise-10',2,478,'8+cotθ=2cosec²θ on CLOSED0..360degrees. Originalsinθnonzero; cotθ2or−3/2 gives four roots,not a single principal inverse value.',[p])
p=proof('a-reduction','2*(sin(x+pi/6)-2*cos(x+pi/3))','3*sqrt(3)*sin(x)-cos(x)',644,'Allrealx; equations have no reciprocal poles.','Expand BOTH original shifted ratios and collect the sine/cosine coefficients. The residual is scaled by nonzero2,so the stated equations are equivalent.',[COMP,EVAL])
q=bounded('b-roots',f'sin({D}+pi/6)-2*cos({D}+pi/3)',['10.9','-169.1'],644,[('tan','x','1/(3*sqrt(3))',1)],[COMP,EVAL],lo='-180',hi='180');q['depends_on_source_parts']=['a-reduction']
add('Exercise-10',3,478,'SHOW sin(x+30°)=2cos(x+60°) reduces to3√3sinx=cosx; HENCE solve the original equation on CLOSED−180..180degrees. Cosinezero gives no lost root.',[p,q])
p=proof('a-identity','1/(sin(x-pi/3)+cos(x-pi/6))','csc(x)',644,'sinx≠0; the ORIGINAL denominator expands exactlytosinx.','Expand original shifted denominator,collect it tosinx,then reciprocate only where it is nonzero.',[COMP,EVAL,RECIP])
q=bounded('b-roots',f'2/(sin({D}-pi/3)+cos({D}-pi/6))-3*cot({D})**2+2',['36.87','143.13','270'],644,[('sin','x','3/5',1),('sin','x','-1',1)],[COMP,EVAL,PYTH,RECIP]);q['depends_on_source_parts']=['a-identity']
add('Exercise-10',4,478,'Prove original reciprocal shifted-sine/cosine identity,then HENCE solve2/(same denominator)=3cot²x−2 on CLOSED0..360degrees. cscx5/3or−1;270degrees is valid,not an excluded tangentpole.',[p,q])
p=bounded('roots',f'5*cos({D})*(1+cos(2*{D}))-4',['42.5','317.5'],644,[('cos','x','(2/5)**(1/3)',1)],[DOUBLE,EVAL])
r=add('Exercise-10',5,478,'Original5cosθ(1+cos2θ)=4 on CLOSED0..360degrees. EXACT source duplicate of Try16Q3:10cos³θ4,roots42.5/317.5. Separate occurrence,not additional structural breadth.',[p]);r.update(source_duplicate_of='8227:TB:YM:C10:Try-Now-16:3',duplicate_basis='Same original equation,interval and requested roots as source466 Try16Q3; checked on both rendered pages.')
p=proof('a-identity','sin(2*x)**2*(csc(x)**2-sec(x)**2)','4*cos(2*x)',644,'sinxcosx≠0,as requiredby the ORIGINAL cosecant/secant.','Expand sin2x=2sinxcosx,retainoriginal nonzero denominators,and reach4(cos²x−sin²x)=4cos2x.',[DOUBLE,EVAL,RECIP])
q=bounded('b-i-roots',f'sin(2*{D})**2*(csc({D})**2-sec({D})**2)-3',['20.7','159.3'],644,[('cos','2*x','3/4',1)],[DOUBLE,EVAL,RECIP],hi='180');q['depends_on_source_parts']=['a-identity']
r=value('b-ii-exact-value','csc(pi/12)**2-sec(pi/12)**2','8*sqrt(3)',645,[DOUBLE,EVAL,RECIP],'Use the proved identity at15degrees: difference=4cos30/sin²30=8√3. Independently recompute the ORIGINAL cosecant/secant difference exactly; all original denominators are nonzero.');r['depends_on_source_parts']=['a-identity']
add('Exercise-10',6,478,'Prove sin²2θ(cosec²θ−sec²θ)=4cos2θ. HENCE solve its3-equation on CLOSED0..180degrees and evaluate cosec²15°−sec²15° exactly. Separate answerpages644/645 kept.',[p,q,r])
p=form('a-R-phase','5','2','sin-plus','Tuple(sqrt(29),Rational(2180,100))',645)
q=bounded('b-roots',f'5*sin(2*{D})+2*cos(2*{D})-4',['13.1','55.1','193.1','235.1'],645,[('sin','2*x+180*atan(Rational(2,5))/pi','4/sqrt(29)',1)],[RFORM]);q['depends_on_source_parts']=['a-R-phase']
r=value('c-smallest-value','1/maximum(x**2,x,Interval(-2*sqrt(29),2*sqrt(29)))','Rational(1,116)',645,[RFORM,RANGE],'The ORIGINAL denominatorinner10sin2θ+4cos2θ has range[−2√29,2√29]. Maximize its SQUARE independently,then invert the positive maximum116. Reciprocal is undefined atinnerzero; this does not remove attainable endpoints±2√29.');r.update(depends_on_source_parts=['a-R-phase'],original_domain='Allrealθ except zeros of10sin2θ+4cos2θ. Both positive and negative amplitude attain the same minimum.')
add('Exercise-10',7,478,'Advanced task:5sin2θ+2cos2θ=√29sin(2θ+α),phase21.80°2dp; original=4 gives four roots on CLOSED0..360. Minimum reciprocal SQUARE of the doubled linear combination is1/116.',[p,q,r])
p=value('a-tangent-ratio','(sqrt(9+160)-3)/4','Rational(5,2)',479,[PYTH,RECIP],'Let t=tanθ and replace sec²θ by1+t² in the ORIGINAL2sec²θ+3tanθ22. Solve2t²+3t−20=0; reject−4 becauseθisacute. Requested output is t5/2,notθ.');extra(p,'original-reduced-polynomial','2*Rational(5,2)**2+3*Rational(5,2)-20','0')
q=value('b-exact-compound-ratio','(Rational(5,2)+tan(3*pi/4))/(1-Rational(5,2)*tan(3*pi/4))','Rational(3,7)',479,[COMP,EVAL],'Apply the tangent sum formula to the ORIGINAL θ+135degrees,with exacttanθ5/2 andtan135−1. Denominator7/2 is nonzero; result3/7.');q['depends_on_source_parts']=['a-tangent-ratio']
add('Example',26,479,'Exam-style: acuteθ,2sec²θ+3tanθ22. Find exacttanθ5/2,then exacttan(θ+135°)3/7. An unasked decimalangle is not the assessed final answer.',[p,q])
p=proof('a-shown-reduction','2*tan(x)**2+sec(x)**2-5+4*tan(x)','3*tan(x)**2+4*tan(x)-4',645,'αacute,so ORIGINAL cosαnonzero.','Replace ORIGINALsec²αwith1+tan²α; collect to the required quadratic residual.',[PYTH,RECIP])
q=value('a-tangent-ratio','(-4+sqrt(16+48))/6','Rational(2,3)',645,[PYTH,RECIP],'Solve the shown quadratic and retain positive2/3 for the ORIGINAL acuteα; reject−2.');q['depends_on_source_parts']=['a-shown-reduction']
r=value('b-cotangent-beta','(1+6*Rational(3,2))/(Rational(3,2)-6)','-Rational(20,9)',645,[COMP,EVAL,RECIP],'From cotα3/2 and ORIGINALcot(α+β)6,use(uv−1)/(u+v)=6. Solve (3/2−6)v=10 to get−20/9. No quadrant restriction onβwas given; do not reject its negativecotangent. Common denominatoru+v=−13/18isnonzero.');r['depends_on_source_parts']=['a-tangent-ratio'];extra(r,'original-compound-cotangent','(Rational(3,2)*(-Rational(20,9))-1)/(Rational(3,2)-Rational(20,9))','6')
add('Try-Now',26,479,'Exam-style: αacute,2tan²α+sec²α5−4tanα. Show3tan²α+4tanα−4=0,hence exacttanα2/3. Given cot(α+β)6,find exactcotβ−20/9 with no extraβquadrant condition.',[p,q,r])
refs=[(124,479,'Example26a reciprocal-Pythagorean solution','sec²θ=1+tan²θ converts the original equation to2t²+3t−20=0;acuteθrejectst−4.',PYTH,'table','Example:26'),(125,479,'Example26 requested-output reminder','The question asks tanθ,not a decimalθ; retain exact5/2.',EVAL,'table','Example:26'),(126,479,'Example26b tangent-addition working','tan135−1; originalsumratio3/7 with nonzero denominator.',COMP,'table','Example:26'),(127,479,'Example26b SOLUTION special-angle triangle','Sides1,1,√2give exacttan45=1;135degrees has negative tangent.',EVAL,'diagram','Example:26')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent);figures[-1]['mathematical_feature_review']['method']='Read the actual acute-angle restriction,exact outputrequest and135degree triangle. Verify tangent/cotangent addition from original ratios and check all original denominators.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='All seven Exercise10 questions,Example26/Try26 and four actual solutionpanelsenumerated. Exercise10Q5 duplicates Try16Q3. Exam-style designation starts479,not on ordinary Exercise10.',scope_screen='Retain original reciprocal poles,negative lower boundQ3,complete double-angle cycles,and no inventedβquadrant restriction.')for page in[478,479]]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C10-exercise-examstyle.json',dict(scope='Complete478–479Exercise10/exam-style responses.',items=answers)),('census-YM-C10-exercise-examstyle.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete478–479page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
