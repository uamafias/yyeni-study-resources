"""YM92–95: truncated products, factorial notation and the general binomial term.

Unwired draft until the current double rebuild has finished. No runtime recipes.
"""
import json
import author_YM_C2_binomial_opening as prior
import author_YM_C2_opening as foundation
from author_YM_C2_binomial_opening import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra,BINOM,COEF,COMBINED
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();foundation.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
add=prior.add

def truncate(label,original,var,degree,key,kp=597):
 return v(label,'expand('+original+').series('+var+',0,'+str(degree+1)+').removeO()',key,kp,
  'Independently distribute the original finite product, then retain ascending powers through degree '+str(degree)+'. Higher powers remain in the full expression; an ellipsis is part of the truncated response, not a claim they are zero.')

def coefficient(label,original,var,degree,key,kp=597):
 return v(label,'expand('+original+').coeff('+var+','+str(degree)+')',key,kp,
  'Multiply the ORIGINAL factors independently and extract the requested coefficient. As an alternative method, combine every pair of factor degrees that adds to '+str(degree)+'. Distinguish a coefficient from the term containing the variable power.')

add('Try-Now-39',1,92,'Expand (1+4y)^6 through y², then extract the y² coefficient of the connected product (1−5y)(1+4y)^6.',[
 truncate('a','(1+4*y)**6','y',2,'1+24*y+240*y**2'),coefficient('b','(1-5*y)*(1+4*y)**6','y',2,'120')],[BINOM,COMBINED],'6')
add('Try-Now-39',2,92,'Expand (1−3a)^5 through a², then combine it with (1+4a)^2 to find a chosen product coefficient.',[
 truncate('a','(1-3*a)**5','a',2,'1-15*a+90*a**2'),coefficient('b','(1+4*a)**2*(1-3*a)**5','a',2,'-14')],[BINOM,COMBINED],'5,2')
add('Try-Now-39',3,92,'Give three ascending-power expansions through b²: each original factor separately and then their product.',[
 truncate('a','(1-2*b)**3','b',2,'1-6*b+12*b**2'),truncate('b','(3+b)**5','b',2,'243+405*b+270*b**2'),truncate('c','(1-2*b)**3*(3+b)**5','b',2,'243-1053*b+756*b**2')],[BINOM,COMBINED],'3,5')
add('Try-Now-39',4,92,'Expand (1−y/2)^5 through y², then find a LINEAR coefficient in a connected product; do not default to degree2.',[
 truncate('a','(1-y/2)**5','y',2,'1-Rational(5,2)*y+Rational(5,2)*y**2'),coefficient('b','(1+6*y)**2*(1-y/2)**5','y',1,'Rational(19,2)')],[BINOM,COMBINED],'5,2')
r=add('Example',40,92,'Rewrite the polynomial base 1+2x−3x² as 1+x(2−3x), then expand its sixth power only through x³.',[
 truncate('through-x-cubed','(1+2*x-3*x**2)**6','x',3,'1+12*x+42*x**2-20*x**3',92)],[BINOM],'6')
r['source_interpretation']='The final requested expansion through x³ is correct. The working displays −585x⁴ after retaining only the first four outer-binomial terms; it is a partial higher-degree contribution, not the coefficient in the full polynomial. The actual full x⁴ coefficient is −345. Do not reuse an intermediate beyond the stated truncation order as a complete coefficient.'
extra(r['subparts'][0],'full-fourth-degree-coefficient','expand((1+2*x-3*x**2)**6).coeff(x,4)','-345')
add('Try-Now-40',1,92,'Expand the sixth power of a quadratic base through y³, collecting contributions by total degree.',[
 truncate('through-y-cubed','(1+y-2*y**2)**6','y',3,'1+6*y+3*y**2-40*y**3')],[BINOM],'6')
add('Try-Now-40',2,92,'Expand two different quadratic bases to prescribed positive-integer powers, retaining terms only through x³.',[
 truncate('a','(1-x-x**2)**4','x',3,'1-4*x+2*x**2+8*x**3'),truncate('b','(1+3*x-x**2)**5','x',3,'1+15*x+85*x**2+210*x**3')],[BINOM],'4,5')

def notation(kind,n,page,note,parts,domain):
 r=foundation.add(kind,n,page,note,parts,[])
 corrections.extend(foundation.corrections[-1:])
 r['teaches_8227_demand_ids']=[BINOM,COEF]
 r['mapping_rationale']='The syllabus explicitly requires knowledge of factorial and nCr notation in objective M1:T2:O01. These drills assess that notation facet, not a full binomial expansion or extraction of a variable term. Keep the objective connection through teaching links without falsely recording the entire expansion demand as directly assessed.'
 r['evidence_role']='prerequisite/supporting notation facet explicitly required by the parent binomial objective'
 r['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'not applicable','quoted_value':domain,'reason':'These are factorial/binomial-coefficient notation calculations, not outer binomial expansions. Their integer factorial domains are recorded separately; no unrelated positive-outer-power decision is manufactured.'}]
 r['precision_angle_check']={'source':'Exact integer or symbolic values; no rounding and no angle quantities.','comparison':'Factorial inputs are nonnegative integers. Cancel only existing nonzero factorials; symbolic nCr formulas retain their stated integer domains.'}
 return r
notation('Example',41,93,'Evaluate 6! and 12!/10! by expanding/cancelling integer products; source calculator keystrokes are an alternative.',[
 v('a','6*5*4*3*2*1','720',93,'Independently multiply the six original positive integers, rather than using the printed answer as an operand.'),v('b','12*11','132',93,'Cancel the common nonzero 10! factor in the original factorial quotient. The remaining product is12·11.')],'6!,12!,10!: positive integer arguments')
p=v('c','11*10*9','20',597,'The original 11!/8! cancels to11·10·9=990. Native key597 prints20, crossed out by handwriting990. The handwritten correction is not the publisher key; the exact product independently establishes990.');p['author_expected_normalised']='990'
notation('Try-Now',41,93,'Evaluate three factorial expressions. The third typeset key is wrong; retain the handwritten correction only as a separately observed annotation.',[
 v('a','9*8*7*6*5*4*3*2*1','362880',597,'Expand the original9! into its full positive-integer product.'),v('b','5*4','20',597,'Cancel3! in5!/3!, leaving5·4.'),p],'9!,5!,3!,11!,8!: positive integer arguments')
notation('Example',42,94,'Evaluate two numeric nCr expressions and simplify nC3 symbolically, keeping the zero-factorial and integer-domain conventions.',[
 v('a','7*6*5/(3*2*1)','35',94,'Original7C3 reduces to7·6·5/(3·2·1).'),v('b','1','1',94,'11C11=11!/(11!0!)=1, since0!=1; the surviving unit value is not0.'),v('c','simplify(factorial(n)/(factorial(3)*factorial(n-3)))','n*(n-1)*(n-2)/6',94,'For integern≥3, cancel(n−3)! fromn!/[3!(n−3)!], yielding n(n−1)(n−2)/6.')],'7C3,11C11; symbolic nC3 has integer n≥3')
notation('Try-Now',42,94,'Evaluate 8C5,10C10,15C0 and simplify nC5; symbolic cancellation requires integer n≥5.',[
 v('a','8*7*6/(3*2*1)','56',597,'8C5=8C3; expand factorials to obtain8·7·6/6.'),v('b','1','1',597,'Selecting all10 positions has one choice;10! cancels and0!=1.'),v('c','1','1',597,'Selecting zero positions has one choice;15! cancels and0!=1.'),v('d','simplify(factorial(n)/(factorial(5)*factorial(n-5)))','n*(n-1)*(n-2)*(n-3)*(n-4)/120',597,'For integern≥5, cancel(n−5)! and compute5!=120. The formula is exact and does not require a decimal approximation.')],'8C5,10C10,15C0; symbolic nC5 has integer n≥5')
refs=[
 (56,92,'Quadratic-base binomial substitution and truncation','Example40 groups the base as1+x(2−3x). To obtain powers through x³, only outer terms of orders0..3 are needed. Higher-degree fragments in that working are not complete higher-degree coefficients: displayed−585x⁴ becomes−345x⁴ once the order4 outer contribution240x⁴ is included.',[BINOM,COMBINED],'table',[('expand((1+2*x-3*x**2)**6).coeff(x,4)','-345')],'Example:40'),
 (57,93,'Factorial definition and zero/one boundary','The boxed definition uses n!=n(n−1)…1 for positive integern and explicitly states0!=1 and1!=1. Factorial notation is syllabus-required; gamma-function extensions are not implied.',[BINOM,COEF],'table',[('Tuple(factorial(0),factorial(1),factorial(4),factorial(5))','Tuple(1,1,24,120)')],None),
 (58,93,'Factorial calculator sequence','Example41 shows calculator factorial entry as an alternative to product expansion/cancellation. Exact integer output and correct argument selection matter; a keypress diagram is not a mathematical proof.',[BINOM,COEF],'table',[('12*11','132')],'Example:41'),
 (59,93,'Factorial representation of fifth-power coefficients','The expanded(x+y)^5 has coefficients1,5,10,10,5,1. The source illustrates1=5!/[0!5!],5=5!/[1!4!] and10=5!/[2!3!]. The accompanying0!/1! reminder supplies boundary notation, not another task.',[COEF],'table',[('Tuple(factorial(5)/(factorial(0)*factorial(5)),factorial(5)/(factorial(1)*factorial(4)),factorial(5)/(factorial(2)*factorial(3)))','Tuple(1,5,10)')],None),
 (60,94,'nCr definition and position alignment','The boxed coefficient is n!/[r!(n−r)!] for integer0≤r≤n. rcounts the exponent/zero-based selection; its term position is r+1. In(x+y)^5 the fourth term corresponds tor3, notr4.',[COEF],'table',[('binomial(5,3)','10')],None),
 (61,94,'Fourth-term coefficient and calculator nCr reminder','Example42 notes7C3 is the coefficient of the fourth generic term of(x+y)^7; the exact coefficient is35. Calculator nCr is an alternative calculation, not permission to shift the term index.',[COEF],'table',[('binomial(7,3)','35')],'Example:42'),
 (62,94,'Equal-index coefficient boundary','The source explains nCn=1 through0!=1. This is a supporting coefficient property; the syllabus says detailed properties of coefficients are not required.',[COEF],'table',[('factorial(11)/(factorial(11)*factorial(0))','1')],'Example:42'),
 (63,95,'Pascal coefficients paired with nCr notation','The table shows rows0..6 with numeric coefficients and matching nCr symbols, and n+1 generic terms. Keep the numeric value separate from its symbolic label and from the variable term it will multiply.',[BINOM,COEF],'table',[('Tuple(binomial(6,0),binomial(6,1),binomial(6,2),binomial(6,3),binomial(6,4),binomial(6,5),binomial(6,6))','Tuple(1,6,15,20,15,6,1)')],None),
 (64,95,'General finite binomial theorem','For positive integern, (a+b)^n=sum of nCr·a^(n−r)b^r forr0..n. This is a finite polynomial identity; no|b/a|<1 restriction is needed, and a0 must not be lost by dividing througha.',[BINOM],'table',[('expand((a+b)**3)','a**3+3*a**2*b+3*a*b**2+b**3')],None),
 (65,95,'First/last coefficient and general term','The reminders give nC0=nCn=1 and T_(r+1)=nCr·a^(n−r)b^r. Original n is a positive integer andr is integer0..n; the coefficient is only one factor of the term.',[BINOM,COEF],'table',[('Tuple(binomial(5,0),binomial(5,5))','Tuple(1,1)')],None),
 (66,95,'Unit-first-term special binomial','The special case(1+x)^n uses the same finite coefficients for positive integern. Unlike an infinite rational-power binomial series, it does not impose|x|<1; outside fractional-power extensions are not licensed.',[BINOM,COEF],'table',[('expand((1+x)**4)','1+4*x+6*x**2+4*x**3+x**4')],None)]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[];f['item_kind']='teaching-figure'
notes={92:'Every Try39Q1–4,Example40 andTry40Q1/2 response and the quadratic-base truncation reference is enumerated. The linear coefficient inTry39Q4(b) remains degree1. Final requested expansions are checked separately from incomplete higher-degree working fragments.',93:'The factorial box,calculator illustration,Example41,Try41 and fifth-power coefficient/factorial references are enumerated. Native typeset Try41(c) key20 is distinguished from handwritten990.',94:'The nCr definition,Example42,Try42,position/calculator reminder and equal-index boundary note are enumerated. Symbolic factorial domains and the difference betweenr andterm positionr+1 are explicit.',95:'All four mathematical reference blocks—Pascal/nCr table,general finite theorem,endpoint/general-term note and(1+x)^n special case—are enumerated. There is no new learner task on this page.'}
pages=[]
for page in range(92,96):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All tasks and mathematical teaching references are enumerated. Full/truncated/product-coefficient outputs are distinguished from required supporting factorial/nCr notation. No infinite-binomial extension is inferred.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-binomial-notation.json',{'scope':'Every92–95 task and mathematical reference.','items':answers}),('census-YM-C2-binomial-notation.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete92–95 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
