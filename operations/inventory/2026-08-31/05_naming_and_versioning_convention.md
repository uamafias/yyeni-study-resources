# 5. Naming and versioning convention

The current folder shows what happens without one: `Business Studies (9609)` and `Business (9609)` for the same subject, `Geography (0460) igcse` beside `IGCSE Geography (0460)`, 40 path segments with stray spaces, 177 with download suffixes, 170 filenames carrying an internal proof label, and `1100-P1.pdf` existing seven times with seven different contents.

## 5.1 Path rules (all zones)

1. **Lowercase kebab-case** for every directory and every generated filename: `9609-business`, `human-resource-management`.
2. **ASCII only.** No `&`, `(`, `)`, `,`, `'`, `’`, `–`. Ampersand becomes `-and-`; parenthesised codes become a leading code segment.
3. **No spaces.** This is the rule that would have prevented 40 of the hygiene defects on its own.
4. **No leading or trailing whitespace, ever.** Trailing-space directories break globs and tab completion; three of them are on the migration path today.
5. **No `(1)`, `-1`, `copy`, `final`, `v2` in a filename** unless the token is part of a formal version field defined below. Download debris is stripped at migration and, where it hid a genuine second copy, resolved by hash.
6. **Depth cap of 8** below the repository root. The deepest current path is 8 (`Question Banks/…/Business Studies (9609)/2024/Oct-Nov (Variant 1)/file.pdf`); the target equivalent is 8 as well, so nothing gets deeper.
7. **Case-only renames are two-step.** macOS is case-insensitive by default: `Business` → `business` must go via a temporary name or the move silently no-ops.

## 5.2 Identifiers

| Thing | Form | Example |
|---|---|---|
| Board | short slug | `cambridge`, `namibia`, `gcse-uk` |
| Level / route | slug | `as-a-level`, `igcse`, `lower-secondary`, `nssco`, `nsscas`, `jsc`, `jsc-legacy`, `jssee`, `sp` |
| Subject directory | `<code>-<subject-slug>` | `9609-business`, `6144-business-studies`, `8245-business-studies` |
| Qualification workspace | `<board-short>-<code>-<route>-<first>-<last>` | `cie-9609-as-2026-2028` |
| Source ID | `SRC-<BOARD><CODE>-<CLASS>-<nnn>` | `SRC-CIE9609-SYL-001`, `SRC-CIE9609-ASM-001`, `SRC-CIE9609-SUP-010` |
| Topic directory | `<topic-number>-<slug>` | `2.1-human-resource-management` |
| Objective ID | `<code>.<topic>.<n>` | `9609.2.1.3` |
| Release ID | `r<YYYYMMDD>.<n>` | `r20260915.1` |

Source-ID classes: `SYL` syllabus, `ASM` AS assessment material, `ALM`/`ALQ` A Level material, `ER` examiner report, `SPC` specimen, `SUP` supporting/third-party. The class letters matter because the scope check reads them.

Subject slugs come from a single table, `shared/subject-slugs.csv`, keyed by board and code. One table is what stops `Business Studies` and `Business` diverging again, and it is also where the misspellings (`Economis (8246)`, `Entreprenuership (8247)`) get corrected once.

## 5.3 Source filenames

**Cambridge assessment — keep Cambridge's own convention unchanged.** `<code>_<series><yy>_<kind>_<paper><variant>.pdf`. It is already canonical, already parseable, already applied to all 1,848 files, and it is what the board itself publishes. Inventing a YYeni scheme here would create a translation problem for no gain. The only change at migration is stripping download debris.

**Namibian assessment — rename.** `<code>-p<paper>-<yyyy>-<kind>.pdf`, e.g. `6144-p1-2022-qp.pdf`, `1131-p3-2015-lt.pdf`. Kinds: `qp`, `ms`, `in`, `er`, `lt` (listening), `tt` (talking/oral). The 170 "First Proof" labels and 185 embedded proof dates move to inventory metadata.

**Syllabuses.** `<board-short>-<code>-syllabus-v<version>-<first>-<last>.pdf`, e.g. `cie-9609-syllabus-v2-2026-2028.pdf`, `nssco-6144-syllabus-2019.pdf`. Where a Namibian syllabus declares only an implementation year, that year is the single date field. **The version and window are mandatory in the filename** — this is the single change that makes document 02's expiry finding visible without opening 44 PDFs.

**Examiner reports.** `<route>-examiner-report-<yyyy>.pdf`, one copy per route per year.

**Supporting / third-party material — preserve original filenames.** Under `supporting/<set-slug>/`, keep the file as it came. Renaming third-party documents destroys their only attribution trail, and their identity lives in the inventory (`source_id`, `original_filename`, `content_hash`, `authority_category`, `reuse_constraints`) where it can be audited.

## 5.4 Generated artifact filenames

Fixed names, so that tooling can find them without globbing: `source_inventory.json`, `objective_registry.json`, `dependency_graph.json`, `glossary.json`, `assessment_evidence.json`, `source_adequacy_and_repair_plan.json`, `contract.json`, `canonical_claim_ledger.json`, `qa_report.json`, `exclusions.json`.

Content units and learning items are per-objective: `content-units/9609.2.1.3.json`, `learning-items/9609.2.1.json`.

Build manifests carry the release: `builds/build_manifest.r20260915.1.json`.

## 5.5 Versioning — the three things that version independently

Conflating these is how a repository ends up unable to answer "which syllabus was this note written from?".

1. **The standard** — `standard/v<semver>[-<stage>]/`. Immutable once released. A build records which standard version it ran under.
2. **The source material** — versioned by the *publisher*, not by YYeni. Cambridge's own `Version 2` is recorded in the syllabus filename and in `likely_syllabus_versions` in the inventory. Content is identified by SHA-256; a source is never edited, only superseded by a newer publisher version, at which point the old file moves to `archive/superseded-syllabi/` and the new one lands in `sources/`. Both hashes stay in the inventory history.
3. **YYeni output** — versioned by release ID inside a qualification workspace. `r<YYYYMMDD>.<n>`, monotonic, never reused, never edited after `state.json` reaches `published`. A correction is a new release that supersedes the old one; the old release stays on disk with `state.json: superseded`.

There is no fourth version number for individual notes. RS-16 makes the structured build the source of truth and the learner document a derived artifact, so the document inherits the release ID and needs no version of its own.

## 5.6 The `latest` pointer

`releases/<qual>/latest` should be a **pointer file** (`latest.json` containing the release ID and its hash), not a symlink. Symlinks survive neither the desktop bridge nor most cloud-sync clients, and a broken `latest` symlink that silently resolves to nothing is a worse failure than a text file someone forgot to update — which a deterministic check can catch anyway.

## 5.7 Dates

ISO 8601 throughout: `2026-08-31`, never `31.08.2026` or `08/31/26`. The 185 filenames currently carrying `dd.mm.yyyy` proof dates are the reason to say so explicitly.

## 5.8 Reserved prefixes

- `_` prefixes a directory that is not subject content: `_quarantine/`, `_examiner-reports/`, `_grade-8/`. It sorts to the top and reads unmistakably as infrastructure.
- `00_`–`99_` numeric prefixes are used **only** in `operations/` report folders, where reading order matters. They are not used in `sources/`, `work/` or `releases/`.

## 5.9 Applying the convention to the six worst current offenders

| Now | Becomes |
|---|---|
| `Question Banks/Namibian Examiner Reports/NSSCO (New) /2023/Examiners Report NSSCO 2023.pdf` | `sources/namibia/nssco/_examiner-reports/2023/nssco-examiner-report-2023.pdf` |
| `Revision Notes/AS/Business (9609)/Chapter Wise Notes Business 9609 AS and A Level Notes /chapter-2-people-in-organisations.pdf` | `sources/cambridge/as-a-level/9609-business/supporting/chapter-notes-2019/chapter-2-people-in-organisations.pdf` |
| `Revision Notes/IGCSE/Chemistry(0620)  IGCSE/…` | `sources/cambridge/igcse/0620-chemistry/supporting/…` |
| `Question Banks/Namibian Curricula/NSSCAS/Economis (8246)/2023/…` | `sources/namibia/nsscas/8246-economics/assessment/2023/…` |
| `Syllabi/Cambridge Curricula/Cambridge AS & A Level/Business Studies 2026-2028-syllabus.pdf` | `sources/cambridge/as-a-level/9609-business/syllabus/cie-9609-syllabus-v2-2026-2028.pdf` |
| `Question Banks/…/Business Studies (9609)/2024/Oct-Nov (Variant 1)/9609_w24_qp_31.pdf` | `sources/cambridge/as-a-level/9609-business/assessment/2024/w24/qp/9609_w24_qp_31.pdf` |
