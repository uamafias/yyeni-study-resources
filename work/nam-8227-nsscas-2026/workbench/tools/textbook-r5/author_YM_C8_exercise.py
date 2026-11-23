"""YM400–402: all closing theorem practice and Exercise8, including visual outputs."""
import author_YM_C8_opening as h
import author_YM_C8_graphs as gg
import author_YM_C8_theorems as t
from author_YM_C8_polynomial_division import ev,pair
from author_YM_C8_inequalities import interval
from author_YM_C8_opening import W,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers
FAC=t.FAC;COEFF=t.COEFF;SOLVE=t.SOLVE;REM=t.REM;QR=t.QR;MOD=h.MOD;EQ=h.EQ
DISCR='8227:2020:M1:T1:O02:D02';GRAPH='8227:2020:M1:T1:O01:D03';TRIG='8227:2020:M1:T6:O06:D02';RECIP='8227:2020:M2:T3:O01:D01'
def add(kind,n,page,note,parts,division_request=False):
 r=t.add('Exercise-8'if kind=='Exercise'else kind,n,page,note,parts,division_request)
 r.update(sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),precision_angle_check=dict(source='Exact algebra unless the original explicitly requests2decimal places inExerciseQ15. ExerciseQ18(ii) uses DEGREES on0≤θ≤180.',comparison='Preserve full real root sets, original rational-function exclusions and units. Degree18(ii) must not silently use radians. Basic/Intermediate/Advanced source headings are difficulty guidance, not Bloom levels or exam-style evidence.'))
 return r
def real_only(label,poly,quot,delta,kp):
 p=reasoning(label,'Only one real root; the remaining quadratic has discriminant '+delta+'.','Divide out the established real linear factor. The exact remaining quadratic has negative discriminant and hence no real root. The claim concerns REAL linear factors; over the complex numbers there are further factors. The supplied factor proof must precede this conclusion.',kp,'show/prove')
 p.update(assessed_8227_demand_ids=[DISCR],component_demand_ids=[FAC],response_format='proof/show-that',original_polynomial=poly)
 extra(p,'remaining-quadratic-discriminant','discriminant('+quot+',x)',delta)
 return p
add('Example',25,400,'Showx−2 is a factor ofx³−2x−4, then establish that the remaining quadraticx²+2x+2 has negative discriminant−4. No other REAL linear factor exists.',[t.proof('a','x**3-2*x-4','x-2',400),real_only('b','x**3-2*x-4','x**2+2*x+2','-4',400)])
r=add('Try-Now-25',1,400,'Prove factorx−2 ofx³−x−6 and hence show there is only one real root. The factor proof repeatsExample21; the subsequent negative-discriminant explanation is an explicit extra output.',[t.proof('a','x**3-x-6','x-2',635),real_only('b','x**3-x-6','x**2+2*x+3','-8',635)])
r['source_duplicate_of']=[dict(subparts=['a'],item_id='8227:TB:YM:C8:Example:21',basis='Same polynomial and supplied factor; only the subsequent real-root explanation adds demand.')]
f='2*x**3-15*x**2+33*x-20'
add('Try-Now-25',2,400,'For one connected cubic find remainder−70 at−1, prove factorx−4, and solve all roots1,5/2,4.',[v('a-remainder',f'({f}).subs(x,-1)','-70',635,'Use the original divisorx+1 root−1 in the exact remainder theorem.'),t.proof('b-factor',f,'x-4',635),t.roots('c-roots',f,'FiniteSet(1,Rational(5,2),4)',635)])
answers[-1]['subparts'][0]['assessed_8227_demand_ids']=[REM];answers[-1]['assessed_8227_demand_ids']=sorted(set(answers[-1]['assessed_8227_demand_ids'])|{REM})
def repeated_cubic_parts():
 f='x**3-2*x**2-5*x+6';p=v('a-remainder',f'({f}).subs(x,2)','-4',635,'Substitute the actual divisorx−2 root2. A nonzero remainder does not establish that factor.');p['assessed_8227_demand_ids']=[REM]
 return [p,t.proof('b-i-factor',f,'x+2',635),t.factor('b-ii-other-factors','quo('+f+',x+2,x)','(x-1)*(x-3)',635),t.roots('b-iii-all-roots',f,'FiniteSet(-2,1,3)',635)]
add('Try-Now-25',3,400,'Forx³−2x²−5x+6 find remainder−4 at2, prove the different factorx+2, find the remaining factorsx−1,x−3 and list ALL roots−2,1,3.',repeated_cubic_parts())
ps=[h.scalar('a','Abs(7*(-5)-1)','36',635),h.scalar('b','7-Abs(3*(-5)+10)','2',635),h.scalar('c','Abs(-5+4)+Abs(2*(-5))','11',635)]
add('Exercise',1,401,'Atx−5 evaluate|7x−1|,7−|3x+10| and|x+4|+|2x|. Outside subtraction in(b) is preserved.',ps)
add('Exercise',2,401,'Solve|-6n|30,|x|+12=11 and|x−9|/8=3. The negative target in(b) gives no solution; the last part gives33,−15.',[h.equation('a','Abs(-6*x)-30','FiniteSet(-5,5)',635),h.equation('b','Abs(x)+12-11','S.EmptySet',635),h.equation('c','Abs(x-9)/8-3','FiniteSet(-15,33)',635)])
add('Exercise',3,401,'Three modulus inequalities with exact interval boundaries:−19/4<p<6; x≤−7 orx≥7; −9≤x≤13. Source p in(a) is the checker x.',[interval('a','Abs(5-8*x)<43','Interval.open(-Rational(19,4),6)',635),interval('b','Abs(x)-1>=6','Union(Interval(-oo,-7),Interval(7,oo))',635),interval('c','Abs(7*x-14)<=77','Interval(-9,13)',635)])
add('Exercise',4,401,'Divide the originaly³ byy+2, retaining quotienty²−2y+4 and remainder−8.',pair('answer','x**3','x+2','x**2-2*x+4','-8',635,'y'),True)
add('Exercise',5,401,'Factorise6x³+17x²−5x−6 into REAL linear factors, reconstructing all original coefficients.',[t.factor('factors','6*x**3+17*x**2-5*x-6','(2*x+1)*(3*x-2)*(x+3)',635)])
r=add('Exercise',6,401,'Solve6x³−23x²+16x−3=0, the exact original cubic already solved inExample24. Its repeat is practice, not added structural breadth.',[t.roots('roots','6*x**3-23*x**2+16*x-3','FiniteSet(Rational(1,2),Rational(1,3),3)',635)])
r['source_duplicate_of']='8227:TB:YM:C8:Example:24';r['duplicate_basis']='Identical original cubic equation and requested complete real roots.'
p=v('remainder','(4*x**5+x**3-7*x**2+5).subs(x,-Rational(1,2))','3',635,'For divisor2x+1 use root−1/2 in the ORIGINAL quintic. The remainder theorem applies; do not misclassify this as a requested degree-five long division.');p['assessed_8227_demand_ids']=[REM]
add('Exercise',7,401,'Find the remainder of quintic4x⁵+x³−7x²+5 under nonmonic2x+1 by exact evaluation at−1/2; result3.',[p])
f='2*x**4+x**3-a*x**2+b*x+a+b-1'
add('Exercise',8,401,'Quadraticx²+x−6 has distinct roots2,−3. Both zero conditions on the original quartic givea16,b3; testing only one root cannot prove the entire quadratic factor.',[t.coeff('a-b',f,[f'({f}).subs(x,2)',f'({f}).subs(x,-3)'],['a','b'],'FiniteSet(Tuple(16,3))',635,FAC)])
ps=[gg.graph('a','Abs(x-1)','1','0','FiniteSet(1)','1','-1','1',635),gg.graph('b','Abs(x-4)-3','4','-3','FiniteSet(1,7)','1','-1','1',636),gg.graph('c','-Abs(x-2)-2','2','-2','S.EmptySet','-4','1','-1',636)]
add('Exercise',9,401,'Sketch three modulus functions, explicitly label all intercepts and the vertex. Every actual original graph coefficient is an integer; source solution pictures are not givens.',ps)
answers[-1]['value_level_scope_decisions']=[dict(rule_id='8227:QUAL01',status='within',quoted_value='|x−1|,|x−4|−3,−|x−2|−2',reason='All actual inner, outer and vertical coefficients are integers.')]
p=v('ordered-pairs','FiniteSet(*solve([3*x-2*y-13,x+y-1],(x,y),set=True)[1],*solve([3*x-2*y-13,x+y+1],(x,y),set=True)[1])','FiniteSet(Tuple(3,-2),Tuple(Rational(11,5),-Rational(16,5)))',636,'Split the ORIGINAL |x+y|=1 into x+y=1 or−1. Solve each branch together with3x−2y13, then check the full ordered pairs in both original equations; x/y values cannot be recombined independently.')
p.update(assessed_8227_demand_ids=[EQ],component_demand_ids=['8227:PRIOR:NSSCO:simultaneous-equations'],response_format='symbolic')
add('Exercise',10,401,'Solve one linear and one modulus relation simultaneously: retain paired solutions(3,−2),(11/5,−16/5). The source gives a substitution hint.',[p])
add('Exercise',11,401,'Solve|3x+1|≤2x+3 on the ORIGINAL domain, including the right-hand-side nonnegative condition. Exact result−4/5≤x≤2.',[interval('solution','Abs(3*x+1)<=2*x+3','Interval(-Rational(4,5),2)',636)])
add('Exercise',12,401,'Divide a³ by(a+2)(a+3), a quadratic divisor. Quotienta−5 and remainder19a+30 reconstruct the original; the rational expression excludesa−2,−3.',pair('answer','x**3','(x+2)*(x+3)','x-5','19*x+30',636,'a'),True)
p=t.coeff('a-b-c','2*x**2+3*x-1',['b-2','c-a*b-3','a*c'],['a','b','c'],'FiniteSet(Tuple(0,2,3),Tuple(-Rational(3,2),1,0))',636)
p.update(assessed_8227_demand_ids=['8227:2020:M1:T1:O03:D02'],component_demand_ids=[QR],author_expected_normalised='FiniteSet(Tuple(0,2,3),Tuple(-Rational(3,2),2,0))',original_domain='The rational identity holds forx≠a.',source_interpretation='The second printed tuple hasb1. Coefficient matching forcesb2 in BOTH branches; the original leading coefficient cannot change.')
add('Exercise',13,402,'Find constants in(2x²+3x−1)/(x−a)=bx+c−1/(x−a). Clearing the denominator onx≠a forcesb2,c−2a3,ac0. The second key tuple incorrectly givesb1.',[p])
f='6*x**3+p*x**2-4*p*x+n';p=t.coeff('m-n',f,[f'({f}).subs(x,-Rational(2,3))',f'({f}).subs(x,2)'],['p','n'],'FiniteSet(Tuple(7,-20))',636,FAC);p['source_parameter_names']={'p':'m'}
add('Exercise',14,402,'Given factors3x+2 andx−2 of6x³+mx²−4mx+n, determine m7,n−20. Nonmonic root−2/3 is used exactly.',[p])
p=v('all-k','solveset(x**3+x**2-3*x-2,x,domain=S.Reals)','FiniteSet(-2,(1-sqrt(5))/2,(1+sqrt(5))/2)',636,'Equal remainders underx−k mean k³−3k=2−k². Factor the resulting(k+2)(k²−k−1); retain all THREE real roots and round only the irrational values to the explicitly requested2decimal places.')
p.pop('printed_key_normalised');p.update(author_expected_normalised='FiniteSet(-2,(1-sqrt(5))/2,(1+sqrt(5))/2)',printed_key_approximate_values=['-2','1.62','-0.62'],key_decimal_places=2,assessed_8227_demand_ids=[COEFF],component_demand_ids=[REM],response_format='symbolic',printed_precision_requirement_note='Two decimal places where necessary; exact integer−2 retained.')
add('Exercise',15,402,'Two original polynomials x³−3x and2−x² have equal remainders underx−k. Find ALL k, giving2dp where necessary:−2,1.62,−0.62.',[p])
f='2*x**3+a*x**2-4*x+b';ps=[t.coeff('a-b',f,[f'({f}).subs(x,3)-3',f'({f}).subs(x,-2)+22'],['a','b'],'FiniteSet(Tuple(-5,6))',636),v('hence-remainder','(2*x**3-5*x**2-4*x+6).subs(x,Rational(1,2))','3',636,'Use the SAME coefficient values a−5,b6 in the original polynomial and divisor2x−1 root1/2.')]
ps[-1].update(assessed_8227_demand_ids=[REM],depends_on_source_parts=['a-b'])
add('Exercise',16,402,'First determine a−5,b6 from remainders3 at3 and−22 at−2, then obtain the connected remainder3 under2x−1.',ps)
r=add('Exercise',17,402,'This is the exact repeated multipart cubic fromTry25Q3: remainder at2, factorx+2, other factors, complete root set.',repeated_cubic_parts());r['source_duplicate_of']='8227:TB:YM:C8:Try-Now-25:3';r['duplicate_basis']='Identical original polynomial, subpart structure and outputs.'
f='6*x**3+11*x**2+a*x+a';p=v('a-show-a','solve((6*x**3+11*x**2+a*x+a).subs(x,-2),a)[0]','-4',636,'Use the explicitly supplied factorx+2; evaluate at−2 to obtain−4−a0, hencea−4.');p.update(assessed_8227_demand_ids=[COEFF],component_demand_ids=[FAC],check_mode='show/prove',response_format='proof/show-that')
q=t.factor('b-i-factors','6*x**3+11*x**2-4*x-4','(x+2)*(2*x+1)*(3*x-2)',636)
r=v('b-ii-theta','acos(-Rational(1,2))*180/pi','120',636,'Putu=secθ and use the established factors. Candidate secants−2,−1/2,2/3 yield cosines−1/2,−2,3/2. Only−1/2 is in[−1,1]; on0≤θ≤180degrees cosine is injective, so the COMPLETE admissible answer is120degrees. Exclude90degrees where secant is undefined.')
r.update(assessed_8227_demand_ids=[TRIG],component_demand_ids=[RECIP],response_format='numeric',units='degrees',original_domain='0≤θ≤180degrees;θ≠90degrees.',depends_on_source_parts=['b-i-factors'])
add('Exercise',18,402,'Use a supplied cubic factor to establisha−4, factor the resulting cubic, then solve its secant-transformed equation over0..180DEGREES. Reject transformed roots with impossible cosine values.',[p,q,r])
f='-x*(x+6)/2'
ps=[v('a-x-intercepts','solveset('+f+',x,domain=S.Reals)','FiniteSet(-6,0)',636,'Set the ORIGINAL quadratic equal to0 and report intercept points(−6,0),(0,0).')]
ps[0].update(assessed_8227_demand_ids=['8227:2020:M1:T1:O06:D01'],response_format='symbolic',author_answer_form='(−6,0),(0,0).')
q=reasoning('b-parabola-sketch','Downward parabola with vertex(−3,9/2),x-intercepts−6,0 and y-intercept0.','Complete the square as−(x+3)²/2+9/2. Both roots and its maximum must be explicitly labelled; source key636shows these features.',636,'sketch');q.update(assessed_8227_demand_ids=[GRAPH,'8227:2020:M1:T1:O01:D02'],response_format='sketch');extra(q,'vertex-and-intercept','Tuple(('+f+').subs(x,-3),('+f+').subs(x,0))','Tuple(Rational(9,2),0)');ps.append(q)
q=v('c-k-interval','Interval(0,Rational(9,2))','Interval.open(0,Rational(9,2))',636,'For−x(x+6)=2k, roots are−3±√(9−2k). Distinct real roots requirek<9/2; their negative sum and positive product requirek>0. Endpoints0 (zero root) and9/2 (repeated roots) are excluded.')
q['operation']={'kind':'identity','operands':['Intersection(solve_univariate_inequality(36-8*x>0,x,relational=False),solve_univariate_inequality(2*x>0,x,relational=False))']};q.update(assessed_8227_demand_ids=['8227:2020:M1:T1:O02:D03'],response_format='symbolic',independent_derivation='Forx²+6x+2k=0, discriminant36−8k>0, sum−6<0, product2k>0. These are necessary and sufficient for two unequal negative roots.');extra(q,'original-discriminant','discriminant(x**2+6*x+2*k,x)','36-8*k');ps.append(q)
q=gg.graph('d-modulus-on-shared-axes','Abs(x)','0','0','FiniteSet(0)','0','-1','1',636);q['depends_on_source_parts']=['b-parabola-sketch'];ps.append(q)
q=interval('e-inequality','-x*(x+6)/2>Abs(x)','Interval.open(-4,0)',636);q['depends_on_source_parts']=['b-parabola-sketch','d-modulus-on-shared-axes'];ps.append(q)
r=add('Exercise',19,402,'One connected graph problem:quadratic intercepts,sketch,parameter range for two unequal NEGATIVE roots,overlay|x| on the SAME axes,and hence compare original graph heights. Do not turn its graph cue into extra givens.',ps)
r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL01',status='within',quoted_value='Overlay g(x)=|x| on the quadratic axes.',reason='The original modulus graph has integer coefficient1 and no fractional shifts. The fractional coefficient in the OTHER quadratic is not governed by the modulus coefficient limit.'))
refs=[(53,400,'Example25 real-factor discriminant argument','Divide outx−2 to getx²+2x+2. Its discriminant−4 proves no further real linear factors, not absence of complex factors.',[DISCR],'table','Example:25'),(54,400,'Example25 long/synthetic layouts','Both exact divisions have quotientx²+2x+2 and remainder0. They are alternatives within the same proof.',[FAC],'table','Example:25'),(55,401,'Exercise10 substitution hint','Use the linear equation inside the modulus relation, retaining BOTH ±1 branches and their correlated ordered pairs.',[EQ],'table','Exercise-8:10')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C8:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C8:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Read exact original proof layouts and hint; recompute discriminants, roots and original simultaneous pairs. Source solution/key sketches are checked as responses, not relabelled as problem givens.'
h.pages=[dict(pdf_page=page,printed_page=pp(page),chapter=8,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample25,Try25Q1–3,Exercise8Q1–19 and three actual teaching panels enumerated. Each requested sketch, connected root filter and explicit2dp requirement is retained.',scope_screen='Quintic remainder evaluation is distinguished from actual division; coefficient/parameter branches and reciprocal-trigonometric domains retained.')for page in range(400,403)]
if __name__=='__main__':h.save('exercise','Complete400–402 closing theorem practice and Exercise8 source population; source difficulty labels are not exam-style flags.')
