# Design exemplar: WB8227-vector-geometry

NSSCAS Mathematics 8227, 2020 syllabus; Vitalis; PLANNER Codex; 24 November 2026. **D4 v0.1.4**, branch `scalar-combination-and-origin-angle`; selection `8227:D:SEL:vector-geometry:scalar-combination-and-origin-angle`. Three manual paper cases only; no runtime item/generator. Claude D4 changed-scope confirmation, then owner approval pending.

For every case supply the three labelled column vectors. Ask(a) for$p$ such that$pOA-OB$ is perpendicular to$OC$, accepting an exact value or, if not exact,3sf. Ask(b) for angle$AOB$ using a scalar product, in degrees to1dp unless exact. All named points are distinct in D1. No diagram-to-coordinate task is claimed.

## Normal — positive parameter, acute angle

$OA=(1,1,1)$, $OB=(2,1,-1)$, $OC=(1,2,1)$.

| Action | Reason | Result |
|---|---|---|
| Scale$OA$, then subtract$OB$ | Only$OA$ is multiplied by$p$ | $(p,p,p)-(2,1,-1)$ or$(p-2,p-1,p+1)$. Both forms earn a:B1. |
| Set dot product with$OC$ to zero | The specified vectors must be perpendicular | $(p-2)+2(p-1)+(p+1)=4p-3=0$, so$p=3/4$ (exact0.75 also valid). |
| Find angle quantities | Rays$OA,OB$ begin at$O$ | Dot$=2$; norms$\sqrt3,\sqrt6$. |
| Apply scalar-product angle relation | Dot$=\lVert OA\rVert\lVert OB\rVert\cos\theta$ | $\theta=\cos^{-1}(2/\sqrt{18})=61.874494\ldots^\circ$, so$61.9^\circ$. |

Complete evidence earns **3+4=7/7**. Independent residual: resultant$(-5/4,-1/4,7/4)$ dotted with$(1,2,1)$ is0. Independent cosine law uses$\lVert A-B\rVert^2=5$ and returns$(3+6-5)/(2\sqrt{18})=2/\sqrt{18}$.

Premature norm rounding to1.73 and2.45 gives$61.8^\circ$: retain genuine b:B1/M1/M2, lose b:A1, total **6/7** with correct(a). Feedback asks to retain exact square roots/guard digits until the final angle. This is one of15 frozen D0 rounding-sensitive tuples; nine survive the D1 filter.

## Changed — negative parameter, obtuse angle

$OA=(1,2,1)$, $OB=(-3,1,-1)$, $OC=(1,1,1)$.

| Action | Reason | Result |
|---|---|---|
| Form required difference | Subtract the negative first component correctly | $(p,2p,p)-(-3,1,-1)=(p+3,2p-1,p+1)$. |
| Apply perpendicularity | Dot with$OC$ is zero | $4p+3=0$, hence$p=-3/4$ (exact$-0.75$ accepted). |
| Use required rays | Retain the negative dot product | Dot$=-2$, norms$\sqrt6,\sqrt{11}$. |
| Compute angle | Negative cosine gives an obtuse direction angle | $\theta=\cos^{-1}(-2/\sqrt{66})=104.251755\ldots^\circ$, so$104.3^\circ$. |

**7/7** with full evidence. Resultant$(9/4,-5/2,1/4)$ sums to0. Independent distance$\lVert A-B\rVert^2=21$ gives the same cosine. Premature3sf norms can yield$104.2^\circ$; retain valid methods and lose only the affected final A mark.

## Repaired admitted boundary — exact right angle, distinct points

$OA=(1,2,1)$, $OB=(-1,1,-1)$, $OC=(1,1,1)$; $A\ne C$.

| Action | Reason | Result |
|---|---|---|
| Form difference | Preserve the scalar’s position | $(p+1,2p-1,p+1)$. |
| Apply perpendicularity | Sum components for dot with$OC$ | $4p+1=0$, so$p=-1/4$ (exact$-0.25$ accepted). |
| Compute angle evidence | The requested scalar-product method is still needed | Dot$=-1+2-1=0$; norms$\sqrt6,\sqrt3$; $\cos\theta=0$. |
| State exact angle | No artificial trailing decimal is needed | $\theta=90^\circ$ or$90.0^\circ$. |

**7/7** with the shown method. Resultant$(3/4,-3/2,3/4)$ has dot0 with$OC$. Independent distance$\lVert A-B\rVert^2=9$ gives$(6+3-9)/(2\sqrt{18})=0$. Reversing a ray here still gives a right angle; it is geometric equivalence, not uncredited wrong working.

The old boundary$(3,-2,3)$ is excluded: it has$A=C$ and lets the wrong method$p(OA-OB)$ give canonical$p=0$. All$p=0$ and wrong-method-identity tuples are removed, not passed off as diagnostic practice.

## Concrete marking/feedback probes

For normal:

- Bare$p=0.75$ or bare$61.9^\circ$ gets0 for the respective part under OD-1. Feedback acknowledges the value and asks for the working, without claiming the value is wrong.
- Correct **distributed** scaled-minus setup alone in(a) earns1/3; complete(b) makes **5/7**.
- Undistributed$p(1,r,1)-(s,1,-1)$ alone gives a:B1=0 (with complete(b),4/7). Showing$(p,rp,p)-(s,1,-1)$ gives the official B1.
- Wrong$p(OA-OB)$ gives$p=0$ from its dot-zero equation. A coherent dot-zero method can retain a:M1; a:B1 and a:A1 fail, so complete(b) makes **5/7**. Feedback: scale$OA$ only, then subtract$OB$.
- Correct(a), reversed-ray dot/formula and final$118.1^\circ$ without supplementary correction: source-accepted reverse-dot, norm and method credit remain; b:A1 fails, total **6/7**.
- Misreads$OB$ as$(-2,1,-1)$ and coherently computes$p=-1/4$ and$118.1^\circ$: under OD-6 correct working earns **6/7**: a2/3 after the one MR−1 at a:B1, then b4/4 on the same misread datum without another deduction. Identify the miscopied sign; this is the owner-endorsed comparable Cambridge convention, not a Namibian tariff claim.
- Ambiguous sign, unit, ordering or cancellation remains pending clarification; use first uncancelled coherent attempt when legible, not the most favourable one.

Finite audit54raw →30admitted, with17part(b) pairs and at most17wholly-unseen complete tasks before examples. Every removal, part key and all15 rounding fixtures with kept/filtered status are retained in `planning/d4/visual-domain-checks.json` and `visual-rounding-fixtures.json`. Independent oracle uses exact dot residuals and Euclidean cosine law. Proposed Bloom Apply3/Apply3, whole3, classification `8227-pilot-design-0.1.1`. Runtime input/render/marking, seeds, history and exhaustion tests remain unrun.

D2 precision-form fixtures: non-exact angles for$(3,-1,1)$,$(3,3,1)$,$(3,3,2)$ require$80.0^\circ$,$63.0^\circ$,$63.0^\circ$. Naked$80^\circ$ or$63^\circ$ loses b:A1 despite numeric equality. Exact$60^\circ$/$90^\circ$ remain accepted without a trailing zero. The saved raw answer form, not only its numeric coercion, must be checked in the later app.

D4 ineligible-reuse fixture: in the changed case, misreading $OA=(1,2,1)$ as $(1,-2,1)$ gives $OA\cdot OC=0$ and $OB\cdot OC=-3$, so no $p$ solves the altered question. Eligibility is recorded as false once and remains false in (b). A visible zero-dot attempt earns a:M1 only, 1/3. In (b), the learner's dot is −6, the correct magnitudes are $\sqrt6$ and $\sqrt{11}$, and the resulting angle is $137.6^\circ$. Canonical marking awards only b:M1 and b:M2, 2/4; **total3/7**, with no MR penalty and no MR accuracy follow-through. Own-figure miscopies are ordinary accuracy errors. The later acceptance decision for a more precise angle such as $79.98^\circ$ remains open.

OD-6 sources: NSSCAS 2025 examiner report PDF345 item4 (`CONVENTION:108`) and Cambridge International 9709/12 March2016 mark scheme PDF3, Penalties. The Cambridge convention is comparable-board evidence adopted by Vitalis, not a Namibian published allocation. The per-datum unit, deduction order, eligibility ledger and gross-before-net dependency mechanics are proposed operational rules in MR03, pending approval of the exact manifest; they are not further owner decisions. Practice feedback names the misread.


D4 deferred-deduction fixture: in the normal case, genuinely misread $OB=(-2,1,-1)$ and then use the named wrong resultant $p(OA-OB)$. The visible zero-dot equation gives a:M1 only, 1/3; correct misread-data work in (b) earns all four gross awards. The first A/B earned on this datum is b:B1, so apply the one net MR deduction there: b3/4, **total4/7**, not5/7. The named error is not rescued and the deduction never removes the gross award used by a dependency. Practice feedback names both the miscopied sign and the separate resultant error.
