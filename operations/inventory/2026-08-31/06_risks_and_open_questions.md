# 6. Risks and open questions

Severity: **HIGH** = blocks the pilot or risks losing/misrepresenting content. **MEDIUM** = will cause rework. **LOW** = tidy-up.

## 6.1 Risks found in the actual folder

### R-01 — HIGH — The pilot qualification has almost no assessment material
Cambridge AS Business 9609 holds five assessment files: one AS Paper 2 mark scheme from the 2020 Oct/Nov series (its question paper absent), and four A Level papers the AS-only route excludes. No AS question paper, no examiner report, no specimen paper.

RS-05 requires assessment mining where materials are available; RS-31 blocks publication while a required stage is incomplete. The pipeline will correctly refuse to publish, which means **the first real task on the pilot is acquisition, not generation.**

Minimum acquisition list to make the pilot viable: 9609 Papers 1 and 2 question papers and mark schemes for the 2023, 2024 and 2025 series (both variants where available), plus examiner reports for the same, plus the specimen papers for the 2026–2028 syllabus. That is roughly 24–30 documents. Note the repository holds 247 Accounting 9706 and 392 Geography 9696 files, so the acquisition route clearly exists and has simply not been pointed at Business.

*Decision needed:* acquire for 9609 first and keep it as the pilot, or pilot on a subject where assessment material is already deep (Accounting 9706 and Economics 9708 are both current to 2028 and Accounting has 247 files) and return to Business once papers are in hand.

### R-02 — HIGH — The supplied 9609 notes track a superseded syllabus edition and omit a fifth of the course
Confirmed by reading the files: chapter titles use pre-2023 wording ("People in Organisations" for what is now *Human resource management*; "Operations and Project Management", where project management is A Level content), chapter 2 uses legacy numbering ("1.6"), and there is no chapter 5, so topic 5 *Finance and accounting* has no chapter notes. Only the ZNotes PDF carries substantive finance content, and its text layer is partial.

Under RS-10/RS-11 the honest expectation is that most objectives will be scored 0–2 and receive `regenerate` or `generate-gap`, not `retain`. That is the standard working as designed, but it changes the effort estimate for the pilot substantially and should be written into the topic contract before authoring, not discovered at semantic review.

*Decision needed:* confirm that "regenerate most of it" is an acceptable pilot outcome, and whether an endorsed textbook will be licensed as a conceptual source (which changes the answer for topic 5 entirely).

### R-03 — HIGH — 25 of 44 Cambridge syllabi expire after the November 2026 series
Read from inside each PDF. Anything generated from those 25 is out of scope for 2027 candidates. The pilot subject (9609 v2) is safe to 2028; Geography 9696, History 9489, Psychology 9990, Sociology 9699 and Travel & Tourism 9395 — which between them hold 1,179 of the 1,747 AS/A Level question-bank files — are not.

*Decision needed:* whether syllabus refresh becomes a standing calendar task (recommended: a scheduled check each January and July against the board's published syllabus list).

### R-04 — HIGH — Copyright and reuse are unrecorded across the whole repository
The `source_inventory` schema has a `reuse_constraints` field and nothing currently populates it. The repository contains Cambridge past papers and mark schemes (board copyright), commercial revision-site exports (15 IGCSE Business files are print-to-PDF captures of a paid revision site, complete with its asset IDs in the filenames), an apparent scan of a commercial revision guide, watermarked third-party notes, and unattributed chapter notes.

If YYeni publishes learner-facing resources derived from these, the exposure is real and it is not mitigated by the resource being "generated". RS-12 makes it worse, not better: it requires claims to be source-backed, which means provenance is recorded — so a derivation from unlicensed material is documented in the claim ledger.

*Decision needed (this is `TEAM_REVIEW_NOTES.md` items 2 and 3, and it is now urgent):* which sources are approved for derivation, which for reference only, and which must be removed from the derivation path. Recommendation: populate `reuse_constraints` during migration (rule R9 forces the question per file) and add a deterministic check that no `publishable` claim traces to a source marked `do_not_redistribute` or `licence_check_required`.

### R-05 — MEDIUM — 170 Namibian papers are labelled "First Proof"
Filenames say "First Proof" with a pre-exam date (e.g. `NSSCO - Business Studies Paper 1 6144-1 - First Proof 08.04.2022.pdf`, dated April for a paper sat later in the year). These may be pre-publication drafts rather than the sat papers. If so, their `authority_category` is not `official_assessment`, and mining them for mark tariffs and command words could teach a version of the paper that candidates never saw.

*Decision needed:* confirm with NEACB or the source of these files whether "First Proof" versions match the final papers. Until confirmed, migrate them with `authority_category: uncertain` and `quality_flags: ["internal_proof_label"]`.

### R-06 — MEDIUM — 42.7% of the revision-notes corpus needs OCR
259 of 606 note PDFs have no usable text layer; a further 171 are partial. At 1,500 pages-plus this is a real cost, and OCR quality on multi-column revision material with diagrams is uneven.

*Decision needed:* the OCR toolchain, and whether OCR is done at migration (once, into `sources/` alongside the original as a `.ocr.txt` sidecar) or on demand per build. Recommendation: at migration, as a sidecar — the original stays immutable, the text becomes cacheable, and the extraction status in the inventory becomes true rather than aspirational.

### R-07 — MEDIUM — Subject coverage and note coverage barely overlap
The six largest question banks (Geography, Travel & Tourism, Accounting, Sociology, Law, History — 1,536 files) have **zero** revision notes. The subjects with the most notes (IGCSE Maths 88, AS Chemistry 43, IGCSE Economics 37) have thin banks. Whatever the standard does, it cannot generate assessment-aligned material for a subject with no papers, or mine adequacy for a subject with no notes.

*Decision needed:* a build order that prioritises subjects where both exist. On current data the strongest candidates are Accounting 9706 (247 papers, current to 2028), Economics 9708 (7 papers but 39 notes), Biology 9700 (10 papers, 26 notes) and Chemistry 9701 (19 papers, 43 notes).

### R-08 — MEDIUM — GCSE (UK) is in scope but has almost nothing in it
Three specification PDFs, no papers, no notes, and one of the three is AES-encrypted. Three boards are represented by one document each (AQA, Edexcel/Pearson × 2), which is not a route so much as three unrelated files.

*Decision needed:* which GCSE board and which subjects are actually being targeted, before any structure is built for them.

### R-09 — MEDIUM — 16 files are corrupt, empty or unreadable and currently look present
13 zero-byte PDFs sit in place with plausible names. A pipeline that checks for file existence rather than content would treat `0500_s20_in_11.pdf` as "the insert exists". Quarantine (rule R11) fixes this, but only if the acquisition list is actually worked.

### R-10 — MEDIUM — 30 of 50 Cambridge syllabus filenames carry no code
Migration rule R3 cannot be fully automated. 12–18 files need a human to confirm the syllabus code, and two are genuinely ambiguous from the filename alone (`AS & A Level English Syllabus.pdf`, `German Language Syllabus.pdf`).

### R-11 — LOW/MEDIUM — Path fragility on macOS
Case-insensitive filesystem (case-only renames need two steps), 40 path segments with stray whitespace, and 13 files over 20 MB that cannot be round-tripped through the desktop bridge and must be handled in place. All manageable, all capable of causing a silent failure if unnoticed.

### R-12 — LOW — Namibian examiner reports duplicated 4× for 279 MB
Fixed by rules R8 and R10. Worth stating only because it is 7% of the repository by size and the whole of the reclaimable space.

### R-13 — LOW — 148 empty directories overstate coverage
Entire subject trees (AS French 8028, AS German 8027, IGCSE German) exist with no files. Not recreated in the target tree.

### R-14 — LOW — No backup has been verified
This inspection did not and could not verify that a copy of these 4 GB exists anywhere else. Stage 0 of the migration plan makes that a precondition rather than an assumption.

## 6.2 Open policy questions the migration forces

These sit on top of `TEAM_REVIEW_NOTES.md`. Items 2, 3 and 10 from that document are now blocking rather than deferrable.

| # | Question | Why it can't wait |
|---|---|---|
| Q-1 | Which external sources are approved for derivation, reference only, or excluded? | Rule R9 assigns `authority_category` and `reuse_constraints` to 615 files. Guessing per file creates 615 decisions nobody owns. (`TEAM_REVIEW_NOTES` item 2) |
| Q-2 | Where do official assessment materials live, and what extraction and quotation rules apply? | Determines whether `sources/**/assessment/` may be mined at all, and whether mark-scheme wording may appear in learner-facing output. (item 3) |
| Q-3 | Do all `generated_gap` factual claims need human approval? | Given R-02, most of the pilot's topic 5 will be `generated_gap`. If every one needs sign-off, the pilot needs a named human reviewer and a time budget now. (item 1) |
| Q-4 | Are "First Proof" Namibian papers authoritative? | 170 files, and it changes their authority category. (new) |
| Q-5 | OCR at migration or on demand, and with what tool? | 259 files; changes whether `sources/` holds sidecar text. (new) |
| Q-6 | Does the pilot stay on 9609, or move to a subject with existing assessment depth? | Determines whether Stage 2 of the migration is worth running this week. (new) |
| Q-7 | Who are the semantic reviewers, and is one of them human for the pilot? | RS-28/RS-29 require independent review with the full critic packet; the pilot cannot reach `APPROVED` without it. (item 7) |
| Q-8 | Release-state vocabulary — is `draft/review/approved/published/superseded` enough, or does YYeni need `pilot` and `teacher-approved`? | `state.json` is trivial to change now and painful once releases exist. (item 8) |
| Q-9 | Is `sources/` enforced read-only at the filesystem level, or only by convention and check C2? | Filesystem-level is safer; it also complicates legitimate acquisition. (new) |
| Q-10 | Does version control apply to `standard/`, `shared/`, `work/` and `operations/`? | Affects whether `work/` churn is recoverable. (new) |

## 6.3 What I recommend deciding first

Three answers unblock everything else: **Q-6** (which subject the pilot runs on), **Q-1 + Q-2 together** (source approval and assessment-material policy), and **Q-3** (human approval threshold for generated claims). The folder architecture in document 03 and the naming rules in document 05 do not depend on any of them and can be approved independently.
