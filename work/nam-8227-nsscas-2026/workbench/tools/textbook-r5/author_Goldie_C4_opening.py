"""Fixed-source product/quotient opening, Goldie PDF97–101; author evidence."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02';CHAIN='8227:2020:M1:T8:O02:D02'
POWER='8227:2020:M1:T8:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01'
def ev(page):
    name='Goldie-key-C3-341'if page==342 else'Goldie-C3-boundary-94'if page==97 else'Goldie-C4-98'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,new_item=False,exponents=None):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Distinguish requested product/quotient derivatives and explicit method instructions from unprompted first-principles teaching. The latter is outside the required proof scope(LIMIT03),with only the resulting rule retained as supporting evidence. No implicit/parametric geometric demand is attached to an explicit function.',
      'representation':'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within'if exponents else'not applicable','quoted_value':', '.join(exponents)if exponents else note,
        'reason':'All actual powers are rational; any denominator/root domain is preserved.'if exponents else'No learner power-rule derivative is requested.'},
       {'rule_id':'8227:LIMIT04','status':'within'if PRODUCT in direct or QUOTIENT in direct else'not applicable','quoted_value':note,
        'reason':'Product/quotient rules belong toMathematics2,not an inventedMathematics1requirement.'if PRODUCT in direct or QUOTIENT in direct else'No assessed use of either rule is claimed for this exposition/context prompt.'},
       {'rule_id':'8227:LIMIT03','status':'outside'if kind=='Worked-derivation'else'not applicable','quoted_value':note,
        'reason':'The first-principles proof is optional source exposition outside the required8227demand; the rule itself remains useful supporting evidence.'if kind=='Worked-derivation'else'No first-principles proof is required in this task.'}],
      'exam_style':False,'exam_style_basis':'Ordinary chapter opening,Example,Activity orExercise4A; no examination attribution or exam-style heading.',
      'precision_angle_check':{'source':'Exact symbolic derivatives; no angle or decimal rounding in this segment.',
       'comparison':'Keep algebraically equivalent answers; source advice to factor is teaching guidance,not an NSSCAS award rule. Explicit using-product/quotient wording still matters.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting teaching exposition or context; no directly assessed calculus coverage'
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'worked-derivation','exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,
      'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'teaches_8227_demand_ids':components or direct,
      'representation':'text','source_evidence':ev(page),'evidence_role':row.get('evidence_role','directly related assessed practice'),
      'answer_key':{'available':True,'pdf_pages':[page],'printed_pages':[page-14],'locator':'Inline first-principles explanatory derivation'},'learner_display':False})
    return row

def derivative(label,original,key,kp,domain='All real x.'):
    p=value(label,f'diff({original},x)',key,kp,
      'Differentiate the original fixed-source function independently with exact symbolic algebra. Compare the separately transcribed printed derivative,retaining its original real domain. A factored or expanded equivalent is accepted; explicit source method instructions are recorded separately.')
    p['original_function']=original;p['original_common_domain']=domain;return p
p=reasoning('contexts','Possible examples include the velocity of a sinusoidally displaced oscillator,and the instantaneous rate of exponential decay or growth.',
 'For s(t)=A*sin(ωt),the derivative isAωcos(ωt);forN(t)=N0exp(kt),it iskN0exp(kt). These are concrete non-polynomial contexts,not a newly asked derivative calculation. The key gives broad waves/decay/population examples; its phrase amplitude of waves is not treated as a claim that a constant amplitude requires differentiation.',342,'matches')
p['additional_operations']={'sinusoidal_displacement_example':{'kind':'identity','operands':['diff(a*sin(b*x),x)']},
 'exponential_rate_example':{'kind':'identity','operands':['diff(a*exp(b*x),x)']}}
add('Prompt',1,97,'Suggest other contexts where differentiating functions other than polynomials is useful. This open contextual brainstorm doesnot ask the learner to perform a derivative.',[p],[],[ELEMENTARY])
p=reasoning('product-rule-proof','For differentiableu,v,(uv)′=vu′+uv′.',
 'The finite increment isδy=vδu+uδv+δuδv. Divide byδx. Asδx→0,differentiability givesδu/δx→u′,δv/δx→v′andδu→0,so the last termδu(δv/δx)vanishes. Thus(uv)′=vu′+uv′. This is supporting exposition;8227doesnot require this first-principles proof.',99,'matches')
p['additional_operations']={'finite_increment_identity':{'kind':'identity','operands':['expand((b+a)*(c+p)-b*c-(c*a+b*p+a*p))']}}
row=add('Worked-derivation',1,98,'Unprompted first-principles derivation of the product rule startsPDF98andconcludes99. Keep the formula asMathematics2support; the proof itself is not required underLIMIT03.',[p],[],[PRODUCT],True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[99]})
add('Example',1,99,'Finddy/dxfor(2x+3)(x²−5)explicitly using the product rule. The following note also verifies by expanding to a cubic;that alternative doesnot remove the source method instruction.',
 [derivative('derivative','(2*x+3)*(x**2-5)','2*(3*x**2+3*x-5)',99)], [PRODUCT],[POWER],exponents=['x²','linear×quadratic'])
add('Example',2,99,'Differentiate20x(x−1)^6in the product-rule section; solution uses product plus chain rule and factors20(x−1)^5(7x−1). Expansion is mathematically valid because the function is a polynomial; no stationary point is actually requested.',
 [derivative('derivative','20*x*(x-1)**6','20*(x-1)**5*(7*x-1)',99)], [PRODUCT,CHAIN],[POWER],exponents=['(x−1)^6'])
p=reasoning('quotient-rule-proof','For differentiableu,vandv≠0,(u/v)′=(vu′−uv′)/v².',
 'The finite difference is[(u+δu)/(v+δv)]−u/v=(vδu−uδv)/(v(v+δv)),when both denominators are nonzero. Divide byδxandtake the limit;continuity givesv+δv→v≠0,andthe numerator difference quotient tendsvu′−uv′. This optional proof is not an8227assessed requirement underLIMIT03.',100,'matches')
p['additional_operations']={'finite_difference_identity':{'kind':'identity','operands':['cancel((b+a)/(c+p)-b/c-(c*a-b*p)/(c*(c+p)))']}}
add('Worked-derivation',2,100,'Unprompted quotient-rule derivation from finite increments; it requires nonzero denominators and differentiability. The resulting quotient rule is inMathematics2; the first-principles proof is outside requiredLIMIT03scope.',[p],[],[QUOTIENT],True)
p=derivative('verification','x**10/x**7','3*x**2',342,'x≠0; simplification to x³doesnot extend the original quotient domain.')
p['additional_comparisons']=[{'label':'explicit quotient-rule calculation','operation':{'kind':'identity','operands':['(x**7*diff(x**10,x)-x**10*diff(x**7,x))/(x**7)**2']},'printed_key_normalised':'3*x**2'}]
add('Activity',1,101,'Verify the quotient rule foru=x^10,v=x^7by comparing it with the simplified powerx³. Keepx≠0even though the simplified power has a larger domain.',[p],[QUOTIENT],[POWER],exponents=['x^10','x^7'])
add('Example',3,101,'Finddy/dxfor(3x+1)/(x−2)explicitly using the quotient rule;retainx≠2. Constant numerator−7in the derivative comes from cancellation,not differentiating numerator and denominator separately.',
 [derivative('derivative','(3*x+1)/(x-2)','-7/(x-2)**2',101,'x≠2.')],[QUOTIENT],[POWER],exponents=['(x−2)^−1'])
add('Example',4,101,'Finddy/dxfor(x²+1)/(3x−1)using the quotient rule. Keepx≠1/3andthe squared denominator; simplify numerator to3x²−2x−3.',
 [derivative('derivative','(x**2+1)/(3*x-1)','(3*x**2-2*x-3)/(3*x-1)**2',101,'x≠1/3.')],[QUOTIENT],[POWER],exponents=['x²','(3x−1)^−1'])
parts=[]
for label,original,key,domain in[
 ('i','(x**2-1)*(x**3+3)','x*(5*x**3-3*x+6)','All real x.'),
 ('ii','x**5*(3*x**2+4*x-7)','x**4*(21*x**2+24*x-35)','All real x.'),
 ('iii','x**2*(2*x+1)**4','2*x*(6*x+1)*(2*x+1)**3','All real x.'),
 ('iv','2*x/(3*x-1)','-2/(3*x-1)**2','x≠1/3.'),
 ('v','x**3/(x**2+1)','x**2*(x**2+3)/(x**2+1)**2','All real x; denominatorx²+1>0.'),
 ('vi','(2*x+1)**2*(3*x**2-4)','2*(2*x+1)*(12*x**2+3*x-8)','All real x.'),
 ('vii','(2*x-3)/(2*x**2+1)','2*(1+6*x-2*x**2)/(2*x**2+1)**2','All real x; denominator2x²+1>0.'),
 ('viii','(x-2)/(x+3)**2','(7-x)/(x+3)**3','x≠−3.'),
 ('ix','(x+1)*sqrt(x-1)','(3*x-1)/(2*sqrt(x-1))','Original functionx≥1; finite derivative formula requiresx>1.')]:parts.append(derivative(label,original,key,342,domain))
add('Exercise-4A',1,101,'Nine derivatives explicitly using product or quotient rule:(x²−1)(x³+3);x^5(3x²+4x−7);x²(2x+1)^4;2x/(3x−1);x³/(x²+1);(2x+1)²(3x²−4);(2x−3)/(2x²+1);(x−2)/(x+3)²;(x+1)√(x−1). Domains and the last square-root endpoint are retained.',parts,[PRODUCT,QUOTIENT],[CHAIN,POWER],exponents=['2','3','5','4','−1','−2','1/2'])

figures=[]
for n,page,label,note,rep,teaches,parent,method in[
 (1,97,'Figure4.1 displacement–time context graph','Qualitative sinusoidal displacement against time for an oscillator;the unscaled curve begins above zero,falls through zero to a minimum,andreturns. No numeric amplitude/period/phase may be read from its unlabelled scale. The swing photograph is context,not metric data.','graph',[ELEMENTARY],'Prompt:1','Use the qualitative sinusoidal shape to motivate velocity/acceleration as derivatives. No quantitative source equation or measurement is invented.'),
 (2,98,'Figure4.2 product polynomial sketch','Giveny=20x(x−1)^6withx-intercepts0(simple crossing)and1(order6touching);a local maximumatx=1/7andflatlocal minimumat1. Odd degree7,positiveleadingcoefficient. This given sketch is reused byExample4.2; no learner sketch is requested there.','graph',[PRODUCT,CHAIN],'Example:2','Differentiate original20x(x−1)^6to20(x−1)^5(7x−1),then use signs:positive before1/7,negative between1/7and1,positive after1. Zero multiplicities determine crossing/touching; source sketch is qualitative,not scaled.'),
 (3,98,'Product-rule formula reference','y=uv⇒dy/dx=u*dv/dx+v*du/dx,withu,vfunctions ofx. Both terms are required. The following first-principles derivation is optional source exposition,not additional assessed scope.','table',[PRODUCT],'Worked-derivation:1','The linked finite-increment proof independently derives the formula;Example4.1checks a concrete polynomial by direct derivative and expansion.'),
 (4,100,'Quotient-rule formula reference','y=u/v⇒dy/dx=(v*du/dx−u*dv/dx)/v²,wherev≠0. The order of the subtraction and the square of the original denominator matter.','table',[QUOTIENT],'Worked-derivation:2','The linked exact finite-difference identity and limiting argument derive the formula under differentiability/nonzero-denominator assumptions;Activity4.1andExamples4.3/4.4check concrete cases.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure'if n==2 else'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,'source_evidence':ev(page),
      'parent_item_id':'8227:TB:Goldie:C4:'+parent,'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT03','status':'not applicable','quoted_value':note,'reason':'The representation is formula/context support; no first-principles proof is imposed as a learner response.'}],
      'value_level_scope_review_status_r5':'author source function/rule/domain read2026-11-18; independent acceptance pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook formula/given-graph support; no examination-frequency or official-marking inference.'},
      'mathematical_feature_review':{'status':'author rendered features and linked independent derivation; independent acceptance pending','method':method}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'All numbered tasks,context prompt,headingless first-principles expositions and mathematical reference/given representations are recorded. Source factorisation advice on100is teaching guidance attached to the derivative tasks,not an official marking condition. Decorative photograph/quote/handwriting are not new mathematical tasks.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(97,102)]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-opening.json',{'scope':'All tasks/expositionsPDF97–101; fixed-source derivatives only.','items':answers}),
     ('census-Goldie-C4-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'PDF97–101every context,example,activity,exposition,exercise andmathematical representation. First-principles proofs are optional support,not required scope.',
      'new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
