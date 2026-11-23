"""YM554–555: textbook exam-style identity chains, removable endpoints and asked sketches."""
import json
import author_YM_C12_trig_powers as t
import author_YM_C12_trapezium_bias as b
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
TRIG=t.TRIG;IDENT=t.IDENT;SQUARE=t.SQUARE;DEF=a.DEF;DOUBLE=t.DOUBLE;RECIP='8227:2020:M2:T3:O01:D01';SKETCH='8227:2020:M2:T5:O04:D01';BIAS=b.BIAS

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(exam_style=True,exam_style_basis='Explicit12.5Exam-StyleQuestionsheadingon554;notverifiedoriginalexamprovenance.',sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='RequiredidentityproofandHENCEusearedistinctoutputs;suppliedidentitydoesnotautomaticallyassessanewchoice. ASKEDsketchandjustifiednumericalbiasareseparateresponses. Example23endpointremovabilityisexplicitlyhandledbyseparateconvergentlimits,notinvalidrawsubstitutionorprincipalvalue.',precision_angle_check=dict(source='Exactradianidentities/values/integrals;Example24estimate3dp0.899,Try24estimate2sf0.90.',comparison='Keep0.90trailingzeroasprecisiondisplay. Originaltan/cotcommon-domainrestrictionsandfiniteendpointlimitsretained. Sketchcriteriaarederivedandcomparedwithbook,notanofficialmarkingtable.'))
 if any(BIAS in p.get('assessed_8227_demand_ids',[])or SKETCH in p.get('assessed_8227_demand_ids',[])for p in parts):
  r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL11',status='within',quoted_value=note,reason='Simplecsc/secgraphswithinexplicitradianviewportsandpole-freeintegrationintervals. Chordgeometryjustifiesbias;formalcurvatureoptional.'))
  r['scope_check']['limits_considered'].append('8227:QUAL11')
 return r

def proof(l,lhs,rhs,kp,method,ds):
 p=t.proof(l,lhs,rhs,kp,method);p['assessed_8227_demand_ids']=ds;return p
p=proof('a-identity','tan(x)+cot(x)','2/sin(2*x)',554,'ReplaceORIGINALtanandcotbysin/cosandcos/sin;Pythagoreanidentitygives1/(sincos). Double-angle2sincos=sin2xprovestargetonoriginalsinxcosx≠0.',[RECIP,DOUBLE]);p['original_common_domain']='sinxcosx≠0'
q=a.val('b-i-exact-value','tan(pi/8)+cot(pi/8)','2*sqrt(2)',554,'HENCEsubstituteπ/8intoprovedidentity,so2/sinπ/4=2√2. Retainexactradicalandoriginalnonzerodenominators.',[RECIP,DOUBLE]);q['depends_on_source_parts']=['a-identity']
r=a.reasoning('b-ii-integral','3;originalendpointsareremovablewithfiniteone-sidedlimits.','On0<θ<π/2,ORIGINAL6/(tanθ+cotθ)=3sin2θ. Originaltan/cotformisundefinedatbothendpoints,butitsone-sidedlimitsare0. Integrateeachhalfseparatelybylimits:0..π/4gives3/2andπ/4..π/2gives3/2. Bothconverge;sum3. Thisisnotaprincipal-valuecancellation.',554,'matches');r.update(assessed_8227_demand_ids=[TRIG,DEF],component_demand_ids=[RECIP,DOUBLE],given_representation='text',response_format='numeric',depends_on_source_parts=['a-identity'],original_integrand='6/(tan(x)+cot(x))',original_bounds=['0','pi/2'],improper_integral=True,original_domain='0<x<π/2;bothendpointformulasundefinedbutremovable.')
extra(r,'original-left-end-limit','limit(6/(tan(x)+cot(x)),x,0,dir="+")','0');extra(r,'original-right-end-limit','limit(6/(tan(x)+cot(x)),x,pi/2,dir="-")','0');extra(r,'separate-left-integral','limit(integrate(3*sin(2*x),(x,b,pi/4)),b,0,dir="+")','Rational(3,2)');extra(r,'separate-right-integral','limit(integrate(3*sin(2*x),(x,pi/4,pi/2-b)),b,0,dir="+")','Rational(3,2)')
r['additional_operations']['continuous-extension-integral']={'kind':'proper-definite-integral','operands':['3*sin(2*x)','0','pi/2']};r['additional_operation_expected']['continuous-extension-integral']='3'
add('Example',23,554,'(a)PROVEtanθ+cotθ=2/sin2θ;(b)HENCE(i)exactvalueatπ/8,2√2,(ii)0..π/2integral6/(tan+cot)=3. Originalundefinedendpointsareexplicitlytreatedasremovablelimits.',[p,q,r])
lhs='(cos(2*x)+9*cos(x)+5)/(cos(x)+4)'
p=proof('a-identity',lhs,'2*cos(x)+1',652,'Usecos2x=2cos²x−1;factororiginalnumerator(2cosx+1)(cosx+4). Denominatorcosx+4≥3,sonopoleorinvalidcancellation.',[DOUBLE])
q=t.dv('b-exact-integral','(cos(4*x)+9*cos(2*x)+5)/(cos(2*x)+4)','-pi','pi','2*pi',652,[TRIG,DEF]);q.update(depends_on_source_parts=['a-identity'],required_method='HENCEapply(a)withangle2x;integrand2cos2x+1. Originaldenominator≥3throughoutbounds.')
# The CAS leaves the original rational trig integral unresolved. Use the
# already-proved HENCE identity and independently verify this exact rewrite.
q['operation']['operands'][0]='2*cos(2*x)+1'
q['integration_input_normalization']='Original quotient equals2cos2x+1;denominatorcos2x+4≥3,so no canceled pole. Original integrand retained.'
extra(q,'original-integrand-rewrite','trigsimp(expand_trig((cos(4*x)+9*cos(2*x)+5)/(cos(2*x)+4)-(2*cos(2*x)+1)))','0')
add('Try-Now-23',1,554,'(a)SHOWrationalcosineidentitywithstrictlypositivedenominator;(b)HENCEexact−π..πintegralafterreplacingangleby2x,result2π.',[p,q])
p=proof('a-half-angle','cos(x)**2','(cos(2*x)+1)/2',652,'Rearrangecos2x=2cos²x−1;actualaskedoutputisanexpressionforcos².',[DOUBLE])
q=t.dv('b-shown-integral','cos(x)**2',0,'pi/3','pi/6+sqrt(3)/8',554,[SQUARE,DEF],True);q['depends_on_source_parts']=['a-half-angle']
r=t.dv('c-complementary-integral','sin(x)**2',0,'pi/3','pi/6-sqrt(3)/8',652,[IDENT,SQUARE,DEF]);r.update(depends_on_source_parts=['b-shown-integral'],required_method='Byappropriateidentitysin²=1−cos²,DEDUCEfrom(b). Thechoiceofcomplementaryidentityisactuallyasked.')
add('Try-Now-23',2,554,'(a)Expresscos²intermsofcos2x;(b)HENCEshowfinite0..π/3cos²integral;(c)CHOOSEidentitytoDEDUCEsine-squareintegralπ/6−√3/8.',[p,q,r])

def sketch(l,fn,kind,kp):
 iscsc=kind=='csc'
 answer='Positive decreasing upward-bending csc curve on0<x≤π/2,asymptotex0,endpoint(π/2,1),point(π/4,√2).'if iscsc else'Positive increasing upward-bending sec curve on0≤x≤π/4,from(0,1)to(π/4,√2).'
 why='Originalsinx>0inviewport;derivative−cosx/sin²x≤0andsecond(1+cos²x)/sin³x>0. Asx→0+,cscx→+infinity.'if iscsc else'Originalcosx>0inviewport;derivativesin/cos²≥0andsecond(1+sin²)/cos³>0. Noverticalasymptoteinsideaskedviewport.'
 p=a.reasoning(l,answer,why,kp,'sketch');p.update(assessed_8227_demand_ids=[SKETCH],component_demand_ids=[],given_representation='text',response_format='sketch',credited_features=answer.split(','),criteria_basis='Author-derivedoriginalfunctionfeaturescomparedwithsourceworkedsketchorbookkey;noofficialawardtable.')
 return p
p=t.ip('a-primitive','(sin(x)-cos(x))**2','x+cos(2*x)/2',555);p.update(assessed_8227_demand_ids=[IDENT,SQUARE],component_demand_ids=[TRIG])
# Fixed-source QA: the default CAS chooses x-sin²x or x+cos²x across
# process hash seeds. Both differentiate to the original integrand and differ
# by a constant. Choose a stable integration algorithm,not the printed key.
p['operation']['integration_algorithm']='manual'
p['primitive_representation_note']='Manual algorithm fixed after six-seed scan exposed additive-constant representation drift; original integrand remains the independent computation input.'
q=b.estimate('b-i-estimate','1/sin(x)','pi/4','pi/2',2,'Rational(899,1000)',555,dp=3,rep='text')
r=sketch('b-ii-sketch','1/sin(x)','csc',555)
s=b.bias('b-ii-bias','Overestimate:straightchordslieabovecurve.','Onoriginalπ/4..π/2,theupward-bendingcosecantgraphhaschordsaboveit. TheASKEDlargerview0<x≤π/2showsasymptote0butnointegrationthroughit. Formalpositivecurvatureisindependentauthorcheck.',555,('diff(1/sin(x),x,2)','(1+cos(x)**2)/sin(x)**3'),'π/4≤x≤π/2','concave (YM upward-bending convention)');s['depends_on_source_parts']=['b-i-estimate','b-ii-sketch']
add('Example',24,555,'(a)Primitive(sin−cos)²byexpansion/identities;(b)(i)two-intervalcscestimateπ/4..π/2,to3dp0.899,(ii)ASKEDsketch0<x≤π/2andjustifyoverestimate. Integralasymptoteisoutsidetheactualfiniteinterval.',[p,q,r,s])
p=b.estimate('a-estimate','1/cos(x)',0,'pi/4',2,'Rational(9,10)',652,sf=2,rep='text');p['printed_key_display']='0.90 units² (2 significant figures)'
q=sketch('b-sketch','1/cos(x)','sec',652)
r=b.bias('b-bias','Overestimate:straightchordsabovetheupward-bendingcurve.','Onoriginal0..π/4,secxpositive,increasingandupwardbending. Thechordposition,notincreasingalone,justifiesoverestimate. Sourcekeysketchshowstheboundedradianintervalandlabels0.90fortheestimate.',652,('diff(1/cos(x),x,2)','(1+sin(x)**2)/cos(x)**3'),'0≤x≤π/4','concave (YM upward-bending convention)');r['depends_on_source_parts']=['a-estimate','b-sketch']
add('Try-Now',24,555,'(a)REQUIREDtwo-intervalsecestimate0..π/4,to2sf0.90;(b)ASKEDappropriateboundedsketchanddetermineoverestimate. Retaintrailingzerofor2sf.',[p,q,r])
refs=[(112,554,'Example23(a) identity proof working','Bothsides1/(sincos)onoriginalsinxcosx≠0.',[RECIP,DOUBLE],'table','Example:23'),(113,554,'Example23(b)(i) exact ratio working','Atπ/8,provedidentitygives2/sinπ/4=2√2.',[DOUBLE],'table','Example:23'),(114,554,'Example23(b)(i) forty-five solution triangle','Sides1,1,√2aidexactsinπ/4evaluation;solutionaid,notgivengeometry.',[DOUBLE],'diagram','Example:23'),(115,554,'Example23(b)(ii) integrand rewrite','Original6/(tan+cot)=3sin2θonopeninterval;endpointlimits0justifycontinuousextension.',[TRIG],'table','Example:23'),(116,554,'Example23(b)(ii) integral evaluation working','Primitive−(3/2)cos2θgives3afterseparateendpointlimits.',[TRIG,DEF],'table','Example:23'),(117,555,'Example24(a) square expansion and primitive','sin²−2sincos+cos²=1−sin2x;primitive x+cos2x/2+C.',[IDENT,SQUARE],'table','Example:24'),(118,555,'Example24(b)(i) width calculation','π/4..π/2,n2,giveshπ/8.',[b.TRAPSET],'table','Example:24'),(119,555,'Example24(b)(i) ordinate table','Source1.4142,1.0824,1areguard-digitdisplaysatπ/4,3π/8,π/2;originalvaluesretainedinternally.',[b.TRAPSET],'table','Example:24'),(120,555,'Example24(b)(i) weighted estimate','h/2timesfirst+twicemiddle+last→0.899to3dp.',[b.TRAP],'table','Example:24'),(121,555,'Example24(b)(ii) SOLUTION sketch and bias reason','Positivecscxdecreasingfromasymptote0to1atπ/2;interpolationtopsabovecurveonπ/4..π/2. ASKEDresponses,notsourcegivens.',[SKETCH,BIAS],'graph','Example:24')]
for n,page,label,note,ds,rep,parent in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readactualrequiredidentityscaffolding,common-domainlimits,exactradianbounds,andASKEDsketches. Independentlyverifybothendpointlimits,eachnumericalordinate,andchordbiassign. Solutiontriangle/graphisnotagivenasset.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample23/Try23Q1–2,Example24/Try24andactualworkedproof/integration/table/solutiontriangle/sketchpanelsenumerated. Exam-styletextbookheadingdoesnotestablishoriginalexaminationprovenance.',scope_screen='Simpleidentityfacilitatedintegrationandprescribedtrapezia;Example23endpointremovabilityexplicit. Cscasymptoteexcludedfromactualintegrationinterval. Askedsketchesandbiasscopesretained.')for page in range(554,556)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-examstyle.json',dict(scope='Complete554–555textbookexam-styleidentity/sketchresponses.',items=answers)),('census-YM-C12-examstyle.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete554–555page/item/solutionfigurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
