# Work order: WB8227-trapezium-sketch-estimate

NSSCAS Mathematics 8227; NIED December 2020 syllabus, Grade 12. Owner Vitalis; PLANNER Codex; 24 November 2026. **Proposed v0.1.4, stage-D4 repair. Claude D4 changed-scope confirmation, then Vitalis approval pending.** Accepted C selection `8227:FAMILY:trapezium-chain`; narrowed selection `8227:D:SEL:trapezium-sketch-estimate:logarithmic-hence-chain`; branch `logarithmic-hence-chain`. Paper design only, no runtime authoring.

## Purpose, connected assessment and reusable boundary

Keep the observed chain: (a) prescribed trapezium estimate, (b) factor/log-law **hence** reuse, (c) log sketch, (d) bias from that own sketch. Do not split it automatically into four recipes or count a numerical estimate as coverage of sketch/bias. New purpose-built 8227 design extends existing Workbench records/provider conventions; no Flashcard Studio content conversion.

| Part | Direct demands (prefix `8227:2020:`) | Primary objective | Prerequisites (not direct coverage) | Marks / response |
|---|---|---|---|---|
| `a` | `M2:T5:O03:D01`, `M2:T5:O03:D02` | `M2:T5:O03` | NSSCO arithmetic/coordinates |3; numeric with method|
| `b` | `M2:T2:O01:D02`, `M2:T5:O03:D02` | `M2:T2:O01` | `M2:T2:O01:D01` logarithm/index meaning; cue/F.T. from(a) |2; numeric with hence working|
| `c` | `M2:T2:O02:D02`, `M2:T5:O04:D01` | `M2:T5:O04` | `M2:T2:O02:D01` definitions/inverse concept |3; sketch|
| `d` | `M2:T5:O04:D02` | `M2:T5:O04` | Own sketch and estimate via cue edges, not new prerequisite coverage |2; explanation|

The O03:D02 link in(b) is the accepted source’s estimate/rescaling facet, **not a second application of the trapezium rule**. It does not double count direct coverage or marks. Primary objectives agree with `visual-design.json` and the final register. Design(b) prioritises its assessed square/log-law transformation (M2:T2:O01), retaining estimate-rescaling as other direct; design(c) prioritises its numerical-method sketch/bias role (M2:T5:O04), retaining logarithm-graph interpretation as other direct. The accepted 2023 analysis uses estimate O03 and log-graph O02 as primaries respectively; this explicit design-role choice does not retag the source analysis. No change of base, formal substitution, exact integration requirement, mixed-curvature or general refinement theorem. Concave-up/overestimate, oscillation and table-only contexts remain later scope.

## Native evidence, qualifiers and calibration

- Syllabus `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`: PDF16/printed13 trapezium/sketch bias; PDF14/printed11 logs/graphs; PDF18/printed15 default3sf. Grade `E:14` PDF23/printed20, `C:15` PDF22/printed19 and `A:10` PDF20/printed17 calibrate simple estimate/sketch bias to a combined problem. MF9 supports notation/formula use, not new assessed scope.
- NSSCAS 2023 P2 Q6(a,b) PDF/printed10, (c,d) PDF/printed11, source `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 2 8227-2 - First Proof 13.03.2023.pdf`, SHA256 `6e6fa13da22e198cdd0686db38550144705e67b05078d2ca0b9cc8d27026fd5e`. The examiner report corroborates the Q6 content; the holdings’ wider final-equivalence caveat remains.
- Award/report2023 `Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf`, PDF337/printed335 Q6, rows `8227:EXAM:2023:P2:Q6:AWARD:01–11`: positive width, correct weighting, factorised form alone, B1FT scaling, non-hence SC1, shape/asymptote/intercept, own-graph bias and dependent geometric reason. Report warns about premature rounding, squaring the estimate, graph-domain/asymptote errors and monotonicity used as an insufficient reason.
- **D1 additional official read:** 2025 P2 Q4, `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2025/8227-2.pdf`, PDF/printed4; examiner report2025 `Question Banks/Namibian Examiner Reports/NSSCAS/2025/NSSCASExaminersReport2025.pdf`, PDF358/printed356 Q4(b), row `8227:EXAM:2025:P2:Q4:AWARD:05`: B1 **F.T. From Their graph**, with “The actual trapeziums must be drawn on the curve.” This is evidence for own-sketch F.T., not a same-type label for this log branch.
- Internal textbooks: all five `trapezium-graph-bias-chain` members read, YM C12 Example21 PDF549, TryNow21Q1 PDF550, Example24/TryNow24 PDF555, Revision12Q5 PDF556. Book hashes, exact subparts and accepted assessed/component union discovery IDs in `planning/visual-source-reads.json/.md`. Other union hits are unadjudicated leads. Textbook originals remain internal. Native pages, not precision/distinction/rejection templates or extracted notes, inform design.

Part-scoped same-type references to2023 Q6(a–d) retain exact source fields/pages in `visual-design.json`. Added precision/asymptote/geometric-reason instructions are disclosed mild scaffolds; they do not add a new task or import references from another branch.

## Finite domain, originals and discriminating errors

$h\in\{1,2,3\}$, $L\in\{4,8\}$, $n\in\{2,4\}$, $k\in\{1,2,3\}$; $f(x)=\ln(x-h)$, interval $[h+1,h+1+L]$, width $\Delta=L/n$. Exclude $(h,L,n)=(2,8,4)$ for **every** $k$, because(a),(c),(d) would reproduce the original parts even when(b) changes. Also exclude $(L,n,k)=(4,4,2)$ for every $h$: the wrong $T^2$ and canonical $2kT$ coincide when rounded to marked 3 s.f. The six exclusions are disjoint:36 raw → **30 admitted presentations**. All logs have argument at least1 during quadrature; the sketch separately includes $h<x<h+1$ where $y<0$. Exclude zero/unequal width, log poles/undefined ordinates, inconsistent assets and replacements with different curvature; $h=0$ is outside the chosen domain, not mathematically invalid.

Ask:

(a) Use $n$ equal trapeziums to estimate $I=\int_{h+1}^{h+1+L}\ln(x-h)\,dx$ to **3 significant figures**.
(b) **Hence**, showing the transformation, estimate $J=\int_{h+1}^{h+1+L}k\ln(x^2-2hx+h^2)\,dx$ to **3 significant figures**.
(c) Sketch $y=\ln(x-h)$, labelling axis intersections and any vertical asymptote.
(d) Use your sketch to state, with a reason about trapeziums and the curve, whether(a) is an over- or underestimate.

Recognition of the square in(b) is not supplied: $x^2-2hx+h^2=(x-h)^2$ and $x-h>0$. The correct hence scale is $2k$, not squaring $T$ or multiplying by $k$ alone. The D2 domain script compares these named wrong computations at the **marked 3 s.f. precision**, and checks that no admitted tuple produces the canonical rounded $J$; it also checks negative width, omission of interior factor2 and double-counting the nonzero final endpoint. Premature rounding may leave the final result unchanged; it is not claimed diagnostically visible in every instance. Two-decimal ordinates change(a) only for$(L,n)=(4,4)$; retain that source-specific limitation rather than claim an exhaustive rounding-error detector.

## Semantic capacity, collisions and exposure

30 presentations correspond to **11** whole contexts keyed by `(L,n,k)`: horizontal translation alone repeats the(a)/(b) computation. Raw-to-whole-context collisions19. Per assessed part:

| Part | Semantic key | Distinct contexts | Distinct canonical conclusion/value classes |
|---|---|---:|---:|
| `a` | `('trapezium-quadrature',L,n)` |4|4 numerical estimates|
| `b` | `('trapezium-hence',L,n,k)` |11|11 scaled canonical estimates|
| `c` | `('log-sketch',h)` |3|3 labelled sketches|
| `d` | `('own-log-chord-context',h,L,n)` |11|1 canonical bias outcome: underestimate|

The(d) key includes the credited own-graph/chord data, not just the word “underestimate”. This is contextual variation, not a new reasoning type or Analyse demand. The four counts4/12/3/1 from D0 remain visible as computation/value/sketch/outcome classes; they are not30 independent repetitions. The mathematical all-part-key packing is **3**, including an attributed h=2 original sketch; its separate three-task mathematical witness is saved. The strict generated-fresh packing is **2** before examples, because h=2 is blocked. After one generated worked example using h=1 or h=3, at most **1** wholly fresh complete task remains; other used part keys may exhaust it sooner. Never call the mathematical witness generated-fresh. Repeating any part is allowed for practice **only labelled after-feedback/not wholly fresh**; it cannot be presented as a wholly fresh test. App owns per-part exposure/reservation/retry, including examples and cross-branch shared work. Exhaustion must not silently repeat, relabel a translation as new mathematics or change curvature/domain. Numerical bounds are a planner-chosen subset of the observed/source workload, not official grade cutoffs.

## Assets and must-read givens (R3-07)

(a,b) are text: must read log base$e$, bounds, shift, interval count, expanded quadratic, factor$k$ and hence/precision instruction. (c) has blank axes only before submission; no supplied answer graph. `response_format`: a/b numeric, c sketch, d explanation. Solution asset fixed: one increasing log branch; variable$h$, window/labels, nodes/chords from(a). Relations: domain$x>h$, asymptote$x=h$, intercept$(h+1,0)$, below-axis branch for$h<x<h+1$, no$y$-intercept; positive decreasing gradient while$y$continues growing without a finite horizontal asymptote. Shading, if used, is exactly between curve and$x$-axis for$h+1\le x\le h+1+L$.

Must-read/check: both axes, asymptote/intercept labels, domain side, integration limits, strip count and curve/chord relation. Derive every question/solution/marker image from one tuple. Dashed asymptotes are conventional and must visibly render dashed in the static illustrations; runtime/app dashes remain an E/F check. Tick/coordinate labels must not intersect the curve. Credits are geometric features, not pixel identity. No measurement calibration is needed. The 16 November owner decision 6 (visual demands) includes sketch/diagram demands; uploaded-image presence alone proves no reliable marking capability.

## Canonical mathematics and operational memo

$T=\frac\Delta2[y_0+2\sum_{j=1}^{n-1}y_j+y_n]$, $y_j=\ln(1+j\Delta)$; $J\approx2kT$. Preserve exact logs/guard digits. Independent author oracle uses direct trapezium-area sums and exact integral$(L+1)\ln(L+1)-L$, not a runtime answer function. Learners need not know that primitive.

**Shared D1-MR01–09 in `subject-rules.md` apply; OD-1/OD-5/OD-6 govern their named rules, other design interpretations await plan approval.** Prefix `WB8227-trapezium-sketch-estimate:`:

| ID | Marks | Required evidence / qualifiers |
|---|---:|---|
| `a:B1` |B1| Positive width $L/n$, unsimplified or seen in the formula. |
| `a:M1` |M1| Correct trapezium weighting, or sum of actual trapezium areas, using positive width. |
| `a:A1` |A1| Correct3sf estimate with valid required method; premature-rounding errors lose this A only. |
| `b:B1` |B1| **Factorised form alone** $k\ln((x-h)^2)$ seen, or correct $2k\ln(x-h)$ (or the $2k$ scale visibly derived from the log law $\ln((x-h)^2)=2\ln(x-h)$), which implies the square. Writing the intermediate square is not compulsory. |
| `b:B2` |B1 F.T.| Correct visible $2k$ times their own(a) value, as present in the coherent final answer or working, with no visibly wrong log-law reasoning (www). Missing factorisation/log-law derivation alone does not prevent B2 when the correct visible product is shown; B1 assesses the form/derivation separately. Judge that product and its 3 s.f.-correct representations, **not a closed canonical list**. Formal F.T. edge `a→b`, not merely a cue. |
| `c:B1` |B1| Single log curve with **shape judged relative to the boundary the curve approaches, drawn or implied**: lies only to its right, approaches it downwards without touching/crossing, rises through quadrants4and1 with decreasing gradient, and has no finite horizontal asymptote. Correct location $x=h$ is awarded only by c:B2. **B0 if more than one function graph is presented**, excluding axes/asymptote/chord guides. |
| `c:B2` |B1| Correct asymptote$x=h$ identified on the sketch: a labelled vertical guide or a clearly labelled approached boundary is enough. A detached text value not tied to the graph is insufficient. Dashed rendering is conventional, not a separate hidden mark. |
| `c:B3` |B1| Correct labelled intercept$(h+1,0)$ on the sketch. |
| `d:B1` |B1 F.T.| The bias conclusion supported by **their own sketch** on(a)’s interval, even if that sketch’s shape is wrong. Correctly concave-up own sketch supports “over”; concave-down supports “under”. |
| `d:DB1` |DB1| Correct top-chord/trapezium position relative to the **same own curve**; depends on `d:B1`. A clear verbal geometric reason, or a correctly drawn chord/trapezium overlay plus a brief statement referring to it, earns this mark. Unambiguous concavity shorthand can establish the geometry; “increasing” alone cannot. Own-curve F.T. for this dependent reason is the sole OD-5 extension. |

Total **3+2+3+2=10**. Shape errors lose(c) credit only; do not repeat that penalty in(d). A clearly absent sketch gives **d0/2**, since the required own-graph evidence is absent. An unreadable/ambiguous upload is **pending clarification**, not a guessed wrong graph. For a clear sketch whose local geometry does not support a unique over/under conclusion, credit only what is actually established; no guessed F.T.

Answer-only by part: (a) bare$T$0/3 under OD-1; (b) bare$J$0/2, not even SC method credit; a visible correct non-hence method is capped **SC1/2**, maximum with the main path, never added. (c) the requested sketch is assessed work, not an unsupported bare numerical answer: its features can earn3/3 without prose. (d) a bias word supported by the submitted own sketch can earn d:B1 under the official own-graph statement award; no geometric reason means DB0. With no sketch, the word alone earns0. No universal full-credit/no-working policy is imported.

### Per-instance(b) accepted answers and rounding

b:B2 is a **follow-through rule**, not a whitelist: take $2k$ times the learner's own(a) value visible in their final answer or coherent working. The eligible answer is that exact product or any representation correct to at least the requested 3 s.f.; higher precision is accepted when it agrees at 3 s.f. If they retain guard digits in working and report3sf separately, either coherently used value is eligible. A wrong scale, or a scale reached by visibly wrong log-law working (www), does not earn b:B2; a numerical coincidence alone does not establish the hence method. A correctly seen factorised square still earns b:B1.

The audit's `b_canonical_path_fixture_strings` are **non-exhaustive examples**: canonical guard-digit result, $2k$ times reported canonical3sf(a), and that product rounded3sf. They are not an `accepted_answer_strings` contract. For the normal,15.23 is a valid more-precise canonical-path value, as are15.2 and the F.T.15.24. The clear line $J=4T$ followed by the appropriate product earns b:B2; no extra accuracy mark is invented.

D2 F.T. fixtures include own(a) working values10.84,11.52,11.52 with $2k=4,4,6$: products43.36/43.4,46.08/46.1,69.12/69.1 remain eligible, even where canonical-path fixtures differ. Premature rounding loses a:A1 only if it changes(a)'s required final value; it does not revoke a legitimate later source-sanctioned F.T. mark. Decimal half-up significant-figure rounding is used, not binary rounding at a boundary.

**MR03 misread — authority and proposed mechanics.** Binding OD-6 principle: a genuine misread of question data with unchanged object and difficulty costs one mark from A/B; all A/B follow through on the misread value and M/DM are judged as usual. Own-figure errors and misreads changing object/difficulty receive ordinary canonical marking. Practice feedback names the misread. Proposed MR03 operational rules, pending Vitalis approval of the exact manifest: decide and record eligibility once at first use; ineligible data remain canonical in every later part. For each eligible misread datum, first mark all gross evidence and dependencies, then deduct one mark from the first earned A/B on that datum in question/criterion order, moving to later-use parts if necessary. Deduct nothing only if no A/B is earned on the datum anywhere. Never deduct from M/DM or make the score negative. The selected criterion remains earned for every DM, dependency and www check; one datum costs at most one net mark. Eligible OD-6 follow-through overrides not-F.T. and c.a.o. restrictions, while correct working, named method exclusions and OD-1 still apply. No-solution exclusion means a misread removes a solution the canonical question has; a designed no-real-solution outcome remains eligible when its demand and difficulty are preserved. Sources: NSSCAS 2025 report PDF345 item4 (CONVENTION108) and comparable Cambridge 9709_m16_ms_12.pdf PDF3 Penalties; the comparable allocation is not a published Namibian rule.

### Qualifier/deviation ledger

2023 Q6 rows01–03 retain positive width, formula-or-otherwise and canonical accuracy. Row04 retains factorised form alone. Row05 retains F.T.; row06 retains exclusive SC1. Rows07–09 retain single-graph exclusion and feature awards; rows10–11 retain own-graph conclusion and dependent reason. No row is passed off as an unchanged official numeric memo for new values.

**`D1-TRAP-FT-BRIDGE`, accepted in OD-5, reworded:** the 2023 same-type Q6(d) row is retained in full. “Must be correct from their graph” is own-graph F.T. for d:B1. The same-type 2023 task needs **no drawn trapeziums**; a clear verbal chord/curve reason is enough. The **only extension** is d:DB1 judged relative to that same own curve, supported by the combined conclusion/reason F.T. mark in 2025 Q4(b). The 2025 drawn-trapezium condition belongs to its differently worded task and is not imported. OD-5 accepts this marking extension; final plan approval remains pending.

A drawn chord or trapezium overlay with a brief statement such as “under: these edges are below my curve” also earns DB1 when it establishes the geometry. If multiple unlabelled function graphs are supplied, even if one looks like the expected curve, **c0/3 and d0/2** (the 2023 prose's ambiguous multiple-graph case). If a unique curve is explicitly labelled $y=\ln(x-h)$, c:B1 still loses its single-function condition when another function graph is present; c:B2/B3 can assess the identifiable requested curve, and(d) uses only that curve. Axes, vertical-asymptote guides and chord overlays are not additional function graphs. An actually unreadable upload remains pending clarification, distinct from legible multiple unlabelled answers.

The formal `c→d` follow-through edge names d:B1 and records DB1's same-own-curve extension; cue and F.T. remain distinct.

## Samples, Bloom and learner modes

For normal$(h,L,n,k)=(1,4,2,2)$, canonical$T=3.81$, $J=15.2$:

| Submission/evidence | Credit with other parts complete | Feedback |
|---|---:|---|
| Correct quadrature, factorisation/hence product, sketch and chord reason |10/10| All evidence present; no invented repair. |
| Shows$2\ln((x-1)^2)$, then wrongly uses$J=T^2$ |9/10| b:B1 remains; b:B2 lost. “You recognised the square; now apply the log power rule instead of squaring the estimate.” |
| Squares$T$ with no correct factorisation or hence scale |8/10| b0/2. Give factorise→log-law→scale repair. |
| Writes the correct $4\ln(x-1)$ directly, then uses $J=4T$ correctly |10/10| The direct log-law expression implies the square: b:B1 and b:B2 both earned. |
| Draws $y=\ln x$ instead, with asymptote0 and intercept1, but correct log shape |8/10 if other parts complete coherently| c1/3 for shape only; the wrong shift loses c:B2/B3, not c:B1. |
| Correct own sketch and a drawn top chord plus “under: the edge is below my curve” |10/10| The overlay and brief referring statement establish DB1. |
| Two unlabelled function graphs, even if one looks like the expected curve |5/10 with correct(a,b)| c0,d0; no arbitrary graph selection. |
| Wrong concave-up(c), correct remaining labels; says “over, my trapezium tops lie above my curve” coherently |9/10 if c:B2/B3 earned| Lose c:B1 only; d2/2 F.T. Correct the log shape in(c), do not penalise its implication twice. |
| No sketch; correct(a,b); bias sentence alone |5/10| c0,d0; ask for the required sketch. |
| Correct sketch; only “underestimate” |9/10| d1/2, missing geometric reason. |
| Unreadable sketch |pending for affected awards| Clarify; preserve original evidence. |

Classification `8227-pilot-design-0.1.1`: all parts **Apply3**. a criteria execute quadrature; b criteria execute square/log/hence transformation; c criteria apply familiar log transformation; d’s own B1/DB1 apply a fixed chord rule. Whole branch3. The canonical bias outcome never varies, so **no Analyse4 claim** remains. Criteria cited in each rationale belong only to that part.

Practice support before submission is answer-free and uses a different bound instance; no current ordinates/graph/bias are leaked. Reveal frozen current solution/feedback only after submission. After any repeated part/example, label after-feedback exposure honestly. Test has no pre-submit help and retains existing post-question review/timing/progress. App owns all state; no generator/app operation is run here.

## Checks and stop

Run `planning/d4/visual-domain-checks.py` (30 presentations/11 contexts, 4/11/3/11 part keys and one bias outcome) and the independently written exemplar oracle. Normal/changed/boundary solutions and static SVG/PNG inspection evidence are recorded. Stage E/F must enumerate all admitted tuples, replay seeds0/1/42/$2^{63}-1$, test marked-precision collisions and the own(a) F.T. fixtures and all own-sketch F.T./blank/unreadable/wrong-log-law/SC cases, asset-label/dash fidelity and per-part reservation/exhaustion. These are design check scripts, not runtime generators.

No textbook original becomes learner-facing; valid exam originals need attribution and are outside fresh pools. No app runtime, import, assignment or production acceptance is claimed. OD-3 stop: Claude D4 changed-scope confirmation, then Vitalis approves this exact repaired design. No commit or push.

### Original-subtask guard for remaining $h=2$ contexts

The admitted mathematical domain still contains **30 presentations / 11 contexts**, with a combinatorial all-part-key packing of **3**. However, its $h=2$ sketch subtask shares 2023 Q6(c) exactly in assessed content. It is **not a fresh generated variant**. A future explicitly selected original/mixed-practice route may show that part only with the original wording and attribution “NSSCAS Mathematics 8227, 2023 Paper 2, Question 6(c), page 11”; the whole question must not be labelled original. The canonical record carries the exact source wording and locator.

A generated-fresh request blocks the part key `('log-sketch',2)`, leaving **22 fully generated presentations**, 11 contexts, part-key counts **4/11/2/8**, and a conservative generated-fresh packing of **2**. All three paper examples here use $h=1$ or $3$ and contain no unlabelled $h=2$ original subtask. Mathematical packing 3 and generated-fresh packing 2 are separate counts; no silent freshness claim is made.

D3 log-law probe: on the changed case, writing only $J=6T=6(11.5)=69.0$ with no factorisation or visible logarithm-law derivation earns **b1/2** (B2 only), not B1. Writing $3\ln((x-3)^2)=6\ln(x-3)$ first earns B1 as well. A genuine reading of $k=2$ as $k=3$ in the normal, followed by correct $3\ln((x-1)^2)=6\ln(x-1)$ and $6T=22.8$ (or $22.86$ from reported $T$), earns b1/2 after one MR−1 at b:B1, total9/10; it first uses that datum in b.

Near-copy disclosure: the admitted $(h,L,n)=(2,8,2)$ integrals differ from 2023 Q6 chiefly in strip count (and possibly k). They remain in the explicitly attributed original/mixed route because c is the original h=2 sketch; no domain change is made. For k=2, wrong scales $k^2$ and $k+2$ equal $2k=4$: do not infer a scale misconception from the number alone. Seeing the factorised square retains b:B1 (official row04). Visibly wrong log-law reasoning then loses b:B2 under its correct-working (www) requirement, even when k=2 makes the numerical scale coincide; the fixture earns b1/2, total9/10. This is a proposed D4 marking clarification, not an OD-1 penalty.

OD-6 sources: NSSCAS 2025 examiner report PDF345 item4 (`CONVENTION:108`) and Cambridge International 9709/12 March2016 mark scheme PDF3, Penalties. The Cambridge convention is comparable-board evidence adopted by Vitalis, not a Namibian published allocation. The per-datum unit, deduction order, eligibility ledger and gross-before-net dependency mechanics are proposed operational rules in MR03, pending approval of the exact manifest; they are not further owner decisions. Practice feedback names the misread.
