"""YM144–147: tangency/discriminants, Exercise3.2 and exam-style examples."""
import json
import author_YM_C3_geometry_opening as g
from author_YM_C3_geometry_opening import W,SRC,SHA,pp,ev,value,line,intersection,rounded,extra,fig,figures,compute,expression,equivalent,LINE,INTERSECT,COORD
from author_YM_C3_opening import reasoning
g.prior.answers.clear();g.prior.new.clear();figures.clear();g.prior.corrections.clear()
answers=g.prior.answers;new=g.prior.new;corrections=g.prior.corrections
TANGENT='8227:2020:M1:T4:O02:D02';COMPOSE='8227:2020:M1:T3:O04:D01';RANGE='8227:2020:M1:T3:O02:D02';SQUARE='8227:2020:M1:T1:O01:D01'

def add(kind,n,page,note,parts,rep='text'):
 for p in parts:p.setdefault('given_representation',rep);p.setdefault('response_format','symbolic')
 return g.add(kind,n,page,note,parts,rep)
def proof(label,expr,result,kp,method,direct):
 p=value(label,expr,result,kp,method,direct);p['check_mode']='show/prove';p['response_format']='proof/show-that';return p

ps=[proof('a','expand((x**2-x+3)-(3*x+a))','x**2-4*x+3-a',144,'Equate the ORIGINAL line/curve ordinates and move all terms to one side. This establishes the requested intersection equation, not a derivative-based tangency method.',[INTERSECT]),value('b','4-(-1)','5',144,'The intersection polynomial has root sum4. Given one x-coordinate−1, the other is5. Independently substituting the given root determines source parameter a8 and yields both roots−1,5.',[INTERSECT])]
extra(ps[1],'original-roots','solveset(x**2-4*x+3-8,x,domain=S.Reals)','FiniteSet(-1,5)')
p=value('c-a','solveset(discriminant(x**2-4*x+3-a,x),a,domain=S.Reals)','FiniteSet(-1)',144,'A tangent gives one repeated root of the ORIGINAL quadratic intersection polynomial. Set its discriminant to zero and obtain a−1; the leading coefficient is fixed1.',[TANGENT]);ps.append(p)
p=value('c-point','Tuple(2,2**2-2+3)','Tuple(2,5)',144,'At a−1 the intersection polynomial becomes(x−2)^2. Use repeated x2 in the ORIGINAL curve to obtain P(2,5), and check the line3x−1 gives the same y.',[TANGENT,INTERSECT]);extra(p,'line-check','3*2-1','5');ps.append(p)
add('Example',22,144,'Curve y=x²−x+3,line y=3x+a: establish the intersection quadratic, find the other root when one is−1, then determine tangent a−1 and contact P(2,5).',ps)
p=value('a','solve_univariate_inequality(discriminant(3*x**2-k*x+12,x)<0,k,relational=False)','Interval.open(-12,12)',601,'Original line gives y=k−x. Substitute into curve y=2x+12/x, with x!=0, to obtain3x²−kx+12=0. Its constant12 ensures x0 is not a candidate root. No real intersection means discriminant k²−144<0, with strict bounds.',[INTERSECT])
p2=value('b','FiniteSet(Tuple(1,15-1),Tuple(4,15-4))','FiniteSet(Tuple(1,14),Tuple(4,11))',601,'At actual k15, solve3x²−15x+12=0 for x1,4 and use ORIGINAL y=15−x. Both inputs are nonzero, so both satisfy the rational curve.',[INTERSECT]);extra(p2,'x-roots','solveset(3*x**2-15*x+12,x,domain=S.Reals)','FiniteSet(1,4)');extra(p2,'original-curve-values','Tuple(2*1+12/1,2*4+12/4)','Tuple(14,11)')
p3=line('c',('Rational(5,2)','Rational(25,2)'),'1','x+10',601)
add('Try-Now',22,144,'Curve y=2x+12/x,line y+x=k: find nonintersection interval−12<k<12. At k15 find both intersection points, then their perpendicular bisector y=x+10.',[p,p2,p3])

p=line('a',(5,8),'-Rational(3,2)','-3*x/2+Rational(31,2)',602);p['canonical_response_form']='3x+2y=31';extra(p,'requested-standard-form','expand(2*(-3*x/2+Rational(31,2))+3*x)','31')
p2=intersection('b','-3*x/2+Rational(31,2)','5*x-30','Tuple(7,5)',602)
add('Exercise-3.2',1,145,'A(2,6),B(8,10),C(6,0): give the AB perpendicular bisector in ax+by=c form, then its intersection D(7,5) with BC.',[p,p2])
ps=[line('a',(1,6),'Rational(1,2)','x/2+Rational(11,2)',602),intersection('b','x/2+Rational(11,2)','x-1','Tuple(13,12)',602)]
p=rounded('c','2*sqrt((1-3)**2+(6-2)**2)+2*sqrt((13-1)**2+(12-6)**2)','35.8',602,'Compute adjacent rectangle lengths AB=sqrt20,BC=sqrt180 from ORIGINAL/derived coordinates and take2(AB+BC)=16sqrt5. The source key rounds to3significant figures35.8; no separate source accuracy instruction is printed.');ps.append(p)
add('Exercise-3.2',2,145,'Rectangle A(3,2),B(1,6),AC:y=x−1. Find BC, C(13,12), then perimeter16sqrt5≈35.8 using adjacent side lengths.',ps,'diagram')
p=reasoning('a','Perpendicular gradient=−(a+4)/(a+10) when a!=−10; at a−10 the perpendicular is vertical and has no finite gradient.','Original AB displacement is(a+4,a+10). A perpendicular direction is(a+10,−(a+4)), so its finite gradient has the stated ratio when its horizontal component is nonzero. At a−4 the ORIGINAL is vertical and the perpendicular has gradient0, still given by the finite formula. The key omits the a−10 exceptional case.',602,'key incomplete');p['assessed_8227_demand_ids']=[LINE];extra(p,'perpendicular-dot','(a+4)*(a+10)+(a+10)*(-(a+4))','0')
p2=value('b','solveset((a+4)**2+(a+10)**2-260,a,domain=S.Reals)','FiniteSet(4,-18)',602,'Use ORIGINAL squared distance(a+4)^2+(a+10)^2=260. Both a4 and−18 give the requested distance and neither is the exceptional parameter−10.',[LINE]);extra(p2,'both-distances-squared','Tuple((4+4)**2+(4+10)**2,(-18+4)**2+(-18+10)**2)','Tuple(260,260)')
add('Exercise-3.2',3,145,'A(a,2a−1),B(2a+4,3a+9): state the perpendicular gradient with its vertical exception; with distance sqrt260 find a4or−18.',[p,p2])
ps=[intersection('A','3*x','(x+11)/4','Tuple(1,3)',602)]
p=value('B','Tuple(solve(12*x+(13-x)+11-68,x)[0],3*solve(12*x+(13-x)+11-68,x)[0])','Tuple(4,12)',602,'Parallelogram diagonals bisect at E(13/2,17/2), so B+D=(13,17). B lies on y=3x and D on4y=x+11. Substitute D_x=13−B_x and solve these original constraints.',[LINE,INTERSECT]);ps.append(p)
p=value('C','Tuple(2*Rational(13,2)-1,2*Rational(17,2)-3)','Tuple(12,14)',602,'Use C=2E−A for opposite vertices after finding actual A. Preserve the source half-integer midpoint exactly.');ps.append(p)
p=value('D','Tuple(13-4,17-12)','Tuple(9,5)',602,'Use D=2E−B and check original AD relation4y=x+11; source parallelogram order is A,B,C,D.');extra(p,'AD-incidence','4*5-(9+11)','0');ps.append(p)
add('Exercise-3.2',4,145,'Parallelogram AB:y=3x,AD:4y=x+11,diagonal midpoint E(6½,8½). Find all four vertices A(1,3),B(4,12),C(12,14),D(9,5).',ps,'diagram')
p=proof('a-isosceles','Tuple((4-(-2))**2+(6-(-1))**2,(6-4)**2+(-3-6)**2)','Tuple(85,85)',602,'Compare ORIGINAL squared side lengths AB²=BC²=85, establishing AB=BC=sqrt85 without rounded lengths.',[])
p2=value('a-area','Abs((4+2)*(-3+1)-(6+1)*(6+2))/2','34',602,'Use half the absolute determinant of ORIGINAL vectors AB=(6,7),AC=(8,−2). This exact area is34, not an unqualified signed cross-product result.');p2['units']=p2['printed_key_units']='square units'
p3=value('b-x','solve(Rational(7,6)*x+Rational(4,3)-(-Rational(6,7)*(x-6)-3),x)[0]','Rational(34,85)',602,'D is where original AB intersects the perpendicular through C(6,−3). Solve the two exact line equations. The question asks only D’s x-coordinate34/85; the key additionally gives y9/5.',[LINE,INTERSECT]);extra(p3,'D-y','Rational(7,6)*Rational(34,85)+Rational(4,3)','Rational(9,5)')
r=add('Exercise-3.2',5,145,'Triangle A(−2,−1),B(4,6),C(6,−3): establish AB=BC, find exact area34, then the x-coordinate34/85 of the foot from C to AB.',[p,p2,p3]);r['direct_demand_aspects']=[{'demand_id':LINE,'assessed_facet':'Only(b)requires the perpendicular-foot line constraints; isosceles and determinant-area outcomes remain prerequisite Euclidean geometry.'}]

p=value('a','solveset(discriminant(x**2+(2*k-2)*x+36-4*k,x),k,domain=S.Reals)','FiniteSet(-7,5)',146,'Original f=4x−2k,g=9/(2−x) gives36/(2−x)−2k=x with x!=2. Multiply by the nonzero denominator, rearrange the quadratic and impose repeated-root discriminant0. Both parameter values remain admissible.',[COMPOSE,'8227:2020:M1:T1:O02:D03']);extra(p,'cleared-polynomial','expand(36-(2-x)*(x+2*k))','x**2+(2*k-2)*x+36-4*k')
p2=value('b','Tuple(-(2*(-7)-2)/2,-(2*5-2)/2)','Tuple(8,-4)',146,'For k−7 the repeated root is8; for k5 it is−4. Keep these correlated parameter/root pairs and verify both in the ORIGINAL rational equation; neither equals excluded input2.',[COMPOSE]);extra(p2,'original-residuals','Tuple(36/(2-8)-2*(-7)-8,36/(2-(-4))-2*5-(-4))','Tuple(0,0)')
r=add('Example',23,146,'f=4x−2k,g=9/(2−x): find k giving equal roots of fg(x)=x, then correlated roots k−7→8 and k5→−4, excluding the original pole2.',[p,p2]);r.update(exam_style=True,exam_style_basis='The source explicitly places this Example under its Exam-Style Questions heading; no board/year attribution or official tariff is claimed.')
def square(label,a,b,c,key,kp):
 p=value(label,f'{a}*(x+Rational({b},{2*a}))**2+({c}-Rational({b*b},{4*a}))',key,kp,'Complete the square independently from original coefficients; retain the requested vertex-form output.',[SQUARE]);return p
ps=[square('a',2,-12,7,'2*(x-3)**2-11',602)]
p=value('b','2*x**2-12*x+7','Interval(-11,oo)',602,'Compute the real image of the original convex quadratic onR, including its attained minimum−11 at x3.',['8227:2020:M1:T3:O02:D02']);p['operation']={'kind':'real-image-range','operands':['2*x**2-12*x+7','S.Reals']};ps.append(p)
p=value('c','solve_univariate_inequality(2*x**2-12*x+7<21,x,relational=False)','Interval.open(-1,7)',602,'The ORIGINAL strict inequality gives (x−3)^2<16. Both boundary roots are excluded; this is a quadratic inequality rather than an image-only question.',['8227:2020:M1:T1:O06:D02']);ps.append(p)
p=value('d','solveset(discriminant(2*(2*x**2-12*x+7)+k,x),k,domain=S.Reals)','FiniteSet(22)',602,'Original g=2x+k, so gf=4x²−24x+14+k. Equal roots require its discriminant0, giving k22; fixed leading coefficient4 does not degenerate.',[COMPOSE,'8227:2020:M1:T1:O02:D03']);ps.append(p)
r=add('Try-Now',23,146,'f=2x²−12x+7: complete the square, give range and solve f<21; with g=2x+k choose k22 so gf=0 has equal roots.',ps);r.update(exam_style=True,exam_style_basis='Located under the source Exam-Style Questions heading; no primary examination attribution or official award evidence.')

ps=[intersection('a-M','x/2-Rational(1,2)','-2*x+12','Tuple(5,2)',147)]
p=value('a-D','Tuple(2*5-3,2*2-6)','Tuple(7,-2)',147,'M is the midpoint of diagonal BD by ORIGINAL BM=MD, so D=2M−B with B(3,6). Check M lies on AC and BD and the diagonals are perpendicular.');ps.append(p)
p=value('b','sqrt((5-(-1))**2+(2-(-1))**2)/sqrt((9-5)**2+(4-2)**2)','Rational(3,2)',147,'Use actual A(−1,−1),M(5,2),C(9,4); lengths are3sqrt5 and2sqrt5. The requested AM:MC ratio is3:2, not the scalar3/2 alone.');p['canonical_response']='AM:MC=3:2';ps.append(p)
r=add('Example',24,147,'Quadrilateral A(−1,−1),B(3,6),C(9,4),diagonals perpendicular at M and BM=MD. Find M(5,2),D(7,−2),then ratioAM:MC3:2.',ps,'diagram');r.update(exam_style=True,exam_style_basis='Source Exam-Style Questions section; no primary examination attribution or official tariff.')
ps=[intersection('a','-2*x/3+Rational(46,3)','3*x/2-Rational(17,2)','Tuple(11,8)',602)]
p=value('b','sqrt((11-2)**2+(8-14)**2)/sqrt((14-11)**2+(6-8)**2)','3',602,'Use actual A(2,14),X(11,8),B(14,6); lengths are3sqrt13 andsqrt13. Return the requested ordered ratio AX:XB=3:1.');p['canonical_response']='AX:XB=3:1';ps.append(p)
r=add('Try-Now',24,147,'A(2,14),B(14,6),C(7,2),X on AB with CX perpendicular AB: find X(11,8) then ordered ratioAX:XB3:1.',ps,'diagram');r.update(exam_style=True,exam_style_basis='Source Exam-Style Questions section; no primary examination attribution or official tariff.')

refs=[(73,145,'Exercise3.2Q2 given rectangle','A(3,2),B(1,6),diagonal AC:y=x−1. Preserve consecutive rectangle order, right angles and diagonal incidence; C is determined by BC and AC, not measured scale.','Exercise-3.2:2'),(74,145,'Exercise3.2Q4 given parallelogram','AB:y=3x,AD:4y=x+11 and diagonal midpointE(13/2,17/2). Both diagonals bisect each other; sides must obey the two exact equations.','Exercise-3.2:4'),(75,147,'Example24 given quadrilateral','A(−1,−1),B(3,6),C(9,4),AC perpendicular BD atM and BM=MD. M need not bisect AC; actual AM:MC is3:2.','Example:24'),(76,147,'Try24 given normal-foot triangle','A(2,14),B(14,6),C(7,2),footX onAB. Preserve X as the perpendicular foot and ordered division AX:XB; the drawing is not a calibrated ratio measure.','Try-Now:24')]
for n,page,label,note,parent in refs:
 fig(n,page,label,note,[LINE,INTERSECT],'diagram',[],parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:');f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure')
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':3,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'Every Example22–24,Try22–24,Exercise3.2Q1–5 response and all four given diagrams are enumerated across144–147. Actual requested forms,strict bounds,ratio order and pole/vertical-gradient cases are retained. The exam-style header is printed2.3 in Chapter3; this is a source heading typo,not a new chapter.','scope_screen':'Quadratic line/curve intersections,tangency and equation-based geometry are in scope. Direct claims follow the asked outputs; Euclidean distance/area/ratio arithmetic is supporting. Source exam-style placement does not establish board attribution or official criteria.'}for page in range(144,148)]

if __name__=='__main__':
 for name,data in [('answers-YM-C3-geometry-exercise.json',{'scope':'Every144–147 requested output.','items':answers}),('census-YM-C3-geometry-exercise.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete144–147 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
