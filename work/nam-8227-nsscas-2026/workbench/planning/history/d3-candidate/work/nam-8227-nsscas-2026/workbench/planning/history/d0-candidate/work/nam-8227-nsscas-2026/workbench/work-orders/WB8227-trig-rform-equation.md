# Work order — WB8227-trig-rform-equation

NSSCAS Mathematics 8227, December 2020 syllabus; Grade 12. Owner Vitalis. PLANNER Codex, 23 November 2026. Proposed version 0.1.0; owner approval and independent design review pending. Stage-D paper design only: these are not runtime items or an installed bank.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Identity, selection and purpose

Recipe `WB8227-trig-rform-equation`; selection `8227:D:SEL:rform-connected`; accepted parents `8227:FAMILY:r-form` and `8227:FAMILY:bounded-trig`. One proposed branch `degree-cycle`, two assessed parts `a-convert` and `b-roots`, seven marks. New purpose-built recipe, extending the existing Workbench workflow; no Flashcard Studio material is an input. It is separate from inverse-principal work because its evidence is a complete finite periodic root set, not one inverse-function output.

Target: match coefficients to rewrite a two-term same-frequency expression, then use that result and the shifted interval to recover **all** allowed roots. The two parts stay connected. Omitting the terminal extrema request of the exam anchor does not turn every exam subpart into a standalone recipe: YM Try Now19 Q1 directly evidences a conversion→hence-equation practice unit. Extra extrema, reciprocal reduction, higher harmonics and radian variants are deferred, not covered by this pilot.

## Sources and author page evidence

Authority: syllabus PDF p15/printed12 M2:T3:O02, and PDF p11/printed8 M1:T6:O06. Paper `2022 P2 Q6(a),(b)(i)`, PDF/printed8; original coefficient is **sqrt(5)**, not5. Examiner report2022 PDF313/printed311 gives B1/M1/A1 for conversion and M1/DM1/A1/A1 for roots, including follow-through and two-answer cap. The exact source paths/hashes and native reads are in `planning/trig-model-source-reads.json`. Official awards are pattern evidence; applying them to new coefficients, negative right sides and the zero boundary below is a **proposed adaptation**, not an official award for our questions.

All members of adopted families `rform-coefficient-conversion` (5) and `rform-solve-cycle` (13) were page-read, including each question and continuation. Best two-part textbook exemplar: YM C10 Try Now19 Q1, PDF470/printed458; it has conversion then roots for a positive combination. Goldie3D11–14 PDF91/printed77 show alternative target forms and domains; YM Examples20–21 show cosine and radian demands, deferred here. The rendering on YM469 has a plus/minus inconsistency in an intermediate identity; no such line is imported. Union-link discovery finds41 inventory items, not just established relations; unselected candidate items remain leads, not negative design evidence. See source-read record for limits.

Grade calibration: E:12 (syllabus PDF23) supports the conversion; C:12 (PDF22) supports equations after conversion; A:06/A:13 (PDF19/20) caps complex identities/equations. The admitted small-coefficient, one-cycle, no-reciprocal domain stays within the observed structures. Numerical endpoints are planner-chosen conservative bounds, pending independent calibration; no exemplar is advertised as a guaranteed grade.

## Parts, demand and Bloom

| Part | Directly assessed demand IDs (prefix8227:2020:) | Prerequisites/components | Marks | Proposed Bloom and criterion evidence |
|---|---|---|---:|---|
| a-convert | M2:T3:O02:D04 | Compound-angle expansion M2:T3:O02:D02 supports coefficient matching, not separately assessed as proof |3|Apply3: a-B1/a-M1/a-A1 apply a specified representation and phase restriction |
| b-roots | M2:T3:O02:D05; M1:T6:O06:D01,D02 | a-convert; calculator inverse and algebra |4|Apply3: b-M1/b-M2/b-A1/b-A2 solve the transformed finite-interval equation and retain the allowed root set |

Whole branch maximum3, from both classified parts. Labels are proposed perversion/branch; no accidental inheritance from another recipe or a sophisticated worked solution. Classification changes if extra proof, model or selection demands are introduced.

## Branch/domain, givens and capacity

Branch `degree-cycle`: integers a,b in{1,2,3,4}, c in{-3,-2,-1,0,1,2,3}; require c²<a²+b², c!=b, gcd(a,b,abs(c))=1. The requested form is R sin(theta+alpha), R>0, 0<alpha<90degrees. The equation is a sin(theta)+b cos(theta)=c for **0<theta<360degrees**. Ask exact R, alpha to2 decimal places, final roots to1 decimal place, retaining unrounded alpha for later working.

The inequalities enforce two distinct interior roots and avoid a root at either excluded endpoint. gcd normalisation rejects scalar duplicates. The90 raw admitted tuples reduce to **78** primitive mathematical tuples; independent integer enumeration checked this count. This is finite semantic capacity, not unlimited renewal. A change of c from positive to negative changes the quadrants needed; c=0 is an admitted axis-root boundary. a,b changes vary both coefficient mapping and phase. Context names/formatting do not increase capacity.

Question asset: text only, with expressions, target form, phase range, degree interval and precision explicitly supplied. No source diagram is reused. Optional post-submission solution sketch must be generated from the same a,b,c and label the shifted interval and both intersections; it is not required learner evidence in this branch.

Fingerprint the version,branch,normalised(a,b,c),response requirements, angle interval and precision. Exclude repeats across current practice/test history at that semantic scope. After78 identities return an explicit exhausted result; do not silently recycle, perturb labels or retry forever. Test selection reserves unused identities first and reports shortage before starting a round. The app owns the actual attempt history and reservation.

## Canonical solution and marking

Expand R sin(theta+alpha)=R cos(alpha)sin(theta)+R sin(alpha)cos(theta). Equate a=R cos(alpha), b=R sin(alpha); hence R=sqrt(a²+b²), alpha=atan2(b,a) in degrees. Set sin(theta+alpha)=c/R; shift **the full interval** to alpha<theta+alpha<360+alpha; enumerate both sine branches there and subtract alpha. Substitute all candidates in the original equation and apply the original strict bounds. Exact equivalent phase forms accepted only if they satisfy the requested form/range; roots from other valid trigonometric methods receive the accuracy credit and any method slots actually demonstrated.

| Criterion | Award | Evidence and dependency |
|---|---|---|
| a-B1 | B1 | Exact positive R |
| a-M1 | M1 | Correct coefficient equations or tan(alpha)=b/a with the specified positive phase |
| a-A1 | A1 | Correct alpha to2dp; dependent on a coherent coefficient method |
| b-M1 | M1 FT | Correctly make sin(theta+their alpha)=c/their R; follow through positive R and admissible acute phase |
| b-M2 | M1 dependent | Both sine branches searched over the shifted interval; depends on b-M1 |
| b-A1,b-A2 | A1 each | Two correct original-equation roots to1dp; accuracy credit may be awarded without b-M2, matching the source distinction |

Part totals3+4=7. If more than two inequivalent roots are submitted, b-A2 is not awarded; source-inspired cap, pending review of this adapted rule. Equivalent duplicate notation for one root does not count as a third root. For negative c or zero, the correct corresponding sine branches replace the anchor's positive first/second-quadrant restriction. No angle-unit follow-through from radian work applied as degrees. No double award for an alternative derivation: one maximum per criterion.

Answer-only: a fully correct requested representation, or clearly labelled correct R and alpha at the requested precision, earns all3 marks for(a), with a-M1 implied by the coefficient-correct representation (proposed implied-method interpretation). Unlabelled ambiguous numbers request clarification. A naked pair of roots earns b-A1+b-A2 (2/4), not the unseen branch-search methods; thus a fully correct answer-only card earns5/7, not7/7. The work order therefore does **not** impose a universal working penalty or award unseen numerical method universally. Alternative complete coefficient or phase-shift reasoning receives the same 7-mark cap when it supplies equivalent evidence for every named criterion. A route bypassing the stated hence reduction does not automatically earn b-M1/b-M2; correct roots still earn the accuracy awards. Showing only one inverse-calculator root is at most b-M1 plus the one correct accuracy award.

## Sample response, feedback and assessment uncertainty

Use the normal exemplar. Full working with R=5,alpha53.13degrees,roots103.3,330.4 earns7/7: 'Both roots satisfy the original equation and interval.' A complete conversion but a single root103.3 with the correct reduced equation earns5/7 (a3,b-M1,b-A1): 'You found one valid angle. Search the other sine branch within the shifted interval.' Fully correct roots by a direct sinusoid method still earn4/4 for b if both method-equivalent decisions are visible. Correct conversion followed by $103.3^\circ$ and $383.6^\circ$, with both correct transformed angles shown but subtraction of the phase missed on the second one, earns a3 plus b-M1/b-M2 and the first correct original-root accuracy mark:6/7. The second submitted value also lies outside the original interval. A photo where103.3 could read108.3 remains pending clarification; do not invent a misconception.

Remaining decision: owner accepts the78-tuple pilot and the proposed implied-method/extra-root conventions; cross-vendor review checks those exact criteria and the three paper exemplars. No runtime marker or UI support is certified. See [exemplar](../exemplars/WB8227-trig-rform-equation.md).

## Shared boundaries and later checks

Use [recipe-contract.md](../recipe-contract.md), [subject-rules.md](../subject-rules.md), shared Bloom policy and the 7 November 2026 learner-text guideline snapshots under `workbench/playbook/guidelines/` with their recorded `provenance.json` hashes. This work order fixes the content decisions; it does not claim those draft metadata fields are accepted by the app. Retain source version, branch, part and criterion identities in the eventual frozen instance. Retain original attempts and historical classifications.

Practice permits another admitted instance without passing first. Before submission offer only an answer-free strategy or a separately identified different-instance example; neither exposes the current canonical solution. After submission show earned credit, the first evidenced issue, repair steps and the full authored solution. A correct solution receives no invented repair. In Workbench Test provide no hints/examples/tutor for an unsubmitted question; preserve question-by-question post-submission review and existing nonfinal two-minute review/early-advance/expiry behavior. Later same-recipe questions after feedback are after-feedback observations, not wholly unaided evidence. No mastery or memory-box change is inferred by this resource.

An unreadable, ambiguous or incomplete submission requests clarification with marking pending; it is not automatically wrong. Number/format adapters may normalise an equivalent value, never change mathematics or invent missing method. No app-owned learner attempt or progress belongs in the content package. Textbook originals and their diagrams remain internal (`learner_display: false`); the paper exemplar questions below are newly authored. NSSCAS/Cambridge originals may be quoted with attribution under Vitalis's instruction, but publication and assignment remain unauthorised.

Future E–F checks: independently enumerate the finite admitted mathematical identities; compare question, solution, marking and assets to the same values; check all named examples and rejected boundaries. Use a separately implemented substitution/inverse oracle, not the answer constructor. Replay seeds 0,1,42,2**63-1 once an implementation exists; use at least64 draws or exhaust the smaller finite branch. Check correct, partial, wrong, alternative and ambiguous submissions, branch-specific same-type labels, no-repeat/exhaustion, decoded Markdown/LaTeX and actual app rendering/reveal timing. Runtime generation, marking and app-render checks are **not run** in stage D. Offline mathematical-syntax and static paper-diagram checks are reported separately. Source/author calculations do not establish independent acceptance.
