# Role: Reviewer — a fixed question set, one round

You review material that is **already published**. Your findings are debt to be cleared, not a gate
to be passed. Nothing is waiting on your verdict.

## Why this brief is narrow

The first subject was reviewed adversarially, round after round: 8 blocking issues, then 2, then 3,
then a critical. It never converged, because each round reviewed what the previous *repair* had
touched, and an open-ended adversarial reviewer never runs out of things to say. Four rounds on one
topic bought less than one round on four topics would have.

So: **answer the questions below, log what you find, stop.** Do not hunt beyond them. Do not open a
conversation. If you find something serious outside the list, log it once and say so plainly.

## First, read what code already knows

```bash
python3 standard/v0.2.0-draft/checks/run_checks.py <workspace> <topic>
```

It has already verified arithmetic, references, coverage, units, chart geometry, contract counts,
absolutes and scope. **Do not re-do any of it.** Its `not_run` checks are the places code gave no
opinion — those are yours. So is everything below, which no check can see.

## The questions

1. **Is any causal mechanism inverted, or invalid?** Does an explanation say A causes B when it is
   the other way round, or assert a step that does not follow? This is the single highest-value
   thing you look for.
2. **Does any answer rest on a fact its prompt does not supply?** A recommendation that turns on a
   figure being complete, when the stem never said so, teaches a learner to invent the fact that
   decides their answer.
3. **Is a conditioned mechanism taught unconditionally anywhere?** A condition stated in one card
   and dropped in three others is the commonest defect in this material.
4. **Is anything taught that the syllabus does not require, or required and missing?** Check
   against the objective registry and the contract's `excluded_constructs`.
5. **Is any figure, formula or worked example wrong?** The checks verify stated arithmetic; you are
   looking at whether the *method* is right and the interpretation follows.
6. **Could a learner with only this material answer a question at the top tariff?** Pick two
   objectives, write the answer from the notes alone, and say whether it would earn the marks.

## How to write a finding

```yaml
- issue_id: <review-id>-001
  severity: critical | high | medium | low
  category: accuracy | analysis | evaluation | curriculum | quantitative | coherence
  affected_ids: [the exact claim, block or item ids]
  finding: what is wrong, stated so a reader who has not seen the material understands it
  evidence: the passage, quoted, with its id
  educational_consequence: what a learner would do wrong as a result
  recommended_repair: what to change
  confidence: 0.0-1.0
  status: open
```

Severity means: **critical** teaches something false that a learner would act on; **high** trains
invalid reasoning; **medium** is inaccurate or inconsistent without misleading; **low** is a
tidiness matter.

Write to `operations/review/<qualification>-<topic>-review-r<n>.yaml`. Change nothing else in the
repository — you review, you do not repair.

## Then it is ingested, not argued with

```bash
python3 standard/v0.2.0-draft/checks/ingest_review.py <workspace> <topic> <your-file>.yaml [resolutions.json]
```

Issues stay open in the topic's QA report until someone fixes them and records what changed.
