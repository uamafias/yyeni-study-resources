"""YM556–557: thirty-mark revision and complete chapter summary."""
import json
import author_YM_C12_trig_powers as t
import author_YM_C12_trapezium_bias as b
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
EXP=a.EXP;DEF=a.DEF;TRIG=t.TRIG;IDENT=t.IDENT;DOUBLE=t.DOUBLE;RECIP='8227:2020:M2:T3:O01:D01';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';AREA='8227:2020:M1:T9:O04:D01'
def add(n,note,parts,tariffs,rep='text'):
 r=a.add('Revision-Exercise-12',n,556,note,parts);r.update(representation=rep,exam_style=True,exam_style_basis='PrintedRevisionExercise12withtotal30marks;notnewlyverifiedexamprovenance.',source_part_tariffs=tariffs,source_total_marks=sum(tariffs.values()),source_marks_kind='Printedtextbookparttotals,notofficialcriterionrows.',mapping_rationale='Preserveaskedlogforms,completeboundedtrigroots,exactintegralsandtextarea. Revision5GIVENgraphisnotanaskedsketch. Sourceconstantsinordinarylogprimitivearevalidonpositiveargumentbranch;fullrealprimitiveusestheabsolutevalueonseparatecomponents. Revisionmarksareparttotalsandarenotnewmarkingcriteria.',precision_angle_check=dict(source='ExactanswersapartfromRevision5explicit2dp12.25andthekey3sf1.77forRevision2(b). Trigargumentsradians.',comparison='Revision2(b)doesnotexplicitlyspecifyrounding;retainexactangleπ−atan5andcomparekey3sf1.77. Revision5stemANDdiagramnativecheckedbothx/3;noexponentdefect.'))
 if any(b.BIAS in p.get('assessed_8227_demand_ids',[])for p in parts):
  r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL11',status='within',quoted_value='Revision5originalsqrt(1+exp(x/3)),0≤x≤6.',reason='Simpleupward-bendingGIVENgraph;justifypositiveoverestimatebychordsabove. Formalcurvatureisanindependentauthorcheck.'))
  r['scope_check']['limits_considered'].append('8227:QUAL11')
 return r
p=a.primitive('a-primitive','2/(4*x-1)','log(4*x-1)/2',652);p.update(original_domain='x≠1/4,independentconstantsoneachcomponent.',printed_primitive_domain='x>1/4forprintedordinaryln;fullrealform(1/2)ln|4x−1|+C.',author_answer_form='(1/2)ln|4x−1|+Cwithindependentconstantsoneachoriginalcomponent;printedpositivebranchvalid.')
q=a.dv('b-single-log','2/(4*x-1)',1,7,'log(3)',652);q.update(depends_on_source_parts=['a-primitive'],required_method='Henceusethepreviousprimitive;giveformlnawithintegera.',author_answer_form='ln3,a3;originalintervalrightofpole1/4.')
add(1,'(a)Primitive2/(4x−1);(b)HENCEexact1..7integralinln(a)form,ln3. Printedordinarylnprimitiveisarestrictedbranch;properintervalcontainsnopole.',[p,q],{'a':2,'b':3})
p=t.proof('a-identity','cos(2*x)/(1+cos(2*x))','1-sec(x)**2/2',652,'Usecos2x=2cos²x−1anddenominator2cos²x;onoriginalcosx≠0,target1−sec²x/2.');p.update(assessed_8227_demand_ids=[DOUBLE,RECIP],original_common_domain='cosx≠0;zerosof1+cos2xexcluded.')
q=a.val('b-roots','pi-atan(5)','Rational(177,100)',652,'Onoriginal0<α<πexcludingπ/2,provedidentitygivestan²α+10tanα+25=0,soONLYtanα=−5. TangentnegativeonlyinIIwithinthisviewport;uniqueαπ−atan5≈1.76819. Key1.77is3sfalthoughstemdoesnotexplicitlyspecifyrounding.',[BND,ALL]);q.update(operation=dict(kind='rounded',operands=['pi-atan(5)'],significant_figures=3),exact_author_answer='pi-atan(5)',source_variable='alpha',normalised_variable='x',original_equation='cos(2α)/(1+cos(2α))=13+5tanα',original_domain='0<α<π,α≠π/2',source_precision_requirement='Noexplicitprecisioninstem;keydisplays1.77to3sf.',available_from_source_parts=['a-identity'])
extra(q,'original-equation-at-exact-root','simplify((cos(2*x)/(1+cos(2*x))-13-5*tan(x)).subs(x,pi-atan(5)))','0');extra(q,'complete-auxiliary-roots','solveset(x**2+10*x+25,x,domain=S.Reals)','FiniteSet(-5)')
r=a.dv('c-exact-integral','cos(x)/(1+cos(x))','-pi/2','pi/2','pi-2',652);r.update(assessed_8227_demand_ids=[TRIG,DEF],component_demand_ids=[DOUBLE],required_method='Avalidhalf-angleidentityrewritesoriginalintegrandas1−(1/2)sec²(x/2). Bothendpointsregular;nostemHENCEinstructionimposed.')
r['operation']['operands'][0]='1-1/(2*cos(x/2)**2)';r['integration_input_normalization']='Exacthalf-angleidentityonwholeoriginalinterval;originalintegrandretained,denominator≥1.';extra(r,'original-integrand-rewrite','trigsimp(expand_trig(cos(x)/(1+cos(x))-(1-1/(2*cos(x/2)**2))))','0')
add(2,'(a)SHOWcos2θ/(1+cos2θ)=1−sec²θ/2;(b)solveboundedαequation,oneangleπ−atan5,key1.77;(c)exact−π/2..π/2integralcosx/(1+cosx)=π−2.',[p,q,r],{'a':2,'b':4,'c':4})
p=t.t.ip('a-primitive','tan(x)**2+sin(2*x)','tan(x)-x-cos(2*x)/2',652,identity=True,domain='cosx≠0;separateconnectedcomponents.')
q=a.dv('b-exact-integral','3*exp(1-2*x)',0,1,'3*exp(1)/2-3/(2*exp(1))',652)
rw=add(3,'(a)Primitiveoftan²x+sin2x,chooseidentitybeforeintegrating;(b)exact0..1integral3e^(1−2x),3e/2−3/(2e).',[p,q],{'a':3,'b':4});rw['source_part_repeats']={'b':'8227:TB:YM:C12:Try-Now-2:3'}
p=a.dv('exact-area','1+exp(2*x-1)','Rational(1,2)',2,'1+exp(3)/2',652);p.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[EXP,DEF],given_representation='text',units='units^2',printed_key_units='units^2')
add(4,'TEXTgivenpositive1+e^(2x−1),x-axis,bounds1/2and2:exactarea1+e³/2. NoaskedsketchorGIVENgraph.',[p],{'area':4})
f='sqrt(1+exp(x/3))'
p=b.estimate('a-estimate',f,0,6,2,'Rational(49,4)',652,dp=2);p['printed_key_display']='12.25 units²'
q=b.bias('b-overestimate','Greaterthanexactarea:straightchordsabovethecurve.','Originalsecond=e^(x/3)(e^(x/3)+2)/(36(1+e^(x/3))^(3/2))>0on[0,6]. UseGIVENupward-bendingdiagram:straighttopsaboveoriginalcurve,sooverestimate. NativecheckconfirmsBOTHstemANDdiagramcoefficient1/3;contact-sheet1/2suspicioncleared.',652,('diff('+f+',x,2)','exp(x/3)*(exp(x/3)+2)/(36*(1+exp(x/3))**Rational(3,2))'),'0≤x≤6','concave (YM upward-bending convention)');q['depends_on_source_parts']=['a-estimate']
add(5,'GIVEN√(1+e^(x/3)),0..6:(a)REQUIREDtwo-stripestimate2dp12.25;(b)withreferencetoGIVENdiagramjustifygreaterthanexactarea. Nativeboth-exponentssame1/3;noexponentdefect.',[p,q],{'a':3,'b':1},'graph')
assert sum(r['source_total_marks']for r in answers)==30
refs=[(122,556,'Revision12Q5 GIVEN exponential-root region','Nativebothstemanddiagram√(1+e^(x/3));positiveincreasingupwardbendon[0,6],shadeundercurve. Noaskedsketch.',[b.TRAPSET,b.BIAS],'graph','Revision-Exercise-12:5',True),(123,557,'Summary exponential primitives','e^xande^(ax+b)primitivesdividebynonzeroa;ifa0theintegrandconstantintegratestox e^b.',[EXP],'table',None,False),(124,557,'Summary reciprocal x primitive','Ordinarylnxshownwithx>0;fullrealprimitive ln|x|onseparatex≠0components.',[EXP],'table',None,False),(125,557,'Summary reciprocal affine primitive','Ordinaryln(ax+b)shownpositiveargument;fullrealformln|ax+b|/aoncomponentsfora≠0. Ifa0,b≠0,primitivex/b.',[EXP],'table',None,False),(126,557,'Summary radian trig primitives','Basicandaffinecos,sin,sec²rules;nonzeroinnercoefficient,originalpolesandarbitraryconstantretained.',[TRIG],'table',None,False),(127,557,'Summary squared-trig identity choices','sin²=(1−cos2x)/2andcos²=(1+cos2x)/2facilitateintegration. Theseareteachingsupport,notextraassignedquestions.',[IDENT,t.SQUARE],'table',None,False),(128,557,'Summary trapezium formula','nstrips,h=(b−a)/n,n+1ordinates;endpointweights1andinteriorweights2. Formulaestimatessignedintegral;positiveareaonlywithappropriatesign.',[b.TRAPSET,b.TRAP],'table',None,False)]
for n,page,label,note,ds,rep,parent,given in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if given else'teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readallrevisiontasksandprintedtariffs,total30;nativecheckbothRevision5exponents. Independentlyrecomputeboundedrootcompletecase,properintegrals,trapeziumestimateandcurvebias. Summarydomainlimitsandconstantcoefficientexceptionsretained.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllRevision12Q1–5withprinted30marktotal,itsoneGIVENgraph,andallsixsummaryreferencepanelsenumerated. Summaryhasnonewaskedresponses.',scope_screen='Exactradian/log/areaanswers,boundedtanrootwithpoleexcluded,andrequirednumericalestimate/bias. Nativeexponentsagree;nofalsegraphdefectrecorded.')for page in range(556,558)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-closing.json',dict(scope='Complete556–557thirty-markrevisionandsummary.',items=answers)),('census-YM-C12-closing.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete556–557page/item/GIVENgraph/summarycensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages;30marks')
if __name__=='__main__':save()
