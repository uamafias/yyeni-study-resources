# NSSCO Maths R8 author repairs — 3 November 2026

The Claude R7 implementation findings have author repairs and regression evidence.
Current candidate collection: **409 recipe settings, 410 assignment choices and
4,022 distinct saved examples**. Eight new types supplement the six repaired power
types: five bill/receipt/account contexts, contextual variation, a speed–time task
and finding a line equation from a graph. Other repairs extend existing recipes.

## Repair ledger

| Review | Repair |
| --- | --- |
| N1 | Exact rational targets, real constant-power equations, long-digit semantic guard; six power types at version 9. |
| N2 | Correct text/maths classification, function names, inline paragraphs, safe historical currency presentation. |
| N3 | Off-table power-graph solutions and independently checked domains/branches. |
| N4 | Actual part-level links for all 439 authored demand entries, including prompt, answer, criteria, seed, version and fingerprint. No multi-clause objective fallback. |
| N5 | Telephone/cell bills, till/payment receipts, clothing accounts, contextual variation and general intersecting loci. |
| Low | Grammar, labels/contrast, repeated answers, fractions, graph scales, rotation notation and set variety. |

The tracing pass also added explicit evidence for zero-exponent standard form,
physical-quantity estimation, 2D area scaling, geometric general terms, inner and
outer matrix products, deceleration, and deriving an equation from the actual graph.

## Verification

- 661 broad backend checks passed; five final focused R8 checks also passed,
  including the subsequently added all-demand traceability test (overlapping runs).
- 27 frontend checks and lint passed; 17 source-export checks passed.
- Real Markdown/KaTeX rendering: 31,758 raw strings and typed paragraphs, zero
  invalid expressions. Existing half-character font-metric notices remain.
- 64 seeds: 512 graph cases, 320 bill/receipt cases, 64 loci, 64 variation cases,
  64 Low-finding sets and 64 additional clause-gap sets passed independent checks.
- Representative diagrams for 14 types were rendered and inspected. This is not
  exhaustive visual review of every seed or all prepared images.
- Full saved-bank uniqueness, exact replay and direct rebuilding pass. All 41
  authorised retirements remain excluded. Source and app mirror: 2,116 files.

## Limits and preservation

These are **author checks**, not independent mathematical, tariff or whole-syllabus
approval. The 439 entries are an authored decomposition of the 152 syllabus-bullet
locators. Part links establish traceable candidate evidence; they do not certify
every permitted branch, context or representation. The report preserves the
original part objective labels and explains direct cross-objective evidence.

Original R7 code and the 60 problematic graph examples remain in the historical
repair baseline. Current corrected versions are separate; learner snapshots and
original submissions are untouched. The source package blocks rejected versions.
Files with unknown authorship remain preserved. Nothing committed or pushed.
