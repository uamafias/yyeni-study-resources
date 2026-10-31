# 6118 Physics - Step 2 review response

Forwarded by Lotto on 30 October 2026. No operator approval inferred from the
reviewer's recommendation that the tables can be approved.

Subsequent decision, 31 October: Lotto explicitly approved moving on and waived
the Paper 1 duration conflict as non-major/non-blocking. The reviewed tables and
documented working syllabus are accepted for progression; no independent NIED
2026 confirmation or governing duration is inferred. Older pending decisions
below describe the review snapshot. See `../curriculum/operator-decisions.json`.

| Finding | Resolution | Status |
|---|---|---|
| Step 1 cannot close while governing syllabus is unconfirmed | Reopened source completeness in STATUS and inventory; cohort decision belongs to Lotto and is required before Step 3 | Corrected; cohort decision OPEN |
| Claim invisible to teammates | Lotto explicitly approved the prepared tracker-only claim; committed and pushed one added ownership row to shared origin/main, preserving all upstream entries | Published as eedcb74a395a6265403adaf9048a339b4d73ca23; remote SHA verified |
| Source placement authority | Recorded Lotto's supplied files and acceptance of placement; Codex performed the copy | Corrected |
| Recheck 2020/2023 duration | Reopened both PDF covers: 6118/1/20 and 6118/1/23 each state 45 minutes | Verified by agent; governing duration still unresolved |
| Missing stated 53% skills / 47% knowledge balance | Added verbatim source region from printed p.39 [PDF 42] to facts and quoted it in brief | Corrected; verification now 713 quotation records |
| Different report evidence across years | Added key/commentary/inference fields per year and a readable locator table; 2025 has a Paper 1 key despite zero marking-heading keyword hits | Intake corrected; detailed Step 3 classification remains pending |

## Syllabus currency evidence

NIED's live New Curriculum catalogue links the 2018 Physics 6118 syllabus.
The linked PDF's complete pdftotext -layout output matches the local working PDF
byte-for-byte; the PDFs themselves have different hashes. The current publication
link is established. This is not independent confirmation of the cohort's
governing syllabus or absence of a separate amendment. Lotto's decision remains
open; see `../curriculum/syllabus-currency.json`.

## Review coverage

The external reviewer checked tables, counts and file layout. They did not verify
Codex's visual inspections, full transcription JSON, 712 original quotation records
or examiner-report page ranges. The regenerated agent checks pass 713 quotation
records, reflecting the newly added skills-weighting statement; they do not turn
unreviewed areas into externally verified material.

## Carry-forward conditions

- The recall-ceiling denominator and governing Paper 1 duration remain unresolved.
- The 335 specific-objective bullets, 61 raw practical bullets and 30 glossary rows
  are source counts, never card quotas.
- The no-nuclide-formulas restriction belongs only to energy sources. Nuclear
  Physics still requires nuclide notation and decay equations.
- Every future evidence record must distinguish explicit key/marking row,
  commentary, and inference. Inference cannot claim official credit.
- Step 3 awaits the cohort syllabus decision and operator table approval.

## Ownership publication completed

Only `operations/SUBJECT-TRACKER.md`, adding one Physics ownership row on top of
the freshly fetched shared `origin/main`. No Chemistry/Biology history, workspace,
papers, harvest log, standard files or other subject rows were included. The patch
and base SHA are supplied alongside this response. Lotto explicitly approved the
commit/push; the fast-forward push succeeded and git ls-remote verified
origin/main at eedcb74a395a6265403adaf9048a339b4d73ca23. The source and Step 2
approvals remain separate and pending.

## Second source-provenance feedback

| Finding | Resolution |
|---|---|
| Publisher-link claim needs online provenance | Inventory now gives the catalogue URL, linked PDF URL, retrieval date and exact UTC time. Fresh retrieval was 2026-10-30 12:29:40 UTC; headers, metadata and hashes are in source-provenance-audit.json. Catalogue evidence is not cohort validity. |
| April 2024 modification unexplained | Local PDF ModDate is 26 April 2024 at 16:09:42 CAT; publisher PDF ModDate is September 2018; publisher HTTP Last-Modified is May 2024. Producer differs. Cause and historical content changes remain unknown. Current extracted text is equal; non-text content was not compared. |
| Original source intake missing | Manual addition is recorded as reported in the forwarded feedback. No matching harvest entry; original acquisition date, URL and person unknown. Current publisher verification URL is not substituted for original provenance. |
| Duration evidence too broad | Explicitly limited to the 2021 and 2025 one-hour Paper 1 covers; no 2026 duration or governing amendment inferred. |

The original source PDFs remain untouched. The inventory generator preserves
these corrections on regeneration. No substantive Step 3 analysis or further
publication was performed in this correction pass.

## Third source-provenance feedback

| Finding | Resolution |
|---|---|
| Confirm two evidence files actually exist | Confirmed both regular files exist locally and parse as JSON. Inventory now links both explicitly; evidence-file-verification.json records absolute paths, hashes, sizes and uncommitted state. Neither was included in the earlier tracker-only push. |
| Most likely publisher re-upload explanation | Added an inference: May 2024 HTTP Last-Modified with September 2018 embedded metadata most likely reflects re-upload/server-side copying of the existing file with unchanged text. No publisher confirmation or historical snapshot comparison is claimed. |
| Explain differing binaries | Documented Word 2010 publisher versus Quartz local Producer, differing ModDate and file sizes; local re-save/reprocessing is a separate inference, with exact history unknown. |
| Compare page images before diagram-dependent planning | Completed now: 52 page pairs rendered at 144 dpi, all exact RGB pixels identical. Script and per-page metrics in the workspace; this is a current-file rendering check, not historical or cohort-validity proof. |

The reviewer independently verified the publisher download, 52-page 2018 edition,
HTTP Last-Modified, publisher metadata, extracted-layout text equality and binary
inequality. They confirmed the origin-note and cover-evidence scope, but explicitly
did not independently check the local April 2024 Quartz ModDate detail. Their
review did not confirm the two JSON files; this pass supplies local existence
evidence and direct links. The new page-image comparison remains an agent check.
