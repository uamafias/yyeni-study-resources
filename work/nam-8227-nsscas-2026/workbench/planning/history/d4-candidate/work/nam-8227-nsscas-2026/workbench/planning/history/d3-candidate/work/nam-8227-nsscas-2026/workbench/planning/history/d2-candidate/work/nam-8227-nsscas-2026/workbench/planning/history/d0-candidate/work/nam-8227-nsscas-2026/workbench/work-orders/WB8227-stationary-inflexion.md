# Locate and classify stationary points, including an inflexion

NSSCAS Mathematics 8227, December 2020 syllabus; Grade 12. Owner Vitalis; PLANNER Codex (calculus assistant), 23 November 2026. Recipe `WB8227-stationary-inflexion`, proposed version `0.1.0`; owner approval pending. This is a stage-D paper design, not an enabled recipe.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Purpose, reuse and source scope

Selections `8227:SEL-D:stationary-two-extrema` and `8227:SEL-D:stationary-inflexion`. A new purpose-built recipe with two branches, using one cubic derivative/classification structure. The stationary-inflexion branch cannot inherit a min/max examination label. It directly assesses the syllabus-required facet absent from a usable NSSCAS exemplar, rather than dropping it because recent papers emphasise maxima/minima. No automatic supporting-drill bank is proposed.

Syllabus PDF12 / printed9, M1:T8 O02 and O04. `8227:2020:M1:T8:O04:D02` explicitly includes maximum, minimum and points of inflexion. All ten members of textbook family `stationary-classify-sketch` were read: YM Example26/27/28 and Try26/27/28, PDF297–300 / printed285–288; Goldie4A Q3 PDF102 / printed88 and4B Q6/Q9 PDF109 / printed95. The adopted derivative-sign method is read from actual YM worked pages, including Example27's x³+1 stationary inflexion. Its line '(0,-1)' conflicts with its function, earlier coordinates and graph; the correct point is (0,1). Preserve the registered defect; do not reuse that wrong line. Full member/search identities are in `planning/calculus-source-reads.json`.

2024 P2 Q10 PDF/printed15 and report2024 PDF342 / printed340 demonstrate stationary solving and second-derivative classification with a logarithmic function; they are related internal references, not a same-type label for a polynomial two-extrema or stationary-inflexion branch. No whole-branch NSSCAS/Cambridge same-type claim is proposed. Examinations test the broader skill; the inflexion facet is syllabus-derived and textbook supported. The official log-question tariff is4+2; the proposed polynomial tariff is independently specified below.

Calibration: Grade c `8227:GRADE:C:08` PDF21 / printed18 and Grade a `8227:GRADE:A:08` PDF20 / printed17 both explicitly include stationary classification/inflexion. Grade e `E:08` PDF23 / printed20 supplies derivative notation, not full classification scope. Source cubics include coefficients beyond these chosen small leading coefficients; our bounds preserve low-degree derivatives and factorable stationary equations. Bounds are proposed design choices, not promised grade outcomes.

## Domains, variation and response

Branch `WB8227-stationary-inflexion:two-extrema`: f(x)=a[(x-h)³-3r²(x-h)]+c. a∈{-2,-1,1,2}, h∈{-2,-1,0,1,2}, r∈{1,2,3}, c∈{-4,-3,-2,-1,0,1,2,3,4}; exactly4×5×3×9=540 distinct expanded polynomials. Ask (points) coordinates of both stationary points,4 marks; (nature) classify each with justification,2 marks. Formula is supplied expanded in the later authored question; shifted form is canonical design identity, not pre-given answer scaffolding. Points h±r and their y values are required.

Branch `WB8227-stationary-inflexion:stationary-inflexion`: f(x)=a(x-h)³+c with a,h,c in the same respective sets; exactly4×5×9=180. Ask (point) locate the stationary point,3; (classification) explain whether y''=0 settles its nature, then classify with derivative/concavity evidence,3. This added reasoning is the branch discriminator, not a cosmetic coefficient change. Supply expanded cubic, not the shifted-root answer form.

Both domains exclude a=0, noninteger h/r/c and r=0 in two-extrema (the latter changes branch). Exclude quartic flat extrema, nonstationary inflexions and rational/log/trig functions from these branch domains. Cases stay within cubic algebra, power differentiation, a quadratic or repeated-square stationary equation and sign/concavity classification. The two domains are disjoint: one has two simple derivative roots, the other one double derivative root. Capacity720 total branch-qualified exact polynomials; count from canonical expanded coefficients, not factor-order rewrites or renamed functions. App-owned no-repeat scope must report exhaustion at540/180; do not silently move a pupil to a different branch.

Given representation: text; must read all coefficients/signs and requested coordinates versus nature. No given asset is needed. Response is symbolic plus explanation; a derivative sign chart or correctly labelled local sketch can be valid evidence, but a bare picture without the decisive signs is not automatic proof. Optional feedback figures must use the same polynomial, show axes, stationary coordinates and whether concavity changes; diagrams are not to scale unless explicitly calibrated. No measuring a screen; no fixed source image.

## Canonical working, awards and classification

Two-extrema: f'=3a[(x-h)²-r²]=0 gives x=h-r,h+r. Substitute into f to get (h-r,c+2ar³) and (h+r,c-2ar³). f''=6a(x-h): left point has sign -a and right +a. For a>0, left maximum/right minimum; for a<0, left minimum/right maximum. Valid alternatives: derivative signs or local value comparison with a justified neighbourhood; algebraic second-derivative evaluation is not compulsory.

Inflexion: f'=3a(x-h)²; stationary point(h,c). f''=6a(x-h) equals0 at h, so that value alone is inconclusive. f' has the same sign on either side, excluding maximum/minimum, while f'' changes sign across h, establishing a stationary inflexion. A cubic's horizontal tangent and verified concavity change is equivalent evidence. No automatic rule 'second derivative zero means inflexion'.

| Branch/part | Suffix awards (all proposed) | Dependencies, exactness and answer-only rule |
|---|---|---|
| two-extrema/points4 | P1 B1 correct derivative; P2 M1 solve f'=0; P3 A1 both x values; P4 A1 both complete coordinates | P2 allows their credible derivative; canonical accuracy for P3/P4. Coordinates alone earn P3/P4=2/4, not unshown derivative/solve evidence. |
| two-extrema/nature2 | C1 M1 valid sign/second-derivative test at both points; C2 A1 both correct types linked to evidence | C1 follows through plausible stationary roots from points, using original f. C2 canonical types. Bare names with no justification earn0/2 because the prompt asks a justified classification. |
| stationary-inflexion/point3 | I1 B1 derivative; I2 M1 set it zero and solve; I3 A1 exact point | A correct coordinate alone earns I3=1/3. No duplicate award for expanding a cubic. |
| stationary-inflexion/classification3 | I4 B1 explain f''(h)=0 alone inconclusive; I5 M1 test signs/concavity on both sides; I6 A1 justified stationary-inflexion conclusion | I6 requires I5. Correct phrase 'stationary inflexion' alone earns 0/3; an unlabelled S-shaped doodle is insufficient. A coherent first-derivative test plus explicit concavity evidence is accepted. |

Dependencies point→nature are cue/reused-coordinate edges; C1/I5 follow-through is separate and must name the plausible inherited coordinate. Earlier arithmetic errors may preserve method evidence but cannot turn a nonstationary point into a canonical inflexion. All criteria are alternative-method slots: maximum 6, never summing two methods or giving extra marks for a graph. Inputs and answers exact; no units or rounding. These answer-only decisions are proposed evidence rules, not a blanket working penalty copied from another recipe.

Bloom proposal: points3 Apply and nature3 Apply in two-extrema, maximum 3. For stationary-inflexion, point3 Apply; classification4 Analyse because I4–I6 require separating inconclusive second-derivative information from a justified neighbourhood/concavity decision. Maximum4, not inherited by two-extrema. Marking must continue to require that analysis for the label to be retained; a routine 'name the cubic' version needs reclassification. Independent review pending.

## Sample work and feedback

Normal two-extrema f=x³-3x+2: correct f'=3x²-3, points(-1,4),(1,0), and f'' values-6,+6 with maximum/minimum gives 6/6. Alternative derivative-sign chart +,−,+ gives the same6. Partial work with the correct derivative and stationary equation/solve shown, and correct x values but y=−1,1, earns P1/P2/P3=3/4; use the original f to find y, not the derivative. Wrong 'minimum at both because f'=0' loses nature marks; feedback says stationarity does not determine type and asks for the signs around each point.

Normal inflexion f=(x-1)³-2 (later displayed expanded): correct point (1,-2), f''(1)=0 inconclusive, f''=6(x-1) changes−to+ and f' positive either side gives 6/6. Partial work showing the correct derivative, stationary equation/solve and point, followed only by 'f''=0, so inflexion', earns 3/6, not classification credit. A bare correct coordinate with that unsupported classification earns only I3=1/6. Alternative signed local concavity sketch with the derivative calculation can earn I5/I6. Ambiguous sign chart without which side is left/right requires clarification; do not infer the intended orientation. A correct stationary-point coordinate alone is not evidence of the requested classification.

Normal/changed/boundary cases for both branches are in `exemplars/WB8227-stationary-inflexion.md`. Full curve sketch and x-intercept solving are deliberately not assessed in this pilot: those textbook responses remain visible as deferred facets.

## Practice, feedback and mode boundary

Before submission, offer answer-free method reminders or a worked example with a different branch-qualified fingerprint. Do not reveal current answers through hints, asset URLs, alt text or diagram labels. A learner may request another instance without first passing. Preserve original work; correction is an after-feedback observation, not evidence of unaided mastery. Full-credit work gets confirmation and no invented repair. For unclear handwriting or ambiguous units, request clarification rather than fabricate a mark. Test gives no hints/example/tutor on an unsubmitted question, retains question-by-question post-submission feedback and the existing review/timing rules; no test policy change is proposed.

## Guideline, validation and release requirements

Use the pinned learner-text authorities in `workbench/playbook/guidelines/provenance.json` and shared Bloom policy. Question, example, feedback, solution and history surfaces need decoded LaTeX and actual app-render inspection at E/F; a Markdown design is not that proof. Interpret source text from rendered pages, not the damaged notes or family distinction/precision templates. Newly authored wording is used here; owner-authorised exam originals may be shown only with their original attribution, never as generated variants. Textbook problem text/artwork remains internal (`learner_display: false`).

At E/F, independently check the full declared finite domains (all are below 1,000 tuples per branch), then replay seeds 0, 1, 42 and 2**63-1 and at least 64 valid draws per branch; small domains permit repeats in draw tests but not false claims of 64 distinct questions. Exhaust each small domain and verify safe exhaustion, no-repeat registry scope and exact answer equivalence. Freeze version, branch, parameters, deterministic engine/asset versions, seed and canonical fingerprint. Render sample/boundary/ambiguous responses. An oracle must use substitution/differentiation, explicit roots or geometric areas, not call the answer constructor twice.

Marking, Bloom and finite domain proposals need cross-vendor branch review and Vitalis's design approval. Automated resource checks, diagram input/feedback and application capability acceptance are unrun. Owner decision 6 includes visual work; nothing is silently held for capability. Flag actual runtime requirements to Vitalis through the common plan handoff. No runtime item, generator or deck is created by this work order.
