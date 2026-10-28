# 6145 NSSCO Economics — Codex cross-check of Claude additions

Date: 28 October 2026. Workspace: `work/nam-6145-nssco-2026/`. Authored baseline: `c7d6bb1`.

**Verdict: publish for the existing approved package, with the coverage and diagram decisions still open.** Claude’s substantial coverage additions are retained. This focused read does not declare the flashcard coverage complete or replace Claude’s whole-subject review.

## Scope and evidence

Read the substantive additions in 101 teaching blocks across the subject, and all 52 changed canonical answers identified by the baseline comparison. Read the 2024 Economics examiner-report homogeneity passage and the syllabus profit-maximisation glossary. The reading manifest lists IDs and hashes. Formatting-only edits and every unchanged card were not re-reviewed. No authoring script was run.

The playbook’s Step 6 repair instructions govern this work; its permission to repair canonical learner text takes precedence over the reviewer role’s report-only instruction. Curriculum, profiles, approved planning files, contracts and work orders remain unchanged against the authored checkpoint. No 0455 path was edited. No commit, push or classroom import was performed.

## Repairs

| Finding | Canonical locations | Resolution |
|---|---|---|
| Private-company transfers described as always needing other shareholders’ agreement | 2.1.2-B05; 2.1-012 | Transfer restrictions are set by the articles. |
| CC natural-person rule stated without statutory representative exceptions | 2.1.2-B13; 2.1-016 | Retain 1–10 members and limited liability; qualify normal individual membership. |
| Conciliation could be mistaken for the complete strike procedure | 2.2-B06 | Identify disputes of interest, attendance/waiting/notice/rule requirements and essential-service restrictions. No legal-procedure checklist is taught. |
| Homogeneity overstates literal identity of every genuine note | 2.3.2-B13; 2.3-029; P02(e); claim 2.3-35 | Preserve the examiner-required appearance/recognisability distinction, while allowing approved note series and differing serial numbers. |
| Cheques presented as a current Namibian payment service | 2.3.2-B03; 2.3.5-B03 | Distinguish historical textbook descriptions from Namibia’s phased-out cheque payments; current examples use electronic services. |
| Old exchange name presented as current | 2.3.5-B02 | Give Namibia Securities Exchange, retaining former Namibian Stock Exchange name for syllabus recognition. |
| MC = MR alone asserted sufficient for maximum profit | 5.1-B01; 5.1-001; claim 5.1-01 | Explain extra output changes from increasing to reducing profit; retain the syllabus equality. |
| NAMFISA remit too broad | 6.3-B03 | Specify non-banking financial services. |
| Inflation gains for borrowers stated without loan terms | 7.1-B04 | Qualify fixed nominal debts and inflation relative to interest terms. |
| National Income equated to GNP minus depreciation without valuation basis | 7.3.1-B03; 7.3-012; claim 7.3-11 | Specify conventional factor-cost basis; market-price figures need tax/subsidy adjustment. |
| Age dependency equated to actual dependants per worker | 8.1-B04 | Use dependent-age bands over working-age population; distinguish actual work/support. Removed repeated prose to keep this unit inside budget. |

Three claim revisions were raised, citing `claims_seen` updated, and unchanged citing texts explicitly recorded as reviewed unchanged. Edited blocks/items were restamped and notes regenerated. `codex-additions-repairs-6145.json` records 19 changed canonical objects; the later exchange-name edit and repeated-prose removal are documented in this table and their repair notes.

## Namibian fact checks

Primary sources checked online on 28 October 2026; these links are review evidence, not additions to the approved assessment corpus.

- [BIPA registration guidance](https://www.bipa.na/business-registration/) supports CC member limits and company suffixes. [Companies Act, section 22](https://namiblii.org/akn/na/act/2004/28/eng@2023-07-21) supports restrictions under articles. [Close Corporations Act, sections 2 and 29](https://namiblii.org/akn/na/act/1988/26/eng@2023-07-21) supplies the membership exceptions. The Companies Act’s general 20-person rule supports the qualified partnership statement; exceptions are not expanded into new syllabus content.
- [Labour Act, sections 74–75](https://namiblii.org/akn/na/act/2007/11/eng@2023-03-15) supports the conciliation/procedure distinction and essential-service restriction.
- [Bank of Namibia monetary-policy explanation](https://www.bon.com.na/Bank/Monetary-Policy.aspx) supports price stability, repo and the parity constraint. [Its exchange-control FAQ](https://www.bon.com.na/Informations/FAQ/Exchange-Control.aspx) identifies both currencies as legal tender. [FNB’s phase-out notice](https://www.fnbnamibia.com.na/downloads/namibia/promotions/FNBNamibiaChequesPhasing.pdf) confirms cessation of cheque services in 2019; the [BoN legal-framework page](https://www.bon.com.na/Bank/National-Payment-System/Legal-Framework/Abolishment-of-Payment-by-Cheque-Act.aspx) identifies the later legislation. [Modified banknotes](https://www.bon.com.na/Currency/2015-modified-N$10-and-N$20-banknotes.aspx) also show why literal identity is too strong.
- [NSX history and structure](https://nsx.com.na/about/history-structure/) supports its functions, Windhoek address and 2024 rebranding.
- [NSA CPI bulletin](https://nsa.org.na/wp-content/uploads/2026/01/Namibia-CPI-Bulletin_-December-2025-SIGNED.pdf) supports monthly CPI publication. [NSA June 2024 trade bulletin](https://nsa.org.na/wp-content/uploads/2024/08/Namibia-Trade-Statistics-Bulletin-June-2024_Dissemination-1.pdf) supports the teaching examples of mineral exports and South Africa as a principal import source. These are historical trade patterns, not a verified ranking for every month of 2026.
- [NaCC enforcement](https://nacc.com.na/divisions/enforcement-exemptions-and-cartels), [NSI mandate](https://www.nsi.com.na/), [NAMFISA complaints](https://www.namfisa.com.na/educates/focus-areas-complaints/) and [CRAN complaints](https://www.cran.na/consumer-complaints-regulations/) support the named institutional examples and distinguish their remits.
- [SSC](https://www.ssc.org.na/) identifies maternity, sick and death benefits. [Employment Equity Commission](https://eec.gov.na/home) supports the affirmative-action law and designated groups. Individual eligibility, amounts and an exhaustive legal compliance review are outside this learner-content check.

## Verification after repairs

- **28/28 PUBLISH; zero deterministic failures.** C-18 warns in every topic. C-26 now warns in eight topics, affecting ten content units.
- **Word counts corrected:** 52 stored content-unit totals differed from actual canonical text. Recalculated using whitespace-separated block words, as the author audit does. Ten units remain outside their approved ranges: 3.1, 3.3.3, 3.5, 4.1, 4.2.2, 5.4.1, 5.4.2, 6.1.1, 7.4 and 7.4.3. This is now visible in QA; publication does not mean every budget is met. See the word-count audit for exact deltas.
- C-35, C-41 and C-43 remain `not_run` in every topic. They are not passes. Machine semantic-review entries still say pending; the narrative reports record human/model reading.
- 580 slot IDs each have exactly one item; all labels explicitly fixed in the work order match. Performance-task labels not explicitly specified there were not independently inferred.
- Re-published **580 items and 67,193 rendered-note words**. All published item fields match their canonical fields, except generated objective titles. Publication hashes are recorded separately from the stale author audit.
- Copied-wording tool: **40 cached subject-only assessment extracts; zero matches of eight or more words**. The syllabus was excluded.

## Proposed next scope for Vitalis

Recommend reopening Step 4 for P1 and P3 together, then returning with generated slot counts, AO balance and diagram work orders for approval. Preserve existing IDs and Claude’s corrections.

| Topic | Coverage to add or strengthen in the plan |
|---|---|
| 2.2–2.3 | Industrial action; central-bank functions/repo; exchange functions |
| 4.1–4.2 | Occupational/geographical mobility; gross/net pay; piece rates |
| 5.1, 5.3–5.4 | Value added; total/average revenue definitions; external economies |
| 6.1–6.2 | Merit goods, privatisation and named direct-tax examples |
| 7.1, 8.1–8.2 | Inflation definition; dependency ratio; HDI |
| 9.1 | Named protection methods |
| Diagrams | PPC; LRAC; labour market; demand/supply shifts; binding price controls, including minimum wage |

Also review the one-mark elasticity calculation slots and template definition terms. For P2, propose a subject-specific handover instruction requiring each objective’s named examinable points and a notes-to-card coverage reconciliation; do not edit shared standard files in this subject review. Handle the ten word-budget warnings during the same approved revision, preserving teaching content.

The playbook requires a person’s verdict-read and plan-approval decisions. Those boxes remain unticked. Current review corrections can be saved separately from a later plan extension when Vitalis requests the Git checkpoint.
