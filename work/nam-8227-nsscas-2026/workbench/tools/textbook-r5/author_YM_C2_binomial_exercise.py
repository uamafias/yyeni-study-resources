"""YM102: every Exercise2.2 response, including notation and correlated parameters.

Fixed-source author audit; independent acceptance remains pending.
"""
import hashlib,json
import author_YM_C2_coefficient_parameters as prior
import author_YM_C2_opening as foundation
from author_YM_C2_coefficient_parameters import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent,extra,BINOM,COEF,COMBINED,coefficient
from author_YM_C2_binomial_notation import truncate,notation
from author_YM_C2_binomial_terms import descending
from author_YM_C2_binomial_opening import poly
old_ev=prior.ev

def ev(page):
 if 598<=page<=601:
  p=W/'checks/r5/textbooks/YM-C2-keys-598-source.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 return old_ev(page)
foundation.opening.base.ev=ev
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();foundation.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections;add=prior.add
add('Exercise-2.2',1,102,'Using Pascal coefficients,fully expand three unit-first-term binomials with positive and negative second terms.',[
 poly('a','(1+x)**5','1+5*x+10*x**2+10*x**3+5*x**4+x**5',597),poly('b','(1-x)**6','1-6*x+15*x**2-20*x**3+15*x**4-6*x**5+x**6',597),poly('c','(1-2*x)**4','1-8*x+24*x**2-32*x**3+16*x**4',597)],[BINOM],'5,6,4')
notation('Exercise-2.2',2,102,'Evaluate eight factorial/nCr expressions; the exact answer locator changes from597to598 partway through this question.',[
 v('a','8*7*6*5*4*3*2*1','40320',597,'Independently multiply the original8! product.'),v('b','(3*2*1)*(5*4*3*2*1)','720',597,'Multiply3! by5!,not8!.'),v('c','14*13','182',598,'Cancel12! from14!/12!,leaving14·13.'),v('d','1/(9*8*7)','Rational(1,504)',598,'6!/9! is reciprocal1/(9·8·7),not a growing product.'),v('e','8*7/(2*1)','28',598,'8C2=8·7/2.'),v('f','11*10*9*8/(4*3*2*1)','330',598,'11C4 reduces to an independent four-factor product quotient.'),v('g','1','1',598,'18C18=18!/[18!0!]=1.'),v('h','1','1',598,'10C0=10!/[0!10!]=1.')],'All original factorial arguments are nonnegative integers; notation includes0! through the nCr boundary cases.')
add('Exercise-2.2',3,102,'Find first four ascending-x terms of three positive-integer binomials; keep their different sign/scale patterns.',[
 truncate('a','(1+x)**9','x',3,'1+9*x+36*x**2+84*x**3',598),truncate('b','(1-x)**10','x',3,'1-10*x+45*x**2-120*x**3',598),truncate('c','(1-3*x)**13','x',3,'1-39*x+702*x**2-7722*x**3',598)],[BINOM],'9,10,13')
r=add('Exercise-2.2',4,102,'Find first four descending-x terms,including a Laurent binomial whose exponent gaps are3.',[
 descending('a','(x+2)**12','x',[12,11,10,9],'x**12+24*x**11+264*x**10+1760*x**9',598),descending('b','(2*x+Rational(1,2))**8','x',[8,7,6,5],'256*x**8+512*x**7+448*x**6+224*x**5',598),descending('c','(x**2-5/x)**7','x',[14,11,8,5],'x**14-35*x**11+525*x**8-4375*x**5',598)],[BINOM],'12,8,7');r['scope_check']['basis']+=' Part(c)requiresx≠0.'
ps=[]
for label,original,target,key in [('a','(a+b/2)**13','binomial(13,8)*a**5*(b/2)**8','Rational(1287,256)*a**5*b**8'),('b','(2*a+b/4)**15','binomial(15,5)*(2*a)**10*(b/4)**5','3003*a**10*b**5'),('c','(a/(2*b)+b**2/a)**13','binomial(13,7)*(a/(2*b))**6*(b**2/a)**7','Rational(429,16)*b**8/a'),('d','(a**2/sqrt(b)+sqrt(b)/a)**9','binomial(9,6)*(a**2/sqrt(b))**3*(sqrt(b)/a)**6','84*b**Rational(3,2)')]:
 p=v(label,target,key,598,'Use the indicated term in the original binomial factor-choice order,so positions9,6,8,7mean r8,5,7,6 respectively. The prompt gives no variable sorting instruction here. Substitute the original first/second terms into nCr·first^(n−r)·second^r and simplify the entire term.')
 p['original_expression']=original
 if label=='d':p['original_real_domain']='a≠0,b>0: sqrt(b) is a denominator and is real.'
 ps.append(p)
r=add('Exercise-2.2',5,102,'Find four indicated terms in original binomial order,with fractional/reciprocal coefficients and one square-root denominator.',ps,[COEF],'13,15,13,9');r['scope_check']['basis']+=' Part(c):a≠0,b≠0. Part(d):a≠0,b>0. Positive outer integer powers are preserved.'
r=add('Exercise-2.2',6,102,'Find two chosen Laurent coefficients by matching the variable exponent,not by taking the same numbered term.',[
 coefficient('a','(x-3/x)**15','x',7,'110565',598),coefficient('b','(x**2+2/x)**9','x',6,'2016',598)],[COEF],'15,9');r['scope_check']['basis']+=' Both originals requirex≠0.'
r=add('Exercise-2.2',7,102,'Find constant terms in two positive-integer Laurent binomials,retaining the original nonzero-x domain.',[
 coefficient('a','(x**2-2/x)**6','x',0,'240',598),coefficient('b','(1/(2*x**2)+x)**9','x',0,'Rational(21,2)',598)],[COEF],'6,9');r['scope_check']['basis']+=' Both originals requirex≠0.'
p=reasoning('correlated-parameters','(a,n,q)=(4,6,37)or(−4,4,41).','The constant coefficienta²=16givesa±4. The linear condition2a−8n=−40givesn5+a/4,so the correlated pairs are(4,6)and(−4,4). The quadratic coefficient is1−an+2n(n−1),giving37or41respectively. Both n values are positive integers. The native key clearly printsq37andq41; an initial contact-sheet impression ofa37was a false lead and is cleared. Both numeric branches and labels are correct.',598,'matches')
extra(p,'first-original-coefficients','Tuple(expand((4+x)**2*(1-x/2)**6).coeff(x,0),expand((4+x)**2*(1-x/2)**6).coeff(x,1),expand((4+x)**2*(1-x/2)**6).coeff(x,2))','Tuple(16,-40,37)')
extra(p,'second-original-coefficients','Tuple(expand((-4+x)**2*(1-x/2)**4).coeff(x,0),expand((-4+x)**2*(1-x/2)**4).coeff(x,1),expand((-4+x)**2*(1-x/2)**4).coeff(x,2))','Tuple(16,-40,41)')
r=add('Exercise-2.2',8,102,'Recover all correlated constant,power and quadratic-coefficient branches from a product whose constant term involves a square.',[p],[COMBINED],'Recoveredpositiveintegerpowers6and4');r['correlated_branch_check']={'required_pairs':[['a4','n6','q37'],['a−4','n4','q41']],'reason':'The values belong to two complete correlated triples,not independent options.'};r['source_interpretation']='Native key598 confirmsq37andq41 with complete correlated triples. The earlier small-render impression ofa37was false; no source-label defect is claimed.'
pages=[{'pdf_page':102,'printed_page':91,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers],'continuation_item_ids':[],'source_evidence':ev(102),'reader':'Codex author','date':'2026-11-19','non_item_content':'EveryExercise2.2Q1–8 response is enumerated. The page contains questions,not a separate teaching diagram. Factorial/nCr drills remain notation-facet support. Both correlated parameter triples and original real denominator/root domains are retained.','scope_screen':'All positive outer powers are within the binomial scope. Part5(d)requiresb>0anda≠0for its real denominator; other reciprocal parts retain nonzero domains. No arbitrary new scope restriction is imposed.'}]
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-binomial-exercise.json',{'scope':'Every102 Exercise2.2 response.','items':answers}),('census-YM-C2-binomial-exercise.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete102 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
