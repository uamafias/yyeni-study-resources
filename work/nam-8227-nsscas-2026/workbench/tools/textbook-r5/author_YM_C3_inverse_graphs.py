"""YM120–123: reflected graphs, natural domains and restricted quadratic inverses.

Fixed-source author audit. Sketch features are author-derived, not official awards.
"""
import json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
DOMAIN='8227:2020:M1:T3:O02:D01';RANGE='8227:2020:M1:T3:O02:D02';INVERSE='8227:2020:M1:T3:O03:D02'
SKETCH='8227:2020:M1:T3:O05:D01';INVSKETCH='8227:2020:M1:T3:O05:D02';SQUARE='8227:2020:M1:T1:O01:D01'

def extra(p,name,expr,target,kind='identity',operands=None):
 p.setdefault('additional_operations',{})[name]={'kind':kind,'operands':operands or[expr]};p.setdefault('additional_operation_expected',{})[name]=target;return p

def add(kind,n,page,note,parts,direct):
 r=prior.add(kind,n,page,note,parts,direct)
 r['mapping_rationale']='Requested domain/range, explicit inverse and actual sketch outputs are separate direct demands. Deriving an inverse inside a sketch or range solution is a component unless separately requested. Preserve the original domain, image, inverse branch and closed/open endpoints. Worked solution figures are not given assets.'
 r['precision_angle_check']={'source':'Exact expressions and labelled Cartesian sketches; no rounding or trigonometric angle units.','comparison':'Reflection in y=x is interpreted in mathematical coordinates. A visual 45-degree reflection needs equal axis scales; finite domain endpoints and branch restrictions cannot be dropped.'}
 r['component_demand_ids']=[INVERSE]if INVERSE not in direct and any(p['response_format']=='sketch'for p in parts)else[]
 return r

def sketch(label,features,kp,ops):
 p=reasoning(label,'; '.join(features),'Read the question and source/key graph independently. Derive the inverse and coordinates from the original rule, then compare labels, slopes, intercepts and reflection. These are author-derived acceptance features for this fixed textbook answer, not official criterion-level marking or a new recipe.',kp,'sketch')
 p.update(given_representation='text',response_format='sketch',credited_features=features,feature_basis='author-derived from source task; textbook graph is comparison evidence, no official award table')
 for name,expr,target in ops:extra(p,name,expr,target)
 return p

def linear_pair(kind,n,page,m,b,kp):
 p=sketch('combined-sketch',[f'Original line y={m}x+({b}) on R; inverse y=(x-({b}))/{m} on R.',f'Original intercepts (0,{b}) and (-({b})/{m},0); inverse intercepts (0,-({b})/{m}) and ({b},0).','Both labelled straight lines appear on the same axes, reflected in y=x; slopes are reciprocal. The relation is made clear by the mirror line or swapped labelled points.'],kp,[('inverse-rule',f'solve(y-({m}*x+({b})),x)[0].subs(y,x)',f'(x-({b}))/{m}'),('intercepts',f'Tuple({b},-Rational({b},{m}),-Rational({b},{m}),{b})',f'Tuple({b},-Rational({b},{m}),-Rational({b},{m}),{b})')])
 r=add(kind,n,page,f'Sketch the affine function {m}x+({b}) and its inverse on one diagram, explicitly showing their reflection relationship.',[p],[SKETCH,INVSKETCH]);r['sketch_response_required']=True
 r['value_level_scope_decisions']=[{'rule_id':'8227:QUAL08','status':'within','quoted_value':f'f(x)={m}x+({b}), x in R; nonzero slope {m}.','reason':'The original is injective on R; both reflected graphs keep their full real domains. Inverse derivation is a component of the explicitly requested sketch.'}]
 return r

linear_pair('Example',11,120,3,2,120)
linear_pair('Try-Now-11',1,121,2,3,600)
linear_pair('Try-Now-11',2,121,3,-2,600)

def interval_part(label,func,kind,domain,key,kp,method):
 p=v(label,func,key,kp,method);p['operation']={'kind':kind,'operands':[func]if kind=='real-function-domain'else[func,domain]};p.update(given_representation='text',response_format='symbolic');return p

ps=[]
for label,func,kind,dom,key,expected,method in[
 ('a-domain','(x-3)/(x+3)','real-function-domain',None,'Complement(S.Reals,FiniteSet(3))','Complement(S.Reals,FiniteSet(-3))','The ORIGINAL denominator x+3 vanishes at -3, not +3. Independent natural-domain computation checks the printed final set against the expression; the source preceding working already has the correct sign.'),
 ('a-range','(x-3)/(x+3)','real-image-range','Complement(S.Reals,FiniteSet(-3))','Complement(S.Reals,FiniteSet(1))',None,'Solve the original fractional-linear relation for its input. Output 1 would require -3=+3 and is impossible; every other real output has a unique admissible preimage.'),
 ('b-domain','sqrt(x-5)','real-function-domain',None,'Interval(5,oo)',None,'The radicand is nonnegative exactly when x>=5; zero output at the closed endpoint is allowed.'),
 ('b-range','sqrt(x-5)','real-image-range','Interval(5,oo)','S.Reals','Interval(0,oo)','The principal real square root is nonnegative. For every y>=0, original input y^2+5 is admissible and gives y. Negative y has no preimage. The source loses this restriction when it treats the inverse polynomial as unrestricted.')]:
  p=interval_part(label,func,kind,dom,key,122,method)
  if expected:p['author_expected_normalised']=expected
  ps.append(p)
r=add('Example',12,122,'Find natural domains and images of (x−3)/(x+3) and sqrt(x−5). The first final domain has a sign error; the second image incorrectly includes negative outputs.',ps,[DOMAIN,RANGE]);r['component_demand_ids']=[INVERSE]
r['source_label_warning']='Original (a) excludes -3, not the printed final +3. Original (b) has range [0,infinity), not all real values. An inverse-formula extension is not the inverse on an enlarged domain.'

ps=[]
for label,func,kind,dom,key,expected,method in[
 ('a-domain','x/(x+1)','real-function-domain',None,'Complement(S.Reals,FiniteSet(-1))',None,'Exclude the original denominator zero x=-1.'),
 ('a-range','x/(x+1)','real-image-range','Complement(S.Reals,FiniteSet(-1))','Complement(S.Reals,FiniteSet(1))',None,'Output1 is impossible; solve for a preimage of every other real output.'),
 ('b-domain','2/sqrt(x-4)','real-function-domain',None,'Interval(4,oo)','Interval.open(4,oo)','The radicand must be nonnegative AND the denominator nonzero, so x>4. The printed x>=4 incorrectly retains division by zero.'),
 ('b-range','2/sqrt(x-4)','real-image-range','Interval.open(4,oo)','Complement(S.Reals,FiniteSet(0))','Interval.open(0,oo)','The numerator and denominator are positive on the whole domain, so outputs are strictly positive. Every y>0 has original preimage 4+4/y^2. The printed y!=0 wrongly admits negative outputs.')]:
  p=interval_part(label,func,kind,dom,key,600,method)
  if expected:p['author_expected_normalised']=expected
  ps.append(p)
add('Try-Now',12,122,'Find natural domains and images of x/(x+1) and 2/sqrt(x−4), retaining both the reciprocal denominator exclusion and the positive-output restriction.',ps,[DOMAIN,RANGE])

p=v('a','2*(x+(-8)/(2*2))**2+(10-(-8)**2/(4*2))','2*(x-2)**2+2',123,'Complete the square from original coefficients 2,-8,10, giving 2(x-2)^2+2. The completed-square form, not merely an equivalent expansion, is requested.');p['canonical_response_form']='2(x−2)^2+2';p['assessed_8227_demand_ids']=[SQUARE];p['response_format']='symbolic'
p2=interval_part('b','2*x**2-8*x+10','real-image-range','Interval(0,2)','Interval(2,10)',123,'The original is decreasing on [0,2], reaching its included minimum2 at x2 and maximum10 at x0. Check both endpoints and the stationary point, not only the unrestricted quadratic range.');p2['assessed_8227_demand_ids']=[RANGE]
p3=reasoning('c','Inverse domain [2,10].','An inverse input is an original output. The actual image of the restricted original [0,2] is [2,10], including both endpoints.',123,'matches');p3.update(response_format='symbolic',given_representation='text',assessed_8227_demand_ids=[DOMAIN])
extra(p3,'original-image','', 'Interval(2,10)','real-image-range',['2*x**2-8*x+10','Interval(0,2)'])
p4=sketch('d',['Original decreasing convex quadratic segment from (0,10) through (1,4) to (2,2), domain [0,2].','Inverse decreasing reflected segment from (2,2) through (4,1) to (10,0), domain [2,10].','g(x)=x is the finite line segment from (0,0) to (10,10).','All three curves are labelled on the same axes. Finite endpoints are included; f and its inverse reflect in g=y=x and meet at (2,2).'],123,[('original-coordinates','Tuple(2*0**2-8*0+10,2*1**2-8*1+10,2*2**2-8*2+10)','Tuple(10,4,2)'),('inverse-coordinates','Tuple(2-sqrt((2-2)/2),2-sqrt((4-2)/2),2-sqrt((10-2)/2))','Tuple(2,1,0)')]);p4['assessed_8227_demand_ids']=[SKETCH,INVSKETCH]
p5=v('e','2-sqrt((x-2)/2)','2-sqrt((x-2)/2)',123,'From y=2(t-2)^2+2, solve t=2±sqrt((y-2)/2). The stated original 0<=t<=2 selects the MINUS root. Retain inverse input [2,10] and output [0,2], including endpoints.');p5.update(response_format='symbolic',assessed_8227_demand_ids=[INVERSE],inverse_domain='Interval(2,10)',inverse_image='Interval(0,2)',original_domain='Interval(0,2)')
extra(p5,'inverse-image','','Interval(0,2)','real-image-range',['2-sqrt((x-2)/2)','Interval(2,10)']);extra(p5,'forward-after-inverse','simplify(2*(2-sqrt((x-2)/2))**2-8*(2-sqrt((x-2)/2))+10-x)','0')
r=add('Example',13,123,'Complete the square for 2x²−8x+10 on [0,2], find its range and inverse domain, sketch it with the inverse and g=x on [0,10], then derive the restricted inverse.',[p,p2,p3,p4,p5],[SQUARE,RANGE,DOMAIN,SKETCH,INVSKETCH,INVERSE]);r['sketch_response_required']=True
r['value_level_scope_decisions']=[{'rule_id':'8227:QUAL08','status':'within','quoted_value':'f(x)=2x^2−8x+10, 0<=x<=2; g(x)=x, 0<=x<=10.','reason':'The original quadratic is one-to-one on [0,2]. The minus inverse branch keeps input [2,10] and image [0,2]. A general injective interval need not start at the turning point; this source interval does end there.'}]

refs=[
 (37,120,'Inverse reflection teaching graph','An injective function and its inverse have swapped graph coordinates and reflect in y=x. Equal Cartesian axis scales make the reflection visually faithful. Noninjective originals need a stated injective restriction before the inverse is a function.',[SKETCH,INVSKETCH],'graph',[],None),
 (38,120,'Example11 inverse construction table and reflected graph','For f=3x+2, inverse=(x−2)/3. Original table inputs −2,0,2 give −4,2,8; inverse inputs −4,5,8 give −2,1,2. The final two-line sketch is solution evidence, not a given diagram.',[INVERSE,SKETCH,INVSKETCH],'graph',[('Tuple(3*(-2)+2,3*0+2,3*2+2,(-4-2)/3,(5-2)/3,(8-2)/3)','Tuple(-4,2,8,-2,1,2)')],'Example:11'),
 (39,121,'Restricted root/inverse domain-image table and swapped graph labels','f=sqrt(x)+1 on [0,9] has image [1,4]; inverse=(x−1)^2 on [1,4] has image [0,9]. Tables and sets are correct. The steep parabola is the INVERSE and the shallow root is f; source graph labels are swapped.',[DOMAIN,RANGE,INVERSE],'graph',[('Tuple(sqrt(0)+1,sqrt(1)+1,sqrt(4)+1,sqrt(9)+1)','Tuple(1,2,3,4)')],None),
 (40,122,'Example12 domain-range exchange working panels','The diagram exchanging original/inverse domain and range is valid for an actual bijection onto its image. Part(a) final natural-domain sign and part(b) unrestricted inverse/image conclusions are defective, despite valid intermediate algebra.',[DOMAIN,RANGE,INVERSE],'diagram',[],'Example:12'),
 (41,123,'Example13 swapped coordinate tables and three-curve solution','Original points (0,10),(1,4),(2,2) swap to inverse points (10,0),(4,1),(2,2). The finite identity line and both restricted branches retain their endpoints and labels. The side note requiring a quadratic restriction FROM the turning point is sufficient in this example, but not necessary for every injective restriction.',[SKETCH,INVSKETCH,INVERSE],'graph',[('Tuple(2*0**2-8*0+10,2*1**2-8*1+10,2*2**2-8*2+10)','Tuple(10,4,2)')],'Example:13')]
for n,page,label,note,teaches,rep,checks,parent in refs:
 fig(n,page,label,note,teaches,rep,checks,parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
notes={120:'Inverse reflection reference and Example11 combined sketch, worked tables and solution graph are enumerated. The inverse formula is a component of the sketch task.',121:'Both Try11 sketch tasks, domain/image root-inverse table and its mislabelled graph are enumerated. The prose denominator/radical checklist is not a universal domain algorithm; logarithms and other functions need their own conditions.',122:'All four Example12 and four Try12 domain/range responses and the worked domain-exchange figure are recorded. Exact source/key errors are registered separately.',123:'All five Example13 parts, coordinate tables, three-curve graph and branch-selection note are recorded. Retain the finite original/inverse/identity domains; do not universalise the turning-point endpoint heuristic.'}
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'Natural domain/image, exact inverse and reflected graph demands are in scope. Invalid printed conclusions are defects, not new scope exclusions. Inverse branch decisions retain actual original intervals.'}for page in range(120,124)]

if __name__=='__main__':
 for name,data in [('answers-YM-C3-inverse-graphs.json',{'scope':'Every120–123 requested response, graph and printed mathematical reference.','items':answers}),('census-YM-C3-inverse-graphs.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete120–123 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
