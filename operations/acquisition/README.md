# Acquisition — Cambridge AS Business 9609

## Files here

- `cie-9609-as-acquisition-list.md` — what is missing and why it blocks the pilot
- `cie-9609-as-acquisition-manifest.csv` — **83 rows**, every document by exact Cambridge filename, with its target path

## Tiers in the manifest

| Tier | Rows | What |
|---|---:|---|
| `0_orphan_pair` | 1 | `9609_w20_qp_21` — the question paper for the AS mark scheme already held. One file makes an existing orphan usable. |
| `1_minimum` | 34 | Variant 1 of Papers 1 and 2 (qp + ms) for s23/w23/s24/w24/s25/w25, plus 6 examiner reports, plus 4 specimen documents for the 2026–2028 edition |
| `2_all_variants` | 48 | Variants 2 and 3 of the same papers |

**Correction to the earlier estimate.** The inspection package said "roughly 24–30 documents". That was loose. With three variants per paper the complete three-year set is 82 documents; the minimum viable set is 34. Tier 1 is enough to run pipeline Stage 4 properly — three years of both AS papers with mark schemes and examiner reports. Tier 2 improves context diversity and reduces the risk of over-fitting depth allocation to one variant's style.

## Variant numbering — how to pick the right file

The Cambridge filename encodes everything:

```text
9609 _ w24 _ qp _ 3 1
 │      │     │    │ └── variant (1, 2 or 3)
 │      │     │    └──── paper number (1, 2 = AS · 3, 4 = A Level)
 │      │     └───────── kind: qp question paper · ms mark scheme · in insert · er examiner report
 │      └─────────────── series: s = May/June · w = Oct/Nov · m = March (India only) + 2-digit year
 └────────────────────── syllabus code
```

**For the AS-only route, only papers 1 and 2 are in scope.** Anything with a paper digit of 3 or 4 is A Level and must not be mined as AS assessment evidence (RS-02 scope lock). The four A Level papers already in `sources/` are marked `status: out_of_scope` for exactly this reason.

Do not trust folder labels. Three files in this repository sit in a folder whose variant contradicts their filename, and in every case the filename was correct. The intake script derives the target path from the filename.

## Intake

Save downloads — any filename — into:

```text
operations/acquisition/inbox/
```

Then the intake step verifies each file is a real PDF with a text layer (13 zero-byte PDFs in this repository are what happens without that check), reads the syllabus/series/kind/paper/variant, renames to the canonical stem, files it at its `target_path`, records its SHA-256 in the source register, appends its `source_inventory.json` row with page count and measured extraction quality, and ticks the manifest row. Anything unparseable or duplicate stops in `inbox/_unresolved/` rather than guessing.

Record where each file came from in the `acquired_from` column when you tick it off. That is bookkeeping, not judgement — provenance policy is a team decision (Q-1, Q-2).
