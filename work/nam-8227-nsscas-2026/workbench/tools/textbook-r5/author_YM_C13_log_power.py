"""YM568: logarithmic and power rearrangements, original domains and starts."""
from author_YM_C13_late_support import *
reset()
f='x-9*exp(-2*x)'
p=a.sketch('a-one-root',['x','9*exp(-2*x)'],'Same axes: increasing line through the origin; positive decreasing exponential through (0,9), tending to zero at positive infinity; one intersection in (1,2).','Original difference derivative 1+18e^(-2x)>0 and limits of opposite sign establish exactly one real root independently of the sketch.',654)
q=a.bracket('b-sign-bracket',f,1,2,'1-9*exp(-2)','2-9*exp(-4)',654,'Original continuous difference has values approximately −0.2180 and +1.8352.');q['depends_on_source_parts']=['a-one-root']
r=reason('c-conditional-fixed-point','A convergent sequence has limit alpha=9e^(-2alpha).','The supplied map is (ln9−ln x)/2 with x>0. At a finite positive limit, rearrange 2alpha=ln9−ln alpha and exponentiate to recover the ORIGINAL equation. This is conditional on convergence, not a formal convergence proof.',654,[RELATE,REARRANGE]);extra(r,'reconstruction','simplify(exp(log(9)-2*x)-9*exp(-2*x))','0')
parts=[p,q,r]+b.sequence_parts('d','(log(9)-log(x))/2','1',['1.0986','1.0516','1.0735','1.0632','1.0680','1.0657'],4,654,f,['1','2'],'1.07',2,'Stem stipulates x1=1; every evaluated state must remain positive for ln x.')
add('Try-Now-5',1,568,'One root of x=9e^(−2x); sketch and sign bracket 1..2; supplied log map, start1, each iterate4dp and final2dp1.07.',parts)
f='3*log(x)-15+x**3'
p=a.sketch('a-one-root',['3*log(x)','15-x**3'],'Domain x>0: logarithm increasing from negative infinity; 15−x³ decreasing, intercept15 and positive-axis crossing cube root15; one intersection in (2,2.5).','The original difference has derivative 3/x+3x²>0 for x>0, and opposite infinite endpoint limits. No logarithm is drawn on x<=0.',654)
q=a.bracket('b-sign-bracket',f,'2','Rational(5,2)','3*log(2)-7','3*log(Rational(5,2))+Rational(5,8)',654,'Original continuous log difference at2 and2.5 is approximately−4.9206,+3.3739.');q['depends_on_source_parts']=['a-one-root']
parts=[p,q]+b.sequence_parts('c','real_root(15-3*log(x),3)','1',['2.46621','2.30785','2.32024','2.31925','2.31933'],5,654,f,['2','Rational(5,2)'],'2.319',3,'No start stipulated; key uses1. This benchmark remains positive. Other suitable starts are permitted; negative intermediate states would make the next logarithm undefined.')
add('Try-Now-5',2,568,'Exactly one positive-domain root of3ln x=15−x³; bracket2..2.5. Supplied cube-root log map; each5dp, final3dp2.319; start open, key chooses1.',parts)
f='x**4-1-x'
p=a.bracket('a-positive-root-bracket',f,1,2,'-1','13',654,'Sign bracket1..2 selects the positive root; the quartic also has a negative root, not requested here.')
q=reason('b-positive-fourth-root','alpha=(1+alpha)^(1/4).','The bracket establishes alpha>0, so the positive fourth-root rearrangement preserves this selected root. The original quartic has another real branch; do not extend this rearrangement to all roots.',654,[REARRANGE,RELATE]);extra(q,'original-reconstruction','expand(x**4-(1+x))',f)
r=val('c-write-recurrence','(1+x)**Rational(1,4)','(1+x)**Rational(1,4)',654,[REARRANGE],'Replace the selected-root equality by the next-state formula x_(n+1)=(1+x_n)^(1/4), with real map domain x_n>=−1 and the selected positive target.');r['depends_on_source_parts']=['b-positive-fourth-root']
parts=[p,q,r]+b.sequence_parts('d','(1+x)**Rational(1,4)','Rational(3,2)',['1.2574','1.2258','1.2214','1.2208'],4,654,f,['1','2'],'1.22',2,'Stem specifies1.5; principal nonnegative fourth root, not an arbitrary real fourth-root sign.')
add('Try-Now-5',3,568,'Quartic x⁴−1−x=0: positive alpha in1..2; show positive fourth-root relation, write recurrence, start1.5, each4dp, root2dp1.22.',parts)
pages=census(568,568,{568:'All Try5Q1–3 and all their explicit sketch, bracket, rearrangement and recurrence responses. No mathematical figure or worked table occurs on this source page; answer graphs remain answer evidence, not GIVEN assets.'})
if __name__=='__main__':save('log-power',pages)
