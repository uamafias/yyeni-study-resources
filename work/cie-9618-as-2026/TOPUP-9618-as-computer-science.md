# Top-up — Cambridge International AS Level Computer Science 9618 (1 October 2026)

The subject is authored and published: 29 topics, all PUBLISH. This run adds **8 programming tasks** and nothing else.

## Why

A planner audit found that 18 Paper 2 cards were relabelled from AO3 (design and programming) to AO2 (application), correctly for what they ask, but it leaves the subject's AO3 practice about 6 points under the syllabus weight of 30% (`curriculum/syllabus-facts.json`). Eight 8-mark AO3 tasks (64 marks) bring it back inside 5 points. The relabelling is now recorded in each topic's `authoring_notes.json`; do not change those cards.

## The eight new slots (already in the work orders)

| topic | new slot ids |
|---|---|
| 9.2 Algorithms | `ITEM-9618-9.2-P05`, `ITEM-9618-9.2-P06` |
| 10.2 Arrays | `ITEM-9618-10.2-P05` |
| 10.3 Files | `ITEM-9618-10.3-P05` |
| 10.4 Introduction to Abstract Data Types (ADT) | `ITEM-9618-10.4-P05` |
| 11.1 Programming Basics | `ITEM-9618-11.1-P05` |
| 11.3 Structured Programming | `ITEM-9618-11.3-P05`, `ITEM-9618-11.3-P06` |

Each slot in `topics/<T>/work_order.json` says: `worked_example`, command word `Write`, 8 marks, `assessment_objectives: ["AO3"]`, Bloom `Create`, difficulty 4. **Carry all of these onto the item exactly**, including AO3 alone.

## What each task is

- An original specification in a realistic context (Namibian settings welcome), asking the learner to write a complete module in pseudocode: a procedure or function with parameters, declarations, initialisation, a loop, a selection, and the value returned or output produced.
- It must use the topic's own content: 9.2 a search, sort or stepwise-refined algorithm; 10.2 a 1D or 2D array; 10.3 reading or writing a text file; 10.4 a stack, queue or linked list; 11.1 input, processing and output with the built-in functions; 11.3 a procedure or function with parameters passed by value or by reference.
- It must differ in specification from every existing worked example in its topic. Read the topic's items first.
- The canonical answer is complete pseudocode in a ```pseudocode fence, in the syllabus pseudocode style the topic's existing items use.
- The marking guidance is mark points (6-8), each naming what earns it, and must name every part the slot's `marking_guidance_must_name` lists.
- `objective_ids`: 2-4 objectives from the topic that the task genuinely exercises, each backed by a claim the item cites. Add a claim to the topic's ledger only if no existing claim covers what the task relies on.

## Rules

Everything in `work/cie-9618-as-2026/HANDOVER-9618-as-computer-science.md` still applies: no Cambridge question, mark-scheme or examiner-report wording; only command words in use at this level; filenames derived, never chosen. Read the handover's rules section before writing.

- Add the 8 items to each topic's existing `learning-items/topic_<T>_items.json`. Do not edit, renumber or remove any existing item, claim or content unit.
- Set the contract's `required_outputs.learning_items` and `depth_constraints.item_budget` in each of the 6 topics to the new item count.
- Write only inside `work/cie-9618-as-2026/topics/`. Do not commit or push.

## Finish

For each of the 6 topics:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-9618-as-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-9618-as-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-9618-as-2026 <T>
```

Loop until every topic reads PUBLISH, then republish the subject:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9618-as-2026
```

Report in under 150 words: the 8 item ids with a one-line description each, the final check line per topic, and anything you changed beyond the 8 items and why.
