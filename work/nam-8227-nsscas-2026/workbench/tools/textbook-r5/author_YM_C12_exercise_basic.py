"""YM552: each Basic/Intermediate Exercise12 item and its actual requested outputs."""
import json
import author_YM_C12_trig_powers as t
import author_YM_C12_trapezium_bias as b
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
EXP=a.EXP;DEF=a.DEF;TRIG=t.TRIG;IDENT=t.IDENT;SQUARE=t.SQUARE;LOG=a.LOG

def add(n,note,parts,rep='text'):
 r=a.add('Exercise-12',n,552,note,parts);r.update(representation=rep,mapping_rationale='EveryExercise12itemhasitsownactualintegrandandaskedanswerform. Requiredwithout-calculator/exactsingle-logformsarepreserved. Finiteboundequationssolvethepositiveparameter;ordinaryintegrationisnotmistakenforanaskedsketch. Common-lognodeevaluationdoesnotrequireaderivationbychangeofbase.',precision_angle_check=dict(source='ExactformsinQ1–3,Q4(a,b),Q5–6. Q4(c)prescribestwo-intervalestimate1decimalplace. Trigargumentsradians.',comparison='Retainarbitraryconstantsandoriginalpolesforprimitives;checkcontinuitybeforefiniteendpointsubtraction. Internalexactlogratiosarenotmandatedlearnermethods.'));return r

def primitive(l,f,key,ds,components=None):
 p=a.primitive(l,f,key,651);p.update(assessed_8227_demand_ids=ds,component_demand_ids=components or[],original_domain='Originalrealintegranddomain;retaincos2x≠0forQ3(a),cosθ≠0forQ5(a),andexponentialdenominatorsneverzero.');return p
p=a.dv('shown-integral','6/(2*x+1)',1,7,'log(125)',552);p.update(check_mode='show/prove',response_format='proof/show-that')
add(1,'SHOW1..7integral6/(2x+1)=ln125. Originalintervalstaysrightofpole−1/2;exactlogratio5multipliedby3.',[p])
p=a.dv('exact-integral','sin(x/2)',0,'2*pi/3','1',651);p.update(assessed_8227_demand_ids=[TRIG,DEF],source_angle_unit='radians')
add(2,'Finite0..2π/3integralsin(x/2),innerfactor1/2requiresprimitive−2cos(x/2);exact1.',[p])
p=primitive('a-primitive','(1+cos(2*x)**4)/cos(2*x)**2','tan(2*x)/2+sin(4*x)/8+x/2',[IDENT,SQUARE],[TRIG]);p['original_domain']='cos2x≠0;independentconstantsoneachconnectedcomponent.'
q=a.dv('b-single-log','2+6/(3*x-2)',4,14,'log(16*exp(20))',651);q.update(required_method='Withoutusingacalculator;giveexactform ln(ae^b)withintegera,b.',author_answer_form='ln(16e^20),a16,b20;theinternalsimplified20+ln16isnotanalternativetotheexplicitlyrequestedpresentation.');extra(q,'requested-form-normalization','log(16*exp(20))','20+log(16)')
add(3,'(a)Primitiveof(1+cos⁴2x)/cos²2xrequiresdivisiontosec²2x+cos²2xthenpowerreduction;(b)exact4..14integral2+6/(3x−2),WITHOUTCALCULATORinln(ae^b)form,ln(16e20).',[p,q])
p=primitive('a-primitive','(4+exp(x))/(2*exp(2*x))','-exp(-2*x)-exp(-x)/2',[EXP]);p['original_domain']='Allrealx;exponentialdenominatorpositive.'
q=a.dv('b-single-log','1/(2*x+5)',2,10,'log(Rational(5,3))',651);q.update(required_method='Withoutusingacalculator,giveformlnk.',author_answer_form='ln(5/3),nottheunsimplifiedhalf-logratioform. Originalinterval2..10excludespole−5/2.')
r=b.estimate('c-trapezium','log(x+2)/log(10)',0,6,2,'Rational(39,10)',651,dp=1);r.update(source_function='log_10(x+2)',source_common_log_base=10,source_diagram_label_anomaly='Graphshapeandboundsareforlog10(x+2),butitslabelrepeatsintegralfrompart(b). Useexplicitstemfunction;retainnativeevidence.')
add(4,'(a)Exponentialquotientprimitive;(b)WITHOUTCALCULATOR2..10reciprocalintegralinlnkform;(c)GIVENcommon-logcurve log10(x+2),0..6,REQUIREDtwo-stripestimate1dp3.9. Preservebase10andignorewrongrepeatedpart(b)graphlabelasdata.',[p,q,r],'graph')
p=primitive('a-primitive','(4+sin(x)**2)/(1-sin(x)**2)','5*tan(x)-x',[IDENT,TRIG]);p.update(source_variable='theta',normalised_variable='x',original_domain='cosθ≠0;primitiveonoriginalconnectedcomponents.')
q=a.val('b-a','solve(integrate(2/(3*x+1),(x,0,a))-log(16),a)[0]','21',651,'Originala>0. Integral(2/3)ln(3a+1)=ln16implies3a+1=64,a21. ChecktheORIGINALfiniteintegralanditsdenominatorpositiveon[0,21].',[EXP,DEF,LOG]);extra(q,'original-parameter-equation','integrate(2/(3*x+1),(x,0,21))','log(16)')
add(5,'(a)Radianprimitive(4+sin²θ)/(1−sin²θ),usePythagoreanrewrite5sec²θ−1;(b)givenpositiveboundintegral2/(3x+1)=ln16,recovera21.',[p,q])
p=a.dv('a-exact-integral','sin(x)*(4*sin(x)+6*cos(x))',0,'pi/4','pi/2+Rational(1,2)',651);p.update(assessed_8227_demand_ids=[IDENT,SQUARE,DEF],component_demand_ids=[TRIG],source_angle_unit='radians')
q=a.val('b-a','solve(integrate(6/(3*x+2),(x,0,a))-log(49),a)[0]','4',651,'Originala>0. Integral2ln((3a+2)/2)=ln49=2ln7;positiveargumentgives3a+2=14,a4. Substituteintotheoriginalintegral.',[EXP,DEF,LOG]);extra(q,'original-parameter-equation','integrate(6/(3*x+2),(x,0,4))','log(49)')
add(6,'(a)Exact0..π/4integralsinx(4sinx+6cosx),expandthenpower/productreduce,resultπ/2+1/2;(b)positiveboundequation6/(3x+2)integralln49givesa4.',[p,q])
fig(109,552,'Exercise12Q4(c) GIVEN common-log area graph','Explicitstemislog10(x+2),0≤x≤6,withpositivey-interceptlog10(2). Sourcegraphlabelerroneouslyrepeatsthepart(b)reciprocalintegral;thatlabelmustnotbeusedasthecurveequation.',[b.TRAPSET],'graph',[],'Exercise-12:4');figures[-1].update(item_id='8227:TB:YM:C12:Teaching-figure:109',printed_page=pp(552),source_evidence=ev(552),value_level_scope_decisions=[],item_kind='given-figure',parent_item_id='8227:TB:YM:C12:Exercise-12:4');figures[-1]['mathematical_feature_review']['method']='Readexplicitstemcommon-logbase,actualboundsandpositivecurve;nativecropchecksthewrongsourcegraphlabel. Independentlycomputeoriginalnodeordinatesandestimate.'
pages=[dict(pdf_page=552,printed_page=pp(552),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers]+[r['item_id']for r in figures],continuation_item_ids=[],source_evidence=ev(552),reader='Codex author',date='2026-11-20',non_item_content='Exercise12Q1–6withallpartsandtheactualQ4(c)GIVENgraphenumerated. Basic/Intermediateheadinglabelsarethedifficultyorganisationofthebook,notverifiedBloomlevels.',scope_screen='Radianintegration,finitecontinuouslogintervals,positiveunknownbounds,andrequiredcommon-lognumericalestimate. Single-loganswerformsandwithout-calculatorconditionretained.')]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-exercise-basic.json',dict(scope='Complete552Exercise12Q1–6actualresponses.',items=answers)),('census-YM-C12-exercise-basic.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete552page/item/GIVENgraphcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
