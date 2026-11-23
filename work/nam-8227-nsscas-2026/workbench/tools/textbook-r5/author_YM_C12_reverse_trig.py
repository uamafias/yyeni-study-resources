"""YM542–543: derived cot/sec derivatives and their scaffolded reverse use."""
import json
import author_YM_C12_trig_opening as t
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
TRIG=t.TRIG;IDENT=t.IDENT;DEF=a.DEF;REV='8227:2020:M2:T5:O01:D03';QUOT='8227:2020:M2:T4:O02:D02';PROD='8227:2020:M2:T4:O02:D01';RECIP='8227:2020:M2:T3:O01:D01';DOUBLE='8227:2020:M2:T3:O02:D03';PYTH='8227:2020:M1:T6:O05:D01'
def val(l,e,k,kp,direct,method,components=None,show=False):
 p=a.val(l,e,k,kp,method,direct);p['component_demand_ids']=components or[]
 if show:p.update(check_mode='show/prove',response_format='proof/show-that')
 return p

def derivative(l,fn,key,kp):
 p=val(l,'diff('+fn+',x)',key,kp,[QUOT],'REQUIREDdifferentiatetheORIGINALquotientbythequotientruleinRADIANS. Retainoriginalsine/cosinedenominatoranditsnonzerodomain. Thederivedcot/secformulaistobeshown,notassumedmandatoryrecall.',[RECIP],True);p.update(original_function=fn,original_domain='sinx≠0'if fn=='cos(x)/sin(x)'else'cosx≠0',required_method='Differentiate the original cos/sin or 1/cos quotient.');return p

def dv(l,f,lo,hi,key,kp,direct,show=False):
 p=a.dv(l,f,lo,hi,key,kp);p.update(assessed_8227_demand_ids=direct,component_demand_ids=[],source_angle_unit='radians')
 if show:p.update(check_mode='show/prove',response_format='proof/show-that')
 return p

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(mapping_rationale='Cot/sec derivatives are established from original quotients as requested,then reused by explicit hence/reverse-derivative scaffolding. They are not added as mandatory memorised derivative formulas. Required identity proofs,second derivative product rule,finite evaluation and reverse recognition remain distinct. A finite negative signed integral is legitimate and is not confused with a geometric area.',precision_angle_check=dict(source='Allradianarguments,exactformsandbounds;noangleapproximation.',comparison='Cotangentisoriginalcos/sin,soπ/2isdefinedas0;1/tanonlyonitscommondomain. Retainsine/cosinepoles,allendpointterms,andrequestedmethoddependencies.'))
 return r
p=derivative('a-shown-derivative','cos(x)/sin(x)','-csc(x)**2',542)
q=dv('b-shown-integral','cos(x)**2/sin(x)**2','pi/4','pi/2','1-pi/4',542,[REV,IDENT,DEF],True);q.update(depends_on_source_parts=['a-shown-derivative'],original_integrand='cot(x)**2',integration_input_normalization='Originalcot=cos/sin;π/2isaregularendpoint. Do notexcludeitmerelybecause1/tanhasaremovablegapthere.',required_method='Expresscot²ascsc²−1andusethederivativefrom(a).')
r=val('c-shown-identity','trigsimp(1/(1-cos(2*x))-csc(x)**2/2)','0',542,[DOUBLE,RECIP],'UseORIGINALcos2x=1−2sin²x,so1−cos2x=2sin²x. Bothsidessin x≠0;do notcross-multiplyandextrapolateatzeros.',show=True);r['original_common_domain']='sinx≠0'
s=a.primitive('d-primitive','1/(1-cos(2*x))','-cot(x)/2',542);s.update(assessed_8227_demand_ids=[REV],component_demand_ids=[TRIG,RECIP],original_domain='sinx≠0;independentconstantsbetweenconsecutivezeros.',depends_on_source_parts=['a-shown-derivative','c-shown-identity'],required_method='HENCEusetheidentityfrom(c)andderivativefrom(a);nofreshunscaffoldedcosecantprimitiveformulaassumed.')
add('Example',17,542,'(a)Derivecotderivativefromcos/sin;(b)usecsc²identityand(a)forfinitecot²integral;(c)express1/(1−cos2x)ascsc²x/2;(d)HENCEprimitive−cotx/2.',[p,q,r,s])
p=val('a-derivative','diff(tan(2*x),x)','2*sec(2*x)**2',651,[t.DERIV],'DifferentiateORIGINALtan2xinradianswithinnerfactor2;cos2x≠0.')
q=dv('b-shown-secant-integral','sec(2*x)**2',0,'pi/6','sqrt(3)/2',543,[TRIG,DEF],True);q.update(depends_on_source_parts=['a-derivative'],required_method='Hence,orotherwise:scalederivativefrom(a)by1/2,oruseavalidaffinesec²primitive.')
# R7 native PDF543 prints tan^2 x, while key651 silently uses tan^2(2x).
# Keep the wrong printed key as source evidence; derive from the actual question.
r=dv('b-tangent-square-integral','tan(x)**2',0,'pi/6','sqrt(3)/2-pi/6',651,[IDENT,TRIG,DEF])
r.update(author_expected_normalised='sqrt(3)/3-pi/6',
    method='The original is tan²x on [0, π/6], continuous throughout. Use tan² x = sec² x − 1; independently differentiate tan x − x and evaluate its endpoints. The separate previous sec²(2x) integral does not replace the actual argument x.',
    depends_on_source_parts=[],required_method='Choose tan²x=sec²x−1 and integrate to tanx−x; evaluate the actual bounds 0 and π/6.',
    source_defect_id='TB-YM-C12-TRY17-Q1B-ARGUMENT-KEY',review_date='2026-11-23')
s=dv('c-exact-integral','1/(1+cos(4*x))',0,'pi/6','sqrt(3)/4',651,[TRIG,DEF]);s.update(depends_on_source_parts=['b-shown-secant-integral'],required_method='USEsuppliedcos4x=2cos²2x−1:torewriteintegrandas(1/2)sec²2x. Noindependentidentityselectiondemandadded.')
add('Try-Now-17',1,543,'Part (a): differentiate tan(2x). Part (b): establish the sec²(2x) integral, then choose an identity to integrate the separately printed tan²x. Its key incorrectly uses the doubled argument. Part (c): use the supplied double-angle identity for the integral of 1/(1+cos(4x)). All bounds are 0 to π/6 radians, avoiding the original poles.',[p,q,r,s])
p=val('a-i-identity','trigsimp(sec(x)**2+sec(x)*tan(x)-(1+sin(x))/cos(x)**2)','0',543,[RECIP],'ReplaceORIGINALsecandtanby1/cosandsin/cos,combinewithsamedenominatorcos². Originalcosx≠0.',show=True);p['original_common_domain']='cosx≠0'
q=val('a-ii-identity','trigsimp(sec(x)**2+sec(x)*tan(x)-1/(1-sin(x)))','0',543,[RECIP,PYTH],'HENCEusecos²=(1−sin)(1+sin);onoriginalcosx≠0,both1±sinarenonzero. Cancelonlyonthatcommondomain.',show=True);q.update(depends_on_source_parts=['a-i-identity'],original_common_domain='cosx≠0;theoriginalsec/tansideisundefinedatallcosinezeros,evenwhereasimplifiedRHSisfinite.')
r=derivative('b-shown-secant-derivative','1/cos(x)','sec(x)*tan(x)',543)
s=dv('c-exact-integral','1/(1-sin(x))',0,'pi/4','sqrt(2)',651,[REV,TRIG,DEF]);s.update(depends_on_source_parts=['a-ii-identity','b-shown-secant-derivative'],required_method='USEresults(a)(ii)and(b):integrandsec²+sectan,primitive tan+sec. Originalintervalhasno1−sinzero.')
add('Try-Now-17',2,543,'(a)(i)provecommon-denominatoridentity,(ii)HENCEreciprocal1/(1−sinx);(b)derive secderivativefrom1/cos;(c)USE(a)(ii),(b)forexact0..π/4integral√2. Originalcommon-domainrestrictionsretained.',[p,q,r,s])
p=derivative('a-shown-secant-derivative','1/cos(x)','sec(x)*tan(x)',543);p.update(source_variable='theta',normalised_variable='x')
q=val('b-shown-second-derivative','trigsimp(diff(1/cos(x),x,2)-(2*sec(x)**3-sec(x)))','0',543,[PROD],'HENCEdifferentiatetheproductsectanfrom(a),retainingbothproducttermssec tan²+sec³. Use tan²=sec²−1toget2sec³−sec. Originalcosθ≠0.',[RECIP,PYTH],True);q.update(depends_on_source_parts=['a-shown-secant-derivative'],source_variable='theta',normalised_variable='x',required_method='Henceuse(a),theproductruleandtan²=sec²−1.')
r=val('b-a-b','Tuple(2,-1)','Tuple(2,-1)',651,[PROD],'Readcoefficientsfromtheindependentlyderivedsecondderivative2sec³θ−secθ:a2,b−1. Checkpolynomialcoefficientidentity,notabarecopiedtuple.',[RECIP]);r['depends_on_source_parts']=['b-shown-second-derivative'];extra(r,'second-derivative-coefficients','trigsimp(diff(1/cos(x),x,2)-(2*sec(x)**3-sec(x)))','0')
s=dv('c-exact-signed-integral','1+tan(x)**2-3*sec(x)*tan(x)',0,'pi/4','4-3*sqrt(2)',651,[REV,IDENT,TRIG,DEF]);s.update(source_variable='theta',normalised_variable='x',depends_on_source_parts=['a-shown-secant-derivative'],required_method='Use1+tan²=sec²andthederivedsecderivative. Primitive tan−3sec. Negativefinal4−3√2islegitimateSIGNEDintegral,notanarea.')
add('Try-Now-17',3,543,'(a)Derive secθderivativefrom1/cosθ;(b)HENCEsecondderivativeandcoefficientsa2,b−1;(c)exact0..π/4integral1+tan²θ−3secθtanθ=4−3√2. Differentiateandreverse-usegenuinegivenresults.',[p,q,r,s])
refs=[(53,542,'Example17(a) required cotangent quotient working','Differentiatecos/sinbyquotientrule;Pythagoreanidentitygives−csc².', [QUOT,RECIP],'Example:17'),(54,542,'Example17(b) scaffolded cotangent-square integral','cot²=csc²−1;primitive−cot−xfrom(a),regularendpointπ/2.',[REV,IDENT,DEF],'Example:17'),(55,542,'Example17(b) derivative sign reminder','d(cotx)=−csc²x,so d(−cotx)=csc²x. Thisisderivedsupport,notamandatoryrecalllistaddition.',[REV],'Example:17'),(56,542,'Example17(c) double-angle reciprocal working','1−cos2x=2sin²x;originalsinx≠0.',[DOUBLE,RECIP],'Example:17'),(57,542,'Example17(c) double-angle reminder inset','Suppliedcos2x=1−2sin²xguidesthereciprocalrewrite.',[DOUBLE],'Example:17'),(58,542,'Example17(d) reverse derivative working','Use(a),(c)for−cotx/2+C,oneconstantpercomponent.',[REV],'Example:17'),(59,542,'Example17(d) derivative-scale reminder','d(−cotx/2)=(1/2)csc²x,notnegativecsc²/2.',[REV],'Example:17')]
for n,page,label,note,ds,parent in refs:
 fig(n,page,label,note,ds,'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readrequiredquotientmethod,eachHENCE/USEcue,fullcotangentdomain,andradianbounds. Independentlydifferentiateoriginalquotientsandcheckallfiniteintegrals. NoextraMandatoryrecallorvisualresponseinferred.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample17(a–d),Try17Q1–3withallsuboutputs,andactualExample17working/reminderpanelsenumerated. Try17Q3constantsaretwooutputsaftershownsecondderivative;sourceθnormalizedconsistently.',scope_screen='Derivedcot/secformulasandreverserecognitionareexplicitlyscaffolded. Noautomaticmandatoryderivativerecalladdition;allcommon-domainandfinite-intervalconditionsretained.')for page in range(542,544)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'],str(got))
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-reverse-trig.json',dict(scope='Complete542–543derivedcot/secandreverse-useresponses.',items=answers)),('census-YM-C12-reverse-trig.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete542–543page/item/panelcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
