# Handover prompt — Cambridge IGCSE Geography 0460

Paste everything below the line into Hermes Agent or OpenCode with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Cambridge IGCSE Geography, syllabus code 0460** (syllabus for 2025 and 2026, Alternative to Coursework route). The learners are Namibian secondary students, English medium, sitting Papers 12, 22 and 42 in the October/November 2026 series; the first 0460 paper is on 2026-10-14. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` (repo root) — which role brief applies. You are the AUTHOR.
2. `work/cie-0460-igcse-2025-2026/PLAN-0460-igcse-geography.md` — **the plan. This is your brief.** Read all of it.
3. `work/cie-0460-igcse-2025-2026/subject-profile.yaml` — the answer parts your marking guidance must name for each card subtype and task type, the conditioned mechanisms, the variant register, the prohibited patterns, and the depiction rule.
4. `work/cie-0460-igcse-2025-2026/curriculum/answer-shapes.json` — how each command word and tariff is marked.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — written for business subjects. Where it conflicts with this handover, this handover wins for 0460: money appears only where a situation involves it (N$), and "never say what a paper contains" means never claim frequencies or what examiners do. The syllabus’s own statements about a paper (its sections, the mapwork question, the Paper 4 criteria) are allowed.

Everything is derived already. `work/cie-0460-igcse-2025-2026/curriculum/syllabus-facts.json` records where each assessment value came from, with the syllabus page and the verbatim line. Do not re-derive them, do not re-read the syllabus PDF, and do not open any other subject’s workspace.

## The job

**21 topics, 629 items (577 flashcards, 52 performance tasks), 39,020–55,870 words of notes.** Work through the topics in this order and take the whole subject in one run. Do not stop after a topic to ask what is next.

```
  1.1   Population dynamics
  1.2   Migration
  1.3   Population structure
  1.4   Population density and distribution
  1.5   Settlements (rural and urban) and service provision
  1.6   Urban settlements
  1.7   Urbanisation
  2.1   Earthquakes and volcanoes
  2.2   Rivers
  2.3   Coasts
  2.4   Weather
  2.5   Climate and natural vegetation
  3.1   Development
  3.2   Food production
  3.3   Industry
  3.4   Tourism
  3.5   Energy
  3.6   Water
  3.7   Environmental risks of economic development
  4     Geographical skills
  5     Geographical enquiry
```

Topics 1.1-3.7 are the three themes (Paper 1); topic 4 is the geographical skills (Paper 2) and topic 5 the fieldwork enquiry (Paper 4). Work in the order listed: topics 4 and 5 draw their resources and settings from the themes, so write them last.

For each topic `<T>`, read `work/cie-0460-igcse-2025-2026/topics/<T>/contract.json` (scope, budgets, exclusions) and `work/cie-0460-igcse-2025-2026/topics/<T>/work_order.json` (every slot, pre-decided; `work_order.md` is the same plan as a table). Then produce, in `work/cie-0460-igcse-2025-2026/topics/<T>/`:

1. `claims/canonical_claim_ledger.json` — every statement the topic teaches, each mapped to the objectives it serves. 2–4 claims per objective.
2. `content-units/CU-0460-<sub-topic>.json` — one unit per sub-topic in the work order, prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json` — one item per slot, flashcards and performance tasks.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `work/cie-0460-igcse-2025-2026/exemplar/` holds two small slices, 2.2 Rivers (a theme topic with its case study and a 7-mark levels-marked task) and 4 Geographical skills (mapwork from a map extract given as a markdown grid), that pass every check. Copy their **shape** — the field set of every claim, block and item, resources as markdown tables or described scenes, the level descriptors in a case-study task’s guidance, a scale calculation written as "a × b = c", `claims_seen` and `authored_hash`. Do not copy their volume or their content, and do not reuse their scenarios in those topics.

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

1. **Command words.** Only these open a prompt: `Describe`, `Explain`, `Suggest`, `Identify`, `Complete`, `Give`, `Compare`, `State`, `Name`, `Calculate`, `Define`, `Estimate`, `Justify`. Never `Devise`, `Predict`, `Sketch`, `Locate`, `Plan`, `Tick`, `Circle`, `Plot`, `Draw`, `Measure`. Definitions open with "State what is meant by"; resource questions with Describe, Identify or Suggest; explanations with Explain. Response formats (Tick, Circle, Put in order, Choose) and marks on a resource (Plot, Draw, Measure) appear only as steps inside a data_response or practical_task item.
2. **Tariffs.** Use the slot’s. A point-marked answer carries exactly as many creditable points as its tariff, and its guidance says which.
3. **Answer shape.** Point-marked: one mark per idea, from a longer list; at 4-5 marks an idea is developed to earn its second mark. A case-study task is marked by levels, and Level 3 needs a named example and place-specific detail. A Paper 4 conclusion states the decision, then paired figures. The marking guidance names every part `subject-profile.yaml -> answer_structures` declares for the subtype or task type, using those words (C-16 matches whole words).
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct idea, and the test that tells them apart — the entry’s `test` field gives it. Never the correct definition repeated.
5. **Glossary.** `curriculum/glossary.json` settles every term’s sense. Use them exactly, everywhere.
6. **Scope.** The contract’s `excluded_constructs` are the limits the syllabus states and the A Level content it excludes, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or mention them, not even to say they are not required. `adjacent_topics` are not scanned: name one in passing, teach it in its own topic.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. The conditioned mechanisms in the subject profile carry their conditions wherever they appear (C-37). Never claim what examiners reward or what a paper contains: the words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).
8. **Self-containment.** A flashcard supplies its own scenario, data, resource or table and never depends on another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit.
9. **Nothing is reproduced.** No Cambridge question, scenario, program, mark-scheme or examiner-report wording, anywhere. Every scenario, prompt, model answer and piece of guidance is yours.
10. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.
11. **Case studies.** Each case-study objective (`…-x.y.2-NN`) is taught in its own content unit (`CU-0460-x.y.2`) with a named real place at the right scale and place-specific detail: named districts, schemes, dates, rounded figures with their year. Use only facts you are confident of. Where the syllabus asks for one country and another of a contrasting kind (over-populated and under-populated, high and low growth), give both.
12. **Case-study tasks.** `item_type: "case_analysis"`, `mark_tariff: 7`. One precise question on the case study, a model answer of about 150-200 words with a named place and place-specific detail, and guidance that gives the three levels (C-16 looks for "level", "named" and "developed").
13. **Resources.** A map extract is a markdown table of grid squares with a stated scale (1:25 000 or 1:50 000); a graph is its data table; a photograph is a described scene. The learner plots and draws on their own paper. No code fences (C-41).
14. **Mapwork.** Eastings before northings; six-figure references with the tenths; compass directions as points, bearings as degrees clockwise from grid north; distances along the route with the scale (1:50 000: 1 cm is 0.5 km). Write each conversion as "a × b = c" so C-32 checks it.
15. **Paper 4 enquiries.** `item_type: "practical_task"`, about 30 marks, parts numbered with their marks. Give the students’ results in a markdown table with headings and units; they are ours, realistic and consistent. Each conclusion part states the decision and gives paired figures; each evaluation names the change and why it makes the results more reliable.
16. **Performance-task labels.** A performance slot gives its `item_type`, brief and Bloom level. Set `assessment_objectives` to the AOs its brief’s `ao_split` names in `subject-profile.yaml`, `mark_tariff` to the marks the brief states, and `command_word` to the word that opens its first part.

## Voice

Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text, and a standalone learning text at once. Every process is explained step by step, every landform described and then its formation explained, every case study written out with place detail. Namibian and southern African examples where they fit (the Kuiseb and the Namib, Windhoek’s growth, the Orange River, Etosha), with invented names for people; money in N$ where it appears. No hedging filler and no bullet-point soup where prose teaches better.

## The work order is a baseline, not a cage

Where a slot does not fit its objective, change it and record the change in `work/cie-0460-igcse-2025-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where an exposure-required subtype genuinely does not fit, add an entry to the contract’s `subtype_waivers` with a reason of at least twelve words rather than padding the bank.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0460-igcse-2025-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0460-igcse-2025-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0460-igcse-2025-2026 <T>
```

`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. Fix every **FAIL**. `not_run` on C-35, C-39, C-41 and C-43, and a C-18 warning (the per-topic AO mix is reported, not targeted), are expected. Set the contract’s `required_outputs.learning_items` and `required_outputs.content_units` to what you actually produced; a check compares them.

When all 21 topics are clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0460-igcse-2025-2026
```

It publishes only topics whose checks pass and reports any topic it skipped.

## Boundaries

- Do not edit anything under `standard/`, or anything in `work/cie-0460-igcse-2025-2026/curriculum/`.
- Do not touch any workspace other than `work/cie-0460-igcse-2025-2026`, and do not edit `work/cie-0460-igcse-2025-2026/exemplar/`.
- Do not regenerate contracts or work orders; they are the plan you are working to.
- There is no review round. The deterministic suite is the gate.

## Report back when the subject is finished

Under 250 words:

- topics completed, and any not completed with the reason
- totals: claims, content units, items, notes words
- the final check line per topic, or a single line if all read `PUBLISH`
- every call you made rather than derived, and every deviation from a work order and why
- anything in the plan that turned out to be wrong
