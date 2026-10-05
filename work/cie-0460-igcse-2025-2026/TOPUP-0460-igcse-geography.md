# Top-up — Cambridge IGCSE Geography 0460 (1 October 2026)

The subject is authored and published: 21 topics, all PUBLISH. This run does two things and nothing else.

## 1. Bring the topic 4 and topic 5 notes up to their word budgets

Six content units sit under the minimum their work order sets (check C-26 warns on them):

| unit | now | minimum | add about |
|---|---:|---:|---:|
| CU-0460-4.1 Mapwork: the skills of the extract | 1,848 | 4,555 | 2,700 |
| CU-0460-4.2 Data skills: graphs, tables and patterns | 588 | 1,993 | 1,400 |
| CU-0460-4.3 Photographs, images and combined resources | 358 | 854 | 500 |
| CU-0460-4.4 The arithmetic of geography | 918 | 2,847 | 1,950 |
| CU-0460-5.2 Collecting the data: questionnaires, counts and measurements | 1,808 | 2,850 | 1,050 |
| CU-0460-5.5 Conclusions, evaluation and extensions | 664 | 950 | 300 |

Each unit must end **inside** its `word_budget` (between min and max), so C-26 passes.

**What the added words are for.** Teaching, not padding. For every objective in the unit, make sure the notes have: a plain explanation of the skill; at least one worked demonstration on a short original resource written into the block (a described map extract as a small grid table, a data table, a described photograph); the common error stated as a discrimination (error, correct move, test) where the topic's misconception register has one; and how the skill is set and marked in its paper, using only what the syllabus says. Topic 4 is Paper 2 (map, graph and resource skills); topic 5 is Paper 4 (fieldwork enquiry).

- Add new blocks, or extend existing ones. Every new statement that teaches something is a claim in the topic's ledger and cited by the block; add claims as needed, each mapped to the objectives it serves.
- Do not change any learning item in topics 4 and 5, and do not change any other unit.
- New blocks need `claims_seen`, `authored_hash` and `qa_status: "review_required"`, as before. An extended block gets a new `authored_hash`, its old one recorded as `prior_hash`, and its `claims_seen` advanced.

## 2. Rewrite two card prompts in topic 2.5 that reuse Cambridge wording

`ITEM-0460-2.5-014-FEATURE` and `ITEM-0460-2.5-015-APP` open with a stock Cambridge case-study question stem ("For an area of tropical rainforest you have studied, ..."). Rewrite both prompts in your own words, keeping what each asks, its command word, tariff and labels. Update the answer or guidance only if the new prompt needs it, then re-stamp the item (new `authored_hash`, old one as `prior_hash`). Record both changes in `topics/2.5/authoring_notes.json`.

## Rules

Everything in `work/cie-0460-igcse-2025-2026/HANDOVER-0460-igcse-geography.md` still applies: no Cambridge question, insert, mark-scheme or examiner-report wording; British English; scope terms; filenames derived, never chosen. Read the handover's rules section before writing. Write only inside `work/cie-0460-igcse-2025-2026/topics/`. Do not commit or push.

## Finish

For topics 4, 5 and 2.5:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0460-igcse-2025-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0460-igcse-2025-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0460-igcse-2025-2026 <T>
```

Loop until each reads PUBLISH with no C-26 warning, then republish:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0460-igcse-2025-2026
```

Report in under 150 words: each unit's new word count, the two rewritten prompts, the final check line per topic, and anything you changed beyond this brief and why.
