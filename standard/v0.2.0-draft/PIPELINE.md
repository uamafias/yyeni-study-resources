# YYeni Study Resource Build Pipeline

**Version:** 0.1.0-draft

This pipeline operationalises `RUNTIME_STANDARD.md`. Each stage produces an artifact consumed by later stages. Agents may iterate backward when a review reveals a defect, but publication may occur only from the approved structured build.

## Build states

```text
UNINITIALISED
  -> INVENTORIED
  -> MAPPED
  -> PLANNED
  -> AUTHORED
  -> VALIDATED
  -> REVIEWED
  -> APPROVED
  -> PUBLISHED
  -> SUPERSEDED
```

A failed gate returns the build to the earliest affected stage.

## Stage 1 — Qualification-level planning

**Inputs:** official syllabus, syllabus updates, route information.  
**Actions:**

- identify board, qualification, subject, code, years, version, language, level, and route;
- parse all syllabus topics, optional routes, assessment objectives, papers, command words, and guided-learning information;
- distinguish core, optional, assumed, and excluded content.

**Outputs:** qualification profile and initial global syllabus tree.

## Stage 2 — Source ingestion and triage

**Inputs:** all files supplied for the qualification or topic.  
**Actions:**

- inventory file names, types, sizes, hashes, dates, and page counts;
- detect byte-identical and near-duplicate files;
- test text extraction, table extraction, formulas, diagrams, scans, and OCR need;
- classify source authority, likely syllabus version, level, topic coverage, and known defects;
- record copyright or reuse constraints.

**Output:** source inventory.

## Stage 3 — Global curriculum map

**Actions:**

- create stable IDs for every syllabus topic and atomic objective;
- build a global glossary of recurring terms;
- identify cross-topic concepts;
- create prerequisite and dependency relationships;
- represent optional routes and mutually exclusive choices;
- recommend a qualification-wide build sequence.

**Output:** objective registry and dependency graph.

## Stage 4 — Assessment-material mining

**Inputs:** specimen papers, past papers, mark schemes, candidate responses, examiner reports.  
**Actions:**

- map each relevant question to objective IDs;
- record paper, series, question part, command word, marks, AO focus, and context;
- extract credit-worthy reasoning and response characteristics;
- record examiner-evidenced misconceptions and common weaknesses;
- flag gaps where assessment materials are unavailable.

**Output:** assessment evidence map.

## Stage 5 — Topic contract

For the selected topic, declare:

- included objective IDs;
- excluded and deferred objective IDs;
- prerequisite concepts inherited from earlier topics;
- required outputs;
- target learner profile;
- assessment expectations;
- depth constraints;
- source and research permissions.

**Output:** topic contract in the build manifest.

## Stage 6 — Atomic objective refinement

For each selected syllabus bullet:

- split it into the smallest meaningful assessable objectives;
- classify objective type;
- assign relevant AOs and command words;
- confirm prerequisites and related concepts;
- preserve the exact syllabus wording alongside the learner-facing objective.

**Output:** topic objective subset.

## Stage 7 — Depth allocation

Assign each objective a depth tier:

| Tier | Typical use | Indicative learner-note depth |
|---|---|---:|
| 1 — Atomic | definition, feature, simple distinction | 100–300 words |
| 2 — Standard | ordinary concept, stage, or method | 300–700 words |
| 3 — Major | multi-part process, comparison, or impact | 700–1300 words |
| 4 — Synoptic | complex decision requiring application, analysis, and evaluation | 1000–1800 words |

Depth is calibrated using complexity, mark tariffs, assessment evidence, misconceptions, prerequisites, cross-topic importance, and calculation or performance demands. These are planning ranges, not quotas.

**Output:** depth plan.

## Stage 8 — Source adequacy audit

For every objective, assess source treatment on a 0–5 scale:

| Score | Meaning | Default action |
|---:|---|---|
| 0 | absent | generate-gap |
| 1 | mentioned only | regenerate |
| 2 | basic and incomplete | regenerate or synthesise |
| 3 | adequate for basic knowledge but weak for transfer | refine and expand |
| 4 | strong with limited gaps | retain and refine |
| 5 | master quality | retain meaning; standardise only |

Critical errors override the numerical score.

**Output:** source-to-objective evidence map and authoring action for every objective.

## Stage 9 — Gap and repair plan

Record:

- missing objectives;
- weak definitions;
- incomplete mechanisms or processes;
- missing application, analysis, or evaluation;
- formula and terminology issues;
- source conflicts;
- jurisdiction risks;
- out-of-scope content;
- required external verification;
- expected content-unit and learning-item outputs.

**Output:** repair plan.

## Stage 10 — Canonical claim authoring

Create atomic claims before prose drafting. Each claim receives:

- claim ID;
- objective ID;
- claim type;
- canonical wording;
- evidence links;
- provenance;
- confidence;
- verification state;
- publishability state.

No unsupported factual claim may be marked publishable.

**Output:** canonical claim ledger.

## Stage 11 — Learner content construction

Build content units from approved claims using the objective-type template. Include only components that serve the objective, such as:

- canonical definition and plain-language explanation;
- mechanism, process, or components;
- examples and non-examples;
- comparisons and boundaries;
- benefits, limitations, and stakeholder effects;
- formulas, worked examples, and interpretation;
- misconceptions and cross-topic links.

**Output:** structured content units.

## Stage 12 — Assessment layer

Using the qualification and subject profiles, add:

- meaningful application vignettes;
- analysis chains with defensible mechanisms;
- contextual evaluation and implementation conditions;
- command-word guidance;
- examination-calibrated questions and model structures;
- explicit links to examiner-evidenced weaknesses where available.

**Output:** assessment-ready content blocks.

## Stage 13 — Learning-item generation

Generate the item type appropriate to the objective:

- flashcards;
- short-answer questions;
- calculations;
- worked examples;
- data-response tasks;
- essay plans;
- practical tasks;
- source analysis;
- listening, speaking, or writing activities.

All items must map to approved objectives and claims.

**Output:** learning-item dataset.

## Stage 14 — Deterministic validation

Run schema and integrity tests for:

- valid file structure;
- unique IDs;
- objective coverage;
- reference integrity;
- evidence requirements;
- level and route boundaries;
- duplicate learning items;
- core/enrichment separation;
- metric accuracy;
- release-state consistency.

**Output:** deterministic QA report.

## Stage 15 — Independent semantic review

Provide the complete critic packet to separate reviewers for:

- curriculum and omission;
- factual accuracy and evidence;
- pedagogy and accessibility;
- assessment alignment;
- learning-item quality;
- subject-specific quality.

Critics must report evidence-bearing issues using the QA issue schema.

**Output:** semantic review reports.

## Stage 16 — Adjudication and repair

- verify critic counts and mechanical claims with code;
- resolve conflicts between reviewers;
- repair the earliest affected artifact;
- rerun downstream stages and tests;
- require human approval for unresolved high-risk claims.

**Output:** approved structured build or rejected build.

## Stage 17 — Publication assembly

Generate learner-facing and teacher-facing artifacts from the approved build:

- master notes;
- retrieval bank;
- practice materials;
- teacher coverage and provenance report;
- platform-ready exports;
- Word, PDF, HTML, JSON, or other required formats.

**Output:** release candidates.

## Stage 18 — Visual, technical, and release QA

- render and inspect documents;
- check heading hierarchy, tables, formulas, page breaks, clipping, navigation, and accessibility;
- compute word, section, claim, and learning-item counts from final artifacts;
- hash outputs;
- confirm output content matches the approved structured build;
- write the final build manifest and release decision.

**Output:** published release or blocked release.

## Minimum reviewer packet

A semantic critic must receive:

1. qualification profile;
2. subject profile;
3. topic contract;
4. objective registry and dependency graph;
5. source inventory;
6. source evidence and adequacy map;
7. gap and repair plan;
8. canonical claim ledger;
9. content units;
10. learning items;
11. exclusions log;
12. deterministic QA report.

A review of the final notes alone is not an omission audit.
