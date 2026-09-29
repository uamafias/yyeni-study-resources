# Handover prompt — Cambridge International AS Level Physics 9702

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge International AS Level Physics, syllabus code 9702** (syllabus for 2025, 2026 and 2027, AS route). The learners are Namibian secondary students, English medium, sitting Papers 12, 22 and 34 in the October/November 2026 series; the first 9702 paper is on 2026-10-14. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/cie-9702-as-2025-2027/PLAN-9702-as-physics.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-9702-as-2025-2027/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the variant register, the prohibited patterns, and the depiction rule.
4. `work/cie-9702-as-2025-2027/curriculum/answer-shapes.json` — how each command word and tariff is marked.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for 9702: money appears only where a situation involves it, and "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus’s own statements about a paper (its marks, its question types, the Paper 3 mark allocation) are allowed.

Everything is derived already. `work/cie-9702-as-2025-2027/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**12 topics, 860 items (823 flashcards, 37 performance tasks), 54,270–77,720 words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next.

```
  1     Physical quantities and units
  2     Kinematics
  3     Dynamics
  4     Forces, density and pressure
  5     Work, energy and power
  6     Deformation of solids
  7     Waves
  8     Superposition
  9     Electricity
  10    D.C. circuits
  11    Particle physics
  12    Practical skills
```

Topics 1-11 are the content, examined on Papers 1 and 2; topic 12 is the Paper 3 practical skills. Work in the order listed: topic 1 (units and uncertainty) underpins every calculation, and topic 12 builds on 1.3.

For each topic `<T>`, read `work/cie-9702-as-2025-2027/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-9702-as-2025-2027/topics/<T>/work_order.json` (every slot, pre-decided; `work_order.md` is the same plan as a table). Then produce, in `work/cie-9702-as-2025-2027/topics/<T>/`:

1. `claims/canonical_claim_ledger.json` — every statement the topic teaches, each mapped to the objectives it serves. 2–4 claims per objective.
2. `content-units/CU-9702-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `work/cie-9702-as-2025-2027/exemplar/` holds two small slices, 9 (9.3 Resistance and resistivity, Papers 1 and 2) and 12 (12.3 gradient, intercept and uncertainty, Paper 3), that pass every check. Copy their **shape** — the field set of every claim, block and item, equations as plain text with Unicode symbols, working carried to three significant figures with each step as "a ÷ b = c", a three-question multiple-choice set with its key and distractor reasons, a practical task with a markdown table of our readings, `claims_seen` and `authored_hash`. Do not copy their volume or their content, and do not reuse their scenarios in those topics.

Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:

```python
import sys, hashlib
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text
x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
```

## Every item carries its labels

Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item.** The item’s `item_id` is its slot id; a MISCON slot also names its `misconception_entry`.

- `assessment_objectives` is what the examination credits. `blooms_level` is what the learner is asked to do: Remember, Understand, Apply, Analyse, Evaluate, Create. Different axes, both required on every item.
- If you change a slot’s subtype, change its Bloom level to match plan section 4 and record the change.

## Rules that come from the syllabus and the corpus

Breaking one produces material that teaches something the papers do not ask, or asks it the wrong way.

1. **Command words.** Only these open a prompt: `Calculate`, `Determine`, `State`, `Describe`, `Explain`, `Show`, `Estimate`, `Define`, `Justify`, `Sketch`, `Complete`, `Compare`, `Suggest`, `Give`. Never `Comment`, `Predict`, `Identify`, `Measure`, `Repeat`, `Set`, `Plot`, `Draw`, `Label`. Definitions open with "Define" or "State what is meant by"; laws and principles with "State". Bench instructions and Plot, Draw, Label appear only as steps inside a practical task or a short answer, never opening a flashcard. Justify and Estimate belong to topic 12.
2. **Tariffs.** Use the slot’s. A point-marked answer carries exactly as many creditable points as its tariff, and its guidance says which.
3. **Answer shape.** A calculation earns its marks in steps: the equation in symbols, the substitution, the answer with its unit. A definition is marked on its key words. A Show answer ends with more significant figures than the value given. State and Define want the bare element. The marking guidance names every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type, using those words (C-16 matches whole words).
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct idea, and the test that tells them apart — the entry’s `test` field gives it. Never the correct definition repeated.
5. **Glossary.** `curriculum/glossary.json` settles every term’s sense. Use them exactly, everywhere.
6. **Scope.** The contract’s `excluded_constructs` are the limits the syllabus states and the A Level content it excludes, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or mention them, not even to say they are not required. `adjacent_topics` are not scanned: name one in passing, teach it in its own topic.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. The conditioned mechanisms in the subject profile carry their conditions wherever they appear (C-37). Never claim what examiners reward or what a paper contains: the words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).
8. **Self-containment.** A flashcard supplies its own scenario, data, data table or readings and never depends on another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit.
9. **Nothing is reproduced.** No Cambridge question, scenario, program, mark-scheme or examiner-report wording, anywhere. Every scenario, prompt, model answer and piece of guidance is yours.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.
11. **Equations and units.** Every equation is written in symbols first, with each symbol’s meaning and unit the first time it appears in a unit. Plain text with Unicode symbols (½, ², ³, ⁻¹, ×, ÷, ρ, λ, θ, Ω, µ, ∆); no LaTeX. SI unit symbols with negative indices: m s⁻², not m/s/s.
12. **Calculations.** Equation, substitution, answer with unit. Convert every prefix to base units first. Carry working to at least three significant figures and round only the final answer, saying to how many. Write each product or quotient as "a × b = c" or "a ÷ b = c" with c unrounded, because C-32 recomputes it; round in a following clause ("= 11.8, so 12 N to two significant figures").
13. **No fences.** There is no chart renderer and no code in this subject, so any code fence fails C-41. Data and readings go in markdown tables. A graph is described by its axes, shape and key values, or given as a table of points for the learner to plot on their own graph paper. Circuits and force diagrams are described in words or tables.
14. **Multiple-choice sets.** `item_type: "multiple_choice_set"`, one item per slot, `mark_tariff` equal to the number of questions. The prompt numbers the questions, each with four options A-D on their own lines; the canonical answer gives the key ("Key: 1 B, 2 C, …") and, for each question, why the key is right and what error each distractor comes from. Build distractors from `curriculum/misconceptions.json` first. About half recall, half application or calculation.
15. **Practical tasks (topic 12).** `item_type: "practical_task"`. Describe the experiment in words, give our readings in a markdown table with quantity / unit headings, and number the parts with their marks. Readings must be realistic and consistent with the physics (check them). Question 1 tasks end with constants from the gradient and intercept, with units; Question 2 tasks give four limitations and four improvements, each tied to the measurement it affects, and test a relationship against a criterion stated first.
16. **Stated limits.** Some outcomes carry a limit in `syllabus_guidance` (no coefficient of friction, no moving observer, no end corrections, NTC thermistors). They are boundaries for you. Do not teach past them and do not mention them; C-11 scans for them.
17. **Performance-task labels.** A performance slot gives its `item_type`, brief and Bloom level. Set `assessment_objectives` to ["AO1", "AO2"] in topics 1-11 and ["AO3"] in topic 12 (the papers assess nothing else); `mark_tariff` to the marks the brief states (the number of questions for a multiple-choice set); `command_word` to null for a multiple-choice set and to the word that opens the first part otherwise.

## Voice

Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every equation is shown working on a small original example, step by step, with units. Situations are Namibian and southern African where a situation is used (a borehole pump, a minibus taxi on the B1, a solar panel in the Kalahari), with invented names; money in N$ where it appears. No hedging filler and no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/cie-9702-as-2025-2027/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-9702-as-2025-2027 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-9702-as-2025-2027 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-9702-as-2025-2027 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-35, C-39, C-41 and C-43, and a C-18 warning (the per-topic AO mix is reported, not targeted), are expected. Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; a check compares them.

When all 12 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9702-as-2025-2027
```

It publishes only topics whose checks pass and reports any topic it skipped.

## Boundaries

- Do not edit anything under `standard/`, or anything in `work/cie-9702-as-2025-2027/curriculum/`.
- Do not touch any workspace other than `work/cie-9702-as-2025-2027`, and do not edit `work/cie-9702-as-2025-2027/exemplar/`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- anything in the plan that turned out to be wrong
