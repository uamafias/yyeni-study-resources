"""Render the revision proposal and split handovers from the generated revision scope."""
from pathlib import Path
import json,collections
W=Path(__file__).resolve().parents[1];R=W/'planning/revision-01';load=lambda p:json.loads(p.read_text());v=load(R/'verification.json');s=load(R/'scope.json');vis=load(R/'claude-visual-work-order.json');B=R/'baseline'
T=['| Topic | Objectives | Flashcards | Packages | New cards | Total items | Notes words |','|---|---:|---:|---:|---:|---:|---:|']
for t in v['by_topic']:T.append(f"| {t['topic_id']} {t['title']} | {t['objectives']} | {t['flashcards']} | {t['packages']} | {t['new_cards']} | {t['total']} | {t['notes_words']['min']:,}–{t['notes_words']['max']:,} |")
T.append(f"| **Total** | **{v['assessable_objectives']}** | **{v['flashcards']}** | **{v['packages']}** | **{v['new_cards']}** | **{v['items']}** | **{v['notes_words']['min']:,}–{v['notes_words']['max']:,}** |")
AO=['| AO | Qualification target | Proposed share | Difference |','|---|---:|---:|---:|']
for a in 'ABC':AO.append(f"| {a} | {v['ao_target_percent'][a]:g}% | {v['ao_share_percent'][a]:.2f}% | {v['ao_share_percent'][a]-v['ao_target_percent'][a]:+.2f} pp |")
units=load(W/'review/codex-additions-word-counts-6145.json')['budget_warnings'];budget=[]
for u in units:
 n=u['actual'];lo=u['budget']['min'];hi=u['budget']['max'];budget.append({'unit_id':u['unit'],'actual_words':n,'min':lo,'max':hi,'change_needed':('add at least '+str(lo-n)+' substantive words')if n<lo else('remove at least '+str(n-hi)+' repeated words'),'owner':'Codex','reviewer':'Claude','constraint':'Preserve all named teaching points; do not change the budget or pad prose.'})
(R/'notes-budget-work-order.json').write_text(json.dumps(budget,indent=2)+'\n')
plan=f'''# Revised plan — 6145 NSSCO Economics

Revision 01, 28 October 2026. Owner: Vitalis P Haupindi. **Proposed scope: awaiting approval.** Vitalis authorised reopening Step 4 and assigned diagram/chart authoring to Claude, with Codex reviewing that work.

The reviewed baseline remains **580 items**, with Claude’s additions and Codex’s corrections preserved. The candidate plan is staged under `planning/revision-01/candidate/`; live curriculum, production content, work orders and publication have not been replaced. Candidate plans contain no authored new cards or new image files. Baseline planning inputs and content/publication hashes are saved under `planning/revision-01/baseline/`.

## What changes

- **{v['new_cards']} additional flashcards**: {v['new_nonvisual_cards']} focused nonvisual retrieval/explanation cards and {v['new_visual_cards']} diagram-construction cards.
- Revised bank: **{v['flashcards']} flashcards + {v['packages']} practice packages = {v['items']} items**. All 580 existing IDs and their planned labels are preserved; all 37 misconception slots remain exactly once. No new practice package is added.
- **12 diagram cards for Claude**: eight new and four existing market-forces cards. Each has a question-side stimulus/starter and an answer-side worked visual: **24 PNGs plus 24 SVG masters**, generated from declarative source data. A multi-panel figure is one image per side.
- {v['assessable_objectives']} assessable outcomes: the 96 printed syllabus anchors are unchanged; 41 further planner decompositions make previously implicit retrieval/representation targets explicit. New member-level exam exposure is not invented from parent counts.
- Keep the same **{v['units']} content units** and **{v['notes_words']['min']:,}–{v['notes_words']['max']:,} topic teaching-word envelope**. Repair ten unit-level budget discrepancies through focused editing, not removal of named examinable content or silent budget expansion.

## Why the additions belong

The approved 6145 syllabus remains the authority: its PDF assessment pages 17–19 and glossary pages 23–26 were reopened. Paper 2 includes drawing and interpretation. The accepted 2020–2024 corpus and both review reports identify the gaps. These additions instantiate existing syllabus outcomes; they do not create a new qualification scope or import another syllabus’s content.

The generated `scope.json` fixes each new card’s source parent, syllabus page/text, specific teaching target, ID, subtype, AO, Bloom level, command and tariff. Do not turn broad source parents into generic definition prompts. Internal corpus evidence is mined, never copied into learner questions or answers.

Nonvisual additions cover industrial action; central-bank functions and repo; NSX capital formation and liquidity; labour mobility; gross/net pay and time/piece rates; value added; total/average revenue definitions; external scale effects; merit goods, privatisation and nationalisation; named taxes; inflation; current-account meaning/components; age dependency; HDI; and protection methods. Two additional Explain cards address the meaning of the elasticity percentage-change ratios.

## Topic totals

'''+ '\n'.join(T)+f'''

The original approved plan’s teaching-word envelope, content-unit allocation and scope exclusions are retained. `candidate/topics/*/contract.json` and `work_order.json/.md` are generated from candidate curriculum/profile inputs. `id-migration.json` documents the reproducible migration from generator ordinal IDs to stable existing IDs; new IDs are allocated after the previous maximum within each topic. No item ID is typed into an authoring output by hand.

## AO balance

'''+ '\n'.join(AO)+f'''

Largest exact gap: **{v['largest_gap_points']:.3f} percentage points**, within five. Exact marks-equivalent: A {v['ao_marks']['A']:g}, B {v['ao_marks']['B']:g}, C {v['ao_marks']['C']:g}; total {sum(v['ao_marks'].values()):g}. This is a planning estimate using the existing task allocations, not a per-question official AO table or a prediction of learners’ marks. No extra cards were added solely to adjust the balance. The shared rollup’s rounding limitations remain; `verification.json` is the exact calculation.

## Elasticity tariff decision

Keep the two existing Calculate-1 result cards and their labels. Those cards award one result mark and must not promise marks for formula and working. The notes still teach formula, substitution and interpretation. Add one Explain-2 card for the meaning of each PED/PES percentage-change ratio, rather than inflating a simple calculation to an unrelated five-mark task. Corpus records distinguish primary Calculate tariffs from compound Use/Calculate forms. The new diagram cards use the observed Use-4 representation shape. Any future change to the old calculation tariffs must be proposed explicitly, not smuggled into authoring.

## Teaching and definition targets

The review’s major named-content repairs must survive every edit. Require each original outcome’s essential terms, classifications, mechanisms, lists and worked cases in a coverage checklist with canonical block/card IDs. An objective’s checked box or a passing structural check does not prove those named points are taught.

Before filling an existing DEF slot, state its standard economic term and distinguishing features. In particular, review `ITEM-6145-5.4-013-DEF` (the coined prompt about firm size as an economic comparison). Propose using the established term **internal growth**, already taught under the same firm-size outcome, retaining its ID and labels and recording the retargeting and any claim revisions. Other valid distinctions such as wage/non-wage factors and expenditure patterns should not be rewritten merely for style. Record any further semantic slot problem before changing the plan.

The ten budget work orders are in `notes-budget-work-order.json`: add a concise substantive example where under minimum; remove repetition where over maximum. Recount actual block text rather than retaining stale declared totals. Codex handles this focused nonvisual work; Claude reviews it. Neither the old packet writers nor the old final-authoring script may run over reviewed content.

## Division of work and order

1. Vitalis approves this concrete revised scope and authorises the plan checkpoint. Then promote the candidate inputs/contracts/orders to live paths, retaining the baseline snapshot and migration map. Do not reset any authored content.
2. **Codex authors the 37 nonvisual additions and repairs the ten unit budgets.** Preserve unaffected items and all reviewed definitions/conditions. Flag incomplete topics while Claude’s visual slots remain pending; do not publish a partial extension as complete.
3. **Claude authors the eight new diagram cards, equips the four existing PROC cards with visuals, and links the worked visuals into the relevant canonical notes.** Claude receives `CLAUDE-DIAGRAM-HANDOVER-6145.md` and the generated visual work order. Run these phases sequentially because several topics are shared.
4. **Cross-review follows authorship:** Claude reviews Codex’s nonvisual changes; Codex reviews Claude’s 12 visual cards, their accompanying note edits and all 24 visual images. Fix documented findings in the permitted canonical source, retaining revision/stamp rules.
5. Regenerate notes, run all topic checks, reconcile all {v['items']} slots and assets, republish and update STATUS. A later teacher-approved MCP import attaches images to the verified classroom. Git publishing and classroom import remain distinct checkpoints.

## YYeni images: verified current contract

On 28 October 2026, the connected `get_flashcard_contracts` tool returned **question_asset_id** and **answer_asset_id**, each an optional managed image ID. The application stores **question_image_url** and **answer_image_url**; learner practice/workout pages render these on the corresponding side. The teacher upload flow obtains a signed upload URL, PUTs the image to Google Cloud Storage, and saves the returned public URL. These were read-only checks, not a live import/display test.

Our authoring phase saves local, reproducible assets and a manifest keyed by repository item ID and side. Later, approved image imports obtain managed asset IDs; card import uses those IDs. Do not paste an expiring upload URL into a card, invent IDs, or add unsupported image properties to the canonical learning-items schema. The manifest also records descriptions, semantic values/relationships, local paths and file hashes. No bucket or hosting change is required by this plan.

A question image contains only the given data/starter or original situation. The fully labelled solution belongs on the answer side. Model answers and marking guidance must also state the necessary values and economic reasoning in text; a picture alone is insufficient teaching or scoring guidance. Student drawing submission and automatic image grading are not certified by this planning check.

## Limits and verification

Candidate registry and base profile validate. All new command/tariff pairs are observed in the accepted corpus; all old IDs and labels survive and every new slot is unique. A separate read-only hash comparison confirms reviewed content and current publication remain unchanged.

The shared visual checker is a business break-even model. The candidate profile explicitly uses the supported `depictions.chart_model: none` setting because this subject has no built-in economic-curve renderer. This does not validate or excuse the visuals: Claude must supply a reproducible subject renderer and data, and Codex must independently check every figure. Keep C-35/C-41 not_run limitations visible where applicable; never fake break-even metadata for demand/supply diagrams. Do not edit standard files to make checks green.

The full legacy profile schema rejects runtime extensions; the base profile validates and the runtime consumes the extensions. The shared notes header, full schema and generic-renderer limitations remain reported debt, not authorisation for standard-file changes.

Existing exemplar structure is retained. It proves no failures on its old thin slice, not that new slots are authored or that image integration is tested. New authoring must validate against the revised live scope after approval. No fresh PUBLISH claim is made for this unfilled candidate plan.

**YOU checkpoint: approve the 625-item revised scope and split authoring/review assignment before production authoring.**
'''
(W/'PLAN-6145-nssco-economics.md').write_text(plan)
visualtable=['| Item | New/existing | Visual target |','|---|---|---|']
for x in vis['cards']:visualtable.append(f"| `{x['slot_id']}` | {'existing'if x['existing_card']else'new'} | {x['target']} |")
claude='''# Claude handover — diagrams and chart cards, 6145 NSSCO Economics

Paste below the line into Claude Code in this same checkout after revision-01 scope approval and plan checkpoint.

---

You are the AUTHOR for the diagram/chart portion of 6145 NSSCO Economics, workspace `work/nam-6145-nssco-2026/`, owner Vitalis P Haupindi. Vitalis explicitly assigned visual authoring to Claude and visual review to Codex. Read AGENTS.md, TEAM-PLAYBOOK.md, only the AUTHOR role brief, STATUS.md and the revised PLAN-6145-nssco-economics.md. This handover narrows the generic whole-subject author instruction to the visual assignment below.

## Approval and preservation

Confirm revision-01 approval and plan checkpoint are recorded in STATUS before authoring. Candidate files alone are not approval. Work from promoted live contracts/orders, not by editing candidate files. Codex’s nonvisual phase should be completed or explicitly paused before you touch shared topic files. The reviewed baseline and any completed nonvisual additions must survive. Do not run author_support.py, write_packet.py, final_author_audit.py, or the original planning bootstrap/write_plan.py. Those scripts describe earlier content or scope and can overwrite reviews.

## Exact visual assignment

Read `planning/revision-01/claude-visual-work-order.json`. It fixes 12 item IDs, parents, labels, targets, side-specific file paths and economic requirements: eight new cards and four existing market-forces PROC cards. Produce 12 question PNGs and 12 answer PNGs, plus matching SVG masters. Save all parameters, plotted points, equations, scales, labels and render code. Names in the work order are derived from item IDs; do not rename files manually.

'''+ '\n'.join(visualtable)+'''

Use exact existing task data wherever enhancing an existing card. For a genuinely necessary change, record it and update the relevant worked calculation/claim and derivatives, rather than quietly drawing a different case. New examples must be original invented Namibian cases, N$, British English. Do not copy official diagrams, question text or marking wording.

## Author the economics, not a decorative picture

- Each card’s target and visual requirements are explicit in the work order. Keep its subtype, AOs, Bloom level, command and tariff. A Use-4 construction has a concrete four-point visual rubric. Include economic reasoning in the model answer, but do not award unrequested extra marks.
- Put the starter/data/original state on the question image. Put the completed solution on the answer image. The question must not give away a labelled answer it asks the learner to construct or identify.
- Derive original curves from declared values. Independently solve intersections, check which curve moves and why, quantify shortages/surpluses where used, and verify all points against equations or supplied schedules. Use competitive-model and binding-control conditions. A control alone does not shift curves; distinguish supply from sales.
- For elasticity, control units/scales and reference points. Do not infer elasticity from visual steepness alone or call every steep supply curve inelastic. Do not confuse LRAC with total cost or short-run diminishing returns. Do not imply a straight PPC has increasing opportunity cost.
- Render programmatically from a declarative specification with a repeatable subject-owned renderer under this workspace. Do not hand-correct SVG coordinates after generation or use text-to-image output for precise economic curves. The standard renderer only understands business break-even charts and cannot validate these figures.
- Use high-contrast lines distinguishable in greyscale, clear curve/axis labels and arrows, and sufficient font size for phone-sized display. Multi-panel comparisons must remain readable as a single image on one card side. Review every PNG at a narrow display width and in offline notes.

## Canonical schema, offline notes and the asset manifest

Write canonical items only in each assigned topic’s existing learning-items JSON; add new claims only where the visual concept needs them, with explicit source provenance. Notes live in content-units, not directly edited Markdown. Teach the visual before a card requires it. Add/correct objective mappings to cover the new planned diagram objectives without deleting old mappings.

Do not invent `question_asset_id` or `answer_asset_id` fields in canonical learning items: the repository schema does not have them. Keep a separate manifest keyed by item ID with question/answer image paths, master/data paths, hashes, descriptions and exact semantic values/relationships. Put all necessary solution facts in canonical_answer and marking_guidance as text as well.

For offline notes, canonical block text may reference the local image as `diagrams/<derived-image-name>.png`, resolving under the topic directory. Render notes with the standard renderer. A reproducible subject-owned publication helper must run the standard publisher, copy the referenced PNGs into the generated publication’s notes/diagrams directory and verify every image reference resolves. Copy the asset manifest with generated publication-relative paths as an upload sidecar. Do not edit exported notes or JSON by hand, and do not assume the standard publisher copies arbitrary new assets.

The repository-relative manifest is the bridge to later import, not a live URL list. Local files are reviewed first. No cloud upload, classroom write, Git commit or push is included in this authoring handover.

## Current YYeni integration design

Verified via the live MCP flashcard contract: each imported card can carry one managed `question_asset_id` and one managed `answer_asset_id`. The app stores the resulting question/answer image URLs; its teacher upload flow uses GCS, and the learner pages render these images separately. Use one composite image per side for multi-panel figures.

Later, with the classroom import authorised, import approved PNGs through the YYeni managed-image workflow and record returned IDs by repository item ID and side. Preview card import with those IDs, show the exact classroom/cards, obtain teacher approval, confirm and reconcile saved cards/assets. Do not store an expiring signed upload URL or raw markup link in place of a managed asset attachment. Current image IDs, storage ACLs, learner drawing input and live Recall grading still need verification at import time.

## Checks and independent review

Preserve reviewed conditions, legal qualifications, homogeneity wording, National Income valuation basis and correct age-dependency interpretation. If a claim changes, increment its revision, update all claims_seen and record reviewed_unchanged on unchanged citing artifacts. Re-stamp edited blocks/items with operations/tools/restamp.py, regenerate notes, run the topic checks and what_to_fix.

Do not publish incomplete topics while the other author’s slots are missing. After all planned cards exist, run all 28 checks and reconcile 625 items exactly. Keep warning/not_run results visible. `depictions.chart_model: none` means the shared checker cannot judge these curves; it does not constitute visual validation. Supply a separate reproducibility/geometry report and a thumbnail/contact-sheet index for Codex to inspect every question and answer image.

Record every affected block/item, asset path and hash and every deviation. Stop for **Codex review of the visual changes**. Codex checks all 24 images, coordinates, mechanisms, textual answers, rubrics, image references, learner answer leakage and narrow-display legibility. A PUBLISH result alone cannot substitute for that review. Report completed/blocked items and exact counts; do not claim a cloud upload or classroom import.
'''
(W/'CLAUDE-DIAGRAM-HANDOVER-6145.md').write_text(claude)
main=f'''# Revision handover — 6145 NSSCO Economics

This replaces the original whole-subject authoring prompt, archived in planning/revision-01/baseline/. Revision-01 is **proposed; approval pending**. Do not run an old whole-subject bootstrap.

## Stage 1: approve and activate

Read STATUS.md and PLAN-6145-nssco-economics.md. Vitalis authorised reopening Step 4, not yet the generated {v['items']}-item scope. After approval and the requested plan checkpoint, promote candidate curriculum, subject profile and generated contracts/orders to their corresponding live paths. Preserve all canonical claims, content units, items and the current publication. The qualification profile has no changed assessment facts. Re-run the scope verification and record activation. Do not label stale old topic QA as a completed build of the new scope.

The generator is planning/reopen_step4_6145.py. It builds a candidate through shared standard generators in a temporary workspace, preserves IDs through an explicit semantic migration, and writes only revision planning files. It asserts the saved reviewed-content hashes; do not reset those assertions to conceal a changed baseline. The final scope verifier must accommodate completed authorised authoring rather than rerun an old author script.

## Stage 2: Codex nonvisual authoring

Role AUTHOR, workspace work/nam-6145-nssco-2026/. Read AGENTS.md, TEAM-PLAYBOOK.md and only the AUTHOR role brief. This narrowed assignment overrides the generic whole-subject run. Use `planning/revision-01/scope.json`, filtered owner Codex: **{v['new_nonvisual_cards']} exact new slots**. Fill the named standard term or function, not a generic abstract category. Follow the labels and use current reviewed notes and the syllabus/corpus anchors. Add a claim where the named concept has no suitable canonical claim, and teach/map it in the existing content unit. Preserve source provenance and all prior fixes.

Complete the ten `notes-budget-work-order.json` tasks, preserving examinable points. Review the single internal-growth retargeting proposed in the plan and record it in authoring_notes before changing its existing prompt/claim dependencies. Do not alter valid cards merely for style, re-author the whole subject or pad prose to a minimum. Recalculate actual block words. If a budget cannot accommodate the named teaching, report it to the planner rather than silently changing the envelope.

Preserve all 580 existing IDs and labels and add exactly the assigned 37 cards. The eight pending Claude visual slots must remain explicitly pending, not filled with placeholders. Several topics will be incomplete until both phases finish; do not republish an incomplete extension as complete. Re-stamp and render affected canonical material, and record partial completion honestly.

## Stage 3: Claude diagrams

After the nonvisual phase stops touching shared topic files, paste CLAUDE-DIAGRAM-HANDOVER-6145.md into Claude. Its exact assignment is eight new and four existing diagram cards with 24 PNGs and 24 SVG masters. Codex will review those images and diagram edits. Claude also independently reviews Codex’s new nonvisual cards and budget edits; distinguish these review responsibilities in STATUS.

## Stage 4: finish and validate

Once all {v['items']} items and assets exist, run all topic checks, complete slot/label reconciliation, copied-wording checking against subject-only assessment extracts, actual-word counts, claims/revision/hash checking, repeatable asset generation, per-side image-reference checks and canonical/export equality. Regenerate using the standard note/publish tools plus the subject-owned asset-copy helper described in the Claude handover. Never edit exports by hand. Report C-18, any C-26 and all not_run limitations honestly.

Then return for the human review/Git checkpoint. A later classroom import remains separately authorised. The later import maps local manifest sides to YYeni managed question_asset_id/answer_asset_id; it is not part of this authoring pass.
'''
(W/'HANDOVER-6145-nssco-economics.md').write_text(main)
# Record the live attachment contract without making a cloud write.
(R/'yyeni-image-integration.md').write_text('''# 6145 diagram attachment design — checked 28 October 2026

Read-only live tool: YYeni get_flashcard_contracts. It exposes question_asset_id and answer_asset_id as optional managed image IDs; question/answer are Markdown and LaTeX. The app uses question_image_url and answer_image_url. The teacher AddCardModal obtains url/publicUrl from /api/chat/upload-lesson-res, PUTs the image to GCS and saves publicUrl. Learner practice.js and workout.js render the URLs on their respective sides.

Do not infer that arbitrary GCS objects are accepted as MCP managed assets. Use import_flashcard_image or the supported managed render flow at the later import stage; record actual returned IDs. No image was rendered or imported through the connected app in this planning pass. No storage bucket/ACL or deployed UI acceptance was tested.

Repository canonical learning items have no native asset_id fields. A sidecar mapping must join each repository item ID to question/answer PNGs and later managed IDs. This file is an integration observation, not a claim that image assets exist.
''')
print('Rendered revised plan, main handover, Claude handover and ten-unit budget work order')
