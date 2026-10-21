# Round-four repairs — Development Studies 6136

Codex addressed both medium and all three low findings from `review/CLAUDE-RESOURCE-REVIEW-4.md`, under Jeremy’s instruction of 2026-10-21. No Claude call or new research was made. These are local repairs, not independent approval.

| Finding | Completed correction | Verification |
|---|---|---|
| F1, medium | Replaced the two inconsistent adjacent pyramid passages with one complete age-sex dataset. Overview, table and bar specifications now agree; the unequal broad age bands have an explicit interpretation limit. | Recomputed both totals, age shares and all bar lengths. Deliberately wrong overview and bar examples are rejected. |
| F2, medium | Removed the separate sector-practice answers; changed systematic, stratified, random, pie, rectangle and sketch-map worked examples away from the assessment datasets. Updated the systematic definition and linked claim together. | Recomputed selection sequence, allocations, angles, lengths and boundaries; checked the related note blocks and retained teaching explanations. |
| F3, low | Replaced the misplaced pillar comparison with an explicit comparison of short-term and long-term planning. | Prompt, answer and two-mark criteria cover both horizons and immediate detail versus strategic direction. |
| F4, low | Rewrote 59 guides with item-specific evidence, mechanisms and consequences, including four additional copied INTERP guides. Removed duplicated generic P01 guidance in ten topics. | Whole-bank scan finds none of the reported generic guide families, duplicate P01 criteria or full-answer copies in non-definition multimark guides. The renewable-resource criterion explicitly includes regrowth. |
| F5, low | The B-only planning task now interprets supplied targets and observed results. The research task describes collection procedures without naming the answer in the stem or next question. | Preserved approved slots, tariffs and AO labels; bare pillar labels earn no interpretation credit. Retained the spoiled-output clarification. |

## Scope and evidence

78 learner artefacts changed and one claim revision propagated. `actions.json` records before/after text hashes; `baseline/` preserves the pre-repair source. `repair.py` rebuilds from that baseline. Do not run earlier authoring scripts over this repaired draft.

65 of the 66 previously restored teaching paragraphs remain unchanged. The remaining paragraph keeps its systematic-sampling definition but intentionally changes its numerical example to match the new independent worked dataset. No teaching paragraph was replaced with a card answer.

`targeted-validation.json` records 18 targeted checks, 17 existing research/numerical checks and two negative cases. `validation.json` records whole-subject results and final content hashes. Standard rendering and restamping were used; all 543 planned item slots and their metadata remain intact. The copied-wording scan against 40 local assessment extracts found no 12-word defects; its single 11-word match is the official SDG 8/12 names, retained as standard terminology.

## Limits

The standard’s automated “publish” result means zero deterministic failures, not independent publication approval. All 749 claims remain honestly marked unverified and non-publishable. Earlier N-03 source-verification debt, unsupported/no-opinion checks and standard profile/runner compatibility issues remain open. These can still affect a future publication verdict independently of F1–F5. No fifth Claude review, commit, push, publication, platform import or pilot completion is claimed or authorised by this repair instruction.
