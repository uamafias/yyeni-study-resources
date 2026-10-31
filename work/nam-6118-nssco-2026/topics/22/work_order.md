# Work order — 22 Current, electromotive force and potential difference

*standard make_work_order.py plus planning/bind_task_specs.py (explicit task bindings; item counts unchanged)*

14 assessable objectives · 18 planned items · 2 content units

## Planned AO mix by item count (reported, not targeted)

| AO | planned | item-count target |
|---|---:|---:|
| A | 75% | 47% |
| B | 25% | 28% |
| C | 0% | 25% |

## Planned AO mix in marks-equivalent — the measure the syllabus uses

| AO | planned | syllabus weight |
|---|---:|---:|
| A | 48% | 47% |
| B | 26% | 28% |
| C | 27% | 25% |

60 marks-equivalent of practice in this topic.

> The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the one that answers "does this resource match the exam". It values each card at the tariff of the question it models, split across the AOs the card declares, and values each performance task at the marks of the paper part it models. The count-based mix below is reported only because it is what a reader expects to see; do not balance against it. AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a structural floor of about 88% in this topic (14 objectives against 16 slots) and cannot reach the None% target by count however many other cards are added - padding the bank to chase it makes the resource worse. The framework already measures the AO4 share in practice time rather than by count for the same reason. Treat AO1 above target as expected, and AO2/AO3/AO4 below target as the thing worth fixing.

## Content units

**CU-6118-5.2.1** — sub-topic 5.2.1, 7 objectives, 842–1347 words
- `OBJ-6118-5.2.1-01` tier 1 — state that a current is a flow of charge and that current is measured in amperes [A] using an ammeter
- `OBJ-6118-5.2.1-02` tier 2 — state and use the correct way to connect an ammeter
- `OBJ-6118-5.2.1-03` tier 2 — Use current I = charge Q / time t.
- `OBJ-6118-5.2.1-04` tier 2 — distinguish between static electricity and current electricity
- `OBJ-6118-5.2.1-05` tier 4 — explain and distinguish between - alternating current (a.c) and direct current (d.c) - the direction of the electron flow and the direction of the conventional current
- `OBJ-6118-5.2.1-05-M01` tier 2 — Distinguish alternating and direct current
- `OBJ-6118-5.2.1-05-M02` tier 2 — Distinguish electron flow and conventional current

**CU-6118-5.2.2** — sub-topic 5.2.2, 7 objectives, 842–1347 words
- `OBJ-6118-5.2.2-01` tier 1 — state that electromotive force (e.m.f) is measured by the energy dissipated (supplied) by a source in driving unit charge round a complete circuit
- `OBJ-6118-5.2.2-02` tier 2 — Use electromotive force = source energy transferred per charge, V = E/Q.
- `OBJ-6118-5.2.2-03` tier 2 — Use potential difference = component work per charge, V = W/Q.
- `OBJ-6118-5.2.2-04` tier 1 — state that both e.m.f and p.d across a circuit component are measured in volts [V]
- `OBJ-6118-5.2.2-05` tier 2 — state the correct way to connect a voltmeter
- `OBJ-6118-5.2.2-06` tier 1 — state that the potential difference between the terminals of a cell enables current to flow around a circuit
- `OBJ-6118-5.2.2-07` tier 2 — state the difference between e.m.f. as the total energy per charge and p.d as the work per charge in a part of the circuit and that the e.m.f. and p.d. involve different energy changes

## Item slots

| Slot | Objective | Subtype | AO | Command word | Tariff | Why |
|---|---|---|---|---|---:|---|
| `001-FEATURE` | state that a current is a flow of charge and that current is measured in amperes [A] using an ammeter | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `002-PROC` | state and use the correct way to connect an ammeter | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `003-CALC` | Use current I = charge Q / time t. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `004-DIST` | distinguish between static electricity and current electricity | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |
| `005-SYNTH` | explain and distinguish between - alternating current (a.c) and direct current (d.c) - the direction of the electron flow and the direction of the conventional current | SYNTH | A/B | Explain | 2 | instructs with Explain, which this objective carries |
| `006-DIST` | Distinguish alternating and direct current | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |
| `007-DIST` | Distinguish electron flow and conventional current | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |
| `008-DEF` | state that electromotive force (e.m.f) is measured by the energy dissipated (supplied) by a source in driving unit charge round a complete circuit | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `009-CALC` | Use electromotive force = source energy transferred per charge, V = E/Q. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `010-CALC` | Use potential difference = component work per charge, V = W/Q. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `015-MISCON` | Use potential difference = component work per charge, V = W/Q. | MISCON | A | Explain | 2 | discriminates misconception MIS-19 (1 examiner statements): Work per charge is potential difference; work per time is power. |
| `011-FEATURE` | state that both e.m.f and p.d across a circuit component are measured in volts [V] | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `012-PROC` | state the correct way to connect a voltmeter | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `013-FEATURE` | state that the potential difference between the terminals of a cell enables current to flow around a circuit | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `014-DIST` | state the difference between e.m.f. as the total energy per charge and p.d as the work per charge in a part of the circuit and that the e.m.f. and p.d. involve different energy changes | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |

## Performance tasks

- **multiple_choice_set** — Create 12 original four-option, one-mark MC questions for this topic. State each key and explain every distractor. Include both knowledge and application; the A/B split is a practice-design estimate, not an official code for individual items. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **short_answer** — An original eight-mark structured task: two one-mark knowledge parts, one two-mark definition/explanation and two two-mark applications or calculations. Use checked task architecture and topic-appropriate verbs; replace the structure if the topic is non-numerical and record the reason. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **practical_task** — An original 16-mark practical task in an in-scope physical context: construct a graph (5), derive and interpret its gradient (3), then plan an investigation (8). Provide realistic invented data with units, a complete operational method, controls, a results table and a data-based conclusion. Use the task-specific source anchors; do not label a reciprocal gradient as density or stiffness. This practices components, not a fixed complete Paper 3 question. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Measuring open-circuit voltage from identical cells in series. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.

## Excluded from this topic

Limits the syllabus states, enforced by C-11 in everything a learner reads: Collision definitions (syllabus PDF 14; topic 2.4); Nuclide formulae in energy-source teaching (syllabus PDF 17; topic 2.10.1); Standalone diverging-lens theory (syllabus PDF 28; topic 4.3.3)
