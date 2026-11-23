"""YM103–106: exam-style practice, tariff-bearing revision and chapter summary.

Fixed-source author audit; independent acceptance remains pending.
"""
import json
import author_YM_C2_binomial_exercise as prior
import author_YM_C2_opening as foundation
from author_YM_C2_binomial_exercise import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra,BINOM,COEF,COMBINED,truncate,coefficient
from author_YM_C2_convergence import CONVERGE,INFINITE,GPTERM,APTERM,INTERPRET,EVALUATE
from author_YM_C2_applications import MODEL
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();foundation.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections

def add(kind,n,page,note,parts,direct,powers=None,components=None,exam=True):
 r=prior.add(kind,n,page,note,parts,direct,powers or'No binomial expansion in this item',components)
 if not any(d in direct for d in [BINOM,COEF,COMBINED]):
  r['value_level_scope_decisions']=[]
  r['mapping_rationale']='Link the requested progression term,sum or context model directly. Explicit positivity,nonzero parameters and connected-part correspondence are retained. Using convergence during an infinite-sum calculation is a component unless the learner must independently report it.'
 r['exam_style']=exam
 r['exam_style_basis']='The source explicitly labels this section2.3 Exam-Style Questions onPDF103.'if exam else'The source labels this RevisionExercise2 and supplies a30-mark textbook tariff; no primary examination attribution is printed.'
 return r
p=v('a-AP-sum','summation(56+(k-1)*(53-56),(k,1,27))','459',103,'Originalfirst56,second53give d−3. Endpoint−22requires−22=56−3(n−1),so n27. Sum those27original terms independently.')
extra(p,'endpoint-index','solve(56-3*(x-1)+22,x)[0]','27')
p2=v('b-i-positive-k','Max(*solveset((2*x)**2-(2*x+6)*(x+2),x,domain=S.Reals))','6',103,'OriginalthreeGPterms require4k²=(2k+6)(k+2). Roots6and−1; the explicitly positive constant condition retains6. Verify all original terms18,12,8.')
p3=v('b-ii-infinite-sum','summation(18*Rational(2,3)**(k-1),(k,1,oo))','54',103,'With k6,the correlated original terms are18,12,8andratio2/3. Independently sum the convergent infinite series to54.')
add('Example',50,103,'Solve an APendpoint-sum problem and a separate positive-parameter GP/infinite-sum problem under the source’s Exam-Style heading.',[p,p2,p3],[APTERM,GPTERM,INFINITE],components=[CONVERGE])
p=v('a-correlated-x-y','Tuple(8,2*8-4)','Tuple(8,12)',598,'The originalAP4,x,y givesy=2x−4; the GPx,y,18 givesy²=18x. Solve(2x−4)²=18x: candidatesx8or1/2. The latter hasy−3,violating the given positivity of BOTHx andy. Thus correlated pair(8,12).')
extra(p,'all-x-candidates','solveset((2*x-4)**2-18*x,x,domain=S.Reals)','FiniteSet(Rational(1,2),8)')
p2=v('b-fourth-terms','Tuple(4+3*(8-4),8*(Rational(12,8))**3)','Tuple(16,27)',598,'Use the same accepted originalpairx8,y12. APdifference4givesfourth16;GPratio3/2givesfourth27. Never mix the rejected candidate with the accepted ratio.')
r=add('Try-Now',50,104,'Solve connected AP/GPconstraints with positive unknowns,then find each progression’s fourth term.',[p,p2],[APTERM,GPTERM]);r['correlated_branch_check']={'required_pairs':[['x8','y12']],'rejected_pair':['x1/2','y−3'],'reason':'Both original unknowns are explicitly positive.'}
p=v('a','real_root((330-60)/10,3)','3',104,'The quadratic coefficient in(2+x/2)^6 is60. In(a+x)^5 it is10a³. Their SUM is330,so a³27,a3. The expression is a sum of expansions,not a product.')
extra(p,'original-sum-coefficient','expand((2+x/2)**6+(3+x)**5).coeff(x,2)','330')
add('Example',51,104,'Recover a constant from a coefficient in a SUM of two binomial expansions,distinguishing addition from multiplication.',[p],[COMBINED],'6,5')
p=v('positive-a','Max(*solveset(10*x**2-160-90,x,domain=S.Reals))','5',598,'The original cubic coefficient of(a+x)^5+(1−2x)^6 is10a²−160. Equate to90,givinga±5; retain the explicitly positivea5.')
extra(p,'original-cubic','expand((5+x)**5+(1-2*x)**6).coeff(x,3)','90')
add('Try-Now-51',1,104,'Recover a positive constant from the cubic coefficient of a SUM of two expansions; retain the source’s positivity restriction.',[p],[COMBINED],'5,6')
p=truncate('a-first-three','(1-k*x)**6','x',2,'1-6*k*x+15*k**2*x**2',598)
p2=v('b-nonzero-k','Min(*solveset(15*x**2+6*x,x,domain=S.Reals))','-Rational(2,5)',598,'From the original product(1−x)(1−kx)^6,the quadratic coefficient is15k²+6k. Zero coefficient givesk0or−2/5; the original explicitly excludesk0.')
extra(p2,'original-quadratic-zero','expand((1-x)*(1+Rational(2,5)*x)**6).coeff(x,2)','0')
add('Try-Now-51',2,104,'Give three ascending terms,then determine a nonzero scale by requiring a connected quadratic coefficient to vanish.',[p,p2],[BINOM,COMBINED],'6')
p=truncate('a-first-three','(2+a*x)**5','x',2,'32+80*a*x+80*a**2*x**2',598)
p2=v('b-all-a','solveset(80*x**2+160*x-240,x,domain=S.Reals)','FiniteSet(-3,1)',598,'The quadratic coefficient of(1+2x)(2+ax)^5 is80a²+160a. Set it to240 andretain both a−3anda1; no positive-a restriction is printed here.')
extra(p2,'both-original-coefficients','Tuple(expand((1+2*x)*(2-3*x)**5).coeff(x,2),expand((1+2*x)*(2+x)**5).coeff(x,2))','Tuple(240,240)')
add('Try-Now-51',3,104,'Expand through the quadratic term,then retain both real parameter values giving a prescribed product coefficient.',[p,p2],[BINOM,COMBINED],'5')

def tariff(part,marks):part['textbook_tariff_marks']=marks;part['tariff_evidence']='Source RevisionExercise2 printed tariff,not an official marking criterion.';return part
ps=[tariff(v('a-ratio','real_root(24/81,3)','Rational(2,3)',598,'Originalfirst81andfourth24give r³24/81=8/27,so realr2/3.'),2),tariff(v('b-infinite','summation(81*Rational(2,3)**(k-1),(k,1,oo))','243',598,'Originalratio2/3converges; independentlysumfirst81series.'),2),tariff(v('c-AP-first-ten','summation(54+(k-1)*(-6),(k,1,10))','270',598,'GPsecond54andthird36becomeAPfirstandFOURTH. Therefored=(36−54)/3=−6,not−18. Sumthefirst10originalAPterms.'),3)]
add('Revision-Exercise-2',1,105,'Link a GPtoanAPvia indexed terms,then compute a ratio,infinite sum and finite APsum. Textbook tariffs2+2+3=7.',ps,[GPTERM,INFINITE,APTERM],components=[CONVERGE],exam=False)
p=tariff(v('cubic-coefficient','expand((1-5*x)**6).coeff(x,3)','-2500',598,'Originallinearcoefficient6a=−30givesa−5. Independentlyexpandthatoriginalbinomialandextractthecubiccoefficient20a³=−2500.'),4);extra(p,'recover-a','solve(6*x+30,x)[0]','-5')
add('Revision-Exercise-2',2,105,'Recover a binomial scale from a linear coefficient,then find a cubic coefficient. Textbook tariff4.',[p],[COMBINED],'6',exam=False)
p=tariff(coefficient('constant','(2*x+1/x**2)**6','x',0,'240',598),3)
r=add('Revision-Exercise-2',3,105,'Find a constant term in a Laurent sixth power. Textbook tariff3.',[p],[COEF],'6',exam=False);r['scope_check']['basis']+=' Originalx≠0.'
p=tariff(v('a-i-day-thirty-loss','10+(30-1)*2','70',598,'The first day AFTERfillingloses10litres,then2moreeachday. Day30thereforehas29increments:10+29·2=68litres. The key70is the day31amount,notday30.'),2);p['author_expected_normalised']='68';p['units']='litres';p['printed_key_units']='litres'
p2=tariff(v('a-ii-empty-day','ceiling((-9+sqrt(9**2+4*1968))/2)','41',598,'OriginalcumulativeplannedAPlossafterjdaysisj²+9j. The first integerjwithtotal≥1968is41. After40complete days,1960litresaregoneand8remain;the tank empties duringday41,so a full90litrescannotactuallyleaveonthatlastday.'),3)
extra(p2,'adjacent-cumulative-loss','Tuple(40**2+9*40,41**2+9*41,1968-(40**2+9*40))','Tuple(1960,2050,8)')
p3=tariff(reasoning('b-percentage-remaining','100[1968−100((11/10)^30−1)]/1968 percent,approximately16.4156%.','Under the alternative10%-growthdaily-lossmodel,thefirst30lossesare10(1.1)^(j−1),j1..30. Their exacttotalis100[(11/10)^30−1],below1968. Subtractfromtheoriginalvolumeanddivideby1968beforemultiplyingby100. The printed key598 omits this explicit4-marksubpart; no publisher comparison is claimed.',598,'no key'),4)
expr='100*(1968-summation(10*Rational(11,10)**(k-1),(k,1,30)))/1968';extra(p3,'exact-original-percentage',expr,str(compute({'kind':'identity','operands':[expr]})))
r=add('Revision-Exercise-2',4,105,'Distinguish daily AP/GPwaterloss,cumulativeemptyingandpercentageofinitialvolume. Textbook tariffs2+3+4=9; the4-markGPpart has no key.',[p,p2,p3],[MODEL,APTERM,GPTERM],exam=False)
p3.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[598],key_evidence=ev(598))
r['source_label_warning']='The key’s empty-day answer41is correct. Its added phrase40thdaysafterfilling conflicts with the prompt’sday1afterfilling; describe40complete days pluspartofday41instead. The GPalternative has an omitted answer.'
p=tariff(v('n','Max(*solveset(x*(63-2*x)-x,x,domain=S.Reals))','31',598,'OriginalAPfirst61,second57hasd−4andS_n=n(63−2n). The conditionS_n=n givesn0or31; the originalpositiveintegerconditionretains31.'),4)
extra(p,'original-sum','summation(61+(k-1)*(-4),(k,1,31))','31')
add('Revision-Exercise-2',5,105,'Find a positive integer when a decreasing AP’s cumulative sum equals its own term count. Textbook tariff4.',[p],[APTERM],exam=False)
p=tariff(coefficient('cubic','(2-x/2)**7','x',3,'-70',598),3)
add('Revision-Exercise-2',6,105,'Find a cubic coefficient of a scaled signed seventh power. Textbook tariff3.',[p],[COEF],'7',exam=False)
assert sum(p['textbook_tariff_marks']for r in answers if r['item_id'].startswith('8227:TB:YM:C2:Revision-Exercise-2:')for p in r['subparts'])==30
refs=[
 (79,104,'Sum-of-expansions coefficient table','Example51 separates the quadratic contributions60and10a³fromaSUMofexpansions. Add those coefficients,not their product; the source’sa3answer then gives330. The two-column working is a teaching table,not a separate question.',[COMBINED],'table',[('60+10*3**3','330')],'Example:51'),
 (80,106,'APsummary definitions and term/sum formulae','The summary gives fixed differenced,term a+d(n−1),and two equivalent finite-sum forms. Use positiveintegern; term values,term counts and cumulative totals have different meanings.',[APTERM],'table',[('simplify(n*(a+(a+(n-1)*b))/2-n*(2*a+(n-1)*b)/2)','0')],None),
 (81,106,'GPsummary finite formula alternatives','The two quotient formulas are algebraically equivalent forr≠1. The source labels themr<1andr>1as convenient choices; neither formula is an infinite-sum condition. At r1usefinite sumna. Ratio-by-division needs nonzero previous terms.',[GPTERM],'table',[('simplify(a*(1-b**n)/(1-b)-a*(b**n-1)/(b-1))','0')],None),
 (82,106,'Sigmasummary with start/end labels','The labelled example3(1)+3(2)+3(3)+3(4)=sum(i1..4)3i preserves inclusive bounds. The index letter must match the summand; it is not itself an exponent.',[INTERPRET,EVALUATE],'table',[('summation(3*k,(k,1,4))','30')],None),
 (83,106,'Convergent sum summary','For a nonzero geometric-series first term,the convergent formulaa/(1−r)requires−1<r<1. This condition is separate from the domainr≠1of finite quotient formulas.',[INFINITE,CONVERGE],'table',[('summation(2*Rational(1,3)**(k-1),(k,1,oo))','3')],None),
 (84,106,'Pascal/nCrsummary triangle','Rows0..6show coefficients and matching nCr notation. The row exponent and coefficient position stay aligned; detailed coefficient properties beyond required notation remain supporting teaching.',[BINOM,COEF],'table',[('binomial(6,3)','20')],None),
 (85,106,'Factorial/nCrsummary notation','The summary repeats0!=1,then nCr=n!/[r!(n−r)!]and nC0=nCn=1. A line calls bothnandrpositiveintegersdespiteallowingr0; the intended correct index domain is nonnegativeintegerr≤nwithpositiveintegern.',[BINOM,COEF],'table',[('Tuple(binomial(5,0),binomial(5,5))','Tuple(1,1)')],None),
 (86,106,'Finite binomial theorem summary','The boxed general finite expansion,termT_(r+1)andunit-first-termcaseallusepositiveintegern,integer0≤r≤n. A term includes variable powers and is not just its nCr coefficient; no infinite rational-power expansion is prescribed.',[BINOM,COEF],'table',[('expand((1+x)**3)','1+3*x+3*x**2+x**3')],None)]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[];f['item_kind']='teaching-figure'
notes={103:'AllExample50(a,b-i,b-ii)responses are recorded. This page explicitly starts2.3Exam-StyleQuestions; the label describes textbook intent,not primary examination provenance.',104:'EveryTry50,Example51andTry51Q1–3response plus the two-column sum-coefficient table is recorded. Correlated positivity,nonzero scales and unrestricted two-root cases remain distinct.',105:'EveryRevisionExercise2Q1–6part is recorded and all printed part tariffs reconcile to30. Q4(a-i)key70iswrong; correct68. Q4(a-ii)emptiesduringday41with8litresremainingafter40full days. Its4-markGPpart(b)key is absent.',106:'Every mathematical summary panel is enumerated:AP,finiteGP,sigma,infiniteGP,Pascal/nCr,factorialnotation andfinitebinomialtheorem. No learner task begins here. This finisheschapter2PDF52–106.'}
pages=[]
for page in range(103,107):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'Every final exam-style/revision task and summary panel is recorded. Textbook tariffs do not establish official marking criteria; no-key parts retain independent author derivations and original scope/domain conditions.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-closing.json',{'scope':'Every103–106 response,tariff and mathematical summary.','items':answers}),('census-YM-C2-closing.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete103–106 page census; closeschapter2.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
