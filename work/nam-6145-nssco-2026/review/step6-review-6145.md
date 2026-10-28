# Step 6 cross-review: 6145 NSSCO Economics

Reviewer: Claude (Opus 5.5), 28 October 2026. Authored by Codex at commit c7d6bb1.
Scope: all 28 topics, 580 items (468 flashcards, 112 practice packages) and all the notes (60,061 words before review, 67,109 after).

## Verdict: **publish**

The authored subject was accurate but incomplete. No mechanism was inverted, every figure recomputed correctly, and all 580 slots were filled.

The weakness was in every topic. The notes argued in careful, abstract terms and left out the named points that the 2020–2024 examiner reports credit. Missing items included:

- the functions of the central bank and the stock exchange;
- unlimited liability;
- the types of tax;
- named causes and consequences of inflation and unemployment;
- the balance-of-payments accounts;
- HDI;
- methods of protection;
- merit goods and privatisation;
- external economies of scale;
- MC = MR (a syllabus glossary definition).

One card taught the answer the 2024 report rejects (homogeneity of money).

I fixed all of this in the learner text. The notes are now fit to teach from. Three things remain, and none blocks publication:

- **Missing cards.** Some examined content has no flashcard, because new cards need new work-order slots (P1).
- **Diagrams.** The notes describe the needed diagrams but none exist yet (P3).
- **No cross-check of the additions.** About 7,000 words of new teaching text are mine and have not been read by a second model (see "Not yet cross-checked").

## What was run

| Check | Result |
|---|---|
| 1. `run_checks.py`, every topic | 28 × PUBLISH, 0 fail, before and after the fixes. Warnings unchanged: C-18 AO mix by item count (all 28); C-35, C-41, C-43 `not_run` (no generated depictions or practice texts). C-26 word budget passes everywhere. |
| 2. Completeness (script) | 580 work-order slots → 580 items, one per slot. Item type, subtype, AOs, Bloom level, command word, tariff and objectives all match the slot. All 37 MISCON cards carry their entry, and there are no orphan items. Re-run after the fixes: unchanged. |
| 3. Copied wording | `check_copied_wording.py` against the 10 question papers (2020–2024) and the 5 examiner-report volumes, read directly from the PDFs (the syllabus was not passed). Result: 0 runs of 8+ words, before and after the fixes. |
| 4–8. Level, scope, truth, numbers, misconceptions, learner test | Eight parallel readers read every topic's notes in full and every item, with the syllabus and the examiner comments mapped to each topic. I checked each finding against the item text, the syllabus or the report evidence before fixing it. |
| Numbers | Every worked figure was recomputed: schedules and equilibria, all elasticities and revenue changes, costs and revenue, exchange conversions, price indices, GDP/GNP and value added, population rates, unemployment and participation rates, and comparative-advantage ratios. All were correct. |

## Findings

Severity follows `REVIEWER.md`:

- **critical**: teaches something false that a learner would act on;
- **high**: trains invalid reasoning or omits examined knowledge;
- **medium**: inaccurate or inconsistent;
- **low**: tidiness.

### Subject-wide

| # | Sev | What | Status |
|---|---|---|---|
| S1 | high | Examined named content missing or only gestured at abstractly, in all 28 topics. Most units were written to within a few per cent of their minimum word budget. | **Fixed**: about 7,000 words of standard named content added. Details per topic below. |
| S2 | medium | Definition cards with no scorable definition, or with template wording: "under the stated measurement convention", "in the syllabus's national-product terminology", "with the measurement basis specified", definitions of coined categories, and answers inverted by the template ("… is a central bank"). | **Fixed** on 33 cards. Claims revised where the definition itself changed (16 claims). |
| S3 | low | About 290 "invented/fictional/hypothetical" and "original example/case" labels in learner text. | **Fixed** by a sweep with article correction. "Hypothetical woman" in the total fertility rate definition was kept, because it is the standard wording. |
| S4 | low | Author-to-author and tooling wording in learner text. Examples: "member unit", "parent unit", "main unit", "next unit"; "this lesson does not invent…"; "not current Namibia figures"; "the question might award one result mark"; "at NSSCO depth"; source-checking citations aimed at the author. | **Fixed** (about 70 sentences). The remaining "use the figures supplied rather than invent…" lines are kept as data-task advice to learners. |
| S5 | low | Template scaffolding inside answers ("Initial change: …; the mechanism is …"). Run-together text ("residents,250", "A30 cloth", "toN$105", "total 2001"). American "Labeling". A broken link URL in 6.3. | **Fixed**. |

### Content

| # | Sev | What | Where | Status |
|---|---|---|---|---|
| C1 | critical | Homogeneity of money taught as "equal value". The 2024 report rejects exactly that answer; the credited answer is that money looks the same. | 2.3 notes, 2.3-029, 2.3-P02(e) | **Fixed**: identical appearance within a denomination. Claims 2.3-35/36 revised. |
| C2 | high | Unlimited liability never named. Partnership definition circular. Close corporation details (1–10 natural-person members, CC) withheld. No named advantages or disadvantages for any form. Private/public sector differences given only as ownership. Shareholders vs board of directors not stated; no dividends, "(Pty) Ltd" or "Ltd". Co-operative features and types missing. Formal vs informal sector missing. | 2.1 | **Fixed**. 2.1-010/011/012/016/005 and P01(a), P02 rewritten. |
| C3 | high | Bank of Namibia functions (lender of last resort, supervision, repo rate) missing. NSX never named; no stock-exchange functions or reasons to list. Effects of fluctuations given for one firm, not the economy. N$–rand peg not explained. Commodity, fiat and legal-tender money missing. Further commercial-bank services missing. | 2.3 | **Fixed**. 2.3-020/033/034/035 rewritten. |
| C4 | high | Industrial action never named. Namibian factors affecting unions limited to distance. Advantages of joining, employer-association roles, industrial and general unions, and economy-wide effects of unions all missing. | 2.2 | **Fixed**. |
| C5 | high | System advantages and disadvantages never listed (no "command", "public goods" or "consumer sovereignty"). MISCON 017/018 content swapped against the slots' misconception entries. | 1.2 | **Fixed**: content moved to the matching slots. |
| C6 | high | "Unlimited wants" missing from scarcity. No production possibility curve. | 1.1 | **Fixed** in the notes (PPC described with a worked example). Diagram not drawn (P3). |
| C7 | high | Types of market, the price-setting role of markets and e-commerce missing (3.1). Determinants not named or given a direction; complements, inferior goods, taxes and subsidies missing; laws of demand and supply, shortage/surplus and extension/contraction missing (3.2). Perfectly elastic and its synonyms missing; price-cut revenue rule missing (3.3). Advertising shifting demand, brand loyalty, non-price competition and methods missing (3.4). Price maker, barriers to entry, price discrimination and price vs non-price competition missing (3.5). | 3.1–3.5 | **Fixed**. 3.1-004 rewritten. |
| C8 | high | Gross/net pay, piece and time rates, the labour market diagram, and reasons for earnings differences missing (4.2). Interest-rate effect on saving not stated; income-group pattern and dissaving missing (4.3). Fringe benefits and promotion missing; mobility undefined (4.1). | 4.1–4.3 | **Fixed**. Template DEF prompts 4.2-010/013/015/016 rewritten. |
| C9 | high | MC = MR missing, although it is the syllabus glossary definition of profit maximisation and examiners credit it. Value added, sectors, aims of firms and labour/capital-intensive missing (5.1). The productivity–profit link missing; HIV effects hedged away; standard IT and improvement methods missing (5.2). | 5.1, 5.2 | **Fixed**. 5.1-001 and 5.2-001 rewritten; claims revised. |
| C10 | high | Short run/long run undefined; no standard fixed/variable examples; no technology effects. MISCON 5.3-022 tested revenue vs profit instead of its entry (average vs marginal revenue). | 5.3 | **Fixed**. 5.3-006 (non-syllabus term) now defines the short run. |
| C11 | high | External economies and diseconomies missing; motives for growth, merger and takeover missing; LRAC curve undescribed. | 5.4 | **Fixed** in text. Diagram not drawn (P3). |
| C12 | high | Merit goods, reasons for state production, parastatals, privatisation and nationalisation, and effects of government employment all missing. | 6.1 | **Fixed**. |
| C13 | high | No named taxes (VAT is absent from the whole subject); reasons for taxation, policy chains against inflation, and Bank of Namibia repo rate and price-stability aim missing. | 6.2 | **Fixed**. 6.2-007/021, 6.2-006 (whose "for" argument contradicted the prompt) corrected. |
| C14 | high | Methods of control (subsidy, quota, maximum and minimum price) missing; named reasons for intervention, consumer and employee protections, and HIV workplace measures refused as "to be checked"; minimum wage effects missing. MISCON 6.3-016 restated a definition and did not discriminate. | 6.3 | **Fixed**. 6.3-012/016 rewritten; claim 6.3-09 revised. |
| C15 | high | Inflation never defined in 7.1. Weighted price index method, cost-push causes, types by speed and consequences of inflation missing. | 7.1 | **Fixed**. |
| C16 | high | Remedies, reasons for unemployment, sectors of employment and consequences for the economy missing. Definitions not scorable. | 7.2 | **Fixed**. 7.2-004/013/014/016 rewritten; claims revised. |
| C17 | high | GNP and National Income definitions opaque; depreciation missing; reasons for measuring and the real GDP method missing; an above-level GDP deflator caution. | 7.3 | **Fixed**. 7.3-011/012/014/015 rewritten; claims revised. |
| C18 | high | Importance of trade never taught. The current account and its parts never named, and "capital account" called legacy wording. Reasons for exchange-rate fluctuations and Namibia's trade pattern missing. | 7.4 | **Fixed**. |
| C19 | high | Characteristics of developed and developing economies, dependency ratio, reasons for population growth and problems of development missing (8.1). HDI and named indicators, IT effects and reasons for disparities between countries missing (8.2). | 8.1, 8.2 | **Fixed**. 8.2-012/013 (coined category terms) now define adult literacy rate and infant mortality rate. |
| C20 | high | The public vs private spending conflict, reasons for and methods of protection (embargo was used in a MISCON entry but never taught), conservation methods and externality examples missing. | 9.1 | **Fixed**. 9.1-005 rewritten. |
| C21 | medium | Wrong cross-references: "occupational skills in 4.2" (should be 4.1), "labour-market opportunities in 4.2" (should be 4.1/7.2). | 5.4, 6.3 | **Fixed**. |
| C22 | medium | Minor errors: crude-death-rate condition said nothing; 8.1-P02(g) never stated the result; 1.3-009 answered about markets, not products; 7.2-P03 read "falls 73 percent"; 7.2-003 guidance said "common denominator"; 5.4-P02(d) gave one point for 2 marks; 4.3-002/007 imprecise; 8.1-015 guidance did not fit TFR. | as listed | **Fixed**. |
| C23 | low | 3.3-011/014 CALC cards credit only the result [1]; the reports credit the formula too. | 3.3 | **Not fixed**: the tariff is a slot label. Notes now tell learners to write the formula (P1). |
| C24 | low | 2.3 DEF cards 017–032 put the second-mark qualifier only in the guidance, not the answer. | 2.3 | **Partly fixed** (020, 029, 033–035). The rest are still answerable from the notes. |

Also checked and sound: N$ currency throughout, no real companies, no learner-facing exam-frequency claims, every Evaluate card reaches a conditional judgement, and the other MISCON cards discriminate their confusion.

## How the fixes were made

- Only `topics/` learner text was edited: items, content-unit blocks, and claim text where the fact itself changed.
- 16 claims had their `revision` raised. Citing items and blocks were stamped with the new revision, and those whose text needed no change carry `reviewed_unchanged`.
- In total, 63 items and about 140 blocks were edited, plus a label sweep over 291 fields.
- Every topic was run through `restamp.py`, `render_notes.py` and `run_checks.py`, then republished with `publish_subject.py`.
- `curriculum/`, contracts and work orders are untouched. No slot label changed.
- Codex's author artefacts (`topics/export-reconciliation.json`, `topics/final-author-audit.json`, `authored_packet.json`) now describe the pre-review text. Do not rerun `author_support.py`; it would overwrite these fixes.

## Not yet cross-checked

The added content is standard textbook material, written by me from the readers' drafts. A second model has not read it.

These Namibian facts were added from general knowledge, not from a source on file:

- disputes go to the Labour Commissioner for conciliation before a lawful strike;
- a close corporation has 1–10 natural-person members;
- company names end in "(Pty) Ltd" or "Ltd";
- a partnership usually has no more than 20 partners;
- the NSX is in Windhoek;
- the N$ and the rand are both legal tender, with a one-to-one peg in the Common Monetary Area;
- the Bank of Namibia aims at price stability and sets the repo rate;
- the Namibia Statistics Agency publishes the CPI monthly;
- the Namibian Competition Commission, NSI, NAMFISA and CRAN regulate consumer-facing areas;
- the Social Security Commission pays maternity, sick-leave and death benefits;
- affirmative action law exists;
- Namibia's main exports and import sources.

A short Codex read of the added paragraphs (search the diff for the new text) is recommended before the subject is called final.

## Plan problems (for Vitalis)

1. **P1: Examined content with no card.** Slots are fixed, so I could not add cards for content now in the notes:
   - central bank functions and the repo rate;
   - NSX functions;
   - industrial action;
   - external economies of scale;
   - merit goods and privatisation;
   - types of tax (direct tax examples);
   - an inflation DEF card;
   - total and average revenue DEF cards;
   - HDI;
   - dependency ratio;
   - methods of protection;
   - value added;
   - gross/net pay and piece rate;
   - occupational and geographical mobility.

   Several DEF slots were also planned for template terms (for example "Define a cost-output relationship"), and the 3.3 CALC tariff of [1] credits no formula. Re-opening step 4 to add slots for these would make the flashcards match the notes.
2. **P2: Authoring style.** Codex wrote most units close to their minimum word budget in hedged, abstract prose and avoided named facts. The authoring brief, or the Codex hand-over, should require the standard named points the reports credit, in each topic.
3. **P3: Diagrams and standard issues** (outside this workspace; report only):
   - No diagrams exist in the 6145 publication, although the plan's depiction rule calls for generated diagrams. The notes now describe the PPC, the LRAC curve, the labour-market diagram, price controls and the shift diagrams in words.
   - `render_notes.py` prints a tooling header ("rendered from the approved content units") and unit sub-numbers ("— 7.4.3") in learner notes.
   - The subject-profile schema rejects `slot_plan` and `conditioned_mechanisms`, which the runtime accepts.
