# Claude Code review: 6136 NSSCO Development Studies, Step 2 syllabus transcription

**Reviewer:** Claude Code (Opus 5.5), independent read-only review of Codex's Step 2 transcription. This is not a Step 6 resource review, not teacher or specialist approval, and not a pipeline pass.

## 1. Verdict: **FIX REQUIRED** (minor; the AO and paper tables themselves are correct)

Every number Jeremy is being asked to check is correct against the printed PDF. That covers the AO definitions, the eight printed grid rows, the summed AO marks, paper marks, durations, weights and Paper 3 section marks. The same goes for the 10 themes, 18 topics, 102 source bullets and 35 glossary entries.

The fixes needed are:
- one sentence in the brief that states an interpretation as a syllabus fact (F1);
- a few omitted pieces of Paper 3 guidance (F2, F3);
- verifier coverage gaps, which mean some fields are only checked by the script that wrote them (F5–F7).

None of these changes a table value.

## 2. What I inspected and limitations

- **I read the primary PDF directly** with the Read tool's pages option, in three batches: **PDF pp.1–10, 11–20 and 21–30**. That is all 30 pages, including the cover, the contents, pp.6–7 (printed pp.3–4), every learning-content table at PDF pp.8–20 (printed pp.5–17), and the AO, scheme, grid, grade-description, explanatory-note and glossary pages at PDF pp.21–29 (printed pp.18–26). PDF p.30 is the back cover.
- **I compared** the PDF against `syllabus-facts.json` (assessment objectives, ao_weights, papers, command_words, themes, limits, paper3_sections, transcribed_notes, and every specific-objective `text` field), the brief, both scripts, and both result JSONs.
- **Limitations:**
  - I did not run either script, as instructed.
  - I did not open `syllabus-grid-pdf23.png`, because I looked at PDF p.23 directly.
  - I did not read `syllabus-page-text.json` in full.
  - I did not check the `verbatim` strings in the source lines character by character against pdftotext output. I checked the reconstructed `text` fields against the rendered page images.
  - Visual checking is my own reading and is still subject to human error.

## 3. Findings

| # | Severity | Status | Location | Issue | Correction |
|---|---|---|---|---|---|
| F1 | Medium | Confirmed defect | Brief, Papers section, line 26; `transcribe_syllabus.py:220` | "The own investigation must be carried out, but is **not itself submitted** as formally assessed coursework." The source never says the investigation is not submitted. PDF p.26 (printed p.23) says "each learner must present his or her own investigation report", and that it "will not be assessed as a formal coursework assignment, a number of questions will be set on it as part of the Paper 3 examination." "Not submitted" is an interpretation. | Replace with: "Learners carry out their own investigation (individually or in groups) and each presents their own report. It is not assessed as a formal coursework assignment, but Paper 3 sets questions on it (Section B, 15 marks) (p.23 [PDF 26]; p.22 [PDF 25])." |
| F2 | Medium | Confirmed omission | `syllabus-facts.json` `limits` / `paper3_sections` | The Paper 3 guidance that defines what Section B can ask is missing. That includes the example exam tasks on p.23 [PDF 26]: identify their own research question or hypothesis; describe how they collected data; illustrate the presentation methods used; justify their choices of collection and presentation; briefly communicate conclusions; evaluate their methodology. It also includes the investigation stages 1–4 and the report components (a)–(e) on p.22 [PDF 25], such as recommendations and the limitations of the data. These go beyond the wording of the 10.1 objectives (for example *justify* and *evaluate their methodology*), and they set 15 marks of Paper 3. | Add verbatim, cited records, for example `paper3_guidance.investigation_stages`, `.report_components` and `.section_b_example_tasks`. Label them as guidance examples, not an exhaustive list. |
| F3 | Low | Confirmed omission | `command_word_table` | The glossary preamble on p.24 [PDF 27] is missing. It says the meaning of a term "must depend in part on its development context" and that "Illustrative techniques … encompasses such things as maps, diagrams, sketches, graphs etc." Ten or more definitions use "illustrative technique", so this note defines a term they depend on. | Add it as `command_word_table.preamble_verbatim` with its citation. |
| F4 | Low | Confirmed omission | `papers[2]`; brief | The Paper 3 note on p.22 [PDF 25] is headed "Paper 3 **(Alternative to coursework)**". This label is not recorded. | Record it in the Paper 3 entry or the transcribed notes. |
| F5 | Medium | Confirmed verifier gap | `verify_syllabus_facts.py` (whole file) | The verifier never checks `ao_weights.grid_rows_as_printed[*].marks`, `qualification_weight_percent_as_printed` or `grid_marks` against the page. It only checks that each verbatim string appears on the page, that each paper's `ao_marks` total its marks, and that `qualification_percent == AO marks/2`. A row-label error would pass, for example the B.1 values attributed to A.4: the moved marks and percentages shift together, so both checks still agree. The writer does compare the grid against a hard-coded list (`transcribe_syllabus.py:81-84`), but that list is Codex's own reading, not an independent check. (I confirmed visually that the values are correct.) | In the verifier, re-parse each grid row's three paper columns and its % column independently from p.23. Assert that they equal `grid_rows_as_printed`. Assert that `grid_marks` and `papers[*].ao_marks` are the row sums. |
| F6 | Low | Confirmed verifier gap | `verify_syllabus_facts.py:33` | Durations are checked against a hard-coded `[135,120,105]`, not parsed from the verbatim. Paper 3 section marks (35/15) and AO `name`/`text` are never compared with their verbatim either. A wrong duration in both files would pass. | Parse hours and minutes from each paper's verbatim. Parse "(NN marks)" from each section verbatim. Assert that each sub-skill's `text` equals the normalised verbatim with its code removed. |
| F7 | Low | Confirmed verifier gap | `verify_syllabus_facts.py:49-55` | Specific objectives are compared as one flattened list. Topic `id`, `title`, `theme` and the topic each bullet belongs to are not verified, so a bullet assigned to the neighbouring topic would pass. Both scripts also use the same pdftotext `-layout` extraction and the same column logic. The brief's "checked against a fresh PDF extraction" is accurate, but STATUS.md's "independently rechecked" overstates it. (I counted bullets per topic myself and all match the PDF: 1.1=7, 1.2=3, 2.1=1, 2.2=2, 3.1=11+3, 4.1=6, 4.2=5, 5.1=8, 6.1=3, 6.2=6, 7.1=7, 7.2=3, 7.3=7, 8.1=5, 9.1=8, 9.2=3, 9.3=2, 10.1=12.) | Assert per-topic bullet counts and topic titles against the left column. Also add a `pdftotext -raw` cross-check, or reword STATUS.md to say "re-extracted with the same tool". |
| F8 | Low | Confirmed inconsistency | `assessment_objectives[3]` | `name` is "Problem solving" (taken from the sub-heading, because `dict(re.findall)` keeps the last match). `verbatim` is "D.     Problem-solving" (taken from the list). The name does not match its own cited line. The source uses both spellings. | Use the sub-heading line as the verbatim, or record both spellings. |
| F9 | Low | Confirmed | `limits[*].source.section` | The section is the placeholder "4 / 10 / 11 as applicable". | Use the real sections: "4 Additional information – Prior learning", "10 Explanatory notes – (ii) Individual research", "11 Glossary". |
| F10 | Low | Interpretation recorded as fact | `transcribed_notes[2]` | The note calls NDP5 a "prescribed example". The source introduces it with "e.g.", so it is an example, not a prescription. The brief's wording ("syllabus examples") is correct. | Change "prescribed examples" to "examples". |
| F11 | Low | Confirmed | Structure of `content_outline` | The General Objectives column only appears inside the verbatim lines; there is no structured field for it. It is not required at Step 2, but the Step 4 registry will need it. | Add `general_objectives[]` with citations. Note that the Theme 8 header on p.14 [PDF 17] misprints the third column as "GENERAL OBJECTIVES". |
| F12 | Low | Confirmed | `content_outline` 3.1, bullet 13 | "micro- electronics" is an artefact of joining the line at the hyphen. The PDF has "micro-" at a line end, so the word is "micro-electronics". ("hunter- gatherers" in 5.1 is printed with the space in the source and is fine.) | Remove the space after a hyphen at a line end when reconstructing text. |
| F13 | Low | Uncertainty | `command_words[9]`, `[10]` | On p.25 [PDF 28] the left column reads "Explain or" / (gap) / "Account for/" / "Factor". The definition "Characteristics bringing about…" lines up with "Factor". The JSON reading ("Explain or Account for/" → Give reasons; "Factor" → Characteristics) is the most plausible, and the count of 35 depends on it. It is still a layout interpretation, and the slash is a typographic artefact in the source. | Keep as is, but add a note saying that this split is a layout reading. |
| F14 | Low | Omission (information) | `edition`, `papers` | "FOR IMPLEMENTATION IN 2019" (cover), "Grades available A\*-G" (p.19), the 130 guided learning hours (p.3), and the column of AOs tested per paper in the weighting table (A,B / A,B / B,C,D) are only kept as raw strings or not at all. | Optionally add them as structured fields. |
| F15 | Low | Presentation | Brief, AO table | The "Overall" column is described as derived in the prose but not in the column header. The brief also omits the eight printed rows, so Jeremy cannot compare the brief row by row with the p.20 grid. | Rename the header "Overall (derived sum of printed rows)" and add the 8-row table from §4a below. |

**Checked and found correct** (no finding):
- All four AO names and all eleven sub-objectives, worded as on p.18 [PDF 21].
- The grid's spelling "diagrammatical" against the AO list's "diagrammatic" is preserved.
- The combined A.1/A.2 row is preserved, and no split between them is invented.
- Blank grid cells are recorded as 0, which is correct.
- Every printed-to-PDF page citation I checked uses the constant +3 offset, which is correct.
- All three paper descriptions are verbatim.
- The p.22 statement that "all the questions … test C and D" is recorded next to the p.20 grid's B=15. Both are kept, the grid is used only for the numbers, and B is not dropped. This is handled correctly.
- The 102-bullet count is right: the enterprise wording on p.7 and its restatement with examples on p.8 are both kept, and it is clearly labelled as not a count of unique objectives.
- The glossary has 35 entries; my own count is 7 + 16 + 12 = 35. The "What differences are shown between A and B changes" label and its two-part definition are retained. Every `use_in_prompts` is null, and no prompt-use approval is implied.
- There are no explicit "not assessed" exclusions in pp.5–17. I confirmed this visually.
- The own-investigation limit is captured verbatim.

## 4. Independently verified tables

### 4a. Specification grid as printed (p.20 [PDF 23]); paper columns are marks

| Printed row | P1 | P2 | P3 | Overall % (printed) |
|---|---:|---:|---:|---:|
| A.1 / A.2 (one combined row) | 20 | 15 | – | 17.5% |
| A.3 | 15 | – | – | 7.5% |
| A.4 | 20 | – | – | 10% |
| B.1 | 25 | 15 | 5 | 22.5% |
| B.2 | – | 25 | 5 | 15% |
| B.3 | – | 15 | 5 | 10% |
| C. Investigation | – | – | 25 | 12.5% |
| D. Problem solving | – | – | 10 | 5% |
| **Total (printed)** | **80** | **70** | **50** | **100** |

### 4b. AO totals: all **derived** by adding the printed rows; no per-AO totals are printed

| AO | P1 | P2 | P3 | Overall (derived) | P1 % / P2 % / P3 % (derived) |
|---|---:|---:|---:|---:|---|
| A Knowledge with Understanding | 55 | 15 | 0 | 35% | 68.75 / 21.43 / 0 |
| B Analysis and Evaluation | 25 | 55 | 15 | 47.5% | 31.25 / 78.57 / 30 |
| C Investigation | 0 | 0 | 25 | 12.5% | 0 / 0 / 50 |
| D Problem solving | 0 | 0 | 10 | 5% | 0 / 0 / 20 |

Each derived overall percentage equals the sum of the printed row percentages, and also equals AO marks ÷ 2 (out of 200 total marks). The two methods agree only because each paper's printed weight equals its marks ÷ 2.

### 4c. Papers: everything printed except where marked

| Paper | Duration (p.19 [PDF 22]) | Marks | Weight (p.20 [PDF 23]) | AOs tested (p.20) | Structure (p.19) |
|---|---|---:|---:|---|---|
| 1 Written | 2 h 15 min | 80 | 40% | A,B | All four questions compulsory, structured, based on stimulus material, drawn from the whole curriculum; 4 × 20 marks |
| 2 Written | 2 h | 70 | 35% | A,B | Two compulsory structured questions on related source material; 2 × 35 marks |
| 3 Written | 1 h 45 min | 50 | 25% | B,C,D | Two compulsory sections: supplied data on a development issue, and the learner's own investigation |

- **Paper 3 sections** (p.22 [PDF 25]): Section A, research methodology using data provided, 35 marks. Section B, the learner's own research investigation, 15 marks.
- **Paper 3 AOs:** p.22 says all questions test C and D, while the p.20 grid gives B=15, C=25, D=10. Both statements are recorded, and the numbers come from the grid.
- "All learners will take papers 1, 2 and 3" (p.19).

## 5. Is the summary ready for Jeremy's Step 2 checkpoint?

**The AO table and paper table are ready to show Jeremy.** Their values and page citations are correct. The brief should get two small edits before it goes to him:
1. Replace the unsupported "not itself submitted" sentence (F1).
2. Label the Overall column as derived, and add the 8-row printed grid so he can compare it line by line with p.20 (F15).

F2 (the Paper 3 Section B guidance) should be added to the facts file before Step 3/4 work relies on it, but it does not affect the tables. F5–F7 are verifier hardening: the current PASS results confirm that the quotes and totals are internally consistent, not that every parsed field matches the source. Jeremy's visual check of PDF pp.21–23 is still the actual checkpoint, and this review does not replace it.
