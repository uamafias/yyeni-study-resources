# NSSCAS Mathematics 8227 — repair round 5 continuation

AUTHOR Codex; owner Vitalis. Updated 21 November 2026. Commission: `review/opus-5-5-repair-r4/REPAIR-PROMPT.md`. Owner decision: both textbooks must be complete AND independently accepted before step 3. No owner-only blocker is known.

## Current verified source checkpoint

All891 pages in the agreed source envelope enumerated: Goldie318, YM573, through PDF585; one duplicate scan excluded.48pages have no retained in-scope item starts. All3940source records are linked into the census;1758are teaching/given-figure records.5752responses across2181responseitems were independently author-derived and compared:4735matches,336sketch,460show/prove,111key wrong,46no key,64key incomplete.268source defects/cautions are not268wrong answers. One wholly out-of-scope Goldie activity has no prescribed response record.

## Current T5 checkpoint

129authored analysis families;771source items fully grouped;1406response items pending. Five wholly out-of-scope items are explicitly excluded. Twenty-two insight sections cover65/138demands;73remain pending. These are analysis groups,not approved recipe counts. Whole connected source items remain preserved when a family cites selected response labels.

Blocks grouped: GoldieC1/C10; YM C1/C2/C3/C5/C8. Cross-book algebra,polynomial/modulus,progression/binomial,functions/coordinate geometry and vectors are authored. Textbook originals remain internal.

Author inputs are five `author_textbook_synthesis_*_r5.py` scripts under `tools/textbook-r5/`,emitting `synthesis-*.json`. `tools/build_textbook_synthesis_r5.py` creates `analysis/textbook-families.json/.md` and `analysis/textbook-insights.md`. `check_textbook_synthesis_r5.py` passes and rejects three seeded errors (unknown member,lost response,unsupported demand).

Focused source/mapping checks pass in `checks/r5/T5-first-audit-validation.log` and `checks/r5/T5-functions-validation.log`. Mapping audit corrections are listed in `analysis/textbook-synthesis-audit-r5.md`. New correction: YM C3Try14Q1(b)explicitly supplies f and fg and asks for missing g,so decomposition demandM1:T3:O04:D02is now directly linked on that part/item. Render126reread in `checks/r5/textbooks/YM-C3-124-source.png`. Math answers and population counts unchanged. Other family claims were narrowed to direct item evidence rather than retagging items to satisfy a family.

The full runner now includes allfive author synthesis scripts,assembler and structural check:258commands/run,34negativefixtures. A new double rebuild is starting;see `checks/r5/T5-first-five-blocks-double-rebuild.log`. Until its completion,the last full PASS remains the archived C13source-page proof (251commands/run,134identical outputs,31negativefixtures),which predates these T5/audit changes. Do not mutate synthesis inputs or generated analysis while a full run is active.

Protected checks at this checkpoint:both textbook PDFhashes,19review files,HEAD and both frozenR4snapshot copies unchanged. Snapshot remainsR4until finalT6. Nothing committed or pushed.

## Continue

1. Verify/finish the new double rebuild and archive its proof. Current partial T5proof is `analysis/history/r5-T5-functions-vectors-checkpoint.json`.
2. Finish the remaining family/insight blocks: circular measure/basic and advanced trigonometry; logarithms/exponentials; differentiation; integration; numerical methods; retained identity/complex-chapter facets. Alloriginal source pages/keys have already been visually read and item records populated. Use fixed source inputs,answer records and `analysis/textbook-insight-working-notes-r5.md`; reread renders for ambiguity. Do not auto-cluster by topic or blindly inherit item demands onto each subpart.
3. Complete whole-book metadata,actual-value qualifier,prose,representation/response and exam-style audits; record every correction in canonical source-author inputs and audit ledger. A worked method does not automatically become directly assessed.
4. After all T1–T5complete,perform fresh-copy deterministic double rebuild,all34+negativefixtures,final snapshot and T6author-complete declaration. Do not claim completion from page counts alone.
5. Prepare cross-vendor handoff only then. Claude draws its own fresh blind sample(atleast10%,own seed). No author sample. Step3waits for independent acceptance.

## Constraints

No commit/push;Vitalis commits. No PLAN,recipe contract,recipes,runtime generators,work orders,imports,publication or assignment. Do not modify review folders,source PDFs/root textbook,standard/,other subjects,app or pinned checkouts. Preserve unrelated work. Acquisition only through YYeni Web Harvester;no new scraping scripts. No delegation authorised. Save verified checkpoints at batches/pauses;the page pass is already fully saved. Earlier handover histories remain under analysis/history/.


## Work prepared while the five-block rebuild runs

Active full double rebuild session48805,log `checks/r5/T5-first-five-blocks-double-rebuild.log`;leave its inputs/generated analysis unchanged. Two new UNWIRED author drafts are saved only as Python source: `tools/textbook-r5/author_textbook_synthesis_logs_r5.py` (21families/194sourceitems/four8-demand insights) and `author_textbook_synthesis_power_diff_r5.py` (30families/136YM C6items/four10-demand insights). They have been source-record/label screened without emitting synthesis JSON. They are NOT included in the current771item/65demand counters or active full proof. After the full run ends,emit them,assemble/check and fix any source-evidence discrepancy before updating counts or runner. No additional source pages remain to census.


## Rebuild discrepancy under investigation — latest,21 November

The five-block double rebuild48805FINISHED WITH A NONDETERMINISM FAILURE,not a pass. Three differing outputs: `analysis/textbook-answer-verification-r5.json`,`analysis/textbook-inventory.json`,`checks/r5/integration-independent-checks.json`. Both assemblies completed their individual checks;byte comparison failed before negative-fixture stage. The last accepted full proof remains archivedC13,not thisrun. Fullfailurelog ispreserved.

Read-only two-seed primitive scans are running in execsessions78915(seed0),14512(seed1),using `checks/r5/diagnose_primitive_seed_drift.py`. Outputs will be `checks/r5/primitive-seed-0.json`and`primitive-seed-1.json`;these scripts do not writeanalysis. Inspectthe differences,prove any mathematical equivalence andfix the deterministicrepresentation choice in canonicalinputs;do not merelyhide differinghashes or change theexpectedanswer. Current repeated oldone-case stabilityguarddidnotcatchthisadditionalcase.

Two further UNWIRED/UNEMITTED drafts now exist: `author_textbook_synthesis_elementary_diff_r5.py`(9families/two4-demandinsights) and `author_textbook_synthesis_implicit_param_r5.py`(19families/eightfamilyextensions/two3-demandinsights). RawIDs/labels/demandscreenpassedapartfromfourpendingresponses:Goldie4A2(i),4C6(i),4E8(iii),YMC11Try16(d). Firsttwoarederivativesforquotient/productfamilies,lastislnrationalcomposite. Goldie4E8(iii)isexplicitlyOUTSIDE LIMIT02(unboundedgeneraltrig);recordapart-levelscopeexclusion ratherthanforceitinto anin-scopefamily. These draftcountsare NOTthe currentgenerated771/65counts.
