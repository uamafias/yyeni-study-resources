# Findings: 8227 Mathematics Workbench steps 1–3 and framework extensions

Review round `opus-5-5-step-1-3`. Reviewer: Claude Opus 5.5 (cross-vendor; the
author pass was Codex). Frozen input: commit `11cd03fe639f9936dd9f83fd04bd6f04d5181676`,
manifest `analysis-snapshot.json` sha256 `1afe99d5…a561f` (all 35 file and 20 source
hashes verified; see `inputs.json`). Scope: source/syllabus/demand/pattern analysis
and the 15 November framework additions. No recipe, generator, branch or seed exists,
so every finding's recipe/version/branch/seed field is **N/A**.

Severity follows the REVIEWER brief, read for analysis records: **high** would
mis-shape planning, marking or coverage if carried into work orders; **medium** is
inaccurate or incomplete in a way that affects scope, branches, marking or teaching;
**low** concerns traceability or tidiness. **WO-blocking** means it must be resolved
before any work order is written for the affected scope. Every finding is `open`.
The repair owner is the author (Codex, for Vitalis) unless an escalation is named.
No finding is author-verified or independently accepted yet.

Locators: paper PDFs are under `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/<year>/`
and reports under `Question Banks/Namibian Examiner Reports/NSSCAS/<year>/`. "P1 p7"
means PDF page 7 of that year's Paper 1. Analysis files are under
`work/nam-8227-nsscas-2026/workbench/analysis/` unless another path is given.

---

## A. Confirmed defects

### R13-01 — Objective coverage is derived only from family primary objectives · high · WO-blocking

- **Locator.** `tools/build_analysis.py` line 138 (`oids = primary objectives of the part's families`) and line 214 (coverage rows built from `families[...]['primary_objective_id']`); `coverage-matrix.json`; `question-analysis.json` `other_directly_assessed_objective_ids`.
- **Expected.** Each part records the objectives and atomic demands it directly assesses, independently of how parts are grouped into families. Coverage is then computed from those links (templates.md, demand registry and Q02 "selected demand → assessed part evidence").
- **Actual.** A part can link to an objective only if some family names that objective as its *primary* objective. Nine of the ten "unlinked" objectives have no family at all (M1 T3 O01, T4 O01, T5 O01, T6 O01, T6 O04, T7 O01, T7 O03, T8 O01, T9 O01). The tenth, M2 T6 O02, has only PAT-62, which has no parts. So their zero counts follow from the encoding; they are not findings about the corpus. Parts that directly assess several of these objectives, verified against the papers:
  - **T7 O01 (3D coordinates).** 2024 P1 Q10(a), p12: A, B, V and N must be located in 3D from the pyramid diagram before AN = −3i + 6j + 7k can be shown.
  - **T7 O03 (position and displacement vectors).** 2021 P1 Q6(a), p7; 2022 P1 Q11(a), p14; 2023 P1 Q7(a), p12; 2024 P1 Q10(a, b).
  - **T4 O01 (graph ↔ equation).** 2024 P1 Q8, p10: line AC, the perpendicular through B, then a reflection. 2025 P1 Q12(a), p18: the equation of diagonal BD.
  - **T8 O01 (gradient notation and interpretation).** 2023 P1 Q11, p18 ("Find f′(x) and f″(x)"); 2025 P1 Q8(a), p11 (substitute into the given dy/dx; no differentiation).
  - **T9 O01 (integrate (ax+b)ⁿ).** 2023 P1 Q12, p19 (∫18(3x+2)⁻²dx); 2021 P1 Q4(a), p5.
- **Educational consequence.** The matrix tells planners that foundational, regularly examined demands are unobserved. Those demands could then be pushed into "syllabus-derived" recipes or supporting drills, or kept out of the connected structures where they are actually examined. Re-tagging families to fix it would inflate family counts.
- **Minimal correction.** Add per-part `directly_assessed_objective_ids` and `directly_assessed_demand_ids` that do not depend on `pattern_ids`. Regenerate `coverage-matrix` from those fields and keep family membership as a separate relation.
- **Verify.** Rebuild, then confirm that the parts listed above link to their objectives. Confirm that the coverage computation no longer reads `families` at all.

### R13-02 — No part→demand links; demand dispositions are boilerplate; unobserved demands are hidden · high · WO-blocking

- **Locator.** `demand-dispositions.json`, all 138 rows; `build_analysis.py` lines 252–260. A search for `:D0` returns 0 hits in `question-analysis.json`, `problem-patterns.json`, `coverage-matrix.json` and `textbook-samples.json`.
- **Expected.** Every demand gets include, exclude or hold, with a hold ID and reason codes where needed (README §4, §C). Unobserved demands stay visible and are labelled "syllabus-derived, not examination-evidenced".
- **Actual.** All 138 rows read `include` with identical text. Each row carries the same two conditional "holds" ("unverified award rules…", "visual assessment if…"). `related_pattern_candidates` is copied from the objective, so every demand of an objective has the same list, and 17 demands have none. `direct_vs_prerequisite` holds the same placeholder in all 138 rows.
  - These syllabus demands are **not assessed by any 2021–2025 part** (regex scan of all ten papers, confirmed by reading): increasing/decreasing intervals (M1 T8 O03 D02), points of inflexion (M1 T8 O04 D02, inflexion branch), division by a quadratic (M2 T1 O03 D02), segment area (M1 T5 O02 D03; the word "segment" never occurs), constructing a unit vector (M1 T7 O03 D01; 2024 P1 Q10 uses i, j, k only as axis notation), a cubic from a graph (M1 T1 O05 D02), failure of an iteration to converge (M2 T6 O02 D02), and principal-value inverse trigonometry (M1 T6 O04; only the defective 2023 P1 Q9, see R13-04).
  - Their parent objectives nevertheless show between 1 and 16 "observed" links.
- **Educational consequence.** Syllabus-derived demands would be presented as examination-observed, or silently dropped, because nothing distinguishes them at demand level. Selection decisions cannot be audited.
- **Minimal correction.** Map each part to demand IDs (R13-01). Give each demand a real disposition, its observed or unobserved status, hold IDs with reason codes, and its prerequisite or context role. Retain the grouped "include" only where a reason is stated.
- **Verify.** Every demand either has at least one part link or carries the explicit syllabus-derived label. A rescan of the papers for the demands listed above agrees with the registry.

### R13-03 — Explicit part dependencies and follow-through are missing in 18 questions · high · WO-blocking for affected questions

- **Locator.** `question-analysis.json` `dependencies`, and the hard-coded `EXPLICIT_DEPENDENCIES` dictionary in `build_analysis.py` lines 93–111.
- **Expected.** Explicit wording cues (Hence, Hence or otherwise, found in part, using your…, these values) and award-table follow-through become annotated edges, with the cue type recorded. Reports state: "If the question states 'hence' and the previous question is not used, no marks may be awarded" (2021 report p236; 2023 p330; 2024 p335). One award table nonetheless gives "SC 1: Correct but hence not used" (2023 P2 Q6(b), report p337), so the rule is set question by question.
- **Actual.** No edge exists for the following. Each was confirmed on the paper text and, where an award table exists, on the table.

  | Question | Missing edge | Cue / evidence |
  |---|---|---|
  | 2021 P1 Q12 | a→b, a→c (b→c) | "For the value of k found in part (a)" (p14–15) |
  | 2021 P2 Q6 | a→b | "Hence" (p8) |
  | 2021 P2 Q12 | a.i→a.ii | "Hence" (p14) |
  | 2022 P1 Q1 | a→b | "Hence, or otherwise" (p2) |
  | 2022 P1 Q2 | a→b | "Hence" (p3) |
  | 2022 P1 Q9 | a→b | "Hence" (p12) |
  | 2022 P2 Q1 | a→b | "Hence, using logarithms" (p2) — also a method restriction |
  | 2022 P2 Q4 | a→b | "When a and b are these values" (p6) |
  | 2022 P2 Q6 | a→b.i, a→b.ii | "Hence" (p8) |
  | 2023 P1 Q2 | c.i→c.ii | "Hence" (p5) |
  | 2023 P1 Q8 | a→b | "Hence" (p15) |
  | 2023 P2 Q8 | a→b | "Hence"; award p339 "Substitute (0, 2)" into the (a) result |
  | 2024 P1 Q12 | a→b | "Hence" (p16) |
  | 2024 P2 Q9 | a→b | "Using your value of tan x in part (a)"; award p342 "F.T. Use their tan x = 4" |
  | 2024 P2 Q10 | a→b | award p342 "F.T. From their y′ in part (a)" |
  | 2025 P1 Q5 | a→b | "Hence" (p7) |
  | 2025 P1 Q6 | a→b | "Hence" (p9) |
  | 2025 P2 Q4 | a→b | "the true value of the integral in part (a)" (p4) |

  **Probable given-reuse edges, also missing.** 2021 P1 Q8 (b needs the total from a); 2022 P2 Q9 (a→b; b.i→c.i); 2023 P1 Q4, Q5 (a→b→c, admissibility), Q6, Q7 (a.i→a.ii); 2024 P1 Q4 (a→b, c), Q6 (a→b, c), Q7, Q13 (a→b); 2025 P1 Q10. Treatment is inconsistent: 2021 P1 Q1 and Q6 have edges, while the structurally identical 2023 P1 Q4 and Q7 do not.
- **Educational consequence.** Work orders would lose "hence" method restrictions, special-case credit and follow-through rules. The result would be wrong credit for alternatives and feedback that ignores the intended chain of reasoning.
- **Minimal correction.** Annotate every explicit-cue edge with its cue type and every award F.T. edge, and separate implicit given-reuse edges. Add a scripted cue scan to the builder so new cues fail loudly.
- **Verify.** The cue scan (method in `inputs.json`) reports no unannotated explicit cue, and every F.T. row in a linked award table maps to an edge.

### R13-04 — 2023 P1 Q9 asks for a principal value outside the principal range · high (source defect) · WO-blocking for T6 O04 and PAT-21

- **Locator.** 2023 P1 p16 (visually confirmed): "Find the possible values of x correct to 2 decimal places for which sin⁻¹(x² − 2) = 2π/3." Mapped as PAT-21 / M1 T6 O03 + T1 O04 with no source hold. Report 2023 p325 discusses it as an ordinary item.
- **Expected.** The syllabus (M1 T6 O04, PDF p11) and the exam's own formula list ("Principal values") define sin⁻¹ on [−π/2, π/2]. Under that convention the equation has **no** solution.
- **Actual.** 2π/3 ≈ 2.094 > π/2 ≈ 1.571 (recomputed). The non-principal reading x² − 2 = sin(2π/3) gives x = ±1.69, but sin⁻¹(√3/2) = π/3, not 2π/3. The author flagged neither this nor its effect on T6 O04 coverage.
- **Educational consequence.** A recipe, worked solution or feedback modelled on this item would teach that sin⁻¹ can return 2π/3. That contradicts a named syllabus requirement and the supplied formula sheet.
- **Minimal correction.** Add a source hold (for example `SRC-8227-PRINCIPAL-2023-P1-Q9`) and exclude the item as an exemplar. Mark M1 T6 O04 syllabus-derived. **Escalate to Jeremy/Vitalis:** is a scheme or erratum available, and should principal-value recipes proceed on a syllabus-derived basis?
- **Verify.** Re-render p16. Recompute 2π/3 against π/2. Confirm the hold appears in `question-analysis.json` and in the selection record.

### R13-05 — 2023 P1 Q1(b) claims distinct real roots where the equation degenerates · medium (source defect) · WO-blocking for the discriminant-proof branch

- **Locator.** 2023 P1 p3 (visually confirmed): "Show that the equation px² + 3px + 2p = 2x² − x − 3 has distinct real roots for values of p, (p ≠ −5)." Mapped to PAT-02 with no hold. Report 2023 p320 asks only for Δ > 0 "for any value of p".
- **Expected.** A discriminant argument requires a nonzero leading coefficient (p ≠ 2).
- **Actual.** The equation becomes (p−2)x² + (3p+1)x + (2p+3) = 0 with Δ = (p+5)². At p = 2 it is linear (7x + 7 = 0), with the single root x = −1 (recomputed), so the statement is false at p = 2.
- **Educational consequence.** A proof branch copied from this item would omit the a ≠ 0 condition, a standard and examinable logical step.
- **Minimal correction.** Hold the exemplar's exact givens. Any authored proof branch must state or require a ≠ 0. Record this as a source defect next to SRC-8227-DOMAIN-2022-P1-Q13.
- **Verify.** Check the recomputation, and confirm the hold is recorded.

### R13-06 — Official 2023 P2 Q7(c) award table accepts a degree-mode answer that does not solve the problem · medium (marking-source anomaly) · WO-blocking for numerical-method marking

- **Locator.** Report 2023 PDF p338, Q7(c): the table lists a radian route to a = 1.587 and an "OR" route a₂ = 0.992360…, a = 0.995. The commentary states "Both radians, as well as degrees gave a solution within 4 steps."
- **Expected.** Workbench marking adopts only alternatives that are valid.
- **Actual.** The radian fixed point 1.587275 satisfies the integral condition: F(a) = a³ + 2cos2a + sin a − 2 = 0.999998 ≈ 1. The degree-mode value 0.994586 gives F = −0.990 and lies outside part (b)'s bracket 1.3 < a < 1.6 (all recomputed). Neither the author's analysis nor the excerpt link records this.
- **Educational consequence.** Adopting the official alternative would credit a wrong answer and teach that calculator angle mode does not matter. The reports themselves warn about this repeatedly (2023 p330; 2024 p335).
- **Minimal correction.** Record a marking-source anomaly and do not encode the alternative. **Escalate to Jeremy/Vitalis** with the recomputation as evidence. Workbench rule: radian mode is required where the integral and limits are in radians.
- **Verify.** Re-run the recomputation (`inputs.json` → `mathematical_sampling`).

### R13-07 — Embedded award excerpts undercounted (24 questions, not 22) · medium · WO-blocking for 2021 P2 Q2 and Q4

- **Locator.** `build_analysis.py` line 86 `MEMO_PAGES['2021-2'] = {1:[237], 3:[238]}`. Counts in `analysis-checks.json`, STATUS, corpus-analysis and acquisition-gaps.
- **Expected.** Every award table found in the reports is linked.
- **Actual.** Report 2021 p237 also gives Q2's table: B1 "kln(2x+1)", B1, M1 for limits, E1 "Use log laws and establish the given result … = ln 81". Report 2021 p238 gives Q4(a) "B1 correct shape in the first quadrant only; B1 5000 seen" and Q4(b) "B1 M1 A1 … t = 34, Accept: 35". Neither is linked. 2021 P2 Q4(a) is a CAP-8227-02 sketch part whose official visual criteria are therefore available but unrecorded. Correct census: 2021 P2 Q1–Q4, 2023 P2 Q1–Q9 and 2024 P2 Q1–Q11, which is 24 questions. No award tables exist in any Paper 1 section or in the 2022 and 2025 reports (per-page scan).
- **Educational consequence.** Missing official criteria for one sketch item and one quoted-answer item, so marking rules for them would be invented unnecessarily.
- **Minimal correction.** Link both pages and correct the counts. Generate excerpt pages by scanning rather than by hard-coding (see R13-17).
- **Verify.** An award-row scan of the five Mathematics sections reproduces the 24-question census.

### R13-08 — Objective and family mis-tags; directly assessed secondary objectives omitted · medium · WO-blocking for affected families

- **Locator.** `question-analysis.json` parts below, generated from `analysis_inputs.py` `QUESTIONS`.
- **Expected.** Each part's primary and directly assessed objectives match the work the part requires.
- **Actual (verified against papers and, where cited, reports):**
  - **Mis-tags.**
    - 2021 P2 Q9(b) is tagged PAT-33 / T9 O03 (definite integral) but is **indefinite**. Report p241 says the "final accuracy mark was lost for omitting the constant".
    - 2021 P2 Q11(a) and 2022 P1 Q2(a) are tagged PAT-04 / T1 O04 (quadratic in a function of x), but both are ordinary quadratics. The disguise appears only in part (b).
    - 2025 P1 Q8(a) is tagged PAT-27 / T8 O02 (differentiate), but the part only substitutes x = 2 into the given dy/dx (T8 O01).
    - 2023 P1 Q10(a) carries PAT-31 (connected rates) but is a maximum-height problem.
    - 2022 P2 Q8 carries M2 T2 O03 (solve aˣ = b), but the step equates logarithm arguments (M2 T2 O01).
    - 2025 P1 Q4(c) on Paper 1 is mapped primarily to M2 T6 O01. M1 T4 O02 (intersections ↔ roots) fits better.
  - **Model-construction parts attributed to calculus objectives.** 2022 P1 Q8(a) (+T8 O04), 2022 P1 Q12(a) (T8 O03), 2023 P1 Q13(a), 2024 P1 Q11(a)–(b) and 2025 P1 Q9(a) (T8 O04) contain no differentiation. They are "show that" derivations from mensuration, similar triangles or perimeter. Report 2023 p326 says Q13(a) "required pre-knowledge on mensuration". This inflates T8 O04 (16 links) and leaves the modelling demand (assessment ability 8) unrepresented.
  - **Secondary T1 O06 (solve quadratic inequalities) omitted** where it carries marks: 2021 P1 Q10(a), 2022 P1 Q4, 2024 P1 Q5(a), 2021 P2 Q3 (award p238 "(x+2)(x−1)<0 … Must be a single inequality") and 2024 P2 Q3 (award p337 "Solve single quadratic inequality"). Coverage shows only 2 links.
- **Educational consequence.** Calculus coverage is overstated, quadratic-inequality coverage is understated, and the model-building step that examiners report candidates failing is lost.
- **Minimal correction.** Retag. Add a "construct model / establish quoted expression" demand or role (prerequisite-dependent), and record the NSSCO prerequisites it uses (see R13-21).
- **Verify.** Re-inspect the listed parts and rebuild the coverage counts.

### R13-09 — Family distinctions unrecorded; selection table below template; families both collapsed and fragmented · medium · WO-blocking (Q08)

- **Locator.** `problem-patterns.json`: all 62 `distinction` fields equal the title plus "different values alone do not justify another pattern" (`build_analysis.py` line 79). `selection-table.md` has 5 columns.
- **Expected.** Each separate recipe or branch states the learner decision that discriminates it, with response evidence (README §C). The selection table carries paper and marking locators, representation, connected parts, hold IDs, the distinguishing decision and the evidence basis (templates.md).
- **Actual.** Only ten families receive a structural discussion, in `corpus-analysis.md`. My reading of all member parts found:
  - **Collapsed families** (distinct reasoning grouped together): PAT-18, which mixes line/shape coordinate geometry (2024 P1 Q8, 2025 P1 Q12) with curve intersections and tangency; PAT-31 (connected rates vs kinematics by differentiation vs rate evaluation); PAT-54 (standard antiderivatives vs reverse-of-a-given-derivative vs algebraic pre-processing such as division); PAT-47 (proof vs equation solving vs exact evaluation); PAT-20 and PAT-38 (graph reading vs sketching); PAT-24 (reading 3D diagrams vs given position vectors); PAT-02 (parameter range vs proof for all values vs rational-root proof).
  - **Fragmented families** (one connected structure split by part): PAT-14 to PAT-17 (one function-analysis chain); PAT-09, 10, 12 and 13 (progressions); PAT-59 to PAT-61 (one numerical-method chain). Singletons: PAT-08, 11, 21 and 25.
  - The full per-family assessment is in `report.md` §4.
- **Educational consequence.** Recipe economy cannot be judged. Both inflated and collapsed recipe sets are likely if the 62 families are used directly.
- **Minimal correction.** For each family, record its discriminating decision and evidence, and its connected-structure membership. Restructure as proposed in `report.md` §4 before any PLAN. Do not convert the family total into a recipe count.
- **Verify.** Independent re-review of the restructured selection table against the template columns.

### R13-10 — Capability holds not carried into selection; sketch-dependent marking parts unflagged · medium · WO-blocking for affected branches

- **Locator.** `selection-table.md` rows PAT-17, PAT-43, PAT-57, PAT-58, and the sketch branches of PAT-20 and PAT-38, all marked "include for analysis/design review". `question-analysis.json` 2023 P2 Q6(d) and 2025 P1 Q4(c) have `capability_hold: null`.
- **Expected.** A selection whose required response or marking is unverified carries a hold with an ID and reason code `capability` (README §4). It is not shown as a plain include.
- **Actual.** CAP-8227-02 is attached only at part level to the 11 sketch parts. All 11 are correctly identified. But 2023 P2 Q6(d) is marked "Must be correct from their graph" (award p337), and 2025 P1 Q4(c) says "Use your graphs…". Both depend on reading the learner's own sketch and are not flagged.
- **Educational consequence.** Downstream planning could schedule held branches as ready, or build feedback that cannot evaluate the sketch it depends on.
- **Minimal correction.** Add selection-level hold IDs for the sketch branches, and flag the two dependent parts with CAP-8227-02.
- **Verify.** Every selection containing a CAP-8227-02 part shows the hold.

### R13-11 — Syllabus grade descriptions (pp19–24) and MF9 (pp25–30) not used · medium · WO-blocking for demand bounds

- **Locator.** `syllabus-page-evidence.json` holds pages 1–2 and 6–18 only. `source-holdings.json` 8227-SRC-001 says "pp7-16 and assessment pp17-18 read". No analysis file mentions grade descriptions or MF9.
- **Expected.** The syllabus is read first-hand for scope and level, including its own grade descriptions, which are official statements of what learners at grades a, c and e demonstrate.
- **Actual.** The grade descriptions state assessed demand detail that sits outside or beyond the specific bullets. Examples:
  - binomial expansion multiplied by a linear or quadratic expression (p19);
  - finding the domain for which a function is one-one, and inverses involving fractions (p19, p21);
  - quadrilaterals and triangles with their associated equations (p19);
  - combined remainder and factor theorem (p20);
  - log inequalities, and graphs of y = e^(ax+b) + c and y = ln(ax+b) + c (p20);
  - y = a|x+b| + c (p20), the form 2023 P2 Q2 uses, whereas the specific bullet lists only |ax|, |ax+b| and |x|+c;
  - quadratic equations established from trigonometric identities (p20);
  - locating a root "using an explanation", and forming an iteration "in more complex cases" (p21).

  MF9 (pp25–30) is broader than the content: it includes rational-n binomial, integration by parts, ∫1/(x²+a²) and tan⁻¹ derivatives. It must not be read as scope.
- **Educational consequence.** Variation bounds and branch lists set from the bullets alone would be too narrow (modulus and log graph forms, binomial products), or could import beyond-scope MF9 items.
- **Minimal correction.** Transcribe the grade descriptions as level-descriptor evidence with page quotations, linked to demands and source kind `syllabus`. They do not create new objectives. Record that MF9 is not a scope extension.
- **Verify.** Every grade-description statement is either linked to a demand or noted as not adding a demand.

### R13-12 — Explicit syllabus qualifiers missing from `syllabus-exclusions.json` · medium · WO-blocking for variation domains

- **Locator.** `curriculum/syllabus-exclusions.json`, 8 limits.
- **Expected.** Every stated limit or qualifier is recorded (TEAM-PLAYBOOK step 2; README §B).
- **Actual.** The following are absent:
  - "where a, b and c are integers" (M2 T1 O02, p14);
  - n "a positive integer" (M1 T2 O01, p9; the normalised rule records only the greatest-term limit);
  - "where n is a small integer or a simple fraction" and "easily reducible to these forms" (M1 T6 O06, p11);
  - "simple cases of 'improper' integrals", with the two named examples (M1 T9 O03, p13);
  - "(ax+b)ⁿ for any rational n except −1" (M1 T9 O01);
  - "about one of the axes" (M1 T9 O04);
  - the "in simple cases" qualifiers on M1 T3 O02, O03 and M1 T4 O02;
  - "for any rational n" (M1 T8 O02).
- **Educational consequence.** Recipe variation could exceed the syllabus (non-integer modulus coefficients, general improper integrals, rotation about non-axis lines) or under-use it.
- **Minimal correction.** Add these as bounding qualifiers linked to demands.
- **Verify.** A side-by-side check of pages 8–16 against the exclusions file.

### R13-13 — Objective registry stores scrambled mathematics; the "literal quote" check is tautological · medium · WO-blocking for affected objectives

- **Locator.** `curriculum/objective_registry.json` `syllabus_text` (for example M1 T2 O01 "use the expansion of nba )(…", M1 T5 O02 "s = r θ and 2 2 1 rA…", M2 T1 O01–O02, M1 T6 O02/O03/O05/O06, M1 T7 O01, M1 T8 O01, M1 T9 O02/O03, M2 T5 O01). `build_analysis.py` line 42 (`assert quote in raw`, where `quote` is a slice of `raw`).
- **Expected.** A verified, readable statement of each objective's mathematics, kept separate from the raw extraction.
- **Actual.** All 60 quotes are literal and correctly paged (verified), and no specific bullet is missing. But at least 13 are unreadable mathematically. The assembly check can only confirm that the anchor occurs once; it cannot fail on content. The source's own typo "|a| = |b| =⇔ a² = b²" (p14) is not noted.
- **Educational consequence.** Downstream authors would either re-transcribe (risk of drift) or trust scrambled text.
- **Minimal correction.** Add a `normalized_math_text` field checked against the rendered page, with a reviewer flag. Keep the raw extraction. Note the source typo.
- **Verify.** Sample the normalised text against rendered pages 8–16.

### R13-14 — 2024 P2 Q5(a) source typo unflagged · low (source defect)

- **Locator.** 2024 P2 p6 (visually confirmed). The question defines f(x) = 4x³ + 16x² + 9x − 15, then asks for "the quotient when p(x) is divided by (2x − 1)".
- **Correction.** Record it in the source-defect list. Authored recipes use consistent names. **Verify:** re-render p6.

### R13-15 — Pattern summary contradicted by the diagram/ratio · low

- **Locator.** `question-analysis.json` 2021 P1 Q6 summary: "Point on vector segment…". Page 7 shows AP = (3/2)AB, so P = (0, 6, 0) lies beyond B (external division; AP·OB = 0 recomputed).
- **Consequence.** A recipe built from the summary would cover only internal division.
- **Correction.** Fix the summary and record an external-division branch. **Verify:** re-render p7.

### R13-16 — Textbook defects: p550 resolved; p550 terminology and p560 method advice conflict with official guidance · medium (learner-facing risk)

- **Locator.** `Y=mc as textbook.pdf`, PDF p550 / printed p538 (Try Now 21) and PDF p560 / printed p548 (13.1 Example 1).
- **Expected.** The author's finding SRC-8227-TEXTBOOK-REF is confirmed and, if possible, resolved. Textbook conventions that conflict with official guidance are recorded.
- **Actual.**
  - **Confirmed and resolvable.** Q2(c) asks about "the true value of **the interval in part (a)**", but (a) asks for M. The intended referent is the **integral** ∫₀²xe⁻ˣdx from part **(b)**. The correct verdict is **under-estimate**: f″ = (x−2)e⁻ˣ < 0 on [0, 2), and the trapezium value T = 0.5032 against the exact value 1 − 3e⁻² = 0.5940 (recomputed).
  - **New.** The same page's "REMEMBER" box labels ∪ as "concave" and ∩ as "convex", the reverse of standard convexity terminology. Reports advise against these words (2023 p335; 2025 p358).
  - **New.** p560 Example 1 says "the best method will be to use tables to sketch the graphs". Reports say tables "should NOT be used to draw graphs at this level" (2023 p335; also 2021 p236; 2024 p338).
- **Educational consequence.** Hints or feedback seeded from these pages would mislabel curvature or recommend a method examiners penalise as producing wrong shapes.
- **Minimal correction.** Record the resolution and both conflicts in `textbook-samples.json` and source-inventory. Feedback should use "trapezium tops above/below the curve" and teach standard graph shapes.
- **Verify.** Re-render p550 and p560 and re-run the recomputation.

### R13-17 — Author checks are weaker than their labels; omissions are hard-coded · low

- **Locator.** `build_analysis.py`.
  - Line 42: the quote check is tautological.
  - Line 155: the tariff check accepts the annotated sequence anywhere as a contiguous run on the question's pages, so a one-part [n] matches any [n] and shared pages are not distinguished.
  - Line 267: `checks` values are literal "pass" strings (guarded by earlier asserts).
  - Lines 85–111: `MEMO_PAGES`, `VISUAL` and `EXPLICIT_DEPENDENCIES` are hand lists, which is the source of R13-03, R13-07 and R13-10.
- **Actual impact.** My independent ordered comparison of all brackets per paper reproduces the 10 × 75 = 750 result exactly, so the totals are right. The weaknesses lie in what the checks can detect, not in the present result.
- **Minimal correction.** Compare the full ordered bracket sequence per paper, including label alignment. Derive excerpt pages and dependency cues by scan, with manual overrides recorded.
- **Verify.** Seed one deliberate error into a disposable copy and confirm the builder fails.

---

## B. Evidence gaps

### R13-18 — Representation and input-diagram demands not inventoried · medium · WO-blocking for diagram-bearing branches

- **Locator.** `question-analysis.json` `response_requirement`: 239 of 250 parts read "inspect exact prompt; …". CAP records cover only response sketches.
- **Gap.** Several parts have essential givens or definitions only in the diagram:
  - 2021 P1 Q2 (x-intercepts −2 and 4 appear only on the diagram, p3);
  - 2022 P1 Q10 and 2024 P1 Q9 (a, b, c and the period read from graphs; Q9(c) the sign of f·g read from graphs, p11);
  - 2023 P1 Q6 (C and D on OA and OB; the shaded region, p10);
  - 2024 P1 Q10 (pyramid geometry, p12);
  - shaded-region definitions in 2021 P1 Q9, 2022 P1 Q14, 2022 P2 Q3, 2023 P1 Q12, 2024 P1 Q7, Q14, 2024 P2 Q6(b) and 2025 P1 Q11.

  These require faithful generated assets derived from instance data (README §E; textbook-analysis "Visual problems"), which is a capability distinct from sketch marking.
- **Needed.** A per-part representation field (given representation, what must be read, response format), and a capability entry for generated diagram assets with scale and labelling requirements.

### R13-19 — Assessment conditions from the papers (formula sheet, precision) not recorded · medium · WO-blocking (what is "given")

- **Locator.** Every paper supplies a "FORMULAE AND NOTATIONS LIST" (for example 2021 P1 cover: "Formulae and notations list is provided on page 17"). Covers add "angles in radians to three significant figures", which is not in the syllabus notes. Reports: "Although the formulae are given" (2021 p231); "Candidates should be taught with formula sheets…" (2023 p330; 2024 p335).
- **Gap.** From 2023 the supplied list drops several items present in 2021–2022 (text comparison, 2022 P1 vs 2023 P1): derivatives of cosec x, cot x and tan⁻¹x; ∫1/(x²+a²), ∫1/(x²−a²), ∫1/(a²−x²) and ∫f′/f; and the notation pages. None of this is in the analysis. It determines what a recipe may treat as supplied, what answer-free support may show, and the precision rules.
- **Needed.** An assessment-conditions record per year, with page locators, noting that sheet items beyond the content are not scope.

### R13-20 — Paper–theme cross-assessment not recorded · medium

- **Locator.** `question-analysis.json`. Eleven Paper 2 parts (27 marks) have primary Mathematics 1 objectives, among them the whole of 2022 P2 Q9 (functions with log₂, 8 marks), 2024 P2 Q6(b), 2024 P2 Q10(b) and 2025 P2 Q8 (7 marks). Many more Paper 2 parts carry M1 secondary links. Syllabus p17: abilities "can be assessed in any question in Paper 1 and 2"; pp8, 14: NSSCO knowledge is prescribed.
- **Gap.** `corpus-analysis.md` does not state that Theme 1 content is examined on Paper 2.
- **Needed.** Record the counts. Planning must not assume theme = paper when composing practice or tests.

### R13-21 — Per-part prerequisite roles are uniform boilerplate · medium

- **Locator.** All 250 `prerequisite_context_note` values are identical.
- **Gap.** NSSCO prerequisites carry marks in identifiable parts: mensuration in 2023 P1 Q13(a) (report p326), 2024 P1 Q11(a)–(b) and 2025 P1 Q9(a); similar triangles in 2022 P1 Q12(a); right-angle trigonometry in 2023 P1 Q6(a) and 2024 P1 Q7(a); simultaneous equations in 2021 P2 Q1(a) (award p237 "lost the last mark … for solving the simultaneous equations"). The Workbench rule that supporting-only links do not earn direct coverage cannot be applied without them.
- **Needed.** Per-part prerequisite and context links, distinct from direct demands.

### R13-22 — Examiner-difficulty register is a thin sample · low

- **Locator.** `examiner-difficulties.json`, 12 entries. All 12 were verified at their cited pages.
- **Gap.** The 700-character excerpts run across unrelated questions (ERR02 includes Q4–Q5 text; ERR10 includes Q11(c)). Recurring rules relevant to Workbench answer checking are not captured: radian vs degree mode, premature rounding and exact answers, a single double inequality, "SHOWN" not accepted as a conclusion, working required for quadratic solving, the first-answer-seen rule, and graphs drawn from tables of values.
- **Needed.** Bound each excerpt to its question. Mine the reports systematically for answer-format and method rules, kept separate from misconceptions.

### R13-23 — Textbook sampling breadth and completion method · low

- **Locator.** `textbook-samples.json`.
- **Gap.**
  - The 17 samples cover 20 of 60 objectives. "All thirteen chapters" is true, but the two sections without samples correspond to whole syllabus topics: 3.2 coordinate geometry (M1 T4) and 4.2 trigonometry (M1 T6).
  - Of the revision/"Exam-Style" sets, only Revision Exercise 1 is sampled.
  - Sampled pages contain leads that are not recorded. p50 Revision Exercise 1 Q5 is a cubic from a graph, the only evidence for M1 T1 O05 D02; Q3 is a quadratic in 1/x².
  - TB08 (p326) links to PAT-32 (recover a curve from an initial condition), but that page has no initial condition.
- **Needed.** The completion method proposed in `report.md` §5.

### R13-24 — Reproducibility of derivatives · low

- **Locator.** `analysis/extracted/*`, `source-holdings.json`, `ocr/ymxc/metadata.json`.
- **Gap.**
  - `extracted/*` (reports, papers and syllabus text) is read by both builders, but no generating script is frozen and the files are not among the 35 hashed files. I recorded a directory digest in `inputs.json`.
  - `source-holdings.json` is both input and output. Records SRC-001 to SRC-017 are maintained by hand.
  - pypdf is not pinned.
  - OCR metadata records an absolute path and the Vision revision but not the macOS build. Resume skips existing pages without checking per-page settings.
- **Status.** A rebuild in a disposable copy reproduced all 18 generated outputs byte-identically.

### R13-25 — Third-party mirror provenance not stated for the 2022–2024 reports · low

- **Locator.** `source-holdings.json` SRC-018 to SRC-020 say "Public NANSO Erongo embedded DNEA report". For the 2025 papers, unlike these reports, the record states that official equivalence is unverified.
- **Needed.** "Third-party mirror; DNEA cover verified; official-copy equivalence unverified."

### R13-26 — Rights and storage basis of commercial textbooks in the shared repository · low · escalation to Vitalis

- **Locator.** Commit 11cd03fe adds `Y=mc as textbook.pdf` (148 MB, repository root, LFS), `sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_…2018.pdf` (LFS) and a full 663-page OCR text derivative.
- **Gap.** The records correctly say there is no reuse permission and that the material is internal only. But committing to the shared repository distributes the files to everyone with repository access. The root-level PDF departs from the `sources/` filing convention. The agent copy into `sources/` was done under explicit owner authority (STATUS); the team rule says only people add sources.
- **Escalation.** Vitalis to confirm the sharing basis for the commercial PDFs and their OCR, and to refile the root PDF. This is not an analysis defect.

### R13-27 — Capability and app evidence records incomplete · low

- **Locator.** `capability-gaps.md`; framework audit "Evidence and boundaries".
- **Gap.**
  - The CAP rows lack the template's "Capability evidence checked" field (dated document/code/test locators) and the acknowledgement/disposition fields.
  - The audit cites app revision `0f0832dd…`, which matches. But that checkout has uncommitted changes, including Workbench test files (observed read-only), so the revision alone does not identify the inspected state.
  - My spot check matches FW-07 at code level: `validate_instance()` requires reconciled criteria but no stable IDs; the public `part_id` is `chr(97 + index)`; `PUBLIC_FIELDS` has no Bloom field. That is code reading, not proof of UI or MCP behaviour.

---

## C. Optional improvements

### R13-28 — Framework extensions (subject-neutral) · low

1. **Assessment-conditions record type** (formula sheet / data booklet, calculator, precision and angle-unit rules, per year). It applies equally to Physics and Chemistry data sheets (R13-19).
2. **Level descriptors** (grade descriptions) as calibration evidence for variation bounds (R13-11).
3. **A source-defect register convention**: ID, exact locator, recomputation, disposition (hold exemplar, correct givens in authored recipes, escalate). This would cover SRC-8227-DOMAIN, R13-04, R13-05, R13-06 and R13-14.
4. **In textbook-analysis.md**: a completion/stop rule, and a requirement to record conflicts between textbook conventions and official assessment guidance (R13-16).
5. **A contract decision on Bloom storage**: which labels are author evidence, which are runtime display metadata and which are private marking references. The app's public allowlist has no Bloom field; BLOOM-CLASSIFICATION says to store labels and rationale "with generated content" (R13-27).
6. **Declare the subject-local JSON shapes** (`workbench-analysis-8227-v1`) as subject-local, or bring them into Jeremy's framework through versioned review. templates.md states that "No new schema/tool implementation is authorized".

### R13-29 — Builder hardening · low

Add a scripted dependency-cue scan, an award-row scan, full ordered tariff comparison with labels, a demand-presence scan, and a negative-test fixture (R13-17). Record the tool, Python and pypdf versions in `analysis-snapshot.json`.

---

## Author findings re-examined

| Author finding | Reviewer result |
|---|---|
| SRC-8227-DOMAIN-2022-P1-Q13 (P1 p18: domain x > 0, point P(−2, −1)) | **Confirmed.** Visually re-read. If the point is used anyway, y = 2x² − 6/x − 12 (c = −12, recomputed). Under the stated domain the curve on x < 0 is undetermined, since the antiderivative on each side of x = 0 has its own constant. The report (2022 p306) does not address it. Keep the hold. |
| SRC-8227-TEXTBOOK-REF (p550 / printed p538, TN21 Q2(c)) | **Confirmed and resolved.** "Interval in part (a)" should read "integral in part (b)"; answer: under-estimate (R13-16). |
| CAP-8227-02 "eleven explicit sketch parts" | **Confirmed** that all 11 are correct and complete as sketch responses. Two sketch-dependent marking parts are added (R13-10), and input-diagram demands are a separate gap (R13-18). |
| "750 marks reconcile" | **Confirmed independently** (ordered sequences identical per paper). |
| "22 linked award excerpts" | **Corrected to 24** (R13-07). |
| "Ten unlinked objectives are mapping gaps" | **Confirmed as gaps**, and shown to be an artefact of the encoding (R13-01). At least five are directly assessed. |
