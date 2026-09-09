# Changelog

## 0.2.0-draft - 2026-09-08

Raised by CR-003 after the RS-28 independent review of the pilot topic (Cambridge AS Business 9609, topic 5.2)
returned **reject** with 15 open issues on a build whose deterministic pass had reported 22 of 25 checks passing.

- **Added RS-33 to RS-40** - bounded generality, generalisations surviving their members, variant completeness,
  assessment claims requiring assessment evidence, command-word-shaped practice, declared answer structures,
  offline reconstructibility, meaningful traceability.
- **Amended RS-07** (a mapping counts only where the item actually practises the objective) and **RS-21**
  (third-party behaviour is likelihood with a reason, never certainty).
- **Six new hard release blockers.**
- **New check suite** at `checks/` - 28 subject-agnostic checks, `not_run` never counts as a pass, a raising check
  is a failing check. Proven against the unrepaired pilot: it independently rediscovered 13 of the 15 review issues.
- **New generated review packet** at `checks/make_review_packet.py` - the reviewer brief and prompt are assembled
  from the build, not hand-written per topic.
- **New human-maintained inputs**: `subject-profile.yaml -> variant_register` and `-> answer_structures`;
  `contract.json -> depth_constraints.excluded_constructs`.
- **New `OPERATOR_RUNBOOK.md`** for teams running the pipeline across many subjects.
- Recorded, in the check source and the runbook, one check that was written and withdrawn for firing on 47 of 68
  items, so nobody rewrites it.

### Found while repairing the pilot topic

- `run_checks.py` now **carries forward any semantic review already on file**. It previously overwrote
  `qa_report.json` wholesale, so every deterministic run silently erased the reviewer's verdict.
- The release decision now reads **unresolved issues**, not the stored verdict. A review that said reject and
  whose issues are all resolved leaves the build awaiting re-review rather than rejected forever - and a build
  whose issues the author has marked resolved can never reach `pass` on that basis alone.
- Added **C-00 schema validity** (the suite had no schema check) and schema support for the three new fields the
  rules require: `generality` on a claim, `generalisation_scope` on a content block, and `variant_register` /
  `answer_structures` on a subject profile.
- Added `build/render_notes.py`. The offline notes are now **rendered from the content units** rather than
  maintained separately, which is what makes RS-39 structural instead of aspirational.
- Two language patterns were narrowed after firing on ordinary prose: `never` and `always` now need a modal or a
  quantified object, and `guarantee` now needs a verb form. `can be` was removed from the hedge list - it was
  suppressing genuine exclusivity claims such as "can be obtained only from".

### Second review round - RS-41 and the propagation gate

The pilot topic was reviewed again after repair and rejected a second time with 14 issues. The finding underneath
most of them was one thing: the repair had corrected claims without propagating to every item and block citing
them, so a claim and a card sat side by side saying opposite things. Two of the three criticals were that.

- **Added RS-41 - derived work goes stale when its source changes.** Claims carry a `revision`; blocks and items
  record `claims_seen`. Bumping a claim leaves every citing artefact stale until re-authored. A stale derivative
  blocks release. Schema support added for all three fields.
- **Added C-29** to enforce it. Bootstrapped from the repair history already recorded in the files, it found
  **22 stale artefacts** on the unrepaired build - including every propagation defect the reviewer named.
- **Fixed C-28.** The packet manifest contained its own hash, which can never verify because writing the line
  changes the file. The manifest now excludes itself and its hash is detached in `packet.sha256.hash`.
- **C-12 now scans per content-unit block** rather than a character window. A variant named three sections away
  from the term has not been named where the term is taught.
- Two more over-broad language patterns narrowed (`no other`, and the `guarantee` noun).

**The lesson worth keeping:** the un-propagated card said limited liability makes borrowing "usually easier and
cheaper". The hedge suppressed the language check. *Hedging can make a factually inverted statement pass a
language check* - the pattern sees caution, the content is still wrong. Language checks police confidence, not
truth, and no amount of pattern work changes that.

## 0.1.0-draft — 2026-08-31

Initial team-review package containing:

- concise operative runtime standard;
- machine-readable runtime standard;
- end-to-end pipeline;
- universal artifact schemas;
- Business subject profile;
- Cambridge International AS Level Business 9609 qualification profile for 2026–2028;
- deterministic validator and pytest suite;
- valid draft fixture and negative controls;
- independent semantic-review protocol;
- draft Claude Co-work handoff prompt;
- team review questions.
