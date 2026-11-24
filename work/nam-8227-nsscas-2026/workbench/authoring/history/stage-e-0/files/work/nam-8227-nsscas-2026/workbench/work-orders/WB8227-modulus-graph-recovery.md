> **Current gate — 24 November 2026:** Claude confirmed D4.1 and Vitalis approved the exact Stage-D manifest `4a054832…17d8ec`, including MR03-OPS-D4. Stage E is active; E/F runtime author checks and cross-vendor content review are next. Earlier pending/next-gate prose below describes the archived Stage-D proposal.

# Work order: WB8227-modulus-graph-recovery

NSSCAS Mathematics 8227; NIED December 2020 syllabus, Grade 12. Owner Vitalis; PLANNER Codex; 24 November 2026. **Proposed v0.1.4, stage-D4 design repair. Claude D4 changed-scope confirmation, then Vitalis approval pending; no stage-E authoring.** Accepted C selection `8227:FAMILY:modulus-reading`; narrowed selection `8227:D:SEL:modulus-graph-recovery:vertex-intercepts`; branch `vertex-intercepts`.

## Purpose, assessment and reuse

Recover integer $a,b,c$ in $y=a\lvert x+b\rvert+c$ from a labelled graph. This inverse reconstruction is distinct from drawing a graph from an equation; supplying the graph does not directly assess learner sketching. New purpose-built 8227 design, extending existing Workbench records/provider boundaries; no Flashcard Studio content is converted. One connected response part `a`, numeric named coefficients or a complete formula; primary objective `8227:2020:M2:T1:O02`, direct demand `8227:2020:M2:T1:O02:D02`. Prerequisite `8227:2020:M2:T1:O01:D01` is modulus meaning, not direct coverage. NSSCO coordinate reading and linear substitution support the task. Quadratics, inequalities, fractional graph coefficients and nonlinear modulus arguments are outside this branch.

## Native sources and calibration

- Syllabus `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`; PDF14/printed11 integer modulus-graph interpretation. Grade-c simpler graphs: `8227:GRADE:C:10`, PDF22/printed19; combined shifted/scaled form at grade a: `8227:GRADE:A:11`, PDF20/printed17. These bound complexity; they are not numerical grade cutoffs or new scope.
- NSSCAS 2023 P2 Q2, PDF/printed3: `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 2 8227-2 - First Proof 13.03.2023.pdf`, SHA256 `6e6fa13da22e198cdd0686db38550144705e67b05078d2ca0b9cc8d27026fd5e`. Same graph-to-coefficients task, three marks. Official original tuple $(a,b,d)=(-2,-3,1)$ is excluded from freshness.
- Examiner report 2023, `Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf`, PDF331/printed329 Q2: all three awards B1 **www**; “Allow all the marks if values are seen in the correct place in the formula.” It names parabola modelling and reading $b$ as the $y$-intercept as errors. The report corroborates this proof-file question content; whole-file final equivalence remains unverified in holdings.
- Textbook breadth: every member of `modulus-equation-to-sketch` was read, YM C8 PDF383–385 and401; Goldie Example1.14 PDF32 and Exercise1C Q4 PDF36. These are forward-sketch practice, not reverse-recovery counterparts. All ten member locators, source hashes and accepted assessed/component union discovery IDs are retained in `planning/visual-source-reads.json/.md`. Fractional YM variants stay outside integer graph bounds. Textbook originals/figures remain internal (`learner_display:false`). Family prose/templates and extracted notes are not design evidence.

The branch-specific same-type reference applies to part `a` only: “Same type as NSSCAS Mathematics 8227, 2023 Paper 2, Question 2, page 3”. Full fields/hash/verifier are in `planning/visual-design.json`; no held original is an anchor.

## Domain, named errors and capacity

Start from $a,b\in\{-3,-2,-1,1,2,3\}$, $d\in\{1,2,3\}$, $c=-ad$. Supply vertex $(-b,c)$, zeros $(-b-d,0),(-b+d,0)$ and $y$-intercept $(0,a\lvert b\rvert+c)$, with exact coordinate labels and matching V orientation.

D1 excludes every tuple where any targeted wrong method accidentally returns the corresponding canonical coefficient:

1. Parabola through vertex/zero gives $a_P=-c/d^2=a/d$: reject $d=1$ (36 raw tuples).
2. Parabola through vertex/$y$-intercept gives $a_P=(y_0-c)/b^2=a/\lvert b\rvert$: reject $\lvert b\rvert=1$ (36 raw tuples).
3. Reading $b=y_0$ gives a canonical coincidence when $b=a(\lvert b\rvert-d)$: reject those eight raw tuples.
4. Exclude the official original $(-2,-3,1)$; it already lies in the above rejection union.

The union removes64 of108 tuples, leaving **44**; counts overlap and are not summed. The earlier12 fully fitting parabolas and all20 reviewer-named collisions are included in this larger union. Other named misreads $b=x_V$ and $c=y_0$ never equal canonical values here. Invalid $a=0$, collapsed $d=0$, noninteger coefficients and inconsistent point labels are rejected. Positive/negative outer coefficient, left/right shift and intercept signs vary within the same inverse-reconstruction branch. Admitted origin-double cases remain valid;24 of44 have the origin as both intercepts.

Part `a` and full-task semantic key: `('modulus-model',a,b,d)`;44 distinct models, because $d=-c/a$ is recoverable. One part asks all three coefficients; repeated individual coefficient values do not create or remove complete task identity. Raw108 → admitted44 → semantic44; at most44 wholly unseen tasks before examples/exposures. App must track semantic keys, reserve unseen tasks atomically and preserve original versions; partly repeated practice is after-feedback, never wholly fresh test evidence. Exhaustion is explicit, not an unbounded rejection loop or silent domain reset. Domain/injectivity/discrimination checks: `planning/d4/visual-domain-checks.py` and its saved JSON.

## Question and assets — must-read givens

Ask: “The labelled graph has the form $y=a\lvert x+b\rvert+c$. Determine $a$, $b$ and $c$.” Supply exact points in accessible text as well as the graph, without showing recovered coefficients. `given_representation: graph`; `response_format: numeric` (a complete correctly positioned formula is an accepted equivalent).

Must read: vertex, both zeros, $y$-intercept, $x/y$ directions, V/inverted-V orientation and the fixed plus-sign convention inside the modulus. Fixed: Cartesian axes, one vertex, straight arms and explicit coordinate labels. Variable: all point values, window, slopes and label offsets. Relations: slopes $-a$ left/$a$ right; symmetry $x=-b$; every point satisfies the same expression. Generate question/solution/reference assets from one tuple. Equal labelled grid units are used in the paper illustrations; no screen measurement is asked. No fixed source crop accompanies incompatible new values.

Place zero labels outside the V with leader lines when needed, never two unattached labels between the dots. Merge the origin label when it serves two roles. Keep axes, points and labels legible. Keep a zero label on its own side of the y-axis where possible. Both retained normal and varied assets have a leader crossing the y-axis; its attached leader and repeated textual coordinates disambiguate it, so the inspection note does not claim otherwise. D2 retained crowded-label fixtures:8 (D0 had28); retained origin-merge fixtures:24 (D0 had36). Enumerated values are in the domain audit. Stage E/F must render these sets and actual app views; static SVG checks do not establish runtime rendering or visual marking. The 16 November owner decision 6 (visual demands) includes this demand without a capability hold.

## Canonical solution and marking

Read $b=-x_V,c=y_V$; substitute a zero or use the signed arm slope to find $a$; check the unused labels and orientation. Each meaningful solution step states action, reason and result. Alternatives use any exact labelled point or correct slope; no compulsory route is imposed. Companion exemplar has normal/changed/boundary cases and checked graph assets.

**Shared rules `subject-rules.md` D1-MR01–09 apply with their stated authority: OD-backed principles bind; proposed operational details await exact-manifest approval.** Full criterion prefix `WB8227-modulus-graph-recovery:`. Source rows are `8227:EXAM:2023:P2:Q2:AWARD:01–03`.

| Criterion | Award | Required evidence and official qualifier |
|---|---:|---|
| `a:B1` | B1 www | Correct signed $a$, without wrong working for it. |
| `a:B2` | B1 www | Correct $b$ in $x+b$, without wrong working for it. |
| `a:B3` | B1 www | Correct $c$, without wrong working for it. |

Total3, independent slots; no F.T., method restriction or duplicate award. **www is preserved on every B1.** A shown parabola model does not earn an accidentally correct coefficient via wrong quadratic working. Credit independent valid modulus vertex/shift work where actually present; do not invent it from the numerical result. Exact integer-equivalent terminating decimals are accepted; no hidden physical units.

**Answer-only per part `a`: official exception under OD-1/D1-MR01.** Correct unambiguous named values $a,b,c$ earn B1 www each, exactly as values in the correct positions of the complete formula do. A fully correct list in the requested named fields earns **3/3**, with no wrong working. The formula allowance extends the same value awards; it does not privilege formula format over named fields. A wrong shown method with an accidentally correct coefficient fails its www award. Ambiguous tuple order stays pending until clarified; named fields settle order. Practice feedback may ask for vertex/point reasoning while preserving earned marks.

The D1 list/formula split is withdrawn: the list/formula split was not an owner decision and did not match the official row. All three www conditions and the named-value/formula allowance now have the same meaning as 2023 Q2. This is an official type exception, not a newly approved deviation.

**MR03 misread — authority and proposed mechanics.** Binding OD-6 principle: a genuine misread of question data with unchanged object and difficulty costs one mark from A/B; all A/B follow through on the misread value and M/DM are judged as usual. Own-figure errors and misreads changing object/difficulty receive ordinary canonical marking. Practice feedback names the misread. Proposed MR03 operational rules, pending Vitalis approval of the exact manifest: decide and record eligibility once at first use; ineligible data remain canonical in every later part. For each eligible misread datum, first mark all gross evidence and dependencies, then deduct one mark from the first earned A/B on that datum in question/criterion order, moving to later-use parts if necessary. Deduct nothing only if no A/B is earned on the datum anywhere. Never deduct from M/DM or make the score negative. The selected criterion remains earned for every DM, dependency and www check; one datum costs at most one net mark. Eligible OD-6 follow-through overrides not-F.T. and c.a.o. restrictions, while correct working, named method exclusions and OD-1 still apply. No-solution exclusion means a misread removes a solution the canonical question has; a designed no-real-solution outcome remains eligible when its demand and difficulty are preserved. An A/B is on a datum when it lies in the datum's first-use part or a later part whose working uses the misread data, whether or not that criterion's own value changes. Eligibility is judged at first use for the connected question. Eligible follow-through never overrides MR09 (no F.T. into a supplied result) or OD-1 answer-only rules. Sources: NSSCAS 2025 report PDF345 item4 (CONVENTION108) and comparable Cambridge 9709_m16_ms_12.pdf PDF3 Penalties; the comparable allocation is not a published Namibian rule.

## Samples and Bloom

For the new normal $a=-2,b=3,c=4$:

| Submission/evidence | Credit | Feedback |
|---|---:|---|
| Correct modulus vertex/point recovery, all coefficients |3/3| All labels and orientation agree; no repair. |
| Bare $a=-2,b=3,c=4$ only, no wrong working |3/3| Official B1 www value awards. For practice, invite the learner to explain the vertex/point reasoning without withholding earned marks. |
| Correct complete formula $y=-2\lvert x+3\rvert+4$, no wrong working |3/3| Same official value awards as named fields; no format preference or invented working penalty. |
| Correct vertex reading $b=3,c=4$, then wrongly uses $0=a(x+3)^2+4$ at $(-1,0)$ and gets $a=-1$ |2/3| Preserve the valid vertex credit. “A modulus graph has straight arms. Substitute into $a\lvert x+3\rvert+4$, not a quadratic.” |
| Valid $a,c$ work but reads $b=-3$ |2/3| Set the inside expression to0 at vertex $x=-3$; the plus-sign form needs $b=3$. |
| Unreadable coefficient sign or ambiguous tuple order |pending| Clarify, preserve original; do not guess marks. |

Bloom proposal `8227-pilot-design-0.1.1`: part `a` Apply3, supported only by its B1/B2/B3 coefficient criteria; whole branch3. No sketch/Analyse demand is claimed. The improved discrimination domain does not itself raise Bloom.

Practice has optional answer-free generic support and a separately bound different-instance example; current solution follows submission. Test has no help before submission and retains existing review/timer/progress rules. Repeated or corrected work is after-feedback evidence, not mastery. Resource code never owns assignments, billing or progress.

## Checks, remaining limits and stop

Current D4 finite-domain check enumerates108 raw/44 admitted tuples, all named-error models, residuals and source exclusion; separately written `planning/d4/visual-exemplar-oracle.py` recomputes every changed exemplar. Three static diagrams are original stage-D assets with value/hash/render evidence, not a runtime generator. Stage E/F: replay seeds0/1/42/$2^{63}-1$, enumerate all44, test negative/crowded/origin cases, WWW/OD1/alternative/ambiguous submissions, semantic no-repeat/exhaustion and actual question/history rendering. Use the existing pinned learner-text guidelines; decoded math/labels must be legible and private criteria must not leak pre-submit.

Textbook originals remain internal. No runtime generation, app marking, import, assignment or production test is claimed. Next: Claude D4 changed-scope confirmation of this design, then Vitalis approves the exact plan/counts/gaps/capabilities/exemplars under OD-3. No commit or push.

OD-6 sources: NSSCAS 2025 examiner report PDF345 item4 (`CONVENTION:108`) and Cambridge International 9709/12 March2016 mark scheme PDF3, Penalties. The Cambridge convention is comparable-board evidence adopted by Vitalis, not a Namibian published allocation. The per-datum unit, deduction order, eligibility ledger and gross-before-net dependency mechanics are proposed operational rules in MR03, pending approval of the exact manifest; they are not further owner decisions. Practice feedback names the misread.
