# Handover — NSSCAS Mathematics 8227, repair round 5

Role: AUTHOR (Codex). Owner: Vitalis. Workspace: `work/nam-8227-nsscas-2026/`.
Commission: `workbench/review/opus-5-5-repair-r4/REPAIR-PROMPT.md`.
Work is active; no owner-only decision blocks progress.

## Verified checkpoint: YM PDF 535, 2026-11-20

- Page census: **841/891**, **50 pending**. Goldie318/318; YM523/573.
- Answers: **5,309 responses /2,071 response items**. Statuses:4,401matches,318sketch,377show/prove,107keywrong,45nokey,61keyincomplete.
- Inventory: **3,751 source records /3,646 individual mapping reviews**. **252 source defect/caution entries**; this is not a count of252 wrong numeric keys.
- Focused answer verifier59856 and sequential integration/inventory/census/progress/R4/R5 suite77301 **passed** through535.
- Full C11 double rebuild43100 **passed**:2×224commands,134byte-identical outputs,30seeded errors rejected. Archived `analysis/history/rebuild-verification-r5-YM-C11-complete.json`.
- C12 opening529–531, curves532–533 and logarithms534–535 are wired. Chapter12 remains incomplete.
- New log-component checker uses d ln|u|=uprime/u only on real nonzero components. It does not join components or allow a definite integral across a pole. Added31st seeded fixture `log-primitive-coefficient`:correct negative coefficient passes first;wrong coefficient is rejected with the expected assertion. Full runner includes it; full31-fixture rebuild still pending.

## Exact continuation

`author_YM_C12_log_geometry.py` covers536–537; first run session16086 ACTIVE. It is **not wired** yet. Its source and all needed key pages have been READ. Once its exact assertions pass, wire before answer verifier and run the sequential focused suite. Preserve original Q2 precision:Try10Q2 does not explicitly request3sf;its key displays9.16/5.84,so compare rounded key values while retaining exact areas internally. Try10Q1 and Example10 explicitly ask3sf.

Source through539 READ in `YM-C12-536-source.png`;538–539 trig tasks **not authored yet**. Source540–543 rendering81583, **not read yet**. Nothing after539 read. Keys649–652 read; later key pages not read.

Next author script: C12 trig opening538–539. Figure IDs next32. Basic trig integrals use M2T5O01D02;identity choice and transformed squared trig demands are M2T5O02D01/D02,not automatic extra direct links on every trig primitive. Preserve radians and tangent/cosine poles. Use the existing primitive helper and independent integration checks. Contact sheet shows Example11/Try11,Example12/Try12,Example13/Try13,plus derivative/integral/identity reference panels. Read source exponents at native scale if unclear. Next read540–543.

All source builders through535 are saved. Current full proof is only through528; current focused proof through535. Both books still await independent acceptance. T5 cross-book families/138-demand synthesis,T6 fresh-copy/final snapshot,whole-book metadata/role/exam-style/prose audits remain open. Frozen analysis-snapshot staysR4untilT6. Both books complete AND accepted before step3.

## New source resolutions

- **Example8(b),PDF535:**native bounds1..3 of4/(3−2x)cross pole3/2. Left integral diverges+infinity,right−infinity. Printed−ln9comes from invalid endpoint subtraction. No ordinary improper integral exists. Registered severe defect;exclude as valid worked exemplar. Native bounds and working crops saved and hashed.
- **Log domain convention,PDF534–535:**printed ordinary-ln primitives with positive-argument intervals are correct restricted branches. Original rational integrands also have negative-argument components. Full real primitives use ln|u|with independent constants on each component. The source advice to use absolute values only for definite integrals is a convention caution,not official marking policy. Registered separately,not as wrong numeric keys.
- C12 Try2Q4(b)really has infinite upper bound;finite expression3−e^−a−2e^−3a has limit3as a→infinity. Convergence retained.
- C12 Try3show-relations ask algebraic/logarithmic rearrangements,not numerical roots. Positive arguments justified from the original integral equation. Try3Q3alone asks a3sf3.65.
- C12 Try5regions distinguish area under a curve from area between y1 and e^−x. Positive parameter selects positive square root in Try5Q1.
- C11 details preserved in `analysis/history/r5-YM-C11-complete-HANDOVER.md` and earlier history. C11=47pages/136responseitems/263responses/138panels;10exam-style textbook items;Revision11=30marks. The final Revision11Q5manual status is key-wrong because second derivative2/5iswrong though Y4/minimum correct;correct value4/25.

## Working procedure and constraints

Render and READ actual pages;rendering alone is not a census. Fixed-source scripts extend existing tools under `tools/textbook-r5/`. Existing item IDs get corrections;new recovered items get explicit metadata. Assessed/component demand sets must be disjoint. Every generated key comparison uses independently transcribed original givens. Textbook originals remain internal.

After a saved batch:answer verifier;relevant independent numeric checks;source addenda;inventory;census;progress;R4;R5 `--stage textbook-working`,sequentially. Do not start inventory before answer verification finishes. Full rebuild hashes analysisroot JSON/MD and globbed author-input JSON:do not mutate those or wired scripts while a full rebuild runs. New renders and unwired Python drafts are safe. Archive successful full proofs. Current runner has31seeded fixtures.

Vitalis requested checkpoints at most roughly100pages apart;save more often at verified batches. Update HANDOVER/STATUS/report and archive useful evidence. Distinguish rendered,read,author-verified,deterministic rebuild and independent acceptance.

**No commit/push;Vitalis commits.** No PLAN,recipe contract,recipes,runtime generators,work orders,imports or learner assignment. Do not modify review folders,source PDFs/root textbook,standard,other subjects,app or pinned checkouts. Preserve unrelated work. No new scraping scripts. No delegated agents authorised.

Part1 saved totals remain821award rows(818official/3derived),42Eflags,95marking rules,31confirmed Cambridge pairs across29NSSCAS questions;independent acceptance pending. Last protected source/review/HEAD verification was at511,unchanged. HEAD`11cd03fe639f9936dd9f83fd04bd6f04d5181676`. Working synthesis:`analysis/textbook-insight-working-notes-r5.md`.


### Checkpoint: YM541, 2026-11-20

Sequential focused suite8378passed through541:847/891pages,44pending;5358responses/2094responseitems;3780source records/3698mappingreviews. Statuses:{'matches': 4440, 'sketch': 318, 'show/prove': 387, 'key wrong': 107, 'no key': 45, 'key incomplete': 61}. 252source defect/caution entries. C12builders529–541wired. Both sources,all19protected review files,HEAD and R4snapshot history reverified unchanged. Full230-command double rebuild is the next action,with31seeded fixtures. UNWIRED542–543mathchecks61860passed;UNWIRED544–545mathchecks4681running. Source546–547READbutnotauthored;noafter547read. Step3,T5/T6andindependentacceptanceunchanged;no commit/push.
