# Pipeline Stage 5 — topic contracts, Cambridge AS Business 9609

**Executed:** 2026-09-07 · **Pipeline state:** `MAPPED` → **`PLANNED`**

Nineteen contracts, one per AS topic, at `work/cie-9609-as-2026-2028/topics/<topic>/contract.json`. Every figure reconciles: **258 objectives, 889 items, 82,600–177,600 words.**

## What a contract declares

The eight Stage 5 fields, populated from the artifacts built at Stages 2 to 4 rather than asserted:

| Field | Source |
|---|---|
| Included / excluded / deferred objective IDs | Objective registry r3 |
| Prerequisites inherited from other topics | Dependency graph |
| Required outputs | Item budget, per objective |
| Target learner profile | Settled this session — see below |
| Assessment expectations | Assessment framework + the 228 evidence records |
| Depth constraints | Tier ranges, item allocation, exposure classes |
| Source and research permissions | **PENDING on all nineteen** |
| Release gates | RS-07, RS-15, RS-22, RS-31 |

## Note depth: full teaching depth, decided

Recorded in every contract. The reasoning is the deciding factor and it is worth stating plainly, because it is not the obvious answer for a revision product:

> The notes serve three purposes at once — the source of record for flashcard generation, the offline study text when the platform is unavailable, and a standalone text a learner reads to learn. Condensing to revision depth would weaken all three.

The consequence is a hard authoring requirement rather than a stylistic preference: **an offline learner cannot ask a follow-up question.** Every mechanism, formula and worked example is written out in full. That is now a line in each contract's `target_learner_profile`, and it is the kind of constraint that gets forgotten unless it is written down before authoring starts.

Word budget stays at 82,600–177,600. The item budget is unaffected at 889.

## Per-topic contracts

| Topic | Objectives | Items | Words | Evidence records | Rarely examined |
|---|---:|---:|---|---:|---:|
| 1.1 Enterprise | 16 | 48 | 4,800–11,200 | 0 | 0 |
| 1.2 Business structure | 14 | 56 | 3,800–8,400 | 44 | 0 |
| 1.3 Size of business | 14 | 47 | 4,800–10,200 | 1 | 4 |
| 1.4 Business objectives | 12 | 36 | 3,000–7,200 | 6 | 0 |
| 1.5 Stakeholders | 8 | 28 | 3,800–7,400 | 0 | 0 |
| 2.1 Human resource management | 25 | 90 | 6,900–15,300 | 20 | 4 |
| 2.2 Motivation | 28 | 72 | 4,600–11,400 | 33 | 11 |
| 2.3 Management | 8 | 37 | 3,200–6,400 | 9 | 1 |
| 3.1 The nature of marketing | 18 | 48 | 4,400–10,600 | 3 | 1 |
| 3.2 Market research | 9 | 21 | 2,100–5,100 | 0 | 0 |
| 3.3 The marketing mix | 24 | 89 | 9,600–19,600 | 18 | 1 |
| 4.1 The nature of operations | 12 | 48 | 4,600–9,600 | 18 | 1 |
| 4.2 Inventory management | 7 | 31 | 4,100–7,900 | 0 | 0 |
| 4.3 Capacity and outsourcing | 4 | 18 | 2,400–4,600 | 0 | 0 |
| 5.1 Business finance | 9 | 25 | 2,100–5,100 | 2 | 1 |
| 5.2 Sources of finance | 22 | 68 | 3,000–8,000 | 27 | 7 |
| 5.3 Cash flow | 3 | 15 | 2,100–3,900 | 0 | 0 |
| 5.4 Costs | 19 | 86 | 9,900–19,100 | 47 | 1 |
| 5.5 Budgets | 6 | 26 | 3,400–6,600 | 0 | 0 |
| **Total** | **258** | **889** | **82,600–177,600** | **228** | **32** |

**Six topics show zero evidence records.** That is a property of the matcher, not of the papers — Stage 4 mapped evidence by member-name matching, which only reaches the eighteen decomposed bullets. Topics with no decomposed bullets have no mapped evidence yet. Mark-scheme mining closes this, and it is the outstanding Stage 4 work.

## The block calendar was wrong, and now it is right

The earlier figure of 178 items per block was simply 889 ÷ 5. The real blocks are markedly uneven:

| Block | Objectives | Items | Share | 3 attempts | Intensive (18 h/wk) | Distributed (2 h/wk) |
|---|---:|---:|---:|---:|---:|---:|
| Finance and accounting | 59 | 220 | 25% | 11.6 h | 3.9 days | 5.8 weeks |
| Business and its environment | 64 | 215 | 24% | 11.3 h | 3.8 days | 5.6 weeks |
| Human resource management | 61 | 199 | 22% | 10.4 h | 3.5 days | 5.2 weeks |
| Marketing | 51 | 158 | 18% | 8.3 h | 2.8 days | 4.1 weeks |
| **Operations management** | 23 | **97** | **11%** | 5.1 h | 1.7 days | 2.5 weeks |

**Operations is under half the size of Finance.** A fixed four-week block per topic would leave Operations idle for a fortnight and rush Finance.

Recommendation: **fixed weekly hours, variable block length.** The distributed schedule then runs about 23 weeks rather than 20. The intensive schedule clears the whole course in roughly nine days of card practice, so the four-week block is generous and the surplus belongs in written work, as already recorded in the budget.

## The blocker

**`source_and_research_permissions.status` is `PENDING` on all nineteen contracts.** Each names what it is blocked on — Q-1, which sources are approved for derivation, and Q-2, the assessment-material extraction and quotation rules — and each carries an interim rule so that drafting is not frozen:

> No claim authored under this contract may be marked publishable if it traces to a source whose `reuse_constraints` include `licence_check_required` or `do_not_redistribute`.

Thirteen of the twenty original pilot sources carry exactly those constraints. So the interim rule is not theoretical: it currently blocks publication from most of the supporting material, which is the correct behaviour and also the reason the decision cannot wait much longer.

## One finding the contracts surfaced

Topic 5.2, Sources of finance, has **22 of 22 objectives at `generate_gap`** — no supplied source covers any of them. It is also the topic with the second-highest count of rarely-examined members (7) and 27 mapped evidence records showing Analyse and Evaluate at up to 12 marks. So it is simultaneously the least supported topic in the repository and one of the most heavily examined. Whatever order authoring runs in, 5.2 needs the most original writing and has the least to lean on.

## Next

**Stage 6 — atomic objective refinement**, per topic, once permissions are granted. Stage 6 also revisits the decomposition: the eighteen split bullets were the obvious cases, and a per-topic pass may find more.
