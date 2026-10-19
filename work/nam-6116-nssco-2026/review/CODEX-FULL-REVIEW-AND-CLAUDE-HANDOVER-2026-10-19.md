# Biology 6116: Codex review of the revised Step 5 draft

Date: 2026-10-19. Workspace: `work/nam-6116-nssco-2026/`.

## Verdict and review limits

The revised authoring is materially better than the first draft. All five topics pass the deterministic checks, the previous C-35 diagnosis has been corrected through the supported Biology profile setting, the visual holds are recorded, and the science corrections I sampled are in place. The package is **not ready for learner release**. A clean `PUBLISH` decision here means the framework checks found no failures; it does not verify science, rights, figures, or teaching quality.

This review inspected the approval/status records, profile, authoring audit, checking scripts, package builder, all 886 item records through systematic queries, a deterministic random sample of 25 flashcards, all 15 performance-task summaries, selected complete items and note sections, and the earlier independent review. I did **not** read every line of all 72,263 rendered note words or independently verify all 1,102 claims. The first Claude review's 223-item sample and two subsequent reported repair rounds are additional evidence, not a substitute for the named teacher.

## Checks reproduced

| Topic | Claims | Units | Items | Rendered note words | Figure holds | Claims with no evidence | Required checks |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 110 | 7 | 109 | 7,410 | 2 | 110 | PUBLISH; C-18 warning |
| 2 | 40 | 2 | 26 | 2,081 | 0 | 26 | PUBLISH; C-18 warning |
| 3 | 587 | 23 | 484 | 36,110 | 23 | 172 | PUBLISH; C-18 and C-20 warnings |
| 4 | 213 | 13 | 156 | 16,516 | 7 | 81 | PUBLISH; C-18 warning |
| 5 | 152 | 5 | 111 | 10,146 | 3 | 59 | PUBLISH; C-18 warning |
| **Total** | **1,102** | **50** | **886** | **72,263** | **35** | **448** | **0 failures** |

I ran `what_to_fix.py` with `.venv/bin/python` for all topics, the learner-text hygiene gate, all five operative budget checks, `check_docs.py`, and `check_visual_bank.py`. All passed. No unit is below its operative minimum. Visual-bank integrity reports 254 approved asset records, 301 files, 226/350 needs with an unreviewed candidate, zero scientific verifications and zero requirements met. Every claim remains unverified and `publishable=false`. C-35, C-41 and C-43 are `not_run` where their inputs do not exist; do not describe those as substantive passes. C-20 names three topic 3 cards: 3-053, 3-125 and 3-140. The first two compare multiple investigation conditions; 3-140 is a single consequential exposed-area inference and the warning may be overbroad.

The cited corrections to bird diagnosis (ITEM-6116-2-020-FEATURE) and deforestation effects (ITEM-6116-5-033-CHAIN) are present. Tasks 3-P03 and 5-P03 are arithmetically coherent in the inspected answers, and their concepts and methods are taught in the notes across Topic 1 and the relevant Biology units. This is a bounded sample, not a whole-bank science verdict.

## Findings for Claude Code, in priority order

### 1. High: held figure items would be packaged

`standard/v0.2.0-draft/build/publish_subject.py` reads every item from a topic with no deterministic rejection. It does not read `topics/<T>/authoring_notes.json` or `visuals_pending`. Building now would put all 35 unsupplied figure items into a folder whose generated index calls it the copy to upload. No such build has been made, which is the right current state. Keep the source slots and honest holds. Produce a review-safe build route that excludes held items or makes the complete build unmistakably internal; record omitted IDs and counts so no visual need is falsely marked fulfilled. Do not edit `standard/` in the Biology authoring lane. Raise a framework change separately if required.

### 2. High: teacher verification and exact-use figures remain open

All 1,102 claims still require a named Biology verifier; 448 currently lack an approved evidence entry. Source gaps are not proof that the claims are false, but they cannot be silently filled with vague citations. The visual bank has zero completed scientific verifications and zero fulfilled requirements. Operator approval of the 254 assets does not settle scientific accuracy, required labels, source rights, or YYeni delivery. The listed cases needing named review include Benedict's heating temperature, Namibian examples, 3.9 expired-air figures, sewage-treatment stages and whether the exemplar's hypotonic/isotonic terminology is in scope. Record the teacher's decision per claim/visual; do not manufacture a verification state.

### 3. Medium: figure-dependent answer keys still need exact assets

ITEM-6116-4-052-FEATURE and ITEM-6116-4-053-FEATURE ask for the function of labelled X or Y, but answer with a menu of possible organs because the diagrams are unselected. For 4-053, the cervix alternative is a structural description rather than a function. ITEM-6116-3-258-APP asks which factor limits a plateau, but its answer depends on whether an absent second curve rises above it. Keep these items held. After exact question variants are selected, key the specified labels/curve and revise the answer and marking point, then restamp and rerun checks.

### 4. Medium: one infant-feeding comparison conflates feeding method and milk type

ITEM-6116-4-059-EVAL says only the mother can give breast milk and contrasts this with bottle-feeding. The 4.3.2 notes say formula may be the only option if the mother is ill. Expressed breast milk can be given from a bottle by another caregiver, and many maternal illnesses do not require stopping breastfeeding. The present comparison is therefore too absolute and may teach the wrong distinction. Review the claim text, note, item and linked ledger claims with the Biology verifier; distinguish direct nursing, expressed breast milk and formula feeding, and avoid general medical advice based only on “mother is ill.” Primary sources: [CDC infant-feeding FAQ](https://www.cdc.gov/breastfeeding/php/faq/faq.html), [CDC bottle-feeding guidance](https://www.cdc.gov/infant-toddler-nutrition/bottle-feeding/index.html), [CDC contraindications](https://www.cdc.gov/breastfeeding-special-circumstances/hcp/contraindications/).

### 5. Medium: audit AO and Bloom by actual demand, with an item-level record

The reported A/B/C mix of 57.2/16.4/26.4 is the approved marks-equivalent *estimator*, which assigns a model split to combined-AO performance tasks. It is not a completed part-by-part judgement of what every authored prompt demands. The alternative whole-item label split in the audit is 56.58/17.00/26.42. Do not change labels or add cards just to move either figure.

There are concrete candidates to inspect: ITEM-6116-4-090-WHY is labelled AO3 but asks for a taught explanation of dry-mass loss before photosynthesis becomes effective, with no investigation decision or result to process. ITEM-6116-3-161-APP is AO3 but applies a known osmosis explanation to two treatments, a possible A/B boundary rather than an obvious practical demand. ITEM-6116-3-174-APP has Bloom Apply and AO1; this may be a taught application boundary, so do not relabel automatically. Roughly 40 mismatch concerns were reported but no itemized list was saved. Make an item-level table containing prompt demand, current and proposed AO/Bloom/command word, reason, boundary/uncertainty, work-order impact and exact recalculated mix. Preserve the operator's settled generic taught-comparison AO1 decision. Bloom Evaluate can still be defensible for a balanced judgement, and Bloom Create can be defensible for ITEM-6116-5-105-SYNTH's investigation plan even though its opening verb is “Describe.”

### 6. Medium: the repair rounds need an auditable issue trail

The workspace holds the first independent Claude review and revised author scripts, but no saved second-round sample IDs, item-level findings, dispositions or the full label-mismatch list. Since this workspace is untracked by Git, the before/after cannot be recovered through a repository diff. Save the review inputs and a bounded resolution ledger: issue ID, exact affected IDs, original defect, repair in its source script, reviewer, result and validation command. Do not claim every item received an independent semantic review if fixers only read their own scripts; state the sampling and role boundaries exactly.

### 7. Low/medium: the learner-text hygiene gate is lexical only

`topics/check_release_hygiene.py` correctly finds zero of its listed phrase patterns and allows exactly one `Fig. VIS-6116-…` token in each held prompt. It does not test whether an item is answerable or prevent the standard builder from exporting it. The standard renderer also adds the internal workspace slug and “rendered from approved content units” in the header of each learner note (for example Topic 1 line 3). That is still pipeline language visible to a learner, outside the current gate. Treat the gate as a wording screen, and ask the framework owner to change the generated header; do not hand-edit rendered notes.

### 8. Low: marking-guidance structure needs an honest convention and targeted QA

In 118 flashcards the number of `marking_guidance` list entries differs from the tariff (topic 1: 11; topic 3: 99; topic 5: 8). This **does not mean 118 rubrics are wrong**: an “any three” option list or several explicit mark sentences in one entry can be valid. It does disprove a literal one-entry-per-mark claim. ITEM-6116-3-355-APP has four drawing credits in one entry; ITEM-6116-5-020-MECH has a framing entry and five possible points for four marks. Audit high-tariff, held and unusual rubrics for independent creditable points, and document how the product displays alternatives and multi-mark guidance. Do not split good answers mechanically to satisfy a list-length count.

### 9. Low: reconcile statistics and check-helper reliability

`topics/authoring_audit.json` gives **448** claims with no evidence, not the 442 quoted in STATUS and the earlier handover. The six-claim difference is in topic 4 (81 now versus 75 earlier). Update status from the current ledger after validation. `topics/scratch_check.sh` lacks `set -e`/`pipefail`; failed renderer, budget and hygiene commands can be hidden by redirection and `tail`. Fix the helper so failures propagate, while handling the separately documented clean-`PUBLISH` exit-code bug in `run_checks.py` explicitly. Direct `what_to_fix.py` and hygiene calls passed in this audit.

### 10. Low: prioritize concision by teaching value

The new 72,263-word total satisfies every unit minimum, but word count alone cannot demonstrate depth. For example, the 5.4.1 eutrophication section states the full nutrient → algae → dead matter → oxygen loss → fish death sequence and then restates it in the same section; some surrounding pollution distinctions also recur. Keep the complete causal chain once, followed by a worked data example or discrimination that adds value. A teacher should judge whether new text added to formerly short units improves understanding rather than merely meeting the lower budget line.

## Suggested repair order and acceptance

1. Save the two review rounds' available evidence and the itemized label concerns. Correct the stale 448 count in the status trail. Do not invent missing reviewer records.
2. Resolve the infant-feeding wording, the three illustrated answer-key problems as far as possible without their figures, and any other confirmed content faults in the author scripts/claim ledger. Where a figure is still missing, keep the item held.
3. Audit label candidates by prompt demand. Record justified work-order deviations and recalculate both AO bases; leave debatable cases documented. The paper's AO percentages are diagnostic, not a quota for the learning bank.
4. Make packaging hold-safe without editing protected `standard/` in this workspace. A review-only artifact must be clearly separated from a learner-upload folder and list held IDs. Do not build a normal `publish/` package that includes unsupplied figures.
5. Rerun scripts/regeneration in the subject's documented order, then `.venv/bin/python` checks for all five topics, unit budgets, authoring invariants, hygiene, wording overlap, docs and visual-bank integrity. Recheck answer keys after exact figures are selected. Keep Step 6, teacher verification, commit, push and learner release open until their real gates are met.

No authored resource, profile, framework, work order or visual asset was changed in this review. No package was built.
