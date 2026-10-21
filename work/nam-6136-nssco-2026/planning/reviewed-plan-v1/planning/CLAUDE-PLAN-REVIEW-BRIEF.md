# Independent Claude Code review — 6136 NSSCO Development Studies, Step 4 plan

Jeremy explicitly asked: “let claude code review the plan”. Review the COMPLETE current plan independently. You are the plan reviewer, not an author and not the eventual Step 6 resource reviewer.

Repository cwd: /Users/jeremytiboth/Documents/yyeni-study-resources
Workspace: work/nam-6136-nssco-2026/

## Authority and process

Read AGENTS.md, TEAM-PLAYBOOK.md (especially Step 4), the PLANNER role only, and workspace STATUS.md. Codex is now the final author and Claude Code the final independent reviewer, per Jeremy on 2026-10-20. Sources, syllabus and corpus checkpoints are approved. The whole-subject plan is awaiting human approval. Vitalis's pilot agreement is already confirmed; do not ask again. Jeremy rejected an extra two-topic authoring trial and has no access to a subject teacher: do not invent either as a blanket gate. Actual source and technical gaps must remain explicit.

The old three-topic retrofit is historical evidence, not the scope. Scope is all ten themes/18 topics of Namibia NSSCO Development Studies 6136, Grades 10–11, including Research Techniques.

## Read the concrete plan

All paths below are relative to the workspace unless stated otherwise.

- PLAN-6136-nssco-development-studies.md and HANDOVER-6136-nssco-development-studies.md
- qualification-profile.yaml and subject-profile.yaml
- curriculum/syllabus-facts.json and curriculum/source-bullet-bridge.json
- curriculum/objective_registry.json: check ALL outcome/member decompositions for missing scope, invented demand, duplication and incorrect objective types. There are 101 integrated source outcomes plus 292 members and 18 structural roots; 102 original source rows include a repeated enterprise continuation.
- curriculum/assessment-framework.json, exam-exposure.json and performance-slot-specs.json
- curriculum/answer-shapes.json, misconceptions.json, glossary.json, scope-scan.json and quality-evidence.json
- planning/registry_decisions.json, member_evidence_decisions.json and profile_quality_decisions.json (explicit semantic judgements)
- planning/plan-validation.json, plan-summary.json and standard-compatibility.json
- topics/*/contract.json and work_order.json: inspect the complete subject distribution, and read representative full work orders for 1.1, 3.1, 7.1, 8.1 and 10.1 plus any suspect branch.
- exemplar/README.md and exemplar/validation.json; inspect the actual capital and pilot-study examples in exemplar/proof/work/nam-6136-nssco-2026/topics/{3.1,10.1}/. Those are thin slices with a reduced proof registry, not completed main topics.
- planning/build_plan.py, finalise_plan.py and build_exemplar.py; inspect the standard builders/checks as needed to assess whether generated labels, guidance and validation mean what the plan says.
- Repository-level operations/analysis/6136-nssco-development-studies-corpus-analysis.md
- assessment-evidence/assessment_evidence.json and GAPS.md. The canonical map conforms to the evidence schema and uses final objective IDs. Full internal question stems and original 102-source-bullet map remain in planning/source-bullet-evidence.json and source-bullet-exposure.json. Member mapping is conservative/partial, not inherited parent frequency.

## Verify against primary evidence

Primary authority is Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf. Read PDF pp.8–26 (printed content pp.5–17 and assessment/research pp.18–23), and glossary PDF pp.27–29. Use Read pages batches within tool limits. You reviewed the Step 2 transcription previously, but this is a fresh session; do not substitute Codex's extraction for the source.

Read assessment-evidence/source-manifest.json to locate this subject's papers and report PDF page ranges. Independently spot-check representative actual papers/report passages supporting the plan: capital/production, numerical/population data, and Paper 3 methods/pilot/findings/conclusions/practical problem solving. Raw/layout extractions under assessment-evidence/extracted/ can help navigate, but identify which claims you checked against primary PDF pages. Reports are NOT standalone mark schemes. Do not claim exact credit structures when no scheme or report statement establishes them.

## Questions requiring your judgement

1. Are qualification, scope, paper marks/durations/weights, AO A/B/C/D definitions and allocations faithful to the source? Do not import AO1–AO4 meanings. Qualification totals A35/B47.5/C12.5/D5 are sums of the printed grid rows; A.1/A.2 remain combined.
2. Does the 393-target decomposition preserve ALL clauses and actual source relationships without making illustrative examples compulsory, creating duplicate facts or unnecessary breadth? Are topic and member objective types appropriate? Is the generated 95,350–137,040-word budget proportionate, or inflated by containers/member duplication? Assess this from sources and the plan; do not assume counts imply quality.
3. Are the selected commands/tariffs appropriate for the actual demanded answers, not merely observed somewhere in the corpus? Is exclusive primary-command counting being over-applied to prohibit legitimate multi-part instructions or research reasoning? Does a short tariff get forced to satisfy too many generic answer-structure keywords? Are Define/State, description, explanation, data interpretation and genuine evaluation distinguished?
4. Do AO assignments reflect the task, especially applied A.3, analysis B, investigation C and practical problem solving D? Are paper/topic allocations justified? Check whether assigning e.g. every overview Suggest to A or every research definition to C is defensible. The plan has exact A39.2874/B45.8432/C12.5416/D2.3278: within five percentage points, but does that tolerance mask a meaningful skill deficit? Do not demand padding merely to chase percentages.
5. Are the 737 flashcard slots and 42 performance activities coherent and non-redundant? Do four 35+15 research cycles actually practise distinct methods/data/problems? Inspect the exact subpart plans, including claimed AO splits and command semantics, not only headline totals. These are planner practice estimates, not official section-level rubrics.
6. Do the seven quality-evidence criteria accurately reflect 6136 source passages? Have reusable patterns from other subjects been adapted rather than importing their content, rubrics or assessment assumptions? Is the settled glossary accurate at this level?
7. Do the scope patterns genuinely enforce syllabus limits, and which important risks remain for semantic review? Is no-content-exclusion being confused with no upper-level boundary?
8. Do the exemplars show sound pedagogy and marking guidance, or only schema conformity? Can every answer be reconstructed from the notes? What precisely do their checks prove or fail to prove?
9. Are the recorded stale profile schema, graph-model limitations, run_checks exit-code mismatch, and not_run/PUBLISH conflict correctly handled? Identify any actual bypass or unsafe claim. Do not edit standard/ or relabel a missing check PASS. Separate standard-owner issues from fixable plan defects and from transparent non-applicability.
10. Is the handover clear enough for Codex to author the whole subject without inventing remaining educational decisions? Are the roles, checkpoints and missing sources represented honestly?

## Output and boundaries

READ-ONLY. Tools are restricted to Read, Glob and Grep. Do not edit any file, execute scripts, create subagents, author main resources, access web/MCP, commit/push, or contact anyone. This is a single independent plan review; stop after the report.

Return a self-contained Markdown report on stdout. Codex saves it verbatim.

1. Verdict: READY FOR HUMAN PLAN APPROVAL, FIX PLAN FIRST, or BLOCKED, with the reason.
2. Exact files/source PDF pages actually inspected and sampling/verification limits. Do not claim a complete source audit from a sample.
3. Prioritised findings table: stable finding ID, severity, exact file/key/slot or source page, confirmed issue vs uncertainty, consequence, and concrete correction. Give examples rather than generic advice.
4. Assessment of coverage/depth, command/tariff shapes, AO balance and practical research demand. Identify what is sound as well as what fails.
5. Which findings Codex can fix in the plan and which require the standard maintainer. Teacher access or an additional authoring trial is not a substitute for this evidence-based review.
6. Whether Jeremy should approve this plan as it stands, and the minimum necessary changes before authoring.

Do not present your judgement as subject-teacher approval or a final resource publication verdict. Do not silently assume absent mark schemes or unreviewed member mappings.
