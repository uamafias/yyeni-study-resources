# Independent review: Workbench PLAYBOOK (D3) and its quality, acceptance and exemplar documents

This is a read-only review of the learning design and author/operator instructions. I did not edit files, run commands, browse, or compute any hash. The plan-mode notice said to write a plan file and call ExitPlanMode. I did neither, because this task asks for the report as the final answer. Nothing was written.

## 1. Verdicts

**Pedagogical playbook (D3 learning standard, D4 gates, D6 PD1–PD6, factorisation walkthrough): usable with corrections.**

- Nothing in the learning standard is blocking.
- The chain from evidence to selected patterns to recipes is mostly sound. It runs from syllabus to demand inventory to pattern evidence to include/exclude/hold, and only then to a recipe (D3:95–116, 140, 560–571, 601–608; D4 Q02, Q08).
- The practice/test contract matches the owner decisions and the existing behaviour I checked in `docs/features/workout-bench.md`:
  - practice cannot move boxes;
  - progress comes from tests, once per recipe per round;
  - the feature record uses "Workbench Test".
- The corrections are concentrated in five areas:
  - undefined terms for holds, and the lack of a durable escalation trail;
  - an under-specified selection audit and zero-recipe path;
  - missing file locations and a missing role mapping for a fresh agent;
  - one referenced gate that does not exist;
  - an exemplar that does not meet its own stated standard.
- Several status statements are also overstated or stale.

**Technical appendix (D3:679–708): not validated, and honestly labelled as such.**

- The draft status is stated clearly. The commands are marked as argument shapes, not as things to run (D3:686–698).
- I confirmed that `yyeni_workbench_tools/__main__.py` and `work/namibia-nssco-6131/workbench/tools/package.py` exist. I did not run or inspect them, so I cannot confirm the "available today" claim about `package.py verify` (D3:700) beyond the file's existence.
- I raise only one defect in the appendix, finding F6 below. That finding is a document contradiction, not a request for engineering.

## 2. Findings

Each finding is labelled MANDATORY (fix before the playbook is called final) or OPTIONAL.

### F1. "Hold" has three unrelated meanings and no definition — MANDATORY, High

- **Where:**
  - D3:88–93 and 566–571 use hold for a capability gap.
  - D3:489–494 sends a missing source to Jeremy or Vitalis.
  - D2:233–235 and D3:598–599 use "held" for a recipe state after a defect.
  - A syllabus-backed demand with no observed pattern also needs a disposition (D3:105–106, 565).
- **Failure an author could cause:** parking an awkward demand as "hold" and never escalating it. A reader cannot tell whether it is a capability, source or scope hold. Alternatively an author escalates everything and floods the owners.
- **Minimal fix:** one short table in D3 listing three hold reasons, each with its trigger, its record, its escalation target and its release condition.
  - Capability: `capability-gaps.md`, flagged to Jeremy or Vitalis.
  - Source: flagged to Jeremy or Vitalis.
  - Unresolved scope/judgement: owner decision.
  - Keep the D2 recipe state "held" as a separate term, for example "withdrawn pending repair".
- **Verify:** a dry run on one accounting cashbook demand and one graph demand yields a unique hold type and record location.

### F2. Capability determination has no baseline, and the escalation trail is not durable — MANDATORY, High

- **Where:**
  - D3:501 asks for a "verified existing capability" but names no reference list.
  - D2:228–231 says the capability list is still to be enumerated.
  - The STATUS template (D3:409–435) has no line for capability gaps or for who was notified.
  - The Step C exit (D3:573–576) and the Step D exit (D3:626–627) do not require flagging before the owner checkpoint.
  - The flag is made "in the current session's report" (D3:503), which disappears when the session ends.
- **Failure:**
  - Two agents classify the same cashbook demand differently, one saying "supported" and one saying "held".
  - Alternatively, a hold is recorded in the file but Jeremy never sees it, and the owner's "analysis read" tick passes without any gap having been flagged.
- **Minimal fix:**
  - Add a `Capability evidence checked:` field to the gap record. It lists the sources consulted, such as the feature record and the router's supported response types, and the date.
  - Add a STATUS line: "Capability gaps flagged to Jeremy/Vitalis: <IDs, date, disposition pending/recorded>".
  - Make that line a precondition for requesting the "analysis read" checkpoint.
- **Verify:** a STATUS file with open gaps and no flag line cannot reach "analysis read".
- **Scope flag:** no engineering is implied. This is document structure only.

### F3. The independent-review request does not audit selection, exclusions or zero-recipe outcomes — MANDATORY, High

- **Where:**
  - The review template (D3:735–746) checks truth, tariff, variation, coverage, duplicates and presentation. It does not ask the reviewer to audit the include/exclude/hold dispositions or the observed-versus-syllabus-only labelling.
  - A zero-recipe outcome ends with its evidence record (D3:605–608). Step G is not triggered, so only the owner's tick stands between the author and a wrongly excluded subject.
  - D4:190 says review can reject the plan, but D4's gates give the reviewer no explicit list of items to check.
- **Failure:** an author or planner excludes a hard demand, or marks a whole subject "zero recipes", with plausible reasons. The only check is an owner tick, which the playbook elsewhere treats as insufficient for content acceptance.
- **Minimal fix:**
  - Add to the review template: "Audit every disposition, observed-versus-syllabus-only labels and the capability register against the cited locators."
  - Add a D4 Q02 evidence row: "for zero-recipe or heavily excluded outcomes, the exclusion list is included in the frozen review input".
  - State whether zero-recipe subjects receive a light independent check. I recommend one cheap review of the exclusion table only.
- **Verify:** a seeded mislabelled "observed" row is caught by a reviewer following only the template.

### F4. Fresh-agent usability: file locations and role brief missing — MANDATORY, Medium-High

- **Where:**
  - D2's directory layout (D2:22–46) has no home for the source inventory, demand registry, selection table, zero-recipe record, exemplar or capability-gaps file. D3:498 introduces `workbench/capability-gaps.md`, and D3:332 mentions `workbench/STATUS.md` only in the STATUS section (D3:406).
  - `PLAN.md` is listed as the recipe plan, but the selection table must exist before the plan (D3:571).
  - AGENTS.md says to read exactly one role brief and no others. D3:332 repeats "the one applicable role brief" without saying which of PLANNER, MINER, AUTHOR or REVIEWER maps to Workbench Steps A–G.
  - AGENTS.md also says the pipeline's checks are the contract (`run_checks.py`). D3:698 correctly says not to substitute them, but a fresh agent has no pointer to a Workbench-specific equivalent.
- **Failure:** a fresh agent invents its own paths, or reads the wrong role brief and inherits notes/flashcard rules such as the AO-gap target (a 5-point maximum) that do not apply to recipes.
- **Minimal fix:**
  - Add a paths table: `workbench/analysis/source-inventory.md`, `demand-registry`, `selection-table`, `zero-recipe-record`, `capability-gaps.md` and `exemplars/`.
  - Add a role-to-brief mapping, with an explicit "ignore notes-pipeline checks that do not apply" sentence.
  - Move the `capability-gaps.md` path into D2's layout, or add it to D3's paths table.
- **Verify:** a fresh agent given only AGENTS.md, TEAM-PLAYBOOK.md and D3 can state where it saves each Step A–D output.

### F5. Reuse of existing analysis may skip the pattern and marking evidence the Workbench needs — MANDATORY, Medium

- **Where:** D3:449–451 and 538–540 allow reuse of verified analysis when the syllabus edition and source hashes match. The existing corpus analysis (TEAM-PLAYBOOK step 3) is calibrated for AO exposure, command words and flashcard misconceptions. It does not necessarily record question-level patterns, method-mark and special-case credit, or part structure.
- **Failure:** an agent reuses a flashcard analysis, finds no pattern evidence, and falls back on "typical" patterns from memory.
- **Minimal fix:** add one sentence. Reuse is by reference only for the facts the existing analysis actually records. Pattern, part-structure and marking-credit evidence must be cited per locator for the Workbench selection table.
- **Verify:** every selection row has a paper locator and a marking locator, or states "none available".

### F6. D3 names a gate that D4 does not define (copied wording) — MANDATORY, Medium (document contradiction, not a technical blocker)

- **Where:** D3:712 lists "copied-wording" among checks "defined in D4". D4's Q01–Q14 contain no copied-wording or assessment-claim gate. D3:555–556 only says never to copy.
- **Existing authority:** TEAM-PLAYBOOK rule 6 and step 6, as I read them:
  - 12 or more identical words in learner-facing text is a defect.
  - 8–11 words are reviewed by eye.
  - Never write "examiners reward".
  - RS-36 requires assessment claims to cite assessment evidence.
- **Failure:** an author lifts a command phrase or a mark-scheme sentence into a recipe or its feedback. No Workbench gate catches it, and the playbook's own list of checks refers to something that does not exist.
- **Minimal fix:**
  - Add a D4 gate, or extend Q01 or Q09, referencing the 12/8-word rule applied to question text, solutions and feedback against the cited papers, mark schemes and reports.
  - Add a learner-text rule: no claims about what "the exam will contain" or what "examiners reward" without cited evidence.
  - Say that the existing check tool is untested for Workbench text.
- **Verify:** the Step F list and the D4 gate list match.

### F7. The exemplar does not meet the standard D3 sets for it, and it contradicts the guidelines it asserts — MANDATORY, Medium

Each sub-issue is cheap to fix by editing the walkthrough text.

- **No boundary case.** D3:61–65 requires a normal instance, a meaningful variation and a boundary case with checked solutions. The walkthrough shows three instances (WT §4) plus excluded classes. It has no boundary instance, such as the largest permitted coefficients or the smallest `a`/`b`.
- **No definition of "evidence of improvement".** D3:72–73 asks what counts as evidence of improvement. WT §6 separates correction from independent success but never says what the independent observation is. One sentence would do: a first-attempt full-credit answer on a fresh instance, without optional support, is recorded as one independent observation and is not mastery.
- **Feedback and variant text break the shared learner-text rule.**
  - The sample feedback (WT:130–133) writes "2(9x² − 25y²)", "3x" and "5y" as Unicode prose. The variation, response and result tables do the same (WT:71, 80–84, 110–115).
  - D3:380–381 (rule 2) says maths must be correct LaTeX from the first draft. Execution-status:66–67 and WT:157–160 say the walkthrough conforms to the shared conventions.
  - Only the task sentence (WT:60) uses LaTeX.
  - Fix by wrapping those expressions in `$…$` in the feedback sample at least. The tables are author-facing, but the feedback sample is meant as learner text.
- **The "completion" claims are ahead of the evidence.**
  - D6 PD5 is ticked "[x]" for a "complete exemplar".
  - It stays ticked only if the first two points above are fixed.

### F8. Answer-only credit is inconsistent across exemplars and unspecified in work orders — MANDATORY, Medium

- **Where:**
  - WT:110 awards 3/3 to a correct answer on its own, "no universal no-working penalty".
  - The speed illustration (D3:236) awards 2/3 to "only 8.3 m/s; 30 km/h, no method; method not demonstrated".
  - D3:39 and 66–68 say marks follow visible evidence.
  - The work-order Marking row (D3:596) does not require a recipe to declare an answer-only rule.
  - Both outcomes can be right for their recipes. The factorisation answer encodes both decisions. The speed answer does not.
- **Failure:** an author copies one pattern into a recipe where it is wrong. Authors will also mark answer-only responses inconsistently, because nothing says to declare the rule.
- **Minimal fix:**
  - Add to the Marking row: "State whether a correct final answer alone earns method marks, with the source evidence or the reason."
  - Add one clause to each exemplar saying which rule it uses and why.

### F9. The "supporting practice" and unobserved-candidate rules can be abused to inflate the catalogue — MANDATORY, Medium

- **Where:**
  - D3:44–48 allows short prerequisite drills if each is justified, with no evidence criterion.
  - D3:105–106 and 565 allow unobserved syllabus candidates, but nothing says whether they may be included, or what happens to the "authentic examination demand" row (D3:36) when no paper evidence exists.
  - D3:612–620 and D4 Q08 reject cosmetic variants but give no test for a separate recipe.
- **Failure:**
  - An author creates many "supporting" drills, each individually "justified".
  - An author includes an unobserved candidate and labels it "exam-style".
  - An author splits a recipe by claiming "different method".
- **Minimal fix:** three one-sentence rules.
  - Supporting recipes need cited evidence of a recurring prerequisite failure, such as an examiner-report statement or a mark-scheme dependency. They do not count toward coverage.
  - An included unobserved candidate must be labelled "syllabus-derived, not examination-evidenced". Its marking is wholly proposed, and it needs owner approval.
  - A separate-recipe claim must name the discriminating learner decision and give one response that earns different credit or feedback on the two recipes.
- **Verify:** each claim appears in the selection table as a required column or note.

### F10. Status documents conflict with each other — MANDATORY, Medium-Low

- D4:3–5 still says "proposed cross-subject contract". README:26–27 says D3/D4 are the "owner-accepted learning standard", and D4 itself records the accepted conditions (D4:34–36, 62–66, 86–92).
- Execution-status:44–46 ("checkpoints 2 and 3 not yet reviewed") and 60–62 ("response ... still pending") are superseded by lines 64–79. The supersession is stated, but a fresh agent reading top-down meets contradictory statements.
- **Minimal fix:**
  - Update the D4 header: the learning-related requirements are owner-accepted on 7 November, and the technical gates remain proposed.
  - Mark or collapse the stale paragraphs in execution-status.
  - Keep the D6 "[x]" lines, but add "(owner acceptance of the design, not subject-content approval)" at the point of the tick, not only in the footer paragraph at D6:24–28.

### F11. No lightweight path for a subject with few or no qualifying demands — MANDATORY (small), Medium

- **Where:**
  - D3:85–88 and 605–608 say zero recipes is valid.
  - Step B requires a stable ID for every assessable clause (D3:519–531), and Step C requires a disposition for every demand and pattern (D3:560–571).
  - No guidance says that exclusions may be grouped, or which later steps are skipped.
- **Failure:** for a recall-heavy subject such as History, an agent either spends a full corpus-mining effort to prove a negative, or skips analysis and asserts "no qualifying demands" with no record.
- **Minimal fix:**
  - Allow group-level exclusion rows that cite a range of demand IDs and one reason.
  - Define the zero-recipe record: the syllabus locators screened, a paper sample scanned for in-scope demands, the exclusion table and the owner's confirmation.
  - Say that subject rules, misconception registers and Steps D–I are skipped.
- **Verify:** the History and a no-papers case produce a short but auditable record.
- Whether the owner wants a sample paper scan is a small decision. I recommend it, but it is a wording choice, not a re-opened scope question.

### F12. "Educator" and "independent subject-content acceptance" are undefined — MANDATORY to clarify, see §4

- **Where:**
  - D3:269 and 420–421 require an "owner and educator" design review.
  - The role table (D3:305–311) has no educator or subject-content reviewer.
  - Independent reviewer means the other AI vendor (D3:316–318).
- Decision 13 distinguishes owner acceptance from independent subject-content acceptance. The documents never say who can give the latter.
- **Failure:** an AI cross-review, or the author's own owner tick, gets recorded as "independent subject-content acceptance".
- **Minimal fix:** state in the role table who may be the "educator" and what independent content acceptance requires. That depends on the owner answer in §4.

### Optional improvements

- **O1: Reuse or extend an existing recipe (WT:41–46).** State that an extension is a versioned change with re-review (D2:239–241, D4 Q14) and that existing assignments keep their old version. Otherwise "extend" can silently change live decks.
- **O2: Same-recipe repeats within one test.** Because solutions are revealed after each question, a second instance of a recipe in the same test follows feedback on the first. D3:156 and 301 cover this generally. One sentence tagging "later instance of a recipe after feedback" as after-feedback evidence would close it. This does not require any test-flow change.
- **O3: Shared LaTeX constant ambiguity.** `LATEX_FORMATTING_INSTRUCTION` says to use `\\` (double backslash). `latex-generation-and-rendering.md` §4 and §8.2 call that ambiguous and pending. D3 rule 7 (L394) and D4:63–66 handle it correctly for authored text (JSON library; decoded Markdown inspected). Add a link to those sections where D3:372–376 requires AI prompts to reuse the constant.
- **O4: Define "valid difficulty bounds"** (D3:37, WT:88–90) as the declared decisions plus a corpus-evidenced coefficient or size range.
- **O5: Commit and push.** TEAM-PLAYBOOK rule 9 says agents never commit or push. D3:323–324 and 784–785 defer to the "active user instruction". That is compatible but is a divergence the README should note, since the README says D3 is additive.
- **O6: D3 length and order.** About 300 lines of learning design precede Step A. A one-paragraph "if you only read one section" pointer to the Steps would help a fresh agent.

## 3. Exemplar assessment (walkthrough-factorisation.md)

**Source reads actually made (via Read's page support):**

- Syllabus (NIED 2018, 6131), PDF page 18.
- 2023 Paper 2 first revised proof, page 4.
- Examiners' report 2023, PDF pages 582–583 (printed 580–581).
- I did not read syllabus pp27–28.

**What I verified:**

- **Syllabus.** The page lists "use brackets and extract common factors" and "factorise … a²x² − b²y²". Both are consistent with WT §1. The page I saw reads "(b) Algebraic manipulation". I could not see the "Topic 6" number the walkthrough cites, so that number is unverified from this page.
- **Paper.** Q4(b) is "Factorise 50x² − 8y² completely", 3 marks. Q4(a) is a substitution and 4(c) is an algebraic fraction. The file is a revised proof, as disclosed. The "Q4(b) is self-contained" claim at WT:51–56 is supported.
- **Report.**
  - The commentary says many scored 1 mark for the HCF of 2 and then failed to factorise further.
  - It also says some "divided the expression by 2 throughout and did not recover the 2".
  - The embedded marking table for 4(b) reads: M1 for 2(25x² − 4y²), M2 for (5x − 2y)(5x + 2y), and an SC2 list of near-misses, including two same-sign or wrong-split forms.
  - These support the 1/3, 2/3 and 3/3 rows.
- **Limits in my reading.**
  - The first SC2 alternative is printed in a way that, at the resolution I could see, looks identical to the full-mark answer. It is probably a typographical slip in the report.
  - The walkthrough's "same-sign case" reading is supported by the second listed alternative. The walkthrough should say that its reading is an interpretation.
  - "SC2" is read as two marks in total. The walkthrough flags overlap risk (WT:113), which is correct.
  - The 2/3 for the missing outer 2 is an inference. The table shows M2 for the bracket pair but does not say it is awarded without M1. The walkthrough labels this "modelled on" and "proposal", which is honest. An independent reviewer must confirm it.
- **Algebra, recomputed by hand (not by tool):**
  - 18x² − 50y² = 2(9x² − 25y²) = 2(3x − 5y)(3x + 5y), and expanding returns the original.
  - 48x² − 75y² = 3(16x² − 25y²) = 3(4x − 5y)(4x + 5y).
  - 20x² − 45y² = 5(4x² − 9y²) = 5(2x − 3y)(2x + 3y).
  - (6x − 10y)(3x + 5y) expands to 18x² − 50y², so it is equivalent but incomplete.
  - The proposed domain k(a²x² − b²y²) with gcd(a, b) = 1 does give k as the highest common numerical factor.
  - The "SymPy confirmed" statement is an author claim I did not reproduce.
- **Speed illustration (D3:212–251), also by hand:**
  - 3000/360 = 25/3 = 8.3 m/s to 2 s.f., ×3.6 = 30 km/h.
  - The stage speeds are 5 and 15 m/s, whose simple mean is 10 m/s, giving 36 km/h.
  - The variant 4000/300 = 40/3 = 13 m/s to 2 s.f., giving 48 km/h.
  - The numbers and rows are correct.
  - It has the same gap as F7: no boundary case. It also has an unspecified case, converting a rounded 8.3 m/s (29.9 km/h) when part (b) says "using an unrounded intermediate".
- **Existing catalogue claim (WT:43–45).** `recipeCatalogue.json` has "Difference of squares", "Factorisation", "Factorising by grouping" and "Common factor then quadratic factors". I did not check whether any existing recipe already covers the two-stage pattern.

**Marking and feedback.** The marking table is plausible, source-anchored where it can be, and honestly labelled as a proposal. The feedback is specific, evidence-based, avoids inventing a misconception and gives a next action. The defects are those in F7 and F8. The walkthrough does not treat generated marking as board-approved, so no correction is needed on that point. The walkthrough is sufficient as a minimum generic exemplar of the standard once F7 and F8 are applied. Subject-specific detail is better handled as work-order requirements (F4, F8, F11), not more exemplars.

## 4. Remaining owner decisions

Only one is genuinely unresolved, and it is not a scope expansion.

1. **Who can give "independent subject-content acceptance"?** Today independent review is the other AI vendor (D3:316–318). TEAM-PLAYBOOK:246 says only to show the analysis to a subject teacher "if a teacher on the team knows the subject". Decision 13 says owner acceptance, independent acceptance, measured benefit and technical delivery are four different things. Please say whether cross-vendor AI review suffices, or whether a named subject teacher must also accept marking and feedback, at least for Accounting and the sciences. This answer drives the F12 wording and the "educator" role.

I am not re-asking any settled decision. F11's optional sample-paper scan for zero-recipe subjects is a wording choice inside decision 4. I flag it for visibility only.

## 5. What I read, and what remains unverified

**Read in full:**

- D3 `03-creation-playbook.md` (all 833 lines, including Steps A–I and the technical appendix).
- D4 `04-quality-and-review-contract.md`.
- D6 `06-acceptance-checklist.md`.
- `walkthrough-factorisation.md`.
- `README.md`.
- `execution-status.md`.
- D2 `02-subject-package-specification.md`.
- Resources `AGENTS.md` and `TEAM-PLAYBOOK.md`.
- App `docs/conventions/`: `ui-language.md`, `ai-generated-output-formatting.md`, `latex-generation-and-rendering.md`, `maths-workbench-question-acceptance.md`.
- `services/api/services/math_formatting_instructions.py`.

**Read in part:**

- `RUNTIME_STANDARD.md`: headings, and the sections on source adequacy, authoring and assessment alignment, learning items, and generalisation/assessment claims (RS-10–RS-38). I did not read its later sections.
- `docs/features/workout-bench.md`: grep only, for naming, five-box and unlock statements. I did not read the router handlers (`start`, `public_activity`, answer and advance), so the two-minute review and marking pause are taken from the playbook and the feature record's wording, not from the code.
- `recipeCatalogue.json`: title grep only.

**Not read:**

- D1 and D5.
- The prior review evidence directories under `evidence/`, including `claude-playbook-review-2026-11-07/`. I avoided them to keep this review independent.
- The `ADR-0086` and `docs/features/README.md` documents.
- Syllabus pp27–28.

**Source pages inspected:** syllabus p18; 2023 Paper 2 proof p4; examiners' report PDF pp582–583. The three source files were opened by exact path. No hashes were computed, so the SHA-256 values in the walkthrough are unverified.

**Unverified overall:**

- Any test, command or tool behaviour, including the `yyeni_workbench_tools` and `package.py verify` claims.
- The SymPy confirmation.
- Whether the existing Workbench UI supports any accounting-table or construction input (this bears on F2).
- The current deployed production behaviour.
- Whether the two existing catalogue recipes already cover the two-stage factorisation pattern.

## 6. Recommended next steps

1. Fix F1–F3, F6 and F10 first. They are small text changes that close ambiguities in the escalation, selection-audit and status chain.
2. Add the paths table and role mapping (F4) and the reuse limit (F5), so a fresh agent can resume from files alone.
3. Revise the walkthrough: add a boundary instance, an evidence-of-improvement sentence and LaTeX in the feedback sample, and state the answer-only rule (F7, F8). Then re-confirm D6 PD5.
4. Add the three one-sentence loophole rules (F9) and the zero-recipe path (F11).
5. Get your answer on the open decision in §4 and apply F12.
6. After those edits, ask for an independent subject-content review of the walkthrough marking adaptation, which is already flagged as pending. Operational validation of the appendix stays deferred, as planned.
