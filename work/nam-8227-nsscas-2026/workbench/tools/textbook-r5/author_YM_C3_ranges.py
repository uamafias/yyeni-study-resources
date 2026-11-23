"""YM112–115: graphical domain/image,restricted polynomial ranges and pointwise operations.

Fixed-source author audit; independent acceptance pending.
"""
import json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,FUNCTION,graph_part
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
DOMAIN='8227:2020:M1:T3:O02:D01';RANGE='8227:2020:M1:T3:O02:D02';MEANING='8227:2020:M1:T3:O01:D02';SQUARE='8227:2020:M1:T1:O01:D01'

def add(kind,n,page,note,parts,direct,rep='text'):
 r=prior.add(kind,n,page,note,parts,direct,rep)
 r['mapping_rationale']='Read a graph’s horizontal/vertical projection with endpoint inclusion,or derive an image from the actual expression and declared domain. An interior extremum can bound the range. Completing the square is directly linked only where the source requests that output. A solution sketch is not an assessed sketch response. Pointwise sums/products are not composition.'
 return r

def extra(p,name,expr,target):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=target;return p

def image(label,function,domain,key,kp):
 p=v(label,function,key,kp,'Independently compute the real image of the ORIGINAL expression over the stated domain. Check whether each extremum lies inside that domain and whether boundary values are attained; endpoint ordering alone is insufficient for a quadratic. The printed range is a separate comparison input.')
 p['operation']={'kind':'real-image-range','operands':[function,domain],'variable':'x'};p['given_representation']='text';p['response_format']='symbolic';return p

def graph_bounds(label,conclusion,method,kp):
 p=graph_part(label,conclusion,method,kp);p['response_format']='symbolic';return p
ps=[graph_bounds('a','D=[−4,4],R=[0,4].','The upper semicircle spans both labelled horizontal endpoints−4/4,has minimumy0at its ends,and maximumy4at the top. No open marker excludes those bounds.',112),graph_bounds('b','D=[−2,2),R=[−1,3).','Read the filled point(−2,−1)and open point(2,3); both coordinate intervals have the same included lower/excluded upper convention.',112),graph_bounds('c','D=[−2,3],R=[−4,8].','The curve starts/ends at(−2,0)/(3,0),with labelled interior extrema(−1,8)/(2,−4). The source’s final intervals are correct,but the working prose wrongly substitutes−1and2as domain endpoints.',112)]
r=add('Example',3,112,'Read domain and image from three given graphs,distinguishing horizontal endpoints from interior turning points and retaining open/closed markers.',ps,[DOMAIN,RANGE],rep='graph');r['source_label_warning']='Part(c)working prose says farthest-left−1andfarthest-right2,which are turning-point xcoordinates. Correct domain endpoints are−2and3,as its final interval already states.'
ps=[graph_bounds('a','Relation-domain=[−2,2],relation-image=[−2,2].','The full circle radius2attains all four extrema. It is NOTa function ofx,but horizontal/vertical projections of a relation remain meaningful. Do not turn this into a valid function exemplar.',598),graph_bounds('b','D=(−1,2),R=(−1,3).','The line has open endpoints(−1,3)and(2,−1). Both extrema in each projection are excluded; its negative slope reverses the endpoint correspondence.',598),graph_bounds('c','D=[−2,4],R=[−2,2].','Read filled endpoints(−2,−1)/(4,−2)and labelled top(1,2). No exact quadratic equation is supplied; the bounds follow from the drawn arc andlabels,not an invented symmetric parabola model.',598)]
ps[0]['assessed_8227_demand_ids']=[];ps[0]['teaches_8227_demand_ids']=[DOMAIN,RANGE];ps[0]['scope_facet']='Supporting relation-domain/image projection; the full circle is not a function ofx.'
r=add('Try-Now',3,113,'Read projection bounds from a full-circle relation,an open-ended line,and a labelled arc. The first is supporting relation practice,not a function example.',ps,[DOMAIN,RANGE],rep='graph');r['source_label_warning']='The answer section repeats label(b)for the final interval pair,which belongs to graph(c). The numerical intervals themselves are correct.'
p=image('a-i','x-3','Interval.open(7,oo)','Interval.open(4,oo)',113)
p2=image('a-ii','7+2*x','Interval.Lopen(-2,3)','Interval.Lopen(3,13)',113)
p3=v('b-vertex-form','3*(x+(-10)/(2*3))**2+(2-(-10)**2/(4*3))','3*(x-Rational(5,3))**2-Rational(19,3)',113,'From original coefficients3,−10,2,use a(x+b/(2a))²+c−b²/(4a). This yields3(x−5/3)²−19/3. Equivalent expanded form alone does not satisfy the explicitly requested vertex form.')
p3['canonical_response_form']='3(x−5/3)²−19/3';p3['assessed_8227_demand_ids']=[SQUARE]
extra(p3,'original-identity','expand(3*(x-Rational(5,3))**2-Rational(19,3)-(3*x**2-10*x+2))','0')
p4=image('b-range','3*x**2-10*x+2','S.Reals','Interval(-Rational(19,3),oo)',113);p4['source_dependency']={'type':'cue','from':'b-vertex-form','verbatim':'hence'}
r=add('Example',4,113,'Find two restricted linear ranges,then explicitly complete a quadratic square andhence derive its range. The source’s first working header has a sign typo.',[p,p2,p3,p4],[RANGE,SQUARE]);r['source_label_warning']='Part(a-i)stem isf=x−3andits values/range use−3correctly,but one working header saysf=x+3. Correct the header; the final rangey>4is valid.'
add('Try-Now-4',1,114,'Find ranges of two affine functions with different monotonic directions and strict/non-strict endpoint conditions.',[
 image('a','3*x-1','Interval.open(-oo,2)','Interval.open(-oo,5)',598),image('b','4-x','Interval.Ropen(-1,2)','Interval.Lopen(2,5)',598)],[RANGE])
add('Try-Now-4',2,114,'Find the unbounded image of2x−5onx≥1; the lower image endpoint is included.',[image('range','2*x-5','Interval(1,oo)','Interval(-3,oo)',599)],[RANGE])
p=v('vertex-form','2*(x+(-8)/(2*2))**2+(5-(-8)**2/(4*2))','2*(x-2)**2-3',599,'Complete the ORIGINAL quadratic2x²−8x+5with coefficient-based square completion,giving2(x−2)²−3.')
p['canonical_response_form']='2(x−2)²−3';p['assessed_8227_demand_ids']=[SQUARE]
p2=image('range','2*x**2-8*x+5','S.Reals','Interval(-3,oo)',599);p2['source_dependency']={'type':'cue','from':'vertex-form','verbatim':'hence'}
add('Try-Now-4',3,114,'Express an unrestricted quadratic in vertex form andhence state its range; these are two required outputs.',[p,p2],[SQUARE,RANGE])
add('Try-Now-4',4,114,'Find the image ofx²on the NONNEGATIVE interval[0,2],rather than assuming its whole-real-domain range.',[image('range','x**2','Interval(0,2)','Interval(0,4)',599)],[RANGE])
p=image('range','-x**2-8*x+7','Interval.Ropen(-8,2)','Interval.Lopen(-13,23)',114)
extra(p,'vertex-and-boundary-values','Tuple(-4,(-(-4)**2-8*(-4)+7),(-(-8)**2-8*(-8)+7),(-(2)**2-8*(2)+7))','Tuple(-4,23,7,-13)')
add('Example',5,114,'Find a concave quadratic’s image on a half-open domain containing its vertex; the attained maximum and excluded right-limit minimum have different inclusion flags.',[p],[RANGE])
for n,note,func,domain,key in [
 (1,'Find the image of a completed-square quadratic on a closed interval whose farther endpoint determines the maximum.','(x-2)**2','Interval(-2,10)','Interval(0,64)'),
 (2,'Find a convex quadratic image on[0,4),with an attained interior minimum and excluded supremum0.','x**2-3*x-4','Interval.Ropen(0,4)','Interval.Ropen(-Rational(25,4),0)'),
 (3,'Find a concave quadratic image on[−2,1),with an attained interior maximum and excluded lower limit−7.','-3*x**2-6*x+2','Interval.Ropen(-2,1)','Interval.Lopen(-7,5)')]:
 add('Try-Now-5',n,114,note,[image('range',func,domain,key,599)],[RANGE])
ps=[v('a-value','(2*3+1)+(3**2+3-6)','13',115,'Pointwise(f+g)(3)meansf(3)+g(3),not f(g(3))andnotfunction multiplication.'),v('b-difference','expand((2*x+1)-(x**2+x-6))','-x**2+x+7',115,'Subtract the entire gpolynomial,including both of its signed terms andconstant. This is a pointwise difference,notcomposition.'),v('c-product','expand((2*x+1)*(x**2+x-6))','2*x**3+3*x**2-11*x-6',115,'Distribute the pointwise product of the two ORIGINAL functions. It is different from f(g(x)).'),v('d-quotient-value','(2*1+1)/(1**2+1-6)','-Rational(3,4)',115,'Evaluatef(1)/g(1)=3/(−4). Denominatorg(1)isnonzero; as a function,the general quotient would exclude x2and−3.')]
for p in ps:p['response_format']='numeric'if p['subpart']in['a-value','d-quotient-value']else'symbolic';p['given_representation']='text'
r=add('Example',6,115,'Interpret andcompute four POINTWISE function operations. These do not assess the composite-function demand.',ps,[FUNCTION]);r['direct_demand_aspects']=[{'demand_id':FUNCTION,'assessed_facet':'Reading pointwise function-operation notation with numeric versus symbolic arguments; no composition or decomposition is asked.'}];r['source_interpretation']='The source separates arithmetic operations from composite functions. Preserve that distinction in demand links and later parameter families. The quotient formula requires the denominator function to be nonzero at every retained input.'
refs=[
 (17,112,'Domain/image definition and projection diagram','The prose calls outputvaluesxandrangeorcodomain; outputs areyandtheactualimage need not equal a chosen codomain. The illustrative line’s vertical axis is labelledxandhorizontalaxisy,contradicting the text/coordinates. Correct axes tohorizontalx/verticalywhile retaining the closed segment endpoints(−2,9)/(4,−3). Native markers are filled; the earlier open-marker suspicion is cleared.',[MEANING,DOMAIN,RANGE],'graph',[],None,'teaching-figure'),
 (18,112,'Example3 given graph panel','The three given graphs are an upper semicircle,a half-open line,and a curve with labelled interior extrema. Each supplies horizontal/vertical projection bounds; no exact curve equation is assumed where none is printed.',[DOMAIN,RANGE],'graph',[],'Example:3','given-figure'),
 (19,112,'Worked domain/range projection brackets','The solution overlays projection brackets on all three graphs. Part(c)finalD[−2,3]andR[−4,8]arecorrect; its prose wrongly gives−1and2as the farthest horizontal points. Turning points determine vertical extrema here,not domain endpoints.',[DOMAIN,RANGE],'graph',[],'Example:3','teaching-figure'),
 (20,113,'Try3 given graph panel','The full circle is a relation with D=R=[−2,2],not a function ofx. The open line and labelled arc are functional graphs. Open versus filled endpoints and labelled extrema determine their projection bounds.',[DOMAIN,RANGE],'graph',[],'Try-Now:3','given-figure'),
 (21,113,'Example4 linear solution sketches','The two worked sketches show an open lower endpoint forx>7and mixed endpoint inclusion for−2<x≤3. The first stem/values arex−3but a working header incorrectly printsx+3. The final ranges are correct.',[RANGE],'graph',[('Tuple(7-3,7+2*(-2),7+2*3)','Tuple(4,3,13)')],'Example:4','teaching-figure'),
 (22,113,'Completed-square quadratic and minimum sketch','The source completes3x²−10x+2to3(x−5/3)²−19/3anddraws its attainedminimum. The sketch is part of the worked solution,not an independently asked sketch response.',[SQUARE,RANGE],'graph',[('expand(3*(x-Rational(5,3))**2-Rational(19,3))','3*x**2-10*x+2')],'Example:4','teaching-figure'),
 (23,114,'Restricted concave quadratic solution diagram','The diagram labels leftpoint(−8,7),interiorvertex(−4,23)and excluded rightlimit(2,−13). Preserve the half-open domain; an excluded endpoint can bound the image without being attained.',[RANGE],'graph',[('Tuple(-(-8)**2-8*(-8)+7,-(-4)**2-8*(-4)+7,-2**2-8*2+7)','Tuple(7,23,-13)')],'Example:5','teaching-figure'),
 (24,114,'Completed-square zero-constant hint','The source note underTry5Q1identifies g=(x−2)²as a completed-square form with additiveconstant0. Its vertexx2lies inside[−2,10],so the zero minimum is attained; larger endpoint distance controls the maximum.',[RANGE],'table',[('(10-2)**2','64')],'Try-Now-5:1','teaching-figure'),
 (25,115,'Pointwise function arithmetic notation table','The table defines sum,difference,product andquotient separately from composition. A quotient must exclude zeros of its denominator function. Multiplying f(x)g(x)isnotf(g(x)); a dot/product notation must not be silently converted to composition.',[FUNCTION],'table',[('expand((2*x+1)*(x**2+x-6))','2*x**3+3*x**2-11*x-6')],None,'teaching-figure'),
 (26,115,'Numeric argument versus symbolic formula guidance','The worked explanation distinguishes operations evaluated at a number from operations yielding a formula inx. Its four outputs13,−x²+x+7,2x³+3x²−11x−6,and−3/4are independently checked. Original denominator restrictions remain part of any general quotient.',[FUNCTION],'table',[('solveset(x**2+x-6,x,domain=S.Reals)','FiniteSet(-3,2)')],'Example:6','teaching-figure')]
for n,page,label,note,teaches,rep,checks,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,checks,parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
notes={112:'Definition/projection reference,Example3(a–c),given graphs and worked projection panels are recorded. Native intro endpoints are filled. Range/codomain terminology,axis letters and part(c)working prose need explicit source corrections.',113:'EveryTry3(a–c)andExample4(a-i,a-ii,b-form,b-range)output andgiven/worked graph panel is recorded. The fullcircle is supporting relation projection,not a functional graph. The linear working-header sign typo is distinct from correct final ranges.',114:'EveryTry4Q1–4,Example5andTry5Q1–3output,restricted-quadratic diagram andprinted square-form hint is recorded. Vertex inclusion and strict/closed range endpoints are checked against actual domains.',115:'The pointwise-operation table,Example6(a–d)and its argument-type guidance are recorded. No composite-function coverage is claimed from addition,multiplication ordivision of function values.'}
pages=[]
for page in range(112,116):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'Graphical domain/image and polynomial range calculations are in scope. Explicit square completion has its own direct link; ordinary pointwise algebra is not composition. No unrelated modulus/calculus/inverse-branch rule is imposed.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C3-ranges.json',{'scope':'Every112–115 explicit response and mathematical reference.','items':answers}),('census-YM-C3-ranges.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete112–115 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
