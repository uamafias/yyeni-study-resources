# Harvest brief — the seven syllabuses three learners sit in the November 2026 series

Paste everything below to the agent running the harvest. It works from the repository root of
**YYeni Study Resources**.

---

You are acquiring the assessment corpus for seven Cambridge syllabuses. Three learners sit these
papers between **30 September and 10 November 2026**, so acquisition order is by exam date, not by
subject. Use the **YYeni Web Harvester**; do not write scraping scripts.

```bash
harvest() { "/Users/professor/Documents/YYeni Web Harvester/bin/harvest" --project "$(pwd)" "$@"; }
```

## Work in this order — earliest exam first

| Order | Code | Subject | Level | Papers sat | First exam | Held now |
|---|---|---|---|---|---|---|
| 1 | **9709** | Mathematics | AS | 12 Pure 1, 52 Prob & Stats 1 | **30 Sep** | 24 files, 1 ms, 0 er |
| 2 | **0500** | First Language English | IGCSE | 12 Reading, 22 Directed Writing | **5 Oct** | 14 files, 7 ms, 0 er |
| 3 | **9618** | Computer Science | AS | 11 Theory, 21 Problem Solving | 9 Oct | 5 files, 4 ms, 0 er |
| 4 | **9702** | Physics | AS | 12 MCQ, 22 Structured, 34 Practical | 14 Oct | 9 files, 6 ms, 0 er |
| 5 | **0460** | Geography | IGCSE | 12 Themes, 22 Skills, 42 Alt to Coursework | 14 Oct | 6 files, 3 ms, 0 er |
| 6 | **9093** | English Language | AS | 12 Reading, 22 Writing | 16 Oct | 11 files, 11 ms, 0 er |
| — | 9609 | Business | AS | 11, 21 | 5 Oct | 363 files — **complete, skip** |

**Zero examiner reports exist for any of the six.** They are the scarcest and most valuable file we
acquire, so within each subject get `er` first, then `ms`, then `qp`, then `in` and `gt`.

## Scope

- **Years:** 2020–2025 inclusive.
- **Series:** June (`s`) and November (`w`); also March (`m`) where it exists.
- **Variants:** all (1, 2, 3).
- **Papers:** get every paper for the syllabus, not only the ones listed above. Mark schemes and
  examiner reports cover a whole series, and the paper a learner sits this year may differ next.
- **Practical and skills papers are wanted, not skipped.** 9702 Paper 3 Advanced Practical Skills,
  9618 Paper 4 Practical, 0460 Paper 4 Alternative to Coursework, 0500's writing papers. Their
  **mark schemes matter most of all**: they carry the technique criteria, the method marks and the
  step-by-step credit that a learner can be taught to reproduce. Get every one you can.
- Rough target: **200–300 files per subject.**

## Two different routing rules

IGCSE has no AS/A Level split and its own folder tree, so it has its own rule. Route each subject
with the right one or the files land in the wrong tree.

```bash
# IGCSE — 0500, 0460
harvest route found.csv --rules cambridge-igcse-question-bank --out routed.csv

# AS & A Level — 9709, 9618, 9702, 9093
harvest route found.csv --rules cambridge-question-bank --out routed.csv
```

Destinations:

```
Question Banks/Cambridge Curricula/IGCSE/Geography (0460)/2024/Oct-Nov (Variant 2)/0460_w24_qp_22.pdf
Question Banks/Cambridge Curricula/IGCSE/Geography (0460)/Examiner Reports/2024/0460_w24_er.pdf
Question Banks/Cambridge Curricula/Cambridge AS and A Level/Mathematics (9709)/AS Level/2024/Oct-Nov (Variant 2)/9709_w24_qp_12.pdf
```

### Paper levels are now read from the syllabuses, not assumed

The AS rule used to map paper 1–2 → AS and 3–4 → A Level for every subject. That was right for
three of these and wrong for two, so it has been replaced by a per-subject table built by reading
each syllabus's assessment overview: `_harvest/lookups/cambridge-paper-levels.csv`. Each row carries
the syllabus sentence that justifies it.

| Code | P1 | P2 | P3 | P4 | P5 | P6 |
|---|---|---|---|---|---|---|
| 9093 English Language | AS | AS | A | A | — | — |
| 9618 Computer Science | AS | AS | A | A | — | — |
| 9609 Business | AS | AS | A | A | — | — |
| **9702 Physics** | AS | AS | **AS** ← practical | A | A | — |
| **9709 Maths** | Pure 1 | Pure 2 | Pure 3 | Mechanics | Prob & Stats 1 | Prob & Stats 2 |

Two things to know. **9702 Paper 3 is an AS paper** — the syllabus route table has the AS-only route
taking Papers 1, 2 and 3 — and the old rule filed it under A Level. **9709's papers are option
units, not levels**: Paper 1 is in every AS and every A Level route, so there is no paper-to-level
answer and the table gives the unit name instead, which is what a learner and an author actually
need to find.

A paper whose code-and-number is not in the table routes to `_unmapped-paper`. That is visible, not
lost. If you see one, read that syllabus's assessment overview, add the row with its justification,
and re-route.

**Smoke-test the rule before the full run.** Route one series of one subject, look at
`harvest tree`, confirm the level segment is what the table above says, and only then go wide. One
minute now against a whole subject refiled later.

## The one thing most likely to go wrong

**Aggregator index pages serve other subjects' files.** Not hypothetical: the 9609 harvest found
`pastpapers.co/caie/a-level/business-9609/2020-march` serving Chemistry **9701** papers.

Neither rule carries a single-subject lock any more — that lock was removed today because it was
rejecting six of these seven codes. Protection now comes from the lookup: a code with no row in
the subject-folder table cannot resolve a folder name and lands in `_unknown-subject`, visible.
**After routing, before fetching:**

```bash
harvest tree routed.csv
grep -c "_unknown-subject" routed.csv                              # expect 0
cut -d, -f3 routed.csv | grep -oE "[0-9]{4}" | sort | uniq -c      # expect only the code you asked for
```

If a foreign code appears, do not fetch. Fix the discovery, re-route, look again.

## Where to look

Start with the aggregator that worked for 9609. Verify the slug for each subject rather than
assuming it — they are not uniformly `<subject>-<code>`:

```
https://pastpapers.co/caie/<level>/<subject-slug>/<year>-<series>
alt_urls: https://pastpapers.co/api/file/caie/<level>/<subject-slug>/<year>-<series>/<file>.pdf?download=1
```

Then widen to the other free Cambridge repositories. Prefer `alt_urls` over a second manifest row,
so one dead host does not lose the file. **Never bypass a paywall** — log it failed and move on.

## The loop

```bash
harvest discover <index-url> --out found.csv
harvest route found.csv --rules <the right rule> --out routed.csv
harvest tree routed.csv                       # eyeball BEFORE fetching
harvest validate routed.csv
harvest run routed.csv
harvest verify --requeue                      # a 200 is not a success
harvest run repair_<date>.csv --force
```

One manifest per subject per year — `_harvest/manifests/qbank-9709-2024.csv` — so a partial failure
is cheap to re-drive. Re-running is safe; anything on disk is skipped.

**Report after each subject, not at the end.** The first exam is on 30 September and the person
waiting on this needs to know what landed while there is still time to use it.

## When you are done

Write `_harvest/reports/coverage_nov2026_entries.md` with, per subject and year:

- counts by kind (`qp`, `ms`, `in`, `er`, `gt`)
- **which series are missing, named individually** — not a total
- anything that resolved to `_unknown-subject`, and what you did with it
- any paywalled or dead source, named, so nobody hunts it twice
- anything that resolved to `_unmapped-paper`, and the syllabus row you added for it

Cambridge publishes recent examiner reports only to registered centres, so some 2024–2025 reports
may genuinely not exist on any free repository. Say so explicitly rather than leaving a silent gap
— the mining stage records that limitation in the learner resource itself.
