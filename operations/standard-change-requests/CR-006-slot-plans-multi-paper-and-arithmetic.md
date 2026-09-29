# CR-006 — Subject slot plans, multi-paper topics, and arithmetic the checks could not read

Status: applied to `standard/v0.2.0-draft`, 29 September 2026.

## Why

Four subjects planned in one pass (9618, 9702, 0460, 9093) broke three assumptions the build and the checks had
carried since the business pilot.

1. **One slot plan fits every subject.** `make_work_order.py` chose card subtypes, command words and AOs from
   defaults tuned for business. Physics needs three calculation cards per "recall and use" objective and a
   multiple-choice set per content topic; geography needs a case-study analysis per case study; computer science
   needs trace and algorithm cards. Hand-editing work orders after generation would be overwritten on the next build.
2. **A topic is examined on one paper with one AO split.** 9618 sections 1-8 sit on Paper 1 and 9-12 on Paper 2;
   9702 topics 1-11 sit on Papers 1 and 2 (AO1/AO2) and topic 12 on Paper 3 (AO3 only). Balancing every topic
   against the qualification weights pushed AO3 cards into topics whose paper never assesses AO3.
3. **C-32 can read every stated calculation.** It could not read binary arithmetic (it recomputed
   0011 0110 + 0001 1011 in base 10) or the typeset × and ÷ signs, so wrong physics products passed unread.

## What changed

- `slot_plan` in `subject-profile.yaml`, read by `make_work_order.py`; absent, the defaults apply unchanged.
- Paper keys (`'1+2'`) for `ao_by_paper`, `ao_by_paper_subtype` and `topic_targets_by_paper`; an optional `papers`
  field on registry objectives.
- C-32: base-2 recomputation with fixed-width modulo; × and ÷ as operators.
- C-35 and C-41: `depictions.chart_model` and `depictions.code_fence_languages` in the subject profile.
- `multiple_choice_set` item type.

## Proof

- Regression: 0450, 0455 and 9609 work orders regenerate with 0 diffs; 9618 with 0 diffs against its pre-change plan.
- 12 new tests; suite 74 passed.
- Exemplars proved after the change: 9618 (both slices), 9702, 0460.
