# YYeni Study Resources

Curriculum source material and the generation standard used to turn official
syllabi into learner notes, retrieval items and examination practice.

## Before you clone — install Git LFS

The study corpus (~4.4 GB across 3,900+ PDFs, plus .docx/.pptx) is stored in
**Git LFS**. If you clone without LFS installed, every document arrives as a
small text pointer instead of a real file.

```bash
brew install git-lfs      # macOS. Linux: apt install git-lfs
git lfs install           # once per machine

git clone https://github.com/uamafias/yyeni-study-resources.git
```

The first clone transfers several gigabytes. To get the project files quickly
and fetch documents only as you need them:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/uamafias/yyeni-study-resources.git
cd yyeni-study-resources
git lfs pull --include="Syllabi/**"        # then pull only what you need
```

## What is in here

| Path | Contents |
|---|---|
| `standard/v0.2.0-draft/` | Active generation standard: runtime rules, pipeline, schemas, validation tests |
| `YYeni_Study_Resource_Generation_Standard_v0.1.0/` | Released v0.1.0 of the standard |
| `Syllabi/` | Official syllabi — Cambridge, Namibian, GCSE (UK), BGCSE |
| `Question Banks/` | Past papers, mark schemes and examiner reports |
| `Revision Notes/` | Notes by phase and qualification (SP, JSC, IGCSE, AS, A Level, NSSCO, NSSCAS) |
| `sources/` | Raw acquired documents, pre-filing, with a `_quarantine/` for out-of-scope material |
| `_harvest/` | Acquisition state: manifests, rules, logs, integrity reports |
| `operations/` | Change requests, review rounds, migration records |
| `work/` | In-progress builds per qualification and topic |
| `shared/` | Cross-cutting lookups (e.g. subject slugs) |

## Working on the standard

```bash
cd standard/v0.2.0-draft
pip install -r tests/requirements.txt
./run_tests.sh                    # schema + integrity + negative-control tests
python validate_project.py <project-dir>
```

`RUNTIME_STANDARD.md` holds the operative rules; `PIPELINE.md` describes the
end-to-end build. Read those two before authoring or reviewing content.

## Acquiring new source documents

Documents are fetched with the **YYeni Web Harvester**, a shared toolkit kept
outside this repository. Do not add scraping scripts here — extend the toolkit
so every project benefits. See `_harvest/POINTER.md` for the full loop, and
`CLAUDE.md` for the rules of the road.

Acquisition state (`_harvest/manifests/`, `_harvest/logs/harvest_log.csv`,
`_harvest/reports/`) is tracked in this repository. Every acquired file must be
traceable to a URL and a timestamp in the log.

## Committing documents

New PDFs are picked up by LFS automatically via `.gitattributes`. Keep pushes
to a reasonable size — add one subject or session at a time rather than
thousands of files in a single commit.

## Note on contents

This repository is **private**. It collects third-party examination-board
material (Cambridge Assessment, NIED/DNEA, Pearson Edexcel) for internal
teaching and resource development. Do not make it public or redistribute the
corpus outside the team.
