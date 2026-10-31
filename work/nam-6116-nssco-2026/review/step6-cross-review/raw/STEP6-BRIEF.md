# Step 6 cross-review brief (READ-ONLY, one round)

You are a REVIEWER under the playbook's Step 6 and standard/v0.2.0-draft/roles/REVIEWER.md (read it first: fixed question set, one round, findings are debt, do not hunt beyond the questions). You change NOTHING in the workspace. Workspace: /Users/yyeniai/yyeni-study-resources/work/nam-6116-nssco-2026. The material is NSSCO Biology 6116 (Namibia, Cambridge-style Ordinary Level, learners about 15-17). Authoring was Codex's first draft followed by substantial Claude repair rounds; you are reviewing the final content as delivered. The named-teacher checkpoint is waived by the operator; the claims stay unverified, so your reading is the only semantic check this material gets: be accurate and be specific.

Deterministic checks (arithmetic, coverage, references, scope scan, contract counts) have passed: do not redo them. Do not report AO / Bloom / command-word / tariff labels (already audited; proposals are recorded). Do not report the standard renderer's header line. Items citing 'Fig. VIS-6116-...' are deliberately held until a figure exists: judge them only for clean wording and a sound biological answer.

## Your inputs
- Items: the JSON file named in your task (every performance task in your area, every misconception item, plus a random sample of flashcards). Read every record.
- Notes: the rendered notes file(s) named in your task. READ THEM IN FULL (Step 6 requires reading every topic's notes).
- curriculum/misconceptions.json (the curated misconception entries; items carry `misconception_entry` ids), curriculum/objective_registry.json (objectives), curriculum/syllabus-exclusions.json and curriculum/scope-scan.json (what is out of scope).

## The questions (answer them, log findings, stop)
1. Is any causal mechanism inverted or invalid? Highest value.
2. Does any answer rest on a fact its prompt does not supply?
3. Is a conditioned mechanism taught unconditionally anywhere (condition stated in one place, dropped elsewhere)?
4. Is anything taught that the syllabus does not require (beyond level or scope), or required and missing? Check objective coverage in the notes for your area against the registry's wording and the exclusions.
5. Is any figure, formula or worked example wrong (recompute every worked number and every cross; check the method and that the interpretation follows)? Could every situation a question describes actually occur or be drawn (a point described as on a curve, a ratio that cannot arise)?
6. Learner test: pick TWO objectives in your area that carry a top-tariff item (tariff 4 or more), write the full answer from the NOTES ALONE, and say whether it would earn the marks. Also, for 6 further sampled flashcards, say whether a learner could answer from the notes alone.
7. Misconceptions: for every item in your file that carries a misconception_entry (or subtype MISCON), say whether it DISCRIMINATES the misconception (the learner must choose between the right idea and the wrong one) or merely restates the definition; also whether the stem gives the answer away.
Additionally (Step 6 item 4/5): wrong cross-references (e.g. a note citing the wrong section number), claims missing their condition, duplicated or contradictory statements between notes and cards.

## Output
Write ONE YAML file to the path in your task, a list of findings in exactly this shape (YAML, no prose around it):
- issue_id: <area>-001
  severity: critical | high | medium | low     # critical = teaches something false a learner would act on; high = trains invalid reasoning; medium = inaccurate or inconsistent without misleading; low = tidiness
  category: accuracy | analysis | evaluation | curriculum | quantitative | coherence
  affected_ids: [exact item ids, note headings or block ids]
  finding: what is wrong, stated so someone who has not seen the material understands it
  evidence: the passage quoted with its id
  educational_consequence: what a learner would do wrong
  recommended_repair: what to change
  confidence: 0.0-1.0
  status: open
After the findings add a final YAML mapping under the key `coverage_statement:` stating how many items and which note sections you read, the answers to questions 6 and 7 (briefly), and what you did not check. Be calibrated: separate certain errors from doubts (use confidence). No praise, no padding. Reply to me in under 120 words with counts by severity.
