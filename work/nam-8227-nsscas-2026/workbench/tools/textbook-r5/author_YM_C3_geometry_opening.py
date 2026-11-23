"""YM136–138: coordinate constraints, perpendicular lines and connected distances.

Page139 is a duplicate scan of138, not a second source population.
"""
import hashlib,json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,v,reasoning,fig,figures,compute,expression,equivalent
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
LINE='8227:2020:M1:T4:O01:D01';INTERSECT='8227:2020:M1:T4:O02:D01';COORD='8227:PRIOR:NSSCO:coordinate-geometry'
def ev(page):
 if 602<=page<=605:
  p=W/'checks/r5/textbooks/YM-C3-keys-602-source.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 return prior.ev(page)
prior.common.base.ev=ev

def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p
def value(label,expr,key,kp,method,direct=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct or[],given_representation='text',response_format='symbolic');return p
def line(label,point,slope,key,kp):
 px,py=point
 return value(label,f'({slope})*(x-({px}))+({py})',key,kp,'Derive the direction from the ORIGINAL parallel/perpendicular constraint, then use the ORIGINAL given point in point-gradient form. Expand only for comparison; equivalent line equations are accepted, not only y=mx+c.',[LINE])
def intersection(label,e1,e2,key,kp):
 solve=f'solve([y-({e1}),y-({e2})],(x,y))'
 return value(label,f'Tuple({solve}[x],{solve}[y])',key,kp,'Independently solve the two derived geometric line constraints simultaneously, then check the coordinate pair in BOTH original equations. A diagram alone does not determine exact coordinates.',[INTERSECT])
def rounded(label,expr,key,kp,method,sf=3,dp=None):
 p=value(label,expr,key,kp,method)
 p['operation']={'kind':'rounded','operands':[expr],**({'decimal_places':dp}if dp is not None else{'significant_figures':sf})};p['units']=p['printed_key_units']='units';extra(p,'exact-distance',expr,str(compute({'kind':'identity','operands':[expr]})));p['response_format']='numeric';return p
def add(kind,n,page,note,parts,rep='text'):
 for p in parts:p.setdefault('given_representation',rep);p.setdefault('response_format','symbolic')
 direct=list(dict.fromkeys(q for p in parts for q in p.get('assessed_8227_demand_ids',[])))
 r=prior.add(kind,n,page,note,parts,direct,rep)
 r['component_demand_ids']=[COORD]
 r['mapping_rationale']='Direct links describe the requested translation of geometric conditions into equations or solution of intersections. Midpoint/distance arithmetic alone remains prerequisite coordinate geometry, not automatic new8227objective coverage. Reuse of an earlier part equation is a component of a later distance, with cues recorded only when printed.'
 r['precision_angle_check']={'source':'Exact coordinates/equations unless a distance is printed to3significant figures or explicitly requested otherwise. Right angles are geometric90degree constraints, not trigonometric equation mode.','comparison':'Retain exact fractions through intersections and squared distances; round only the final length. Generic gradient-product formulas apply to finite slopes; horizontal/vertical perpendicular pairs require separate equations.'}
 return r

ps=[line('a',(3,1),'-Rational(1,2)','-x/2+Rational(5,2)',136)]
p=value('b','sqrt(((3+(-21))/2-3)**2+((1+11)/2-1)**2)','13',136,'Use the actual midpoint C of A(3,1),B(−21,11), C(−9,6), then displacement C−A=(−12,5) and Pythagoras. This part does not require the perpendicular line in(a).');p['units']=p['printed_key_units']='units';p['response_format']='numeric';ps.append(p)
add('Example',16,136,'A(3,1),B(−21,11),C midpoint: find the line through A perpendicular to y=2x−7, then distance AC=13 from the actual midpoint.',ps)
ps=[line('a',(4,-2),'2','2*x-10',601)]
extra(ps[0],'original-midpoint','Tuple((14-6)/2,(-7+3)/2)','Tuple(4,-2)');extra(ps[0],'original-gradient','(3-(-7))/(-6-14)','-Rational(1,2)')
p=rounded('b','sqrt((14-0)**2+(-7-(-10))**2)','14.3',601,'Use the midpoint/perpendicular line from(a), obtain D at y-axis x0 as(0,−10), then compute distance from actual A(14,−7):sqrt205. Compare final3sf14.3, without rounding coordinates.');p['component_demand_ids']=[LINE,COORD];ps.append(p)
add('Try-Now',16,136,'A(14,−7),B(−6,3),C midpoint; line through C perpendicular to AB meets the y-axis at D. Find its equation2x−10 and distance AD=sqrt205≈14.3.',ps)
ps=[line('a-BC',(4,6),'Rational(1,2)','x/2+4',137),line('a-CD',(12,5),'-2','-2*x+29',137),intersection('b','x/2+4','-2*x+29','Tuple(10,9)',137)]
extra(ps[0],'AD-gradient','(5-0)/(12-2)','Rational(1,2)');extra(ps[1],'perpendicular-product','Rational(1,2)*(-2)','-1')
for p in ps:p['given_representation']='diagram'
r=add('Example',17,137,'Trapezium A(2,0),B(4,6),D(12,5), BC parallel AD and angleBCD90degrees: derive BC/CD equations and their intersection C(10,9).',ps,'diagram');r['source_label_warning']='Working annotation calls the point(12,5) by B, but it is D in the original and diagram. The actual CD equation uses the correct coordinates and its final result is valid.'
ps=[line('a',(-2,8),'-Rational(2,3)','-2*x/3+Rational(20,3)',601)]
extra(ps[0],'AB-gradient','(14-8)/(2-(-2))','Rational(3,2)')
p=value('b-C','Tuple(solve(-2*x/3+Rational(20,3),x)[0],0)','Tuple(10,0)',601,'C lies on the x-axis and on BC. Set y0 in the derived line; retain exact x10.',[INTERSECT]);ps.append(p)
p=value('b-D','Tuple(2+10-(-2),14+0-8)','Tuple(14,6)',601,'A,B,C,D are consecutive rectangle vertices; vector AD=BC, so D=A+C−B=(14,6). Check all adjacent side dot products and opposite directions. This vector/coordinate completion is prerequisite geometry, not another asked line equation.');extra(p,'adjacent-dot','(2-(-2))*(10-(-2))+(14-8)*(0-8)','0');ps.append(p)
for p in ps:p['given_representation']='diagram'
add('Try-Now-17',1,137,'Rectangle A(2,14),B(−2,8),C on the x-axis: find BC, then C(10,0) and D(14,6), preserving consecutive vertex order and right angles.',ps,'diagram')
ps=[line('a',(5,11),'-Rational(1,2)','-x/2+Rational(27,2)',601),intersection('b','-x/2+Rational(27,2)','3+(x-1)/3','Tuple(13,7)',601)]
extra(ps[0],'AB-gradient','(11-3)/(5-1)','2');extra(ps[1],'AX-gradient','(4-3)/(4-1)','Rational(1,3)')
for p in ps:p['given_representation']='diagram'
add('Try-Now-17',2,137,'Right triangle A(1,3),B(5,11),angleABC90degrees and X(4,4) on AC: find BC and intersect it with the line AX to obtain C(13,7).',ps,'diagram')
ps=[line('a',(7,3),'Rational(1,2)','x/2-Rational(1,2)',138)]
extra(ps[0],'midpoint','Tuple((5+9)/2,(7-1)/2)','Tuple(7,3)');extra(ps[0],'AB-gradient','(-1-7)/(9-5)','-2')
p=rounded('b','sqrt((Rational(9,5)-9)**2+(Rational(2,5)-(-1))**2)','7.33',138,'The parallel through C(1,2) has equation y=−2x+4. Intersect it with the actual perpendicular bisector y=x/2−1/2 to obtain X(9/5,2/5). Compute BX exactly as sqrt(269/5), then3sf7.33. The book’s final radical is equivalent and valid.');p['assessed_8227_demand_ids']=[INTERSECT];extra(p,'derived-intersection','Tuple(solve([y-(x/2-Rational(1,2)),y-(-2*x+4)],(x,y))[x],solve([y-(x/2-Rational(1,2)),y-(-2*x+4)],(x,y))[y])','Tuple(Rational(9,5),Rational(2,5))');ps.append(p)
add('Example',18,138,'A(5,7),B(9,−1): find the perpendicular bisector; a parallel to AB through C(1,2) meets it at X. Derive X exactly and find BX≈7.33 to3sf.',ps)

refs=[
 (63,136,'Parallel/perpendicular and bisector reminder','Parallel finite-slope lines have equal gradients; perpendicular finite nonzero slopes multiply to−1. The drawn bisector crosses AB at its midpoint at a right angle. Horizontal/vertical cases must be handled as separate line equations.',[LINE],'diagram',None,'teaching-figure'),
 (64,137,'Example17 given trapezium','A(2,0),B(4,6),D(12,5); BC parallel AD, right angle BCD. The exact C(10,9) follows from these constraints, not drawn scale. The CD working point-label slip does not change the coordinates.',[LINE,INTERSECT],'diagram','Example:17','given-figure'),
 (65,137,'Try17Q1 given rectangle','Consecutive vertices A(2,14),B(−2,8),C on the x-axis,D unknown. Right-angle and parallel-edge constraints must hold simultaneously; preserve the given coordinate labels and vertex order.',[LINE,INTERSECT],'diagram','Try-Now-17:1','given-figure'),
 (66,137,'Try17Q2 given right triangle','A(1,3),B(5,11),X(4,4) on AC, right angle at B. The diagram supplies incidence and perpendicularity, not independent measured side lengths.',[LINE,INTERSECT],'diagram','Try-Now-17:2','given-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'All Examples16–18, Try16, Try17Q1/2 and every printed reference/given diagram are recorded over136–138. Page139 repeats138 and is explicitly excluded as a duplicate scan, not another item or answer. No learner sketch is requested by these questions.','scope_screen':'Geometric line equations and intersections are in scope; midpoint and length operations remain prerequisite components unless the requested integrated work directly requires an equation/intersection. No inverse/calculus qualifier applies.'}for page in range(136,139)]

if __name__=='__main__':
 for name,data in [('answers-YM-C3-geometry-opening.json',{'scope':'Every136–138 requested output.139 duplicates138.','items':answers}),('census-YM-C3-geometry-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete136–138 page census;139 is not new content.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
