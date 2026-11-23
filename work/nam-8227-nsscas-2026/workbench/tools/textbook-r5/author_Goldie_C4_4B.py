"""Fixed-source Exercise4B1–12, Goldie PDF108–110; no generated questions."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_Goldie_C4_opening import derivative
from author_Goldie_C4_4A import stat,at_deriv,at,tangent
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02'
POWER='8227:2020:M1:T8:O02:D01';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02'
TANGENT='8227:2020:M1:T8:O03:D01';NOTATION='8227:2020:M1:T8:O01:D02';RATE='8227:2020:M1:T8:O03:D03';SKETCH='8227:2020:M1:T3:O05:D01'
ATTR={10:'9709,Paper2Q6,November2008',11:'9709,Paper2Q6,June2008',12:'9709,Paper22Q5,June2010'}
def ev(page):
    name='Goldie-key-C3-341'if page==343 else'Goldie-C4-110'if page==110 else'Goldie-C4-106'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(n,page,note,parts,direct,components=None,sketch=False,rep='text'):
    for p in parts:
        kp=p.pop('key_page_override',343);p.pop('source_page_override',None)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Exercise-4B:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Classify actual derivative,rate,stationary,classification,sketch or symmetry decisions. A point wheref″=0isnotautomatically a stationary point(f′=0). An individual given stationary abscissa isnot an all-stationary-points task. Optional log rewrites retain the original real domain.',
      'representation':rep,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within','quoted_value':note,'reason':'Polynomial/reciprocal/radical powers appearing as components are rational. Natural-log arguments must remain positive; no negative branch is removed just to use a convenient log law.'},
       {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'No change of logarithm base.'},
       {'rule_id':'8227:QUAL07','status':'not applicable','quoted_value':note,'reason':'Original function domains are preserved;no standalone range output is requested.'}],
      'exam_style':n in ATTR,'exam_style_basis':'Printed textbook attribution:'+ATTR[n]+'. Internal lead,not a new original-paper provenance verification.'if n in ATTR else'Ordinary exercise;no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Exact answers except4B3rate values,whose key uses3sfandmetres per hour. The river model is supplied onlyfor0≤t≤3hours.',
        'comparison':'Keep exact exp/log values until final rounding. Graphs preserve excluded0/poles andone-sided limits. Source graph limitations are disclosed separately from correct key numbers.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row
parts=[]
for label,f,key,domain in[
 ('i','3*log(x)','3/x','x>0'),('ii','log(4*x)','1/x','x>0'),('iii','log(x**2)','2/x','x≠0,both branches'),
 ('iv','log(x**2+1)','2*x/(x**2+1)','All realx'),('v','log(1/x)','-1/x','x>0'),
 ('vi','x*log(x)','1+log(x)','x>0'),('vii','x**2*log(4*x)','x*(1+2*log(4*x))','x>0'),
 ('viii','log((x+1)/x)','-1/(x*(x+1))','x<−1orx>0'),('ix','log(sqrt(x**2-1))','x/(x**2-1)','x<−1orx>1'),
 ('x','log(x)/x**2','(1-2*log(x))/x**3','x>0')]:parts.append(derivative(label,f,key,343,domain))
add(1,108,'Ten log derivatives:3lnx;ln4x;lnx²;ln(x²+1);ln(1/x);xlnx;x²ln4x;ln((x+1)/x);ln√(x²−1);lnx/x². Original domains are recorded per part,including negative components forlnx²andthelastquotient/radicalarguments where allowed.',parts,[ELEMENTARY,COMPOSITE,PRODUCT,QUOTIENT],[POWER])
parts=[]
for label,f,key in[
 ('i','3*exp(x)','3*exp(x)'),('ii','exp(2*x)','2*exp(2*x)'),('iii','exp(x**2)','2*x*exp(x**2)'),
 ('iv','exp((x+1)**2)','2*(x+1)*exp((x+1)**2)'),('v','x*exp(4*x)','exp(4*x)*(1+4*x)'),
 ('vi','2*x**3*exp(-x)','2*x**2*exp(-x)*(3-x)'),('vii','x/exp(x)','(1-x)/exp(x)'),
 ('viii','(exp(2*x)+1)**3','6*exp(2*x)*(exp(2*x)+1)**2')]:parts.append(derivative(label,f,key,343))
add(2,108,'Eight exponential derivatives:3e^x;e^(2x);e^(x²);e^((x+1)²);x e^(4x);2x³e^(−x);x/e^x;(e^(2x)+1)^3. All original real domains are unrestricted;product/quotient ornegative-exponent alternatives are valid.',parts,[ELEMENTARY,COMPOSITE,PRODUCT,QUOTIENT],[POWER])
f='3*exp(9*x/10)/25';parts=[derivative('i',f,'27*exp(9*x/10)/250',343,'0≤x≤3hours as the stated forecast interval.')]
for t,key in[(0,'0.108'),(1,'0.266'),(2,'0.653'),(3,'1.61')]:
    p=value('ii-'+str(t)+'h',at_deriv(f,str(t)),key,343,'Differentiate the supplied height model independently;substitute this exact hour andround onlythefinalrate to the printed3sf. Height is metres andtime hours,so the rate unit ism h^-1.')
    p['operation']={'kind':'rounded','operands':[at_deriv(f,str(t))],'significant_figures':3};p['units']='m h^-1';p['printed_key_units']='m h^-1';parts.append(p)
add(3,108,'A supplied river-height predictionh=0.12e^(0.9t)metres appliesoverthenext3hours,withtinhours. Finddh/dtandthewater-rise rates att=0,1,2,3hours;keyrates use3sfandm h^-1.',parts,[RATE,COMPOSITE],[ELEMENTARY])
f='x*exp(x)'
add(4,108,'Given graph ofy=x e^xwithminimumP:findfirstandsecondderivatives,andcoordinatesofP. The minimum nature is supplied;an extra classification is not a separately requested response.',[
 derivative('i-first',f,'(1+x)*exp(x)',343),value('i-second',f'diff({f},x,2)','(2+x)*exp(x)',343),
 stat('ii',f,'FiniteSet(Tuple(-1,-1/E))',343)],[PRODUCT,STATIONARY,NOTATION],[ELEMENTARY],rep='graph')
f='x*log(x**2)'
p=reasoning('i','The graph has rotational symmetry of180°abouttheorigin,onits punctured domainx≠0.',
 'The domain is symmetric underx↦−xandf(−x)=−x ln((−x)²)=−xln(x²)=−f(x). Thus every defined graph point has its rotated partner. The origin itself is not in this original graph;odd symmetry doesnot require the centre to belong to the domain.',343,'matches')
p['additional_operations']={'odd_residual':{'kind':'identity','operands':[f'({f}).subs(x,-x)+({f})']}}
p['additional_operation_expected']={'odd_residual':'0'}
row=add(5,108,'Given graph off(x)=xln(x²):describe/reason symmetry;findf′andf″;findall stationary coordinates. Original domainx≠0is preserved,including the negative branch;the source given curve omits a hole at the origin. Parts continue109.',[
 p,derivative('ii-first',f,'2+log(x**2)',343,'x≠0,both real components.'),
 value('ii-second',f'diff({f},x,2)','2/x',343),stat('iii',f,'FiniteSet(Tuple(-1/E,2/E),Tuple(1/E,-2/E))',343)],
 [PRODUCT,STATIONARY,NOTATION],[ELEMENTARY],rep='graph')
row['direct_demand_aspects']=[{'role':'additional directly requested textbook symmetry decision','assessed_facet':'Prove odd-function/half-turn graph symmetry on a punctured domain;no separate core8227demand is invented.'}]
for part in row['subparts']:part['source_pdf_page']=109;part['source_evidence']=ev(109)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[109]})
f='exp(x)/x'
p=reasoning('iii','Two-branch sketch onx≠0:verticalasymptotex=0;negativebranch decreasesfrom0−to−∞;positivebranch fallsfrom+∞to minimum(1,e),thenrises to+∞.',
 'f′=e^x(x−1)/x²,negative forx<1andpositiveforx>1within each connected domain. Limits at0are−∞/+∞;at−∞thecurveapproaches0frombelow,andat+∞itgrowswithoutbound. Thereareno real zeros. The key graph hasthesefeatures.',343,'sketch')
p['additional_operations']={'asymptotic_limits':{'kind':'identity','operands':[f'Tuple(limit({f},x,-oo),limit({f},x,0,dir="-"),limit({f},x,0,dir="+"),limit({f},x,oo))']}}
p['additional_operation_expected']={'asymptotic_limits':'Tuple(0,-oo,oo,oo)'}
add(6,109,'Fory=e^x/x:find derivative,allstationarycoordinates,and sketch both originaldomainbranchesx≠0. The unique positive stationary point is a minimum;the negativebranchhasnostationarypoint.',[
 derivative('i',f,'exp(x)*(x-1)/x**2',343,'x≠0.'),stat('ii',f,'FiniteSet(Tuple(1,E))',343),p],
 [QUOTIENT,STATIONARY,CLASSIFY,SKETCH],[ELEMENTARY],True)
f='x*log(x)'
add(7,109,'Given graph off(x)=xlnx,find exactstationarycoordinates. Real domainx>0;thelimitingorigin isnot an actual function point. Derivativeworkingusesproduct/standardlogrules,butnoextraderivativeoutputorclassificationisasked.',[
 stat('point',f,'FiniteSet(Tuple(1/E,-1/E))',343)],[STATIONARY],[PRODUCT,ELEMENTARY],rep='graph')
f='x/exp(x)'
p=reasoning('ii','The stationary point(1,1/e)is a maximum.',
 'f′=e^(−x)(1−x)changespositivetonegativeat1. Alternativelyf″=e^(−x)(x−2)hasvalue−1/eat1.',343,'matches')
p['additional_operations']={'second_derivative_at_stationary':{'kind':'identity','operands':[at_deriv(f,'1',2)]}}
p['additional_operation_expected']={'second_derivative_at_stationary':'-1/E'}
add(8,109,'Fory=x/e^x,given thatthereisone stationarypoint:finditexactlyanddetermine maximum/minimum. Rewritingx e^(−x)orusingquotientrule gives equivalentvalidworking.',[
 stat('i',f,'FiniteSet(Tuple(1,1/E))',343),p],[STATIONARY,CLASSIFY],[QUOTIENT,COMPOSITE,ELEMENTARY])
f='log(x)/x'
p=reasoning('iii','Forx>0,thecurve crosses(1,0),risesfrom−∞at0+to maximum(e,1/e),thenfallstoward0+asx→∞.',
 'The original domain ispositive. Derivative(1−lnx)/x²ispositivebeforeeandnegativeaftere. The limitsare−∞at0+and0at+∞. Thereisno y-axisinterceptbecause0isoutside thedomain. Thesearethekeysketchfeatures.',343,'sketch')
p['additional_operations']={'end_limits':{'kind':'identity','operands':[f'Tuple(limit({f},x,0,dir="+"),limit({f},x,oo))']}}
p['additional_operation_expected']={'end_limits':'Tuple(-oo,0)'}
add(9,109,'Forf(x)=lnx/x,x>0:findthex-axis crossing,exactstationarycoordinates,and sketch. Preserve thepositive-domainverticalasymptote andthepeak atx=e.',[
 value('i','Tuple(solve(log(x),x)[0],0)','Tuple(1,0)',343),stat('ii',f,'FiniteSet(Tuple(E,1/E))',343),p],
 [STATIONARY,CLASSIFY,SKETCH],[QUOTIENT,ELEMENTARY],True)
f='x*exp(-x/2)';root=f'solve(diff({f},x,2),x)[0]'
p=value('point',f'Tuple({root},({f}).subs(x,{root}))','Tuple(4,4*exp(-2))',343,
 'Independentlyformthesecondderivative,solveitszeroequation,andputthatxintotheoriginalcurve. This conditionisf″=0,notf′=0;no stationary-point orclassification claimis made.')
p['additional_operations']={'first_derivative_at_answer':{'kind':'identity','operands':[at_deriv(f,'4')]},'second_derivative_at_answer':{'kind':'identity','operands':[at_deriv(f,'4',2)]}}
p['additional_operation_expected']={'first_derivative_at_answer':'-exp(-2)','second_derivative_at_answer':'0'}
row=add(10,109,'Fory=x e^(−x/2),findtheexactpointwhere d²y/dx²=0. Thepoint(4,4e^(−2))isnotstationarybecauseitsfirstderivativeis−e^(−2);do not maptheconditionto all-stationary-point coverage.',[p],[PRODUCT,COMPOSITE,NOTATION],[ELEMENTARY])
row['direct_demand_aspects']=[{'role':'second-derivative condition','assessed_facet':'Solvef″=0andrecoveracurvepoint;not a requesttoclassifyinflexionorstationality.'}]
f='(x-2)*exp(x)'
p=reasoning('ii','The stationary point(1,−e)is a minimum.',
 'f′=(x−1)e^xvanishesonlyat1. f″=x e^xhaspositivevalueeat1;orusef′changingnegative-to-positive.',343,'matches')
p['additional_operations']={'second_derivative_at_stationary':{'kind':'identity','operands':[at_deriv(f,'1',2)]}}
p['additional_operation_expected']={'second_derivative_at_stationary':'E'}
add(11,109,'Fory=(x−2)e^x,givenone stationarypoint:findexactcoordinatesanddetermine itsnature. Theproductderivativeisworking,not anextra requestedformula.',[
 stat('i',f,'FiniteSet(Tuple(1,-E))',343),p],[STATIONARY,CLASSIFY],[PRODUCT,ELEMENTARY])
f='x**3*exp(-x)'
p=value('i',at_deriv(f,'3'),'0',110,
 'Product/chainrulesgivef′=x²e^(−x)(3−x),sothegivenabscissa3haszero gradient. Thisdoesnotassertuniqueness:thereisalsoastationarypointatx=0,which thispartdoesnotasktofind.')
p['check_mode']='show/prove';p['additional_operations']={'all_stationary_coordinates_for_audit':{'kind':'stationary-points','operands':[f]}}
p['additional_operation_expected']={'all_stationary_coordinates_for_audit':'FiniteSet(Tuple(0,0),Tuple(3,27*exp(-3)))'}
add(12,110,'Fory=x³e^(−x):showthereisastationarypointwherex=3,thenfindtangentatx=1. Thetaskdoesnotaskforallstationarypoints;theadditionalx=0pointmustnotbeignoredifalateradaptationchangesthequestion.',[
 p,value('ii',tangent(f,'1'),'(2*x-1)/E',343)],[STATIONARY,TANGENT],[PRODUCT,COMPOSITE,ELEMENTARY])
figures=[]
for n,page,parent,label,note,method in[
 (13,108,4,'Exercise4B4 x exp(x)minimum graph','Giveny=x e^xpasses(0,0),hasminimumP=(−1,−1/e),approaches0frombelowasx→−∞,andriseswithoutboundasx→∞.',
  'Differentiateoriginalfunction;signof(1+x)e^xfixestheminimum. Exactlimitsandparentderivativescheckthequalitativegivencurve.'),
 (14,108,5,'Exercise4B5 punctured odd-log graph','Thegivenx ln(x²)curveisodd,withstationarypoints±1/e,butisundefinedatx=0. Thesourcecurvedrawsthroughtheoriginwithoutahole,soitsdisplayneedsexplicitdomaincorrection.',
  'Useoriginalreal-logdomainx≠0,oddidentityandstationaryequationlnx²=−2. Thelimitat0is0frombothsides,butthatdoesnotdefinetheoriginalfunctionat0;do notaddanoriginintercept.'),
 (15,109,7,'Exercise4B7 positive-domain x ln(x)graph','Givenxlnxhasdomainx>0,minimum(1/e,−1/e),androot1. Thecurveapproachesthelimitingoriginasx→0+;0isexcluded. Theunmarkedendpointintheroughsourcegraphmustnotbeassumedincluded.',
  'Derivative1+lnxgivesx=1/eandoriginalordinate−1/e;limitat0+is0. Forredraw,statepositive domainandmarktheexcludedoriginifshown. Thecurvehasnorootat0.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure','exercise':'Given figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
     'teaches_8227_demand_ids':[STATIONARY],'representation':'graph','source_evidence':ev(page),'parent_item_id':f'8227:TB:Goldie:C4:Exercise-4B:{parent}','learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL07','status':'within','quoted_value':note,'reason':'Simpleactualdomainconditionsareretained;alimitingpointisnotautomaticallyafunctionvalue.'}],
     'value_level_scope_review_status_r5':'author original-function/domain/givengraphread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internaltextbookgivengraph;notexaminationfrequencyorofficialmarkingevidence.'},
     'mathematical_feature_review':{'status':'authorsourcefeaturesandoriginal-functionanalysis;independentacceptancepending','method':method}})
# Page110alsohastrigActivity4.2. Itscompletecensusbelongstothenextsegment.
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'AllExercise4B1–11tasks/givenfiguresandQ5continuationenumerated. Q12on110willbecombinedwiththetrigactivityinthepage110census.',
 'reader':'Codex author','date':'2026-11-18'}for page in[108,109]]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-4B.json',{'scope':'Alltwelvesourcequestionsandeveryexplicitresponse;originaldomainsandconditionspreserved.','items':answers}),
     ('census-Goldie-C4-4B.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages108–109;Q12on110recordedbutpage110awaitstrigactivitycensus.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
