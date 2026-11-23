# Source inventory for Namibia AS Mathematics 8227

15 November 2026. Owner Vitalis; investigator Codex. Syllabus: NIED December 2020,
Grade 12, implementation/first examination 2021. Scope: whole-syllabus problem-type
mapping; current assessment corpus window 2021–2025, with later availability to check.

Current analysis update: 20 registered files (19 PDFs and one unusable HTML file),
five annual reports, complete local OCR of the Namibia textbook, and the first
119-question/250-part structural map are now available. See [corpus analysis](corpus-analysis.md).
Owner instruction authorised steps 1–3 with visible gaps; it did not certify source completeness.

Exact file identities, SHA-256, byte types, page counts, extraction metrics and
inspection scope are in [source-holdings.json](source-holdings.json). This inventory
distinguishes readable holdings from documents actually analysed. Corpus completeness
is pending; see [acquisition gaps](acquisition-gaps.md).

## Syllabus and assessment authority

Existing path:
`Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf`.
33 pages; SHA-256 `c53e77d60f8de1410163c4fccbfa1c41ae88479fb9a53e2bd26ef1bcc727fb30`.
The current [NIED NSSCAS index](https://www.nied.edu.na/documents/syllabuses/seniorsecondary/NSSCAS/)
links to the same edition. A fresh official download in `_harvest/inbox/` matches
the local file byte-for-byte. No claim is made that every separate amendment or
subject circular has been located.

Front matter, learning-content and assessment pages were read before paper/source
analysis. Exact extracted pages are retained in `syllabus-page-evidence.json`;
mathematical extraction can scramble powers, fractions and absolute-value bars.
The assessment table was rendered and visually checked.

| Item | Source locator and inspected fact |
|---|---|
| Edition | PDF pp1–2: 8227, Grade 12, December 2020, implementation/first examination 2021 |
| Content | PDF pp7–16 / printed pp4–13: Mathematics 1 has nine topics; Mathematics 2 has six |
| Assessment | PDF p17 / printed p14: one area, technique with application, with eleven listed abilities; abilities may be assessed in either paper |
| Papers | PDF p18 / printed p15: both compulsory, no choice; each 75 marks, two hours and 50% |
| Calculator/precision | Same page: non-programmable scientific calculator; default nonexact answers three significant figures, angles one decimal place unless specified |
| Command words | No standalone command-word table found in the read content/assessment sections; complete extracted syllabus searched; no standalone table found (author finding, not an invented official list) |

No separate AO weighting split has been inferred from paper/topic names. These
source notes do not replace the owner syllabus checkpoint or verified objective registry.

## Examination holdings

Papers are in `Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/<year>/`.

| Year | Paper 1 | Paper 2 | Schemes/report position |
|---|---|---|---|
| 2021 | Existing PDF, cover verified | Existing PDF, cover verified | Both filenames say First Proof; official combined report acquired; separate schemes missing |
| 2022 | Existing PDF, cover verified | Existing PDF, cover verified | Proof-labelled filenames; report acquired; standalone schemes missing |
| 2023 | Existing PDF, cover verified | Existing PDF, cover verified | Proof-labelled filenames; report acquired; standalone schemes missing |
| 2024 | Existing `8227-1.pdf` | Existing `8227-2.pdf` | Covers verified; report acquired with P2 award excerpts; standalone schemes missing |
| 2025 | Newly acquired `8227-1.pdf` | Newly acquired `8227-2.pdf` | Covers verify 2025/8227/75 marks/two hours; official combined report acquired; separate schemes missing |

The 2025 files were acquired through the public annual folders linked by
[Namibia Papers](https://www.namibiapapers.com/nssca/mathematics), not from an
authenticated school account. Their covers identify DNEA; archival provenance
does not independently certify final-version equivalence. The exact download URLs
and run evidence are retained in the Harvester manifest/log.

Ten papers passed Harvester's integrity sweep: no corruption or image-only files
reported. Covers were inspected for year/code/component; all 119 connected questions and 250 parts now have a first structural reading and
proposed objective/pattern links. Not every formula/diagram has been visually
verified, and mathematical/marking correctness is not independently accepted.

Official reports acquired under `Question Banks/Namibian Examiner Reports/NSSCAS/`:

- 2021: `NSSCAS_2021_Examiners.pdf`, 256 pages; Mathematics Paper 1 starts PDF p231,
  Paper 2 p236. Remaining Mathematics section boundaries require confirmation.
- 2022: `NSSCAS_Examiners_Report_2022.pdf`, 332 pages; Mathematics P1 starts PDF p301, P2 p307.
- 2023: `NSSCAS_Examiners_Report_2023.pdf`, 356 pages; Mathematics P1 p321, P2 p330.
- 2024: `NSSCAS_Examiners_Report_2024.pdf`, 362 pages; Mathematics P1 p325, P2 p335.
- 2025: `NSSCASExaminersReport2025.pdf`, 382 pages; Mathematics Paper 1 starts PDF
  p345, Paper 2 p355; Physics begins p365. Selected comments were sampled, not fully mined.

Commentary alone is not a complete marking scheme. However, report award tables
were located for 24 questions: four in 2021 P2, nine in 2023 P2 and eleven in 2024 P2.
Exact excerpt pages are linked in `question-analysis.json`. Method/accuracy awards,
alternatives and follow-through require transcription/reconciliation from those
actual tables or other schemes; unverified rules remain proposals.

## Textbook ingredients

The supplied Downloads file was copied, preserving the original, to:
`sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf`.

- Printed title: Cambridge International AS & A Level Mathematics, Pure Mathematics
  2 & 3, second edition. Author Sophie Goldie; series editor Roger Porkess.
- Publisher Hodder Education, 2018; ISBN 9781510421738; 371 PDF pages.
- SHA-256 `f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85`;
  saved copy matches Downloads byte-for-byte.
- Front matter/contents PDF pp3–7 read; title page and PDF p249 / printed p235
  visually inspected. The latter includes vector representations, Figures 10.1–10.3.
- Original Cambridge curriculum identity is retained. Use only material mapped to
  current Namibia objectives. A Cambridge A-level chapter is neither automatically
  excluded nor automatically in scope for Namibia AS.
- User-supplied source for internal analysis. Publisher permissions for copied
  exercise text/artwork or learner redistribution have not been established.
  Author original problems/diagrams; flag any proposed direct reuse separately.

The local `Revision Notes/NSSCAS/NSSCAS Mathematics (8227)/y=mx+c AS Level .pdf`
contains a Google 403 HTML page, not a textbook. It remains preserved and excluded
from usable holdings.

### Namibia textbook supplied 15 November 2026

The user supplied `Y=mc as textbook.pdf` at the repository root. This is now the
registered Namibia textbook source (`8227-SRC-017`); it does not overwrite the old
HTML/403 file. The root copy and both Downloads files (`Y=mc as textbook.pdf` and
`Y=MX+C  AS LEVEL TEXT BOOK GALLANT.pdf`) match byte-for-byte.

- Cover: **y=mx+c to success: Advanced Subsidiary Level Mathematics Grade 12**, Karen
  D’Emiljo; Namibia Senior Secondary Phase; new syllabus starting 2021.
- 663 PDF pages, 148,002,847 bytes; SHA-256
  `0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f`.
- PDF pp1–11 inspected visually, including introduction/contents. Contents pp5–10
  identify thirteen chapters across Mathematics 1 and Mathematics 2, followed by
  answers/index. Publication/impression were not visible in these scan pages. The back cover
  PDF p663 was subsequently inspected visually and confirms ISBN 9789991696645.
- PDF p150 / printed p138 has function diagrams/graphs; PDF p326 / printed p314
  has worked integration and practice exercises. These sampled pages are visually
  readable. All 663 pages extract only scanner labels or blank text; scanner text
  must not be mistaken for a usable mathematical text layer. Tesseract is not on
  PATH. A complete 663-page local Apple Vision OCR derivative has now been
  generated and indexed, with per-page source identity and hashes. Mathematical OCR
  remains unreliable; see `ocr-validation.json` and `textbook-exercise-index.json`.
- Use visual reading or a checked OCR derivative linked to this exact hash. Record
  PDF and printed locators individually; do not assume a constant offset throughout
  the scan. Whole-scan completeness, individual mathematical claims and exercises
  still require inspection during analysis.

This resolves the missing Namibia textbook acquisition, while detailed syllabus
mapping, extraction preparation and any teacher-guide acquisition remain open.
Original problems/diagrams remain the intended learner outputs; copying source
wording/artwork requires a separately established basis.

The newly acquired NIED 2022 NSSCAS textbook catalogue is at
`sources/namibia/nsscas/8227-mathematics/support/NIED_NSSCAS-Textbook-Catalogue_2022.pdf`.
PDF p18 / printed p15 was checked as text and rendered table. It identifies:

| Title | Publisher / author | Learner book ISBN | Teacher guide ISBN |
|---|---|---|---|
| Living Mathematics AS Level | Oxford University Press; J. M. E. Du Toit et al.; 2020 | 9780190746957 | 9780190732400 |
| Y=mx+c to success AS Level | Straightline Publishing; K. D’ Emiljo; 2020 | 9789991696645 | 9789991696652 |

The y=mx+c learner-book title/author now matches the supplied scan described above;
the back cover now confirms its learner-book ISBN, while impression remains unconfirmed. The other listed books/guides remain
acquisition leads, not verified current availability or prices. The [publisher](https://www.straightlinepublishing.co/)
and licensed ebook listings are leads for lawful access; no purchase was made.

## Acquisition and inspection evidence

YYeni Web Harvester 1.3.0, existing installation beside this repo. Health check
outside the sandbox verified dependencies and Chromium. Network/browser failures
inside the sandbox were retried with approved escalation.

- `_harvest/manifests/nsscas-8227-acquire-2026-11-15.csv`: four acquisitions, all successful;
  report `_harvest/reports/run_20261115-161611-114.md`.
- `_harvest/manifests/nsscas-8227-support-2026-11-15.csv`: official catalogue and
  verification copy of syllabus, both successful; report
  `_harvest/reports/run_20261115-175822-651.md`.
- `_harvest/manifests/nsscas-8227-report-leads-2026-11-15.csv`: uncurated discovery,
  including an unrelated NSSCO link; not an acquisition list to run wholesale.
- `_harvest/reports/integrity_2026-11-15.md` and `.tsv`: ten-paper sweep.

The Ministry report page timed out in both web access and Harvester browser fallback.
Initial Harvester anchor discovery did not expose the NANSO embedded documents.
A subsequent manual inspection of the public page source located its explicit
`data-embed-download-url` attributes. Those observed links were passed to the
existing Harvester; all three reports were acquired successfully. Manifest:
`_harvest/manifests/nsscas-8227-report-gaps-2026-11-15.csv`; run report:
`_harvest/reports/run_20261115-185311-464.md`. No substitute acquisition system,
paid research call, account login or paywall bypass was used.

Read-only connected Drive searches for 8227, NSSCAS report filenames and the known
Mathematics folder found existing-source leads, not the missing schemes/reports.
Search result metadata was not treated as document evidence or source possession.


Repair round 2 update, 16 November 2026: SRC-018–020 are third-party mirror
copies with DNEA covers verified; official-copy equivalence remains unverified.
Owner decision 5 accepts both commercial books and their OCR in this shared
repository; no general public textbook reuse licence is inferred. Exact attributed
examination-question reuse is separately authorised by owner request N2.
The source register is rebuilt from frozen tools/source_holdings_inputs.json.
Cambridge evidence and its separate hashes/locators are in cambridge-evidence.json;
corpus discovery completeness is described in cambridge-corpus-index.json.
