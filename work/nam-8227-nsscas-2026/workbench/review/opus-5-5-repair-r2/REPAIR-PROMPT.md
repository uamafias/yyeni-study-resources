# Repair round 3 and source-analysis completion: NSSCAS Mathematics 8227

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this work, and his decisions are final.

The cross-vendor re-review of repair round 2 (Claude Opus 5.5, 2026-11-17) returned **accept named analysis scope**. This round has two jobs:

- fix the remaining review findings (R2-01 to R2-07);
- complete the outstanding source analysis (step 2 of Vitalis's agreed sequence: R13-22, R13-23 and R2-08).

It does **not** create the PLAN, recipe contract, recipes, generators or work orders; those are step 3.

## Read first

1. `AGENTS.md`, `TEAM-PLAYBOOK.md` and `standard/v0.2.0-draft/roles/AUTHOR.md`. Then `workbench/playbook/README.md`, `quality.md`, `templates.md` and `textbook-analysis.md`.
2. The re-review folder `work/nam-8227-nsscas-2026/workbench/review/opus-5-5-repair-r2/`, in this order:
   - `report.md` §1 and §3;
   - `findings.md`, sections A and B (each finding gives the locator, the correction and the check);
   - `inputs.json`.
3. Binding owner decisions: `review/opus-5-5-step-1-3/owner-decisions-2026-11-16.md`.

Before changing anything, copy the current `analysis/analysis-snapshot.json` (sha256 `85b782f9dc620f0b1697c29cb4a4bdf942f345a66abace60fd7c61b6b6f174ee`) to `analysis/history/analysis-snapshot-r2.json`.

## A. Fix the re-review findings

### R2-01: Diagram crops (do this first)

- **2024 P1 Q9 (PDF p11).** Re-crop `assets/2024-1-q9-given.png`. The current box `60,55,510,245` cuts off "B (90, −3)" and "f(x) = a sin x". B is the only given that fixes a = −3.
- **2025 P1 Q12 (PDF p18).** Re-crop `assets/2025-1-q12-given.png`. The current box `115,50,460,255` cuts off vertex D, its label, and the x-axis label.
- **Trim text bleed** from:
  - `2024-1-q11-given` (two lines of question text);
  - `9709_w16_qp_12-q6-given` ("…etal plate ABCD…");
  - `2022-2-q3-given`, `2021-1-q9-given` and `2021-1-q12-c-response-frame` (edge glyph fragments).
- **Add a build check.** Every PDF text span or vector drawing that intersects a crop box must lie wholly inside it, or be listed as an intentional exclusion with a reason. Run it on all 39 crops, and regenerate `asset-index.json` hashes.

### R2-03: Part→demand corrections

Edit `tools/repair_inputs.py` as follows.

- **Add 1.6.3.1 (exact special-angle values)** to these parts:
  - 2021 P2 Q6(b);
  - 2022 P1 Q9(b);
  - 2022 P2 Q3(a) and Q3(b);
  - 2023 P2 Q3(a);
  - 2024 P1 Q12(b);
  - 2024 P2 Q2;
  - 2024 P2 Q9(b).
- **2023 P2 Q7(a):** replace 2.5.1.1 with 1.9.1.2. The integrand 3x² − 4 sin 2x + cos x has no exponential or reciprocal-linear term.
- **Add these secondary links:**
  - 1.8.2.2 to 2025 P2 Q8 (chain rule on 6/(t + 1));
  - 2.3.2.3 to 2022 P2 Q10(b) (dx/dθ = 0 needs sin 2θ = 2 sin θ cos θ);
  - 2.3.2.1 to 2025 P2 Q7(a) (1 + tan²x = sec²x);
  - 1.9.3.1 or 1.9.2.1 to 2021 P1 Q4(b), whichever matches the award or method.
- **Re-run** the coverage and thin-demand counts, and report what changed (1.6.3.1 should no longer appear thin).

### R2-04: Dependency edges

- **Add these edges:**
  - 2023 P2 Q6 **a→d** ("whether your answer to part (a) is an over-estimate");
  - 2025 P1 Q4 **a→c** ("Use your graphs", plural);
  - 2024 P2 Q11 **a→c** ("Deduce" uses the sketches from (a)).
- **Extend the cue scan** so that plural "graphs" and an explicit "part (x)" each add every referenced source part.

### R2-05: Diagram parameters

`tools/visual_inputs.py` currently copies one column into both `fixed` and `constraints`, as untrimmed fragments, in all 55 parts.

- Split that column into three fields:
  - `fixed`: what stays the same (e.g. degrees, concentric circles);
  - `variable`: what changes per instance;
  - `relations`: equations or conditions that must hold (e.g. r = R cos(θ/2)).
- Trim the fragments.
- Apply the same three fields to the 7 Cambridge diagram items.

### R2-06: Cambridge purpose label

Relabel `8227:CAMBRIDGE:s15:11:8-iii` as `variety`. Its demands are observed in NSSCAS, so it does not fill a gap.

### R2-07: Held parts

Add `learner_display: false` (with a reason) to the references of the three held parts: 2022 P1 Q13, 2023 P1 Q1(b) and 2023 P1 Q9. Make the builder fail if any held part's reference is learner-displayable.

## B. R13-22: Examiner marking-convention register

Create `analysis/marking-conventions.json` and `.md` from all 2021–2025 NSSCAS examiner reports.

**1. Convention register.** Each rule records:

- `rule_id`;
- its type: answer format, exact form, precision and rounding, angle units, method required ("hence", "show all working", "using logarithms"), follow-through behaviour, accepted alternative method, or recurring error that loses marks;
- a short verbatim excerpt;
- its source locator (report year, PDF page, question and part);
- the demand IDs and groups it applies to;
- its strength: an explicit general rule, or a single-question remark;
- any conflict with other sources (keep the R13-06 degree-mode anomaly as a rejected alternative).

**2. Award tables.** Transcribe the 24 award tables (2021 P2 Q1–4, 2023 P2 Q1–9, 2024 P2 Q1–11) into criterion-level rows:

- part;
- mark type (M, A or B) and value;
- what earns it;
- dependencies and F.T.;
- accepted alternatives;
- the exact source page.

Check each question's total against the paper tariff.

**3. Coverage statement.** State which questions and years have no award table, so that later marking work labels those criteria as derived rather than official.

## C. R13-23: Textbook inventory

Follow `analysis/textbook-completion-method.md`. Create `analysis/textbook-inventory.json` and `.md` covering the in-scope chapters of both textbooks. Each item records:

- book and chapter;
- exercise and item number;
- printed and PDF page;
- the 8227 demand IDs;
- representation (text, diagram, graph or table) and whether a sketch response is required;
- exam-style flag;
- answer-key availability and its locator;
- scope check against 8227 limits;
- notes on defects.

Rules:

- Use OCR for discovery only. Check diagram items and mathematics on the rendered page.
- Report coverage honestly: chapters completed, items counted, and any stop rule applied. Do not claim it is exhaustive unless it is.
- Summarise per demand: textbook item count, diagram item count, and demands with no textbook support.
- **Rights.** Vitalis authorised exact *exam* questions (NSSCAS and Cambridge) for learner use. Textbook items stay internal evidence for breadth and variation. Do not mark them learner-displayable.

## D. R2-08: NSSCAS→Cambridge provenance pass

For each of the 119 NSSCAS questions, search the local 9709 corpus (2015–2025 index in `analysis/cambridge-discovery/`) for a question it was adapted from.

- Use distinctive values, expressions, figures and wording. Confirm every match on the rendered pages of both papers.
- Record matches in `analysis/nsscas-cambridge-provenance.json` and `.md`. Each match records:
  - both locators;
  - what is shared and what changed;
  - a confidence level (identical, adapted, or structurally similar);
  - whether the match explains a recorded source defect.
- **Three matches are already confirmed by the reviewer:**

  | NSSCAS question | Cambridge source |
  |---|---|
  | 2023 P1 Q6 | 9709/13 Oct/Nov 2016 Q5 |
  | 2024 P2 Q5 | 9709/22 Feb/March 2022 Q6 (the source of the "p(x)" typo) |
  | 2022 P2 Q5 | 9709/22 and 9709/23 May/June 2016 Q5 |

- **References.** Add a `derived-from` relation to the NSSCAS part's `examination_references`. Generate a draft learner label of the form "Adapted from Cambridge International AS Level Mathematics 9709, Paper 13, Oct/Nov 2016, Question 5". Display rules are decided in the PLAN.
- **No match is not evidence.** Never treat a missing match as proof that a question is original.

## Deliverables

- The updated tools, records, assets and `asset-index.json`.
- The new files:
  - `marking-conventions.json/.md`;
  - `textbook-inventory.json/.md`;
  - `nsscas-cambridge-provenance.json/.md`.
- A regenerated `analysis-snapshot.json`.
- `workbench/checks/repair-r3-report.md`, containing:
  - a table mapping R2-01 to R2-08, R13-22 and R13-23 to what changed, the file and the check that proves it, or to "deferred" with a reason;
  - counts before and after;
  - the coverage limits of the new registers.
- STATUS.md and HANDOVER.md updated. The next step is a focused cross-vendor check of these changes, then step 3 (recipe contract and pilot PLAN).

## Checks before handing back

- The deterministic double rebuild passes, and all seeded negative fixtures still fail.
- Add negative fixtures for:
  - a crop that cuts a text span;
  - a learner-displayable held reference.
- Both re-cropped diagrams are inspected by eye, against a source render with the crop box overlaid.
- Each award-table total equals the paper tariff for that question.
- Every provenance match is confirmed on both rendered pages.

## Not in this round (for step 3, the PLAN)

- Computing "same type" references per recipe branch (R2-02).
- The diagram-generation spec and acceptance check.
- Sketch-marking criteria per branch.
- Bloom levels.
- Turning grade bounds into parameter domains.
- Deciding whether shared modules are standalone recipes or embedded modules.
- Targets for wider Cambridge variety.

## Constraints

- Do not commit or push; Vitalis commits.
- Do not modify:
  - either review folder;
  - source PDFs;
  - `standard/`;
  - other subjects;
  - app code;
  - pinned checkouts.
- Acquire anything only with the YYeni Web Harvester; write no new scraping scripts.
- No PLAN, recipes, generators, work orders, imports or learner assignment.
