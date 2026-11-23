"""YM76–79: unknown sigma bounds/parameters and convergent geometric sums."""
import json
import author_YM_C2_thresholds_sigma as prior
from author_YM_C2_thresholds_sigma import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM,INTERPRET,EVALUATE,extra
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();prior.base.base.base.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
CONVERGE='8227:2020:M1:T2:O05:D01';INFINITE='8227:2020:M1:T2:O05:D02';GP='8227:2020:M1:T2:O02:D02'

def add(kind,n,page,note,parts,direct,components=None):
 r=prior.add(kind,n,page,note,parts,direct,components)
 r['mapping_rationale']='Classify the requested outcome: a finite count, sigma representation/evaluation, a convergent infinite sum, or an explicitly asked convergence decision. Using a convergence condition during an infinite-sum calculation remains component evidence unless the learner must report/justify it. Unknown symbols in a summand are not automatically upper limits.'
 return r

def sigma(label,expr,lo,hi,terms):
 p=reasoning(label,'Sum('+expr+', (k,'+str(lo)+','+str(hi)+'))',
 'Infer the original ordered term rule and inclusive bounds,then independently expand the proposed sigma form to reproduce every supplied term. A shifted lower index andmatching formula are equally valid; a matching numeric total alone does not establish this representation.',595,'matches')
 extra(p,'ordered-expansion','Tuple('+','.join(expr.replace('k','('+str(i)+')')for i in range(lo,hi+1))+')',terms)
 return p
add('Try-Now-27',1,76,'Write two fully listed finite AP/GPseries in sigma notation,withall8or6terms preserved.',[
 sigma('a','29-3*k',1,8,'Tuple(26,23,20,17,14,11,8,5)'),sigma('b','2*5**(k-1)',1,6,'Tuple(2,10,50,250,1250,6250)')],[INTERPRET])
p=reasoning('a','Sum(2*k,(k,1,45))','The requested45even-number terms havegeneral term2kandbounds1..45. Confirmfirst2andlast90andcount45. Shiftedk0..44with2k+2is equivalent.',595,'matches');extra(p,'endpoints-count','Tuple(2*1,2*45,45-1+1)','Tuple(2,90,45)')
p2=reasoning('b','Sum(8*k-5,(k,1,p))','The original3,11,19,…hasfirst3anddifference8,so its kth term is8k−5. The stated pterms mean a positive integerp; alternativek0..p−1with3+8kisvalid.',595,'matches');extra(p2,'first-three','Tuple(8*1-5,8*2-5,8*3-5)','Tuple(3,11,19)')
p3=sigma('c','3*Rational(1,3)**(k-1)',1,6,'Tuple(3,1,Rational(1,3),Rational(1,9),Rational(1,27),Rational(1,81))')
add('Try-Now-27',2,76,'Write sigma representations for a fixed-length AP,a symbolic-length APand a finite GPwhose endpoint determines its length.',[p,p2,p3],[INTERPRET])
p=v('n','log(1+378/6)/log(2)','6',76,'The original summand3·2^rstartsatr1,so the first term is6,not3. Itsfinite sum6(2^n−1)=378givesn6.')
extra(p,'original-total','summation(3*2**k,(k,1,6))','378')
add('Example',28,76,'Find an unknown upper summation bound from a finite doubling GPtotal; retain its first index1.',[p],[GPTERM],components=[INTERPRET,EVALUATE])
parts=[]
for label,eq,key,method in [
 ('a','x*(x-2)-48','8','The originalsum(2a−3),a1..n,isn(n−2). Solve n(n−2)=48andretain positiveintegern8,not−6.'),
 ('b','8*(1-Rational(1,2)**x)-Rational(511,64)','9','The exacttarget7+63/64=511/64gives2^(−n)=1/512,son9.'),
 ('c','-2*x**2-x+36','4','The APsumof1−4r,r1..n,is−2n²−n. Itsoriginaltarget−36givesn4,not−9/2.'),
 ('d','Rational(3,2)*(2**x-1)-Rational(1533,2)','9','The originalsummand(3/2)2^(b−1)starts3/2; its sum766½requires2^n512,son9.'),
 ('e','x*(11*x+1)/2-273','7','Sum11q−5forq1..n toobtainn(11n+1)/2; retain positiveintegerroot7.'),
 ('f','-16*(1-Rational(1,2)**x)+Rational(63,4)','6','The originalnegativeGPstarts−8andhasratio1/2. Itsfirstn sum−16(1−2^(−n))=−15¾givesn6.')]:
 p=v(label,'Max(*solveset('+eq+',x,domain=S.Reals))',key,595,method)
 # Exact discrete verification uses the original summand after solving.
 summand={'a':'2*k-3','b':'4*Rational(1,2)**(k-1)','c':'1-4*k','d':'Rational(3,2)*2**(k-1)','e':'11*k-5','f':'-8*Rational(1,2)**(k-1)'}[label]
 target={'a':'48','b':'Rational(511,64)','c':'-36','d':'Rational(1533,2)','e':'273','f':'-Rational(63,4)'}[label]
 extra(p,'original-sum','summation('+summand+',(k,1,'+key+'))',target);parts.append(p)
p=v('g','solve(summation(2*k+3*x,(k,3,5))-51,x)[0]','3',595,'Here n is a parameter INSIDEthe summand,not the upper bound5. Three original terms give24+9n=51,son3. No progression length is being requested.')
parts.append(p)
p=v('h','solve(summation(x*2**(k-1),(k,1,3))-21,x)[0]','3',595,'Here n is a coefficient INSIDEthe summand with fixedbounds1..3. The coefficient sum1+2+4is7,so7n21givesn3.')
parts.append(p)
p=reasoning('i','All positive integersn≥14; the key gives onlyn14.',
 'The original finite sum is n(9n−19)/2. Solving>637gives(n−13)(9n+98)>0. For positiveintegern,thisis exactlyn≥14. The source asksfindthevalueofnwithoutaskingtheleast; the key’s14is the minimum but does not enumerate all solutions.',595,'key incomplete')
extra(p,'factor-check','expand((x-13)*(9*x+98)-(9*x**2-19*x-1274))','0');extra(p,'boundary-sums','Tuple(summation(9*k-14,(k,1,13)),summation(9*k-14,(k,1,14)))','Tuple(637,749)');parts.append(p)
p=reasoning('j','n2oranypositiveintegern≥4; the key gives onlyn4.',
 'The original alternatingsum is(81/4)[1−(−1/3)^n]. It is<21 iff(−1/3)^n>−1/27. Every positiveevennqualifies; oddn1fails,n3is equality andfails,andalloddn≥5qualify. Thusn2andalln≥4arevalid. The stem doesnotaskforaminimum; evenifitdid,theminimumwouldbe2,not4.',595,'key incomplete')
extra(p,'first-five-partial-sums','Tuple('+','.join('summation(27*(-Rational(1,3))**(k-1),(k,1,'+str(i)+'))'for i in range(1,6))+')','Tuple(27,18,21,20,Rational(61,3))');parts.append(p)
r=add('Try-Now',28,76,'Solve six unknown sigma bounds,two coefficients inside summands,andtwo inequalities. Preserve allinteger solutions instead of silently rewriting the task asfindtheleast.',parts,[APTERM,GPTERM,EVALUATE],components=[INTERPRET])
for p in r['subparts']:
 p['assessed_8227_demand_ids']=[APTERM]if p['subpart']in['a','c','e','i']else[GPTERM]if p['subpart']in['b','d','f','j']else[EVALUATE]

parts=[]
for label,count,key in [('a',10,'80.99862826'),('b',15,'80.99999436'),('c',20,'80.99999998')]:
 expr='summation(54*Rational(1,3)**(k-1),(k,1,'+str(count)+'))'
 p=v(label,expr,key,77,'Sum the original54(1/3)^(k−1)over exactly'+str(count)+'positions. Compare with the source’s displayed8decimal places; retain the exact finite sum separately. The source formula is valid; itsmiddle display has a last-digit rounding discrepancy.')
 p['operation']={'kind':'rounded','operands':[expr],'decimal_places':8};extra(p,'exact-finite-result',expr,str(compute({'kind':'identity','operands':[expr]})))
 if label=='b':p['author_expected_normalised']='Rational(8099999435,100000000)'
 p['precision_interpretation']={'question_precision_requirement':None,'source_display_decimal_places':8,'basis':'Audit the decimal at its own displayed precision,not an invented question requirement; exact finite value retained.'}
 parts.append(p)
parts.append(v('d-infinite','summation(54*Rational(1,3)**(k-1),(k,1,oo))','81',77,'The originalratio1/3hasabsolutevalue<1. Independently sum the infinite series to81,which finite sums approach but never reach.'))
add('Example',29,77,'Compare10-,15-and20-term GPpartial sums withthe sum toinfinity; the source’sS15last decimal digit rounds incorrectly.',parts,[GPTERM,INFINITE],components=[CONVERGE])

def inf(label,a,ratio,key,kp):
 p=v(label,'summation(('+a+')*('+ratio+')**(k-1),(k,1,oo))',key,kp,'Independently sum the original infinite geometric term expression after verifying the absolute ratio is strictly below1. Use the actual first term at the stated start; preserve negative ratios andsigns.')
 extra(p,'ratio-convergence','Abs('+ratio+')<1','True');return p
parts=[inf('a','8','Rational(1,2)','16',595),inf('b','Rational(1,2)','Rational(1,2)','1',595),inf('c','49','Rational(2,7)','Rational(343,5)',595),inf('d','Rational(9,100)','Rational(1,10)','Rational(1,10)',595)]
add('Try-Now-29',1,78,'Find four convergent infinite GPtotals,including exactdecimal firstterms andrationalratio2/7.',parts,[INFINITE],components=[CONVERGE])
p=v('first-four','Tuple(12,12*Rational(1,2),12*Rational(1,2)**2,12*Rational(1,2)**3)','Tuple(12,6,3,Rational(3,2))',595,'Givenfirst12andS∞24,the valid convergent ratio solves24=12/(1−r),so r1/2. Then derive the firstfour original terms.')
extra(p,'recover-ratio','solve(24*(1-x)-12,x)[0]','Rational(1,2)')
add('Try-Now-29',2,78,'Recover the GPratio fromfirsttermandinfinite sum,then reportthefirstfourterms.',[p],[INFINITE,GPTERM],components=[CONVERGE])
p=v('sum','summation(24*Rational(1,4)**k,(k,1,oo))','8',78,'Originalindexn1makesfirst24/4=6,not24. Ratio1/4converges,andthe exactinfinite sum is8.')
add('Example',30,78,'Evaluate a sigma infiniteGPwhosefirstexponentis1,soitscoefficient24isnotitsfirstterm.',[p],[INFINITE],components=[CONVERGE,INTERPRET])
parts=[]
for label,expr,lo,key in [('a','Rational(1,2)*Rational(1,2)**(k-3)',1,'4'),('b','Rational(2,3)**(k-2)',1,'Rational(9,2)'),('c','24*Rational(1,4)**k',1,'8'),('d','81*Rational(1,3)**(k-1)',0,'Rational(729,2)'),('e','(-1)**(k+1)/2**k',0,'-Rational(2,3)'),('f','(-Rational(1,3))*(-Rational(1,2))**(k-3)',3,'-Rational(2,9)')]:
 p=v(label,'summation('+expr+',(k,'+str(lo)+',oo))',key,595,'Evaluate the original summand at its actual lowerindex'+str(lo)+'toidentifythefirstterm,then independentlysumtheconvergentseries. Startingat0or3andnegativeexponentsarevalid; do notresettheoriginalformulatostartat1withoutshiftingit.')
 parts.append(p)
add('Try-Now-30',1,78,'Evaluate six infinite sigmaGPswithshiftedexponents,zero/nonunitlowerboundsandnegativefirstterms/ratios.',parts,[INFINITE],components=[CONVERGE,INTERPRET])
p=v('sum','summation(3*(2*(-Rational(3,4))+1)**k,(k,1,oo))','-1',595,'Substitute the originalx−3/4beforeclassifyingthe ratio:2x+1=−1/2. Firstterm−3/2andratio−1/2giveinfinite sum−1; negative ratio doesnotmean divergence.')
add('Try-Now-30',2,78,'Evaluate a parameterised infiniteGPafter substitutingx−3/4; the resulting ratio isnegativeandconvergent.',[p],[INFINITE],components=[CONVERGE,INTERPRET])
p=v('p','solve(12*(1-x)-2,x)[0]','Rational(5,6)',79,'The originalinfinite sum2p^(n−1),n1..∞,hasfirst2andratiorp. Equation12=2/(1−p)givesp5/6. Verify|5/6|<1beforeacceptingit.')
extra(p,'original-infinite-sum','summation(2*Rational(5,6)**(k-1),(k,1,oo))','12')
add('Example',31,79,'Recover an infiniteGPratio parameter from a givensum,thencheckitsconvergencecondition.',[p],[INFINITE],components=[CONVERGE,INTERPRET])
p=v('p','solve(x*Rational(1,4)/(1-Rational(1,4))-Rational(8,3),x)[0]','8',595,'The originalp·2^(−2m)startsatm1andhasratio1/4,firstp/4. Infinite sum isp/3=8/3,sop8.')
extra(p,'original-infinite-sum','summation(8*2**(-2*k),(k,1,oo))','Rational(8,3)')
add('Try-Now-31',1,79,'Recover a scalar coefficientfromaninfiniteGPwithnegativeevenexponents.',[p],[INFINITE],components=[INTERPRET,CONVERGE])
p=v('q','solve(x*Rational(1,3)**3/(1-Rational(1,3))-Rational(7,2),x)[0]','63',595,'The originalq(1/3)^(k+2),k1..∞,starts q/27,notq/3. Itsinfinite sum isq/18=7/2,soq63.')
extra(p,'original-infinite-sum','summation(63*Rational(1,3)**(k+2),(k,1,oo))','Rational(7,2)')
add('Try-Now-31',2,79,'Recover a coefficientfromaninfiniteGPwhoseexponentshiftchangesitsfirstterm.',[p],[INFINITE],components=[INTERPRET,CONVERGE])
p=v('first-three','Tuple(2,2*(-Rational(1,3)),2*(-Rational(1,3))**2)','Tuple(2,-Rational(2,3),Rational(2,9))',595,'FromS∞3/2andS3=14/9,useS3/S∞=1−r³,so r³−1/27andr−1/3. Thena=S∞(1−r)=2. Reportthethreecorrelatedterms.')
extra(p,'original-given-sums','Tuple(summation(2*(-Rational(1,3))**(k-1),(k,1,3)),summation(2*(-Rational(1,3))**(k-1),(k,1,oo)))','Tuple(Rational(14,9),Rational(3,2))')
add('Try-Now-31',3,79,'Recover firstthreeGPterms jointlyfromfiniteandinfinite sums,preservingthenegativeratiobranch.',[p],[INFINITE,GPTERM],components=[CONVERGE])
p=reasoning('a-type-reason','GP,becauseconsecutivetermshavetheconstantnonzeroratio1/3.','Check(7/3)/7=(7/9)/(7/3)=1/3. Thisexplicitclassificationandreasonaredirectlyasked,notinferredfromaninfinite-sumcalculation.',595,'matches');extra(p,'ratio-test','Tuple((Rational(7,3))/7,Rational(7,9)/Rational(7,3))','Tuple(Rational(1,3),Rational(1,3))')
p2=reasoning('b-convergence-reason','Convergent,because−1<1/3<1.','For the intendedinfinitegeometriccontinuationwithnonzerofirst7,theabsolutecommonratiois1/3<1,sothepartialsumshaveafinitelimit. A constantdifferencesumrulecannotjustifythisclaim.',595,'matches');extra(p2,'convergence-condition','Abs(Rational(1,3))<1','True')
p3=inf('c-sum','7','Rational(1,3)','Rational(21,2)',595)
add('Try-Now-31',4,79,'ExplicitlyclassifyaGP,justifyconvergence,andcomputeitsinfinitesum;thesearethreeseparateassessedoutputs.',[p,p2,p3],[GP,CONVERGE,INFINITE])
p=v('a-x-range','solve_univariate_inequality(Abs(x)<1,x,relational=False)','Interval.open(-1,1)',595,'The nonzerofirstterm1andratioxgiveconvergenceiff|x|<1,i.e.−1<x<1. Endpoints±1diverge; x0isvalidinthepolynomialseries1+0+0+….')
p2=v('b-x','solve(Rational(2,3)*(1-x)-1,x)[0]','-Rational(1,2)',595,'Undertherangefrom(a),1/(1−x)=2/3givesx−1/2,whichliesin(−1,1). A convergentnegative-ratioseriescansumtoless thanitsfirstterm.')
extra(p2,'original-series','summation((-Rational(1,2))**k,(k,0,oo))','Rational(2,3)')
add('Try-Now-31',5,79,'Findthefullparameterconvergencerange,thenrecoveronevaluefromagiveninfinitesum.',[p,p2],[CONVERGE,INFINITE])
refs=[
 (33,77,'Convergence formula and unit-ratio wording defect','The sourceincorrectlysaysr1wouldnotbegeometric. A nonzeroconstantsequenceisgeometricwithr1,butitsinfinite seriesdiverges. Fornonzerofirstterm,finiteinfinite-sumformulaa/(1−r)requires|r|<1; finitequotientformrequiresr≠1.',[CONVERGE,INFINITE],'table',[('Tuple(4/4,4/4)','Tuple(1,1)')],None),
 (34,77,'Negative expansive ratios diverge by oscillation','Sourceprosesaysr<−1hasthesameunbounded-growthbehaviourasitspositive2,6,18,…example. Bothdiverge,butnegative-ratiopartialsumsalternate; theydonottendto+∞. Fora1,r−2,firstfourpartialsums1,−1,3,−5sufficeasacounterexampletothesamedirectionclaim.',[CONVERGE],'table',[('Tuple(1,1-2,1-2+4,1-2+4-8)','Tuple(1,-1,3,-5)')],None),
 (35,77,'Example29 gridded geometric-area illustration','The gridlabels54,18and6illustratesequentialpositivecontributionswithratio1/3,towardtotal81. Preserveadjacency/shadingandlabelledrelativecontributions; thefinitefirstthreecontributionssum78,not81. Thisisateachingasset,notaseparatelyaskedlearnerdiagramresponse.',[INFINITE,CONVERGE],'diagram',[('Tuple(54+18+6,81-(54+18+6))','Tuple(78,3)')],'Example:29'),
 (36,77,'Finite partial sums approaching an infinite limit','For54+18+6+…,S_n=81(1−3^(−n))isstrictlybelow81forallfinitepositiveintegern,whileS∞81. TheS15decimalroundinghasalast-digitdiscrepancy; donotreplacefinitevaluesbythelimit.',[GPTERM,INFINITE],'table',[('81*(1-Rational(1,3)**15)','Rational(14348906,177147)')],'Example:29'),
 (37,78,'Infinite sigma notation reference','The upper∞denotesafinitepartialsumlimit,notanintegerlastterm. Fornonzeroageometricseriesconvergeswhen|r|<1. Thezero-seriesdegeneracyrequiresanexplicitconventionifgeneralisingtheformula.',[INTERPRET,CONVERGE,INFINITE],'table',[('summation(Rational(1,2)**(k-1),(k,1,oo))','2')],None),
 (38,79,'Example31 parameter and convergence check','The original2p^(n−1)starts2andhasratiop. Solving12=2/(1−p)givesp5/6; verifythecandidateconvergesratherthanusinganinfinite-sumformulaoutsideitsdomain.',[INFINITE,CONVERGE],'table',[('Abs(Rational(5,6))<1','True')],'Example:31')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={76:'EveryTry27Q1/2,Example28andall10Try28responsesrecorded. Twoboundinequalitiesneedfullintegersets; n2isomittedfromTry28jkey. Summandparametersg/hareseparatefromunknownbounds.',77:'Allconvergenceteachingprose,formula,Example29finite/infiniteresponses,griddedareaillustrationandpartialsumcomparisonrecorded. Unit-ratioandnegative-expansionwordingdefectsandS15decimaldiscrepancyareexplicit.',78:'AllTry29Q1/2,infinitesigmareference,Example30andTry30Q1/2responsesrecorded. Actualstartindicesandexponentshiftsarepreserved.',79:'EveryExample31andfiveTry31taskoutputsrecorded,includingtheexplicitclassification/convergenceexplanationsandparameterrange. Nonzerofirstterm/convergenceconditionsremainexplicit.'}
pages=[]
for page in range(76,80):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Everyfinite-sigmaandinfiniteGPtask/teachingreferenceaccountedfor. Convergenceconditions,actualstartindices,fullintegerinequalitysolutionsandfiniteversusinfinitetotalsarekeptdistinct.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-convergence.json',{'scope':'Every76–79requestedresponseandconvergenceteachingasset.','items':answers}),('census-YM-C2-convergence.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete76–79pagecensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
