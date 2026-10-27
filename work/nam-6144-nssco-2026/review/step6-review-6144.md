# Step 6 cross-review — 6144 NSSCO Business Studies

Reviewer: Claude (Opus 5.5), 27 October 2026. Authored by Codex at commit 5b88c8a.
Scope: all 22 topics, 562 items (474 flashcards, 88 practice packages), 75,192 words of notes.

## Verdict: **publish**

There were no inverted mechanisms and no arithmetic errors. Every fixable finding below has been fixed. Three plan-level matters remain (bottom of this file). None of them blocks publication, but Vitalis should decide them before the subject is called final.

## What was run

| Check | Result |
|---|---|
| 1. `run_checks.py`, every topic | 22 × PUBLISH, 0 fail, before and after the fixes. Warnings unchanged: C-18 AO mix by item count (19 topics), C-26 word budget (21 topics); C-35, C-41, C-43 `not_run` everywhere (no generated depictions or practice texts in this subject). |
| 2. Completeness (script) | 562 work-order slots → 562 items, one per slot. Item type/subtype, AOs, Bloom, command word and tariff match the slot (blueprint for packages). 47 MISCON cards carry their entry. No orphan items. Re-run after fixes: unchanged. |
| 3. Copied wording | `check_copied_wording.py` against the ten 2020–2024 papers and five examiner reports (syllabus not passed): 9 runs of 12+ words, 10 runs of 8–11. All are verbatim **syllabus glossary** definitions (business plan, brand loyalty, brand name, price, industrial union, "feeling that you have done a good job", inventory turnover; glossary pp. 29–32, Annexe A p. 34). Allowed as standard definitions. No new runs after the fixes. |
| 4–8. Level, scope, truth, numbers, misconceptions, learner test | Notes read in full and every item read, all 22 topics, by six parallel readers; each reported finding was verified by me against the item text, the syllabus or the examiner reports before fixing. |
| Numbers | Every worked figure recomputed (Neri/Ema ratio sets, cost examples, pay calculations, pricing, conversion, survey percentages and pie angles). All correct. Ratio formulas match Annexe A. |
| Diagrams | All 7 viewed. Sound: product life cycle stages and shape, both organisation charts, survey charts (12/18/10 of 40 = 30/45/25%). |

## Findings

Severity follows `REVIEWER.md`: critical = teaches something false a learner would act on; high = trains invalid reasoning or omits examined knowledge; medium = inaccurate or inconsistent; low = tidiness.

### Subject-wide (template damage)

| # | Sev | What | Where | Status |
|---|---|---|---|---|
| S1 | medium | Define [2] answers were the whole notes paragraph (117 of 133 over 40 words; up to 125). | All DEF cards | **Fixed**: trimmed to the definition sentence (129 cards); 2 cards repaired where the split broke a sentence (2.4-007 "i.e.", whose guidance was already truncated in the original; 1.1-015 needed both terms). |
| S2 | medium | "State two" answers gave a whole paragraph, or one point stated twice. | 1.1-003/018/021/022, 1.2-009/011/012/016/019, 2.2-015, 2.5-008, 2.6-007, 3.1-001, 3.2-010/012, 3.4-014, 4.1-005, 4.4-005, 5.1-001 | **Fixed**: two clear points (or "Two from: …"). |
| S3 | low | "Fictional/invented/hypothetical" before nearly every name (780 learner-facing occurrences), "Original pack:/plan:/table:" labels, and "under the original facts" in single-scenario essay plans. | All topics; also the 4.2 line-chart title | **Fixed** (sweep with article correction; chart regenerated). |
| S4 | low | Author-to-author disclaimers in learner text ("do not invent legal conditions", "this lesson does not prescribe them", "teaching rate", "in the syllabus model"). | 2.1, 2.4, 3.4, 5.1–5.4 | **Fixed**. |
| S5 | medium | APP/CHAIN/DIST answers open with the full notes paragraph before the case application (about 150 cards). Most still answer the prompt, but they are padded. | Most 6- and 8-mark cards | **Partly fixed**: the four whose padding displaced the answer (2.2-012, 2.3-005, 2.4-002, 4.4-012) were rewritten. The rest remain. |
| S6 | low | Generic marking guidance ("Context: credit the specific case link or contrast stated…") on about 210 cards; CALC guidance labels a working line as "Formula". | Most non-DEF cards | **Not fixed**: needs a re-authoring pass. |

### Content

| # | Sev | What | Where | Status |
|---|---|---|---|---|
| C1 | high | Sources of finance never sorted by term, though the syllabus says "sources of long-term and short-term finance" and the 2023 report records learners failing to see that a machine needs medium-term finance. | 2.3 notes | **Fixed**: short/medium/long-term grouping with matching rule added. |
| C2 | high | Owner's savings asserted to be external finance (the usual convention for sole traders/partnerships is internal). | 2.3 notes, 2.3-002 | **Fixed**: conditioned on business form. Claim revised. |
| C3 | high | Theme 5 taught only abstractions where the reports credit concrete points: exporter help (reasons and methods, ER 2020), government HIV protection (ER 2023), minimum wage set by government with its advantages/disadvantages (ER 2023/2024), consumer protection measures, social benefits incl. jobs (ER 2020), SACU never explained. | 5.1–5.4 notes and cards | **Fixed at generic level**: those knowledge points added; HIV card reframed to government protection. Named Namibian statutes/rates not added (see plan problem P1). |
| C4 | medium | Planned/market economy definitions hedged ("a substantial part") so they did not separate the three systems; no advantages/disadvantages, though the syllabus asks for them. | 1.1 | **Fixed**. Claims revised. |
| C5 | medium | Glossary pairs direct = variable and fixed = indirect; notes said the pairs are "not universal synonyms" and gave a fixed direct cost. | 2.4 notes, 2.4-005 | **Fixed**: glossary pairing taught. |
| C6 | medium | Inventory turnover listed as a liquidity ratio in the 2.4 outline but as efficiency in Annexe A; notes gave only the Annexe grouping. | 2.4 | **Fixed**: both groupings explained. |
| C7 | medium | Economies of scale defined as requiring that diseconomies "must not offset savings" (definition confused with net effect). | 4.5 notes, 4.5-016 | **Fixed**. |
| C8 | medium | Locating abroad: no reasons for going abroad (tariff avoidance, wages, incentives); every case favoured home. | 4.5 | **Notes fixed**; no case where abroad wins (needs a new practice case). |
| C9 | medium | Product life cycle explained only by sales direction. | 4.4 | **Fixed**: stage features and extension strategies. |
| C10 | medium | Rena case labelled a customer-requested evening menu "the owner's preferred" one, so the market/product-orientation contrast taught the wrong label. | 4.1-P01/P02 | **Fixed**. |
| C11 | medium | Answers resting on facts the prompt never gave: shift "tomorrow" (2.6-020), "tabletop target" (2.5-P01), hours 08:00–17:00, pay and the advert address (3.5-007/008/011), "fewer defects" (4.5-004), line graph "requested" (4.2-011), noise (5.1-P01). | as listed | **Fixed**. |
| C12 | medium | Off-topic template splices: product/production in promotion types (4.4-027), cost-plus/competitive/promotional pricing in a penetration/skimming card (4.4-012), training in employer associations (3.4-038), tool segmentation in a clothing case (4.1-012). | as listed | **Fixed**. |
| C13 | medium | Partnership disadvantages omitted unlimited liability and lack of continuity. | 2.1 | **Fixed**. |
| C14 | medium | Self-contradictory planning-office case (told to fetch data it already had). | 1.2-021 | **Fixed**. |
| C15 | medium | 2.1-P01 a(ii) and b asked about sole traders and co-operatives in a partnership-to-company case. | 2.1-P01 | **Fixed**. |
| C16 | medium | 2.5-P04 never named the decision level of buying a second line. | 2.5-P04 | **Fixed** (strategic). |
| C17 | medium | Job advert contents omitted pay. | 3.5 | **Fixed**. |
| C18 | medium | Packaging MISCON could be read as "promotion is not a packaging function". | 4.4-053 | **Fixed**. |
| C19 | low | Minor accuracy/wording: drawings limited to a "sole owner"; limited liability "normally" for all borrowers; 4-point "gap" mislabelled; shareholder in a sole trader's case; white-collar union omits management; glossary synonyms (field/desk research, negotiation = collective bargaining); span of control used in 3.2 undefined; Herzberg case ambiguous; CC share issue; Sera Foods undefined "both investors"; Eha Bags "preparation"; grammar (1.1-P02, 2.6-P02, 3.4-038); "sales dollar". | various | **Fixed**. |
| C20 | low | Depreciation sentence (not in the 6144 2.4 content). | 2.4 | **Fixed** (removed). |
| C21 | low | Weak MISCON 3.1-009 (definitions handed over in the prompt); duplicate DEF cards 2.2-004/007, 4.1-001/003, 4.5-001/002; names reused for different businesses (Tuli, Nela, Omi…); product life cycle drawn with straight segments. | as listed | **Not fixed**: slots are in the work order; cosmetic. |
| C22 | low | "Organisation by systems" defined as project teams; the syllabus names it without defining it. | 2.2-019 | **Not fixed**: unverified; check a Namibian NSSCO text. |

Also checked and sound: cross-references, N$ currency, British spelling, no real companies, no learner-facing exam-frequency claims, MISCON cards discriminate (except C21), every Evaluate card reaches a conditional judgement.

## How the fixes were made

- Only `topics/` learner text was edited (items, content-unit blocks, and claim text where the fact itself changed).
- 63 claims had their `revision` raised. Citers were stamped with the new revision, and those whose text needed no change carry `reviewed_unchanged`.
- Every topic was run through `restamp.py` (repair_note recorded), `render_notes.py` and `run_checks.py`, then republished with `topics/publish_with_assets.py`.
- `curriculum/`, contracts and work orders are untouched. No slot labels changed.
- The fixes themselves have not been reviewed by a second model.

## Plan problems (for Vitalis)

1. **P1: Namibian legal anchors.** The plan's rule "No unsupported current legal detail" (`planning/build_plan_inputs_6144.py`, `prohibited_patterns`) removed every Namibian law and institution from 3.4 and theme 5. The generic knowledge points are now in. Naming the Labour Act 11 of 2007, the Social Security Commission (Act 34 of 1994), the Companies Act 28 of 2004 / BIPA, the Competition Act 2 of 2003, the Environmental Management Act 7 of 2007, and the national minimum wage (N$18.00/hour from 1 January 2025) would strengthen application marks. These were not added because the plan forbids them without a source on file. Decide whether to supply sources and lift the rule for these.
2. **P2: Template authoring.** `topics/authoring_composer.py` builds every card on an objective from one notes paragraph. That produced S5 and S6, and the duplicate-flavoured cards in C21. A trim pass in the authoring tool (case-led answers, real marking points) would raise quality substantially. It is not a correctness problem.
3. **P3: Standard issues** (outside this workspace; report only):
   - `render_notes.py` prints a tooling header in learner notes ("rendered from the approved content units").
   - The subject-profile schema rejects `slot_plan`, `depictions` and `conditioned_mechanisms`, which the runtime accepts (already recorded in `planning/plan-validation.json`).
   - `REVIEWER.md` says the reviewer repairs nothing, while the playbook's step 6 says the reviewer fixes learner text. The playbook was followed.
