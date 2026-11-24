# Differentiate an implicit exponential curve and use its gradient

NSSCAS Mathematics 8227, December 2020 syllabus; Grade 12. Owner Vitalis; PLANNER Codex (calculus assistant), 23 November 2026. Recipe `WB8227-implicit-normal`, proposed version `0.1.0`; owner approval pending. This is a stage-D paper design, not an enabled recipe.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Purpose, reuse and evidence

Select `8227:SEL-D:implicit-exponential-point` and `8227:SEL-D:implicit-normal-extension`. New purpose-built 8227 design using the existing framework; no Flashcard Studio conversion or claim that a lower-syllabus recipe already satisfies it. The shared derivative core is reused between two branches; the normal extension is not a second recipe because the given curve, point and derivative are unchanged and only the connected geometry output extends them. It remains a separately reviewable branch/teacher choice.

Syllabus PDF p15 / printed12, M2:T4 O01/O02/O03; normal geometry also PDF12 / printed9, M1:T8 O03. All full demand IDs are in `planning/calculus-design.json`. Prerequisites: power rule, differentiation of exponential, point-slope line and negative reciprocal. No parametric differentiation, singular-point classification, trigonometric implicit proof or curve-again intersection is included.

Native evidence: 2025 P2 Q5, PDF/printed5; report2025 PDF359 / printed357, five official awards. It permits substitution before isolating dy/dx and warns about omission of dy/dx and derivative-of-constant zero. The 2023 P2 Q8, PDF/printed14, report2023 PDF339 / printed337 is related evidence: its derivative is a supplied show-that result and its point must be recovered from the y-axis. Those extra requirements are not silently inherited. Source file paths/hashes, native reads and award criterion IDs are in `planning/calculus-source-reads.json`.

All six members of `implicit-given-point-gradient` and the one member of `implicit-linked-normal-curve-sketch` were read: Goldie 4D Q2/Q3/Q6, PDF121 / printed107; YM Example29 and Try29 Q1–3, PDF510 / printed498. Goldie Q6(ii) supports a connected normal equation; its later intersection/asymptote/sketch responses are excluded. YM Try29 Q3 is the closest exponential-product point-gradient source. The accepted item-level assessed/component union supplied the discovery pool, not only positive relations. Other union hits remain later-design leads; they are not rejected without page reads.

Grade calibration: easiest proposed point-gradient instances align with Grade c descriptor `8227:GRADE:C:13` (PDF22 / printed19); upper complexity stays within Grade a `8227:GRADE:A:14` (PDF20 / printed17), which explicitly includes product and implicit differentiation. Grade e elementary composites are prerequisite support, not a claim that this full pattern is Grade e. Numeric bounds are planner-chosen within these source structures, not official grade cut-offs.

## Branches, parameter domain and assets

Both branches supply, in text, a curve a exp(kx)y + y² = q(q+a) and the point (0,q). Domains: integer a in {1,2,3,4}, k in {1,2,3}, q in {-5,-4,-3,-2,-1}; exclude a+2q=0 (vertical/singular gradient) and q=-a (constant zero permits factorisation that changes the intended implicit demand). Exactly 42 tuples survive, exhaustively counted; gradient is nonzero. The normal branch adds the normal equation to the same gradient task. These are 42+42=84 branch-qualified fingerprints, not 84 independent curriculum demands. Do not count renamed coordinates/context as new capacity.

`WB8227-implicit-normal:gradient`: one part `gradient`, 5 marks. `WB8227-implicit-normal:normal`: `gradient` (5) then `normal` (2), total7. New values vary the curve, sign/magnitude of gradient and normal; all preserve product plus exponential chain and implicit y² differentiation. Proposed invariant ceiling: one exponential product, one y² term, a supplied x=0 point and a nonzero finite slope. No logarithms, added trig functions, point recovery or show-that scaffolding without a new branch review.

Given representation: text; must read the complete exponent kx, multiplication by y, constant q(q+a), supplied coordinate order and requested outputs. No given diagram or response drawing is required. Optional solution diagrams must be generated from this same implicit curve and local gradient, with labelled point, axis units dimensionless and tangent/normal perpendicular; do not measure an arbitrary screen. Marker accepts symbolic derivation and equivalent affine normal forms. There is no fixed textbook image in the question.

Fingerprint is a canonical serialization of curriculum, recipe/version, branch and (a,k,q), plus output-affecting contract/asset revision; source names are not identity. No repeats within the app-owned relevant exposure scope; exhaust after42 fresh instances of a branch and report exhaustion honestly. Never silently reseed or loosen exclusions.

## Canonical solution and criteria

Action: differentiate the curve holding y=y(x). Reason: both factors of a exp(kx)y depend on x and d(y²)/dx=2y y'. Result: a k exp(kx)y + a exp(kx)y' + 2y y'=0. Substitute (0,q) before rearranging, or isolate first: m=-akq/(a+2q). The normal is y-q=(a+2q)/(akq) x. Exact fractions, equivalent terminating decimals and algebraically equivalent line forms are accepted; no rounding is needed. No physical units.

Awards below are proposed adaptations of the five official 2025 awards, not an official normal memo. All criterion IDs are recipe/version/branch-qualified using the suffixes below. Gradient direct demands: M2:T4 O03:D01, O02:D01, O01:D02, O03:D03. The atomic exponential derivative O01:D01 is prerequisite here; do not add an inferred direct source tag.

| Suffix | Award | Evidence and dependency |
|---|---|---|
| G1 | M1 | Product-rule attempt differentiates both factors; one numeric slip allowed, omission of a factor not allowed. |
| G2 | A1 | Correct exponential product derivative a k exp(kx)y + a exp(kx)y'; depends on G1. |
| G3 | B1 | 2y y' and derivative of constant zero correctly present. |
| G4 | M1 | Substitute the supplied point into the differentiated relation and solve for y'; requires at least G1 or G3, as the source allows. |
| G5 | A1 | Correct exact finite gradient; canonical accuracy, not follow-through. |
| N1 | M1 | Use negative reciprocal of the finite nonzero gradient; follow through a credible nonzero arithmetic-error slope from the derivative. |
| N2 | A1 | Correct line through (0,q) with canonical normal slope; canonical accuracy. |

Connected dependency: gradient→normal is a cue/reused result; N1 follow-through is separately typed and limited to the learner's credible finite nonzero derivative. It cannot reward zero/undefined slopes or unsupported guesses. No extra independent mark for rearranging a line; alternative derivations compete for the same slots, maximum 5 or7. No award is counted twice under symbolic rearrangement and implicit substitution routes.

Answer-only: correct numeric gradient alone earns G5 only (1/5); it does not demonstrate the four derivative/setup awards. A correct differentiated relation and substitution can demonstrate the method even without explanatory prose. An exact correct normal equation alone earns N1+N2 (2/7) in the extended branch because it encodes the required perpendicular line; absent earlier derivative work does not earn G1–G4. This is the proposed evidence-specific policy, not a universal working penalty. Equivalent direct differentiation of a locally solved explicit quadratic branch is accepted if it proves the same method/point facts; the point must stay on the intended local branch.

Explicit-quadratic alternative (exclusive path, same five slots and five-mark cap): put $C=q(q+a)$ and $D(x)=a^2e^{2kx}+4C$. The locally correct root is

$$
y(x)=\frac{-ae^{kx}+\sigma\sqrt{D(x)}}{2},\qquad \sigma=\operatorname{sign}(a+2q).
$$

At $x=0$, $D(0)=(a+2q)^2>0$, so this selects the supplied point and a real local branch. Its derivative is

$$
y'(x)=\frac12\left(-ake^{kx}+\frac{\sigma a^2k e^{2kx}}{\sqrt{D(x)}}\right).
$$

The alternative award mapping is: G1 M1 for a valid quadratic-solving attempt from the original curve; G2 A1 for the correct local explicit branch through the supplied point; G3 B1 for the correct exponential/root-chain derivative; G4 M1 for point substitution and simplification; G5 A1 for the canonical exact gradient. This path replaces, never adds to, the implicit-path awards. Mixed work fills each evidence slot at most once, with no credit for an inconsistent root or an unproved explicit expression. Either complete valid path earns 5/5. Normal N1/N2 are unchanged. These alternative awards are proposed, not transcribed official criteria. Method-path records must distinguish the demonstrated root-chain route from product/implicit differentiation; full recipe credit is not a claim that every possible method facet was demonstrated.

Bloom proposal: each assessed part is Level3 Apply, linked to G1–G5 and N1–N2 respectively. A standard implicit/product/chain procedure and point-slope substitution are required; the expression's sophistication does not make it Analyse. Both complete branches have maximum 3. Classification remains proposed pending independent review; a new singular-point, proof or point-recovery branch must be classified afresh.

## Sample submissions and feedback (normal tuple a=3,k=2,q=-4)

Correct: differentiated relation 6e^(2x)y+3e^(2x)y'+2y y'=0, then m=-24/5 and y+4=(5/24)x: 7/7. Confirm method and result; no repair.

Partial: correct product derivative but 2y in place of 2y y'; then unsupported slope. G1+G2=2/5, G3 absent; G4 only if a valid differentiated relation from G1 is actually substituted. Feedback: attach y' when differentiating y² because y depends on x; do not diagnose an unseen misconception.

Alternative: isolate y'= -6e^(2x)y/(3e^(2x)+2y), then substitute: full gradient5. Equivalent 5x-24y-96=0 is the same normal, full2.

Wrong: m=24/5 with otherwise correct differentiated equation and an arithmetic sign slip: G1,G2,G3,G4=4/5; N1 may follow through -5/24, N2 fails. Feedback points to collecting the y' coefficients at the actual point.

Ambiguous: a photograph where '-24/5' could be '-24/3' needs clarification; preserve the original and keep affected accuracy unresolved. Do not invent a numerical mark from uncertain reading. Numeric-only -24/5 earns1/5 under the stated proposed policy.

Worked normal/changed/boundary examples and rejected tuples: `exemplars/WB8227-implicit-normal.md`.

## Practice, feedback and mode boundary

Before submission, offer answer-free method reminders or a worked example with a different branch-qualified fingerprint. Do not reveal current answers through hints, asset URLs, alt text or diagram labels. A learner may request another instance without first passing. Preserve original work; correction is an after-feedback observation, not evidence of unaided mastery. Full-credit work gets confirmation and no invented repair. For unclear handwriting or ambiguous units, request clarification rather than fabricate a mark. Test gives no hints/example/tutor on an unsubmitted question, retains question-by-question post-submission feedback and the existing review/timing rules; no test policy change is proposed.

## Guideline, validation and release requirements

Use the pinned learner-text authorities in `workbench/playbook/guidelines/provenance.json` and shared Bloom policy. Question, example, feedback, solution and history surfaces need decoded LaTeX and actual app-render inspection at E/F; a Markdown design is not that proof. Interpret source text from rendered pages, not the damaged notes or family distinction/precision templates. Newly authored wording is used here; owner-authorised exam originals may be shown only with their original attribution, never as generated variants. Textbook problem text/artwork remains internal (`learner_display: false`).

At E/F, independently check the full declared finite domains (all are below 1,000 tuples per branch), then replay seeds 0, 1, 42 and 2**63-1 and at least 64 valid draws per branch; small domains permit repeats in draw tests but not false claims of 64 distinct questions. Exhaust each small domain and verify safe exhaustion, no-repeat registry scope and exact answer equivalence. Freeze version, branch, parameters, deterministic engine/asset versions, seed and canonical fingerprint. Render sample/boundary/ambiguous responses. An oracle must use substitution/differentiation, explicit roots or geometric areas, not call the answer constructor twice.

Marking, Bloom and finite domain proposals need cross-vendor branch review and Vitalis's design approval. Automated resource checks, diagram input/feedback and application capability acceptance are unrun. Owner decision 6 includes visual work; nothing is silently held for capability. Flag actual runtime requirements to Vitalis through the common plan handoff. No runtime item, generator or deck is created by this work order.
