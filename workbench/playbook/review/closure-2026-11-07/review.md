# Closure review: Workbench playbook (Step 3)

I made no edits and ran no commands. I used only Read, Glob and Grep. I did not write the plan file that plan mode asks for, because you asked for the report as the final answer and no edits.

## A. Verdict

**Pedagogical playbook: minor nonblocking corrections.** All twelve first-review findings (F1–F12) are closed against the actual rules, not just the response ledger. I found no blocker. Of the five new findings below, only the status-line update (N1) must be done at finalisation. N2 is a small clarification worth making then too. N3–N5 are optional.

**Technical appendix:** I reviewed it only as honest labelling, and it is honest. It states it is unvalidated, shows commands as argument shapes only, and says no engineering resumes (`technical-appendix.md:3-8, 43-59`). It is not part of the pedagogical verdict, and I did not inspect any tool code.

## B. F1–F12 closure table

| # | Status | Current locators | Substantiation |
|---|---|---|---|
| F1 Hold meanings | **Closed** | `README.md:118-132`; `templates.md:98-119` | A three-row table (capability, source, scope) gives trigger, durable record, recipient and exit condition. A defective authored version is renamed "held (withdrawn pending repair)" and linked, not conflated (`README.md:129-132`). The cashbook, graph and repair cases in `validation.md:33-70` each resolve to one reason code and one file. |
| F2 Capability baseline and durable flag | **Closed** | `README.md:134-151, 214-215, 253-254`; `templates.md:49-51, 63-68, 105-108` | "Capability evidence checked" is a dated field in both the record and STATUS. STATUS has a "flagged to Jeremy/Vitalis" line with the actual recipient. A blank flag line blocks both "analysis read" and "plan approved". A handoff via Jeremy is not recorded as delivery to Vitalis. `preservation.md:28-36` keeps unclear support unverified, which matches your decision. |
| F3 Selection audit and zero outcome | **Closed** (see N3) | `README.md:292-300, 217-235`; `templates.md:199-220`; `quality.md:18, 29, 33-42` | The review prompt reads every disposition, grouped exclusion, observed-versus-syllabus label and capability record. It also checks that no demand disappears and that no held capability is disguised as an exclusion. An owner tick explicitly does not replace review (`quality.md:41`). A seeded false "observed" row would be caught by following only the template. A false zero is caught only if the reviewer happens to rescan the corpus, which the prompt does not require (N3). |
| F4 Paths and role mapping | **Closed** (residual N2) | `README.md:54-62`; `templates.md:8-38`; `AGENTS.md:6-9`; `TEAM-PLAYBOOK.md:3-6` | There is a full WB-relative path table, including `capability-gaps.md`, `zero-recipe-record.md` and `review/<round>/`. Roles map to one brief each. Both entry documents now point to the Workbench playbook. The record paths and role mapping are executable. The remaining gap is that `REVIEWER.md` still carries notes-pipeline instructions (N2). |
| F5 Reuse limits | **Closed** | `README.md:71-75, 186-187`; `templates.md:84-88` | Reuse is limited to facts the existing analysis actually records. Each pattern needs a paper locator and a marking locator, or "none available" with its impact. |
| F6 Copied-wording gate | **Closed** | `quality.md:31, 102-118`; `templates.md:178, 212` | Q15 exists. It applies the 12-word rule and the 8–11-word manual review. It bans "examiners reward" and unsupported exam-content claims. It says the old checker is not validated for runtime feedback, and requires the gate in the F-stage author report. The "Q01–Q15" list matches the gates actually defined. |
| F7 Exemplar completeness | **Closed** | `exemplars/factorisation.md:52-61, 66-96, 106-125, 134-150` | There is a normal case, two variants, and small and upper boundaries (8x²−18y² and 125x²−80y²). Rejected cases carry reasons (`:87-92`). "One independent observation, not mastery" is defined (`:146-150`). The task, variation, response and repair tables all use LaTeX. The feedback sample (`:134-138`) has only plain numerals, which `latex-generation-and-rendering.md:27` allows. |
| F8 Answer-only credit | **Closed** | `templates.md:152-155, 166-168`; `exemplars/factorisation.md:106-110`; `quality.md:22, 62-64` | A work-order field requires an answer-only rule with a source or rationale. The exemplar states its own rule and warns against copying it. The inconsistent speed example is removed, and `review-response.md:46-50` says so. |
| F9 Catalogue inflation | **Closed** | `README.md:192-207`; `templates.md:89-96`; `quality.md:24, 44-47` | A separate recipe needs a discriminating learner decision plus a concrete response that earns different credit or feedback. A supporting drill needs a cited dependency or difficulty, a reason existing recipes are insufficient, and owner acceptance. It earns no direct coverage. An unobserved candidate carries the label "syllabus-derived, not examination-evidenced", proposed marking, owner acceptance and independent review. |
| F10 Status conflicts | **Closed** | `README.md:3-7, 349-353`; `quality.md:3-6, 138-142`; app drafts | The five states are separated: owner design, author checks, independent acceptance, published release, activation. I confirmed "Superseded review draft" banners at line 1 of the app's `02`, `03`, `04`, `06` and `walkthrough-factorisation.md`. The app's `execution-status.md:16-18` marks its history as superseded, and the app's `README.md:12-15` points to the current standard. |
| F11 Zero and no-papers route | **Closed** | `README.md:175-177, 217-235`; `templates.md:78-82, 121-137` | Grouped exclusions are allowed, with ranges so no clause is lost. The zero record is defined. The scan must declare unscanned space and cannot justify an unqualified zero. Steps D–F and H–I are skipped. A no-papers subject is labelled syllabus-only and never given invented papers. A capability-blocked demand is explicitly not a zero. |
| F12 Acceptance roles | **Closed** | `README.md:64-69, 305-306`; `quality.md:122-126`; `templates.md:218-219` | Cross-vendor AI review suffices for independent content acceptance. Mixed authorship is recorded, an author cannot accept their own work, and teacher advice is optional. A grep for "educator" finds no required signature left. |

**Optional items (O1–O6):** all dispositions are proportionate and I accept them.
- **O1:** `README.md:76-78`, `preservation.md:41-45`. It honestly does not claim deck version-pinning exists.
- **O2:** `README.md:336-337`, `quality.md:98-99`, `exemplars/factorisation.md:152-155`.
- **O3:** `guidelines/README.md:24-29`. The §4 and §8.2 references exist at `latex-generation-and-rendering.md:86-99, 141-142`.
- **O4:** `quality.md:67-69`, `exemplars/factorisation.md:78-85`.
- **O5:** `README.md:80-84`. It is a documented divergence from `TEAM-PLAYBOOK.md` rule 9, and no commit is authorised here.
- **O6:** `README.md:9-11`.

## C. New findings

None of these is a true blocker.

- **N1. Status lines predate this closure. Low, housekeeping, do at finalisation.**
  - **Where:** `review-response.md:5-9`, `validation.md:131-138`, `technical-appendix.md:6-8`, `README.md:3-7`, `quality.md:3-6`, `exemplars/factorisation.md:3-5, 157-164`, and the `candidate-inputs.json` status.
  - **Problem:** they say "awaits independent closure" and "no Claude follow-up launched".
  - **Fix:** add one dated line recording this closure (reviewer, frozen digest, scope, verdict). Keep every "does not approve" limit. Re-freeze the `candidate-inputs.json` hashes after the edit, since any edit invalidates them.
  - **Verify:** a grep for "pending" and "No Claude follow-up" is consistent.

- **N2. `REVIEWER.md` conflicts with the Workbench reviewer role. Low–Medium, nonblocking.**
  - **Where:** `README.md:61` against `REVIEWER.md:3` ("already published"), `:12-14, 26` (a fixed six-question set, "do not hunt beyond"), `:16-24` (run `run_checks.py` first) and `:62-68` (write YAML to `operations/review/` and ingest it).
  - **Failure:** a fresh reviewer reading exactly one brief could limit itself to six notes-card questions, run a check that does not apply, and file the report in the wrong place. `README.md:50-52` overrides only quotas and verdicts.
  - **Fix:** add one sentence to `README.md:61`: "REVIEWER.md's published-notes questions, run_checks, operations/review YAML and ingest do not apply. Use the review-request template and write to WB/review/<round>/."
  - **Related fix (templates.md:10-17, nonblocking):** also say that WB `STATUS.md` is separate from `work/<workspace>/STATUS.md` in `TEAM-PLAYBOOK.md:117-139`. Also say that if no workspace exists, one is created after the tracker claim, using `TEAM-PLAYBOOK.md` §6 naming.
  - **Verify:** a fresh reviewer given `README.md` and `REVIEWER.md` can state which parts of the brief it ignores.

- **N3. A reviewer is not told to rescan the corpus independently. Low, optional but recommended.**
  - **Where:** `templates.md:199-220`; `README.md:229-231`.
  - **Failure:** a false zero or heavy exclusion is caught only if the author's cited locators happen to reveal it. Reading the author's locators confirms what the author cited, not what the author missed.
  - **Fix:** add one clause: "for zero or heavily excluded outcomes, independently sample question structures across the inventoried corpus, not only cited locators, and report what you sampled."
  - **Verify:** a seeded missed calculation question in an uncited paper is found.

- **N4. The marking ambiguity could be pinpointed. Low, optional.**
  - **Where:** `exemplars/factorisation.md:101-105, 117`.
  - **What I saw:** at the resolution I read, the first SC2 form on PDF p583 looks identical to the full-mark answer. The explicit same-sign form listed is the plus-plus one, and the exemplar's both-minus row is an extension of it.
  - **Why it is already adequate:** `:101-105` and `:116-118` mark these as proposed or "confirm interpretation", and `:122-125` declares precedence. Stating it specifically would make the later source review faster.

- **N5. Selection-only review comes late for nonzero subjects. Optional.**
  - **Where:** `README.md:214-215`.
  - **Problem:** the independent selection review happens at G, after authoring, so a wrong exclusion forces a reopen of C after E/F effort.
  - **Fix:** the playbook could allow an earlier selection-only review before plan approval when a selection is large or contested. This is not required, and it is a wording choice inside your existing decisions.

## D. Exemplars and workflow exercise

**Sources I actually read, as page images; I did no text extraction:**
- **Syllabus PDF, pages 17–18.**
  - Page 17 has the "TOPIC 6: ALGEBRA" heading. This closes the first review's unverified "Topic 6" point.
  - Page 18, section (b) "Algebraic manipulation", lists "use brackets and extract common factors" and "a²x² − b²y²".
- **2023 Paper 2 first revised proof, page 4.**
  - Q4(b) is "Factorise 50x² − 8y² completely" for 3 marks.
  - Q4(a) is a substitution and Q4(c) is an algebraic fraction, so (b) is self-contained.
- **Examiners' report, PDF pages 582–583 (printed 580–581).**
  - The commentary says many scored 1 mark for the HCF of 2 and then failed to factorise further. It also says some "divided the expression by 2 throughout and did not recover the 2".
  - The table gives M1 for 2(25x²−4y²), M2 for (5x−2y)(5x+2y), and an SC2 list including the redistributed forms (10x−4y)(5x+2y) and (10x+4y)(5x−2y).
  - These support the 1/3 row, the redistributed-factor row and the 3/3 row. The lost-outer-factor 2/3 row and the same-sign row are inferences, labelled as proposals.
- **Mark scheme:** a Glob of the 2023 Mathematics folder found only the two papers, so the "no standalone mark scheme" claim at `exemplars/factorisation.md:26` holds.

**My own computations, by hand, not by tool:**
- **Domain size:** 4 values of k times 10 coprime ordered (a,b) pairs from {2,3,4,5} gives 40.
- **Unique pairs:** the pair (ka², kb²) determines k, because k = gcd(ka², kb²), so the 40 expressions are distinct.
- **Complete factorisation:** k(a²x²−b²y²) = k(ax−by)(ax+by) is an identity, so every instance is correct. gcd(a,b)=1 makes k the highest common numerical factor, and the linear factors are irreducible over the integers.
- **Maximum coefficient:** 5·5² = 125.
- **Named examples:** all five are in the domain: (k,a,b) = (2,3,5), (3,4,5), (5,2,3), (2,2,3), (5,5,4).
- **Marking rows:**
  - 2(3x−5y)(3x−5y) expands to 18x²−60xy+50y², so it is wrong.
  - (6x−10y)(3x+5y) equals 18x²−50y², so it is equivalent but incomplete.
  - (3x−5y)(3x+5y) equals 9x²−25y², which is half the original, so losing the 2 changes the value.

**Credit and feedback promoted as release-approved:** none. Every adapted award is labelled proposed (`exemplars/factorisation.md:112, 116-118`). The sample feedback is brief, recognises real progress, names no guessed misconception, and matches the contract's summary-plus-`repair_steps` split. The finite bounds are explicitly not corpus-calibrated (`:83-85`).

**Marking caveats:** adequately disclosed for a generic design exemplar. They appear at `:26-32, 101-105, 116-118, 122-125, 157-164` and `review-response.md:56-58`. Actual subject release approval is not required to accept the playbook.

**Workflow exercise:** I walked the normal, capability-hold, graph, zero and no-papers routes through the files, and a fresh agent can execute them.
- **Paths, roles, records and escalation checkpoints:** executable, with the N2 residual for reviewers.
- **Selection-only review:** it catches a false "observed" label from the template alone. It catches a false zero only partly (N3).
- **Hypothetical exercises:** the exercises in `validation.md` are the author's own instruction-level walkthroughs, not seeded tests.

**Author evidence, not independent:** the digests in `guidelines/provenance.json` and `candidate-inputs.json` match for all five snapshots by textual comparison only. I did not recompute any hash. The 40-instance script is not in the bundle, and `author-validation.json` records counts only, with no mention of SymPy. I could not rerun the author's check, so I replaced it with the hand computation above.

## E. Remaining owner decisions

None are genuinely unresolved. Cross-vendor sufficiency and test feedback timing are settled. Adopting N3 and N5 is a wording preference only. The two marking interpretations must be resolved before any real recipe release, not before the playbook is accepted.

## F. Next steps and limits

**Next steps**
1. Make the N1 status updates and the N2 clarification. N3–N5 are optional.
2. Re-freeze hashes after the edits. Because those edits are status and clarification only, a diff glance is enough, not a full re-review.
3. Run the first real subject pilot to test the route end to end.

**This verdict does NOT approve**
- any subject's content, marking or exclusions;
- the two marking adaptations;
- the technical appendix, tooling or operational readiness;
- publication, deployment or learner assignment;
- any commit or push;
- any claim of learning benefit.

**Not read**
- the `PLANNER`, `MINER` and `AUTHOR` briefs;
- `ai-generated-output-formatting.md`, which I did not open, and `ui-language.md`, which I only grepped;
- the app feature record, router or timing code, so test and unlock behaviour is taken from `preservation.md` and your decisions;
- syllabus pp27–28 and the rest of the three source PDFs;
- the app's `01` and `05` documents and the old review evidence;
- `review/closure-2026-11-07/*`, which I saw listed and deliberately did not open, to stay independent;
- unrelated subject workspaces.

**Not run:** no commands, tests, hashes, copied-wording checks or tool executions, and no verification of the three source-PDF SHA-256 values or the frozen-bundle hashes against current bytes.
