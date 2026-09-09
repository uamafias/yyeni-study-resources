# Acquisition list — Cambridge AS Business 9609 (2026–2028, AS only)

Generated at Stage 2, from the source inventory and the assessment-evidence gap analysis. Until these are held, the pilot cannot pass pipeline Stage 4 and cannot be published under RS-31.

## Priority 1 — AS assessment material (blocking)

Papers 1 and 2 are the AS components. For each of the **2023, 2024 and 2025** series (June and November), all variants where published:

- question papers: `9609_{s,w}{23,24,25}_qp_{11,12,13,21,22,23}`
- mark schemes: `9609_{s,w}{23,24,25}_ms_{11,12,13,21,22,23}`
- insert/case-study booklets where Paper 2 uses them: `9609_{s,w}{yy}_in_2{1,2,3}`
- examiner reports (`er`) for the same series
- specimen papers and specimen mark schemes for the 2026–2028 syllabus

Approximately 24–36 documents. Note that `9609_w20_ms_21.pdf` is already held but its question paper is not — acquiring `9609_w20_qp_21` makes an existing orphan usable.

## Priority 2 — a licensed conceptual source for topic 5

Topic 5 *Finance and accounting* has no chapter notes in the supplied material, and the only source with substantive finance content (`SRC-CIE9609-SUP-001`, ZNotes) has a partial text layer and unverified licence. Either license an endorsed textbook as an approved conceptual source, or accept that topic 5 will be authored as `generated_gap` throughout — which under RS-13 means every factual claim in it needs external verification or human approval.

## Priority 3 — resolve licences on what is already held

Thirteen of the twenty pilot sources carry `authority_category: uncertain` and `reuse_constraints` including `licence_check_required`. Until open questions Q-1 and Q-2 are answered, none of them may feed a `publishable` claim.

Specifically: `SRC-CIE9609-SUP-002` (apparent scan of a commercial revision guide, OCR required, licence unverified) should not be extracted at all until its status is settled.

## How acquisition interacts with `sources/` immutability

New files land in `sources/cambridge/as-a-level/9609-business/assessment/<yyyy>/<series>/<kind>/` under the Cambridge filename convention, and each acquisition is recorded here with date and provenance. The `sources/` immutability check (document 08, C2) treats a file that appears without a matching acquisition record as a failure, so this file is not optional bookkeeping — it is what makes new arrivals legitimate.
