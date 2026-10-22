# Review of NSSCAS Chemistry 8224 pilot evidence

**Reviewed:** 2026-10-18  
**Reviewer:** Codex  
**Status:** Substantively sound, but not yet ready to be marked verified

## Overall assessment

The Chemistry package has a solid factual foundation. The syllabus and source claims are mostly correct, but the frequency evidence and YYeni curriculum mapping need repair before the package can support a final pilot decision or authoritative claims about the most frequently examined topics.

## 1. Frequency count

The percentages in `assessment-evidence/FREQUENCY-COUNT.md` are internally consistent and reconstruct to 348 classified marks or items.

However:

- Only 188 of the available 240 Paper 2 marks were captured.
- Therefore, 52 Paper 2 marks are missing. The combined evidence contains 348 of the intended 400 Paper 1 and Paper 2 marks, or 87%.
- The number of missing marks varies by year, causing some examination years to carry more weight than others.
- The stated uncertainty of approximately ±3 percentage points has not been established through validation. The missing marks could produce changes larger than three percentage points.
- The classifier script and question-level assignments were not retained, so the classifications cannot be reproduced or audited.
- Assigning all marks in a multi-mark question part to a single topic can distort integrated questions that assess more than one syllabus area.

The frequency table is suitable as a preliminary planning aid, but it is not yet defensible as evidence for a formal “most examined” claim.

## 2. Live YYeni curriculum

The principal classroom claims were confirmed:

- School 17 is `NSSCAS Template Classrooms`.
- Classroom `a5695c1d-390d-4025-b013-2e218a2c1ca9` is `NSSCAS Chemistry`.
- It contains four sections and 44 lessons.
- It currently contains zero flashcards.
- There are 202 objective records, of which five are blank.

The following objective-level problems were found:

### Redox processes — lesson 6626

One objective record is blank. The syllabus objective requiring learners to use oxidation numbers to name oxyanions is absent from the usable objective text.

### Group 2 — lesson 6658

The objective about trends in physical properties, including melting points, is duplicated. The syllabus objective covering reactions of Group 2 elements with oxygen, water and dilute acids is absent.

### Group 17 — lesson 6674

One objective record is blank. The missing syllabus content is the interpretation of relative hydride stability in terms of bond energies.

### Alcohols — lesson 6832

Three objective records are empty. The syllabus objective requiring recall and use of systematic alcohol nomenclature, for chains containing up to six carbon atoms, is absent from the usable objectives.

### Stoichiometry — lesson 6508

Objective 30757 is truncated during the note defining standard and room conditions. It ends after “where s.t.p is expressed as 101 kPa, approximately,” and omits the remainder of the syllabus wording.

These objective records should be repaired before flashcards are authored or mapped to classroom objectives.

## 3. Syllabus-to-YYeni mapping

The following statements in `curriculum/SYLLABUS-SUMMARY.md` need correction:

- Theme 1 contains six YYeni lessons mapping to syllabus topic 1.3, not five.
- The two lessons containing “electronegativity” do not represent an objective overlap. Lesson 6557 maps to 1.3.3, while lesson 6589 maps to 1.3.4. The repeated term comes from the syllabus headings.
- The two Atoms, molecules and stoichiometry lessons already merge the five syllabus subtopics: lesson 6507 contains 1.1.1–1.1.4 and lesson 6508 contains 1.1.5. They do not merely need to carry those units in the future.

The following mapping problems in the summary were confirmed:

- Topic 1.2 Atomic structure has no YYeni lesson.
- The Group 2 trends lesson is incorrectly filed under Physical chemistry rather than Inorganic chemistry.
- Reaction kinetics 2.4.1 and 2.4.2 are merged into one lesson.
- Organic chemistry 4.1.2 and 4.1.3 are merged into one lesson.

## 4. Syllabus verification

The summary was checked against the official local NIED syllabus:

`Syllabi/Namibian Curricula/NSSCAS/NSSCAS_8224_Chemistry_approved_syllabus_updated_20_November_2020.pdf`

The following statements are correct:

- The qualification is a one-year NSSCAS course with approximately 180 guided learning hours.
- NSSCO Chemistry is recommended prior learning rather than a compulsory entry requirement.
- Grades run from a to e.
- Paper 1 contains 40 multiple-choice questions, lasts one hour and carries 40 marks.
- Paper 2 lasts 1 hour 15 minutes and carries 60 marks.
- Paper 3 lasts two hours, carries 40 marks and consists of two or three experiments.
- The Data Booklet is available in Papers 1 and 2.
- The qualitative-analysis notes are supplied with Paper 3.
- The four themes, 20 topics and 52 leaf teaching units are counted correctly.
- The stated content boundaries concerning mass spectrometry, hybridisation, ionisation-energy explanations, infrared data, stereoisomer terminology and practical qualitative analysis are supported by the syllabus.
- The listed burette-reading requirement of 0.05 cm³ is correct.
- The organic structural-formula conventions are correctly attributed to Annexe C.

The sentence saying that cards must not require learners to recall information supplied in the Data Booklet should be labelled as a flashcard design policy rather than a syllabus rule. Recall of supplied information may still be educationally useful, even though the examination does not require unaided retrieval.

## 5. Assessment-weighting conflicts

The summary correctly identifies internal contradictions in the syllabus.

### Paper weighting

The syllabus gives:

- Paper 1: 31%
- Paper 2: 46%
- Paper 3: 23%

This agrees with its prose statement of 77% theory and 23% practical, but it does not agree with the raw marks. The 40/60/40 mark allocation produces approximately:

- Paper 1: 28.6%
- Paper 2: 42.9%
- Paper 3: 28.6%

### Assessment-objective weighting

The syllabus prints AO A 40%, AO B 40% and AO C 20%. Its mark grid instead assigns A 50 marks, B 50 marks and C 40 marks, which produces approximately:

- AO A: 35.7%
- AO B: 35.7%
- AO C: 28.6%

The package should preserve these as unresolved contradictions in the official syllabus rather than choosing one representation without qualification.

## 6. Source inventory

The source inventory and recorded hash prefixes were checked against the local files and are correct.

Confirmed:

- Papers 1–3 are present for 2021–2024.
- The proof-version descriptions in `sources/SOURCES.md` match the filenames.
- No Chemistry 8224 marking-scheme files were found in the repository.
- No Chemistry 8224 examiner reports for 2021–2024 were found.
- The NSSCAS Examiners Report 2025 contains Chemistry 8224 coverage for Papers 1, 2 and 3, beginning at printed page 71.
- The report supplies Paper 1 keys and performance percentages, along with comments and expected-answer or marking information for Papers 2 and 3.
- The 2025 question papers are not in the repository, so the report cannot be joined to the original question text.
- The NSSCAS Chemistry revision-notes directory contains only `.gitkeep`.

The 2025 examiner report is currently stored under the Biology workspace. It should eventually be placed in a shared source directory so that Chemistry does not depend on a path belonging to another subject package.

## 7. Authority order

The authority order in `CLAIM.md` should include official assessment evidence. A clearer order is:

1. Official syllabus for examinable scope and stated boundaries
2. Official question papers for observed assessment coverage
3. Official examiner reports and marking guidance for difficulty, credited responses and common errors
4. YYeni classroom curriculum for operational lesson and objective mapping
5. Revision notes and textbooks as explanatory secondary sources

These sources serve different functions, so question frequency should not override syllabus scope, and learner difficulty should not be treated as frequency.

## 8. Required work before pilot selection

1. Repair the corrupt and missing YYeni objectives.
2. Retain the classification script in the repository.
3. Create a row-level evidence file recording year, paper, question, part, marks, primary topic, any secondary topic, confidence and source page.
4. Recover and classify all 240 Paper 2 marks.
5. Manually review ambiguous and integrated questions.
6. Validate the keyword classifier against a manually coded sample before assigning an uncertainty range.
7. Keep examination frequency and documented learner difficulty as separate measures before combining them for prioritisation.
8. Incorporate the 2025 examiner-report evidence as a separate difficulty analysis.

## Provisional pilot recommendation

Subject to the repairs above, topic 1.1, Atoms, molecules and stoichiometry, is the strongest provisional pilot area. It has the largest share in the preliminary 2021–2024 frequency count, while the 2025 examiner report independently identifies difficulties involving the mole concept, mass spectral analysis and significant figures.

A manageable first flashcard set should target a defined objective cluster rather than all five subtopics at once. Suitable clusters include:

- interpreting mass spectra and calculating relative atomic mass;
- the mole, Avogadro constant and reacting-mass calculations; or
- empirical and molecular formula calculations with correct significant figures.

This recommendation remains provisional until the Paper 2 evidence is complete and the question-level classifications have been manually checked.
