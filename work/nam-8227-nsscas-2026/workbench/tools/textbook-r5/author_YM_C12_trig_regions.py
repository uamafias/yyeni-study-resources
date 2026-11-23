"""YM544–545: the indicated first region, a maximum-bounded region and a product curve."""
import json
import author_YM_C12_trig_powers as t
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
AREA='8227:2020:M1:T9:O04:D01';BND='8227:2020:M1:T6:O06:D01';STAT='8227:2020:M1:T8:O04:D01';DOUBLE=t.DOUBLE;COMPOUND=t.COMPOUND;TRIG=t.TRIG;DEF=a.DEF;IDENT=t.IDENT

def val(l,e,k,kp,ds,method,comp=None,show=False):
 p=a.val(l,e,k,kp,method,ds);p.update(component_demand_ids=comp or[],given_representation='graph',source_angle_unit='radians')
 if show:p.update(check_mode='show/prove',response_format='proof/show-that')
 return p

def area(l,f,lo,hi,k,kp,components=None):
 p=a.dv(l,f,lo,hi,k,kp);p.update(assessed_8227_demand_ids=[AREA],component_demand_ids=components or[TRIG,DEF],given_representation='graph',units='units^2',printed_key_units='units^2',shaded_interval=[str(lo),str(hi)],source_angle_unit='radians');return p

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(representation='graph',mapping_rationale='GIVENgraphshadingselectsthefirstpositiveboundedregionorregionendingattheindicatedmaximum. Requestedrootandstationaryabscissasaredirectonlywhereseparatelyasked;anunaskedarea-boundrootisacomponent. Aseparateshowntrigidentityisassessedinitsownpart;thelaterareausesitsgivenscaffold. NoALL-solutionscoverageisclaimedfromselectingoneindicatedroot.',precision_angle_check=dict(source='Exactradianbounds,areaexpressionsandcoefficients;noapproximationrequested.',comparison='Graphselectstheactualfirstlobe;donotsumunshadedlaterlobes. Preserveinnerargumentshiftsandpositivearea;solutionsketches/trianglesarenotGIVENassets.'))
 return r
f='4*sin(x)**2+8*sin(x)+3'
p=val('a-P-x','Min(*solveset('+f+',x,domain=Interval.open(0,2*pi)))','7*pi/6',544,[BND],'Original4sin²x+8sinx+3=(2sinx+1)(2sinx+3). Rejectsinx−3/2;sinx−1/2firstoccursat7π/6afterpositivefirstlobe. TheGIVENPistheFIRSTpositivex-axisintersection,notlater11π/6. Internal0..2πsearchisacompletenesscheck,notanaddedsourceviewport.')
extra(p,'original-admissible-first-cycle-roots','solveset('+f+',x,domain=Interval.open(0,2*pi))','FiniteSet(7*pi/6,11*pi/6)')
q=val('b-shown-identity','trigsimp(('+f+')-(5+8*sin(x)-2*cos(2*x)))','0',544,[DOUBLE],'Useactualsin²x=(1−cos2x)/2toobtaingivenform5+8sinx−2cos2x;retain8sinx.',show=True)
r=area('b-exact-area',f,0,'7*pi/6','35*pi/6+7*sqrt(3)/2+8',544);r.update(depends_on_source_parts=['a-P-x','b-shown-identity'],required_method='USEshownformandtheindicatedfirstrootfrom(a);alloriginalcurvevaluesnonnegativeontheboundedlobe.')
add('Example',18,544,'GIVEN4sin²x+8sinx+3andfirstintersectionP:(a)exactPabscissa7π/6;(b)SHOWreducedformandUSEittocalculateFIRSTenclosedarea35π/6+7√3/2+8.',[p,q,r])
p=area('exact-area','sin(x)**2',0,'pi','pi/2',651,[t.SQUARE,TRIG,DEF]);p['required_method']='Byexpressingsin²xintermsofcos2x;theidentitydirectionisprescribed. GIVENregioniswholepositivehump0..π.'
add('Try-Now-18',1,545,'GIVENsin²xgraph0≤x≤π,findareaofwholehumpBYEXPRESSINGsin²intermsofcos2x. Correctπ/2;identitymethodprescribed,notanindependentchoice.',[p])
f='2*cos(x)-cos(2*x)'
p=val('a-M-x','Min(*solveset(diff('+f+',x),x,domain=Interval.open(0,pi/2)))','pi/3',651,[STAT],'IndependentlydifferentiateORIGINAL2cosx−cos2x:2sinx(2cosx−1). GIVENMistheinteriorfirstmaximum,soselectπ/3,notstationaryboundary0. Secondderivativeatπ/3is−3<0.',[t.DOUBLE]);extra(p,'original-local-maximum-second','diff('+f+',x,2).subs(x,pi/3)','-3')
q=area('b-exact-area',f,0,'pi/3','3*sqrt(3)/4',651);q['depends_on_source_parts']=['a-M-x']
add('Try-Now-18',2,545,'GIVEN2cosx−cos2xwithmaximumM,shadeendsatverticalthroughM:(a)findMabscissaπ/3;(b)areaONLY0..π/3,3√3/4. Do notextendtothecurvefirstroot.',[p,q])
f='2*cos(2*x)*cos(2*x+pi/6)';target='sqrt(3)*(1+cos(4*x))/2-sin(4*x)/2'
p=val('a-shown-form','trigsimp(expand_trig(('+f+')-('+target+')))','0',545,[COMPOUND,DOUBLE],'ExpandORIGINALcos(2x+π/6)bycompoundformula,thenusedouble-angleonsquared/productterms. Resultk1(1+cos4x)+k2sin4xwithk1√3/2,k2−1/2. Keepnegativecross-term.',show=True)
q=val('a-k1-k2','Tuple(sqrt(3)/2,-Rational(1,2))','Tuple(sqrt(3)/2,-Rational(1,2))',651,[COMPOUND,DOUBLE],'Theindependentlyprovedexpandedformhascoefficients√3/2and−1/2. Checksourceproductidentityseparatelybeforeidentifyingcoefficients.');q['depends_on_source_parts']=['a-shown-form'];extra(q,'original-coefficient-identity','trigsimp(expand_trig(('+f+')-('+target+')))','0')
r=area('b-exact-area',f,0,'pi/6','sqrt(3)*pi/12',651,[TRIG,DEF,BND]);r.update(depends_on_source_parts=['a-shown-form'],required_method='ReadGIVENfirstpositiveboundedregion. Firstzerois2x+π/6=π/2→π/6;cos2xzeroπ/4islaterandwouldincludeunshadednegativearea. Integrateoriginalproductortheprovedform.');extra(r,'actual-first-bound','('+f+').subs(x,pi/6)','0');extra(r,'interior-positive-value','('+f+').subs(x,pi/12)','sqrt(3)/2')
add('Try-Now-18',3,545,'GIVEN2cos2xcos(2x+π/6),shadefirstlobe:(a)SHOWk1(1+cos4x)+k2sin4xANDidentifycoefficients;(b)exactarea0..π/6is√3π/12.',[p,q,r])
refs=[(60,544,'Example18 GIVEN first-lobe graph','Curve4sin²x+8sinx+3,initialordinate3,firstmaximum15,andfirstpositiverootP7π/6;shadingexcludeslaterlobes.',[AREA,BND],'graph','Example:18',True),(61,544,'Example18(a) sine quadratic working','Factors2sinx+3and2sinx+1;impossible−3/2rejected.',[BND],'table','Example:18',False),(62,544,'Example18(a) quadrant-selection reference','Negativehalf-sinefirstpositiveangleinIIIis7π/6;sourcequadrantdiagramselectsthefirstroot.',[BND],'diagram','Example:18',False),(63,544,'Example18(a) special-angle reference triangle','Sides1,√3,2andreferenceangleπ/6aidexactrootselection;thisisasolutionfigure,notgivengeometry.',[BND],'diagram','Example:18',False),(64,544,'Example18(b) identity and area working','Reduce4sin²toconstant/cos2x,andusetheactual0..7π/6bounds.',[DOUBLE,AREA],'table','Example:18',False),(65,544,'Example18(b) cosine endpoint quadrant reference','cos7π/6=−√3/2isnegative;retainthesignin−8cosx.',[TRIG],'diagram','Example:18',False),(66,544,'Example18(b) doubled endpoint quadrant reference','2(7π/6)=7π/3,sine√3/2;donotcopythesignofsin7π/6.',[TRIG],'diagram','Example:18',False),(67,545,'Try18Q1 GIVEN sine-square hump','Wholepositivehump0..π,zerosbothends,maximum1atπ/2.',[AREA],'graph','Try-Now-18:1',True),(68,545,'Try18Q2 GIVEN maximum-bounded shade','Original2cosx−cos2x,firstmaximumMπ/3;shadestopsatMvertical,notthecurveintercept.',[STAT,AREA],'graph','Try-Now-18:2',True),(69,545,'Try18Q3 GIVEN first product-curve lobe','Original2cos2xcos(2x+π/6),positivefirstlobefrom0toπ/6;unshadednegativepartfollowsbeforeπ/4.',[AREA],'graph','Try-Now-18:3',True)]
for n,page,label,note,ds,rep,parent,given in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if given else'teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='ReadGIVENshadesandlabelsseparatelyfromsolutionquadrant/triangleaids. Independentlyderiveoriginalroots,maximumbound,shiftedproductfirstzeroandareas. Preservefirst-lobeselectionratherthanallfutureperiods.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample18/Try18Q1–3andactualGIVENregions/solutionquadrant/triangle/workingpanelsenumerated. Differentshadedboundariesandexplicitidentitymethodsretained.',scope_screen='Exactradianrootsandareasofspecifiedlobes;noall-periodsolveorunrequestedsketchimplied. Maximumabscissadirectonlywhenasked.')for page in range(544,546)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-trig-regions.json',dict(scope='Complete544–545given-regionresponses.',items=answers)),('census-YM-C12-trig-regions.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete544–545page/item/visualcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
