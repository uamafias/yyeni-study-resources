# Review report: 8227 Mathematics Workbench steps 1–3 and framework extensions

Round `opus-5-5-step-1-3`. Reviewer: Claude Opus 5.5 (Claude Code), the independent
cross-vendor reviewer of the Codex author pass. Frozen input: commit
`11cd03fe639f9936dd9f83fd04bd6f04d5181676` on `main`, manifest `analysis-snapshot.json`
sha256 `1afe99d597617897cb3bf0489cd3bcbc236624fef05cef53a8aa4a92704a561f`. All 35 file
hashes, 20 source hashes and 663 OCR page hashes were verified. Exact pages, checks and
limits are in [inputs.json](inputs.json); every finding is in [findings.md](findings.md).
This review covers analysis and selection only. It is not owner acceptance, content
acceptance of any recipe, or evidence about the application.

## 1. Verdict: **repair analysis**

The source preparation is careful and largely trustworthy. Identities and hashes were
checked, acquisitions are traceable, the syllabus was read before the papers, the part
census is complete and the tariffs reconcile.

The mapping layer built on that foundation is not yet fit to underpin planning:

- objective coverage is computed only from family primary objectives (R13-01);
- there are no part→demand links, and the 138 demand dispositions are boilerplate (R13-02);
- explicit "hence"/follow-through dependencies are missing in 18 questions (R13-03);
- the 62 family distinctions are unrecorded (R13-09);
- three unflagged source or marking defects would mislead recipes modelled on them (R13-04 to R13-06).

These are repairs within the existing playbook and inputs, not a reason to redesign the
framework. **No PLAN, work order or recipe should start until the WO-blocking findings
(§7) are closed and the changed scope is independently re-reviewed.**

**Accepted without repair (named sub-scope).** These identity and census facts are
accepted only as far as they are stated:

1. The 20 registered source files: identity, SHA-256, real-PDF status (the HTML/403 file is correctly excluded), and acquisition traceability in the committed Harvester log.
2. Syllabus edition and assessment facts: NIED, December 2020, Grade 12, implementation and first examination 2021. Two compulsory papers of 75 marks, 2 hours and 50% each. Eleven unweighted abilities in one area, assessable in either paper. No command-word table.
3. The 60 specific-objective bullets, which are complete, literal and correctly paged as raw extraction. Normalised mathematics is still pending (R13-13).
4. The 119-question / 250-part census with labels and tariffs, and the 750-mark reconciliation, which I reproduced independently.
5. The 11 sketch-response parts.
6. The 17 textbook sample locators: PDF and printed pages and item identities.
7. The 12 examiner-difficulty citations, which are page-accurate.
8. The OCR derivative's identity as a discovery aid.
9. Source defect SRC-8227-DOMAIN-2022-P1-Q13, confirmed.

None of this acceptance extends to the demand decomposition, objective or demand
mapping, dispositions, families, dependencies, marking rules or capability claims.

## 2. Strengths to retain

- **Syllabus first, with no inventions.** The author correctly found no command-word table and no per-ability weights and invented neither. Paper facts are tied to the page.
- **Source honesty.** Proof-labelled papers, third-party archive provenance for the 2025 papers, the HTML "textbook", the OCR's mathematical unreliability and the missing schemes are all stated plainly. The acquisition of the 2022–2024 reports through the existing Harvester is documented and traceable.
- **A complete, verifiable census.** All 10 papers, 119 questions and 250 parts carry hashed locators, and the 750-mark total reconciles. The builders reproduce byte-identically.
- **Correct restraint.** Bloom is explicitly unclassified, no recipes are claimed, no Studio cards were converted, no app capability is claimed, and 62 is repeatedly called "not a recipe count".
- **Useful structural insight** in `corpus-analysis.md` §"Patterns that require structural distinctions". The ten family discussions there are sound. I agree with all ten, especially discriminant proof vs condition, optimisation models, trig graph reading vs construction, and the numerical-method global vs local claims.
- **Good marking-evidence judgement where it was applied.** The two worked award examples (2023 p331 and 2024 p343) are accurate. So is the caution against turning "hence" into a global prohibition: I found a 2023 award table giving special-case credit when "hence" was not used.
- **Both author source findings hold.** SRC-8227-DOMAIN is confirmed. The textbook cross-reference is confirmed, and I resolved it (R13-16).

## 3. Material findings (summary)

| ID | Sev. | WO-blocking | Finding |
|---|---|---|---|
| R13-01 | high | yes | Objective links come only from family primaries, so the ten "unlinked" objectives are an encoding artefact. At least T4 O01, T7 O01, T7 O03, T8 O01 and T9 O01 are directly assessed. |
| R13-02 | high | yes | No part→demand links; all 138 dispositions identical. Eight syllabus demands have no 2021–2025 part but hide under "observed" objectives. |
| R13-03 | high | yes | 18 questions with explicit "hence"/"found in part"/award F.T. cues have no dependency edge. |
| R13-04 | high | yes | 2023 P1 Q9: sin⁻¹(x²−2) = 2π/3 lies outside the principal range, so there is no solution. Unflagged, and it is the only item on principal values. |
| R13-05 | medium | yes | 2023 P1 Q1(b): the "distinct real roots" claim fails at p = 2, where the equation becomes linear. |
| R13-06 | medium | yes | The official 2023 P2 Q7(c) table accepts a degree-mode answer that does not satisfy the problem. |
| R13-07 | medium | yes | 24 questions have award excerpts, not 22. The links for 2021 P2 Q2 and Q4 are missing, including official sketch criteria. |
| R13-08 | medium | yes | Mis-tags: an indefinite integral tagged definite, plain quadratics tagged "disguised", modelling parts attributed to stationary points. T1 O06 is omitted where awards show it. |
| R13-09 | medium | yes | Family distinctions are title boilerplate and the selection table is below template. Families are both collapsed and fragmented (§4). |
| R13-10 | medium | yes | Sketch capability holds are not carried to selection. Two marking-dependent parts are unflagged. |
| R13-11 | medium | yes | Grade descriptions (pp19–24) and MF9 (pp25–30) are unused, although they widen the assessed forms (for example a\|x+b\|+c, e^(ax+b)+c, binomial products). |
| R13-12 | medium | yes | Explicit syllabus qualifiers are missing from the exclusions (integer modulus coefficients, "simple" improper integrals, axes-only volumes and others). |
| R13-13 | medium | yes (affected) | The registry stores scrambled mathematics, and the quote check is tautological. |
| R13-16 | medium | before textbook-derived hints | Textbook p550: reversed concave/convex labels. p560 recommends plotting from tables, against examiner advice. |
| R13-18 | medium | yes (diagram branches) | Input-diagram demands are uninventoried, and 239 parts have a placeholder representation. |
| R13-19 | medium | yes | The papers' formula sheet and precision rules are unrecorded. The sheet was trimmed from 2023. |
| R13-20 | medium | tracked | Theme 1 content is examined on Paper 2 (27 primary marks), but this is not recorded. |
| R13-21 | medium | with R13-02 | Prerequisite roles are uniform boilerplate. |

The low findings (R13-14, 15, 17, 22–29) cover source typos, a pattern summary, check
strength, reproducibility, provenance wording, rights escalation, capability-record
fields and framework improvements.

## 4. Disposition audit coverage and family assessment

**What I audited.**

- **Syllabus.** All 60 objective transcriptions, all 138 demand labels and all 138 disposition rows. Every one of the 138 dispositions is `include` with identical holds, so there are no exclude or hold decisions to audit (R13-02).
- **Papers.** All 119 question records and 250 part records, against the full text of every paper. Diagram and formula pages were checked visually where the text was scrambled (58 rendered crops over 10 papers).
- **Families.** All 62 families, against their member parts.
- **Marking.** All 11 sketch parts, all 22 linked award excerpts plus the 2 unlinked ones, and all 12 examiner difficulties.
- **Textbook.** All 17 textbook samples, on page images.
- **Selection table.** All 62 rows: 61 "include for analysis/design review" and PAT-62 "include for design review: syllabus/textbook-derived". There are no exclusions.

**What I did not do.** Not every part was independently solved; the solved set is listed
in `inputs.json`. Award tables were not transcribed into criterion-level rules.

**Family assessment.** These are my recommendations for re-structuring. They are not a
recipe count, and any count is premature until R13-01/02/09 are repaired. Codes:
**R** candidate recipe (or group with branches), **B** structural branch inside the
named group, **V** ordinary variation, **D** supporting-drill candidate (needs cited
need, insufficiency argument and owner acceptance), **M** merge into a connected
multipart structure, **H** held (source or capability).

| Families | Recommendation | Basis (examples) |
|---|---|---|
| PAT-01 | B of the quadratic group, and a module inside the function chains (PAT-14–17) | 2022 P1 Q1 standalone; 2024 P1 Q6 and 2025 P1 Q7 feed range/inverse. 2022 P2 Q4(b) is a trivial extremum (V). |
| PAT-02 | Split: **R** parameter-range condition, including the line–curve branch, which needs a quadratic inequality (2021 P1 Q10(a), 2022 P1 Q4, 2024 P1 Q5(a)); **R** proof for all parameter values, with a rational-root branch (2021 P1 Q10(b), 2025 P1 Q1(a)). Root count at a given value is V. | Different evidence (solution set vs argued conclusion). The 2023 P1 Q1(b) exemplar is H (R13-05). |
| PAT-03 | R with branches: polynomial product identity (2024 P1 Q2) and rational identity (2023 P1 Q3, scope note: "in polynomials") | Different procedure. |
| PAT-04 | R with branches: power/radical substitution, exponential substitution (Paper 2, needs logs), and "hence" reuse of a solved quadratic. Remove the mis-tagged 2021 P2 Q11(a), 2022 P1 Q2(a) and 2023 P1 Q9 (R13-08, R13-04). | The recovery and admissibility decision differs by substituted function. |
| PAT-05 | R: quadratic branch (observed); cubic branch syllabus-derived plus textbook p50 Q5 | One exam observation only. |
| PAT-06 | R, plus a D candidate | Reports penalise presentation as two inequalities (2021 p234, p238; 2024 p337). It is also a component in 5 parts (R13-08). |
| PAT-07 | R with branches: product with a linear factor (2021 Q1, 2023 Q4); sum or difference of expansions (2022 Q3, 2025 Q2); term independent of x (2024 Q3) | Each branch has a distinct decision. The grade description covers products. |
| PAT-08, 11 | B inside GP and sum-to-infinity (PAT-10, PAT-12) | Singletons. A Σ representation is a different reading of the same GP. |
| PAT-09, 10, 12 | R each: AP from conditions; GP, including a threshold branch (integer n via logs or inequality, 2024 P1 Q4(b)); convergence condition with a parameter plus sum to infinity with an admissibility check (2023 P1 Q5) | Different decisions. Context, such as inclusive-year counting, is not purely cosmetic. |
| PAT-13 | M: connected AP/GP multipart (2021 P1 Q8, 2025 P1 Q5) drawing on 09/10/12 | The cross-progression link is the decision. |
| PAT-14–16 | M: one connected function-analysis group with branches by function type (radical, log/exp, rational, restricted quadratic) and part modules (domain bound, range on an interval, inverse and its domain, composition including an inadmissible input). D candidates: sign choice for a restricted-quadratic inverse, and range on a restricted domain (ERR04). | The current split is by part, not by decision (R13-09). |
| PAT-17 | H (CAP-8227-02), sketch module of the function group | Visual response. |
| PAT-18 | Split: **R** line/shape coordinate geometry (perpendicular bisector, reflection, midpoint, quadrilateral vertices: 2024 P1 Q8, 2025 P1 Q12; grade-a descriptor); B line–curve intersection and tangency (shared with PAT-02/28); intercept reading V; line sketch H | Collapsed family (R13-09); T4 O01 mapping (R13-01). |
| PAT-19 | Split: **R** symbolic composite perimeter/area (2021 P1 Q7); **R** contact/tangent geometry needing right-angle trigonometry before sector formulae (2023 Q6, 2024 Q7, 2025 Q10); the constraint model is B, feeding PAT-30 (2022 P1 Q8(a)). Segment area is syllabus-derived. | The geometric reasoning differs. Generated diagrams are required (R13-18). |
| PAT-20 | Split: **R** read graph parameters, sign and product (2022 P1 Q10, 2024 P1 Q9; input-visual); sketching H | Reading vs sketching are different capabilities. |
| PAT-21 | H (source defect, R13-04). Principal values stay syllabus-derived. | Only one item, and it is defective. |
| PAT-22, 23 | R prove identity; R "show the equation reduces to…, hence solve" as a connected pair (2022 P1 Q9, 2024 P1 Q12); PAT-23 as branches (quadratic in a trig ratio, tan form, multiple-angle interval as in 2024 P2 Q5(c), radians) | PAT-23 (16 parts) is mostly a secondary tag on other families. |
| PAT-24 | Split: **R** position-vector relations, including the external-division branch (2021 P1 Q6, R13-15); **R** reading 3D diagram coordinates (2024 P1 Q10, textbook TB05) | Different input evidence. T7 O01/O03 (R13-01). |
| PAT-25 | B of PAT-26 (magnitude). The unit-vector branch is syllabus- or textbook-derived (TB06). | Singleton. |
| PAT-26 | R with branches: angle (vector direction choice, 2025 report p347), perpendicularity proof, perpendicularity parameter | Distinct decisions. |
| PAT-27, 50 | B/D components; mostly embedded in larger parts | Thin standalone evidence. 2025 P1 Q8(a) is not differentiation. |
| PAT-28 | R with forward (equation at a point) and inverse (gradient → point or parameter: 2022 P1 Q7, 2024 P1 Q13(a)) branches | The inverse direction is a distinct decision (ERR05). |
| PAT-29 | R with branches by function class. Inflexion is syllabus-derived (R13-02). | — |
| PAT-30 | R optimisation, with shape branches (perimeter→area; fixed volume→surface). The model-construction "show that" demand becomes explicit (R13-08). | Shapes are branches, not recipes. |
| PAT-31 | Split: **R** connected rates (2022 P1 Q12); B kinematics by differentiation with event conditions (2025 P2 Q8, 2023 P2 Q9(a)); rate evaluation V (2025 P2 Q11(c)). Remove 2023 P1 Q10(a). | Collapsed family. |
| PAT-32 | R recover a curve, with branches by the source of the constant. The 2022 P1 Q13 exemplar is H. | — |
| PAT-33, 34, 35, 36 | R definite integral (unknown-limit branch; quoted exact result) with an improper branch (2023 P1 Q12); R area (under a curve vs between curves); R volume (y-axis branch distinct); PAT-36 B of kinematics integration (polynomial vs exponential) | Remove the mis-tagged 2021 P2 Q9(b). |
| PAT-37 | R modulus with branches: simple equation; inequality between two moduli (squaring or critical values, both credited per the 2021 p238 award); line intersection with leg rejection (2024 P2 Q11(b)); graphical deduction (Q11(c)); modulus in an exponent (2025 P2 Q2) | Distinct evidence and case decisions. |
| PAT-38 | Split: reading parameters (2023 P2 Q2, form a\|x+b\|+c per the grade description) B; sketching H | — |
| PAT-39–41 | R division (non-monic linear branch; quadratic divisor syllabus-derived); R coefficients from factor/remainder data (coupled-polynomials branch, 2022 P2 Q4); R factorise/solve (find a factor vs given; "hence" from division; composite-substitution branch, 2024 P2 Q5(c)) | — |
| PAT-42, 44 | R log laws (show-that; inequality with domain conditions, 2024 P2 Q3); R exponential/log equations (single exponential with a context threshold; equating log arguments; exact form). Move quadratic-in-exponential to PAT-04. | PAT-44 (13 parts) is broad. |
| PAT-43 | H (CAP-8227-02); transformed forms per the grade description | — |
| PAT-45 | R linearisation from a given graph (input-visual), with base-e and base-3 branches | — |
| PAT-46, 49 | PAT-46 is component tags (B inside 47/48/56); PAT-49 is B of 48 | — |
| PAT-47, 48 | Split 47: **R** prove identity, **R** solve via identity, B exact evaluation. R R-form with sin/cos-form branches and a reduce-first branch (2025 P2 Q9(b)). | — |
| PAT-51–53 | R product/quotient applications; R parametric (axis-crossing parameter; vertical tangent; numerical parameter from a prior iteration); R implicit (derive, then find the other coordinate) | Matches corpus-analysis. |
| PAT-54 | Split: **R** standard antiderivatives; **R** reverse of a given derivative ("hence": 2021 P2 Q5(b), 2024 P2 Q4(b), 2025 P2 Q10(b)); B algebraic pre-processing (2021 P2 Q9(a), 2024 P2 Q5(b)) | ERR08/ERR12 show distinct difficulties. |
| PAT-55 | R trigonometric integrals with identity branches (double-angle/Pythagorean; reuse an identity at a changed argument; reuse a derivative) | Matches corpus-analysis. |
| PAT-56, 57 | R trapezium, with a log-rescaling "hence" branch (2023 P2 Q6(b)); PAT-57 has a sketch-based branch H and a non-sketch reasoning branch | — |
| PAT-58–61 | M: one connected numerical-method group with branches "given equation" (2021 P2 Q8, 2025 P2 Q12) and "equation derived from a prior calculus condition" (2022 P2 Q5, 2023 P2 Q7, 2024 P2 Q7). The graphical root count's sketch is H. The Paper 1 instance (2025 P1 Q4(c)) belongs with T4 O02. | The origin of the equation is a real structural difference. |
| PAT-62 | Keep visible as syllabus-derived and textbook-derived (Goldie p170). Proposed marking needs owner acceptance. | No exam observation. |

**Inflation and collapse.** Splitting parts into families by part inflates the family
count in the function, progression and numerical areas. Collapsed families hide distinct
reasoning in coordinate geometry, connected rates, antiderivatives, identities, graph
reading vs sketching, and 3D diagrams. The net effect on any recipe count is unknown. It
must come from the repaired demand-level selection, never from 62.

## 5. Textbooks and visual demands

**Current samples (reviewed).** All 17 locators are correct on the page images. The
PDF-to-printed offset is 11 up to p109 and 12 from p155 onwards. Curriculum fit is
reasonable. Two issues:

- TB08's link to PAT-32 is weak, because the page has no initial condition.
- The decisions recorded per sample are sound summaries but do not list the other structures on the same page (R13-23).

Two convention conflicts and one resolved cross-reference are in R13-16.

**What the sampling misses.**

- **Topics.** Coordinate geometry and M1 trigonometry have no samples.
- **Revision sets.** Twelve of the 13 revision/exam-style sets are unsampled.
- **Demand gaps the book could fill.** The book is the only evidence for the cubic from a graph (p50 Q5).
- **Alternative methods.** Tables of values for sketching, and synthetic division by a non-monic linear factor, need to be checked against report guidance.
- **Visual items.** Input diagrams were not inventoried as demands.

**Defensible completion method** (separate from this review, and not done here):

1. Build the population of every Example, Try Now, Exercise and Revision/Exam-style item from the OCR heading leads, confirming item numbering on each page image.
2. Classify each item visually at demand level: decision, givens, representation (input and response), connected parts, and methods shown.
3. Classify exhaustively for the revision/exam-style sets, for any demand with at most one exam observation, and for every visual item.
4. For well-observed demands, continue until two consecutive sections add no new decision or representation, and record the stopping point.
5. Record conflicts between the book's conventions and the official reports, and check answer keys for any item used as evidence.
6. Have a seeded 10% sample double-classified by the cross-vendor reviewer.
7. List unreviewed pages explicitly. OCR mathematics is never evidence.

**Visual demands.** The 11 sketch parts are correct. Add:

- the two parts whose marking depends on the learner's sketch (R13-10);
- the input-diagram demands (R13-18).

Showing a diagram or accepting a photograph proves neither reliable assessment nor
faithful asset generation. No syllabus demand should be weakened to fit the current UI.
The sketch branches stay held.

## 6. Marking, sources, framework, Bloom and honesty

**Marking evidence.**

- **Answer-only credit.** The award tables establish question-specific rules: correct factors without working score 0 (2021 P2 Q1(b), 2023 P2 Q1(b)), and values placed in the formula earn full marks (2023 P2 Q2). The report commentary adds that the final accuracy mark is lost for omitting the constant on an indefinite integral (2021 P2 Q9, report p241).
- **Alternatives.** Alternative routes are explicitly credited (2021 P2 Q3, 2023 P2 Q3(a) and Q5(a), 2024 P2 Q6(b) and Q11(b)).
- **"Hence".** "Hence" can carry zero marks, or special-case credit when it is ignored (2023 P2 Q6(b)).
- **Follow-through.** F.T. is explicit in tables (2023 P2 Q6(d); 2024 P2 Q4(b), Q5(b–c), Q9(b), Q10(b), Q11(c)).
- **Missing schemes.** No Paper 1 has any award evidence, and the 2022 and 2025 papers have none at all. Missing full schemes must stay explicit, and author solutions cannot fill them.
- **Unsafe official rule.** At least one official alternative is mathematically unsafe (R13-06), so official tables still need review before adoption.

**Sources.**

- The edition is confirmed. Proof vs final status for 2021–2023 is unresolved, as are schemes, specimens, manuals, amendments, the teacher guide and the second approved textbook. The acquisition-gaps file records all of these correctly.
- Additions needed: provenance wording for third-party mirrors (R13-25), the formula-sheet record (R13-19) and the source-defect list (R13-04 to R13-06, R13-14).

**Framework.**

- **The extensions extend Jeremy's playbook coherently.** They are small additive edits, the closure-review boundary is stated, Studio conversion is excluded, and app-owned decks are separated.
- **Implemented and proposed are correctly separated.** BLOOM-CLASSIFICATION states that the policy is approved but not implemented. The quality.md additions are marked as not implemented by the CLI. The audit's FW items are proposals, and its verification commands are reported with their FAIL or BLOCKED results.
- **Remaining contract gaps** are in R13-27/28: an assessment-conditions record, use of level descriptors, a source-defect register, textbook convention conflicts, a textbook completion rule, Bloom storage across author evidence, display metadata and private marking, and stable part and criterion IDs.
- **App code.** FW-07 is confirmed at code level only: there are no stable part IDs, and the public `part_id` comes from part order. Exposed connector tool names show no Workbench operation, consistent with FW-09. That is an observation of names, not a test.
- **Scope of the pilot.** High-level Maths does not demonstrate lower-grade or Physics coverage, and the audit's Phase 6 rightly keeps Physics separate.
- **Subject-local schema.** The 8227 JSON record shapes are subject-local. Keep them so, or adopt them only through versioned review.

**Bloom.** The policy is right: the whole card takes the highest genuinely assessed part
level; labels are recipe-version- and branch-specific; incomplete classification stays
explicit; and Bloom is distinct from AO, difficulty and marks. The author leaves all 250
parts unclassified, which is correct while demands and marking are unsettled.

**Honesty.** Processing, author checks, independent review, owner acceptance and future
application testing are kept separate throughout (author-report, snapshot, STATUS).
Minor overstatements to correct:

- "pass" labels on tautological checks (R13-17);
- "22" award excerpts (R13-07);
- "all thirteen chapters" (R13-23);
- the "ten unlinked objectives" presented as open mapping gaps, when the current encoding cannot link them at all (R13-01).

Source extracts are clearly marked internal and not approved for learner reuse. The
repository-sharing basis for the commercial PDFs and OCR is escalated (R13-26).

## 7. Sequenced repair plan

**Must be closed before any PLAN or work order:** R13-01, 02 (with 21), 03, 04, 05,
06, 07, 08, 09, 10, 11, 12, 13 (affected objectives), 18 and 19.

**Can be tracked through a bounded next stage:** R13-14, 15, 16 (before any
textbook-derived hint or feedback), 17, 20 (before test composition), 22–29.

1. **Owner and escalation decisions** (Jeremy/Vitalis; see §8). These can run in parallel with steps 2–4.
2. **Restructure the records** (author).
   - Add per-part directly assessed objective and demand IDs, prerequisite/context links, a representation field (input and response), and dependency edges typed by cue or F.T.
   - Regenerate the coverage and demand dispositions from these, with real include/exclude/hold decisions, hold IDs and observed/unobserved labels.
   - Harden the builder: cue scan, award scan, ordered tariff comparison, negative fixture.
   - Verify by rebuilding and re-running the scans in `inputs.json`.
3. **Complete the syllabus records** (author).
   - Transcribe the grade descriptions as level-descriptor evidence and note that MF9 is not scope.
   - Add the missing qualifiers, the normalised mathematics text (checked against rendered pages), and an assessment-conditions record with formula-sheet changes and precision rules per year.
   - Add the cross-paper theme note.
4. **Apply the corrections** (author).
   - Fix the mis-tags (R13-08).
   - Record source defects and holds (R13-04/05/14/15) and the marking anomaly (R13-06).
   - Record the textbook resolution and the convention conflicts (R13-16).
   - Link the two missing award excerpts and correct the counts (R13-07).
5. **Restructure the families** (author). Record each family's discriminating decision and evidence, restructure per §4, and bring `selection-table.md` up to the template columns, including hold IDs.
6. **Independent re-review** (cross-vendor, selection-only) of the changed records and dependencies. Then the owner's "analysis read" checkpoint, with capability notification evidence in STATUS.
7. **Bounded next stage**, in parallel or afterwards:
   - transcribe the 24 award tables into criterion-level rules, with anomalies held;
   - mine the reports systematically for answer-format rules (R13-22);
   - complete the textbook analysis per §5;
   - continue source acquisition (schemes, final papers, specimens, teacher guide);
   - tidy provenance and reproducibility (R13-24/25);
   - complete the capability records (R13-27).

## 8. Escalations to Jeremy/Vitalis

1. **2023 P1 Q9 principal value (R13-04).** Options: (a) treat it as defective and hold it; build T6 O04 only as syllabus-derived with standard principal ranges (recommended). (b) Seek the DNEA scheme to see what was credited, keeping the hold meanwhile.
2. **2023 P2 Q7(c) degree-mode alternative (R13-06).** Options: (a) do not adopt it, and require radian mode where the problem is in radians (recommended). (b) Ask DNEA for clarification. Either way, record the anomaly.
3. **2023 P1 Q1(b) degenerate case (R13-05).** Hold the exemplar. Proof recipes must state the a ≠ 0 condition.
4. **Grade descriptions as calibration evidence (R13-11).** Confirm they are to bound variation and branch scope. I recommend yes, because they are part of the official syllabus.
5. **Commercial textbooks and OCR in the shared repository (R13-26).** Confirm the sharing basis and refile the root PDF.
6. **Capability notification.** CAP-8227-02 should be extended to the two sketch-dependent parts, and a generated-diagram asset capability added (R13-10, R13-18). These need a recorded acknowledgement before "analysis read".

## 9. Limits of this review

This review covered analysis and selection only. Not every part was independently solved;
the reviewer-worked list and the scripted recomputations are in `inputs.json`. Report
commentary for 2022 pp315–316, 2024 Paper 1 and most of 2025 was not read. The award
tables were read but not transcribed. Only the 17 textbook sample pages and the p550 OCR
record were inspected; the 572 heading-lead pages, the answer keys and the back cover
were not re-inspected. App behaviour, MCP delivery and visual grading were not tested;
three code locations were read. No web sources were re-fetched. Acceptance is withheld
for everything outside the named sub-scope in §1.
