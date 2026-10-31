# NSSCO Biology 6116: Codex pre-approval review

Reviewed 18 October 2026. Verdict: **fix the plan first**.

This completes the requested independent review of the plan and a spot-check of the visual bank. It does not complete TEAM-PLAYBOOK Step 6: full authoring has not started, so there is no complete authored resource to review. Plan approval, authoring, scientific image approval and learner delivery remain open. No curriculum, contract, work-order, learner item or original image was changed by this review.

## Verified plan facts

The five work orders contain 106, 23, 481, 153 and 108 flashcard slots, respectively: 871 flashcards and 15 performance tasks, 886 items. No duplicate flashcard slot ID or missing command word, tariff or marking-parts list was found. The operative budget check passes for all five topics: 50,800–80,040 words. The registry has 540 non-container objectives. Exposure is explicitly Papers 2 and 3 only; Paper 1 remains unmapped.

I recomputed the AO total directly from the slot tariffs using rational arithmetic, splitting multi-AO slots equally and using the documented task assumptions: MCQ 12 marks at 7.5 A / 4.5 B; structured question 8 marks at 5 A / 3 B; practical 10 marks C, per topic.

| AO | Marks-equivalent | Percentage | Gap from stated target |
|---|---:|---:|---:|
| A | 866.5 | 42.7057663874 | -4.2942336126 |
| B | 626.5 | 30.8772794480 | +2.8772794480 |
| C | 536 | 26.4169541646 | +1.4169541646 |
| Total | 2,029 | 100 | |

The aggregate is inside five points **under the present classifications and task assumptions**. The handover's 43/31/26 is rounded. The task allocations are planning assumptions, not verified classifications of future authored parts; actual authored task marks must be checked again. The syllabus PDF pages 38–40 confirm the stated 47/28/25 target and paper marks. Weighting those paper marks by 30/50/20 gives the separate final-grade share 50/30/20. These bases are correctly distinguished.

## Plan findings

| ID | Severity | Where | Finding and required repair | State |
|---|---|---|---|---|
| P01 | high | PLAN §4/§6; subject-profile.yaml AO classification; syllabus PDF p.38 | AO A explicitly includes explanations using knowledge and understanding. AO B includes reasoned explanations and describes application to novel information. Assigning every taught WHY/CHAIN explanation to B by subtype/objective type does not resolve that distinction. Examine representative planned demands with a Biology teacher and document a rule based on the actual demand. If B coverage is short, design authentic data/application tasks within scope and rebuild; do not merely relabel or add filler. | Open before plan approval |
| P02 | high | EV-6116-2024-P2-6(a); review_low_confidence.json | Visual inspection of PDF p.11 shows Q points to the nucleus boundary. The part identifies a cell structure; it does not test drawing/interpreting a prepared meiosis slide (OBJ-6116-4.1-07). Remap to the cell-structure objective OBJ-6116-3.2-01 with the contextual limitation recorded, then regenerate evidence and exposure. The Miner's speculation about a centriole/spindle is unsupported. | Open before plan approval |
| P03 | medium | EV-6116-2023-P2-2(c); review_low_confidence.json | The question asks for a process of pesticide uptake into roots. Current objectives concern phloem translocation and osmosis/water uptake; those describe related context, not a settled match to the precise uptake demand. The figure does not identify the intended process and there is no mark scheme. Restore explicit uncertainty and review the uptake-process mapping; do not certify either translocation or water uptake as directly credited solely from context. | Open before plan approval |
| P04 | medium | planning/check_docs.py; HANDOVER introduction; PLAN §9 | The checker passed despite stale wording that the contracts/work orders print the superseded budget, a claim that both low-confidence mappings are figure-dependent (one is extinction), and doubled percent signs in §6. These were corrected in the generator. The checker covers selected phrases/sample facts, not every claim in the packet. | Wording fixed; checker strengthened for these facts |

P01 sensitivity: 255 marks, 12.5678% of the whole plan, sit on WHY/CHAIN slots assigned solely to AO2. Moving all of these to A would give 55.2735/18.3095/26.4170. This is a sensitivity calculation, **not** an adopted reclassification or instruction to change labels. It shows why the present balance cannot settle the classification question.

## All five mapping rechecks

I read the relevant complete source pages, including their figures; extracted text alone was not used to identify Q or the renal vessel.

| Source part | Result |
|---|---|
| 2023 P2 2(c), PDF pp.3–4 | P03 above: uptake demand remains uncertain; current contextual mappings are not independently confirmed. |
| 2023 P3 1(c)(ii), PDF pp.2–3 | Temperature/light-factor mappings are plausible routes to balancing loss and uptake. Keep medium: the open suggestion also admits other routes, so it is not exclusive evidence for both factors. |
| 2025 P2 2(a)(ii), PDF p.4 | Vein-structure mapping is plausible from the drawn vessel wall/lumen. Retain medium. The review note's claim that structure is the skill regardless of the figure is too broad: evidence must actually be visible. No official marking answer can be inferred. |
| 2024 P2 6(a), PDF p.11 | P02 above: nucleus identification, not a prepared-slide meiosis skill. |
| 2022 P2 1(d)(i), PDF pp.2–3 | The definition of extinction is examined. Retaining a low-confidence contextual link to conservation is honest, but habitat destruction specifically is not tested by this definition part. Keep the glossary support and do not report the causes objective as directly examined on this evidence alone. |

The existing evidence counts (261 high, 78 medium, 2 low) were not altered. They describe the current map, pending the repairs above.

## Visual-bank spot-check

Integrity check passes: 254 records, 301 stored files, 109 objectives, 158 kind-bindings, 240/350 needs with an unreviewed candidate, 64 variants pending and 46 gaps. **Zero scientific approvals and zero requirements met.** I inspected nine stored originals (ROOT-001/002, OSMOSIS-001, STEM-001, BLOOD-001, ORG-042, HUM-021/023/026), all three teaching variants, and the ten generated question graphs. The variation graph has answer files only, which is permissible for a preparation bank but is not a prepared question variant. This is a sample review, not scientific certification of all 233 Commons assets.

I checked creator/licence fields on seven live Commons pages: ROOT-001/002, OSMOSIS-001, STEM-001, BLOOD-001, ORG-042 and HUM-023. The recorded licences and named creators agree where present. HUM-023 still has no identified creator in its file summary; uploader names in the history do not settle authorship. Its hold remains justified. A Commons licence tag does not resolve the suspected third-party artwork in ORG-042.

| Asset | Independent decision |
|---|---|
| ROOT-001 | Keep the original untouched and never use its scale for measurement. The teaching variant still displays endodermis and pericycle despite the stated syllabus-term restriction, and its starch-grain label obscures the original leader. A blanked scale number leaves an uncalibrated bar, not a usable scale. Restrict labels/questions to required structures and have placements reviewed. |
| ROOT-002 | Retain hold: identity/tissue detail is not established. The file description says only “Dicot”; it does not establish the organ. |
| OSMOSIS-001 | Retain hold for plasmolysis: the wall–protoplast separation is not sufficiently clear for this teaching use. The source page conflicts between 400× and 4000×. Do not calculate size from it or identify the disputed feature from the title alone. |
| STEM-001 | Epidermis, xylem and pith placements are plausible. Phloem remains uncertain; the dot lies in the outer bundle/cap region and needs expert confirmation. The vascular-bundle dot marks a point, not its extent: bracket the bundle before using it to teach the whole structure. |
| BLOOD-001 | No lymphocyte is demonstrated in this field; retain that limitation. Platelet and ambiguous white-cell labels remain subject to teacher review and phone-size legibility. It cannot alone satisfy a lymphocyte/phagocyte comparison. |
| ORG-042 | Retain provenance hold. The illustration's appearance raises a concern; the file page's own-work assertion does not independently trace the artwork. Do not state infringement as proved. |
| HUM-023 | Retain attribution hold pending identified creator/provenance. |
| HUM-021 / HUM-026 | Retain the identity cautions. Do not promote uncertain cell-type identifications into teaching keys. No specialist cell identification is certified by this review. |
| Generated graphs | The question images distinguish illustrative curves/readings from measured results. HUMANPOP still needs source/value verification. Blank plotting grids need their declared data table supplied in the actual item. No prepared graph is approved by inspection alone. |

One additional preparation issue: ROOT-001 and BLOOD-001 asset-level rights.changes still say no changes while their file lists include masked/labelled variants. The lineage records disclose edits, but eventual attribution must identify the actual variant's changes and reuse terms. Do not copy the original's “none” into a derivative credit.

Live sources checked: [root](https://commons.wikimedia.org/wiki/File:Ranunculus_Root_Cross_Section.png), [alternative root](https://commons.wikimedia.org/wiki/File:Transverse_section_of_a_dicot_root.jpg), [onion](https://commons.wikimedia.org/wiki/File:Plasmolysis_of_red_onion_(Allium_cepa)_cells.jpg), [stem](https://commons.wikimedia.org/wiki/File:Herbaceous_Dicot_Stem_Older_Helianthus_(35022512084).jpg), [blood](https://commons.wikimedia.org/wiki/File:Normal_Adult_Blood_Smear.JPG), [root artwork](https://commons.wikimedia.org/wiki/File:Tap_Root_%26_Fibrous_Root.png), [neutrophils](https://commons.wikimedia.org/wiki/File:Segmented_neutrophils.jpg). Label-placement judgements above come from the stored images, not the pages' titles.

Preparation, teacher approval and delivery are clearly separated in the plan. Existing visual gaps remain honest gaps. No new candidate or binding was added, no hold lifted, no visual approved and no YYeni write made.

## Framework findings for Vitalis

These are reports, not requests to change standard/ in this workspace.

| Code path | Expected versus actual; minimal example |
|---|---|
| standard/v0.2.0-draft/build/render_chart.py:41; checks/yyeni_checks.py:1321 | A required biological figure needs a supported rendering/reference and checking route. Actual renderer/C-41 support break-even charts. Minimal use: require a root cross-section or blood micrograph; no corresponding image-delivery validation is provided. An external bank integrity pass is not that validation. |
| standard/v0.2.0-draft/checks/yyeni_checks.py:1010–1017 (C-24) | Reviewed, human-verified claims need a supported post-review state. Actual check rejects every verification.status other than null/unverified, regardless of review. Minimal claim: publishable=false, verification.status=verified; C-24 fails. Sidecar verification records do not repair the shared lifecycle. |
| standard/v0.2.0-draft/build/make_contract.py:34 (WORDS_BY_EXPOSURE) | Subject-specific/per-source-bullet budgets should govern. Actual fixed per-objective bands charge split members separately. Minimal example: split one descriptive bullet into two unseen objectives; the formula budgets 460–660 words before unit overhead. Workspace apply_notes_budget.py supplies the operative override. |
| standard/v0.2.0-draft/build/make_work_order.py:281 (sub_topic) | Preserve meaningful source sub-topic depth. Actual function truncates to three dotted levels. Minimal input OBJ-6116-3.6.2.3-01 becomes 3.6.2, merging distinct source sections. |
| standard/v0.2.0-draft/build/make_work_order.py:455–471 | Missing usable command/tariff/marking structure should produce a diagnostic. Actual slot append accepts the unresolved values. Minimal profile with no observed command-word candidates and no answer structure can emit command_word=null and empty marking parts rather than refusing the slot. Current Biology slots have these values populated; this is a shared failure-mode report. |

## Exit conditions

Resolve P01 with a demand-based classification decision and P02/P03 with explicit mapping decisions, then regenerate the affected stages in planning/RUN_ORDER.md. Recompute the unrounded AO aggregate without padding/relabel shortcuts. Return the updated topic/AO tables to Lotto for approval. Visual repairs and expert approvals can remain staged under the explicit holds; they must be completed before dependent learner material is released.

The operator still needs to name the Biology verifier and school textbook. The recall-ceiling denominator and 2026 Paper 1 duration remain unresolved as already recorded. No approval, source-completeness confirmation, commit, push or learner release is implied by this review.
