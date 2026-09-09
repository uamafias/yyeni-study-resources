# 1. Current folder inventory

**Root:** `/Users/professor/Documents/YYeni Study Resources`
**Measured:** 2026-08-31
**Totals:** 3,235 substantive files (plus 5 `.DS_Store`), 1,277 directories, **4.0 GB**, 148 empty directories.

## 1.1 File types

| Extension | Files | Note |
|---|---:|---|
| `.pdf` | 3,177 | 98.2% of everything |
| `.json` | 21 | all inside the standard package |
| `.md` | 11 | all inside the standard package |
| `.docx` | 9 | 8 content files + 1 Word lock file (`~$220-M1.docx`) |
| `.py` | 6 | standard package |
| `.pptx` | 4 | NSSCAS Physics teaching decks |
| `.yaml` | 3 | standard package |
| `.txt` | 2 | standard package |
| `.sh`, `.ini` | 2 | standard package |

The repository is effectively a PDF archive. Any generation pipeline built on it is bounded by PDF extraction quality, which is the subject of §1.4.

## 1.2 Top-level branches

| Branch | Files | Size | Character |
|---|---:|---:|---|
| `Question Banks/` | 2,417 | 2,200 MB | Past papers, mark schemes, insert booklets, examiner reports |
| `Revision Notes/` | 615 | 1,935 MB | Third-party and teacher-created notes, by level and subject |
| `Syllabi/` | 158 | 125 MB | Official curriculum documents, four jurisdictions |
| `YYeni_Study_Resource_Generation_Standard_v0.1.0/` | 45 | 0.2 MB | The governing standard |

Note the inversion: `Revision Notes/` is a quarter of the file count but nearly half the bytes, because much of it is image-based (§1.4).

## 1.3 Structure by route

### Question Banks (2,417 files)

| Route | Files | Size |
|---|---:|---:|
| Cambridge AS and A Level | 1,747 | 1,340 MB |
| Cambridge IGCSE | 101 | 20 MB |
| Namibian JSC (Legacy) | 184 | 89 MB |
| Namibian NSSCO (New) | 189 | 421 MB |
| Namibian NSSCAS | 129 | 122 MB |
| Namibian JSSEE | 44 | 20 MB |
| Namibian NSSCO (Legacy) | 10 | 9 MB |
| Namibian Examiner Reports | 13 | 179 MB |

Cambridge subject depth is extremely uneven. The largest banks are Geography 9696 (392 files), Travel & Tourism 9395 (258), Accounting 9706 (247), Sociology 9699 (230), Law 9084 (221) and History 9489 (188). At the other end: **Business Studies 9609 has 5 files**, Computer Science 9618 has 5, Economics 9708 has 7, Physics 9702 has 9, Biology 9700 has 10.

Cambridge question-bank paths are uniformly four levels deep — `<route>/<Subject (code)>/<year>/<series (variant)>/<file>` — and **all 1,848 Cambridge files follow the official Cambridge filename convention** `<code>_<series><yy>_<kind>_<paper><variant>.pdf`. That is the single most valuable structural fact in this inventory: the Cambridge branch is already machine-parseable and can be migrated by rule with no human classification.

Breakdown of those 1,848: 813 mark schemes, 772 question papers, 263 inserts. By series: 944 May/June, 903 Oct/Nov, 1 March. By year: 2020 → 297, 2021 → 372, 2022 → 358, 2023 → 362, 2024 → 412, 2025 → 47.

Namibian question-bank filenames follow no single convention: subject-code stems (`6144-1.pdf`, `1500-P2.pdf`), full descriptive titles carrying internal proof labels (`NSSCO - Business Studies Paper 1 6144-1 - First Proof 08.04.2022.pdf`), and mixtures of both. 170 files carry "First Proof" and 185 carry an embedded proof date.

### Revision Notes (615 files)

| Level | Files | Size | Subject folders |
|---|---:|---:|---:|
| IGCSE | 290 | 1,011 MB | 12 |
| AS | 230 | 474 MB | 11 |
| JSC | 35 | 158 MB | 2 (Grade 8, Grade 9) |
| NSSCO | 27 | 109 MB | 15 |
| SP (Grade 4–7) | 20 | 127 MB | 4 |
| NSSCAS | 13 | 57 MB | 5 |
| `A Level`, `2026` | 0 | — | empty placeholders |

### Syllabi (158 files)

| Jurisdiction | Files |
|---|---:|
| Namibian Curricula (SP, JSC Legacy, JSC New, NSSCAS, NSSCO New) | 76 |
| Cambridge (AS & A Level 20, IGCSE 24, Lower Secondary 6) | 50 |
| Botswana BGCSE | 29 |
| GCSE (UK) | 3 |

**GCSE (UK) is a stub.** Three specification PDFs (AQA Combined Science 8464, Edexcel GCSE Maths, GCSE 9-1 History), no question banks and no revision notes. One of the three is AES-encrypted and cannot be read without handling (§2.3). If GCSE is genuinely in scope, this route needs sourcing before it needs organising.

## 1.4 Text-extraction quality

Measured as characters of extractable text per page over the first three pages. This is a proxy, but a sharp one: a born-digital exam paper yields 1,000–3,000, a scan or an image-export yields under 200.

| Band | PDFs | Interpretation |
|---|---:|---|
| ≥ 800 chars/page | 2,209 | Good text layer, ready for extraction |
| 200–799 | 691 | Partial — headers/tables extract, body may be image |
| 1–199 | 254 | Image-only, OCR required |
| 0 | 8 | No text layer at all |
| unreadable | 15 | Corrupt, empty or encrypted (§2.3) |

By branch:

| Branch | PDFs | Weak (OCR/broken) | Partial |
|---|---:|---:|---:|
| Question Banks | 2,414 | 15 (0.6%) | 475 |
| Revision Notes | 606 | **259 (42.7%)** | 171 |
| Syllabi | 157 | 3 (1.9%) | 45 |

**The official material is clean; the notes are not.** Forty-three per cent of the revision-notes corpus needs OCR before a single claim can be extracted from it. The worst affected folders:

| Folder | Files | Good | Partial | Image-only |
|---|---:|---:|---:|---:|
| `IGCSE/Math (0580) Extended` | 47 | 0 | 11 | 36 |
| `IGCSE/IGCSE Economics (0455)` | 37 | 0 | 3 | 34 |
| `IGCSE/Math (0580) Core` | 41 | 0 | 9 | 32 |
| `AS/Chemistry (9701)` | 43 | 4 | 13 | 26 |
| `IGCSE/IGCSE Computer Science (0478)` | 27 | 0 | 5 | 22 |
| `AS/Physics (9702)` | 32 | 2 | 12 | 18 |
| `AS/Pure Mathematics 1 (9709)` | 18 | 0 | 0 | 18 |
| `IGCSE/IGCSE Business Studies (0450)` | 15 | 0 | 0 | **15** |
| `AS/ (9709) Mechanics` | 8 | 0 | 0 | 8 |
| `IGCSE/1st English (0500)` | 7 | 0 | 0 | 7 |

The IGCSE Business Studies set is instructive: 15 files, 58 MB, every one an image-only print-to-PDF of a commercial revision site (filenames carry the source's page slugs and asset hashes). High byte cost, zero extractable text, and third-party copyright — the worst combination in the repository.

By contrast `AS/Business (9609)` is 14 files of which 12 have a good text layer. The pilot subject is one of the better-conditioned note sets, which is part of why it is a sensible pilot.

## 1.5 Empty directories (148)

Scaffolding created ahead of content that never arrived:

- **Entire subject trees, no files at all:** Cambridge AS French 8028 (30 dirs), Cambridge AS German 8027 (18), IGCSE German (16), IGCSE Accounting 0452 (14 of 16 year/variant dirs), IGCSE Geography 0460 (14), IGCSE Sociology 0495 (5), IGCSE Travel & Tourism 0471 (5).
- **Level placeholders:** `Revision Notes/A Level`, `Revision Notes/2026`.
- **Subject placeholders:** 8 NSSCAS subjects, 1 NSSCO subject, 4 AS Chemistry topics, 20 SP Grade 4–7 subjects, `IGCSE Business Studies (0450)/First teaching 2025-First Exams 2027`.
- One is a genuine sign of intent worth noting: `First teaching 2025-First Exams 2027` shows someone already knew IGCSE Business 0450 has a new edition coming.

Empty directories are harmless but they make the tree look like coverage that does not exist. They should not be recreated in the target structure (migration rule R12).

## 1.6 Non-PDF content files

Thirteen files outside the standard package are not PDFs and need format-specific handling:

| File | Issue |
|---|---|
| `Question Banks/.../IGCSE Geography (0460)/2024/May-June (Variant 1)/0460_s24_qp_11.docx` | A question paper as `.docx` — almost certainly not the official artifact |
| `Question Banks/Namibian Curricula/JSC (Legacy)/Life Science/2019/~$220-M1.docx` | Word lock file; delete candidate |
| `Question Banks/Namibian Curricula/NSSCAS/Computer science (8231)/2021/...Paper 2...docx` | Official paper supplied as `.docx` |
| `Syllabi/Namibian Curricula/JSC (New)/JSAccountingSyllabusDecembe2025.docx` | Duplicate format of the same syllabus PDF; filename also misspelt ("Decembe") |
| 4 × `.pptx` in `Revision Notes/NSSCAS/NSSCAS Physics (8225)` | Teaching decks, Sept 2020, theme 1 topics 1.2/1.5/1.6/1.7 only |
| 4 × `.docx` in `Revision Notes/SP` and `NSSCAS Geography` | Home Ecology Grades 5–7 (40 MB combined) and NSSCAS Geography notes |

## 1.7 Files over 20 MB (13)

Relevant because the desktop bridge writes at most 20 MB per file, so these cannot be round-tripped through a cloud step; they must be handled in place.

`Was the Weimar Republic Doomed from the Start_v1.pdf` (48.2 MB), Home Economics Grade 8 (34.2 MB) and Grade 9 (33.8 MB), NSSCO Examiners Report 2023 (33.9 MB, held in **four** copies), NSSCAS Physics Notes (25.5 MB), NSSCO Examiners Report 2020 (24.0 MB, **four** copies), NSHE Grade 5 Tasks (21.1 MB).

## 1.8 What the inventory says about readiness

1. The Cambridge question-bank branch is the strongest asset in the repository: large, well-named, machine-parseable, and 99.4% text-extractable. It is ready for Stage 4 assessment mining as soon as it is addressable by qualification.
2. The revision-notes corpus is the weakest: 42.7% needs OCR, most of it is third-party material of unverified licence, and the folder names embed no version information.
3. Coverage and depth are inversely correlated with YYeni's stated priorities. Subjects with 200–400 papers (Geography, Travel & Tourism, Law, Sociology, Psychology) have zero revision notes; subjects with notes (Business, Economics, Physics, Chemistry, Maths) have thin question banks. Neither side of the repository was built with the other in mind.
4. Nothing in the current layout records syllabus version, exam window, route or level as data. Every one of those is either implicit in a folder name or absent — which is precisely what RS-02 (scope lock) forbids.
