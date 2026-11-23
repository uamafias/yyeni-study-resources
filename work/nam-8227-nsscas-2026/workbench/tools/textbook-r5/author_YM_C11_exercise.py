"""YM523–524: all ten Exercise11 tasks, complete bounded roots and original point checks."""
import json
from author_YM_C4_composite_equations import roots
import author_YM_C11_implicit_opening as i
import author_YM_C11_parametric_opening as b
import author_YM_C11_opening as a
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=a.ev;h.common.base.ev=ev
DERIV=i.DERIV;IMPLICIT=i.IMPLICIT;PARAM=b.PARAM;GEOM=i.GEOM;STAT=a.STAT;TANG=a.TANG;NATURE='8227:2020:M1:T8:O04:D02';RFORM='8227:2020:M2:T3:O02:D04'

def add(n,page,note,parts,rep='text'):
 r=a.add('Exercise-11',n,page,note,parts);r.update(representation=rep,exam_style=False,exam_style_basis='OrdinaryExercise11basic/intermediate/advanced;11.7Exam-StyleQuestionsbeginsonNEXTpage525.',mapping_rationale='Directlinksfollowactuallyaskedderivative/point/nature/lineoutputs. ExplicitcurvegeometrydoesNOTinheritimplicit/parametricgeometry. RequiredR-formconversionhasitsownlink;finiteintervalrootrecoveryandGIVENP/Qlabelorderareverifiedfromoriginalderivative. Originalimplicitpointincidenceandparametricdomainskept.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='within'if n in[3,9,10]else'not applicable',quoted_value=note,reason='Actualangulararguments1or2andoriginalfiniteintervalskeptwhereboundedrootrecoveryoccurs;otheritemsarealgebraic/loggeometry.'),dict(rule_id='8227:LIMIT02',status='within'if n in[3,10]else'not applicable',quoted_value=note,reason='Onlyoriginalboundedrootsetsareasked;otheritemsarenotgeneraltrigequations.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03','8227:LIMIT02']),precision_angle_check=dict(source='Radians;Q3stationarycoordinateseach3dp;Q10P/Qabscissaseach4sf. Otheroutputs exactandintegerlineformswhereasked.',comparison='Retainexactphaseandwholeoriginalintervalbeforeenumeration/rounding. A sourceprincipalinversevalueoutsidetheintervalisnotanadmissiblelabelledpoint.'))
 return r

def val(label,expr,key,kp,direct,method,components=None):return a.val(label,expr,key,kp,direct,method,components)
def rnd(p,name,expr,key,dp=None,sf=None):
 op={'kind':'rounded','operands':[expr]}
 if dp is not None:op['decimal_places']=dp
 else:op['significant_figures']=sf
 p.setdefault('additional_operations',{})[name]=op;p.setdefault('additional_operation_expected',{})[name]=key
p=val('shown-derivative','trigsimp(diff(cos(x)/sin(x),x)+csc(x)**2)','0',649,[a.QUOT],'Use the REQUIREDoriginalcosx/sinxquotient,notamemorisedcotderivativerule. Quotientnumerator−sin²x−cos²x−1,originalsinx≠0;hencederivative−csc²x.',[DERIV]);p.update(check_mode='show/prove',response_format='proof/show-that')
add(1,523,'BydifferentiatingORIGINALcosx/sinx,SHOWcotxderivative−cosec²x. Originalradiansandsinxnonzeroretained;methodexplicitlyrequired.',[p])
p=val('a-stationary-x','solveset(diff(x**2*log(x),x),x,domain=Interval.open(0,oo))','FiniteSet(exp(-Rational(1,2)))',649,[STAT],'ORIGINALx>0;derivativex(1+2lnx)0givesexactxexp(−1/2). Thex0factorisoutsideoriginaldomain.',[DERIV,a.PROD])
q=reasoning('b-nature','Minimum.','Originalsecondderivative3+2lnxequals2atxexp(−1/2)>0.',649,'matches');q.update(assessed_8227_demand_ids=[NATURE],component_demand_ids=[DERIV],depends_on_source_parts=['a-stationary-x'],response_format='explanation');extra(q,'positive-second-derivative','diff(x**2*log(x),x,2).subs(x,exp(-Rational(1,2)))','2')
add(2,523,'ForORIGINALx²lnx,x>0,findexactstationaryxexp(−1/2)andnatureminimum. Noordinatesasked.',[p,q])
f='3*exp(-x)*sin(2*x)';p=val('a-origin-tangent','('+f+').subs(x,0)+diff('+f+',x).subs(x,0)*x','6*x',649,[TANG],'ORIGINALoriginliesoncurveandfinitegradient6,so tangenty6x.',[DERIV,a.PROD,a.CHAIN])
q=reasoning('b-stationary-M-coordinates','M=(0.554,1.543),each3dp.','OnORIGINAL0≤x≤π/2,thederivative3e^(−x)(2cos2x−sin2x)hasonezero,xatan2/2. RecoverORIGINALordinate3e^(−x)sin2xtherebefore3dprounding. Endpointsnotstationary.',649,'matches');q.update(assessed_8227_demand_ids=[STAT],component_demand_ids=[DERIV,a.PROD,a.CHAIN],response_format='symbolic')
rnd(q,'x','atan(2)/2','Rational(554,1000)',3);rnd(q,'y','('+f+').subs(x,atan(2)/2)','Rational(1543,1000)',3);extra(q,'original-stationary-derivative','simplify(diff('+f+',x).subs(x,atan(2)/2))','0')
add(3,523,'GIVENf3e^(−x)sin2xon0..π/2:(a)tangentatorigin6x;(b)stationaryMcoordinatesEACH3dp0.554,1.543. Sourcegraphisgiven,notaskedsketch.',[p,q],'graph')
f='exp(4*x)/(2*x+3)';p=val('tangent','('+f+').subs(x,0)+diff('+f+',x).subs(x,0)*x','10*x/9+Rational(1,3)',649,[TANG],'ORIGINALx0point(0,1/3),finitegradient10/9;integerline10x−9y+3=0. Originalpole−3/2retained.',[DERIV,a.QUOT,a.CHAIN]);p['source_integer_line']='10x−9y+3=0'
add(4,523,'TangenttoORIGINALe^(4x)/(2x+3)atx0,inintegerax+by+c0form10x−9y+3=0. Point(0,1/3)andslope10/9checked.',[p])
f='3*x**2*log(x/6)';p=val('a-gradient-at-P','diff('+f+',x).subs(x,6)','18',649,[a.GRAD],'ORIGINALdomainx>0;actualx-axisinterceptPrequiresln(x/6)0,sox6. Evaluateoriginalderivative18there;theoriginismerelyalimit,notanotherdefinedintercept.',[DERIV,a.PROD])
q=val('b-minimum-coordinates','Tuple(6*exp(-Rational(1,2)),('+f+').subs(x,6*exp(-Rational(1,2))))','Tuple(6*exp(-Rational(1,2)),-54/E)',649,[STAT],'ORIGINALpositive-xstationarity2ln(x/6)+1=0givesx6exp(−1/2). Recoveroriginalordinate−54/e. Secondderivative6>0there,confirminggivenminimumM.',[DERIV,a.PROD]);extra(q,'positive-second-derivative','diff('+f+',x,2).subs(x,6*exp(-Rational(1,2)))','6')
add(5,523,'GIVENf3x²ln(x/6),domainx>0:(a)gradientatx-axisinterceptP(6,0)is18;(b)EXACTminimumM(6e^(−1/2),−54/e). Originlimit0isnotoriginalcurvepoint.',[p,q],'graph')
F='x**3+y**3-9*x*y';p=i.implicit('a-shown-derivative',F,'(3*y-x**2)/(y**2-3*x)',649);p.update(check_mode='show/prove',response_format='proof/show-that')
q=val('b-tangent','4+((-diff('+F+',x)/diff('+F+',y)).subs({x:2,y:4}))*(x-2)','4*x/5+Rational(12,5)',649,[GEOM],'ORIGINAL(2,4)liesoncurve,Fy30nonzero,slope4/5. Requestedintegerline4x−5y+12=0.',[IMPLICIT]);q['depends_on_source_parts']=['a-shown-derivative'];q['source_integer_line']='4x−5y+12=0';extra(q,'original-point-incidence','('+F+').subs({x:2,y:4})','0')
add(6,524,'Originalx³+y³9xy:(a)SHOWdy/dx(3y−x²)/(y²−3x);(b)tangentat(2,4),4x−5y+12=0. OriginalcurveandfiniteFychecked.',[p,q])
F='x**2+2*y**2+5*x+6*y-10';p=val('tangent','-1+((-diff('+F+',x)/diff('+F+',y)).subs({x:2,y:-1}))*(x-2)','8-9*x/2',649,[GEOM],'ORIGINAL(2,−1)incidencevalid,Fy2nonzero;gradient−9/2givesintegerline9x+2y−16=0.',[IMPLICIT]);p['source_integer_line']='9x+2y−16=0';extra(p,'original-point-incidence','('+F+').subs({x:2,y:-1})','0')
add(7,524,'TangenttoORIGINALx²+2y²+5x+6y10at(2,−1),inintegerax+by+c0form9x+2y−16=0.',[p])
p=b.param('a-shown-derivative','1+log(t-2)','t+9/t','(t**2-9)*(t-2)/t**2',649,'Originalt>2;dX/dt1/(t−2)>0.',True)
q=val('b-stationary-coordinates','Tuple((1+log(t-2)).subs(t,3),(t+9/t).subs(t,3))','Tuple(1,6)',649,[GEOM],'Originalt>2excludescandidatest−3andt2. Regularstationaryt3givesbothoriginalcoordinates(1,6).', [PARAM]);q['depends_on_source_parts']=['a-shown-derivative'];extra(q,'complete-original-stationary-parameter','solveset(diff(t+9/t,t),t,domain=Interval.open(2,oo))','FiniteSet(3)')
add(8,524,'OriginalX1+ln(t−2),Yt+9/t,t>2:(a)SHOWderivative;(b)COORDINATESofonlystationarypoint(1,6). Actualparameterdomainrejects−3and2.',[p,q])
p=val('gradient','(diff(4+2*cos(2*t),t)/diff(3*t+sin(2*t),t)).subs(t,pi/6)','-sqrt(3)/2',649,[GEOM],'ORIGINALtπ/6,radian;dX/dt3+2cos2t4nonzero,dY/dt−2√3. Exactgradient−√3/2.',[PARAM,DERIV])
add(9,524,'FindEXACTgradientofORIGINALX3t+sin2t,Y4+2cos2tattπ/6,radians. Correct−√3/2.',[p])
p=val('a-derivative','diff(sin(2*x)+3*cos(2*x),x)','2*cos(2*x)-6*sin(2*x)',649,[DERIV,a.CHAIN],'DifferentiateORIGINALradianf=sin2x+3cos2x,retaininginnerfactor2onbothterms.')
q=reasoning('b-R-form','R=2√10,α=atan3,derivative2√10cos(2x+atan3).','Match ORIGINALcos2xcoefficient2=Rcosαandsin2xcoefficient−6=−Rsinα. Rpositive,αacuteinradians;exactatan3. Printed1.249045isusedonlyasapproximatelydisplayedphase,notanexactidentityorrounded solverinput.',649,'matches');q.update(assessed_8227_demand_ids=[RFORM],component_demand_ids=[DERIV],depends_on_source_parts=['a-derivative'],response_format='symbolic');extra(q,'original-R-form-identity','trigsimp(expand_trig(2*sqrt(10)*cos(2*x+atan(3)))-(2*cos(2*x)-6*sin(2*x)))','0')
r=roots('b-P-Q-abscissas','2*cos(2*x)-6*sin(2*x)-3',['-0.08623','1.979'],649,[('cos','2*x+atan(3)','3/(2*sqrt(10))',1)],unit='radian',hi='pi',approx=True);r.update(assessed_8227_demand_ids=[a.GRAD,RFORM],component_demand_ids=[DERIV],depends_on_source_parts=['a-derivative','b-R-form'],response_format='numeric',correct_original_root_approximations=['P1.979','Q3.055'],source_key_interpretation='NativekeyP−.08623isOUTSIDEoriginal0≤x≤π. CorrectorderedPleft≈1.9788andQright≈3.05536;thekeylosesthecycle-shiftedsecondvalidrootandmislabelsitsretainedone.',original_equation_zero_form='2*cos(2*x)-6*sin(2*x)-3')
rnd(r,'correct-P','pi-(acos(3/(2*sqrt(10)))+atan(3))/2','Rational(1979,1000)',sf=4);rnd(r,'correct-Q','pi+(acos(3/(2*sqrt(10)))-atan(3))/2','Rational(3055,1000)',sf=4)
add(10,524,'GIVENf=sin2x+3cos2xonCLOSED0..π,gradient3atlabelledP/Q:(a)derivative;(b)REQUIREDRcos(2x+α)formthenP/QxvaluesEACH4sf. CorrectP1.979,Q3.055;nativekeyusesoutside−.08623andlosesthecycle-shiftedroot.',[p,q,r],'graph')
refs=[(121,523,'Exercise11Q3 GIVEN exponential-trig graph','Original3e^(−x)sin2xon0..π/2,zeroendpointsandonepositivemaximumM;originrequested tangentpoint.',STAT,'graph','Exercise-11:3'),(122,523,'Exercise11Q5 GIVEN logarithmic curve','Original3x²ln(x/6),x>0,approachesoriginaslimit;realinterceptP(6,0),minimum(6e^(−1/2),−54/e). Do notmakex0defined.',STAT,'graph','Exercise-11:5'),(123,524,'Exercise11Q10 GIVEN labelled trig curve','Originalsin2x+3cos2xon0..π;Pleftpositive-gradientpointnear1.979andQrightnear3.055. NativekeynegativePdoesnotmatchstatedinterval/diagram.',a.GRAD,'graph','Exercise-11:10')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C11:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure',parent_item_id='8227:TB:YM:C11:'+parent);figures[-1]['mathematical_feature_review']['method']='Readoriginalgivengraphlabels,intervals/logdomainsandrequestedpointpositions. Independentlyverifycurvefeaturesandwhole-intervalgradientroots;anoriginlimitdoesnotcreateanundefinedcurvepoint.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=11,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExercise11Q1–10andthreeGIVENgraphsenumerated;ordinaryexercisebeforethe525examstyleheader. CompleteQ10branch/domainerrorretainedwithnativeevidence.',scope_screen='Explicitversusimplicit/parametricgeometrykeptdistinct. Actualpositivearguments,regularpointconditions,finiteintervals,requiredR-formandprecisionretained.')for page in[523,524]]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C11-exercise.json',dict(scope='Complete523–524Exercise11.',items=answers)),('census-YM-C11-exercise.json',dict(book='YM',book_id='8227-SRC-017',chapter=11,source_path=SRC,source_sha256=SHA,scope='Complete523–524page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
