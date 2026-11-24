# Implicit differentiation: revised gradient and show-that/normal exemplars

NSSCAS Mathematics 8227, NIED December 2020 syllabus; Grade 12. Owner Vitalis; PLANNER Codex, 24 November 2026. Proposed version **0.1.4**, classification `8227-pilot-design-0.1.1`. Newly authored stage-D paper illustrations, not runtime items. Claude's D4 changed-scope confirmation and then Vitalis's approval are pending. Source qualifiers and shared D1-MR01–09 rules are bound by the matching work order. Textbook originals remain internal.

## gradient: normal — `WB8227-implicit-normal:gradient:normal`

**Question.** A curve has equation $3e^{2x}y+y^2=4$ and the point $P=(0,-4)$ lies on it. Find its gradient at P, showing all working. Give an exact value or a correctly rounded three-significant-figure decimal. [5]

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor2 | $6e^{2x}y+3e^{2x}y'$ |
| Differentiate y² and the constant | y depends on x, while 4 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(3e^{2x}+2y)y'=-6e^{2x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{6 y e^{2 x}}{2 y + 3 e^{2 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-6(-4)}{3+2(-4)}=- \frac{24}{5}$ |

**Marking:** G1 M1 product attempt with its two contributions, G2 A1 correct product result, G3 B1 y²/constant derivatives, G4 M1 substitute the point, G5 A1 www canonical gradient after correct derivative working: **5/5**. Copying only the correct gradient earns **0/5** under OD-1; feedback acknowledges its correctness and requests the derivative/substitution steps.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## gradient: changed — `WB8227-implicit-normal:gradient:changed`

**Question.** A curve has equation $3e^{3x}y+y^2=-2$ and the point $P=(0,-1)$ lies on it. Find its gradient at P, showing all working. Give an exact value or a correctly rounded three-significant-figure decimal. [5]

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor3 | $9e^{3x}y+3e^{3x}y'$ |
| Differentiate y² and the constant | y depends on x, while -2 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(3e^{3x}+2y)y'=-9e^{3x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{9 y e^{3 x}}{2 y + 3 e^{3 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-9(-1)}{3+2(-1)}=9$ |

**Marking:** G1 M1 product attempt with its two contributions, G2 A1 correct product result, G3 B1 y²/constant derivatives, G4 M1 substitute the point, G5 A1 www canonical gradient after correct derivative working: **5/5**. Copying only the correct gradient earns **0/5** under OD-1; feedback acknowledges its correctness and requests the derivative/substitution steps.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## gradient: boundary — `WB8227-implicit-normal:gradient:boundary`

**Question.** A curve has equation $4e^{3x}y+y^2=5$ and the point $P=(0,-5)$ lies on it. Find its gradient at P, showing all working. Give an exact value or a correctly rounded three-significant-figure decimal. [5]

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor3 | $12e^{3x}y+4e^{3x}y'$ |
| Differentiate y² and the constant | y depends on x, while 5 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(4e^{3x}+2y)y'=-12e^{3x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{12 y e^{3 x}}{2 y + 4 e^{3 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-12(-5)}{4+2(-5)}=-10$ |

**Marking:** G1 M1 product attempt with its two contributions, G2 A1 correct product result, G3 B1 y²/constant derivatives, G4 M1 substitute the point, G5 A1 www canonical gradient after correct derivative working: **5/5**. Copying only the correct gradient earns **0/5** under OD-1; feedback acknowledges its correctness and requests the derivative/substitution steps.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## normal: normal — `WB8227-implicit-normal:normal:normal`

**Question.** A curve has equation $3e^{2x}y+y^2=4$ and the point $P=(0,-4)$ lies on it.

- **show-derivative [4]:** Show that $y'=- \frac{6 y e^{2 x}}{2 y + 3 e^{2 x}}$ where the denominator is nonzero, showing all necessary working.
- **gradient [2]:** Hence, using your derivative or the displayed formula, find the gradient at P. Give an exact value or a correctly rounded three-significant-figure decimal.
- **normal [3]:** Find the exact equation of the normal at P. Show the perpendicular-gradient and line-construction steps.

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor2 | $6e^{2x}y+3e^{2x}y'$ |
| Differentiate y² and the constant | y depends on x, while 4 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(3e^{2x}+2y)y'=-6e^{2x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{6 y e^{2 x}}{2 y + 3 e^{2 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-6(-4)}{3+2(-4)}=- \frac{24}{5}$ |
| Find the perpendicular gradient | The normal is perpendicular to the tangent | $m_\perp=-\frac1{- \frac{24}{5}}=\frac{5}{24}$ |
| Form the line through P | Use the point together with that perpendicular gradient | $y-(-4)=\frac{5}{24}x$ |

**Marking:** S1 M1, S2 A1, S3 B1, S4 terminal A1 for a complete correct forward derivation: **4/4**; H1 M1 substitution into the given derivative, H2 A1 gradient: **2/2**; N1 M1 labelled perpendicular gradient equal to −1/(their m), N2 DM1 point-line construction, N3 A1 exact equivalent line: **3/3**. Total **9/9**. The gradient part does not re-award the derivative marks. Copying the shown formula earns0/4; a proof slip followed by that formula cannot earn S4. A bare correct normal line earns0/3, not an inferred M1. A failed proof does not prevent correctly using the given formula for later H/N awards.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## normal: changed — `WB8227-implicit-normal:normal:changed`

**Question.** A curve has equation $3e^{3x}y+y^2=-2$ and the point $P=(0,-1)$ lies on it.

- **show-derivative [4]:** Show that $y'=- \frac{9 y e^{3 x}}{2 y + 3 e^{3 x}}$ where the denominator is nonzero, showing all necessary working.
- **gradient [2]:** Hence, using your derivative or the displayed formula, find the gradient at P. Give an exact value or a correctly rounded three-significant-figure decimal.
- **normal [3]:** Find the exact equation of the normal at P. Show the perpendicular-gradient and line-construction steps.

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor3 | $9e^{3x}y+3e^{3x}y'$ |
| Differentiate y² and the constant | y depends on x, while -2 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(3e^{3x}+2y)y'=-9e^{3x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{9 y e^{3 x}}{2 y + 3 e^{3 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-9(-1)}{3+2(-1)}=9$ |
| Find the perpendicular gradient | The normal is perpendicular to the tangent | $m_\perp=-\frac1{9}=- \frac{1}{9}$ |
| Form the line through P | Use the point together with that perpendicular gradient | $y-(-1)=- \frac{1}{9}x$ |

**Marking:** S1 M1, S2 A1, S3 B1, S4 terminal A1 for a complete correct forward derivation: **4/4**; H1 M1 substitution into the given derivative, H2 A1 gradient: **2/2**; N1 M1 labelled perpendicular gradient equal to −1/(their m), N2 DM1 point-line construction, N3 A1 exact equivalent line: **3/3**. Total **9/9**. The gradient part does not re-award the derivative marks. Copying the shown formula earns0/4; a proof slip followed by that formula cannot earn S4. A bare correct normal line earns0/3, not an inferred M1. A failed proof does not prevent correctly using the given formula for later H/N awards.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## normal: boundary — `WB8227-implicit-normal:normal:boundary`

**Question.** A curve has equation $4e^{3x}y+y^2=5$ and the point $P=(0,-5)$ lies on it.

- **show-derivative [4]:** Show that $y'=- \frac{12 y e^{3 x}}{2 y + 4 e^{3 x}}$ where the denominator is nonzero, showing all necessary working.
- **gradient [2]:** Hence, using your derivative or the displayed formula, find the gradient at P. Give an exact value or a correctly rounded three-significant-figure decimal.
- **normal [3]:** Find the exact equation of the normal at P. Show the perpendicular-gradient and line-construction steps.

| Action | Reason | Result |
|---|---|---|
| Differentiate the exponential product | Both factors depend on x; retain the chain factor3 | $12e^{3x}y+4e^{3x}y'$ |
| Differentiate y² and the constant | y depends on x, while 5 is constant | $2yy'$ and $0$ |
| Collect the derivative terms | A forward derivation must establish the requested derivative | $(4e^{3x}+2y)y'=-12e^{3x}y$ |
| Divide by the nonzero coefficient | On this local branch the derivative is finite | $y'=- \frac{12 y e^{3 x}}{2 y + 4 e^{3 x}}$ |
| Substitute P | The requested gradient belongs to this point, not an arbitrary root of the curve | $m=\frac{-12(-5)}{4+2(-5)}=-10$ |
| Find the perpendicular gradient | The normal is perpendicular to the tangent | $m_\perp=-\frac1{-10}=\frac{1}{10}$ |
| Form the line through P | Use the point together with that perpendicular gradient | $y-(-5)=\frac{1}{10}x$ |

**Marking:** S1 M1, S2 A1, S3 B1, S4 terminal A1 for a complete correct forward derivation: **4/4**; H1 M1 substitution into the given derivative, H2 A1 gradient: **2/2**; N1 M1 labelled perpendicular gradient equal to −1/(their m), N2 DM1 point-line construction, N3 A1 exact equivalent line: **3/3**. Total **9/9**. The gradient part does not re-award the derivative marks. Copying the shown formula earns0/4; a proof slip followed by that formula cannot earn S4. A bare correct normal line earns0/3, not an inferred M1. A failed proof does not prevent correctly using the given formula for later H/N awards.

**Independent check.** Solving the curve as a quadratic in y gives the local branch $y=(-ae^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, with $\sigma=\operatorname{sign}(a+2q)$. Its independently computed derivative at x=0 agrees with the gradient above; the normal slope times that gradient is−1. The oracle also computes the implicit partial-derivative ratio separately and checks the shown symbolic formula. It does not call a question generator.

## Boundary, source and marking checks

The changed tuple is now(3,3,-1): it keeps a genuine exponential chain factor and has positive gradient9, normal slope−1/9. Its proof identity differs from the normal(3,2,-4) example. The boundary(4,3,-5) has the largest admitted a,k,|q| and finite nonzero slope−10. None is the excluded official original(2,3,-5).

Reject k=1 (the declared composite-chain demand is absent), a+2q=0, q=-a, q=0 outside the chosen domain, and the2025Q5 original tuple. A point not on the curve is invalid. For the negative-constant cases a nearby vertical turn is a later diagram hazard; the pilot omits optional diagrams. No source crop or copied textbook problem accompanies these examples.

An alternative full explicit-quadratic proof/gradient route earns the exclusive mapped cap only with complete valid working; it does not add marks to the implicit route. In the extended branch the hence substitution must use the displayed derivative or their credible expression from the proof; no non-hence SC is invented. A coherent slipped gradient followed by a shown negative reciprocal and a line through P earns N1+N2=2/3, while N3 stays0 unless the canonical exact line is obtained, except for eligible OD-6 genuine question-data misreads under the once-per-datum rule. Multiple attempts, ambiguous handwriting and premature rounding follow D1-MR03/05/07 without fabricated credit.

The six paper cases passed the separate oracle in `planning/d4/calculus-exemplar-oracle.json`. Domain audit counts27point tasks on23 curves and8 show-derivative identities; these are not six assigned fresh questions. Partwise no-repeat guards and source attribution remain later app acceptance requirements. Proposed whole Bloom3 for each complete branch; no runtime, grading or app-rendering acceptance is claimed.

## D2 marking-route examples

For the normal curve $3e^{2x}y+y^2=4$, an e-index error produces $y'=-6e^xy/(3e^{2x}+2y)$. At P=(0,−4) its value is still −24/5. Gradient-only G1/G3/G4 can earn 3/5; G2 and G5 www are zero. Feedback identifies the wrong general exponential derivative, rather than treating the correct final value as proof of a correct method.

A valid divided-relation proof starts from $3e^{2x}+y=4/y$ and obtains $6e^{2x}+y'=-4y'/y^2$. Complete correct rearrangement and substitution of $4=3e^{2x}y+y^2$ give $y'=-6e^{2x}y/(3e^{2x}+2y)$. S1–S4 map as in the work order and earn4/4. A failed or missing back-substitution after correct differentiation earns S1/S2/S3=3/4 and S4=0. The equivalent log-absolute route is also mapped. At the supplied negative-y branch an invalid $\ln y$ without moduli gives S1=0, dependent S2/S4=0; separately correct S3 evidence can earn1/4 at most (CALC-D2-DEV09 (D3 clarification)).

If a proof drops k, their own derivative substitution earns H1 but not canonical H2: for this example the wrong gradient is −12/5. Using the displayed correct derivative instead earns2/2 for the later part. The known wrong-index derivative substituted in part(b) gives H1/H2=2/2 because its value is canonical at x=0; proof S2/S4 remain lost. A stated labelled perpendicular gradient $m_\perp=5/24=-1/(−24/5)$ is sufficient N1 method evidence; a correct final line alone earns0/3.

For the boundary target, explicitly cancelling 2 gives $-12ye^{3x}/(4e^{3x}+2y)=-6ye^{3x}/(2e^{3x}+y)$, so the simplified equivalent endpoint earns S4 after a complete correct forward derivation.

## D4 OD-6 misread samples

Use the matching work order’s MR03 application. Vitalis’s OD-6 principle is supported by NSSCAS report2025 PDF345 item4 and comparable Cambridge9709/12 March2016 scheme PDF3, not a Namibian one-mark tariff. The unit, ordering, persistent eligibility and gross/net ledger are proposed operational rules pending approval.

Gradient normal: read k=2 as3 from the question, then differentiate correctly to $9e^{3x}y+(3e^{3x}+2y)y'=0$. The point (0,−4) remains on the curve. Substitution gives $m=-36/5$. All G1–G5 meet their evidence on the misread data; MR−1 comes from first earned A/B G2: **4/5**. Feedback: “You read the exponent coefficient as3; the question gives2. Your differentiation and substitution are consistent with3.”

Extended normal: prove the actual displayed derivative correctly (4/4), then misread its numerator6 as8 only when applying part(b). Correct substitution gives $m=-32/5$, and shown normal working gives $m_\perp=5/32$, $y+4=(5/32)x$. Deduct H2 once in part(b), **1/2**; normal **3/3**, total **8/9**. No second charge and no repair of a failed proof by changing its supplied target. The first-use ledger identifies the later numerator misread separately from the correctly read proof.

Misreading own calculated −24/5, changing data so the supplied point is off the curve, changing the proof target, or using an invalid e-index rule is not this eligible MR case. A correct number with wrong e-index working still cannot earn gradient-only G5 www. Only if no A/B is earned on that datum anywhere is the net deduction zero; otherwise select the first earned A/B in question order. Gross dependencies survive the net penalty.

## D4 connected eligibility and net-penalty examples

For $3e^{2x}y+y^2=4$, $P=(0,-4)$, a first-use C4→5 misread makes the point inconsistent with the curve. It is ineligible once for the whole connected question. A perfect derivative proof is nevertheless unchanged because C differentiates to0; using the true displayed derivative for gradient and normal gives **9/9 canonically**, with no MR adjustment.

A first-use a3→4 misread in that same question is also ineligible and remains canonical in later parts. The learner’s derivative is $-8e^{2x}y/(4e^{2x}+2y)$, its substituted gradient is−8, and their normal is $y+4=x/8$. The ordinary rubric gives S1/S3=2, H1=1, N1/N2=2, hence **5/9**. Correct method follow-through does not convert wrong canonical H2/N3 accuracy into MR accuracy.

For the eligible k2→3 gradient-only misread above, the gross G2 evidence remains correct and earned after the one-mark net deduction is allocated there. G5 therefore remains earned: **4/5, not3/5**. The operating choice is proposed; the one-mark-with-follow-through principle is owner-decided.
