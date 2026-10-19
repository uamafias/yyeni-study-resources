# Handover prompt — NSSCO Biology 6116

Paste everything below the line into the authoring harness with this repository open. It is self-contained: the agent needs no other instruction. (Claude Code: per TEAM-PLAYBOOK step 5, the lead agent gives each topic sub-agent the brief there and points it at this file.)

---

**Plan approved by Lotto, 2026-10-18.** The originally banked 254 images are operator-approved at their recorded hashes; four later item-specific graphs remain unapproved. The authored draft and Step 6 review copy are complete, but 35 figure items remain held. The operator waived the named-teacher checkpoint without verifying claims. This handover does not authorise a commit, push, YYeni write or learner release; retain all scientific, rights, data and delivery holds.

You are authoring the complete learner resource for **NSSCO Biology, syllabus code 6116** (NIED 2018 syllabus, Ordinary Level, Grades 10–11). The learners are Namibian secondary students, English medium, sitting Papers 1, 2 and 3 in the 2026 examination. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/nam-6116-nssco-2026/PLAN-6116-nssco-biology.md` — **the plan. This is your brief.** Read all of it.
3. `work/nam-6116-nssco-2026/subject-profile.yaml` — the answer parts your marking guidance must name for each subtype and task type, the conditioned mechanisms, the variant register, the prohibited patterns and the depiction rule.
4. `work/nam-6116-nssco-2026/curriculum/answer-shapes.json` — how each command word behaves in the papers (tariffs only: no mark scheme exists).
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for 6116: money appears only where a situation involves it, the context object's business fields are null, and "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus's own statements about a paper (marks, question types) are allowed.

Everything is derived already. `work/nam-6116-nssco-2026/curriculum/syllabus-facts.json` records where each assessment value came from. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject's workspace.

## The job

**5 topics, 540 objectives, 886 items (871 flashcards, 15 performance tasks), 50,800–80,040 words of notes** (the budget in `curriculum/notes-budget.json`, carried in the contracts and work orders as the operative budget; the older formula is retained as `word_budget_superseded`). Work through the topics in this order and take the whole subject in one run.

```
  1     Scientific processes
  2     Classification and diversity of living organisms
  3     Organisation and maintenance of the organism
  4     Development of the organism and the continuity of life
  5     Relationship of organisms with one another and with their environment
```

**Topic 3 is authored in four groups** (`work/nam-6116-nssco-2026/planning/topic3_groups.json`), one agent per group, each owning whole content units: 3A 3.1, 3.2, 3.3.1, 3.3.2, 3.3.3, 3.4, 3.5; 3B 3.6, 3.6.1, 3.6.2; 3C 3.7, 3.8.1, 3.8.2, 3.8.3, 3.9; 3D 3.10.1, 3.10.2, 3.11, 3.12, 3.13.1, 3.13.2, 3.13.3, 3.14. Follow the protocol in that file: own unit files, `learning-items/topic_3_items_<group>.json`, claims staged in `claims/staging/claims_<group>.json` with ids `CLM-6116-<group>-NNN`; the lead merges the claims into the one ledger, renders once and checks the whole topic.

Topic 1 (scientific processes: mathematical requirements, graphs, units, error, experimental technique) underpins the practical objectives in every later topic. Topic 3 is by far the largest; give it the time its size needs.

For each topic `<T>`, read `work/nam-6116-nssco-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/nam-6116-nssco-2026/topics/<T>/work_order.json` (every slot, pre-decided; `work_order.md` is the same plan as a table). Then produce, in `work/nam-6116-nssco-2026/topics/<T>/`:

1. `claims/canonical_claim_ledger.json` — every statement the topic teaches, each mapped to the objectives it serves. 2–4 claims per objective.
2. `content-units/CU-6116-<sub-topic>.json` — one unit per content unit in the work order, prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
4. Then render the notes and run the checks (commands at the end).

**Notes budget.** Each content unit's `word_budget` is the figure its work order gives (`work_order.json`, `content_units[].word_budget`, taken from `work/nam-6116-nssco-2026/curriculum/notes-budget.json`); C-26 measures the unit against it and `planning/check_unit_budgets.py` confirms you declared the right one. Ignore `word_budget_superseded`: it is the old per-objective formula, kept only for the record. **The budget is a ceiling, not a target**: never pad to reach the minimum; if a unit is complete below it, say so in one line in `authoring_notes.json`, and if it needs more, say why there. One explanation serves all the members of a split bullet; give each member its own sentence or table row, not its own essay. Read `work/nam-6116-nssco-2026/exemplar/REPRESENTATIVE-SECTION.md` for the depth and length expected.

**Structural exemplar.** `work/nam-6116-nssco-2026/exemplar/` holds two slices that pass every check (verified in a scratch copy of this workspace; see its README): 3, the whole of 3.3.2 Osmosis and 3.3.3 Active transport (every slot of ten objectives, Key points blocks, two complete investigation plans, two "discuss" cards written as developed points), and 4, part of 4.4.2 monohybrid inheritance (a full genetic diagram). Item and task types shown: APP, CALC, CHAIN, DEF, FEATURE, LIM, MISCON, PROC, SYNTH, WHY, multiple_choice_set, practical_task, short_answer. Copy their **shape**: the field set of every claim, block and item, the evidence entries on claims, the null business fields of `context`, `claims_seen`, `authored_hash`, working written as "a ÷ b = c", concise canonical answers. **Reuse:** group 3A starts units 3.3.2 and 3.3.3 from the exemplar, which already is those units, and completes them against the work order (re-stamping anything it changes); topic 4 extends the 4.4.2 slice to the whole unit. Nowhere else reuse the exemplar's scenarios.

Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:

```python
import sys, hashlib
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text
x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
```

## Every item carries its labels

Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item.** The item's `item_id` is its slot id; a MISCON slot also names its `misconception_entry`.

- `assessment_objectives` is what the examination credits (AO1 = NSSCO A, AO2 = B, AO3 = C). `blooms_level` is what the learner is asked to do. Different axes, both required on every item.
- Read each slot's `ao_demand`: the planned demand and conditions are mandatory. B requires actual information handling or reasoning; supplied data or unfamiliarity are not universal prerequisites. A renamed taught case alone is insufficient. C requires a practical demand. Record the new input and inference for conditional B slots in `authoring_notes.json`. If the actual prompt cannot support the planned AO, report it rather than silently changing the demand or label.
- If you change a slot's subtype, change its Bloom level to match plan section 4 and record the change.

## Rules that come from the syllabus and the corpus

1. **Command words.** Only these open a prompt: `describe`, `explain`, `name`, `state`, `suggest`, `identify`, `define`, `complete`, `draw`, `calculate`, `give a reason/give reasons`, `give`, `show`, `discuss`, `outline`, `write`, `construct`, `list`, `describe and explain`, `label`, `count`, `determine`, `distinguish`, `match`, `plot`, `shade`, `what is meant by`, `work out`, `estimate`, `indicate`, `measure`, `read`, `record`, `support`. Never `apply/use`, `compare`, `predict`, `sketch`. Command words are lower case in the slot; capitalise the first word of the prompt as normal English. The skills behind the never-used words (predict, compare, apply) stay in scope; ask for them with a word the papers use.
2. **Tariffs.** Use the slot's. A point-marked answer carries exactly as many creditable points as its tariff, and its guidance says which.
3. **Answer shape.** Marking guidance names every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type, using one of its listed words (C-16 matches whole words). All guidance is proposed: no mark scheme exists for 6116, so never present a marking rule as the board's.
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct idea, and the test that tells them apart; the entry's `discriminating_test` gives it. Where the entry carries an `authoring_constraint` (MISCON-6116-013: no ciliated cells as a mechanical barrier; MISCON-6116-019: no week number for embryo and fetus), the card respects it.
5. **Glossary.** `curriculum/glossary.json` settles each confusable term's sense; where it quotes the syllabus's definition, use that definition word for word.
6. **Scope.** The contract's `excluded_constructs` are the limits the syllabus states, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or mention them, not even to say they are not required. Note what is NOT excluded: "water potential" is required in 3.3.2 (osmosis); "maternal and paternal chromosomes" is the wording of 4.1.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional, in which case set `generality` on the claim. The conditioned mechanisms in the subject profile carry their conditions wherever they appear (C-37). The words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).
8. **Self-containment.** A flashcard supplies its own scenario, data or readings and never depends on another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit.
9. **Nothing is reproduced.** No question, scenario, indicative answer or examiner-report wording from any NSSCO paper or report, anywhere. Every scenario, prompt, model answer and piece of guidance is yours. 12 or more identical words is a defect; 8–11 is allowed only for a standard definition or term.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything.
11. **Staged visuals, no ASCII pictures.** Code fences fail C-41. Preserve images and generated graphs in the visual bank with proposed bindings. Keep tables with quantity / unit headings alongside graphs; a table does not replace an image-reading task. Genetic crosses may also use labelled lines or a markdown grid. C-41 does not certify bank assets: planning/check_visual_bank.py checks integrity and Biology review checks meaning.
12. **Multiple-choice sets.** `item_type: "multiple_choice_set"`, `mark_tariff` equal to the number of questions, `command_word` null. Four options A–D on their own lines; the canonical answer gives the key and, for each question, why the key is right and what error each distractor comes from. Build distractors from the misconception register first. About five in eight on knowledge, three in eight on handling information.
13. **Practical tasks.** `item_type: "practical_task"`, `assessment_objectives: ["AO3"]`. Describe the experiment in words, give a learner's readings in a markdown table with quantity / unit headings, and number the parts with their marks: variables, completing or processing the table, a trend or conclusion from the data, a controlled variable, a source of error with an improvement tied to it. Readings must be realistic and consistent with the biology (check them).
14. **Structured questions.** `item_type: "short_answer"`, `assessment_objectives: ["AO1", "AO2"]`, about 8 marks in four or five parts, each part's marks shown; `command_word` is the word that opens the first part.
15. **"Discuss" cards.** An EVAL slot (two-sided objectives only) weighs points on both sides to a judgement. A CHAIN slot worded "discuss" gives developed points, each with its consequence; never force a for/against frame on it, and an energy cost is not an argument against a process the organism needs.
16. **Complete tasks.** A SYNTH slot is a whole investigation plan (5 marks: changed, measured, kept the same, method, repeats). A drawing slot (APP, draw, 4 marks) asks for a complete labelled drawing and its guidance names the drawing criteria. A key slot asks the learner to construct a key, or to use one on several organisms. A genetics CALC slot (draw, 5 marks) asks for the full genetic diagram. A MECH slot asks for the whole mechanism in order. Never cut these down to a fragment. Never write as if the learner has carried a practical out; `curriculum/practical-coverage.json` records the hands-on part as not covered.
17. **Accuracy and certainty.** Plan section 8 lists the corrections the sample review required (membrane proteins, carrier energy, water potential and pressure, root water routes, plasmolysis). Where a prompt does not establish a cause, say "one likely reason" or "if ..."; accept a control only if the method states it.
18. **Teach in the notes, retrieve on the cards.** Open every content unit with a Key points block (block type `summary`) that states the essential knowledge, usually as a table. Keep each canonical answer to the shortest complete answer that earns its marks (about one short sentence per mark, plus data). Put the fuller explanation in the notes, say a mechanism once in its own unit and link to it elsewhere, and use a table wherever it removes repetition.
19. **Visuals.** Read `visuals/INDEX.md`, `visuals/manifest.json`, `visuals/bindings.json`, `planning/figure_item_candidates.json` and `curriculum/visual-requirements.json` for your topic. Existing candidates can be acquired, reviewed and stored before YYeni image delivery is demonstrated. Preserve originals, licences and scale bars; keep teaching, question and answer variants separate. Do not treat a proposed binding as covered or claim image display or drawing submission without interface evidence. Where an objective needs an image, teaching diagram or model drawing, write the notes and items as planned; an item that cannot be answered without the image names it ("Fig. VIS-6116-<objective>") and is listed under `visuals_pending` in `authoring_notes.json`. Never replace a required image with a verbal description and count the objective as covered. No ASCII drawings, no code fences.
20. **Evidence.** Every substantive claim carries at least one `evidence` entry from `planning/references.json` (source_id, a locator such as "5.2 Passive Transport", support_type). Where no approved reference covers a claim (often a practical procedure), leave evidence empty and say so in the claim's `notes`, for the verifier. Leave `verification.status` as "unverified" and `publishable` false: verification is a later human step (C-24).
21. **Dependencies.** Read `prerequisite_ids` on your objectives (from `planning/dependencies.json`). Link to a prerequisite taught in another unit with a cross_link block and use its glossary terms; do not re-teach it. If your topic uses a term defined later (e.g. "chromosome" in 4.1), define it briefly on first use and link forward.
22. **Sensitivity.** Human inherited conditions, HIV and AIDS, birth control and drug use are taught factually and respectfully, without judgement of people (syllabus note, 4.4.2).

## Voice

Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text and a standalone learning text at once. Every process is explained step by step; every calculation is shown working on a small original example. Use a Namibian setting where the situation needs one (pearl millet in a school garden, a flooded maize field, quiver trees) with invented names; do not add place names that carry nothing. Money in N$ where it appears.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/nam-6116-nssco-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Never add cards to change the AO balance.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-6116-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/nam-6116-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/nam-6116-nssco-2026 <T>
python3 work/nam-6116-nssco-2026/planning/check_unit_budgets.py work/nam-6116-nssco-2026 <T>
```

`what_to_fix.py` prints only failures, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. Expected and not yours to fix: `not_run` on C-35, C-41 and C-43 (no graphical stimulus, generated depiction or practice text), and a C-18 warning (the per-topic AO mix by item count is reported, not targeted). Set the contract's `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; C-42 compares them.

If the same check still fails after three attempts, stop on that topic and report the check, its output and what you tried. Do not work around it.

When all 5 topics are clean, run the isolated checker and the learner-text gate, then build the review copy:

```bash
.venv/bin/python work/nam-6116-nssco-2026/topics/check_release_hygiene.py          # wording gate (lexical only)
.venv/bin/python work/nam-6116-nssco-2026/topics/build_review_package.py           # review-only copy, held-figure items omitted
```

**Do not run `standard/v0.2.0-draft/build/publish_subject.py` on this workspace while any figure item is held.** The standard builder exports every item, ignores `visuals_pending` and calls its output the copy to upload. `topics/build_review_package.py` wraps it on a filtered copy, writes only to `work/nam-6116-nssco-2026/review-package/`, lists the omitted item IDs and refuses to run if `publish/nam-6116-nssco-2026` exists. Omitting a held item does not meet its visual need. The Step 6 review is complete for the review copy; the operator waived the named-teacher checkpoint without verifying the claims. Release to learners still requires resolving the figure holds, testing actual YYeni image delivery, a release decision and the remaining handover checks. Say in your report that the package is a review copy and unreleased.

## Boundaries

- Do not edit anything under `standard/` or another subject workspace. Treat `work/nam-6116-nssco-2026/curriculum/`, `work/nam-6116-nssco-2026/planning/` and `work/nam-6116-nssco-2026/exemplar/` as traced inputs: record any new decision at its source, regenerate dependants and run the checks.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- Do not commit or push.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- per topic: items held under `visuals_pending`, claims with no evidence entry, units below their budget minimum
- anything in the plan that turned out to be wrong
