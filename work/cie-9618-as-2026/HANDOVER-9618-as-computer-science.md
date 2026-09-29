# Handover prompt — Cambridge International AS Level Computer Science 9618

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge International AS Level Computer Science, syllabus code 9618** (syllabus for 2026, AS route). The learners are Namibian secondary students, English medium, sitting Paper 1 and Paper 2 in the October/November 2026 series; the first 9618 paper is on 2026-10-09. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/cie-9618-as-2026/PLAN-9618-as-computer-science.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-9618-as-2026/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the variant register, the prohibited patterns, and the depiction rule.
4. `work/cie-9618-as-2026/curriculum/answer-shapes.json` — how each command word and tariff is marked.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for 9618: money appears only where a scenario involves it, and "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus’s own statements about a paper (its marks, its sections, the pseudocode insert) are allowed.

Everything is derived already. `work/cie-9618-as-2026/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**29 topics, 751 items (669 flashcards, 82 performance tasks), 41,960–60,050 words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next.

```
  1.1   Data Representation
  1.2   Multimedia
  1.3   Compression
  2.1   Networks including the internet
  3.1   Computers and their components
  3.2   Logic Gates and Logic Circuits
  4.1   Central Processing Unit (CPU) Architecture
  4.2   Assembly Language
  4.3   Bit manipulation
  5.1   Operating Systems
  5.2   Language Translators
  6.1   Data Security
  6.2   Data Integrity
  7.1   Ethics and Ownership
  8.1   Database Concepts
  8.2   Database Management Systems (DBMS)
  8.3   Data Definition Language (DDL) and Data Manipulation Language (DML)
  9.1   Computational Thinking Skills
  9.2   Algorithms
  10.1  Data Types and Records
  10.2  Arrays
  10.3  Files
  10.4  Introduction to Abstract Data Types (ADT)
  11.1  Programming Basics
  11.2  Constructs
  11.3  Structured Programming
  12.1  Program Development Life cycle
  12.2  Program Design
  12.3  Program Testing and Maintenance
```

Sections 1-8 are Paper 1 topics and sections 9-12 are Paper 2 topics; each topic’s work order is balanced against its own paper. Work in the order listed: the Paper 2 topics build on each other, and 11.3 draws on 9.2, 10.2 and 10.3.

For each topic `<T>`, read `work/cie-9618-as-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-9618-as-2026/topics/<T>/work_order.json` (every slot, pre-decided; `work_order.md` is the same plan as a table). Then produce, in `work/cie-9618-as-2026/topics/<T>/`:

1. `claims/canonical_claim_ledger.json` — every statement the topic teaches, each mapped to the objectives it serves. 2–4 claims per objective.
2. `content-units/CU-9618-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `work/cie-9618-as-2026/exemplar/` holds two small slices, 10.3 Files (Paper 2) and 1.1 Data Representation (Paper 1), that pass every check. Copy their **shape** — the field set of every claim, block and item, pseudocode in a ```pseudocode fence inside a prompt and on its own lines in an answer, the mark-point form of a worked example’s guidance, binary arithmetic with its working, `claims_seen` and `authored_hash`. Do not copy their volume or their content, and do not reuse their scenarios in those topics.

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

1. **Command words.** Only these open a prompt: `Complete`, `Write`, `Describe`, `Explain`, `Identify`, `State`, `Give`, `Draw`, `Convert`, `Show`, `Calculate`, `Suggest`, `Add`, `Outline`, `Define`, `Perform`, `Trace`. Never `Justify`, `Compare`, `Contrast`, `Discuss`, `Analyse`, `Assess`, `Evaluate`, `Predict`, `Summarise`, `Tick`. Definitions open with "State what is meant by" or "Describe what is meant by"; justifications with "Explain why". A Write flashcard is 3-4 marks (a statement, a query, an instruction); the 8-mark module is a worked example.
2. **Tariffs.** Use the slot’s. A point-marked answer carries exactly as many creditable points as its tariff, and its guidance says which.
3. **Answer shape.** At 3 marks and above a point is developed to earn its second mark; State and Identify want the bare item; Complete earns one mark per gap, row or statement; a worked example’s guidance lists its mark points, one per element. The marking guidance names every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type, using those words (C-16 matches whole words).
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct idea, and the test that tells them apart — the entry’s `test` field gives it. Never the correct definition repeated.
5. **Glossary.** `curriculum/glossary.json` settles every term’s sense. Use them exactly, everywhere.
6. **Scope.** The contract’s `excluded_constructs` are the limits the syllabus states and the A Level content it excludes, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or mention them, not even to say they are not required. `adjacent_topics` are not scanned: name one in passing, teach it in its own topic.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. The conditioned mechanisms in the subject profile carry their conditions wherever they appear (C-37). Never claim what examiners reward or what a paper contains: the words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).
8. **Self-containment.** A flashcard supplies its own scenario, data, code or table and never depends on another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit.
9. **Nothing is reproduced.** No Cambridge question, scenario, program, mark-scheme or examiner-report wording, anywhere. Every scenario, prompt, model answer and piece of guidance is yours.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.
11. **Pseudocode.** Cambridge pseudocode only, exactly as the Paper 2 insert defines it: DECLARE, CONSTANT, IF … THEN … ELSE … ENDIF, CASE OF … OTHERWISE … ENDCASE, FOR … TO … NEXT, WHILE … ENDWHILE, REPEAT … UNTIL, PROCEDURE … ENDPROCEDURE, FUNCTION … RETURNS … ENDFUNCTION, CALL, RETURN, INPUT, OUTPUT, OPENFILE … FOR READ/WRITE/APPEND, READFILE, WRITEFILE, CLOSEFILE, EOF(); the assignment arrow ←; & to join strings; only the insert’s built-in functions. Never a programming language (C-11 scans for Python, Java and Visual Basic syntax). Identifiers are never keywords, data types or function names.
12. **Complete, closed code.** Every model algorithm has its heading and ending, its declarations, its initialisation and every end statement. A function RETURNs its value; a module takes its values through its parameters.
13. **Fences and tables.** Code in a prompt or a note goes in a fence labelled ```pseudocode (```sql for SQL). There is no chart renderer, so no other fence: truth tables, trace tables and data are markdown tables, circuits are logic expressions or gate tables, flowcharts and structure charts are described box by box (C-41).
14. **Binary and hexadecimal.** Working shown, binary in groups of four bits, the result in the width asked. C-32 checks binary sums.
15. **Scenarios.** Every scenario card answers for its scenario, and its guidance says a generic answer earns nothing. No brand names.

## Voice

Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every technique (a conversion, a trace, a truth table, a construct, a module) is shown working on a small original example, step by step. Scenarios are Namibian and southern African where a scenario is used, with invented organisations; money in N$ where it appears. No hedging filler and no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/cie-9618-as-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-9618-as-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-9618-as-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-9618-as-2026 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-35, C-39, C-41 (unless the topic shows code) and C-43, and a C-18 warning (the per-topic AO mix is reported, not targeted), are expected. Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; a check compares them.

When all 29 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9618-as-2026
```

It publishes only topics whose checks pass and reports any topic it skipped.

## Boundaries

- Do not edit anything under `standard/`, or anything in `work/cie-9618-as-2026/curriculum/`.
- Do not touch any workspace other than `work/cie-9618-as-2026`, and do not edit `work/cie-9618-as-2026/exemplar/`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- anything in the plan that turned out to be wrong
