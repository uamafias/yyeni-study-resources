# Targeted leaks and activity repair — 29 October 2026

**The named prompt leaks, 8-P03 structure and command issues are repaired. This is not a completed bank-wide editorial review. Publication remains on hold.**

## Completed in this round

| Feedback | Repair |
|---|---|
| 8-013 colour mapping supplied | Removed the colours from the prompt. The rubric requires the remembered Fe²⁺/green and Fe³⁺/red-brown links for one mark, plus the reason shared insolubility cannot distinguish them. One mark is now counted as recall. |
| 9-015 extraction answer supplied | The prompt supplies only that X lies below carbon and occurs as its oxide. Credit requires selecting carbon reduction and linking it to that position; the method alone earns no mark. |
| 8-029 reference matching | Removed the bromide reference. The learner identifies bromide from the observations, then uses the remaining chloride comparison to explain discrimination. One mark now counts as recall. |
| 8-P03 repeated data and trivial cation part | One shared laboratory record precedes the five parts. Part (b) is now two marks: cation identification plus correction of precipitate versus solution using the excess-ammonia result. The sequence is recording observations → identification/state correction → halide procedure → interpretation/reagent choice → limits of the conclusion. Tariffs are 3/2/2/3/2, still 12 overall. |
| Authoring phrase | No current activity prompt contains “Original synthetic results”. |
| 8-023 / 8-024 commands | 8-023 uses Deduce with Analyse; 8-024 uses Plan with Create. The existing barium colour question 8-019 now explicitly maps to the barium outcome and teaching claim, preserving its Describe practice without mislabelling the planning task. |
| MC key-only full stop | Removed terminal full stops uniformly from all 132 sets of four options. Zero sets now have a terminal full-stop cue. Keys and scientific option content are unchanged. This does not certify every possible stylistic cue. |
| 7-056 / 7-063 | 7-056 now assesses only the general insolubility rule for one mark. Its explanation explicitly includes soluble barium hydroxide alongside sodium/potassium, and slightly soluble calcium hydroxide. 7-063 retains the named barium-hydroxide and lead-ethanoate exceptions. |
| Fuel-oil contradiction | Removed the remaining “ships and industrial heating” wording from the notes/claims; current wording is ships and home heating systems. The fraction sequence now also includes the lubricating fraction. |
| VIS-5-02 | Changed the carbon-anode equation to water oxidation, 2H₂O → O₂ + 4H⁺ + 4e⁻, and stated that the solution becomes more acidic. The former hydroxide equation was atom/charge balanced; the water form makes the aqueous copper-sulfate context and acidification clearer. The regenerated image was visually inspected. |
| Topic 12 caption / Topic 11 meta-text | Removed the stale hardness-apparatus caption from the cooling figure and the project-webpage/authoring commentary from the desalination paragraph. |
| Scrambled sections | Added authoring/render_notes_ordered.py: it uses the unchanged standard renderer, then sorts numbered sections by syllabus number. All numbered section sequences are checked. Cross-mapped objectives no longer pull later numbered sections to the front. |

## Explicitly unresolved / deferred

- **236 answer-only Activity worked example / Activity feedback blocks remain in the notes.** They have not been converted into independent worked-method examples or removed in this round. They must not be described as fixed.
- **Missing worked methods and wider note structure/padding remain open.** Numeric section ordering is fixed, but that is not a full teaching-quality rewrite.
- **MC length bias remains open.** Correct options are uniquely longest in 12/132 questions and longest including ties in 56/132. Removing punctuation cues does not resolve length or distractor-quality issues.
- **Near-duplicate pairs outside the targeted cards remain open.** Automated similarity checks do not establish that all semantic duplicates have been removed.
- **Broader visual corrections/review remain open.** This round changed VIS-5-02 and the named caption; it does not claim all other visuals were changed or independently verified.

These are explicit deferred release-work items. They are not being treated as passed or as optional merely because mechanical checks pass.

## Anion direction — precise limitation

8-026 through 8-036 give observations and ask for the ion. **No card currently asks the complete forward question “Which reagent is used for Cl⁻, and what do you see?”** The notes table and complementary procedure cards do not remove this card-direction gap. The optional two forward-direction cards were not added in this round.

## Recall, scope and validation

The new remembered colour and bromide answers add one recall mark each. Revised 8-P03 has four recall marks rather than two. To implement the contingency through authored demand, 11-057 now interprets measured exhaust changes and a misleading all-emissions claim; 11-045 assesses a nitrogen-packaging trial and the limits of its conclusion. Each replaces two factual marks with specific supplied-evidence credit. No Annexe B recall cards were removed.

Net change: +1 +1 +2 −2 −2 = 0. Recall remains **390/1,637 (23.82%)**, an author estimate requiring independent acceptance. The bank remains 808 cards plus 36 activities. AO marks are A 780 (47.65%), B 550 (33.60%), C 307 (18.75%). The existing decision to retain a study-bank interpretation emphasis stands; this is not an exam blueprint.

All 12 topic QA reports have zero failures and hold. Accounting, freshness, learner-asset/MC and targeted regression checks pass. The full copied-wording scan retains all 28 documented paths: zero 12-word defects, nine eight-word standard-term matches. See planning/round9-repair-checks.json for the exact repair assertions and unresolved-block count.

Rebuild with authoring/apply_round5_repairs.py (now ending with round9_repairs), relevant visual generators, then **authoring/render_notes_ordered.py**. Rerun all topic checks and accounting/regression checks after rendering. Direct use of the generic renderer alone can restore the cross-objective ordering issue. No standard/ files were changed, and nothing was committed or published.
