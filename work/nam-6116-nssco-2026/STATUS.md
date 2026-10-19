# STATUS — 6116 Biology (Namibia NSSCO)
Workspace: work/nam-6116-nssco-2026/   Owner: Lotto   Authoring tool: Codex (Step 5; Claude exemplar/planning retained)

Legacy-content review/migration for the 2026 Angra Pequena learners, started from the
15 October 2026 forensic audit in `Biology_Claude_Code_Handoff/6116_Biology/`.
Audit baseline: main 575a56c5c84f7013833304cc792153e9ddd43902 — the commit this
workspace was started from, so the audit's absence findings still hold.

## Pilot rule: OVERRIDDEN BY THE OPERATOR — settled

Recorded 2026-10-18: Lotto's explicit override of 2026-10-16 is the decision of record. Consulting
Vitalis is not a blocker for any step of this subject and is not to be raised again as one. The
consequences below are kept for the pilot record, not as open gates.

At the time of the override, `operations/SUBJECT-TRACKER.md` recorded the Namibia NSSCO kind
as `not yet` piloted; the tracker now records this review-copy pilot as complete. TEAM-PLAYBOOK.md
step 0 and section 6 reserve the first subject of each new kind to Vitalis.
**Lotto overrode that rule on 2026-10-16 and directed that this subject be run as the NSSCO
pilot by Lotto rather than Vitalis.** The agent raised the rule and stopped before any subject
work; this entry records the deliberate decision rather than a silent bypass.

Consequences the override carries forward, to be resolved before publication:
- Section 6 warns that checks built against exam-evidence files can return `not_run` on a
  subject lacking that evidence, and `not_run` is never a pass. This subject has **no mark
  schemes**, so expect `not_run` on mark-scheme-derived checks.
- Section 6 requires that any check which cannot apply is resolved **in the standard**, never
  worked around in a workspace. Agents may not edit `standard/`, so each such check becomes a
  question for the operator/Vitalis.
- Vitalis has not been consulted on this subject as at the date above.

- [x] 1 Sources found — re-scanned 2026-10-17 (syllabus; 18 papers 2020-2025; 6 distinct combined examiner reports 2020-2025, each carrying a Biology 6116 section; NO mark schemes). Supersedes the 2026-10-16 count of 15 papers / 4 reports.
- [ ] 1 YOU: sources complete — not ticked, deliberately. Actual state (recorded 2026-10-18 on Lotto's instruction): every available source is inventoried in curriculum/source-inventory.json: the syllabus, 18 question papers and 6 examiner reports, 2020-2025. NO mark scheme exists for any series.
- [x] 2 Syllabus facts written — 2026-10-16 (curriculum/syllabus-facts.json: 70 sub-topics, 393 specific objectives, 18 command words, 5 stated exclusions; brief at operations/analysis/6116-nssco-biology-syllabus-brief.md)
- [x] 2 YOU: AO table checked against the PDF (PDF p.38, 39, 40) — Lotto, 2026-10-17, APPROVED WITH TWO ISSUES OPEN (see Open issues)
- [x] 3 Corpus analysis written — 2026-10-17 (operations/analysis/6116-nssco-biology-corpus-analysis.md; 340 question parts, 261 examiner statements, 77 raw misconceptions; GAPS.md records the missing mark schemes, the First Proof years and the unreviewed mapping)
- [x] 3 YOU: analysis read — Lotto, 2026-10-17 (corrected analysis approved)
- [x] 4 Plan built — 2026-10-18 (after authorised demand audit: 57.195663/16.387383/26.416954 against stated 47/28/25; largest gap 11.612617 points, OUTSIDE tolerance; AO approach and full plan approved by Lotto, 2026-10-18; discrepancy remains reported. 540 objectives, 886 items; notes 50,800-80,040 words. See targeted Step 4 repairs at the end.)
- [x] 4 Independent plan and visual-bank spot-review by Codex — 2026-10-18; verdict: fix the plan first (review/CODEX-PLAN-REVIEW-2026-10-18.md). This is not the post-authoring Step 6 review.
- [x] 4 YOU: AO-classification and coverage-first approach approved — Lotto, 2026-10-18; partial approval only. No percentage-driven additions; full-plan approval remains open.
- [x] 4 YOU: plan approved — Lotto, 2026-10-18; explicit approval of the current plan, including the recorded AO mismatch/coverage-first approach and retained scientific/delivery holds.
- [x] 4 YOU: plan included in the Step 7 repository commit — Lotto, 2026-10-19
- [x] 5 Topics authored: 5 / 5 drafted and revised after review (871 flashcards + 15 activities, 1,102 claims, 72,322 rendered words); all five topics PUBLISH on the deterministic checks (2026-10-19); claims unverified, 35 figure items held
- [ ] 5 Published
- [x] 6 Post-authoring cross-review by Claude, 2026-10-19: verdict publish as a review copy, not releasable to learners; see review/STEP6-REVIEW-REPORT-2026-10-19.md (authoring was Codex's draft plus Claude repair rounds, so not a clean two-vendor separation; the named-teacher step is waived, not performed)
- [x] 6 YOU: verdict read — Lotto, 2026-10-19; approved proceeding with Step 7 as a repository review copy
- [ ] 7 YOU: committed and pushed
- [x] 7 NSSCO pilot work completed for repository review-copy scope — Lotto, 2026-10-19; learner release remains open

## Legacy input (not repository output)

The platform currently carries 1,215 shared Biology cards across 61 core lessons and 410
platform objectives (school_id=68, classroom ded8c94a-66ec-449d-8f05-2d963f522117). No
generated workspace, claim ledger, published bank or repository QA pass existed for 6116 in
the inspected snapshot. These cards are reusable legacy input, not a published release.

## Framework findings so far (for the pilot record)

1. `standard/v0.2.0-draft/mine/` is read-only by playbook rule (lines 272, 540): those scripts are
   worked examples wired to Cambridge subjects and the original planner's machine. Step 4.2 directs
   an agent to write its own scripts under `work/<workspace>/planning/`, which is what this
   workspace does. No adapter entry in `standard/` is needed, and none was added.
2. `pdftotext` was absent and was installed (`brew install poppler`, playbook section 1.1).
3. The syllabus PDF needs geometric extraction, not text-order extraction, in two places: the
   three-column content table (column offsets move page to page) and the glossary (the Word table
   renders Outline's and Predict's meanings one line above their term, so plain reading order
   crosses them). Both are handled in planning/transcribe_syllabus.py and documented there.
4. Two sub-topic codes are irregularly typeset in the source: `4.3.5.` and `4.4 .3`.

## Corrections, 2026-10-17

- Source inventory re-scanned after four files were added by another agent and verified here by
  SHA-256, page count and cover text. Earlier totals (15 papers, 4 reports) are superseded.
- Earlier claim that the examiner reports were "general, not Biology-specific" was WRONG. Every
  NSSCO volume 2020-2025 carries a Biology 6116 section (PDF p.49, except 2025 at p.47).
- Assessment-objective transcription completed to exact A1-C5 wording with lead-ins and the
  parenthetical conditions on C1-C3; the earlier table was an abbreviated summary.
- Glossary pairing corrected again: nearest-term matching fixed Outline/Predict but bled a trailing
  line onto Define, Explain and State. Now assigns each meaning to the lowest term at or above it
  within one line-height. All 18 definitions verified clean.
- Raw-mark proportion and final-grade weighting recorded as distinct quantities: AO raw 47/28/25,
  final-grade 50/30/20. Neither is a card quota.
- Paper 1 duration diverges: syllabus says 45 minutes, 2025 paper says 1 hour. Open for the operator.

## Checkpoint queries resolved, 2026-10-17

1. Page citations separated. AO A/B wording printed p.35 [PDF 38]; AO C wording printed p.36
   [PDF 39]; AO percentages and per-paper marks printed p.37 [PDF 40]; paper descriptions,
   durations and marks printed p.36 [PDF 39]. The brief previously cited a single range for both.
2. Grid labels preserved verbatim, including "47% (not more than 24% recall)", under the column
   header "Overall Weighting across all components" (the grid calls its weightings "approximate").
   The denominator of the 24% is NOT stated anywhere in the syllabus; both readings are recorded
   with their evidence and NO interpretation is adopted (`recall_ceiling_denominator`, provenance
   `uncertain`). The derived raw-mark/final-grade reconciliation stays separate, tagged
   `judgement`. No assessment percentage is converted into any card count.
3. Paper 1 duration conflict investigated and left open. Syllabus 45 minutes; 2020-2024 papers
   45 minutes; 2025 paper 1 hour, identity verified (6116/1/25, 40 questions counted, 40 marks).
   No revised syllabus or amendment exists in the repo; the 2025 examiner report is silent on
   duration. Both statements retained (`paper_1_duration_conflict`, provenance `conflict`).
   OPEN FOR THE OPERATOR: confirm with NIED/DNEA what governs the 2026 cohort.
4. Sub-topic count reconciled. The outline parser was matching the section heading
   "5 LEARNING CONTENT" as a sub-topic, giving 71 outline entries against 70 content rows with
   code "5" duplicated. Fixed and regenerated: outline 70 = 5 topics + 65 sub-topics, content 70,
   no duplicate codes, both reconciliation sets empty. Specific objectives unchanged at 393.

- [x] 2 YOU: AO table checked against the PDF — Lotto, 2026-10-17 (approved with two issues open)

## OPEN ISSUES — carried forward, approved as non-blocking by Lotto 2026-10-17

These remain open through the analysis and the plan. Neither may be closed by adopting an
interpretation; both need an external authority.

1. **Denominator of "not more than 24% recall" is undefined.** The syllabus states the phrase at
   printed p.37 [PDF 40] inside AO A's cell, in the "Overall Weighting across all components"
   column, and nowhere defines what the 24% is a share of. Recorded with the evidence for both
   readings in `curriculum/syllabus-facts.json` -> `recall_ceiling_denominator`, provenance
   `uncertain`. No interpretation adopted. Not to be converted into any card count.
2. **Paper 1 duration unconfirmed for 2026.** Syllabus states 45 minutes (printed p.36 [PDF 39]);
   the 2020-2024 papers agree; the 2025 paper states 1 hour with its identity verified. No revised
   syllabus or amendment exists in the repository and the 2025 examiner report is silent. Recorded
   in `curriculum/syllabus-facts.json` -> `paper_1_duration_conflict`, provenance `conflict`.
   Needs NIED/DNEA. No 2026 duration is to be claimed as confirmed.

## Checkpoint review corrections, 2026-10-17 (analysis stage)

1. Paper 2 marks: 479 -> 480. Extraction defect found and fixed (the part "(ii) phagocyte [1]",
   2021 Q3, was discarded by a nine-character length threshold). All 12 structured papers now
   reconcile to their cover totals; this is now a standing check.
2. The 261 examiner statements account as 185 classified + 76 unclassified (Paper 1 performance
   sentences carrying only a percentage). Classes are first-match-wins, so 13 statements (5%)
   matching two classes lose the secondary one; per-class counts are lower bounds.
3. WITHDRAWN: "the failures are knowing and naming, not arguing". Unsupported and contradicted by
   this analysis's own evidence (explain 35 parts, suggest 25, calculate leads Paper 3, every 5-6
   mark task is design or multi-step reasoning, AO B 28% and AO C 25%).
4. "No extended responses anywhere in the qualification" narrowed to the six sampled series. The
   5- and 6-mark tasks were read individually: experimental design, causal chains and genetic
   diagrams. Low tariff does not mean low demand, and the observed ceiling is not a syllabus rule.
5. Topic difficulty rankings marked PROVISIONAL with method, n and spread shown. The three
   "hardest" sub-topics rest on one observation each; all percentages are Paper 1 only and are not
   comparable across papers. The claim about 2.2 Diversity is withdrawn.
6. Mapping validation and misconception curation are now stated as gates that must close BEFORE
   the plan, with coverage of every mandatory objective explicitly independent of exposure.
7. Command-word frequency recorded as governing PROMPT WORDING only; prediction, comparison and
   application remain in scope and must be practised.
8. Answer shapes: no official marking rule may be claimed, but source-backed model answers and
   marking guidance labelled `proposed` and carrying evidence are legitimate and expected.

## Step 4 directives from the operator, 2026-10-17

- Topic-difficulty rankings are EXCLUDED from planning inputs. Evidence and limitations stay in the
  analysis; nothing derived from them reaches the registry, contracts or work orders.
- Mapping validation and misconception curation complete BEFORE the plan is finalised.
- Every mandatory syllabus objective is covered regardless of measured exposure.
- Totals wording: Paper 2 contributes 480 marks across six papers, Paper 3 240 across six,
  together 720 across twelve.
- The two syllabus uncertainties (recall denominator, Paper 1 duration) remain open.

## Step 4 progress, 2026-10-17

Gates closed before planning:
- Mapping validation: second independent method (phrase matching) run against the first
  (distinctive terms). 107 of 341 parts validated by agreement (31%); 258 of 720 marks usable for
  emphasis. Only validated parts inform emphasis; coverage is unaffected.
- Misconception curation: 89 raw -> 26 dropped -> 23 routed to a command-word-miss register ->
  40 curated. 23 have discriminating tests; 17 flagged as needing teacher input.

Correction: the objective count was 393 and is now 364. The earlier figure included 28 repetitions
of the column header "Learners should be able to:" and one wrapped topic-intro line, all registered
as objectives. Filtered at source in transcribe_syllabus.py; everything downstream rebuilt.

Built: curriculum/objective_registry.json (434 entries, 364 assessable, all mandatory),
curriculum/assessment-framework.json, PLAN-6116-nssco-biology.md.

Not yet built: qualification-profile.yaml, subject-profile.yaml, glossary.json, topic contracts,
work orders, exemplar, HANDOVER. These follow approval of the plan.

## Step 4 state, 2026-10-17 end of session — NOT ready for approval

Sequencing corrected: profiles, contracts and work orders are now generated BEFORE the approval
checkpoint, as the playbook requires. The exemplar and HANDOVER are not built.

Generated and passing:
- qualification-profile.yaml, subject-profile.yaml (with slot_plan), glossary.json,
  scope-scan.json, syllabus-exclusions.json, exam-exposure.json
- objective_registry.json: 0 schema violations via build/conform_registry.py
- 5 topic contracts via build/make_contract.py
- work orders for all 5 topics via build/make_work_order.py (62 content units)

FOUR DEFECTS that must be fixed before this plan can be approved:

1. DECOMPOSITION PRODUCES NONSENSE OBJECTIVES. "explain and use sub-multiple prefixes for units
   (kilo, deci, centi, milli, micro)" became "explain deci", "explain centi", "explain milli",
   "explain micro". The member list is a set of prefixes, not a set of skills. The splitter needs
   to distinguish a list of things a learner must handle from a list that only qualifies one skill.
2. EXTRACTION GARBAGE AT TOPIC LEVEL. OBJ-6116-2-01 reads "of teaching time)" — a fragment of
   "(N hours of teaching time)" registered as an objective. Topic-row capture is picking up
   parenthetical prose. 60 of 621 registry entries are suspect on a conservative scan.
3. WORK ORDERS CARRY NO ITEM SLOTS. The generated content_units have blocks_required but no slots
   with subtypes, so the declared slot_plan is not driving item selection. Until this is resolved
   the work orders describe units, not items, and cannot brief an author.
4. AO MIX UNRESOLVED. Work orders report AO 15/20/65 against the syllabus 47/28/25, a 40-point
   gap, and the figure is identical for every topic and did not move when the AO crosswalk,
   flashcard_subtype_ao_map, slot_plan or item_mix_target were supplied. The source of 15/20/65
   has not been located. The playbook requires the largest gap to be 5 points or fewer.

CORRECTION to an earlier claim: the hardcoded AO_CODES in make_work_order.py were reported as a
hard framework blocker. They are not. The tool reads slot_plan.subtypes_by_objective_type and
ao_by_objective_type from subject-profile.yaml (make_work_order.py:308-316), which is the declared
place for a subject to bring its own vocabulary. A workspace-level AO crosswalk (AO1=A, AO2=B,
AO3=C) is recorded in qualification-profile.yaml. standard/ was not edited.

## Step 4 rebuilt, 2026-10-18 — READY FOR APPROVAL

All four defects of 2026-10-17 are closed, each at its cause. Full record:
`planning/REGISTRY-REVIEW-2026-10-18.md`; the order to rerun everything: `planning/RUN_ORDER.md`.

1. **Nonsense decompositions** ("explain deci"). Cause: a regex splitter. All of its output was
   discarded. Decomposition is now written judgement (`planning/decomposition.json`): 80 bullets
   split into complete objectives, one lead-in absorbing six bullets, and reasons recorded for
   lists kept whole.
2. **Extraction fragments** ("of teaching time)"). Cause: the content table was read in -layout
   text order, whose column offsets move line by line. It is now read by word geometry. Further
   damage found and fixed: 4.1 and 4.2.1 collapsed, 3.6.2.3 split, page numbers appended,
   subscripts lost, two stated limits missed. Verified independently: 364 of 364 bullets re-read
   with pdftotext -raw (`planning/verify_transcription.py`). Registry: 540 objectives under 5 topic
   containers; headings and split bullets kept in the planning sidecar with the verbatim source
   bullet for every objective.
3. **Work orders with no usable slots.** Cause, traced in build/make_work_order.py: the framework's
   command words had no `exact_mark_tariff`/`used_at_level`, so every slot got command_word null,
   tariff null and 0 marks. The subject profile also used subtype names the item schema forbids
   (LABEL, APPLY, TECHNIQUE, GRAPH, DATA, DESIGN), and its answer-structure keys ("DEF card")
   matched no subtype. Now 840 slots plus 15 performance tasks. Every slot has a command word the
   papers use at a tariff they set, plus its marking parts. Every objective has slots, and every
   objective's own command word is used by one of its slots (C-15).
4. **AO mix 15/20/65 in every topic.** Cause: with every card worth 0 marks, the mix came only from
   the default Business Studies performance tasks (essay plan, case analysis). Now 44/31/25 against
   the STATED 47/28/25 (largest gap 3), with `top_up` empty: no card is added to chase the target,
   and every AO label follows the item's skill (reasons in subject-profile.yaml).

Also corrected this session:
- Misconceptions: entry-by-entry review, 40 → 27, each tied to one objective with a written test;
  3 flagged for a teacher (`planning/misconception_review.json`).
- Scope: 7 stated limits, not 5, with patterns tested against must-catch and must-allow text. Two
  2026-10-17 patterns would have blocked required content ("water potential" in 3.3.2,
  "maternal and paternal chromosomes" in 4.1).
- Command-word rule: the >= 2 observations threshold was our heuristic, not a repo requirement.
  Now the repo's rule (observed_count > 0, mine/assemble.py:144): 22 words.
- AO bases documented: 47/28/25 is stated (the specification grid) and is the balance target;
  50/30/20 is derived (the final-grade share) and is reference only.
- qualification-profile.yaml: a wrong note saying AO codes are hardcoded in the build is withdrawn.
- glossary.json, scope-scan.json and syllabus-exclusions.json are now generated
  (build_glossary.py, build_curriculum_evidence.py); they were hand-written.
- Corpus analysis: a dated corrections section was appended (counts superseded at the plan stage).
- Exemplar built (exemplar/3, exemplar/4): both slices PUBLISH in a scratch copy.
- PLAN and HANDOVER regenerated by planning/write_plan_docs.py.

Open, needs the operator:
- C-39 reports not_run for every topic: no objective-level evidence map exists (parts are mapped
  to sub-topics). not_run is not a pass. Either a meaning-based objective mapping (Miner work) or
  a decision in the standard.
- Recall-ceiling denominator and Paper 1 duration: still open, as before.
- Step 1 "YOU: sources complete": see the checkbox line for the recorded state.

## Step 4 follow-up, 2026-10-18 — the operator's three points

Lotto held authoring until three points were settled. Each is settled:

1. **Notes length.** The contract formula (make_contract.py:34, 230-470 words per registry
   objective) paid once per member of every split bullet, which gave 132k-190k words. The notes are
   now budgeted per syllabus bullet (planning/notes_budget.py -> curriculum/notes-budget.json):
   **50,800-80,040 words**, in line with 9702 Physics (54k-78k). A full representative section
   (all of 3.3.2 and 3.3.3: 1,630 words of notes, 25 cards and tasks) is
   exemplar/REPRESENTATIVE-SECTION.md, and it passes the suite. C-26 measures each unit against
   the new budget.
2. **C-39.** No longer not_run. All 341 Paper 2 and 3 parts were read in their papers and mapped
   by meaning to objectives, in three Miner passes (planning/objective_mapping/): 261 high, 75
   medium and 5 low confidence. They are built into assessment-evidence/assessment_evidence.json
   (schema-valid, status partial because Paper 1 is not mapped). Exposure is now computed per
   objective from that map. **C-39 passes on all five topics** and in both exemplar slices. The
   mappers' findings on the mined records are in assessment-evidence/GAPS.md.
3. **Misconceptions.** The contradiction is removed. MISCON-6116-013 was settled by reading the
   source question (it asked for the body's mechanical barriers). 019 and 038 discriminate without
   the detail the evidence lacks. All 27 are authorable and none awaits a teacher. 013 and 019
   carry an authoring_constraint (no ciliated cells as a mechanical barrier; no week number for
   embryo and fetus).

Also this round:
- AO balance recomputed independently from the work-order tariffs and our three performance task
  types, with no Business Studies defaults anywhere: 42.8/32.9/24.3 against 47/28/25. It moved
  from 44/31/25 because "discuss" objectives now get an EVAL slot worded "discuss" (3 marks, as in
  the papers) instead of an APP slot worded "suggest". B is +4.9, inside the tolerance.
- Topic 3 is authored in four groups of whole content units (planning/topic3_groups.json), with a
  merge protocol for claims.
- Photosynthesis erratum verified and logged (planning/syllabus_errata.json): the syllabus prints
  "6HO2". The Cambridge 0610 syllabus (2026-2028, p.17) prints 6CO2 + 6H2O → C6H12O6 + 6O2, and the
  atoms balance only with 6H2O.

Plan approval (4 YOU) is still open; authoring has not started.

## Consistency follow-up, 2026-10-18 — the operator's two points

1. **Word budgets.** The superseded figures no longer reach authors. planning/apply_notes_budget.py
   runs after the standard build and writes the operative budget (curriculum/notes-budget.json)
   into every work-order unit and every contract. It keeps the formula's figure beside it as
   word_budget_superseded, and re-renders work_order.md with a note saying which figure governs.
   `apply_notes_budget.py --check` passes for all five topics. On the authoring side,
   planning/check_unit_budgets.py confirms each content unit declares the operative figure, so C-26
   measures against it. It runs in the exemplar harness: both slices pass.
2. **Question references and command words.** mine_papers.py is repaired (assessment-evidence/GAPS.md):
   - full references, 341 of 341 unique, 720 marks;
   - the opening instruction recorded as the command word;
   - parent instructions inherited by parts whose stem lacks one;
   - direct questions recorded as such.

   Every record lines up with its earlier version, and the meaning-based mappings carry across,
   now keyed on year/paper/full reference. Command words, tariffs, framework, exposure, contracts
   and work orders were regenerated. C-39 passes on all five topics from the repaired evidence.
   The mapping is still one unreviewed pass, five parts at low confidence: kept for Codex at step 6.

AO balance after the repair: rollup 43/33/24 (largest gap 5). Unrounded from the slots it is
42.5/33.2/24.3, a 5.2-point gap on B, at the edge. Reported, not tuned.

Representative section read as a learner (exemplar/REPRESENTATIVE-SECTION.md). Every card and task
is answerable from the notes, except that the practical task's variable questions rely on topic 1.
Three fixes made: a cross-link to 1.1/1.2 for those variable skills; a sentence explaining "net"
in the osmosis definition; a 3.3.3 cross-link to 3.3.1 for "concentration gradient".

## Sample review by Lotto, 2026-10-18 — revisions made

Verdict received: revise the sample, then use it as the authoring exemplar. Every point is addressed
in planning/make_exemplar.py, and each correction is also carried into the plan, so authors inherit it.

| Finding | Done |
|---|---|
| Membrane table: "proteins not needed" too categorical | Row now reads: none for simple diffusion; water also through water channel proteins; carrier proteins for active transport (claim 26) |
| Carrier account and item 164 imply direct respiration-driven shape change for nitrate | Generic particle; energy from respiration "used directly by some carriers and indirectly by others"; transport stops when respiration stops |
| Items 160 and 162 force For/Against/Overall | Rewritten as developed points (CHAIN, "discuss", Understand). Plan change, evidenced: Discuss = "a critical account of the points involved" (syllabus p.39); 6 of 7 discuss parts in 2020-2025 ask for developed points. EVAL now only for the 7 two-sided objectives |
| P03(d) accepted cylinder size not stated | Method now states equal length and diameter (cork borer); guidance accepts only controls the method states |
| Root water: fixed cell-to-cell route; concentration only | Gradient towards xylem, through cells and along walls; water potential depends mainly on concentration and also on pressure (claims 16, 17); item 156 rewritten |
| P02(d) accepted "flaccid" with "shrunk" | Plasmolysis credited only for the cell membrane (with cytoplasm) pulled away from the wall; notes and claims use the same wording |
| Item 151 "too little time" stated as fact; fertiliser causation unconditional | "One likely reason", alternative accepted (claim 27); fertiliser answer conditional on the soil water having the lower water potential (claim 18) |
| Skill labels | CHAIN Bloom level set to Understand plan-wide (a taught account); Evaluate kept only for two-sided EVAL and for LIM (evaluating a method, C5) |
| Practical coverage | curriculum/practical-coverage.json: 83 practical objectives, 52 with a hands-on component recorded as NOT covered by the resource. Design objectives' PROC cards ask for a plan (item 153 now a fair-test plan) |

Checks after revision, in the scratch copy: both slices PUBLISH. C-08, C-11, C-16, C-32 and C-39
pass; unit budgets are operative. Notes are now 1,268 + 600 words (budgets 920-1,440 and 500-800).
The AO balance is unchanged at 42.5/33.2/24.3: a 3-mark discuss CHAIN carries the same AO B marks
as the EVAL it replaced.

## Whole-plan review by Lotto, 2026-10-18 — "revise before approval": revisions made

1. **Visuals.** curriculum/visual-requirements.json (planning/build_visual_requirements.py): 92 objectives
   need a visual. 27 need a stimulus image, 70 a teaching diagram, 11 a model drawing and 12 a graph.
   Graphs are deliverable now as tables to plot. For 82 objectives the capability is UNRESOLVED:
   the shared build has no image route (render_chart.py draws only break-even charts, C-41 checks only
   those, and 0455's diagrams were added outside the build). Each requirement states its supply route
   and a teacher acceptance check. Items that need an image name their figure and are held back. The
   PLAN states that the resource is not yet standalone for those objectives.
2. **Complete tasks, matched to the skill**, with marks from the papers' 4-6 mark parts. Evidence is
   per objective in planning/objective_overrides.json:
   - a 5-mark coherent plan (SYNTH) for each of 30 investigate/design/plan objectives;
   - construct a key and use one (4 + 4);
   - a 4-mark labelled drawing for 9 drawing objectives;
   - a 5-mark full genetic diagram for 3 cross objectives;
   - a 4-mark full mechanism (MECH) for 19 multi-step objectives.

   Tariffs now: 82 at 1 mark, 671 at 2, 51 at 3, 33 at 4, 34 at 5. The previous 713 two-mark slots
   became 671.
3. **Sources and verification.** planning/references.json lists the approved references (syllabus;
   OpenStax Biology 2e and Concepts of Biology, CC BY; Cambridge 0610 for conventions; the school
   textbook, to be named). It excludes the unlicensed notes in Revision Notes/. Every substantive
   claim cites evidence or is flagged. A named Biology teacher verifies after step 6 and records it
   in topics/<T>/verification.json; nothing is released before that. The exemplar has 29 of 36
   claims cited and 7 practical procedures flagged.
4. **AO on unrounded marks**: 42.71 / 30.73 / 26.56 against 47 / 28 / 25; largest gap 4.29 (A), within 5.
   Reached by task design; nothing was added or relabelled to move it. The classification judgement
   (B5 explanations as AO B) and the alternative reading are written into PLAN section 6 for a
   teacher to confirm.
5. **Teaching and retrieval.** Key points block per unit; concise canonical answers; a table where it
   removes repetition; one mechanism, one home. The budget is a ceiling, not a target. The exemplar
   was revised to match: decorative place names removed, the duplicated block removed, two complete
   plans and a full genetic diagram added.
6. **Documents reconciled** and guarded by planning/check_docs.py. Sample word counts are read from the
   files; the exemplar types are listed from the items; the reuse rule is one rule (3A starts from
   the exemplar); the repaired question-reference defects are described as repaired.

Also done:
- The five low-confidence mappings were re-read (objective_mapping/review_low_confidence.json): three
  were re-mapped or upgraded, two stay low because they depend on figures.
- Exposure is labelled "Papers 2 and 3 only" in the file and on every objective.
- "extinction" was added to the glossary.
- Teaching dependencies: 21 recorded and written into prerequisite_ids on 237 objectives; split
  siblings are linked through related_ids.

Framework findings to report to Vitalis (standard/ not edited):
- No route for biological images.
- C-24 gives verification no post-review state in the ledger.
- make_contract.py:34 word budgets ignore the subject profile.
- make_work_order.py:281 sub_topic() keeps three code levels.
- make_work_order.py:455-471 writes a null command word, tariff or marking parts without a warning.

Plan approval (4 YOU) still open; full authoring not started.


## Operator visual-bank direction, 2026-10-18 — preparation authorised, full authoring not approved

The operator directed that existing Biology visuals be inventoried/sourced now and stored with objective, card-side, notes and activity mappings for future YYeni image support. This replaces the assumption that no visuals can be prepared without a shared renderer.

- Verified: Economics has a separate reproducible plotting generator at publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py. It is useful for data graphs; it cannot create authentic biological micrographs.
- New bank: visuals/INDEX.md, manifest.json, bindings.json and source-inventory.json. Selected local-note extractions and external originals are staged; sources and hashes are preserved. No candidate is scientifically approved or attached to YYeni.
- The page inventory covers both local NSSCO Biology notes PDFs and all 18 question papers (330 candidate pages; page-text tags are discovery proposals, not semantic mappings). Vector-only figures may need a later crop/extraction pass. No official question text was copied into a new activity.
- Existing-note images include a blank extraction, text tables, a stock watermark and an inaccurate osmosis comparison: dispositions record exclusions/holds. An authentic-looking source is not automatically accurate or cleared for reuse.
- Visual requirements increased from 92 to 97 after explicit judgement additions for magnification and osmosis, and restored image-reading context on split root/stem objectives. Kinds overlap: 33 stimulus, 72 teaching, 11 model drawing, 13 graph requirements. No visual coverage is certified complete.
- One SVG graph is generated from the exemplar P03 mass readings; no micrograph is fabricated. A table supports plotting but does not replace a visual interpretation stimulus.
- PLAN and HANDOVER regenerated with source-first curation, preserved originals, separate teaching/question/answer variants, unfamiliar assessment examples, exact-use bindings and gap reporting. Existing claims and learner items were not changed.
- YYeni card-image display and learner drawing/image submission remain unavailable until demonstrated in the real interfaces. Acquisition, approval and delivery are separate states. Shared-build integration is still unresolved; bank integrity checks do not claim to replace Biology review.
- Full authoring/plan approval remain unticked. No standard/ changes, commit, push, import or learner release.

## Visual bank built and Codex's changes reconciled, 2026-10-18 — preparation only; plan approval still open

Codex's uncommitted changes were inspected and reconciled before rebuilding:
- Kept: the bank layout (originals / reference-only / generated / provenance), the source inventory, the local-note dispositions and Codex's 7 register additions, which were reviewed and moved into planning/visual_requirement_additions.json with reasons.
- Changed: requirement IDs are now stable (VIS-6116-<objective>), so bindings and INDEX were regenerated. The hand-written osmosis SVG was retired in favour of planning/make_graphs_6116.py, which reuses the 0455 matplotlib approach (11 graphs, question and answer variants). Downloads now go through the shared harvester rather than urllib (CLAUDE.md).
- Register: 97 → 109 objectives after review. The additions cover magnification of a drawing, keys, classification groups, flowers, hydrophytes and xerophytes, stomata, extra graphs, distant accommodation (sibling of near) and the pupil reflex.

Bank now:
- 254 asset records: 233 Commons, 10 local-notes reference-only, 11 generated graphs. 301 stored files (397 MB of originals).
- All 233 web originals were fetched with `harvest run` and match the SHA-1 Commons publishes. Commons metadata is stored for each in visuals/provenance/. Every licence is CC0, PD, CC BY or CC BY-SA.
- Three sourcing passes inspected every candidate they proposed; curator holds and notes are in planning/visual_candidate_review.json.
- Teaching, question and answer variants exist for three originals (stem, blood, root), placed from planning/visual_labels.json. Uncertain labels are flagged and the originals are confirmed unchanged.
- Needs: 240 of 350 have an unreviewed candidate, 64 are variants to prepare and 46 are gaps. Approved images: 0. Requirements met: 0.

Accuracy defects found by inspection (an image being found ≠ accurate):
- ROOT-001's scale bar reads "3 µm". It is wrong, so it is covered in variants and the original is unchanged.
- BLOOD-001 has no lymphocyte.
- ROOT-002's organ is unidentified (held).
- OSMOSIS-001 does not clearly show plasmolysis (held).
- ORG-042 looks like a textbook scan under a doubtful licence (held).
- HUM-023 has no creator for attribution (held).
- HUM-026 may be a band neutrophil rather than a monocyte; HUM-021's second cell is uncertain.
- Several diagrams go beyond the syllabus or are keyed only on the Commons page.

Gaps (visuals/INDEX.md):
- All 11 model drawings and their criteria.
- Teaching diagrams for the vertebrate and arthropod groups (2.2-09 to -16), onion and animal tissues, xylem and phloem, blood, the pupil reflex, distant accommodation, meiosis, agents of pollination and xerophytes.
- Relay neurone (3.13.1-01).
- Human population image stimulus (5.3-08).
- Unfamiliar example for 4.3.2-01.
- No dichotomous key image.

Delivery: YYeni card images and learner drawing or image submission are still treated as unavailable until demonstrated. No card was changed and no YYeni write was made. Checks: check_visual_bank PASS (integrity only), check_docs consistent. No standard/ change, commit or push. Plan approval (4 YOU) still open; full authoring not started.

## Codex independent pre-approval review, 2026-10-18 — fix the plan first

Completed the requested plan review and independent visual-bank spot-check. Full findings, all five mapping decisions, sampled asset/source checks and framework reports are in `review/CODEX-PLAN-REVIEW-2026-10-18.md`.

- Verified current totals: 540 objectives; 871 flashcards plus 15 tasks = 886 items; operative notes budget 50,800–80,040 words. No duplicate flashcard slot IDs or missing command words, tariffs or marking-parts lists found.
- Independently recomputed the unrounded AO marks: A 866.5, B 626.5, C 536 of 2,029; shares 42.705766/30.877279/26.416954. Largest gap 4.294234 points, conditional on existing labels and performance-task assumptions. The 47/28/25 stated and 50/30/20 derived bases match the syllabus assessment pages.
- Approval blocker P01: the taught-explanation AO classification needs a demand-based decision against the full A/B wording on syllabus PDF p.38. WHY/CHAIN slots alone carry 255 marks currently assigned to B; arithmetic does not validate that classification. No slots were relabelled.
- Mapping findings P02/P03: 2024 P2 6(a) labels the nucleus, not a prepared-slide meiosis skill; 2023 P2 2(c) asks pesticide uptake, which is not settled by the current translocation/water-uptake contextual links. All five source questions and relevant figures were read. The extinction mapping remains a low-confidence context link, not direct evidence of habitat-destruction knowledge. Evidence/exposure inputs were left unchanged for the plan repair.
- Visual review: nine stored originals, three teaching variants and ten question graphs inspected; seven Commons creator/licence pages checked. All four holds remain justified. Root labels still include beyond-syllabus terms and an obscured leader; stem phloem/bundle and blood labels need teacher review; derivative credit must disclose edits. No visual approved or newly counted. HUMANPOP values remain unverified.
- Corrected documentation through `planning/write_plan_docs.py`: pending-approval/review instructions, stale budget wording, doubled percent signs, and the incorrect explanation of the two low-confidence mappings. Strengthened `planning/check_docs.py` for item/budget totals, these stale phrases, visual-state wording and the authoring hold. Regenerated PLAN/HANDOVER and checked them.
- Checks run: `check_visual_bank.py` PASS (integrity only); `apply_notes_budget.py --check` PASS; `check_docs.py` PASS after regeneration. No claim of full-subject PUBLISH is made: topics remain unauthored. The existing exemplar's earlier PUBLISH result was not independently rerun in this plan-focused round.

Step 4 independent review is marked complete above. Step 6 stays unticked because TEAM-PLAYBOOK defines it as the post-authoring review; no complete authored material exists. Plan approval and every YOU checkpoint remain unchanged. No standard/ edits, curriculum/work-order edits, new learner material, downloads, YYeni writes, commits or pushes.

Next: resolve P01–P03 in planning inputs, regenerate the affected steps in `planning/RUN_ORDER.md`, recompute the unrounded AO balance, and return the revised topic/AO tables to Lotto for plan approval. No additional approval is needed merely to prepare that repair; authoring still needs Lotto's plan approval.

## Targeted Step 4 repairs authorised and applied, 2026-10-18 — proposed AO rule awaits decision

Lotto directed the nucleus/pesticide/extinction repairs, a demand-based AO proposal and slot audit,
explicit visual holds/derivative disclosures, regeneration and checks. This authorised the targeted
plan repairs only, not plan approval or full authoring.

- Evidence: nucleus identification remapped to OBJ-6116-3.2-01 with the cell-example limitation recorded.
  Pesticide uptake is unresolved and extinction is definition/context only; neither counts as direct
  objective exposure. All 341 raw parts remain: 339 direct records plus 2 entries in
  assessment-evidence/mapping_exceptions.json. Direct confidence: 262 high / 77 medium / 0 low;
  the unresolved pesticide part remains low confidence in the exception register. This is not
  independent approval of the entire map. Paper 1 remains unmapped.
- Proposed AO rule: taught explanation/comparison/implications = A; consequential information
  processing or inference = B; actual C1–C5 practical demand = C. Words/subtypes alone do not decide.
  planning/ao_demand_audit.json records all 871 slots, including conditional authoring demands.
  136 labels changed; counts, tariffs, command words, Bloom labels and objectives are unchanged.
  WHY: 66 A, 3 genetics B, 22 practical C; 51 taught CHAIN accounts are A. Seven generic EVAL slots
  are provisionally A, and one genetics WHY probability explanation is provisionally B. Eight
  explicit ambiguous cases are listed for the operator; the remaining unauthored B/C slots also
  carry conditions and require prompt review later.
- Exact aggregate: A 1160.5, B 332.5, C 536 of 2029 marks-equivalent =
  57.1956628881 / 16.3873829473 / 26.4169541646. Largest gap 11.6126170527 on B, OUTSIDE tolerance.
  No attempt was made to tune labels or add filler to close it. Performance-task allocations remain
  provisional marks-equivalent assumptions, to be recomputed from authored parts later.
- Visual bank: 10 explicit holds, including the previous four plus ROOT-001/STEM-001/BLOOD-001,
  HUM-021/HUM-026 and HUMANPOP. Held assets count towards no candidate need. 226/350 needs have
  unreviewed candidates, 76 variants remain to prepare, 48 are gaps; zero approvals/fulfilled needs.
  Derivative files now disclose labels/leaders, masks/key panels and draft source/licence/change
  credits; originals are unchanged. Metadata/hold checks were strengthened, not weakened.
- Regenerated evidence/exposure, framework, contracts/work orders, exact AO rollup, operative
  budgets, practical/visual requirements, bank metadata/bindings/INDEX, existing exemplar labels,
  representative sample, README, PLAN and HANDOVER. New AO audit application is mandatory in
  planning/RUN_ORDER.md, after the shared work-order build and before budgets/docs.
- Validation: evidence schema and direct/exception accounting pass; C-39 passes all five topics;
  slot/tariff/command/Bloom invariants and independent rational AO total pass; AO audit, operative
  budget, visual-bank integrity/holds/derivative disclosure and document checks pass. The existing
  exemplar slices receive PUBLISH with zero failed checks, C-18 warnings, and NOT_RUN C-35/C-41/C-43
  where no applicable stimulus/depiction/practice text exists. Unit budgets pass. No full-subject
  PUBLISH or visual scientific approval is claimed.
- New framework report: standard/v0.2.0-draft/checks/run_checks.py exits 0 only when release_decision
  equals pass, but successful reports return publish. Both exemplar runs report PUBLISH with exit 1.
  The isolated harness records the mismatch and asserts the report verdict plus zero failed checks;
  standard/ was not changed.

Full packet: review/STEP4-REPAIRS-2026-10-18.md. Historical review findings are retained in
review/CODEX-PLAN-REVIEW-2026-10-18.md; its P02 is repaired, P03 is honestly unresolved/excluded,
and P01 now has an audited proposal rather than the old subtype rationale.

Remaining operator decision: confirm/amend the proposed AO rule and the eight ambiguous cases.
If accepted, meaningful data/application demands need designing in appropriate existing slots;
that next design step has not been performed to restore tolerance. All YOU boxes and the later
Step 6 box remain unchanged. No full authoring, standard/ edits, commit, push or YYeni write.

## Operator AO clarification incorporated, 2026-10-18

The operator supplied a detailed question/report review and directed: generic taught comparisons A,
genotype inference and consequential information processing B, investigation demands C. The operator
also corrected the earlier overstatement: the syllabus does not say that B always requires supplied
data or an unfamiliar context. Actual reasoning is the test; novelty alone is not.

- Stored the operator review as judgement input in planning/ao_operator_review.json, distinguishing
  the supplied paraphrases/model answers from independently verified official marking guidance.
- Revised the audit generator, mandatory work-order annotations, profile and document generators to
  remove the universal data/unfamiliarity requirement. Existing case-based APP input constraints
  remain that task design, not a universal definition of B.
- Seven generic EVAL comparisons are now settled as taught A by operator direction. Two disputed
  boundaries remain explicit on four affected slots: breastfeeding taught/study-pattern explanation
  (3-437-CHAIN A, 3-438-APP B provisional), and full derivation versus recognition of standard genetic
  ratios (4-110-CALC B and 4-111-WHY B provisional). A table or standard ratio alone does not settle AO.
- Provisional labels, counts/tariffs and exact totals are unchanged: A 1160.5, B 332.5, C 536 of 2029;
  57.1956628881 / 16.3873829473 / 26.4169541646. The plan remains outside tolerance.
- Paper 1 examples are classification evidence supplied by the operator; they were not inserted
  into the direct exposure map, which remains Papers 2 and 3 only.
- Regenerated the demand audit, work-order metadata/mix summaries, operative budgets, repair packet,
  PLAN and HANDOVER. Audit/budget/evidence/slot-invariant/document checks pass. No actual item labels
  changed in this follow-up, so existing exemplar QA verdicts remain those from the preceding run.

Plan approval remains open. No further demand redesign, full authoring, visual approval, standard/
edit, commit, push or YYeni write occurred. The next planning decision is how to address the B-demand
shortfall while preserving the corrected classifications and the two explicit boundaries.

## Partial approval and move to coverage audit, 2026-10-18

Lotto: "let’s move on. I approve of this part of the plan."

Recorded as approval of the corrected AO-classification and coverage-first approach discussed
immediately before that instruction. It is not full-plan approval or authority to start authoring.
The two explicit classification boundaries remain documented. The five-point repository tolerance
is reported as a framework rule; neither its definition nor standard/ was changed.

Completed the next bounded planning audit: review/REASONING-COVERAGE-AUDIT.md and its JSON sidecar,
generated by planning/audit_reasoning_coverage.py. Explicit existing slots provide routes for every
B1–B7 demand type, plus C planning/data/conclusion/method reasoning. Some are demonstrated by the
existing exemplar. No wholly missing B demand type was identified in this audit, and no activities
were added/redesigned merely to reach the exam weighting. This does not establish sufficient
breadth/frequency/challenge of an unauthored bank. Actual prompts and their necessary stimuli need
review later; existing visual holds remain in force.

Updated judgement inputs, mandatory demand metadata and generated PLAN/HANDOVER/repair packet to
record partial approval and avoid treating the AO mismatch as proof of inadequate reasoning
practice. Counts/labels/tariffs, evidence repairs and exact AO totals are unchanged. Full-plan,
source-completeness, visual approval and release checkpoints remain unchanged. No full authoring,
standard/ edit, commit, push or YYeni write.

## Independent coverage verification and C5 reference correction, 2026-10-18

Recorded the operator's independent verification in planning/reasoning_coverage_review.json:
B1–B7 cited routes, genuine reasoning in the sample, item totals, checks and unauthored/approval
state were independently confirmed. The qualification remains: planned routes do not establish
sufficient breadth, frequency or difficulty across the finished bank.

Corrected the one citation weakness in planning/audit_reasoning_coverage.py: replaced the grouped
C3–C5 row with separate C3 processing/anomalies, C4 evidence/conclusions and C5 method-evaluation
rows. C5 now cites existing ITEM-6116-1-057-PROC and ITEM-6116-1-058-LIM, both on the explicit
objective "Identify sources of error and suggest possible improvements in procedures". The actual
task must connect a stated method's error to its effect and an appropriate improvement.

Regenerated review/REASONING-COVERAGE-AUDIT.md and its JSON sidecar; the generator validates all
cited slots and AO assignments. Document consistency check passes. No activity, count, label,
tariff or work-order demand changed. All approval boundaries and visual holds remain unchanged.

## Full-plan and generated-image approval, 2026-10-18

Lotto: "I approve of the plan. As well as the generated images."

Step 4 YOU: plan approved is ticked with Lotto and date. Planning/operator_approvals.json records
approval of the current plan and the 11 original generated graph assets, pinned to all 42 current
PNG/SVG variant hashes. This supersedes earlier entries saying full-plan approval was open.
The approval accepts the present plan's recorded AO approach/discrepancy; no activity is added to
chase percentages. The shared framework is unchanged.

Generated graphs now carry operator_approval separately from scientific_review and delivery.
Source/data verification (notably HUMANPOP), known label/identity/rights holds on sourced images,
missing visual needs and actual YYeni display/submission checks remain recorded. The user approval
is not falsely attributed to a named Biology teacher, nor extended to all sourced images.

The plan/HANDOVER, repair packet and visual bank documents/manifest are regenerated to reflect
approval. Full authoring has not started in this approval-recording turn. The separate plan-commit
checkpoint remains open; agents do not commit/push. No learner release or YYeni write occurred.

### Image-approval scope clarified by Lotto, 2026-10-18

Lotto: 'I approve of the sourced images as well. meant "generated" in a general sense'.
This supersedes the narrower interpretation in the preceding entry: operator approval covers all
254 current bank assets (301 stored files), sourced as well as original generated. The approval
register now pins every asset's current file hashes. Operator approval is not being withheld from
any sourced image. Existing reference-only rights status, accuracy/label/data issues and delivery
holds remain visible; no missing licence, scientific verification or platform feature is inferred.

Approval-record regeneration completed: operator approvals appear in all 254 manifest assets and
are pinned to all 301 stored file hashes. PLAN/HANDOVER and visual INDEX reflect full-plan and
sourced/generated-image approval. Document consistency and visual-bank integrity/approval-hash
checks pass; scientific verification, existing issue holds and delivery states were not advanced.

## Step 5 started by explicit operator instruction, 2026-10-18

Lotto directed authoring all Biology notes, flashcards and activities under the approved plan,
keeping unresolved images pending and running required checks; no commit, push or learner release.
This explicitly authorises authoring while the plan-commit checkpoint remains unticked.

Topic 1 first authoring pass: 110 claims, 7 content units, 109 items, rendered notes 7,187 words.
Schema, coverage, arithmetic, labels, budgets and remaining applicable checks pass after repair.
C-35 remains failed on ITEM-6116-1-044-PROC: an abstract graph-interpretation procedure is treated
as an actual break-even chart and required to declare business chart coordinates. Exact code:
standard/v0.2.0-draft/checks/yyeni_checks.py c35(), lines 582–598. Expected: assess biological
stimulus or recognise a general procedure with no supplied chart; actual: requires price,
variable_cost/fixed_costs chart model. No false business chart or check bypass supplied.
Unresolved image-dependent drawing/measurement/plotting items are recorded in authoring_notes.json.
The topic remains check-blocked, not PUBLISH, while the next topics are authored.

Topic 2 authored: 40 claims, 2 content units, 26 items; rendered notes 1,742 words.
Final deterministic decision PUBLISH; budget declaration check passes. This is structural build
readiness, not learner release or scientific verification. Missing sources and image/model/delivery
needs are listed in topics/2/authoring_notes.json and the claim ledger.

Topic 3 uses the four whole-unit authoring groups explicitly required by HANDOVER. Group 3A
reuses the two approved membrane units and authors its remaining units: 121 claims, 7 units,
103 items. Local schema, answer-shape, arithmetic and scope checks pass on that group; full-topic
checks wait for the merge. Diffusion B cases were strengthened to require inference from effective
exposed area, confounded bulk mixing and total diffusion path rather than renamed taught examples.

## Step 5 authoring inventory and final checks, 2026-10-18

All five topics have been drafted in the approved order. Topic 3 used the four whole-unit
authoring groups required by HANDOVER; the lead merged their claims and items, preserving
group artefacts under topics/3/authoring-groups/ so the live datasets contain no duplicates.
Reproducible author scripts are under topics/, not the protected planning/framework directories.
Full detail, including held item IDs, missing-reference claim IDs, below-minimum units,
all documented deviations and current check output: topics/authoring_audit.json.

| Topic | Claims | Units | Flashcards | Activities | Rendered words | Final gate | Image-held items | Claims without evidence | Units below minimum |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 110 | 7 | 106 | 3 | 7,105 | REJECT: C-35 | 4 | 110 | 2 |
| 2 | 40 | 2 | 23 | 3 | 1,742 | PUBLISH (checks only) | 3 | 26 | 0 |
| 3 | 587 | 23 | 481 | 3 | 32,514 | REJECT: C-35 | 23 | 172 | 3 |
| 4 | 213 | 13 | 153 | 3 | 11,175 | REJECT: C-35 | 7 | 75 | 9 |
| 5 | 152 | 5 | 108 | 3 | 7,405 | REJECT: C-35 | 3 | 59 | 2 |

Totals: 540 objectives, 1,102 claims, 50 content units, 871 flashcards and 15 activities
(886 items); 57,133 body words and 59,941 rendered words including headings/metadata. All
50 units are within their ceilings; 16 are below their stated minima, explicitly recorded with
no-padding reasons and still subject to teaching-depth review. All 1,102 claims remain unverified
and publishable=false; 442 lack a sufficiently specific approved reference and carry teacher flags.

The approved AO estimator is unchanged: AO1 1160.5, AO2 332.5, AO3 536 of 2029 marks-equivalent,
or 57.19566288812223 / 16.387382947264662 / 26.41695416461311 percent. This uses the original
paper-model split for performance tasks; it is not a completed part-by-part semantic AO audit.
No slot or flashcard AO/Bloom/command-word/tariff changed to meet a percentage.

Checks completed: full deterministic suite and what_to_fix for each topic; operative-budget
declarations for every topic; subject-wide exact slot coverage, label equality, claim revisions,
artefact hashes, MCQ set lengths, source-ID linkage and pending-figure checks. No invariant failures.
Docs remain consistent and visual-bank integrity passes: 254 approved assets/301 files; zero
completed scientific verifications, zero fulfilled visual requirements, no YYeni attachments.
Forty image-dependent items remain explicitly held. All original image/rights/data/delivery issues
remain tracked; no source or derived image was changed by this authoring run.

**Unresolved build blocker — C-35.** Topics 1, 3, 4 and 5 each have one failure:
ITEM-6116-1-044-PROC, ITEM-6116-3-258-APP, ITEM-6116-4-089-PROC and ITEM-6116-5-045-APP.
Code: standard/v0.2.0-draft/checks/yyeni_checks.py c35(), lines 575–605. Biology's profile omits
depictions.chart_model; the checker defaults to break_even and treats literal graph/chart in a
prompt as requiring price, variable_cost and fixed_costs. Minimal example: the general procedure
“Describe a sequence for interpreting a graph of plant length against time.” has no plotted chart
and no context.chart. Expected: a Biology-appropriate check or an honest not_run for unsupported
scientific coordinates; actual: business-chart failure. Repeated identical failures were recorded,
and repair of that integration gap stopped. No business metadata invented, graph demand hidden,
check weakened or protected profile/framework/planning input edited.

A separate runner issue remains: run_checks.py returns exit 1 even for Topic 2's publish decision
because its final comparison expects pass; what_to_fix exits 0 and confirms PUBLISH. C-18 is the
expected count-based AO warning. C-26 records the intentional below-minimum units. C-20 flags
two Topic 3 integrated practical comparisons (-053-APP and -125-APP); these retain their complete
planned tasks rather than being split to satisfy a warning.

**Originality screen.** The PDF workflow extracted 346 nonempty pages from all 18 held papers
and the Biology sections of six reports; the syllabus was not reopened. An exact normalised
eight-word screen found three non-definition artefacts, which were rephrased (one generic
exemplar instruction and a stomata function answer/rubric). The remaining 35 flags are prescribed
or settled definitions, retained under HANDOVER rule 5. Six of those also trigger the generic
twelve-word threshold: the explicit word-for-word-definition requirement takes precedence and
the exceptions are recorded, not silently cleared. Screen and author review are in
topics/wording_overlap_audit.json and topics/authoring_audit.json. Image-only text and extraction
order remain limitations; this does not replace independent semantic/originality review.

**Authoring decisions and deviations.** Per-topic authoring_notes.json records each from/to/why:

- Topic 1: structured activity's final part assesses consequential extrapolation from supplied
  0–4 h data, keeping practical repeat/method evaluation in C tasks. Redundant arithmetic prose
  was condensed to respect the unit ceiling; the MCQ spread question was made unambiguous.
- Topic 2: practical classification uses standardised litter observation/counts and diagnostic
  evidence, with the required drawing and image tasks still held.
- Topic 3: approved membrane claims retain legacy IDs (including five cross-mapped claims for
  three objectives); the exemplar's three-question MCQ slice was completed to twelve questions
  across the full topic. Diet/health uses ethical observation, alcohol effects and anaerobic
  recovery are qualified, and unresolved neutral-letter/model keys remain held. Diffusion B
  tasks require consequential inference. Breast-milk explanation remains explicitly A/B debatable.
- Topic 4: the breastfeeding B task evaluates confounded exposure data; the standard antibody
  explanation and standard-ratio recognition remain debatable. Homologous-chromosome, selection
  and Down-syndrome accounts carry necessary qualifications; exemplar claim IDs are namespaced
  and restamped. The annual-plant curve task actually requires its pending graph.
- Topic 5: poaching/tourism investigation is ethical and observational; the practical microcosm
  task tests nutrient-related algal growth without claiming proof of the whole eutrophication
  sequence. Pesticide-uptake mapping remains unresolved, and extinction definitions are not
  presented as evidence of directly testing habitat-destruction causes.

The content-unit block schema forbids qa_status, so blocks have claims_seen and authored_hash,
while units/items have review_required. This schema/brief mismatch is recorded in the audit.
The approved generated PLAN/HANDOVER are unchanged; this STATUS records the current authoring state.

**Package not built.** HANDOVER permits publish_subject only when every topic is clean; four
C-35 failures remain. Step 5 is therefore not marked complete or published. Post-authoring Step 6
cross-vendor review and named-teacher verification have not been performed. Nothing was committed,
pushed, uploaded to YYeni or released to learners. No standard/, curriculum/, planning/, exemplar/
or other subject workspace file was edited.


## Review implemented, 2026-10-19 — checks clean, package still unreleased

Operator instruction: implement the changes from review/CLAUDE-REVIEW-OF-CODEX-AUTHORING-2026-10-18.md.

- **C-35 resolved, not a framework defect.** Added `depictions.chart_model: none` to subject-profile.yaml (the framework's own switch, CR-006; used by 0460, 9702 and 9618). All five topics now report PUBLISH with zero failed checks (warnings C-18; C-20 in topic 3). The earlier report to Vitalis about C-35 is withdrawn (topics/authoring_audit.json: chart_model_resolution). The separate run_checks.py exit-code mismatch on a clean PUBLISH is unchanged and still a framework report. Use `.venv/bin/python`: system python3 has no PyYAML and the checker then runs with no profile.
- **Content fixes, two rounds, at the source (the author scripts).** Round 1 from the first independent review; round 2 from a fresh second-pass review on a new random sample. Both rounds ran on topics 1–5 with every item of each script reviewed for the defect classes found, not only the sampled ones.
  - Learner text: no pipeline wording (new gate topics/check_release_hygiene.py: PASS, 0 problems; it fails on VIS codes outside held prompts, "pending/reviewed/Proposed" wording and rubric template labels). Notes teach only; defensive meta-commentary and mis-titled sections fixed; unit titles are section-level.
  - Marking guidance rewritten as plain one-point-per-mark statements across all topics (the C-16 answer-structure words kept naturally). Marks that restated the stem, split one idea over two marks, bundled several ideas or fixed categories that would zero valid answers were corrected; "any two" lists added where alternatives are valid.
  - Science: beak removed as a bird diagnostic, virus-versus-cell difference corrected, deforestation oxygen mark replaced, quiver-tree wording, auxin/root wording, 3.8.3 overstatements, glucagon table consistency, triplet-code and UV mentions removed, Namibian examples checked (Okavango → Kavango; unsupported regional malaria claim removed).
  - Image items: 35 held under visuals_pending (T1 2, T3 23, T4 7, T5 3); each cites its figure once and has no status wording. Topic 2's three figure items were reworked to need no figure.
  - Tariffs, AO labels, Bloom levels, command words, subtypes and slot IDs were not changed (audit_authoring.py asserts they match the work orders). AO estimator unchanged: A 57.20 / B 16.39 / C 26.42.
  - Notes now total 72,263 rendered words, inside the 50,800–80,040 budget; no unit is below its minimum.
- **Originality screen** re-run against all papers and Biology report pages: the only overlaps are prescribed syllabus definitions (recorded exceptions); one non-definition prompt phrase was reworded.
- **Protected inputs untouched:** nothing under standard/, curriculum/, planning/ (except none edited in this round), exemplar/ or visuals/ changed. Exemplar-derived items and the standard renderer's header line ("rendered from the approved content units...") cannot be edited here.

Open, for the operator:
- **Label questions** the fixers raised and left alone (AO/Bloom/command-word mismatches, e.g. several APP items at AO3 that are plain recall, "Evaluate" items at AO1, "draw" tasks at Apply, 2-marks-for-3-structures items). Changing them changes the approved work orders and the AO plan.
- **Teacher verification:** all 1,102 claims remain unverified and not publishable; 442 have no evidence entry. Named Biology verifier and school textbook still needed. Items to check are listed in the fixer reports, notably Benedict's temperature, Namibian examples, 3.9 expired-air figures, and whether hypotonic/isotonic terms (used in exemplar-derived 3.3.2 notes and P02) are in scope.
- **Package not built.** publish_subject.py would package the 35 held figure items as they are; the playbook's Step 5 "Published" and Step 6 review stay open. No commit, push, YYeni write or learner release.

## Codex full review actioned, 2026-10-19 — held-figure packaging made safe; label proposals recorded, none applied

Source: review/CODEX-FULL-REVIEW-AND-CLAUDE-HANDOVER-2026-10-19.md (operator instruction: fix the confirmed Step 5 defects). Planning inputs were not changed. The documented planning regeneration order was re-run in a scratch copy: every work order was byte-identical and every contract differed only in `generated_at`.

- **Held-figure packaging (high).** `topics/build_review_package.py` builds a REVIEW-ONLY copy through the standard builder on a filtered copy: 851 of 886 items, the 35 held items omitted and listed in `review-package/HELD-ITEMS-OMITTED.json`, written to `review-package/` and never `publish/`. It refuses to run if `publish/nam-6116-nssco-2026` exists and refuses to finish if any exported prompt cites a figure. The standard builder was not run and `standard/` is not edited. Omitting items does not meet any visual need. HANDOVER and RUN_ORDER now say not to run `publish_subject.py` here; framework report: review/FRAMEWORK-REPORTS-FOR-VITALIS-2026-10-19.md (also the learner-note header and the runner exit code).
- **Figure-dependent keys.** 3-258 now states the figure content it needs (second curve above the first plateau); 4-052/4-053, 3-033, 3-057, 3-375, 3-413 are keyed by structure or stated assumption, with the cervix given a function; each `visuals_pending` reason says what the bound figure must show. All stay held; no hold lifted.
- **Infant feeding (4-059 / 4.3.2-07).** Method (breast or bottle) separated from milk type (breast milk, expressed or direct, versus formula); the "only the mother can give it" and "mother is ill" absolutes removed; health-worker advice stated. Claim remains unverified; the Biology verifier should confirm against the CDC guidance Codex cited.
- **Evidence count.** Corrected to **448** claims without an evidence entry (T1 110, T2 26, T3 172, T4 81, T5 59); the earlier 442 used a stale topic 4 figure.
- **Guidance structure.** Entries differing from the tariff fell from 118 to 31 after the shared helper began giving each stated credit its own entry. Screen (`topics/audit_guidance_structure.py`): 840 one entry per mark, 24 explicit multi-mark entries, 7 option rules, 0 unclear. A reviewer pass over the 94 highest-risk items found 7 real problems, all addressed above (3-033, 3-057, 3-355, and the four held keys). How YYeni displays multi-mark or option-rule guidance is not demonstrated: confirm in the real interface.
- **AO / Bloom / command-word audit** (review/AO-BLOOM-LABEL-AUDIT-2026-10-19.md): every item read against its prompt; 40 proposals (9 AO, 20 Bloom only, 11 command word) and 67 boundary cases kept. **Nothing applied.** Estimator mix now 57.20 / 16.39 / 26.42; if all AO proposals were adopted 57.79 / 15.70 / 26.52 (57.59 / 15.89 / 26.52 excluding those touching an operator ruling); whole-item label split 56.58 / 17.00 / 26.42 now. The paper weighting 47/28/25 is a diagnostic, not a quota. The audit lists the patterns that need one rule (recall of a practical method, conclusions from an investigation, drawing from a photograph) and the work-order fields each change would touch.
- **Audit trail.** review/step5-repair-evidence/ holds the review briefs and findings given to the fixers, the sampled item IDs for both review rounds, and RESOLUTION-LEDGER.md (roles and limits, issue ledger, itemised label concerns). Reviewer reports themselves were not saved by the tooling; nothing is presented as a reviewer record that was not saved.
- **Concision.** The 5.4.1 eutrophication restatement was replaced by a worked data example. The deeper teaching-value edit of the new text in the formerly short units is for the Biology reviewer.
- **Helpers.** `topics/scratch_check.sh` now fails loudly and takes its verdict from `what_to_fix.py` (not from `run_checks.py`, which exits 1 on a clean PUBLISH). The hygiene gate remains a lexical screen only.
- **Results (`.venv/bin/python`).** `what_to_fix.py`: PUBLISH for all five topics (C-18 everywhere, C-20 in topic 3); unit budgets pass; authoring invariants pass; hygiene PASS; 8-word overlap screen: only prescribed definitions; docs consistent; visual-bank integrity PASS (254 assets, 301 files, 0 scientific verifications, 0 requirements met).
- **Still held or open:** 35 held figure items; all 1,102 claims unverified and not publishable; Biology verifier and textbook not named; label proposals await the operator; Step 6, "Published", commit, push and learner release unticked. No YYeni write. No claim of teacher verification.

### Follow-up to the second Codex review, 2026-10-19
- **Manifest (R-15).** The review package's MANIFEST.json and every flashcard file now carry `review_only: true`, `learner_upload: false`, `release_status: "unreleased"`, `claims_verified_by_teacher: 0`, `figures_supplied: false`; each topic's `release_decision` reads `review_only_unreleased` (the structural result is kept as `deterministic_decision`), `open_review_issues` is null with a note, and each note copy has a review-only banner.
- **Infant feeding (R-16).** 4-059 / 4.3.2-07 now compare one thing: breast milk with formula milk. The method points (no preparation, anyone can give the feed) are gone from both milks and the note says a bottle can hold either milk. The claim stays unverified for the Biology verifier.
- **Package guard (R-17).** The guard now screens for explicit figure-reference wording rather than only `VIS-6116`. It caught all 35 known held prompts and found nothing in the 851 exported items; three false positives were read and exempted by text hash. It is a heuristic and cannot prove an unflagged prompt is answerable without a figure; the docstring and REVIEW-ONLY.md say so.
- The label proposals stay proposals. 3-375, 4-052 and 4-053 stay held. Checks re-run: all five topics PUBLISH (C-18; C-20 in topic 3), unit budgets, hygiene, authoring invariants, docs and visual-bank integrity pass. Still unticked: Step 6, "Published", commit, push and learner release; no YYeni write; no teacher verification claimed.

### Follow-up to the third Codex review, 2026-10-19
- **4-059 and the 4.3.2 section.** The answer no longer says a baby gets breast milk "only if the mother can produce enough" (it now allows expressed or donated milk); "no risk from unsafe water" is now "not having to be made up with water"; the 4.3.2 summary now speaks of breast milk and formula milk; the unsupported "questions often use the terms" sentence is gone. The claim is still for the Biology verifier.
- **Review copies.** The renderer's "rendered from the approved content units" line is replaced in the review-package notes with a draft statement. In MANIFEST.json `not_published` is now `builder_skipped_topics` and `deterministic_decision` is now `structural_check_result`. The workspace notes still carry the renderer line (framework report).
- **Dashboard.** The rendered word total is 72,322. The earlier 442 remains in history entries; 448 is current.
- Checks re-run after the edits; the 35 holds, 3-375, 4-052 and 4-053 remain held; label proposals remain proposals. No teacher verification claimed; nothing committed, pushed, published or written to YYeni.

### Fourth Codex review, 2026-10-19
- 4-059 now says the supply depends on how much milk the mother can produce "unless safely screened donor milk is available" (the earlier "expressed or donated" was imprecise: a mother's own expressed milk does not fix a low supply, and donor milk must be screened). Wording only; the clinical judgement and the CDC and WHO donor-milk guidance remain for the Biology verifier. Structural checks, hygiene, authoring invariants, wording screen, unit budgets and docs re-run clean; review package rebuilt (851 items, 35 held omitted); no learner `publish/` folder; nothing committed, pushed or written to YYeni.

### Operator decision on teacher verification, 2026-10-19
- Lotto explicitly accepts the current authored Biology content and waives the project-specific named-Biology-teacher verification checkpoint for this subject. This is an operator waiver, not teacher verification: all 1,102 claim records remain `unverified` and `publishable: false`, and no figure is scientifically verified.
- The waiver does not clear the 35 held figure items, change the AO/Bloom/command-word proposals, complete the post-authoring Step 6 review, demonstrate YYeni image delivery, or authorise a learner release. The review package remains unreleased; no learner `publish/` package has been built. Earlier plan and handover wording describing teacher verification as required records the pre-waiver rule; this dated decision supersedes that checkpoint for this subject only.

### Step 6 post-authoring review, 2026-10-19
Report: review/STEP6-REVIEW-REPORT-2026-10-19.md. Verdict: publish as a review copy; not releasable to learners. Six reviewers read every topic's notes in full and a sample of items (every performance task and misconception item plus random flashcards): 60 findings (0 critical, 2 high, 23 medium, 35 low). All 58 findings that concerned editable text were repaired in the author scripts (the two exemplar-derived ones were not); a second independent read checked all 60: 56 fixed, 1 partial (practical P03 mapped to 2.2-16, a work-order matter), 2 left open on purpose (protected exemplar items 3-P02 and 4-152), 1 repair had introduced an error (the 5.2 forest-oxygen sentence), now fixed. Copied-wording tool: only prescribed definitions. All five topics PUBLISH on the structural checks; 0 units outside budget; review package rebuilt (851 items, 35 held omitted). Findings are ingested into each QA report (58 resolved by author claim, 2 open, 0 blocking). The 35 held items have a resolution plan in review/HELD-FIGURE-ITEMS-RESOLUTION-PLAN.md. Still open: figures, YYeni image route, label proposals, claim verification (waived, not done), commit, push, learner release.

### Codex post-Step-6 repairs, 2026-10-19

- **Exemplar findings fixed at their generator.** 3-P02 now asks for *no net* water gain/loss, preserving two-way movement in an isotonic solution. 4-152 now tests why a `tall × short` phenotype record cannot determine both parental genotypes. `planning/make_exemplar.py`, both exemplar slices and topics 3/4 were regenerated. The Step 6 findings 3AB-005 and 4-015 are recorded as resolved by an author repair in the topic QA reports, not as a second independent reviewer verdict.
- **Topic 2 P03 mapping fixed.** The task no longer claims drawing objective 2.2-16. Its final part now uses the supplied features to identify both an insect and a crustacean, the two objectives it actually cites. Sampling and mean calculations remain practical prerequisites. Item 2-011's resolution note was updated in the QA report.
- **Demand-based labels decided.** The 40 proposed changes were applied, plus the parallel spinal-cord drawing 3-068. Exact decisions and reasons: `planning/post_authoring_label_decisions.json`; review explanation: `review/POST-AUTHORING-LABEL-DECISIONS-2026-10-19.md`. Ten AO labels, 29 Bloom labels and 11 command words changed. The revised exact 2029 marks-equivalent mix is AO1 1168.5 (57.5899457861%), AO2 318.5 (15.6973878758%), AO3 542 (26.7126663381%). This was not tuned to 47/28/25. All item labels match their work orders; ten learner stems were revised to match command words (4-114 already said “Deduce”).
- **Figure work remains held.** The five existing graph candidates were checked against actual prompts: the breathing-rate, plant-height and generic-pyramid graphs were mismatches. Four new item-specific project graphs were generated for breath volume, annual-plant dry mass, the stated grassland biomass values and the model-town population table. `planning/figure_item_candidates.json` now records six exact draft question/answer graph pairs (including the existing photosynthesis and sigmoid pairs). All 35 figure items remain held and omitted from the review package; the other 29 lack exact item-level bindings. The four new assets have no operator approval or scientific verification. The approved human-population files were restored byte-for-byte when regeneration changed their layout; the generator now preserves those approved hashes. Current visual bank: 258 assets, 317 files, 254 operator-approved assets, zero scientifically verified assets, zero fulfilled requirements.
- **YYeni route checked read-only.** Current connector contracts expose card-side image asset IDs and an image-attachment action. Actual display, learner image/drawing submission and multi-mark guidance rendering remain undemonstrated. No YYeni write was made.
- **Regeneration and checks.** Exemplar, all authors, notes, work orders, PLAN/HANDOVER and the review-only package were rebuilt. The package has 851 items and 72,833 rendered notes words; all 35 held items are listed as omitted, review-only/unreleased flags remain, and no learner `publish/` directory exists. All five topic check decisions are PUBLISH on structural checks alone (C-18 everywhere, C-20 in topic 3). Authoring invariants, AO arithmetic/slot checks, evidence mappings, unit budgets, hygiene, wording, guidance structure, docs, visual-bank integrity and exact-graph candidate checks pass. `run_checks.py` still exits 1 despite PUBLISH; `what_to_fix.py` exits 0. No teacher verification, commit, push, learner release or YYeni write occurred.

### Step 7 repository review-copy publication, 2026-10-19

Lotto approved the Step 6 verdict and directed repository publication and completion of the
Namibia NSSCO pilot. The published artifact for this pilot is `review-package/`, explicitly
marked review-only, unreleased and not for learners: 851 items from 886 authored, with all 35
figure-dependent items omitted and still held. The Step 5 learner `Published` box stays open:
there is no `publish/nam-6116-nssco-2026` folder, YYeni upload or learner release. All 1,102
claims remain unverified and marked not publishable; the operator's teacher-checkpoint waiver
does not change their verification state. The post-Step-6 author repairs were checked by tools
but have not had another independent semantic read. The pilot completion records the completed
planning, authoring, review and review-copy workflow, not learner release.

The repository copy omits downloaded Commons originals and derivatives and third-party
reference-only extracts. The latter have unknown reuse rights; the former are reconstructible
from the tracked source inventory, provenance and generation scripts. Project-generated graphs
are included. A fresh clone must rebuild the visual bank before running its file-integrity
check. The source workspace and review package keep visual needs open; omitted files are not
presented as supplied figures. See `review/REPOSITORY-PUBLICATION-RECORD-2026-10-19.md`.
