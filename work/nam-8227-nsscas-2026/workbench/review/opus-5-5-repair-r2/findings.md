# Findings: re-review of 8227 analysis repair round 2

Reviewer: Claude Opus 5.5. Date: 2026-11-17. Inputs are frozen in `inputs.json` (snapshot `85b782f9…74ee`).

The IDs continue from round 1. **R2-** findings are new; the round-1 **R13-** findings are dispositioned in section C. The severity levels are:

- **high:** blocks planning;
- **medium:** blocks the named branches, or must be decided in the recipe contract;
- **low:** fix in the next author pass.

## A. Confirmed defects

### R2-01: Two given-diagram crops cut off essential labels · medium · blocks the affected diagram branches

- **Where:** `analysis/assets/2024-1-q9-given.png` (crop box `60,55,510,245` on PDF p11) and `analysis/assets/2025-1-q12-given.png` (box `115,50,460,255` on PDF p18).
- **Expected:** Each crop contains every given the part needs (README §E, R13-18).
- **What I found:** I rendered both source pages with PDFKit and overlaid the author's crop boxes (`inputs.json`, scratchpad `r2assets/src/box-*.png`).
  - **2024 P1 Q9:** The box ends above the labels "B (90, −3)" and "f(x) = a sin x". The y-axis has no numeric scale, so B is the only given that fixes a, which is −3 (f(90°) = −3). The crop therefore cannot be used to answer part (a).
  - **2025 P1 Q12:** The box cuts off vertex D and its label (below the x-axis), and the x-axis label.
- **Text bleeding into crops (cosmetic):**
  - 2024-1-q11: two lines of question text at the bottom.
  - 9709_w16_qp_12-q6: "…etal plate ABCD made from two parts. The part BCD".
  - 2022-2-q3, 2021-1-q9 and the 2021-1-q12-c response frame: glyph fragments at the edges.
- **Educational consequence:** The image-generation loop and learners would work from diagrams missing their givens. For Q9 the variant would have no unique answer.
- **Correction:**
  1. Re-crop both diagrams to include all labels.
  2. Trim the bleed.
  3. Add a build check: every PDF text span or drawing that intersects a crop box must lie wholly inside it, or be explicitly excluded.
- **Verify:** Re-render both crops, then confirm by eye and with the new check.

### R2-02: Learner-visible "Same type as …" references exist for only 12 of 67 groups · medium · must be decided in the recipe contract

- **Where:** `analysis/problem-patterns.json`, `examination_references`. There are 354 group-level references: 334 are `related` (no learner label) and 20 are `same-type`, spread over 12 groups. 55 groups have no learner-visible reference at all, including large observed groups such as `function-analysis`, `bounded-trig`, `numerical-method-chain` and `quadratic-substitution`.
- **Cause:** `same-type` requires a part's demand set and response format to equal the whole group's union. Multi-branch groups therefore almost never match.
- **Expected (owner request N1):** Every generated problem shows "Same type as …" for the exam parts it is genuinely modelled on.
- **Assessment:** Codex's rule is honest at group level; I am not asking for looser claims. The part-level data needed to do this properly already exists: 250/250 parts carry an `original` reference with a correct label, plus their own demand sets and response formats.
- **Correction (PLAN or recipe contract):** Compute `same-type` per recipe **branch**, not per group. A member part is same-type to a branch when it exercises that branch's discriminating decision and response format. Group-level `related` references stay internal.
- **Verify:** Every included branch backed by NSSCAS or Cambridge evidence has at least one learner-visible reference. Branches without one are labelled syllabus-derived.

### R2-03: Small omissions and one mis-tag in part→demand links · low · no demand status changes

None of these changes any demand's observed/comparable/syllabus status, because every demand below is observed elsewhere. They do affect thin-demand counts and branch evidence.

- **1.6.3.1 (exact special-angle values) is linked only where a question says "exact value".** It is also needed in these parts:
  - 2021 P2 Q6(b): tan x = 1/√3.
  - 2022 P1 Q9(b): sin x = −½, in radians.
  - 2022 P2 Q3(a) and (b): exact x = 7π/6 and the exact gradient there.
  - 2023 P2 Q3(a): expanding cos(θ + 30°).
  - 2024 P1 Q12(b): cos x = ½.
  - 2024 P2 Q2: sin 60° and cos 60°.
  - 2024 P2 Q9(b): tan 3π/4.

  The registry therefore counts this demand as thin (2 parts) when it is used routinely. That matters for the Cambridge "thin demand" priority list.
- **2023 P2 Q7(a): mis-tag.** It links 2.5.1.1 (exponential or reciprocal-linear), but the integrand 3x² − 4 sin 2x + cos x has no such term. Replace it with 1.9.1.2 (powers).
- **Missing secondary links:**
  - 2025 P2 Q8: 1.8.2.2, the chain rule on 6/(t + 1).
  - 2022 P2 Q10(b): 2.3.2.3, because dx/dθ = 0 needs sin 2θ = 2 sin θ cos θ.
  - 2025 P2 Q7(a): 2.3.2.1, because 1 + tan²x = sec²x.
  - 2021 P1 Q4(b): 1.9.3.1 or 1.9.2.1, because the distance needs a definite integral or s(0) = 0.
- **Verify:** Rebuild, then re-run the coverage and thin-demand counts.

### R2-04: Three dependency edges still missing · low

The 18 required questions from R13-03 are all present. Three multi-source cues were resolved to only one earlier part:

- **2023 P2 Q6(d):** "Use your sketch … whether your answer to part (a) is an over-estimate". The edge c→d exists; **a→d** is missing. My scan for explicit "part (x)" wording found only this one omission.
- **2025 P1 Q4(c):** "Use your graphs" is plural and refers to the sketches from parts (a) and (b). The edge b→c exists; **a→c** is missing.
- **2024 P2 Q11(c):** "Deduce the solution of the inequality" uses the sketches from (a) and the intersection from (b). The edge b→c (F.T.) exists; **a→c** is missing.

**Verify:** Each of these edges appears in `dependency_edges`. The cue scan should treat plural "graphs" and an explicit "part (x)" as additional sources.

### R2-05: Diagram parameters do not separate fixed elements from constraints · low

- **Where:** All 55 parts with `diagram_parameters`. In every one, `fixed` is identical to `constraints`, and the list items are untrimmed comma fragments (each starts with a space).
- **Cause:** `tools/visual_inputs.py` holds a single "fixed relations/constraints" column, which the builder copies into both fields.
- **Educational consequence:** The source annotation itself is good. But a generator spec needs three separate things:
  - what stays the same (e.g. degrees, concentric circles);
  - what varies;
  - which relations must hold between them (e.g. r = R cos(θ/2)).
- **Correction:** Split the column into `fixed` and `relations`, trim the fragments, and keep `variable` as it is.

### R2-06: One Cambridge item is labelled `gap-fill` without a gap demand · low

- **Item:** `8227:CAMBRIDGE:s15:11:8-iii` ("Explain why f has an inverse").
- **Problem:** It links 1.3.1.3 and 1.3.3.1. Both are observed in NSSCAS (e.g. 2025 P1 Q7(b)), so neither is a gap demand.
- **Correction:** Relabel it `variety`. It also helps a thin demand.

### R2-07: Held defective parts still carry learner labels · low

- **Parts:** 2022 P1 Q13, 2023 P1 Q1(b) and 2023 P1 Q9 each keep an `original` reference with a learner label.
- **Current protection:** Group references already exclude held exemplars.
- **Correction:** Add an explicit `learner_display: false` (or equivalent) to held parts' references, so that no later consumer shows a defective original to learners.

## B. Evidence gaps and observations

### R2-08: Some NSSCAS questions are adapted directly from specific Cambridge 9709 questions · observation and opportunity

I searched the indexed 9709 text and checked the rendered pages. Three NSSCAS questions are adapted from Cambridge questions:

| NSSCAS question | Cambridge source | How it was adapted |
|---|---|---|
| 2023 P1 Q6 | 9709/13 Oct/Nov 2016 Q5 (PDF p2) | Same figure, same 6 cm, 1.8 rad and "show radius 3.73 cm", and the same part structure. |
| 2024 P2 Q5 | 9709/22 Feb/March 2022 Q6 | Same polynomial 4x³ + 16x² + 9x − 15 and the same remainder −6. The divisor changed from (2x + 3) to (2x − 1). Cambridge names the polynomial p(x), which explains the "p(x)" left in NSSCAS (R13-14 / `SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5`). |
| 2022 P2 Q5 | 9709/22 and 9709/23 May/June 2016 Q5 | Same y = 6xe^(x/3) and the same "show that p = 3 ln(…/(p + 3))". The gradient changed from 40 to 20. |

- **Other likely sources:** Structurally similar items appear for 2023 P1 Q7 and 2024 P1 Q6 (9709 2015 P1). I have not established these.
- **Opportunity 1:** Add a `derived-from` relation to `examination_references` for adapted NSSCAS questions. This strengthens the learner-facing "same type" link to Cambridge material.
- **Opportunity 2:** Use the Cambridge original when diagnosing an NSSCAS source defect.
- **Not blocking.** Run a systematic NSSCAS→Cambridge provenance pass with the next source-analysis step.

### Reviewer corrections to my own round-1 material

- Codex is right that my candidate "9709_w21_qp_22 PDF p9 Q9(c)" is **Q6(c)**. It concerns conditional convergence, not failure to converge.
- Codex is also right to keep principal values as a single `comparable` status with the held NSSCAS part attached. This is consistent with owner decision 1 and with the three-status rule.

## C. Disposition of round-1 findings R13-01 to R13-29

**Key:**

- **Closed:** verified in this re-review.
- **Closed (spot):** structure verified, contents sampled.
- **Superseded:** replaced by an owner decision.
- **Deferred:** still open by agreement.

| Finding | Status | Evidence / residue |
|---|---|---|
| R13-01 | Closed | `demand_coverage.compute` has no family input. All round-1 examples now link: 2024 P1 Q10 → 1.7.1.1; T7 O03 parts → 1.7.3.2 and 1.7.3.3; 2024 P1 Q8 and 2025 P1 Q12 → 1.4.1.1; 2023 P1 Q11 → 1.8.1.2; 2025 P1 Q8(a) → 1.8.1.1; 2023 P1 Q12 and 2021 P1 Q4(a) → 1.9.1.2. |
| R13-02 | Closed | All 250 parts are linked and the statuses are 126/8/4. I checked the 12-gap list and the inflexion facet against every part and found no NSSCAS part that should close a gap. Residue: R2-03. |
| R13-03 | Closed | 76 typed edges, covering all 18 required questions. Residue: R2-04. |
| R13-04, 05, 06 | Closed | Applied per owner decisions 1–3 in `source-defects.json`. |
| R13-07 | Closed | 24 award questions (2021 P2 Q1–4, 2023 P2 Q1–9, 2024 P2 Q1–11), matching my round-1 census. |
| R13-08 | Closed | Every listed mis-tag is corrected. Model-only parts carry MODEL and prior knowledge only. The T1 O06 secondary links are added to all five parts. |
| R13-09 | Closed as analysis groups | The 67 groups follow report §4. The splits, merges and the `identity-extrema` departure are accepted. `bounded-trig` (16 parts) and other shared modules overlap other groups (42 parts sit in 2–3 groups). Recipe economy is for the PLAN. |
| R13-10 | Superseded (owner decision 6) | All 13 sketch and sketch-dependent parts are `include`, and credited sketch features are recorded. |
| R13-11 | Closed | All grade-description content on pp19–24 is present in 46 descriptors. Both grade-floor exceptions (division, linearisation) are accepted as labelled judgements. |
| R13-12 | Closed (spot) | LIMIT01–08 plus 11 QUALs carry page locators; QUAL01, 03 and 05 and LIMIT05 were read. |
| R13-13 | Closed (spot) | Four normalised objectives are correct, including the documented modulus typo fix. |
| R13-14, 15, 16 | Closed | Register entries are present. R2-08 explains R13-14. |
| R13-17 | Closed | Both negative fixtures fail, and I reproduced this in a disposable copy. |
| R13-18 | Partly closed | Representation fields exist on all 250 parts. 37 of 39 crops are complete. Residue: R2-01 and R2-05. |
| R13-19, 20 | Closed (spot) | Structure verified, and the 2025 P1 cover record was read. |
| R13-21 | Closed | Prerequisite roles are recorded per part. Prior and MODEL links never create coverage. |
| R13-22 | **Deferred, and needed before the marking/feedback contract** | 12 bounded excerpts only. There is no convention register yet. |
| R13-23 | **Deferred, and needed before the bank structure is settled** | 19 samples and a completion method; no inventory has been made yet. |
| R13-24 | Partly closed | Derivatives are reproducible. The historical OCR environment remains unrecorded, which is acceptable. |
| R13-25 | Closed (not re-verified) | Mirror provenance is recorded. |
| R13-26 | Owner-settled | Refiling the root PDF is deferred (cosmetic). |
| R13-27 | Closed | Capability records are dated, and announcement is kept separate from runtime evidence. |
| R13-28 | Deferred | Adoption into the shared schema is Vitalis's call. |
| R13-29 | Closed | Hardening and environment evidence are present. |
