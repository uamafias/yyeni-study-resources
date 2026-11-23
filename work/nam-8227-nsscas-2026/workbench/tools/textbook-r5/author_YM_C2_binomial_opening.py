"""YM89–91: complete Pascal investigation and first binomial expansion tasks."""
import json
import author_YM_C2_progression_closing as prior
import author_YM_C1_opening as common
from author_YM_C2_progression_closing import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear();prior.prior.prior.prior.prior.base.base.base.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
BINOM='8227:2020:M1:T2:O01:D01';COEF='8227:2020:M1:T2:O01:D02';COMBINED='8227:2020:M1:T2:O01:D03'

def scope(row,powers):
 row['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'within','quoted_value':'Original outer binomial exponents: '+powers,
  'reason':'The explicitly expanded powers are positive integers. Given exponent0is a boundary reference,not a rational-power infinite expansion. No arbitrary grade/difficulty bound is inferred from this qualifier.'}]
 row['mapping_rationale']='Full expansion,requestedcoefficientandcombined-productcoefficientaredifferentoutcomes. ConceptualPascalpatternobservationsremainexplicitfacet/supportinglabels;usingthetriangledoesnotcreateseparatecoefficientcoverageunlessthatoutputisasked. Exponentsinsidecoefficientsarenottheouterbinomialpower.'
 row['precision_angle_check']={'source':'Exactpolynomialandrationalcoefficients;noangleunitsorrounding.','comparison':'Preservetermsigns,nonzerodenominatorsandtherequestedorder/truncation. Coefficientofapowerisnotthesignedtermcontainingthatpower.'}
 return row

def add(kind,n,page,note,parts,direct,powers,components=None):return scope(prior.add(kind,n,page,note,parts,direct,components),powers)

def poly(label,source,key,kp=596,method=None):
 return v(label,'expand('+source+')',key,kp,method or'Independentlydistributetheoriginalpositive-integerbinomialproductandcollectliketerms. Compareeverycoefficientandpowerwiththeseparatelytranscribedsourcekey. A Pascalrowisthebook’smethod;thesignscomefromtheactualsecondterm.')

def nokey(label,conclusion,derivation):
 return reasoning(label,conclusion,derivation+' Thechapter2answerpages594–597containnoInvestigationheadingoraseparateanswerforthissubtask. Source90/91illustrationsareusedonlywhereexplicitlynoted;nostudenthandwritingiscertifiedasapublisheranswer.',596,'no key')
ps=[]
for label,n,target in [('1-a',3,'a**3+3*a**2*b+3*a*b**2+b**3'),('1-b',4,'a**4+4*a**3*b+6*a**2*b**2+4*a*b**3+b**4'),('1-c',5,'a**5+5*a**4*b+10*a**3*b**2+10*a**2*b**3+5*a*b**4+b**5'),('1-d',6,'a**6+6*a**5*b+15*a**4*b**2+20*a**3*b**3+15*a**2*b**4+6*a*b**5+b**6')]:
 p=nokey(label,target,'Thepromptrequiresactualmultiplication,soindependentlydistribute'+str(n)+'copiesof(a+b),thencombinepowersofeachvariable. Do notjustifythisfirstexplorationonlybyquotingthetheoremitisdiscovering.')
 extra(p,'distributed-original-product','expand('+('*'.join(['(a+b)']*n))+')',target);p['assessed_8227_demand_ids']=[BINOM];ps.append(p)
for n,coeffs in [(3,'Tuple(1,3,3,1)'),(4,'Tuple(1,4,6,4,1)'),(5,'Tuple(1,5,10,10,5,1)'),(6,'Tuple(1,6,15,20,15,6,1)')]:
 p=reasoning('2-row-'+str(n),coeffs,'Completeeachrequestedblankcoefficientrowfromtheactualexpandedproducts. ThesubsequentpublisherPascaltriangleonPDF90explicitlyprintstheserowsandservesasinlinecomparison;fainthandwrittenanswersonthe89worksheetarenotusedasofficialkeys.',90,'matches')
 extra(p,'coefficients-from-distribution','Tuple('+','.join('expand((a+b)**'+str(n)+').coeff(a,'+str(n-j)+').coeff(b,'+str(j)+')'for j in range(n+1))+')',coeffs);p['assessed_8227_demand_ids']=[COEF];ps.append(p)
for label,conclusion,method in [
 ('3-a','Exponent-nrowhasn+1entries/terms.','Useexponentlabelsstartingn0:choosingj0..ngivesn+1positions. Ordinalrowcountstarting1wouldshiftthatformula;thesource’snlabelsaretheauthority.'),
 ('3-b','Firstentryis1.','In(a+b)^n,theall-afactorchoiceoccursinoneway,givingcoefficient1ona^n.'),
 ('3-c','Lastentryis1.','Theall-bfactorchoiceoccursinoneway,givingcoefficient1onb^n.'),
 ('3-d','Eachrowispalindromic.','Swapallchoicesofaandb;thesamecountappearsatpositionsjandn−j. Theprintedtriangle90providesexamplesbutthesymmetryclaimneedsanexplanation,notjustavisualguess.'),
 ('3-e','Eachinteriorentryisthesumofthetwoadjacententriesabove;endpointsremain1.','Multiplyingthen−1productby(a+b)makeseachcoefficientfromoneprioratimeschoiceandonepriorbtimeschoice. ThisgivestherecurrenceC(n,j)=C(n−1,j)+C(n−1,j−1).'),
 ('3-f','Yes;row10is1,10,45,120,210,252,210,120,45,10,1.','Repeatedadjacentadditionconstructsrow10andthecorresponding11termpolynomial. Thequestionaskswhetherthiscanbedone,notnecessarilytoreproduceanentireexpansionhere. Example37(b)90laterusesthisrowwithalternatingsigns.'),
 ('3-g','Thismethodisfiniteandpracticalforsmallnonnegativeintegerpowers;buildingmanyrowsislaboriousforlargepowers.','Noarbitrarymaximumexponentexistsmathematically. ThefinitePascaltrianglealgorithmdoesnotdirectlygiveafiniteexpansionfornegative/nonintegerpowers;thoseextensionsarenotprescribedhere. Thisisanefficiency/scopeobservation,notanewsyllabuslimit.')]:
 p=nokey(label,conclusion,method);p['assessed_8227_demand_ids']=[];p['teaches_8227_demand_ids']=[BINOM,COEF];ps.append(p)
extra(ps[-3],'Pascal-recurrence-check','binomial(10,5)-binomial(9,5)-binomial(9,4)','0')
extra(ps[-2],'row-ten','Tuple('+','.join('binomial(10,'+str(j)+')'for j in range(11))+')','Tuple(1,10,45,120,210,252,210,120,45,10,1)')
r=common.add('Investigation',1,89,'CompleteallPascalinvestigationsubtasks:fourrepeated-productexpansions,fourcoefficientrows,andsevenpattern/limitationsresponses. Nopublisheranswerisclaimedfortheauthor-derivedlogicalresponses.',ps,[BINOM,COEF])
r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C2:');new[-1]['item_id']=r['item_id'];new[-1]['item_kind']='investigation';scope(r,'3,4,5,6;conceptualrow10;givenboundaryrows0,1,2')
for p in r['subparts']:
 if p['author_comparison_status']=='no key':p.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[594,595,596,597],key_evidence=ev(596))
r['component_demand_ids']=[];r['teaches_8227_demand_ids']=[BINOM,COEF]
add('Example',37,90,'Expandtwohighpositive-integerpowersusingPascalrows8and10;preserveeverytermandsignalternation.',[
 poly('a','(x+y)**8','x**8+8*x**7*y+28*x**6*y**2+56*x**5*y**3+70*x**4*y**4+56*x**3*y**5+28*x**2*y**6+8*x*y**7+y**8',90),
 poly('b','(a-b)**10','a**10-10*a**9*b+45*a**8*b**2-120*a**7*b**3+210*a**6*b**4-252*a**5*b**5+210*a**4*b**6-120*a**3*b**7+45*a**2*b**8-10*a*b**9+b**10',90)],[BINOM],'8,10')
p=reasoning('a','a^7+7a^6b+21a^5b²+35a^4b³+35a³b^4+21a²b^5+7ab^6+b^7;checkerastandsforsourcep,bforsourceq.',
 'ThepromptasksFULL(p+q)^7expansion. Nativekey596printsonlylastthreeterms21p²q^5+7pq^6+q^7,withnoellipsis. Thoseprintedtermsarecorrectbutfiveleadingtermsaremissing. Independentlydistributetheoriginalpowerandlistall8terms.',596,'key incomplete')
extra(p,'full-expansion','expand((a+b)**7)','a**7+7*a**6*b+21*a**5*b**2+35*a**4*b**3+35*a**3*b**4+21*a**2*b**5+7*a*b**6+b**7')
p2=poly('b','(a-b)**9','126*a**4*b**5+84*a**3*b**6-36*a**2*b**7+9*a*b**8-b**9',596,'Checkerastandsforsourcek,bforsourcem. Nativekey596omitstheleadingfourterms,anditsretained126k^4m^5haswrongpositivesign;thecorrectj5signisnegative. Independentlyexpandall9factors.')
p2['author_expected_normalised']='a**9-9*a**8*b+36*a**7*b**2-84*a**6*b**3+126*a**5*b**4-126*a**4*b**5+84*a**3*b**6-36*a**2*b**7+9*a*b**8-b**9'
p3=reasoning('c','Thetwoexponentsineachmonomialsumtotheoriginalouterbinomialpower.','In(a+b)^n,atermchoosingjsecondfactorshasfirstexponentn−jandsecondj,theirtotaln. Thisstatementdescribestotaldegree,notcoefficientvalueandnotasumofexponentsinaone-variablebinomialcontainingaconstant.',596,'matches');extra(p3,'degree-sum','(n-x)+x','n')
r=add('Try-Now-37',1,90,'Expand(p+q)^7and(k−m)^9fully,anddescribehomogeneoustotaldegree. Thefirsttwokeysaretruncated;thesecondalsohasasignerror.',[p,p2,p3],[BINOM],'7,9');r['source_symbol_basis']={'a':'pfor(a),kfor(b)','b':'qfor(a),mfor(b)'}
add('Try-Now-37',2,90,'UsePascalrow6forexpanding(1+b)^6andhencededucethealternatingsignexpansion(1−y)^6.',[
 poly('a','(1+b)**6','1+6*b+15*b**2+20*b**3+15*b**4+6*b**5+b**6'),poly('b','(1-y)**6','1-6*y+15*y**2-20*y**3+15*y**4-6*y**5+y**6')],[BINOM],'6')
add('Try-Now-37',3,90,'Expand(a−1)^8fullywithalternatingsignsandconstantterm1.',[poly('expansion','(a-1)**8','a**8-8*a**7+28*a**6-56*a**5+70*a**4-56*a**3+28*a**2-8*a+1')],[BINOM],'8')
add('Example',38,91,'Expandthreebinomialswithscaled,signedandfractionalterms;rowcoefficientsalonearenotthefinalcoefficients.',[
 poly('a','(2*x+3*y)**3','8*x**3+36*x**2*y+54*x*y**2+27*y**3',91),poly('b','(a-3)**4','a**4-12*a**3+54*a**2-108*a+81',91),poly('c','(1+p/2)**5','1+Rational(5,2)*p+Rational(5,2)*p**2+Rational(5,4)*p**3+Rational(5,16)*p**4+Rational(1,32)*p**5',91)],[BINOM],'3,4,5')
ps=[poly('a','(1+3*a)**7','1+21*a+189*a**2+945*a**3+2835*a**4+5103*a**5+5103*a**6+2187*a**7'),poly('b','(a+2*b)**3','a**3+6*a**2*b+12*a*b**2+8*b**3'),poly('c','(3*a-1)**4','81*a**4-108*a**3+54*a**2-12*a+1'),poly('d','(a-b/2)**5','a**5-Rational(5,2)*a**4*b+Rational(5,2)*a**3*b**2-Rational(5,4)*a**2*b**3+Rational(5,16)*a*b**4-Rational(1,32)*b**5'),poly('e','(2*a+1/b)**4','16*a**4+32*a**3/b+24*a**2/b**2+8*a/b**3+1/b**4'),poly('f','(a/3-b)**4','a**4/81-Rational(4,27)*a**3*b+Rational(2,3)*a**2*b**2-Rational(4,3)*a*b**3+b**4')]
r=add('Try-Now',38,91,'Expand6scaledbinomials,includingnegativefractionaltermsandareciprocalcoefficient1/b;retainb≠0inthatbranch.',ps,[BINOM],'7,3,4,5,4,4');r['scope_check']['basis']+=' Inpart(e),theoriginal1/brequiresb≠0;outerpower4isstillapositiveinteger.'
p=v('a-through-a-squared','expand((1+2*a)**5).series(a,0,3).removeO()','1+10*a+40*a**2',91,'Retainascendingpowers0,1,2only,withanellipsisforhigherpowersinthefullanswer. Thetruncationdoesnotsaythefullfifth-degreepolynomialisquadratic.')
p2=v('b-product-coefficient','expand((1-3*a)**2*(1+2*a)**5).coeff(a,2)','-11',91,'Independentlymultiplytheoriginalproductandextractcoefficientofa². Thebook’sefficientmethodonlyneedsexponentpairs(0,2),(1,1),(2,0),giving40−60+9=−11. Coefficient−11isnotterm−11a².')
add('Example',39,91,'Expandthrougha²,thenfindthea²coefficientofaconnectedproductbyallcontributingpowerpairs.',[p,p2],[BINOM,COMBINED],'5,2',components=[COEF])
refs=[
 (47,89,'Binomial square introductory reference','Thegiven(a+b)²=a²+2ab+b²recallsanOrdinary-Levelprerequisitebeforehigherpowers. Itisateachingreference,notanadditionallearnerprompt.',[BINOM],'table',[('expand((a+b)**2)','a**2+2*a*b+b**2')],None),
 (48,89,'Pascal investigation completion frame','Theworksheetgivesexponentrows0,1,2andblanksfor3..6,alignedwithfull(a+b)^nforms. Handwrittenfillsarenotpublisheranswers. Correctrowcountandcoefficientpositionsmustmatchtheexponentlabels.',[BINOM,COEF],'table',[('Tuple(binomial(3,0),binomial(3,1),binomial(3,2),binomial(3,3))','Tuple(1,3,3,1)')],'Investigation:1'),
 (49,90,'Printed Pascal triangle and adjacent addition','Theprintedrows0..6showendpoints1,symmetryandtwoadjacententries6+4combiningto10inthefollowingrow. Exponent0isagivenboundaryreference,notapositive-powerassessedexpansion.',[BINOM,COEF],'table',[('6+4','10')],None),
 (50,90,'Example37 Pascal row lookup','Theworkedlookuptriangleincludesrows8and10usedbythetwofull-expansiontasks. Thehighlightedcoefficientrowisnotthesameasthecompletepolynomial;variablesandsignsarestillrequired.',[BINOM,COEF],'table',[('binomial(8,4)','70')],'Example:37'),
 (51,90,'Exponent descent and ascent callout','For(x+y)^8,thexexponentsrun8..0whileyexponentsrun0..8. Thereare9genericterms,not8;thetwopowersineachtermsumto8.',[BINOM],'table',[('Tuple(8+0,7+1,0+8)','Tuple(8,8,8)')],'Example:37'),
 (52,90,'Signed-binomial warning','For(a−b)^nwithapositiveintegerouterpowerandsymbolica,b,theformalcoefficientsalternate+and−startingwitha^n. Numericvaluesofnegativeaorbdonotjustifydroppingtheiroriginalsignsduringdistribution.',[BINOM],'table',[('expand((a-b)**3)','a**3-3*a**2*b+3*a*b**2-b**3')],'Example:37'),
 (53,91,'Example38 small Pascal lookup triangle','Theprintedtriangleupthroughrow5providescoefficientrows3,4,5fornonunitbinomialterms. Powersof2,3or1/2multiplythosecoefficients;thetrianglealoneisnotafinalanswer.',[BINOM,COEF],'table',[('binomial(5,2)/2**2','Rational(5,2)')],'Example:38'),
 (54,91,'Example38 minus-sign and unit-coefficient callouts','Onecalloutallowsomittingwrittenunitcoefficients;anothertracksalternatingsignsin(a−3)^4. Omitonlythecoefficient1,notaterm,variablepowerorminusonoddpowers.',[BINOM],'table',[('expand((a-3)**4).coeff(a,3)','-12')],'Example:38'),
 (55,91,'Truncated expansion and product power-pair selection','Example39retains1+10a+40a²+…andmultipliesonlythetermswhosecombineddegreeis2with1−6a+9a². Contributions40,−60,9sum−11. Highertermscannotcontributetodegree2becausebothfactorshavenonnegativepowers.',[BINOM,COMBINED],'table',[('40-60+9','-11')],'Example:39')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[];f['item_kind']='teaching-figure'
notes={89:'AllbinomialintroductoryreferenceandtheentirePascalinvestigation(1a–d,rows3–6,3a–g)enumerated;previousinventorymissedthisunnumberedInvestigation. Noauthor-selectedreviewsampleiscreated.',90:'EveryExample37andTry37Q1–3response,printedtriangle,lookupandtwoexponent/signcalloutsrecorded. NativeTry37keytruncationsandretainedsignerrorareexplicit.',91:'EveryExample38,Try38(a–f)andExample39(a/b)responsepluslookup/sign/truncationteachingreferencesrecorded. Reciprocalcoefficientb≠0retained;combinedcoefficientisdistinctfromafullproductexpansion.'}
pages=[]
for page in range(89,92):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Allbinomialtasksandmathematicalreferencesrecorded. Originalexpandedpowersarepositiveintegers;givenrow0isboundarysupport. Full/truncated/combined-coefficientoutputsandmanualconceptualresponsesarekeptdistinct.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-binomial-opening.json',{'scope':'Every89–91responseincludingallpreviouslyuncataloguedInvestigationsubtasks.','items':answers}),('census-YM-C2-binomial-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete89–91pagecensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
