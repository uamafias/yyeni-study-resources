# Repair round 2: NSSCAS Mathematics 8227 steps 1–3 analysis

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this repair. His decisions are final; do not wait for, or route anything to, other approvers.

The independent review (Claude Opus 5.5, verdict **repair analysis**) found that the source work is sound but the mapping layer is not ready to plan from. This round repairs the analysis and adds two owner-approved extensions. It does **not** create a PLAN, work orders, recipes or generators; those follow re-review.

## Read first

1. `AGENTS.md`, `TEAM-PLAYBOOK.md` and `standard/v0.2.0-draft/roles/AUTHOR.md`. Then `workbench/playbook/README.md`, `quality.md`, `templates.md` and `textbook-analysis.md`.
2. This folder, in this order:
   - `owner-decisions-2026-11-16.md`. It is binding and overrides the review where they differ, notably on capability holds.
   - `report.md` §1, §3, §4 (the family table) and §7.
   - `findings.md`. Each finding gives a locator, the expected state, a minimal correction and a check.
   - `inputs.json`, which lists the reviewer's scans and recomputations that you must re-run.
3. Your round-1 records under `workbench/analysis/`, `workbench/tools/` and `curriculum/`.

Before changing anything, copy `analysis/analysis-snapshot.json` (sha256 `1afe99d5…a561f`) to `analysis/history/analysis-snapshot-r1.json`.

## Work, in order

### A. Mapping repair (R13-01, R13-02, R13-21, R13-03)

- **Per-part fields.** Give each of the 250 parts these fields:
  - `directly_assessed_objective_ids` and `directly_assessed_demand_ids`. These are independent of `pattern_ids`.
  - `prerequisite_demand_ids` with their role.
  - Typed dependency edges: `cue` ("hence", "using your answer", given result) or `follow-through` (F.T. in the award table).
- **Coverage.** Compute coverage from the part→demand links only. The coverage code must not read families.
- **Demand status.** Give every one of the 138 demands a real disposition with a reason, plus one status:
  - `examination-observed (NSSCAS 8227)`, with part links;
  - `comparable-examination-observed (Cambridge 9709)`, with Cambridge links (section F); or
  - `syllabus-derived`.
- **Demand list.** Confirm or correct the reviewer's list of unexamined demands (R13-02).
- **Dependencies.** Add the 18 questions with missing dependency edges (R13-03). Derive cues by scan and record any manual overrides.

### B. Syllabus records (R13-11, R13-12, R13-13, R13-19, R13-20)

- **Grade descriptions (owner decision 4).** Transcribe the grade a/c/e descriptions (syllabus pp19–24) as level-descriptor evidence, each statement linked to objective and demand IDs. For each family, record the grade statements that bound its variation: the easiest branch at grade e/c and the hardest no further than grade a. Record MF9 (pp25–30) as notation and formula support, not scope.
- **Qualifiers.** Add the missing syllabus qualifiers and limits (R13-12).
- **Normalised mathematics.** Add normalised mathematical text for each objective, checked against the rendered pages. Replace the tautological quote check (R13-13).
- **Assessment conditions.** Add an assessment-conditions record per year: the formula sheet contents (trimmed from 2023), precision and angle rules (R13-19), and the cross-paper theme note (R13-20).

### C. Corrections and source defects (owner decisions 1–3; R13-04–08, R13-14–16)

Apply these owner decisions:

- **2023 P1 Q9.** Record it as defective and held. Principal-value inverse trigonometry becomes syllabus-derived, supported by Cambridge evidence.
- **2023 P2 Q7(c).** Do not adopt the degree-mode alternative. Require radian mode, and record the anomaly against report p338.
- **2023 P1 Q1(b).** Hold it as an exemplar. Proof recipes state a ≠ 0.

Then fix the following:

- Link the two missing award excerpts (2021 P2 Q2 and Q4) and correct the count to 24 (R13-07).
- Fix the mis-tags (R13-08).
- Record 2024 P2 Q5(a) (R13-14) and 2021 P1 Q6 external division (R13-15).
- Record the textbook p550 resolution and the convention conflicts (R13-16).

### D. Representation, diagrams and sketches (owner decision 6; R13-10, R13-18, R13-27)

From 2026-11-17 the app reads sketched answers and diagrams, and generates diagrams similar to a source diagram. Nothing is held for capability. Record what the generator and marker need instead, on every part:

- **`given_representation`.** One of text, diagram, graph or table, with what must be read from it.
- **`diagram_assets`.** Crop each diagram from the rendered page, not from text extraction. Store it under `analysis/assets/` with source path, page, crop box and sha256.
- **`diagram_parameters`.** Which labels and values in the diagram vary with the instance, which are fixed, and the constraints that must hold (scale, angles, shaded region definition).
- **`response_format`.** One of numeric, symbolic, proof/show-that, sketch or explanation.
- **Sketch parts.** For sketch responses, list the credited features from the award table where one exists; otherwise label them as derived from the tariff.

Cover all 11 CAP-8227-02 parts, the two sketch-dependent parts (2023 P2 Q6(d) and 2025 P1 Q4(c)), and every diagram-bearing question listed in R13-18. Mark all of them `include`.

### E. Families (R13-09; report §4)

- Record each family's discriminating decision and evidence.
- Restructure the families per the §4 recommendations: merge, split or retain. Departures are allowed with a reason.
- Bring `selection-table.md` up to the template columns.

### F. Examination references (owner request N1)

Add `examination_references` to every part, family and Cambridge item. Each reference has:

```
board                 "NSSCAS" | "Cambridge International"
syllabus_code         "8227" | "9709"
year, session         session null for NSSCAS; "Feb/March" | "May/June" | "Oct/Nov" for Cambridge
paper                 "1" | "2" (NSSCAS); component+variant e.g. "12" (Cambridge)
question, part
printed_page          verified on the page image; also keep pdf_page
source_path, source_sha256
relation              "original" | "same-type" | "related"
verified_by
learner_label         built by the builder from the fields above
```

Only `original` and `same-type` references are shown to learners; `related` stays internal. The label templates are approved:

- **Generated variant:** "Same type as NSSCAS Mathematics 8227, 2023 Paper 1, Question 5(b), page 7".
- **Original NSSCAS question shown verbatim:** "NSSCAS Mathematics 8227, 2023 Paper 1, Question 5(b), page 7".
- **Original Cambridge question shown verbatim:** "Cambridge International AS Level Mathematics 9709, Paper 12, May/June 2017, Question 5, page 6".

A family's references are the union of its member parts' and its Cambridge items' references. A part is `same-type` to a family only when its demand set and response format match the family's.

### G. Cambridge evidence (owner request N2)

**Corpus.** Use the 9709 P1 and P2 question papers and mark schemes for 2015–2025 under `Question Banks/Cambridge Curricula/Cambridge AS and A Level/Mathematics (9709)/`. Vectors are in pre-2020 P1 (moved to P3 in 2020). Use a P3 part only when it is strictly within 8227 scope. Acquire any further files only with the YYeni Web Harvester.

**Scope.** The 8227 syllabus and LIMIT01–08 decide what counts. Record a scope check for every item: in-scope, in-scope-parts-only, or out-of-scope with the reason.

**Priority:**

1. **Every gap demand** (zero NSSCAS parts after section A). Aim for at least three distinct verified items per demand where they exist, and report demands with none. Start from the candidate table in `owner-decisions-2026-11-16.md` N2. Note that 9709 2020+ excludes points of inflexion.
2. **Diagram-bearing questions** for any in-scope demand.
3. **Thin demands**, those with two or fewer NSSCAS parts.
4. **Wider variety** as time allows. Report what share of demands gained Cambridge items.

**Records.** Write `analysis/cambridge-evidence.json` and `.md`. Each item records:

- `item_id`;
- its locator and mark-scheme locator;
- marks;
- `verbatim_text`;
- `diagram_assets` and `diagram_parameters`;
- `assessed_8227_demand_ids` and objective IDs;
- `scope_check`;
- `purpose` (`gap-fill` or `variety`);
- `evidence_label: "comparable-examination-observed (Cambridge 9709)"`;
- `examination_references`.

**Verbatim text.** Owner-authorised for learner use, with attribution. Transcribe it exactly, with mathematics in LaTeX, and check it against the rendered page image (pypdf output garbles mathematics). Record `transcription_status`. Never paraphrase an item presented as an original, and never present a Cambridge item as Namibian.

### H. Builder and checks (R13-17)

Make the builder:

- compare full ordered tariff sequences with label alignment;
- derive award-excerpt pages and dependency cues by scan, with overrides recorded;
- fail on a seeded negative fixture.

## Deliverables

- Updated records under `workbench/analysis/` and `curriculum/`, with new files `cambridge-evidence.json/.md` and `analysis/assets/`.
- Updated builders under `workbench/tools/`.
- A regenerated `analysis-snapshot.json`.
- `workbench/checks/repair-r2-report.md`, containing:
  - a table mapping every finding ID (R13-01 to R13-29) and owner decision to what changed, the file and the check that proves it, or to "deferred" with a reason;
  - the counts before and after the repair.
- STATUS.md and HANDOVER.md updated: the decisions are recorded, and the next step is cross-vendor re-review.

## Checks before handing back

- The rebuild is deterministic, and the reviewer's scans in `inputs.json` re-run and agree. Explain every difference.
- Every part has at least one demand link. Coverage code does not read families. Every demand carries exactly one of the three statuses.
- Every Cambridge item has:
  - verbatim text checked against the rendered page;
  - a scope check;
  - a mark-scheme locator;
  - an attribution label.
- Every family has examination references, or is explicitly syllabus-derived.
- The seeded error fails the build.

## Constraints

- Do not commit or push; Vitalis commits.
- Do not modify:
  - this review folder;
  - source PDFs;
  - `standard/`;
  - other subjects;
  - app code (Vitalis owns the app changes);
  - pinned checkouts.
- No new scraping scripts.
- No PLAN, work orders, recipes, generators, imports or learner assignment in this round.
