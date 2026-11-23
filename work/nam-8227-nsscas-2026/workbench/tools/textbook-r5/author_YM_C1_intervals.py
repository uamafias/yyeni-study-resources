"""Fixed YM36–39 source checks: reconstruction, interval endpoints and coordinate pairs."""
import hashlib,json
import author_YM_C1_opening as opening
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
RECON='8227:2020:M1:T1:O05:D01';CRIT='8227:2020:M1:T1:O06:D01';INTERVAL='8227:2020:M1:T1:O06:D02'
PAIR='8227:2020:M1:T4:O02:D01'

def ev(page):
 name='YM-C1-end-keys-590-source'if 590<=page<=593 else'YM-C1-keys-586-source'if 586<=page<=589 else f'YM-C1-{12+4*((page-12)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
opening.base.ev=ev

def add(kind,n,page,note,parts,direct,rep='text',sketch=False):
 r=opening.add(kind,n,page,note,parts,direct)
 prior=new.pop();corrections.append({k:prior[k]for k in ['item_id','pdf_page','printed_page','continuation_pdf_pages']})
 r.update(representation=rep,sketch_response_required=sketch,
  mapping_rationale='Reconstruction, critical values, selected sign intervals and requested number-line responses are distinct assessed outputs. Solving a linear/nonlinear pair is linked only where the learner is asked to find intersections or coordinate pairs; graph teaching does not automatically assess a sketch.',
  precision_angle_check={'source':'Exact graph/interval data, except Try29Q4 explicitly requires two decimal places. No angle units.','comparison':'Preserve closed/open endpoints and exact internal critical values. Rounded displayed endpoints are approximations to exact boundaries, not a changed exact solution set.'})
 return r

def interval(label,original,key,kp,method):
 return v(label,'solve_univariate_inequality('+original+',x,relational=False)',key,kp,method+' Solve the original inequality after collecting all terms; use a sign interval or graph argument and preserve equality endpoints.')

def numberline(label,original,key,kp,features):
 p=reasoning(label,features,'Independently derive the exact interval set from the original inequality, then compare the rendered key’s endpoint labels, open/filled dots, connected intervals and outward rays. This is a number-line response, not an unrequested function sketch.',kp,'sketch')
 p['additional_operations']={'exact_interval':{'kind':'identity','operands':['solve_univariate_inequality('+original+',x,relational=False)']}}
 p['additional_operation_expected']={'exact_interval':key}
 return p

ps=[v('a','expand(((-0+8)/(0-2)**2)*(x-2)**2-8)','2*x**2-8*x',589,
 'Vertex(2,−8) gives A(x−2)²−8. Through the origin gives4A−8=0, so A2.'),
 v('b','expand(((2+2)/(0-1)**2)*(x-1)**2-2)','4*x**2-8*x+2',589,
 'Vertex(1,−2) gives A(x−1)²−2; intercept2 gives A4. Verify vertex and intercept with this same polynomial.')]
add('Try-Now',26,36,'Reconstruct two parabolas from their turning point and an origin/y-intercept constraint. Both extra points lie away from the vertex abscissa.',ps,[RECON])
ps=[v('X','expand(((10+6)/(0+2)**2)*(x+2)**2-6)','4*x**2+16*x+10',36,
 'Read X’s vertex(−2,−6) and point(0,10) from the grid. Vertex form gives A4. Do not read the top viewport limit12 as the y-intercept.'),
 v('Y','expand((6/((0+2)*(0-6)))*(x+2)*(x-6))','-x**2/2+2*x+6',36,
 'Read roots−2,6 and y-intercept6. Scale A−1/2. Independently use the vertex(2,8) and intercept6 to obtain the same A.'),
 v('Z','expand(((6-2)/(2-4)**2)*(x-4)**2+2)','x**2-8*x+18',36,
 'Read Z’s vertex(4,2) and point(2,6), giving A1 in A(x−4)²+2. Keep the three curve identities distinct on shared axes.')]
add('Example',27,36,'Reconstruct three labelled parabolas X,Y,Z on one grid. For Y the source demonstrates root-factor and vertex-form alternatives for the same curve.',ps,[RECON],rep='graph')
ps=[v('X','expand(((0-4)/(-1+3)**2)*(x+3)**2+4)','-x**2-6*x-5',589,
 'Read X’s maximum(−3,4) and root−1 (also−5). A(−1+3)²+4=0 gives A−1. Check intercept−5 and both roots.'),
 v('Y','expand(((13-4)/(0-3)**2)*(x-3)**2+4)','x**2-6*x+13',589,
 'Read Y’s minimum(3,4) and intercept13, giving A1. It has no real roots and must remain above the axis.')]
add('Try-Now',27,37,'Read the two shared-axis parabolas and reconstruct each from its vertex and an additional graph constraint. Do not confuse the two vertical scales or curve labels.',ps,[RECON],rep='graph')
add('Example',28,37,'Solve2x²−3x≥2. Standardise, find both critical values and choose the two exterior closed rays.',[
 interval('solution','2*x**2-3*x>=2','Union(Interval(-oo,-Rational(1,2)),Interval(2,oo))',37,
 'The standard polynomial is(2x+1)(x−2). It opens upward and is nonnegative outside its roots−1/2,2, including both roots.')],[CRIT,INTERVAL])
rows=[('a','x**2-5*x>=-6','Union(Interval(-oo,2),Interval(3,oo))',589,'Roots2,3; fill both endpoints and draw rays left of2 and right of3.'),
 ('b','-5*x**2+13*x+6>0','Interval.open(-Rational(2,5),3)',589,'Roots−2/5,3; use open dots and connect only the interval between them.'),
 ('c','(x+1)*(x-2)>=4','Union(Interval(-oo,-2),Interval(3,oo))',590,'Standard roots−2,3; fill endpoints and draw exterior rays.'),
 ('d','(4*x+7)*(x-8)>x-8','Union(Interval.open(-oo,-Rational(3,2)),Interval.open(8,oo))',590,'Collect without dividing byx−8: (4x+6)(x−8)>0. Open endpoints−3/2,8; exterior rays. Dividing by an unsigned expression would lose a branch.')]
ps=[]
for l,original,key,kp,features in rows:
 ps.append(interval(l+'-solution',original,key,kp,features));ps.append(numberline(l+'-number-line',original,key,kp,features))
add('Try-Now',28,38,'Solve all four source quadratic inequalities and supply each explicitly requested number line. Equality and strictness change endpoint dots; the shifted product must be collected before sign analysis.',ps,[CRIT,INTERVAL],sketch=True)
add('Example',29,38,'Solve x²−6x−7<0 by selecting the negative portion of an upward parabola; both roots are excluded.',[
 interval('solution','x**2-6*x-7<0','Interval.open(-1,7)',38,'Factor(x−7)(x+1); the curve is negative only between its roots−1,7.')],[CRIT,INTERVAL])
rows=[('a','x**2-3*x-10<0','Interval.open(-2,5)','Open endpoints−2,5 and connect their interior.'),
 ('b','-3*x**2-13*x-4<=0','Union(Interval.open(-oo,-4),Interval.open(-Rational(1,3),oo))','Correct graph: closed endpoints−4,−1/3 with exterior rays; printed text incorrectly uses strict inequalities.'),
 ('c','x**2<=3*x','Interval(0,3)','Closed endpoints0,3 and their connected interval.'),
 ('d','(5*x-2)**2-9<0','Interval.open(-Rational(1,5),1)','Open endpoints−1/5,1 and their connected interval.')]
ps=[]
for l,original,key,features in rows:
 p=interval(l+'-solution',original,key,590,'Find the original critical values and the sign demanded by the inequality. '+features)
 graphkey=key
 if l=='b':
  graphkey='Union(Interval(-oo,-4),Interval(-Rational(1,3),oo))';p['author_expected_normalised']=graphkey
 ps.append(p);ps.append(numberline(l+'-number-line',original,graphkey,590,features))
add('Try-Now-29',1,38,'Solve four source inequalities and draw their requested number lines. In(b), the correct closed-dot graph contradicts the key’s strict textual inequality.',ps,[CRIT,INTERVAL],sketch=True)
add('Try-Now-29',2,38,'Solve4x(4−x)≤15. Because the parabola opens downward, the permitted set lies outside the two roots and includes them.',[
 interval('solution','4*x*(4-x)<=15','Union(Interval(-oo,Rational(3,2)),Interval(Rational(5,2),oo))',590,'Move15 to the left. The roots are3/2,5/2 and the original expression is at most15 on the exterior rays.')],[CRIT,INTERVAL])
p=interval('solution','x**2<(9*x+5)/2','Interval.open(-Rational(1,2),5)',590,'The standard polynomial2x²−9x−5=(2x+1)(x−5) is negative between−1/2 and5.')
p['author_source_graph_comparison']={'status':'key wrong','reason':'The main interval and function sketch use−1/2 correctly, but the number-line lower-end label is malformed (rendered as−10/5). It does not legibly represent the required lower endpoint−1/2.',
 'observed_features':'Malformed fraction/overlapping lower-end label under the left open circle; upper endpoint5 and open-dot selection are correct.','correct_features':'Clearly label the left open endpoint−1/2 and the right open endpoint5; avoid overlapping an origin tick with the fraction.'}
add('Try-Now-29',3,38,'Solve x²<(9x+5)/2. The key’s main interval is correct; its supplementary number-line lower label is recorded as a source-render defect.',[p],[CRIT,INTERVAL])
rounded_parts=[]
for label,expr,key in [('a-negative-root','(2-sqrt(10))/3','-Rational(39,100)'),('a-positive-root','(2+sqrt(10))/3','Rational(172,100)')]:
 p=v(label,expr,key,590,'The original3x²−4x−2 has discriminant40 and exact roots(2±√10)/3. Compute independently from these exact values and round only the final roots to the explicitly requested2decimal places. Exact values remain the internal interval boundaries.')
 p['operation']={'kind':'rounded','operands':[expr],'decimal_places':2}
 p['additional_operations']={'exact_roots':{'kind':'real-roots','operands':['3*x**2-4*x-2']}}
 p['additional_operation_expected']={'exact_roots':'FiniteSet((2-sqrt(10))/3,(2+sqrt(10))/3)'}
 rounded_parts.append(p)
p2=reasoning('b-interval','Exact set[(2−√10)/3,(2+√10)/3]; displayed to2dp as−0.39≤x≤1.72.',
 'The original upward quadratic is nonpositive between its two real roots, including both. The source explicitly asks2decimal places, so its displayed bounds are rounded representations of exact endpoints, not an assertion that−0.39 is an exact root. A proposed reusable recipe should retain exact internal bounds and format them only at display.',590,'matches')
p2['additional_operations']={'exact_interval':{'kind':'identity','operands':['solve_univariate_inequality(3*x**2-4*x-2<=0,x,relational=False)']}}
p2['additional_operation_expected']={'exact_interval':'Interval((2-sqrt(10))/3,(2+sqrt(10))/3)'}
add('Try-Now-29',4,38,'Solve a quadratic equation and hence its nonpositive interval, with the explicit2dp answer requirement. Preserve exact internal endpoints and their inclusive status.',rounded_parts+[p2],[CRIT,INTERVAL])

# Coordinate pairs are kept correlated, not separated into unrelated x/y sets.
def system(label,equations,key,kp,method):
 return v(label,'FiniteSet(*solve(['+','.join(equations)+'],(x,y)))',key,kp,method+' Independently substitute every ordered pair into both original equations. Do not combine x and y values from different branches.')
p=system('intersection-pairs',['x+2*y-9','x*y+18'],'FiniteSet(Tuple(-3,6),Tuple(12,-Rational(3,2)))',39,
 'Substitute x9−2y into xy+18=0, yielding2y²−9y−18=0. Recover x separately for each y and retain both ordered pairs.')
add('Example',30,39,'Find both coordinate pairs where x+2y=9 meets xy+18=0. Recovering the second coordinate is required for each root.',[p],[PAIR])
p=system('intersection-pairs',['y+2*x-11','x*y-15'],'FiniteSet(Tuple(Rational(5,2),6),Tuple(3,5))',590,
 'Substitute y11−2x into xy15 to obtain2x²−11x+15=0; x5/2 or3 leads to y6 or5 respectively.')
add('Try-Now-30',1,39,'Find the intersection coordinate pairs of y+2x=11 and xy=15; both branches satisfy the original positive product.',[p],[PAIR])
p=v('x-coordinates','solveset(2*x**2-8*x+9-(3-x),x,domain=S.Reals)','FiniteSet(Rational(3,2),2)',590,
 'Eliminate y using x+y3. The resulting2x²−7x+6=0 gives x3/2 and2. The stem asks only x-coordinates, so do not impose an extra ordered-pair response requirement.')
add('Try-Now-30',2,39,'Find only the x-coordinates where y=2x²−8x+9 meets x+y=3; this response differs from the preceding full-coordinate task.',[p],[PAIR])
ps=[system('a',['2*x-1+3*y','3*y**2-x**2-2'],'FiniteSet(Tuple(-1,1),Tuple(5,-3))',590,
 'Use the linear2x1−3y to reduce the quadratic relation. Both solution branches are real and satisfy the original nonlinearity.'),
 system('b',['2*x+3*y+19','2*x**2+3*y-5'],'FiniteSet(Tuple(4,-9),Tuple(-3,-Rational(13,3)))',590,
 'Subtract the two equations after matching3y, obtaining2x²−2x−24=0. Recover y with the original line for each x.')]
add('Try-Now-30',3,39,'Solve two linear/nonlinear simultaneous systems, keeping their solution pairs correlated. An elimination alternative is available when the linear terms align.',ps,[PAIR])
refs=[
 (54,36,'Three-parabola reconstruction grid','Shared axes show X minimum(−2,−6), intercept10; Y maximum(2,8), roots−2,6, intercept6; Z minimum(4,2), point(2,6). These are compatible constraints per curve, not interchangeable labels.',[RECON],'graph',[('Tuple(4*0**2+16*0+10,-2**2/2+2*2+6,2**2-8*2+18)','Tuple(10,8,6)')],'Example:27'),
 (55,36,'Two equivalent reconstructions for Y','Root-factor and vertex forms both give−x²/2+2x+6 for the sameYcurve. These are alternative methods within a structure, not two source families.',[RECON],'table',[('expand(-(x+2)*(x-6)/2+((x-2)**2/2-8))','0')],'Example:27'),
 (56,37,'Try27 given two-parabola grid','X has maximum(−3,4) and roots−5,−1. Y has minimum(3,4), intercept13 and no crossings. The grid provides data to reconstruct each equation; no sketch response is requested.',[RECON],'graph',[('Tuple(-(-3)**2-6*(-3)-5,3**2-6*3+13)','Tuple(4,4)')],'Try-Now:27'),
 (57,37,'Example28 root/sign sketch','The upward graph2x²−3x−2 crosses at−1/2,2. Nonnegativity selects exterior regions, not the negative interior.',[CRIT,INTERVAL],'graph',[('Tuple(2*(-Rational(1,2))**2-3*(-Rational(1,2))-2,2*2**2-3*2-2)','Tuple(0,0)')],'Example:28'),
 (58,37,'Example28 exterior number line','Both roots−1/2,2 are included for≥0; filled endpoints and two outward rays must agree with the original inequality.',[INTERVAL],'diagram',[],'Example:28'),
 (59,37,'Inequality sketch checklist','The note asks for original quadratic orientation and x-intercepts before reading sign regions. Endpoint inclusion follows the relational symbol, not the chosen plotting method.',[CRIT,INTERVAL],'table',[],'Example:28'),
 (60,38,'Example29 negative-region sketch','x²−6x−7 opens upward and crosses at−1,7; the function is negative precisely between them.',[CRIT,INTERVAL],'graph',[('expand((x-7)*(x+1))','x**2-6*x-7')],'Example:29'),
 (61,38,'Example29 interior number line','For strict negativity use open endpoints−1,7 and connect their interior. The inequality excludes both roots.',[INTERVAL],'diagram',[],'Example:29'),
 (62,39,'Linear substitution arrow in Example30','x9−2y from the linear equation is substituted forx inxy+18=0. This produces2y²−9y−18=0; each resultingy must recover its ownx.',[PAIR],'table',[('expand(-((9-2*y)*y+18))','2*y**2-9*y-18')],'Example:30')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={36:'Every Try26 and Example27 equation recorded. Shared graph and two-methodYreference separately retained.',37:'Try27 given grid, Example28 solution, sign sketch, number line and orientation checklist fully recorded.',38:'Every Try28 and independently numbered Try29 task recorded, including all explicitly requested number-line responses. Example29 graph and number line retained. Rounded-boundary policy and source-key discrepancies are explicit.',39:'Example30 and all three independently numbered Try30 tasks recorded, including both systems under Q3. Ordered-pair versus x-only requirements are preserved; substitution arrow retained.'}
pages=[]
for page in range(36,40):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All reconstruction/inequality/intersection content accounted for. Actual strictness and explicit precision are preserved; secondary answer-graph defects do not erase a correct main interval.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-intervals.json',{'scope':'Every36–39source response, with separately requested number lines.','items':answers}),('census-YM-C1-intervals.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete36–39page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
