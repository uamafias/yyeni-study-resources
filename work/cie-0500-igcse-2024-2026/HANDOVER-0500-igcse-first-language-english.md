# Handover prompt — Cambridge IGCSE First Language English 0500

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge IGCSE First Language English, syllabus code 0500** (syllabus for 2024–2026). The learners are Namibian secondary students, English medium, sitting Paper 1 Reading and Paper 2 Directed Writing and Composition in the October/November 2026 series, the first 0500 paper on 2026-10-05. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/cie-0500-igcse-2024-2026/PLAN-0500-igcse-first-language-english.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-0500-igcse-2024-2026/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the prohibited patterns.
4. `work/cie-0500-igcse-2024-2026/curriculum/answer-shapes.json` — how every task is set and marked, with each level table paraphrased band by band.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for 0500: there are no Namibian-dollar figures or invented businesses here, and its "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus’s own statements about a task (its marks, length, texts and text types) are allowed.

Everything is derived already. `work/cie-0500-igcse-2024-2026/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line, and every objective’s syllabus text was verified against its page. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**10 topics, 276 items (207 flashcards, 69 performance tasks), 24 original practice texts of 14,300–16,900 words, and 11,200–17,350 words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next. Paper 1 comes first because it is the harder paper: a C needs 44% of its marks, against 53% on Paper 2.

```
  1.1  Comprehension: explicit and implicit meaning
  1.2  Selective summary
  1.3  Words and phrases in context
  1.4  How writers achieve effects
  1.5  Extended response to reading
  2.1  Directed writing: evaluating the texts
  2.2  Directed writing: arguing and persuading in form
  2.3  Descriptive writing
  2.4  Narrative writing
  2.5  Vocabulary, sentences and accuracy
```

0500 is examined by **task and skill**, not by topic. Each topic above is one paper task, or one Paper 2 skill. The skills are R1–R5 (reading) and W1–W5 (writing); every slot names the ones it practises.

For each topic `<T>`, read `work/cie-0500-igcse-2024-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-0500-igcse-2024-2026/topics/<T>/work_order.json` (every slot, every practice text, pre-decided; `work_order.md` is the same thing as a table). Then produce, in `work/cie-0500-igcse-2024-2026/topics/<T>/`:

1. `texts/<text_id>.md` — each practice text the work order lists, **written first**, because its tasks are answered from it. Front matter: `text_id`, `title`, `genre`, `setting`, `written_for`, `words_min`, `words_max`, `original: true`; then the text.
2. `claims/canonical_claim_ledger.json` — every statement the topic teaches: definitions, the conventions of a form, the steps of a technique, why a move works. 3–6 per objective, each mapped to the objectives it serves.
3. `content-units/CU-0500-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.
4. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
5. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `work/cie-0500-igcse-2024-2026/exemplar/` is a small, complete slice of topic 1.3 that passes every check: a ledger, two content units, five flashcards, two tasks answered from a practice text, and the text. Copy its **shape** — the field set of every claim, block and item, `context.text_id`, the text’s front matter, `claims_seen` and `authored_hash`. Do not copy its volume or its content. Do not reuse its text or its items in topic 1.3.

Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:

```python
import sys, hashlib
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text
x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
```

## Every item carries its labels

Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `sub_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all six onto the item**, plus `context.text_id` where the slot names a text.

The item’s `item_id` is its slot id. After the run, `standard/v0.2.0-draft/mine/verify_0500.py` compares every item with its slot; a difference not recorded in `authoring_notes.json` is reported as drift.

- `assessment_objectives` (AO1 reading, AO2 writing) and `sub_objectives` (R1–R5, W1–W5) are what the examination credits.
- `blooms_level` is what the learner is asked to do: Remember, Understand, Apply, Analyse, Evaluate, Create. A different axis, required on every item.
- `command_word` and `mark_tariff` are null on a technique card that models no paper item. Do not invent either.

If you change a slot’s subtype, change its Bloom level to match the plan’s section 5 and record the change.

## Rules that come from the syllabus and the corpus

Breaking one produces material that teaches something the papers do not ask, or asks it the wrong way.

1. **The syllabus facts, and only those.** You may state what the syllabus states about a task: its marks, its length, its texts, its text types, the skills it tests (plan section 0). Never state that accuracy is marked in Paper 1 — it is not, from 2024. Never claim what examiners reward, report or want: the words "examiner" and "mark scheme" must not appear in learner-facing text (C-10). Teach the technique and why it works.
2. **Command words.** Only four exist: `Identify`, `Explain`, `Give`, `Describe`. Use one where the slot names it. Elsewhere use the task form of the paper item the slot models (summarise on a focus, write in role, analyse the language of two paragraphs). Vary your wording: never copy a stem formula from a paper you may know.
3. **Tariffs.** Use the slot’s. A comprehension item’s marks decide how many points its answer needs.
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct move, and the test that tells them apart — the `test` field gives it.
5. **Glossary.** `curriculum/glossary.json` settles every term’s sense. Use them exactly.
6. **Scope.** Never mention `Coursework Portfolio`, `Component 3`, `Component 4`, `Speaking and Listening` (C-11 scans for them). Adjacent topics in each contract: name in passing, teach there.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. Two registered mechanisms must carry their conditions wherever they appear (C-37): a short sentence creates emphasis by contrast with the sentences around it; a formal register is right for an audience and a purpose, not in general.
8. **Self-containment.** A flashcard supplies its own sentence or extract — original, written for the card — and never depends on a practice text or another card. A performance task names its text by `context.text_id`, and its prompt refers to the text by title and paragraph.
9. **Nothing is reproduced.** No Cambridge text, question, task, title, mark-scheme or examiner-report wording, anywhere. Every text, prompt, model answer and piece of guidance is yours.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.

## Practice texts

- **Original and the right length.** The work order gives each text’s range, which is the syllabus’s (Text A and B 700–750, Text C 500–650, directed writing 650–750 in total). C-43 checks the file, the declaration and the length.
- **Written for their tasks.** Plan section 6 says what each topic’s texts must make possible. Write the text, then the items; revise the text if an item needs something it lacks.
- **Namibian and southern African settings, with at least one text per topic set elsewhere.** Vary the genre: fiction, memoir, articles, reports, speeches, letters, reviews, as the syllabus asks.
- **Directed-writing texts come as a pair or a single text** inside one file, headed Text A and Text B, and together inside the stated range.
- Age-appropriate, and never modelled on the subject of a Cambridge paper you may know.

## Answers and marking guidance

- **Point-marked items:** the answer, one mark per point, the acceptable alternatives, and what is not credited and why.
- **Level-marked tasks:** a model answer written to the top band and inside the stated length. Then guidance that names, table by table, the band descriptors in `answer-shapes.json` the answer meets, in your own words, and one or two sentences on what a middle-band answer to the same task would do instead.
- **Summaries** also list the content points on the focus.
- The guidance must name every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type (C-16).

## Voice

Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every technique is shown working on a short original extract, step by step. No hedging filler and no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/cie-0500-igcse-2024-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0500-igcse-2024-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0500-igcse-2024-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0500-igcse-2024-2026 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-18 (no per-topic AO target, by design), C-35, C-39 and C-41 is expected. Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; a check compares them.

When all 10 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0500-igcse-2024-2026
```

It publishes only topics whose checks pass, carries each practice text with the tasks that use it, and reports any topic it skipped.

## Boundaries

- Do not edit anything under `standard/`, or anything in `work/cie-0500-igcse-2024-2026/curriculum/`.
- Do not touch any workspace other than `work/cie-0500-igcse-2024-2026`, and do not edit `work/cie-0500-igcse-2024-2026/exemplar/`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, practice texts, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- anything in the plan that turned out to be wrong
