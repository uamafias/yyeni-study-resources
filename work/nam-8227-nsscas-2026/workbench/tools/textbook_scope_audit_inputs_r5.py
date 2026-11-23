"""Final author actual-value annotations, selected explicitly from already-read sources.

These supplement missing qualifier records; they neither infer a decision from a
topic tag nor change the source item's independent direct/component mapping.
"""
PATCHES=[]
def rows(rule, reason, table, status='within'):
    for line in table.strip().splitlines():
        short,value=line.split('|',1)
        PATCHES.append(dict(item_id='8227:TB:'+short, decision=dict(
            rule_id='8227:'+rule,status=status,quoted_value=value,
            reason=reason,author_audit='T5-AUDIT-013; Codex author; independent check pending')))

rows('QUAL06','The actual requested axis is a coordinate axis. Preserve the original region, radius distances and all separately recorded boundary/method cautions; this axis check does not certify the rest of the task.', '''
YM:C7:Example:31|y=x^2; 1<=x<=3; full rotation about x-axis
YM:C7:Try-Now-31:1|y=x^3+1; 0<=x<=3; full rotation about x-axis
YM:C7:Try-Now-31:2|y=4sqrt(x)-x; 0<=x<=16; full rotation about x-axis
YM:C7:Example:32|y=32/(x+4); 4<=x<=12; rotation about x-axis
YM:C7:Try-Now-32:1|y=8/(3x+2); A(0,4), B(2,1); rotation about x-axis
YM:C7:Try-Now-32:2|y=6/(5-2x); 0<=x<=1; rotation about x-axis
YM:C7:Try-Now-32:3|y=x^2+2/x; 1<=x<=2; rotation about x-axis
YM:C7:Example:33|y=x^2+1; 1<=y<=2; rotation about y-axis
YM:C7:Try-Now-33:1|y=x^2+1; point(2,5); rotation about y-axis
YM:C7:Try-Now-33:2|x=8/y^2-2; 1<=y<=2; rotation about y-axis
YM:C7:Example:34|y=sqrt(x+1), y=x+1; left of y-axis; rotation about y-axis
YM:C7:Try-Now-34:1|x+y=5, y=4/x; rotation about x-axis
YM:C7:Try-Now-34:2|intersection(2,13), boundary switch y=5; rotation about y-axis
YM:C7:Try-Now-34:3|inverse-fourth-root curve/chord gap; rotation about x-axis
YM:C7:Try-Now-34:4|y^2=4-x, x+2y=4; separate rotations about x-axis and y-axis
YM:C7:Example:35|y=x+4/x, y=5; 1<=x<=4; rotation about x-axis
YM:C7:Try-Now-35:1|y=x/2+6/x, y=4; 2<=x<=6; rotation about x-axis
YM:C7:Try-Now-35:2|y=sqrt(25-x^2), y=3, A(4,3); rotation about x-axis
YM:C7:Example:36|y^2=r^2-x^2; truncated sphere by rotation about x-axis
YM:C7:Try-Now:36|cone h>0,r>0; full rotation about its coordinate-axis length h
YM:C7:Example:40|root curve and normal PQ; volume of the named region about x-axis
YM:C7:Try-Now:40|y=4/x^2, y=3x+1, y=1; rotation about x-axis
YM:C7:Example:41|root curve, x-axis and x=4; rotation about x-axis; left boundary remains source-ambiguous
YM:C7:Try-Now-41:2|under-curve region corresponding to Try32Q1; rotation about x-axis
YM:C7:Exercise-7:5|y=6/x^2; 1<=x<=2; full rotation about x-axis
YM:C7:Exercise-7:10|specified left-of-axis shaded region; rotation about y-axis
YM:C7:Revision-Exercise-7:3|below-axis quartic region, x>=0; separate volumes about x-axis and y-axis
''')
rows('QUAL04','The actual simple power tail or one-sided endpoint is checked with a finite cutoff inside its original real domain. No principal-value cancellation or general convergence test is imposed.', '''
YM:C7:Try-Now:29|12/sqrt(x^5) on (0,9]; x^(-1/2)+x^(-2) on (0,25]; both diverge as lower cutoff tends to 0+
YM:C7:Example:30|20/(2x+5)^2 on [0,k], k tends to positive infinity
YM:C7:Try-Now-30:1|3/sqrt(2-x) on [0,k], k tends to 2 from below
YM:C7:Try-Now-30:2|1/cuberoot(x) on [p,1], p tends to 0 from above
''')
rows('QUAL03','The actual trig equation uses a small integer/simple-fraction multiplier and a finite stated window. Preserve all original poles, strict endpoints and the actual argument range.', '''
YM:C8:Revision-Exercise-8:4|cotangent substitution; first-quadrant radian interval, multiplier 1
YM:C8:Exercise-8:18|secant-transformed cubic; 0<=theta<=180 degrees, multiplier 1
YM:C12:Revision-Exercise-12:2|bounded alpha equation giving pi-atan(5); no general solutions
YM:C12:Example:18|4sin^2(x)+8sin(x)+3; first positive intersection, P at 7pi/6
YM:C4:Example:54|sin(2theta+pi/3)=1/2; 0<=theta<=pi
YM:C4:Try-Now-55:1|4sin(x)-1; -pi/2<=x<=pi/2; requested axis intercepts
YM:C4:Try-Now-55:2|5-2sin(2x)=6; 0<=x<=pi
YM:C4:Try-Now-55:3|3-4cos^2(x)=1; 0<=x<=pi
''')
rows('QUAL01','The modulus coefficients in the original named modulus curve are integers; the companion quartic is not a modulus coefficient.', '''
YM:C8:Revision-Exercise-8:3|abs(3x)=16-x^4; modulus coefficient 3, shifts 0 and 0
''')
rows('QUAL05','Only the actual ordinary power/finite polynomial integration facet is governed here. Exponents are rational and not -1; reciprocal-linear logarithms and extra preparation remain separate.', '''
Goldie:C8:Exercise-8E:3|three retained finite power-series terms integrate as n=0,1,2; original negative-series preparation remains extra
Goldie:C8:Exercise-8H:2|retained proper rational/linear-power integrals on 8..24; nonlinear extra parts excluded, trig part separately governed
Goldie:C9:Exercise-9C:1|dy/dx=x^2-1, y(3)=2; integration exponents 2 and 0
Goldie:C9:Example:4|dy/dx=3x^2-2; integration exponents 2 and 0
Goldie:C9:Exercise-9B:1|dy/dx=x^2 and sqrt(x); exponents 2 and 1/2; cos(x), exp(x) use separate standard forms
''')
rows('QUAL10','The actual derivative has a constant rational exponent; reverse-use integrals have their own separate method/qualifier records. This does not apply the constant-power rule to a variable exponent.', '''
YM:C7:Example:12|(x^2-5)^(-1); derivative outer exponent -1
YM:C7:Try-Now-12:1|(4-2x^3)^(-1); derivative outer exponent -1
YM:C7:Try-Now-12:2|(2x^2-1)^6; derivative outer exponent 6
YM:C7:Try-Now-12:3|(x^2-4x+5)^6; derivative outer exponent 6
YM:C7:Worked-illustration:2|x^4+3, x^4-7, x^4+50; derivative exponent 4
''')
rows('QUAL08','The actual function is one-to-one on its stated branch. Exchange its original image/domain rather than dropping an open/closed endpoint; reflected logarithms retain their natural half-plane domain.', '''
YM:C9:Exercise-9:14|g(x)=-log_2(x); x>0; inverse input all real
YM:C9:Example:28|exp(x) on R; image (0,infinity)
YM:C9:Try-Now-28:1|2^x on R; image (0,infinity)
YM:C9:Try-Now-28:2|given increasing logarithm and point B; inverse/reflections retain the supplied positive-input graph branch
YM:C9:Try-Now-28:3|base3 logarithm with input/output reflections; input-reflected originals have x<0
YM:C9:Example:29|log_2(x-3); x>3
YM:C9:Try-Now-29:1|ln(x-2), x>2; original composition domains remain
YM:C9:Try-Now-29:2|3^x-2; image (-2,infinity)
YM:C9:Try-Now-29:3|exp(x+1), x>=0; image [e,infinity)
''')
rows('QUAL09','The actual line-curve system reduces to a quadratic at a nondegenerate parameter and tangency requires a repeated root. A degenerating linear equation with one intersection is not automatically tangency.', '''
YM:C1:Example:31|y=2x+k and y^2=4x; repeated root in y
YM:C1:Try-Now-31:1|y=kx+6 and y=x^2+3x+2k
YM:C1:Try-Now-31:2|2y+x=p and y^2+2x=13
YM:C1:Try-Now-31:3|y=2x^2-6x+5 and specified tangent slope
YM:C1:Try-Now-32:4|y=x+2 and y^2+(x+k)^2=2; tangency expressly allowed
YM:C1:Example:38|upward parabola; strict whole-curve positivity and a separate specified tangent line
YM:C1:Try-Now:38|parameter line/fixed quadratic; discriminant at the unique tangent parameter
YM:C1:Exercise-1:20|y+px=12 and x^2+xy=12; p=1 is a degenerate single-intersection case, not a tangent
YM:C3:Example:22|y=x^2-x+3 and y=3x+a; intersection quadratic, tangent a=-1
''')
rows('QUAL07','Use the actual expression and original domain, including attained extrema and open endpoints. These are direct simple real image/domain decisions or explicitly retained source branches, not an added objective; source errors and nonfunction facets stay separately qualified.', '''
Goldie:C2:Prompt:2|log_a(x), a>1; domain x>0; point (1,0)
Goldie:C5:Prompt:2|x^2-2x+3 polynomial versus a rational denominator discontinuity
YM:C3:Example:3|semicircle endpoints x=-4,4; half-open line (-2,-1) to (2,3); third graph endpoints x=-2,3, interior extrema (-1,8),(2,-4)
YM:C3:Try-Now:3|circle radius2 is a relation only; open line (-1,3) to (2,-1); arc endpoints (-2,-1),(4,-2), top (1,2)
YM:C3:Example:4|x-3 for x>7; 7+2x for -2<x<=3; 3x^2-10x+2 on R
YM:C3:Try-Now-4:1|3x-1 for x<2; 4-x for -1<=x<2
YM:C3:Try-Now-4:2|2x-5 for x>=1
YM:C3:Try-Now-4:3|2x^2-8x+5 on R
YM:C3:Try-Now-4:4|x^2 for 0<=x<=2
YM:C3:Example:5|-x^2-8x+7 for -8<=x<2
YM:C3:Try-Now-5:1|(x-2)^2 for -2<=x<=10
YM:C3:Try-Now-5:2|x^2-3x-4 for 0<=x<4
YM:C3:Try-Now-5:3|-3x^2-6x+2 for -2<=x<1
YM:C3:Example:12|(x-3)/(x+3), x!=-3; sqrt(x-5), x>=5
YM:C3:Try-Now:12|x/(x+1), x!=-1; 2/sqrt(x-4), x>4
YM:C3:Example:13|2x^2-8x+10 on [0,2]; inverse input [2,10]
YM:C3:Try-Now-13:2|-x^2+6x-5 on x>=m; m=3 for injectivity, then reset m=5
YM:C3:Try-Now-13:3|x^2-4x+k on x>=p; least injective p=2
YM:C3:Example:14|f=2x+3,x>=0; g=3x^2-12,x<=q; q=-2 then reset q=-3
YM:C3:Try-Now-14:1|f=x^2+1, g=2x+3, both original domains x>0
YM:C3:Try-Now-14:2|f=2x^2+3, g=3x+2, x>=0
YM:C3:Try-Now-14:3|f=8/(x-2)+2, x>2; same rule g on 2<x<4
YM:C3:Try-Now-14:4|2x^2-12x+11, x<=k; k=3 then reset k=1
YM:C3:Example:15|3x-2 on [-1,1]; 4/(5-x) on (1,4]
YM:C3:Try-Now:15|3-x^2 on [0,2]; 3x-7 on [2,4], common value at 2
YM:C3:Try-Now:23|2x^2-12x+7 on R; completed-square range
YM:C3:Revision-Exercise-3:2|f=2x+5 on R; g=8/(x-3), x!=3; inverse excluded input retained
YM:C3:Exercise-3.1:3|2x^2-8x+11 on R; restricted inverse branch x<=2
YM:C3:Exercise-3.1:4|x^2+4x on x>=c; c>=-2; source reset c=0
YM:C9:Example:29|log_2(x-3), x>3
YM:C9:Try-Now-29:1|ln(x-2), x>2; g=x+3; composition admissibility retained
YM:C9:Try-Now-29:2|3^x-2 on R; lower output -2 is excluded
YM:C9:Try-Now-29:3|exp(x+1) on x>=0; lower output e is included
YM:C10:Example:23|2sin(x)+5cos(x) has inner range [-sqrt(29),sqrt(29)]; 2cos(x)-sqrt(3)sin(x) has [-sqrt(7),sqrt(7)]
YM:C10:Try-Now:23|sqrt(3)sin(x)+cos(x) has [-2,2]; 3cos(x)-2sin(x) has [-sqrt(13),sqrt(13)]
YM:C10:Example:24|3sin(theta)+4cos(theta) has [-5,5]; shift2, square and cube
YM:C10:Try-Now:24|5sin(theta)-12cos(theta) has [-13,13]; shift-3, square and cube
YM:C10:Example:25|7+5cos(phi/2)-12sin(phi/2), inner range [-13,13], half-angle period720degrees
YM:C10:Try-Now:25|15cos(theta)-9sin(theta)=3(5cos(theta)-3sin(theta)); range [-3sqrt(34),3sqrt(34)]
YM:C10:Exercise-10:7|5sin(2theta)+2cos(2theta); range [-sqrt(29),sqrt(29)]; reciprocal SQUARE of doubled combination
''')
