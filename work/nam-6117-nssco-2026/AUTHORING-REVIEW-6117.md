> October 29 update: latest recall estimate **366/1,557 (23.51%)**, AO **48.43/31.41/20.17**. See [decision rule and repair scope](RECALL-RULE-2026-10-29.md). Earlier percentages below are historical. Independent review and release hold remain open.

# Chemistry 6117 — authored bank for independent review

**Latest revision:** [Independent-review repair brief](REVIEW-REPAIRS-6117.md). The first bank review found fixable defects; repairs are ready for re-verification, not publication.

All twelve topics were authored by Codex after the user approved the nine prototypes. Step 3 and Step 4 remain approved. This handoff concerns the actual notes, cards, activities and visuals, not another review of the plan.

There are **772 cards + 36 activities = 808 items**, 64 content units, 1,849 unverified claims and 125,086 content-unit words. All 418 assessable outcomes, 55 practical experiences, 35 required visual IDs and 19 misconception targets have coverage. One additional hardness visual and auxiliary panels support the activities.

All topics returned zero blocking deterministic failures on the repair run. C-16 is explicitly not_run where its literal keyword test rejects direct chemical credit points; this is an outstanding semantic rubric gate, not a pass. This is not semantic approval. C35/C41 do not validate these Chemistry graphics; the author inspected them separately. C43 is inapplicable because these are not practice-text tasks. Independent scientific/numerical/visual review and copied-wording scanning remain open.

| Topic and notes | Cards | Activities | Words | Final checks |
|---|---:|---:|---:|---|
| [1 Scientific processes](topics/1/1-scientific-processes.md) | 74 | 3 | 11,401 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [2 Matter](topics/2/2-matter.md) | 158 | 3 | 24,202 | 37 pass, 3 warnings, 4 not run; 0 fail |
| [3 Materials](topics/3/3-materials.md) | 43 | 3 | 8,216 | 39 pass, 1 warnings, 4 not run; 0 fail |
| [4 Stoichiometry](topics/4/4-stoichiometry.md) | 41 | 4 | 5,869 | 39 pass, 1 warnings, 4 not run; 0 fail |
| [5 Electrochemistry](topics/5/5-electrochemistry.md) | 33 | 3 | 6,414 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [6 Chemical reactions](topics/6/6-chemical-reactions.md) | 69 | 4 | 11,254 | 39 pass, 1 warnings, 4 not run; 0 fail |
| [7 Acids, bases and salts](topics/7/7-acids-bases-and-salts.md) | 62 | 3 | 9,509 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [8 Qualitative analysis](topics/8/8-qualitative-analysis.md) | 50 | 3 | 7,102 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [9 Metals](topics/9/9-metals.md) | 49 | 3 | 8,231 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [10 Organic chemistry](topics/10/10-organic-chemistry.md) | 81 | 3 | 14,614 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [11 Environmental and industrial chemistry](topics/11/11-environmental-and-industrial-chemistry.md) | 79 | 3 | 13,536 | 38 pass, 2 warnings, 4 not run; 0 fail |
| [12 Practical skills and investigation planning](topics/12/12-practical-skills-and-investigation-planning.md) | 33 | 1 | 4,738 | 39 pass, 1 warnings, 4 not run; 0 fail |

The notes include worked answers. Each topic’s `learning-items/topic_<T>_items.json` contains the actual card and activity bank; `authored_assessment_parts.json` retains the individual activity tariffs, AOs and Bloom labels. `visuals/` contains SVG originals and PNG previews. [Practical index](PRACTICAL-INDEX.md) links all 55 experiences.

## Balance and changes

The authored bank totals **1,557 marks-equivalent**: A 763 (49.00%), B 480 (30.83%), C 314 (20.17%). The full-demand repairs and factual-label corrections moved a net 47 marks from A to B; the approximate syllabus target remains 50/30/20. See REVIEW-REPAIRS-6117.md.

Recall after the complete 1,008-response audit is **363/1,557 = 23.31%**, below the 24% warning and 25% ceiling. Explicit credit decisions in planning/full-demand-audit.json determine the count independently of Bloom labels. The author reviewed all prompts and rubrics; independent semantic confirmation remains required. The earlier 385-mark MECH-only estimate is superseded. There is no per-topic cap.

[Production audit](planning/production-audit.json) records every changed top-level slot label and the check results. Each topic’s `authoring_notes.json` records the reasons and practical-part mapping changes. Key changes include:

- Actual-demand corrections to card subtypes/AOs/Bloom labels and MC subparts, retaining stable IDs. Some IDs retain their original subtype suffix; the current subtype field is authoritative. The planned 56 CALC slots become 55 CALC cards because a unit-identification slot is correctly DEF.
- Topic 3 P02 is a 14-mark continuous free response, adding seven marks to the 1,550-mark baseline. Topics 7 and 11 retain seven-mark free responses.
- Topic 5 industrial drawing slots become supplied-feedstock applications because the syllabus excludes technical industrial diagrams.
- Several practical subparts are mapped to the skill they actually exercise instead of generic scale reading.
- Full calculation/planning rubrics required documented unit-budget changes in Topics 3, 4, 9, 11 and 12. C26 editorial warnings remain in Topics 5, 8, 10 and 11; the full notes total is inside the planned subject range.
- Topic 7 qualifies the syllabus limewater wording: solubility is not degree of dissociation. Topic 11 qualifies the dated desalination statement using the official environmental authority record cited in the notes.
- The Chemistry adapter distinguishes a syllabus exclusion of diagrams from a requirement to draw them. Standard files were not edited.

## Claude Code review brief

Paste this into Claude Code in the same local repository; these production files are currently uncommitted. No Git operation is required to read them.

```text
You are the independent REVIEWER for NSSCO Chemistry 6117, workspace work/nam-6117-nssco-2026/. Codex authored all twelve topics. Read TEAM-PLAYBOOK.md Step 6, the REVIEWER role and this workspace’s HANDOVER, then AUTHORING-REVIEW-6117.md. The user approved Step 3, Step 4 and the nine authored prototypes; full-bank review is now due. Do not re-open those approvals without a concrete new finding.

Review the actual 772 cards, 36 activities, notes and rendered visuals. Re-run planning/check_resource_topic.py for all twelve topics and authoring/audit_production.py. Read all topic notes, sample at least 20 cards per topic, inspect all 36 activities and visuals, and recompute every worked numerical answer. Review actual AO/Bloom/recall demand and every documented deviation. Check learner answerability, original wording, scientific scope, mark allocations and all 19 misconception diagnostics.

Run the repository copied-wording check against Chemistry question papers and the relevant examiner-report corpus, excluding the syllabus. Read matches in context; report permitted standard definitions/formulae separately. Do not treat automatic anchor matches, schema passes or author self-reviews as scientific verification.

Record findings with item/block/visual IDs and severity. Fix permitted learner-facing issues using the repository revision/restamping workflow, rerun affected checks and report plan problems separately. Do not modify standard/, unrelated Biology work, harvest logs or source PDFs. Do not commit, push or publish: the Chemistry HANDOVER requires independent review and fixes before publication. Preserve all carry-forward constraints. Return a clear verdict and remaining issues for the owner to read.
```

## Carry-forward and release state

- Reused internal examiner-report answer rows require original wording and independent arithmetic. The 299 internal rows remain source material, not ready-made learner rubrics.
- No invented official mark allocations for the five commentary-only 2022 Paper 2 Q3 parts. Newly authored tasks have explicitly original allocations.
- Paper 1 syllabus duration is 45 minutes; retain the separate 2025 cover discrepancy of one hour.
- The 2022 and 2023 papers are proof versions.
- Claims and items remain review-required/unverified. Nothing from this production run has been committed, pushed or published. Earlier approved plan/prototype commits are separate.

The general playbook describes packaging before cross-review; the subject HANDOVER explicitly requires independent review and repairs before publishing. This handoff follows the subject-specific requirement.
