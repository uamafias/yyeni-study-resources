"""YM84–87: recurring decimals, cash-flow timing, bounce geometry, Exercise2.1."""
import hashlib,json
import author_YM_C2_applications as prior
from author_YM_C2_applications import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM,MODEL,extra,money
from author_YM_C2_convergence import CONVERGE,INFINITE,INTERPRET,EVALUATE,inf
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();prior.prior.prior.base.base.base.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections

def add(kind,n,page,note,parts,direct,components=None,continuation=None):return prior.add(kind,n,page,note,parts,direct,components,continuation)

def supporting_decimal(row):
 row['teaches_8227_demand_ids']=[INFINITE,CONVERGE]
 row['mapping_rationale']='The requested result is a fraction orordinaryseriesrepresentationofa recurringdecimal,not an explicitly mandatedGPsumorsigmaformula. Thebookteachesaconvergent-seriesmethod,butequivalentplace-valuealgebraisvalid. Retainassupportingtextbookpractice;donotclaimdirectcoverageof8227infinite-sumorcontext-modellingdemandfromthefractionansweralone.'
 row['evidence_role']='prerequisite/supporting recurring-decimal practice; source teaches an optional convergent-GP method'

p=reasoning('a-series','4/5+2/25+1/125+… = sum fromk1to∞of8·10^(−k).','Eachfurther8occupiesthenextdecimalplace. Theoriginal0.overline8starts0.8,0.08,0.008,…;indexk1givesfirst8/10. Thesourceduplicateslabel(a)forthenextfractionrequest;stablelabelsretainedasseries/fractionratherthanquietlyrenumberingtheoriginal.',84,'matches');extra(p,'first-three','Tuple(8/10,8/100,8/1000)','Tuple(Rational(4,5),Rational(2,25),Rational(1,125))')
p2=v('a-fraction','summation(8*Rational(1,10)**k,(k,1,oo))','Rational(8,9)',84,'Independentlysumtheplace-valuetail8/10+8/100+…. Equivalentnon-seriescheck:10z−z=8,givingz8/9.')
p3=v('b-mixed-fraction','Rational(42,10)+summation(Rational(68,1000)*Rational(1,100)**(k-1),(k,1,oo))','4+Rational(133,495)',84,'Nativeoriginal4.2overline68hasnonrepeatingprefix4.2andrepeatingtail0.068+0.00068+…. Itis2113/495=4+133/495,not4.overline268.')
r=add('Example',34,84,'Convert0.overline8toaseriesandreducedfraction,and4.2overline68toamixedfraction. Theduplicatedstem(a)labelsareexplicit.',[p,p2,p3],[]);supporting_decimal(r)
for n,note,specs in [(1,'Convertthreepurelyrecurringdecimalblockstoreducedfractions; native dotgroupingsandhintsspecifytheblocks.', [('a','0','Rational(4,10)','Rational(1,10)','Rational(4,9)'),('b','0','Rational(54,100)','Rational(1,100)','Rational(6,11)'),('c','0','Rational(234,1000)','Rational(1,1000)','Rational(26,111)')]),(2,'Convertfourmixedrecurringdecimalswithdifferentnonrepeatingprefixesandblocklengths;retainwholenumberparts.', [('a','Rational(8,10)','Rational(2,100)','Rational(1,10)','Rational(37,45)'),('b','Rational(55,10)','Rational(62,1000)','Rational(1,100)','5+Rational(557,990)'),('c','Rational(231,10)','Rational(783,10000)','Rational(1,1000)','23+Rational(33,185)'),('d','Rational(321,100)','Rational(78,10000)','Rational(1,100)','3+Rational(719,3300)')])]:
 ps=[]
 for label,prefix,first,ratio,key in specs:
  ps.append(v(label,'('+prefix+')+summation(('+first+')*('+ratio+')**(k-1),(k,1,oo))',key,596,'Readthenativerecurringdots:separatetheprefix'+prefix+'fromfirsttailblock'+first+'andplace-valueshift'+ratio+'. Independentlysumthatconvergenttailandreduceexactly. A place-valueequationisanalternative;donotusefloatingrepeateddigits.'))
 r=add('Try-Now-34',n,84,note,ps,[]);supporting_decimal(r)
p=money('end-fifty-years','summation(500*Rational(21,20)**k,(k,1,50))','109907.70',85,'Theworkedsourceassumes50annualdepositsatBEGINNINGSOFyears,eachaccruingbetween1and50yearsofinterestatvaluation. Sum500(1.05)^kfork1..50,androundonlyfinalcurrency. Thestemdoesnotspecifydepositdates;end-of-yearpaymentswouldusek0..49andinsteadproduce104674.00.')
extra(p,'end-of-year-payment-alternative','summation(500*Rational(21,20)**k,(k,0,49))',str(compute({'kind':'identity','operands':['summation(500*Rational(21,20)**k,(k,0,49))']})))
r=add('Example',35,85,'Sum50annualinvestmentsat5%undertheworkedsource’sbeginning-of-yearpaymentconvention;retainthestem’stimingambiguity.',[p],[MODEL,GPTERM]);r['source_interpretation']='Thekey109907.70isconditionalonbeginning-of-yearpayments. With50end-of-yearpayments,thevalueis104674.00. Deposit/credit/valuationdatesmustbeexplicitinafutureauthoringcontract.'
p=v('a-contribution-series','Tuple(1000*Rational(27,25),1000*Rational(27,25)**2,1000*Rational(27,25)**3)','Tuple(1080,Rational(5832,5),Rational(157464,125))',596,'Thebookordersfinalaccumulatedcontributionsby1,2,3yearsofgrowth,notbychronologicaldepositdate. Underitsbeginning-of-yearconvention,firstterms1080,1166.4,1259.712arecorrect;reversingthe10contributionspreservesthetotal.')
p2=money('b-total','summation(1000*Rational(27,25)**k,(k,1,10))','15645.49',596,'Sum10annual1000paymentsgrownfor1..10yearsat8%. Thebook’stimingconventionisconditional,notanunambiguousconsequenceofyear-by-yearwording.')
r=add('Try-Now-35',1,85,'Writethefirstthreeaccumulated-contributiontermsandsum10annualprizeinvestmentsat8%,underthebook’spaymenttiming.',[p,p2],[MODEL,GPTERM]);r['source_interpretation']='Intendedbeginning-of-yearpaymentsgiveinterestdurations1..10;end-of-yearpaymentswouldgivedurations0..9. Thequestionmustspecifytimingbeforeunconditionalreuse.'
p=money('end-2012-total','summation(8000*Rational(107,100)**k,(k,1,19))','319963.94',596,'1994through2012inclusivecontains19deposits. Underthebook’sbeginning-of-yearconvention,theirend2012valuesgrowfor19through1years. Sumthose19contributions;end-of-yearpaymentswouldgivedurations18through0andtotal299031.72.')
r=add('Try-Now-35',2,85,'Findtheend2012valueofannualinvestmentsbeginningin1994,retaininginclusiveyearcountandpaymenttiming.',[p],[MODEL,GPTERM]);r['source_interpretation']='19annualpaymentsarecounted,buttheirinterestdurationsdependontheunspecifieddepositdate. Key319963.94usesbeginning-of-yearpayments;end-of-yearalternative299031.72staysinternal.'
p=money('a-A-five-years','1250*Rational(26,25)**5','1520.82',596,'Aissingleinitial1250compoundedat4%for5end-of-yearcredits,notanannualnewdeposit.')
p2=v('b-A-first-exceedance','floor(log(Rational(8,5))/log(Rational(26,25)))+1','12',596,'ForA,1250(1.04)^j>2000meansj>log_(1.04)(8/5). Leastwholeyear12;theinitialbalanceisj0.')
extra(p2,'adjacent-A-tests','Tuple(1250*Rational(26,25)**11<=2000,1250*Rational(26,25)**12>2000)','Tuple(True,True)')
p3=v('c-B-first-exceedance','floor((2000-1250)/70)+1','11',596,'Baddsafixed70eachyear,so1250+70j>2000requiresj>75/7;leastinteger11.')
p4=reasoning('d-eventual-comparison','Yes:after18yearsAexceedsB.','Atj18,theoriginalmodels giveA1250(1.04)^18≈2532.27andB1250+70·18=2510. ThisexplicitcounterexampletoAalwaysbelowBsufficesfortheaskedeverquestion. Exponentialgrowthversuslinearadditionsalsoexplainswhythiscanhappen;justsayingr>1withouttheBmodelisnotageneralcomparisonproof.',596,'matches')
extra(p4,'witness-inequality','1250*Rational(26,25)**18>1250+70*18','True')
r=add('Try-Now-35',3,85,'Comparetwoaccounts:compoundpercentagegrowthversusfixedannualincrements. Findbalances,thresholdyears,andaneventual-comparisonwitness.',[p,p2,p3,p4],[MODEL,GPTERM,APTERM],continuation=[86])
for p in r['subparts'][2:]:p.update(source_pdf_page=86,source_evidence=ev(86))
p=v('a-third-impact-distance','1+2*summation(Rational(2,3)**k,(k,1,2))','3+Rational(2,9)',86,'Thethirdfloorimpactcontainsinitialdrop1plusTWOcompleteup/downreboundsofrisingheights2/3and4/9. Donotdoubletheinitialdroporincludeathirdreboundaftertheaskedimpact.');p['check_mode']='show/prove'
p2=v('b-total-bound','1+2*summation(Rational(2,3)**k,(k,1,oo))','5',86,'Afterinitialdrop1,everycompletebouncecontributestwiceitsheight. Theinfiniteheighttailstarts2/3withratio2/3and sums2;totalbound1+2·2=5m. Everyfiniteimpactdistanceisbelow5,sotheaskedcannotexceedclaimholdsunderidealconstantreboundratio.');p2['check_mode']='show/prove'
r=add('Example',36,86,'Modelinitialdropandpairedup/downrebounds,thenestablishthird-impactdistanceandaninfinitetotal-distancebound.',[p,p2],[MODEL,GPTERM,INFINITE],components=[CONVERGE])
for p in r['subparts']:p['units']='m';p['printed_key_units']='m'
p=v('total-bound','1+2*summation(Rational(9,10)**k,(k,1,oo))','19',596,'The1minitialdropoccursONCE;eachlaterheight(0.9)^kiscoveredupanddown. Infinitebound1+2·[0.9/(1−0.9)]=19m. Allfinitepartialdistancesarebelowthatbound;themodelignoresphysicalstopping.');p['check_mode']='show/prove';p['units']='m';p['printed_key_units']='m'
add('Try-Now',36,86,'Showthe19mtotal-distanceboundforaballreboundingto9/10ofeachpreviousheight;preservetheunpairedinitialdrop.',[p],[MODEL,INFINITE],components=[CONVERGE])
p=v('a-x','solve(x**2-(x+5)*(x-4),x)[0]','20',596,'TheoriginalthreeGPtermsx+5,x,x−4give x²=(x+5)(x−4),hencex20. Alloriginalterms25,20,16arenonzeroandpositive.')
p2=v('b-ratio','20/(20+5)','Rational(4,5)',596,'Useconsecutiveoriginalterms20/25=4/5;independently16/20agrees.')
p3=v('c-infinite-minus-twenty','summation(25*Rational(4,5)**(k-1),(k,1,oo))-summation(25*Rational(4,5)**(k-1),(k,1,20))','1.44',596,'Computeinfinite125minusoriginalfirst20sumexactly,thenroundthepositiveleftovertailtotherequested2dp. Itis125(4/5)^20≈1.44115,notaninfinite-minus-term20difference.');p3['operation']={'kind':'rounded','operands':p3['operation']['operands'],'decimal_places':2}
add('Exercise-2.1',1,87,'FindaGPparameterandratio,thenitsremainingtailafter20termswithanexplicit2dpanswer.',[p,p2,p3],[GPTERM,INFINITE],components=[CONVERGE])
add('Exercise-2.1',2,87,'Evaluatethefinitepower-of3sigmawithbounds4..12andshowworking.',[v('sum','summation(3**(k-2),(k,4,12))','88569',596,'Thefirsttermis9,last3^10andcount9. Independentlysumtheoriginalpowers;equivalentGPformula9(3^9−1)/2=88569.')],[EVALUATE],components=[INTERPRET,GPTERM])
p=v('infinite-sum','summation(Rational(3,10)**(6+2*(k-1)),(k,1,oo))','Rational(801,1000000)',596,'Originalterms(0.3)^6,(0.3)^8,(0.3)^10havefirst0.3^6andratio0.3²=0.09. Independentlysuminfiniteandcomparewiththekey’slabelled8.01×10^−4(3sf),retainingtheexactvalue.');p['operation']={'kind':'rounded','operands':p['operation']['operands'],'significant_figures':3};extra(p,'exact-sum','Rational(3,10)**6/(1-Rational(9,100))','Rational(729,910000)')
add('Exercise-2.1',3,87,'SumtheinfiniteGPwhosedecreasingpowersincreaseby2,soitsratiois0.09ratherthan0.3.',[p],[INFINITE],components=[CONVERGE])
p=v('third-term','12*Rational(1,4)*Rational(1,4)**2','Rational(3,16)',596,'Froma12randS∞4,wehave12r=4(1−r),sor1/4anda3. Thisrconverges;T3=ar²=3/16.')
extra(p,'recover-ratio','solve(12*x-4*(1-x),x)[0]','Rational(1,4)')
add('Exercise-2.1',4,87,'UsearelationbetweenGPfirsttermandratio,plusaninfinite sum,torecoverits thirdterm.',[p],[INFINITE,GPTERM],components=[CONVERGE])
p=v('a-a-in-d','solve((4*a+6*b)-3*(a+3*b),a)[0]','3*b',596,'Theoriginalsumfirst4is4a+6d,and3timesT4is3a+9d;equategivinga3d. Checkerbstandsford.')
system='solve([a-3*b,a+17*b-3],(a,b))'
p2=v('b-first-difference','Tuple('+system+'[a],'+system+'[b])','Tuple(Rational(9,20),Rational(3,20))',596,'UsethegivenT18=3togetherwitha3d;solvejointly,retaininga9/20,d3/20.')
p3=v('c-S16','summation(Rational(9,20)+(k-1)*Rational(3,20),(k,1,16))','25+Rational(1,5)',596,'IndependentlysumtheoriginalAPwiththerecoveredconstants;S16=126/5.')
add('Exercise-2.1',5,87,'EstablishasymbolicAPrelationshipfromafirst-four/term-fourcondition,thenrecoverconstantsandfirst16sum.',[p,p2,p3],[APTERM])
p=v('a-slab-count','1+(Rational(124,100)-Rational(79,100))/Rational(25,1000)','19',596,'Useconsistentmetresand18incrementsbetween0.79and1.24;19slabs. Positivityandintegercountarechecked.')
p2=v('b-path-length','summation(Rational(79,100)+(k-1)*Rational(25,1000),(k,1,19))','19.285',596,'Sum19actualslablengths,end-to-endwithnogapsoroverlap:19.285m.');p2['units']='m';p2['printed_key_units']='m'
p3=money('c-total-cost','19*(Rational(20160,100)+324)/2','4993.20',596,'Pricesspan201.60to324in19APterms;sumtheendpointaverage×19independentlyoflengthunits.');
add('Exercise-2.1',6,87,'Recoveraslabcount,totallengthandtotalpricefromtwoconnectedAPswithdifferentunits.',[p,p2,p3],[MODEL,APTERM])
p=v('longest-side','4*(2*280/(8*(1+4)))','56',596,'Letshortestaandlongest4a;8APsidessum8(a+4a)/2=280,givinga14,longest56cm. Longest56<224sumofothers,sothepolygonisfeasible.');p['units']='cm';p['printed_key_units']='cm'
add('Exercise-2.1',7,87,'FindthelongestsideofanAP-sidedoctagonfromitsperimeterand4:1extremeratio.',[p],[MODEL,APTERM])
refs=[
 (42,84,'Recurring decimal place-value series','Theworked0.overline8tailhasratio1/10;4.2overline68hasprefix4.2andtailfirst0.068,ratio1/100. Dotpositionsandblocklengthmustvaryconsistentlywiththetail;fractionconversionaloneissupportingpractice,notproofthataconvergentGPmethodwasassessed.',[INFINITE],'table',[('Rational(42,10)+Rational(68,1000)/(1-Rational(1,100))','4+Rational(133,495)')],'Example:34'),
 (43,85,'Annual deposit timing and contribution values','Theworkedseries525,551.25,578.8125,…usesfinalcontributionsgrownfor1,2,3,…yearsat5%,equivalenttobeginning-of-yearannualpayments. End-of-yearpaymentsstart500instead525. Thecash-flowdatesarenotfixedbyannualalone.',[MODEL,GPTERM],'table',[('Tuple(500*Rational(21,20),500*Rational(21,20)**2,500*Rational(21,20)**3)','Tuple(525,Rational(2205,4),Rational(9261,16))')],'Example:35'),
 (44,86,'Bouncing ball impact and paired-distance diagram','Theworkedfigurehasanunpaired1minitialdownwardarrow,andup/downpairsat2/3,4/9,8/27,…m. Eachsuccessiveheightismultipliedby2/3. Toimpact3,includeonlythefirsttwopairs;aninfinitetotalincludesallpairs. Arrows,impactlabelsandheightsmustremainconsistent.',[MODEL,GPTERM,INFINITE],'diagram',[('1+2*(Rational(2,3)+Rational(4,9))','3+Rational(2,9)')],'Example:36'),
 (45,86,'Ball total-distance bound reference','Suminfiniteofpairedheights(4/3)+(8/9)+(16/27)+…is4m;addingtheinitial1mgives5. Theinitialdropmustnotbedoubledandthefirstreboundmustnotbecutoff.',[MODEL,INFINITE],'table',[('summation(2*Rational(2,3)**k,(k,1,oo))','4')],'Example:36')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
 if f['item_id'].endswith(':44'):f['item_kind']='teaching-figure';f['asset_role']='Worked-solutiondiagram,notagivenintheoriginalprompt.'
 if f['item_id'].endswith(':44'):
  crop=W/'checks/r5/textbooks/YM-C2-bouncing-diagram-native.png';f['source_evidence_native']={'path':str(crop.relative_to(W.parents[2])),'sha256':hashlib.sha256(crop.read_bytes()).hexdigest(),'crop_box_pdf_points':[60,315,500,410],'inspection':'Codex author visually read all arrows,impact labels and height values; independent acceptance pending.'}
notes={84:'EveryExample34andTry34Q1/2responseandplace-valuereferencerecorded. Nativedotgroupschecked;fractionconversionkeptassupportingpracticebecauseGPmethodisnotrequiredbytheprompt.',85:'EveryExample35,Try35Q1/2andTry35Q3startrecorded. Cash-flowtimingisexplicitlyconditional;Try35Q3continues86.',86:'Try35Q3(c/d)continuation,Example36,itsbouncearrowsandtotalsumreference,andTry36proofallaccountedfor.',87:'AllExercise2.1Q1–7responsesrecordedwithkey596. BareAP/GPoutputsandphysicalslab/polygonmodelsdistinguished. RemainingExercise2.1questionsstart88.'}
pages=[]
for page in range(84,88):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:YM:C2:Try-Now-35:3']if page==86 else[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Alltasks,continuationsandmathematicalteachingassetsrecorded. Supportingdecimalpracticeisnotautomaticallydirect8227coverage;investmenttiming,initialdropparity,unitsandfinite/infiniteprecisionareexplicit.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-finance-bounce.json',{'scope':'Every84–87requestedresponseandteachingasset.','items':answers}),('census-YM-C2-finance-bounce.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete84–87pagecensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
