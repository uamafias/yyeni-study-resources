# D2 confirmation findings: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5, cross-vendor REVIEWER. **Date:** 2026-11-24. This check confirms Codex's D2 repair, limited to the changed scope.

**Inputs.** The inputs are frozen in `inputs.json`:
- plan manifest `2b9e53a5…`, content digest `0663d48f…`, recomputed and matching;
- git HEAD `fa0a09d4`.

At the start, all 809 design files, 436 sources and 62 review files matched the manifest. The D1 manifest `c8914cf9…` and all 273 D1 candidate files are recoverable. D2 changed nothing outside `work/nam-8227-nsscas-2026/`, and neither earlier review folder was edited after we wrote it.

**Owner decision.** OD-6 (misread) was taken during this check; see `owner-decisions-2026-11-24-d2.md`.

## Method

**Seven checking agents (Claude, same vendor as this reviewer).** Each one re-tested its scope with its own code and cases, using the D1 agent evidence as the baseline. Their evidence is in the `check-*.json` files:

| Agent | Scope |
|---|---|
| motion | OD-4 motion redesign; S09–S12; misread in motion |
| calc | Implicit normal and stationary; S01, S05–S08 |
| trig | Principal, R-form and log; S03, S04, S13; the rounding count |
| visual | Modulus and trapezium; D1-B01, S14–S21 |
| vecrec | Vector; shared rules; misread rule; register; versions; OD-1 sweep |
| coverage | Counts, Bloom, coverage, weights, receipts, app handoff |
| closeout | R7 residuals S28–S30 |

**Totals across the agents:**
- 122 recomputations, all agreeing;
- 84 marking tests, 76 behaving as expected (each of the other 8 is a finding below);
- 37 native page views.

**What I verified myself:**
- **The misread convention**, on NSSCAS 2025 report PDF 345 and Cambridge `9709_m16_ms_12.pdf` PDF 3, before putting OD-6 to the owner.
- **These findings, read in the current bytes:** D2-S01, S02, S03, S04, S07, S08, S09, S10, S11 and S12.
- **The rebuild**, in two fresh copies (§C).
- **The D2 write scope**, against the D1 baseline.

## A. Dispositions of the D1 findings

**D1-B01 (blocking) is repaired.** Correct a, b and c earn B1 www each, as bare named values or in the formula (3/3 either way). A value reached by wrong working loses its www mark; swapped fields score 1/3. The official 2023 P2 Q2 row (report PDF 331) was re-rendered. `D1-MOD-OD1-LIST` survives only as a withdrawn register row, and nothing calls the split owner-binding. All seven visual parts carry structured `answer_only_*` conditions that agree with their work orders.

**Of the 31 D1 findings, 28 are repaired and 3 are partly repaired.**

| Partly repaired | Remaining gap | Carried as |
|---|---|---|
| D1-S01 | `exemplars/WB8227-stationary-inflexion.md:111` still proposes Bloom 4 for classification | D2-S07 |
| D1-S06 | The generic S3 contradicts the worked routes on where back-substitution is marked | D2-S08 |
| D1-S23 | The stationary work order copies the implicit recipe's G1–G5 example. Several parts have no allocation. The rule itself is now replaced by OD-6. | OD-6 |

**Agent-level items:**
- **Partly repaired, all later-test:** trig-D1-03 (rounding fixtures; see trig-D2-04) and calc2-D1-10 (unnormalised answer strings).
- **Partly repaired:** calc2-D1-12 (stale `@0.1.1` criterion IDs; D2-S06).
- **Disposition wrong:** calc2-D1-07, whose disposition calls the log domain "owner-fixed" (D2-S04).

## B. Corrections to our own D1 short check

| D1 item | Correction |
|---|---|
| **Trig rounding count (trig-D1-03)** | **Both counts are right, for different rounding paths.** <br>• **14 flips:** c/R at 3 s.f. with exact α (Codex). <br>• **10 flips:** c/R at 3 s.f. with α at its requested 2 d.p. That was our scratch path, but `check-trig.json` never stated the α condition. The gap is ours. <br>• **Agreed:** 33 when α and β both come from R at 3 s.f.; 34 for α only. |
| **REPAIR-D2-PROMPT §2, R1 wording** | We wrote "solve v = 0 (one slip allowed), then compare the roots with the interval or test signs". That makes solving mandatory, so a rigorous no-change argument made without solving scores 1/4 (D2-S02). |
| **REPAIR-D2-PROMPT §2, minority construction** | We asked for a bounded no-change minority and gave "the positive root lies beyond T" as an example. We did not require that the outcome be unpredictable from visible parameters. Codex built the minority from short intervals, and the interval length now separates the outcomes (D2-S01). |
| **Step-3 exam weight** | Our 720.1 rounded the rows with binary-float rounding. Under decimal half-up the rounded rows sum to 720.5. The exact total, 2162/3 ≈ 720.7, is unaffected (coverage-D2-04). |

## C. What passed

**Owner decisions.**
- **OD-4:**
  - Stationary classification is Apply 3 in every canonical record. The single stale exemplar sentence is D2-S07.
  - The motion pool admits 132 = 108 sign-change + 24 no-change instances (2/11). It has 30 normalised shapes and 66/66 directions. No root sits at an endpoint. The no-change positive root lies 1 or 2 beyond T.
  - One 4+2 tariff serves both outcomes, and the marking reproduces: wrong root 3/4, root work plus quadrature 1/4, numeric-only 0/4, never-split 1/4, unchecked no-change 1/4.
  - R4 depends on R2 and R3.
  - Bloom is 13 Apply / 1 Analyse.
- **OD-5:** the wording is faithful in the work order, exemplar, register, checkpoint and subject rules. The 2023 Q6(d) row is kept in full, and only DB1 is extended to the learner's own curve. The chord and multiple-graph cases are defined, and the c → d follow-through edge exists (`visual-design.json:500-508`).

**Exemplars.** All 42 cases recompute, including:
- the new no-change case k = −2, r = 3, c = 2, T = 1: distance = displacement = 37/3, with roots −2 and 3 outside [0, 1];
- the endpoint-triangle value 17 (true distance 44/3);
- the e-index error, which gives the right gradient in 27/27 tuples;
- the divided, log, product and explicit-root proofs, each of which reaches the target in 27/27 tuples;
- all 128 quartics, which pass every factor-theorem step.

**Capacities.** Every claim reproduces:

| Recipe | Capacity |
|---|---|
| Polynomial motion | 137 / 35 |
| Exponential motion | 56 / 14 |
| Mixed motion | 132 / 30 |
| Implicit | 40 raw, 27 tasks, 23 curves, 8 proofs |
| Stationary | 540 / 30 and 256 / 16 |
| Principal | 47 / 12 |
| R-form | 58 (classes 6/42/10) |
| Log | 20 / 4 / 2 |
| Modulus | 108 → 44 |
| Trapezium | 30 / 11 / packing 3; generated-only 22 / packing 2 |
| Vector | 54 → 30 / 17 |

**Originals and coincidences.**
- Every (3,1,2,\*) and (30,½,\*) motion context is excluded, as is (2,8,4,\*) and (4,4,2) in the trapezium.
- The h = 2 sketch subtask is attributed to part (c) only, and the generated-fresh route blocks it.
- No named wrong method hits a canonical trapezium value at 3 s.f. half-up.
- The polynomial motion error sweep matches Codex's disclosures tuple by tuple.

**Marking repairs.** These are confirmed:
- e-index error at 3/5, with the explicit-root route still 5/5;
- alternative proofs capped at 4;
- H1 own derivative and N1 labelled value;
- quartic AS prerequisite routes;
- principal real-route P-B1 at 2/3 for rote interval plus forward work;
- R-form own-root-set F.T. (6 class changes, 8 c = a endpoint cases, the same tuples Codex lists);
- log U-M1 own-line F.T.;
- trapezium own-(a) rule (15.23, 43.4, 46.1, 69.1 all accepted), own-asymptote shape 1/3, and direct 2k ln(x−h);
- vector undistributed B0, with the three 80.0 / 63.0 fixtures.

**OD-1 sweep.** The work order, exemplar and JSON agree on all 27 parts. 24 parts give zero for a bare answer. The three exceptions (modulus a, trapezium c and d) each cite the official award.

**Records.**
- One classification string, `8227-pilot-design-0.1.1`, with every recipe at 0.1.2.
- The register has 20 rows, matching the design-file IDs in both directions, and the Markdown and JSON agree.
- No active file says "owner-binding". D2-S04 covers two misattributions.

**Counts.**
- 9 / 14 / 42 / 27 and 83 marks.
- Decks 19 / 20 / 17. D0 14 → 19 decomposes as principal 2 → 3 plus implicit 5 → 9.
- Facets 38 + 1 conditional; objectives 26 / 60 = 25 + M1:T6:O03; 99 outside.
- 138 / 138 frequency rows match ours, and 2162/3 + 88/3 = 750.
- G09 has 28 exam parts (counted three ways) and zero pilot parts.
- The receipts and the 11 audit hashes match the final bytes.

**R7 close-out.**
- **D1 → D2 changes:** exactly 31 records changed, only in restored text, reason and tag. The 19 positives match HEAD verbatim, and the 12 absolute-exponent sentences are negative. A clause-level polarity scan finds 84 flips at HEAD, 31 at D1 and 0 at D2.
- **Totals:** 209 / 912 / 1777, 2,718 main, 13 parts without a relation and 73 same-type demands.
- **The guard** fails all 7 targeted seeds, including lost negation and over-negation. See closeout-D2-01 for what it misses.
- **The freeze** pins all 7,769 historical paths and 5,417 historical check files, plus the README. The `review` exclusion drops nothing else.

**Rebuild.** I ran this myself in two fresh copies (`rebuild.json`).
- Each copy ran 285 commands, and all 275 outputs are identical across both copies and the author checkout.
- `--negative-only` rejects all 38 established subprocess negatives.
- `freeze_analysis_r7_closeout.py --check` passes on the author checkout and on copy 2 (7,771 / 436 / 37). Copy 1 differs only in the negatives receipt that its own negatives run rewrote.
- `planning/d2/freeze-plan.py --check` passes.

## D. Findings

There is no design-blocking defect.

### Owner decision OD-6 (misread): implement in D3

| ID | Locator | What changes |
|---|---|---|
| **D2-OD6** | `subject-rules.md:57,67,149`; misread lines in all nine work orders (e.g. `WB8227-stationary-inflexion.md:102`, `WB8227-implicit-normal.md:128`, `WB8227-motion-integration.md:37,54`, `WB8227-vector-geometry.md`); `misread_policy` fields in the design JSON (`visual-design.json:651`, `trig-model-design.json:625`; the calculus JSON has none); exemplar samples (motion V = 21 at `exemplars/WB8227-motion-integration.md`, repeated at :81 and :97; vector 3/7); `OWNER-CHECKPOINT.md:42` and `d2/deviation-register.json` | **Replace D2-MISREAD-ALLOCATION with OD-6.** A genuine misread of question data, with object and difficulty unchanged, costs one mark from the A or B marks, and all A and B marks follow through on the misread value. **This absorbs:** <br>• vecrec-D2-01 / calc-D2-03: the stationary work order copies the implicit G1–G5 example; <br>• vecrec-D2-02: the rationale calls the Cambridge convention an "invention"; <br>• vecrec-D2-03: subject-rules heads the whole MR table "binding OD-1"; <br>• vecrec-D2-06: the vector (a) `misread_policy` copies (b)'s; <br>• vecrec-D2-09 and motion-D2-10: missing per-part allocations; <br>• motion-D2-08: V = 18 and V = 30 copy the V = 21 sentence. |

### Should-fix (correct in D3, before approval)

**Motion: OD-4's live decision**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D2-S01 | `work-orders/WB8227-motion-integration.md:27`; `calculus-design.json:4618-4650`, `:4690` | **The printed interval end T separates the outcomes.** No-change instances use only T ∈ {1, 2}, and sign-change instances only T ∈ {3, 4, 5}. In addition, \|k\| ∈ {1, 3} occurs only with a sign change (72 of 108). A learner can learn "short interval means no split" without analysing v. The title "Check direction change and find travelled distance" also cues the check (motion-D2-01, motion-D2-09). | Overlap the outcomes on every visible parameter, for example no-change tuples with T ∈ {3, 4, 5} and \|k\| ∈ {1, 3}, keeping a bounded minority. Re-run the enumeration and the coincidence sweeps at the marked precision. Use a strategy-neutral title, for example "Distance and displacement from a quadratic velocity". |
| D2-S02 | `work-orders/WB8227-motion-integration.md:47,52`; JSON R1 (`calculus-design.json:4681`) | **R1 credits only solving v = 0.** A rigorous no-change argument scores 1/4, for example both endpoint values of the same sign plus concavity, or the vertex value (motion-D2-03; our prompt wording, §B). Also, in a no-change case a one-slip root inside (0, T) gives the canonical total, so it scores 4/4 while claiming a sign change. This is unstated, as are the vertex/zero split coincidences in 14 of 24 cases (motion-D2-04). | Add an R1 alternative: a valid complete argument that v keeps one sign on [0, T], with the same award and nothing extra. State the intended score for the harmless-split case, and disclose those coincidences in the mixed sweep. |
| D2-S03 | `work-orders/WB8227-motion-integration.md:48`; JSON R5 (`calculus-design.json:4685`) | **R5 accepts "the signed sum of evaluated legs from (a)" without requiring a primitive.** A learner using calculator legs gets 2/2 on displacement, while whole-interval quadrature gets 0/2 (motion-D2-02). | "… or the signed sum of the legs from (a), evaluated from an attempted primitive with both bounds." Align the work order, both JSON files and the exemplars. |

**Records that misstate authority**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D2-S04 | `calculus-design.json:4689`; `pilot-design.json:5778`; `checks/plan-repair-d2-trig-dispositions.json:149` | **Two records attribute choices to the owner that the owner did not make.** <br>• "owner OD4 permits … one fixed 4+2 rubric": OD-4 says nothing about a tariff; the one tariff came from our repair prompt. <br>• "Retained the owner-fixed narrow domain" for the log recipe: m ∈ {2, 3} came from our step-3 REPAIR-PROMPT:74, not from any OD (motion-D2-07, vecrec-D2-04, trig-D2-03). | "OD-4 requires mixed outcomes with the check credited. The fixed 4+2 rubric is a proposed design pending approval." Log: "reviewer-prescribed (step-3 calc2-08), disclosed; owner approval pending." |

**Stale counts and IDs**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D2-S05 | `calculus-design.json:5164` | `branch_qualified_capacity` is 387, the D1 value. The current branches sum to 23+8+30+16+137+56+132 = 402 (motion-D2-05). | Set it to 402, or derive it. |
| D2-S06 | `calculus-design.json:2087,2129,3192,3233`; `pilot-design.json:3093,3139,4236,4281`; `part-evidence-register.*` | The Bloom rationales of the four polynomial/exponential motion parts cite `@0.1.1` criterion IDs. Their `bloom_criterion_ids` are `@0.1.2`, and S3 changed meaning in 0.1.2 (motion-D2-06, vecrec-D2-05). | Regenerate the rationales from the `@0.1.2` IDs. |
| D2-S07 | `exemplars/WB8227-stationary-inflexion.md:111`; `exemplars/WB8227-implicit-normal.md:127`; `planning/calculus-source-reads.md:65` | Line 111 still says classification is "proposed … 4", while line 115 says Apply 3. These files cite the D1 receipts as the current checks (calc-D2-01, coverage-D2-01, coverage-D2-02). | Replace the line 111 Bloom sentence with the OD-4 statement, and cite the `planning/d2` receipts. |

**Marking text that contradicts itself**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D2-S08 | `work-orders/WB8227-implicit-normal.md:112` vs `:114`; `calculus-design.json:433` | The generic S3 includes "any justified identity/back-substitution". The worked divided and log routes put back-substitution in S4. A divided-route proof whose back-substitution fails scores 3/4 under :114 but 2/4 under :112 and the JSON (calc-D2-02). | Keep back-substitution in S4. Keep "justified identity" in S3 for the explicit-root route only. |
| D2-S09 | `work-orders/WB8227-principal-inverse.md:50` (no-real P-B1 cell) vs `:54`; `trig-model-design.json:594,625` | The work order cell still gives B1 for "Correct principal range". The JSON requires the bound "used in the actual comparison" and says "a generic range fact alone is not B1". So "range is [−π/2, π/2]; no real solution" scores 1/3 under one and 0/3 under the other (trig-D2-01). | Match the JSON in the work order cell, and add the 0/3 response as a fixture. |
| D2-S10 | `work-orders/WB8227-trig-rform-equation.md:84` | It still says the source DM1 "is replaced by the explicit class table". This contradicts :68, the JSON and the register, which judge the learner's own root set (trig-D2-02). A marker could reapply the canonical classes to an inverted-ratio response, which is the defect D1-S04 removed. | Use the register wording: a complete root search in the learner's own shifted interval, with the class table describing canonical instances only. |
| D2-S11 | `planning/visual-design.json:383` ("freshpacking3"), `:522`; `work-orders/WB8227-trapezium-sketch-estimate.md:52`; exemplar `:71` | Several places still call 3 the strict fresh packing. `strict_all_assessed_parts_unseen_capacity` is 3 and its witness includes an h = 2 card, but the strict generated-fresh bound is 2 (`pilot-design.json:686`) (visual-D2-01). | Name both bounds everywhere ("mathematical packing 3; generated-fresh packing 2"). Set the strict field to 2, or rename it. |
| D2-S12 | `work-orders/WB8227-trapezium-sketch-estimate.md:71` vs `:87`; JSON b:B1 | "(or the correctly derived 2k scale)" lets a bare "J = 6 × 11.5" score 2/2. The official row (report PDF 337) and the JSON give 1/2 (visual-D2-02). | "… or a 2k scale visibly derived from the logarithm law." Add the sample row "J = 2k × T with no logarithm working: 1/2". |

**The approval record**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D2-S13 | `planning/OWNER-CHECKPOINT.md:20-43`; `planning/checkpoint-stage-d.json:24-38` | **The register Vitalis will approve is hard to read.** Many cells have lost their spaces ("Newstemexplicitlydegrees; radianonlyresponsewithholdsfinaldegreeA1"), and the two vector rows have no status class (vecrec-D2-07). Separately, `checkpoint-stage-d.json` is pinned as a current planning file but still states D0 figures: 15 choices and Bloom {2:1, 3:11, 4:3} (calc-D2-09). | Restore normal spacing, and give every row a class. Replace the misread row with OD-6. Mark `checkpoint-stage-d.json` historical, or move it to `planning/history/`. |

### Later-test (carry into stage E/F)

- **coverage-D2-05.** A fixture proving that the `interior-reversal` choice ID and the case tags never reach the learner before submission (`app-change-handoff.md:32,125`).
- **trig-D2-04.** Rounding fixtures for α carried at its 2-d.p. value: R at 4 s.f. (3 flips), the acos route (35), and the (1,3) arcsin route.
- **vecrec-D2-08.** Whether a more precise angle (79.98) earns b:A1. Under OD-6, the outcome when a misread leaves no p.
- **visual-D2-06.** Unlabelled multiple graphs are never resolved by shape, and c:B1 uses the boundary the curve approaches, drawn or implied.
- **motion-D2-12.** Normalise the stored velocity strings, and label the new case D2.

### Notes (apply when touching the text; no approval impact)

**Calculus**
- **calc-D2-04:** state the H1/H2 outcome for e-index working carried into (b).
- **calc-D2-05:** N1 qualifier "equal to −1/(their m)".
- **calc-D2-06:** list the division demand M2:T1:O03:D01 for the factor-theorem route.
- **calc-D2-07:** the path-storage sentence at :46 should cover every alternative route.
- **calc-D2-08:** state the marks for ln y without moduli.

**R7 close-out**
- **closeout-D2-01:** the guard checks `rejection_reason` by containment only. Assert the full template and the R6 anchor; current data satisfy both, 403 of 403.
- **closeout-D2-02:** 19 live D0/D1 `checks/plan-*` files are pinned by neither manifest. Their archived copies are pinned.
- **closeout-D2-03:** the regenerated reading `.md` files dropped the member tables and the motion caveat (the JSON keeps them). `repair-r7-closeout.md:9` overstates this.

**Coverage**
- **coverage-D2-03:** derive the receipt's literals.
- **coverage-D2-04:** the rounding convention (§B).

**Trig and log**
- **trig-D2-05:** the report's "not the review's 10" wording (§B).
- **trig-D2-06:** exemplar :47 should use −3π/4 < −π/2.
- **trig-D2-07:** the principal Bloom rationale names P-M1 for the decision.
- **trig-D2-08:** log U-M1 "their log-equation (from (a), or a correct one written in (b))".

**Trapezium and modulus**
- **visual-D2-03:** (2,8,2,\*) near-copies of the 2023 Q6 integrals on the mixed route; disclose or restrict.
- **visual-D2-04:** k = 2 scale slips coincide; feedback fixture only.
- **visual-D2-05:** the normal modulus asset's leader also crosses the y-axis.
- **visual-D2-07:** state the generated-fresh packing after a worked example is shown.

**Motion**
- **motion-D2-11:** cross-reference the key alias rule in the work order.

## E. Not checked

- **Runtime.** No app, generator, marker, renderer, local website or MCP operation was run.
- **Page reads.** Native pages were read for 3 of the 31 R7 corrected records; the other 28 were checked against HEAD and R6 text.
- **Single read.** Each recipe was re-tested by one agent, so marking judgements at the margin carry that limit. The misread rule is the exception: two agents raised it independently, and I verified it myself.
