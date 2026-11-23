"""YM107–111: functions across graphs,tables,ordered pairs and mapping arrows.

Fixed-source author audit; independent acceptance pending.
The existing source-audit record format is retained; no runtime recipes.
"""
import hashlib,json
import author_YM_C1_opening as common
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent
FUNCTION='8227:2020:M1:T3:O01:D01';NOTATION='8227:2020:M1:T3:O01:D03';ONEONE='8227:2020:M1:T3:O03:D01'

def pp(page):return page-11 if page<=138 else page-12

def ev(page):
 name='YM-C2-keys-598-source'if 598<=page<=601 else'YM-C2-104-source'if page==107 else f'YM-C3-{108+4*((page-108)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
common.base.ev=ev;common.base.answers.clear();common.base.new.clear();figures.clear()
answers=common.base.answers;new=common.base.new;corrections=[]

def add(kind,n,page,note,parts,direct,rep='text',continuation=None):
 r=common.add(kind,n,page,note,parts,direct)
 r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C3:');meta=new.pop();meta['item_id']=r['item_id']
 corrections.append({'item_id':r['item_id'],'pdf_page':page,'printed_page':pp(page),'continuation_pdf_pages':continuation or[]})
 r['continuation_pdf_pages']=continuation or[];r['representation']=rep
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],
 'qualifier_applicability_note':'These tasks interpret function/injectivity conditions. No modulus coefficient,restricted inverse branch orcalculus qualifier applies merely because another chapter uses it.'}
 r['value_level_scope_decisions']=[]
 if ONEONE in direct:
  actual_values='Reciprocal-shaped graph;3→6,4→7,5→8;−2/2→64and1/−1→1.'if kind=='Example'else'Cubic-like graph;11→1,13→4and6,15→8;sideways curve.'
  r['value_level_scope_decisions']=[{'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':actual_values,'reason':'The inverse-branch restriction is not applicable to a classification-only task. Actual function/injectivity statuses are independently read from the original graph or finite data; no inverse branch is claimed.'}]
 r['mapping_rationale']='Function validity means exactly one output for each declared domain input. One-to-one status additionally requires distinct inputs to have distinct outputs. These are distinct asked outcomes; repeated outputs alone do not invalidate a function,and repeated identical pairs do not create conflicting outputs.'
 r['precision_angle_check']={'source':'Exact finite values and qualitative graph/arrow classifications; no angle units or rounding.','comparison':'Read every labelled input/output and preserve declared domains. A vertical/horizontal line outside the relevant domain/image can have zero intersections; the applicable graph test is at most one.'}
 return r

def finite_part(label,pairs,printed,kind='function',domain=None,kp=109):
 declared=set(domain if domain is not None else[x for x,y in pairs]);by={x:set()for x in declared}
 for x,y in pairs:
  assert x in by;by[x].add(y)
 valid=all(len(ys)==1 for ys in by.values())
 injective=valid and len({next(iter(ys))for ys in by.values()})==len(declared)
 actual=('one-to-one'if injective else'many-to-one')if kind=='injectivity'and valid else'function'if valid else'not a function'
 assert actual==printed,(label,pairs,actual,printed)
 p=reasoning(label,printed,'Read the ORIGINAL finite pairs/arrows independently. Group outputs by each declared input; each group must contain exactly one distinct output. Only after that check can distinct-output counts establish injectivity. A repeated identical pair leaves its output set unchanged. The source key/classification is transcribed separately.',kp,'matches')
 p['independent_finite_relation_check']={'input_pairs':pairs,'declared_domain':sorted(declared),'output_sets_by_input':[[x,sorted(by[x])]for x in sorted(declared)],'is_function':valid,'is_injective':injective if valid else None,'derived_classification':actual,'method':'Standalone source builder recomputes finite relation grouping from original data; no printed classification is a computation input.'}
 p['given_representation']='table'if label.startswith('b-')else'text'
 return p

def graph_part(label,printed,method,kp,rep='graph'):
 p=reasoning(label,printed,method+' This is a visually checked logical interpretation of the original render,not an invented exact graph equation or an automated pixel proof. Independent review remains pending.',kp,'matches');p['given_representation']=rep;return p
ps=[graph_part('a-i','function','The given horizontal segment assigns one yto eachx in its horizontal extent. Vertical lines outside that domain meet no point; within it they meet one.',109),graph_part('a-ii','not a function','The given vertical column contains several points at the samex with differentyvalues. One such column is a counterexample to unique output.',109),graph_part('a-iii','not a function','The two right-facing diagonal rays share positivexvalues with two differentyvalues. The common vertex alone does not repair the conflicting columns.',109),
 finite_part('b-i',[(2,-3),(4,6),(3,-1),(6,6),(2,3)],'not a function'),finite_part('b-ii',[(-3,5),(-2,5),(-1,5),(0,5),(1,5)],'function'),finite_part('c-i',[(-2,10),(0,-8),(2,-6),(4,-4),(6,-2)],'function'),finite_part('c-ii',[(1,2),(2,4),(1,6),(3,8)],'not a function')]
add('Example',1,109,'Classify three graphs,two tables and two coordinate lists as functions or nonfunctions. Conflicting outputs,not merely repeated printed xentries,are decisive.',ps,[FUNCTION],rep='graph')
ps=[graph_part('a-i','function','The cubic-like curve shown has one yperx despite turning points. Horizontal repetition affects injectivity,not the vertical-line function test.',598),graph_part('a-ii','function','The finite horizontal row has distinctxpositions and one commonyvalue. Repeated outputs are permitted in a many-to-one function.',598),graph_part('a-iii','not a function','The sideways curve has an upper andlower point at the same positivex; it fails the vertical-line test.',598),
 finite_part('b-i',[(-10,-6),(-8,-8),(-6,-10),(-4,-6)],'function',kp=598),finite_part('b-ii',[(3,4),(1,3),(3,6),(4,7)],'not a function',kp=598),finite_part('c-i',[(-2,-2),(-1,0),(0,2),(1,4),(2,6)],'function',kp=598),finite_part('c-ii',[(4,3),(5,3),(6,3),(7,3)],'function',kp=598)]
r=add('Try-Now',1,109,'Classify three graph relations,then two tables and two coordinate lists on the next page; repeated outputs in the last relation are allowed.',ps,[FUNCTION],rep='graph',continuation=[110])
for p in r['subparts'][3:]:p.update(source_pdf_page=110,source_evidence=ev(110))
p=graph_part('a','one-to-one','The two reciprocal-shaped branches occupy opposite y-signs; each horizontal line meets at most one shown point. A line aty0 meets none. The graph is not assigned an unprinted exact equation.',111)
p2=finite_part('b',[(3,6),(4,7),(5,8)],'one-to-one','injectivity',kp=111);p2['given_representation']='diagram'
p3=finite_part('c',[(-2,64),(2,64),(1,1),(-1,1)],'many-to-one','injectivity',kp=111);p3['given_representation']='diagram'
add('Example',2,111,'Decide one-to-one versus many-to-one for a reciprocal-shaped graph and two finite arrow mappings. The finite outputs,not only one-output-per-input,justify the injectivity labels.',[p,p2,p3],[ONEONE],rep='diagram')
p=graph_part('a','function; many-to-one','The cubic-like graph has one yperx,but horizontal lines between its two turning heights meet more than one point. It is a function and is not injective.',598)
p2=finite_part('b',[(11,1),(13,4),(13,6),(15,8)],'not a function',kp=598);p2['given_representation']='diagram'
p3=graph_part('c','not a function','The sideways graph has two yvalues for the same x. One-to-one/many-to-one function classification is therefore not applicable to it.',598)
add('Try-Now',2,111,'First decide function validity,then classify injectivity where applicable; do not label a nonfunction many-to-one merely because arrows or repeated values appear.',[p,p2,p3],[FUNCTION,ONEONE],rep='diagram')
refs=[
 (1,108,'Input/output function machine','The machine maps inputx tooutput2x+1 and distinguishes the rule from its output value. Variable letters in f(x),h(a),A(t)are inputs,not multiplication by a function name.',[FUNCTION],'diagram',[('2*3+1','7')],None,'teaching-figure'),
 (2,108,'Function inside relation inclusion diagram','The printed inclusion box places(2,8),(3,12),(1,4)inside a function,and other ordered pairs in an outer relation. Treat those as sets of pairs: repeated identical pairs do not create a conflict. Parent relation/function set domains must be explicit before claiming a total function.',[FUNCTION],'diagram',[],None,'teaching-figure'),
 (3,108,'Vertical-test relation/function panel','The composite panel contrasts a discrete horizontal function,a vertical-parabola function,a circle and a conflicting-column scatter relation. It contains coordinate/sign and overgeneralised duplicate-value notes requiring explicit correction. The circle’s lower point cannot have positivey5; the scatter note must preserve its−3output.',[FUNCTION],'graph',[],None,'teaching-figure'),
 (4,109,'Example1 given graph panel','Three given graphs are a horizontal segment,a vertical point column and two right-facing rays. Preserve whether any vertical column has two distinct points; arbitrary numeric labels are not needed for that classification.',[FUNCTION],'graph',[],'Example:1','given-figure'),
 (5,109,'Example1 given tables','The two tables have a conflicting repeatedinput2withoutputs−3/3,versusdistinctinputsallmappingto5. Repeat output6in the first table is incidental; the x2conflict is decisive.',[FUNCTION],'table',[],'Example:1','given-figure'),
 (6,109,'Worked vertical-line overlays','The solution draws vertical test lines through all three graphs. Its one-intersection wording needs the domain qualifier: at most one for arbitrary vertical lines,exactly one for inputs in the declared domain.',[FUNCTION],'graph',[],'Example:1','teaching-figure'),
 (7,109,'Worked table conflict annotations','The solution repeats both original tables and calls duplicatexvalues nonfunctional. Actual conflicting outputs justify its first classification,but identical repeated pairs would not. Repeated outputs alone do not establish that an arbitrary relation is a function.',[FUNCTION],'table',[],'Example:1','teaching-figure'),
 (8,109,'Try1 given graph panel','A cubic-like graph,a finite horizontal point row and a sideways curve must retain their distinct vertical-intersection properties. Handwritten marks are not publisher answer evidence.',[FUNCTION],'graph',[],'Try-Now:1','given-figure'),
 (9,110,'Try1 given table continuation','The first table repeatsoutput−6withdistinctinputs. The second repeatsinput3withtwooutputs4and6. Preserve those roles; duplicate-y and conflicting-x conditions are different.',[FUNCTION],'table',[],'Try-Now:1','given-figure'),
 (10,110,'One-to-one finite mapping diagram','Inputs−2,0,2,4mapto−3,1,5,9by2x+1. Every output is distinct. The accompanying prose gives only the ordinary unique-output condition; injectivity also needs distinct inputs to have distinct outputs.',[FUNCTION,ONEONE],'diagram',[('Tuple(2*(-2)+1,2*0+1,2*2+1,2*4+1)','Tuple(-3,1,5,9)')],None,'teaching-figure'),
 (11,110,'Many-to-one square mapping diagram','Inputs are−4,−2,2,3,NOT0. They mapto16,4,4,9byx². Every input has exactly one arrow,and±2shareoutput4. Native inspection cleared the false missing-zero-arrow lead.',[FUNCTION,ONEONE],'diagram',[('Tuple((-4)**2,(-2)**2,2**2,3**2)','Tuple(16,4,4,9)')],None,'teaching-figure'),
 (12,110,'Two nonfunction arrow diagrams','The left mapping’s declaredinputdhasnooutput. The right mapping’sinputfhasoutputsbandc. A missing declared-domain image and conflicting images are distinct reasons for failing total function validity.',[FUNCTION],'diagram',[],None,'teaching-figure'),
 (13,111,'One-to-one mapping/graph comparison','The first summary panel repeats the finite2x+1map and an increasing line with a horizontal test overlay. Read arrow uniqueness ANDdistinct outputs. Horizontal lines outside the image may meet zero points.',[ONEONE],'diagram',[('Tuple(2*(-2)+1,2*0+1,2*2+1,2*4+1)','Tuple(-3,1,5,9)')],None,'teaching-figure'),
 (14,111,'Many-to-one mapping/graph comparison','The second summary panel repeats the square map on−4,−2,2,3and pairs it with a parabola. The finite map has no0input; the drawn parabola represents a broader illustrative graph,not only those four points. Both show noninjectivity.',[ONEONE],'diagram',[('(-2)**2-2**2','0')],None,'teaching-figure'),
 (15,111,'Example2 given graph/arrow panel','The reciprocal-shaped graph is injective; the3→6,4→7,5→8map is injective; the±2→64and±1→1map is many-to-one. Each relation is already a function. Preserve distinct-output counts rather than the inadequate each-input-one-output argument alone.',[ONEONE],'diagram',[],'Example:2','given-figure'),
 (16,111,'Try2 given graph/arrow panel','The cubic is a many-to-one function,the middle map sends13to4and6and is not a function,and the sideways curve is not a function. Injectivity labels apply only after function validity.',[FUNCTION,ONEONE],'diagram',[],'Try-Now:2','given-figure')]
for n,page,label,note,teaches,rep,checks,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,checks,parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
notes={107:'Chapter3 title,topic list and biographical portrait only. The portrait is not a quantitative teaching diagram and no learner task starts here.',108:'Function machine,relation/function inclusion diagram and four-graph vertical-test panel are enumerated. Definitional qualifications and graph-coordinate source defects remain explicit; no new learner task begins here.',109:'EveryExample1(a-i..iii,b-i..ii,c-i..ii),its original graph/table panels and worked overlays is enumerated. Try1(a-i..iii)starts here; its table/point parts continue110.',110:'AllTry1(b/c)continuation responses and tables are recorded. The one-to-one,many-to-one and two nonfunction arrow panels are enumerated. Native maps contain no0input in the square example; false missing-arrow lead is cleared.',111:'Both summary mapping/graph panels,Example2(a–c)andTry2(a–c),and their given panels are enumerated. Function validity and injectivity are separate decisions; inappropriate labels on nonfunctions are not accepted.'}
pages=[]
for page in range(107,112):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated'if ids else'prose only','item_ids':ids,'continuation_item_ids':['8227:TB:YM:C3:Try-Now:1']if page==110 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'Function interpretation and one-to-one decisions are within scope. No inverse branch,calculus or modulus qualifier is manufactured. Original finite domains and actual given representations are retained.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C3-opening.json',{'scope':'Every107–111 requested response; graphical reasoning remains manual and independent acceptance pending.','items':answers}),('census-YM-C3-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete107–111 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   for label,op in p.get('additional_operations',{}).items():
    if label in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][label])),(row['item_id'],p['subpart'],label)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
