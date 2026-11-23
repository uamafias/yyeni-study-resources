"""Fixed-source integration opening, PDF135–139; definitions and tasks separated."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2];sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
EXPINT='8227:2020:M2:T5:O01:D01';DEF='8227:2020:M1:T9:O03:D01';AREA='8227:2020:M1:T9:O04:D01'
REVERSE='8227:2020:M2:T5:O01:D03';DOMAIN='8227:2020:M1:T3:O02:D01';FUNC='8227:2020:M1:T3:O01:D01'
def ev(page):
    name='Goldie-C4-134'if page<138 else'Goldie-C5-138'if page<142 else'Goldie-key-C4-C5-345'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,rep='text',new_item=False):
    for p in parts:
        kp=p.pop('key_page_override',page)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C5:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
     'mapping_rationale':'The requested integral, area or domain explanation is direct. Teaching formula blocks have teaches links only. Contextual estimation does not become prescribed calculus coverage.',
     'representation':rep,'sketch_response_required':False,'exam_style':False,'exam_style_basis':'Unattributed worked example, activity or boxed prompt; no examination attribution.',
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL04','status':'not applicable','quoted_value':note,'reason':'Proper finite integrals on one continuous domain component, or qualitative source support; no integral through a pole is allowed.'},
      {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Natural logarithms, not a change-of-base task.'}],
     'precision_angle_check':{'source':'Examples1(ii),2,3,4 display 3 significant figures after exact working. No angle quantities in this segment.','comparison':'Retain exact integration and original domains. A negative signed integral is distinct from positive geometric area.'},
     'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'prompt','exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'representation':rep,'source_evidence':ev(page),'learner_display':False})
    return row

def indefinite(label,f,key,page):
    p=value(label,'0',key,page,'Integrate the original source integrand independently. For real logarithmic primitives use ln|u| on each component u≠0; additive constants can differ between disconnected components. Differentiate the resulting real primitive away from zeros/poles.')
    p['operation']={'kind':'real-elementary-antiderivative','operands':[f]};p['author_answer_form']='The listed primitive plus an arbitrary real constant on each connected domain component.';return p

def definite(label,f,lo,hi,key,page,sf=None):
    op={'kind':'proper-definite-integral','operands':[f,str(lo),str(hi)]}
    if sf:
        p=value(label,f'integrate({f},(x,{lo},{hi}))',key,page,'Check continuity on the entire finite interval, evaluate exactly, then round only the final result to the stated significant figures.')
        p['operation']={'kind':'rounded','operands':[f'integrate({f},(x,{lo},{hi}))'],'significant_figures':sf}
        p['additional_operations']={'exact_proper_integral':op}
    else:
        p=value(label,'0',key,page,'Check continuity on the whole interval before evaluating the original integrand. A primitive endpoint subtraction is not accepted across an original pole.')
        p['operation']=op
    return p
p=reasoning('method','Partition the photograph into sample squares, estimate birds per square and scale by occupied squares; report an estimate rather than an exact count.',
 'A consistent spatial sample supplies an approximate density. The image has uneven flock density and perspective, so a single square is not guaranteed representative. The source key explicitly offers squares and estimated birds per square as one possible method. No unique numerical bird count is specified.',345,'matches')
add('Prompt',1,135,'The opening photograph asks how to estimate its bird count. It supports sampling/estimation discussion, not an invented assessed integration objective.',[p],[],[],rep='diagram')
add('Example',1,136,'Integrate e^(2x−3) indefinitely and evaluate ∫₁⁵6e^(3x)dx, with the solution reporting the second result to 3 significant figures.',[
 indefinite('i','exp(2*x-3)','exp(2*x-3)/2',136),definite('ii','6*exp(3*x)',1,5,'6540000',136,3)],[EXPINT,DEF])
add('Example',2,136,'Evaluate ∫₂⁵1/(2x)dx. The interval is positive and has no pole; solution exact ½ln(5/2), displayed 0.458 to 3 significant figures.',[
 definite('value','1/(2*x)',2,5,'0.458',136,3)],[EXPINT,DEF])
add('Example',3,137,'Evaluate ∫₀²1/(5x+3)dx. The affine denominator stays positive on the entire interval; solution displays 0.293 to 3 significant figures.',[
 definite('value','1/(5*x+3)',0,2,'0.293',137,3)],[EXPINT,DEF])
p=reasoning('i','The two shaded geometric areas are equal for 0<a<b.',
 'On the given y=1/x graph, substitute x=−u or use odd symmetry. The left signed integral ∫₋ᵦ⁻ᵃ1/x dx=ln(a/b) is the negative of the right signed integral ln(b/a). Their positive geometric areas therefore agree. Never identify a negative integral with a negative geometric area.',345,'matches')
p2=reasoning('ii','The equality follows from y=1/x being odd, or the substitution u=−x with reversed bounds.',
 'With 0<a<b, the substitution reverses limits b→a and introduces dx=−du, so the left signed integral is −ln(b/a). Negate it for the below-axis area. The book supplies the substitution proof on the next page; the answer-key remark supplies odd symmetry as an alternative.',138,'show/prove')
p2['additional_operations']={'signed_integral_relation':{'kind':'identity','operands':['(log(a)-log(b))+(log(b)-log(a))']},'odd_symmetry':{'kind':'identity','operands':['1/(-x)+1/x']}}
p2['additional_operation_expected']={'signed_integral_relation':'0','odd_symmetry':'0'}
row=add('Activity',1,137,'Activity5.1 compares shaded regions under y=1/x on [a,b] and above it on [−b,−a], with positive a<b read from the labelled diagram; conjecture equality and prove it.',[p,p2],[AREA],[EXPINT],rep='graph')
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[138]})
add('Example',4,138,'Evaluate ∫₅⁷1/(4−x)dx. Both limits lie to the right of the pole x=4; use ln|4−x| or ln|x−4| and preserve the negative integral. The displayed value is −1.10 to 3 significant figures.',[
 definite('value','1/(4-x)',5,7,'-1.10',138,3)],[EXPINT,DEF])
p=reasoning('rational-discontinuity','Zeros of the original denominator p₂(x) are excluded from the original quotient; cancellation does not restore the original function there.',
 'A polynomial is continuous everywhere. A quotient of continuous polynomials is continuous wherever its denominator is nonzero. A common numerator factor may give a removable hole, but the original quotient is still undefined there. The source key says the denominator can take value zero.',345,'matches')
p2=reasoning('polynomial-continuity','The polynomial x²−2x+3 is continuous for all real x.',
 'It is a polynomial (equivalently a quotient with denominator 1), so it has no real denominator holes. The key additionally completes the square to (x−1)²+2≥2; positivity is true but is not needed to prove polynomial continuity.',345,'matches')
p2['additional_operations']={'completed_square':{'kind':'identity','operands':['expand((x-1)**2+2)-(x**2-2*x+3)']}}
p2['additional_operation_expected']={'completed_square':'0'}
add('Prompt',2,139,'Explain how a rational equation signals a discontinuity, then prove y=x²−2x+3 has none. Distinguish denominator holes from numerator zeros; completing the square shows positivity but is not the continuity criterion.',[p,p2],[DOMAIN,FUNC])
figures=[]
def fig(n,page,label,note,teaches,rep,checks=None,parent=None):
    results=[]
    for expr,target in checks or []:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C5:Teaching-figure:{n}','item_kind':'given-figure'if parent else'teaching-figure','exercise':'Teaching figure','item_number':str(n),'pdf_page':page,'printed_page':page-14,
     'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
     'representation':rep,'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C5:'+parent if parent else None,'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL04','status':'not applicable','quoted_value':note,'reason':'A reference/given figure; no improper integral is prescribed. Poles are explicitly retained.'}],
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],'relation':'Internal source teaching/given figure; not another problem family or official mark scheme.'},
     'mathematical_feature_review':{'status':'author rendered source and listed checks; independent acceptance pending','method':'Inspect the actual source labels,domains,orientation and geometric relationships. Recompute explicit mathematical features where listed; visual reading remains a manual source check,not an automated image proof. Retain stated conditions for general formulas.','checks':results}})
fig(1,135,'Bird-estimation photograph','A flock image supports an estimation method; no metric scale or exact count is asserted. Density varies, so the same image cannot accompany arbitrary exact-count variants.',[],'diagram',parent='Prompt:1')
fig(2,135,'Exponential reverse-derivative reference','d(e^(ax+b))/dx=a e^(ax+b) gives primitive e^(ax+b)/a for a≠0. At a=0 use the constant integrand separately.',[EXPINT,REVERSE],'table',[('diff(exp(a*x+b)/a,x)','exp(a*x+b)')])
fig(3,136,'Reciprocal-linear integration reference','For ax+b>0, d ln(ax+b)/dx=a/(ax+b), and ∫1/(ax+b)dx=ln(ax+b)/a+c for a≠0. The arbitrary constant may change when rescaled; the next page extends the real domain with absolute values.',[EXPINT,REVERSE],'table',[('diff(log(a*x+b),x)','a/(a*x+b)')])
fig(4,137,'Figure5.1 equal-area reciprocal branches','The graph y=1/x has shaded right region [a,b] above the axis and left region [−b,−a] below it, where 0<a<b. Physical areas agree; signed integrals have opposite signs.',[AREA],'graph',[('1/(-x)+1/x','0')],parent='Activity:1')
fig(5,138,'Absolute-value logarithm primitives','∫1/x dx=ln|x|+c and ∫f′(x)/f(x)dx=ln|f(x)|+c on each connected differentiable component where the denominator is nonzero. No formula authorises integrating through a pole.',[EXPINT,REVERSE],'table',[('diff(log(-x),x)','1/x'),('diff(log(x),x)','1/x')])
fig(6,139,'Figure5.2 pole warning','The y=1/x hyperbola is undefined at0. A proper definite integral of1/x cannot cross0; bounds must lie on the same sign component. This warning distinguishes the divergent improper integral from a principal-value cancellation.',[EXPINT,DEF],'graph',[('limit(1/x,x,0,dir="+")','oo'),('limit(1/x,x,0,dir="-")','-oo')])
# Exercise5A1–3 also begins139; its builder owns the combined page census.
pages=[]
for page in range(135,139):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[row['item_id']]if page==138 else[],
     'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every opening example, boxed question, activity and mathematical/given figure recorded; general explanatory prose is attached to its reference block. Page139 census awaits5A1–3.'})
if __name__=='__main__':
    for name,data in [('answers-Goldie-C5-opening.json',{'scope':'Every opening task and all Example1–4 subparts.','items':answers}),
     ('census-Goldie-C5-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete135–138; Prompt2/figure6on139 await combined5A census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for row in answers:
        for p in row['subparts']:
            if 'operation'in p:
                got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got)
                for op in p.get('additional_operations',{}).values():compute(op)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
