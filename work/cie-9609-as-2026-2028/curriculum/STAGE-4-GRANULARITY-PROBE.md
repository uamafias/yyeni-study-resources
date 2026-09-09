# Stage 4 investigation — does Cambridge examine at member level or at bullet level?

**Raised by Vitalis, 2026-08-31.** Verdict deferred to him after the evidence is in. This file exists so the question is not lost between stages.

## The question, precisely

Topic allocation by exam frequency was rejected — we cannot predict which topics the next paper favours, and chasing last year's distribution is how a resource becomes a revision guide for a paper that has already been sat. The better question is about **granularity**:

> When a syllabus bullet expands into N named members — fourteen sources of finance, nine non-financial motivators, six motivation theorists — do exam questions actually reach into the individual member, or do they stay at the level of the bullet?

If questions routinely name **debt factoring** rather than "sources of finance", then depth belongs at member level and the 95 members earn private allocations. If six years of papers never name a member and always ask about the category, then the members are vocabulary inside one objective, and depth belongs at the bullet.

This is a question the evidence can answer, and it applies to every subject afterwards, not just Business.

## Why the decomposition had to happen first

The split into 95 members is a prerequisite for the probe, not a pre-emption of it. Without member-level objective IDs there is nothing for a question about debt factoring to map to, so member-level probing would be undetectable — every such question would map to `5.2.2-02` and look like a category question.

Splitting settles **visibility and traceability**. The probe settles **how much each member earns**. Different decisions, and they are correctly taken in this order.

## Method

Against 168 AS question papers and mark schemes, 2020–2025, all variants including the March series.

For every question part:

1. Map it to the finest objective ID it addresses.
2. Record whether the stem or the mark scheme **names a specific member** ("debt factoring", "Herzberg", "penetration pricing") or stays at category level ("sources of finance", "motivation theory", "pricing methods").
3. Record command word, mark tariff, AO focus and paper.

Then, for each of the 18 decomposed bullets:

| Metric | Meaning |
|---|---|
| **member-probe rate** | distinct members named at least once ÷ total members. `5.2.2-02` scoring 3/14 means eleven sources were never named in six years. |
| **member-question share** | question parts naming a specific member ÷ all question parts touching that bullet |
| **tariff at member level** | mean marks when a member is named, against mean marks when the category is asked |
| **AO at member level** | are member-named questions AO1 recall, or do they reach AO3 and AO4? |

The fourth metric is the one that decides the answer. A member named only in 2-mark "define" questions justifies one definition card. A member named in an 8-mark "analyse the impact of using debt factoring" justifies a full objective with its own chain and evaluation items.

## Decision rule to bring back

Three outcomes, and the evidence picks one:

- **Members are probed, and at tariff.** Members become first-class objectives at tier 2, take private item allocations, and the 700 budget must rise or the unsplit bullets must give ground. Expect the budget conversation to reopen.
- **Members are named but only at low tariff.** Members stay tier 1 with a shared recall item, exactly as budgeted today. No change.
- **Members are never named.** The split still stands for adequacy and traceability, but members carry no separate item allocation at all, and the 32-item member pool is redeployed to evaluation practice.

My expectation, stated in advance so the evidence can contradict it: **mixed by bullet, not uniform.** Motivation theorists and pricing methods are named in stems routinely; the fourteen sources of finance are more often supplied as a case-study fact for the candidate to evaluate than named in the question. If that holds, the answer is per bullet rather than a single policy — which is itself a useful finding for the standard, because it means granularity has to be an evidence-set field on each objective rather than a global rule.

## Output

`assessment-evidence/granularity-probe.json` with the four metrics per decomposed bullet, plus a summary table in the Stage 4 report. Verdict is Vitalis's.
