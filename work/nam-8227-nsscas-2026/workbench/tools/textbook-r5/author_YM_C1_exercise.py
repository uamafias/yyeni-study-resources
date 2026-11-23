"""Fixed YM47–48 Exercise1: every requested output, original reciprocal exponents."""
import hashlib,json
import author_YM_C1_intervals as base
import author_YM_C1_quadratic_graphs as graphs
import author_YM_C1_identities_cubics as identities
from author_YM_C1_intervals import opening,W,SRC,SHA,ev,v,reasoning,compute,expression,equivalent,fig,figures
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=base.corrections
SQUARE=graphs.SQUARE;VERTEX=graphs.VERTEX;SKETCH=graphs.SKETCH;RECON=graphs.RECON;IDENTITY=identities.IDENTITY;CUBIC=identities.CUBIC
RECOG='8227:2020:M1:T1:O04:D01';SOLVE='8227:2020:M1:T1:O04:D02';FILTER='8227:2020:M1:T1:O04:D03'
CALC='8227:2020:M1:T1:O02:D01';NATURE='8227:2020:M1:T1:O02:D02';PAIR=base.PAIR;TANGENT='8227:2020:M1:T4:O02:D02';CRIT=base.CRIT;INTERVAL=base.INTERVAL

def add(n,page,note,parts,direct,components=None,rep='text',sketch=False):
 r=base.add('Exercise-1',n,page,note,parts,direct,rep,sketch)
 r['component_demand_ids']=components or[]
 r['exam_style']=True
 r['exam_style_basis']='The continuation of this same Exercise1Q1–22 series has the printed running heading1.7 Exam-Style Questions on source48. Source-labelled textbook exam-style only; no primary NSSCAS paper attribution is asserted.'
 r['mapping_rationale']='Requested results and enforced method are direct. Ordinary quadratic arithmetic, common-base exponent matching and incidental discriminants remain components when another result is the assessed goal. Native source mathematics, including negative exponents, controls the computation; printed keys never determine the original equation.'
 return r

def roots(label,f,key,method):
 p=v(label,f,key,591,method);p['operation']={'kind':'real-roots','operands':[f]};return p

def rounded(label,expr,key):
 p=v(label,expr,key,591,'Derive the original exact quadratic root, preserve its nonzero denominator/domain, then round only the final answer to the explicitly requested2decimal places. The decimal key does not determine the exact root.')
 p['operation']={'kind':'rounded','operands':[expr],'decimal_places':2};return p

ps=[v('a','solve(3**(x-2)-81,x)[0]','6',591,'81=3⁴, so common positive bases give x−2=4. This does not demonstrate a requested logarithmic method.'),
 v('b','solve(4**x+2**(2*x-3)-Rational(9,8),x)[0]','0',591,'Write4^x=2^(2x) and2^(2x−3)=2^(2x)/8. Then(9/8)2^(2x)=9/8, givingx0.'),
 v('c','imageset(Lambda(x,log(x)/log(3)),solveset(x**2-12*x+27,x,domain=Interval.open(0,oo)))','FiniteSet(1,2)',591,'Setu=3^x>0. The quadraticu²−12u+27 has positive roots3,9, givingx1,2; preserve both branches.'),
 roots('d','sqrt(6*x+1)-5','FiniteSet(4)','Originalx≥−1/6; squaring yieldsx4, which satisfies the original principal-root equation.'),
 roots('e','sqrt(3*x-4)-sqrt(11)','FiniteSet(5)','Originalx≥4/3; equal nonnegative square roots give3x−4=11 andx5.'),
 reasoning('f','No real solution.',
 'The original√(2x−3)=5√(x+2) requiresx≥3/2. Squaring gives2x−3=25x+50 and candidate−53/23, outside that domain. Thus no original real solution exists; the key correctly says no solution.',591,'matches')]
ps[-1]['additional_operations']={'squared_candidate':{'kind':'real-roots','operands':['2*x-3-25*(x+2)']}};ps[-1]['additional_operation_expected']={'squared_candidate':'FiniteSet(-Rational(53,23))'}
r=add(1,47,'Solve all six source equations, distinguishing common-base prerequisites, a positive-exponential quadratic substitution, and original square-root domain filtering.',ps,[RECOG,SOLVE,FILTER],components=[opening.QUAD]);r['direct_demand_aspects']=[{'demand_id':RECOG,'assessed_facet':'Part(c) exponential substitution; common-base(a,b) are supporting prerequisites.'},{'demand_id':FILTER,'assessed_facet':'Retain positive substitution values in(c), and original principal-root domains in(d–f).'}]
ps=[rounded('positive-root','(1+sqrt(61))/10','Rational(88,100)'),rounded('negative-root','(1-sqrt(61))/10','-Rational(68,100)')]
add(2,47,'Solve5x−3/x=1 with x≠0 and give both roots to2dp.',ps,[RECOG,SOLVE,FILTER],components=[opening.QUAD])
p=reasoning('m','m1; the printed key omits this requested parameter.',
 'Substitute given root−3/2 in2x²+mx−3=0:9/2−3m/2−3=0, hence m1. The key lists roots−3/2 and1 but never statesm. Its other-root value1 is correct; only the requested parameter is missing.',591,'key incomplete')
p['additional_operations']={'parameter':{'kind':'identity','operands':['solve(2*(-Rational(3,2))**2+x*(-Rational(3,2))-3,x)[0]']}};p['additional_operation_expected']={'parameter':'1'}
add(3,47,'Given root−3/2 of2x²+mx−3=0, determine m and the other root. The answer key omits m but correctly shows the other root.',[p,v('other-root','(-3/2)/(-Rational(3,2))','1',591,'Withm1, factor(2x+3)(x−1). Product of roots−3/2 divided by given−3/2 also gives1.')],[],components=[opening.QUAD])
add(4,47,'Find k so kx²+(k+2)x=−2 has equal roots; check that the resulting leading coefficient is nonzero.',[
 v('k','solveset((x+2)**2-8*x,x,domain=S.Reals)','FiniteSet(2)',591,'Repeated roots require Δ(k−2)²0. The onlyk2 is nonzero and gives2(x+1)²0. Atk0 the equation is linear with a single root, not equal quadratic roots.')],[CALC,NATURE,'8227:2020:M1:T1:O02:D03'])
ps=[graphs.form('a','-2*x**2+6*x+8','-2*(x-Rational(3,2))**2+Rational(25,2)',591),
 v('b-maximum','(-2*x**2+6*x+8).subs(x,Rational(3,2))','Rational(25,2)',591,'The negative outer coefficient makes the vertex a global maximum; the squared term vanishes atx3/2.'),
 v('b-x','-6/(2*(-2))','Rational(3,2)',591,'The maximum occurs at the independently derived symmetry abscissax3/2.')]
add(5,47,'Complete−2x²+6x+8 in the requested form and state the maximum and attaining x.',ps,[SQUARE,VERTEX])
add(6,47,'Solve2x²≥3x+2, keeping both inclusive exterior intervals.',[base.interval('solution','2*x**2>=3*x+2','Union(Interval(-oo,-Rational(1,2)),Interval(2,oo))',591,'The standard polynomial factors(2x+1)(x−2); it is nonnegative outside the roots.')],[CRIT,INTERVAL])
add(7,47,'Solve4x<x²+3, excluding the two equality endpoints.',[base.interval('solution','4*x<x**2+3','Union(Interval.open(-oo,1),Interval.open(3,oo))',591,'The standard polynomial(x−1)(x−3) is strictly positive outside its roots.')],[CRIT,INTERVAL])
add(8,47,'Sketch y=x²−2x−8 with the requested vertex and both-axis intersections.',[
 graphs.sketch('sketch','x**2-2*x-8',591,['-2','4'],'Tuple(1,-9)','Upward; vertex(1,−9), symmetry axisx1, x-intercepts(−2,0),(4,0), y-intercept(0,−8). All source-key labels agree.')],[SKETCH],sketch=True)
add(9,47,'Use point(0,−3) to find c, then determine axis and vertex by completing the square.',[
 v('c','solve(x+3,x)[0]','-3',591,'Atx0 the graph ordinate equalsc; the supplied point givesc−3.'),graphs.form('completed-form','x**2-2*x-3','(x-1)**2-4',591),
 v('axis','2/2','1',591,'The completed square vanishes atx1; the symmetry line isx1, not a single plotted point.'),graphs.vertex('vertex','x**2-2*x-3','Tuple(1,-4)',591)],[SQUARE,VERTEX],components=[opening.QUAD])
add(10,47,'Determine A,B,C from the supplied cubic identity with a linear factor and constant remainder.',[
 identities.coeff('constants','2*x**3+3*x**2-14*x-5','(a*x+b)*(x+3)*(x+1)+c',['a','b','c'],'Tuple(2,-5,10)',591,'Checker a,b,c correspond to sourceA,B,C.')],[IDENTITY])
add(11,47,'Solve the source quadratic, then use its roots in the affine substitution2y−3 for the connected equation.',[
 roots('a','2*x**2+x-6','FiniteSet(-2,Rational(3,2))','Factor(2x−3)(x+2) and retain both quadratic roots.'),
 roots('b','2*(2*x-3)**2+(2*x-3)-6','FiniteSet(Rational(1,2),Rational(9,4))','Use the preceding roots as2y−3=−2 or3/2; recover y1/2 or9/4, preserving both branches.')],[RECOG,SOLVE,FILTER],components=[opening.QUAD])
p=roots('all-real-roots','x**(-6)-9*x**(-3)+8','FiniteSet(Rational(1,2),1)',
 'Native source shows NEGATIVE exponents y^(−6)−9y^(−3)+8=0, withy≠0. Setu=y^(−3), giving(u−1)(u−8)=0. The real reciprocal-cube map givesy1 or1/2. The printed key is correct; reading positive exponents from the small contact would create a false defect.')
native=W/'checks/r5/textbooks/YM-C1-Exercise12-source-native.png'
p['source_evidence_native']={'path':str(native.relative_to(W.parents[2])),'sha256':hashlib.sha256(native.read_bytes()).hexdigest()}
p['additional_operations']={'original_residuals':{'kind':'identity','operands':['Tuple(1**(-6)-9*1**(-3)+8,Rational(1,2)**(-6)-9*Rational(1,2)**(-3)+8)']}};p['additional_operation_expected']={'original_residuals':'Tuple(0,0)'}
add(12,47,'Solve the reciprocal-power equation y^(−6)−9y^(−3)+8=0. Native enlargement resolves both exponent signs and confirms key1,1/2.',[p],[RECOG,SOLVE,FILTER],components=[opening.QUAD])
add(13,47,'Express6+4x−x² as a−(x+b)² and state its constants; the key’s completed form encodes both.',[
 graphs.form('completed-form','6+4*x-x**2','10-(x-2)**2',591),v('constants','Tuple(6+4, -4/2)','Tuple(10,-2)',591,'Coefficient comparison in a−(x+b)² gives−2b4 and a−b²6, hencea10,b−2.')],[SQUARE])
add(14,48,'Reconstruct the quadratic coefficients from roots±3 and intercept−3.',[
 identities.coeff('coefficients','a*x**2+b*x+c','(x**2-9)/3',['a','b','c'],'Tuple(Rational(1,3),0,-3)',591,'Independently use y=A(x+3)(x−3). The given intercept−3 gives−9A−3, henceA1/3; compare the expanded coefficient vector.')],[RECON])
ps=[v('a-non-real','solve_univariate_inequality((x+3)**2-4*Rational(1,8)*(4*x**2+36)<0,x,relational=False)','Complement(S.Reals,FiniteSet(3))',591,'The fixed quadratic coefficient1/8 never degenerates. Δ=−(k−3)² is negative except atk3.'),
 v('b-real','solve_univariate_inequality((x+3)**2-4*Rational(1,8)*(4*x**2+36)>=0,x,relational=False)','FiniteSet(3)',591,'A negative square can be nonnegative only when it is zero. Thus onlyk3 gives a repeated real root; there is no distinct-real-root parameter.')]
add(15,48,'Classify parameter k for non-real versus real roots of the fixed-leading-coefficient quadratic with discriminant−(k−3)².',ps,[CALC,NATURE,'8227:2020:M1:T1:O02:D03'])
add(16,48,'Find both coordinates where x+2y=10 intersects4y=20+8x−x².',[
 base.system('intersection-pairs',['x+2*y-10','4*y-20-8*x+x**2'],'FiniteSet(Tuple(0,5),Tuple(10,0))',591,'Substitution eliminatesy and givesx(x−10)=0. Recover each associatedy from the original line.')],[PAIR])
add(17,48,'Determine k for two distinct intersections of y=2x+k with the supplied implicit curvex²+y²=20.',[
 v('parameter-range','solve_univariate_inequality((4*x)**2-4*5*(x**2-20)>0,x,relational=False)','Interval.open(-10,10)',591,'Substitution gives5x²+4kx+k²−20=0. Its fixed leading coefficient5 and Δ400−4k² require−10<k<10, excluding tangency at the endpoints. No extra circle theorem is needed.')],[PAIR,CRIT,INTERVAL])
p=identities.coeff('constants','x+8','a*(x+3)+b*(x-2)',['a','b'],'Tuple(2,-1)',591,'Clear the supplied rational identity only forx≠2,−3; checker a,b correspond to sourceA,B. Matching numerator coefficients givesA+B1,3A−2B8.')
p['original_common_domain']='All realx except2 and−3.'
add(18,48,'Determine A,B in the supplied two-linear-denominator identity while preserving both original exclusions.',[p],[IDENTITY])
add(19,48,'Reconstruct and expand the cubic crossing at−1, touching at2 and passing through(−2,32).',[
 v('equation','expand((32/((-2+1)*(-2-2)**2))*(x+1)*(x-2)**2)','-2*x**3+6*x**2-8',591,'UseA(x+1)(x−2)². Atx−2 the product is−16, givingA−2. Expansion is explicitly requested; retain that response form.')],[CUBIC])
p=v('p','solveset(144-4*(1-x)*(-12),x,domain=S.Reals)','FiniteSet(4)',591,
 'Eliminatey=12−px fromx²+xy12, obtaining(1−p)x²+12x−12=0. Forp≠1, tangency requires Δ192−48p0, givingp4. Atp1 the eliminated equation is linear with one intersection but not tangency; curve derivative−12/x²−1 atx1 is−13, whereas the line slope is−1. Forp4 contact(2,4) satisfies both original equations.')
p['additional_operations']={'valid_contact':{'kind':'identity','operands':['Tuple(4+4*2-12,2**2+2*4-12)']},'linear_non_tangent_slope_difference':{'kind':'identity','operands':['(-12/1**2-1)-(-1)']}}
p['additional_operation_expected']={'valid_contact':'Tuple(0,0)','linear_non_tangent_slope_difference':'-12'}
add(20,48,'Find p for tangency between y+px=12 andx²+xy=12. One intersection at the degenerate parameterp1 is not itself evidence of tangency.',[p],[TANGENT])
add(21,48,'Read A as the left root of f(x)=2x²+5x+3, then find the line through A and the given y-interceptB.',[
 v('a-A','Tuple(Min(*solveset(2*x**2+5*x+3,x,domain=S.Reals)),0)','Tuple(-Rational(3,2),0)',591,'Roots−3/2,−1 match the diagram; A is explicitly the left crossing. Its ordinate is0.'),
 v('b-line','(3-0)/(0+Rational(3,2))*x+3','2*x+3',591,'B is the graph’s y-intercept(0,3); A(−3/2,0). The gradient is2, and the line equation follows. Check both original points.')],['8227:2020:M1:T4:O01:D01'],components=[opening.QUAD],rep='graph')
ps=[]
f='a*x**3+b*x**2+c*x+p'
for label,eqs,key,method in [
 ('a',['a/8+b/4+c/2+p','-27*a+9*b-3*c+p','p-30','a+b+c+p+20'],'5*(2*x-1)*(x+3)*(x-2)',
 'The two given roots1/2,−3, intercept30 and point(1,−20) give four independent linear equations for cubic coefficients. Solve that system from the givens; the third root2 is a result, not an input borrowed from the key.'),
 ('b',['8*a+4*b+2*c+p','p+4','a+b+c+p+1','-a+b-c+p+21'],'(x-2)*(2*x**2-3*x+2)',
 'Use root2, intercept−4 and points(1,−1),(−1,−21) to solve all four cubic coefficients. Factoring outx−2 leaves an irreducible real quadratic; no nonreal roots are requested or assessed.')]:
 expr='expand(('+f+').subs(solve(['+','.join(eqs)+'],(a,b,c,p),dict=True)[0]))'
 ps.append(v(label,expr,key,591,method))
add(22,48,'Reconstruct real cubics from sufficient mixed root/point data, using a coefficient system when three real roots are not supplied.',ps,[CUBIC])
fig(80,48,'Exercise21 given parabola and secant','The diagram labels f(x)=2x²+5x+3, its right root−1, left rootA, and y-interceptB3. ThusA(−3/2,0),B(0,3), and the secant has equation2x+3.',['8227:2020:M1:T4:O01:D01'],'graph',[('Tuple(2*(-Rational(3,2))**2+5*(-Rational(3,2))+3,2*0**2+5*0+3)','Tuple(0,3)')],'Exercise-1:21')
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
pages=[]
for page in [47,48]:
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19',
 'non_item_content':'Every Exercise1Q1–22 output recorded; Q1–13start47,Q14–22start48. Basic/intermediate/advanced are source labels, not accepted grade bounds. Native Q12 negative exponents clear a false key-error lead. The givenQ21graph is separately recorded.',
 'scope_screen':'Prescribed transformed equations, quadratic graphs, parameter ranges, identities and cubic reconstruction. Basic common-base and ordinary quadratic work stay supporting where no matchingASoutput is requested. No complex roots are inferred from an unrequested irreducible factor.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-exercise.json',{'scope':'Every Exercise1Q1–22 requested output and native reciprocal-exponent check.','items':answers}),('census-YM-C1-exercise.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete47–48source-page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and p['operation']['kind']!='polynomial-sketch':assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for c in p.get('additional_comparisons',[]):assert equivalent(compute(c['operation']),expression(c['printed_key_normalised'])),(row['item_id'],p['subpart'],'features')
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
