"""YM80–83: progression modelling, units, inclusive years and elapsed time."""
import json
from datetime import date,timedelta
import author_YM_C2_convergence as prior
from author_YM_C2_convergence import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM,extra
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();prior.prior.base.base.base.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
MODEL='8227:2020:M1:T2:O03:D03'

def add(kind,n,page,note,parts,direct,components=None,continuation=None):
 r=prior.add(kind,n,page,note,parts,direct,components)
 if continuation:r['continuation_pdf_pages']=continuation;corrections[-1]['continuation_pdf_pages']=continuation
 r['mapping_rationale']='A physical,financial orcalendar model is direct when translating that context into terms/sums is necessary. Bare even-number summation is an APsum,not separately contextual modelling. Unitconversion,geometry totals andlogarithm manipulation are componentsunless separately requested. Termindices andelapsedyears must be distinguished.'
 return r

def money(label,expr,key,kp,method):
 p=v(label,expr,key,kp,method);p['operation']={'kind':'rounded','operands':[expr],'decimal_places':2}
 p['units']='N$';p['printed_key_units']='N$';extra(p,'unrounded-original-total',expr,str(compute({'kind':'identity','operands':[expr]})))
 return p

ps=[]
for label,conclusion in [('piece-count','No feasible positiveintegerpiececount for the stated62cmrope;31pieces is conditional onchangingthetotalto62m.'),('difference','No validcommon differencefor the impossible statedrope;0.1m isconditionalontheintended62mtotal.')]:
 p=reasoning(label,conclusion,'Convert62cmto31/50m. A stated3.5mpiece aloneexceedsthetotal0.62m,so no cutting exists. The formalAPsumwouldgiven=0.31,notapositiveinteger. Theworkedsolutionmixes62cmwithmetreendpointsandobtains31and0.1asif62weremetres. Do notsilentlycorrecttheoriginal; keeptheintendedalternativeconditional.',80,'key wrong')
 extra(p,'unit-normalised-total','62/100','Rational(31,50)');extra(p,'formal-count','2*Rational(31,50)/(Rational(1,2)+Rational(7,2))','Rational(31,100)');extra(p,'intended-metre-count','2*62/(Rational(1,2)+Rational(7,2))','31')
 ps.append(p)
add('Example',32,80,'An AP-rope cutting model is infeasible as printed: total62cmversusshortest0.5mandlongest3.5m. Preserve the unitdefect ratherthanadopttheworked31piecesunconditionally.',ps,[MODEL,APTERM])
p=v('side-count','2*42/(Rational(13,10)+Rational(57,10))','12',595,'Allsideunitsaremetres. APmeanlength(1.3+5.7)/2=3.5andperimeter42give12sides. The inferredpositiveintegercountalsomustbeatleast3,andlargest5.7isbelowthesumofothers36.3.')
extra(p,'difference','(Rational(57,10)-Rational(13,10))/(12-1)','Rational(2,5)')
add('Try-Now-32',1,80,'Infer the numberofpolygonsides froman APofside lengthsandperimeter,withconsistentmetreunits.',[p],[MODEL,APTERM])
add('Try-Now-32',2,80,'Sumtheevenintegersfrom50to100inclusively; thisisabareAPsumratherthanaphysicalcontextmodel.',[
 v('total','summation(50+(k-1)*2,(k,1,26))','1950',595,'Thereare(100−50)/2+1=26evenintegers. Directsum1950; endpoint100isincluded.')],[APTERM])
angle_system='solve([a+5*b-3*a,6*a+15*b-360],(a,b))'
p=v('six-angles','Tuple('+','.join(angle_system+'[a]+'+str(i)+'*'+angle_system+'[b]'for i in range(6))+')','Tuple(30,42,54,66,78,90)',595,'Letfirstangleaanddifference d. Thelargestconditiona+5d=3aandfullturnsum6a+15d=360givea30,d12. Reportall6angleswithdegrees,notradians.')
extra(p,'derive-first-difference','Tuple(solve([a+5*b-3*a,6*a+15*b-360],(a,b))[a],solve([a+5*b-3*a,6*a+15*b-360],(a,b))[b])','Tuple(30,12)');extra(p,'full-turn','30+42+54+66+78+90','360');p['units']='degrees';p['printed_key_units']='degrees'
add('Try-Now-32',3,80,'Model6sectoranglesasanAPusingthefull360°turnandlargest=3smallest; geometryservesascomponentcontext.',[p],[MODEL,APTERM])
length_system='solve([a+5*b-5*a,6*a+15*b-36],(a,b))'
p=v('six-lengths','Tuple('+','.join(length_system+'[a]+'+str(i)+'*'+length_system+'[b]'for i in range(6))+')','Tuple(2,Rational(18,5),Rational(26,5),Rational(34,5),Rational(42,5),10)',595,'For6APsides,total36andlasta5givea2,d8/5. Everylengthispositiveandlargest10<26sumofothers,soapolygonisfeasible. Noanglesorregularityareimplied.')
extra(p,'derive-first-difference','Tuple(solve([a+5*b-5*a,6*a+15*b-36],(a,b))[a],solve([a+5*b-5*a,6*a+15*b-36],(a,b))[b])','Tuple(2,Rational(8,5))');p['units']='cm';p['printed_key_units']='cm'
add('Try-Now-32',4,80,'Recoverall6hexagonsidelengthsfromtheirAP,totalperimeterand5:1extremeratio.',[p],[MODEL,APTERM])
p=v('a-first-year','1995+(floor(log(Rational(1,5))/log(Rational(9,10)))+2)-1','2011',81,'The originaldonationinyear1995isT1=10000; lateronesmultiplyby0.9. T_n<2000firstoccursatn17,correspondingto1995+17−1=2011,not2012.')
extra(p,'adjacent-donation-tests','Tuple(10000*Rational(9,10)**15>=2000,10000*Rational(9,10)**16<2000)','Tuple(True,True)')
p2=money('b-1995-through-2004','summation(10000*Rational(9,10)**(k-1),(k,1,10))','65132.16',81,'Bothendyearsincluded:1995..2004contains10donations,positions1..10. Roundcurrencyonlyafterindependentlysummingexactamounts.')
p3=money('c-2005-through-2014','summation(10000*Rational(9,10)**(k-1),(k,11,20))','22710.18',82,'2005isposition11and2014position20intheORIGINALsequence. Sumthose10termsdirectly; resettingfirstdonationto10000wouldansweradifferentperiod.')
p4=v('d-first-exceedance-count','floor(log(Rational(1,10))/log(Rational(9,10)))+1','22',82,'Cumulativefirstnyearlydonations=100000(1−0.9^n)>90000iffn>log_(0.9)(0.1). Leastintegercount22. Thiscountsannualdonationevents;their22ndcalendaryearis2016.')
extra(p4,'adjacent-cumulative-tests','Tuple(100000*(1-Rational(9,10)**21)<=90000,100000*(1-Rational(9,10)**22)>90000)','Tuple(True,True)')
r=add('Example',33,81,'Modelannualdecliningdonations,afirst-termthreshold,inclusivecalendarblocksandacumulativesumthreshold. Theworkedexamplecontinueson82.',[p,p2,p3,p4],[MODEL,GPTERM],continuation=[82])
for p in r['subparts'][2:]:p.update(source_pdf_page=82,source_evidence=ev(82))
ps=[v('a-i-year-two','30000*Rational(3,5)','18000',595,'Losing40%ofthebeginningvolumeleaves60%. Beginningyear2is30000·0.6=18000m³.'),
 v('a-ii-year-five','30000*Rational(3,5)**4','30000*Rational(3,5)**4',595,'Beginningyear5followsFOURcompletedlossyears,soitis30000·0.6^4. Thisestablishesthegivenresultwithoutchangingitintoafifthloss.')]
ps[-1]['check_mode']='show/prove'
p=v('a-iii-general-beginning-volume','30000*Rational(3,5)**(n-1)','30000*Rational(3,5)**(n-1)',595,'Usepositiveintegern;beginningyear1hasn−1=0losses. Thetermformcomesfromtheoriginal40%lossmodel,notfromananswerkey.')
extra(p,'first-and-second','Tuple(30000*Rational(3,5)**0,30000*Rational(3,5)**1)','Tuple(30000,18000)');ps.append(p)
p=v('b-loss-during-year','expand(30000*Rational(3,5)**(n-1)-30000*Rational(3,5)**n)','12000*Rational(3,5)**(n-1)',595,'Lossduringyearnisbeginningyearnminusthefollowingbeginningvolume,equivalently40%ofthen-beginningvolume. Thisisaseparatedecreasingsequencefromtheretainedvolume.');p['check_mode']='show/prove';ps.append(p)
p=v('c-six-year-loss','summation(12000*Rational(3,5)**(k-1),(k,1,6))','28600',595,'Independentlysumthefirst6yearlylosses,thencomparewiththekey’slabelled3sftotal28600m³. Exactloss28600.32alsoequalsinitialvolumeminusbeginningyear7.')
p['operation']={'kind':'rounded','operands':['summation(12000*Rational(3,5)**(k-1),(k,1,6))'],'significant_figures':3};extra(p,'conservation-of-volume','30000-30000*Rational(3,5)**6','Rational(715008,25)');ps.append(p)
for p in ps:p['units']='m³';p['printed_key_units']='m³'
r=add('Try-Now-33',1,82,'ModelretainedwaterandannualwaterlossasseparateGPs;showtheyear5andgeneral-lossresults,andcalculatesixyears’cumulativeloss.',ps,[MODEL,GPTERM],continuation=[83])
for p in r['subparts'][3:]:p.update(source_pdf_page=83,source_evidence=ev(83))
p=v('first-calendar-year','1960+floor(log(5)/log(Rational(21,20)))+1','1993',595,'Initial100isheldon1January1960;thefirst5%creditisin1961. Afterjcredits,balance100(1.05)^j>500firstrequiresj33. Calendar1960+33=1993. Thekey’sn34iscompatiblewithcalling1960T1; itisnot34elapsedinterestyears.')
extra(p,'adjacent-credit-tests','Tuple(100*Rational(21,20)**32<=500,100*Rational(21,20)**33>500)','Tuple(True,True)')
r=add('Try-Now-33',2,83,'Findthefirstyearasavingsbalanceexceeds500withinterestcreditsstartingoneyearafteropening.',[p],[MODEL,GPTERM]);r['source_label_warning']='Keyn34countsinitialbalanceasT1,butthereare33interestcredits/elapsedyears. Itsfinalcalendaryear1993iscorrect; donotmisclassifythatintermediatetermindexasawrongcalendaranswer.'
p=v('days','ceiling(log(17)/log(Rational(6,5)))','16',595,'Cumulativeafterjfullmodeldaysis50[(6/5)^j−1]. Thetaskneedsatleast800m²,hence(6/5)^j≥17andfirstintegerday16. Thefinaldaystopswhen800isreached;donotclaimthefullgeometricday16areawasdug.')
extra(p,'adjacent-area-tests','Tuple(50*(Rational(6,5)**15-1)<800,50*(Rational(6,5)**16-1)>=800)','Tuple(True,True)')
add('Try-Now-33',3,83,'Modellingdailyincreasingdugareas,findthefirstcompletiondaywithapartiallastdayallowed.',[p],[MODEL,GPTERM])
p=v('a-april-seven-distance','35*Rational(19,20)**9','22',595,'From29March2011to7April2011inclusiveis10days. OriginalT10=35(0.95)^9≈22.0587km,roundtonearestkm22.')
p['operation']={'kind':'rounded','operands':['35*Rational(19,20)**9'],'decimal_places':0};p['units']='km';p['printed_key_units']='km'
assert(date(2011,4,7)-date(2011,3,29)).days+1==10
p2=reasoning('b-completion-date','20April2011,day23.','Theoriginalfirstndistances sum700(1−0.95^n). Needatleast480,so0.95^n≤11/35andn≥log_(0.95)(11/35),whoseceilingis23. CountingMarch29asday1,day23isApril20. Thelastdayistruncatedatthetarget480km.',595,'matches')
extra(p2,'count','ceiling(log(Rational(11,35))/log(Rational(19,20)))','23');extra(p2,'adjacent-cumulative-tests','Tuple(700*(1-Rational(19,20)**22)<480,700*(1-Rational(19,20)**23)>=480)','Tuple(True,True)');assert date(2011,3,29)+timedelta(days=22)==date(2011,4,20)
add('Try-Now-33',4,83,'Findonecalendarday’sdistanceandthecompletiondateforadecreasingdailywalk,withanearest-kmresponseandpartiallastday.',[p,p2],[MODEL,GPTERM])
p=v('a-first-three','Tuple(3,3**2,3**3)','Tuple(3,9,27)',595,'Underthestandardbranchingmodel,eachroundreachesthreetimesasmanyNEWdistinctpeopleasthepreviousround. Thefirstsendcountsasround1,so3,9,27,… .')
p2=v('b-total-recipients','summation(3**k,(k,1,5))','363',595,'Fiveforwardingroundsincludingtheinitialsendgive3+9+27+81+243=363underadisjoint-recipientmodel. Ifrecipientsrepeat,thenumberofdistinctpeoplecannotbededucedfromtheforwardingrulealone.')
r=add('Try-Now-33',5,83,'ModelfiveemailforwardingroundsasbranchingGPtermsandcumulativerecipients;makeabsenceofoverlappingrecipientsexplicit.',[p,p2],[MODEL,GPTERM]);r['source_interpretation']='Thekey363usesanidealdisjoint-new-recipientmodel. Thewording3otherfriendsdoesnotguaranteeglobaldistinctnessorunlimitedgrowth. Recordthemodellingassumption; donotpresent363asanobservedunique-personcount.'
add('Try-Now-33',6,83,'ModelweeklytrainingdistancesasanAPwithfirst200kmandincrease25kmperweek,thenfindweek7andfirst15total.',[
 v('a-week-seven','200+(7-1)*25','350',595,'Week7hassixincrements,so350km.'),v('b-first-fifteen','summation(200+(k-1)*25,(k,1,15))','5625',595,'Sum15weeklydistancesfromtheoriginalfirst200anddifference25;total5625km.')],[MODEL,APTERM])
p=v('a-elapsed-years','(72000-48000)/4800','6',595,'Salary starts48000andriseseachENDofyearby4800. Fivecompletedraisesreach72000; thatisstartofsalaryyear6. ThequestionasksAFTERhowmanyyears,soelapsedanswer5,thekey’sn6isatermindexratherthanelapsedtime.');p['author_expected_normalised']='5'
p2=money('b-ten-year-total','summation(48000+(k-1)*4800,(k,1,10))','696000',595,'Thereare10annualsalaryamounts:48000inyear1through91200inyear10. End-of-yearraisesaffectthefollowingannualamount; total696000.')
add('Try-Now-33',7,83,'Distinguishcompletedyearsbeforereachingasalaryfromthesalary’sannualtermindex,thenfind10years’earnings.',[p,p2],[MODEL,APTERM])
refs=[
 (39,80,'Context modelling method note','Chooseanintendeddifference/ratiofromthecontext,thendecidewhethera termoracumulativesumisrequested. Threeconsecutivetermssupportthebook’sclassificationheuristic; a finiteprefixalonecannotproveanunlimitedcontinuationrule.',[MODEL],'table',[],None),
 (40,81,'Donation calendar and index correspondence','DonationT1occursin1995,T10in2004,T11in2005andT20in2014. Inclusiveperiodlengthandoriginalindexmustbothbepreserved. TermthresholdT_n<2000andcumulativethresholdS_n>90000aredifferenttasks.',[MODEL,GPTERM],'table',[('Tuple(1995+10-1,1995+11-1,1995+20-1)','Tuple(2004,2005,2014)')],'Example:33'),
 (41,82,'Declining donation second-block working','Theworkedsecondperiodusesfirstterm10000·0.9^10,not10000,and10terms. ItisequivalenttooriginalS20−S10. Contextualperiodchangesdo notpermitresettingtheoriginalfirstvalue.',[MODEL,GPTERM],'table',[('simplify(10000*Rational(9,10)**10*(1-Rational(9,10)**10)/(1-Rational(9,10))-(10000*(1-Rational(9,10)**20)/(1-Rational(9,10))-10000*(1-Rational(9,10)**10)/(1-Rational(9,10))))','0')],'Example:33')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={80:'EveryExample32andTry32Q1–4outputrecorded. The62cmversusmetreendpointsdefectmakesExample32infeasibleasprinted;conditional62mworkingkeptseparate. Bareevensumdoesnotclaimcontextmodelling.',81:'AllfourExample33responsesbeginhere,but(c/d)workingcontinues82. Calendar/indexcorrespondenceandcurrencyroundingreferenceaccountedfor.',82:'Example33(c/d)continuationanditssecond-periodreferenceareaccountedfor. Try33Q1startsherewithretained-volumepartsandcontinues83withloss/totalparts.',83:'Try33Q1continuationandallTry33Q2–7responsesrecorded. Initialbalanceversusinterest-creditcount,partiallastdays,recipientoverlapassumptionandcompletedyearsversussalaryindexareexplicit.'}
pages=[]
for page in range(80,84):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 continuations=['8227:TB:YM:C2:Example:33']if page==82 else['8227:TB:YM:C2:Try-Now-33:1']if page==83 else[]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':continuations,
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Allapplicationtasksandcontinuationsrecorded. Validatepositive/integertimeindices,consistentunits,inclusivecalendarperiods,feasiblecuttingandexplicitmodellingassumptions.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-applications.json',{'scope':'Every80–83requestedmodellingresponseandcontinuation.','items':answers}),('census-YM-C2-applications.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete80–83pagecensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
