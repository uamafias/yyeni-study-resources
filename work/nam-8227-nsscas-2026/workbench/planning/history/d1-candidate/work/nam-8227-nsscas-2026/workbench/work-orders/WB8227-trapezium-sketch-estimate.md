# Work order: WB8227-trapezium-sketch-estimate

NSSCAS Mathematics 8227; NIED December 2020 syllabus, Grade 12. Owner Vitalis; PLANNER Codex; 23 November 2026. **Proposed v0.1.1, stage-D1 repair. Claude short check, then Vitalis approval pending.** Accepted C selection `8227:FAMILY:trapezium-chain`; narrowed selection `8227:D:SEL:trapezium-sketch-estimate:logarithmic-hence-chain`; branch `logarithmic-hence-chain`. Paper design only, no runtime authoring.

## Purpose, connected assessment and reusable boundary

Keep the observed chain: (a) prescribed trapezium estimate, (b) factor/log-law **hence** reuse, (c) log sketch, (d) bias from that own sketch. Do not split it automatically into four recipes or count a numerical estimate as coverage of sketch/bias. New purpose-built 8227 design extends existing Workbench records/provider conventions; no Flashcard Studio content conversion.

| Part | Direct demands (prefix `8227:2020:`) | Primary objective | Prerequisites (not direct coverage) | Marks / response |
|---|---|---|---|---|
| `a` | `M2:T5:O03:D01`, `M2:T5:O03:D02` | `M2:T5:O03` | NSSCO arithmetic/coordinates |3; numeric with method|
| `b` | `M2:T2:O01:D02`, `M2:T5:O03:D02` | `M2:T2:O01` | `M2:T2:O01:D01` logarithm/index meaning; cue/F.T. from(a) |2; numeric with hence working|
| `c` | `M2:T2:O02:D02`, `M2:T5:O04:D01` | `M2:T5:O04` | `M2:T2:O02:D01` definitions/inverse concept |3; sketch|
| `d` | `M2:T5:O04:D02` | `M2:T5:O04` | Own sketch and estimate via cue edges, not new prerequisite coverage |2; explanation|

The O03:D02 link in(b) is the accepted source’s estimate/rescaling facet, **not a second application of the trapezium rule**. It does not double count direct coverage or marks. Primary objectives agree with `visual-design.json` and the final register. No change of base, formal substitution, exact integration requirement, mixed-curvature or general refinement theorem. Concave-up/overestimate, oscillation and table-only contexts remain later scope.

## Native evidence, qualifiers and calibration

- Syllabus `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`: PDF16/printed13 trapezium/sketch bias; PDF14/printed11 logs/graphs; PDF18/printed15 default3sf. Grade `E:14` PDF23/printed20, `C:15` PDF22/printed19 and `A:10` PDF20/printed17 calibrate simple estimate/sketch bias to a combined problem. MF9 supports notation/formula use, not new assessed scope.
- NSSCAS 2023 P2 Q6(a,b) PDF/printed10, (c,d) PDF/printed11, source `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 2 8227-2 - First Proof 13.03.2023.pdf`, SHA256 `6e6fa13da22e198cdd0686db38550144705e67b05078d2ca0b9cc8d27026fd5e`. The examiner report corroborates the Q6 content; the holdings’ wider final-equivalence caveat remains.
- Award/report2023 `Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf`, PDF337/printed335 Q6, rows `8227:EXAM:2023:P2:Q6:AWARD:01–11`: positive width, correct weighting, factorised form alone, B1FT scaling, non-hence SC1, shape/asymptote/intercept, own-graph bias and dependent geometric reason. Report warns about premature rounding, squaring the estimate, graph-domain/asymptote errors and monotonicity used as an insufficient reason.
- **D1 additional official read:** 2025 P2 Q4, `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2025/8227-2.pdf`, PDF/printed4; examiner report2025 `Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf`, PDF358/printed356 Q4(b), row `8227:EXAM:2025:P2:Q4:AWARD:05`: B1 **F.T. From Their graph**, with “The actual trapeziums must be drawn on the curve.” This is evidence for own-sketch F.T., not a same-type label for this log branch.
- Internal textbooks: all five `trapezium-graph-bias-chain` members read, YM C12 Example21 PDF549, TryNow21Q1 PDF550, Example24/TryNow24 PDF555, Revision12Q5 PDF556. Book hashes, exact subparts and accepted assessed/component union discovery IDs in `planning/visual-source-reads.json/.md`. Other union hits are unadjudicated leads. Textbook originals remain internal. Native pages, not precision/distinction/rejection templates or extracted notes, inform design.

Part-scoped same-type references to2023 Q6(a–d) retain exact source fields/pages in `visual-design.json`. Added precision/asymptote/geometric-reason instructions are disclosed mild scaffolds; they do not add a new task or import references from another branch.

## Finite domain, originals and discriminating errors

$h\in\{1,2,3\}$, $L\in\{4,8\}$, $n\in\{2,4\}$, $k\in\{1,2,3\}$; $f(x)=\ln(x-h)$, interval $[h+1,h+1+L]$, width $\Delta=L/n$. Exclude official original $(h,L,n,k)=(2,8,4,3)$ from fresh variants:36raw → **35 admitted presentations**. All logs have argument at least1 during quadrature; the sketch separately includes $h<x<h+1$ where $y<0$. Exclude zero/unequal width, log poles/undefined ordinates, inconsistent assets and replacements with different curvature; $h=0$ is outside the chosen domain, not mathematically invalid.

Ask:

(a) Use $n$ equal trapeziums to estimate $I=\int_{h+1}^{h+1+L}\ln(x-h)\,dx$ to **3 significant figures**.
(b) **Hence**, showing the transformation, estimate $J=\int_{h+1}^{h+1+L}k\ln(x^2-2hx+h^2)\,dx$ to **3 significant figures**.
(c) Sketch $y=\ln(x-h)$, labelling axis intersections and any vertical asymptote.
(d) Use your sketch to state, with a reason about trapeziums and the curve, whether(a) is an over- or underestimate.

Recognition of the square in(b) is not supplied: $x^2-2hx+h^2=(x-h)^2$ and $x-h>0$. The correct hence scale is $2k$, not squaring $T$ or multiplying by $k$ alone. The domain script checks that these named wrong computations never produce canonical $J$; it also checks negative width, omission of interior factor2 and double-counting the nonzero final endpoint. Premature rounding may leave the final result unchanged; it is not claimed diagnostically visible in every instance. Two-decimal ordinates change(a) only for$(L,n)=(4,4)$; retain that source-specific limitation rather than claim an exhaustive rounding-error detector.

## Semantic capacity, collisions and exposure

35 presentations correspond to **12** whole contexts keyed by `(L,n,k)`: horizontal translation alone repeats the(a)/(b) computation. Raw-to-whole-context collisions23. Per assessed part:

| Part | Semantic key | Distinct contexts | Distinct canonical conclusion/value classes |
|---|---|---:|---:|
| `a` | `('trapezium-quadrature',L,n)` |4|4 numerical estimates|
| `b` | `('trapezium-hence',L,n,k)` |12|12 scaled canonical estimates|
| `c` | `('log-sketch',h)` |3|3 labelled sketches|
| `d` | `('own-log-chord-context',h,L,n)` |12|1 canonical bias outcome: underestimate|

The(d) key includes the credited own-graph/chord data, not just the word “underestimate”. This is contextual variation, not a new reasoning type or Analyse demand. The four counts4/12/3/1 from D0 remain visible as computation/value/sketch/outcome classes; they are not35 independent repetitions. The strict “none of this task’s assessed part keys has been exposed” packing has maximum **3** before any examples, bounded by(c); a three-task witness is saved in the domain audit. A viewed example can reduce it. Repeating any part is allowed for practice **only labelled after-feedback/not wholly fresh**; it cannot be presented as a wholly fresh test. App owns per-part exposure/reservation/retry, including examples and cross-branch shared work. Exhaustion must not silently repeat, relabel a translation as new mathematics or change curvature/domain. Numerical bounds are a planner-chosen subset of the observed/source workload, not official grade cutoffs.

## Assets and must-read givens (R3-07)

(a,b) are text: must read log base$e$, bounds, shift, interval count, expanded quadratic, factor$k$ and hence/precision instruction. (c) has blank axes only before submission; no supplied answer graph. `response_format`: a/b numeric, c sketch, d explanation. Solution asset fixed: one increasing log branch; variable$h$, window/labels, nodes/chords from(a). Relations: domain$x>h$, asymptote$x=h$, intercept$(h+1,0)$, below-axis branch for$h<x<h+1$, no$y$-intercept; positive decreasing gradient while$y$continues growing without a finite horizontal asymptote. Shading, if used, is exactly between curve and$x$-axis for$h+1\le x\le h+1+L$.

Must-read/check: both axes, asymptote/intercept labels, domain side, integration limits, strip count and curve/chord relation. Derive every question/solution/marker image from one tuple. Dashed asymptotes are conventional and must visibly render dashed in the static illustrations; runtime/app dashes remain an E/F check. Tick/coordinate labels must not intersect the curve. Credits are geometric features, not pixel identity. No measurement calibration is needed. Owner decision6 includes sketch/diagram demands; uploaded-image presence alone proves no reliable marking capability.

## Canonical mathematics and operational memo

$T=\frac\Delta2[y_0+2\sum_{j=1}^{n-1}y_j+y_n]$, $y_j=\ln(1+j\Delta)$; $J\approx2kT$. Preserve exact logs/guard digits. Independent author oracle uses direct trapezium-area sums and exact integral$(L+1)\ln(L+1)-L$, not a runtime answer function. Learners need not know that primitive.

**D1-MR01–09 in `subject-rules.md` bind every criterion.** Prefix `WB8227-trapezium-sketch-estimate:`:

| ID | Marks | Required evidence / qualifiers |
|---|---:|---|
| `a:B1` |B1| Positive width $L/n$, unsimplified or seen in the formula. |
| `a:M1` |M1| Correct trapezium weighting, or sum of actual trapezium areas, using positive width. |
| `a:A1` |A1| Correct3sf estimate with valid required method; premature-rounding errors lose this A only. |
| `b:B1` |B1| **Factorised form alone** $k\ln((x-h)^2)$ seen, or an equivalent correct visible square-rewrite. The log-law scale is not additionally required for this first mark. |
| `b:B2` |B1 F.T.| Correct $2k$ times their(a); correct hence/log-power scale visible in working. Formal F.T. edge `a→b`, not merely a cue. |
| `c:B1` |B1| Single log curve with **all shape features**: exists only$x>h$; approaches$x=h$ downwards without touching/crossing; rises through quadrants4and1 with decreasing gradient; continues upwards without a finite horizontal asymptote. **B0 if more than one function graph is presented**, excluding axes/auxiliary guides. |
| `c:B2` |B1| Correct asymptote$x=h$ identified on the sketch: a labelled vertical guide or a clearly labelled approached boundary is enough. A detached text value not tied to the graph is insufficient. Dashed rendering is conventional, not a separate hidden mark. |
| `c:B3` |B1| Correct labelled intercept$(h+1,0)$ on the sketch. |
| `d:B1` |B1 F.T.| The bias conclusion supported by **their own sketch** on(a)’s interval, even if that sketch’s shape is wrong. Correctly concave-up own sketch supports “over”; concave-down supports “under”. |
| `d:DB1` |DB1| Correct top-chord/trapezium position relative to that own curve; depends on `d:B1`. Correct mathematical concavity shorthand can establish the geometric reason if unambiguous from their sketch. “Increasing” alone cannot. |

Total **3+2+3+2=10**. Shape errors lose(c) credit only; do not repeat that penalty in(d). A clearly absent sketch gives **d0/2**, since the required own-graph evidence is absent. An unreadable/ambiguous upload is **pending clarification**, not a guessed wrong graph. For a clear sketch whose local geometry does not support a unique over/under conclusion, credit only what is actually established; no guessed F.T.

Answer-only by part: (a) bare$T$0/3 under OD-1; (b) bare$J$0/2, not even SC method credit; a visible correct non-hence method is capped **SC1/2**, maximum with the main path, never added. (c) the requested sketch is assessed work, not an unsupported bare numerical answer: its features can earn3/3 without prose. (d) a bias word supported by the submitted own sketch can earn d:B1 under the official own-graph statement award; no geometric reason means DB0. With no sketch, the word alone earns0. No universal full-credit/no-working policy is imported.

### Per-instance(b) accepted answers and rounding

The memo lists all three accepted numerical representations (duplicates coalesced):

1. `round3(2kT)` from guard-digit(a);
2. `2k × round3(T)` as the source-sanctioned F.T. product;
3. `round3(2k × round3(T))`.

Decimal half-up significant-figure rounding is used; do not round a binary-float approximation at a boundary. All35 per-instance sets are saved as `b_accepted_answer_strings` in `planning/d1/visual-domain-checks.json`; the companion exemplar lists its own set. The unrounded F.T. product is retained because the official B1FT award credits multiplying their reported(a), not a newly invented independent accuracy award. This is explicitly disclosed operational F.T. handling, not an assertion that extra digits are the canonical3sf result. Stage E fixtures include$(L,n,k)=(8,2,1),(8,2,2),(8,2,3)$ and the rounding-sensitive$(4,4,1)$ case. Wrong(a) can still earn the source B1FT if the correct scale is used; a wrong scale or squared$T$ does not.

### Qualifier/deviation ledger

2023 Q6 rows01–03 retain positive width, formula-or-otherwise and canonical accuracy. Row04 retains factorised form alone. Row05 retains F.T.; row06 retains exclusive SC1. Rows07–09 retain single-graph exclusion and feature awards; rows10–11 retain own-graph conclusion and dependent reason. No row is passed off as an unchanged official numeric memo for new values.

**Named deviation `D1-TRAP-FT-BRIDGE`, for Claude/Vitalis:** this Q6-style two-mark(d) keeps2023’s verbal/chord-reason alternatives and makes own-sketch F.T. explicit using2025 Q4(b). The2025 row additionally requires actual drawn trapeziums; this hybrid does **not** require a chord overlay when a clear own sketch and correct verbal geometric reason already establish the2023 DB1. The departure is stated rather than hiding that qualifier. If the owner rejects this hybrid, require the overlay in the stem/memo and recheck the exemplars; no owner approval is inferred now.

## Samples, Bloom and learner modes

For normal$(h,L,n,k)=(1,4,2,2)$, canonical$T=3.81$, $J=15.2$:

| Submission/evidence | Credit with other parts complete | Feedback |
|---|---:|---|
| Correct quadrature, factorisation/hence product, sketch and chord reason |10/10| All evidence present; no invented repair. |
| Shows$2\ln((x-1)^2)$, then wrongly uses$J=T^2$ |9/10| b:B1 remains; b:B2 lost. “You recognised the square; now apply the log power rule instead of squaring the estimate.” |
| Squares$T$ with no correct factorisation or hence scale |8/10| b0/2. Give factorise→log-law→scale repair. |
| Wrong concave-up(c), correct remaining labels; says “over, my trapezium tops lie above my curve” coherently |9/10 if c:B2/B3 earned| Lose c:B1 only; d2/2 F.T. Correct the log shape in(c), do not penalise its implication twice. |
| No sketch; correct(a,b); bias sentence alone |5/10| c0,d0; ask for the required sketch. |
| Correct sketch; only “underestimate” |9/10| d1/2, missing geometric reason. |
| Unreadable sketch |pending for affected awards| Clarify; preserve original evidence. |

Classification `8227-pilot-design-0.1.1`: all parts **Apply3**. a criteria execute quadrature; b criteria execute square/log/hence transformation; c criteria apply familiar log transformation; d’s own B1/DB1 apply a fixed chord rule. Whole branch3. The canonical bias outcome never varies, so **no Analyse4 claim** remains. Criteria cited in each rationale belong only to that part.

Practice support before submission is answer-free and uses a different bound instance; no current ordinates/graph/bias are leaked. Reveal frozen current solution/feedback only after submission. After any repeated part/example, label after-feedback exposure honestly. Test has no pre-submit help and retains existing post-question review/timing/progress. App owns all state; no generator/app operation is run here.

## Checks and stop

Run `planning/d1/visual-domain-checks.py` (35presentations/12contexts, 4/12/3/12 part keys and one bias outcome) and the independently written exemplar oracle. Normal/changed/boundary solutions and static SVG/PNG inspection evidence are recorded. Stage E/F must enumerate all admitted tuples, replay seeds0/1/42/$2^{63}-1$, test the four rounding contexts and all own-sketch F.T./blank/unreadable/wrong-log-law/SC cases, asset-label/dash fidelity and per-part reservation/exhaustion. These are design check scripts, not runtime generators.

No textbook original becomes learner-facing; valid exam originals need attribution and are outside fresh pools. No app runtime, import, assignment or production acceptance is claimed. OD-3 stop: Claude short check, then Vitalis approves this exact repaired design. No commit or push.
