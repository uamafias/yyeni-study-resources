# Work order — WB8227-trig-rform-equation

NSSCAS Mathematics 8227, NIED December 2020; Grade 12. Owner Vitalis; PLANNER Codex, 23 November 2026. Proposed recipe version 0.1.3 and classification `8227-pilot-design-0.1.1`. Stage-D D3 repair only. Claude’s changed-scope confirmation comes before Vitalis approves the plan; no runtime authoring, imports, assignments, commit or push.

## Identity and retained selection

Recipe `WB8227-trig-rform-equation`; branch `degree-cycle`; selection `8227:D:SEL:trig-rform-equation:degree-cycle`. Accepted parent groups remain `8227:FAMILY:r-form` and `8227:FAMILY:bounded-trig`. New purpose-built recipe using the existing framework; not a Flashcard Studio conversion. Conversion and hence-equation stay connected; extra extrema, reciprocal/pole reduction, higher harmonics and radian forms remain later facets, not extra recipes.

Target: coefficient-consistent amplitude/phase, then all roots in the actual shifted interval using the prior result. A direct non-hence method does not satisfy the restricted stem. No source is inferred from a topic label: the actual anchor is2022 P2 Q6(a),(b)(i), PDF/printed8. The coefficient is $\sqrt5$, not extracted plain5.

## Sources, scope and calibration

Syllabus PDF 15/printed12, M2:T3:O02, and PDF 11/printed8, M1:T6:O06. The native 2022 examiner report PDF 312–313/printed310–311 supplies the wrong-ratio, degree-mode, shifted-root and extra-answer evidence and its B1/M1/A1 + M1FT/DM1/A1/A1 table. General rules:2021 PDF 236,2025 PDF 355. Exact non-square surds are supported by 2021 PDF 236/243;2022 PDF 312 specifically says a perfect-square root must be evaluated. Related2025 P2 Q9, paperPDF9/reportPDF361, confirms fourth-quadrant transformed-angle examination breadth; it is not silently copied as the anchor’s own memo.

All source paths/hashes/render locators are in `planning/trig-model-source-reads.json`, D1 append. The accepted D0 reads cover every member of adopted textbook families `rform-coefficient-conversion` (5) and `rform-solve-cycle` (13); union discovery41 items includes explicit unread leads, never proof of absence. YM Try Now19 Q1 supports a connected conversion→equation practice unit. Source signs, requested sine/cosine form and original interval were read from the page. All textbook use is internal.

Grade E:12 (syllabusPDF23) supports conversion; C:12 (PDF 22) supports equations after conversion; A:06/A:13 (PDF 19/20) bounds harder trig work. The pilot remains a small-coefficient, one-cycle, no-pole subset. Numerical bounds are proposed corpus-informed limits, not official grade cutoffs.

## Part identity, links and proposed Bloom

All IDs below are authoring identities, not display-order letters. The common contract resolves conditional links before an eventual instance is frozen.

### Branch `degree-cycle`

- Part `WB8227-trig-rform-equation:degree-cycle:a-convert`; 3 marks; response `symbolic`; primary `8227:2020:M2:T3:O02`; other direct objectives: none.
- Direct demand IDs: `8227:2020:M2:T3:O02:D04`.
- Prerequisite IDs: `8227:2020:M2:T3:O02:D02` (prerequisite or previously assessed result; no direct coverage in this part).
- Proposed Bloom: Apply 3: this part only earns a-B1 for amplitude,a-M1 for coefficient/phase method,a-A1 for phase accuracy; no sibling root criterion is used.
- Criterion IDs: `WB8227-trig-rform-equation:degree-cycle:a-convert:a-B1`, `WB8227-trig-rform-equation:degree-cycle:a-convert:a-M1`, `WB8227-trig-rform-equation:degree-cycle:a-convert:a-A1`.
- Part `WB8227-trig-rform-equation:degree-cycle:b-roots`; 4 marks; response `numeric`; primary `8227:2020:M2:T3:O02`; other direct objectives: `8227:2020:M1:T6:O06`.
- Direct demand IDs: `8227:2020:M2:T3:O02:D05`, `8227:2020:M1:T6:O06:D01`, `8227:2020:M1:T6:O06:D02`.
- Prerequisite IDs: `8227:2020:M2:T3:O02:D04` (prerequisite or previously assessed result; no direct coverage in this part).
- Proposed Bloom: Apply 3: this part uses b-M1 hence reduction,b-M2 complete shifted-interval branch search and b-A1/b-A2 allowed original roots; routine phase/root procedures, not Analyse.
- Criterion IDs: `WB8227-trig-rform-equation:degree-cycle:b-roots:b-M1`, `WB8227-trig-rform-equation:degree-cycle:b-roots:b-M2`, `WB8227-trig-rform-equation:degree-cycle:b-roots:b-A1`, `WB8227-trig-rform-equation:degree-cycle:b-roots:b-A2`.

Branch maximum3 from its own classified parts; proposed only, never an average or a sibling maximum.

## D1 finite domain and diagnostic invariant

$a,b\in\{1,2,3,4\}$, $c\in\{-3,-2,-1,0,1,2,3\}$. Require $c^2<a^2+b^2$, $c\ne b$, $\gcd(a,b,|c|)=1$. Exclude $(1,4,\pm3)$ and $(4,1,\pm3)$ for the very close one-decimal root boundaries, and $(2,4,\pm1)$ and $(3,4,\pm2)$ for the remaining two-decimal-intermediate flips. Exclude $a=b$: the native report’s named error $\tan\alpha=a/b$ then equals the correct $b/a$.

Counts:112 grid tuples→102 feasible→90 without endpoint roots→78 primitive D0 tuples→70 after eight rounding exclusions→58 after twelve inverse-ratio collision exclusions. The two new exclusion sets do not overlap. All 58 are finite, real, two-distinct-root tasks strictly inside $0^\circ<\theta<360^\circ$; the diagnostic script checks the wrong ratio numerically, not merely the inequality.

Question wording: (a) express $a\sin\theta+b\cos\theta$ as $R\sin(\theta+\alpha)$ with $R>0$, $0^\circ<\alpha<90^\circ$, exact $R$ and phase to 2 dp [3]; (b) **Hence** solve the original equation $a\sin\theta+b\cos\theta=c$ for the stated strict degree interval, roots to 1 dp [4]. “Hence” is retained, not “or otherwise”. The word is a method restriction, not decorative scaffolding.

Let $\alpha=\tan^{-1}(b/a)$ and $\beta=\sin^{-1}(c/R)$, in degrees. b-M2 requires the transformed roots inside $\alpha<\theta+\alpha<360^\circ+\alpha$:

| Class | Exact transformed-root evidence | D1 count |
|---|---|---:|
| $c>b$, equivalently $\beta>\alpha$ | $\beta$ and $180^\circ-\beta$ |6|
| $c<b$, $c\ne0$ | $180^\circ-\beta$ and $360^\circ+\beta$; positive-small targets need the wrap, negative targets use the negative-sine quadrants |42|
| $c=0$ | $180^\circ$ and $360^\circ$ |10|

Subtract the phase from each retained transformed root, then check the original equation and bounds. Positive versus negative alone is not the complete distinction. Named wrong methods checked for all 58: inverted coefficient ratio, returning a radian phase as a degree phase, one calculator root only, forgetting the phase shift and subtracting the final first root from 180 to invent the second. Premature-rounding fixtures are accuracy tests, not accusations of an unrelated misconception.

## Part capacity, exposure and exhaustion

Raw full-card mathematical capacity58; part(a) has 12 distinct $(a,b)$ prompts but10 distinct phase ratios/decisions. Part(b) has 58 primitive original-equation tasks. No-repeat keys are (a,b,requested form,unit) for part(a), reduced(b:a) for its phase subdecision, and primitive(a,b,c,interval,hence restriction) for part(b). Different $c$ does not make a revealed conversion fresh. A wholly fresh test card requires both assessed-part keys unseen; before any exposures there are at most12 fully fresh conversion contexts, and phase repeats are separately disclosed. Partly repeated practice may continue with after-feedback labelling. These counts are numeric variation inside three reasoning classes, not58 different types. At exhaustion return an honest exhausted result, not a label/seed refresh.

## Marking: official qualifiers retained

| Criterion | Award and qualifiers | Required visible evidence |
|---|---|---|
| a-B1 | B1 | Correct exact positive amplitude, embedded in eligible working. Unsimplified non-square surds such as $\sqrt{20}$ are accepted; a perfect square such as $\sqrt{25}$ must be written5 |
| a-M1 | M1 | Correct coefficient comparison/phase method, e.g. $\tan\alpha=b/a$; a correct equivalent triangle argument earns the same slot |
| a-A1 | A1 | Correct acute phase to 2 dp or an accurately stated more-precise value; not a value spoiled by prematurely rounding $R$ |
| b-M1 | M1 F.T. | Uses part(a)’s positive $R$ and admissible acute phase to make sine the subject |
| b-M2 | DM1, dependent on b-M1 | Complete root set of their transformed equation in $(\alpha_{\rm their},360^\circ+\alpha_{\rm their})$, with endpoints rejected; use their positive $R$ and acute $\alpha$, not the canonical class table |
| b-A1 | A1 c.a.o. | One correct original root to 1 dp; source explicitly allows this without b-M2, but it does not waive required visible working/hence use |
| b-A2 | A1 c.a.o. | The other correct original root to 1 dp; A0 if extra final values are submitted |

All part totals are3+4=7, with no overlapping alternative awards. D1-MR01 applies separately: bare correct $R,\alpha$ earns0/3; bare correct root pair earns0/4. A bare fully correct final $R\sin(\theta+\alpha)$ representation also earns zero without the required visible coefficient method. No official answer-only exception was located for either part. Correct practice feedback still says the values are right and asks for the working. Visible correct prior conversion alone is not enough to infer the missing root method.

A visible non-hence root method earns0 for(b): actual2022 R-form table has no SC row;2021 PDF 236/2025 PDF 355 give the hence restriction. The SC1s on2023 Q6(b) and2022 P1 Q2(b) are other question types, not transferable “official R-form SC1”. This evidence-based correction to the review’s analogous SC1 suggestion is recorded as D1-INTERPRET-RF-HENCE. If a future owner-approved version says “hence or otherwise”, its permitted methods and references require a new review; this version does not.

Extra-answer cap is on distinct submitted final numerical values. Any value outside the strict interval—including a coterminal negative angle—counts as an extra final value and loses b-A2. Only another spelling of the same value, such as $330.4^\circ$ and $330.40^\circ$, is a duplicate rather than an extra. Clear cancellation follows D1-MR07.

D1-MR05: keep unrounded $R,\alpha,\beta$ internally; early approximation that leaves the final answers correct is not penalised. If it changes a required phase/root, retain valid M/DM marks and withhold the affected A, with premature-rounding feedback. Store all eight excluded tuples and near2 dp phase pairs as later E/F fixtures. Non-square surd alternatives and exact phases do not require artificial trailing zeros; the D1 symmetric45degree cases are excluded diagnostically, not mathematically invalid.

## Responses, feedback and remaining review

The new normal example is $(a,b,c)=(2,3,1)$, not the old rounding-sensitive $(3,4,2)$. Full working earns7. A correct conversion, correct reduced sine equation and just the first valid root earns5/7. If the two transformed roots are shown but the learner keeps the out-of-domain calculator value instead of wrapping it, b-M2 fails, and only a genuinely correct original-root A can survive. A correct conversion plus two correct roots and an uncancelled coterminal extra loses b-A2. A completely correct non-hence method with full conversion elsewhere earns only the 3 conversion marks. A bare correct card earns0; give supportive method-request feedback. Ambiguous handwriting remains pending.

D1-ADAPT-RF-CLASSES: the source’s “first and second quadrant only” DM1 is adapted to a complete root search in the learner’s own shifted interval, using their own positive $R$ and acute phase. The class table describes canonical instances only; it does not replace their own interval when awarding b-M2. The reason/source distinction is disclosed, not an invented verbatim official rule. D1 limits and the updated three worked examples are in [the exemplar](../exemplars/WB8227-trig-rform-equation.md). The four named alpha-near-boundary pairs plus their proportional partners are frozen for later marker tests; runtime acceptance is still pending.

## Shared delivery, feedback and later validation

[recipe-contract.md](../recipe-contract.md), [subject-rules.md](../subject-rules.md) D1-MR01–09 and OD-1–OD-6 govern; the local qualifier/deviation ledger below specifies the actual adapted rows. The 7 November 2026 guideline snapshots and `workbench/playbook/guidelines/provenance.json` remain the text authority. Mathematical solutions use decoded LaTeX; no mathematics inside emphasis. These paper records do not claim an implemented metadata schema or marker.

Practice permits a new admitted instance without passing first. Current-instance hints are answer-free; a worked example uses a different semantic identity. Show solution and criterion feedback after submission, preserve the original response, acknowledge a correct bare answer and request its working under OD-1. A later repetition after feedback is not wholly unaided evidence. Ambiguous handwriting or an unclear sign stays pending clarification, not zero by assumption. Full-credit work gets no invented repair.

Workbench Test keeps no hints/example/tutor before submission; preserve question-by-question post-submission review, marking-time pause and existing nonfinal two-minute review/advance/expiry behavior. The app owns attempts, progress, no-repeat history, reservations and once-per-recipe-round credit. No resource field silently changes these policies.

Later E/F: independently enumerate admitted domains; verify mathematics, method/accuracy/dependency paths, answer-only zero, exactness, misread/rounding/extra-answer examples and semantic no-repeat. Replay seeds0,1,42 and2**63-1 once implemented, with at least64 draws per branch or exhaust smaller spaces. A separate oracle must not call the future answer constructor. Validate actual notation input/rendering, role-safe assets, solution reveal and grading. The D2 script is a design checker, not a question generator or runtime marker. Applicable runtime checks are not run now.

Textbook originals and images remain internal (`learner_display:false`). Exact exam originals require their own attribution and are outside the fresh pools; a same-type label never authorises unattributed verbatim reuse. Source findings and accepted item-level links are not retagged. Family templates, rejection notes and extracted prose are not design evidence. D0 whole-family page reads/union leads are preserved in `planning/trig-model-source-reads.json`; the D1 append records the current native marking reads. No whole-syllabus coverage or learning-effectiveness claim follows.

## D2 own-result follow-through and later rounding fixtures

The three-class table describes canonical instances. For b-M2, after b-M1, judge the complete transformed-root search against **their** positive $R$ and acute phase. Enumerate roots of $\sin z=c/R_{\rm their}$ inside $\alpha_{\rm their}<z<360^\circ+\alpha_{\rm their}$. Showing the complete eligible set, with any endpoint rejected, earns the dependent method mark even when the canonical $c$-versus-$b$ class would require different quadrants. Canonical b-A1/b-A2 remain c.a.o.; follow-through method is not follow-through accuracy.

For $(a,b,c)=(1,3,2)$, the inverted-ratio phase is $\alpha'=\tan^{-1}(1/3)$. The learner's two transformed roots are the first- and second-quadrant roots in their interval, although the canonical instance needs a wrapped root. A complete search in their own interval earns b-M2; copying the canonical class table does not.

For $c=a$ after the same inverted-ratio error, $\beta=\alpha'$. The transformed root $z=\alpha'$ gives $\theta=0$, which is outside the strict interval. The other root $z=180^\circ-\beta$ is the only eligible root. A complete search that retains this one and explicitly rejects $\theta=0$ earns b-M2. Keeping the endpoint does not. The same complete-set principle handles an own equation with no real roots or a tangent root, with a valid justification; it never converts a wrong parameter into canonical A credit.

Freeze the six class-change tuples and eight $c=a$ endpoint tuples in `planning/d2/trig-d2-fixtures.json`. The fixture file also records every admitted-tuple premature-rounding flip under phase/root angles at 1 d.p., amplitude at 3/4 significant figures, ratio at 3 significant figures and the rounded-amplitude arccos route. Include the four both-2-d.p. half-up ties, including 299.55, and the $(3,1)$ and $(1,3)$ amplitude-at-6-s.f. phase cases. Later accepted-answer generation must use decimal round-half-up; binary banker's rounding is not the specified policy. Earned M/DM remains when premature rounding alone spoils final accuracy. These are design fixtures, not a runtime marker or renderer pass.

OD-6 / D1-MR03: For a genuine misread of question data with the object and difficulty unchanged, judge M/DM normally and follow all earned A/B through on that datum. Deduct one mark per misread datum from the earliest eligible earned A/B criterion in the first-use part, unless the actual scheme specifies an order; later parts reuse it with no repeat deduction. If that part earns no A/B, deduct nothing and do not defer the penalty. Scores cannot be negative. Own-figure mistakes and misreads that change the object or difficulty (including making the task easier or leaving no solution) receive normal canonical marking. Correct working (www), named-error exclusions and OD-1 still apply; answer-only work is not rescued. Practice feedback names the misread. Basis: owner OD-6; NSSCAS 2025 report PDF 345 item 4 (CONVENTION:108), and Cambridge 9709_m16_ms_12.pdf PDF 3 Penalties, explicitly a comparable board convention, not a Namibian rule.

D3 precision-path clarification: `planning/d2/trig-d2-fixtures.json` remains frozen D2 evidence. Its ratio-at-3-s.f. path has 14 flips with exact phase; the review’s 10 uses the phase carried at its requested 2 d.p. Both are correct for their stated paths. Coupled phase/root recovery from 3-s.f. amplitude has 33 flips with an unrounded phase and 35 after writing that phase to 2 d.p.; isolated phase error with exact root angle has 34. D3 freezes the missing explicit paths and 6-s.f. arcsine case in `planning/d3/trig-d3-fixtures.json`. These are proposed stage-E/F acceptance fixtures; no runtime marker or accepted-answer behavior is established.
