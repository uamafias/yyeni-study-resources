# STATUS — 8224 Chemistry (Namibia NSSCAS)
Workspace: work/nam-8224-nsscas-2026/   Owner: Jeremy   Authoring tool: Codex   Review tool: Claude Code

Pilot: first NSSCAS subject; run with Vitalis's agreement (Jeremy, 2026-10-18). Topic 1.1 (Atoms, molecules and stoichiometry) is the step 4 exemplar slice. This workspace began before the playbook was read; earlier files (`CLAIM.md`, `REVIEW.md`, `REVIEW-RESPONSE.md`, `curriculum/SYLLABUS-SUMMARY.md`, `assessment-evidence/`) are working notes. They do not replace `syllabus-facts.json` or the corpus analysis.

- [x] 0 Claim: tracker row added — 2026-10-18; committed in b7ca4eb on 2026-10-22
- [x] 1 Sources found — 2026-10-18 (syllabus NIED 2020, updated 20 Nov 2020; 12 papers 2021-2024; 0 mark schemes; 1 examiner report, 2025 only)
- [x] 1 YOU: sources complete — Jeremy, 2026-10-18
- [x] 2 Syllabus facts written (`curriculum/syllabus-facts.json`; 143 quotes re-verified by `planning/mine_syllabus_8224.py --verify`; brief at `operations/analysis/8224-nsscas-chemistry-syllabus-brief.md`) — 2026-10-18
- [x] 2 YOU: AO table and paper table checked against the PDF — Jeremy, 2026-10-18
- [x] 3 Corpus analysis written (`operations/analysis/8224-nsscas-chemistry-corpus-analysis.md`; evidence 475 records, `curriculum/exam-exposure.json`, `answer-shapes.json` (partial), `misconceptions.json` (19, single-source), `scope-scan.json` (10 drafts), gap register and all 76 diagram-dependent records visually checked) — 2026-10-21
- [x] 3 YOU: analysis read — Jeremy authorised progression into planning, 2026-10-21
- [x] 4 Plan built — 2026-10-22. Both structural exemplars reach PUBLISH with zero failed checks; Topic 5.1 is validated against its five-objective reduced scratch contract. Current AO gap: 4 points; approved and committed locally in b7ca4eb.
- [x] 4 YOU: plan approved — Jeremy, 2026-10-22 (explicit “approved” in this session)
- [x] 4 YOU: plan committed locally — 2026-10-22, after Jeremy’s approval; remote push outstanding
- [x] 5 Topics authored: 21 / 21 (all topics complete; blocked: none) — 2026-10-22
- [x] 5 Local package generated and verified — 2026-10-22; independent review complete; human diagram and applicable claim approvals remain recorded as pending
- [x] 6 Reviewed by Claude: verdict **publish**; operator final validation complete, all 21 topics PUBLISH with zero failed checks. Four substantive findings fixed; 12 low findings open. Human diagram and applicable RS-13 claim approvals remain recorded as pending. 2026-10-22; see review/claude-full-r1/REVIEW.md and operator-final-validation.json
- [x] 6 YOU: verdict read — Jeremy requested “Publish now” after receiving the final verdict, 2026-10-22
- [ ] 7 YOU: committed and pushed
- [ ] 8 (diagram) Compare with existing YYeni NSSCAS Chemistry cards (school 17, classroom `a5695c1d-390d-4025-b013-2e218a2c1ca9`; 0 cards on 2026-10-18)
- [ ] 8 (diagram) YOU: approve replacements, preview and import into YYeni

## Quality policy (reconciled with the playbook, 2026-10-22)
- Codex authors this subject and Claude Code performs the required independent cross-vendor review in a fresh context.
- RS-12 governs claims: source-backed, externally verified against an approved authority, or transparently derived from verified premises. There is no blanket two-source publication rule.
- A knowledgeable Chemistry teacher sample is recommended when available, but is not a release prerequisite. RS-13 still requires human approval for unresolved low-confidence, jurisdiction-specific, contested, medical, legal or safety-sensitive claims.
- Every generated diagram is viewed by a person, not only checked by data checks.

## Step 3 limits to carry forward
- No mark schemes 2021-2024; one examiner report (2025, papers not held). All 19 misconceptions are single-source.
- All 76 diagram-dependent evidence records were checked against 46 page images on 2026-10-21; see `assessment-evidence/IMAGE-REVIEW.md`. One locator was corrected and no meaning mapping changed.
- 2024 Paper 2 Q1(a)-(f): 6 marks inferred at 1 each (page shows only a total of 6).
- The keyword-based frequency count in `assessment-evidence/FREQUENCY-COUNT.md` is superseded by analysis section 5; do not quote it.
- Step 4 has started: `objective_registry.json`, `assessment-framework.json`, `glossary.json`, `subject-profile.yaml`, `qualification-profile.yaml`, 21 topic contracts and 21 work orders have been regenerated after Claude's review. The repaired plan has 253 objectives, 565 flashcards, 66 performance tasks and AO mix A 44%, B 39%, C 18% (largest gap 4 points). Topic 1.1 is complete (27 claims, 5 units, 30 items) and reached `DECISION: PUBLISH`. The thin Topic 5.1 titration slice (6 claims, 1 unit, 4 items, 426 content words) now passes reduced-contract validation. Both exemplars have 40 PASS, 1 WARN and 3 NOT_RUN results, with zero failures. The practical slice warning compares its legitimate 100% AO C to whole-qualification targets; graph/chart/practice-text checks are inapplicable. These are structural check results, not independent claim verification or release approval.

## Open items carried over (not playbook steps)
- Resolved 2026-10-22: Jeremy explicitly authorised adding `EQUATION` and `DIAGRAM` to both shared-schema subtype enums. Topic 1.1’s temporary PROC exception was removed and its planned EQUATION subtype restored; history remains in authoring_notes.json.
- YYeni template objective records need repair (lessons 6626, 6658, 6508, 6674 and 6832 identified in the live audit). Topic 1.2 also needs a lesson in the existing classroom and lesson 6658 needs moving to the correct existing section. Nothing has been repaired: changes require an exact YYeni preview and approval.
- The old keyword frequency classifier remains unvalidated and superseded. The 2024 Paper 2 page-image check confirmed six one-response parts under `[Total: 6]`; the one-mark-per-part allocation remains explicitly inferred.
- Evidence and knowledge gaps are maintained in `assessment-evidence/GAPS.md`; authoring uses the local corpus rather than per-card web searches.
- Parked: `work/nied-6117-nssco-2020-2024/` (NSSCO 6117, earlier start; Lotto covers Ordinary).

## Step 4 completion — 2026-10-22
- `planning/validate_practical_exemplar_8224.py` copies the local curriculum/evidence into a temporary workspace, narrows only the Topic 5.1 registry branch and exemplar contract, renders notes and runs the unchanged shared check suite. Durable outputs are in `exemplar/5.1/`, including the reduced contract, context, report and hash manifest. The full practical contract and 84-slot work order remain intact.
- Fixed early rounding: 24.375 cm³ is retained through cV and the final concentration is 0.09750 mol dm⁻³ to four significant figures.
- Corrected the framework's permitted subtype/AO union to include C for PROC, APP, CALC, INTERP, EVAL and SYNTH; the subject profile still chooses actual AOs by objective and paper.
- Corrected nested exposure evidence to recompute from direct objective mappings. All 39 practical criteria currently have no direct bullet-level evidence mapping; the existing broad skill-category figures are retained only as explicitly labelled planning proxies (`frequency_basis`). They must not be described as per-objective examination frequencies. No contracts, work orders or slot allocations were regenerated.
- Shared CLI defect observed: `run_checks.py` prints PUBLISH but returns 1 because it compares the release decision with `pass`. The workspace validator checks the persisted `publish` decision and every check status; no standard file was edited.
- Completed checkpoints: Jeremy approved the plan (committed locally as b7ca4eb), then explicitly approved the narrow shared-schema extension. Next: author Topic 1.2 and the remaining topics in numerical order without another scope-approval request.

## Approval recorded — 2026-10-22
Jeremy explicitly approved the completed plan: 21 topics, 253 objectives, 565 flashcards, 66 tasks and 65,205–92,861 notes words. Scope approval is complete. The shared-schema decision was subsequently approved separately; the exact applied patch is retained under `planning/schema-compatibility/`.

## Shared-schema extension completed — 2026-10-22
- Explicit instruction: Jeremy said “yes extend shared schema”, overriding the author-role restriction only for this change.
- Added EQUATION and DIAGRAM to both subtype enums in `standard/v0.2.0-draft/schemas/learning_items.schema.json`. No checker logic or other standard file changed. The approved 21 equation and 30 diagram slots retain their original demands and metadata.
- Restored ITEM-8224-1.1-019-EQUATION to EQUATION, removed temporary procedure-only marking guidance, restamped it and removed the workaround from the exemplar generator. No topic was rebuilt.
- Validation: four existing schema tests executed directly (pytest is unavailable in the default interpreter), acceptance checks for both new labels and rejection of an unknown label; all passed. Topic 1.1 and the reduced practical exemplar both retain PUBLISH with zero failed checks. Their existing AO warning and three inapplicable checks remain.
- Next action: full subject authoring, starting with Topic 1.2. No additional plan or subtype approval is pending. Claude review remains reserved for the complete subject.

## Pre-build preparation completed — 2026-10-22

Jeremy authorised the preparation pass after asking whether everything was ready. Scope approval and the approved schema extension remain valid; no plan regeneration occurred.

- Recovered the exact original NSSCAS Examiners Report 2025 from NIED into this subject’s reference pack. The SHA-256 matches the previous record, so the 92 derived report records remain attached to the same source content.
- Archived and indexed the OpenStax Chemistry textbook (2015 edition, 2017 revision; 1,355 pages), the Organic Chemistry Tenth Edition study guide (222 pages), 40 organic textbook sections and the current Chemistry 2e mole section. All 253 objectives have topic-level reference routes; claims must still cite exact supporting locators and be semantically checked. The existing registry coverage ratings describe the old corpus; use the new reference inventory alongside them without regenerating frozen work orders.
- Harvester integrity verification: all three acquired PDFs readable, none corrupt or image-only. Each HTML reference was checked for substantive textbook article content rather than a page shell. URLs, dates, hashes and searchable text are recorded locally.
- Added subject-local original SVG/PNG generators for charged-particle paths, displayed ethanol, gas-volume/rate data and titration apparatus. A one-objective visual pilot passes with zero failed checks. Asset generation reproduces byte-for-byte; local image references survive the subject-local publication wrapper. These pilot outputs are not counted as additional production Topic 1.2 items.
- `exemplar/visual/contact-sheet.png` was inspected by Codex; repaired a font-glyph issue and made the proton/electron relative deflection clear. This is model inspection only. Human visual review remains required before final publication.
- Use `planning/publish_chemistry_8224.py` for the eventual full-subject package: the generic publisher does not copy image assets. The wrapper requires passing reports and validates image paths, then carries assets into both notes and flashcards. No shared code changed in this pass.

Next: author Topics 1.2–5.1 sequentially from the approved work orders. Full-subject Claude review, human visual inspection and platform import remain later stages. No further plan or preparation approval is required to begin.

## Full authoring run — 2026-10-22
Jeremy said “start”. Topic 1.2 is now authored: 40 claims, three content units, 35 items and 4,026 content words. The full checker reports PUBLISH with zero failures and the expected topic-level AO warning. Original field/orbital visuals have model inspection; human visual review remains pending before final release. Two MECH slots were transparently authored as WHY because their particle-property/nucleon-counting targets do not involve reaction intermediates or products. Labels, objectives, command words and tariffs are otherwise preserved. Next: Topic 1.3.

Topic 1.3 authored: 60 claims, six units, 55 items, 7,095 content words. Full check decision PUBLISH with zero failures and expected AO warning. Seven MECH-to-WHY property-explanation deviations and the nanotube/C60 classification clarification are recorded. Four new visual previews inspected by Codex; human inspection is still pending. Al2Cl6 bridge connectivity is a source-verification focus for the later semantic review; the general dative model and syllabus example are documented, but the teaching reference pack does not directly establish that detailed connectivity.

Topic 1.4 authored: nine claims, one unit, ten items, 1,006 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY explanation deviation; generic variant-check punctuation defect documented without changing the shared checker. Both s.t.p. and r.t.p. and their respective molar-volume approximations remain explicitly taught. Current total: 136 claims, 15 units, 130 items, 15,094 content words. Next: Topic 2.1.

Topic 2.1 authored: 26 claims, two units, 26 items, 2,837 content words. Full check decision PUBLISH with zero failures and expected AO warning. Three MECH-to-WHY deviations; additional unmarked construction practice added to the planned pathway interpretation. Thermochemical standard settings are explicitly defined and separated from gas-volume reference settings. Percentage-equation checker scales a percent suffix a second time, so original correct working spells out percent; no shared checker changes. Two original diagram previews inspected by Codex after replacing unsupported superscript unit glyphs. Human review remains outstanding. Total now 162 claims, 17 units, 156 items, 17,931 content words. Next: Topic 2.2.

Topic 2.2 authored: 28 claims, two units, 25 items, 2,855 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; school selective-discharge approximation explicitly separated from engineered industrial recovery. Manganese process-specific evidence remains a semantic-review focus; no plant recipe or broad deposition guarantee is asserted. Total: 190 claims, 19 units, 181 items, 20,786 content words. Next: Topic 2.3.

Topic 2.3 authored: 26 claims, two units, 29 items, 3,263 content words. Full check decision PUBLISH with zero failures and expected AO warning. Four MECH-to-WHY explanation deviations; industrial temperature/pressure variables stated explicitly instead of the generic gas-volume conditions label. Constants, concentration changes, rate/yield interpretations and strong-acid pH worked examples are original. Total: 216 claims, 21 units, 210 items, 24,049 content words. Next: Topic 2.4.

Topic 2.4 authored: 26 claims, three units, 25 items, 2,638 content words. Full check decision PUBLISH with zero failures and expected AO warning. 8 MECH-to-WHY deviations; enzyme operating ranges distinguished from a universal on/off setting. Two analytic, normalized Boltzmann distribution figures generated and visually inspected by Codex; human inspection outstanding. Total: 242 claims, 24 units, 235 items, 26,687 content words. Next: Topic 3.1.

Topic 3.1 authored: 40 claims, four units, 40 items, 4,424 content words. Full check decision PUBLISH with zero failures and expected AO warning. 9 MECH-to-WHY deviations; state-dependent chloride bonding and aqueous aluminium hydrolysis explicitly qualified. General ionisation trends respect the detailed-pairing exclusion. Total: 282 claims, 28 units, 275 items, 31,111 content words. Next: Topic 3.2.

Topic 3.2 authored: 23 claims, two units, 21 items, 2,282 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; irregular melting points preserved. Nitrate decomposition, complete solubility directions, numerical melting data and cement-stage reference detail are explicit semantic-review focuses.

Topic 3.3 authored: 32 claims, two units, 25 items, 2,978 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; five-box construction practised in the structured task. Uranium identified as an actinide and its prepared-compound reduction separated from aqueous leaching. Specific local metallurgy references remain review points. Total: 337 claims, 32 units, 321 items, 36,371 content words. Next: Topic 3.4.

Topic 3.4 authored: 36 claims, five units, 33 items, 3,561 content words. Full check decision PUBLISH with zero failures and expected AO warning. Three MECH-to-WHY deviations; detailed halide tests, hot-alkali products and application distinctions recorded as semantic source-review focus.

Topic 3.5 authored: 29 claims, two units, 23 items, 2,811 content words. Full check decision PUBLISH with zero failures and expected AO warning. Four MECH-to-WHY deviations; N2O explicitly average +1; organic-fertiliser solubility appropriately qualified. Official WHO Q&A and pollutant page consulted once for the guideline/health issue, with durable verification metadata in the reference pack. WHO guidance distinguished from plant-specific legal emission limits, without numerical limits or current Van Eck compliance claims. Ammonium tetrahedral visual generated and inspected by Codex; human inspection outstanding. Soil/ecological mechanisms still require independent semantic reference verification. Total: 402 claims, 39 units, 377 items, 42,743 content words. Next: Topic 4.1.

Topic 4.1 authored: 15 claims, three units, 14 items, 1,445 content words. Full check decision PUBLISH with zero failures and expected AO warning. Genuine radical-chain MECH retained. Terminology, all named compound families, geometry and IR are taught; original fission/shape/synthetic-spectrum visuals inspected by Codex. Exact NSSCAS data booklet is not held: local authoritative IR references and explicit ranges accompany the practice; board-table alignment remains a verification focus. Total: 417 claims, 42 units, 391 items, 44,188 content words. Next: Topic 4.2.

Topic 4.2 authored: 53 claims, three units, 60 items, 7,120 content words. Full check decision PUBLISH with zero failures and expected AO warning. Three MECH-to-WHY deviations; genuine radical and electrophilic mechanisms retained. Exact syllabus cold acidified manganate endpoint, supported bromonium intermediate depth, and polymer/environment applications recorded as semantic-review focuses. Three original structure/mechanism figures visually inspected by Codex; HBr arrow origins/targets corrected after inspection. Human visual approval outstanding. Total: 470 claims, 45 units, 451 items, 51,308 content words. Next: Topic 4.3.

Topic 4.3 authored: 20 claims, two units, 22 items, 2,425 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; primary direct substitution explicitly has no discrete intermediate. Replacement-family detail and exact ethanolic school preparations require independent source verification. Two generated figures inspected by Codex; human approval outstanding. Total: 490 claims, 47 units, 473 items, 53,733 content words. Next: Topic 4.4.

Topic 4.4 authored: 17 claims, one unit, 24 items, 2,349 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation. All three planned misconception cards discriminate their specific wrong idea; ethanol iodoform exception and local OH-carbon classification taught. School preparation settings, coal extraction and alcohol-specific test verification remain review focuses. Ethanol visual inspected by Codex; human approval outstanding. Total: 507 claims, 48 units, 497 items, 56,082 content words. Next: Topic 4.5.

Topic 4.5 authored: 12 claims, one unit, 15 items, 1,933 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; calculation slot uses exact isomer counts rather than unrelated measured quantities. Restricted C4H8 enumeration distinguishes three connectivities from four forms. Two generated spatial figures inspected by Codex; human approval outstanding. Total: 519 claims, 49 units, 512 items, 58,015 content words. Next: Topic 4.6.

Topic 4.6 authored: eight claims, one unit, 11 items, 1,060 content words. Full check decision PUBLISH with zero failures and expected AO warning. No subtype deviations. Condensed carbonyl figure inspected by Codex; human approval outstanding. Topic 4.4 cross-link corrected to describe carbonyl structures rather than promise tests outside the frozen Topic 4.6 scope; re-rendered/rechecked, now 2,351 words.

Topic 4.7 authored: 20 claims, two units, 24 items, 2,631 content words. Full check decision PUBLISH with zero failures and expected AO warning. One MECH-to-WHY deviation; primary amine defined at nitrogen and base ester hydrolysis correctly gives salt before acidification. Original connection figure inspected by Codex; human approval outstanding. Total: 547 claims, 52 units, 547 items, 61,708 content words. All theory authored; next: full Topic 5.1 practical resource.


## Full authoring handover — 2026-10-22

All 21 topics read PUBLISH with zero failed deterministic checks and C-18 AO warning. No topics blocked. Totals: 625 claims, 56 content units, 565 flashcards and 66 performance tasks (631 items); 69,017 content words. The publisher counts 69,886 rendered notes words including headings/tables and presentation text; these are different counting methods, not different manuscripts.

Topic 5.1: 78 claims, four units, 84 items and 7,274 content words. Six distinct 20-mark practical families authored, with original/simulated datasets, calculations, recording, control, error and improvement practice. Initial C-31 omissions repaired by actual generated instruction-sequence, volume-curve and calibration-graph practice. Four practical figures inspected by Codex; human approval still outstanding.

Correction to earlier Topic 4.1 source note: the complete official Data Booklet is embedded in the held syllabus, Annexe E. Its IR table on printed p64 has now been read and incorporated; Topic 4.1 is 1,480 content words and again passes. Annexe D supplies the qualitative notes used in the practical topic. Carbonyl Topic 4.6's four-objective scope was rechecked against the actual syllabus content page and matches it.

`planning/authoring-build-report-8224.json` lists every topic's final counts/check result, all 81 recorded deviations/clarifications, and 51 explicit MECH-to-WHY slot changes. Exact slot IDs, objective mappings, AOs, Bloom labels, command words and tariffs agree with the frozen work orders across all 631 items. All units meet their individual budgets. Main plan mismatches: generic mechanism rubrics assigned to property explanations; isomer calculation appropriately uses exact counts; practical recording calculations retain table requirements. Additional structure/construction practice stays inside existing slots/tasks. Detailed factual/source focuses are retained in each topic's authoring_notes.json.

The subject wrapper generated `publish/nam-8224-nsscas-2026/`: 21 note files, 21 item files, index/manifests and 180 asset copies (30 figures × PNG/SVG/geometry × notes/flashcards). All asset hashes and packaged Markdown image references verified. Review-build status is explicitly displayed in the generated index/manifest.

**Next checkpoint: Step 6.** Independent Claude Code review has not been run; all 625 claims remain unverified and nonpublishable in their ledgers. Human diagram approval is also outstanding. C-35/C-41 do not independently check these image depictions, and the arithmetic regex has limited coverage; visual/model inspection and independent recomputation are not cross-vendor or human approval. Missing mark schemes and single-report misconception provenance remain as recorded above. No authored-work commit/push or YYeni import performed. Follow TEAM-PLAYBOOK Step 6: user commits the authored package and starts the fresh-context review in Claude Code.


## Independent Claude review — interrupted2026-10-22

User explicitly requested the review. Fresh Claude Opus/medium session171bd519-1270-4d30-ab79-bc043dd93e0e reviewed all notes and sampled items through Topic4.2 (15/21 topics), with a detailed worklog at `review/claude-full-r1/reviewer-worklog.md`. Initial checks reran21/21 PUBLISH; exact metadata audit631 items/zero mismatches. Copied-wording scan used12 Chemistry papers plus2025 report:10 matches of8–10 words, zero12+ matches. Final match allowances and two learner tests remain unfinished. The baseline is an uncommitted working-tree snapshot with a full pre-repair archive/hash manifest; no commit or push was made.

Claude stopped with HTTP429 account session limit, reporting reset at20:20 Africa/Windhoek on22 October2026. No final verdict or consolidated coverage report was produced; do not mark review complete. Remaining topics4.3–4.7 and5.1. No claim verification/publication flags have been advanced.

Claude identified3 substantive findings before stopping: reconcile nanotube syllabus classification; name Contact-process V2O5 catalyst; align Group17 H–X example with board Data Booklet431/366/299 and recompute132 kJ/mol and2.99 kJ. Codex applied these exact repairs after the interruption, revising4 claims and updating all dependent claim revisions/reviewed-unchanged notes. Repaired topics1.3,2.3,3.4 were restamped/rendered/rechecked with zero failures (C-18 warnings; authentic archived prior hashes supplied for unchanged dependents, clearing C-30); the local review package was regenerated. These repairs await independent confirmation by resumed Claude. Minor precision, spelling and diagram-label notes remain in the worklog.

Resume checkpoint: `review/claude-full-r1/operator-checkpoint.json`; command `python3 work/nam-8224-nsscas-2026/review/claude-full-r1/resume_review.py` after quota reset. It resumes the same independent review and directs Claude to validate repairs, finish6 topics and complete the required outputs. Initial authoring generators predate these manual review repairs: do not rerun them over repaired topic JSONs. Source ledgers/content units/items remain the source of record.

## Independent Claude review — completed (resumed session) 2026-10-22

**Coverage**
- All 21 topics: all teaching text in all 56 content units (1.1 field by field from the packet; 1.2–5.1 via the rendered notes generated from the same blocks).
- All 390 sampled items, plus 5 repair dependants.
- Every topic's authoring_notes, including all 81 deviations/clarifications.
- All 30 PNG figures, inspected by eye.
- Every worked number in the notes and sampled items, recomputed.
- Syllabus scope, the Data Booklet (constants, bond energies, IR table) and the Annexe D qualitative notes, cross-checked.
- Not read: the 241 unsampled items (except repair dependants), every claim locator individually, the SVG/geometry files and publish/.

**Repairs**
- The three Codex repairs (1.3 nanotube grouping; 2.3 V2O5; 3.4 Data Booklet H–X values 431/366/299 → 132 kJ mol⁻¹, 2.99 kJ) were independently validated from the current JSON, including claim revisions and dependants.
- Claude applied CC-8224-R1-004 in 3.4: AgBr "partially soluble in dilute ammonia" and AgI "insoluble in dilute ammonia", per Annexe D. This changed CLM-8224-3.4-019 (revision 1 → 2), block 3.4-3-01-b1, ITEM-3.4-016, and the claims_seen/reviewed_unchanged entries on ITEM-3.4-017, 018 and 019.
- Claude fixed spacing in blocks 1.3-6-01-b1 and 3.4-2-04-b1.

**Findings**
- 0 critical, 0 high, 4 medium (all fixed) and 12 low (open: precision, "sulph-" spelling, ~80 missing spaces before numerals, MCQ filler text, figure tidiness, bromonium mark-scheme alignment, 100 vs 101 kPa, tooling blind spots C-35/C-41/C-32).
- Plan problems (51 MECH slots on non-mechanism objectives; CALC on isomerism and on recording) were handled within slots and are not blocking.
- Copied wording: all 10 runs of 8–10 words are allowed (standard equations or option numerals).
- Both learner tests (5.1 titration practical; Contact-process conditions) can be answered from the notes.

**Preliminary verdict: publish.** Final operator validation is still pending: restamp, render and check 1.3 and 3.4; checks on all 21 topics; copied-wording recheck; then `planning/publish_chemistry_8224.py`. Human diagram approval and RS-13 claim approval remain outstanding; no claim was marked verified or publishable. No commit or push was made.

Outputs: `review/claude-full-r1/REVIEW.md`, `findings.json`, `coverage.json`, `repairs.json`.


## Final operator validation — 2026-10-22

Claude completed the resumed independent review with verdict PUBLISH after final operator checks. `review/claude-full-r1/REVIEW.md`, findings.json, coverage.json and repairs.json record the complete stated coverage, four medium findings fixed,12 low findings left open, and all10 acceptable copied-wording matches. The live CLI records confirm reviewer model claude-opus-5-5.

Final repairs in1.3 and3.4 were restamped and re-rendered. All21 topics were rechecked: PUBLISH, zero failures, C-18 warnings only. Exact slot/metadata audit again confirms631 items, no objective/AO/Bloom/command/tariff mismatches and51 recorded subtype deviations. All56 units meet budgets; updated content total69,073 words. Copied-wording recheck remains13 sources,10 runs of8–10 words and zero12+ runs; Claude explicitly allows each as standard equations or option labels.

Operator corrected only the new Annexe D source locator from printed p52 to p53 after checking the held syllabus (p52 is Annexe C). CLM-8224-3.4-019 advanced to revision3 for that evidence-only correction; all dependent stamps/history were updated. Its chemical text is the same revision2 wording Claude reviewed. This erratum is documented separately without altering Claude's original review report.

`operator-final-validation.json` records the final checks and fingerprints the current manuscript and figure assets. The subject wrapper uses that fingerprint to label only this matching build as independently reviewed, and includes the review files in the local package. Human approval for30 diagrams and the625 generated-gap claims remains outstanding; verification/publication flags were not advanced. No commit/push or YYeni import was performed. Next playbook checkpoint: Jeremy reads the verdict and arranges the remaining human approvals before release/import.

## GitHub publication — 2026-10-22

Jeremy requested “Publish now” and clarified GitHub as the expected destination. This authorises the subject-scoped commit and push normally performed by the person in playbook Step 7. Publishing the reviewed package does not assert individual claim verification or human inspection of every diagram. The source ledgers and package retain those pending approval states and the 12 open low-severity findings. YYeni import is separate. Publication branch: `nsscas-8224-chemistry`.
