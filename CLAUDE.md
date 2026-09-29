# YYeni Study Resources

**Read `AGENTS.md` first.** It routes you to the one role brief you need and states the three rules
that apply to every agent working in this repository. This file carries only the web-acquisition
toolkit notes below.


<!-- yyeni-web-harvester -->
## Web acquisition (shared toolkit)

Source documents for this project are acquired with the **YYeni Web Harvester**, a
shared toolkit that lives outside this folder:

```
/Users/professor/Documents/YYeni Web Harvester
```

Do **not** write new scraping scripts in this project. Use the toolkit. If it is
missing a capability, add it to the toolkit so every project gains it.

**The command** (define once per shell session, or symlink it onto PATH):

```bash
harvest() { "/Users/professor/Documents/YYeni Web Harvester/bin/harvest" --project "$(pwd)" "$@"; }
```

**The loop**

```bash
harvest discover <page-url> --out found.csv          # 1. point it at a site, get candidate links
harvest route found.csv --rules <rule> --out r.csv   # 2. assign folders + filenames by rule
harvest tree r.csv                                   # 3. check the folder tree before fetching
harvest validate r.csv                               # 4. pre-flight: collisions, bad URLs
harvest run r.csv                                    # 5. fetch, creating folders as it goes
harvest verify --requeue                             # 6. check integrity; write a repair manifest
harvest run repair_<date>.csv --force                # 7. re-acquire whatever came back broken
```

**State lives here, in the project**, never in the toolkit:

- `_harvest/manifests/` — what we asked for
- `_harvest/logs/harvest_log.csv` — every attempt ever made, with its outcome
- `_harvest/reports/` — per-run markdown reports and integrity sweeps

**Manifest format** — CSV, only `url` is required:

| column | meaning |
|---|---|
| `url` | what to fetch |
| `folder` | destination folder, relative to this project |
| `filename` | what to save it as |
| `target_path` | full destination path instead of folder+filename |
| `mode` | `auto` (default) · `http` · `browser` · `render` · `skip` |
| `alt_urls` | `\|`-separated fallbacks tried in order |
| `note` | free text, echoed into the log |

Unrecognised columns are carried through untouched, so an existing catalogue CSV
can be used as a manifest as long as it has a `url` column.

**Folders are derived, not typed.** `harvest rules` lists the routing rules; a rule
reads the structure already in the filename (`9609_w24_qp_31.pdf`) and builds the
destination path from it. Project-specific rules live in `_harvest/rules/` and
override toolkit rules of the same name. Rows a rule cannot parse go to an
`_unresolved` folder and are reported — never filed on a guess.

**Rules of the road**

- Never bypass a paywall. Log it as failed and move on.
- A 200 response is not a success — `harvest verify` is part of the job, not an extra.
- Every acquired file must be traceable to a URL and a timestamp in the log.
- Re-running a manifest is safe: anything already on disk is skipped.

Full documentation: `/Users/professor/Documents/YYeni Web Harvester/docs/`
