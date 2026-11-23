"""YM581–582: polynomial, parametric-gradient and trapezium-linked examples."""
from author_YM_C13_late_support import *
reset()
DIV='8227:2020:M2:T1:O03:D01';QUOT='8227:2020:M2:T1:O03:D03';FACTOR='8227:2020:M2:T1:O04:D02';PARAM='8227:2020:M2:T4:O03:D02';PARAMG='8227:2020:M2:T4:O03:D03';TRAPSET='8227:2020:M2:T5:O03:D01';TRAPCALC='8227:2020:M2:T5:O03:D02'
poly='x**4-3*x**3+3*x**2-25*x+48'
p=val('a-division','div('+poly+',x-3,x)','Tuple(x**3+3*x-16,0)',581,[DIV,QUOT],'The GIVEN root3 supplies linear factorx−3. Independently divide original quartic; verify reconstruction and zero remainder.');extra(p,'original-reconstruction','expand((x-3)*(x**3+3*x-16))',poly)
q=reason('a-hence-rearrangement','alpha=real cube root(16−3alpha).','The other root alpha is not3; divide original equation byx−3 to getx³+3x−16=0. Cubing/real cube-root inversion is bijective overreals, giving the provided form.',581,[REARRANGE,RELATE],rep='graph');q['depends_on_source_parts']=['a-division']
parts=[p,q]+b.sequence_parts('b','real_root(16-3*x,3)','Rational(3,2)',['2.2572','2.0975','2.1332','2.1253'],4,581,'x**3+3*x-16',['2','Rational(11,5)'],'2.13',2,'Start unspecified; working chooses1.5. Original non3 root is in(0,3); QA bracket2..2.2 independently locates it.')
parts[-1]['verification_bracket_origin']='Author QA bracket for quotient root; source only locates alpha graphically between0and3.'
add('Example',10,581,'Exam-style GIVEN quartic and x-interceptsalpha,3: divide by suitable linear factor, hence supplied cube-root relation, each4dp and root2dp2.13. Start1.5 is one source choice.',parts,'graph')
poly='x**4+2*x**3+2*x**2-12*x-32'
p=val('a-factor-theorem','('+poly+').subs(x,-2)','0',656,[FACTOR],'Evaluate the original polynomial at−2 to obtain0; explicitly invoke factor theorem to justifyx+2. A zero without the theorem link is not the whole requested explanation.')
q=val('b-quotient','div('+poly+',x+2,x)','Tuple(x**3+2*x-16,0)',656,[DIV,QUOT],'Divide the ORIGINAL quartic by its established factorx+2; remainder0 and quotientx³+2x−16.');q['depends_on_source_parts']=['a-factor-theorem'];extra(q,'original-reconstruction','expand((x+2)*(x**3+2*x-16))',poly)
r=val('b-p-and-q','Tuple(16,-2)','Tuple(16,-2)',656,[REARRANGE,RELATE],'For the other, positive root beta, the quotient equation givesx³=16−2x. In the stipulated x=real cube root(p+qx), p16 andq−2. Coefficients come from the independently derived quotient, not a guessed numerical root.');extra(r,'quotient-reconstruction','expand(x**3-(16-2*x))','x**3+2*x-16');r['depends_on_source_parts']=['b-quotient']
parts=[p,q,r]+sequence_sf('c','real_root(16-2*x,3)','2',['2.28943','2.25201','2.25692','2.25627','2.25636'],6,656,'x**3+2*x-16',['2','Rational(5,2)'],'2.256',4,'No stipulated start; source chooses2. Per-state6 SIGNIFICANT FIGURES, final4 SIGNIFICANT FIGURES; preserve positive beta rather than known root−2.')
add('Try-Now',10,581,'Exam-style GIVEN quartic positivebeta and negativealpha: factor theorem at−2, quotient and supplied cube-root coefficientsp16,q−2, then positivebeta4sf2.256, each6sf.',parts,'graph')
p=reason('a-parametric-gradient-relation','p=(p+2)^(1/6)−1/2.','Original x=1/(2t+1)², y=sqrt(t+2). For finite derivative t>−2,t≠−1/2: dx/dt=−4/(2t+1)³,dy/dt=1/(2sqrt(t+2)), hence dy/dx=−(2t+1)³/(8sqrt(t+2)). Gradient−1 implies (2p+1)³=8sqrt(p+2)>0, so p>−1/2. Take REAL cube root to obtain2p+1=2(p+2)^(1/6), and divide2. Genuine parametric geometry, not an explicit-function item.',582,[PARAMG,REARRANGE]);p['component_demand_ids']=[PARAM];extra(p,'parametric-ratio','simplify(diff(sqrt(x+2),x)/diff(1/(2*x+1)**2,x))','-(2*x+1)**3/(8*sqrt(x+2))')
parts=[p]+b.sequence_parts('b','(x+2)**Rational(1,6)-Rational(1,2)','Rational(7,10)',['0.68003','0.67857','0.67847','0.67846'],5,582,'x-(x+2)**Rational(1,6)+Rational(1,2)',['Rational(3,5)','Rational(7,10)'],'0.678',3,'Stem stipulates.7; calculated states arex2..x5. Native solution wrongly labels themx1..x4; values and final root are correct.')
row=add('Example',11,582,'Exam-style parametric gradient−1, provided sixth-root rearrangement, start.7, each5dp and final3dp.678. Source table headings off byone; native cross-reference saysChapter12 though parametric differentiation isChapter11.',parts)
for part in parts[1:]:part['source_index_label_anomaly']='Source headingsx1..x4 correspond to calculatedx2..x5 after given initial.7.'
p=val('a-trapezium','0','Rational(46,25)',656,[TRAPSET,TRAPCALC],'On0..pi/2, TWO intervals giveh=pi/4 and nodes0,pi/4,pi/2. Compute original ordinates sqrt2,sqrt(2−sqrt2/2),1; T=pi/8*(sqrt2+2sqrt(2−sqrt2/2)+1), then round2dp1.84.')
p.update(operation=dict(kind='rounded',operands=['pi*(sqrt(2)+2*sqrt(2-sqrt(2)/2)+1)/8'],decimal_places=2),original_integrand='sqrt(2-sin(x))',original_bounds=['0','pi/2'],trapezium_intervals=2)
extra(p,'independent-trapezium', 'pi*(sqrt(2)+2*sqrt(2-sqrt(2)/2)+1)/8','pi*(sqrt(2)+2*sqrt(2-sqrt(2)/2)+1)/8')
parts=[p]+b.sequence_parts('b','sqrt(2-sin(x))','pi/4',['1.1371','1.0453','1.0653','1.0607','1.0617'],4,656,'x**2+sin(x)-2',['1','Rational(6,5)'],'1.06',2,'Start unspecified; key choosespi/4. Radians; positive square-root and selected first-quadrant intersection P.')
parts[-1]['verification_bracket_origin']='Author QA bracket1..1.2 for original first-quadrant intersection; not a source-stated bracket.'
add('Try-Now',11,582,'Exam-style GIVEN sqrt(2−sinx),0..pi/2: trapezium with2intervals,2dp1.84; separately use supplied map for liney=x intersection, each4dp and root2dp1.06. No inference of a common assessment demand from the shared curve.',parts,'graph')
for r in answers:r.update(exam_style=True,exam_style_basis='Explicit source section13.4 Exam-Style Questions; this is textbook-derived examination style, not evidence of NSSCAS exam occurrence.')
refs=[
 (69,581,'Example10 GIVEN quartic root diagram','Original quartic has rootsalpha and3, alpha positive<3. Linear factor3 supports division; diagram not a requested sketch.',[DIV,REARRANGE],'graph','Example:10',True),
 (70,581,'Example10 synthetic division working','Original coefficients1,−3,3,−25,48 divide by3 to quotient1,0,3,−16 and remainder0.',[DIV,QUOT],'table','Example:10',False),
 (71,581,'Example10 recurrence table','Chosen1.5 then2.2572,2.0975,2.1332,2.1253; last two round2.13.',[ITERATE,STOP],'table','Example:10',False),
 (72,581,'Try10 GIVEN quartic root diagram','Negative rootalpha−2 and positivebeta; target ofiteration isbeta.',[FACTOR,REARRANGE],'graph','Try-Now:10',True),
 (73,582,'Example11 parametric derivative working','Source original parameters and ratio checked on t>−2,t≠−.5. Gradient−1 forcesp>−.5 and correct even-root branch.',[PARAMG,REARRANGE],'table','Example:11',False),
 (74,582,'Example11 off-by-one iteration headings','Given initial.7; native headingsx1..x4 displaycalculatedx2..x5. Numeric values and final.678are correct.',[ITERATE,STOP],'table','Example:11',False),
 (75,582,'Try11 GIVEN square-root trigonometric curve','sqrt(2−sinx),0..pi/2; positive, decreasing, endpoints sqrt2 and1. Nodes determine trapezium estimate; liney=x introduced only inb.',[TRAPSET],'graph','Try-Now:11',True)]
for args in refs:panel(*args)
pages=census(581,582,{581:'Both full exam-style polynomial questions, GIVEN quartic diagrams, division and recurrence panels. Six-significant-figure instruction distinguished from decimal places.',582:'All parametric Example11 and trapezium/intersection Try11 parts, GIVEN graph, parametric working and iteration table. Native table index defect retained without changing valid numbers.'})
if __name__=='__main__':save('examstyle',pages)
