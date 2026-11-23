"""YM88: remaining progression exercise, including staircase geometry."""
import hashlib,json
import author_YM_C2_finance_bounce as prior
from author_YM_C2_finance_bounce import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM,MODEL,INFINITE,CONVERGE,extra,money
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();prior.prior.prior.prior.base.base.base.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
add=prior.add
ps=[v('a-ratio','real_root(Rational(8,9)/24,3)','Rational(1,3)',596,'T5/T2=r³=(8/9)/24=1/27. Itsunique realcube rootis1/3.'),v('b-first','24/Rational(1,3)','72',596,'UseT2=ar=24,sofirsta72.'),v('c-original-infinite','summation(72*Rational(1,3)**(k-1),(k,1,oo))','108',596,'OriginalGPconvergeswithratio1/3;independentlysum72(1/3)^(k−1).'),v('d-squared-terms-infinite','summation((72*Rational(1,3)**(k-1))**2,(k,1,oo))','5832',596,'SquaringEACHtermcreatesfirst72²andratio(1/3)²=1/9. Sumthesquaredterms,notthesquareoftheoriginalsum108².')]
add('Exercise-2.1',8,88,'RecoveraGPfromtwoindexedterms,thencompareoriginalandsquared-termseriesinfinite sums.',ps,[GPTERM,INFINITE],components=[CONVERGE])
p=money('a-eleventh-bid','Rational(95,2)+(11-1)*Rational(17,4)','90',596,'Originalbids47.50,51.75,56.00havecommondifference4.25. The11thbidis90.')
p2=v('b-hours','floor((150-Rational(95,2))/Rational(17,4)+1)+1','26',596,'BidsoccuratENDofeachhour,sobidindexnequalselapsedhours. StrictT_n>150requiresn>1+(150−47.5)/4.25;least26.')
extra(p2,'adjacent-bid-tests','Tuple(Rational(95,2)+24*Rational(17,4)<=150,Rational(95,2)+25*Rational(17,4)>150)','Tuple(True,True)')
p3=money('c-total-bids','summation(Rational(95,2)+(k-1)*Rational(17,4),(k,1,24))','2313',596,'Sumall24bidvaluesasasked. Thisisnotrevenuereceived:thequestiondoesnotclaimallbidsarepaid.')
add('Exercise-2.1',9,88,'ModelhourlyAPbidamountswithanexplicitend-of-hourtiming,thresholdandsumofbidvalues.',[p,p2,p3],[MODEL,APTERM])
ps=[]
for label,expr,key in [('a-tenth-year','2000*Rational(9,10)**9','774.84'),('b-first-twenty','summation(2000*Rational(9,10)**(k-1),(k,1,20))','17568.47'),('c-long-run','summation(2000*Rational(9,10)**(k-1),(k,1,oo))','20000')]:
 p=v(label,expr,key,596,'Originalfirst-yearproduction2000kgdecreasesbyfactor0.9eachyear. Derivetheaskedterm,finitefirst20sumorinfiniteidealisedtotalfromthesameannualsequence;roundonlythefinalanswertotherequested2dp.')
 p['operation']={'kind':'rounded','operands':[expr],'decimal_places':2};p['units']='kg';p['printed_key_units']='kg';extra(p,'exact-original-value',expr,str(compute({'kind':'identity','operands':[expr]})));ps.append(p)
add('Exercise-2.1',10,88,'Modeldecliningannualmetalextraction,thencomputeatenth-yearamount,20-yearsumandlong-runidealisedtotalwith2dpandkg.',ps,[MODEL,GPTERM,INFINITE],components=[CONVERGE])
p=v('a-step-count','1+(250-10)/15','17',596,'Thefirstbottomriseris10cm,eachadditionalriser15cm. Totalheightfornstepsis10+15(n−1),not15n. Solve250cmforpositiveintegern17.')
p2=v('b-side-area','30*summation(10+(k-1)*15,(k,1,12))/10000','3.33',596,'Decomposethesideinto12verticalstripsofwidth30cm,height10,25,…,175cm. Sumtheirareas33300cm²thenconvertby10000cm²perm²,giving3.33m². Do notuse250cmfrom(a),whichisanotherstaircase.')
p2['units']='m²';p2['printed_key_units']='m²'
r=add('Exercise-2.1',11,88,'Readastaircaseprofilewithfirst10cmriser,later15cmrisersand30cmtreads;deriveastepcountanda12-stepstrip-sumarea.',[p,p2],[MODEL,APTERM]);r['representation']='diagram'
fig(46,88,'Staircase four-step profile','Thegivenfour-stepdiagramhasbottomriser10cm,threefurther15cmrises,andfour30cmtreads. Itsheightis55cm,width120cm. Part(a)asksadifferent17stepstaircase;part(b)asks12steps. Preservefirst-riserexception,constanttreadwidthandphysicalsquare-unitconversion.',[MODEL,APTERM],'diagram',[('Tuple(10+3*15,4*30)','Tuple(55,120)')],parent='Exercise-2.1:11')
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:');f['printed_page']=77;f['source_evidence']=ev(88);f['value_level_scope_decisions']=[]
 crop=W/'checks/r5/textbooks/YM-C2-staircase-native.png';f['source_evidence_native']={'path':str(crop.relative_to(W.parents[2])),'sha256':hashlib.sha256(crop.read_bytes()).hexdigest(),'crop_box_pdf_points':[340,500,565,630],'inspection':'Codex author visually read full staircase outline,4tread labels and4riser labels; independent acceptance pending.'}
pages=[{'pdf_page':88,'printed_page':77,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers]+[r['item_id']for r in figures],'continuation_item_ids':[],'source_evidence':ev(88),'reader':'Codex author','date':'2026-11-19','non_item_content':'EveryExercise2.1Q8–11responseandthefour-stepgivendiagramrecorded. SquaredGPterms,explicithour-endbidtiming,productionunitsandstaircasefirst-riserexceptionchecked. Thisfinishestheprogressionsection.','scope_screen':'Allfourquestionsinprescribedscope. Long-runextractionisanidealisedconvergentsummodel;actualfinitephysicalproductionisnotcertified.'}]
if __name__=='__main__':
 for name,data in [('answers-YM-C2-progression-closing.json',{'scope':'Every88responseandstaircaseasset.','items':answers}),('census-YM-C2-progression-closing.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete88census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
