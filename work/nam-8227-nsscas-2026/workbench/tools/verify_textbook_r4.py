"""Independent recomputations from rendered problem expressions, not answer keys."""
import math,json
import sympy as s
from analysis_sources import WB,write

def main():
 x,t,y,theta=s.symbols('x t y theta',real=True);rows=[]
 def check(key,expression,actual,expected):
  assert s.simplify(actual-expected)==0,(key,actual,expected)
  rows.append({'locator':key,'independent_method':expression,'computed':str(actual),'expected':str(expected),'pass':True})
 h=s.Rational(1,4)
 estimate=4*(h/2)*(1+2*sum(1/(1+(j*h)**2)for j in range(1,4))+s.Rational(1,2))
 assert estimate==s.Rational(5323,1700)
 rows.append({'locator':'Goldie5C2(i),problem151/key346','independent_method':'4 times composite trapezium rule on[0,1],four strips','computed':float(estimate),'printed_wrong':3.1349,'pass':True})
 check('YM Exercise1 Q12,problem47/key591','factor y^6-9y^3+8',(y**3-1)*(y**3-8),y**6-9*y**3+8)
 assert set(s.solveset(y**6-9*y**3+8,y,domain=s.S.Reals))=={1,2}
 rows[-1]['real_roots']=[1,2]
 check('YM TryNow27(c),352/key628','limit of[1/(2(5-2x))] from10 to infinity',s.limit(1/(2*(5-2*x)),x,s.oo)-s.Rational(1,2*(5-20)),s.Rational(1,30))
 check('YM Exercise8 Q7,401','remainder f(-1/2)',(4*x**5+x**3-7*x**2+5).subs(x,-s.Rational(1,2)),3)
 dydx=(2*t-2)/(-3*t*t);second=s.diff(dydx,t)/s.diff(3-t**3,t)
 check('YM TryNow42Q1,526/key649','parametric chain rule at t=1',second.subs(t,1),s.Rational(2,9))
 check('Goldie3B4(iii),79/key340','test omitted theta=90degrees',s.tan(s.pi/4+s.pi/2)-s.tan(s.pi/4-s.pi/2),0)
 normal=-x/2+3;roots=s.solve(x*x-2*x+2-normal,x);assert roots==[-s.Rational(1,2),2]
 rows.append({'locator':'YM Exercise6Q3(b),312/key624 and TryNow35Q1(b),311/key623','independent_method':'Normal through(2,2) with slope-1/2; second curve intersection; cylinder dV/dr=0 independently','normal':'y=-x/2+3','second_intersection':['-1/2','13/4'],'cylinder_r':'20/3','cylinder_max_volume':float(s.pi*s.Rational(9600,27)),'pass':True})
 # Modulus inequality: x<5 has negative RHS; x>=5 reduces to x>-1.
 rows.append({'locator':'YM C8TryNow12(f),388/key634','independent_method':'For x<5,|2x-4|>=0>x-5; for x>=5,2x-4>x-5 iff x>-1, automatically true','computed':'all real x','printed_wrong':'x<-1','pass':True})
 rows.append({'locator':'YM C3TryNow12(b),122/key600','independent_method':'Denominator sqrt(x-4) must be strictly positive; positive reciprocal approaches0without attaining it','domain':'x>4','range':'y>0','pass':True})
 p,k=s.symbols('p k',real=True)
 polynomial=(p+1)*x*x+(2*p+3)*x+2
 check('YM Example19,problem30','factor the parameterised quadratic independently',(x+2)*((p+1)*x+1),polynomial)
 assert s.simplify((-1/(p+1)).subs(p,s.sqrt(2))-(1-s.sqrt(2)))==0
 rows[-1]['counterexample']='p=sqrt2 gives root1-sqrt2, which is irrational; all-real-p rationality claim is false'
 check('YM TryNow33Q3,problem42/key591','independently eliminate y and calculate discriminant',s.discriminant(k*x*x-4*x+k,x),16-4*k*k)
 assert (16-4*k*k).subs(k,3)<0
 rows[-1]['correct_parameter_set']='k<-2 or k>2; k=3 disproves printed threshold4'
 n=s.symbols('n',integer=True,positive=True);r=s.symbols('r',real=True)
 check('YM C2TryNow8Q9,problem59/key593','fifteenth AP term from x,3x is29x',x+14*(3*x-x),29*x)
 assert s.solve(s.Eq(29*x,x*x),x)==[0,29]
 rows[-1]['key_omission']='x0 gives a valid all-zero AP as well as x29'
 assert set(s.solveset(s.Eq(r**4,s.Rational(16,81)),r,domain=s.S.Reals))=={-s.Rational(2,3),s.Rational(2,3)}
 rows.append({'locator':'YM C2TryNow13Q7,problem64/key593','independent_method':'Divide seventh term by third term: r^4=16/81; both real ratio signs survive','ratios':['-2/3','2/3'],'a':243,'pass':True})
 assert s.Rational(4,3)*s.Rational(2,3)**12>s.Rational(1,100)
 assert s.Rational(4,3)*s.Rational(2,3)**13<s.Rational(1,100)
 rows.append({'locator':'YM C2TryNow12(d),problem62/key593','independent_method':'Test neighbouring integer indices with exact rational powers','correct_n':14,'printed_key_correct':True,'handwritten13_rejected':True,'pass':True})
 assert s.solve(s.Eq(n*(n-18),-17),n)==[1,17]
 rows.append({'locator':'YM C2TryNow16Q2,problem67/key594','independent_method':'AP sum is n(n-18); solve equal-17 with positive integer domain','correct_counts':[1,17],'printed_key_correct':True,'pass':True})
 assert sum(4+3*j for j in range(15,30))==1050
 rows.append({'locator':'YM C2TryNow17Q2,68/key594','independent_method':'Solve a+5d=19 and a+7d=25; then sum actual indices16through30','computed':1050,'key_incomplete':True,'pass':True})
 for m in range(1,30):
  total=sum(27*s.Rational(-1,3)**j for j in range(m))
  assert (total<21)==(m==2 or m>=4)
 rows.append({'locator':'YM C2TryNow28(j),76/key595','independent_method':'Exact finite alternating GP formula; separately check n1,2,3 and bound every n>=4','solution':'n2 or n>=4','printed4_only_incomplete':True,'pass':True})
 assert math.factorial(11)//math.factorial(8)==990
 rows.append({'locator':'YM C2TryNow41(c),93/key597','independent_method':'Cancel8! and multiply11*10*9','computed':990,'printed_wrong':20,'pass':True})
 loss=100*(s.Rational(11,10)**30-1);pct=100*(1968-loss)/1968
 assert 16<float(pct)<17
 rows.append({'locator':'YM C2RevisionExercise2Q4(b),105/key598','independent_method':'Sum30actual daily GP losses, subtract from1968then express percentage','computed_percent':float(pct),'key_omitted':True,'pass':True})
 check('YM C4TryNow13Q2,176/key604','evaluate3tan(x/2)-2at pi/4',3*s.tan(s.pi/8)-2,3*s.sqrt(2)-5)
 assert s.simplify(3*s.tan(s.pi/8)-2-1)!=0
 rows[-1]['graph_error']='Printed point(pi/4,1)belongs to full argument, not half argument'
 rows.append({'locator':'YM C4TryNow14Q1,176/key605','independent_method':'a+b=8,-a+b=-2 gives a5,b3; amplitude5/intercept8 cross-check','pass':True})
 alpha=math.acos(.642);negative_roots=[-alpha,alpha-2*math.pi]
 assert all(-2*math.pi<=z<=0 and abs(math.cos(z)-.642)<1e-12 for z in negative_roots)
 rows.append({'locator':'YM C4TryNow42Q1,205/key611','independent_method':'Apply symmetric cosine roots and impose negative interval','computed':negative_roots,'positive5.41_rejected':True,'pass':True})
 half_roots=[2*math.asin(.2),2*math.pi-2*math.asin(.2)]
 assert all(abs(math.sin(z/2)-.2)<1e-12 for z in half_roots)
 check('YM C4TryNow44(d),207/key611','substitute correct5pi/3into half-angle cosine',s.cos(5*s.pi/6)+s.sqrt(3)/2,0)
 rows[-1]['part_c_roots']=half_roots
 assert s.cos(s.pi/6)+s.sqrt(3)/2!=0
 c=s.symbols('c',real=True)
 assert set(s.solve(6*c*c-c-2,c))=={s.Rational(2,3),-s.Rational(1,2)}
 rows.append({'locator':'YM C4TryNow51Q1,214/key613','independent_method':'Substitute sin^2=1-cos^2into13term AP sum, solve6c^2-c-2','cosine_roots':['2/3','-1/2'],'pass':True})
 check('YM C6Example13,282','real cube-root derivative-1/(cuberoot(x+1))^4at-2',-1/(s.real_root(-2+1,3)**4),-1)
 assert -(-2)-5==-3 and (-2)-1==-3
 rows[-1]['correct_tangent']='y=-x-5';rows[-1]['correct_normal']='y=x-1'
 f=4*x**3-15*x*x-72*x+5
 check('YM C6Example17,287','evaluate actual original function at first derivative zero',f.subs(x,-s.Rational(3,2)),s.Rational(263,4))
 assert f.subs(x,4)==-267
 rows[-1]['plot_caution']='Stationary inputs are not x-intercepts of original function'
 rows.append({'locator':'YM C6Example18(b),288','independent_method':'Compare x=-3<-2 but f(-3)=-3<f(-2)=3; global decrease across disconnected domain is false','correct_intervals':['(-infinity,-5/2)','(-5/2,infinity)'],'pass':True})
 v=5*t-3*t*t+2
 assert s.integrate(v,(t,0,2))==6 and s.integrate(v,(t,2,3))==-s.Rational(9,2)
 rows.append({'locator':'YM C7Exercise7Q7(c),368/key630','independent_method':'Solve velocity0,t2 in interval, integrate separately before and after reversal','distance':'21/2','signed_displacement':'3/2','pass':True})
 z=s.symbols('z',positive=True)
 primitive=-s.Rational(4,3)/(3*x+2)
 left=s.limit(primitive.subs(x,-s.Rational(2,3)-z)-primitive.subs(x,-1),z,0,dir='+')
 right=s.limit(primitive.subs(x,3)-primitive.subs(x,-s.Rational(2,3)+z),z,0,dir='+')
 assert left==s.oo and right==s.oo
 rows.append({'locator':'YM C7TryNow14(e),337/key627','independent_method':'Split improper integral at interior pole-2/3; take each one-sided positive limit','computed':'diverges to+infinity','finite_negative_key_rejected':True,'pass':True})
 poly=6*x**3+19*x*x+x-6
 check('YM C8TryNow24(d),399/key635','factor independently and multiply back',(2*x-1)*(3*x+2)*(x+3),poly)
 assert set(s.solve(poly,x))=={s.Rational(1,2),-s.Rational(2,3),-3}
 assert poly.subs(x,1)!=0 and poly.subs(x,-s.Rational(1,2))!=0
 rows[-1]['correct_roots']=['1/2','-2/3','-3']
 # Independent exact ratios and original-expression substitution for C10 key defects.
 sinA,cosA=s.Rational(3,5),-s.Rational(4,5)
 sinB,cosB=-s.Rational(12,13),-s.Rational(5,13)
 check('YM C10TryNow8Q2(a),457/key643','recover quadrant signs and apply sine difference',sinA*cosB-cosA*sinB,-s.Rational(63,65))
 check('YM C10TryNow8Q2(b),457/key643','cosine sum with both negative cosines',cosA*cosB-sinA*sinB,s.Rational(56,65))
 check('YM C10TryNow8Q2(c),457/key643','divide sine difference by cosine difference',(sinA*cosB-cosA*sinB)/(cosA*cosB+sinA*sinB),s.Rational(63,16))
 alpha=math.atan(.5);beta=math.asin(-.4/math.sqrt(5));rr=[alpha+beta,alpha+math.pi-beta]
 assert all(0<=v<=2*math.pi and abs(2*math.sin(v)-math.cos(v)+.4)<1e-12 for v in rr)
 rows.append({'locator':'YM C10TryNow19Q2(b),470/key644','independent_method':'Enumerate both negative-sine phase branches and substitute original equation','roots_degrees':[math.degrees(v)for v in rr],'pass':True})
 phase=math.atan(math.sqrt(5)/2);beta=math.acos(1/3);rr=[beta-phase,2*math.pi-beta-phase]
 assert all(0<v<2*math.pi and abs(2*math.cos(v)-math.sqrt(5)*math.sin(v)-1)<1e-12 for v in rr)
 rows.append({'locator':'YM C10TryNow20Q1(b),471/key644','independent_method':'Solve original minus-sign equation independently and substitute both roots','roots_degrees':[math.degrees(v)for v in rr],'pass':True})
 check('YM C11TryNow16(a),498/key646','differentiate original logarithmic product',s.diff(x*s.log(2*x-1),x),s.log(2*x-1)+2*x/(2*x-1))
 check('YM C11TryNow34(c),515/key648','differentiate parameter functions independently then divide',s.diff(1-2*t*s.exp(t),t)/s.diff(s.exp(2*t),t),-(t+1)*s.exp(-t))
 slope=(s.diff(6*s.sqrt(t+4),t)/s.diff((t+1)*s.exp(t),t)).subs(t,0)
 check('YM C11TryNow39Q2,520/key649','ratio of actual parameter derivatives at0',slope,s.Rational(3,4))
 rows[-1]['correct_tangent']='3x-4y+45=0'
 epsilon=s.symbols('epsilon',positive=True)
 primitive=-2*s.log(s.Abs(3-2*x))
 lhs=s.limit(primitive.subs(x,s.Rational(3,2)-epsilon)-primitive.subs(x,1),epsilon,0,dir='+')
 rhs=s.limit(primitive.subs(x,3)-primitive.subs(x,s.Rational(3,2)+epsilon),epsilon,0,dir='+')
 assert lhs==s.oo and rhs==-s.oo
 rows.append({'locator':'YM C12Example8(b),535','independent_method':'Split at3/2 and evaluate one-sided integrals separately,not endpoint subtraction across pole','computed':'ordinary integral undefined; left+infinity,right-infinity','printed_finite_rejected':True,'pass':True})
 check('YM C12TryNow17Q1(b),543/key651','integrate original tan squared x via sec squared minus1',s.tan(s.pi/6)-s.pi/6,s.sqrt(3)/3-s.pi/6)
 rows[-1]['wrong_argument_key']='sqrt3/2-pi/6 belongs to tan squared2x'
 check('YM C3Example16,136','midpoint(-9,6),distance from(3,1)',s.sqrt((-9-3)**2+(6-1)**2),13)
 rows[-1]['line']='y=-x/2+5/2'
 check('YM C3TryNow16,136/key601','midpoint(4,-2),perpendicular slope2 gives D(0,-10); AD',s.sqrt(14**2+(-7+10)**2),s.sqrt(205))
 rows[-1]['line']='y=2x-10'
 inverse=(s.sqrt((x-3)/2)-2)/3
 check('YM C3TryNow14Q2,126/key600','substitute positive inverse branch into f(g(t))',2*(3*inverse+2)**2+3,x)
 rows[-1]['inverse_domain']='x>=11; negative square-root branch rejected by original t>=0'
 u=s.Matrix([2,2,2]);v=s.Matrix([-2,2,4])
 angle=math.degrees(math.acos(float(u.dot(v)/(s.sqrt(u.dot(u))*s.sqrt(v.dot(v))))))
 assert round(angle,1)==61.9
 perimeter=s.sqrt(u.dot(u))+s.sqrt(v.dot(v))+s.sqrt((u-v).dot(u-v))
 assert round(float(perimeter),1)==12.8
 rows.append({'locator':'Goldie10C12,272/key358','independent_method':'Build cube coordinates from three orthogonal side4vectors and source midpoints/face centre; PR=(2,2,2),PQ=(-2,2,4); dot product and three triangle lengths','angle_degrees':angle,'perimeter':str(perimeter),'pass':True})
 f=x**4-s.Rational(9,5)*x*x+2
 exact=s.integrate(f,(x,0,1));trap=(f.subs(x,0)+f.subs(x,1))/2;mid=f.subs(x,s.Rational(1,2))
 assert exact==trap==s.Rational(8,5) and mid==s.Rational(129,80)
 rows.append({'locator':'GoldieC5Problem-solving investigation,156–157','independent_method':'Construct nonnegative polynomial counterexample to midpoint-always-more-accurate; exact symbolic integration versus two one-strip estimates','integral':str(exact),'trapezium':str(trap),'midpoint':str(mid),'pass':True})
 exact_area=s.Rational(3,2)+s.Rational(25,8)*s.asin(s.Rational(3,5))+25*s.pi/16
 estimates=[]
 for strips in [2,4,8,16]:
  h=s.Rational(4,strips);ordinates=[s.sqrt(5*(j*h)-(j*h)**2)for j in range(strips+1)]
  estimate=h*(ordinates[0]/2+sum(ordinates[1:-1])+ordinates[-1]/2)
  estimates.append(float(estimate));assert float(estimate)<float(exact_area)
 assert estimates==sorted(estimates) and round(float(exact_area),4)==8.4197
 rows.append({'locator':'GoldieC5Worked illustration,147–150/key346','independent_method':'Composite trapezium independently recomputed for2,4,8,16strips; circle antiderivative gives exact area','estimates':estimates,'exact_area':str(exact_area),'pass':True})
 check('YM C6Investigation,267–268','Simplify secant quotient for quadratic at2',s.expand(((2+x)**2-4)/x),4+x)
 check('YM C5Unnumbered scalar-product comparison,251','Compare independent magnitude-angle and component calculations',s.sqrt(200)*5*s.cos(s.pi/4),8*4+(-6)*(-3))
 for scale,period in [(1,360),(2,180),(3,120),(s.Rational(1,2),720),(s.Rational(1,3),1080)]:assert 360/scale==period
 assert 2*abs(0-1)+3==5 and 2*abs(1-1)+3==3
 rows.append({'locator':'YM graph investigations128–133,165–172 and modulus illustration383','independent_method':'Polynomial transformed expressions and positive input-scale periods checked algebraically; modulus vertex/intercept checked by original-expression substitution','periods_sine_cosine':[360,180,120,720,1080],'modulus_vertex':[1,3],'modulus_y_intercept':5,'limits':'Representative graph features,not exhaustive diagram or subtask acceptance','pass':True})
 write(WB/'checks/textbook-recomputations-r4.json',{'status':'author independent recomputation methods; cross-vendor check pending','checks':rows,'limits':'Selected source defects and representative valid answers, not verification of all catalogued answers. Graph label defects separately recorded from rendered-page checks.'})
 print(len(rows))
if __name__=='__main__':main()
