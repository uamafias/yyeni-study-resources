# Design exemplar: WB8227-vector-geometry

NSSCAS Mathematics 8227 (2020); owner Vitalis; PLANNER Codex; 23 November 2026; proposed v0.1.0, branch `scalar-combination-and-origin-angle`. Three manual stage D illustrations only; no runtime item/generator. For each, give the three labelled column vectors, ask(a) the scalar$p$ for which $p\overrightarrow{OA}-\overrightarrow{OB}$ is perpendicular to$OC$, then(b) use a scalar product to find angle$AOB$ in degrees to1 dp. All givens are newly authored; see work order for source and mark-pattern evidence.

## Normal — positive parameter, acute angle

$OA=(1,1,1)$, $OB=(2,1,-1)$, $OC=(1,2,1)$.

| Action | Reason | Result |
|---|---|---|
| Form the required difference | Scalar multiplication and subtraction preserve component order | $pOA-OB=(p-2,p-1,p+1)$. |
| Set its dot product with$OC$ to zero | Both nonzero vectors are perpendicular exactly when dot product is0 | $(p-2)+2(p-1)+(p+1)=4p-3=0$, so $p=3/4$. |
| Compute dot and magnitudes for the angle rays | Angle$AOB$ uses$OA$ and$OB$, both starting at$O$ | $OA\cdot OB=2+1-1=2$; $\lvert OA\rvert =\sqrt3$, $\lvert OB\rvert =\sqrt6$. |
| Use scalar-product angle equation | $OA\cdot OB=\lvert OA\rvert \lvert OB\rvert \cos\theta$ | $\cos\theta=2/\sqrt{18}$, so $\theta=61.87449\ldots^\circ=61.9^\circ$. |

All criteria a:B1/M1/A1 and b:B1/M1/M2/A1 earned: **7/7**. Independent check(a): resultant$(-5/4,-1/4,7/4)$ has dot$-5/4-2/4+7/4=0$ with$OC$. Independent check(b): $|A-B|^2=5$, so cosine law gives $(3+6-5)/(2\sqrt{18})=2/\sqrt{18}$, agreeing without invoking the answer-building dot formula twice.

## Changed — negative parameter, obtuse angle

$OA=(1,2,1)$, $OB=(-3,1,-1)$, $OC=(1,1,1)$.

| Action | Reason | Result |
|---|---|---|
| Form the difference | The negative first component of$OB$ must be subtracted correctly | $pOA-OB=(p+3,2p-1,p+1)$. |
| Apply perpendicularity | Dot product with$OC$ is the sum of these components | $4p+3=0$, hence $p=-3/4$. |
| Compute angle quantities | Keep signs; do not take absolute value of the dot product | $OA\cdot OB=-3+2-1=-2$; norms$\sqrt6,\sqrt{11}$. |
| Recover the requested angle | Negative cosine implies an obtuse direction angle | $\theta=\cos^{-1}(-2/\sqrt{66})=104.25175\ldots^\circ=104.3^\circ$. |

All seven marks earned. Independent check(a): resultant$(9/4,-5/2,1/4)$ has sum0. Independent check(b): $|A-B|^2=21$, so cosine law gives $(6+11-21)/(2\sqrt{66})=-2/\sqrt{66}$.

This variation changes the sign decisions in both parameter solving and angle recovery; it is not a new recipe. Using the acute supplement$75.7^\circ$ without a justified conversion is wrong for angle$AOB$.

## Admitted boundary — scalar zero and a right angle

$OA=(1,3,1)$, $OB=(-2,1,-1)$, $OC=(1,3,1)$.

| Action | Reason | Result |
|---|---|---|
| Form required combination |$p$ is a scalar, not a point/segment fraction | $pOA-OB=(p+2,3p-1,p+1)$. |
| Apply perpendicularity | Dot product with$OC$ is zero | $(p+2)+3(3p-1)+(p+1)=11p=0$, so $p=0$. |
| Check nonzero vector | Calling a zero vector perpendicular would be inappropriate geometry | At$p=0$ the combination is$(2,-1,1)$, not zero, and $2-3+1=0$. |
| Use scalar product for the angle | The prescribed method still needs evidence even for an exact right angle | $OA\cdot OB=-2+3-1=0$, norms$\sqrt{11},\sqrt6$; $\cos\theta=0$, giving$90.0^\circ$. |

All seven marks earned. No rule requires$p>0$ or point$P$ between two other points: no such point exists in the question. $A$ and$C$ share a position in this case, which is allowed because only their vector values are supplied and the task does not assert three distinct vertices or a solid. If a later diagram demands distinct$A,C$, exclude$r=t$ and recompute capacity; do not silently impose that geometric condition here. Independent cosine-law check: $|A-B|^2=17$, so $(11+6-17)/(2\sqrt{66})=0$.

## Rejected cases, sample credit and limits

A zero$OA$ or$OB$ would make the requested angle undefined. A later domain with$OA\cdot OC=0$ could produce no or nonunique$p$ and must be screened rather than divided by zero. A point$P=pOA$ lying on a particular segment would introduce an additional geometric condition absent from this branch. No fixed 3D source image should be attached to these values unless generated consistently; the current problem needs text/column vectors only.

Normal-case samples: a correct component vector with its dot expression$4p-3$ but no zero equation or$p$ earns only a:B1 (1/3); correct full(b) makes5/7. A consistent reversed-ray method ending with the supplementary-angle correction can earn7/7. A reversed-ray computation returning$118.1^\circ$ without correction retains the source-accepted reversed-dot B1 and genuine magnitude/formula method marks, but loses the final requested-angle A1; with correct(a),6/7. Bare final values are marked under the explicitly proposed method-evidence rule in the work order, not a universal whole-bank rule. Ambiguous signs/units remain unresolved until clarified.

Inline checks counted54 distinct vector triples, all nonzero required/resultant vectors, positive$2+rt$, and defined cosine ratios. All admitted cases were independently tested by dot residuals and Euclidean distance/cosine law. These are paper design checks, not generator seed tests or reliable image/marking acceptance. Proposed Bloom3/3, whole3, pending independent review and owner design approval.
