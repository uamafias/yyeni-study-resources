# Repair round 5 — NSSCAS Mathematics 8227

AUTHOR Codex; owner Vitalis.21November2026. **T1–T6 author complete; ready for Claude’s independent check.** Independent review has not accepted either textbook. Step3continues to wait.

## Review repairs

| Finding | What changed | File and executable evidence |
|---|---|---|
|R4-01|Eight marking-row corrections,each re-read atscale4or greater;false source-print claims removed.|analysis/award-repairs-r5.json;checks/r5/award-*;check_repair_r5.py --stage part1|
|R4-02|42printed Erows retain establishment flags;self-alternatives removed;part marking statuses regenerated;small row/report-defect corrections retained.|marking-conventions.json;award-audit-reconciliation-r5.json;question-analysis.json;check_repair_r5.py and seeded negatives|
|R4-03|Five requested provenance pairs added/corrected;changed fields,duplicate and wording-only dispositions repaired;full local rare-phrase/value screen and158rendered candidate readings.|nsscas-cambridge-provenance.json;provenance-full-screen-r5.json;provenance-reading-r5.json;check_repair_r5.py --stage part1|
|R4-04 / R3-08|Both textbook populations,individual mapping,actual-value rules,all response checks,families and per-demand insights completed by the author.|textbook-page-census.json;textbook-inventory.json;textbook-answer-verification-r5.json;textbook-families.json;textbook-insights.md;textbook-completion-audit-r5.json/.md|
|R4-05|Convention076covers calculators that differentiate,integrate or solve cubics while explicit B,SCandFTawards retain authority.|tools/convention_inputs.py;marking-conventions.json;Part1checks|
|Owner decision17November|Step3waits for BOTH textbooks complete AND independently accepted;original textbook questions remain internal.|CurrentSTATUS/HANDOVER;everyitem learner_display:false;no PLAN/recipe/assignment|

Part1preserves119NSSCASquestions,250parts,821award rows(818official,3derived completions),42Eflags and95convention rules. Provenance:31confirmed pairs on29NSSCASquestions;3structural comparisons,1hidden wording-only hypothesis and1folded duplicate.119questions were compared with3208local pages;158above-threshold candidate pages were visually read. A missing match is not evidence of originality.

## Textbook completion

|Stage|Before this repair|Current author evidence|Remaining boundary|
|---|---|---|---|
|T1census|R4reported759target pages,not an exhaustive per-page/item/figure census.|891agreed source-envelope pages;all3940records linked;one duplicate scan excluded;48pages explicitly screened without retained item starts.|Independent page resampling. The changed envelope is not a like-for-like page-growth claim.|
|T2records|1933catalogued items;about448shared notes;range-seeded mapping disagreements.|3940individual records:2182nonfigure plus1758figures;no sibling-shared notes;direct/component roles disjoint;everyexam_styleflag has a source basis.|Independent classification,including62implicit/parametric and101log-boundary records exposed by the final audit.|
|T3actual values|Systematic actual-value screening incomplete.|Allgoverned direct demands carry applicableQUAL01–11records;425applications checked.108missing annotations explicitly supplied,including27rotation axes.|Reviewer rechecks actual values;source ambiguities/exclusions remain binding.|
|T4answers|49recorded mathematical recomputations;full subpart audit incomplete.|5752responses across2181items;exact answer-page or explicit absence;all discovered investigations/subtasks/visuals retain checks.|Independent recomputation;author checks do not certify acceptance.|
|T5families/insights|No final cross-book family/138-demand synthesis.|380analysis families;2177eligible items resolved;5whole-item and3part exclusions;zero pending responses.58insightsections cover138/138demands.|Reviewer validates decisions,source claims and splits;families are not approved recipes.|
|T6 handoff|No author completion declaration or final fresh-copy proof.|All 3940 items author-complete; awaiting independent check. Fresh copy passed 273 commands twice, 141 byte-identical outputs and 38 expected seeded failures; copied outputs matched the author checkout.|Independent acceptance remains pending; final snapshot freezes this handoff.|

|Answer status|Count|
|---|---:|
|matches|4735|
|sketch|336|
|show/prove|460|
|key wrong|111|
|no key|46|
|key incomplete|64|

268registered defect/caution entries include precision,labels,scope and source-method caveats;they are not268wrong answers. The one nonfigure item without an answer population is wholly excluded Goldie general-solutionActivity3. Three named excluded parts are separate from family coverage. Radian interpretation has two teaching figures but no separately posed textbook task;that practice gap stays visible.

## Final audit corrections

Seeanalysis/textbook-synthesis-audit-r5.md,001–015. The final pass correctsGoldie6B5/6unsupplied-map decisions,explicitly records rotation axes/inverse branches/simple limits,retains20visual-role/status exceptions,and removes accidental non-area membership ofYMExercise12Q4. Thex^xlogarithmic-differentiation exception is source-enforced and recorded;ordinary explicit derivatives cannot inherit implicit/parametric geometry labels.

A failed earlyT5double rebuild is preserved atchecks/r5/T5-first-five-blocks-double-rebuild.log. Sixhash-seed scans isolated an additive-constantCASprimitive representation drift forYMC12Example24(a). A fixed independent manual integration algorithm and fresh-process guards resolve it;no answer status changed. Subsequent nine-block proof passed262commands per run,139byte-identical outputs and35negative fixtures. That proof predates the final changes and is not represented as final evidence.

## Reproduction and acceptance

The final runner includes all17synthesis author scripts,independent math checks,final inventory promotion and whole-population audits. Three new seeded completion errors cover missing volume axis,explicit-as-implicit misclassification and unresolved family responses;all fail for their stated reason. Final proof passed: **38 negative fixtures rejected**, 273 commands per run, 141 byte-identical outputs and matching author-checkout results. All 436 source files were hash-checked. See `fresh-copy-verification-r5.json` and `analysis/history/rebuild-verification-r5-final-fresh-copy.json`; final log `checks/r5/final-accepted-inputs-fresh-copy.log`. The R5 snapshot freezes these records.

Neither textbook is independently accepted. No author-selected review sample is prepared. Claude draws a fresh blind sample of at least10percent and rechecks pages,mapping,qualifiers,answers and family/insight claims. After acceptance,step3may begin. No app/website/production testing is claimed. No commit,push,import or assignment.

## Author completion declaration

**Textbook population complete; ready for Claude’s independent check.** See `analysis/textbook-author-completion-r5.json/.md`. Both books remain independently unaccepted. Final comparison audit016 gives219structural examination comparisons and161textbook-only groups; no branch-level same-type approval is inferred. The full reproducibility proof is in an isolated copy on this host, not another-OS or educational acceptance. Current HANDOVER and STATUS supersede all historical checkpoints. Nothing was committed or pushed.
