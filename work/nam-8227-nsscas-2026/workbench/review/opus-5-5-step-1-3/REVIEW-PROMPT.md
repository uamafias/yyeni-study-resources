# Independent review: framework and NSSCAS Mathematics 8227 steps 1–3

You are Claude Opus 5.5, the independent second reviewer of Codex's work. Work in
the YYeni Study Resources repository. Your role is **REVIEWER**; your subject
workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this review prompt.
This request commissions a review, not repairs to the author's frozen inputs.

## Purpose and boundaries

Assess whether the framework extensions and first source/syllabus/problem-family
analysis are sound enough to underpin the next planning stage. Challenge the
analysis, including omissions and weak distinctions. Return a reasoned verdict;
do not assume the counts or successful assembly checks establish correctness.

The pilot is Namibia NSSCAS Mathematics **8227, Grade 12**, with whole-syllabus
mapping as the aim. Verify the exact syllabus edition and unresolved edition/source
questions from the documents. The former NSSCO 6131 proposal is historical.
Retain and improve Jeremy's existing Workbench framework; do not design a competing
one. Workout Bench serves calculative subjects beyond Mathematics. High-level
Maths is a demanding test case, not proof that lower grades or Physics are covered.
Flashcard Studio cards must not be converted into Workbench recipes.

Read `AGENTS.md`, `TEAM-PLAYBOOK.md`, and exactly one role brief:
`standard/v0.2.0-draft/roles/REVIEWER.md`. Then apply the Workbench-specific
workflow in `workbench/playbook/README.md`, `quality.md` and `templates.md`.
Its review scope/output rules supersede the static notes/flashcard review procedure;
static PUBLISH checks and quotas do not certify Workbench work. Do not delegate.

## Freeze and record the inputs

Use the committed revision containing this prompt. Before reviewing, record its
full commit ID, branch and working-tree status. Do not mix later edits into the
review silently. Verify Git LFS source files contain real PDFs, not pointers.

The frozen author-pass manifest is:

`work/nam-8227-nsscas-2026/workbench/analysis/analysis-snapshot.json`

Expected SHA-256:
`1afe99d597617897cb3bf0489cd3bcbc236624fef05cef53a8aa4a92704a561f`

Verify its 35 file hashes and 20 source hashes. OCR page hashes have a separate
index in `ocr-validation.json`. The snapshot's `resource_git_head` is the author's
starting revision, not the eventual containing commit. Statements that no commit
was performed describe that authoring pass; Vitalis subsequently authorised the
Git checkpoint containing this prompt. Hashes establish identity, not accuracy.
Freeze the additional framework documents below by commit/path/hash as well.

Read in this order:

1. Actual syllabus PDF identified in `source-holdings.json`: assessment abilities,
   paper structures, weightings, scope, exclusions and any command-word guidance.
   Verify first-hand before using papers or the author's interpretation.
2. `workbench/STATUS.md`, `HANDOVER.md`, `analysis/REVIEW-START-HERE.md`,
   `analysis/corpus-analysis.md`, `analysis/source-inventory.md`,
   `analysis/acquisition-gaps.md`, and `checks/author-report.md` in the pilot workspace.
3. Curriculum JSON, demand registry/dispositions, question analysis/index,
   problem patterns, selection table and coverage matrix; use the actual PDFs
   and exact page/part locators to assess these records.
4. Textbook source map, samples, exercise discovery index, examiner difficulties,
   OCR validation, and the underlying source pages/images.
5. Framework audit `workbench/playbook/review/2026-11-15-framework-audit.md`,
   `workbench/playbook/textbook-analysis.md`, `BLOOM-CLASSIFICATION.md`, and changes
   to AGENTS, TEAM-PLAYBOOK, playbook README/quality/templates and the tracker.
   The author's baseline is `d6b8f551a405673f3149910e00ebfb7f1e5312a5`.
   The older playbook closure review does not approve these new extensions.

## Review questions

**Framework.** Does this extend useful existing work coherently? Are source roles,
textbook analysis, diagrams, provenance, review gates, ownership and evidence types
clear and reusable across subjects/grades? Distinguish implemented/tested behavior
from proposals and historical notes. Identify remaining contract gaps, without
assuming they were implemented in this source-analysis phase. Check the separation
of author evidence, runtime recipes, display metadata and app-owned learner data.
Review app capability/handoff claims against their stated evidence; do not turn a
read-only code inspection into proof of UI, visual grading or MCP delivery support.
External app paths may be unavailable; record this and continue with local evidence.

**Syllabus and sources.** Verify all 60 objective transcriptions and the 138 proposed
atomic demands, including compound bullets, prerequisites, explicit limits and
analyst inference. Check assessment statements against actual tables. Are source
titles, editions, identities, URLs, hashes and page locators defensible? Distinguish
official final papers from local proof copies. Check outstanding schemes, amendments,
specimens and corpus gaps. Do not claim an unverified document was inspected.

**Questions and coverage.** Audit all 119 connected questions and 250 part records
against the ten 2021–2025 papers, including primary/directly assessed secondary
objectives, prerequisites, tariffs, representations and dependencies. Verify the
750-mark reconciliation independently. Assess all include/exclude/hold decisions
and all 62 provisional families: which should be separate recipes, structural
branches, ordinary variations or supporting drills? Test for both inflated counts
and collapsed reasoning demands. An objective association is not full demand
coverage. The ten currently unlinked objectives and missing atomic-demand links
are unresolved mapping gaps, not evidence that the syllabus demand is absent.
Do not turn 62 provisional families into an approved recipe count.

**Textbooks and visual demands.** Verify all 17 inspected sample locators and their
curriculum fit, reasoning and representations. Inspect the relevant page images;
the 663-page OCR is a discovery aid with known mathematical errors. The 572 heading
leads are not 572 reviewed exercises. Determine whether the sampling method misses
important problem structures, diagrams or valid alternative methods, and propose
a defensible completion method. Separate reviewing the current samples from doing
an exhaustive textbook analysis. Check the 11 identified visual-response parts and
look for missed visual demands; displaying a diagram or accepting a photograph
does not prove reliable assessment. Do not weaken a syllabus demand to fit the UI.

**Marking and source defects.** Inspect the 22 linked embedded award excerpts and
the cited examiner difficulties. Check what they really establish about answer-only
credit, methods, alternatives, part dependencies and follow-through; missing full
schemes must remain explicit. Independently inspect both reported source issues:
2022 Paper 1 Q13, PDF page 18 (domain versus point), and the Namibia textbook PDF
page 550 / printed page 538, Try Now 21 Q2(c) (part reference). Confirm, correct or
reject those findings with evidence. Recompute mathematics where needed to resolve
a finding; document the extent. No generated recipe solutions exist to certify yet.

**Bloom and honesty.** Verify highest genuinely assessed part determines the whole
card; preserve part rationale and recipe-version/branch specificity. Incomplete
classification stays explicit. Bloom is distinct from AO, difficulty and marks.
Do not require invented classifications before demands/marking are settled. Check
that source extracts are internal evidence, not authorised learner-facing reuse.
Check that reports clearly separate processing, author checks, independent review,
owner acceptance and future local application testing/publication.

**Tools and checks.** Inspect `analysis_inputs.py`, `build_source_addenda.py`,
`build_analysis.py` and `operations/tools/pdf_ocr_macos.swift`. Identify assumptions,
tautological checks, brittle extraction, silent omissions and reproducibility risks.
Existing passing checks do not establish annotation correctness. If rerunning
builders, use a disposable copy so the frozen inputs remain unchanged. Prefer
cached OCR; a full 663-page rerun is not necessary merely to review its identity.

## Deliverables and verdict

Write only your review outputs under:
`work/nam-8227-nsscas-2026/workbench/review/opus-5-5-step-1-3/`.
Preserve this prompt and the frozen author inputs. Produce:

- `inputs.json`: commit, snapshot digest, additional input hashes, exact sources
  and pages read, checks run, mathematical/visual sampling, and unchecked scope.
- `findings.md`: stable finding IDs, severity, exact file/record/source locator,
  expected versus actual, educational consequence, minimal correction and how to
  verify it. Separate confirmed defects, evidence gaps and optional improvements.
- `report.md`: strengths retained, material findings, disposition audit coverage,
  remaining source/analysis work and a sequenced repair plan. Give a verdict of
  **accept named analysis scope**, **repair analysis**, or **fix mapping/plan first**.

If you cannot review all requested records, report the exact completed and omitted
sets and withhold acceptance of the omitted scope. Do not disguise samples as a
whole-corpus audit. Do not manufacture findings to fill a quota or rubber-stamp
because JSON references and marks reconcile. Identify which issues must be resolved
before work orders and which can remain tracked through a bounded next stage.

Do not modify author inputs, source PDFs, `standard/`, the existing generator bank,
other subjects, application code or pinned checkouts. Do not commit, push, publish,
import, assign learners, invoke paid research, or activate production. Do not claim
recipe/content acceptance where the review only covers analysis. Escalate unresolved
source/marking decisions to Jeremy/Vitalis with precise evidence and options.
