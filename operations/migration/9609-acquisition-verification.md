# Independent verification — 9609 acquisition, 2026-08-31

Verified from the filesystem, not from the harvester's own report.

## Integrity of what was already here

Re-hashed the whole legacy tree and diffed against the Stage 0 baseline (3,235 files):

| Check | Result |
|---|---|
| Files lost | **0** |
| Files modified in place | **0** |
| Files relocated | 5 — the original 9609 papers, moved into the new level-first folders; hashes matched at their new paths |
| Files added | **363** |
| Stage 2 pilot copies in `sources/` | **20 of 20 unchanged** |

New baseline written: `operations/backups/post-acquisition-2026-08-31/manifest.sha256` — 3,598 files, 4,499,623,324 bytes. The pre-migration baseline is retained.

## Quality of what arrived

All 363 checked with `pdfinfo` and `pdftotext`:

| Check | Result |
|---|---|
| Readable PDFs with a text layer | **363 / 363** |
| Zero-byte, corrupt or image-only | **0** |
| Filenames matching the Cambridge convention | **363 / 363** |
| Syllabus codes present | **9609 only** — no contamination |
| First page mentions 9609 or "Business" | **363 / 363** |
| Byte-identical duplicates within the set | **0** |

The Chemistry near-miss was real and was avoided: no 9701 file reached the folder.

## Coverage — AS scope (papers 1 and 2)

**168 files · 84 complete question-paper + mark-scheme pairs · zero orphans.**

| Series | P1 qp | P1 ms | P2 qp | P2 ms | Variants |
|---|---:|---:|---:|---:|---|
| s20 · w20 | 3 · 3 | 3 · 3 | 3 · 3 | 3 · 3 | 1,2,3 |
| s21 | **4** | **4** | **4** | **4** | 1,2,3,**4** |
| w21 · s22 · w22 | 3 each | 3 each | 3 each | 3 each | 1,2,3 |
| s23 · w23 · s24 · w24 · s25 · w25 | 3 each | 3 each | 3 each | 3 each | 1,2,3 |
| March series (m20–m25) | 10 total | 10 total | 10 total | 10 total | India-only sittings |

June 2021 ran a **fourth variant** — `9609_s21_qp_14`, `_24`, `_34` and their mark schemes. The acquisition manifest in `operations/acquisition/` assumed a maximum of three and would have missed these; the harvest caught them. The manifest cap was wrong, not the harvest.

**51 March-series files** are present (India-only sittings). Same syllabus, same assessment objectives, so they are legitimate AS evidence and add paper variety. Worth an explicit decision rather than an accident: recommend including them, flagged `context_type: march_series_india`.

## Other document kinds

- **Examiner reports: 11** — m20, w20, s21, m21, w21, m22, s22, w22, s23, m23, m25. The most recent June/November report is s23.
- **Grade thresholds: 16** — a kind not in the acquisition manifest at all. Not required by the standard, but useful for calibrating what a mark tariff means in practice.
- **Insert booklets: 42** — all Paper 3 (A Level). 9609 Paper 2 prints its stimulus in the paper, so no AS inserts are expected or missing.

## Manifest reconciliation

**74 of 83 rows satisfied.** All nine outstanding rows are Tier 1:

| Outstanding | Why |
|---|---|
| Examiner reports w23, s24, w24, s25, w25 | Cambridge publishes recent examiner reports only to registered centres via the School Support Hub. Not a harvest failure. |
| Specimen paper 1 and 2, specimen mark scheme 1 and 2 (2026–2028) | Not yet acquired |

Coverage also **exceeds** the manifest: it asked for 2023–2025 and received 2020–2025.

## Two things to fix

**1. Sixteen duplicate PDFs are sitting in `sources/_quarantine/`.** The harvest wrote `sources/_quarantine/2026-08-31_out-of-scope-A-Level/` containing 16 A Level PDFs plus a README. All 16 are byte-identical to files already in the Question Bank, so nothing unique is at risk — but two things are wrong with it:

- `sources/` is the immutable zone; nothing outside the migration should write there, and repository check C2 will flag it.
- Quarantine is for files that cannot be read — zero-byte, encrypted, malformed. Valid A Level material that is simply outside the AS route belongs in `sources/` marked `status: out_of_scope`, which is exactly how the four A Level papers from Stage 2 are already recorded. Putting readable material in quarantine loses that distinction.

Recommended: delete the folder (every file is duplicated elsewhere) and let migration rule R6 place the A Level papers with an out-of-scope status.

**2. The level-first restructure will be undone by Stage 4.** `AS Level/<year>/` and `A Level/<year>/` is a third layout in a repository that already has two. Migration rule R6 derives the target path from the filename, so this folder shape has no effect on where files end up — `sources/cambridge/as-a-level/9609-business/assessment/2024/w24/qp/`. Running `harvest refile` across the other 17 subjects would move several thousand files into a shape that Stage 4 immediately moves again. Recommend skipping the refile step for future subjects and letting the files land wherever the harvest puts them.
