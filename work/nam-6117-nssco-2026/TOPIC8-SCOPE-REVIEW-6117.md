> **Latest targeted repair:** [Prompt, activity and open-item report](TARGETED-LEAK-REPAIRS-6117.md). Named leaks and 8-P03 repaired; all 12 QA runs pass. **236 answer-only note blocks, missing worked methods, MC length bias and broader semantic/visual review remain open.** Recall 390/1,637 (23.82%); publication stays on hold.

# Topic 8 and copied-wording review response — 29 October 2026

All five feedback points have been addressed. **Release remains on hold for independent review.** The changes and classifications below are author decisions, not a new independent approval.

## Exact copied-wording scope

The previous 24 paths were selected from assessment-evidence source locators: all 22 PDFs in the Chemistry question-bank folder plus the 2024 and 2025 reports in the annual examiner-report archive. The four omitted paths were the archive copies of the 2020–2023 reports. Each is **byte-for-byte identical** to the corresponding report inside the Chemistry folder; SHA-256 comparison confirms this. The earlier report failed to make that path-level distinction clear. No distinct report content was removed.

The check now explicitly includes **all 28 paths**, representing **24 distinct file contents**. See [the exact path list](review/copied-wording-sources.md) and [the machine-readable paths, SHA-256 hashes and duplicate relationships](review/copied-wording-sources.json). The corpus contains no separately released mark schemes; examiner reports provide the available marking guidance. The full-source script reconstructs and verifies this manifest on each run.

The new full scan reports zero runs of 12 or more words and nine eight-word matches. Those nine were read as standard definitions/terminology. See review/copied-wording.md. This is a copied-wording test, not certification of source interpretation.

## Topic 8 design changes

The flame-test cluster no longer consists of paired wire-blank cards. Only 8-017 retains that diagnostic design.

| Cards | Current purpose |
|---|---|
| 8-015, 8-019, 8-021 | Closed-book flame colours: lithium/sodium; potassium/barium; calcium and the object observed. |
| 8-016 | Design result-table headings that distinguish flame colour and individual repeats. |
| 8-017 | Diagnose a wire-blank contamination result. |
| 8-018 | Judge consistency across three repeat observations, without a wire-blank scenario. |
| 8-020 | Explain masking of a weaker potassium colour by brighter sodium emission. |
| 8-022 | Improve an imprecise colour record and inconsistent viewing conditions. |
| 8-023 | Use a fresh-portion precipitation result to resolve an ambiguous flame result. |
| 8-024 | Arrange a fair comparison of differently prepared samples. |
| 8-037, 8-039, 8-042, 8-043, 8-045 | Recall the reagent/indicator or splint and positive observation for the five gas tests. |
| 8-038, 8-040, 8-041, 8-044, 8-046 | Retain distinct follow-ups: spray versus gas exposure, gas versus precipitate colour, a timed bleaching sequence, ignition safety, and a flawed oxygen-test procedure. |

The application cards are no longer used to replace every closed-book test question. Short factual test cards are useful here; a common “test and observation” answer shape is deliberate for those cards rather than being presented as novel reasoning.

## Annexe B knowledge coverage

The following cards require test knowledge without supplying the matching reference in the prompt. The anion questions test identification from remembered observations; they are not a claim that every full reagent recipe is independently elicited by those six cards.

| Required knowledge | Current card numbers |
|---|---|
| Lithium and sodium flame colours | 8-015 |
| Potassium and barium flame colours | 8-019 |
| Calcium flame colour | 8-021 |
| Ammonia test and positive observation | 8-037 |
| Carbon dioxide test and positive observation | 8-039 |
| Chlorine test and positive observation | 8-042 |
| Hydrogen test and positive observation | 8-043; also 7-064 |
| Oxygen test and positive observation | 8-045 |
| Carbonate, chloride, bromide, iodide, nitrate, sulfate identification | 8-026, 028, 030, 032, 034, 036 respectively |

All the listed Topic 8 cards now have explicit recall credit. The previously zero-recall nitrate-identification card was corrected to one recalled mark. Direct and reverse test knowledge is supported by the consolidated notes table and the complementary procedure/error cards. The exact current IDs and coverage assertions are in planning/round8-diversity-checks.json.

## Minor label fixes

10-032 now opens **State**, and remains FEATURE / AO A / Remember with one recalled mark. It no longer disguises a known double-bond answer as a suggestion.

12-014 is now **Calculate / CALC / AO B / Apply**, mapped to numerical processing objective 12.2-02 and backed by the numerical-differences teaching claim. It asks for corrected delivered volume from 1.20 and 24.80 cm³ readings, both 0.20 cm³ high. The answer is 23.60 cm³; the common offset cancels. Its one mark credits this single result. It remains distinct from 1-051's apparatus selection.

## AO and recall decision

Current marks are **A 784 (47.89%), B 546 (33.35%), C 307 (18.75%)**, totalling 1,637. The largest difference from the approximate 50/30/20 syllabus proportions is B at +3.35 percentage points.

**Author decision: retain this balance for the study bank.** The bank deliberately includes extra evidence interpretation and diagnostic practice alongside explicit test knowledge. It is not a mock examination, and the qualification's assessment proportions are not an exact quota for this collection. Labels follow the authored credit; no cards were relabelled solely to make the totals look closer. Any exam-style assembly must separately follow the syllabus paper structure and weights.

Restoring test recall raises the estimate from **373 to 390/1,637 (23.82%)**: 16 marks of restored direct test recall plus one nitrate-identification correction. It is below the 24% trigger but above the contingency's preferred 23% target. This is a deliberate tradeoff to restore essential retrieval practice, not a claim that more headroom has been achieved. Nineteen additional recall marks fit below 25%; twenty would breach it. Three additional marks would reach the 393-mark internal review trigger.

The recall rule and revised cognitive demands still require independent acceptance. If review triggers another correction batch, preserve the explicit Annexe B retrieval coverage rather than removing it again to improve a percentage.

## Validation and rebuild

All twelve topic QA runs have zero failures and retain hold. Production accounting, audit fingerprints, learner-asset/MC regressions and current round-five/six/eight checks pass. The round-seven entry point explicitly delegates to the current combined replacement check because some historical zero-recall assertions are intentionally superseded. The new check verifies exact authored text, recall credit, Annexe B coverage, one remaining wire-blank card in the flame cluster, numeric correction, and all 28 source hashes.

The final repair pipeline is apply_round5_repairs.py → round6_polish → round7_replacements → round8_diversity, followed by note rendering and QA. Run check_copied_wording_full.py for the full source manifest and copied-wording scan. Nothing was committed or published. Earlier carry-forward requirements and independent review gates remain in force.
