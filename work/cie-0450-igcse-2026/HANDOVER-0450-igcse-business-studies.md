# Handover prompt — Cambridge IGCSE Business Studies 0450

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge IGCSE Business Studies, syllabus code 0450**, first examined 2026. The learners are Namibian secondary students, English medium, sitting this exam within weeks. They may have nothing else to study from.

## Start here

Read these four files before writing anything:

1. `AGENTS.md` (repo root) — tells you which role brief applies. You are the AUTHOR.
2. `work/cie-0450-igcse-2026/PLAN-0450-igcse-business-studies.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-0450-igcse-2026/subject-profile.yaml` — the answer structure your marking guidance must name for each card subtype, the conditioned mechanisms, the prohibited patterns.
4. `standard/v0.2.0-draft/roles/AUTHOR.md`

Everything you need is derived already. `work/cie-0450-igcse-2026/curriculum/syllabus-facts.json` records where each assessment value came from — the syllabus page and the verbatim line that states it — and a check re-opens the PDF to prove every quote is real. So the assessment objectives, the AO weights, the paper structures and the command words in the plan are the document’s, not a summary of it. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**25 topics, 884 items, 49,040–70,500 words of notes.** Work through the topics in the order listed below and take the whole subject in one run. Do not stop after each topic to ask what is next.

```
  1.1  1.2  1.3  1.4  1.5  2.1  2.2  2.3  2.4  3.1
  3.2  3.3  3.4  4.1  4.2  4.3  4.4  5.1  5.2  5.3
  5.4  5.5  6.1  6.2  6.3
```

For each topic `<T>`, read `work/cie-0450-igcse-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-0450-igcse-2026/topics/<T>/work_order.json` (every item slot, pre-decided), then produce four things in `work/cie-0450-igcse-2026/topics/<T>/`:

1. `claims/canonical_claim_ledger.json` — every factual claim the topic teaches, each mapped to the objectives it serves. Roughly 2–4 claims per assessable objective.
2. `content-units/CU-0450-<sub-topic>.json` — one unit per sub-topic, a list of prose blocks, each citing the claims it rests on.
3. `learning-items/topic_<T>_items.json` — the flashcards and performance tasks, one per slot in the work order.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** Neither of this subject’s topics is written yet, so copy the exact metadata field set from `work/cie-9609-as-2026-2028/topics/5.4/` — its claim ledger, its four content units and its item file. That is a different qualification: take its SHAPE and its depth, never its content, its command words or its tariffs, which belong to AS Business 9609 and are wrong here.

Every block and every item needs `claims_seen` (`{claim_id: revision}`), `authored_hash`, and `qa_status: "review_required"`. Compute the hash with:

```python
import sys, hashlib
sys.path.insert(0, 'standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text
x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
```

## Every item carries both labels

The work order has already decided each slot’s `subtype`, `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item you generate.**

- `assessment_objectives` is what the examination credits.
- `blooms_level` is what the learner is being asked to do: Remember, Understand, Apply, Analyse, Evaluate, Create.

They are different axes and both are required on every item. If you change a slot’s subtype, change its Bloom level to match the table in section 4 of the plan, and record the change.

## Rules that come from the corpus, not from a style guide

These were measured across 84 mark schemes and 17 examiner reports for this syllabus. Breaking one produces a card that models a question the paper does not set.

1. **Command words.** Use only: `Explain`, `Define`, `Identify`, `Outline`, `Consider`, `Using`, `Calculate`, `State`. Never use `Justify` — it is listed in the syllabus command-word table but never opens a question in 84 mark schemes. Justify appears only inside longer stems, attached to another command word; a prompt that opens with it models a question the paper does not set.
2. **Tariffs.** A command word’s tariff is not free. Use the modal tariff in the plan’s section 2 table, or one of that word’s observed tariffs. Never invent one.
3. **Answer shape.** Section 3 of the plan gives the shape behind each tariff, with the share of real questions it holds for. Write to the shape. The marking guidance on each card must name every part of its subtype’s declared structure in `subject-profile.yaml`.
4. **Misconceptions.** `work/cie-0450-igcse-2026/curriculum/misconceptions.json`, filtered on your topic id, lists confusions examiners record learners actually making. Each earns a `MISCON` card, and a MISCON card is a **discrimination** — the boundary between the two ideas and the test that tells them apart — not the correct definition repeated.
5. **Glossary.** `work/cie-0450-igcse-2026/curriculum/glossary.json` settles senses. Use them exactly and do not invent alternatives. Where a sense is still `null`, settle it once and use that everywhere in the subject.
6. **Scope.** The contract’s `excluded_constructs` are the limits the syllabus states anywhere in this subject, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic, so do not teach, practise or mention them, not even to say they are not required. `adjacent_topics` are not scanned: name one in passing if you must, teach it in its own topic.
7. **Truth.** No unqualified universals — always, never, every, only — unless definitional, legal or arithmetic. A mechanism whose conclusion holds only under conditions carries those conditions every time it appears, not just once in the claim. What an independent third party will do is a likelihood with a reason, never a certainty. Never claim what examiners reward or what a paper contains.
8. **Self-containment.** A flashcard may not depend on another card, and its answer may not rest on a fact its own prompt does not supply. Arithmetic is correct, every figure carries its unit or currency, and a quantity is named in the units it is measured in.
9. **Nothing is reproduced.** You may not have Cambridge question or mark-scheme wording in front of you, and you must not reproduce any. Write every prompt and every answer yourself.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.

## Voice

Plain, direct explanatory prose. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once, so every mechanism, formula and worked example is written out. Worked examples in Namibian dollars (N$) with Namibian and southern African contexts, and at least one non-African example per unit. No hedging filler, no "it is important to note", no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it — and record the change in `work/cie-0450-igcse-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure class demands a subtype that genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a written reason of at least twelve words rather than padding the bank with a card that teaches nothing.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0450-igcse-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0450-igcse-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0450-igcse-2026 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**; `C-30` stamp warnings and `not_run` on checks whose input does not apply are fine.

Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced — a check compares them.

When all 25 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0450-igcse-2026
```

It publishes only topics whose checks pass and reports any it skipped.

## Boundaries

- Do not edit anything under `standard/`.
- Do not touch any workspace other than `work/cie-0450-igcse-2026`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every scope call you had to make rather than derive — where the syllabus wording was ambiguous, or where you deviated from a work order and why
- anything in the plan that turned out to be wrong
