"""YM558–560: source opening, prescribed graph pairs and continuous sign brackets."""
import hashlib,json
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,fig,figures,extra,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02'
def ev(page):
 name='YM-C13-key-653'if 653<=page<=656 else'YM-C11-key-649'if 649<=page<=652 else'YM-C12-556-source'if page in[558,559]else f'YM-C13-{560+4*((page-560)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev

def add(kind,n,page,note,parts,new_item=False):
 if new_item:
  direct=sorted({d for part in parts for d in part.get('assessed_8227_demand_ids',[])})
  comp=sorted({d for part in parts for d in part.get('component_demand_ids',[])}-set(direct))
  r=h.add(kind,n,page,note,parts,direct,comp,new_item=True)
  r['item_id']=r['item_id'].replace(':YM:C7:',':YM:C13:');new[-1]['item_id']=r['item_id']
  for part in parts:part['review_date']='2026-11-20'
 else:
  r=a.add(kind,n,page,note,parts);r['item_id']=r['item_id'].replace(':YM:C12:',':YM:C13:');corrections[-1]['item_id']=r['item_id']
 r.update(representation='text',sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='The source prescribes two graphs and asks their sketches/count,or asks a continuous sign bracket. A global root count requires the full admissible branches;one sign change alone proves existence,not uniqueness or the count. Requested root count is included in graph-response criteria when part(a)asks both;Try1Q3separatelyasks sketch then HENCEcount.',value_level_scope_decisions=[],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=[],qualifier_applicability_note='Graph/root-bracket opening;no iteration or formal convergence test is prescribed.'),precision_angle_check=dict(source='Exactgraphdefinitionsandendpointvalues;bookkeyroundssurdvaluesinTry1Q2to3sf. Noanglesinthisopening.',comparison='Compare exact signs before rounded display. Forln(x+1)keepx>−1;forevenrootskeepx≥−1. Sourcegraphiclabeldefectdoesnotchangetheexplicitstemfunctions.'))
 if new_item:new[-1].update(mapping_rationale=r['mapping_rationale'],scope_check=r['scope_check'],value_level_scope_decisions=r['value_level_scope_decisions'])
 return r

def sketch(l,functions,features,why,kp,status='sketch'):
 p=a.reasoning(l,features,why,kp,status);p.update(assessed_8227_demand_ids=[ROOTG],component_demand_ids=[],given_representation='text',response_format='sketch',original_functions=functions,credited_features=features.split(';'),criteria_basis='Author-derivedfromoriginalfunctionsandcomparedwithsourceworked/answergraph. Noofficialawardtable. Graphpair/countasaskedmustbepreserved.');return p

def bracket(l,f,lo,hi,left,right,kp,why):
 p=a.reasoning(l,'Atleastonerootbetween'+str(lo)+'and'+str(hi)+'.',why,kp,'show/prove');p.update(assessed_8227_demand_ids=[BRACKET],component_demand_ids=[],given_representation='text',response_format='proof/show-that',original_equation_zero_form=f,original_bracket=[str(lo),str(hi)],continuity_check='Originalfunctionisrealandcontinuousthroughouttheclosedbracket. Oppositeendpointsignsproveexistence;otherpartsestablishrootcount/whichroot.')
 p['source_endpoint_order']=[str(lo),str(hi)]
 if expression(str(lo))>expression(str(hi)):p['original_bracket']=[str(hi),str(lo)]
 extra(p,'original-endpoint-values',f'Tuple(({f}).subs(x,{lo}),({f}).subs(x,{hi}))',f'Tuple({left},{right})')
 extra(p,'opposite-endpoint-signs',f'sign(({f}).subs(x,{lo}))*sign(({f}).subs(x,{hi}))','-1');return p
p=sketch('a-sketch-one-root',['x**3','11-2*x'],'Sameaxes:y=x³increasingthroughorigin;y=11−2xstraightlinewithintercept11andslope−2;exactlyoneintersection,betweenx1and2.','Originaldifferencex³+2x−11hasderivative3x²+2>0andlimits±infinity,soexactlyoneglobalroot. Thisindependentauthorargumentconfirmsthegraphcount. Nativeworkedplotgeometryandtablematch11−2x,butitslinecaptionwronglyprints11−2x³. Preserveoriginalstem,correctcaption,andone-rootconclusion.',560,'key wrong');p['source_graph_defect']='Nativeplotlinecaptiony11−2x³wrong;itmustbey11−2x. Drawnstraightlineandtableareforcorrectstem.'
extra(p,'original-graph-difference','expand(x**3-(11-2*x))','x**3+2*x-11')
q=bracket('b-sign-bracket','x**3+2*x-11',1,2,'-8','1',560,'Originalcontinuouspolynomialf1−8,f2+1givesroot(1,2). Globaluniquenessfrom(a);existencefromsigns.');q['depends_on_source_parts']=['a-sketch-one-root']
add('Example',1,560,'(a)BYSKETCHINGprescribedx³and11−2xonsharedaxes,showoneglobalroot;(b)SHOWBYCALCULATIONbracket(1,2). Sourceplotlinecaptioncontainswrongpower3;actualstem/table/geometryretained.',[p,q])
f='x**3+5*x**2+2*x-4'
p=sketch('a-sketch-three-roots',['x**3+5*x**2','4-2*x'],'Sameaxes:cubicx³+5x²hasturnsx−10/3and0;straightline4−2xwithintercept4;threeintersections,onein(−5,−4),onein(−2,−1),onein(0,1).','Originaldifferencehasthreeindependentdisjointsignbrackets. Adegree3polynomialhasatmost3distinctroots,soexactly3. Curvefeaturechecksconfirmcubicturningstructureandlineincidences;nolearnercubicradicalformulaisrequired.',652)
extra(p,'three-separate-original-brackets','Tuple(sign(('+f+').subs(x,-5))*sign(('+f+').subs(x,-4)),sign(('+f+').subs(x,-2))*sign(('+f+').subs(x,-1)),sign(('+f+').subs(x,0))*sign(('+f+').subs(x,1)))','Tuple(-1,-1,-1)')
q=bracket('b-smallest-root',f,-4,-5,'4','-14',652,'Originalf(−4)=4,f(−5)=−14. Correctnumericalorderis−5<root<−4;thebookstatesendpointsinreverseorder. Part(a)identifiesitassmallest.');q['depends_on_source_parts']=['a-sketch-three-roots']
r=bracket('c-largest-root',f,0,1,'-4','4',652,'Originalf0−4,f1+4;largestrootin(0,1)asidentifiedby(a).');r['depends_on_source_parts']=['a-sketch-three-roots']
add('Try-Now-1',1,560,'(a)ASKEDshared-axessketchx³+5x²and4−2xshowingTHREEroots;(b)calculatesmallest-rootbracket−5..−4;(c)largest-rootbracket0..1. Allroot-countbrancheskept.',[p,q,r])
f='x**2-sqrt(1+x)'
p=sketch('a-sketch-two-roots',['sqrt(1+x)','x**2'],'Realrootcurve√(1+x)starts(−1,0)andpasses(0,1);parabolax²hasvertexorigin;exactlytwointersections,onein(−1,0),onein(1,2).','Originaldomainx≥−1. Squaringx²=√(1+x)givesquarticx⁴−x−1=0withnospurioussignbecausex²≥0. Quartichasexactlytworealrootsandnonebelow−1;theirbracketsandoriginaldomainconfirmthetwographintersections. Squaringusedonlyasindependentauthorcompletenesscheck.',652)
extra(p,'independent-quartic-real-root-count','Poly(x**4-x-1,x).count_roots(-oo,oo)','2')
q=bracket('b-smaller-root',f,-1,0,'1','-1',652,'Original√(1+x)isrealandcontinuousincludingendpoint−1. Values1,−1proveasmallerrootbetween−1and0.');q['depends_on_source_parts']=['a-sketch-two-roots']
r=bracket('c-larger-root',f,1,2,'1-sqrt(2)','4-sqrt(3)',652,'Originalf1=1−√2<0,f2=4−√3>0. Sourcekey−.414and2.27are3sfdisplaysoftheseexactvalues.');r['depends_on_source_parts']=['a-sketch-two-roots']
# Verify the separately printed rounded displays against the original expressions.
r['additional_operations']['key-left-3sf']={'kind':'rounded','operands':['1-sqrt(2)'],'significant_figures':3};r['additional_operation_expected']['key-left-3sf']='-Rational(207,500)'
r['additional_operations']['key-right-3sf']={'kind':'rounded','operands':['4-sqrt(3)'],'significant_figures':3};r['additional_operation_expected']['key-right-3sf']='Rational(227,100)'
add('Try-Now-1',2,560,'(a)ASKEDshared-axessketch√(1+x)andx²showingTWOroots;(b)smallerrootbracket−1..0;(c)larger1..2. Preserveeven-rootdomainandexactsignsbeforeroundedkeydisplays.',[p,q,r])
p=sketch('a-pair-sketch',['log(x+1)','3*x-5'],'Sameaxes:ln(x+1),domainx>−1,verticalasymptotex−1,throughorigin;line3x−5through(0,−5),x-intercept5/3;twointersectionsincludingoneveryclosetotherightof−1.','Theunrestrictedadmissiblegraphhasbothbranchesnearasymptoteandatlargex. Independentdifferenceg=ln(x+1)−3x+5isstrictlyconcave,withuniquemaximumat−2/3,value7−ln3>0,andlimit−infinityatbothdomainends. Thereforeexactly2roots;theleftoneisnotlosttocoarsescale.',653)
q=a.reasoning('b-root-count','Two real roots.','HENCEthetwosketchedintersectionsarepreciselyzerosoforiginalln(x+1)−3x+5. Originaldomainx>−1andbothintersectionbranchesretained;anarrowgraphviewportmustnotomittherootnearasymptote.',653,'matches');q.update(assessed_8227_demand_ids=[ROOTG],component_demand_ids=[],given_representation='text',response_format='explanation',depends_on_source_parts=['a-pair-sketch'])
add('Try-Now-1',3,560,'(a)ASKEDshared-axessketchln(x+1)and3x−5;(b)HENCEdeduceTWOroots. Keepthenear-asymptoteintersectionratherthanclaimingonefromacoarseviewport.',[p,q])
refs=[(1,559,'Graphical and sign-change root teaching figure','Genericcontinuouscrossingillustratespositive/negativefunctionvaluesandonecrossingroot. A sign change provesexistenceundercontinuity;itdoesnotcatchalltouchingevenroots.',[ROOTG,BRACKET],'graph',None),(2,560,'Example1 first source value table','Originalcubicnodes−1,0,2give−1,0,8.',[ROOTG],'table','Example:1'),(3,560,'Example1 second source value table','Correctstemline11−2xat0,1,2,3gives11,9,7,5.',[ROOTG],'table','Example:1'),(4,560,'Example1 SOLUTION pair graph with wrong line caption','Drawnstraightline/tableare11−2x,butnativecaption11−2x³wrong. Correctoriginalpairhasoneintersectionbetween1and2.',[ROOTG],'graph','Example:1'),(5,560,'Example1 sign-change working','Originalpolynomialvaluesf1−8,f2+1;continuityprovesexistence,globalmonotonicityindependentlyconfirmsuniqueness.',[BRACKET],'table','Example:1')]
for n,page,label,note,ds,rep,parent in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C13:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C13:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readprescribedgraphfunctions,realroot/logdomains,allintersectionbranchesandoriginalsignvalues. NativecheckconfirmswrongExample1caption;tableandgeometryremainconsistentwithcorrectstem. Globalcountargumentseparatefromsign-bracketexistence.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=13,page_status='prose only'if page==558 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='558title/scope/biographyhasnoassignedmathematicaltask.559introandgenericcrossingfigureteachrootlocation.560containsallExample1/Try1Q1–3andactualtables/solutionplot. AllASKEDgraphsaretext-givenprompts,notGIVENdiagrams.',scope_screen='Continuousgraph/sign-changeapproach;noformaliterationconvergencecriterion. Rootexistence,count,andselectedsmallest/largestbracketsdistinguished.')for page in range(558,561)]
def save():
 for row in answers:
  for p in row['subparts']:
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C13-opening.json',dict(scope='Complete558–560graph-pairandbracketopening.',items=answers)),('census-YM-C13-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=13,source_path=SRC,source_sha256=SHA,scope='Complete558–560page/item/sourcefigurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
