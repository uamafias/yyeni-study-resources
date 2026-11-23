"""Every reference block on PDF133 and the PDF134 outcome-only boundary."""
import hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2];sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
P='8227:2020:M2:T4:O03:D02';I='8227:2020:M2:T4:O03:D01';E='8227:2020:M2:T4:O01:D01';C='8227:2020:M2:T4:O01:D02';R='8227:2020:M2:T4:O02:D01';WPOW='8227:2020:M1:T8:O02:D01'
def ev(page):
    p=W/f"checks/r5/textbooks/{'Goldie-C4-130'if page==133 else'Goldie-C4-134'}.png"
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
figures=[]
blocks=[
 (1,'Power rule','d(kx^n)/dx=knx^(n−1), with real k,n in the source. For 8227 use only its permitted rational powers and real differentiable branches; the generic source statement does not enlarge syllabus scope.',[WPOW],[('diff(k*x**n,x)','k*n*x**(n-1)')]),
 (2,'Chain rule','dy/dx=(dy/du)(du/dx), on differentiable composed branches. This reference block is not an additional learner task.',[C],[('diff(exp(x**2),x)','2*x*exp(x**2)')]),
 (3,'Product rule','For y=uv, y′=v u′+u v′. The representative check uses two genuinely varying factors.',[R],[('diff(x**2*exp(x),x)','exp(x)*2*x+x**2*exp(x)')]),
 (4,'Quotient rule','For y=u/v, y′=(v u′−u v′)/v², wherever v≠0. Original denominator exclusions survive simplification.',[R],[('diff((x**2+1)/(x-2),x)','((x-2)*2*x-(x**2+1))/(x-2)**2')]),
 (5,'Reciprocal derivative','dy/dx=1/(dx/dy) only for a locally invertible differentiable relation with nonzero finite reciprocal derivative. It does not justify dividing at a horizontal or vertical exceptional point.',[C],[('1/diff(y**3,y)','1/(3*y**2)')]),
 (6,'Natural logarithm derivative','d(ln x)/dx=1/x on the original real domain x>0.',[E],[('diff(log(x),x)','1/x')]),
 (7,'Exponential derivative','d(e^x)/dx=e^x for real x.',[E],[('diff(exp(x),x)','exp(x)')]),
 (8,'Three linear-argument trigonometric derivatives','d(sin kx)/dx=k cos kx; d(cos kx)/dx=−k sin kx; d(tan kx)/dx=k sec²kx. Arguments are radians and the tangent domain excludes cos kx=0.',[E,C],[('diff(sin(k*x),x)','k*cos(k*x)'),('diff(cos(k*x),x)','-k*sin(k*x)'),('diff(tan(k*x),x)','k*sec(k*x)**2')]),
 (9,'Implicit definition and differentiation illustrations','An implicit relation leaves y unsolved. The block illustrates y² and 4x³y² with y dependent on x, and states that a constant differentiates to zero. It does not claim every relation is globally a function.',[I],[('diff(y**2,x)+diff(y**2,y)*p','2*y*p'),('diff(4*x**3*y**2,x)+diff(4*x**3*y**2,y)*p','12*x**2*y**2+8*x**3*y*p'),('diff(c,x)','0')]),
 (10,'Parametric definition','Write two coordinates in terms of a third variable, the parameter. This is definition prose in the key-points table; no numerical response or additional independent task.',[P],[]),
 (11,'Parametric plotting procedure','Plot points obtained from different parameter values. Preserve the original parameter domain and trace direction; finite samples do not by themselves certify every intervening curve feature.',[P],[]),
 (12,'Parametric ratio and regularity','dy/dx=(dy/dt)/(dx/dt), explicitly provided dx/dt≠0. Exceptional parameters require their own branch/limit analysis rather than cancellation alone.',[P],[('diff(2*t,t)/diff(t**2,t)','1/t')])]
for n,title,note,teaches,checks in blocks:
    results=[]
    for source,target in checks:
        got=compute({'kind':'identity','operands':[source]});assert equivalent(got,expression(target)),(title,got)
        results.append({'operation':{'kind':'identity','operands':[source]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{45+n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(45+n),
     'pdf_page':133,'printed_page':119,'source_label':f'Key points {n}: {title}','notes':note,'what_it_shows':note,
     'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':'table','source_evidence':ev(133),'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'not applicable','quoted_value':note,'reason':'Reference/theorem support rather than an assessed power-rule example; the generic real-n statement must not broaden 8227 rational-power scope.'}],
     'value_level_scope_review_status_r5':'author source statement and applicable domain reviewed; independent check pending',
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],'relation':'Internal formula/teaching reference, not another examination-observed task.'},
     'mathematical_feature_review':{'status':'author source render and listed checks; independent acceptance pending','method':'Read the complete statement and qualify its real domain/regularity. Listed representative chain/product/quotient checks illustrate the general rule; they are not a proof of the theorem for all functions. Definition/procedure prose is explicitly non-numerical.','checks':results}})
pages=[{'pdf_page':133,'printed_page':119,'chapter':4,'page_status':'items enumerated','item_ids':[r['item_id']for r in figures],'continuation_item_ids':[],
 'source_evidence':ev(133),'non_item_content':'All twelve numbered key-point blocks have individual internal reference records, including both examples in the implicit block and all three trig derivatives. No new learner problem.','reader':'Codex author','date':'2026-11-18'},
 {'pdf_page':134,'printed_page':120,'chapter':4,'page_status':'prose only','item_ids':[],'continuation_item_ids':[],'source_evidence':ev(134),
 'non_item_content':'Learning-outcome checklist only; no new task, teaching figure, worked example or formula table. Chapter 5 starts on PDF135.','reader':'Codex author','date':'2026-11-18'}]
if __name__=='__main__':
    (W/'tools/textbook-r5/census-Goldie-C4-closing.json').write_text(json.dumps({'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
     'scope':'All reference blocks and closing outcome-only page, PDF133–134.','new_items':figures,'corrections':[],'pages':pages},ensure_ascii=False,indent=2)+'\n')
    print('12 reference blocks;',sum(len(r['mathematical_feature_review']['checks'])for r in figures),'formula checks; chapter boundary read')
