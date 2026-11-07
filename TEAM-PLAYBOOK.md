# YYeni team playbook: from syllabus to published notes and flashcards

For Workbench calculation/procedural recipes, follow the companion
[Workbench playbook](workbench/playbook/README.md). This document continues to
govern the notes/flashcard pipeline; its item quotas/check verdicts are not a
Workbench content-acceptance process.

**Who this is for.** Every YYeni team member (Vitalis, Jeremy, Justus, Lotto) and the AI agent they work with: Claude Code or Codex. Read it once yourself. Your agent reads it every time.

**What it produces.** For one syllabus, a published set of learner notes and flashcards. Every flashcard carries its assessment objective, command word, mark tariff and Bloom level. Every topic passes the automatic checks, and an agent from the other vendor has reviewed the subject.

**How to start.** After `git pull`, open Claude Code or Codex in the repository folder and paste the start prompt in section 2 with the subjects you want. The agent works one subject per session. It stops only at the checkpoints marked **YOU**, and it records each of your answers in the subject's `STATUS.md`, so any session can pick up where another left off.

**Which document wins.**

- This playbook decides the **order of work** and the **checkpoints**.
- The role briefs in `standard/v0.2.0-draft/roles/` decide **how** each step is done.
- A subject's `HANDOVER-*.md` wins over `AUTHOR.md` for that subject.
- If `AGENTS.md` and this playbook disagree on process, follow the playbook and tell Vitalis about the conflict.

---

## 1. One-time setup (30 minutes)

Do this once per computer.

1. **Install git, Python 3 and Git LFS.**
   - On a Mac: `brew install git git-lfs python poppler`. Poppler gives `pdftotext`, which reads exam PDFs.
   - On Windows: install Git for Windows (it includes LFS), Python 3 from python.org, and poppler.
2. **Get access and clone the repository.**
   - Ask Vitalis to give your GitHub account access to the repository.
   - Clone it into `Documents/YYeni Study Resources`:
     ```bash
     cd ~/Documents
     git clone https://github.com/uamafias/yyeni-study-resources.git "YYeni Study Resources"
     cd "YYeni Study Resources"
     ```
   - Then:
     ```bash
     git config --global user.name  "Your Name"
     git config --global user.email "you@yyeni.com"
     git lfs install
     git lfs pull
     ```
   - The PDFs are stored with Git LFS. Without it, every PDF looks modified and new PDFs will not upload properly.
3. **Install the Python tools** in a virtual environment inside the repository folder:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   pip install -r standard/v0.2.0-draft/tests/requirements.txt pypdf
   python -c "import jsonschema, yaml; print('tools ok')"
   ```
   - On Windows, type `py` where this playbook says `python3`.
   - Activate the environment (`source .venv/bin/activate`) in every new terminal, and tell your agent to do the same before it runs a tool.
4. **Set the agent up.**
   - **Claude Code:** open it in the repository folder. Choose **Opus 5.5** at **medium** effort; use **high** for steps 2 to 4 on a complicated syllabus. Do not use the most expensive tier: it costs several times more for little gain on this work.
   - **Codex:** open the repository folder in **Local** mode, **never Worktree**. Use the default Codex model at medium reasoning (high for steps 2 to 4).
     - A worktree is a copy made from the last commit, so it cannot see anything not yet committed. That cost us half a day on 0455 Economics.
   - **Both:** allow file edits and shell commands for this folder, or the agent stops to ask permission at every file.
5. **Get the harvester.** The YYeni Web Harvester is a separate toolkit that sits beside the repository, at `Documents/YYeni Web Harvester`. Ask Vitalis for a copy. Use it to download missing past papers (step 1). Never write new scraping scripts in the repository.

---

## 2. The start prompt

Paste this at the start of every session.

```
Read TEAM-PLAYBOOK.md at the repository root and follow it exactly.

My name is <your name>. My subjects for today are listed below. First, for every subject, check operations/SUBJECT-TRACKER.md (is it claimed by me? is its kind piloted?) and find its source documents, then give me one table: owner, pilot status, what exists, what is missing. Do not create any workspace yet. Then work on the FIRST subject only, from whatever step its STATUS.md says comes next, and tell me the exact prompt to paste into a new session for each of the others.

Subjects:
- <board> <level> <subject name> <code if known>
- ...
```

For example:

```
Subjects:
- Namibia NSSCO Business Studies 6144
- Namibia NSSCAS Business Studies 8245
- Cambridge IGCSE Chemistry 0620
```

If you do not know a code, give the subject name and level; the agent reads the code off the syllabus cover.

The prompt for each further session names one subject:

```
Read TEAM-PLAYBOOK.md at the repository root and follow it exactly. Work on this one subject, from whatever step its STATUS.md says comes next:
- <board> <level> <subject name> <code>
```

**If a session stops part-way** (credits ran out, laptop closed, connection dropped), open a new session in the **same tool** and paste the one-subject prompt. `STATUS.md` and the files on disk tell the agent where it stopped.

---

## 3. The pipeline at a glance

| Step | What happens | Who | Recorded in `STATUS.md` |
|---|---|---|---|
| 0 | Claim the subject | YOU | — (tracker row) |
| 1 | Gather the source documents | YOU, agent checks | sources found; **YOU: sources complete** |
| 2 | Read the syllabus: AOs, papers, command words | agent | **YOU: AO table checked against the PDF** |
| 3 | Analyse past papers, mark schemes and examiner reports | agent | **YOU: analysis read** |
| 4 | Plan the subject | agent | **YOU: plan approved** |
| 5 | Author every topic (parallel sub-agents) | agent | topics done; published |
| 6 | Cross-review with the other vendor | YOU start it; the other agent reviews and fixes | **YOU: verdict read** |
| 7 | Commit and push; update the tracker | YOU | published |

**The order is fixed.** No plan without the syllabus read first and the corpus analysed. No notes or flashcards without a plan. The build tools enforce part of this: contracts and work orders refuse to build until the syllabus facts and the corpus analysis exist.

### STATUS.md: how sessions remember

Every subject has `work/<workspace>/STATUS.md`. The agent creates it at step 1 and updates it at the end of every step.

```markdown
# STATUS — <code> <subject name> (<board> <level>)
Workspace: work/<workspace>/   Owner: <name>   Authoring tool: <Claude or Codex>

- [x] 1 Sources found — 2026-10-12 (syllabus 2026-2028; 18 papers, 18 mark schemes, 6 reports)
- [x] 1 YOU: sources complete — Jeremy, 2026-10-12
- [x] 2 Syllabus facts written
- [x] 2 YOU: AO table checked against PDF pages 12-13 — Jeremy, 2026-10-12
- [ ] 3 Corpus analysis written
- [ ] 3 YOU: analysis read
- [ ] 4 Plan built (AO gap: _ points)
- [ ] 4 YOU: plan approved
- [ ] 4 YOU: plan committed
- [ ] 5 Topics authored: 0 / N   (blocked: none)
- [ ] 5 Published
- [ ] 6 Reviewed by <the other tool>: verdict _
- [ ] 6 YOU: verdict read
- [ ] 7 YOU: committed and pushed
```

**At a YOU checkpoint, the agent stops and asks.** It ticks the box only after you answer, writing your name and the date. On resuming, it starts at the first unticked box.

**A workspace that exists but has no `STATUS.md`** was started before this playbook (for example 0500 First Language English).

- The agent does not start again at step 1, and never rebuilds or overwrites its `curriculum/`, contracts or work orders.
- Instead, it reads what exists (syllabus facts, analysis, work orders, items, published output, `operations/LAUNCH-PROMPTS.md`) and writes a `STATUS.md` that ticks only what the files prove.
- It then asks you to confirm that status before doing anything else.

---

## 4. The steps in detail

Each step says what **you** do and what the **agent** does. Agent instructions are written to the agent.

### Step 0: Claim the subject (YOU)

1. Open `operations/SUBJECT-TRACKER.md`.
2. Add or edit the subject's row: your name, status `in progress`.
3. Commit and push that one file straight away:
   ```bash
   git pull
   git commit -m "Claim <code> <subject>" -- operations/SUBJECT-TRACKER.md
   git push
   ```
   Two people must never work on the same subject.

**Agent:** before any other step on a subject, check the tracker. If the subject is claimed by someone else, or its kind is not yet piloted and you are not working with Vitalis, stop and say so.

**Pilot rule.** The first Namibian NSSCO subject, the first NSSCAS subject, the first grades 8 to 9 subject and the first upper primary subject are **pilots** (section 6). Until the tracker marks a kind of subject as piloted, only Vitalis claims it.

### Step 1: Gather the source documents (YOU, agent checks)

**Agent:**

1. Work out the workspace name (section 6).
2. Create `work/<workspace>/` and its `STATUS.md`.
3. Look for the subject's documents, in this order:
   - `sources/` (for example `sources/cambridge/igcse/<code>-<subject>/`; Namibia has only JSC material here so far);
   - `Syllabi/` (Namibian syllabuses: `Syllabi/Namibian Curricula/NSSCO (New)/`, `NSSCAS/`, `JSC (New)/`, `SP Grade 4-7 Namibia/`);
   - `Question Banks/` (Namibian papers: `Question Banks/Namibian Curricula/NSSCO (New)/<Subject> (<code>)/<year>/`, with examiners' reports beside them and in `Question Banks/Namibian Examiner Reports/`);
   - `_harvest/`.
4. Report one table: the syllabus (edition and exam years), and the question papers, mark schemes and examiner reports by year and series. List what is missing.
5. Tick "Sources found" in `STATUS.md`. **Stop.**

**YOU:**

1. Supply anything missing, with the harvester or by hand.
   - Never bypass a paywall. Log a file behind one as unavailable and carry on without it.
2. Put new files under `sources/<board>/<level>/<code>-<subject>/syllabus/` or `.../assessment/<year>/`. Keep the official filenames.
3. Commit them now, so the rest of the team has them:
   ```bash
   git pull
   git add sources/<board>/<level>/<code>-<subject>
   git commit -m "Sources for <code> <subject>" -- sources/<board>/<level>/<code>-<subject>
   git push
   ```
4. Tell the agent the sources are complete.

**What is required:**

| Document | Required? |
|---|---|
| The current syllabus, for the exam years we serve | **Yes. Nothing starts without it** |
| Past question papers: the last 3 to 6 years on the current syllabus | Yes, where they exist |
| Mark schemes for those papers | Yes, where they exist |
| Examiner or moderator reports | Strongly wanted: they show where learners lose marks |
| Specimen papers | Use them when there are no past papers yet |

Agents never write to `sources/`. Only people add source documents.

### Step 2: Read the syllabus first (agent; YOU check)

**Agent:**

1. Read the syllabus PDF itself, before any past paper.
2. Transcribe into `work/<workspace>/curriculum/syllabus-facts.json`, each value with its page number and the verbatim line:
   - the assessment objectives, with names and weights;
   - each paper or component: marks, duration, weighting, and the AO split per paper;
   - the command-word table;
   - every limit the syllabus states ("will not be assessed", "not required", "knowledge of ... is not expected");
   - the content outline, topic by topic.
3. Never write an AO weight, a per-paper split or a command word from memory. If the syllabus does not state something, write that it does not.
4. Write a one-page syllabus brief at `operations/analysis/<stem>-syllabus-brief.md`. The `<stem>` names the subject uniquely; section 6 gives the pattern, for example `6144-nssco-business-studies` or `mathematics_jss-gr8-9`. Every analysis file for this subject starts with it.
5. Show me the AO table and the paper table, with page numbers. **Stop.**

**YOU:** open the syllabus PDF at the pages cited and check both tables match. This takes two minutes, and it is the most valuable two minutes in the pipeline: every later step inherits a wrong weight.

### Step 3: Analyse past papers, mark schemes and examiner reports (agent; YOU read)

**Agent:**

1. Read `standard/v0.2.0-draft/roles/MINER.md`.
2. Use these analyses as models of shape:
   - `operations/analysis/9702-as-physics-corpus-analysis.md` (a science);
   - `operations/analysis/0455-igcse-economics-corpus-analysis.md` (a social science);
   - `operations/analysis/0500-igcse-first-language-english-corpus-analysis.md` (a language).
3. Extract text with `pdftotext -layout` and `pdftotext -raw`. Two-column papers read differently in each, so use both.
4. Write `operations/analysis/<stem>-corpus-analysis.md` with these sections:
   1. **The corpus:** what was used, which years, and what was set aside (for example, papers from an older syllabus).
   2. **What each paper looks like:** question types, mark tariffs, and which command words carry the marks.
   3. **Command words actually used:** count, modal tariff and tariffs seen; also the words listed but never used. This becomes the rule for which words may open a flashcard.
   4. **What a creditable answer looks like:** from the mark schemes' structure. One point per mark? Development needed? Steps in calculations? Context required?
   5. **Where the marks fall:** the share of marks per topic, and the outcomes examined in most years. This calibrates emphasis. It never removes coverage.
   6. **How candidates lose marks:** the recurring failures from examiner reports, each with what the resource will do about it.
   7. **Misconceptions:** confusions the reports evidence, restated in our words, each with a test that tells the two ideas apart.
      - Write them to `curriculum/misconceptions.json`.
      - Curate them: drop duplicates, fragments and answering habits. The 0450 Business Studies register had 72 raw entries, of which only 29 were real confusions.
   8. **Scope:** each limit from step 2 becomes a pattern in `curriculum/scope-scan.json`, with examples it must catch and in-scope text it must leave alone.
   9. **What this means for the plan.**
5. Also write `curriculum/exam-exposure.json` and `curriculum/answer-shapes.json`.
6. Show me sections 2, 3 and 6 as a short summary. **Stop.**

**YOU:** read the summary. Does it sound like the exam your learners sit? If a teacher on the team knows the subject, show it to them.

**The rule that never bends: mine, do not reproduce.** Past papers, mark schemes and examiner reports are evidence of structure, frequency, tariffs and failures. Their wording never reaches a learner.

- **12 or more identical words** copied from them into learner-facing text is a defect.
- **8 to 11 words** is reviewed by eye. It is allowed only where it is standard terminology, a standard definition or a formula.

### Step 4: Plan the subject (agent; YOU approve)

**Agent:**

1. Read `standard/v0.2.0-draft/roles/PLANNER.md`.
2. Pick the finished workspace most like this subject, as your model of shape:

   | Subject type | Model workspace |
   |---|---|
   | Science or mathematics | `work/cie-9702-as-2025-2027/` (9702 AS Physics) |
   | Business or social science | `work/cie-0455-igcse-2026/` (0455 IGCSE Economics) or `work/cie-0450-igcse-2026/` (0450 IGCSE Business Studies) |
   | Computing | `work/cie-9618-as-2026/` (9618 AS Computer Science) |
   | Geography | `work/cie-0460-igcse-2025-2026/` (0460 IGCSE Geography) |
   | English or another language | `work/cie-9093-as-2024-2026/` (9093 AS English Language) |

   Copy the shape, never the content. Never edit another subject's workspace.

   **Your own scripts.** You will write small scripts to read the syllabus, mine the papers and build the curriculum files.
   - Put them in `work/<workspace>/planning/`.
   - The scripts in `standard/v0.2.0-draft/mine/` (for example `mine_syllabus.py`, `exposure.py`, `mine_ms.py`, `mine_er.py`, `scope_scan.py`, `verify.py`) are worked examples. They are wired to particular subjects and to the original planner's machine. Read them for the method; do not run or edit them.
3. In `work/<workspace>/`, write:
   - `qualification-profile.yaml`: board, level, route, exam window, papers.
   - `curriculum/objective_registry.json`: every syllabus outcome as an objective, with its `depth_tier` and `objective_type`. A list in the syllabus ("sole trader, partnership, ...") becomes a container plus one objective per member.
   - `curriculum/assessment-framework.json`: AO weights in marks, the paper structure, and command words with their tariffs.
   - `curriculum/glossary.json`: each recurring term's settled meaning.
   - `subject-profile.yaml`:
     - `answer_structures`: the parts each card type's marking guidance must name;
     - conditioned mechanisms: claims true only under a condition, which must carry it;
     - `variant_register`;
     - prohibited patterns;
     - the depiction rule;
     - and, where needed, `slot_plan`: performance tasks with their AO split, AOs by objective type, top-up order, per-paper targets, misconception slots. 0455 Economics and 9702 Physics show every key.
4. Build the plan with the tools, never by hand. Run each with `--help` first if unsure of its arguments. The contract and work-order tools refuse to run until `curriculum/syllabus-facts.json` and `operations/analysis/<code>-*-corpus-analysis.md` both exist. Here `<code>` is the second part of the workspace name (section 6).
   ```bash
   python3 standard/v0.2.0-draft/build/conform_registry.py work/<workspace>
   python3 standard/v0.2.0-draft/build/make_contract.py    work/<workspace>
   python3 standard/v0.2.0-draft/build/make_work_order.py  work/<workspace> --all
   ```
5. Check the result:
   - `curriculum/ao_coverage.md` reads **largest gap 5 points or fewer**. If not, adjust `slot_plan` and rebuild. Never pad the bank to chase an AO.
   - Every contract carries every scope limit (`excluded_constructs`).
   - Every slot's command word is one the papers use, at a tariff the papers set.
6. Build a small structural exemplar under `work/<workspace>/exemplar/`: one or two thin topic slices that pass every check. Authors copy its shape.
7. Write `work/<workspace>/PLAN-<stem>.md` and `HANDOVER-<stem>.md`, following `PLAN-9702-as-physics.md` and `HANDOVER-9702-as-physics.md` section for section.
8. Show me the topic table (topics, objectives, items, notes words) and the AO balance table. **Stop.**

**YOU:**

1. Check the topic list matches the syllabus and the totals look sensible. A typical subject has 10 to 40 topics and 400 to 900 items.
2. Approve, or say what to change.
3. Once approved, commit the plan, so the authoring can be reviewed or reverted:
   ```bash
   git add work/<workspace> operations/analysis/<stem>-*
   git commit -m "<code> <subject>: plan" -- work/<workspace> operations/analysis/<stem>-*
   git push
   ```

### Step 5: Author every topic, in parallel (agent and sub-agents)

**Agent (lead):**

1. Read `standard/v0.2.0-draft/roles/AUTHOR.md` and the subject's HANDOVER. Where they disagree, the HANDOVER wins.
2. Split the topics:
   - **Claude Code:** spawn one sub-agent per topic, up to 5 at a time.
   - **Codex:** author the topics one after another in this session.
3. Give every sub-agent this brief, filled in:
   ```
   You are the AUTHOR for topic <T> of <code> <subject>, workspace work/<workspace>/.
   Read AGENTS.md, standard/v0.2.0-draft/roles/AUTHOR.md, work/<workspace>/HANDOVER-<...>.md (it wins over AUTHOR.md), and the exemplar in work/<workspace>/exemplar/.
   Write ONLY inside work/<workspace>/topics/<T>/. Do not commit or push.
   Produce claims/canonical_claim_ledger.json, content-units/*.json and learning-items/topic_<T>_items.json: one item per work-order slot, with the slot's id, subtype or item_type, assessment_objectives, blooms_level, command_word and mark_tariff.
   Never copy wording from any exam paper, mark scheme or examiner report. Every scenario and answer is your own.
   Then run render_notes.py, run_checks.py and what_to_fix.py for your topic and fix what what_to_fix.py names, until it reports nothing to fix.
   If the same check still fails after 3 attempts, stop and report the check, its output and what you tried. Do not work around it.
   Record any deviation from the work order in topics/<T>/authoring_notes.json as {from, to, why}.
   Report: items written, the final check line, deviations.
   ```
   The commands, for reference:
   ```bash
   python3 standard/v0.2.0-draft/build/render_notes.py work/<workspace> <T>
   python3 standard/v0.2.0-draft/checks/run_checks.py   work/<workspace> <T>
   python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/<workspace> <T>
   ```
4. As each sub-agent finishes, re-run `run_checks.py` on its topic yourself; do not trust its report alone. Update `STATUS.md` (topics done: n / N).
5. If a topic is stuck on the same check after 3 attempts: write `blocked: <topic>, <check>, <one line why>` in `STATUS.md`, carry on with the other topics, and tell me at the end. A stuck check usually means the plan is wrong, not the author.
6. When every topic reads PUBLISH:
   ```bash
   python3 standard/v0.2.0-draft/build/publish_subject.py work/<workspace>
   ```
7. Report to me in under 250 words:
   - topics done and any blocked;
   - totals: claims, content units, items, notes words;
   - the final check line per topic;
   - every deviation from the plan, and anything in the plan that turned out wrong.

No YOU checkpoint here. Leave it running and check in when it reports.

### Step 6: Cross-review with the other vendor (YOU start it)

**Authored with Claude? Review with Codex. Authored with Codex? Review with Claude.** A second model catches what the first is blind to. If authoring switched tools part-way, `STATUS.md` says which tool wrote which topics; the reviewer is the tool that wrote fewer of them.

**YOU:**

1. Commit the authored work first:
   ```bash
   git add work/<workspace> publish/<workspace>
   git commit -m "<code> <subject>: authored" -- work/<workspace> publish/<workspace>
   ```
2. Open the other tool in the repository folder (Codex in Local mode) and paste:
   ```
   Read TEAM-PLAYBOOK.md, section 4, step 6. You are the REVIEWER for <code> <subject>, workspace work/<workspace>/. It was authored by <Claude or Codex>. Do the review exactly as step 6 says, fix what it allows you to fix, update STATUS.md, and give me the review report.
   ```

**Agent (reviewer):** read `standard/v0.2.0-draft/roles/REVIEWER.md`, then:

1. **Checks.** Re-run `run_checks.py` on every topic. All must read PUBLISH. List the warnings.
2. **Completeness.** Every work-order slot has exactly one item with that `item_id`, carrying the slot's subtype, AOs, Bloom level, command word and tariff. Any item without a slot, and any changed label, must be recorded in that topic's `authoring_notes.json`. Write a short script for this; do not check 900 items by eye.
3. **Copied wording.** Run the tool against the subject's papers, mark schemes and reports. Never pass the syllabus.
   ```bash
   python3 operations/tools/check_copied_wording.py work/<workspace> "<folder holding the subject's papers, mark schemes and reports>"
   ```
   Pass only the folders holding papers, mark schemes and reports. Reword every 12+ word run unless it is a standard definition or formula. Read the 8 to 11 word runs and reword any that copy an exam's phrasing. List what you allowed and why.
4. **Level and scope.** Nothing is taught beyond the syllabus or above the level. On 0455 Economics an A-Level term, the Marshall-Lerner condition, reached IGCSE notes. The scope patterns cannot catch everything, so read for it.
5. **Truth.** Read every topic's notes, and at least 20 cards per topic. Look for:
   - inverted mechanisms ("limited liability reduces the lender's risk" is backwards);
   - claims missing their condition;
   - wrong cross-references (on 0455: "price elasticity is topic 2.6" when it is 2.7).
6. **Numbers and pictures.** Recompute every worked figure. Check that any situation a card describes could actually be drawn. On 0455, a point "on" a curve lay outside it, and an indirect tax was passed on in full to buyers despite an upward-sloping supply curve.
7. **Misconceptions.** Each misconception the plan gave a slot has a card that discriminates it, not one that restates the definition.
8. **Learner test.** Could a learner answer each sampled card from the notes alone?

**Fixing:**

- Fix learner-facing text in `topics/` yourself. After editing items or blocks in a topic, re-stamp them with:
  ```bash
  python3 operations/tools/restamp.py work/<workspace> <T> --note "<what you changed and why>"
  ```
- If you change a claim:
  1. raise its `revision`;
  2. update `claims_seen` on everything that cites it;
  3. where a citing text needed no change, add `"reviewed_unchanged": "<why>"` to it;
  4. run `restamp.py` on the topic.
- Re-run the checks, then republish with `publish_subject.py`.
- Do **not** change anything in `curriculum/`, the contracts or the work orders. List plan problems in the report instead.

**Report:**

- a verdict: **publish**, or **fix the plan first**;
- a findings table: what, where, fixed or not;
- plan problems, if any.

Update `STATUS.md`. **Stop.**

**YOU:**

- Read the verdict.
- If it says **fix the plan first**, open a new session in the **authoring** tool and paste:
  ```
  Read TEAM-PLAYBOOK.md. For <code> <subject>, workspace work/<workspace>/, the step 6 review found these plan problems: <paste them>. Re-open step 4: fix the plan, rebuild contracts and work orders, re-author only the topics affected, re-run their checks, republish, and update STATUS.md.
  ```
  Then run step 6 again on what changed.

### Step 7: Commit, push, update the tracker (YOU)

First set your tracker row to `published`, with the item count, the authoring tool and the reviewer. Then:

```bash
git pull
git add work/<workspace> publish/<workspace> operations/analysis/<stem>-*
git commit -m "<code> <subject>: reviewed and published" -- work/<workspace> publish/<workspace> operations/analysis/<stem>-* operations/SUBJECT-TRACKER.md
git push
```

- **Add and commit only your subject's paths, naming them after `--` as above.** Several sessions share one folder, so another session may have staged its own files. Naming your paths keeps them out of your commit. Never `git add -A` or `git commit -a`.

---

## 5. Rules every agent follows

1. **The syllabus is the source of truth.** Read it first. Transcribe from it; never write a weight, split or command word from memory.
2. **No plan without the corpus analysis. No resources without the plan.**
3. **One syllabus code, one set of documents:** one workspace, one analysis, one PLAN, one HANDOVER. Name every file with its code and subject. When you mention a code, give the subject name beside it ("9702 Physics"); people do not know the codes by heart.
4. **Every flashcard carries its Bloom level** (Remember, Understand, Apply, Analyse, Evaluate, Create), as well as its AOs, command word and tariff.
5. **Learner resources contain only what the analysis specifies.** Nothing beyond the syllabus, nothing above the level.
6. **Mine, do not reproduce.** No exam question, mark-scheme or examiner-report wording in learner-facing text. Never write "examiners reward", and never claim what a paper contains.
7. **Generated, never typed.** Contracts, work orders, notes markdown and published output come from the tools. Never edit them by hand, and never rename their output files.
8. **Stay in your lane.** Write only in your subject's workspace, its `operations/analysis/<stem>-*` files and its published output. Never write to `standard/`, `sources/` or another subject's workspace. If the standard itself seems wrong, report it to Vitalis.
9. **Agents never commit or push.** The person does, at the points shown.
10. **Context is Namibian.** Scenarios use Namibian and southern African places, businesses and names. Money is in N$. Spelling is British English.

---

## 6. Workspace names, and Namibian and junior/primary subjects

**Workspace names** give the board, the code (or subject), the level and the exam years, in lower case with hyphens:

| Qualification | Pattern | Example |
|---|---|---|
| Cambridge | `cie-<code>-<level>-<years>` | `cie-9702-as-2025-2027` |
| NSSCO (Namibia Senior Secondary Certificate, Ordinary) | `nam-<code>-nssco-<years>` | `nam-6144-nssco-2026` |
| NSSCAS (Advanced Subsidiary) | `nam-<code>-nsscas-<years>` | `nam-8245-nsscas-2026` |
| Junior secondary, grades 8 to 9 | `nam-<subject>_jss-gr8-9-<year>` | `nam-mathematics_jss-gr8-9-2026` |
| Upper primary, grades 4 to 7 | `nam-<subject>_up-gr4-7-<year>` | `nam-natural_science_up-gr4-7-2026` |

**The second part of the workspace name is the subject's code.** The build tools read it from there, and look for `operations/analysis/<code>-*-corpus-analysis.md`. So:

- take the code from the syllabus cover;
- if there is none, build one from the subject and the band, joined with underscores and with no hyphens inside it, such as `mathematics_jss` or `natural_science_up`. A hyphen inside it would split it, and the tools would read `natural` as the code.

**The file stem** (`<stem>`) names a subject's analysis, PLAN and HANDOVER files:

- with a code: `<code>-<level>-<subject>`, for example `9702-as-physics` or `6144-nssco-business-studies`;
- without a code: the code you built, then the grade band, for example `mathematics_jss-gr8-9` or `natural_science_up-gr4-7`.

The pipeline was proven on Cambridge IGCSE and AS subjects. Namibian subjects use the same steps, with these differences.

- **Sources.**
  - NIED publishes the syllabuses. DNEA sets the NSSCO and NSSCAS examinations and publishes examiners' reports.
  - NSSCO and NSSCAS papers and examiners' reports are under `Question Banks/Namibian Curricula/`, filed by subject and code, for example `NSSCO (New)/Business Studies (6144)/2023/`.
  - Papers labelled "First Proof" may not be the final printed version. The analysis says so when it uses them.
- **AOs and command words.** NSSCO and NSSCAS syllabuses state assessment objectives and a specification grid. Transcribe them exactly as in step 2, using the syllabus's own names and codes, for example "knowledge with understanding".
- **Subjects without external papers** (most grades 4 to 9 subjects):
  - **Step 3 becomes an analysis of the syllabus's own assessment**, written to the same file name. It covers the learning objectives and basic competencies, the assessment section (continuous assessment, tasks, tests and their weighting) and any official specimen or sample tests. It says plainly that there are no past papers, so every objective is weighted by the syllabus alone.
  - **Misconceptions** come from the syllabus, teacher guides and the team's teachers. They are never invented and labelled as evidenced.
  - **Flashcards for grades 4 to 7** are short and concrete, with one idea per card and language matched to the grade. Most are Remember, Understand and Apply.
- **Pilots first.** The checks were built against exam-evidence files. A subject with no papers may meet a check that reports `not_run` for lack of evidence, and `not_run` is never a pass.
  - The first subject of each new kind is a pilot, run by Vitalis: NSSCO, NSSCAS, grades 8 to 9, upper primary.
  - Any check that cannot apply is resolved in the standard. Nobody works around it in a workspace.
  - Each pilot is marked in the tracker when it publishes. Then the team scales that kind.
- **Grades 4 to 9 frameworks.** How these steps change for each band is in `operations/frameworks/`: `JSS-GR8-9-FRAMEWORK.md` (grades 8 to 9, with a crosswalk from older JSSEE and JSC papers to the current syllabus), `UP-GR4-7-FRAMEWORK.md` (grades 4 to 7, no exams) and `GR4-9-SOURCE-MATRIX.md` (what we hold for every subject). They are drafts until each pilot publishes.

---

## 7. Throughput: four subjects per person per day

**The target.** About 4 subjects per person per day, and the backlog cleared in about 3 days. That is realistic only if the work runs in parallel and the sources are ready before the day starts.

**The day:**

| When | What |
|---|---|
| Evening before | Steps 0 and 1 for tomorrow's subjects. Missing papers found at 9 a.m. stall the day |
| Morning | Steps 2 to 4 for subjects 1 and 2, in two sessions; answer their checkpoints as they come. Planning takes the most judgement and the most of your attention |
| Midday | Step 5 for subjects 1 and 2 (they run unattended). Meanwhile, steps 2 to 4 for subjects 3 and 4 |
| Afternoon | Step 5 for subjects 3 and 4. Step 6 reviews as authoring finishes |
| End of day | Step 7 for everything reviewed |

**Parallel work:**

- One subject per session. Never two sessions on the same workspace.
- Two sessions on different subjects in the same repository folder is fine.
- Commit only your own subject's paths.

**Cost:**

- Opus 5.5 at medium effort for authoring and review; high only for steps 2 to 4 on a hard syllabus. Codex at medium reasoning.
- If credits run out mid-run, nothing is lost. Start a new session in the **same tool** and paste the one-subject prompt.
- If you must switch tools, note in `STATUS.md` which topics each tool wrote (step 6 needs it).

---

## 8. When something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| Codex says the topics are empty, or a work order has a different number of tasks | Codex is in a **Worktree**: a copy from the last commit | Switch Codex to **Local** on the repository folder |
| `git` says `index.lock` exists | A git command was interrupted | Make sure no other git command is running, then delete `.git/index.lock` |
| Every PDF shows as modified | Git LFS is not installed | `git lfs install && git lfs pull` |
| "Out of credits" mid-run | — | New session in the same tool, same one-subject prompt; it resumes from `STATUS.md` |
| A topic fails the same check 3 times | The plan is probably wrong, not the author | `STATUS.md` says blocked. Re-open step 4 (prompt in step 6) or ask Vitalis |
| A check says `not_run` | Its input is missing | Find the missing input. `not_run` is never a pass. On a no-papers subject, see the pilot rule (section 6) |
| The scope check (C-11) fails on ordinary text | Its pattern is too broad. 0450 had one that flagged every "N$180 − N$40 = N$140" | Re-open step 4: narrow the pattern in `curriculum/scope-scan.json`, re-test its must-catch and must-allow examples, rebuild |
| `check_copied_wording.py` finds no text in PDFs | Poppler is not installed, or the PDFs are scans | Install poppler or pypdf. Scanned papers need OCR first; ask Vitalis |

---

## 9. Reference

**Where things are:**

| Path | What it is |
|---|---|
| `TEAM-PLAYBOOK.md` | This document: the order of work |
| `AGENTS.md`, `CLAUDE.md` | Read first by every agent; route to the role briefs and to this playbook |
| `standard/v0.2.0-draft/roles/` | `PLANNER.md`, `MINER.md`, `AUTHOR.md`, `REVIEWER.md`: how each step is done |
| `standard/v0.2.0-draft/build/` | `conform_registry.py`, `make_contract.py`, `make_work_order.py`, `render_notes.py`, `publish_subject.py` |
| `standard/v0.2.0-draft/checks/` | `run_checks.py`, `what_to_fix.py` (the fix loop), `yyeni_checks.py` (the check suite) |
| `operations/tools/` | `check_copied_wording.py` and `restamp.py` (step 6) |
| `standard/v0.2.0-draft/mine/` | Worked examples of the planning scripts. Read, do not run |
| `operations/analysis/` | Syllabus briefs and corpus analyses, one set per subject |
| `operations/SUBJECT-TRACKER.md` | Who is doing which subject, and its status |
| `operations/LAUNCH-PROMPTS.md` | Prompts for subjects planned before this playbook |
| `work/<workspace>/` | One subject: `STATUS.md`, `curriculum/`, `topics/<T>/`, `PLAN-*.md`, `HANDOVER-*.md`, `exemplar/`, `review/` |
| `publish/<workspace>/` | Published notes, flashcards (JSON), `INDEX.md`, `MANIFEST.json`, optional `diagrams/` |
| `sources/`, `Syllabi/`, `Question Banks/` | Original documents. Agents read them and never write to them. Namibian syllabuses are mostly under `Syllabi/Namibian Curricula/` |

**Finished subjects to learn from:**

| Code and subject | Workspace | Items |
|---|---|---:|
| 9618 Cambridge AS Computer Science | `cie-9618-as-2026` | 759 |
| 9702 Cambridge AS Physics | `cie-9702-as-2025-2027` | 860 |
| 9093 Cambridge AS English Language | `cie-9093-as-2024-2026` | 417 |
| 0460 Cambridge IGCSE Geography | `cie-0460-igcse-2025-2026` | 629 |
| 0450 Cambridge IGCSE Business Studies | `cie-0450-igcse-2026` | 913 |
| 0455 Cambridge IGCSE Economics | `cie-0455-igcse-2026` | 674, plus 46 diagrams |

**What every flashcard carries:**

- `item_id` (its work-order slot id);
- `subtype` or `item_type`;
- `assessment_objectives`, `blooms_level`, `command_word`, `mark_tariff`;
- `claims_seen`, `authored_hash`, `qa_status`;
- and, on MISCON cards, `misconception_entry`.
