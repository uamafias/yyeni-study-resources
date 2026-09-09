# YYeni Independent Semantic Review Protocol

Use this protocol only after deterministic validation has produced a report. The reviewer must operate in a fresh context and must receive the complete review packet listed below.

## Required review packet

1. qualification profile;
2. subject profile;
3. topic contract and build manifest;
4. complete objective registry and dependency graph;
5. source inventory;
6. source-to-objective evidence and adequacy map;
7. gap and repair plan;
8. canonical claim ledger;
9. content units;
10. learning-item dataset;
11. exclusions and conflict-resolution log;
12. deterministic QA report.

Do not review the learner document alone. A reviewer cannot reliably detect omissions without the original objective map.

## Reviewer roles

Run the following reviews separately where possible.

### 1. Curriculum and omission reviewer

Check:

- correct board, version, level, route, and topic scope;
- every mandatory objective has adequate content and a suitable learning item;
- no objective is covered only nominally;
- no out-of-level or optional content appears as core;
- prerequisites and cross-topic terms are handled consistently;
- relevant supplied material was not dropped without a recorded reason.

### 2. Accuracy and evidence reviewer

Check:

- definitions, classifications, formulas, dates, and factual relationships;
- whether source claims are represented fairly;
- whether generated claims have adequate verification;
- whether analytical inferences follow from verified premises;
- whether legal and jurisdictional claims are appropriately qualified;
- whether contradictions are resolved correctly.

### 3. Pedagogy and accessibility reviewer

Check:

- clarity for the intended learner;
- conceptual progression and prerequisite order;
- whether mechanisms are explained rather than merely listed;
- whether distinctions and misconceptions are taught explicitly;
- proportionality and cognitive load;
- examples, non-examples, diagrams, and worked steps;
- whether the learner could reconstruct the knowledge without the source notes.

### 4. Assessment reviewer

Check:

- alignment to assessment objectives and command words;
- use of past-paper, mark-scheme, and examiner-report evidence where available;
- genuine contextual application;
- causal validity of analysis chains;
- decisiveness and contextual relevance of evaluation;
- accuracy and interpretation of quantitative work;
- whether practice matches paper formats and mark tariffs.

### 5. Learning-item reviewer

Check:

- objective and claim mapping;
- atomicity and self-containment;
- answer completeness;
- prompt ambiguity or answer leakage;
- semantic duplication;
- progression from recall to transfer;
- balance of flashcards and performance tasks;
- one consistent item architecture across the topic.

## Bidirectional audit

Perform both checks:

1. **Objective to content:** For every objective, identify exactly where it is adequately taught and practised.
2. **Content to objective:** For every substantial block, identify the objective, prerequisite, or approved enrichment reason that justifies inclusion.

## Reconstruction test

Using only the generated resource, attempt a representative sample of:

- definitions and distinctions;
- explanation questions;
- unfamiliar case applications;
- analysis questions;
- evaluation questions;
- calculations and interpretations;
- relevant past-paper questions.

Report any objective for which the resource does not contain enough knowledge or reasoning support to construct a strong answer.

## Required issue format

Every issue must be evidence-bearing:

```yaml
issue_id: unique-id
severity: critical | high | medium | low
category: curriculum | accuracy | evidence | pedagogy | application | analysis | evaluation | quantitative | learning-item | coherence | publishing
affected_ids:
  - objective-or-claim-or-item-id
finding: precise description of the defect
evidence:
  - exact source, block, claim, card, or page reference
educational_consequence: how the defect could affect learner understanding or assessment performance
recommended_repair: specific corrective action
confidence: 0.0-1.0
status: open
```

Do not report unsupported impressions such as “this feels weak.” Identify the exact defect and evidence.

## Severity guidance

- **Critical:** wrong syllabus scope, dangerous misinformation, materially wrong definition or formula, missing compulsory topic, or unsupported factual claim that changes learner understanding.
- **High:** major omission, invalid causal reasoning, misleading evaluation, or systematic application failure.
- **Medium:** limited example range, structural inconsistency, incomplete comparison, or repeated learning items.
- **Low:** wording, formatting, minor sequencing, or non-blocking clarity issue.

## Review decision

- **Pass:** no open critical, high, or medium issues; low issues are resolved or explicitly accepted.
- **Conditional pass:** only clearly bounded issues remain and publication is still blocked until they are resolved.
- **Reject:** any critical issue, unresolved high issue, systematic failure, or inability to verify coverage.

Mechanical counts, hashes, duplicate detections, and schema claims must be confirmed by code rather than accepted solely from the reviewer.
