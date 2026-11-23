"""Selected original 9709 excerpts transcribed against rendered pages by Codex.

These are source-analysis items, not renewable recipes. Text consists of the
original shared stem and selected labelled parts, with mathematics in LaTeX.
Unselected parts are declared, never paraphrased into an 'original'.
"""


def entry(file,page,question,part,marks,text,demands,families,ms_pages,**extra):
    return dict(file=file,pdf_page=page,question=question,part=part,marks=marks,
                verbatim_text=text,demands=demands.split(),family_slugs=families.split(),
                ms_pages=ms_pages,**extra)


ITEMS=[
 entry('9709_w15_qp_11',2,3,None,4,
       r'Solve the equation $\sin^{-1}(4x^4+x^2)=\frac16\pi$.',
       '1.6.4.1 1.1.4.1 1.1.4.2 1.1.4.3','principal-values quadratic-substitution',[4]),
 entry('9709_m16_qp_12',2,4,'a',2,
       r'(a) Solve the equation $\sin^{-1}(3x)=-\frac13\pi$, giving the solution in an exact form.',
       '1.6.4.1 1.6.3.1','principal-values',[4],selected_parts=['a'],omitted_parts=['b']),
 entry('9709_w23_qp_12',3,2,None,2,
       r'Find the exact solution of the equation $\frac16\pi+\tan^{-1}(4x)=-\cos^{-1}(\frac12\sqrt3)$.',
       '1.6.4.1 1.6.3.1','principal-values',[6]),
 entry('9709_s15_qp_13',3,8,None,4,
       r'''The function $f$ is defined by $f(x)=\frac{1}{x+1}+\frac{1}{(x+1)^2}$ for $x>-1$.

(i) Find $f'(x)$.

(ii) State, with a reason, whether $f$ is an increasing function, a decreasing function or neither.''',
       '1.8.2.1 1.8.2.2 1.8.3.2','monotonicity',[5,6],selected_parts=['i','ii'],omitted_parts=['iii'],response_format='explanation'),
 entry('9709_w15_qp_13',2,3,'ii',3,
       r'''(ii) The function $f$, where $f(x)=x^3-3x^2+7x-8$, is defined for $x\in\mathbb R$. Find $f'(x)$ and state, with a reason, whether $f$ is an increasing function, a decreasing function or neither.''',
       '1.8.2.1 1.8.3.2','monotonicity',[4],selected_parts=['ii'],omitted_parts=['i'],response_format='explanation'),
 entry('9709_w16_qp_13',2,4,None,4,
       r'''The function $f$ is such that $f(x)=x^3-3x^2-9x+2$ for $x>n$, where $n$ is an integer. It is given that $f$ is an increasing function. Find the least possible value of $n$.''',
       '1.8.2.1 1.8.3.2 1.1.6.1 1.1.6.2','monotonicity',[4],response_format='numeric'),
 entry('9709_w15_qp_21',2,6,'i',4,
       r'''(i) Find the quotient and remainder when $x^4+x^3+3x^2+12x+6$ is divided by $(x^2-x+4)$.''',
       '2.1.3.2 2.1.3.3','polynomial-division',[5],selected_parts=['i'],omitted_parts=['ii','iii']),
 entry('9709_s16_qp_22',2,2,'i',3,
       r'''(i) Find the quotient and remainder when $2x^3-7x^2-9x+3$ is divided by $x^2-2x+5$.''',
       '2.1.3.2 2.1.3.3','polynomial-division',[4],selected_parts=['i'],omitted_parts=['ii']),
 entry('9709_m20_qp_22',3,2,'a',3,
       r'''(a) Find the quotient when $4x^3+17x^2+9x$ is divided by $x^2+5x+6$, and show that the remainder is $18$.''',
       '2.1.3.2 2.1.3.3','polynomial-division',[6],selected_parts=['a'],omitted_parts=['b'],response_format='proof/show-that'),
 entry('9709_s15_qp_12',3,9,'ii',4,
       r'''Relative to an origin $O$, the position vectors of points $A$ and $B$ are given by $\overrightarrow{OA}=2\mathbf i+4\mathbf j+4\mathbf k$ and $\overrightarrow{OB}=3\mathbf i+\mathbf j+4\mathbf k$.

The point $C$ is such that $\overrightarrow{AB}=\overrightarrow{BC}$.

(ii) Find the unit vector in the direction of $\overrightarrow{OC}$.''',
       '1.7.2.1 1.7.2.3 1.7.3.1 1.7.3.3 1.7.4.1','unit-vector',[6],selected_parts=['ii'],omitted_parts=['i','iii']),
 entry('9709_s17_qp_11',3,2,None,6,
       r'''Relative to an origin $O$, the position vectors of points $A$ and $B$ are given by $\overrightarrow{OA}=\begin{pmatrix}3\\-6\\p\end{pmatrix}$ and $\overrightarrow{OB}=\begin{pmatrix}2\\-6\\-7\end{pmatrix}$, and angle $AOB=90^\circ$.

(i) Find the value of $p$.

The point $C$ is such that $\overrightarrow{OC}=\frac23\overrightarrow{OA}$.

(ii) Find the unit vector in the direction of $\overrightarrow{BC}$.''',
       '1.7.2.1 1.7.2.2 1.7.3.1 1.7.3.2 1.7.4.1 1.7.4.2 1.7.5.2','unit-vector vector-product',[4,5]),
 entry('9709_s18_qp_11',12,7,'ii',3,
       r'''Relative to an origin $O$, the position vectors of the points $A$, $B$ and $C$ are given by $\overrightarrow{OA}=\begin{pmatrix}1\\-3\\2\end{pmatrix}$, $\overrightarrow{OB}=\begin{pmatrix}-1\\3\\5\end{pmatrix}$ and $\overrightarrow{OC}=\begin{pmatrix}3\\1\\-2\end{pmatrix}$.

(ii) The point $M$ is the mid-point of $AC$. Find the unit vector in the direction of $\overrightarrow{OM}$.''',
       '1.7.2.1 1.7.2.2 1.7.3.1 1.7.3.3 1.7.4.1','unit-vector',[11],selected_parts=['ii'],omitted_parts=['i','iii']),
 entry('9709_m16_qp_12',4,9,'a',4,
       r'''(a) In Fig. 1, $OAB$ is a sector of a circle with centre $O$ and radius $r$. $AX$ is the tangent at $A$ to the arc $AB$ and angle $BAX=\alpha$.

(i) Show that angle $AOB=2\alpha$.

(ii) Find the area of the shaded segment in terms of $r$ and $\alpha$.''',
       '1.5.2.2 1.5.2.3','segment-area',[6],selected_parts=['a.i','a.ii'],omitted_parts=['b'],
       diagram_box=[205,70,390,224],diagram_read='Fig. 1: tangent AX, chord AB, equal radii OA and OB; minor segment above AB',
       diagram_variables=['r','alpha'],diagram_constraints=['positive r','0<2alpha<pi','OA=OB=r','AX perpendicular OA','shade sector less triangle']),
 entry('9709_w16_qp_12',2,6,None,8,
       r'''The diagram shows a metal plate $ABCD$ made from two parts. The part $BCD$ is a semicircle. The part $DAB$ is a segment of a circle with centre $O$ and radius $10$ cm. Angle $BOD$ is $1.2$ radians.

(i) Show that the radius of the semicircle is $5.646$ cm, correct to $3$ decimal places.

(ii) Find the perimeter of the metal plate.

(iii) Find the area of the metal plate.''',
       '1.5.2.1 1.5.2.2 1.5.2.3','segment-area circular-symbolic',[6],
       diagram_box=[190,420,450,632],diagram_read='Major segment DAB plus external semicircle BCD; BD is shared internal chord',
       diagram_variables=['circle radius','angle BOD'],diagram_constraints=['positive radius','0<theta<pi','semicircle radius=R*sin(theta/2)','perimeter excludes BD','area includes major segment and semicircle']),
 entry('9709_w22_qp_11',6,5,None,6,
       r'''The diagram shows a sector $OAB$ of a circle with centre $O$. The length of the arc $AB$ is $8$ cm. It is given that the perimeter of the sector is $20$ cm.

(a) Find the perimeter of the shaded segment.

(b) Find the area of the shaded segment.''',
       '1.5.2.1 1.5.2.2 1.5.2.3','segment-area',[9],pdf_pages=[6,7],
       diagram_box=[205,72,395,230],diagram_read='Minor segment cut by chord AB; 8 cm labels the arc, not the chord',
       diagram_variables=['arc length','sector perimeter'],diagram_constraints=['2r+s=P','r>0','0<s/r<pi','shading is sector less triangle']),
 entry('9709_w15_qp_11',4,10,'i',4,
       r'''The diagram shows a cuboid $OABCPQRS$ with a horizontal base $OABC$ in which $AB=6$ cm and $OA=a$ cm, where $a$ is a constant. The height $OP$ of the cuboid is $10$ cm. The point $T$ on $BR$ is such that $BT=8$ cm, and $M$ is the mid-point of $AT$. Unit vectors $\mathbf i$, $\mathbf j$ and $\mathbf k$ are parallel to $OA$, $OC$ and $OP$ respectively.

(i) For the case where $a=2$, find the unit vector in the direction of $\overrightarrow{PM}$.''',
       '1.7.1.1 1.7.2.1 1.7.2.2 1.7.3.1 1.7.3.2 1.7.4.1','unit-vector vector-3d-diagram',[7],selected_parts=['i'],omitted_parts=['ii'],
       diagram_box=[190,70,410,310],diagram_read='Cuboid orientation, T on vertical BR, M midpoint AT; axis directions i,j,k',
       diagram_variables=['a','base width','height','BT'],diagram_constraints=['positive lengths','0<BT<height','M=(A+T)/2','normalize nonzero PM','axis orientation unchanged']),
 entry('9709_w22_qp_12',9,6,'c',3,
       r'''(c) Sketch the graph of $y=4x^2+20x+6$ showing the coordinates of the stationary point. You are not required to indicate where the curve crosses the $x$- and $y$-axes.''',
       '1.1.1.2 1.1.1.3','quadratic-form',[10],selected_parts=['c'],omitted_parts=['a','b'],response_format='sketch'),
 entry('9709_s15_qp_13',4,11,'iii',1,
       r'''In the diagram, $OAB$ is a sector of a circle with centre $O$ and radius $r$. The point $C$ on $OB$ is such that angle $ACO$ is a right angle. Angle $AOB$ is $\alpha$ radians and is such that $AC$ divides the sector into two regions of equal area.

It is given that the solution of the equation in part (i) is $\alpha=0.9477$, correct to $4$ decimal places.

(iii) Find angle $AOB$ in degrees.''',
       '1.5.1.2','angle-units',[7],selected_parts=['iii'],omitted_parts=['i','ii'],response_format='numeric',
       diagram_box=[220,70,390,230],diagram_read='Sector angle AOB is alpha radians; C is the perpendicular foot from A onto OB',
       diagram_variables=['r','alpha'],diagram_constraints=['angle label in radians','OC perpendicular AC','specified alpha supplies conversion input; do not re-solve omitted parts']),
 entry('9709_m16_qp_12',3,7,None,8,
       r'''The diagram shows a pyramid $OABC$ with a horizontal triangular base $OAB$ and vertical height $OC$. Angles $AOB$, $BOC$ and $AOC$ are each right angles. Unit vectors $\mathbf i$, $\mathbf j$ and $\mathbf k$ are parallel to $OA$, $OB$ and $OC$ respectively, with $OA=4$ units, $OB=2.4$ units and $OC=3$ units. The point $P$ on $CA$ is such that $CP=3$ units.

(i) Show that $\overrightarrow{CP}=2.4\mathbf i-1.8\mathbf k$.

(ii) Express $\overrightarrow{OP}$ and $\overrightarrow{BP}$ in terms of $\mathbf i$, $\mathbf j$ and $\mathbf k$.

(iii) Use a scalar product to find angle $BPC$.''',
       '1.7.1.1 1.7.1.2 1.7.2.1 1.7.2.2 1.7.2.3 1.7.3.2 1.7.3.3 1.7.4.1 1.7.4.2 1.7.5.1','vector-3d-diagram vector-product',[5],purpose='variety',
       diagram_box=[195,70,408,240],diagram_read='Right triangular pyramid with P on sloping CA, and O-based orthogonal axes',
       diagram_variables=['OA','OB','OC','CP'],diagram_constraints=['positive lengths','CP<CA','three angles at O right','P computed along CA','vector directions at angle vertex correct']),
 entry('9709_w22_qp_13',7,6,None,5,
       r'''It is given that $\alpha=\cos^{-1}(\frac{8}{17})$. Find, without using the trigonometric functions on your calculator, the exact value of $\frac{1}{\sin\alpha}+\frac{1}{\tan\alpha}$.''',
       '1.6.4.1 2.3.1.1 2.3.2.1 2.3.2.5','principal-values exact-trig-evaluation',[9]),
 entry('9709_s15_qp_11',3,8,'iii',1,
       r'''The function $f:x\mapsto5+3\cos(\frac12x)$ is defined for $0\le x\le2\pi$.

(iii) Explain why $f$ has an inverse.''',
       '1.3.1.3 1.3.3.1','function-analysis',[7],purpose='variety',selected_parts=['iii'],omitted_parts=['i','ii','iv'],response_format='explanation'),
 entry('9709_w21_qp_22',8,6,None,8,
       r'''(a) By sketching a suitable pair of graphs on the same diagram, show that the equation $\ln x=2e^{-x}$ has exactly one root.

(b) Verify by calculation that the root lies between $1.5$ and $1.6$.

(c) Show that if a sequence of values given by the iterative formula $x_{n+1}=e^{2e^{-x_n}}$ converges, then it converges to the root of the equation in part (a).

(d) Use the iterative formula in part (c) to determine the root correct to $3$ significant figures. Give the result of each iteration to $5$ significant figures.''',
       '2.2.2.1 2.2.2.2 2.6.1.1 2.6.1.2 2.6.2.1 2.6.3.1 2.6.3.2 2.6.4.1 2.6.4.2','numerical-method-chain exponential-sketch',[9,10],pdf_pages=[8,9],purpose='variety',response_format='sketch',
       evidence_limit='Conditional convergence is not an assessed failure-to-converge example. Owner candidate Q9(c) is actually Q6(c) on printed page 9; corrected from source.')
]


ITEMS += [
 entry('9709_s22_qp_11',12,7,'a',4,
       r'''The diagram shows the curve with equation $y=(3x-2)^{\frac12}$ and the line $y=\frac12x+1$. The curve and the line intersect at points $A$ and $B$.

(a) Find the coordinates of $A$ and $B$.''',
       '1.4.2.1','line-curve',[13],purpose='variety',selected_parts=['a'],omitted_parts=['b'],
       diagram_box=[140,75,520,257.5],diagram_read='Square-root curve and straight line cross at A and B; common coordinates satisfy both equations',
       diagram_variables=['linear radicand','line gradient and intercept'],diagram_constraints=['radicand nonnegative at both intersections','squared-equation candidates checked in original relation','two distinct admissible intersections']),
 entry('9709_s25_qp_11',8,6,'a',4,
       r'''The equation of a curve is $2x^2-kxy+2=0$ and the equation of a line is $y=px+3$, where $k$ and $p$ are constants.

(a) Given that $k=2$ and $p=11$, find the coordinates of the points of intersection of the curve and the line.''',
       '1.4.2.1','line-curve',[16],purpose='variety',selected_parts=['a'],omitted_parts=['b']),
 entry('9709_s25_qp_12',3,2,None,4,
       r'Find the coordinates of the points of intersection of the curve and the line with equations $2xy+5y^2=24$ and $2x+y+4=0$.',
       '1.4.2.1','line-curve',[10],purpose='variety'),
 entry('9709_w16_qp_22',2,3,'ii',2,
       r'(ii) Sketch the curve $y=4e^{\frac12x}+3$ for $0\le x\le2$.',
       '2.2.2.2','exponential-sketch',[4],purpose='variety',selected_parts=['ii'],omitted_parts=['i','iii'],response_format='sketch'),
 entry('9709_w24_qp_22',6,4,'a',2,
       r'(a) Sketch the graphs of $y=1+e^{2x}$ and $y=|x-4|$ on the same diagram.',
       '2.2.2.2 2.1.2.1','exponential-sketch modulus-sketch',[8],purpose='variety',selected_parts=['a'],omitted_parts=['b','c'],response_format='sketch'),
]

ITEMS += [
 entry('9709_s16_qp_11',3,6,'a',3,
       r'(a) Find the values of the constant $m$ for which the line $y=mx$ is a tangent to the curve $y=2x^2-4x+8$.',
       '1.4.2.2 1.1.2.1 1.1.2.2 1.1.2.3','line-curve root-conditions',[5],selected_parts=['a'],omitted_parts=['b.i','b.ii']),
 entry('9709_w16_qp_12',2,3,'ii',3,
       r'''A curve has equation $y=2x^2-6x+5$.

(ii) Find the value of the constant $k$ for which the line $y=2x+k$ is a tangent to the curve.''',
       '1.4.2.2 1.1.2.1 1.1.2.2 1.1.2.3','line-curve root-conditions',[4],selected_parts=['ii'],omitted_parts=['i']),
 entry('9709_s20_qp_12',7,6,'a',3,
       r'''The equation of a curve is $y=2x^2+kx+k-1$, where $k$ is a constant.

(a) Given that the line $y=2x+3$ is a tangent to the curve, find the value of $k$.''',
       '1.4.2.2 1.1.2.1 1.1.2.2 1.1.2.3','line-curve root-conditions',[9],selected_parts=['a'],omitted_parts=['b']),
]


DIAGRAM_FIXED={
 ('9709_m16_qp_12',9):['circle sector OAB','AX tangent at A','minor segment shaded','radians'],
 ('9709_w16_qp_12',6):['major circular segment DAB joined to semicircle BCD','shared chord BD is internal','radians'],
 ('9709_w22_qp_11',5):['circle sector','shaded minor circular segment','centimetres'],
 ('9709_w15_qp_11',10):['cuboid topology','OABC horizontal','T on vertical BR','M midpoint AT','i,j,k follow OA,OC,OP'],
 ('9709_s15_qp_13',11):['circular sector OAB','right angle ACO','alpha in radians','C lies on OB'],
 ('9709_m16_qp_12',7):['right triangular pyramid','OAB horizontal','OC vertical','orthogonal O-based axes','P lies on CA'],
 ('9709_s22_qp_11',7):['square-root curve and straight line','Cartesian axes','two intersections A and B']
}
for item in ITEMS:
 if item.get('diagram_box'):item['diagram_fixed']=DIAGRAM_FIXED[(item['file'],item['question'])]
