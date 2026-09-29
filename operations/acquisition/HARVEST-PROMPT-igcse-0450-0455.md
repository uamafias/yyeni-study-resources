# Harvest brief — IGCSE Business Studies 0450 and Economics 0455

Paste everything below to the agent running the harvest. It works from the repository root of
**YYeni Study Resources**.

---

You are acquiring the assessment corpus for two Cambridge IGCSE subjects. Use the **YYeni Web
Harvester**; do not write scraping scripts.

```bash
harvest() { "/Users/professor/Documents/YYeni Web Harvester/bin/harvest" --project "$(pwd)" "$@"; }
```

## What to get

| | |
|---|---|
| Subjects | **Business Studies 0450** and **Economics 0455** |
| Years | **2020 to 2025** inclusive |
| Series | June (`s`) and November (`w`). Also March (`m`) where it exists — India-only, same syllabus, valid evidence |
| Variants | **all** (1, 2, 3) |
| File kinds, in priority order | `er` examiner reports · `ms` mark schemes · `qp` question papers · `in` inserts · `gt` grade thresholds |

**Examiner reports first.** They are the scarcest and the most valuable: the only source that
observed real candidates failing, and the thing we currently hold **zero** of for both subjects.
If a run has to be cut short, it should be cut short after the reports are in.

Rough target so you can tell whether the harvest under-delivered: **200–250 files per subject**.
We currently hold 5 for 0450 and 8 for 0455.

## The routing rule to use

```bash
harvest route found.csv --rules cambridge-igcse-question-bank --out routed.csv
```

It is a project rule in `_harvest/rules/`. **Do not use `cambridge-question-bank`** — that one is
hardcoded to the `Cambridge AS and A Level` tree and locked to code 9609, so it would both misfile
these and reject them.

Destinations it produces:

```
Question Banks/Cambridge Curricula/IGCSE/Business Studies (0450)/2024/Oct-Nov (Variant 1)/0450_w24_qp_21.pdf
Question Banks/Cambridge Curricula/IGCSE/Business Studies (0450)/Examiner Reports/2024/0450_w24_er.pdf
Question Banks/Cambridge Curricula/IGCSE/Business Studies (0450)/Grade Thresholds/2024/0450_w24_gt.pdf
```

## The one thing most likely to go wrong

**Aggregator index pages serve other subjects' files.** This is not hypothetical: the 9609 harvest
found `pastpapers.co/caie/a-level/business-9609/2020-march` serving Chemistry **9701** papers, and
only a subject lock stopped them being filed as Business Studies.

The IGCSE rule has no code filter. Instead it resolves the subject folder from an IGCSE-only
lookup, so anything that is not one of our IGCSE codes lands in `_unknown-subject` where you can
see it. **After routing and before fetching:**

```bash
harvest tree routed.csv
grep -c "_unknown-subject" routed.csv        # expect 0
cut -d, -f3 routed.csv | grep -oE "^[0-9]{4}" | sort | uniq -c   # expect only 0450 and 0455
```

If a foreign code appears, do not fetch. Fix the discovery, re-route, look again.

## Where to look

Start with the aggregator that worked for 9609 — its index pages are one per subject per series,
and its `alt_urls` download form is worth keeping:

```
https://pastpapers.co/caie/igcse/business-studies-0450/<year>-<series>
alt_urls: https://pastpapers.co/api/file/caie/igcse/business-studies-0450/<year>-<series>/<file>.pdf?download=1
```

Check the exact slug before assuming it — IGCSE slugs are not always `<subject>-<code>`. Then widen
to the other free Cambridge repositories. Use `alt_urls` rather than a second manifest row when a
file is available from more than one place, so a single failure does not lose the file.

**Never bypass a paywall.** Log it as failed and move on.

## The loop

```bash
harvest discover <index-url> --out found.csv
harvest route found.csv --rules cambridge-igcse-question-bank --out routed.csv
harvest tree routed.csv                       # eyeball the tree BEFORE fetching
harvest validate routed.csv                   # collisions, bad URLs
harvest run routed.csv
harvest verify --requeue                      # a 200 is not a success
harvest run repair_<date>.csv --force
```

Re-running a manifest is safe; anything already on disk is skipped. Keep the manifest per subject
per year so a partial failure is easy to re-drive: `_harvest/manifests/qbank-0450-2024.csv`.

## When you are done

Write `_harvest/reports/coverage_0450_0455.md` with, per subject and year:

- how many of each kind you got (`qp`, `ms`, `in`, `er`, `gt`)
- **which series are missing, named individually** — not a total
- anything that resolved to `_unknown-subject`, and what you did with it
- any paywalled or dead source, named, so nobody hunts it again

Missing files matter more than acquired ones here. Cambridge publishes recent examiner reports only
to registered centres, so some of the 2024–2025 reports may be genuinely unavailable — say so
explicitly rather than leaving a silent gap, because the downstream mining stage records that
limitation in the resource.

Report back: files acquired per subject, examiner reports acquired per subject and year, what is
missing and why, and anything that landed in `_unknown-subject`.
