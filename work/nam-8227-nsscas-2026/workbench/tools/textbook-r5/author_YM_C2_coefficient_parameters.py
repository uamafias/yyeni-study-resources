"""YM100–101: chosen Laurent coefficients and parameter recovery.

Fixed-source author audit; independent acceptance remains pending.
"""
import json
import author_YM_C2_binomial_terms as prior
import author_YM_C2_opening as foundation
from author_YM_C2_binomial_terms import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra,BINOM,COEF,COMBINED,coefficient
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();foundation.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections;add=prior.add
add('Example',48,100,'Extract quadratic/cubic coefficients from(2−x)^6,then the cubic coefficient after multiplication by3x+1. Native stem confirms power6.',[
 coefficient('a-quadratic','(2-x)**6','x',2,'240',100),coefficient('a-cubic','(2-x)**6','x',3,'-160',100),coefficient('b-product-cubic','(3*x+1)*(2-x)**6','x',3,'560',100)],[COEF,COMBINED],'6')
r=add('Try-Now-48',1,100,'Find the coefficient ofx in a seventh-power Laurent binomial; select the exponent before its coefficient.',[
 coefficient('coefficient','(x+2/x**2)**7','x',1,'84')],[COEF],'7');r['scope_check']['basis']+=' Originalx≠0.'
r=add('Try-Now-48',2,100,'Find an x^9 coefficient where the two inner terms have exponents3and−2; solve the resulting exponent equation.',[
 coefficient('coefficient','(2*x**3-1/x**2)**8','x',9,'-1792')],[COEF],'8');r['scope_check']['basis']+=' Originalx≠0.'
p=v('b-k','solve(x*(-Rational(135,2))+2*Rational(135,4),x)[0]','1',597,'The source says there is NOx³term,meaning its coefficient is0. From independently derived quadratic/cubic coefficients135/4and−135/2,solve−135k/2+135/2=0,so k1.')
extra(p,'original-product-zero','expand((1+2*x)*(1-Rational(3,2)*x)**6).coeff(x,3)','0')
add('Try-Now-48',3,100,'Extract two coefficients,then determine a multiplier constant by requiring a connected cubic coefficient to vanish.',[
 coefficient('a-quadratic','(1-Rational(3,2)*x)**6','x',2,'Rational(135,4)'),coefficient('a-cubic','(1-Rational(3,2)*x)**6','x',3,'-Rational(135,2)'),p],[COEF,COMBINED],'6')
r=add('Try-Now-48',4,100,'Find a quadratic product coefficient from a Laurent sixth power and factor1+x²; both a quadratic and a constant contribution are needed.',[
 coefficient('coefficient','(1+x**2)*(x/2-4/x)**6','x',2,'-145')],[COMBINED],'6');r['scope_check']['basis']+=' Originalx≠0.'
p=v('k','Max(*solveset(binomial(7,4)*(2*x)**3-binomial(7,5)*(2*x)**2,x,domain=S.Reals))','Rational(3,10)',597,'The original k is explicitly NONZERO. Equating x^4/x^5 coefficients gives280k³=84k². Divide by nonzero k²,obtainingk3/10; exclude the algebraic zero root using the stated domain,not a positive-value assumption.')
extra(p,'original-coefficients-equal','expand((x+2*Rational(3,10))**7).coeff(x,4)-expand((x+2*Rational(3,10))**7).coeff(x,5)','0')
add('Try-Now-48',5,100,'Determine a nonzero binomial parameter by equating two chosen coefficients; the zero algebraic branch is explicitly excluded.',[p],[COMBINED],'7')
p=v('n','solve(3*x/2-2-7,x)[0]','6',101,'The linear coefficient of(3−2x)(1+x/2)^n is3n/2−2. Setting it to7 givesn6,a valid positive integer.')
p2=coefficient('quadratic-coefficient','(3-2*x)*(1+x/2)**6','x',2,'Rational(21,4)',101)
add('Example',49,101,'Recover a positive-integer binomial power from a linear product coefficient,then determine the quadratic coefficient.',[p,p2],[COMBINED],'Recoveredn6')
for number,constant,linear,nval,quadkey,expr,note in [
 (1,'5','69','7','406','(5-x)*(1+2*x)**7','Recovera,n,qfromconstant5,linear69andquadraticq in(a−x)(1+2x)^n.'),
 (2,'4','-95','8','984','(4+x)*(1-3*x)**8','Recovera,n,pfromconstant4,linear−95andquadraticp in(a+x)(1−3x)^n.')]:
 n_expr='solve(2*('+constant+')*x-1-('+linear+'),x)[0]'if number==1 else'solve(1-3*('+constant+')*x-('+linear+'),x)[0]'
 p=v('a','('+constant+')',constant,597,'The original factor multiplying the binomial has constant a; atx0 its constant coefficient is exactlya,so compare with the stated constant term.')
 p2=v('n',n_expr,nval,597,'Use the original linear coefficient after deriving a from the constant term. Retain the positive integer power and verify it in the original product.')
 p3=coefficient('q'if number==1 else'p',expr,'x',2,quadkey)
 extra(p3,'original-constant-and-linear','Tuple(expand('+expr+').coeff(x,0),expand('+expr+').coeff(x,1))','Tuple('+constant+','+linear+')')
 add('Try-Now-49',number,101,note,[p,p2,p3],[COMBINED],'Recoveredn'+nval)
p=v('n','Max(*solveset(x*(x-1)/2-66,x,domain=S.Reals))','12',597,'The linear coefficient nk=−9 ensures k≠0. Divide the stated quadratic relation by k² to obtain n(n−1)/2=66. Roots12and−11; only the positive integer12is admissible.')
p2=v('k','-9/12','-Rational(3,4)',597,'Use the same n12in nk=−9,givingk−3/4. Check both linear and quadratic source coefficients jointly.')
extra(p2,'original-source-coefficients','Tuple(expand((1-Rational(3,4)*x)**12).coeff(x,1),expand((1-Rational(3,4)*x)**12).coeff(x,2))','Tuple(-9,66*Rational(9,16))')
add('Try-Now-49',3,101,'Recover a positive-integer power and signed scale from two related coefficients,justifying division by the nonzero scale.',[p,p2],[COMBINED],'Recoveredn12')
refs=[
 (75,100,'Coefficient versus term and product-degree arrows','Example48 distinguishes240and−160fromtheirterms240x²and−160x³. Multiplication by3x+1 gives cubic coefficient3·240−160=560. These are chosen coefficients,not a requirement to display the entire product.',[COEF,COMBINED],'table',[('3*240-160','560')],'Example:48'),
 (76,100,'Vanishing coefficient and Laurent contribution hints','The printed hints say nox³term means0x³,and a target product coefficient may need a constant plus another degree from the Laurent factor. Preserve the original nonzero denominator conditions and sum every contributing power pair.',[COMBINED],'table',[('expand((1+x**2)*(x/2-4/x)**6).coeff(x,2)','-145')],None),
 (77,101,'Symbolic nC1 and nC2 derivation','The worked source derives nC1=n and nC2=n(n−1)/2 from factorial notation. It cross-refers to Example41(c),but the symbolic nC3 example is actually Example42(c); the displayed algebra is independently valid. Parenthetical coefficient-property knowledge is supporting evidence,not a new syllabus demand.',[COEF,COMBINED],'table',[('simplify(factorial(n)/(factorial(2)*factorial(n-2)))','n*(n-1)/2')],'Example:49'),
 (78,101,'Compare constant,linear and quadratic terms','Example49 labels the producta+7x+bx²+… and compares coefficients. A symbolic letter introduced for an answer coefficient is distinct from the binomial exponentn; a recovered n must be a positive integer.',[COMBINED],'table',[('expand((3-2*x)*(1+x/2)**6).coeff(x,2)','Rational(21,4)')],'Example:49')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[];f['item_kind']='teaching-figure'
pages=[]
for page,note in [(100,'EveryExample48andTry48Q1–5output and both coefficient/hint references is enumerated. The original positive outer powers coexist with Laurent inner terms; k≠0inQ5isexplicit.'),(101,'EveryExample49andTry49Q1–3output and symbolic-coefficient/comparison references is enumerated. All recovered n values are positive integers and coefficient pairs are checked jointly.')]:
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':note,'scope_screen':'Chosen coefficients,zero coefficients and parameter recovery are in scope. Original nonzero domains and the positive-integer outer-power condition are retained; coefficient-property teaching is supporting only.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-coefficient-parameters.json',{'scope':'Every100–101 original response and mathematical reference.','items':answers}),('census-YM-C2-coefficient-parameters.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete100–101 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
