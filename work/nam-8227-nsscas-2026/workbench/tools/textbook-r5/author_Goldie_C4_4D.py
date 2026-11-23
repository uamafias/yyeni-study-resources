"""Every fixed-source implicit Exercise4D1–12, Goldie PDF120–122."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
IMPLICIT='8227:2020:M2:T4:O03:D01';GEOM='8227:2020:M2:T4:O03:D03';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02'
PRODUCT='8227:2020:M2:T4:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';POWER='8227:2020:M1:T8:O02:D01'
SKETCH='8227:2020:M1:T3:O05:D01';LOGLAW='8227:2020:M2:T2:O01:D02';LOGDEF='8227:2020:M2:T2:O02:D01'
ATTR={8:'9709,Paper2Q5,June2006',9:'9709,Paper31Q5,June2011',10:'9709,Paper2Q7,June2008',11:'9709,Paper32Q3,November2009',12:'9709,Paper3Q6,June2008'}
def ev(page):
    name='Goldie-key-C3-341'if page==344 else'Goldie-C4-118'if page<=121 else'Goldie-C4-122'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,sketch=False):
    for p in parts:
        kp=p.pop('key_page_override',344);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Exercise-4D:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'These are genuinely implicit derivative/geometry tasks,except that4D1isabuilding-blockdrill. Preserve logarithm domains,allpointrequirements,method instructions andnonzero parameters;do not acceptsingularcandidatesasregularzero slopes.',
      'representation':'text','sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'not applicable'if n in[2,3,7,9]else'within','quoted_value':note,
        'reason':'Q7hasvariableexponentx^xanduseslogarithmic/implicit differentiation,not the constant-rational-exponent power rule. Other listedcasesarelog/exp/trig targets.'if n in[2,3,7,9]else'Actual polynomial powers areintegers;implicit y powers keepdy/dx.'},
       {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Natural logs areexplicitin2/7/9;nochange ofbase isrequested.'},
       {'rule_id':'8227:QUAL09','status':'not applicable','quoted_value':note,'reason':'Implicit tangents/normals andstationaryconditionsusecalculus,not aquadratic-discriminant tangent exercise.'}],
      'exam_style':n in ATTR,'exam_style_basis':'Printed book attribution:'+ATTR[n]+'. Internal lead;original paper not newly verified.'if n in ATTR else'Ordinary exercise without examination attribution.',
      'precision_angle_check':{'source':'Exact algebra except4D7stationarycoordinates to3decimalplaces. Trig inputs are radians;lnargumentsremainpositive.',
        'comparison':'Keep exact internal values before requested final decimal-place rounding. Preserve original domain holes/asymptotes anddistinguish regular implicit slopes from singular points.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

def implicit(label,F,target,kp=344):
    p=value(label,'0',target,kp,'Differentiate the original curve using independent partial derivatives andisolate−Fx/FywhereFy≠0. Theprinted target is separately transcribed;it isnot an input to this calculation.')
    p['operation']={'kind':'implicit-derivative','operands':[F]}
    return p

def slope(F,a,b):return f'(-diff({F},x)/diff({F},y)).subs({{x:{a},y:{b}}})'
def hor(label,F,key,nonzero=None):
    p=value(label,'0',key,344,'SolveF=0andFx=0jointly,retainallrealpoints,andcheckFy≠0at every candidate. A singular candidate requires separatebranchanalysisandisnot silentlyaccepted.')
    p['operation']={'kind':'implicit-horizontal-points','operands':[F]}
    if nonzero:p['operation']['nonzero_parameters']=nonzero
    return p
parts=[]
for label,F,target,domain in[
 ('i','y**4','4*y**3*p','Real localy(x).'),('ii','x**2+y**3-5','2*x+3*y**2*p','Real localy(x).'),
 ('iii','x*y+x+y','x*p+y+1+p','Real localy(x).'),('iv','cos(y)','-sin(y)*p','Radiany.'),
 ('v','exp(y+2)','exp(y+2)*p','Real localy(x).'),('vi','x*y**3','y**3+3*x*y**2*p','Real localy(x).'),
 ('vii','2*x**2*y**5','4*x*y**5+10*x**2*y**4*p','Real localy(x).'),('viii','x+log(y)-3','1+p/y','y>0.'),
 ('ix','x*exp(y)-cos(y)','x*exp(y)*p+exp(y)+sin(y)*p','Radiany.'),('x','x**2*log(y)','2*x*log(y)+x**2*p/y','y>0.'),
 ('xi','x*exp(sin(y))','exp(sin(y))+x*exp(sin(y))*cos(y)*p','Radiany.'),
 ('xii','x*tan(y)-y*tan(x)','tan(y)+x*sec(y)**2*p-(tan(x)*p+y*sec(x)**2)','cosx≠0andcosy≠0;radianarguments.')]:
    p=value(label,'0',target,344,'Treatyasy(x),useFx+Fy*dy/dx,andretainchain/product terms. Internalpnormalisesdy/dx;it isnot a sourceparameter.')
    p['operation']={'kind':'implicit-expression-derivative','operands':[F]};p['normalised_notation']={'p':'dy/dx'};p['original_common_domain']=domain;parts.append(p)
row=add(1,120,'Twelve formal derivatives withydependent onx:y^4;x²+y³−5;xy+x+y;cosy;e^(y+2);xy³;2x²y^5;x+lny−3;x e^y−cosy;x²lny;x e^(siny);x tany−y tanx. Log/trig domainsandall dy/dxtermsarepreserved.',parts,[IMPLICIT],[PRODUCT,ELEMENTARY,POWER])
row['direct_demand_aspects']=[{'demand_id':IMPLICIT,'assessed_facet':'Formalbuildingblocks,not a solved implicitcurve/geometricapplication by themselves.'}]
F='x*y**3-5*log(y)';p=value('gradient',slope(F,'0','1'),'1/5',344)
p['assertions']=[{'expression':f'({F}).subs({{x:0,y:1}})','expected':'0'}]
add(2,121,'Forxy³=5lny,find gradientat(0,1). Originaly>0;thegivenpointisverifiedonthecurveandFy=−5thereisnonzero.',[p],[IMPLICIT,GEOM],[ELEMENTARY,PRODUCT])
F='exp(sin(x))+exp(cos(y))-E-1';p=value('gradient',slope(F,'pi/2','pi/2'),'0',344)
p['assertions']=[{'expression':f'({F}).subs({{x:pi/2,y:pi/2}})','expected':'0'}]
add(3,121,'Fore^(sinx)+e^(cosy)=e+1,findgradientat(π/2,π/2). ThepointisonthecurveandFy=−1there,soazero numeratorreallygivesazero regular slope.',[p],[IMPLICIT,GEOM],[COMPOSITE,ELEMENTARY])
F='x**2+3*x*y+y**2-x-3*y';m=slope(F,'2','-1');p=value('i',m,'0',344);p['assertions']=[{'expression':f'({F}).subs({{x:2,y:-1}})','expected':'0'}]
add(4,121,'Forx²+3xy+y²=x+3y,findgradientat(2,−1)andhencetangentthere. Thefinitegradientiszero,so thetangentis horizontal.',[
 p,value('ii',f'-1+({m})*(x-2)','-1',344)],[IMPLICIT,GEOM],[POWER,PRODUCT])
add(5,121,'Findallstationarycoordinatesofx²+y²+xy=3. Solveoriginalcurveandhorizontal-gradientconditiontogether;bothrealcandidatesare regular.',[
 hor('points','x**2+y**2+x*y-3','FiniteSet(Tuple(1,-2),Tuple(-1,2))')],[IMPLICIT,GEOM,STATIONARY],[POWER])
F='(x-6)*(y+4)-2';m=slope(F,'7','-2');N=f'-2+(-1/({m}))*(x-7)';other=f'solve((x-6)*(({N})+4)-2,x)[0]'
p=reasoning('iv-asymptotes','Thecurve isy+4=2/(x−6),withasymptotesx=6andy=−4.',
 'Solve the original equation fory. Since thenumerator2isnonzero,x=6hasnocurvepoint. Asx→±∞,2/(x−6)→0,so thehorizontalasymptoteisy=−4.',344,'matches')
p['additional_operations']={'explicit_equation_residual':{'kind':'identity','operands':['cancel(((x-6)*(y+4)-2).subs(y,-4+2/(x-6)))']}}
p['additional_operation_expected']={'explicit_equation_residual':'0'}
p2=reasoning('iv-sketch','Twohyperbolabranchescentredat(6,−4):rightbranchliesabovey=−4andleftbranchbelowit;bothdecrease,withverticalasymptotex=6.',
 'Fromy=−4+2/(x−6),the derivative−2/(x−6)²isnegativeonbothcomponents. Thegivenpoint(7,−2)isontheupperrightbranch;theothernormalintersection(2,−9/2)isonthelowerleftbranch. Preserve thepole,not a connectedcurve acrossit.',344,'sketch')
p2['additional_operations']={'pole_limits':{'kind':'identity','operands':['Tuple(limit(-4+2/(x-6),x,6,dir="-"),limit(-4+2/(x-6),x,6,dir="+"))']}}
p2['additional_operation_expected']={'pole_limits':'Tuple(-oo,oo)'}
add(6,121,'For(x−6)(y+4)=2:finddy/dx;normalat(7,−2);where thatnormalmeetsthecurveagain;rewrite y−a=b/(x−c),identifyasymptotesandsketch. Theintersectionquestionexcludes thegivenpoint.',[
 implicit('i',F,'(y+4)/(6-x)'),value('ii-normal',N,'(x-11)/2',344),
 value('iii',f'Tuple({other},({N}).subs(x,{other}))','Tuple(2,-9/2)',344,
 'Substitutetheindependentlyderivednormalinto theoriginalcurve. Itsrootsare2and7;7isthegivenpoint,sotake theotherroot2anditsoriginalnormalordinate.'),p,p2],
 [IMPLICIT,GEOM,SKETCH],[PRODUCT],True)
F='log(y)-x*log(x)'
p=reasoning('i','lny=xlnx,onx>0andy=x^x>0.',
 'The source explicitlyaskslogstobasee. Apositivexmakesx^xpositiveandthelogpowerlawisvalid:ln(x^x)=xlnx. Nochangeofbaseisinvolved.',344,'matches')
p2=value('ii','0','p/y-1-log(x)',344,'Differentiatethelogarithmicequationwithydependent onx. Theleftsidegives(1/y)dy/dxandtherightside1+lnx;solvinggivesy′=y(1+lnx).')
p2['operation']={'kind':'implicit-expression-derivative','operands':[F]};p2['normalised_notation']={'p':'dy/dx'};p2['author_answer_form']='(1/y)dy/dx=1+lnx.'
r='solve(log(x)+1,x)[0]';Y=f'(x**x).subs(x,{r})'
px=value('iii-x',r,'0.368',344,'Sincey>0,theonlystationaryabscissasatisfieslnx+1=0;lnisincreasingonx>0. Deriveexact1/e,thenroundthecoordinate to3decimalplaces.')
px['operation']={'kind':'rounded','operands':[r],'decimal_places':3};px['additional_operations']={'exact_abscissa':{'kind':'identity','operands':[r]}}
py=value('iii-y',Y,'0.692',344,'Substitutetheexactstationaryabscissaintotheoriginalpositivex^x,andonlythenroundtheordinate to3decimalplaces.')
py['operation']={'kind':'rounded','operands':[Y],'decimal_places':3};py['additional_operations']={'exact_ordinate':{'kind':'identity','operands':[Y]}}
p3=reasoning('iv','Onx>0,thegraphapproachesthelimitingpoint(0,1),decreasesto(1/e,e^(−1/e)),thenincreaseswithoutboundandpasses(1,1). Thelimitpointat0isexcluded.',
 'Writey=exp(xlnx). Becausexlnx→0asx→0+,y→1there,but0isnotintheoriginaldomain. Sincey>0,thederivativesignisthesignof1+lnx:negativebefore1/eandpositiveafterit. Thekeysketchhasthisminimumandpositive-domainshape;do notinterpretitsunmarkedlimitingendpointasallowingx=0.',344,'sketch')
p3['additional_operations']={'left_limit':{'kind':'identity','operands':['exp(limit(x*log(x),x,0,dir="+"))']},'unit_point':{'kind':'identity','operands':['exp(1*log(1))']}}
p3['additional_operation_expected']={'left_limit':'1','unit_point':'1'}
row=add(7,121,'Fory=x^x,x>0:explicitlytakebasee logs,differentiatethelogequation,findstationarycoordinates to3decimalplaces,andsketchthepositive-domaincurve. Thisusesavariableexponentandisnot theconstant-powerderivativerule.',[p,p2,px,py,p3],
 [LOGLAW,LOGDEF,IMPLICIT,GEOM,STATIONARY,CLASSIFY,SKETCH],[PRODUCT,COMPOSITE],True)
row['source_interpretation']={'domain':'x>0,y=x^x>0','source_precision':'Eachcoordinate3decimalplaces,not a general3significant-figurerule.','source_graph_endpoint':'At0showanexcludedlimitpointifshown;no0^0valueisclaimed.'}
F='3*x**2+2*x*y+y**2-6';p=value('i','solve(diff(3*x**2+2*x*y+y**2-6,x),y)[0]','-3*x',344,
 'Horizontal tangentrequiresFx=0providedFy≠0,so6x+2y=0givesy=−3x. Thefollowingjoint-systemcheckverifiesbothcandidatesareon theoriginalcurveandregular.')
p['check_mode']='show/prove';p['author_answer_form']='y=−3x.'
add(8,121,'For3x²+2xy+y²=6,giventwotangentsparalleltothex-axis:showy=−3xatthosepoints,thenfindbothcoordinates. OriginalFyisnonzeroatbothresults.',[
 p,hor('ii',F,'FiniteSet(Tuple(1,-3),Tuple(-1,3))')],[IMPLICIT,GEOM,STATIONARY],[POWER])
F='6*exp(2*x)+k*exp(y)+exp(2*y)-c';p=value('i',f'({F}).subs({{x:log(3),y:log(2)}})','58+2*k-c',344,
 'Substitutethegivenexactlogcoordinatesintheoriginalcurve;exp(2ln3)=9,exp(ln2)=2,exp(2ln2)=4. Normalisedresidualzeroisthesource58+2k=c.')
p['check_mode']='show/prove';p['author_answer_form']='58+2k=c.'
ms=slope(F,'log(3)','log(2)')
sol=f'solve([({F}).subs({{x:log(3),y:log(2)}}),({ms})+6],(k,c),dict=True)[0]'
p2=value('ii',f'Tuple(({sol})[k],({sol})[c])','Tuple(5,68)',344,
 'Independentlyderiveimplicitgradientatthegivenpointandsetitto−6,jointlywiththeoriginalpointrelation. Retainnonzerodenominator;thefoundconstantsgiveFy=18there.')
p2['additional_operations']={'Fy_at_given_point_with_solution':{'kind':'identity','operands':[f'diff({F},y).subs({{x:log(3),y:log(2),k:5,c:68}})']}}
p2['additional_operation_expected']={'Fy_at_given_point_with_solution':'18'}
add(9,121,'For6e^(2x)+k e^y+e^(2y)=cpassingthroughP=(ln3,ln2):show58+2k=c;usegivenimplicitgradient−6atPtorecoverk,c. Natural-logdefinitionsandoriginalcurveregularityarechecked.',[p,p2],[IMPLICIT,GEOM,LOGDEF],[ELEMENTARY,COMPOSITE])
F='x**2+y**2-4*x*y+3';p=implicit('i',F,'(2*y-x)/(y-2*x)');p['check_mode']='show/prove'
add(10,121,'Forx²+y²−4xy+3=0,showdy/dx=(2y−x)/(y−2x),thenfindeverypointwhosetangentisparallel to thex-axis. Bothresultshavenonzeroimplicitdenominator.',[
 p,hor('ii',F,'FiniteSet(Tuple(2,1),Tuple(-2,-1))')],[IMPLICIT,GEOM,STATIONARY],[POWER,PRODUCT])
F='x**3-x**2*y-y**3-3';m=slope(F,'2','1');p=value('ii',f'1+({m})*(x-2)','(8*x-9)/7',344,
 'Verifythegivenpointontheoriginalcurve,deriveitsfinitegradient8/7,andformtangentthrough(2,1). Thenexpressthesame linein theexplicitlyrequestedax+by+c=0form.')
p['assertions']=[{'expression':f'({F}).subs({{x:2,y:1}})','expected':'0'}]
p['response_form_requirement']={'required':'ax+by+c=0','canonical_display':'8x−7y−9=0','internal_normalisation_only':'y=(8x−9)/7'}
add(11,122,'Forx³−x²y−y³=3:finddy/dxintermsofx,y,andtangentat(2,1)intheexplicitformax+by+c=0. Equivalentlinevaluesalone do notremove the requesteddisplayform.',[
 implicit('i',F,'(3*x**2-2*x*y)/(x**2+3*y**2)'),p],[IMPLICIT,GEOM],[PRODUCT,POWER])
F='x*y*(x+y)-2*a**3'
p=reasoning('uniqueness','Theonlyrealhorizontal-tangentpointis(a,−2a),fora≠0.',
 'Fx=y(2x+y)=0. They=0branchwouldmakeF=−2a³≠0,socannotlieonthecurve. Thusy=−2x;substitutiongives2x³=2a³,andthereal cubefunctionisone-to-one,sox=aandy=−2a. ThereFy=x²+2xy=−3a²≠0becausea≠0. Thisverifiesbothuniquenessandregularity;theexcludedcasea=0wouldchangethecurveanditsstationarystructure.',344,'show/prove')
p['additional_operations']={'horizontal_condition_factorisation':{'kind':'identity','operands':['factor(diff(x*y*(x+y)-2*a**3,x))']},
 'candidate_residual':{'kind':'identity','operands':['(x*y*(x+y)-2*a**3).subs({x:a,y:-2*a})']},
 'Fy_at_answer':{'kind':'identity','operands':['diff(x*y*(x+y)-2*a**3,y).subs({x:a,y:-2*a})']}}
p['additional_operation_expected']={'horizontal_condition_factorisation':'y*(2*x+y)','candidate_residual':'0','Fy_at_answer':'-3*a**2'}
row=add(12,122,'Forxy(x+y)=2a³,wherethe sourceexplicitlystatesanonzero realconstant:showthereisonlyonehorizontal-tangentpointandfinditscoordinates. Thea≠0conditionisessential,not cosmetic.',[
 p,hor('point',F,'FiniteSet(Tuple(a,-2*a))',['a'])],[IMPLICIT,GEOM,STATIONARY],[PRODUCT,POWER])
row['source_interpretation']={'parameter_domains':{'a':'real,nonzero'},'reason':'a=0createsextraaxisbranchesandlosestheuniqueness/regularityargument;donotuseitasanordinaryvariation.'}
# Page122alsoopenstheparametricrideexposition;itscompletecensusisownedbythenextsegment.
pages=[]
for page in[120,121]:
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]
    if page==120:own+=['8227:TB:Goldie:C4:Teaching-figure:29','8227:TB:Goldie:C4:Teaching-figure:30']
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated','item_ids':own,
     'continuation_item_ids':['8227:TB:Goldie:C4:Example:18']if page==120 else[],
     'source_evidence':ev(page),'non_item_content':'All4D1–10partsandtheExample18continuation/twosolutionpanelsenumerated.4D11–12on122areauthoredherebuttheirpagecensusawaitstheparametricopening.',
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-4D.json',{'scope':'Alltwelveimplicitexercises,everyformalderivative/geometry/parameter/sketchoutput.','items':answers}),
     ('census-Goldie-C4-4D.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Complete120–121;4D11–12on122awaitcombinedpagecensuswiththeparametricopening.','new_items':[],'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;noadditionalchapterfigures')
