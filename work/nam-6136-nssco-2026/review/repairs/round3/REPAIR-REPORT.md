# Third-review repairs — Development Studies 6136

Jeremy authorised these repairs on 21 October 2026. Codex repaired the ten findings in the preserved [third independent review](../../CLAUDE-RESOURCE-REVIEW-3.md). These are author repair dispositions; no fourth independent review has been requested or performed.

| Finding | Local disposition and evidence |
|---|---|
| R3-01 | Expanded all ten cited P01(b) four-mark model answers in topics 5.1–9.3 into developed causal explanations using their supplied facts. Updated the corresponding marking guidance to credit distinct contextual development, without imposing a universal one-mark-per-sentence rule. |
| R3-02 | Replaced 62 blocks that contained full card prompts with authored worked explanations using different scenarios or quantities. Corrected the additional stale 7.3.02 example separately. The final note-to-card comparison finds zero complete card prompts pasted in notes. All 66 restored teaching paragraphs remain intact. |
| R3-03 | 4.2.05-04 now describes 100 people available for work, preserving the distinctions between unemployed, employed, underemployed and unmet work needs. |
| R3-04 | 10.1-P02 explicitly states that both output totals include spoiled bags. The numerical audit now requires this supplied fact; removing it in an in-memory negative case is rejected. |
| R3-05 | 7.3-006 and its notes now explicitly map community apprenticeship to traditional education and college to modern institutional education. Both use the same qualification and cost conditions. The obsolete allowance and apprenticeship assessment scenario is removed. |
| R3-06 | Removed assessment-pipeline provenance from the SDG lesson. Added Quality Education, Gender Equality and Climate Action, with a developed climate-impact, adaptation and future-needs explanation. Local assessment locators remain in the revised claim ledger. |
| R3-07 | 1.2-006 now asks for one action, one resource-saving explanation and one directly supported goal. Its three-mark guidance credits each component. The answer uses SDG 12 and no unsupported paid-work condition. |
| R3-08 | Corrected 2.2-003 guidance to assess its actual HPP pillar contrast. Existing three-mark 2.2-P02(a) now practises describing three HPP pillars through interpretation of supplied actions, with three distinct descriptive marking points. This supplies the requested practice without adding a slot or mislabelling a recall-only task as interpretation. |
| R3-09 | Existing two-mark 1.2-P01(a) now asks for two sustainable-development pillars. NDP5 notes distinguish named pillars from intended goals. All existing item labels and total tariffs are retained; the changed practice focus is recorded in authoring_notes.json. |
| R3-10 | Removed internal item IDs from learner notes and replaced guidance for 8.1-025/027–032 with specific credit criteria. |

## Validation

- All 18 topics return deterministic decision `publish`, zero failures and `what_to_fix` exit 0. The known runner exit-code discrepancy remains explicit; a tool decision is not independent approval.
- All 543 planned slots retain their IDs, objective mappings, subtypes, AOs, Bloom labels, commands and tariffs. Totals remain 749 claims, 101 units, 505 flashcards and 38 activities. Rendered notes contain 36,079 words.
- Twelve targeted regression checks pass, including preservation of all 66 restored paragraphs, zero complete card prompts in notes, aligned education scenarios, supplied output/loss denominators and goal/tariff/guidance consistency.
- Seventeen checks parse actual research stimuli, answers and tariffs. A negative case proves that omitting the spoiled-inside-output fact is detected. The age-sex audit now reads the actual 7.1 card stimulus rather than relying on duplicated card prose in the notes.
- Recomputed the new worked examples: storage loss 18 to 8 leaves 82 to 92 usable units; tourism differences N$15 and 15 litres; density 18,000/600 = 30; population changes 5% and 20%; school-place gap 120; enrolment 60% and 80%; goods surplus N$7 million; export receipts N$10,000 and N$8,000; stratified allocation 12 and 6 from a sample of 18.
- Copied-wording scan: 40 saved assessment extracts, zero 12+ word defects. One 11-word match consists of the official titles and numbers for SDGs 8 and 12. It is retained as standard goal terminology, not copied question wording.

Two claim texts have proper revision increments, propagated claims_seen records and explicit unchanged-text decisions where appropriate. The official restamp tool records previous text hashes for edited items and blocks. `baseline/` preserves exact pre-repair JSON; `actions.json`, `targeted-validation.json`, `render-restamp-log.json` and `validation.json` record changes and checks.

## Remaining limits and reproduction

Earlier N-03 external fact/source-verification debt and the standard-owner graph/schema/runner limitations remain open. These repairs remove the reported notes duplication and vary its worked cases; they do not claim that every recurring scenario in the card bank has been replaced. The third review's plan/profile inspection remained partial. Claims remain unverified/non-publishable and items remain review_required.

The current repair source is `round3/repair.py`, replayed after the previous repair scripts. It reads its immutable pre-repair snapshot, writes targeted edits, then requires the standard restamp and render tools before checks. Run `validate_repairs.py`, `topics/audit_build.py` and the copied-wording scan. Do not run old author scripts alone. No web research, Claude call, publication, import, commit or push occurred during this repair pass.
