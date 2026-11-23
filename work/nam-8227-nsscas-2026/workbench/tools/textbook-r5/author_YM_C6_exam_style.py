"""YM314–317: source-labelled exam-style tangent/domain/parameter problems."""
import json
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;CHAIN='8227:2020:M1:T8:O02:D02';POINT='8227:2020:M1:T8:O04:D01';NATURE='8227:2020:M1:T8:O04:D02';TANGENT='8227:2020:M1:T8:O03:D01';MONO='8227:2020:M1:T8:O03:D02';LINE='8227:2020:M1:T4:O01:D01';INTERSECT='8227:2020:M1:T4:O02:D01';COORD='8227:PRIOR:NSSCO:coordinate-geometry';extra=h.extra
def val(label,expr,key,kp,direct,method,components=None,fn=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[])
 if fn:p['original_function']=fn
 return p
def add(kind,n,page,note,parts,domain,rep='text',continuation=None):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 components=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 inputs=[p['original_function']for p in parts if 'original_function'in p]
 r=h.add(kind,n,page,note,parts,direct,components,powers=inputs)
 r.update(representation=rep,original_domain=domain,exam_style=True,exam_style_basis='Source-labelled6.3Exam-StyleQuestions,headingPDF314/printed302. Textbook-derivedpractice;noexternalpaperattributionorofficialmarkingisclaimed.',mapping_rationale='Separate explicit tangent/derivative/domain tasks from connected prerequisite geometry. A source exam-style label is not examination-observed evidence. Parameter positivity/nonzero conditions decide valid simplification and branch classification.')
 if continuation:corrections[-1]['continuation_pdf_pages']=continuation
 for p in parts:p['given_representation']=rep
 return r
def rounded(p,expr,dp):p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp};return p

ps=[val('a-chord','expand(Rational(2,4)*(x-1))','x/2-Rational(1,2)',314,[LINE],'ORIGINAL A(1,0),B(5,2)give chordgradient(2−0)/(5−1)=1/2. Useeitheroriginalpointandreturnthe requested y=mx+cform.'),val('b-tangent','expand(1+Rational(1,2)*(x-2))','x/2',314,[TANGENT],'Originalcurvey=sqrt(x−1)hasderivative1/(2sqrt(x−1))onx>1. ParalleltoABrequiresgradient1/2,sox2andoriginalordinate1. Point-gradientformgives tangentx/2.',[CHAIN],fn='sqrt(x-1)'),val('c-distance','sqrt(Rational(1,5)**2+Rational(2,5)**2)','0.45',315,[],'Use the two establishedparallel LINESy=x/2and y=x/2−1/2. OriginliesonthetangentLINE,butnotontheoriginalrootcurve. A perpendiculartransversal y=−2xmeetsABat(1/5,−2/5);distancefromoriginis1/sqrt5. This connected prior-geometrycalculation doesnotaddanindependentcalculusdemand.',[TANGENT,COORD])]
ps[2]=rounded(ps[2],'sqrt(Rational(1,5)**2+Rational(2,5)**2)',2);ps[2].update(exact_canonical_answer='1/sqrt(5)',source_precision='Questionexplicitlyasks2decimalplaces.')
extra(ps[1],'original-slope-condition','(1/(2*sqrt(x-1))).subs(x,2)','Rational(1,2)');extra(ps[2],'independent-line-distance','Rational(1,2)/sqrt(1+Rational(1,2)**2)','1/sqrt(5)')
r=add('Example',36,314,'Givenrootcurve,chordABandparallel tangent:derivebothlinesandperpendiculardistancewith2dpoutput.',ps,'Curve x>=1;finite tangentx>1.','graph',[315]);r['connected_part_structure']='Part(b)useschordgradientfrom(a);(c)usesbothlineequations. Origin is a pointon thetangentline,notonthecurve.'
p=val('tangent','expand(6+(-3)*(x-3))','-3*x+15',624,[TANGENT],'Originalcubicy=x³−9x²+24x−12musthavetangentgradient−3toparallelgivenliney2−3x. Itsderivativeequal−3gives3(x−3)²0,sox3,originaly6,andtangent−3x+15.',[POWER],fn='x**3-9*x**2+24*x-12');extra(p,'required-gradient','diff(x**3-9*x**2+24*x-12,x).subs(x,3)','-3')
add('Try-Now-36',1,315,'Find the unique cubic tangent parallel to a given negative-slope line,with all necessaryworking.',[p],'Allrealx.')
p=val('a-show-M','Tuple((-1+2)/2,(12+3)/2)','Tuple(Rational(1,2),Rational(15,2))',624,[INTERSECT],'Intersect ORIGINALquadraticx²−4x+7andliney9−3x. Solve x²−x−2=0givingx−1,2andoriginalordinates12,3. Their midpointis(1/2,15/2),establishingthe stated result.',[COORD],fn='x**2-4*x+7');p.update(check_mode='show/prove',response_format='proof/show-that');extra(p,'intersection-abscissas','FiniteSet(*solve(x**2-4*x+7-(9-3*x),x))','FiniteSet(-1,2)')
ps=[p,val('b-Q','Tuple(Rational(1,2),(x**2-4*x+7).subs(x,Rational(1,2)))','Tuple(Rational(1,2),Rational(21,4))',624,[TANGENT],'ParalleltoORIGINALliney9−3xmeanstangentgradient−3. Originalcurvederivative2x−4=−3givesx1/2;evaluate ORIGINALcurveordinatetoobtainQy21/4.',[POWER],fn='x**2-4*x+7'),val('c-MQ','sqrt((Rational(1,2)-Rational(1,2))**2+(Rational(15,2)-Rational(21,4))**2)','Rational(9,4)',624,[],'Use the previously establishedM,Q. Theysharex1/2,sodistanceisthepositiveverticaldifference15/2−21/4=9/4. This is a connected prior-coordinate-geometryresult,notadditionaltangentcalculation.',[COORD,TANGENT,INTERSECT])]
r=add('Try-Now-36',2,315,'Curve/line intersectionsandmidpointM,tangent-parallelpointQ,anddistanceMQ.',ps,'Allrealx.');r['connected_part_structure']='Part(c)usesMfrom(a)andQfrom(b).'
p=val('tangent','expand(refine(3+((2/a)*(a**2)**(-Rational(1,2))+a*(a**2)**(-Rational(3,2)))*(x-a**2),Q.positive(a)))','3*x/a**2',316,[TANGENT],'ORIGINAL GIVENdy/dx=(2/a)x^(−1/2)+a*x^(−3/2),aPOSITIVE,andA(a²,3). Theexpressionisalreadya derivative. Positiveaallows sqrt(a²)=a,so gradient3/a². Point-gradientformthroughAgivestangent3x/a². Do notdifferentiatethegiven derivativeagainorignorethepositiveassumption.',[CHAIN],fn='(2/a)*x**(-Rational(1,2))+a*x**(-Rational(3,2))');p['original_parameter_assumptions']='a>0;thegivenpointx=a²liesinside x>0.'
add('Example',37,316,'Obtain a parameterised tangent from a supplied derivativeandpositive-parametercurvepoint.',[p],'a>0;x>0forthegivenrootderivative.')
p=val('k','7-(4**2-5*4)','11',625,[TANGENT],'Originalnormal3y+x25hasgradient−1/3,sotangentgradient3. Originalcurvey=x²−5x+khasderivative2x−5;equating3givesx4. TheNORMALgivesy7at4. Originalcurveordinatethenforcesk11.',[POWER],fn='x**2-5*x+k');extra(p,'normal-point-and-tangent','Tuple(3*7+4,(2*x-5).subs(x,4))','Tuple(25,3)')
add('Try-Now',37,316,'Use a givennormal line to determine the unknownverticalconstantof a quadratic curve.',[p],'Allrealx;kconstant.')
p=val('largest-k','Rational(5,2)','Rational(5,2)',316,[MONO],'Originalf=(2x−1)^(3/2)−6xonOPENdomain1/2<x<k. Derivative3sqrt(2x−1)−6isnegativeexactlyfor1/2<x<5/2. Thelargest endpointk5/2isallowedbecausetheupperendpointisEXCLUDED;anylargerkadmitsapositive-gradientinterval.',[CHAIN],fn='(2*x-1)**Rational(3,2)-6*x');extra(p,'gradient-at-boundary','(3*sqrt(2*x-1)-6).subs(x,Rational(5,2))','0')
add('Example',38,316,'Find the largestopen-domainendpointfor ashifted-rootfunctiontoremaindecreasing,includingthecriticalboundarycorrectly.',[p],'1/2<x<k.')
p=val('largest-a','-Rational(4,3)','-Rational(4,3)',625,[MONO],'Originalcubichasderivative(3x+4)(x−2),positiveon(−infinity,−4/3)and(2,infinity). The ENTIREdomainx<aextendsleftwithoutbound,soitmuststayintheleftpositivecomponent. Largesta−4/3;thecriticalboundaryisexcludedbyx<a.',[POWER],fn='x**3-x**2-8*x+5');extra(p,'derivative-factor','factor(diff(x**3-x**2-8*x+5,x))','(3*x+4)*(x-2)')
add('Try-Now-38',1,317,'Selectlargestleft-raydomainendpointforagivencubic tobeincreasing,notmerelyanypositive-derivativeinterval.',[p],'Allx<a.')
p=val('smallest-k','4','4',625,[MONO],'Originalderivative3(x−2)(x−4)ispositiveoutside[2,4]. The ENTIREright-raydomainx>kmustavoid theinteriornegativeinterval,so smallestk4. Thezerogradientat4isexcludedbytheopenendpoint.',[POWER],fn='x**3-9*x**2+24*x-12');extra(p,'derivative-factor','factor(diff(x**3-9*x**2+24*x-12,x))','3*(x-2)*(x-4)')
add('Try-Now-38',2,317,'Selectsmallestright-raydomainendpointforagivencubic tobeincreasing.',[p],'Allx>k.')
ps=[val('a-derivative','diff(x**3+3*x**2-9*x+k,x)','3*x**2+6*x-9',317,[POWER],'Differentiate ORIGINALpolynomial;treatkasa constant.',fn='x**3+3*x**2-9*x+k'),val('b-x-values','FiniteSet(*solve(3*x**2+6*x-9,x))','FiniteSet(-3,1)',317,[POINT],'SettheORIGINALderivedgradient3x²+6x−9to0;retainbothstationaryabscissas−3and1.',[POWER]),val('c-k-values','FiniteSet(-((-3)**3+3*(-3)**2-9*(-3)),-(1**3+3*1**2-9*1))','FiniteSet(-27,5)',317,[LINE],'Use the two already locatedstationaryabscissas. To put one ofthosepointsONTHExAXIS,itsORIGINALordinate mustbe0. Thusk−27forx−3ork5forx1. This is an inverse graph/ordinatecondition,not another independentstationary-rootcalculation.',[POINT])]
add('Example',39,317,'Derivative,stationaryabscissas,andthetwoverticalparameterswhichputastationarypointonthexaxis.',ps,'Allrealx;kconstant.')
p=val('x-values','FiniteSet(*solve((k*x-3)**2-1,x))','FiniteSet(2/k,4/k)',625,[POINT],'ORIGINALy=(kx−3)^−1+(kx−3),kNONZERO. Derivativek[1−1/(kx−3)²]0giveskx−3=±1,sox2/k,4/k. Excludetheoriginalpole3/k. Either signofkisallowed;do not silentlyassume kpositive.',[CHAIN],fn='1/(k*x-3)+(k*x-3)')
ps=[p]
for label,root,conclusion,target in [('maximum','2/k','Maximumatx2/k.','-2*k**2'),('minimum','4/k','Minimumatx4/k.','2*k**2')]:
 p=reasoning(label,conclusion,'Originalsecondderivative2k²/(kx−3)³evaluatedatthecorrespondingbranchis'+target+'. SinceREALk≠0,k²>0,sothesignprovesthenatureforBOTHpositiveandnegativek. The numericalorderingofthestationaryabscissasreverseswhenkisnegative,buttheirbranchlabelsdo not.',625,'matches');p.update(assessed_8227_demand_ids=[NATURE],component_demand_ids=[CHAIN],original_parameter_assumptions='k real,k≠0')
 extra(p,'second-at-branch',f'(2*k**2/(k*x-3)**3).subs(x,{root})',target);ps.append(p)
add('Try-Now',39,317,'FindstationaryabscissasintermsofNONZERO signedkandjustifymaximum/minimumwithoutassumingtheirleft-rightorder.',ps,'k≠0;x≠3/k.')

refs=[(62,314,'Example36 given root curve and chord','y=sqrt(x−1),A(1,0),B(5,2). Aisanendpointwithverticaltangent,butthe requestedPARALLELtangentoccursat interiorx2. GivenlineABisachord,notitselfthecurvetangent.',[LINE,TANGENT],'graph','Example:36','given-figure'),(63,315,'Example36 worked parallel-line distance construction','Tangentliney=x/2passesthroughorigin,whiletheROOTCURVEdoesnot. Perpendiculartransversaly−2xfromoriginmeetsthechordaty=x/2−1/2at(1/5,−2/5). Thiscomputeslinedistance;itisnotclaimingthecurvehasapointat(0,0).',[TANGENT],'graph','Example:36','teaching-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:');r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
 r['mathematical_feature_review']['method']='Inspectoriginalcurvepointlabels,chordversustangent,andperpendicularconstruction. Verifyincidence/exactdistancealgebraically;distinguishapointonthetangentLINEfromapointonthecurve.'
pages=[]
for page in range(314,318):
 pages.append(dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C6:Example:36']if page==315 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllExamples36–39,Try36Q1/2,Try37,Try38Q1/2,Try39,andtwoExample36graphpanelsare enumerated over314–317. Source6.3Exam-Styleheadingisexplicit;noactualexam-boardattributionisprinted. OnlyExample36solutioncontinues315.',scope_screen='Prescribedtangent,derivative,monotonic-domainandstationary-parameterdemands. Connectedgeometrycanremainprerequisitesupport. Preserveapositive,knonzero,openendpoints,andoriginalroot/poleconditions.'))
if __name__=='__main__':
 for name,data in [('answers-YM-C6-exam-style.json',dict(scope='All314–317explicit tasks.',items=answers)),('census-YM-C6-exam-style.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete314–317page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
