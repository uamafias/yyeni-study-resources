# Repair round 2 report — NSSCAS Mathematics 8227 steps 1–3

16 November 2026. Author: Codex. Commissioned by Vitalis, final decision-maker.
Status: **author repair awaiting cross-vendor re-review**. The first independent
verdict remains **repair analysis** until re-review changes it. “Repaired” below
means author implementation and checks, not independent closure or owner acceptance.
No PLAN, work orders, recipes, runtime generators, imports or assignments created.
No commit/push. Original review folder and source PDFs preserved.

Two complete rebuilds produced 83 byte-identical assembled outputs. Both seeded
negative fixtures failed (ordered tariff and label alignment), with all assembled
output hashes unchanged after failure. The derivative verifier reproduced all 16
layout JSON files byte-for-byte from 1,945 PDF pages and checked 663 OCR hashes.
These are author checks. Reviewer scratchpad scripts were not supplied; the
recorded scan methods are re-run using the frozen tools here, against the same
source PDFs/text layer. This is not another independent review.

Read `analysis/analysis-snapshot.json` for the frozen current files/environment,
`checks/rebuild-verification.json` for deterministic/negative checks and
`checks/reviewer-scan-reconciliation.json` for rerun scans/recomputations. The R1
snapshot was copied before repair to `analysis/history/analysis-snapshot-r1.json`:
SHA256 `1afe99d597617897cb3bf0489cd3bcbc236624fef05cef53a8aa4a92704a561f`.

| Measure | Round1 / review baseline | Round2 author record |
|---|---|---|
| Specific objectives / demand IDs | 60 /138 | 60 /138 retained; normalized mathematics and missing qualifiers added |
| NSSCAS questions / parts / marks |119 /250 /750 |119 /250 /750; ordered tariffs and labels checked, IDs preserved |
| Direct part→demand links |0 explicit |250 parts linked;564 links including explicitly separate prior/model links |
| Dependency edges |49, missing18 questions |76 typed edges; all 18 reviewed questions checked; within-part “hence” cues separately resolved |
| Questions with award excerpts |22 linked;24 actually present |24 linked and scanned:2021P2 Q1–4,2023P2 Q1–9,2024P2 Q1–11 |
| Coverage |Family-primary-objective proxy |Only usable directly assessed part→demand edges; prior/context/families excluded |
| Evidence status of138 demands |Boilerplate/unreliable |126 NSSCAS-observed;8 comparable Cambridge-observed;4 syllabus-derived |
| Zero usable NSSCAS demands |Review gives eight examples, not exhaustive |12 exact IDs plus inflexion as an unobserved facet of a compound demand |
| Analysis groupings |62 provisional families |67 restructured groups/modules; neither number is an approved recipe count |
| Grade evidence |Not used |46 statements:15a,16c,15e; MF9 kept as support only |
| Per-part representations / responses |Incomplete |All250 annotated;11 sketches and2 sketch-dependent parts included |
| Durable source visual crops |0 |26 NSSCAS givens +6 response frames +7 Cambridge diagrams |
| Verified Cambridge selections |0 |30 selected originals /41 assessed parts /115 source marks;50/138 demands gain evidence (36.23%); seven diagram items |
| Local Cambridge discovery |Owner's initial candidates |415 paths/402 hashes/400 logical keys indexed, real PDF bytes; no acquisitions this round |
| Textbook samples / OCR |17 /663 pages;572 heading-lead pages |19 /663;572 heading leads; no exhaustive exercise/answer claim |
| Layout-text derivatives |Unfrozen, no generator |16 files /1,945 pages recomputed from PDFs;663 OCR identities/hashes checked |

Counts of8 comparable-only demands and4 syllabus-only demands are evidence
statuses, not assertions that all variation or standalone recipes are ready.
Conceptual demand facets with no direct evidence remain visible. Domain/range
answers, a required one-to-one condition and inversion of ln(x-2) are credited
interpretations of the broader syllabus terms, with direct links and rationales.
They are not incorrectly declared absent for lacking a definition-only question. The AP/GP donation model in2021
P1Q8 now directly links recognition as well as calculation; this accounts for
the AP gap removed during the author checking loop; the three source-checked
conceptual interpretation links remove three further overstated gaps.

## Finding-by-finding disposition

Paths below are relative to this Workbench folder unless beginning `../curriculum/`.
Common executable checks are `tools/check_repair_r2.py`, `run_repair_checks.py` and
`verify_derivatives.py`; their saved results identify exactly what was checked.

| Finding | Author change / disposition | File(s) | Check / remaining limit |
|---|---|---|---|
| R13-01 |Repaired: coverage no longer consumes families; direct/other assessed objectives retained |`tools/demand_coverage.py`, `analysis/question-analysis.json`, `coverage-matrix.json` |Independent dictionary recomputation equals all 138 rows; coverage function accepts no family argument/import |
| R13-02 |Repaired: all 250 direct-demand annotations and all 138 reasoned dispositions/statuses; gap reconciliation |`tools/repair_inputs.py`, `analysis/demand-dispositions.json`, `gap-demand-reconciliation.json` |Every part has valid direct links;126/8/4 statuses; exact12 gaps/facet and Cambridge search outcomes recorded |
| R13-03 |Repaired18 questions plus implicit reuse; typed cue/F.T. edges and scan/manual provenance |`tools/build_mapping.py`, `analysis/part-source-scan.json`, `question-analysis.json` |Required18-question edge table and absence of unadjudicated cue hits checked; two within-part modelling cues do not create false inter-part edges |
| R13-04 |Owner1 applied: hold2023P1Q9; standard principal range; separate Cambridge support |`analysis/source-defects.json`, part record, `cambridge-evidence.json` |Inverse-sine range recomputation; no usable NSSCAS link from held part |
| R13-05 |Owner3 applied: hold2023P1Q1(b); require nonzero leading coefficient in future proof branches |`analysis/source-defects.json`, root-proof group |Symbolic discriminant and p=2 linear case recomputed; held exemplar excluded |
| R13-06 |Owner2 applied: reject degree-mode alternative; radians required |`analysis/source-defects.json`, reportPDF338 locator |Eight radian/degree iterates and equation residuals recomputed; source anomaly disclosed |
| R13-07 |Repaired missing2021P2Q2/Q4 links; census24 |`analysis/award-source-scan.json`, question records |Report-heading/award-token scan and expected24-question set; Q4 features use actual PDF238 |
| R13-08 |Repaired direct mappings and grouping mis-tags, including model-only and prior techniques |`tools/repair_inputs.py`, `build_mapping.py`, question records |Every direct ID checked; affected question data available for re-review; prior/model IDs cannot inflate138-demand coverage |
| R13-09 |Repaired: discriminating decisions; §4 merges/splits/retentions; seven-column table |`tools/family_inputs.py`, `build_families.py`, `analysis/problem-patterns.json`, `selection-table.md` |67 groups with evidence/decisions; explicit departure for2025P2Q7(b) identity-extrema rather than R-form; recipe economy remains re-review work |
| R13-10 |Superseded by owner6: all visual demands include, no capability holds |part records, `capability-gaps.md` |All11 sketch and2 dependent parts include; graph consistency distinguished from literal F.T. |
| R13-11 |Repaired:46 grade statements and family calibration; MF9 not scope |`../curriculum/grade-descriptions.json`, family bounds, syllabus-page evidence |46 source-linked statements; all families have floor/ceiling IDs. Division/linearisation have explicit e/c prerequisite-scaffold floors because full demand is named only at a; no invented c descriptor |
| R13-12 |Repaired: missing qualifiers/limits, keeping LIMIT01–08 |`../curriculum/syllabus-exclusions.json`, `tools/build_curriculum.py` |Objective-linked QUAL01–11 and normalized source text; limits not inferred from sampled absence |
| R13-13 |Repaired: static author transcriptions/normalized mathematics, checked on renderedpp8–16; independent literal check |`tools/syllabus_author_transcriptions.json`, objective registry |60 literal source-page matches; changed quotes must match actual PDF, not self-generated search; normalized math remains human-reviewed evidence |
| R13-14 |Recorded2024P2Q5(a) polynomial-name typo |`analysis/source-defects.json` |Exact question/source locator and correction record; original PDF untouched |
| R13-15 |Corrected2021P1Q6 to external division |question summary and source-defect register |P=(0,6,0), AP·OB=0 and point beyond B recomputed |
| R13-16 |Resolved textbookPDF550 Q2(c)→integral(b); under-estimate; convention conflicts recorded |`analysis/source-defects.json`, `textbook-samples.json` |Stationary point, trapezium and exact integral recomputed; PDF550/560 and175 advice compared with official graph/trapezium guidance |
| R13-17 |Repaired: full ordered tariff/label checks, derived award pages/cues, seeded failures |`tools/build_mapping.py`, `run_repair_checks.py` |Ten paper sequences/250 labels; both seeded fixtures must fail without output changes |
| R13-18 |Repaired: every part representation/response;26 given diagrams +6 frames cropped from renders |`analysis/assets/`, `asset-index.json`, `tools/visual_inputs.py` |Crops have source/page/box/hash; author crop inspection; same-value geometry/label constraints recorded; independent visual re-review pending |
| R13-19 |Repaired per-year/paper formula, precision, angle, calculator/working conditions |`../curriculum/assessment-conditions.json` |Ten cover/formula records; reduced list from2023; supplied formulas do not extend scope |
| R13-20 |Repaired cross-paper theme note and counts from direct objectives |assessment conditions, `analysis/corpus-analysis.md` |Current primary/any-direct counts saved; historical reviewer27-mark primary count retained as historical, not enforced against repaired mappings |
| R13-21 |Repaired prerequisite roles and separate assessed prior/model demands |per-part prerequisite records, demand registry |Role fields required; prerequisites never create coverage; no blanket identical prior-role assignment |
| R13-22 |Partially repaired: bounded12 excerpts. **Deferred** systematic answer-format/method-rule mining |`tools/build_source_addenda.py`, `analysis/examiner-difficulties.json` |12 cited anchors retained; paragraph/next-question boundaries replace700-character bleed. A full independently checked convention register is not claimed; needed before criterion authoring |
| R13-23 |Partially repaired:19 samples; missed sections, PDF50 Q3/Q5 and TB08 fixed; completion method recorded. **Deferred** full item population/answer-key classification |`textbook-samples.json`, `textbook-completion-method.md` |Rendered141/175 and50 inspected; stop rule and exhaustive visual/exam-style/gap populations specified, not falsely claimed performed |
| R13-24 |Partially repaired: frozen source-register inputs, pinned dependencies, all derivatives/hashes; manifest-backed regeneration/verification script. **Deferred** historical OCR environment recovery/shared resume hardening |`tools/source_holdings_inputs.json`, `requirements-analysis.txt`, `verify_derivatives.py`, current snapshot |16/1,945 layout pages recomputed;663 OCR hashes. Original OCR macOS build/per-page settings unavailable; no retroactive proof invented or shared tool changed |
| R13-25 |Repaired mirror provenance |`analysis/source-holdings.json`, `source-inventory.md` |SRC018–020 explicitly third-party mirror, DNEA cover verified, official-copy equivalence unverified |
| R13-26 |Owner5 settles storage/sharing. Root refiling **deferred** under no-source-change constraint |source register, acquisition gaps, STATUS |Both books/OCR accepted in shared repo; no new public textbook reuse licence inferred; original paths/hashes preserved |
| R13-27 |Repaired dated evidence/acknowledgement/disposition fields and dirty-app-state limitation |`capability-gaps.md`, `framework-extension-handoff.md` |Owner6 announcement for17Nov separated from16Nov source/author checks; app runtime/MCP remain untested |
| R13-28 |Subject-local extension examples recorded. **Deferred** adoption into common versioned schema/app |`analysis/framework-extension-handoff.md` |Six reviewer proposals plus references/visual fields mapped to existing framework; no competing framework or standard/app writes |
| R13-29 |Repaired builder hardening and environment evidence |tools, `checks/reviewer-scan-reconciliation.json`, `rebuild-verification.json` |Cue/award/demand-presence scans, ordered tariffs/labels, negatives and deterministic double rebuild; full environment in snapshot |

## Binding owner decisions and extensions

| Decision/request | Applied state / locator | Acceptance evidence and boundary |
|---|---|---|
|0 Authority |Vitalis final; STATUS/HANDOVER and all owner records |No routing to Jeremy or another approver; cross-vendor re-review is the commissioned next activity |
|1 Principal-value defect |Hold original2023P1Q9; source-defect/principal family |Syllabus authority preserved; valid Cambridge observations labelled comparable, never NSSCAS |
|2 Degree-mode alternative |Rejected; radians required; reportPDF338 anomaly |Independent iterates/residuals recorded |
|3 Degenerate proof |Original2023P1Q1(b) held; a≠0 boundary |Symbolic/linear case recomputation |
|4 Grade bounds |46 statements; per-family floor/ceiling evidence; MF9 support |Two explicit prerequisite-floor exceptions remain for reviewer scrutiny; no numerical-hardness proxy |
|5 Commercial PDFs/OCR |Shared repository storage accepted |Source bytes untouched; minor root refiling deferred |
|6 Visual capability/include |All11+2 parts and supplied diagrams include |Per-part givens, variable/fixed constraints, source crops and credited sketch features; app announcement is not runtime test evidence |
|N1 Examination references |Every part, family and selected Cambridge item has references or family syllabus-derived reason |Board/session/component/part/printed+PDF page/hash/relation/author verification and generated labels checked; family union exact; same-type only exact demand/response match; related internal; held exemplars excluded |
|N2 Cambridge |30 checked originals + matching schemes + scope/attribution from existing local corpus |Gap-first searches for all 12 current gaps and inflexion facet; seven diagrams;50/138 demands have comparable links. At least3 examples for principal/unit/segment/monotonicity/quadratic-division/tangency gaps; one each for quadratic sketch and angle conversion; inverse-interpretation adds variety. Four gaps and inflexion remain without a verified item; not a universal absence claim. Wider diagram/thin-demand expansion remains non-exhaustive |
|N3 Other subjects |Direction retained; **deferred**, expressly outside this repair |No other subject changes; later Physics pilot must test transfer |

## Differences from the review's scans

- Part/mark census is unchanged. Award count22→24 is the reported correction.
  Family groupings62→67 reflect decision-based restructuring, not content quantity.
- Exact12 gaps are derived from part edges. Review's eight examples included
  inflexion, which remains a facet inside an observed compound demand. The held
  principal-value source cannot establish usable NSSCAS observation. The identity/equation
  distinction, standalone quadratic sketch, radian meaning/conversion and tangency
  remain explicit; broader function/log interpretations are mapped to actual outputs. AP recognition
  is directly observed in the donation model. No family tag silently fills a gap.
- Principal-value demand is syllabus-authorised, with comparable Cambridge
  evidence; its one evidence status becomes comparable when those items are linked.
  This reconciles owner1 with the mutually exclusive three-status requirement.
- 2023P2Q6(d) says “Must be correct from their graph”; it does not literally say
  F.T. It is recorded as a graph-consistency cue, while2024 formal F.T. rows have
  distinct edges. The mathematical expectation is retained.
- Reviewer candidate9709_w21_qp_22 PDF9 is Q6(c), not Q9(c). It concerns conditional
  convergence to the equation's root, not recognising iteration failure. It is
  retained as variety, and does not close that gap.
- All eight scripted mathematical sampling cases were recomputed. The converged
  radian-root residual is1; the review's0.999998 uses the displayed rounded iterate.
  Other displayed numerical differences are rounding only. No degree alternative
  is adopted. Full author results and baseline values sit side by side in the scan
  reconciliation JSON.
- Cross-paper primary counts change from11 parts/27 marks to13 parts/35 marks
  for Mathematics1 on Paper2:2021P2Q11(b) and2022P2Q2 now name quadratic
  substitution/recovery as primary, with exponential solving retained as directly
  assessed secondary content. Paper1 changes from1 part/1 mark primarily
  Mathematics2 to0:2025P1Q4(c) now names Mathematics1 graph intersections.
  Any-direct measures are47 Paper2 parts with Mathematics1 and5 Paper1 parts
  with Mathematics2; these overlapping links are not objective-specific marks.
- The review's35-file snapshot describes R1. Current permitted author files are
  expected to change; R1 historical bytes and all20 original source hashes are
  checked separately. Current snapshot also freezes raw derivatives and assets.

The re-review should inspect mathematical and educational judgements independently,
especially direct-versus-prerequisite roles, compound-demand facets, group economy,
verbatim transcriptions, source-diagram crops and grade-floor exceptions. Structural
passes do not close those review questions. After re-review, the next authorised
scope can address deferred analysis and planning; nothing is silently promoted into
an accepted recipe bank or production-ready application feature.
