# Pipeline Stage 4 — assessment-material mining, Cambridge AS Business 9609

**Executed:** 2026-08-31 · **Corpus:** 84 AS question papers, 2020–2025, all variants including March · **988 question parts extracted**

Artifacts: `assessment-evidence/assessment_evidence.json` (228 records, schema-valid, status `partial`), `assessment-evidence/granularity-probe.json`, `assessment-evidence/examiner-findings-firstpass.json` (766 statements from 11 examiner reports).

---

## 1. The command-word tariff table is exact, and my framework was wrong in three places

Across the 2023–2025 series there is **zero variance**. Cambridge does not vary the tariff for a command word at AS:

| Command word | Parts | Marks | My Stage 3 estimate | Verdict |
|---|---:|---|---|---|
| Identify | 42 | **always 1** | 1–2 | close |
| Define | 63 | **always 2** | 1–2 | close |
| Explain | 147 | **always 3** | 3–5 | **too wide** |
| Calculate | 42 | **always 3** | 2–4 | close |
| Analyse | 105 | **5 or 8** (8 in 84 cases, 5 in 21) | 5–8 | correct |
| Evaluate | 84 | **always 12** | 12–20 | **too wide — 20 never occurs at AS** |
| **Assess** | **0** | — | 8–12 | **never used at AS** |
| **Advise** | **0** | — | 10–12 | **never used at AS** |
| **Justify** | **0** in 2023–25 | 22 uses pre-2023 | 8–12 | **retired at AS** |

Three of the nine official command words — Assess, Advise and Justify — **do not appear in a single AS paper from 2023 to 2025.** They are in the syllabus's command-word glossary because it covers AS *and* A Level; Papers 3 and 4 use them. The framework I wrote at Stage 3 told authors to build Advise and Assess items for an exam that never asks them.

This alone changes what gets generated.

## 2. The 2023 revision changed the command-word set — pre-2023 papers must not calibrate practice

| | 2020–2022 | 2023–2025 |
|---|---|---|
| Discuss | **64 uses** | 0 |
| Recommend / Justify (combined, 11 marks) | present | 0 |
| Evaluate | 19 | **84** |
| Identify | 0 | **42** |
| Define | 105 | 63 |

"Discuss" is not in the current official list at all, yet it is the dominant extended-response verb in the older papers. The Evaluate count quadruples after 2023 and Identify appears from nothing.

The `series_predates_2023_syllabus_revision` flag applied to 162 sources at Stage 2 has turned out to matter more than expected: **the 2020–2022 papers are usable for content and context, but must not be used to calibrate command words, tariffs or AO shape.** Only 2023–2025 does that job — which is 42 of the 84 papers.

## 3. The granularity probe — the answer to your question

**Method.** 95 member objectives, each with a search pattern against 988 question stems. Members were graded `H` (distinctive multi-word term or proper noun) or `M` (single common word needing context). Only the 84 `H` members carry the verdict; the `M` matches are reported but excluded, for a reason that turned out to be interesting — see §4.

**Headline: 63 of 84 high-confidence members (75%) are named in an AS question stem at least once in six years, and 43 of 95 members reach 8 marks or more.**

Members are not vocabulary. They are question targets, and they are targets at analysis and evaluation tariff, not just recall.

Real examples, all 12 marks:

- *Evaluate whether MLC should change from a private limited company to a public limited company.*
- *Evaluate whether Samira should accept Lara's offer to invest venture capital.*
- *Evaluate whether a bank loan is the most appropriate source of finance for JC's growth.*
- *Evaluate whether Frank should introduce price skimming.*
- *Evaluate whether ZB should introduce performance-related pay.*
- *Evaluate whether a joint venture is the most appropriate way for SF to grow.*

Each names one member of a bullet I split, and asks for a judgement about that specific member in a specific business context. Under the pre-split registry every one of these would have mapped to a category objective and been indistinguishable from a general question.

### But the answer is per bullet, not global

| Bullet | Members | Named (H) | Rate | Max tariff | Reading |
|---|---:|---:|---:|---:|---|
| 1.2.2 ownership types | 8 | 8 | **1.00** | 12 | **Fully probed at evaluation** |
| 1.4.1 objectives by sector | 3 | 3 | 1.00 | 12 | Fully probed |
| 4.1.2 efficiency / productivity / sustainability | 3 | 3 | 1.00 | 12 | Fully probed |
| 2.1.6 training types | 3 | 3 | 1.00 | 8 | Fully probed |
| 2.1.3-01 recruitment process / methods | 2 | 2 | 1.00 | 11 | Fully probed |
| 5.4.1 cost types | 2 | 2 | 1.00 | 3 | Named, recall only |
| 3.3.4 pricing methods | 7 | 6 | 0.86 | 12 | Mostly probed |
| 2.2.4-02 payment methods | 8 | 6 | 0.75 | 12 | Mostly probed |
| 2.3.1-04 management styles | 4 | 3 | 0.75 | 12 | Mostly probed |
| 5.4.4 break-even measures | 4 | 3 | 0.75 | 12 | Mostly probed |
| **5.2.2-02 external sources of finance** | 14 | 10 | **0.71** | **12** | **Probed and evaluated** |
| 2.1.3-03 selection methods | 6 | 4 | 0.67 | 8 | Partly probed |
| 3.1.6 segmentation methods | 3 | 2 | 0.67 | 3 | Named, recall only |
| **2.2.3 motivation theorists** | 6 | 3 | **0.50** | 12 | **Half never named** |
| 5.2.2-01 internal sources | 5 | 3 | 0.50 | 12 | Half never named |
| **1.3.3-02 external growth types** | 5 | 1 | **0.20** | 2 | **Effectively never probed** |

### Twenty-one high-confidence members never named in six years

`psychological pricing` · `bonuses` · `fringe benefits` · `job re-design` · `paternalistic management style` · `level of profit` · `share capital` · `debentures` · `new partners` · `mortgages` · `application forms` · `geographic segmentation` · **`Taylor`** · **`Mayo`** · **`Vroom`** · `owner's investment` · `sale of unwanted assets` · **`horizontal integration`** · **`vertical integration (backward)`** · **`vertical integration (forward)`** · **`conglomerate diversification`**

### Two results I did not expect

**I predicted the opposite on both counts, and the evidence says so.**

I said theorists would be named routinely and sources of finance would appear as case facts rather than question targets. **The reverse is closer to true.** Venture capital, bank loans, crowdfunding and overdrafts are named in 12-mark evaluation questions. Taylor, Mayo and Vroom are never named at all; only Maslow (2), Herzberg (1) and McClelland (2) appear.

**The integration taxonomy is not examined at AS.** Searching all 988 parts: "integration" **0**, "horizontal" **0**, "conglomerate" **0**, "vertical" **1**. Growth itself is examined heavily — fourteen question parts at 8 marks or more — but as *"grow internally (organically)"*, *"merger"*, *"joint venture"*, never as the horizontal/vertical/conglomerate taxonomy that every textbook devotes pages to. The syllabus requires the taxonomy, so it stays in the registry as mandatory; but it earns a definition card, not a chapter.

## 4. The glossary homonym warning was empirically confirmed

The `M`-confidence matches were contaminated in exactly the way the Stage 3 glossary predicted:

- `opportunities for promotion` matched *"Evaluate the usefulness of digital promotion to TT"* — marketing promotion, not employee promotion
- `development` matched *"new product development"*
- `contribution` matched *"the contribution of the managers in a new hospital"* — the ordinary sense, not selling price minus variable cost

Three of the five homonyms flagged at Stage 3 produced false positives in the first automated pass over real papers. That is a rare thing: a predicted failure mode, verified against evidence, before it reached a learner. It is also why those matches are excluded from the verdict.

## 5. Assessment evidence map

228 schema-valid records, `status: partial`. 63 distinct objectives cited across 73 source papers and 17 exam series. AO focus of the mapped evidence: AO1 47%, AO2 30%, AO3 16%, AO4 7%.

That distribution is skewed toward AO1 because member names are most reliably detectable in short recall questions; it is a property of the matcher, not of the papers. Mark-scheme mining for credit-worthy points is the remaining work.

**Examiner reports:** 766 candidate-weakness statements extracted across all 11 reports, first pass. Not yet mapped to objectives. One is worth quoting now because it bears directly on the item design: *"where the command word is 'evaluate' candidates often fail to offer a clear answer, which in most cases still requires a judgement."*

---

## The verdict is yours — three options

**Option A — members become first-class objectives everywhere.** Simple, uniform, and wrong in the light of §3: it would give `conglomerate diversification` the same treatment as `venture capital`, and inflate the item budget past 700 for content the exam never asks about.

**Option B — granularity set per bullet from this evidence.** Members in the fully-probed bullets (ownership types, objectives by sector, efficiency/productivity/sustainability, training types, recruitment) promote to tier 2 with private item allocations including APP and EVAL. Members in mostly-probed bullets promote for the named members only. Members never named in six years stay tier 1 with a shared recall card. The integration taxonomy stays mandatory but minimal.

This is my recommendation, and it fits inside 700 — the promotions are roughly offset by the 21 never-named members dropping to shared coverage.

**Option C — split the difference: promote by tariff, not by naming.** Only members reaching 8+ marks (43 of 95) promote. Cleaner rule, slightly blunter: it would demote `cost types` and `segmentation methods`, which are named consistently but only ever at 2–3 marks — which is arguably correct, since a 3-mark ceiling really does mean one card.

Whichever you pick, three things follow regardless and I would apply them now:

1. **Drop Assess and Advise from the AS item generation rules.** Zero occurrences in three years. The framework currently mandates them.
2. **Fix the tariffs to the exact values** — Identify 1, Define 2, Explain 3, Calculate 3, Analyse 5 or 8, Evaluate 12. No ranges.
3. **Restrict command-word and AO calibration to the 42 papers from 2023 onward.** The older 42 stay in scope for content and context only.
