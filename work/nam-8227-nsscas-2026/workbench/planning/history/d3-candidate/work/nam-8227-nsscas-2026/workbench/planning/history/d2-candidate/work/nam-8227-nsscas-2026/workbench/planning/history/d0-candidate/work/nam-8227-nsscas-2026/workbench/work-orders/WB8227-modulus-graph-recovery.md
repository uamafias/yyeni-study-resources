# Work order: WB8227-modulus-graph-recovery

NSSCAS Mathematics 8227, December 2020 syllabus, Grade 12. PLANNER Codex; owner Vitalis; 23 November 2026. Proposed version **0.1.0**; stage D paper design; owner approval and independent branch review pending. Selection `8227:SELECT:D:modulus-graph-recovery`, a narrow pilot branch of accepted C selection `8227:FAMILY:modulus-reading`; branch `vertex-intercepts`. This is not a runtime recipe/item or an instruction to start authoring before plan approval.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Target, reuse and boundaries

Recover the three integer coefficients in $y=a|x+b|+c$ from a supplied labelled modulus graph. New purpose-built recipe: no installed 8227 implementation has been demonstrated and no Flashcard Studio material is an input. Reuse the existing Workbench contract/work-order structure, accepted curriculum IDs and source registers. A graph-to-parameters response tests inverse reconstruction; an equation-to-sketch example does not supply this practice. This justifies a separate recipe from direct graph sketching.

One assessed part, stable `a`, response format `numeric` (three named coefficients; the complete correctly positioned symbolic formula is an accepted equivalent response). Primary objective `8227:2020:M2:T1:O02`; direct demand `8227:2020:M2:T1:O02:D02`. Prerequisite `8227:2020:M2:T1:O01:D01` (meaning of modulus), plus NSSCO coordinate reading and linear substitution. Prerequisite links do not earn direct coverage. No learner sketch is asked, so this recipe does not directly cover `M2:T1:O02:D01`. Quadratics, inequalities, noninteger graph coefficients, nonlinear modulus arguments and unspecified-scale measurement are outside it.

## Sources and calibration

| Authority | Exact locator | What it supports / limit |
|---|---|---|
| Syllabus | `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, PDF14/printed11, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30` | Integer modulus-graph interpretation; grade-a combined form is PDF20/printed17, descriptor `8227:GRADE:A:11`. Grade-c simpler modulus graphs: PDF22/printed19, `8227:GRADE:C:10`. Grade descriptors calibrate demand, not extra scope. |
| NSSCAS question | `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 2 8227-2 - First Proof 13.03.2023.pdf`, Q2 PDF/printed3, SHA256 `6e6fa13da22e198cdd0686db38550144705e67b05078d2ca0b9cc8d27026fd5e` | Same inverse parameter recovery, 3 marks. Source $a=-2,b=-3,c=2$. Native page checked, including graph. |
| Award/report | `Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf`, PDF331/printed329, Q2 | Three independent B1 awards; correctly placed values in formula accepted. Report warns against treating modulus as parabola and confusing $b$ with the $y$-intercept. Source hash in `planning/visual-source-reads.json`. Adapted numeric criteria below are proposed. |
| Textbook breadth | YM C8 PDF383–385/printed371–373 and Exercise8 Q9 PDF401/printed389; Goldie Example1.14 PDF32/printed18 and Exercise1C Q4 PDF36/printed22 | All ten members of `modulus-equation-to-sketch` read. They teach forward sketching, not this reverse recovery. `visual-source-reads.json` records book/file hashes, all selected subparts and 15 accepted assessed/component union discovery hits. Fractional YM Try9 Q2(e) and Try8 Q2(d) are outside the integer coefficient limit. |

Textbooks are internal evidence (`learner_display: false`); original wording and artwork are not outputs. Native-page comparisons, not family distinction/precision templates or extracted notes, inform this design. The same-type label is branch-specific: “Same type as NSSCAS Mathematics 8227, 2023 Paper 2, Question 2, page 3”. The full reference fields, source hash, relation and verification date are in `planning/visual-design.json`. No held original is used. Changed response requirements require a fresh reference comparison.

The easiest admitted cases use $|a|=1$ and simple integer labels (grade-c related transformations); hardest use $|a|=3$ with horizontal and vertical shifts, bounded by the grade-a combined-form description and the three-coefficient source task. These numerical bounds are a planner-chosen pilot subset, not official grade cutoffs or a claim that this exhausts grade a.

## Domain, variation and capacity

Choose independently $a,b\in\{-3,-2,-1,1,2,3\}$ and $d\in\{1,2,3\}$; set $c=-ad$. The canonical givens are the vertex $V=(-b,c)$, both zeros $(-b-d,0),(-b+d,0)$, and the $y$-intercept $(0,a|b|+c)$. Give those exact labels, a V/inverted-V shape and the model form with coefficients unknown. The meaning of $a,b,c$ stays fixed. Upward/downward orientation, left/right shifts, slope size, intercept signs and a coincident axis crossing vary; these are ordinary variations of the one inverse-reconstruction decision, not extra recipes.

Capacity: $6\times6\times3=108$ distinct coefficient triples. The map from $(a,b,d)$ is injective because $d=-c/a$, so no two parameter tuples are the same labelled problem. This is finite numerical/graph variation, not 108 problem types. A duplicate fingerprint uses recipe/version/branch, the coefficient triple, exact displayed labels and requested response; omit random identifiers and do not use final answer alone. No-repeat scope must be per learner/selected version across practice and fresh test reservations; app owns history. At exhaustion return a typed exhausted result and offer an owner-approved domain extension or disclosed reset; never silently repeat or broaden the domain. Stage-E generator design must use bounded constructive selection, not unbounded rejection.

Rejected cases: $a=0$ removes the modulus vertex; $b=0$ is excluded by this pilot domain (not mathematically invalid); $d=0$ collapses both zeros and changes the evidence; noninteger $a,b,c$ violate the selected syllabus bound. Inconsistent vertex/intercepts are invalid. $|b|=d$ is admitted: the origin is both an $x$- and $y$-intercept and the shared label must remain unambiguous.

## Given asset and response specification — must-read givens (R3-07)

`given_representation: graph`. **Must read:** vertex label, both zero labels, $y$-intercept label, which axis is $x/y$, V orientation and the displayed form $a|x+b|+c$. Exact coordinates are also stated accessibly in text so no screen measurement is needed. They are the same data, not extra solution help.

Asset ID `given-modulus`; fixed: Cartesian axes, straight arms, one vertex, exact labels and no measurement task. Variable: coefficient-derived vertex, zeros, intercept, visible window and label offsets. Relations: arms are $a|x+b|+c$; slopes $-a$ left and $a$ right; vertex symmetry line $x=-b$; all four labelled points satisfy the same formula. Use equal numeric coordinate calibration when showing tick scales; mark any schematic projection explicitly and never imply a false scale. Pad beyond every important point, avoid crossing labels, and merge the origin label when needed. Generate from the same authoritative tuple as answer/solution; a fixed source crop cannot accompany incompatible parameters. Must-read asset data and accessible text must match.

No response frame, sketch assessment, physical units or angle mode is needed. Marker accepts named $a,b,c$, a coefficient tuple with unambiguous order, or a correctly positioned full formula. A screenshot/photo capability is not assumed proven reliable. Owner decision6 includes visuals; record the required graph rendering/answer reading and test them later rather than holding the demand for capability.

## Canonical solution, criteria and Bloom

For every tuple: read $(-b,c)$, so $b=-x_V,c=y_V$. Substitute either zero or the $y$-intercept to obtain $a$. Check sign against orientation and substitute into the remaining point. A slope method using the vertex and either zero is equally valid. Worked instances are in the companion exemplar.

Criterion IDs have prefix `WB8227-modulus-graph-recovery:`. All awards adapted from official Q2 B1/B1/B1, proposed pending review.

| ID | Marks | Evidence / dependency | Direct demand |
|---|---:|---|---|
| `a:B1` | B1 | Correct $a$, including correct orientation sign; independent of the other answers | `M2:T1:O02:D02` |
| `a:B2` | B1 | Correct $b$ in the supplied plus-sign convention, not $x_V$ | same |
| `a:B3` | B1 | Correct $c$ | same |

Part/whole total **3**. No method restriction, no compulsory working, no follow-through and no double credit. Correct values in the appropriate formula positions earn full credit, as in the official source. An equivalent formula such as $-2|x+2|+2$ demonstrates all three; a differently parameterised expression must be normalised or read as an equivalent function, without marking its temporary letter names as wrong. A tuple with no order and no labels is ambiguous, not automatically wrong. Exact integers required; $-2.0$ is exact-equivalent, but approximate coefficients changing a labelled point are not.

Proposed part Bloom **Apply (3)**, classification `8227-pilot-design-0.1.0`: the learner applies familiar transformation/point-substitution rules to a supplied graph, evidenced by all three coefficient criteria. Whole-card maximum is 3 because the sole assessed part is classified. Reading a complex model solution does not raise it. This label belongs to this branch/version, remains proposed until independent review, and is not inherited by a future proof/sketch branch.

## Submission and feedback expectations

For normal exemplar $y=-2|x+2|+2$:

| Submission | Credit | Specific feedback / next action |
|---|---:|---|
| $a=-2,b=2,c=2$ | 3/3 | All three coefficients fit the graph. No invented repair. |
| $a=-2,b=-2,c=2$ | 2/3 | The vertex has $x=-2$. In the displayed plus-sign form, $x+b=0$ there, so $b=2$. Check the horizontal shift. |
| Full formula $y=-2\lvert x+2\rvert +2$ with no working | 3/3 | Full credit; the requested result is entirely present. |
| $a=2,b=2,c=2$ | 2/3 | The graph opens downward, so its outer coefficient is negative. Substitute one labelled zero to confirm. |
| “$-2,2,2$” with no specified tuple order | unresolved if order not established | Ask which value is $a,b,c$; retain the original response and do not invent a misconception or reliable mark. If the response UI already labels the fields, award normally. |

Practice: before submission, optional general reminder that the expression inside the modulus vanishes at the vertex; any worked example must be a different tuple and must not reveal current coefficients. After submission reveal the frozen current solution, credited criteria and first evidenced correction. Fresh next attempts may be requested without first passing; an aided retry is not an unaided mastery observation. Test: no hints/example/tutor before submission; preserve existing question-by-question post-submission review, marking pause and timer/progress protections. App owns unlock/progress, never this recipe.

## Checks and approval limits

Stage D: three manual exemplar cases checked by substitution, slopes and a separate coefficient recovery, and 108-tuple capacity/injectivity counted. Stage E/F required: independent point residual checks for all 108 tuples, admitted-origin collision render, invalid/contradictory-given fixtures, no-repeat/exhaustion, replay seeds0/1/42/$2^{63}-1$ and targeted boundaries; at least64 valid draws or full finite enumeration as appropriate. Do not verify a generator only with its own answer function.

Apply the existing 7 November 2026 learner-text snapshots in `workbench/playbook/guidelines/provenance.json`, not a new instruction fork: safe decoded Markdown/LaTeX, action/reason/result, accessible labels and saved-history render. Actual app rendering, seeded generation, marking orchestration, privacy/reveal timing and source-wording comparisons are **not run** in stage D. Any direct exam original must retain attribution and source disposition; textbooks stay internal. No runtime release is accepted by these paper checks.

Owner checkpoint: Vitalis accepts scope/count108, graph requirements, proposed credit/Bloom and the normal/varied/boundary exemplar. Authoring waits for plan approval; independent content/branch review and app testing still follow.
