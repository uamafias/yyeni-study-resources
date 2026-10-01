# Cambridge International AS Level English Language 9093 (syllabus v2, examined 2024-2026)

Study notes and flashcards. 11 topics, 417 flashcards and performance tasks, 20,637 words of notes.

Every topic here passes the full deterministic check suite. Semantic review runs on published material rather than ahead of it, so the **Open issues** column is debt that ships visibly and is cleared in a maintenance pass - it is not a warning that the topic is unusable.


## Paper 1 Reading

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **1.1** Form, audience, purpose and context | [1.1-form-audience-purpose-and-context.md](notes/1.1-form-audience-purpose-and-context.md) | [1.1-form-audience-purpose-and-context-flashcards.json](flashcards/1.1-form-audience-purpose-and-context-flashcards.json) | 39 | 1,857 | — |
| **1.2** Linguistic elements and literary features | [1.2-linguistic-elements-and-literary-features.md](notes/1.2-linguistic-elements-and-literary-features.md) | [1.2-linguistic-elements-and-literary-features-flashcards.json](flashcards/1.2-linguistic-elements-and-literary-features-flashcards.json) | 75 | 2,808 | — |
| **1.3** Evidence and analytical writing | [1.3-evidence-and-analytical-writing.md](notes/1.3-evidence-and-analytical-writing.md) | [1.3-evidence-and-analytical-writing-flashcards.json](flashcards/1.3-evidence-and-analytical-writing-flashcards.json) | 27 | 1,547 | — |
| **1.4** Directed response and comparison | [1.4-directed-response-and-comparison.md](notes/1.4-directed-response-and-comparison.md) | [1.4-directed-response-and-comparison-flashcards.json](flashcards/1.4-directed-response-and-comparison-flashcards.json) | 58 | 2,465 | — |
| **1.5** Text analysis | [1.5-text-analysis.md](notes/1.5-text-analysis.md) | [1.5-text-analysis-flashcards.json](flashcards/1.5-text-analysis-flashcards.json) | 40 | 2,286 | — |

## Paper 2 Writing

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **2.1** Shorter writing and reflective commentary | [2.1-shorter-writing-and-reflective-commentary.md](notes/2.1-shorter-writing-and-reflective-commentary.md) | [2.1-shorter-writing-and-reflective-commentary-flashcards.json](flashcards/2.1-shorter-writing-and-reflective-commentary-flashcards.json) | 49 | 2,358 | — |
| **2.2** Structuring longer writing | [2.2-structuring-longer-writing.md](notes/2.2-structuring-longer-writing.md) | [2.2-structuring-longer-writing-flashcards.json](flashcards/2.2-structuring-longer-writing-flashcards.json) | 27 | 1,712 | — |
| **2.3** Imaginative and descriptive writing | [2.3-imaginative-and-descriptive-writing.md](notes/2.3-imaginative-and-descriptive-writing.md) | [2.3-imaginative-and-descriptive-writing-flashcards.json](flashcards/2.3-imaginative-and-descriptive-writing-flashcards.json) | 30 | 1,647 | — |
| **2.4** Discursive and argumentative writing | [2.4-discursive-and-argumentative-writing.md](notes/2.4-discursive-and-argumentative-writing.md) | [2.4-discursive-and-argumentative-writing-flashcards.json](flashcards/2.4-discursive-and-argumentative-writing-flashcards.json) | 25 | 1,384 | — |
| **2.5** Review and critical writing | [2.5-review-and-critical-writing.md](notes/2.5-review-and-critical-writing.md) | [2.5-review-and-critical-writing-flashcards.json](flashcards/2.5-review-and-critical-writing-flashcards.json) | 20 | 1,316 | — |
| **2.6** Expression, range and accuracy | [2.6-expression-range-and-accuracy.md](notes/2.6-expression-range-and-accuracy.md) | [2.6-expression-range-and-accuracy-flashcards.json](flashcards/2.6-expression-range-and-accuracy-flashcards.json) | 27 | 1,257 | — |

## What is in a flashcard file

One JSON file per topic, carrying `topic_number`, `topic_title` and a list of `items`. Each item has:

- `prompt` — what the learner sees
- `canonical_answer` — the model answer
- `marking_guidance` — what earns credit, part by part
- `subtype` — DEF, DIST, APP, CHAIN, EVAL, CALC and so on, or a performance task
- `assessment_objectives` — what the examination credits, and `difficulty` 1 to 5
- `blooms_level` — what the learner is being asked to do: Remember, Understand, Apply, Analyse, Evaluate or Create. A different axis from the assessment objective, and on every item
- `objective_ids` **and `objective_titles`** — what the card teaches, by code and in words
- `claim_ids` — the claims in the topic ledger the answer rests on

## Where the source lives

This folder is the copy to upload. The source of record is `work/cie-9093-as-2024-2026/topics/<number>/`, which holds each topic's claim ledger, content units, learning items and QA report. Regenerate this folder at any time with `build/publish_subject.py`; nothing in it is edited by hand.
