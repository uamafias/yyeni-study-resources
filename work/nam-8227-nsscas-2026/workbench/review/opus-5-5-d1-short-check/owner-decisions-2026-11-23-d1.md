# Owner decisions: D1 short check, 23 November 2026

**Owner:** Vitalis.
**Recorded by:** Claude (REVIEWER), during the OD-3 short check of the D1 plan manifest. That manifest is `planning/plan-manifest.json`, sha256 `c8914cf9…`.

These decisions are final. They bind the D2 repair. They add to OD-1, OD-2 and OD-3 in `../opus-5-5-step-3/owner-decisions-2026-11-23.md` and do not replace them.

| # | Question put to the owner | Decision |
|---|---|---|
| OD-4 | D1 keeps two Analyse-level branches, but the check finds neither is supported. (1) **Stationary-point classification:** a routine first-derivative sign test earns full marks. The official 2025 P1 Q9(c) scheme accepts that test alone, and the two-extrema part labels the same evidence Apply. (2) **Motion direction change:** in all 108 instances the velocity changes sign at exactly one root inside the interval, so the decision never varies. This followed the step-3 repair prompt's own instruction, "one interior simple root". How should the pilot label these? | **Make the motion decision live and relabel classification Apply.** <br>• Motion: admit a bounded minority of instances where the velocity does not change sign inside the interval. The learner must then check before splitting, and the marking credits that check. <br>• Stationary-point classification: relabel it Apply 3. <br>• The pilot keeps one Analyse branch, which must be supported by its own criteria. |
| OD-5 | Trapezium bias part (d) uses D1-TRAP-FT-BRIDGE. A correct sketch is marked as in 2023 Q6(d): a verbal or chord reason is enough, and no drawn trapeziums are needed. A learner's own wrong curve gets follow-through, which 2025 Q4(b) supports. Codex calls this a departure; the check finds it does not misjudge learners. How should (d) be marked? | **Accept the bridge, reworded.** <br>• "No drawn trapeziums" is the 2023 same-type standard, not a departure. <br>• The only extension is that DB1 is judged against the learner's own curve, as supported by 2025 Q4(b). <br>• Define the two missing cases: a drawn chord with a brief statement, and more than one graph in (c). |

**Settled by OD-1, so not put to the owner again:** the modulus answer-only split.
- **The official row.** The official 2023 P2 Q2 row (report PDF 331, printed 329) reads "a = −2 www B1, b = −3 www B1, c = 2 www B1", plus "Allow all the marks if values are seen in the correct place in the formula".
- **What OD-1 requires.** The official scheme for this question type therefore awards correct values given without wrong working. Under OD-1, correct a, b and c with no wrong working earn B1 www each, whether given as named values or in the formula.
- **The D1 split.** The D1 rule is "list 0, formula 3", labelled `D1-MOD-OD1-LIST` as an "owner-binding interpretation". It was never an owner decision.
