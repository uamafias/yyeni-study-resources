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
harvest discover <page-url> --out found.csv   # 1. point it at a site, get candidate links
                                              # 2. curate found.csv — set folder/filename, drop noise
harvest validate found.csv                    # 3. pre-flight: collisions, bad URLs, missing folders
harvest run found.csv                         # 4. fetch (HTTP, escalating to Chromium on 403/HTML)
harvest verify --requeue                      # 5. check integrity; write a repair manifest
harvest run repair_<date>.csv --force         # 6. re-acquire whatever came back broken
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

**Rules of the road**

- Never bypass a paywall. Log it as failed and move on.
- A 200 response is not a success — `harvest verify` is part of the job, not an extra.
- Every acquired file must be traceable to a URL and a timestamp in the log.
- Re-running a manifest is safe: anything already on disk is skipped.

Full documentation: `/Users/professor/Documents/YYeni Web Harvester/docs/`
