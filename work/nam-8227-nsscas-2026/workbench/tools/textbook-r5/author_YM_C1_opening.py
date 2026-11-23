"""Fixed-source YM opening12–21: prerequisites,domains andexact original signs."""
import hashlib,json
import author_Goldie_C8_opening as base
from author_Goldie_C8_opening import W,value,reasoning,fig,figures,compute,expression,equivalent

SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
REPO=W.parents[2];BINOM='8227:2020:M1:T2:O01:D01';EXP='8227:2020:M2:T2:O03:D01'
EXPDEF='8227:2020:M2:T2:O02:D01';QUAD='8227:PRIOR:NSSCO:quadratic';SIMULT='8227:PRIOR:NSSCO:simultaneous-equations'

def ev(page):
    name='YM-C1-keys-586-source'if 586<=page<=589 else f'YM-C1-{12+4*((page-12)//4)}-source'
    p=W/f'checks/r5/textbooks/{name}.png'
    return{'path':str(p.relative_to(REPO)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

base.ev=ev;base.answers.clear();base.new.clear();figures.clear();answers=base.answers;new=base.new

def ym_printed_page(page):
    """Verified scan mapping, including repeated printed127 at PDF138/139."""
    if page>=587:return 'A'+str(page-586)
    if page==139:return 127
    return page-11 if page<=138 else page-12

def add(kind,n,page,note,parts,direct=None,components=None,teaches=None):
    row=base.add(kind,n,page,note,parts,direct or[],components or[],teaches=teaches or[])
    row['item_id']=row['item_id'].replace('Goldie:C8:','YM:C1:');new[-1]['item_id']=row['item_id']
    for p in row['subparts']:
        p['review_date']='2026-11-19';kp=p['answer_pdf_page'];p['answer_printed_page']=ym_printed_page(kp)
    new[-1]['printed_page']=ym_printed_page(page)
    new[-1]['answer_key']['printed_pages']=[ym_printed_page(k)for k in new[-1]['answer_key']['pdf_pages']]
    row['value_level_scope_decisions']=[]
    row['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],
      'limits_considered':[],'qualifier_applicability_note':'Item-specific qualifier decisions require actual source values and are recorded separately. Supporting arithmetic does not establish an assessed demand unless the requested output warrants that link.'}
    row['mapping_rationale']='Distinguish a prescribed binomial output from prerequisite index/surd arithmetic. These common-base exponential solutions do not demonstrate the official use-logarithms method;they support that demand rather than automatically cover it. Real-root and nonzero-denominator conditions are retained.'
    row['precision_angle_check']={'source':'These algebraic answers are exact unless an individual item records a requested approximation. No angle quantities occur in this source segment.',
      'comparison':'Preserve exact radicals,all admissible real roots,andoriginal nonzero denominators. Fractional powers of negative real bases use real odd roots where defined;never silently replace them with principal complex powers.'}
    new[-1].update(scope_check=row['scope_check'],value_level_scope_decisions=[],mapping_rationale=row['mapping_rationale'])
    return row

def v(label,expr,key,kp,method):return value(label,expr,key,kp,method)

def binomial_facet(row,parts):
    row['direct_demand_aspects']=[{'demand_id':BINOM,'assessed_facet':'Only '+','.join(parts)+' explicitly expands a positive-integer square;other index/surd outputs remain prerequisite support.'}]
    row['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'within','quoted_value':'Outer binomial exponent2in '+','.join(parts),
      'reason':'The outer expansion exponent is the positive integer2. Fractional exponents inside its coefficients/terms are not rational-power infinite binomial series.'}]

# Root-basis symbols a,b below stand for explicitly documented real roots of
# the original named parameters. This avoids principal-complex power rewrites.
parts=[v('a','expand((a-5*b)**2)','a**2-10*a*b+25*b**2',14,
 'Let the checker basis a=√(sourcea),b=√(sourceb),withboth original parameters nonnegative. Distribute the original square;return sourcea−10√(sourcea)√(sourceb)+25sourceb. The key is normalised in that same root basis.'),
 v('b','expand((a**2+b)*(a**4-a**2*b+b**2))','a**6+b**3',14,
 'Let checker a be the real cube root of sourcep andbthe real cube root of sourceq. The six distributed terms cancel in pairs,givinga^6+b³=sourcep²+sourceq. This remains valid for negative original parameters under real odd-root conventions.')]
parts[0]['source_root_basis']={'a':'sqrt(original a),original a>=0','b':'sqrt(original b),original b>=0'}
parts[1]['source_root_basis']={'a':'real cube root(original p)','b':'real cube root(original q)'}
row=add('Example',1,14,'Expand a square with square-root terms,andthen a sum-of-cubes factor product with fractional-power notation. The binomial-square facet andprerequisite cubic identity are kept separate.',parts,[BINOM]);binomial_facet(row,['a'])

p1=v('a','expand((2*a-3*b)**2)','4*a**2-12*a*b+9*b**2',587,
 'Use checker a=realcuberoot(originala),b=fourthroot(originalb),withoriginalb≥0. The original square expands to4a²−12ab+9b²in this basis,or4sourcea^(2/3)−12sourcea^(1/3)sourceb^(1/4)+9sourceb^(1/2).')
p1['source_root_basis']={'a':'real cube root(original a)','b':'nonnegative fourth root(original b),original b>=0'}
p2=v('b','expand((a**2-b)*(a**4+a**2*b-b**2))','a**6+b**3',587,
 'The native source has a minus before the finalq^(2/3),not the plus needed for a standard difference-of-cubes factorisation. With a=realcuberoot(p),b=realcuberoot(q),direct distribution givesa^6−2a²b²+b³. The printed keyp²+qomits the mixed term. Do not silently change the source expression to a different intended identity.')
p2['source_root_basis']={'a':'real cube root(original p)','b':'real cube root(original q)'};p2['author_expected_normalised']='a**6-2*a**2*b**2+b**3'
p2['additional_operations']={'source_p1_q1':{'kind':'identity','operands':['(1-1)*(1+1-1)']},'printed_p1_q1':{'kind':'identity','operands':['1**2+1']}}
p2['additional_operation_expected']={'source_p1_q1':'0','printed_p1_q1':'2'}
row=add('Try-Now-1',1,14,'Expand the two original fractional-power expressions. Part(a)is a binomial square;part(b)’s exact printed signs give a mixed term missing from the key. Native source andkey evidence are retained.',[p1,p2],[BINOM]);binomial_facet(row,['a'])

parts=[v('a','solve(Eq(3**x,243),x)[0]','5',14,'243=3^5andthepositive-base exponential is injective,so the exponent is5.'),
 v('b','solveset(1-x**2,x,domain=S.Reals)','FiniteSet(-1,1)',14,'The fixed base6is positive andnot1. Hence6^(1−x²)=1requires1−x²=0;retain both real roots−1and1.'),
 v('c','solve(Eq(12**x,Rational(1,144)),x)[0]','-2',14,'The original2^(2y)3^y=(4·3)^y=12^yand1/144=12^(−2). Positivity of the bases justifies these real exponent laws.')]
add('Example',2,14,'Solve three common-base index equations,including a quadratic exponent with two roots andthe combined base12. These are preparatory exponential-equation structures without a forced log method.',parts,components=[QUAD],teaches=[EXP])
parts=[v('a','solve(Eq(2**x,16),x)[0]','4',587,'Match16with2^4under the injective real exponential.'),
 v('b','solveset(x**2-4,x,domain=S.Reals)','FiniteSet(-2,2)',587,'The original7^(y²−4)=1has exponent0;bothy=−2andy=2satisfy it.'),
 v('c','solve(Eq(75**x,Rational(1,75)),x)[0]','-1',587,'Combine the original5^(2x)3^xas75^xandmatch the reciprocal75^(−1).')]
add('Try-Now-2',1,15,'Solve the original powers-of2,quadratic powers-of7,andcombined-base75equations. Keep both signs in the zero-exponent case.',parts,components=[QUAD],teaches=[EXP])
p=v('exponent-y','solve(Eq(3**x+3**(x+2),90),x)[0]','2',15,
 'Factor the common positive3^y:3^y(1+3²)=90,so3^y=9and y=2. This is an exact factor-before-matching structure,not a numerical logarithm approximation.')
add('Example',3,15,'Solve3^y+3^(y+2)=90by splitting the shifted index andextracting the common exponential factor.',[p],teaches=[EXP])
p=v('a','solve(Eq(2**(x+4)-2**x,120),x)[0]','3',587,'Factor2^x(16−1)=120,so2^x=8andx=3.')
p2=v('b','solveset(x**2-3*x-4,x,domain=S.Reals)','FiniteSet(-1,4)',587,
 'Native source confirms125is raised to n. Thus5^(n²−4)=125^n=5^(3n),givingn²−3n−4=0andn=−1or4. The initially suspected±√7answer came from overlooking that source superscript;it is not a key defect.')
p2['additional_operations']={'original_two_residuals':{'kind':'identity','operands':['Tuple(5**((-1)**2-4)-125**(-1),5**(4**2-4)-125**4)']}}
p2['additional_operation_expected']={'original_two_residuals':'Tuple(0,0)'}
add('Try-Now-3',1,15,'Factor a shifted power-of2difference,andthen solve a power-of5equation with125^nontheother side. Both roots of the second quadratic exponent condition are retained.',[p,p2],components=[QUAD],teaches=[EXP])

system='solve([x+2*y+1,3*x-y-4],(x,y))'
p=v('simultaneous','Tuple('+system+'[x],'+system+'[y])','Tuple(1,-1)',15,
 'The original3^x9^y=1/3givesx+2y=−1. The original8^x/2^(y+1)=8gives3x−y=4. Solve the two linear equations;then substitute both values into both original positive-base equations.')
p['additional_operations']={'original_residuals':{'kind':'identity','operands':['Tuple(3**1*9**(-1)-Rational(1,3),8**1/2**(-1+1)-8)']}};p['additional_operation_expected']={'original_residuals':'Tuple(0,0)'}
add('Example',4,15,'Solve the two simultaneous index equations by rewriting both in their own common positive bases,then solving the resulting linear pair.',[p],components=[SIMULT],teaches=[EXP])

system='solve([4*x-y+7,x+3*y+5],(x,y))'
p=v('a','Tuple('+system+'[x],'+system+'[y])','Tuple(-2,-1)',587,
 '49^(2x)(1/7)^(y−4)=1/343reduces to4x−y=−7. Dividing3^(x+3)by1/(27^y)multiplies by27^y,sox+3y=−5. The original reciprocal division changes the exponent sign;keep the source’s y−4shift.')
p['additional_operations']={'original_a_residuals':{'kind':'identity','operands':['Tuple(49**(2*(-2))*Rational(1,7)**(-1-4)-Rational(1,343),3**(-2+3)/(1/(27**(-1)))-Rational(1,9))']}};p['additional_operation_expected']={'original_a_residuals':'Tuple(0,0)'}
p2=v('b','FiniteSet(*solve([x+5*y,3*x-y+12+4/y],(x,y)))','FiniteSet(Tuple(Rational(5,4),-Rational(1,4)),Tuple(-5,1))',587,
 'The native source has2^(y−12)and1/(16^(1/y));y≠0. Firstx+5y=0. The second gives3x−y+12=−4/y. Substitute x=−5yandmultiply bynonzeroyto get4y²−3y−1=0. Bothy=1and−1/4are allowed,givingx=−5and5/4. Recheck every pair in the original equations.')
p2['additional_operations']={'original_b_residuals':{'kind':'identity','operands':['Tuple(3**Rational(5,4)*243**(-Rational(1,4))-1,8**Rational(5,4)/2**(-Rational(1,4)-12)-16**4,3**(-5)*243**1-1,8**(-5)/2**(1-12)-Rational(1,16))']}}
p2['additional_operation_expected']={'original_b_residuals':'Tuple(0,0,0,0)'}
add('Try-Now-4',1,16,'Solve two simultaneous index systems. The first includes division by a reciprocal;the second includes a reciprocal exponent1/yandgives two admissible pairs. Native source shifts andnonzero-ycondition are explicit.',[p,p2],components=[SIMULT,QUAD],teaches=[EXP])
parts=[v('a','21/(63/21)','7',587,'Fromab=21andab²=63divide the second by the first to obtainb=3,then a=21/3=7. The supplied nonzero ordinates justify division.'),
 v('b','63/21','3',587,'Use the successive exact outputs ofthe same model;the ratio isb=3,not the difference42.'),
 v('p','solve(Eq(7*3**x,189),x)[0]','3',587,'Witha7andb3,the third point requires3^p=27,so p=3. Check allthree original point pairs withone shared model.')]
add('Try-Now-4',2,16,'Determinea,bandpfromthree point constraints on y=ab^x. The first two points fixone model,andthe third determines an unknown input. No graph-gradient linearisation is requested.',parts,teaches=[EXPDEF,EXP])

for kind,n,page,note,rows in [
 ('Example',5,16,'Simplify two positive square roots by extracting maximal square factors.',[
  ('a','sqrt(50)','5*sqrt(2)',16),('b','sqrt(80)','4*sqrt(5)',16)]),
 ('Try-Now-5',1,17,'Simplify four given positive square roots into exact surd form.',[
  ('a','sqrt(20)','2*sqrt(5)',587),('b','sqrt(96)','4*sqrt(6)',587),('c','sqrt(72)','6*sqrt(2)',587),('d','sqrt(325)','5*sqrt(13)',587)]),
 ('Example',6,17,'Combine like surds,keep unlike radicals separate,andextract square factors before combining the final three-root expression.',[
  ('a','8*sqrt(3)-2*sqrt(3)','6*sqrt(3)',17),('b','9*sqrt(6)+2*sqrt(5)-4*sqrt(6)','5*sqrt(6)+2*sqrt(5)',17),('c','sqrt(32)+sqrt(98)-sqrt(162)','2*sqrt(2)',17)]),
 ('Try-Now-6',1,17,'Simplify four signed surd sums,including unlabelled unit coefficients andradicals with extractable square factors.',[
  ('a','6*sqrt(7)-4*sqrt(7)-sqrt(7)','sqrt(7)',587),('b','2*sqrt(11)-3*sqrt(13)+4*sqrt(11)','6*sqrt(11)-3*sqrt(13)',587),('c','sqrt(63)-sqrt(45)+sqrt(252)','9*sqrt(7)-3*sqrt(5)',587),('d','4*sqrt(90)-sqrt(80)+3*sqrt(160)-sqrt(180)','24*sqrt(10)-10*sqrt(5)',587)]),
 ('Example',7,18,'Simplify two radical products andexpand a squared radical binomial. The final square has its mixed term andtwo positive square terms.',[
  ('a','sqrt(8)*sqrt(56)','8*sqrt(7)',18),('b','2*sqrt(54)*3*sqrt(75)','270*sqrt(2)',18),('c','expand((3*sqrt(2)-4*sqrt(6))**2)','114-48*sqrt(3)',18)]),
 ('Try-Now-7',1,18,'Simplify two positive radical products anddistribute a two-binomial radical product withfour signed terms.',[
  ('a','sqrt(14)*sqrt(21)','7*sqrt(6)',587),('b','3*sqrt(11)*4*sqrt(66)','132*sqrt(6)',587),('c','expand((4*sqrt(7)-3*sqrt(5))*(sqrt(7)+2*sqrt(5)))','5*sqrt(35)-2',587)]),
 ('Example',8,20,'Rationalise two single-root denominators,keeping numerator factors andthe final reduced rational coefficient.',[
  ('a','6/sqrt(3)','2*sqrt(3)',20),('b','8*sqrt(3)/(9*sqrt(10))','4*sqrt(30)/45',20)]),
 ('Try-Now-8',1,20,'Rationalise three positive radical denominators,including√32andthe fractional coefficient9/(4√11).',[
  ('a','21/sqrt(7)','3*sqrt(7)',587),('b','4*sqrt(5)/sqrt(32)','sqrt(10)/2',587),('c','9*sqrt(5)/(4*sqrt(11))','9*sqrt(55)/44',587)]),
 ('Example',9,20,'Rationalise two binomial radical denominators by their conjugates. The second original denominator has negative conjugate product−31,so the final signs must be normalised together.',[
  ('a','(5-sqrt(2))/(3+sqrt(2))','(17-8*sqrt(2))/7',20),('b','(8*sqrt(2)-5*sqrt(7))/(4*sqrt(2)-3*sqrt(7))','(41-4*sqrt(14))/31',20)]),
 ('Try-Now-9',1,20,'Rationalise three binomial denominators,including a difference of two irrational terms andmixed radicals in both numerator anddenominator.',[
  ('a','1/(sqrt(3)+sqrt(2))','sqrt(3)-sqrt(2)',587),('b','5/(2*sqrt(3)-1)','(10*sqrt(3)+5)/11',587),('c','(7*sqrt(3)-5*sqrt(2))/(4*sqrt(3)+3*sqrt(2))','(114-41*sqrt(6))/30',587)])]:
    parts=[v(label,expr,key,kp,'Use exact real square roots ofthe positive numeric radicands. Independently distribute/extract square factors ormultiply numerator anddenominator bythe same nonzero conjugate;then simplify andcompare withthe separately transcribed printed key. Keep allsigns andrational coefficients.')for label,expr,key,kp in rows]
    direct=[BINOM]if kind=='Example'and n==7 else[]
    row=add(kind,n,page,note,parts,direct)
    if direct:binomial_facet(row,['c'])

for n,page,label,note,teaches,rep,checks,parent in [
 (1,13,'Power/base/index notation','The source labels2asbase,6asindexand64as2^6. The repeated product has six factors2;this is prerequisite notation,not another asked task.',[],'table',[('2**6','64')],None),
 (2,13,'Index laws and real-domain definitions','Product/quotient/power laws need defined real expressions andnonzero divisors. a^0=1requiresa≠0;the native note correctly lists0^0,0^(−1),0^(−2)as undefined. Real odd roots allow negative radicands;even roots require nonnegative radicands. The inversion identities keep their original nonzero domain.',[],'table',[('(-341**0)','-1'),('7**0','1')],None),
 (3,14,'Binomial-square term diagram','The square gives first square,twice the signed product,last square. The two minus-term factors make a positive final square. The outer exponent is2even when original coefficient notation has fractional exponents.',[BINOM],'diagram',[('expand((a-5*b)**2)','a**2-10*a*b+25*b**2')],'Example:1'),
 (4,14,'Common-base matching reminder','Injectivity of a fixed positive base different from1justifies matching real exponents. A generic instruction to equate quantities after matching indices needs care:an even power is not injective over allreal bases. The source examples use valid positive common bases.',[EXP],'table',[],None),
 (5,15,'Splitting an exponent and factoring','3^(y+2)=3^y·3²,so3^y+3^(y+2)=10·3^y. This retains a common exponential factor,not a spurious sum rulefor exponents.',[EXP],'table',[('simplify(3**y+3**(y+2)-10*3**y)','0')],'Example:3'),
 (6,16,'Surd product/quotient domains','For sourcea>0,b>0,the positive square-root product/quotient identities hold andthe quotient denominator is nonzero. Products also extend to nonnegative radicands;quotients still require the denominator root positive.',[],'table',[],None),
 (7,16,'Rational multiple of an irrational root caution','The note needs a nonzero rational multiplier:0·√2=0is rational. For nonzerorationaln,ifn√awere rational then division bynwouldmake√arational. This is a missing qualification,not a new ASdemand.',[],'table',[('0*sqrt(2)','0')],None),
 (8,17,'Like and unlike radicals','Terms can be collected after their radicands are normalised. Source3√5and−8√5are like;3√2and2√3are unlike. Do not add their radicands.',[],'table',[],None),
 (9,17,'Perfect-square factor extraction reminder','The final Example6sum uses32=16·2,98=49·2,and162=81·2. Allthree roots then share√2;the original third response is(c),despite the worked line’s repeated(b)label.',[],'table',[('Tuple(sqrt(32),sqrt(98),sqrt(162))','Tuple(4*sqrt(2),7*sqrt(2),9*sqrt(2))')],'Example:6'),
 (10,17,'Unasked radical-product illustration','√2·√8=√16=4. This is supporting exposition,not another learner output.',[],'table',[('sqrt(2)*sqrt(8)','4')],None),
 (11,18,'Multiplication coefficient/root separation','6√3·2√5has coefficient12andradical√15. Multiplying only the radicands wouldlose the numeric coefficient.',[],'table',[('6*sqrt(3)*2*sqrt(5)','12*sqrt(15)')],None),
 (12,18,'Prime factors in a radical product','4050=2·3^4·5²allows extraction of3²·5fromits square root. The Example7coefficient6thenproduces270√2.',[],'table',[('2*3**4*5**2','4050')],'Example:7'),
 (13,18,'Unasked radical quotient','8√6/(2√3)=4√2. Divide the rational coefficients andthe nonzero-root factors separately;do not cancel a root against an added term.',[],'table',[('8*sqrt(6)/(2*sqrt(3))','4*sqrt(2)')],None),
 (14,19,'Conjugate table','The paired real binomials are3+√2with3−√2,and4√2−3√7with4√2+3√7. Only the sign between terms changes;each conjugate is nonzero here.',[],'table',[('expand((3+sqrt(2))*(3-sqrt(2)))','7'),('expand((4*sqrt(2)-3*sqrt(7))*(4*sqrt(2)+3*sqrt(7)))','-31')],None),
 (15,19,'Rationalised single-binomial illustration','1/(3+√2)=(3−√2)/7because the conjugate product is7. The denominator is nonzero;this is supporting worked exposition.',[],'table',[('simplify(1/(3+sqrt(2))-(3-sqrt(2))/7)','0')],None),
 (16,19,'Calculator equality check panel','The symbolic forms are exactly equal. The source displays the same truncated decimal0.226540919forboth;the true value is about0.226540919660986. This panel is not a request for a9decimal-place rounded answer.',[],'table',[('simplify(1/(3+sqrt(2))-(3-sqrt(2))/7)','0')],None),
 (17,21,'Quadratic definition','The source explicitly requiresa≠0inax²+bx+c=0. Ifa=0,the equation changes degree;this condition must survive any later parameter variation.',['8227:2020:M1:T1:O02:D02'],'table',[],None),
 (18,21,'Factorisation method for one quadratic','2x²+3x−9=(2x−3)(x+3),withroots3/2and−3. This teaching cell uses one common original equation across allfour methods.',['8227:2020:M1:T1:O02:D02'],'table',[('expand((2*x-3)*(x+3))','2*x**2+3*x-9')],None),
 (19,21,'Quadratic formula method for the same equation','a2,b3,c−9give discriminant81androots(−3±9)/4. These agree withthe factorisation cell;one example is not four distinct problem types.',['8227:2020:M1:T1:O02:D01'],'table',[('3**2-4*2*(-9)','81')],None),
 (20,21,'Completing square method for the same equation','Dividing by2andadding(3/4)²gives(x+3/4)²=81/16,thenx=−3/4±9/4. The corresponding vertex ofthe original function is(−3/4,−81/8).',['8227:2020:M1:T1:O01:D01','8227:2020:M1:T1:O01:D02'],'table',[('expand(2*(x+Rational(3,4))**2-Rational(81,8))','2*x**2+3*x-9')],None),
 (21,21,'Table and graphical root method','The source tablex=−4,−3,−2,−1,0,1,2hasy=11,0,−7,−10,−9,−4,5. The upward parabola hasroots−3,3/2andvertex(−3/4,−81/8). Treat table plotting as a source teaching method;compare with examiner graph-shape conventions before future learner guidance.',['8227:2020:M1:T1:O01:D03'],'graph',[('Tuple(2*(-4)**2+3*(-4)-9,2*(-3)**2+3*(-3)-9,2*(-2)**2+3*(-2)-9,2*(-1)**2+3*(-1)-9,-9,2+3-9,8+6-9)','Tuple(11,0,-7,-10,-9,-4,5)')],None)]:
    fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
    f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
    f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]

notes={12:'Chapter cover andsyllabus-outline bullets;the engineer biography/photo is decorative context,not a calculative given ornew mathematical task.',
 13:'Index notation,alllaw/definition/example rows andthe exponent-inversion reminder are retained in two reference records. Native source clears the apparent zero-power note error:the listed exponents after0are negative.',
 14:'EveryExample1/2andTryNow1response is recorded,withthe binomial-square diagram andcommon-base reminder. Native source confirms the three exact signs inTry1(b);its key omits a mixed term.',
 15:'EveryTryNow2/3,Example3/4response,andthe index-splitting/factor callout is recorded. Native source confirms125^ninTry3(b),so its two-root key iscorrect.',
 16:'BothTryNow4question blocks are separate items. Allpairs/constants checked;source reciprocal exponents andy−12shift retained. Surds definitions/properties,n≠0qualification caution,andExample5responses recorded. The book labels surds enrichment;no automatic AScoverage is claimed.',
 17:'EveryTryNow5/6andExample6response recorded;like/unlike radical distinctions,perfect-square extraction reminder andunasked product illustration have reference records.',
 18:'EveryExample7/TryNow7response recorded. Multiplication,factor-extraction anddivision illustrations have distinct supporting records;onlyExample7(c)is a directly requested binomial square.',
 19:'Rationalisation exposition,conjugate table,difference-of-squares illustration andcalculator equality panel retained as reference records. No separately asked response starts.',
 20:'EveryExample8/9andTryNow8/9response recorded. Conjugate signs andnonzero denominators are kept. Exact key page is587(A1).',
 21:'Nonzero-leading-coefficient definition andallfourmethod cells retained as supporting teaching records forone shared quadratic. The graphical table/curve are checked against the same values. FormalExample10starts22andbelongs to the next segment.'}
pages=[]
for page in range(12,22):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated'if ids else'prose only','item_ids':ids,'continuation_item_ids':[],
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
      'scope_screen':'Allopeningrecap/enrichment tasks andmathematical reference blocks retained withprerequisite/direct roles explicit. No decorative biography is counted as a mathematical figure.'})

if __name__=='__main__':
    for name,data in [('answers-YM-C1-opening.json',{'scope':'EveryExample1–9/TryNow1–9output,withTryNow4questionblocks separate.','items':answers}),
      ('census-YM-C1-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete12–21openingpage census;allrecap/enrichment original responses andteaching blocks recorded.','new_items':new+figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for row in answers:
        for p in row['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;',len(pages),'pages')
