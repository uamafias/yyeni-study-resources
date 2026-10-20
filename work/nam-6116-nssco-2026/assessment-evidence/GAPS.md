# 6116 NSSCO Biology — evidence gaps

MINER.md: "A limitation recorded is a limitation managed; a limitation omitted becomes a false
claim about the resource."

## 1. No mark schemes exist — the governing gap

DNEA does not publish mark schemes for NSSCO. None is held for any of the six series.

**Consequence.** The playbook's step 3.4, "what a creditable answer looks like", has no direct
evidence. `curriculum/answer-shapes.json` carries `answer_structure: null` for all 22 command
words. No award grammar, point count, development requirement or band descriptor can be stated for
this subject. Marking guidance must not be invented to fill this.

**Partial substitute, explicitly not equivalent.** The examiner reports print 39 indicative
`Answer:` blocks beside some questions. They lack tariff breakdowns and band descriptors and cover
only a subset of parts. Useful to read before authoring; not a mark scheme.

## 2. Series held and not held

| Series | Papers | Examiner report |
|---|---|---|
| 2020 | 1, 2, 3 (final) | yes |
| 2021 | 1, 2, 3 (final) | yes |
| 2022 | 1, 2, 3 — **First Proof** | yes |
| 2023 | 1, 2, 3 — **First Proof** | yes |
| 2024 | 1, 2, 3 (final) | yes |
| 2025 | 1, 2, 3 (final) | yes |

The 2022 and 2023 papers are First Proof versions. Section 6 of the playbook warns these may not
match the printed paper. Any command-word count or tariff drawn from those two years inherits that
uncertainty; they contribute roughly a third of the mined parts.

No specimen papers exist. No pre-2020 series applies — the current syllabus was first examined
in 2020.

## 3. Mapping not yet reviewed

MINER.md requires objective mapping by meaning, and warns that a token-matched pass on 9609 was
wrong repeatedly. This pass has **not** made objective-level claims. It proposes a **sub-topic**
per question part and per examiner statement using distinctive-term matching, records
`match_strength`, `matched_terms` and `mapping_confidence` on every record, and labels the method
in the data.

Of 341 question parts: 124 high confidence, 107 medium, 110 low.

**Consequence.** `exam-exposure.json` is sub-topic-level and provisional. The three sub-topics
showing no question part (3.6.2.1 Diet and nutrients, 4.3.3 Methods of birth control and increasing
fertility, 5.3 Population) are unconfirmed absences. No emphasis or coverage decision should rest
on them until a human has read the stems.

## 4. Misconception register uncurated

77 raw entries, each citing a named examiner statement. The curation pass that drops duplicates,
fragments and answering habits, and writes each discriminating test, has not run. 0450 went from
72 raw to 29 real. Treat 77 as a ceiling, not a count.

## 5. Carried forward from the syllabus stage

- **Denominator of "not more than 24% recall" undefined.** No interpretation adopted.
- **Paper 1 duration unconfirmed for 2026.** Syllabus 45 minutes; 2025 paper 1 hour; no amendment
  in the repository; 2025 examiner report silent. Needs NIED/DNEA.

## 6. Not attempted

Comparison against the 1,215 existing YYeni cards. Deferred to the upload stage per Vitalis; this
analysis builds from the syllabus and the assessment evidence.

## 7. Added after checkpoint review, 2026-10-17

**Mark reconciliation is now a standing check.** All twelve structured papers sum part marks to
their cover total (Paper 2 80/80 in each of six years, Paper 3 40/40). The earlier 479 for Paper 2
was an extraction defect: a length threshold intended to drop question-total lines also dropped the
genuine part "(ii) phagocyte [1]" (2021 Q3, nine characters). The test is now absence of words, not
shortness. Any future mismatch means the extractor is wrong, not the paper.

**Scoring percentages are Paper 1 only.** The reports give per-question percentages for the
multiple-choice paper and essentially none for Papers 2 and 3. They measure multiple-choice item
difficulty and are not comparable across papers. Three sub-topics rest on a single observation
each; one sub-topic has 18 observations spanning 25%-80%. No topic-difficulty ranking is supported
until the mapping pass has run.

**Classifier limitations.** Each examiner statement takes the first matching class, so 13
statements (5%) that match two classes lose the secondary one; per-class counts are lower bounds.
The "shallow development" patterns are the narrowest of the six and its single hit across 70 pages
is a classifier artefact, not a finding about candidates.

**Two gates must close BEFORE the plan is built:** validate the mappings that guide emphasis, and
curate the 77 raw misconceptions. Coverage is not gated by either - every mandatory syllabus
objective is covered regardless of measured exposure.

## Defects in the mined part records, found during objective mapping (2026-10-18) — REPAIRED the same day

Reported by the three Miner passes that read every Paper 2 and 3 part in its paper
(`planning/objective_mapping/map_A|B|C.json`). Mapping is keyed on `part_index`, so none of these
affects it. They matter to anything that keys on `question_ref` or trusts `command_word`.

- **`question_ref` drops the parent letter** (mine_papers.py). "2(i)" is really 2(b)(i), so refs
  collide within a paper. Examples: 2020 P2 "4(ii)" is parts 10, 12 and 14; 2022 P2 "7(i)" is parts
  135, 138 and 140; 2025 P3 "4(i)" is parts 333 and 337. Never use question_ref as a key.
- **Stems missing their parent instruction.** Parts 62–64 are the single words "lymphocyte",
  "phagocyte" and "red blood cell"; part 267's stem is cut off.
- **Mislabelled part.** Part 188 ("6(iii) end products [3]") is the whole of 2023 P2 6(c).
- **Wrong or missing command words.** Part 277 is "construct", recorded as "identify". `command_word`
  is None for many parts opened by "Give a reason", "What is meant by" or "Make a large labelled
  drawing". The command-word counts in the corpus analysis are therefore slight undercounts.
- **Stray margin text.** A stray "Use" and leading "(i)" appear in several stems.
- **Figures not in the text.** Parts 168, 242, 280, 281 and 304 depend on labelled figures; their
  mappings rest on context, at medium or low confidence.
- **Errors in the papers themselves.** 2021 P2 2(c)(iii) refers back to "(i)" but means "(ii)"; 2020
  P2 figure numbering is out of order; 2021 P2 Q8 points to "Table 6.1"; 2024 "tube-tube A".
- **Content beyond the syllabus wording in the papers.** 2023 P2 asks for smooth endoplasmic
  reticulum (the syllabus lists rough ER only) and for ATP counts (not in the syllabus). Recorded as
  evidence of what was asked, not as scope: the resource stays within the syllabus.

### Repair, 2026-10-18

`planning/mine_papers.py` was corrected and the papers re-mined:
- **Full references.** Every level is kept: 4(b)(ii), not 4(ii). A letter printed on the question
  line ("4 (a) Peeled apples ...") and a sub-part printed on the letter's line ("(a) (i) Make a ...")
  are now read. Answer-line sub-items that share one part are numbered (4(e)-1, 4(e)-2, 4(e)-3).
  Unmarked answer lines followed by one mark are recorded as the whole item (2023 P2 6(c), 3 marks).
  Result: 341 parts, 341 unique references, 720 marks, matching the covers.
- **Command words.** The recorded word is now the one that opens the instruction, not any glossary
  word found in the stem. "Use Fig. 2.1 to calculate" is calculate; "Construct a dichotomous key"
  is construct, not identify. Slashed glossary forms are split ("Give a reason" counts under "give a
  reason/give reasons"). A part whose instruction sits in its parent stem inherits it ("lymphocyte
  [1]" under "State the functions of ..."). Five parts asked as direct questions ("How many
  stomata ...?") are recorded as `direct question`, not as a command word.
- **Stray margin text.** The "For Examiner's Use" margin is stripped before the opener is read.

Every part lines up with its earlier record by position, tariff and stem. The objective mappings
were made by reading each true item in its paper, so they carry across; they are now keyed on
year/paper/full reference (`part_key`), not on list position. The command-word counts, modal
tariffs, framework, exposure and work orders were regenerated from the repaired records.

### Targeted mapping repair, 2026-10-18 (Codex)

All 341 raw parts and 720 source marks remain inventoried. There are now 339 direct objective
records and two explicitly excluded records in `mapping_exceptions.json`: 2023 P2 2(c)
(pesticide-uptake process unresolved) and 2022 P2 1(d)(i) (extinction definition, conservation
context only). Neither counts as direct objective exposure. 2024 P2 6(a) identifies the nucleus
in the source figure and now maps to cell structure, not prepared-slide meiosis. The cell type
differs from the palisade/liver examples in that objective, so the limitation is retained.

Direct confidence is 262 high, 77 medium and zero low. This does not mean the whole mapping has
independent approval: it is the original Miner pass with targeted repairs, and the unresolved
pesticide part remains low confidence in the exception register. See `review/STEP4-REPAIRS-2026-10-18.md`.
