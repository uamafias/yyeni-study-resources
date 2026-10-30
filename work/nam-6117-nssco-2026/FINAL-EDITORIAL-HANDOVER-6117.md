> **Latest re-review:** must-fix list cleared by the independent reviewer; four minor wording items subsequently implemented and checked. All 12 topic QA runs and 12 audit/regression scripts pass. Independent coverage and operator AO/recall/publication decisions remain open. See the minor-follow-up section of [the review delta](REVIEW-DELTA-2026-10-30.md).

> **30 October 2026 review repair:** [Changed-item re-review packet](REVIEW-DELTA-2026-10-30.md). All latest named defects addressed, including optional items; counts clarified as 20 MISCON-subtype cards, 19 examiner mappings and eight image-bearing activities. Current author recall/AO figures remain unapproved; publication stays on hold. This working-tree repair follows the previously committed snapshot.

> **Repository checkpoint:** the corrected review snapshot was committed locally as `6bb957f` on `chemistry-6117-approved-plan` after the user instructed us to move on. No push or learner publication. Start independent review with [REVIEW-NEXT-6117.md](REVIEW-NEXT-6117.md). Earlier “no commit” statements below describe the repair pass before this checkpoint.

# NSSCO Chemistry 6117 — final editorial repair handover

29 October 2026. **The requested author repairs are complete; publication remains on hold for independent re-verification and release approval.** This document supersedes the current-state claims in earlier repair reports. Those reports remain as history. No commit, push or publication was performed in this repair pass.

## Latest reviewer follow-up — implemented

The previous completion statement was too broad: 78 MC rubrics still contained generic feedback, some authoring labels remained, and examples were in the right units but after closing material. Those defects are now fixed in the rebuild sources and checked in the generated files.

| Feedback | Delivered correction |
|---|---|
| Missing distractor explanations | All **132 questions** now give a separate reason for each of the three wrong options: **396 explanations**, present in both answer feedback and marking guidance. Generic fallback text occurs **zero** times. The 11-P01(3) filtration distractor was also made unambiguously false. |
| Length measure | **Whitespace-delimited words:** 3 uniquely longest keys, 72 tied, 75 longest including ties. **Unicode characters including spaces, excluding option labels:** 14 uniquely longest, 14 tied, 28 including ties. No claim that length cues have vanished under every measure. |
| 9-015 | Names zinc oxide instead of supplying its position relative to carbon. Requires a chemically suitable route and comparison of supplied processing costs (N$8 versus N$20/kg), with both links required for credit. |
| Authoring labels | Removed remaining capitalised and lower-case “original practice/illustrative/example/results/data” labels and the timed-gas caption wording. Chemically meaningful references to the original sample or readings remain. |
| Worked-method placement | All 12 are headed **Worked example:** and placed immediately after their relevant explanation, before Connections. Topic 4’s formula/amount refresher precedes reacting masses; its titration method follows “Solutions and reacting amounts”. Exact positions are recorded in the check artifact. |
| Command/demand mismatch | 10-028 and 10-045 now open with **State**. 11-003 asks whether the evidence is sufficient to choose, rather than presupposing one source is more secure. Its three-point evaluation remains intact. |
| Fraction boilerplate | Each of the two recurring advice sentences now occurs **once**, together in the refinery-gas paragraph. The other six fraction descriptions retain only their specific content. |
| Image attachments | Verified Markdown attachments in 3-P03, 4-P03, 6-P02 and 6-P03. This confirms delivery links, not independent scientific review of images. |

Verification: all 12 topic QA runs have zero failures; all ten existing regression/audit scripts and the new [follow-up regression](planning/round10-repair-checks.json) pass. The full 28-path copied-wording scan still has zero 12-word matches and nine standard-terminology 8-word matches. Counts, tariffs, AO and recall totals are unchanged. These are author checks, not independent certification. The existing publication hold has not been removed; no commit or push was made.

## Completed repairs

- Removed the leaks in 8-013, 9-015 and 8-029. Topic 8 now also tests the forward reagent-and-observation directions explicitly: 8-027 chloride and 8-029 bromide. Both are counted as recall. Flame, anion and gas-test knowledge remains assessed; supplied references are not used to pretend that recall has been tested.
- Rebuilt 8-P03 around one shared observation record. Its parts build on the record without repeating it; the cation part requires two credited elements. Corrected 8-023/024 commands to Deduce/Plan and removed learner-facing authoring jargon.
- Removed all **236 answer-only activity feedback blocks** from the notes. Added **12 topic-specific worked-method blocks plus three further stoichiometry methods**, using fresh examples. They explain decisions, steps and checks rather than reproducing the activity answer key. Their new numerical results have 24 explicit recomputations in the final check.
- Removed **59 repeated long sentences**, dropped five empty connection blocks, put all 64 sections in numerical syllabus order and replaced unwieldy objective-sentence headings with section names. Supplemental material and worked methods now sit in relevant sections. The notes contain 80,030 words; the former length target has not been met by restoring padding.
- Reworked six redundant designs: 2-086, 3-021, 5-031, 6-052, 10-016 and 11-040. Reviewed 65 prompt-similarity candidates; retained distinct molecules, contrasting definitions and distinct test/fraction knowledge with reasons. This is not a claim that every possible pair was independently reviewed.
- Revised **44 MC option sets** into more comparable forms. All 11 keys remain balanced and non-cyclic; the answer-only terminal-full-stop cue is absent. All 132 questions now include per-option distractor reasons in feedback and rubrics. By whitespace-delimited word count, only **3/132** correct options are uniquely longest; 75 are longest including ties. Equal lengths are not a substitute for independent distractor-quality review.
- Corrected the named hydroxide-rule distinction, fuel-oil use, electrolysis half-equation, Topic 12 caption and Topic 11 authoring text. All 71 registered visuals received an author inspection using contact sheets, selected full-size views and source checks. Removed residual authoring titles and corrected the qualitative-analysis key so it does not claim sample purity. Four activities now have actual Markdown image attachments rather than only filenames. Learner delivery follows the explicit allowlist; keyed figures stay separate.

## Current bank and verification

| Measure | Current value |
|---|---:|
| Cards / activities / total items | 808 / 36 / 844 |
| Activity parts / audited responses | 236 / 1,044 |
| Content units / claims | 64 / 934 |
| Marks | 1,637 |
| AO A / B / C marks | 784 / 550 / 303 |
| AO A / B / C shares | 47.89% / 33.60% / 18.51% |
| Recall credit | 392 marks, 23.95% |
| Registered visual assets, including variants | 71 |

The approximate syllabus AO profile is 50/30/20. The present modest drift toward B is accepted for this teaching bank because the revisions require interpretation/application; labels were not changed to manufacture the target percentages. This bank is not a single exam blueprint.

All 12 topic QA reports have **zero failures**, retain their warnings and four `not_run` checks, and correctly say **hold**. Semantic/rubric review is not automated. Existing regression checks, calculation checks, audit freshness and the new final editorial check pass. The copied-wording scan covers **28 exact source paths / 24 distinct file contents**, including all six annual reports. Four additional archive paths are byte-identical copies, not omitted evidence. There are zero 12-word matches and nine 8-word matches; the latter are standard chemistry terminology/definitions, a repeated compound name or a standard equilibrium rule, not borrowed examination scenarios.

Recall is an **author credit-level estimate**, not independent certification or a percentage established by Bloom labels. The current 392 marks are below the 24% intervention trigger: at this denominator, **393 triggers review/rebalancing**. The maximum whole-number recall total below 25% is 409: 17 further marks fit, 18 breach it. Independent reclassification must update the audit and invoke the replacement contingency rather than preserve the headline percentage. The recall-rule decision still requires explicit acceptance; do not infer it from mechanical checks.

## Review packet

- [Latest follow-up checks: explanations, placement, commands and both length measures](planning/round10-repair-checks.json)
- [Final editorial checks and new arithmetic](planning/final-editorial-checks.json)
- [Regression run results](planning/final-check-run.json)
- [Current production totals and per-topic checks](planning/production-progress.json)
- [Visual author-review ledger with SVG/PNG hashes](review/final-visual-author-review.json)
- [Visual delivery roles](planning/visual-delivery-audit.json)
- [Pair-review dispositions](review/final-pair-review.json)
- [Exact copied-wording sources](review/copied-wording-sources.md) and [scan results](review/copied-wording.md)
- [Recall rule](RECALL-RULE-2026-10-29.md) and [contingency](RECALL-CONTINGENCY.md)

## Remaining release gate

The preceding checks and visual inspection are **Codex author reviews**. They do not replace the other-vendor review required by TEAM-PLAYBOOK Step 6. The independent reviewer should verify the changed notes and visuals, inspect at least 20 cards per topic and all 19 examiner-misconception cards, and confirm the recall decisions and marker-usable rubrics. Preserve earlier independent review findings, but do not treat them as approval of this changed version. QA scripts rewrite reports; the reviewer can run them on a scratch copy as before.

The four carry-forward controls remain: internal report rows are source material, never learner copy; their reused numbers require recomputation; the five commentary-only 2022 Paper 2 Q3 parts receive no invented allocations; Paper 1 uses the syllabus **45 minutes**, with the 2025 cover discrepancy recorded; the 2022/2023 papers remain labelled first proofs.

There are no deliberately deferred author repairs from the latest feedback. Independent review and the user's release decision remain open. Do not commit unrelated Biology files, the harvest log or the 2025 question papers with this work.
