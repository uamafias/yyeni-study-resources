# Step 6 review — NSSCAS Chemistry 8224 (work/nam-8224-nsscas-2026)

Reviewer: Claude Code (Opus 5.5), independent cross-vendor reviewer. Authoring tool: Codex. Date: 2026-10-22.
The review ran over two sessions. Session 1 covered topics 1.1–4.2 and stopped at an account quota limit before any edit. Session 2 covered topics 4.3–5.1, validated the operator repairs, applied one further repair and wrote these outputs.

## Verdict

**Publish**, once the operator has validated the final edits.

- The factual review is complete for the scope listed under *Coverage*.
- No critical or high-severity defects were found.
- Four medium findings were found and all four are now repaired:
  - three were applied by Codex and independently validated here;
  - one was applied by Claude in 3.4.
- Twelve low findings remain open. They are tidiness, source gaps and tooling notes; none teaches false chemistry.
- The plan problems below are mapping defects. Each was handled transparently within the frozen slots, and none prevents a learner from reaching the objectives. They do not justify "fix the plan first".

### Factual readiness vs outstanding approvals

| Item | State |
|---|---|
| Independent semantic review (this report) | Complete for the stated coverage |
| Operator: restamp, render and check 1.3 and 3.4 after Claude's edits; check all 21; copied-wording recheck; republish | **Pending**. Claude has no shell and ran none of these. |
| Human diagram approval (30 PNGs) | **Outstanding**. Inspection here is model review, not human approval. |
| RS-13 human approval of 625 `generated_gap` claims (C-24 gate holds: 0 verified/publishable) | **Outstanding**. No claim was marked verified or publishable. |
| Commit/push, YYeni import | Not done (out of scope) |

**Baseline limitation.** The build is uncommitted. I reviewed the filesystem snapshot (`before-repair.tar.gz`, `before-sha256.json`), not git HEAD. Topics 1.1–4.2 were read before the Codex repairs. Repaired regions were re-read from the current original JSON.

## Deterministic checks (raw results inspected)

- 21/21 topics read PUBLISH, with 0 failures, both pre-repair and post-repair (operator checkpoint for 1.3, 2.3 and 3.4).
- **Warnings:** 21 × C-18 (AO mix against 40/40/20 applied per topic). Theory topics carry 0% AO C and 5.1 carries 100% AO C. This is expected from the subject design and is not a defect.
- **not_run:** 63, which is C-35, C-41 and C-43 in every topic.
  - C-41 says no item shows a generated depiction, and C-35 says there is no graphical task. In fact 30 generated figures exist, including the 5.1 graphs and tangent.
  - C-32 parses limited arithmetic; for example, 4.2 reports 0 calculations.
  - PUBLISH is therefore a structural gate only. All figures were inspected by eye and all worked numbers were recomputed by hand (see coverage.json).
- **Completeness (metadata-completeness.json):**
  - 631 items, one per frozen slot, with no unplanned additions.
  - 0 mismatches in objective, AO, Bloom level, command word or tariff.
  - 51 subtype changes, all MECH→WHY, each recorded in the topic's authoring_notes.

## Findings

| ID | Sev / category | Where (exact IDs) | Evidence | Learner consequence | Repair | Conf. | Status |
|---|---|---|---|---|---|---|---|
| R1-001 | medium / curriculum | 1.3-6-01-b1, CLM-8224-1.3-053, ITEM-1.3-043/044 | Syllabus l.458-461 lists "fullerene allotropes (C60 and nanotubes only)" as simple molecular. Notes set nanotubes against molecular structures. | Could contradict the syllabus classification | Codex stated the grouping and the intra- vs inter-tube distinction; Claude validated it and fixed the spacing in "of60" | 0.85 | **Fixed** |
| R1-002 | medium / curriculum | 2.3-1-07-b1, CLM-8224-2.3-016, ITEM-2.3-015/016/026 | 0 occurrences of V2O5 in any topic. Syllabus l.576-578 asks for the choice of catalyst; the 2023 P12 V2O5 item is in the corpus. | Cannot name the Contact catalyst | Codex named V2O5 (OpenStax l.47400); Claude validated it | 0.9 | **Fixed** |
| R1-003 | medium / quantitative | 3.4-2-04-b1, ITEM-3.4-015-INTERP, CLM-3.4-017/018 | Notes used OpenStax 432/370/295. The Data Booklet (l.2207-2209, p59) gives 431/366/299. | Numbers disagree with exam data | Codex changed to 431/366/299, 132 kJ mol⁻¹ and 2.99 kJ; Claude recomputed and fixed the spacing | 0.95 | **Fixed** |
| R1-004 | medium / curriculum | 3.4-3-01-b1, CLM-8224-3.4-019 (rev 1→2), ITEM-3.4-016/017/018/019 | Annexe D (l.2013-2018, p52): AgBr "partially soluble in dilute ammonia", AgI "insoluble in dilute ammonia". Notes said "AgBr dissolves appreciably in concentrated ammonia". | Conflicts with the Paper 3 reference notes | Claude aligned the wording in the claim, block and item, and updated dependants | 0.85 | **Fixed** (restamp pending) |
| R1-005 | low / quantitative | 2.1 bond-count block, ITEM-2.1-011-CALC, 2.1-P02 | Supplied Cl–Cl 243 and H–Cl 432 vs Data Booklet 242 and 431 (−185 vs −184) | Small mismatch if cross-checked | Align to the Data Booklet | 0.9 | Open |
| R1-006 | low / accuracy | 2.1 standard-state block, ITEM-2.1-003 | "standard pressure, 100 kPa"; the syllabus uses 101 kPa elsewhere | Minor | Mention 101 kPa (1 atm) | 0.6 | Open |
| R1-007 | low / coherence | 2.2–3.5 notes | 39 × "sulph-" vs the syllabus "sulfur" | Cosmetic | Normalise the spelling | 0.95 | Open |
| R1-008 | low / coherence | 5.1 items (36), 4.x P-tasks, some claims/blocks | ~80 joins such as "Total20 marks" and "to3 significant figures" | Readability | Scripted fix + restamp | 0.9 | Open |
| R1-009 | low / coherence | ITEM-4.2…4.7-P01 | Filler sentence "Each distractor identifies the stated error." | Cosmetic | Remove the sentence | 0.95 | Open |
| R1-010 | low / figures | tetrahedral-carbon (unused duplicate), calibration (no vertical construction), molecular-separation, label overlaps, caret units, touching p lobes | Visual inspection | Readability | Regenerate before human approval | 0.9 | Open |
| R1-011 | low / curriculum | 4.2 "Electrophilic addition" block | Bromonium taught; open carbocation called "unsupported"; no mark schemes held | Possible confusion with class teaching | Teacher check | 0.5 | Open |
| R1-012 | low / quantitative | 1.1.5-b5, 1.1.2-b5, ITEM-1.1-004-APP | 15.68 dm³ and 1.204 × 10²³ from 3 s.f. data | Mixed messages on significant figures | 15.7 dm³; 1.20 × 10²³ | 0.8 | Open |
| R1-013 | low / curriculum | 2.3 industrial block | No typical operating values. The ER 2025 item supplies 450 °C, and the reasoning is present. | Cannot recall values if asked | Optional, sourced | 0.5 | Open |
| R1-014 | low / audit | ITEM-1.3-043/044, 2.3-015…, 3.4-014 | Operator reviewed_unchanged reasons are a generic boilerplate sentence | Audit trail only | Make each reason specific | 0.9 | Open |
| R1-015 | low / coherence | 3.5 WHO block | Live external URL in learner notes | Unusable offline | Confirm the link policy | 0.6 | Open |
| R1-016 | low / tooling | C-35, C-41, C-32 | Not run / limited despite figures and arithmetic | PUBLISH is structural only | Report to standard owners (outside my lane) | 0.95 | Open |

The full YAML-style fields are in findings.json.

## Repair validation (operator-applied)

All three Codex repairs were checked against the current original JSON:

- the claim revision is incremented;
- every dependent block and item cites the new revision;
- unchanged dependants carry `reviewed_unchanged`;
- the new values were recomputed against the Data Booklet;
- no claim was marked verified.

Details are in repairs.json. Claude's own edits (R1-004 and two spacing fixes) need operator restamp, render and check of **1.3 and 3.4**, then a whole-subject copied-wording recheck and republish.

## Plan problems (for the record, not blocking)

1. **MECH assigned to non-mechanism objectives.** 51 slots in 17 topics were planned as MECH (electron movement, intermediate, product) for property, energetics, equilibrium, kinetics, periodicity and application objectives. Codex changed each to WHY while keeping the objective, AO, Bloom level, command word and tariff. I agree with every change. The planner's subtype-to-objective mapping is defective and should be fixed for future NSSCAS science plans.
2. **A CALC task assigned to isomerism (4.5)**, where no measured quantity exists. It was handled with exact counts; this is acceptable.
3. **Seven CALC slots on Paper 3 recording objectives (5.1).** They were handled as completed table entries; this is acceptable.
4. **Per-topic AO targets (C-18)** cannot be met by a design that separates theory (A/B) from practical (C). The warning is structural, and the subject-level mix was approved at 44/39/18.
5. **The authoring clarification on the C60/nanotube grouping** departed from correct registry wording. It is superseded by R1-001.

Other recorded deviations and clarifications were read in every topic's authoring_notes (81 = 51 MECH→WHY + 30 scope, source-focus or clarification records). Examples:

- the resolved EQUATION schema exception (1.1);
- checker variant/abbreviation limitations (1.4, 2.1, 2.3);
- construction practice added inside existing slots (2.1, 3.3);
- enzyme ranges (2.4);
- the selective-discharge approximation (2.2);
- Al2Cl6 and chloride state qualifications (3.1);
- the WHO and N2O-average clarifications (3.5);
- the IR-table correction (4.1);
- the bromonium and cold dilute acidified MnO4⁻ settings (4.2);
- one-step SN at primary carbon (4.3);
- practical AO C and simulated-data framing (5.1).

None of the others is an actual plan defect beyond items 1–4 above.

## Source gaps (no error found, verification still outstanding)

- Al2Cl6 bridge connectivity (1.3): no exact local locator.
- Group 2 specifics: nitrate decomposition pattern, solubility directions, Mg/Ca melting points, cement stages (3.2).
- Mn electrowinning and uranium Mg-reduction precursor (2.2, 3.3).
- Cold dilute acidified manganate diol endpoint and the board's expected bromonium depth (4.2).
- AgBr in concentrated ammonia (3.4, retained clause).
- Ethanol dehydration at 170 °C; alcohol solvent for coal sulfur (4.4).
- Soil and eutrophication detail (3.5).
- Standard pressure convention (2.1).
- No mark schemes are held. All 19 misconceptions come from a single examiner report.

## Copied wording (13 sources: 12 papers and the 2025 examiner report; syllabus excluded)

There are no runs of 12 or more words. All ten runs of 8–10 words are **allowed**:

| Run | Location | Reason allowed |
|---|---|---|
| `cl2 aq 2oh aq cl aq clo aq h2o l` (10) | CU-8224-3.4.4 / 3.4-4-01-b1 | Standard balanced equation (cold-alkali disproportionation) |
| `the contact process 2so2 g o2 g 2so3 g` (9) | CU-8224-2.3.1 / 2.3-1-07-b1 | Process name plus standard equation |
| `cao s 2hcl aq cacl2 aq h2o l` (8) | ITEM-8224-3.2-P02 | Standard balanced equation |
| `a 1 b 2 c 3 d 4` / `a 2 b 3 c 4 d 5` (8 each) | ITEM-1.2-P01, 2.1-P01, 3.1-P01, 3.3-P01, 3.4-P01, 3.5-P01, 4.1-P01 | Option letters with small integers (counts, oxidation states); no question phrasing copied |

The post-repair rerun (operator checkpoint) returned the same 10 runs. A further rerun is needed after Claude's 3.4 edit, whose new wording paraphrases syllabus Annexe D (the syllabus is excluded from the tool).

## Misconceptions (all 19 planned slots sampled)

Each card names its misconception entry and discriminates the wrong idea with a test that can be answered from the notes:

- 1.1-025/026/027 (s.t.p. vs r.t.p.; molecular peaks ≠ isotopes; heights ≠ percentages)
- 1.2-029/030/031/032 (zero masses; equal deflection; Cr exception; orbitals ≠ electrons)
- 1.3-051/052 (HCl gas is not ionic; I–I bond vs van der Waals)
- 2.2-022 (nitrate(III) charge test)
- 2.3-026 (yield-only temperature)
- 2.4-020/021/022 (wrong axes; area ≠ Ea; collisions only)
- 3.1-037 (maximum oxidation state rising to S)
- 4.2-057 (pentavalent carbon in the repeat unit)
- 4.4-019/020/021 (dilute acid; solution colour vs precipitate; CHI3 ≠ iodobutane)

The weakest is 1.2-031, whose test is "check the known exception". It is still answerable from the notes.

## Learner tests (top-tariff objectives; answers built from the notes alone)

**Test 1 — 5.1 acid–base titration practical (ITEM-8224-5.1-P01, 20 marks).**

1. Rinse the burette with NaOH, fill it, clear the tip of bubbles and remove the funnel.
2. Pipette 25.00 cm³ of HCl with a filler into a flask on a white tile and add the supplied indicator.
3. Do a rough titration, then careful titrations, adding dropwise and swirling near the endpoint until a persistent change.
4. Record a table with Initial / Final / Titre (cm³) to the nearest 0.05 cm³, keeping the rough row.
5. Titres 24.65 and 24.70 cm³ are concordant (within 0.10 cm³); mean 24.675 cm³.
6. HCl + NaOH → NaCl + H2O; n = 0.100 × 0.024675 = 2.4675 × 10⁻³ mol; c = 2.4675 × 10⁻³ / 0.02500 = 0.0987 mol dm⁻³ (3 s.f.).
7. Overshooting inflates the titre and so the concentration. Remedy: dropwise delivery near the endpoint. Repeats reveal scatter but not bias.

Every element is taught in 5.1.1–5.1.4 (setup, tables, concordance, n = cV, rounding, error and improvement). **Sufficient for full marks.** The only item not taught is the choice of indicator, which the task supplies.

**Test 2 — 2.3.1-07/08 Contact-process conditions (P2-style explanation; ER 2025 item asks to justify 450 °C).**

- The forward reaction is exothermic, so lower temperature favours SO3 at equilibrium but slows the rate. About 450 °C is a compromise between an acceptable rate and an acceptable yield.
- V2O5 provides a lower-activation-energy pathway, which speeds the approach to equilibrium without changing the yield at that temperature.
- Three gas moles become two, so higher pressure favours SO3. Because conversion is already high, the extra cost of compression is hard to justify.

All points appear in block 2.3-1-07-b1. **Sufficient after repair R1-002.** Before the repair, the catalyst point was missing. The notes give no typical numerical conditions (R1-013, open).

## Coverage

All 21 topics were covered:

- all teaching text in all 56 content units;
- all 390 sampled items (plus 5 repair-dependent items);
- authoring_notes for every topic;
- all 30 figures;
- every worked number in the notes and sampled items, recomputed;
- syllabus scope, the Data Booklet (constants, bond energies, IR) and Annexe D cross-checked.

Per-topic evidence is in coverage.json.

**Limitations:**

- Topics 1.2–5.1 were read via the rendered notes, which are generated from the same blocks.
- The 241 unsampled items were not read, except for repair dependants.
- Claim evidence locators were spot-checked, not exhaustively verified.
- SVG/geometry files and the publish package were not inspected.
- Rendered notes for 1.3, 2.3 and 3.4 are stale until the operator re-renders them.
- No shell validation was run by Claude.
