# 3. Proposed target folder architecture

## 3.1 The design rule

`RUNTIME_STANDARD.md` and the handoff prompt both demand one separation above all others: **immutable source material, regenerable working files, and published releases must not live in the same space.** Everything else in this design follows from that, plus one addition the current folder makes necessary — a place for things that are neither sources nor outputs (corrupt files, out-of-scope jurisdictions, superseded originals).

Six top-level zones:

| Zone | Mutability | Who writes it |
|---|---|---|
| `standard/` | append-only by version | humans, on a standard release |
| `sources/` | **immutable after landing** | humans, on acquisition only |
| `work/` | freely regenerable | agents |
| `releases/` | append-only | the publication stage |
| `shared/` | slow-changing | humans + agents |
| `operations/` | append-only logs | agents |
| `archive/` | cold | migration only |

An agent may write to `work/`, `releases/` and `operations/`. An agent must never write to `sources/`, `standard/` or `archive/`. That single sentence is enforceable (document 08, check C2) and is the whole point of the split.

## 3.2 The tree

```text
YYeni Study Resources/
│
├─ standard/                                  # the generation standard, one folder per version
│   └─ v0.1.0-draft/                           ← the current package, moved intact
│       RUNTIME_STANDARD.md|.yaml, PIPELINE.md, schemas/, tests/, prompts/, profiles/, ...
│
├─ shared/                                     # cross-qualification, reusable
│   ├─ subject-profiles/                        business.yaml, business.md, ...
│   ├─ glossaries/                              per-subject canonical term definitions (RS-08)
│   └─ templates/                               objective-type and learning-item templates
│
├─ sources/                                    # IMMUTABLE. Original material only.
│   ├─ cambridge/
│   │   ├─ as-a-level/
│   │   │   ├─ 9609-business/
│   │   │   │   ├─ syllabus/   cie-9609-syllabus-v2-2026-2028.pdf
│   │   │   │   ├─ assessment/2024/w24/qp/9609_w24_qp_31.pdf
│   │   │   │   │              2024/w24/ms/…   2024/w24/in/…
│   │   │   │   └─ supporting/ chapter-notes-2019/…  znotes-v2/…  single-topic-2020/…
│   │   │   ├─ 9696-geography/ …
│   │   │   └─ …  (16 subjects)
│   │   ├─ igcse/            0450-business-studies/, 0610-biology/, … (16 subjects)
│   │   └─ lower-secondary/  0860-computing/, 0893-science/, … (frameworks only)
│   │
│   ├─ namibia/
│   │   ├─ sp/               grade-4/ … grade-7/   (+ syllabus/ per subject)
│   │   ├─ jsc/              current JSC (New) reform: 20 syllabi
│   │   ├─ jsc-legacy/       2016 syllabi + the 184-file legacy question bank
│   │   ├─ jssee/            44-file question bank + moderator report
│   │   ├─ nssco/            6144-business-studies/, … + _examiner-reports/<year>/
│   │   ├─ nssco-legacy/     10-file Afrikaans bank
│   │   └─ nsscas/           8245-business-studies/, … (15 subjects)
│   │
│   ├─ gcse-uk/
│   │   ├─ aqa-8464-combined-science/syllabus/
│   │   ├─ edexcel-1ma1-mathematics/syllabus/
│   │   └─ pearson-1hi0-history/syllabus/
│   │
│   └─ _quarantine/          zero-byte, encrypted, malformed — never a build input
│       └─ 2026-08-31/       + quarantine.json giving the reason per file
│
├─ work/                                       # generated; safe to delete and rebuild
│   └─ cie-9609-as-2026-2028/                   one workspace per qualification+route+window
│       ├─ qualification-profile.yaml            copied from standard/, frozen for this build
│       ├─ inventory/     source_inventory.json, extraction-report.json
│       ├─ curriculum/    objective_registry.json, dependency_graph.json, glossary.json
│       ├─ assessment-evidence/  assessment_evidence.json, per-series mining notes
│       ├─ adequacy/      source_adequacy_and_repair_plan.json
│       ├─ topics/
│       │   └─ 2.1-human-resource-management/
│       │       contract.json
│       │       claims/canonical_claim_ledger.json
│       │       content-units/*.json
│       │       learning-items/*.json
│       │       reviews/  curriculum.json accuracy.json pedagogy.json assessment.json items.json
│       │       qa_report.json
│       ├─ builds/        build_manifest.<release-id>.json
│       └─ exclusions.json
│
├─ releases/                                   # append-only, one folder per release
│   └─ cie-9609-as-2026-2028/
│       ├─ r20260915.1/    state.json (draft|review|approved|published|superseded)
│       │                  notes/  retrieval-bank/  practice/  teacher-report/  exports/
│       │                  build_manifest.json  output-hashes.json
│       └─ latest → r20260915.1        (symlink or a pointer file, see 05 §5.6)
│
├─ operations/
│   ├─ inventory/2026-08-31/     ← this package becomes this
│   ├─ migration/                migration maps, dry-run logs, rollback manifests
│   ├─ backups/                  pre-migration hash manifests
│   └─ acquisition/              what still needs to be obtained (see 06 R-01)
│
└─ archive/
    ├─ out-of-scope/botswana-bgcse/    29 syllabi, preserved not deleted
    ├─ superseded-syllabi/<board>/<code>/
    └─ duplicates/2026-08-31/          + provenance.json naming the kept copy
```

## 3.3 Why the source tree is curriculum-first, not artifact-first

The current folder is artifact-first: `Question Banks/`, `Revision Notes/`, `Syllabi/` are three parallel trees, and a single qualification's material is scattered across all three. Cambridge AS Business 9609 currently lives in three places four levels apart.

Stage 2 of the pipeline demands a **per-qualification source inventory**. Stage 8 demands **per-objective adequacy scoring across all sources**. Both are cheap when one qualification's syllabus, papers and notes sit under one parent, and expensive when they do not. Hence `sources/<board>/<level>/<code>-<subject>/{syllabus,assessment,supporting}/`.

The cost of this choice is that "show me all mark schemes" is no longer one directory listing. That is the right trade: nobody builds a resource by browsing all mark schemes, and a glob (`sources/*/*/*/assessment/*/*/ms/`) answers it anyway.

## 3.4 Why `work/` is keyed by qualification-route-window

`cie-9609-as-2026-2028` names a board, a syllabus code, a route and an exam window. RS-02 requires all four to be locked before authoring. Putting them in the workspace name makes the lock visible in every path, and makes the 2029–2031 rebuild a new sibling folder rather than an in-place overwrite of work that 2028 candidates are still using.

This also solves the syllabus-expiry problem from document 02 §2.4: when a syllabus expires, the workspace name tells you, and the old workspace stays intact as the record of what was published.

## 3.5 Topic workspaces

`examples/README.md` in the standard package sketches a flat `topic_workspace/`, with the explicit warning not to impose it blindly on legacy content. This design keeps the artifact set but hangs it under `work/<qualification>/topics/<topic-id>-<slug>/`, so that the qualification-level artifacts the pipeline shares across topics — objective registry, glossary, assessment evidence, source inventory — exist exactly once instead of per topic. That matters for RS-08 (one canonical definition per recurring term): a per-topic glossary makes the rule unenforceable.

## 3.6 How the tree satisfies the handoff requirements

| Handoff requirement | Location |
|---|---|
| original source files | `sources/**` (immutable) |
| official syllabuses and assessment materials | `sources/<board>/<level>/<code>-<subject>/{syllabus,assessment}/` |
| source inventories | `work/<qual>/inventory/source_inventory.json` |
| global objective registries and glossaries | `work/<qual>/curriculum/`, `shared/glossaries/` |
| qualification and subject profiles | `work/<qual>/qualification-profile.yaml`, `shared/subject-profiles/` |
| topic workspaces | `work/<qual>/topics/<topic>/` |
| canonical claim ledgers | `work/<qual>/topics/<topic>/claims/` |
| structured content units | `work/<qual>/topics/<topic>/content-units/` |
| flashcards and learning items | `work/<qual>/topics/<topic>/learning-items/` |
| deterministic and semantic QA reports | `work/<qual>/topics/<topic>/qa_report.json`, `reviews/` |
| published learner resources | `releases/<qual>/<release-id>/` |
| superseded versions and build manifests | `releases/<qual>/<release-id>/` with `state.json: superseded`; `work/<qual>/builds/` |
| **separation of immutable / generated / published** | the `sources/` `work/` `releases/` split, enforced by check C2 |

## 3.7 What this design deliberately does not do

- **It does not use git.** A 4 GB PDF archive is a poor fit for git, and `sources/` immutability plus release manifests give the audit trail that version control would otherwise provide. If the team wants version control, apply it to `standard/`, `shared/`, `work/` and `operations/` only, with `sources/` and `releases/` outputs excluded.
- **It does not flatten the Namibian legacy/new split.** Legacy question banks are only interpretable against legacy syllabi; merging them would destroy that pairing.
- **It does not delete anything.** Botswana BGCSE, duplicates and corrupt files all land in `archive/` or `_quarantine/`, retrievable.
- **It does not decide release-state names.** `state.json` carries whatever the team settles in `TEAM_REVIEW_NOTES.md` item 8; the folder layout is indifferent to the vocabulary.
