# Work order — WB8227-principal-inverse

NSSCAS Mathematics 8227, December 2020 syllabus; Grade 12. Owner Vitalis. PLANNER Codex, 23 November 2026. Proposed version 0.1.0; owner approval and independent design review pending. Stage-D paper design only: these are not runtime items or an installed bank.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Identity, selection and purpose

Recipe `WB8227-principal-inverse`; selection `8227:D:SEL:principal-range`; accepted parent `8227:FAMILY:principal-values`. Two branches `admissible-linear` and `range-obstruction`, two marks each. New purpose-built recipe: it repairs a genuine syllabus-practice gap without turning defective2023 P1 Q9 into a learner anchor. Independent target: respect the **principal output range** of inverse sine before taking sine or solving for x. It is distinct from periodic trig equations and does not request all angle families.

## Evidence and scope

Syllabus PDF11/printed8 M1:T6:O04 explicitly requires the principal inverse relations. Exact special-angle values are O03. Cambridge9709 Paper12 Feb/March2016 Q4(a), PDF/printed2, asks sin^-1(3x)=-pi/3 for an exact solution. Matching scheme PDF/printed4 awards M1 for3x=-sqrt(3)/2 and A1 for x=-sqrt(3)/6. Both pages were visually read this stage. This is **comparable-examination-observed (Cambridge9709)**, not a Namibian observation. Exact document paths, hashes and attribution fields are in the design JSON and source-read register.

The `admissible-linear` branch has a part-scoped same-type reference to that Cambridge item: same two directly assessed demands, symbolic response, exact principal-angle then linear recovery, no other source parts. The `range-obstruction` branch is **syllabus-derived, not examination-evidenced**; proposed2-mark explanation criteria. The defective NSSCAS2023 P1 Q9 is internal related motivation only, `learner_display:false`; it is not an original or same-type learner reference. Cambridge2015 quartic and2023 compound inverse equations are wider variety leads; their algebra/compound demands are not silently inherited.

Read every member of `principal-inverse-values` (4) and `principal-inverse-calculator-illustrations` (3), on YM PDF215–217/printed203–205. They illustrate principal outputs and degree/radian special angles; they do not supply official marking. The printed YM tangent interval includes endpoints incorrectly; the correct inverse tangent output range is open. No textbook diagram or statement is reproduced to learners. Union discovery finds34 assessed/component-linked inventory items; this plan does not label unread candidates as absence evidence.

Grade boundary E:06, syllabus PDF23, directly supports principal-value notation; the admissible special-angle equation uses routine exact algebra and lies within that objective. E:12/C:12/A:13 are supporting trigonometry calibration, not new scope. No inverse differentiation, no unrestricted trig solutions, no reciprocal notation confusion. Cosine/tangent principal values, axis targets0,+/-pi/2 and nonlinear-inner equations remain visible later facets, not fully covered by this sine-only pilot.

## Branches, parts and classification

| Branch / part | Direct demand IDs (prefix8227:2020:) | Prerequisites | Marks | Proposed Bloom, criterion link |
|---|---|---|---:|---|
| admissible-linear / p-solve | M1:T6:O04:D01; M1:T6:O03:D01 | Linear equation manipulation |2|Apply3: V-M1 takes sine at the specified exact angle after respecting the principal range; V-A1 recovers the unique exact x |
| range-obstruction / p-explain | M1:T6:O04:D01 | Comparing exact angles with an interval |2|Understand2: X-B1 gives the inverse-sine principal interval and X-B2 uses it to explain impossibility; this is not Evaluate merely because it rejects an equation |

Whole branch maximum is3 for admissible-linear and2 for range-obstruction. The second branch must not inherit3 from its sibling. Both classifications are proposed, criterion-linked and version0.1.0; independent approval pending.

## Finite domains, invalid cases and assets

Both branches supply the textual equation arcsin(kx)=theta with integer k in{2,3,4,5}, radians explicitly stated and the requested response explained. `admissible-linear`: theta in{+/-pi/6,+/-pi/4,+/-pi/3}. **24** distinct admitted equations. `range-obstruction`: theta in{+/-2pi/3,+/-3pi/4,+/-pi}. **24** distinct admitted no-real-solution equations. Total48 across two non-interchangeable branches; labels/contexts do not increase it. Every valid branch equation has exactly one real x=sin(theta)/k. Every obstruction equation has no real x irrespective of its forward-sine image.

The branch definitions exclude k=0 because it destroys unique recovery; exclude arbitrary irrational target angles to preserve exact-special-angle demand; reject degree/radian mixing and an absent unit. An axis target is mathematically valid when in the principal range, but outside this **pilot branch**, not a false mathematical impossibility. A target within[-pi/2,pi/2] cannot be sent to obstruction. Do not silently change branch to obtain desired marks or Bloom.

Given representation is text; must-read givens are the inverse symbol, argument kx, sign/exact angle and radians. No diagram is needed for the question. Optional solution diagram: inverse-sine range on a labelled vertical line, no scale-measurement claim. Fixed interval endpoints are +/-pi/2; variable target marker is placed from the exact same theta; its location must agree with the explanation. This is teaching support, not extra assessed sketch work.

Use semantic identity(version,branch,k,theta,angle-unit,response-format), not seed or label, for no-repeat and exhaustion. At24 identities for a branch return explicit exhaustion and request a different approved branch or reset with repeat disclosure; never pretend a repeated answer is new mastery. App owns history and test reservation. No generator exists in this stage.

## Solutions and memo

Admissible: first verify theta belongs to[-pi/2,pi/2]. Taking sine is then reversible for this equation; kx=sin(theta), so x=sin(theta)/k, automatically kx in[-1,1]. Substitute in the **inverse** relation, not only in sin(theta). V-M1 (1) is the exact forward ratio/reversible transformation; V-A1 (1) is the correct simplified exact x. This adapts the two Cambridge awards. Equivalent rationalised or unrationalised surds accepted. Visible exact ratio with a later division slip earns1/2. Correct exact x alone earns2/2 by implied transformation in this simple two-mark equation (proposed application of the ordinary implied-method convention; reviewer to confirm). An approximate or rounded decimal-only final response fails the exact A1, but an evidenced exact method can retain M1. No generic no-working deduction.

Obstruction: X-B1 (1) states arcsin(real input) lies in[-pi/2,pi/2] (or equivalent correct range comparison); X-B2 (1) concludes there is no real solution because the supplied target is outside it. 'No real solution' alone earns X-B2 only (1/2); a wrong reason such as kx>1 does not earn the range award. Proposed criteria, not an official memo. A forward-sine value obtained after ignoring range is not a solution and earns0 unless a correct range fact was separately established. No follow-through turns an out-of-range target into a valid branch. No duplicate credit for stating the interval twice.

## Response examples and guidance

For arcsin(4x)=-pi/6, complete exact working to x=-1/8 earns2/2; '4x=-1/2, x=-1/2' earns1/2: 'You used the correct exact sine value. Divide by4 to isolate x.' Decimal x=-0.125 is exact but the requested exact form accepts a terminating decimal as exact rational only if clearly exact; approximate notation -0.13 earns at most evidenced method credit. The equivalent x=-2/16 is accepted. Writing both +/-1/8 loses the unique-solution accuracy award; feedback identifies the unsupported second sign rather than guessing a misconception. If the minus sign is illegible, request clarification and keep marking pending.

For arcsin(4x)=2pi/3, the interval plus conclusion earns2/2; 'no real solution' alone earns1/2; x=sqrt(3)/8 based only on taking sine earns0: 'Taking sine loses the principal-range restriction. Can arcsin return2pi/3?' A full-credit explanation gets no repair. Before submission a general hint may remind the learner to distinguish inverse sine from reciprocal sine without supplying the target-specific conclusion.

Outstanding review: approve this sine-only pilot and its explicit deferred facets, exact-answer convention, implied method and the syllabus-derived explanation memo. Capability need is ordinary symbolic/explanation input with exact surd equivalence; implementation and marker reliability are unverified, not a reason to weaken the target. See [exemplar](../exemplars/WB8227-principal-inverse.md).

## Shared boundaries and later checks

Use [recipe-contract.md](../recipe-contract.md), [subject-rules.md](../subject-rules.md), shared Bloom policy and the 7 November 2026 learner-text guideline snapshots under `workbench/playbook/guidelines/` with their recorded `provenance.json` hashes. This work order fixes the content decisions; it does not claim those draft metadata fields are accepted by the app. Retain source version, branch, part and criterion identities in the eventual frozen instance. Retain original attempts and historical classifications.

Practice permits another admitted instance without passing first. Before submission offer only an answer-free strategy or a separately identified different-instance example; neither exposes the current canonical solution. After submission show earned credit, the first evidenced issue, repair steps and the full authored solution. A correct solution receives no invented repair. In Workbench Test provide no hints/examples/tutor for an unsubmitted question; preserve question-by-question post-submission review and existing nonfinal two-minute review/early-advance/expiry behavior. Later same-recipe questions after feedback are after-feedback observations, not wholly unaided evidence. No mastery or memory-box change is inferred by this resource.

An unreadable, ambiguous or incomplete submission requests clarification with marking pending; it is not automatically wrong. Number/format adapters may normalise an equivalent value, never change mathematics or invent missing method. No app-owned learner attempt or progress belongs in the content package. Textbook originals and their diagrams remain internal (`learner_display: false`); the paper exemplar questions below are newly authored. NSSCAS/Cambridge originals may be quoted with attribution under Vitalis's instruction, but publication and assignment remain unauthorised.

Future E–F checks: independently enumerate the finite admitted mathematical identities; compare question, solution, marking and assets to the same values; check all named examples and rejected boundaries. Use a separately implemented substitution/inverse oracle, not the answer constructor. Replay seeds 0,1,42,2**63-1 once an implementation exists; use at least64 draws or exhaust the smaller finite branch. Check correct, partial, wrong, alternative and ambiguous submissions, branch-specific same-type labels, no-repeat/exhaustion, decoded Markdown/LaTeX and actual app rendering/reveal timing. Runtime generation, marking and app-render checks are **not run** in stage D. Offline mathematical-syntax and static paper-diagram checks are reported separately. Source/author calculations do not establish independent acceptance.
