# Handover prompt — Cambridge International AS Level English Language 9093

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge International AS Level English Language, syllabus code 9093** (syllabus for 2024–2026, AS Level route). The learners are Namibian secondary students, English medium, sitting Paper 1 Reading and Paper 2 Writing in the October/November 2026 series, the first paper on 2026-10-16. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/cie-9093-as-2024-2026/PLAN-9093-as-english-language.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-9093-as-2024-2026/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the variant register, the prohibited patterns.
4. `work/cie-9093-as-2024-2026/curriculum/answer-shapes.json` — how every task is set and marked, with each level table paraphrased band by band.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for this subject: there are no Namibian-dollar figures or invented businesses here, and its "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus’s own statements about a task (its marks, length, texts and AOs) are facts you may state.

Everything is derived already. `work/cie-9093-as-2024-2026/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line, and every objective’s syllabus text was verified against its page. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**11 topics, 417 items (319 flashcards, 98 performance tasks), 24 original practice texts of 13,200–18,000 words, and 17,800–27,100 words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next.

```
  1.1  Form, audience, purpose and context
  1.2  Linguistic elements and literary features
  1.3  Evidence and analytical writing
  1.4  Directed response and comparison
  1.5  Text analysis
  2.1  Shorter writing and reflective commentary
  2.2  Structuring longer writing
  2.3  Imaginative and descriptive writing
  2.4  Discursive and argumentative writing
  2.5  Review and critical writing
  2.6  Expression, range and accuracy
```

9093 at AS is examined by **task**: six tasks on two papers, every one marked by levels. Topics 1.1–1.3 carry what every task uses (forms and audiences, the analytical vocabulary, how evidence is written); the rest are the paper sections. Forty of the hundred marks are for analysis (AO3), forty-five for writing (AO2), fifteen for reading the unseen text (AO1).

For each topic `<T>`, read `work/cie-9093-as-2024-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-9093-as-2024-2026/topics/<T>/work_order.json` (every slot, every practice text, pre-decided; `work_order.md` is the same thing as a table). Then produce, in `work/cie-9093-as-2024-2026/topics/<T>/`:

1. `texts/<text_id>.md` — each practice text the work order lists, **written first**, because its tasks are answered from it. Front matter: `text_id`, `title`, `genre`, `setting`, `written_for`, `words_min`, `words_max`, `original: true`; then the text.
2. `claims/canonical_claim_ledger.json` — every statement the topic teaches: definitions, the conventions of a form, the steps of a technique, why a choice has its effect. 3–6 per objective, each mapped to the objectives it serves.
3. `content-units/CU-9093-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.
4. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
5. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `work/cie-9093-as-2024-2026/exemplar/` is a small, complete slice of topic 1.5 that passes every check: a ledger, three content units, ten flashcards, a 25-mark text analysis answered from a practice text, and the text. Copy its **shape** — the field set of every claim, block and item, `context.text_id`, the text’s front matter, `claims_seen` and `authored_hash`, how the model analysis quotes briefly and is organised by effect. Do not copy its volume or its content. Do not reuse its text in topic 1.5.

Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:

```python
import sys, hashlib
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text
x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
```

## Every item carries its labels

Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item**, plus `context.text_id` where the slot names a text. There are no sub-objectives in 9093: leave `sub_objectives` out.

The item’s `item_id` is its slot id. After the run, the planner’s audit (`standard/v0.2.0-draft/mine/verify_9093.py`) compares every item with its slot; a difference not recorded in `authoring_notes.json` is reported as drift.

- `assessment_objectives` (AO1 reading, AO2 writing, AO3 analysis) are what the examination credits.
- `blooms_level` is what the learner is asked to do: Remember, Understand, Apply, Analyse, Evaluate, Create. A different axis, required on every item.
- `command_word` and `mark_tariff` are null on every flashcard: no AS question is short enough for a card to model. Do not invent either.
- **Paired tasks.** Where a performance slot has `written_about`, it is a part (b): author its part (a) first, put the part (a) item id in `prerequisite_item_ids`, and write the part (b) model answer about the part (a) model answer, quoting it. The part (b) prompt refers to "your" text from the previous task.

If you change a slot’s subtype, change its Bloom level to match the plan’s section 5 and record the change.

## Rules that come from the syllabus and the corpus

Breaking one produces material that teaches something the papers do not ask, or asks it the wrong way.

1. **The syllabus facts, and only those.** You may state what the syllabus states about a task: its marks, its length, its texts, its AOs, its categories (plan section 0). Never claim what examiners reward, report or want: the words "examiner" and "mark scheme" must not appear in learner-facing text (C-10). Teach the move and why it works. Never state a fixed deduction for a word count.
2. **Command words.** Only three are listed, and only two are used at AS: `Compare` (Paper 1 Question 1(b)) and `Analyse` (Paper 1 Question 2). Use one where the slot names it. **Never use `Discuss`** (C-14). Elsewhere use the task form of the paper item the slot models: write a directed response in a stated form, role and audience; write no more than 400 words to a brief; write a reflective commentary; write 600–900 words in a named category. Vary your wording: never copy an instruction from a paper you may know.
3. **Tariffs.** Use the slot’s. A task’s tariff and `ao_marks` decide which tables its guidance marks against.
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct move, and the test that tells them apart — the `test` field gives it.
5. **Glossary.** `curriculum/glossary.json` settles every term’s sense, including the pairs learners confuse (grammatical voice and a writer’s voice; tone and register; form and structure). Use them exactly.
6. **Scope.** Never mention `Paper 3`, `Paper 4`, `language change`, `child language acquisition`, `English in the world`, `language and the self`, `n-gram`, `phonemic transcription` (C-11 scans for them). Adjacent topics in each contract: name in passing, teach there.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. Three registered mechanisms must carry their conditions wherever they appear (C-37): a short sentence creates emphasis by contrast with the sentences around it; a formal register is right for an audience and a purpose, not in general; a rhetorical question works by the answer it invites.
8. **Variants.** Wherever imaginative/descriptive or discursive/argumentative appears, name its variants (narrative, descriptive; discursive, argumentative) and what each needs (C-12).
9. **Self-containment.** A flashcard supplies its own sentence or extract — original, written for the card — and never depends on a practice text or another card. A performance task names its text by `context.text_id`, and its prompt refers to the text by its title and paragraph.
10. **Nothing is reproduced.** No Cambridge text, question, task, title, mark-scheme or examiner-report wording, anywhere. Every text, prompt, model answer and piece of guidance is yours.
11. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.

## Practice texts

- **Original and the right length:** about 550–750 words, as the syllabus sets. The work order gives each text’s range, genre and subject. C-43 checks the file, the declaration and the length.
- **Written for their tasks.** Plan section 6 says what each topic’s texts must make possible. A Section A text (1.4) must give its paired directed response content to re-use and a form of its own to compare against; a Section B text (1.5) must reward twenty marks of analysis. Write the text, then the items; revise the text if an item needs something it lacks.
- **Real texts in form, not in fact.** A feature article reads like a feature article, with a headline, a standfirst and quoted voices; a memoir like a memoir. Invented people, places and organisations only; no real public figures quoted.
- **Settings:** Namibian, southern African or international, as suits the genre, with at least a third of each topic’s texts set in Namibia or southern Africa.
- Age-appropriate, and never modelled on the subject of a Cambridge paper you may know.

## Answers and marking guidance

- **Every paper-style task is levels-marked.** Write a model answer to the top band and inside the stated length. Then guidance that names, table by table, the band descriptors in `answer-shapes.json` the answer meets, in your own words, and one or two sentences on what a Level 3 answer to the same task would do instead.
- **Analyses** (comparison, text analysis, commentary) quote briefly and embed their quotations, run feature, evidence, effect, link to purpose, and are organised by effect, not by paragraph order. The exemplar shows the shape.
- **Writing tasks** keep to the form, audience, purpose and range; the guidance names the conventions used and the focus achieved.
- The guidance must name every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type (C-16).

## Voice

Plain, direct explanatory prose in British English, at AS level: precise terms, defined once and then used. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every term and move is shown working on a short original extract. No hedging filler and no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/cie-9093-as-2024-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-9093-as-2024-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-9093-as-2024-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-9093-as-2024-2026 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-18 (no per-topic AO target, by design), C-35, C-39 and C-41 is expected. Set the contract’s `required_outputs.learning_items`, `required_outputs.content_units` and `required_outputs.practice_texts` to what you actually produced; a check compares them.

When all 11 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9093-as-2024-2026
```

It publishes only topics whose checks pass, carries each practice text with the tasks that use it, and reports any topic it skipped. The planner then audits the whole subject against its plan; you do not need to run that audit.

## Boundaries

- Do not edit anything under `standard/`, or anything in `work/cie-9093-as-2024-2026/curriculum/`.
- Do not touch any workspace other than `work/cie-9093-as-2024-2026`, and do not edit `work/cie-9093-as-2024-2026/exemplar/`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, practice texts, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- anything in the plan that turned out to be wrong
