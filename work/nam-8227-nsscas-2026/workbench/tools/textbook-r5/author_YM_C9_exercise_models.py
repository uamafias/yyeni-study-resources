"""YM442: undefined transformed axes, original logdomains and reflected-versus-inverse graph."""
import json
import author_YM_C9_exercise_basic as b
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=b.ev;h.common.base.ev=ev
LIN='8227:2020:M2:T2:O04:D01';CONSTANTS='8227:2020:M2:T2:O04:D02';LAW=b.LAW;GRAPH=b.GRAPH;INV=b.INV;INVSK='8227:2020:M1:T3:O05:D02'
def scalar(label,expr,key,direct,method,dp=None,sf=None):
 p=v(label,expr,key,641,method);p.update(assessed_8227_demand_ids=direct,response_format='numeric')
 if dp is not None:p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp}
 if sf:p['operation']={'kind':'rounded','operands':[expr],'significant_figures':sf}
 return p
def manual(label,result,proof,direct,status='matches',response='symbolic'):
 p=reasoning(label,result,proof,641,status);p.update(assessed_8227_demand_ids=direct,response_format=response);return p
def add(n,note,parts,rep='text'):
 r=g.add('Exercise-9',n,442,note,parts);r.update(representation=rep,sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),component_demand_ids=[],mapping_rationale='Classify original parameter recovery,logdomain filtering,actual reflection sketch and inverse separately. Missing axes are a source defect,not permission to infer unlabelled givens silently. Reflection inx-axis is outputnegation;reflection iny=x is inverse.',scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT06']),value_level_scope_decisions=[dict(rule_id='8227:LIMIT06',status='within',quoted_value=note,reason='Use the original stated logarithmic transformation,or an explicitly labelled conditional interpretation where missing;no mandatory change-of-base formula.')],precision_angle_check=dict(source='Q13explicitly2sf;Q11keydisplaysp2.82andx.452withoutanexplicitquestionprecision. Others exact.',comparison='Retain exact intermediate gradient/intercept/logdomain conditions. A generic base10log and a naturallog are not interchangeable axes. No angles.'))
 for p in parts:p['given_representation']=rep
 return r
method='The ORIGINAL y=p x^q is nonlinear in rawx,y. Its text says points on "the straight line" without specifying axes. CONDITIONAL on intended log10y versuslog10x,the gradientis(3.45−.45)/(1−0)=3andintercept.45=log10p. Under another logbase orrawaxis interpretation the parameterpchanges;the key does not repair the missing given.'
p=scalar('a-p','10**Rational(45,100)','Rational(282,100)',[CONSTANTS],method,dp=2);p.update(conditional_assumption='Unstated intended axeslog10y versuslog10x.',requested_precision='Noexplicitquestionprecision;2dphereonlycomparesthekeydisplay2.82.')
q=scalar('a-q','(Rational(345,100)-Rational(45,100))/(1-0)','3',[CONSTANTS],method);q['conditional_assumption']=p['conditional_assumption']
r=scalar('b-x','(Rational(26,100)/10**Rational(45,100))**Rational(1,3)','Rational(452,1000)',[CONSTANTS],method+' Use unroundedpthenpositiverealrootx=(.26/p)^(1/3);theintendedmodelhaspositiveinputs.',sf=3);r.update(conditional_assumption=p['conditional_assumption'],requested_precision='Noexplicitprecision;3sfcomparesthekeydisplay.452.')
row=add(11,'Modely=p x^qandpoints(0,.45),(1,3.45)said to lie on an unspecified straight line. Keyassumesbase10log-logaxes:p≈2.82,q3,thenx≈.452fory.26. All numericalanswersareCONDITIONALonmissingaxes.',[p,q,r]);row['source_question_defect']='Transformation/axis labels and logbase are absent. Retain conditional solution;do not treatp2.82as uniquely entailed by literal givens.'
p=v('x-over-k','Intersection(solveset(2*x**2+x-6,x,domain=S.Reals),Interval.open(0,2))','FiniteSet(Rational(3,2),-2)',641,'ORIGINAL k>0and2lnx=ln(3k+x)+ln(2k−x)requires0<x<2k. Setcheckerx=originalx/k,thedimensionlessratio:2t²+t−6=0gives3/2or−2,buttheoriginaldomainratio0<t<2retains3/2only. The printed−2khasnegativeoriginalxandinvalidlnx.')
p.update(author_expected_normalised='FiniteSet(Rational(3,2))',assessed_8227_demand_ids=[LAW],response_format='symbolic',source_variable_basis='Checkerxistheoriginalratiox/k,k>0.',original_equation='2lnx=ln(3k+x)+ln(2k−x)',original_domain='k>0and0<x<2k.',correct_answer='x=3k/2only.',printed_key_display='x=3k/2orx=−2k');extra(p,'actual-factorisation','expand((2*x-3)*(x+2))','2*x**2+x-6')
add(12,'Solve the original natural-log equation withk>0. Fullargumentfiltereliminatesprintedextraneous−2k;onlyx3k/2remains.',[p])
m='((Rational(292,100)-Rational(160,100))/(5-2))';logA='(Rational(160,100)-'+m+'*(2-1))'
ps=[scalar('A','exp('+logA+')','Rational(32,10)',[CONSTANTS],'Originalmodely=A e^(p(x−1))giveslny=p x+(lnA−p). Fromsuppliedlny-axispointsderivep.44,thenlnA=1.60−.44(2−1)=1.16. Do NOT mistake the y-intercept.72forlnA.',sf=2),scalar('p',m,'Rational(44,100)',[CONSTANTS],'The ORIGINAL given axesarelnyversusx;gradient(2.92−1.60)/3=.44directlygivesp.',sf=2)]
add(13,'Givenlny-versus-xgraphpoints(2,1.60),(5,2.92),modely=A e^(p(x−1)):p.44,A3.2to2sf. The translatedexponentchangesinterceptinterpretation.',ps,'graph')
p=manual('a-g-sketch','g=−log_2x;domainx>0;decreasing;zero(1,0);verticalasymptotex0;noy-intercept','Originalgoutputnegationoflog_2xkeepspositivexdomain. The keygcurveand(1,0)arecorrect.',[GRAPH],status='sketch',response='sketch');p['credited_features']=p['author_conclusion'].split(';')
q=manual('b-i-f-sketch','f=log_2x;domainx>0;increasing;zero(1,0);verticalasymptotex0;reflectionofginthe x-axis','The ORIGINAL instruction saysfisthex-axisreflectionofg. Thus every(x,y)becomes(x,−y);thecorrectsketchisincreasinglog_2x. The native key instead draws/labellsg^−1=2^(−x),whichreflectsginy=xandhasdifferentdomain/intercept/asymptote. The key(b)(ii)formulaiscorrectbutdoesnotmakeits(b)(i)diagramcorrect.',[GRAPH],status='key wrong',response='sketch');q.update(credited_features=q['author_conclusion'].split(';'),printed_key_diagram='g^−1(x)=2^(−x),through(0,1),decreasingexponential.',criteria_basis='Author-derived reflection features;printed wrong sketch separately recorded.')
r=scalar('b-ii-f','-(-log(x)/log(2))','log(x)/log(2)',[GRAPH],'Apply ORIGINAL outputnegationf=−g,notinput-outputswap. Formula f=log_2xhasx>0.');r['response_format']='symbolic'
s=scalar('c-inverse','solve(-log(y)/log(2)-x,y)[0]','2**(-x)',[INV],'Swapand solve ORIGINAL g:its inverseis2^(−x),allrealinput,positiveimage. This belongs to(c),not the reflectionsketch(b)(i).');s['response_format']='symbolic'
add(14,'Connected g=−log_2xsketch,x-axisreflectionfsketch/formula,andinverseg^−1. Nativekey(b)(i)drawstheinverseinsteadoftherequestedreflection;itsformula(b)(ii)and(c)inversearecorrect.',[p,q,r,s])
p=manual('a-line','log10y=x+1.','The ORIGINAL graphhascoordinates(−1,0),(0,1),whereverticalaxislog10y. Independentslope1andintercept1giveY=X+1. Exponentiatebase10onlyafteridentifyingtheseaxes.',[LIN])
q=scalar('a-y-of-x','10**(((1-0)/(0-(-1)))*x+1)','10*10**x',[CONSTANTS],'Recover ORIGINAL ybyexponentiatinglog10y=x+1,so y10^(x+1). The suppliedpoint(−1,0)isnotrawy0.');q['response_format']='symbolic'
r=scalar('b-y-at-2','(10**(x+1)).subs(x,2)','1000',[CONSTANTS],'Substituteoriginalx2intothe derived ORIGINAL ymodel,notintothetransformedaxisordinatealone.')
add(15,'Advanced suppliedlog10y-versus-xline through(−1,0),(0,1):stateitsline,deriveoriginalymodel,andfindy1000atx2.',[p,q,r])
fig(108,442,'Exercise9Q13 GIVEN translated-exponent semi-log graph','Horizontalx,verticallny;points(2,1.60),(5,2.92). Gradientp.44,interceptlnA−p.72;do not assignA=e^.72.',[CONSTANTS],'graph',[],'Exercise-9:13');figures[-1].update(item_id='8227:TB:YM:C9:Teaching-figure:108',printed_page=pp(442),source_evidence=ev(442),value_level_scope_decisions=[],item_kind='given-figure',parent_item_id='8227:TB:YM:C9:Exercise-9:13');figures[-1]['mathematical_feature_review']['method']='Read actual axes and translated original exponent;derive both point residuals and recovered constants independently.'
pages=[dict(pdf_page=442,printed_page=pp(442),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers]+[r['item_id']for r in figures],continuation_item_ids=[],source_evidence=ev(442),reader='Codex author',date='2026-11-20',non_item_content='AllExercise9Q11–15andthegivenQ13semi-loggraphenumerated. MissingQ11axes,extraneousQ12root,andQ14wrongreflectiondiagramexplicit.',scope_screen='Originaldomainandtransformed-axismeaningpreserved;ambiguitynotresolvedbymatchingthekey.')]
def save():
 for name,data in [('answers-YM-C9-exercise-models.json',dict(scope='Complete442Exercise9Q11–15withactualgraphanddomaincorrections.',items=answers)),('census-YM-C9-exercise-models.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete442page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
