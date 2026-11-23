"""YM96–99: prescribed order, Laurent terms and connected product coefficients."""
import json
import author_YM_C2_binomial_notation as prior
import author_YM_C2_opening as foundation
from author_YM_C2_binomial_notation import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra,BINOM,COEF,COMBINED,truncate,coefficient
from author_YM_C2_binomial_opening import poly
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();foundation.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections;add=prior.add

def descending(label,original,var,powers,key,kp):
 expr='+'.join('expand('+original+').coeff('+var+','+str(p)+')*'+var+'**('+str(p)+')'for p in powers)
 return v(label,expr,key,kp,'Independently expand the original finite product and select the first four NONZERO terms in the stated descending variable order. The degrees here are '+','.join(map(str,powers))+'. Retain an ellipsis for all remaining terms; selecting powers by printed factor order alone can reverse the requested order.')

add('Example',43,96,'Find the first four terms of(a+2b)^8 in descending powers ofa,using correct term position r+1.',[
 descending('first-four','(a+2*b)**8','a',[8,7,6,5],'a**8+16*a**7*b+112*a**6*b**2+448*a**5*b**3',96)],[BINOM],'8')
add('Try-Now',43,97,'Give first four descending-a terms for two scaled binomials,including a ninth power with first term3a.',[
 descending('a','(a+2)**12','a',[12,11,10,9],'a**12+24*a**11+264*a**10+1760*a**9',597),descending('b','(3*a+b)**9','a',[9,8,7,6],'19683*a**9+59049*a**8*b+78732*a**7*b**2+61236*a**6*b**3',597)],[BINOM],'12,9')
add('Example',44,97,'Find four ascending-x terms of a simple signed binomial and a related quadratic-base ninth power.',[
 truncate('a','(1-x)**9','x',3,'1-9*x+36*x**2-84*x**3',97),truncate('b','(1-x+2*x**2)**9','x',3,'1-9*x+54*x**2-228*x**3',97)],[BINOM],'9')
add('Try-Now',44,97,'Give first four ascending-x terms of two tenth powers; quadratic terms change the collected coefficients.',[
 truncate('a','(1-2*x)**10','x',3,'1-20*x+180*x**2-960*x**3'),truncate('b','(1-2*x-4*x**2)**10','x',3,'1-20*x+140*x**2-240*x**3')],[BINOM],'10')
add('Example',45,97,'Expand(3x−y/2)^4 fully,with exact fractional coefficients and signs.',[
 poly('expansion','(3*x-y/2)**4','81*x**4-54*x**3*y+Rational(27,2)*x**2*y**2-Rational(3,2)*x*y**3+y**4/16',97)],[BINOM],'4')
add('Try-Now',45,98,'Expand four positive-integer binomials with scaled and fractional terms,retaining exact coefficients.',[
 poly('a','(2*x+3)**5','32*x**5+240*x**4+720*x**3+1080*x**2+810*x+243',597),poly('b','(x-3*y)**4','x**4-12*x**3*y+54*x**2*y**2-108*x*y**3+81*y**4',597),poly('c','(2+b/2)**6','64+96*b+60*b**2+20*b**3+Rational(15,4)*b**4+Rational(3,8)*b**5+b**6/64',597),poly('d','(3*a-b/4)**4','81*a**4-27*a**3*b+Rational(27,8)*a**2*b**2-Rational(3,16)*a*b**3+b**4/256',597)],[BINOM],'5,4,6,4')
ps=[]
for label,power,key in [('a-sixth',15,'-3075072*x**15'),('b-independent',0,'96096'),('c-containing-x-six',6,'823680*x**6')]:
 p=v(label,'expand((2*x**2-1/x)**15).coeff(x,'+str(power)+')*x**('+str(power)+')',key,98,'Originalx≠0. The generic term has x-power30−3r for r0..15,so descending powers agree with factor-choice order. For the sixth term use r5; for the constant use r10; for x^6 use r8. Independently expand the original Laurent polynomial and extract that entire term,not only its coefficient.')
 extra(p,'selected-r-index','solve(30-3*x-'+str(power)+',x)[0]',{'a-sixth':'5','b-independent':'10','c-containing-x-six':'8'}[label]);ps.append(p)
r=add('Example',46,98,'Extract a sixth term,a constant and an x^6 term from a Laurent binomial using exponent equations and descending order.',ps,[COEF],'15');r['scope_check']['basis']+=' Original1/x requires x≠0.'
p=v('a-fourth','expand((a-3/a**2)**12).coeff(a,3)*a**3','-5940*a**3',597,'Originala≠0. Its descending exponents are12−3r,r0..12. The fourth term uses r3 and is−5940a³.')
p2=reasoning('b-variable-mismatch','Intended constant in a:40095. Literally every term is independent of x,so the printed prompt does not identify a unique term.',
 'The original expression uses only a,but the source asks for the term independent of x. Its key40095 corresponds to independence of a:12−3r=0 givesr4. Retain the typo and both readings; do not silently replace x by a in an original. With a held fixed,the derivative of the entire original with respect to x is0.',597,'key incomplete')
extra(p2,'intended-a-constant','expand((a-3/a**2)**12).coeff(a,0)','40095');extra(p2,'literal-x-independence','diff((a-3/a**2)**12,x)','0')
r=add('Try-Now-46',1,99,'Extract the fourth descending-a term,then record the wrong-variable ambiguity in the requested independent term.',[p,p2],[COEF],'12');r['scope_check']['basis']+=' Originala≠0; the second prompt names x although the expression uses a.'
r['source_interpretation']='Key40095 is the intended a-constant answer. Literally every displayed term is independent of x; the source wording is ambiguous and is not silently repaired.'
p=v('a-sixth-descending','expand((1/(2*x**2)-x)**9).coeff(x,-6)*x**(-6)','-Rational(63,8)/x**3',597,'Originalx≠0. Reorder by DESCENDING x as requested: powers9,6,3,0,−3,−6,−9,−12,−15,−18. The sixth term is63/(16x^6). The printed key−63/(8x³) is fifth in that descending order; it is sixth only in the opposite,first-factor order.')
p['author_expected_normalised']='Rational(63,16)/x**6'
extra(p,'full-descending-polynomial','expand((1/(2*x**2)-x)**9-(-x**9+Rational(9,2)*x**6-9*x**3+Rational(21,2)-Rational(63,8)/x**3+Rational(63,16)/x**6-Rational(21,16)/x**9+Rational(9,32)/x**12-Rational(9,256)/x**15+Rational(1,512)/x**18))','0')
p2=v('b-constant','expand((1/(2*x**2)-x)**9).coeff(x,0)','Rational(21,2)',597,'The exponent equation−18+3r=0 givesr6 in the original factor-choice order. Independently extract the constant21/2; constant selection does not depend on ascending/descending ordering.')
p3=reasoning('c-term-x-six','(9/2)x^6.','The question explicitly asks for the term containingx^6,but the answer section proceeds fromTry46Q2(b)directlytoTry47. In the original factor-choice order solve−18+3r=6,givingr8,and term9·(1/2)·x^6=(9/2)x^6. This is author-derived with no separate key.',597,'no key')
extra(p3,'original-term','expand((1/(2*x**2)-x)**9).coeff(x,6)*x**6','Rational(9,2)*x**6')
r=add('Try-Now-46',2,99,'Extract terms from a Laurent binomial whose original factor order ascends in x,while the prompt requires descending order. The third key is absent.',[p,p2,p3],[COEF],'9');r['scope_check']['basis']+=' Original1/(2x²) requires x≠0.'
p3.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[597],key_evidence=ev(597))
add('Example',47,99,'Obtain a three-term ascending expansion,then use every contributing pair to find a degree2 product coefficient.',[
 truncate('a','(2-a/4)**10','a',2,'1024-1280*a+720*a**2',99),coefficient('b','(1+2*a-3*a**2)*(2-a/4)**10','a',2,'-4912',99)],[BINOM,COMBINED],'10')
p=truncate('a-four-nonzero-terms','(2+y**2/4)**8','y',6,'256+256*y**2+112*y**4+28*y**6')
p['method']+=' Only even degrees occur:the first four nonzero terms have degrees0,2,4,6,not0,1,2,3.'
p2=coefficient('b-product-coefficient','(2-3/y**2)*(2+y**2/4)**8','y',4,'140')
p2['method']+=' Originaly≠0. The pole term−3/y² shifts the y^6 contribution into degree4,so a truncation only through y^4 would lose a required contribution.'
r=add('Try-Now-47',1,99,'Find four nonzero even-power terms,then a product coefficient with a reciprocal factor that needs the higher y^6 term.',[p,p2],[BINOM,COMBINED],'8');r['scope_check']['basis']+=' Part(b)hasy≠0;the factor−3/y² requires retaining the first expansion through degree6.'
add('Try-Now-47',2,99,'Expand two quartics in ascending powers of b,then find a cubic product coefficient.',[
 poly('a','(2-b)**4','16-32*b+24*b**2-8*b**3+b**4',597),poly('b','(1+2*b)**4','1+8*b+24*b**2+32*b**3+16*b**4',597),coefficient('c','(2-b)**4*(1+2*b)**4','b',3,'-72')],[BINOM,COMBINED],'4')
refs=[
 (67,96,'Four-term calculation and calculator alignment','Example43 tabulates r0,1,2,3 against term positions1,2,3,4 for(a+2b)^8,and calculator nCr values1,8,28,56. Powers of2 then change the full coefficients to1,16,112,448. r and term position are different.',[BINOM,COEF],'table',[('Tuple(binomial(8,0),binomial(8,1)*2,binomial(8,2)*2**2,binomial(8,3)*2**3)','Tuple(1,16,112,448)')],'Example:43'),
 (68,97,'Related quadratic-base expansion substitution','Example44 uses(1−x)^9 to expand[1−x(1−2x)]^9 through degree3. Collect contributions by total x-degree; a term index in the outer expansion is not the final power of x when the substituted term contains x.',[BINOM],'table',[('expand((1-x+2*x**2)**9).series(x,0,4).removeO()','1-9*x+54*x**2-228*x**3')],'Example:44'),
 (69,97,'Signed fractional binomial worked sequence','Example45 writes the second term as−y/2 before raising its powers,then keeps exact fractions. The full fourth power contains five generic terms; signs alternate because odd powers of the negative second term stay negative.',[BINOM],'table',[('expand((3*x-y/2)**4).coeff(x,1).coeff(y,3)','-Rational(3,2)')],'Example:45'),
 (70,98,'Sixth term uses r5','For(2x²−1/x)^15,the table-free general-term step setsr+1=6,so r5. The resulting full term is−3075072x^15,not the scalar coefficient alone. Originalx≠0 remains necessary despite positive outer power15.',[COEF],'table',[('binomial(15,5)*2**10*(-1)**5','-3075072')],'Example:46'),
 (71,98,'Constant term by exponent equation','The same source derives x-power30−3r. Setting it to0 selectsr10;the constant is96096. A requested independent term is found by zero VARIABLE exponent,not zero binomial index.',[COEF],'table',[('binomial(15,10)*2**5','96096')],'Example:46'),
 (72,98,'Requested x-six term by exponent equation','Setting30−3r=6 givesr8 andterm823680x^6. Extract the entire term when asked for a term; the answer to a coefficient question would instead be823680.',[COEF],'table',[('binomial(15,8)*2**7','823680')],'Example:46'),
 (73,99,'Product coefficient power-pair arrows','Example47 selects720,2·(−1280),and−3·1024,all degree2 contributions; their sum is−4912. Arrows connect source-factor degrees0+2,1+1 and2+0,not merely adjacent printed positions.',[COMBINED],'table',[('720+2*(-1280)-3*1024','-4912')],'Example:47'),
]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[];f['item_kind']='teaching-figure'
notes={96:'Example43’s entire four-term task and calculation/calculator table are enumerated. No extra learner prompt is hidden in the worked table.',97:'Every Try43,Example44,Try44 andExample45 response and two worked-reference sequences are enumerated. Full/first-four expansions and requested variable order are preserved.',98:'Every Try45 andExample46 response,term-position note,zero-exponent step and chosen-power step are enumerated. Laurent denominators require x≠0.',99:'Every Try46Q1/2,Example47 andTry47Q1/2 response is enumerated. Wrong independent-variable wording,incorrect descending-order key and absent Q2(c)key are explicit. Negative-power factors affect necessary truncation depth.'}
pages=[]
for page in range(96,100):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Every requested expansion,chosen term and connected coefficient is recorded. Positive outer integer powers remain in scope despite rational inner terms; original nonzero denominators and requested term ordering remain mandatory.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-binomial-terms.json',{'scope':'Every96–99 response and worked-reference asset.','items':answers}),('census-YM-C2-binomial-terms.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete96–99 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
