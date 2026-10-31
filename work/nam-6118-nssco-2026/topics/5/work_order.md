# Work order — 5 Position, speed and acceleration

*standard make_work_order.py plus planning/bind_task_specs.py (explicit task bindings; item counts unchanged)*

20 assessable objectives · 26 planned items · 3 content units

## Planned AO mix by item count (reported, not targeted)

| AO | planned | item-count target |
|---|---:|---:|
| A | 65% | 47% |
| B | 35% | 28% |
| C | 0% | 25% |

## Planned AO mix in marks-equivalent — the measure the syllabus uses

| AO | planned | syllabus weight |
|---|---:|---:|
| A | 45% | 47% |
| B | 34% | 28% |
| C | 22% | 25% |

73 marks-equivalent of practice in this topic.

> The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the one that answers "does this resource match the exam". It values each card at the tariff of the question it models, split across the AOs the card declares, and values each performance task at the marks of the paper part it models. The count-based mix below is reported only because it is what a reader expects to see; do not balance against it. AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a structural floor of about 87% in this topic (20 objectives against 23 slots) and cannot reach the None% target by count however many other cards are added - padding the bank to chase it makes the resource worse. The framework already measures the AO4 share in practice time rather than by count for the same reason. Treat AO1 above target as expected, and AO2/AO3/AO4 below target as the thing worth fixing.

## Content units

**CU-6118-2.3.1** — sub-topic 2.3.1, 4 objectives, 528–852 words
- `OBJ-6118-2.3.1-01` tier 1 — recognise and state that the concepts ‘position’ and ‘reference point’ (can be represented as x, y or z) are fundamental in the study of speed, velocity and acceleration
- `OBJ-6118-2.3.1-02` tier 1 — recognise that position, relative to a reference point, can be either positive or negative
- `OBJ-6118-2.3.1-03` tier 1 — define distance as a measure of how far an object travels along a particular path (without considering direction)
- `OBJ-6118-2.3.1-04` tier 1 — define displacement as a vector which has a magnitude equal to the shortest distance between the initial and final points and a direction from the initial to the final point

**CU-6118-2.3.2** — sub-topic 2.3.2, 9 objectives, 1188–1917 words
- `OBJ-6118-2.3.2-01` tier 1 — define speed as a rate of change of distance
- `OBJ-6118-2.3.2-02` tier 1 — define instantaneous velocity as a ‘rate of change of displacement’ or speed in a given direction
- `OBJ-6118-2.3.2-03` tier 1 — Define average velocity as total displacement divided by total elapsed time.
- `OBJ-6118-2.3.2-04` tier 2 — explain what positive and negative values of velocity mean
- `OBJ-6118-2.3.2-05` tier 2 — Use average speed = total distance / total time, and speed = distance / time.
- `OBJ-6118-2.3.2-06` tier 2 — plot readings for and interpret a distance-time graph
- `OBJ-6118-2.3.2-07` tier 2 — plot readings for and interpret a speed-time graph
- `OBJ-6118-2.3.2-08` tier 2 — identify from the shape of a distance-time or speed-time graph when a body is - at rest - moving with constant speed - moving with changing speed
- `OBJ-6118-2.3.2-09` tier 2 — distinguish between speed and velocity by means of similarities and differences

**CU-6118-2.3.3** — sub-topic 2.3.3, 7 objectives, 923–1491 words
- `OBJ-6118-2.3.3-01` tier 1 — define acceleration as the rate of change of velocity
- `OBJ-6118-2.3.3-02` tier 2 — explain what positive and negative values of acceleration mean
- `OBJ-6118-2.3.3-03` tier 2 — identify linear motion for which the acceleration is constant and calculate the acceleration
- `OBJ-6118-2.3.3-04` tier 2 — identify motion for which the acceleration is not constant
- `OBJ-6118-2.3.3-05` tier 2 — calculate the area under a speed-time graph to determine the distance travelled for motion with constant acceleration
- `OBJ-6118-2.3.3-06` tier 1 — state that the acceleration of free fall for a body near the Earth’s surface is constant and has a value of approximately 10 m/s 2
- `OBJ-6118-2.3.3-07` tier 2 — Use the constant-acceleration equations v = u + at, s = ut + ½at², v² = u² + 2as, a = (v − u)/t and s = (u + v)t/2.

## Item slots

| Slot | Objective | Subtype | AO | Command word | Tariff | Why |
|---|---|---|---|---|---:|---|
| `001-FEATURE` | recognise and state that the concepts ‘position’ and ‘reference point’ (can be represented as x, y or z) are fundamental in the study of speed, velocity and acceleration | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `002-FEATURE` | recognise that position, relative to a reference point, can be either positive or negative | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `003-DEF` | define distance as a measure of how far an object travels along a particular path (without considering direction) | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `004-DEF` | define displacement as a vector which has a magnitude equal to the shortest distance between the initial and final points and a direction from the initial to the final point | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `005-DEF` | define speed as a rate of change of distance | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `006-DEF` | define instantaneous velocity as a ‘rate of change of displacement’ or speed in a given direction | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `007-DEF` | Define average velocity as total displacement divided by total elapsed time. | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `008-MECH` | explain what positive and negative values of velocity mean | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `009-CALC` | Use average speed = total distance / total time, and speed = distance / time. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `023-MISCON` | Use average speed = total distance / total time, and speed = distance / time. | MISCON | A | Explain | 2 | discriminates misconception MIS-03 (1 examiner statements): Average speed is total distance divided by total elapsed time, not an unweighted average of speeds. |
| `010-INTERP` | plot readings for and interpret a distance-time graph | INTERP | B | Draw | 2 | instructs with Draw, which this objective carries |
| `011-INTERP` | plot readings for and interpret a speed-time graph | INTERP | B | Draw | 2 | instructs with Draw, which this objective carries |
| `012-INTERP` | identify from the shape of a distance-time or speed-time graph when a body is - at rest - moving with constant speed - moving with changing speed | INTERP | B | Draw | 2 | instructs with Draw, which this objective carries |
| `021-MISCON` | identify from the shape of a distance-time or speed-time graph when a body is - at rest - moving with constant speed - moving with changing speed | MISCON | A | Explain | 2 | discriminates misconception MIS-01 (1 examiner statements): A horizontal speed-time segment means constant speed; it does not mean the object is at rest as a horizontal distance-time segment does. |
| `013-DIST` | distinguish between speed and velocity by means of similarities and differences | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |
| `014-DEF` | define acceleration as the rate of change of velocity | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `015-MECH` | explain what positive and negative values of acceleration mean | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `016-CALC` | identify linear motion for which the acceleration is constant and calculate the acceleration | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `017-INTERP` | identify motion for which the acceleration is not constant | INTERP | B | Draw | 2 | instructs with Draw, which this objective carries |
| `018-CALC` | calculate the area under a speed-time graph to determine the distance travelled for motion with constant acceleration | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `022-MISCON` | calculate the area under a speed-time graph to determine the distance travelled for motion with constant acceleration | MISCON | A | Explain | 2 | discriminates misconception MIS-02 (1 examiner statements): Distance comes from speed-time area; acceleration comes from gradient. |
| `019-FEATURE` | state that the acceleration of free fall for a body near the Earth’s surface is constant and has a value of approximately 10 m/s 2 | FEATURE | A | State | 1 | instructs with State, which this objective carries |
| `020-CALC` | Use the constant-acceleration equations v = u + at, s = ut + ½at², v² = u² + 2as, a = (v − u)/t and s = (u + v)t/2. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |

## Performance tasks

- **multiple_choice_set** — Create 12 original four-option, one-mark MC questions for this topic. State each key and explain every distractor. Include both knowledge and application; the A/B split is a practice-design estimate, not an official code for individual items. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **short_answer** — An original eight-mark structured task: two one-mark knowledge parts, one two-mark definition/explanation and two two-mark applications or calculations. Use checked task architecture and topic-appropriate verbs; replace the structure if the topic is non-numerical and record the reason. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **practical_task** — An original 16-mark practical task in an in-scope physical context: construct a graph (5), derive and interpret its gradient (3), then plan an investigation (8). Provide realistic invented data with units, a complete operational method, controls, a results table and a data-based conclusion. Use the task-specific source anchors; do not label a reciprocal gradient as density or stiffness. This practices components, not a fixed complete Paper 3 question. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Uniformly accelerating model vehicle. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.

## Excluded from this topic

Limits the syllabus states, enforced by C-11 in everything a learner reads: Collision definitions (syllabus PDF 14; topic 2.4); Nuclide formulae in energy-source teaching (syllabus PDF 17; topic 2.10.1); Standalone diverging-lens theory (syllabus PDF 28; topic 4.3.3)
