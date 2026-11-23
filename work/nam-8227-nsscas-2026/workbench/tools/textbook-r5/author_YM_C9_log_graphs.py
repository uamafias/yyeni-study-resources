"""YM428–431: logarithm investigation, explicit viewports,inverses and reflections."""
import json
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,ev,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
GRAPH='8227:2020:M2:T2:O02:D02';EXP=g.EXP;INV='8227:2020:M1:T3:O03:D02';INVSK='8227:2020:M1:T3:O05:D02';DOMAIN='8227:2020:M1:T3:O01:D02'
def manual(label,conclusion,proof,kp,direct,fmt='explanation',page=None):
 p=reasoning(label,conclusion,proof,kp,'sketch'if fmt=='sketch'else'matches')
 p.update(assessed_8227_demand_ids=direct,response_format=fmt,given_representation='text')
 if page:p['source_page_override']=page
 return p
def log_graph(label,base,anchors,kp,page):
 f='log(x)/log('+base+')'
 p=manual(label,'Sketchy=log_('+base+')x;domainx>0,rangeR,zero(1,0),verticalasymptotex0,noy-intercept.',
 'Use the ORIGINAL positive nonunit base and exact positive anchor arguments. The sign ofln(base) determines increasing or decreasing orientation. Logarithms are defined only forx>0;the finite sourceviewport doesnotadmitx0ornegativeinputs. The internal quotient representation is a computation oracle;the source softwareentryprocedure is separately scope-labelled.',kp,[GRAPH],'sketch',page)
 p.update(original_function=f,original_domain='x>0',credited_features=['Correct increasing/decreasingorientation','Zero(1,0)','Verticalasymptotex0;no y-axisintersection','Bothpositiveandnegativeordinates;quadrantsIandIV'],criteria_basis='Derivedoriginalfeaturescomparedwithrenderedsourceplot;notanofficialawardtable.')
 extra(p,'original-positive-anchor-values','Tuple(('+f+').subs(x,Rational(1,2)),('+f+').subs(x,1),('+f+').subs(x,2))',anchors)
 return p
def add(kind,n,page,note,parts,continuation=None):
 r=g.add(kind,n,page,note,parts)
 for p in r['subparts']:
  pg=p.pop('source_page_override',page);p.update(source_pdf_page=pg,source_evidence=ev(pg))
 r.update(sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='Preserve each explicitly requested sketch,domain/range,symmetry,inverse and root-count output. Logarithm graphs retainx>0;inversegraphs swapdomain/rangeandreflectiny=x. A source softwareentrymethodoutsideLIMIT06isprocedurecontext,notanextraassesseddemand.')
 if continuation:r['continuation_pdf_pages']=continuation;corrections[-1]['continuation_pdf_pages']=continuation
 return r
p=manual('a-shared-sketch','On−2≤x≤2,ploty=(1/2)^xandliney1−xonsharedaxes. Intersections(−1,2),(0,1);linealso crossesx-axisat1.',
 'ReadtheEXPLICITsourceviewport−2≤x≤2. Exponentialendpointvalues4and1/4remainpositive;lineendpointvalues3and−1. Includeeachfunctionlabelandclosedviewportends;do notextendtheaskedsketchoutsideitsstateddomain.',639,[GRAPH],'sketch')
p.update(original_domain='−2≤x≤2forbothrequestedgraphs.',credited_features=['Sharedaxesandbothlabels','Exponentialdecreasing,positive,through(0,1)','Lineintercepts(0,1),(1,0)','Bothintersections−1,0','Explicitviewportendpoints−2,2'])
extra(p,'original-viewport-endpoints','Tuple(2**2,2**(-2),1-(-2),1-2)','Tuple(4,Rational(1,4),3,-1)')
q=manual('b-root-count','Two real solutions.',
 'ForF(x)=2^(−x)+x−1,theactualroots−1and0bothgivezero. Fsecond=(ln2)²2^(−x)>0everywhere,soFstrictlyconvexandcannot have three distinctzeros. Bothrootslieintheaskedviewport;thisindependentlyconfirms thesourcecount2.',639,[EXP,GRAPH])
q['depends_on_source_parts']=['a-shared-sketch'];extra(q,'two-original-zero-residuals','Tuple(2**1-1-1,2**0+0-1)','Tuple(0,0)');extra(q,'original-strict-convexity-sign','sign(diff(2**(-x)+x-1,x,2))','1')
add('Try-Now-26',1,428,'SketchreciprocalexponentialanddescendinglineonEXPLICIT−2..2domain,thenstatetwoequationroots. Finiteviewportandglobalroot-countargumentarekeptdistinct.',[p,q])
p=manual('a-shared-sketch','Sharedgraphsof e^xande^(−x),boththrough(0,1),positiveeverywhere;oneincreasing,theotherdecreasing,withopposite-endhorizontalasymptotey0.',
 'Substitutex−1,0,1intotheORIGINALpairandcomparetheactualsourcekeysketch. Argumentnegationswapsleftandrightbehaviour;neithercurvecrossesthex-axis.',639,[GRAPH],'sketch')
p['credited_features']=['Sharedaxesandbothlabels','Common(0,1)','Oppositeincreasing/decreasingorientation','Correctendasyptotesy0'];extra(p,'original-paired-anchors','Tuple(exp(-1),exp(0),exp(1),exp(1),exp(0),exp(-1))','Tuple(exp(-1),1,E,E,1,exp(-1))')
q=manual('b-reflection','Reflectioninthe y-axis.','Replacingxby−xmaps(x,y)to(−x,y). Theoriginalpair e^x,e^(−x)thereforehasy-axissymmetry,notx-axissymmetry.',639,[GRAPH]);q['depends_on_source_parts']=['a-shared-sketch']
add('Try-Now-26',2,428,'Sketchtheoriginalnaturalexponentialandnegative-argumentcounterpartonthesameaxes,thendescribetheir y-axisreflection.',[p,q])
ps=[log_graph('a-f-plot','2','Tuple(-1,0,1)',429,428),log_graph('b-g-plot','10','Tuple(-log(2)/log(10),0,log(2)/log(10))',429,428),log_graph('b-h-plot','Rational(6,5)','Tuple(-log(2)/log(Rational(6,5)),0,log(2)/log(Rational(6,5)))',429,428)]
ps.append(manual('b-base-comparison','ForbaseA>1,increasingAlowerstheordinatewhenx>1andraisesitwhen0<x<1;allpass(1,0).','lnx/logAhasnumeratorpositiveonx>1andnegativeon0<x<1;denominatorlogAincreaseswithA. Thebaseeffectmustthereforebesplitacrossx1.',429,[GRAPH],page=428))
ps.append(log_graph('c-natural-plot','E','Tuple(-log(2),0,log(2))',429,428))
for label,answer,proof in [('c-common-point','Allfourpass(1,0).','Everyvalidbaseraisedto0is1,so log_A1=0.'),('c-quadrants','QuadrantsIandIV,andthex-axispoint(1,0).','Domainx>0;forA>1,lnx/logAisnegativebetween0and1andpositiveabove1.'),('c-zero-to-one-behaviour','On0<x≤1,thegraphsrisefrom−∞to0.','ForA>1,logApositiveandlnx→−∞asx→0+;atx1thelogis0.'),('c-y-intercept','None;verticalasymptotex0.','TheORIGINALlogarithmisundefinedat0;approachingtheaxisdoesnotproduce anintersection.')]:ps.append(manual(label,answer,proof,429,[GRAPH],page=428))
data=[('e-r','Rational(1,2)','Tuple(1,0,-1)'),('e-t','Rational(1,10)','Tuple(log(2)/log(10),0,-log(2)/log(10))'),('e-s','Rational(5,6)','Tuple(log(2)/log(Rational(6,5)),0,-log(2)/log(Rational(6,5)))'),('e-u','exp(-1)','Tuple(log(2),0,-log(2))')]
for l,b,a in data:ps.append(log_graph(l+'-plot',b,a,429,429))
for label,answer,proof in [('e-base-comparison','ForactualbaseAin(0,1),increasingAlowerstheordinateforx>1andraisesitfor0<x<1.','Differentiatethebaseparameterconceptually:−lnx/(A(lnA)²)hasthesignoppositetolnx. ThecomparisonusesACTUALreciprocalbases,notthesourceoriginalunreciprocatedAvalues.'),('e-common-point','Allfourpass(1,0).','log_A1=0foranyvalidbase,including0<A<1.'),('e-quadrants','QuadrantsIandIV,and(1,0).','Negative logA reversesthesignrelative tolnx:positivefor0<x<1andnegativeforx>1.'),('e-zero-to-one-behaviour','On0<x≤1,thegraphsfallfrom+∞to0.','lnx→−∞butlnA<0;theirquotienttendsto+∞,thenreaches0at1.'),('e-y-intercept','None;verticalasymptotex0.','Positive-argumentdomaindoesnotincludex0forreciprocalbaseseither.')]:ps.append(manual(label,answer,proof,429,[GRAPH],page=429))
r=add('Investigation-logarithmic',1,428,'Allsourcea–emathematicaloutputsforbases2,10,1.2,eandtheirreciprocals:plots,baseeffect,commonpoint,quadrants,0<x≤1behaviourandy-axisnonintersection.',ps,[429])
r['procedural_subtasks']=[dict(source_labels=['a','b','d'],status='Sourceproprietarymenu/function-entry/newscreeninstructionsread. logx/logbaseentryexplicitlyuseschangeofbase,butissoftwareprocedurecontextoutsideLIMIT06;themathematicalgraphsarecheckedwithoutrequiringthislearnerderivation. Softwareitselfwasnotexecuted.')]
r['value_level_scope_decisions']=[dict(rule_id='8227:LIMIT06',status='outside',quoted_value='Source428saysenterlogx/log2(changeofbaselaw)todrawlog_2xinthesoftware.',parts=['softwareentryprocedure'],reason='Theextraprescribedsoftwareentrytechniqueisnotanassessed8227requirement. Retainactualgraphinterpretationseparately;donotclaimchange-of-basecoverage.')]
r['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['Softwarechange-of-baseentryinstructionoutsideLIMIT06;allunderlyinggraphdemandsretained.'])
r['notation_normalisation']={'source':'u(x)=ln_subscript(1/e)x','normalised':'u(x)=log_(1/e)x=−lnx','reason':'lnwithoutasubscriptmeansbasee;sourceintendsareciprocal-basegraph,asconfirmedbyitsplot.'}
p=v('base-a','2**(1/Rational(1,4))','16',430,'Use the ORIGINAL point(2,1/4)iny=log_ax. Theinversepowerrelationa^(1/4)=2givesapositivevalidbase16,notafourthrootof2.');p.update(assessed_8227_demand_ids=[GRAPH],component_demand_ids=[g.LOG],response_format='numeric')
add('Example',27,430,'Determinevalidlogarithmbaseafrompoint(2,1/4);a16. GivenpointisTEXTdata,notagivengraph.',[p])
ps=[]
for l,arg,ordinate,key in [('a','2','1','2'),('b','9','2','3'),('c','4','-2','Rational(1,2)'),('d','Rational(1,5)','1','Rational(1,5)')]:
 p=v(l,'('+arg+')**(1/('+ordinate+'))',key,639,'TheORIGINALpoint(X,Y)requiresa^Y=Xwitha>0,a≠1. Recovera=X^(1/Y)usingtheactualnonzeroY;negativeYpermitsavalidreciprocalbase.');p.update(assessed_8227_demand_ids=[GRAPH],component_demand_ids=[g.LOG],response_format='numeric');ps.append(p)
add('Try-Now-27',1,431,'Fourgivenpointsspecifybases2,3,1/2,1/5. Fractionalpositivebasesarevalid;negativeordinatesmustnotbeignored.',ps)
p=manual('a-shared-log-sketch','y=log_3xand−log_3xshare(1,0),domainx>0,verticalasymptotex0;oneincreasesandtheotherdecreases.',
 'Originaloutputnegationmaps(x,y)to(x,−y). Checkpairedvaluesatx1/3,1,3andcomparetheactualsourcekeysketch.',639,[GRAPH],'sketch');extra(p,'original-log-reflection-anchors','Tuple(log(Rational(1,3))/log(3),log(1)/log(3),log(3)/log(3),-log(Rational(1,3))/log(3),-log(1)/log(3),-log(3)/log(3))','Tuple(-1,0,1,1,0,-1)')
q=manual('b-domain-range','BOTHdomainsx>0;BOTHrangesR.','Theoriginalpositive-inputlogdomainisunchangedbyoutputnegation;log3xalreadytakes everyrealvalue,andnegation preservesR.',639,[DOMAIN]);q['depends_on_source_parts']=['a-shared-log-sketch']
r=manual('c-reflection','Reflectioninthe x-axis.','AnOUTSIDEminusnegatesywhilekeepingx;thisdiffersfromtheearlierargumentnegationofexponentials.',639,[GRAPH]);r['depends_on_source_parts']=['a-shared-log-sketch']
add('Try-Now-27',2,431,'Sketchbase3loganditsOUTSIDEnegativeonthesameaxes;explicitlystatebothdomains/rangesandtheirx-axisreflection.',[p,q,r])
def inverse_parts(base,kp):
 inv='log(x)'if base=='E'else'log(x)/log('+base+')'
 p=v('a-inverse','solve(('+base+')**y-x,y)[0]',inv,kp,'FromORIGINALy=base^x,swapthevariablesandusethepositive-baseinversepowerdefinition. OriginalexponentialdomainRisitsrange(0,∞);inversehasdomainx>0andrangeR. Noextrabranchrestrictionisneededforastrictlymonotoneexponential.')
 p.update(assessed_8227_demand_ids=[INV],component_demand_ids=[GRAPH],response_format='symbolic',original_domain='ExponentialR;inverse(0,∞).',assessed_facet='Findtheinverseofanalreadyone-to-onefunction;notpracticeinchoosingabranchrestriction.')
 extra(p,'inverse-positive-anchor','simplify(('+inv+').subs(x,'+base+'))','1')
 q=manual('b-shared-inverse-sketch','Sharedaxes:originalexponentialthrough(0,1),inverse'+inv+'through(1,0);horizontal/verticalasymptotey0/x0andreflectedpointpairs.',
 'ReadtheORIGINALbaseanditsactualinverse. Swapthecoordinatesofeachoriginalpoint,takingcarethatroundedsourcecoordinatesareapproximate. Exponentialandlogdomains/rangesareswapped,notcopiedunchanged.',kp,[INVSK,GRAPH],'sketch');q['depends_on_source_parts']=['a-inverse']
 r=manual('c-inverse-symmetry','Reflectioninthe liney=x.','Foraninversefunction,eachoriginalpoint(x,y)becomes(y,x),whichisreflectionin the line y=x. Thisisdistinctfromtheearlierx-axisory-axisreflections.',kp,[INVSK,GRAPH]);r['depends_on_source_parts']=['a-inverse']
 return[p,q,r]
add('Example',28,431,'Finde^x inverse,sketchbothfunctionsontheSAMEaxesanddescribey=xsymmetry. Sourceanchorvaluesareapproximate,notexacte^xvalues.',inverse_parts('E',431))
add('Try-Now-28',1,431,'Findequationofinverseof2^x,sharedoriginal/inversesketchandsymmetry. ThisQ1endsonthepage;laterTry28questionsnotclaimedread.',inverse_parts('2',639))
refs=[(57,429,'Increasing-base logarithm investigation SOLUTION plot','Fouroriginalbase>1logcurvespass(1,0),domainx>0,quadrantsI/IVandverticalasymptotex0.',GRAPH,'graph','Investigation-logarithmic:1'),(58,429,'Reciprocal-base logarithm investigation SOLUTION plot','Fouractualbasesin(0,1)givedecreasinglogs. Nonstandardln_subscript1/emeansintendedlog_(1/e)x=−lnx.',GRAPH,'graph','Investigation-logarithmic:1'),(59,430,'Increasing logarithm family summary diagram','Base>1conditioniscorrecthere;allcurvespass(1,0)andhavenoy-intercept.',GRAPH,'graph',None),(60,430,'Decreasing logarithm family summary diagram','0<base<1andpositiveargumentdomain;thepicturedoesnotadmitx0.',GRAPH,'graph',None),(61,430,'Reciprocal-log-base reflection callout','log_(1/a)x=−log_axforvalidabase,sooutputreflectionisinthe x-axis.',GRAPH,'table',None),(62,430,'Example27 inverse-power coefficient method','Substitutegivenpoint(2,1/4);a^(1/4)=2andhencea16.',GRAPH,'table','Example:27'),(63,431,'Example28 inverse variable-swap method','Swappingx,ygivesx=e^y,henceylnxwithpositivex.',INV,'table','Example:28'),(64,431,'Example28 SOLUTION inverse graph pair','Originale^xandlnxreflectiny=x;theiraxisinterceptsandasyptotesareswapped.',INVSK,'graph','Example:28'),(65,431,'Example28 approximate exponential anchor table','Atx−1,0,1,2sourcey0.4,1,2.7,7.4areapproximateplottingvalues.',GRAPH,'table','Example:28'),(66,431,'Example28 swapped approximate log anchor table','The source swapscoordinatesofitsapproximateexponentialtable. ln0.4isnotEXACTLY−1;thistableisanapproximateplottingaid.',GRAPH,'table','Example:28'),(67,431,'Exponential/logarithm inverse callout','One-to-onematchingbaseexponentialandlogarithmareinversesonR↔(0,∞).',GRAPH,'table','Example:28')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,[teaches],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readactualbases,positive-inputdomains,axisreflectionsandapproximatetableprecision. Independentlycheckoriginalpositiveanchorvaluesandcoordinate-swappinglogic;do nottreatsoftwarechange-of-baseentryasanassessedrequirement.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C9:Investigation-logarithmic:1']if page==429 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry26Q1–2,loginvestigationa–e,Example27/Try27Q1–2,Example28/Try28Q1andeleventeachingpanelsenumerated. Explicitviewportandalloriginaldomainsretained.',scope_screen='Actualgraphsareprescribed;extra softwarechange-of-baseentryisproceduralboundaryevidence. Nofigurealoneprovesreliableappruntimemarking.')for page in range(428,432)]
def save():
 for name,data in [('answers-YM-C9-log-graphs.json',dict(scope='Every428–431graph/investigation/inverseoutput.',items=answers)),('census-YM-C9-log-graphs.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete428–431page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
