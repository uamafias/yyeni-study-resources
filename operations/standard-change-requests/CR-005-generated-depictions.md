# CR-005 — Depictions are generated, not authored

**Raised:** 2026-09-12 · **Against:** standard v0.2.0-draft · **Delivers:** RS-47, a chart renderer, C-41 and C-42
**Trigger:** the fourth RS-28 review of topic 5.4
(`operations/review/cie-9609-as-2026-2028-5.4-review-r4.yaml`) returned **reject** with one **critical** issue —
the first critical since round two — on a build whose deterministic pass had reported 41 of 41 checks clean.

## 1. The defect

Four items showed a break-even chart. Their declared parameters were right (price N$80, variable cost N$40,
fixed costs N$160 000). Every number stated about the chart was right (break-even 4 000 units at N$320 000,
margin of safety 2 000, profit N$80 000). The ASCII picture the learner actually sees drew the revenue trace
*above and roughly parallel to* the total-cost trace. **The two lines never crossed.** The prompts asked
learners to read a break-even point that was not on the page.

C-35 passed all four. It verifies a chart's declared parameters against the arithmetic stated about them —
metadata against metadata. It had never looked at the picture, and nothing in the suite had.

The same defect was in the offline notes, in the block that teaches learners to read and draw a chart. The
review did not reach it. It was found by the machinery this CR installs, which is the point of installing it.

## 2. The rule

| Rule | Requirement |
|---|---|
| **RS-47 Depictions are generated, not authored** | A learner-visible depiction of declared data — a chart, graph, diagram or plotted figure — MUST be generated from that data by the build, never drawn by hand beside it. The generator is the single source of the picture, and the published depiction must be byte-identical to what regenerating it produces. |

This is the same principle as RS-45, one step further out. RS-45 said a derived *number* is recomputed, never
edited. RS-47 says a derived *picture* is too. Anything a build can generate from data it already holds should
be generated, because the alternative is a second copy of the truth that drifts without anyone noticing.

## 3. What was built

- **`build/render_chart.py`** — renders a break-even chart from `{price, variable_cost, fixed_costs,
  current_output}`. It plots each line from the function itself rather than from typed characters, marks the
  intersection, chooses round gridline steps, and returns the readings (break-even output and value, profit and
  margin of safety at current output, and the revenue/fixed-cost crossing) so an answer can be checked against
  the same source the picture came from.
- **C-41** (RS-47) — re-renders every declared chart and fails any prompt or block whose plot is not
  byte-identical to the result. A plot with no declared chart also fails: a picture with nothing to regenerate
  it from cannot be verified. Content blocks are scanned as well as items, because the notes are rendered from
  blocks and the offline text is where the teaching figure lives.
- **C-42** (RS-45) — compares the contract's authorised counts against the live build. Issue R4-004: the
  contract still authorised 92 items beside a bank of 105.
- **C-35 narrowed** — it now accepts the revenue/fixed-cost crossing as a real point on the chart. Its original
  form assumed every "crosses at N units" was the break-even crossing, which made a correct sentence fail.
- **`answer_structures.PROC`** added to the subject profile. PROC was a valid subtype with no declared
  structure, so C-16 had been reporting PROC cards complete without having any parts to test (R4-006).

## 4. The lesson worth keeping

This is the third time the same shape of error has appeared, and it is now worth stating as a design rule
rather than an anecdote:

> **A check that tests for the presence of a thing will pass a fake version of that thing.**
> C-31 tested that a graphical objective had an item using chart vocabulary; round two supplied one whose
> chart was algebraically impossible. C-35 was built to test the chart's numbers; round four supplied one
> whose numbers were right and whose lines did not meet. Each check was correct and each was satisfied by
> something that did not exist.
>
> The escape is not another check on the artefact. It is to stop authoring the artefact. A generated picture
> cannot be faked, because there is nothing to fake it with — the data is the picture.

Where an artefact cannot be generated, the check must reach the thing a learner actually receives, not a
declaration about it. Reviewing metadata is reviewing a claim about the work.
