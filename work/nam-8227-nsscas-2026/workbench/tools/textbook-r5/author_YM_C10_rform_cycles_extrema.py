"""YM472–475: exact-radian phases,multiple cycles and representative extrema."""
import json
from author_Goldie_C3_rform_intro import rform
from author_YM_C4_composite_equations import roots
import author_YM_C10_opening as o
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
RFORM='8227:2020:M2:T3:O02:D04';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';RANGE='8227:2020:M1:T3:O02:D02';D='(x*pi/180)'

def form(label,a,b,target,key,kp,unit='degree',dp=2):
 p=rform(label,a,b,target,unit,key,kp,['0','90']if unit=='degree'else['0','pi/2'],dp);p.update(assessed_8227_demand_ids=[RFORM],component_demand_ids=[o.COMPOUND],response_format='symbolic',original_sine_coefficient=a,original_cosine_coefficient=b);return p

def bounded(label,expr,key,kp,branch,unit='degree',opened=False):
 p=roots(label,expr,key,kp,[branch],unit=unit,approx=isinstance(key,list),opened=opened);p.update(assessed_8227_demand_ids=[RFORM,BND,ALL],response_format='numeric',original_equation_zero_form=expr,method='Use ORIGINALcoefficientsandtheactualargumentmultiplier,withunroundedphase. TransformtheWHOLEboundedintervalbeforeenumeratingallphasebranches/cycles;thenrecoveroriginalxandcompareprintedvalues. Exactradianphasesstayexact.');return p

def value(label,expr,key,kp,direct,method,dp=None,show=False):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,response_format='proof/show-that'if show else'symbolic')
 if dp is not None:p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp}
 if show:p['check_mode']='show/prove'
 return p

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts);r.update(mapping_rationale='Distinguish exact-radian phase/coefficient recovery,all roots across repeatedcycles,and extremumvalues/attainingarguments. A source request for the OTHER solution excludes the alreadygivenroot;thecompleteoriginalsetisstill independentlychecked. Unrestrictedextremumargumentsareperiodic;sourcepositiverepresentativesarenotuniquerealanswers.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='within'if kind!='Example'or n!=23 else'not applicable',quoted_value=note,reason='Solvedoriginalinputmultipliers1,2,3areexplicitandtheirwholefiniteintervalskept;anextremumexpressionisnotaboundedperiodicequationset.'),dict(rule_id='8227:LIMIT02',status='within'if kind!='Example'or n!=23 else'not applicable',quoted_value=note,reason='Finiteintervalrootsasked. Example23asksattainingxwithoutastatedinterval;sourceworkingusesonepositivecycle representative,notanewgeneral-solutionrequirement.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03','8227:LIMIT02']),precision_angle_check=dict(source='Exactradianphases/anglesinExample21/Try21;explicit2dpdegreephasesinotherformtasks. Sourceboundeddegree/attaininganglekeysgenerally1dp.',comparison='Keepfullphaseprecision. Do not lose2xor3xcycles,roundthebasicanglebeforedividing,orinterpretonepositiveextremumrepresentativeasuniqueforallrealx.'))
 return r
p=form('a-R-phase','-1','5','cos-plus','Tuple(sqrt(26),Rational(1131,100))',644)
q=bounded('b-roots',f'5*cos({D})-sin({D})-4',['27.0','310.4'],644,('cos','x+180*atan(1/5)/pi','4/sqrt(26)',1),opened=True);q['depends_on_source_parts']=['a-R-phase']
add('Try-Now-20',2,472,'Original5cosθ−sinθhas√26cos(θ+α),α11.31°;original4-equationonSTRICT0..360has27.0,310.4.',[p,q])
p=form('a-R-phase','sqrt(3)','1','cos-minus','Tuple(2,pi/3)',472,'radian',None)
q=value('b-shown-given-root','cos(7*pi/12)+sqrt(3)*sin(7*pi/12)','sqrt(2)',472,[RFORM],'Substitute the GIVEN7π/12into the ORIGINALcosθ+√3sinθ;exact simplificationgives√2. This demonstrates the suppliedroot ratherthan merelyrepeatingitslabel.',show=True)
r=value('b-other-root','Complement(solveset(2*cos(x-pi/3)-sqrt(2),x,domain=Interval.open(0,2*pi)),FiniteSet(7*pi/12))','FiniteSet(pi/12)',472,[RFORM,BND,ALL],'Use the independentlyverifiedEXACTpart(a)R-form,hencecos(θ−π/3)=√2/2onORIGINAL0<θ<2π. Obtain bothπ/12,7π/12,thenremoveonlytheKNOWNgivenrootbecause the questionasks the OTHER solution. Do not call the one requestedotherroot an incomplete fullanswer.');r.update(depends_on_source_parts=['a-R-phase','b-shown-given-root'],complete_original_solution_set='FiniteSet(pi/12,7*pi/12)')
r['additional_operations']={'complete-original-root-set':{'kind':'bounded-trig-equation','operands':['cos(x)+sqrt(3)*sin(x)-sqrt(2)','0','2*pi'],'left_open':True,'right_open':True}}
r['additional_operation_expected']={'complete-original-root-set':'FiniteSet(pi/12,7*pi/12)'}
add('Example',21,472,'ExactradianR-formforcosθ+√3sinθgivesR2,απ/3. Showgivenθ7π/12satisfiestheoriginal√2-equation;findOTHERθπ/12inSTRICT0..2π.',[p,q,r])
p=form('a-R-phase','1','sqrt(3)','cos-minus','Tuple(2,pi/6)',644,'radian',None)
q=bounded('b-roots','sqrt(3)*cos(x)+sin(x)-1','FiniteSet(pi/2,11*pi/6)',644,('cos','x-pi/6','1/2',1),'radian',True);q['depends_on_source_parts']=['a-R-phase']
add('Try-Now',21,473,'Original√3cosθ+sinθhasexactR2,απ/6inradians;original=1onSTRICT0..2πgivesπ/2and11π/6. Preserveexactanswers.',[p,q])
p=form('a-R-phase','7','-6','sin-minus','Tuple(sqrt(85),Rational(4060,100))',473)
q=bounded('b-three-cycle-roots',f'7*sin(3*{D})-6*cos(3*{D})-Rational(19,5)',['21.6','65.4','141.6','185.4','261.6','305.4'],473,('sin','3*x-180*atan(6/7)/pi','19/(5*sqrt(85))',1));q.update(depends_on_source_parts=['a-R-phase'],source_solution_label='Nativeworkedsolutionlabelisoverwritten/looks(c),withanaddedstroke. Theactualstemlabelsit(b);stablepartIDfollowsthatunambiguousstem.',actual_argument_interval='0≤3x≤1080degreesbeforetheexactphaseshift.')
add('Example',22,473,'Original7sinθ−6cosθasksR√85/phase40.60°. HENCEtheDIFFERENT3xargument7sin3x−6cos3x=3.8on0..360needsSIXoriginalroots. Stemb/rootworkingcnumberingmismatchrecorded.',[p,q])
p=form('a-R-phase','-1','3','cos-plus','Tuple(sqrt(10),Rational(1843,100))',644)
q=bounded('b-two-cycle-roots',f'3*cos(2*{D})-sin(2*{D})-2',['16.2','145.4','196.2','325.4'],644,('cos','2*x+180*atan(1/3)/pi','2/sqrt(10)',1));q.update(depends_on_source_parts=['a-R-phase'],actual_argument_interval='0≤2x≤720degreesbeforetheexactphaseshift.')
add('Try-Now',22,474,'Original3cosθ−sinθasksR√10/phase18.43°. HENCEsolveits2xversion=2on0..360:FOURoriginalroots16.2,145.4,196.2,325.4.',[p,q])
ps=[]
for label,a,b,target,keyR,phase,maxangle,minangle,kmax,kmin in [('a','2','5','sin-plus','sqrt(29)','atan(Rational(5,2))','90-180*atan(Rational(5,2))/pi','270-180*atan(Rational(5,2))/pi','Rational(218,10)','Rational(2018,10)'),('b','-sqrt(3)','2','cos-plus','sqrt(7)','atan(sqrt(3)/2)','360-180*atan(sqrt(3)/2)/pi','180-180*atan(sqrt(3)/2)/pi','Rational(3191,10)','Rational(1391,10)')]:
 phasekey='Rational(6820,100)'if label=='a'else'Rational(4089,100)'
 p=form(label+'-R-phase',a,b,target,'Tuple('+keyR+','+phasekey+')',475);p['parameter_normalisation']='Use the sourceworkedpositiveamplitude/acutephase convention. The questiondoesnotseparatelyrequireallphase-equivalentrepresentations.';ps.append(p)
 for suffix,expr,key,method,dp in [('maximum-value','sqrt(('+a+')**2+('+b+')**2)',keyR,'The ORIGINALunrestrictedlineartrigexpressionhasglobalmaximumthepositivecoefficientnorm,becauseitsverifiedR-formattainsunitcosine/sine. No anglewindowisgiven.',None),('maximum-x',maxangle,kmax,'Solve the verifiedunittrigfactor=1,thenreporttheSOURCEpositive0..360representative. Othercoterminalargumentsalsovalidbecauseoriginalstemhasnointerval.',1),('minimum-value','-sqrt(('+a+')**2+('+b+')**2)','-'+keyR,'The ORIGINALglobalminimumisthenegativecoefficientnorm;itisattainedwhentheverifiedunittrigfactor=−1.',None),('minimum-x',minangle,kmin,'Solve the verifiedunittrigfactor=−1andreporttheSOURCEpositive-cycle representative. This is not the unique real attainingargument.',1)]:
  p=value(label+'-'+suffix,expr,key,475,[RFORM,RANGE],method,dp);p.update(original_expression='('+a+')sinx+('+b+')cosx',attaining_angle_convention='Degreeworkinginthesource;positive0..360representativeonly,noexplicitquestioninterval.');ps.append(p)
 # Validate the actual ORIGINAL extremum value and zero derivative at exact representatives.
 original='('+a+')*sin(x)+('+b+')*cos(x)'
 maxrad='pi/2-('+phase+')'if label=='a'else'2*pi-('+phase+')';minrad='3*pi/2-('+phase+')'if label=='a'else'pi-('+phase+')'
 extra(ps[-4],'original-at-exact-maximum','('+original+').subs(x,'+maxrad+')',keyR);extra(ps[-3],'original-maximum-derivative','diff('+original+',x).subs(x,'+maxrad+')','0')
 extra(ps[-2],'original-at-exact-minimum','('+original+').subs(x,'+minrad+')','-'+keyR);extra(ps[-1],'original-minimum-derivative','diff('+original+',x).subs(x,'+minrad+')','0')
row=add('Example',23,475,'TwooriginalR-form/extremumtasks:2sinx+5cosxhas±√29atpositivecycle21.8/201.8degrees;2cosx−√3sinxhas±√7at319.1/139.1. Noquestioninterval;theseareSOURCErepresentatives,nottheonlyrealattainingangles.',ps);row['original_domain']='Allrealx;bookworkedanglesindegrees. Coterminalextremumargumentsnotexcluded.'
refs=[(95,472,'Example21 exact-radian coefficient working','Originalcos1/sin√3givesR2,απ/3;notadecimaldegreephase.',RFORM,'table','Example:21'),(96,472,'Example21 radianπ/6/π/3 solution triangle','Sides1,√3,2supplyexactphaseπ/3.',RFORM,'diagram','Example:21'),(97,472,'Example21 radianπ/4 given-root evaluation triangle','Theknown7π/12becomesphaseargumentπ/4;√2/2exact.',RFORM,'diagram','Example:21'),(98,472,'Example21 two exact phase branches','Original0<θ<2πcontainsπ/12and7π/12;onlytheformeristheOTHERrequestedroot.',ALL,'diagram','Example:21'),(99,473,'Example22 R-form coefficient working','7,−6gives√85andacutephase40.60degreeapproximation;unroundedphaseusedforroots.',RFORM,'table','Example:22'),(100,473,'Example22 shifted 3x quadrant diagram','ArgumentcoversTHREEfullturnsbeforephaseshift. Recoveroriginalxbydividingafterallbranches.',ALL,'diagram','Example:22'),(101,473,'Example22 three-revolution root working','Twoadmissiblephasebranchesineachofthreecyclesgivesixoriginalxroots;printed(c)workingbelongstostem(b).',ALL,'table','Example:22'),(102,474,'Sine maximum/minimum guide','Unit sineattains±1;positiveamplitudescalesrangeto[−R,R].',RANGE,'graph',None),(103,474,'Cosine maximum/minimum guide','Unit cosineattains±1;maximum/minimumargumentsdifferfromsine-targetones.',RANGE,'graph',None),(104,474,'R-form global range derivation','For nonzerocoefficientpairR=√(a²+b²)>0,therangeis[−R,R]. Zero pair givesconstant0andno uniquephase.',RANGE,'table',None),(105,474,'R-form extrema summary panel','Globalmaximum+R/minimum−Rrequireattainingunitfactor±1;astatedrestrictedintervalwouldneedaseparateattainmentcheck.',RANGE,'table',None),(106,475,'Example23a coefficient/extremum working','Originalsin2/cos5gives√29,phase68.20;sourcepositiveattainingrepresentatives21.8/201.8degrees.',RFORM,'table','Example:23'),(107,475,'Example23a SOLUTION sine extrema guide','Sineunitfactoris+1at90and−1at270;subtracttheactualphasefororiginalx.',RANGE,'graph','Example:23'),(108,475,'Example23b coefficient/extremum working','Originalcos2/sin−√3gives√7,phase40.89;positivecosine-targetrepresentatives319.1/139.1.',RFORM,'table','Example:23'),(109,475,'Example23b SOLUTION cosine extrema guide','Cosineunitfactoris+1at0/360and−1at180;thephaseisADDED,sooriginalxsubtractsphase.',RANGE,'graph','Example:23')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent if parent else None);figures[-1]['mathematical_feature_review']['method']='Readactualdegree/radianphases,known-versus-otherrootrequest,2x/3xintervals,andglobalversusrestrictedextremumcontext. Verifyoriginalcoefficientnormsandattainingvalues/derivativesindependently.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry20Q2,Example21/Try21,Example22/Try22,Example23and15actualreference/solutionpanelsenumerated. Exactradians,multiplecyclesandrepresentativeextremumangleskeptdistinct.',scope_screen='Actualsmallmultiplierrootintervalskept;unrestrictedextremumrepresentativesarenotsilentlymadeuniqueorconvertedintoanassessedgeneralsolutionrequirement.')for page in range(472,476)]
def save():
 for name,data in [('answers-YM-C10-rform-cycles-extrema.json',dict(scope='Complete472–475exactphases,multiplecyclesandoriginalextrema.',items=answers)),('census-YM-C10-rform-cycles-extrema.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete472–475page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
