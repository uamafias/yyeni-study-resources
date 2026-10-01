# Changelog

## 0.2.0-draft - CR-007, 2026-10-01

From the first four authoring runs (9618 Computer Science, 9702 Physics, 0460 Geography, 9093 English Language).

- **C-32 reads chained working.** `1000 × 9.81 × 0.20 = 1962` is evaluated whole, multiplication and division
  first; before, the check read the 81 of 9.81 as an operand and failed correct physics answers.
- **MISCON items may carry their register entry** (`misconception_entry` or `misconception_id`). The work orders
  named it and the schema refused it, so authors had hidden it in `provenance`. Backfilled from the slots on all
  four subjects (329 items) and republished; all 73 topics still PUBLISH.
- 6 new tests in `tests/test_cr007_chains_and_misconception_ids.py`. Suite: 80 passed.

## 0.2.0-draft - CR-006, 2026-09-29

Found while planning Cambridge AS Computer Science 9618, AS Physics 9702, IGCSE Geography 0460 and AS English
Language 9093, the first subjects whose papers split content or AOs between them. Full reasoning in
`operations/standard-change-requests/CR-006-slot-plans-multi-paper-and-arithmetic.md`.

- **A subject can declare its own slot plan.** `make_work_order.py` reads `subject-profile.yaml -> slot_plan`:
  `subtypes_by_objective_type`, `subtypes_by_tier`, `high_tariff`, `command_words_by_subtype`, `tariff_overrides`,
  `ao_by_objective_type` (`'*'` wildcard), `ao_by_paper`, `ao_by_paper_subtype`, `topic_targets_by_paper`, `top_up`,
  `performance_tasks` (with a `papers` filter and `{n}` for the multiple-choice set size) and
  `misconception_slots: one_per_entry`. Absent, the old defaults apply, so every earlier subject regenerates
  byte-identical (0450, 0455 and 9609: 0 diffs; 9618: 0 diffs against its pre-change plan).
- **Multi-paper topics.** A topic's paper key is its papers joined with `+` (`'2'`, `'1+2'`); `ao_by_paper`,
  `ao_by_paper_subtype` and `topic_targets_by_paper` are keyed by it, so a topic examined on two papers with
  different AO splits is balanced against their combined split. `objective_registry.schema.json` gains an
  optional `papers` field per objective.
- **C-32 arithmetic.** Binary sums and differences are recomputed in base 2, and a fixed-width result modulo its
  width (9618). The typeset signs × and ÷ are read as operators (9702), so a wrong product or quotient in a physics
  answer now fails instead of passing unread.
- **C-35 and C-41 read the subject's chart model.** `depictions.chart_model: none` stops C-35 treating every
  graph-like prompt as a break-even chart; a fence labelled with a code language (`depictions.code_fence_languages`,
  default pseudocode and sql) is code, not a picture, for C-41.
- **`multiple_choice_set`** is a valid `item_type` (9702 Paper 1, 0455 Paper 1).
- 12 new tests in `tests/test_cr006_binary_and_depictions.py` and `tests/test_cr006_physics_arithmetic.py`.
  Suite: 74 passed.
- Numbering note: the CR-004 heading above (2026-09-29) and the earlier CR-004 and CR-005 entries below
  (2026-09-12) are distinct changes; this one takes the next free number.

## 0.2.0-draft - CR-004, 2026-09-29

Found while planning Cambridge IGCSE First Language English 0500, the first task-and-skill subject.

- **The item schema refused the fields every plan tells an author to carry.** `blooms_level`, `command_word` and
  `mark_tariff` are decided on every work-order slot and the handovers say to carry them onto the item, but
  `learning_items.schema.json` did not allow them, so C-00 failed. Every 9609 topic had been failing C-00 since the
  Bloom enrichment added `blooms_level`; every 0450 and 0455 topic would have failed on its first item. Added as
  optional fields, with `blooms_level_basis`, `sub_objectives` (a syllabus's finer assessed grain, e.g. 0500's
  R1-R5 and W1-W5) and `context.text_id`. All 19 9609 topics pass again.
- **The 0450 and 0455 registries failed C-00 on every topic** (missing `qualification_profile_id`,
  `subject_profile_id`, `related_ids`, `source_coverage`; unknown `authority`, `generated_at`, `granularity_note`,
  `syllabus_guidance`). An author told not to touch the curriculum could not have cleared it. Added
  `build/conform_registry.py`, which adds only the required fields and never rewrites an unchanged file; the
  descriptive fields are now optional in the schema.
- **RS-48 and C-43, practice texts.** A task answered from a text names it by `context.text_id`; the text lives at
  `topics/<T>/texts/<id>.md`, declares `original: true`, and sits inside its stated `words_min`-`words_max`. An
  official assessment text is never reproduced. `publish_subject.py` now carries each text with the task that uses
  it (`stimulus_text`) and copies it to `publish/<ws>/texts/`. Seven tests in `tests/test_c43_practice_texts.py`.
- **Step one is enforced.** `build/gates.py`: `make_contract.py` and `make_work_order.py` refuse to run until the
  syllabus facts and the corpus analysis for the code both exist.
- **C-11 enforces the syllabus's stated limits; before, it passed on them without looking.** The 0450
  and 0455 contracts held each limit as a tagged sentence ("Knowledge of the formula and calculations of
  PED will not be assessed. [stated in the syllabus]") and each adjacent-topic note as a tagged label.
  C-11 searched learner text for the whole string, so it could never match: an author could have taught
  the PED formula and every check would have passed. Now:
  - `mine/scope_scan.py` writes `curriculum/scope-scan.json`: each stated limit (the syllabus sentence,
    page verified) with the pattern that teaching past it would produce (our judgement), and controls it
    must catch and must allow. 4 limits for 0450, 6 for 0455. A limit applies to the whole subject.
  - `make_contract.py` puts every scan entry in every contract of the subject, moves neighbour-topic notes
    to `depth_constraints.adjacent_topics` (not scanned), and refuses to build a subject with stated
    limits but no scope scan.
  - C-11 accepts `{construct, pattern}` entries and **fails any entry it cannot scan** (a sentence, a tagged
    label, a pattern that does not compile), so this cannot pass vacuously again. 7 tests.
  - The scan found two work-order slots planning what the syllabus rules out: a PED calculation card
    (0450 3.3) and an exchange-rate calculation card (0450 6.3), both from objectives typed as
    calculations. Retyped as comparisons and `Calculate` removed; 0450 now plans 884 items, not 888.
    The syllabus's "will not be assessed" asides are removed from `learner_objective` (shown to learners
    as objective titles); `syllabus_text` keeps them verbatim.
  - `mine/verify.py` section 9 now plants a violation of every limit in every topic and requires C-11 to
    fail it, and checks that no slot plans a ruled-out calculation. It previously checked only that the
    sentences reached the contracts, which is what let the gap through.

## 0.2.0-draft - 2026-09-08

Raised by CR-003 after the RS-28 independent review of the pilot topic (Cambridge AS Business 9609, topic 5.2)
returned **reject** with 15 open issues on a build whose deterministic pass had reported 22 of 25 checks passing.

- **Added RS-33 to RS-40** - bounded generality, generalisations surviving their members, variant completeness,
  assessment claims requiring assessment evidence, command-word-shaped practice, declared answer structures,
  offline reconstructibility, meaningful traceability.
- **Amended RS-07** (a mapping counts only where the item actually practises the objective) and **RS-21**
  (third-party behaviour is likelihood with a reason, never certainty).
- **Six new hard release blockers.**
- **New check suite** at `checks/` - 28 subject-agnostic checks, `not_run` never counts as a pass, a raising check
  is a failing check. Proven against the unrepaired pilot: it independently rediscovered 13 of the 15 review issues.
- **New generated review packet** at `checks/make_review_packet.py` - the reviewer brief and prompt are assembled
  from the build, not hand-written per topic.
- **New human-maintained inputs**: `subject-profile.yaml -> variant_register` and `-> answer_structures`;
  `contract.json -> depth_constraints.excluded_constructs`.
- **New `OPERATOR_RUNBOOK.md`** for teams running the pipeline across many subjects.
- Recorded, in the check source and the runbook, one check that was written and withdrawn for firing on 47 of 68
  items, so nobody rewrites it.

### Found while repairing the pilot topic

- `run_checks.py` now **carries forward any semantic review already on file**. It previously overwrote
  `qa_report.json` wholesale, so every deterministic run silently erased the reviewer's verdict.
- The release decision now reads **unresolved issues**, not the stored verdict. A review that said reject and
  whose issues are all resolved leaves the build awaiting re-review rather than rejected forever - and a build
  whose issues the author has marked resolved can never reach `pass` on that basis alone.
- Added **C-00 schema validity** (the suite had no schema check) and schema support for the three new fields the
  rules require: `generality` on a claim, `generalisation_scope` on a content block, and `variant_register` /
  `answer_structures` on a subject profile.
- Added `build/render_notes.py`. The offline notes are now **rendered from the content units** rather than
  maintained separately, which is what makes RS-39 structural instead of aspirational.
- Two language patterns were narrowed after firing on ordinary prose: `never` and `always` now need a modal or a
  quantified object, and `guarantee` now needs a verb form. `can be` was removed from the hedge list - it was
  suppressing genuine exclusivity claims such as "can be obtained only from".


### Topic 5.4 review round 1 - the measurement, and four checks it bought

5.4 was the first topic authored under v0.2.0 rather than repaired into it. It passed all 31 checks first time and
came back from review **reject: 2 critical, 6 high, 5 medium** - against 5.2's 3 critical and 10 high. Blocking
issues fell from 13 to 8.

**The finding that matters:** every defect class the rules were written for was gone. What remained was
subject-matter accuracy - a collapsed cost classification, owner's drawings treated as a fixed cost, an invalid
claim that break-even assumptions cancel between options, and an arithmetic error in a worked answer. The rules
eliminate process defects and do nothing about knowledge defects. Review is a permanent per-topic cost, not a
gate the framework eventually outgrows.

Four new checks, each built from a finding and each verified to reproduce it before the repair began:

- **C-31 syllabus modality coverage.** An objective whose syllabus wording names a chart, graph or diagram must be
  practised in that form. 5.4.4-02 was decomposed into four members but never into its two modalities, so numeric
  coverage passed while the compulsory graphic half went untaught and untested.
- **C-32 stated arithmetic is correct.** Every equation in a canonical answer is recomputed. It catches the kind of
  error that is worst in a quantitative topic and entirely checkable.
- **C-33 flashcards are self-contained.** A prompt opening "The same print shop ..." with no recorded prerequisite
  cannot be answered when scheduled alone.
- **C-34 interpretation is not an arithmetic check.** Re-deriving a figure by a second route verifies it; saying what
  it means for the business interprets it.

**C-30 was rebuilt.** Its first design compared a hash computed at stamp time against the same text, so it could
never fire. It now records `prior_hash` - the text the stamp replaced - and distinguishes a proven bulk stamp from a
stamp made before the field existed, which it reports as unauditable rather than claiming a verdict it cannot
support. `reviewed_unchanged` implements the part of RS-41 that says a re-read finding nothing to change must be
recorded rather than stamped silently.

**RS-41 drove a repair for the first time.** Revising six claims marked 21 artefacts stale and the gate named every
one, instead of a reviewer finding them three rounds later.

### Second review round - RS-41 and the propagation gate

The pilot topic was reviewed again after repair and rejected a second time with 14 issues. The finding underneath
most of them was one thing: the repair had corrected claims without propagating to every item and block citing
them, so a claim and a card sat side by side saying opposite things. Two of the three criticals were that.

- **Added RS-41 - derived work goes stale when its source changes.** Claims carry a `revision`; blocks and items
  record `claims_seen`. Bumping a claim leaves every citing artefact stale until re-authored. A stale derivative
  blocks release. Schema support added for all three fields.
- **Added C-29** to enforce it. Bootstrapped from the repair history already recorded in the files, it found
  **22 stale artefacts** on the unrepaired build - including every propagation defect the reviewer named.
- **Fixed C-28.** The packet manifest contained its own hash, which can never verify because writing the line
  changes the file. The manifest now excludes itself and its hash is detached in `packet.sha256.hash`.
- **C-12 now scans per content-unit block** rather than a character window. A variant named three sections away
  from the term has not been named where the term is taught.
- Two more over-broad language patterns narrowed (`no other`, and the `guarantee` noun).

**The lesson worth keeping:** the un-propagated card said limited liability makes borrowing "usually easier and
cheaper". The hedge suppressed the language check. *Hedging can make a factually inverted statement pass a
language check* - the pattern sees caution, the content is still wrong. Language checks police confidence, not
truth, and no amount of pattern work changes that.

## 0.2.0-draft — 2026-09-13 (agent routing and work orders)

The pipeline made runnable by open-weights models, with frontier models on the judgement-heavy ends.

- **`AGENTS.md`** at the repository root — the routing file every agent reads first, whatever tool
  it runs in. Three universal rules, then one role brief each.
- **`standard/v0.2.0-draft/roles/`** — AUTHOR (open weights), PLANNER, MINER, REVIEWER (frontier).
- **`build/make_work_order.py`** — computes every decision before authoring: content-unit split,
  each card's objective, subtype, AOs, command word, tariff, difficulty and required guidance parts,
  AO balance and word budgets. Derived from `objective_type`, `depth_tier`, command words and the
  exposure floors. Reproduces the unit split on 18 of the first subject's 19 topics.
- **`checks/what_to_fix.py`** — the failures only, ordered structure-first, each with its ids and
  the one action that clears it. Exits 0 when clean, so it drives an author's fix loop.
- The work order states the **structural AO1 floor** rather than chasing a count target that cannot
  be reached: every objective needs a recall anchor, so padding the bank to hit 30% AO1 by count
  makes the resource worse. AO2, AO3 and AO4 are topped up to target; AO1 is reported.

**The lesson worth keeping:** seventeen frontier authors, one brief, seventeen different judgement
calls. A brief that asks for judgement gets as many answers as it has readers, and a cheaper model
makes that worse. Move the judgement into a generator and the model's job shrinks to writing prose
into slots — which is the thing it is actually good at.

## 0.2.0-draft — 2026-09-12 (shipping pivot)

The release bar changed, and the pipeline was made to run at subject scale.

- **RS-42 amended.** The deterministic suite is the publication gate: a topic publishes when no
  check fails. Semantic review no longer gates publication — it runs on published material and its
  findings are debt the topic carries visibly. A `not_run` check no longer holds publication
  either; those checks are named in the report so a reviewer knows where code gave no opinion.
  Four review rounds across two topics established that the loop does not converge, because each
  round reviews what the previous *repair* touched.
- **`AUTHORING_BRIEF.md`** — the subject-agnostic instruction set for building one topic. It reads
  command words, tariffs, AO targets and answer structures out of the subject's own profile files,
  so one brief serves every syllabus. Topics are independent and are authored in parallel.
- **`build/naming.py`** — the single source of every published filename, derived from the contract's
  `topic_title`. `render_notes.py` now derives its own output name instead of falling back to
  `notes-<number>.md`, and removes a superseded one.
- **`build/publish_subject.py`** — generates `publish/<qualification>/` with named notes and
  flashcards, `INDEX.md` and `MANIFEST.json`. Flashcards carry `objective_titles` beside
  `objective_ids`. Only topics whose checks pass are published.
- The check suite and packet builder find the notes by the derived name.

**The lesson worth keeping:** a file called `notes-4.3.md` costs a person something every time they
open the folder, and that cost is paid for years. Naming is derived data like any other — the topic
title is already in the contract, so the filename comes from there. The same reasoning as RS-47,
applied one level out: if the build can derive it, the build derives it.

## 0.2.0-draft — 2026-09-12 (CR-005)

One rule, two checks and a renderer, from the fourth review of topic 5.4 — one critical, on a build the
deterministic suite had reported clean. Full reasoning in
`operations/standard-change-requests/CR-005-generated-depictions.md`.

- **RS-47 / C-41 — depictions are generated, not authored.** `build/render_chart.py` renders a break-even chart
  from its declared parameters; C-41 re-renders every declared chart, in items and in content blocks, and fails
  any plot that is not byte-identical to the result. A plot with no declared chart fails too.
- **C-42 (RS-45) — contract counts match the live build.** The contract authorised 92 items beside a bank of 105.
- **C-35 narrowed** to accept the revenue/fixed-cost crossing as a real point on the chart.
- **`answer_structures.PROC`** declared, so C-16 stops passing procedural cards vacuously.
- Suite: 43 checks, 48 tests.

**The lesson worth keeping:** a check that tests for the *presence* of a thing will pass a fake version of that
thing. C-31 tested that a graphical objective had a chart item, and got one that was algebraically impossible.
C-35 was built to test the chart's numbers, and got one whose numbers were right and whose lines never met. The
escape is not another check on the artefact — it is to stop authoring the artefact. A generated picture cannot
be faked, because the data is the picture.

## 0.2.0-draft — 2026-09-12 (CR-004)

Four rules, four checks and two mechanisms, from the third review of topic 5.4 (0 critical, 3 high, 4 medium).
Full reasoning in `operations/standard-change-requests/CR-004-conditions-completeness-and-derived-data.md`.

- **RS-43 / C-37 — conditioned mechanisms carry their conditions.** The subject profile registers each mechanism
  whose conclusion holds only under stated conditions; the check fails any claim, block or item that asserts one
  without carrying every condition.
- **RS-44 / C-38 — an answer may not supply its own facts.** A completeness assertion in an answer needs the
  prompt to establish it, or the recommendation to be explicitly conditional. Naming a cost *category* states a
  total; enumerating named *instances* does not.
- **RS-45 / C-39 — derived metadata is recomputed, never edited.** Exposure figures must recompute from the
  evidence records, satisfy the file's own class definitions, and keep no superseded figure beside the new one.
- **RS-46 / C-40 — quantities are named in their own units.** A currency amount is not named in physical units.
- **C-27 gains written waivers.** A class floor names subtypes; where one does not fit the objective the contract
  waives it with a reason of at least twelve words, reported on every run. Padding a bank to satisfy a count
  teaches nothing; a silent gap hides a real one.
- **`checks/ingest_review.py`** replaces the hand edit that merged a review into a qa report, and refuses to mark
  an issue resolved without a written reason.
- Exposure class definitions amended to read on frequency as well as tariff. Recomputing all 258 objectives moved
  exactly one.
- Suite: 41 checks, 43 tests.

**The lesson worth keeping:** all three high issues in round three came from the *repair* step, not from
authoring. A repair that fixes the claim leaves the topic wrong, because every mechanism is taught in several
places and the condition has to travel to all of them. RS-41 cannot see this - the unrepaired copies were never
stale, they cite a different claim. Only a check that recognises the mechanism itself can find them.

## 0.1.0-draft — 2026-08-31

Initial team-review package containing:

- concise operative runtime standard;
- machine-readable runtime standard;
- end-to-end pipeline;
- universal artifact schemas;
- Business subject profile;
- Cambridge International AS Level Business 9609 qualification profile for 2026–2028;
- deterministic validator and pytest suite;
- valid draft fixture and negative controls;
- independent semantic-review protocol;
- draft Claude Co-work handoff prompt;
- team review questions.
