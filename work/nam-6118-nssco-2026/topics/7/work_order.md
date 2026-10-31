# Work order — 7 Mass, weight and density

*standard make_work_order.py plus planning/bind_task_specs.py (explicit task bindings; item counts unchanged)*

12 assessable objectives · 16 planned items · 2 content units

## Planned AO mix by item count (reported, not targeted)

| AO | planned | item-count target |
|---|---:|---:|
| A | 85% | 47% |
| B | 15% | 28% |
| C | 0% | 25% |

## Planned AO mix in marks-equivalent — the measure the syllabus uses

| AO | planned | syllabus weight |
|---|---:|---:|
| A | 47% | 47% |
| B | 23% | 28% |
| C | 30% | 25% |

54 marks-equivalent of practice in this topic.

> The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the one that answers "does this resource match the exam". It values each card at the tariff of the question it models, split across the AOs the card declares, and values each performance task at the marks of the paper part it models. The count-based mix below is reported only because it is what a reader expects to see; do not balance against it. AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a structural floor of about 92% in this topic (12 objectives against 13 slots) and cannot reach the None% target by count however many other cards are added - padding the bank to chase it makes the resource worse. The framework already measures the AO4 share in practice time rather than by count for the same reason. Treat AO1 above target as expected, and AO2/AO3/AO4 below target as the thing worth fixing.

## Content units

**CU-6118-2.5** — sub-topic 2.5, 7 objectives, 950–1499 words
- `OBJ-6118-2.5-01` tier 1 — define the mass of a body as a measure of the matter in it and that mass depends on the number of particles the body contains and the mass of those atoms
- `OBJ-6118-2.5-02` tier 1 — define inertia as the property of mass which 'resists' change in motion (Newton’s first law of motion)
- `OBJ-6118-2.5-03` tier 1 — define gravitational field strength (g) as the gravitational force or weight per unit mass
- `OBJ-6118-2.5-04` tier 1 — state that gravitational field strength (g) is equal to the gravitational acceleration (a)
- `OBJ-6118-2.5-05` tier 2 — describe qualitatively the motion of bodies falling in a uniform gravitational field with and without air resistance, including reference to terminal velocity
- `OBJ-6118-2.5-06` tier 2 — recall and use the equation weight = mass × gravitational field strength and know that near the Earth’s surface g is approximately 10 N/kg
- `OBJ-6118-2.5-07` tier 2 — determine the mass of an object from its weight (using a balance or a spring)

**CU-6118-2.6** — sub-topic 2.6, 5 objectives, 679–1070 words
- `OBJ-6118-2.6-01` tier 2 — Relate density to mass and volume using density = mass / volume.
- `OBJ-6118-2.6-02` tier 2 — describe an experiment to determine the density of a liquid and of a regularly shaped solid
- `OBJ-6118-2.6-03` tier 2 — describe the determination of the density of an irregularly shaped solid by the method of displacement
- `OBJ-6118-2.6-04` tier 1 — describe floating and sinking in terms of different densities
- `OBJ-6118-2.6-05` tier 2 — state that the density of water around 4  C is a maximum and explain how this is an advantage to aquatic life

## Item slots

| Slot | Objective | Subtype | AO | Command word | Tariff | Why |
|---|---|---|---|---|---:|---|
| `001-DEF` | define the mass of a body as a measure of the matter in it and that mass depends on the number of particles the body contains and the mass of those atoms | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `013-MISCON` | define the mass of a body as a measure of the matter in it and that mass depends on the number of particles the body contains and the mass of those atoms | MISCON | A | Explain | 2 | discriminates misconception MIS-06 (1 examiner statements): Mass is retained when gravitational field strength changes; weight is not. |
| `002-DEF` | define inertia as the property of mass which 'resists' change in motion (Newton’s first law of motion) | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `003-DEF` | define gravitational field strength (g) as the gravitational force or weight per unit mass | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `004-FEATURE` | state that gravitational field strength (g) is equal to the gravitational acceleration (a) | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `005-MECH` | describe qualitatively the motion of bodies falling in a uniform gravitational field with and without air resistance, including reference to terminal velocity | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `006-CALC` | recall and use the equation weight = mass × gravitational field strength and know that near the Earth’s surface g is approximately 10 N/kg | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `007-PROC` | determine the mass of an object from its weight (using a balance or a spring) | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `008-CALC` | Relate density to mass and volume using density = mass / volume. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `009-PROC` | describe an experiment to determine the density of a liquid and of a regularly shaped solid | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `010-PROC` | describe the determination of the density of an irregularly shaped solid by the method of displacement | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `011-FEATURE` | describe floating and sinking in terms of different densities | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `012-MECH` | state that the density of water around 4  C is a maximum and explain how this is an advantage to aquatic life | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |

## Performance tasks

- **multiple_choice_set** — Create 12 original four-option, one-mark MC questions for this topic. State each key and explain every distractor. Include both knowledge and application; the A/B split is a practice-design estimate, not an official code for individual items. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **short_answer** — An original eight-mark structured task: two one-mark knowledge parts, one two-mark definition/explanation and two two-mark applications or calculations. Use checked task architecture and topic-appropriate verbs; replace the structure if the topic is non-numerical and record the reason. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **practical_task** — An original 16-mark practical task in an in-scope physical context: construct a graph (5), derive and interpret its gradient (3), then plan an investigation (8). Provide realistic invented data with units, a complete operational method, controls, a results table and a data-based conclusion. Use the task-specific source anchors; do not label a reciprocal gradient as density or stiffness. This practices components, not a fixed complete Paper 3 question. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Mass and volume of a liquid after subtracting the container mass. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.

## Excluded from this topic

Limits the syllabus states, enforced by C-11 in everything a learner reads: Collision definitions (syllabus PDF 14; topic 2.4); Nuclide formulae in energy-source teaching (syllabus PDF 17; topic 2.10.1); Standalone diverging-lens theory (syllabus PDF 28; topic 4.3.3)
