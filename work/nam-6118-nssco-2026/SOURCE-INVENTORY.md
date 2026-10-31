# 6118 NSSCO Physics - source inventory

Local verification: 30 October 2026. Owner: Lotto N. Nanghonda Jr.
Machine-readable file: `curriculum/source-inventory.json`.
Regenerate from the repository root with:

```bash
.venv/bin/python work/nam-6118-nssco-2026/planning/inventory_sources.py
```

## Ownership and pilot status

Physics was unclaimed at startup; Lotto's ownership is now recorded locally.
The tracker marks NSSCO piloted through Biology's repository review copy, with
learner release still open. The Physics ownership claim was committed and pushed
to shared origin/main on 30 October 2026 with Lotto's explicit approval:
`eedcb74a395a6265403adaf9048a339b4d73ca23`. The remote SHA was verified.
This tracker-only publication did not include the source PDFs or workspace.

## Syllabus

`Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Physics_syllabus.pdf`:
2018 NIED edition, code 6118, Grades 10-11, implementation 2019, first examination
2020 (cover, PDF p.1; publication information, PDF p.2). It carries no
end-of-validity statement establishing currency for our cohort.

**Dated publisher evidence:** retrieved 30 October 2026 at 12:29:40 UTC.
The [NIED New Curriculum catalogue](https://www.nied.edu.na/documents/syllabuses/seniorsecondary/Others/)
has a link labelled “NSSCO Syllabus Physics.pdf” pointing to
[this publisher PDF](https://www.nied.edu.na/assets/documents/02Syllabuses/05SeniorSecondary/PhysicalScience/NSSCO_Physics_syllabus.pdf).
That downloaded PDF identifies the 2018 edition. Its complete extracted layout
text matches the local copy; the binary files differ. This is evidence of what
the catalogue linked on the retrieval date, not a 2026 validity statement.
The URLs, HTTP headers, PDF metadata, exact retrieval timestamp and hashes are
recorded in [source-provenance-audit.json](review/source-provenance-audit.json)
and [syllabus-currency.json](curriculum/syllabus-currency.json). Both files were
confirmed to exist and parse as JSON in this local workspace on 30 October 2026.
They are local, uncommitted working files; the approved GitHub push contained only
the tracker claim, so a separate clone or remote-branch directory check will not
yet contain them. See `review/evidence-file-verification.json` for their absolute
paths, byte sizes, hashes and publication state.
Lotto approved using this documented edition as the working source on
31 October 2026 and instructed proceeding to Step 3. This is an operator decision,
not an independent NIED confirmation of 2026 applicability; the latter remains
an external-authority caveat and is not a further approval gate.

**Local origin:** manually added, as reported in the operator-forwarded review.
The local harvest log has no matching entry for this syllabus (4,500 rows scanned
on 30 October). The person who added it, original acquisition date and original
download URL are unknown. The dated publisher URL above is a verification
reference, not reconstructed original acquisition provenance.

**April 2024 modification:** the local PDF's CreationDate is 18 September 2018,
09:44:23 CAT; its ModDate is **26 April 2024, 16:09:42 CAT**. The local Producer
is macOS Quartz PDFContext; the retrieved publisher copy's Producer is Microsoft
Word 2010 and its PDF ModDate remains 18 September 2018. The HTTP Last-Modified
header on the publisher response is 17 May 2024, 16:58:53 GMT, a separate server
timestamp.

**Inference, not a publisher statement:** the most likely explanation for the
publisher's May 2024 HTTP timestamp together with its September 2018 PDF metadata
is a re-upload or server-side copy of the existing document with unchanged text.
HTTP Last-Modified alone does not prove that explanation, and no historical
2018 snapshot was compared. NIED has not confirmed a re-upload or content history.

**Why the binaries differ:** their embedded Producer and ModDate fields, file
sizes and PDF encoding differ: the publisher file is a 979,057-byte Word 2010
PDF; the local file is a 1,000,664-byte Quartz PDFContext PDF. A local re-save or
reprocessing is the likely explanation for the local binary change. This is a
separate inference from the publisher re-upload; the processing history is unknown.
These metadata/encoding differences explain how file hashes can differ while
the extracted text is identical. They do not establish a revised syllabus.

**Current page-image comparison completed before Step 4:** all 52 pages of both
hash-identified PDFs were rendered with Poppler at 144 dpi and compared as exact
RGB pixel arrays. All 52 page pairs are identical, including diagrams; zero
differing pages. This replaces the earlier “figures not compared” caveat for
these current file versions. The result is limited to that fixed-resolution
rendering and does not prove unchanged historical content, hidden PDF structures
or cohort validity. Reproducible script: `planning/compare_syllabus_pages.py`;
page hashes, dimensions and metrics: [syllabus-page-image-comparison.json](review/syllabus-page-image-comparison.json).

## Assessment sources

Years below are verified from paper covers and report volume identities.
Examination month/series is not stated on the inspected question-paper covers.
All page references below use one-based PDF viewer pages.

| Year | Question papers | Stand-alone mark schemes | Physics section in combined report | Report paper headings |
|---|---|---|---|---|
| 2020 | Papers 1, 2, 3 | None found | PDF pp.467-478 | Papers 2, 3; no separate Paper 1 heading located |
| 2021 | Papers 1, 2, 3 | None found | PDF pp.485-496 | Papers 1, 2, 3 |
| 2022 | Papers 1, 2, 3; First Proof filenames | None found | PDF pp.565-578 | Papers 1, 2, 3 |
| 2023 | Papers 1, 2, 3; First Proof filenames | None found | PDF pp.661-674 | Papers 1, 2, 3 |
| 2024 | Papers 1, 2, 3 | None found | PDF pp.653-668 | Papers 1, 2, 3 |
| 2025 | Papers 1, 2, 3; user-supplied downloads verified 2026-10-30 | None found | PDF pp.643-660 | Papers 1, 2, 3 |

The page ranges end before the next subject, Woodwork 6190, and can include a
trailing blank page. They are section locators, not a statement that every page
contains Physics commentary.

Question papers are under `Question Banks/Namibian Curricula/NSSCO (New)/Physics/`.
The 2021 files `317656.pdf`, `317657.pdf`, `317658.pdf` are respectively Papers
1, 2 and 3, confirmed by the full code/year on each cover.
Reports are under `Question Banks/Namibian Examiner Reports/NSSCO (New) /`;
the space after the closing parenthesis is part of the existing directory name.

Report sections include embedded Paper 1 keys in 2021-2025 and some structured
marking guidance, particularly Paper 3. These are distinct from stand-alone
mark schemes. Their completeness and exact question links must be checked at
Step 3; no claim of complete marking coverage is made here.

## Checks and limits

- 25 official-source PDFs: one syllabus, 18 papers, six combined report volumes.
- Each has a PDF header, a usable text layer, page counts reconciled between
  pdfinfo and extraction, and a distinct SHA-256 recorded in the JSON inventory.
- Paper codes, years and durations were read from covers. Report subject and
  paper headings were located in the text; this is not substantive corpus analysis.
- Filename searches covered repository sources, syllabuses, question banks and
  harvest material. No further official 6118 files were located. This is a local
  availability finding, not a claim that missing documents do not exist elsewhere.
- Two revision-note PDFs exist locally under `Revision Notes/NSSCO/NSSCO Physics (6118)/`.
  They are secondary material, not counted as official assessment sources or read here.
- First Proof filenames are retained as a provenance limitation. No final-print
  equivalence has been established.
- Duration conflict: syllabus printed p.38 / PDF p.41 states Paper 1 is 45 minutes;
  the 2021 and 2025 Paper 1 covers state 1 hour. The 2020 and 2022-2024 covers state 45 minutes.
  Those two one-hour covers are the **only held evidence** of a different duration;
  no amendment or circular establishing a change was located. No inference about
  the governing 2026 duration is made.
- The 2020 and 2023 Paper 1 covers were reopened after reviewer feedback: both
  state 45 minutes and carry identities 6118/1/20 and 6118/1/23 respectively.

## Memo evidence by year - intake classification

| Year | Explicit Paper 1 key | Paper 2/3 commentary entry pages | Inference |
|---|---|---|---|
| 2020 | No separate key located in Physics section | 467 / 473 | Any future inferred guidance must be tagged judgement |
| 2021 | PDF p.485 | 486 / 492 | Same policy |
| 2022 | PDF p.565 | 566 / 575 | Same policy |
| 2023 | PDF p.661 | 663 / 671 | Same policy |
| 2024 | PDF p.653 | 657 / 665 | Same policy |
| 2025 | PDF p.643 | 647 / 656 | Same policy |

The JSON inventory stores excerpts and explicit key/commentary/inference fields
for each year. These are intake locators, not complete answer or mark-allocation
coverage. Detailed marking rows remain to be classified at Step 3. In particular,
the 2025 keyword scan found no marking headings but its Paper 1 key is present;
zero keyword hits must not be described as no memo evidence.

## Source-completeness checkpoint - operator approved 31 October 2026

The three 2025 papers were supplied through Lotto's ChatGPT Work mode download
in `/Users/yyeniai/Downloads/NSSCO 2025 Physics/` and copied byte-for-byte to the
question-bank year folder, retaining the supplied filenames. Paper 1 has 12 pages,
Paper 2 has 16 pages and Paper 3 has 12 pages. Covers identify 6118/1/25,
6118/2/25 and 6118/3/25. Original download URLs were not supplied or established;
the intake origin and SHA-256 values are recorded in the JSON inventory.
Lotto supplied the files and accepted their placement through the forwarded
review feedback on 30 October 2026. Codex carried out the byte-for-byte copy;
the record does not imply Lotto personally copied them or that Codex downloaded
new source documents independently.

Still unavailable: stand-alone mark schemes and an independent NIED statement
specifically confirming 2026 applicability. Lotto has accepted the working source
for progression, so the latter is a documented caveat rather than another gate. Missing schemes
must remain explicit if unavailable; embedded report guidance must not be promoted
to complete schemes by assumption.

On 30 October 2026 Lotto instructed: “we'll use the examiner's reports as the
memos. let's move on to the next step”. This approves using the six Physics
report sections as marking evidence/memos. It does not settle the governing
syllabus or close Step 1. Stand-alone schemes
are not a further permission gate. Embedded keys and marking rows, commentary,
and our judgement must remain distinguishable at Step 3; approval does not
establish complete marking coverage. Syllabus currency remains unconfirmed.
On 31 October Lotto approved moving on: the reviewed Step 2 tables and use of
this syllabus as the working source are accepted for progression. The earlier
pending-approval statements above describe the previous state. Paper 1's duration
conflict was explicitly waived by Lotto as non-major/non-blocking. Neither the
45-minute nor one-hour source value is adopted as the governing 2026 timing.
See `curriculum/operator-decisions.json`. Step 3 is now in progress.
