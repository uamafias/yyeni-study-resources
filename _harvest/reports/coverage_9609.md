# Business Studies (9609) — coverage, 2020–2025

**Source:** pastpapers.co · **Acquired:** 2026-08-31 · **Files:** 363 · **Integrity:** 363/363 parse with a text layer

Structure: `AS Level/` (papers 1–2) · `A Level/` (papers 3–4, with inserts) · `Examiner Reports/` · `Grade Thresholds/`

| Series | QP | MS | Inserts | Examiner report | Grade threshold |
|---|---|---|---|---|---|
| 2020 March | 0 | 0 | 0 | yes | — |
| 2020 May-June | 9 | 9 | 3 | **not published** | — |
| 2020 Oct-Nov | 9 | 9 | 3 | yes | yes |
| 2021 March | 3 | 3 | 1 | yes | yes |
| 2021 May-June | 12 | 12 | 4 | yes | yes |
| 2021 Oct-Nov | 9 | 9 | 3 | yes | yes |
| 2022 March | 3 | 3 | 1 | yes | yes |
| 2022 May-June | 9 | 9 | 3 | yes | yes |
| 2022 Oct-Nov | 9 | 9 | 3 | yes | yes |
| 2023 March | 4 | 4 | 1 | yes | yes |
| 2023 May-June | 12 | 12 | 3 | yes | yes |
| 2023 Oct-Nov | 12 | 12 | 3 | **not published** | yes |
| 2024 March | 4 | 4 | 1 | **not published** | yes |
| 2024 May-June | 12 | 12 | 3 | **not published** | yes |
| 2024 Oct-Nov | 12 | 12 | 3 | **not published** | yes |
| 2025 March | 4 | 4 | 1 | yes | yes |
| 2025 May-June | 12 | 12 | 3 | **not published** | yes |
| 2025 Oct-Nov | 12 | 12 | 3 | **not published** | yes |

## Known gaps

**Examiner reports — 11 of 18 series.** Missing: 2020 May-June, 2023 Oct-Nov, 2024 March, 2024 May-June, 2024 Oct-Nov, 2025 May-June, 2025 Oct-Nov.

These are not a harvest failure. Cambridge publishes recent examiner reports only to registered centres through the School Support Hub, so public aggregators do not carry them. They were requested and reported as absent, not skipped. If the centre login is available, they can be added by hand into `Examiner Reports/<year>/` using the same `9609_<series>_er.pdf` name.

**Chemistry contamination, excluded.** The source's `business-9609/2020-march` index actually serves Chemistry (9701) files. 12 documents were excluded by the rule's `include = { code = "9609" }` subject lock and are listed in the routing output. Business Studies has no March 2020 series.

## Reproducing

```bash
harvest route all-9609.csv --rules cambridge-question-bank --out qbank-9609-full.csv
harvest tree qbank-9609-full.csv
harvest run  qbank-9609-full.csv
harvest verify "Question Banks/.../Business Studies (9609)"
```