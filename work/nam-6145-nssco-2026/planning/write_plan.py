"""Render the 6145 plan and handover from generated work orders."""
import json
from pathlib import Path

import yaml

WS=Path(__file__).resolve().parents[1]
load=lambda p:json.loads(p.read_text())
v=load(WS/'planning/plan-verification.json')
f=load(WS/'curriculum/syllabus-facts.json')
fw=load(WS/'curriculum/assessment-framework.json')
sp=yaml.safe_load((WS/'subject-profile.yaml').read_text())
q=load(WS/'exemplar/topics/1.1/qa_report.json')
root='work/nam-6145-nssco-2026'
table=['| Topic | Objectives | Flashcards | Practice packages | Notes words |','|---|---:|---:|---:|---:|']
for t in v['by_topic']:
 table.append(f"| {t['topic_id']} {t['title']} | {t['objectives']} | {t['flashcards']} | {t['practice_packages']} | {t['notes_words']['min']:,}–{t['notes_words']['max']:,} |")
table.append(f"| **Total** | **{v['assessable_objectives']}** | **{v['flashcards']}** | **{v['practice_packages']}** | **{v['notes_words']['min']:,}–{v['notes_words']['max']:,}** |")
ao=['| AO | Calculated qualification target | Planned marks-equivalent share | Gap |','|---|---:|---:|---:|']
for a in 'ABC':
 ao.append(f"| {a} | {v['ao_target_percent'][a]:g}% | {v['ao_share_percent'][a]:.2f}% | {v['ao_share_percent'][a]-v['ao_target_percent'][a]:+.2f} pp |")
L=['# Plan — Namibia NSSCO Economics 6145','',
   'Generated 28 October 2026 from the approved syllabus facts, accepted corpus analysis and generated work orders. Owner: Vitalis P Haupindi. Authoring tool: Codex. Status: **proposed; awaiting Vitalis’s scope approval**. Production authoring has not started.','',
   '## 0. What the syllabus says','',
   'NIED 2018, implementation 2019, first examination 2020; Vitalis confirmed the source and tables for the 2026 learners. The PDF does not itself give a terminal year. AO definitions are on printed p.13 / PDF p.17; scheme p.14 / PDF p.18; specification grid p.15 / PDF p.19. Every assessment fact is transcribed with its quote in curriculum/syllabus-facts.json.','',
   '| AO | Name | Paper 1 | Paper 2 |','|---|---|---:|---:|',
   '| A | Knowledge with understanding | 50% | 28% |',
   '| B | Application and analysis | 16% | 35% |',
   '| C | Evaluation and decision making | 34% | 37% |','',
   'Paper 1: 150 minutes, 80 marks, 50% of qualification; compulsory short answers (40) and applied cases (40). Paper 2: 120 minutes, 80 candidate marks, 50%; compulsory Q1 (20), plus three of five optional questions (20 each). No topic is optional coverage merely because some paper questions are optional.','',
   'The overall A/B/C targets of 39/25.5/35.5 are **calculated** from the equally weighted paper splits. A shared compatibility key calls them “stated_qualification_weight_percent”; that field name does not turn the calculation into a quoted table.','',
   '## 1. What the corpus says','',
   'The accepted 6145 analysis mines ten QPs and five Economics report sections, 2020–2024: 271 tariffed parts and 1,000 marks offered (800 candidate marks). All totals reconcile. There are 269 performance-comment records and 37 curated concept confusions. Most sources include answer/guidance tables; twelve 2020 P1 Section B parts lack complete answer grids. No standalone schemes or 2025 documents are held.','',
   'The recurring demands are precise retrieval, diagram labelling, causal development, use of case evidence, direction of change and supported evaluation. Fourteen source anomalies are quarantined in assessment-evidence/source-anomalies.json. Never inherit the currency-direction, public-good, real-debt, scale or numerical errors in those rows.','',
   '## 2. Command words and tariffs','',
   'Only observed primary directive/tariff pairs are used for individual card slots; prefaced/compound source forms remain documented separately. The selected card tariffs are Define 2, Identify 1, Explain 2 or 4, Use 4, Calculate 1 and Evaluate 8. All are observed primary forms. Packages additionally use Describe 6, Examine 7, Suggest 7, Explain 7, Discuss 7 and Evaluate 9. They are complete multi-part tasks, not a single 16/20-mark verb claim.','',
   '| Primary opening | Count | Tariffs observed |','|---|---:|---|']
for c in fw['command_words']:
 if c['word'] in {'Define','Identify','Explain','Use','Calculate','Evaluate','Describe','Examine','Suggest','Discuss'}:
  L.append(f"| {c['word']} | {c['observed_count']} | {', '.join(str(x) for x in c['observed_tariffs'])} |")
L += ['', 'Each work-order slot fixes its command and tariff. An embedded Calculate at 2 is not silently treated as a primary-opening pair; the chosen Calculate 1 is a focused result with method/meaning supplied in the teaching. Marking guidance must respect the one-mark tariff, without claiming three separate marks for formula, working and result.','',
      '## 3. Answer shapes','',
      'Read curriculum/answer-shapes.json. Short definitions need discriminating qualifiers; causal answers need a direction, mechanism and specified actor; a diagram task needs the correct representation and the amount of explanation actually requested. Two-sided decisions need developed opposing considerations and a supported judgement; descriptive Discuss tasks do not automatically need a debate.','',
      'Each topic has four complementary practice packages: a Paper 1 Section B-style 20-mark applied case; a 16-mark short knowledge mini-test; a Paper 2-style 20-mark structured case; and a 9-mark evaluation plan. The mini-test has eight independent 2-mark parts. Package AO allocations are planning estimates, not official per-part AO tables. Authors must make every part feasible within its topic and give a concrete answer/rubric, rather than repeat a generic answer skeleton.','',
      '## 4. Card types, assessment objectives and Bloom levels','',
      '| Subtype | Permitted AOs | Bloom level |','|---|---|---|']
for m in fw['flashcard_subtype_ao_map']:
 L.append(f"| {m['subtype']} | {'/'.join(m['assessment_objectives'])} | {m['blooms_level']} |")
L += ['', 'AOs and Bloom are separate axes. Read the exact slot labels; a tier-4 integrated demand can raise a recall-looking subtype’s cognitive level. A member row ensures a named concept is not omitted; a parent row practises the integrated distinction, mechanism or judgement. Do not give a parent and child the same definition card.','',
      '## 5. The topics','',*table,'',
      f"There are {v['content_units']} planned content units. The 223 assessable objectives comprise 96 original syllabus anchors and 127 finer member objectives. Every anchor has an explicit crosswalk in curriculum/objective-crosswalk.json. Open lists are visibly planner-specified realisations, not invented syllabus quotations. Examples include named forms of business, factors of production, money functions/qualities, tax forms and population measures. Separate calculation slots cover demand/supply elasticity, total/average revenue and absolute/comparative advantage. These do not share one generic calculation card.", '',
      '## 6. AO balance, in marks','',*ao,'',
      f"Largest exact gap: **{v['largest_gap_points']:.2f} percentage points**, within the five-point planning tolerance. This is recomputed from {sum(v['ao_marks'].values()):,.0f} marks-equivalent, using each card’s tariff and the declared package allocation. It is not an official predicted mark split or a pupil workload requirement. The shared ao_coverage.md rounds topic shares; planning/plan-verification.json preserves the exact calculation. Individual topics can differ from the qualification average.", '',
      'No AO top-up loop adds duplicate cards. The package mix supplies genuine short-answer, applied case and judgement practice. The marks-based target is the planning measure; the item-count check may still warn and that warning remains visible.','',
      '## 7. Misconceptions, glossary and scope','',
      'All 37 curated misconception entries have exactly one named MISCON slot, checked by ID. The card must discriminate the recorded confusion using an original test. Listing, unit omissions and answering habits are practised without falsely labelling them conceptual misconceptions. The glossary has 92 original settled definitions.','',
      'All seven syllabus-derived scope/depth safeguards appear in every contract; their 30 controls pass. These are positive-depth/definition/prerequisite guards rather than imported prohibitions. Economic rent, comparative advantage, monopoly/perfect competition and the glossary’s marginal concepts must not be banned by using another qualification’s exclusions. See the source-anomaly register before teaching these.','',
      'Member exposure is not invented by copying a parent’s counts to every child. Parent mappings stay intact. A zero at finer grain means no separate member-level mapping has been asserted; the parent evidence is still visible. Full coverage is maintained regardless.','',
      '## 8. Rules particular to this subject','',
      '1. Original invented Namibian cases, N$, British English, explicit conditions and relevant time horizons. No copied official question or case text.',
      '2. Notes teach each concept and mechanism before the cards use it. Full teaching depth does not mean repeated template paragraphs. Give numerical and conceptual examples where useful; stay within each generated word budget.',
      '3. Marking guidance names the actual content credited and the allocation. Required structure keywords are minimum components, not text to paste mechanically.',
      '4. Diagrams use declared original coordinates/parameters and generated assets or complete coordinate tables. Supply/demand geometry needs subject-specific checking; a business break-even checker is not evidence that an economic diagram is correct. Check shifts, intercepts, binding controls and new equilibrium independently.',
      '5. Conditions must travel with each mechanism. Distinguish a competitive binding wage floor from a universal minimum-wage claim; price responsiveness from revenue effects; growth from gains reaching households; depreciation from guaranteed external-balance improvement.',
      '6. Avoid unverified live legal thresholds and company-membership limits. For Namibia-specific consumer/employee protections, verify an official anchor before making a precise legal claim, or teach the sourced general principle with the limitation recorded. Never invent an Act section or claim a law is current from a dated report alone.',
      '7. Production authoring waits for Vitalis’s scope approval and plan commit checkpoint. Codex authors sequentially. Independent Claude review remains required after authoring; the exemplar’s deterministic result is not that review.',
      '8. Keep every card/package ID and five planned labels. Report a genuine mismatch before changing inputs; document any permitted deviation. Do not silently add, drop or relabel items.', '',
      '### Structural exemplar and validation','',
      'exemplar/topics/1.1/ contains an original complete thin slice: three objectives, eight claims, one 942-word content unit, ten cards and four packages. It has zero deterministic failures and decision PUBLISH. C-18 remains a warning about item-count AO balance; C-35, C-41 and C-43 are not_run because this slice has no graphical stimulus, generated depiction or separate practice text. No claim is thereby made that those checks have validated diagrams or texts elsewhere. Copy the structure, never its prose or cases.','',
      'The registry and qualification profile validate; the legacy subject-profile schema rejects the three runtime-supported extensions slot_plan, conditioned_mechanisms and depiction_rule. The base profile validates and the runtime reads these extensions. Standard files were left untouched. Other shared boilerplate references to Cambridge/AO4 and fractional-gap formatting are recorded in planning/plan-verification.json; this subject’s explicit A/B/C plan is authoritative.','',
      '**YOU: scope approval pending.** All production topics remain unauthored; the exemplar stays separate. No repository commit/push or YYeni classroom import is included in this step.','']
(WS/'PLAN-6145-nssco-economics.md').write_text('\n'.join(L))

H=f'''# Handover prompt — Namibia NSSCO Economics 6145

Paste below the line into the authoring session after the approved plan is committed.

---

You are the AUTHOR for Namibia NSSCO Economics 6145, workspace `{root}/`, owner Vitalis P Haupindi. The learner examination is in 2026. The accepted syllabus is NIED 2018, first examination 2020; the user has confirmed it for these learners. Do not invent a terminal validity year.

## Start here

Read AGENTS.md, TEAM-PLAYBOOK.md, this subject's PLAN-6145-nssco-economics.md, subject-profile.yaml, curriculum/answer-shapes.json and the AUTHOR role brief. This handover wins over generic business-oriented author instructions. Do not read another subject workspace. Approved syllabus facts and evidence already exist; do not re-mine or overwrite them.

Check STATUS.md first. **Do not author production topics until the scope approval and plan-commit checkpoints are ticked.** The exemplar is an example, not proof of user approval.

## The job

Author the complete 28-topic subject in syllabus order: {v['flashcards']} flashcards and {v['practice_packages']} packages, {v['items']} planned items, {v['content_units']} content units and {v['notes_words']['min']:,}–{v['notes_words']['max']:,} teaching words. Codex works sequentially; Claude may delegate according to the playbook. Use every topic's contract.json and work_order.json. Exact output filenames are generated in the work order.

The exemplar at exemplar/topics/1.1/ has eight ledger claims, one content unit, ten cards and four packages, with no check failures. Copy field structure and dependency stamps, not its prose, scenarios or volume. It is outside production topics and does not count as topic 1.1 authored. Its warning/not_run checks remain visible in qa_report.json.

Produce claims/canonical_claim_ledger.json, content-units/*.json and learning-items/topic_<T>_items.json for each topic. Every claim has a revision. Every block/item cites claims, carries claims_seen and a SHA-256 authored_hash from checks.yyeni_checks._artefact_text. Claims remain unverified and not publishable until the proper review/approval stage. Each item has a complete model answer and content-specific marking guidance.

## Every item carries its labels

Copy item_id from slot, subtype or item_type, assessment_objectives, blooms_level, command_word and mark_tariff. A MISCON slot also copies misconception_entry. Performance labels use the subject profile's declared task allocation: data_response B/C; short_answer A; case_analysis A/B/C; essay_plan C. Mark tariffs are 20, 16, 20 and 9 respectively. Package opening command is the actual first directive; every part uses an observed form and its stated tariff.

## Rules that come from the syllabus and corpus

1. The A/B/C names are those in the 6145 syllabus. Overall targets 39/25.5/35.5 are calculated from the equal paper weights, not a separately printed qualification table. Do not substitute AO1–AO4 conventions.
2. Every named member must be taught. A parent compares, links or evaluates; a child defines or practises its own concept. Do not duplicate a definition to fill a parent slot. The objective crosswalk identifies original anchors and planner-specified members of open lists.
3. Commands and tariffs come from slots. Calculate 1 awards one result mark even when teaching shows method. Diagram construction uses Use 4; interpretation is separate. Never treat every Discuss task as a debate or every 7-mark task as the same rubric.
4. Each package is a full original task with source facts and answers for all parts. The Paper 1-style data case has Describe 6, Examine 7 and Suggest 7; the knowledge set has eight two-mark parts; the Paper 2-style case has 2/4/7/7 parts; the 9-mark evaluation plan has developed opposing cases and a supported distinct judgement. If a narrow topic cannot support its package within scope, report the specific mismatch rather than invent an unrelated economic issue.
5. A MISCON card asks a discriminating question from the register; it is not another definition. Use new numbers/examples, never report wording.
6. Use original invented Namibian businesses or community settings, N$ and British spelling. Notes are a standalone teaching text. Do not pad answers with generic template phrases or paste the same rubric onto different cards.
7. Read assessment-evidence/source-anomalies.json and GAPS.md. Do not repeat the reversed imported-inflation mechanism, misleading public-good/private-sector line, blanket multinational legal-form claim, malformed population arithmetic or scale/diminishing-returns conflation.
8. Apply all registered conditions wherever a mechanism is asserted. Use exact real-income deflation when an exact index calculation is requested; label approximations. Elasticity coefficients are not percentages. Keep net migration and a migration rate distinct.
9. Derive diagrams from original parameters. Check geometry and numerical solutions independently, preserve explicit figure/coordinate data and resolve every referenced asset. Do not claim that the generic break-even chart checker verified demand/supply geometry. If using coordinates for a learner to plot, supply axes, labels, original/new points and the written reasoning.
10. No copied official question, case or marking wording reaches learners. No claims about what examiners reward or future question frequency. Source evidence is internal only.
11. For precise Namibia legal/current institutional claims, verify an official source rather than relying on a dated report. Keep general textbook principles and verified live law separate; record any remaining limitation.
12. Do not edit standard/, sources/, another subject, the approved curriculum, contracts or work orders. If a slot is semantically wrong, record the issue for the planner. Do not silently weaken checks or add cards solely to tune AO counts.

## Voice

Plain, connected explanatory prose with worked original examples, precise distinctions, labelled calculations and case-led reasoning. Each model answer is as long as its demand needs; no filler. A two-mark explanation should not become an essay. Each piece of marking guidance identifies the specific credit-worthy content and actual allocation.

## The work order is the approved scope

Exactly one item per slot. Report genuine required deviations in topics/<T>/authoring_notes.json as from/to/why; do not overwrite the plan. A planner must approve and regenerate a revised plan before a mismatch is silently normalised. Parent exposure is not automatically evidence for every named child.

## Finishing each topic

Run:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py {root} <T>
python3 standard/v0.2.0-draft/checks/run_checks.py {root} <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py {root} <T>
```

Fix failures, retaining warnings/not_run results. The run_checks CLI exits 1 even when the saved decision is publish; inspect qa_report.json and use what_to_fix, which exits 0 when no failures remain. Do not call a not_run check a pass. Update STATUS.md after each topic. If the same check fails three times, record the topic/check/attempts and continue other independent topics as the playbook directs.

After every production topic is clean, run publish_subject.py for the workspace and reconcile counts/exports. Do not publish the exemplar as a separate classroom resource.

## Boundaries

No Git commit/push or YYeni import by default. Follow the user's explicit authorisation and the playbook checkpoints. Business Studies import is deferred. Stop when production authoring/publication is complete so the user can start independent Claude review; **this subject still requires step 6 review**.

## Report back when the subject is finished

Report topics completed/blocked, actual counts, notes words, final decisions, warning/not_run limitations, deviations and plan problems. Do not call authored content independently reviewed or imported. Keep the summary under 250 words.
'''
(WS/'HANDOVER-6145-nssco-economics.md').write_text(H)
(WS/'exemplar/README.md').write_text('''# Structural exemplar — 6145 NSSCO Economics

This is a separate, original thin topic 1.1 slice for the Step 4 authoring pattern. It is not production content and must not be imported independently. The source generator is ../planning/make_exemplar.py; the adjacent topic QA report records the exact warnings and not_run checks. Run the checks from the repository root against work/nam-6145-nssco-2026/exemplar, topic 1.1.

The same claims, notes and content-specific rubrics are intentionally different from the official cases. This deterministic result is not a semantic review or a user approval of the subject scope.
''')
print('Plan and handover written; scope approval remains pending.')
