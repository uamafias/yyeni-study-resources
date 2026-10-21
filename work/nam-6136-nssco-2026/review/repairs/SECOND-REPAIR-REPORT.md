# Repairs after Claude’s second whole-subject review

Jeremy authorised one read-only, whole-subject Claude Code review on 2026-10-20. Claude returned **FIX CONTENT BEFORE PUBLICATION**. Codex then repaired the actionable content findings in one subject-wide pass. Claude did not edit the subject, run its checks, browse the web or use subagents. Codex has not sent these repairs for another review.

The full second review is preserved at [`CLAUDE-RESOURCE-REVIEW-2.md`](../CLAUDE-RESOURCE-REVIEW-2.md), with the raw response, brief and input manifest alongside it. The first review and its repairs are retained separately.

| Finding | Repair / disposition |
|---|---|
| N-01 — 66 teaching paragraphs overwritten by card answers | Restored every identified baseline teaching paragraph and retained the newer card application under an “Applied example” label. This restores definitions and explanations for sampling methods, questionnaires, interviews, diet, groups and the other affected content. Re-rendered the subject notes from the structured units. The 10.1 sampling methods are now defined directly in the lesson. |
| N-02 — work-category totals unclear in topic 4.2 | Explicitly distinguished 30 unemployed, 70 employed, and 70 people with unmet work needs. The 40 underemployed people count in both the employed and unmet-needs totals, so those totals overlap. |
| N-03 — source links attached too broadly | Removed the review-identified unit-wide locator additions and restored the claims’ earlier provenance labels. All claims remain `unverified` and non-publishable. Claim-level support for recent external facts still needs evidence; no new web research was undertaken. **Partially resolved; this remains a quality limitation.** |
| N-04 — generic prompts in 8.1 and 9.2 | Rewrote all 13 cited cards into natural, specific prompts with focused answers, keeping the original item slots and metadata. |
| N-05 — 7.3-006 objective/prompt mismatch | Reframed the comparison around community apprenticeship and college education, and retained a reasoned judgement. The prompt avoids the literal command “Evaluate” because the unchanged standard check C-14 bars that word for this objective; the metadata remains unchanged and the deviation stays visible. |
| N-06 — NDP5 terminology and missing HPP pillar practice | Revised the NDP5 evaluation card to use the goals taught in the notes and added a two-mark contrast between HPP’s economic-advancement and infrastructure-development pillars. |
| N-07 — obsolete fictional-model clause | Removed the clause from all four 10.1 package marking-guidance headers. |
| N-08 — duplicate prerequisite sentence | Removed the repeated formula/units requirement from the CALC task specifications. |
| R6136-004 — narrow SDG coverage | Added examples visible in the saved 2022 examination figure, the linked economic/social/environmental pillars, and a 1.2 card requiring two named SDGs alongside responsible-production practice. Used only the local syllabus and saved assessment corpus. |

## Verification

- Re-rendered all 18 topics from their structured content units.
- Reran the full subject audit, including each topic’s standard checks, work-order/slot comparison, registry validation and research numerical audit: **18/18 topic decisions `publish`, zero deterministic failures, zero slot-metadata mismatches**.
- Final draft totals: **749 claims, 101 units, 505 flashcards, 38 activities and 36,241 rendered-note words**.
- Re-ran the saved assessment-text copied-wording scan against 40 local extracts: zero 8+ word matches and zero 12+ word defects.
- Claims remain unverified; all items remain `review_required`. Automated `publish` is only the deterministic tool decision, not human or independent approval.

One partial disposition recorded in Claude’s review of the earlier findings remains: R6136-015 still has some repeated scenario patterns. The R6136-004 SDG-name and three-pillar coverage gap was addressed using the saved syllabus and exam evidence. The unresolved N-03 source-attribution gap and standard-owner/tool findings T-1 and T-3 remain open.

No external source research, publication, commit, push, learner release, platform import or third Claude review was performed. The open source-attribution issue, standard-owner issues, no-opinion checks and absence of specialist subject approval remain visible.

Reproduce the local repairs with `python3 review/repairs/repair_resources.py`, `python3 planning/repair_review_demands.py`, then `python3 review/repairs/repair_second_review.py`; render all topics with the standard `render_notes.py`, run `topics/audit_build.py`, and rerun the copied-wording scan. These scripts make no network or model calls.
