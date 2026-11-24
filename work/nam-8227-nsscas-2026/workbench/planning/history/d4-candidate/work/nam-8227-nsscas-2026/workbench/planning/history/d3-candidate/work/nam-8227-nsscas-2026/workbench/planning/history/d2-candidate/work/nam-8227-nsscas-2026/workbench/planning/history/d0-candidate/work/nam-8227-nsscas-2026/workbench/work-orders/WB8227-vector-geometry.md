# Work order: WB8227-vector-geometry

NSSCAS Mathematics 8227, December 2020 syllabus, Grade 12. PLANNER Codex; owner Vitalis; 23 November 2026. Proposed version **0.1.0**, branch `scalar-combination-and-origin-angle`; owner approval and independent review pending. Design selection `8227:SELECT:D:vector-geometry` narrows accepted C selection `8227:FAMILY:vector-product`. No runtime item, generator or assignment is created.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Target and reuse decision

Use a zero scalar product to solve a scalar-combination perpendicularity condition, then use a scalar product to obtain an angle between two nonzero position vectors at the origin. The two parts share the given vectors but(b) does not depend on the answer to(a). Preserve that distinction; do not invent an a→b follow-through edge. New 8227 recipe reuses existing source/demand/part conventions. No Flashcard Studio cards are converted. This is a deliberately narrow pilot branch, not generic coverage of every vector diagram, unit-vector, ratio or line-equation task.

| Stable part | Direct demands (prefix `8227:2020:`) | Primary objective | Marks | Response |
|---|---|---|---:|---|
| `a` | `M1:T7:O02:D02`, `M1:T7:O02:D03`, `M1:T7:O04:D02`, `M1:T7:O05:D02` | `M1:T7:O05` |3| numeric $p$ with method |
| `b` | `M1:T7:O04:D01`, `M1:T7:O04:D02`, `M1:T7:O05:D01` | `M1:T7:O05` |4| numeric angle with scalar-product method |

Prerequisite `M1:T7:O01:D02`: interpret column-vector notation; NSSCO algebra, square roots and inverse cosine. Supplied coordinate triples are not an assessment of constructing coordinates from a three-dimensional diagram. Addition is not silently counted as a separate directly assessed demand merely because subtraction can be written as addition of a negative. Unit vectors, segment/internal/external division, vector-line geometry, geometric proof and choosing an unspecified plane are outside this branch.

## Native source evidence and grade calibration

| Source | Locator / identity | Design evidence |
|---|---|---|
| Syllabus | `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, PDF12/printed9; SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30` | Vector subtraction/scalar multiplication, magnitude, scalar product, angle and perpendicularity. |
| Question | `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2025/8227-1.pdf`, Q3(a) PDF/printed4 and(b) PDF/printed5; SHA256 `9b8c39c4f0001ff266f943ff0d01d6681ac88f42f2b90dbab162844e858ae816` | Same two-part scaffold: solve $p\overrightarrow{OA}-\overrightarrow{OB}\perp\overrightarrow{OC}$, then scalar-product angle $AOB$. Source3+4marks. |
| Award/report | `Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf`, PDF347/printed345 Q3 |(a) B1 resultant components, M1 dot product set0, A1 parameter; (b) B1 dot, M1 magnitudes, M1FT scalar-product equation, A1 angle. Wrong vector directions give the supplement; degree answers1 dp. Exact source/render hash in `planning/visual-source-reads.json`. |
| Grade calibration | Same syllabus PDF21/printed18 `8227:GRADE:C:07`; PDF20/printed17 `8227:GRADE:A:07`; foundation PDF23/printed20 `8227:GRADE:E:07` | Simple supplied-vector arithmetic/angles, up to 3D scalar-product applications. Numerical domain below is a planner subset, not a grade threshold. |
| Textbook method and variation | YM C5 Examples13/14, TryNow13/16/17, Exercise5 and Revision5; Goldie C10 Example10.9 and Exercise10C/10F | All19 members of `vector-between-directions-angle` and `vector-perpendicularity-parameter` read on exact pages listed in the source-read JSON (YM PDF253–254,258–261,263; Goldie PDF265,268–270,291). Source tasks include acute/obtuse, coordinate sign and varying parameter placement. They are not a licence to add line equations: Goldie10F13(ii) is only the supplied direction/axis-angle subpart. |

Accepted assessed/component union search found89 magnitude/dot and49 angle/perpendicular records (overlap; do not sum); all IDs retained. Only the19 members in the two adopted comparison families were adjudicated on native pages. Other hits are leads, not rejected by absence from the relation ledger. Textbook methods/figures remain internal (`learner_display:false`). Book identities/hashes are in the native-read manifest. Family precision/distinction templates, rejection templates and damaged extracted notes were not used as design evidence.

### Per-branch, per-part examination references (R2-02)

Part(b) has the same direct-demand set and numeric response/method requirement as2025 P1 Q3(b), so its part-scoped learner label is “Same type as NSSCAS Mathematics 8227, 2025 Paper1, Question3(b), page5” (display uses standard spaces). Part(a) is conservatively **related/internal**: the accepted source part’s demand list additionally includes `M1:T7:O02:D01` (addition), while the new criterion evidence directly asks the scalar combination/subtraction. Do not retag accepted item evidence or assert literal equality to get an attractive label. The source still supports the observed method/award pattern. Independently resolve whether the mapping granularity can legitimately match before enabling a same-type label for(a). Full references, applicable local parts and this reason are recorded in `planning/visual-design.json`. A part(b) reference is not a whole-card claim. No family-wide source union is automatically learner-visible.

## Finite domain, constraints and capacity

Supply $\overrightarrow{OA}=\mathbf u=(1,r,1)$, $\overrightarrow{OB}=\mathbf v=(s,1,-1)$, $\overrightarrow{OC}=\mathbf w=(1,t,1)$ with $r,t\in\{1,2,3\}$, $s\in\{-3,-2,-1,1,2,3\}$. Part(a) asks for the scalar $p$ such that $(p\mathbf u-\mathbf v)\cdot\mathbf w=0$. Part(b) explicitly requires a scalar product to find angle $AOB$, in degrees to1 dp.

Canonical formulas: $\mathbf u\cdot\mathbf w=2+rt>0$, $\mathbf v\cdot\mathbf w=s+t-1$, hence $p=(s+t-1)/(2+rt)$. For(b), $\mathbf u\cdot\mathbf v=s+r-1$, $|\mathbf u|=\sqrt{r^2+2}$, $|\mathbf v|=\sqrt{s^2+2}$, so $\theta=\cos^{-1}\![(s+r-1)/\sqrt{(r^2+2)(s^2+2)}]$, $0<\theta<180^\circ$.

All54 tuples are admitted and have54 distinct complete given triples. There is a unique real$p$ since $2+rt\ge3$. All supplied vectors are nonzero. The resultant $p\mathbf u-\mathbf v$ cannot vanish: its third component would give$p=-1$, and its second would then require$-r-1=0$, impossible for$r>0$. Similarly $\mathbf u$ and$\mathbf v$ cannot be parallel. Thus the angle is defined and genuine perpendicularity never relies on the zero vector. The case $p=0$ is admitted; no point$P$, segment placement or internal ratio has been introduced. The right-angle case in(b) is also admitted and must still show the requested method. Negative/zero/positive dot products provide obtuse/right/acute variation, not separate recipe counts.

Domain components have magnitude at most3, below the source’s maximum6; two- or three-term scalar-product arithmetic and fractions remain grade-c/a-compatible, without demanding new geometric interpretation. The resulting $p$ values may be rational or zero. These are proposed illustration bounds needing independent calibration; no claim is made that this covers the hardest vector tasks.

Capacity is $3\times6\times3=54$. Fingerprint recipe/version/branch plus all supplied vectors, angle vertex, response instructions and precision, not only$p$ or$\theta$ (which repeat). App owns per-learner seen/reserved fingerprints, persistence and saved versions. On finite exhaustion return an explicit exhausted state; an authorised domain expansion is versioned and re-reviewed, never silently sampled outside the set. StageE implementation can enumerate constructively with no rejection loop. Invalid cases for any later extension: zero angle vector, collinear vectors when the task assumes a proper triangle, zero $\mathbf u\cdot\mathbf w$ giving no/infinitely many$p$, or a zero resultant called perpendicular without checking geometry.

## Representations and assets — must-read givens (R3-07)

`given_representation: text`, using three labelled column vectors. **Must read:** vector names/directions $OA,OB,OC$, every signed component, origin convention, the difference order in $p\mathbf u-\mathbf v$, the perpendicular target$OC$, and angle vertex$O$ in$AOB$. This source is not a diagram-to-coordinate task. No input figure is necessary; do not add an image merely to count a diagram recipe.

If a schematic solution diagram is later added: fixed origin $O$, labelled rays $OA,OB,OC$ (rays $OA$ and $OC$ coincide when $r=t$), angle arc at $O$, “not to scale”; variable endpoints and ray orientation derive from the exact vectors. Relations: anglearc is between$OA$ and$OB$, not$AO$ and$OB$; perspective may not be used to measure the 3D angle. Labels must not suggest a segment restriction on$p$ or imply the schematic is a planar embedding of all three vectors. No measurement, physical units, photograph or sketch response is required. Main capability need is column-vector/superscript/degree rendering, reliable signed-component reading and method-sensitive marking; owner decision6 does not certify these tests, but no capability hold is imposed.

## Criteria, alternatives, precision and Bloom

Criterion prefix `WB8227-vector-geometry:`. Adapted from2025 Q3 official B/M/A pattern, proposed for the new domain.

| ID | Marks | Evidence and dependencies |
|---|---:|---|
| `a:B1` |B1| Correct $(p-s,rp-1,p+1)$ (or equivalent scalar-product expansion visibly containing correct components). |
| `a:M1` |M1| Compute scalar product with$(1,t,1)$ **and equate it to0**. A dot product with no zero/perpendicular condition is insufficient. |
| `a:A1` |A1| Correct exact$p$, dependent on a valid method. |
| `b:B1` |B1| Correct $s+r-1$ for $OA\cdot OB$, or its sign-reversed value explicitly identified as $AO\cdot OB$, as accepted by the source award table. The requested final angle still requires a supplementary-angle correction if a ray is reversed. |
| `b:M1` |M1| At least one correct magnitude. Reversing a direction does not change its magnitude; genuine magnitude work retains this mark even when the angle direction is later wrong. |
| `b:M2` |M1FT| Correct use of $\mathbf u\cdot\mathbf v=\lvert \mathbf u\rvert \lvert \mathbf v\rvert \cos\theta$ with their coherent quantities; within-part FT only, never an invented dependence on(a). |
| `b:A1` |A1| Correct angle$AOB$ to1 dp in degrees. |

Totals **3+4=7**. No double credit for rearranged versus unrearranged forms of the same equation. Dot-product expansion before collecting coefficients, or bilinearity $p(\mathbf u\cdot\mathbf w)=\mathbf v\cdot\mathbf w$, are valid alternatives. A reversed ray may be used with an explicit supplementary-angle correction; rejecting that correct alternative would be unfair. The cosine rule alone does not satisfy the explicit “use a scalar product” method in(b); it may support independent checking but not substitute for method evidence. Source accepts a radian answer; our new prompt explicitly requests degrees1 dp, so a correct radian intermediate with a final degree conversion is valid, while a radian-only final retains method but loses the requested final-format A1.

Answer-only: no universal automatic zero. An unsupported exact$p$ earns final a:A1 only when the selected memo permits an independent final result; this proposed branch makes a:A1 dependent on valid method, so a bare$p$ earns0/3. Correct bare$\theta$ demonstrates final value but not dot/magnitude/scalar-product method; under this proposed memo b:A1 is dependent on a valid scalar-product path and a bare angle earns0/4. A full mathematical equation that encodes the required method, without prose, can earn all relevant credit. These method dependencies are proposed branch policy, not a claim that every M/A table universally forbids inferred method; independent review must accept or revise them before authoring.

Classification `8227-pilot-design-0.1.0`: (a) Apply3, criteria a:B1/M1/A1 perform a familiar scalar-product zero test and solve a linear scalar equation; (b) Apply3, b:B1/M1/M2/A1 apply the explicitly required formula and angle directions. Whole-card maximum **3**. The problem being3D or having negative values does not make it Analyse. Labels are proposed for this complete branch only and require independent review; a future unspecified geometric deduction could differ.

## Sample marking and feedback

Normal exemplar $\mathbf u=(1,1,1)$, $\mathbf v=(2,1,-1)$, $\mathbf w=(1,2,1)$:

| Submission | Proposed credit | Feedback |
|---|---:|---|
| $4p-3=0$, $p=3/4$; dot2, norms$\sqrt3,\sqrt6$, cosine equation, $61.9^\circ$ |7/7| Both methods and requested results are present; no repair. |
| Correct resultant, writes its dot product$4p-3$ but never sets it0 or solves; complete(b) |5/7| The components are right. Use the perpendicular condition to set that scalar product to zero, then solve for$p$. |
| Uses bilinearity $p(\mathbf u\cdot\mathbf w)=\mathbf v\cdot\mathbf w$, all correct |7/7| Valid equivalent method; do not insist on a separate displayed resultant if the correct expansion is already evident. |
| Correct(a); uses$AO$ instead of$OA$ and returns$118.1^\circ$ without correction, correct norms and formula |6/7| a3; b:B1/M1/M2 earned, b:A1 lost. The required rays start at$O$; reversing one ray gives the supplementary angle. |
| Photo/typed work where a sign or angle unit cannot be read |unresolved| Ask which sign/unit was intended; preserve original submission rather than diagnosing a direction error from uncertain evidence. |

Practice may show a general scalar-product reminder or a different vector example before submission, never the current dot products/parameter/angle. Current full solution and response-specific repairs follow submission. Test has no hints/examples/tutor before submission; preserve marking pauses and post-question review/timing rules. An aided correction and a later after-feedback test attempt remain labelled accordingly, not unaided mastery. App owns progress and assignment behaviour.

## Checks and release limits

All three exemplars below were checked by exact dot-product substitution and an independent Euclidean cosine-law calculation. Inline finite enumeration checked54unique tasks, denominator positivity, nonzero resultants and angle existence. Stage E/F must exhaust these54 tuples, verify all exact/rational/zero $p$ and acute/right/obtuse cases, compare independent angle oracles, test reversed-ray and unit alternatives, and replay seeds0/1/42/$2^{63}-1$ plus exhaustion/reservation/snapshot cases. A clamped cosine must not hide genuinely invalid vectors; tiny floating residuals need a documented tolerance rather than changed mathematics.

Use existing learner-text snapshots pinned by `workbench/playbook/guidelines/provenance.json` (7 November 2026); raw decoded column matrices, minus signs, exact fractions and degree marks require actual render checks, including saved history. Runtime marking, generator replay, learner/teacher safe payloads, actual app timing, installation and production readiness are untested at stage D. Vitalis approves this narrow7 mark branch,54capacity, conservative attribution and proposed criteria/Bloom/exemplars before authoring. No commit or push.
