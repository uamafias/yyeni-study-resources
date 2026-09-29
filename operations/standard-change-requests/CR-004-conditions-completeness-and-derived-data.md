# CR-004 — Conditions, completeness, derived data and units

**Raised:** 2026-09-12 · **Against:** standard v0.2.0-draft · **Delivers:** four runtime rules, four checks,
a waiver mechanism for C-27 and a review-ingest step
**Trigger:** the third RS-28 review of topic 5.4 (`operations/review/cie-9609-as-2026-2028-5.4-review-r3.yaml`)
returned **reject** with 7 open issues — 0 critical, 3 high, 4 medium — on a build whose deterministic pass had
reported 35 of 37 checks passing.

## 1. What round three actually measured

| Round | Standard in force | Blocking issues (critical + high) |
|---|---|---|
| 5.2 R1 | v0.1.0 | 13 |
| 5.4 R1 | v0.2.0 | 8 |
| 5.4 R2 | v0.2.0 + R1 repairs | 2 |
| 5.4 R3 | v0.2.0 + R2 repairs | **3, none critical** |

The curve is flattening but it has not reached zero, and the reason is worth writing down. Of the three high
issues in round three, **all three were defects the round-one and round-two repairs introduced or failed to
finish** — not authoring defects. R3-002 is the clearest case: the round-two repair correctly conditioned
`CLM-9609-5.4-040` on the overhead being unavoidable, and left four parallel cards teaching the same mechanism
with no condition at all. The claim was right and the learner-facing material was still wrong.

**The rule this gives us: a repair is not finished when the claim is correct. It is finished when every
artefact that asserts the same mechanism carries the same conditions.** RS-41 already made *stale* derivatives
visible by comparing revisions; it could not see an artefact that was never stale because it cited a different
claim. RS-43 closes that hole.

## 2. New runtime rules

| Rule | Requirement | Born from |
|---|---|---|
| **RS-43 Conditioned mechanisms carry their conditions** | Where a subject registers a mechanism whose conclusion holds only under stated conditions, every claim, block and item asserting it must carry every condition. The register is `conditioned_mechanisms` in the subject profile. | R3-002 (keep-or-drop chains asserting overhead unchanged, and omitting the opportunity cost of freed capacity), R3-007 (bank charges classed fixed by label against the topic's own behaviour rule) |
| **RS-44 An answer may not supply its own facts** | A canonical answer or its marking guidance must not assert a completeness fact unless the learner-visible prompt establishes it, or the recommendation is made explicitly conditional on checking it. | R3-003 (ITEM-055 rewarding the learner for establishing that N$5 was the total incremental cost, which the stem never said) |
| **RS-45 Derived metadata is recomputed, never edited** | Every count, series total, maximum tariff, command mix and exposure class must recompute from its evidence records and satisfy the definitions the file itself states. A superseded figure is removed, not retained beside the new one. | R3-004 (nested pre-remap metrics kept beside new totals; exposure classes contradicting the file's own tariff definition; downstream prose still quoting the old figures) |
| **RS-46 Quantities are named in their own units** | A currency amount is not expressed in physical units, nor a count in currency, and a figure not derivable from the stated data is not asserted. | R3-005 ("60 haircuts of profit"), R3-006 (a lowest-price question with no determinate answer) |

## 3. New checks

- **C-37** (RS-43) — scans every claim, block and item against the subject's registered conditioned mechanisms
  and fails any artefact that asserts one without carrying every condition. `not_run` where no register exists,
  which is an honest "nothing to enforce" rather than a silent pass.
- **C-38** (RS-44) — fails an answer that asserts a completeness fact its own prompt does not establish. The
  distinction that makes it precise: naming a cost **category** ("its variable cost is N$110") states a total;
  enumerating named **instances** ("flour, yeast and packaging come to N$5") does not.
- **C-39** (RS-45) — recomputes every exposure figure from the evidence records, parses the file's own class
  thresholds out of its `classes` text and tests each classification against them, and fails a metric duplicated
  at the top level of an entry beside the nested `evidence` object the rest of the file uses.
- **C-40** (RS-46) — fails a currency amount named in physical units, or a count named in currency.

**C-27 gains a waiver mechanism.** An exposure class names the subtypes an objective gets as a *floor*. Where a
named subtype does not fit the objective, or would duplicate a card held elsewhere, the topic contract waives it
in `subtype_waivers` with a written reason of at least twelve words; anything shorter fails the check. Padding a
bank to satisfy a count teaches nothing, and a silent gap hides a real one — so every waiver is reported on
every run, and a waiver whose card later exists is reported as redundant.

**`checks/ingest_review.py` is new.** Merging a semantic review into a topic's qa report was a hand edit until
now, which is how review R3 came to be answered in the artefacts while the qa report still showed R1 and R2. At
~3 000 topic builds a hand edit is a defect generator. The script requires a written resolution per issue and
refuses anything under twelve words; unresolved issues stay open and count against RS-42.

## 4. One amendment outside the rules

`exam-exposure.json` classed objectives `probed_high` on tariff alone, which made `probed_high` with a 3-mark
ceiling a contradiction of the file's own definition — R3-004's finding. The definitions now read on both
dimensions: **probed_high is 8 marks or more *or* named in 5 or more distinct series**, and probed_low is a low
ceiling reached rarely. This is what they always meant; frequency was an unwritten exception. Recomputing all
258 objectives against the amended definitions moved exactly one: `OBJ-9609-5.4.2-05`, probed_low to
probed_high on an 8-mark maximum. The two `unmeasured_*` classes are judgements about what the probe can
distinguish, not computed classes, and the recompute leaves them alone.

## 5. Proof

`standard/v0.2.0-draft/tests/test_checks_r3.py` proves each new check twice — it must fire on a minimal
synthetic build that plants its defect, and pass on the same build repaired — plus C-37's `not_run` behaviour
and C-27's waiver semantics. Suite total: **43 tests**. Before the repair, all four new checks fired on the
real 5.4 build and named the artefacts the reviewer named, plus two the reviewer did not: ITEM-046-CALC for the
completeness defect, and ITEM-053-APP as a false positive that drove the category/instance distinction above.

## 6. The lesson worth keeping

CR-003's lesson was that *hedging can make a factually inverted statement pass a language check*. This round's
is narrower and more useful:

> **A repair that fixes the claim leaves the topic wrong.** Every mechanism is taught in several places, and
> the condition has to travel to all of them. A check that compares revisions cannot see this, because the
> unrepaired copies were never stale — they cite a different claim. Only a check that recognises the
> *mechanism*, independently of which claim it hangs on, can find them.

The second-order version, already recorded under C-35 and confirmed again here: rounds two and three found
defects introduced by repair, not by authoring. Repair deserves the same deterministic scrutiny as authoring,
which is why `repair_5_4_r3.py` aborts rather than stamping any artefact it did not actually re-author.
