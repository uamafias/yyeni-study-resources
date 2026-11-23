"""YM386–389: original modulus inequalities, complete sets and requested visuals."""
import hashlib
import author_YM_C8_opening as h
from author_YM_C8_opening import W,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers
INEQ='8227:2020:M2:T1:O01:D03';SKETCH='8227:2020:M2:T1:O02:D01'
def ev(page):
 name='YM-C8-key-634' if page>=634 else 'YM-C8-key-630' if page>=630 else f'YM-C8-{376+4*((page-376)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev
def interval(label,original,key,kp,correct=None):
 p=v(label,'solve_univariate_inequality('+original+',x,relational=False)',key,kp,
 'Solve the ORIGINAL inequality on the whole real domain. Split at the modulus zero and retain its actual sign on each branch; intersect with each branch domain and union the resulting sets. A negative right side must be handled before squaring. Preserve strict versus inclusive endpoints, empty sets, singletons and the whole real line.')
 p.update(original_inequality=original,assessed_8227_demand_ids=[INEQ],response_format='symbolic',original_domain='All real x.')
 if correct:p.update(author_expected_normalised=correct,source_interpretation='The printed Try12(f) key x<−1 omits valid values. For x<2, the original gives x<3 and thus the whole branch; for x≥2 it gives x>−1 and thus the whole branch. The union is R.')
 return p
def visual(label,original,key,kp,kind='number-line',curves=None):
 p=reasoning(label,'Solution set '+key+'.',
 'Independently solve the original inequality, then check the visual representation against that full set. Number lines require correctly placed open/closed endpoints, interior intervals or exterior rays, with explicit empty/whole-real/singleton cases. Function sketches require original vertices, slopes and intersections; no extraneous intersection from a squared equation is admitted.',kp,'sketch')
 p.update(assessed_8227_demand_ids=[INEQ],response_format='sketch',given_representation='text',original_inequality=original,credited_features=['Exact set '+key,'Correct endpoint inclusion and interval/ray direction'],criteria_basis='Derived from the explicit source request and exact solution, not an official marking tariff.')
 extra(p,'complete-original-set','solve_univariate_inequality('+original+',x,relational=False)',key)
 if curves:
  p['assessed_8227_demand_ids'].append(SKETCH)
  p['curves']=curves
  p['key_visual_availability']='The key supplies only the symbolic interval, not a separate function sketch. Sketch features and the no-intersection case are author-derived from the original curves.'
  p['credited_features']+=['Correct original modulus vertex and ray slopes','Correct straight line and every actual intersection','Identify the region satisfying the original inequality, including any no-intersection case']
  extra(p,'actual-curve-intersections','solveset(('+curves[0]+')-('+curves[1]+'),x,domain=S.Reals)',curves[2])
 return p
def add(kind,n,page,note,parts):
 r=h.add(kind,n,page,note,parts)
 r.update(sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='Solving the ORIGINAL inequality is direct. Explicit number-line or function-sketch requests remain separate response evidence. Ordinary linear/quadratic manipulation is a component; it is not a second independently assessed AS demand. Worked solution pictures are teaching assets, not given diagrams.',value_level_scope_decisions=[dict(rule_id='8227:QUAL01',status='within' if any(SKETCH in p['assessed_8227_demand_ids']for p in parts)else 'not applicable',quoted_value=note,reason='All requested original modulus function sketches here have integer coefficients. Scalar inequalities and number-line responses are not fractional-coefficient modulus graph tasks.')])
 return r
add('Example',10,386,'Solve |2x+3|≤6 and |x+1|+6<0. The worked graph is a solution aid, not a requested learner sketch.',[interval('a','Abs(2*x+3)<=6','Interval(-Rational(9,2),Rational(3,2))',386),interval('b','Abs(x+1)+6<0','S.EmptySet',386)])
data=[('a','Abs(x-3)<=4','Interval(-1,7)'),('b','Abs(x+2)<3','Interval.open(-5,1)'),('c','Abs(x-7)<6','Interval.open(1,13)'),('d','Abs(3+x)+4<0','S.EmptySet'),('e','Abs(2*x-4)<10','Interval.open(-3,7)'),('f','Abs(3*x+2)<0','S.EmptySet'),('g','Abs(x-9)<=0','FiniteSet(9)'),('h','Abs(9*x+2)<=1','Interval(-Rational(1,3),-Rational(1,9))'),('i','Abs(3-2*x)-5<=0','Interval(-1,4)')]
add('Try-Now',10,387,'Nine less-than modulus inequalities, including impossible negative targets and a zero-target singleton. All original coefficients and relational signs are retained.',[interval(l,o,k,633)for l,o,k in data])
add('Example',11,387,'Solve |2−6x|>10 and |3x−9|>0. Dividing a branch inequality by −6 reverses its sign; the second solution excludes only x=3.',[interval('a','Abs(2-6*x)>10','Union(Interval.open(-oo,-Rational(4,3)),Interval.open(2,oo))',387),interval('b','Abs(3*x-9)>0','Union(Interval.open(-oo,3),Interval.open(3,oo))',387)])
data=[('a','Abs(2*x-3)>5','Union(Interval.open(-oo,-1),Interval.open(4,oo))',633),('b','Abs(2*x-3)-7>=0','Union(Interval(-oo,-2),Interval(5,oo))',633),('c','Abs(6*x+10)>3','Union(Interval.open(-oo,-Rational(13,6)),Interval.open(-Rational(7,6),oo))',633),('d','Abs(-2*x-4)>9','Union(Interval.open(-oo,-Rational(13,2)),Interval.open(Rational(5,2),oo))',633),('e','Abs(x/2)+9>13','Union(Interval.open(-oo,-8),Interval.open(8,oo))',633),('f','Abs(x+12)+3>=17','Union(Interval(-oo,-26),Interval(2,oo))',633),('g','Abs(2*x-4)>=0','S.Reals',634),('h','Abs(4+x)>-3','S.Reals',634),('i','Abs(2*x-3)+5>5','Union(Interval.open(-oo,Rational(3,2)),Interval.open(Rational(3,2),oo))',634)]
ps=[]
for l,o,k,kp in data:ps.extend([interval(l+'-solution',o,k,kp),visual(l+'-number-line',o,k,kp)])
add('Try-Now-11',1,387,'Nine greater-than inequalities explicitly require number lines as well as full symbolic solution sets. All-real cases (g),(h) and the single excluded value in (i) are genuine branches.',ps)
data=[('a','Abs(x-3)>3','Union(Interval.open(-oo,0),Interval.open(6,oo))'),('b','Abs(1+x)<8','Interval.open(-9,7)'),('c','Abs(x+3)<4','Interval.open(-7,1)')]
ps=[]
for l,o,k in data:ps.extend([interval(l+'-solution',o,k,634),visual(l+'-number-line',o,k,634)])
add('Try-Now-11',2,387,'Three mixed inequalities each explicitly ask for a number line. The complete question ends on this page; Q3 on the next page is independently numbered.',ps)
data=[('a','Abs(7*x)<=42','Interval(-6,6)'),('b','Abs(4+5*x)>24','Union(Interval.open(-oo,-Rational(28,5)),Interval.open(4,oo))'),('c','-3*Abs(x)<18','S.Reals'),('d','Abs(x)-3>7','Union(Interval.open(-oo,-10),Interval.open(10,oo))'),('e','Abs(6*x)/8>4','Union(Interval.open(-oo,-Rational(16,3)),Interval.open(Rational(16,3),oo))'),('f','10*Abs(10*x-8)<=80','Interval(0,Rational(8,5))')]
add('Try-Now-11',3,388,'Six inequalities include a negative OUTSIDE multiplier in (c), yielding all real values. This independently numbered Q3 asks solutions, without repeating the prior Q2 number-line instruction.',[interval(l,o,k,634)for l,o,k in data])
p=interval('solution','Abs(x-3)>=2*x-9','Interval(-oo,6)',388)
p['source_method_warning']='The printed equality check rejects x=4 because it is not an intersection. But x=4 DOES satisfy the inequality. The final union x≤6 is correct; failed equality is not a valid reason to reject an interior inequality point.'
add('Example',12,388,'Solve |x−3|≥2x−9 by algebra and a worked graph. Final x≤6 is correct; the source equality-check explanation incorrectly implies that x=4 is invalid.',[p])
data=[('a','Abs(x-3)<2*x-4','Interval.open(Rational(7,3),oo)',['Abs(x-3)','2*x-4','FiniteSet(Rational(7,3))']),('b','Abs(2*x-5)>x+1','Union(Interval.open(-oo,Rational(4,3)),Interval.open(6,oo))',['Abs(2*x-5)','x+1','FiniteSet(Rational(4,3),6)']),('c','Abs(x-3)>2*x-6','Interval.open(-oo,3)',['Abs(x-3)','2*x-6','FiniteSet(3)']),('d','Abs(x-3)<=-2*x+6','Interval(-oo,3)',['Abs(x-3)','-2*x+6','FiniteSet(3)']),('e','Abs(2*x-4)>=x+1','Union(Interval(-oo,1),Interval(5,oo))',['Abs(2*x-4)','x+1','FiniteSet(1,5)']),('f','Abs(2*x-4)>x-5','S.Reals',['Abs(2*x-4)','x-5','S.EmptySet'])]
ps=[]
for l,o,k,curves in data:
 p=interval(l+'-solution',o,'Interval.open(-oo,-1)'if l=='f'else k,634,k if l=='f'else None)
 ps.extend([p,visual(l+'-sketch',o,k,634,'function-sketch',curves)])
add('Try-Now',12,388,'Six modulus-versus-line inequalities explicitly request supporting sketches. In (f), |2x−4|>x−5 is true for ALL real x, unlike the printed key x<−1. Original integer graph coefficients are retained.',ps)
p=interval('solution','Abs(x+2)<Abs(5-2*x)','Union(Interval.open(-oo,1),Interval.open(7,oo))',389)
extra(p,'squared-difference-factorisation','factor((x+2)**2-(5-2*x)**2)','-3*(x-7)*(x-1)')
add('Example',13,389,'Solve |x+2|<|5−2x| by squaring two NONNEGATIVE quantities, then selecting exterior intervals; compare with the worked two-V graph. No separate learner sketch is requested.',[p])
data=[('a','Abs(2*x-1)<Abs(3*x)','Union(Interval.open(-oo,-1),Interval.open(Rational(1,5),oo))'),('b','Abs(x-3)<Abs(2*x+1)','Union(Interval.open(-oo,-4),Interval.open(Rational(2,3),oo))'),('c','Abs(x-4)>Abs(x+1)','Interval.open(-oo,Rational(3,2))'),('d','Abs(x-3)>Abs(x+2)','Interval.open(-oo,Rational(1,2))'),('e','Abs(2*x-3)<=Abs(3*x)','Union(Interval(-oo,-3),Interval(Rational(3,5),oo))'),('f','Abs(x-2)>Abs(x+5)','Interval.open(-oo,-Rational(3,2))')]
add('Try-Now',13,389,'Six modulus-versus-modulus inequalities. Squaring is equivalent because BOTH sides are nonnegative. Opposite-equal leading squares in (c),(d),(f) reduce the comparison to a linear inequality.',[interval(l,o,k,634)for l,o,k in data])
refs=[(24,386,'Modulus inequality reference table','Less/more branches, open/closed number lines and exceptional target signs. The source more-than caption, example right endpoint text and bottom sign-case notes contain errors; use separately derived complete cases.',INEQ,'table',None),(25,386,'Example10 solution graph and number line','Correct interval [−9/2,3/2] and vertex−3/2. The source left endpoint label lacks its minus sign; the tick−2 is not the vertex label.',INEQ,'graph','Example:10'),(26,386,'Example10 AND and nonnegative-target notes','The two less-than constraints must BOTH hold. A modulus cannot be less than a negative number. The impossible case is explicit.',INEQ,'table','Example:10'),(27,387,'Example11 solution graph and exterior number line','|2−6x|>10 has open boundaries−4/3,2 and exterior rays. Vertex1/3,0 is distinct from the boundary−4/3.',INEQ,'graph','Example:11'),(28,387,'Negative-division direction reminder','Dividing by−6 reverses the inequality. Inclusive/strict endpoints remain tied to the original relation.',INEQ,'table','Example:11'),(29,388,'Example12 solution graph','Original |x−3| and line2x−9 intersect only at6. The union x≤6 includes4 even though4 is not an intersection.',INEQ,'graph','Example:12'),(30,388,'Example12 flawed equality check','Testing equality can establish intersection candidates, not reject inequality interior points. The source final set is nevertheless correct.',INEQ,'table','Example:12'),(31,389,'Example13 squared-difference quadratic','The negative quadratic −3(x−1)(x−7) is <0 outside1,7. Both original moduli are nonnegative, so squaring preserves their order.',INEQ,'graph','Example:13'),(32,389,'Example13 original two-V comparison graph','|x+2| and|5−2x| intersect at1 and7, with vertices−2 and5/2. The original right-hand V lies above the left forx<1 orx>7.',INEQ,'graph','Example:13'),(33,389,'Example13 intersection check and alternate sign form','Equality at1 and7 identifies boundaries only. The source alternate x²−8x+7>0 has the same exterior set.',INEQ,'table','Example:13')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,[teaches],rep,[],parent)
 figures[-1].update(item_id=f'8227:TB:YM:C8:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C8:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read rendered number-line endpoints, interval directions, original graph vertices and intersection boundaries. Derive original inequality sets independently; source errors are registered separately. These are teaching/solution panels, not diagram givens.'
h.pages=[dict(pdf_page=page,printed_page=pp(page),chapter=8,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='All Examples10–13,Try10,Try11Q1–3,Try12,Try13 and ten reference panels enumerated. Q2 ends387;Q3 starts388. Number-line and supporting-function-sketch instructions are retained.',scope_screen='Original real inequalities, nonnegative squaring conditions and exact endpoint cases preserved. Requested graph coefficients here are integers.')for page in range(386,390)]
if __name__=='__main__':h.save('inequalities','Complete386–389 inequality responses and actual teaching panels; original solution sets checked independently of keys.')
