"""YM443–447: connected exam-style substitutions,30 revision marks and summary figures."""
import json
import author_YM_C9_exercise_basic as b
from author_YM_C9_log_equations import solution
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=b.ev;h.common.base.ev=ev
LIN='8227:2020:M2:T2:O04:D01';CONSTANTS='8227:2020:M2:T2:O04:D02';LAW=b.LAW;EXP=g.EXP;INEQ='8227:2020:M2:T2:O03:D02';MEQ='8227:2020:M2:T1:O01:D02';MINEQ='8227:2020:M2:T1:O01:D03';GRAPH=b.GRAPH

def val(label,expr,key,kp,direct,method,sf=None,dp=None,show=False):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,response_format='proof/show-that'if show else'numeric')
 if sf:p['operation']={'kind':'rounded','operands':[expr],'significant_figures':sf}
 if dp is not None:p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp}
 if show:p['check_mode']='show/prove'
 return p

def meq(label,left,right,key,kp):
 p=val(label,'solveset(('+left+')**2-('+right+')**2,x,domain=S.Reals)',key,kp,[MEQ],'The ORIGINAL two absolute values are nonnegative. Equality of their squares is equivalent to equality of their moduli. Solve both resulting branches and check each original expression;do not apply sign assumptions to the bare affine forms.')
 p.update(response_format='symbolic',original_equation='|'+left+'|=|'+right+'|');return p

def add(kind,n,page,note,parts,tariffs=None,rep='text'):
 r=g.add(kind,n,page,note,parts);r.update(exam_style=True,exam_style_basis='The source explicitly places this item under9.8 Exam-Style Questions or Revision Exercise9. This is textbook classification,not primary examination provenance.',representation=rep,sketch_response_required=False,component_demand_ids=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(r['assessed_8227_demand_ids'])),mapping_rationale='Retain the original connected hence links,positive exponential/nonnegative modulus substitution domains and distinct proof/coefficient/solution outputs. The highest-degree auxiliary root set is not the final answer until original-variable admissibility/recovery is complete.',scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT06','8227:QUAL01']),value_level_scope_decisions=[dict(rule_id='8227:LIMIT06',status='within',quoted_value=note,reason='Apply original common-base logs or exponential substitution. The actual textbook linear forms are obtained by the power law,not a mandatory memorised change-of-base formula.'),dict(rule_id='8227:QUAL01',status='not applicable',quoted_value=note,reason='Any modulus here is an equation/inequality,not a modulus graph requiring integer coefficients.')],precision_angle_check=dict(source='Individual3sf/2dp/2sf requests retained. Revision2strictcutoffisroundedonlyforcomparingkeydisplay,notforanexactsolutionset.',comparison='No angles. Keep exact intermediate roots/logarithms and original domains. Textbook tariffs are totals,not official criterion schedules;no method awards invented.'))
 if tariffs:r.update(source_part_tariffs=tariffs,source_total_marks=sum(tariffs.values()),source_marks_kind='Textbook printed tariffs;not official criterion rows.')
 for p in parts:p['given_representation']=rep
 return r
p=meq('a-x','3*x+4','3*x-11','FiniteSet(Rational(7,6))',443)
q=val('b-y','log(Rational(7,6))/log(2)','Rational(222,1000)',443,[EXP],'Use ORIGINAL hence substitutionu=2^y>0. Establishedu7/6ispositive,so uniqueylog_2(7/6). Round once to3sf.',sf=3);q['depends_on_source_parts']=['a-x']
add('Example',34,443,'Firstsolve|3x+4|=|3x−11|,then HENCE recover the positive exponential substitute2^yandfinaly.222to3sf.',[p,q])
p=meq('a-x','x+2','x-13','FiniteSet(Rational(11,2))',641)
q=val('b-y','log(Rational(11,2))/log(3)','Rational(155,100)',641,[EXP],'Original hence substitutionu=3^y>0;the modulus answer11/2is admissible. Recoverlog_3(11/2)and round3sf.',sf=3);q['depends_on_source_parts']=['a-x']
add('Try-Now-34',1,443,'Modulus equation establishesx11/2,then HENCE a base3exponential substitution givesy1.55to3sf.',[p,q])
p=val('a-interval','solve_univariate_inequality((2*x-5)**2<(x+3)**2,x,relational=False)','Interval.open(Rational(2,3),8)',641,[MINEQ],'Square the ORIGINAL two nonnegative absolute values. The quadratic difference factors(3x−2)(x−8)<0,so retain strict interval2/3<x<8.');p['response_format']='symbolic'
q=val('b-largest-integer-y','ceiling(exp(8))-1','2980',641,[INEQ],'Original hence substitutionu=lny requiresy>0. Established2/3<u<8gives e^(2/3)<y<e^8. The upper endpoint is STRICT;largest integerisceil(e^8)−1=2980,not rounded e^8.');q.update(depends_on_source_parts=['a-interval'],original_domain='y>0;the requested finaly is an integer.');extra(q,'last-integer-boundary-check','And(log(2980)<8,log(2981)>8,log(2980)>Rational(2,3))','True')
add('Try-Now-34',2,443,'Solve a strict modulus inequality and HENCE the largest INTEGER yafterlnysubstitution. Preservebothlogdomainandstrictupperendpoint;answer2980.',[p,q])
p=val('a-positive-power','Intersection(solveset(x**2-5*x-14,x,domain=S.Reals),Interval.open(0,oo))','FiniteSet(7)',641,[EXP],'ORIGINAL3^(2x)=5·3^x+14becomesu²−5u−14=0withu=3^x>0. Rejectu−2,retainu7.');p['response_format']='symbolic'
q=val('a-x','log(7)/log(3)','Rational(177,100)',641,[EXP],'Recover originalxfrom positive3^x7andround3sf.',sf=3);q['depends_on_source_parts']=['a-positive-power']
r=val('b-absolute-x','FiniteSet(-log(7)/log(3),log(7)/log(3))','FiniteSet(-log(7)/log(3),log(7)/log(3))',641,[MEQ,EXP],'ORIGINAL3^(2|x|)=5·3^|x|+14givespositiveintermediate3^|x|7and|x|log_3(7)>0. Recover BOTH signsx±log_3(7),notonlythepositiveroot. The source displays±1.77.');r.update(response_format='symbolic',depends_on_source_parts=['a-positive-power','a-x'],printed_key_display='x=1.77or−1.77;roundeddisplayforcompleteexactset.')
positive='Intersection(solveset(x**2-5*x-14,x,domain=S.Reals),Interval(1,oo))'
r['operation']={'kind':'identity','operands':['Union(imageset(Lambda(y,log(y)/log(3)),'+positive+'),imageset(Lambda(y,-log(y)/log(3)),'+positive+'))']}
extra(r,'original-absolute-exponential-residual','3**(2*Abs(log(7)/log(3)))-5*3**Abs(log(7)/log(3))-14','0')
add('Try-Now-34',3,443,'Quadraticin3^xaskspositiveintermediateandx3sf;HENCE compositionwith|x|requiresbothoriginalsigns. Do notretainanegativepowerorloseanegativex.',[p,q,r])
line='solve(y*log(3)-(x+2)*log(4),y)[0]'
p=val('a-linear-form',line,'x*log(4)/log(3)+2*log(4)/log(3)',444,[LIN],'Take logs of ORIGINAL3^y=4^(x+2),bring downbothoriginalexponentsandsolvefory. Itsaffineformdemonstratesthestraightline.',show=True)
q=val('a-exact-gradient','diff('+line+',x)','log(4)/log(3)',444,[CONSTANTS],'Differentiatetheindependentlyrearrangedlinearformorreaditscoefficientofx;theexactgradientisln4/ln3,notitsroundedvalue.');q['response_format']='symbolic'
r=val('b-intersection-x','solve(2*x-('+line+'),x)[0]','Rational(342,100)',444,[EXP],'Intersect the ORIGINAL derived linewithy2x. Solve(2ln3−ln4)x=2ln4;denominatorln(9/4)nonzero. Round finalx2dp.',dp=2);r['depends_on_source_parts']=['a-linear-form']
add('Example',35,444,'For3^y=4^(x+2),prove yversusxislinear,findexactgradient,andintersectwithy2xto2dp. The originalexponentshift2contributestheintercept.',[p,q,r])
line='solve((y+1)*log(5)-3*x*log(2),y)[0]'
p=val('a-linear-form',line,'3*x*log(2)/log(5)-1',641,[LIN],'Take logs of ORIGINAL5^(y+1)=2^(3x),retain the+1beforedividing,andshowy=(3ln2/ln5)x−1.',show=True)
q=val('b-gradient','diff('+line+',x)','log(8)/log(5)',642,[CONSTANTS],'Originalxcoefficient3ln2/ln5equalsln8/ln5;sourcekeybeginsnextanswerpage642.');q['response_format']='symbolic'
r=val('b-y-axis-point','Tuple(0,('+line+').subs(x,0))','Tuple(0,-1)',642,[CONSTANTS],'Set ORIGINALx0in theindependentlyderivedline;givethecoordinatePAIR(0,−1),notjustitsordinate.');r['response_format']='symbolic'
add('Try-Now-35',1,444,'Prove original5^(y+1)=2^(3x)givesa straightline,thenstateexactgradientandy-axispoint. Answer(a)on641and(b)on642keptseparate.',[p,q,r])
p=val('x-y-pair','FiniteSet(*solve([x+2*y-7,4*x-y-10],(x,y),set=True)[1])','FiniteSet(Tuple(3,2))',642,[LAW,g.LOG],'From ORIGINAL2^x4^y128getx+2y7. Fromln(4x−y)=ln2+ln5get4x−y10>0. Solveoriginalsystemandcheckarguments,preservingcorrelatedpair.');p.update(response_format='symbolic',component_demand_ids=['8227:PRIOR:NSSCO:simultaneous-equations']);extra(p,'original-power-and-log-argument','Tuple(2**3*4**2,4*3-2)','Tuple(128,10)')
add('Try-Now-35',2,444,'Simultaneousoriginalpowerandnaturallogrelationsgivex3,y2withpositivelogargument10. Negativeindividualvariableswouldnotbeexcludedunlessanactualargumentrequiresit.',[p])
p=val('x','log(2)/(log(5)-2*log(2))','Rational(311,100)',642,[EXP],'Take logarithms of ORIGINAL5^x=2^(2x+1);thecoefficientisln5−2ln2=ln(5/4)>0. Recoverandround3sf.',sf=3)
add('Revision-Exercise-9',1,445,'Use logarithms on5^x=2^(2x+1);keep the+1constantwhencollectingexponents. Finalx3.11to3sf.',[p],{'whole':3})
p=val('cutoff-display','log(Rational(1,2))/log(Rational(4,5))','Rational(311,100)',642,[INEQ],'ORIGINAL(0.8)^x<0.5:divide byNEGATIVEln(0.8),reversingtothe strictsolutionx>ln(.5)/ln(.8). The key3.11is onlyaroundedboundarydisplay;the exactcutoffremains3.1062837… internally.',sf=3);p.update(response_format='symbolic',exact_solution_set='Interval.open(log(Rational(1,2))/log(Rational(4,5)),oo)',printed_key_display='x>3.11',boundary_precision_note='The rounded key cutoff is not an exactly equal half-line. Preserve the exact boundary and mark any display approximation explicitly.')
add('Revision-Exercise-9',2,445,'Solve original(0.8)^x<.5with reversedcomparison. Store exacthalf-line separatelyfromthekeyroundedcutoff3.11;do not alterboundarycases.',[p],{'whole':3})
p=val('y-equals-mx','solve(x*log(5)-4*y*log(3),y)[0]','x*log(5)/(4*log(3))',642,[LIN],'Take logs of ORIGINAL5^x=3^(4y)and solve fory. The linepasses throughorigin;thequestionasksproofandcoefficient.',show=True)
q=val('m','log(5)/(4*log(3))','Rational(366,1000)',642,[CONSTANTS],'Recovercoefficientfromtheoriginaltwo-baseequationandround3sf,notfromaroundedslope.',sf=3)
add('Revision-Exercise-9',3,445,'Use logarithms to showy=mxfor5^x=3^(4y),thenfindm.366to3sf.',[p,q],{'whole':3})
p=val('a-two-power-y','Intersection(solveset((1+x**2)-5*(3+x),x,domain=S.Reals),Interval.open(0,oo))','FiniteSet(7)',642,[EXP],'Set ORIGINALu=2^y>0;4^y=u². Multiplicationisvalidbecause3+u>0. Solveu²−5u−14=0,rejectu−2,retainu7.');p['response_format']='symbolic'
q=val('b-y','log(7)/log(2)','Rational(281,100)',642,[EXP],'Recover ORIGINALylog_2(7)frompart(a)andround3sf.',sf=3);q['depends_on_source_parts']=['a-two-power-y']
add('Revision-Exercise-9',4,445,'For(1+4^y)/(3+2^y)=5,find2^yfirst,thenuseln/logtofindy3sf. Positivesubstitutionpreventsaspuriousnegativepoweranswer.',[p,q],{'a':3,'b':2})
p=meq('a-x','2*x+3','x+8','FiniteSet(5,-Rational(11,3))',642)
q=val('b-y','log(5)/log(2)','Rational(232,100)',642,[EXP],'ORIGINALhenceequation|2^(y+1)+3|=|2^y+8|correspondstox=2^y>0in(a). Rejectnegative−11/3;retain5androundlog_2(5)to3sf.',sf=3);q['depends_on_source_parts']=['a-x']
add('Revision-Exercise-9',5,445,'Modulusequationgives5and−11/3;HENCEexponentialsubstitutionallowspositive5only,followedbyy2.32to3sf.',[p,q],{'a':3,'b':2})
p=solution('x','4*x**2-(x+3)*(3*x+5)','Interval.open(0,oo)','FiniteSet(15)',642,'2ln(2x)−ln(x+3)=ln(3x+5)');p['source_key_locator_note']='The key labels this6(a);the source hasunsplitQuestion6. The numerical15iscorrect.'
add('Revision-Exercise-9',6,445,'Originalnaturallogargumentsrequirex>0. Quadraticcandidates−1,15leaveonly15. KeyrenumberssourceQ6as6(a);retaincorrectsourceidentity.',[p],{'whole':5})
m='((Rational(139,100)-Rational(181,100))/(Rational(14,10)-Rational(6,10)))';c='(Rational(181,100)-'+m+'*Rational(6,10))'
p=val('K','exp('+c+')','Rational(84,10)',642,[CONSTANTS],'ORIGINAL y=K/a^(2x)giveslny=lnK−2x lna. Givenaxeslnyagainstxandsuppliedpointsgivem−.525,c2.125,soKe^2.125→8.4to2sf.',sf=2)
q=val('a','exp(-('+m+')/2)','Rational(13,10)',642,[CONSTANTS],'Recovera=e^(−m/2)fromORIGINALdenominatorexponent2x,notmerelye^(−m). Final1.3to2sf.',sf=2)
row=add('Revision-Exercise-9',7,445,'GIVENlny-versus-xpoints(.6,1.81),(1.4,1.39),originaly=K/a^(2x):findK8.4,a1.3to2sf. KeymislabelsQ7as6(b);valuescorrespondtoQ7.',[p,q],{'whole':6},'graph');row['source_key_locator_note']='Answer642under6(b)belongs to sourceQ7;no separateQ7heading.'
assert sum(r.get('source_total_marks',0)for r in answers)==30
refs=[(109,443,'Example34 two-modulus branch working','Both absolute values nonnegative;oppositesignbranch givesx7/6,equalsignbranch impossible.',MEQ,'table','Example:34'),(110,443,'Example34 ORIGINAL equation check','Atx7/6bothmoduliare15/2;checkbeforeexponentialrecovery.',MEQ,'table','Example:34'),(111,443,'Example34 hence-substitution working','2^y=7/6>0,thenlogarithmsyieldy.222to3sf.',EXP,'table','Example:34'),(112,444,'Example35 logarithmic linear form','Powerlawonbothoriginalexponentsgives y=(ln4/ln3)x+2ln4/ln3.',LIN,'table','Example:35'),(113,444,'Example35 intersection working','Substitutey2xandcollectnonzerocoefficientln(9/4);x3.42to2dp.',EXP,'table','Example:35'),(114,445,'Revision9Q7 GIVEN transformed graph','Horizontalx,verticallny;points(.6,1.81),(1.4,1.39);negativegradient−.525.',CONSTANTS,'graph','Revision-Exercise-9:7'),(115,446,'Summary product log law','Validbasepositiveandnot1;positivearguments. log_a(xy)=log_ax+log_ay.',LAW,'table',None),(116,446,'Summary quotient log law','Positivearguments/nonzerodenominator;log_a(x/y)=log_ax−log_ay.',LAW,'table',None),(117,446,'Summary power log law','Forpositivex,log_a(x^n)=nlog_ax;do notextendseparatelogstonegativefactors.',LAW,'table',None),(118,446,'Summary inverse power-log identities','loga(a)=1,loga1=0,loga(a^x)=x,a^(loga x)=xunderappropriatepositiveargument/baseconditions.',g.LOG,'table',None),(119,446,'Summary natural-log definition','Naturallogisbasee; e≈2.718281828. The displayed inversion e^x=y iff x=lnyrequiresy>0.', '8227:2020:M2:T2:O02:D01','table',None),(120,446,'Summary increasing logarithm family','Allshownbases1.2,2,e,10exceed1,so curvesincreaseandcross(1,0). Headera>0isincomplete;mustbea>1forincreasinglogarithm.',GRAPH,'graph',None),(121,446,'Summary decreasing logarithm family','Reciprocalpositivebasesbelow1give decreasingcurvesonx>0. Nonstandardlnsubscript1/emeansintendedlog_(1/e)x=−lnx,notordinarylnx.',GRAPH,'graph',None),(122,447,'Summary increasing exponential family','Allshownbases10,e,2,1.2exceed1,givingcurvesthrough(0,1). Increasingheadera>0wrong;requirea>1.',GRAPH,'graph',None),(123,447,'Summary decreasing exponential family','Originalnegativeexponentsforbasesgreaterthan1areequivalenttoreciprocalbasesbetween0and1. Allcurvespositiveandthrough(0,1).',GRAPH,'graph',None),(124,447,'Summary raw exponential model','y=k a^xhasxinindex;positivevariables/parametersadmitsemi-logline.',LIN,'graph',None),(125,447,'Summary raw power model','y=k x^nhasxasbase;positiveoriginalinput/outputadmitlog-logline.',LIN,'graph',None),(126,447,'Summary semi-log linearisation','Horizontalx,verticallogy;slope loga,interceptlogk. Fixedlogbaseconsistent.',LIN,'table',None),(127,447,'Summary log-log linearisation','Horizontal logx,vertical logy;slope n,interceptlogk. This is not thesemi-logparameterinterpretation.',LIN,'table',None)]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if n==114 else'teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readactualquestion/solution/summaryrole,allaxesandlabels. Recomputeparentoriginalquantities,andtestmonotonicityfrombaseconditions. Repeatedbadincreasingheadersarelinkedtosourceregister,notcountedasnewrecipebreadth.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample34–35,Try34Q1–3/Try35Q1–2,Revision9Q1–7and19teaching/given/summarypanelsenumerated. Textbookrevisiontotal30reconciled. Answerkey6(a)/6(b)renumberingdoesnotchangetheactualsourcequestionIDs.',scope_screen='Actualpositivepowers,nonnegativeabsolutes,logdomains,andstrictinequalityboundariesretained;summaryheaderscorrectedasinternalsourcecautions.')for page in range(443,448)]
def save():
 for name,data in [('answers-YM-C9-closing.json',dict(scope='Complete443–447examstyle/revision/summarypopulation;30textbookmarksreconciled.',items=answers)),('census-YM-C9-closing.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete443–447page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
