# Junior secondary (grades 8–9): resource-generation framework

Draft, 31 October 2026 (Claude). Approved for piloting by Vitalis on 1 November 2026; the pilot will revise it. This is how the playbook's seven steps run for Namibian Junior Secondary Phase subjects. It changes only what must change; every rule in `TEAM-PLAYBOOK.md` §5 still applies. Evidence: `GR4-9-SOURCE-MATRIX.md`.

## The idea in one paragraph

Grade 8–9 learners are taught the **revised Junior Secondary Phase syllabus** (Grade 8 from 2025, Grade 9 from 2026). That syllabus is the only authority. For six subjects it also states an end-of-Grade-9 semi-external exam set by DNEA. No paper has been set on it yet, but we hold two older generations of papers:
- the **JSSEE papers** (2018–2024) from the previous two-year phase: the same grades, exam body and format;
- the **old JSC papers** (2013–2019) from the three-year phase, examined at the end of Grade 10.

We mine both for tariffs, command words, answer shapes and learner errors, as we did for NSSCO. Every old question is first mapped to a current objective, so nothing that the current syllabus dropped, or that belonged to Grade 10, reaches a learner.

## What stays exactly as for NSSCO

- **Steps:** claim, sources, syllabus first, analysis, plan, author, cross-vendor review, publish. The YOU checkpoints are the same.
- **Rules:**
  - "mine, do not reproduce";
  - the check tools;
  - `syllabus-facts.json` with a page and a verbatim line for every value;
  - the AO-coverage tolerance;
  - Bloom, AO, command word and tariff on every card;
  - the visual-resource pipeline (plan, author, independent acceptance);
  - publication through a guarded build.
- **Naming** (playbook §6): workspace `nam-<subject>_jss-gr8-9-2026`, for example `nam-mathematics_jss-gr8-9-2026`; stem `<subject>_jss-gr8-9`.

## What changes

### Step 1: sources

Gather, in this order:
1. The **current (C) syllabus** from `Syllabi/Namibian Curricula/JSC (New)/`.
2. The **previous (B) syllabus** from `Syllabi/Namibian Curricula/JSC (Legacy)/`, where it exists. It is needed for the crosswalk.
3. **JSSEE papers** and the 2019 moderators' report.
4. **Old JSC papers** and that year's examiner reports. These are combined reports: extract only the subject's section, recording page ranges.
5. **DNEA specimen papers** for the 2026 exam, if they exist (Harvester).
6. **Revision notes**, as a coverage cross-check only.

The step 1 table gives each source a **generation (A, B or C)** and an **evidence band** (1 exam-evidenced, 2 legacy-evidenced, 3 syllabus-only).

### Step 2: syllabus facts (two additions)

1. **Grade tag.** Every objective records whether the syllabus places it in **Grade 8, Grade 9 or both**. The C syllabi set out content by grade; transcribe the grade with its page reference. The tag drives deck splitting at publication, so it must come from the syllabus, never from inference.
2. **Two assessment layers.** Transcribe both:
   - the school-based **promotion assessment**: continuous-assessment components and their weightings, and the end-of-year exam papers (for example, Physical Science: CA 35 %, exam 65 %);
   - the **semi-external exam** where stated (for example, Mathematics: Paper 1 short questions with no calculator, Paper 2 structured questions, set by DNEA and marked regionally).

   Every AO weight comes from the specification grid, page cited. Where a grid splits by component, keep the split.

### Step 3: corpus analysis, with a crosswalk first

New file `curriculum/legacy-crosswalk.json`: one row per question part in the B and A papers, with:
- `generation` and `year/paper/question`;
- `current_objective_ids`: the C objectives it tests, or empty;
- `status`, one of:
  - `in_scope`;
  - `in_scope_changed_wording`;
  - `grade_10_content`: in A only, and not in C;
  - `removed_from_syllabus`;
- the evidence: the C syllabus page that justifies the mapping.

Only `in_scope` parts feed the counts of tariffs, command words and topic frequency. Examiner and moderator report findings count only for objectives still in C.

The corpus analysis file keeps the playbook's nine sections, with three rules:
- **Weighting by generation.** B (JSSEE) is primary evidence for format, tariffs and command words. A (old JSC) supports topic frequency and learner errors, never format, because A was a Grade 10 exam with different papers.
- **Band 3 subjects** use the playbook's syllabus-only step 3: the syllabus's own assessment section, with no invented exam evidence.
- **Changes between B and C syllabi** are listed explicitly ("the plan's coverage of changed objectives rests on the syllabus alone"), because no paper has tested them yet.

### Step 4: plan

- **Size.** Smaller banks than NSSCO, sized from objectives × depth: the planner proposes and Vitalis approves. Expected range: 250–600 items per subject across both grades. This range is not a target: the pilot calibrates it.
- **Grades.** Every item carries `grade: 8 | 9`, inherited from its objective. Notes are written per topic in syllabus order, and topics are grouped by grade.
- **Reading level.** Learner text is plain English for 13–15-year-olds. The `subject-profile.yaml` sets a sentence-length and vocabulary rule; the pilot's reviewers check it.
- **Practice packages.** Their shape follows the semi-external papers where they exist (band 1), and the end-of-year school paper described in the syllabus otherwise. They are kept proportionate: no NSSCO-style 30-mark investigations unless the grade 9 papers set them.
- **Model workspace.** The nearest NSSCO workspace of the same subject family, using its shape only. For example, `nam-6137-nssco-2026` for JS Geography, or `cie-9702-as-2025-2027` for maths and science.

### Steps 5–7: unchanged

The same as NSSCO, with two exceptions:
- **Publication output** carries a per-grade split: `publish/<workspace>/flashcards/grade-8/` and `grade-9/`, one deck per grade per topic. YYeni then assigns decks by grade.
- **Cross-vendor review** adds one question: does any card teach content outside the grade or the C syllabus (for example old JSC Grade 10 content)?

## Standard and check implications (for the standard owner, not workspaces)

- **The crosswalk is new.** It needs one check, "no learner item cites only an `out_of_scope` legacy question". This will be filed as a change request in `operations/standard-change-requests/`.
- **Grade tag.** It must become a schema field on objectives and items, and the publisher must split by it.
- **Band 3 subjects.** They will meet checks that read exam evidence (`not_run`). Playbook §6 already says `not_run` is never a pass and that the fix belongs in the standard. The pilot will list exactly which checks are affected.

## Pilot

The playbook's pilot rule applies: the first JSS subject is run by Vitalis, and the kind is marked `piloted` when it publishes.

**Decided (Vitalis, 1 November 2026): Geography**, workspace `nam-geography_jss-gr8-9-2026`, stem `geography_jss-gr8-9`. It reuses the 6137 map and visual tooling we have just proven. Its evidence is a little thinner than Mathematics (JSSEE has no 2024 papers).

Mathematics, which has the richest evidence (both semi-external papers for four years, seven years of old JSC papers, both syllabi and notes for both grades), stays first in line after the pilot.

## Tracker

Use the same tracker table:
- Board and level: "Namibia JSS (gr 8–9)".
- Code column: "–". Subject: the syllabus title. Workspace: the §6 name.
- One owner per syllabus. That owner covers both grades: one objective registry and one plan span both grades, so splitting ownership by grade would duplicate steps 2–4.

The full subject list stays in `GR4-9-SOURCE-MATRIX.md` as backlog. No rows are claimable until the pilot publishes, except by Vitalis.
