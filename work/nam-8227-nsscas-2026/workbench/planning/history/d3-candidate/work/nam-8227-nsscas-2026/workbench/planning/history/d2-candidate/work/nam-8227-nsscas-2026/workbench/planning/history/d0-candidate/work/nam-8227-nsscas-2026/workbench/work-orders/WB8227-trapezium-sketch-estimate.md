# Work order: WB8227-trapezium-sketch-estimate

NSSCAS Mathematics 8227, December 2020 syllabus, Grade 12. PLANNER Codex; owner Vitalis; 23 November 2026. Proposed version **0.1.0**; stage D paper design; approval pending. Design selection `8227:SELECT:D:trapezium-sketch-estimate` narrows accepted C selection `8227:FAMILY:trapezium-chain`; branch `logarithmic-hence-chain`. No runtime item/generator or assignment is created.

Partwise primary/other direct objective roles and criterion-linked Bloom rationales are explicitly recorded in [the pilot part evidence register](../planning/part-evidence-register.md) and its JSON. This supplements the specific criteria below; source-item links remain unchanged.

## Purpose, reuse and assessed structure

Keep an authentic connected task: (a) estimate a logarithmic integral by prescribed trapeziums; (b) use a factorisation/log law and **hence** reuse that estimate; (c) sketch the same function; (d) use that sketch to justify the bias of(a). A correct numerical trapezium total alone does not cover sketching or the chord/curve explanation. New 8227 recipe reuses the accepted source IDs and Workbench learning/marking conventions; it is not a Flashcard Studio conversion. One recipe serves the chain; do not turn four dependent parts into four unconditionally assigned drills.

| Stable part | Directly assessed demand IDs (prefix `8227:2020:`) | Primary objective | Marks | Response |
|---|---|---|---:|---|
| `a` | `M2:T5:O03:D01`, `M2:T5:O03:D02` | `M2:T5:O03` |3| numeric with method |
| `b` | `M2:T2:O01:D02`, `M2:T5:O03:D02` | `M2:T2:O01` |2| numeric with hence transformation |
| `c` | `M2:T2:O02:D02`, `M2:T5:O04:D01` | `M2:T5:O04` |3| sketch |
| `d` | `M2:T5:O04:D02` | `M2:T5:O04` |2| explanation |

Prerequisites: `M2:T2:O01:D01` logarithm/index meaning for(b), `M2:T2:O02:D01` exponential/log inverse concept for(c); NSSCO arithmetic and coordinate plotting. These support but do not earn direct coverage here. No change of base, general substitution integration, analytic exact integration requirement, convergence/refinement investigation, oscillation or mixed-concavity inference. Concave-up/overestimate examples remain visible later branches/recipes, not claimed covered by this logarithmic branch.

## Source evidence and bounds

- Syllabus `Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`, SHA256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`, PDF16/printed13 for trapezium/sketch bias; PDF14/printed11 for logs/graphs; PDF18/printed15 for default3 sf precision. Grade bounds: `8227:GRADE:E:14` PDF23/printed20 (simple trapezium estimate), `8227:GRADE:C:15` PDF22/printed19 (simple sketch-bias), `8227:GRADE:A:10` PDF20/printed17 (bias within more complex integration). These are calibration descriptors, not numerical grade thresholds. MF9 supports formula notation, not new scope.
- Question: `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 2 8227-2 - First Proof 13.03.2023.pdf`, SHA256 `6e6fa13da22e198cdd0686db38550144705e67b05078d2ca0b9cc8d27026fd5e`; Q6(a,b) PDF/printed10, (c,d) PDF/printed11. Source is an observed 10-mark connected chain, not merely a computation tagged “trapezium”.
- Official award/report: `Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf`, PDF337/printed335 Q6. Full source/file hash and native render identities: `planning/visual-source-reads.json`. Source awards3+2+3+2. Report warns about premature rounding, squaring the estimate instead of using log laws, missing asymptotes/negative log branch, and “increasing/decreasing” given as a bias reason without chord/curve comparison.
- Internal textbook breadth: all five members of `trapezium-graph-bias-chain` read: YM C12 Example21 PDF549/printed537, TryNow21Q1 PDF550/printed538, Example24 and TryNow24 PDF555/printed543, Revision12Q5 PDF556/printed544. Book source `Y=mc as textbook.pdf`, SHA256 `0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f`. The examples add trig, product/exponential and elementary curves plus over/under cases; none licenses copying a whole heterogeneous family’s precision or a misleading concave/convex vocabulary label. Example21’s solution response label(c) is a source typo for stem(b). Textbook originals stay internal, `learner_display:false`.
- Discovery: accepted assessed/component union links found29 estimate and18 bias records (overlapping, not summed); complete IDs and all-member reads are recorded. Other hits are unadjudicated leads, not rejections. Native pages were read; extracted notes and relation templates are not design evidence.

Per-branch references are the four exact Q6 part references in `planning/visual-design.json`, after demand/response/scaffolding checks. Each learner-visible label applies only to the corresponding part: e.g. “Same type as NSSCAS Mathematics 8227, 2023 Paper2, Question6(c), page11” (normal word spacing in generated display). No inherited family-wide label and no textbook attribution masquerading as an exam question.

## Finite domain and requested work

Parameters: horizontal shift $h\in\{1,2,3\}$, length $L\in\{4,8\}$, strips $n\in\{2,4\}$, factor $k\in\{1,2,3\}$. Define $f(x)=\ln(x-h)$, interval $[h+1,h+1+L]$, width $\Delta=L/n$ and transformed integrand $k\ln(x^2-2hx+h^2)$. Ask:

(a) Use $n$ equal trapeziums to estimate $I=\int_{h+1}^{h+1+L}\ln(x-h)\,dx$, to3 sf.
(b) Hence estimate $J=\int_{h+1}^{h+1+L} k\ln(x^2-2hx+h^2)\,dx$, showing the transformation.
(c) Sketch $y=\ln(x-h)$, labelling intercepts and any vertical asymptote.
(d) Use your sketch to state, with a reason about trapeziums and curve, whether(a) over- or underestimates the exact integral.

Keep the square visible as an expanded quadratic in(b): recognising $(x-h)^2$ is assessed, not supplied. On this interval $x-h\ge1$, so $\ln((x-h)^2)=2\ln(x-h)$ without an omitted absolute-value/domain error. Varying strip count and length changes the ordinate/evidence workload; $h$ changes the asymptote/intercept and expanded square; $k$ changes the hence scale. This does not claim new task types for every number tuple.

Capacity $3\times2\times2\times3=36$ unique complete tuples/given tasks. Numerical estimates repeat under horizontal translation but graph/b-polynomial givens differ; answer-only deduplication is inappropriate. Fingerprint recipe/version/branch and all displayed $(h,L,n,k)$ plus response/part structure. App must reserve unseen fingerprints across practice/test for each learner and preserve old snapshots. Exhaustion is a typed finite-bank condition; no silent reset, substitution of a curve with different bias, or expansion beyond approved bounds. The pilot has just36 choices and must disclose that limit. Constructive enumeration avoids rejection loops.

Invalid/rejected: $n=0$, unequal widths passed to the equal-width rule, $h=0$ outside this domain (not mathematically invalid), $x\le h$ in any log ordinate, hidden poles, noninteger or much larger strip counts outside the selected workload, mixed-curvature replacement and inconsistent diagram parameters. Lowest admitted width is1 ($L=4,n=4$); the log graph still needs both sides of its intercept in(c), including $h<x<h+1$ where $y<0$.

Numerical bounds are a proposed modest subset of the four-strip source and two-strip textbook cases; they are not an official statement that8 strips are required (this branch permits only2 or 4). The easiest estimate is at grade-e described complexity; the complete log/graph/bias chain is bounded by the observed source and grade-c/a descriptions. Independent review must calibrate the proposed branch, not infer grade from marks or Bloom.

## Assets and required response — must-read givens (R3-07)

(a,b) given representation `text`: must read limits, log base $e$, the shift, interval count, expanded square, multiplicative factor and hence instruction. No supplied curve gives away(c). (c) response `sketch`; optional blank axes only, not a graph of the current answer. Fixed axes are Cartesian with labelled $x,y$; variable window allows the vertical line $x=h$ and intercept $h+1$ to be labelled distinctly. Response-frame width/height is not a measurement scale.

Canonical solution asset `solution-log-graph`: fixed: one increasing, concave-down log branch, vertical asymptote and axes; variable: $h$, axis/window/labels, quadrature nodes and optional dashed chord overlay. Relations: domain $x>h$, asymptote $x=h$, intercept $(h+1,0)$, no $y$-intercept because $h\ge1$, curve tends to $-\infty$ as $x\downarrow h$, gradient decreases while remaining positive. Show part of the curve below the $x$-axis and above it. For(d) put trapezium top chords below the curve over the integration interval, from exactly the same nodes as(a). **Must-read/check:** exact asymptote/intercept labels, domain side, axes, interval limits and strip count; these cannot be cropped or overwritten by tick/ordinate labels. Shaded area, if used, is exactly the region $h+1\le x\le h+1+L$, $0\le y\le\ln(x-h)$.

Marker needs actual sketch features, not image presence alone. Accept equivalent hand-drawn curves irrespective of pixel-perfect shape; do not require a point table or an analytically derived second derivative. No physical calibration or visual measurement is requested. Owner decision6 includes diagram/sketch demands; actual generated-image consistency, capture, recognition and feedback are unverified and require later app tests, not a capability exclusion.

## Canonical mathematics and marking

$T=\frac\Delta2[y_0+2(y_1+\cdots+y_{n-1})+y_n]$, with $y_j=\ln(1+j\Delta)$; $J\approx2kT$. Preserve unrounded ordinate values until final rounding. If decimal ordinates are displayed, retain at least4 decimal places and sufficient hidden precision. Canonical exact-integral check is $[(x-h)\ln(x-h)-(x-h)]_{h+1}^{h+1+L}$; learners are not required to know it.

Full criterion prefix `WB8227-trapezium-sketch-estimate:`. Proposed adapted criteria follow official Q6, including source `DB1` dependency in(d) rather than silently flattening it.

| ID | Marks | Earns / dependency / alternative |
|---|---:|---|
| `a:B1` |B1| Correct positive width $L/n$, possibly embedded in working. |
| `a:M1` |M1| Correct endpoint/interior weighting or summation of the actual trapezium areas using positive width. |
| `a:A1` |A1| Correct3 sf estimate, dependent on a valid trapezium method; independently correct numeric result with no required method evidence does not establish M1. |
| `b:B1` |B1| Factor the quadratic and show $k\ln((x-h)^2)=2k\ln(x-h)$ on the integration interval. |
| `b:B2` |B1 FT| Use $2k$ times their(a), with coherent rounding; cue and explicit follow-through edge `a→b`. |
| `c:B1` |B1| Single correct increasing log shape on $x>h$, with below/above-axis portions. Auxiliary asymptote/chords are not extra function graphs. |
| `c:B2` |B1| Correct labelled vertical asymptote $x=h$. |
| `c:B3` |B1| Correct labelled intercept $(h+1,0)$. |
| `d:B1` |B1| Underestimate, consistent with the relevant portion of their sketch. Cue edges `a→d` and `c→d`. |
| `d:DB1` |DB1| Top chords/trapeziums lie below the curve on the integration interval; depends on `d:B1`. |

Total(a,b,c,d) **3+2+3+2=10**. Exact logarithms in a correctly weighted formula and a final rounded value are valid. (b) has a special cap **SC1/2** for correct result obtained without hence; compare with the main2 mark path and take the maximum, never sum. If(b) uses the stated3 sf(a), credit coherent FT even if the last digit differs from unrounded canonical scaling; see boundary exemplar7.96 versus7.97. This is an explicit proposed rounding implementation of the source’s “$6\times$ their(a)” rule, for independent review. Incorrect log law such as squaring $T$ does not earn transformation credit; arithmetic FT does not authorise a wrong scale.

Answer-only: (a) a bare numeric answer does not demonstrate the requested trapezium method; award the independent width B1 only if inferable from an explicit width, and withhold A1 without valid method under this proposed memo. (b) correct bare $J$ can receive SC1 but not the2 mark hence path. (c) the sketch itself is the complete response and can earn3/3 with no prose. (d) “underestimate” alone earns at most1/2 and only if consistent with their sketch. No blanket no-working rule applies to other parts/recipes. “Increasing” alone is not a bias reason; “concave down” plus a correct own sketch can be accepted as mathematical shorthand for chord placement. Bare “concave/convex” follows whichever convention is evidenced by their curve, not the textbook’s potentially reversed naming.

Potential marking interpretation to review: the source’s “must be correct from their graph” does not explicitly resolve every incorrectly sketched but self-consistent overestimate. Proposed branch credit requires the actual correct logarithmic shape and underestimate, with reason tied to that sketch; do not claim official general follow-through on a wrong function graph. Preserve submitted sketch and flag ambiguous recognition rather than manufacture reliable marks.

## Bloom, support and test boundary

Classification version `8227-pilot-design-0.1.0`, all proposed pending independent review. Part(a) Apply3: execute width/weight/rounding, criteria a:B1/M1/A1. Part(b) Apply3: factor a familiar square and apply log law/hence scale, b:B1/B2. Part(c) Apply3: execute a familiar log transformation, c:B1/B2/B3. Part(d) Analyse4: relate the chord/trapezium geometry to the curve to justify the sign of the error, d:B1/DB1. Whole-card maximum **4**, not a mark-weighted average. It does not make the numerical calculations level4. Any future supplied-graph/omitted-sketch branch needs fresh classification and references.

Practice help before submission may explain endpoint/interior weights on a different function/interval, not provide current ordinates, graph, integral or bias. A different-instance worked example must be separately bound. Reveal current frozen solution and credited/repair criteria after submission. Test permits no hints/examples/tutor on an unsubmitted question and preserves per-question post-submission review/timer pause. A corrected response is not a new unaided observation; another fresh instance can be requested without passing first. App owns assignments, unlocks, boxes, billing and saved attempts.

For the normal exemplar: full valid $T=3.81$, log-law scale $J=15.2$, correct sketch and chord explanation earns10/10. Correct(a), $J=T^2$, correct(c,d) earns8/10 (b0), with feedback first recognising correct quadrature then replacing squaring the estimate by a log-law transformation. Independent exact integration for(a) is a valid mathematical computation but does not fulfil “use trapeziums”; do not award the requested method. Missing asymptote loses only c:B2, not all sketch marks. An unreadable curve with “under” stays unresolved until evidence can be read; retain original submission and ask for clarification. A source-consistent transformed integral computed directly without hence receives at most SC1 for(b), not double method credit.

## Acceptance checks and limits

Manual normal/changed/boundary examples, separate trapezium-area sums, analytic-integral bias checks and36tuple enumeration are recorded in the exemplar and planner JSON. Stage E/F must independently check all36 tuples, all ordinate domains, all line/curve/chord data and marking samples; replay seeds0/1/42/$2^{63}-1$, exhaustion/no repeats, admitted width1 and invalid domains. No runtime tool has passed merely because this matrix is specified.

Use the existing 7 November 2026 pinned learner-text guideline/provenance snapshots at `workbench/playbook/guidelines/`. Raw decoded LaTeX, graph labels, part IDs, current/history render, teacher/learner projections, same-instance solution binding, wording attribution and reveal timing still need author/app tests. User-authorised attributed exam originals are permitted; textbook originals remain internal. No source/report prose is silently converted into learner feedback. Vitalis approves this proposed scope, finite36 capacity, visual requirements, adapted credit/Bloom and exemplars before stage E. Cross-vendor review and app/production acceptance remain separate.
