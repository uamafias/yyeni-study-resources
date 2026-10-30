# Final-resource review — NSSCO Geography 6137

Reviewer: Codex. 30 October 2026. Owner: Vitalis P Haupindi.

**Verdict:** accept the two new maps and re-accept the town-plan resource. The two tourism resources are repaired but await Claude's independent check of Codex's changes. Whole-subject acceptance is deliberately absent. Nothing was published, committed, pushed, uploaded or imported.

## Resource decisions

| Resource | Decision | Evidence |
|---|---|---|
| VIS-6137-2.2-02 | Accept | Question and four answer variants, all four bound cards/rubrics, teaching block BL-6137-2.2.04-01 and new claim independently read. Central cattle/southern small-stock pattern corroborated against raw farming polygons intersected with regions. Inset explicitly schematic. |
| VIS-6137-2.6-02 | Accept | Both images, card/rubric, BL-6137-2.6.01-09 and new claim independently read. Etosha/Torra/Salambala areas recomputed using an independent equal-area transform; registration attributes checked. CCF farm point is about 40 km east of Otjiwarongo, not an asserted surveyed building position. |
| VIS-6137-3.3-02 | Re-accept | Image bytes unchanged; all seven bound cards read. The new description correctly says schematic and not to scale. BL-6137-3.3.04-14 unchanged and consistent. |
| VIS-6137-2.3-01 | Return repaired for cross-check | P04 numerical solution correct, but “Facilities clean / Facilities broken” mixed cleanliness and condition. Codex changed the negative endpoint to “Facilities dirty” and regenerated. No self-acceptance. |
| VIS-6137-2.3-02 | Return repaired for cross-check | P05 numbers and images correct. Rubric incorrectly treated distance as a proxy for years of use. Codex repaired answer/rubric: present path form is compared with distance; neither visitor use nor change over time was measured. No self-acceptance. |

All current question sheets were inspected at full resolution, 390 px width and greyscale; all map answer variants and both practical answers were inspected. The corrected P04 answer was inspected again after rendering. Small map labels require zoom on a phone. Crop density, livestock types and conservancy symbols remain distinguishable in greyscale. Question sides withhold the missing values, graph points and requested explanations. Base 036/038 and P07 PNGs remain byte-identical to the input manifest.

## Sources and map qualifications

The NSA/HDX gbHumanitarian substitution is appropriate: the actual file has 14 regions including Kavango East/West and Zambezi; the rejected gbOpen file actually has 13 historical regions. The metadata's “2011” year conflicts with the later region names, so it is not evidence that this geometry represents administrative conditions in 2011. [geoBoundaries metadata](https://www.geoboundaries.org/api/current/gbHumanitarian/NAM/ADM1/).

The Atlas download page explicitly offers the book's maps and underlying datasets alongside its CC BY 4.0 attribution guidance. The original thematic maps use these downloadable vectors, not traced examination maps. Historical farming-system data (2006), an undated national cleared-land layer and irrigation locations are labelled as such; no current operation or farm-level purpose is inferred. [Atlas downloads and attribution](https://atlasofnamibia.online/prelim-pages/download-files), [farming](https://atlasofnamibia.online/chapter-8/farming), [source notes](https://atlasofnamibia.online/end-pages/notes-and-references).

The conservancy shapefile has 89 records but only 87 distinct names: =/=Gaingu and Doro !nawas repeat. Thus “89 records” is a dataset description, not a defensible national count or evidence of a decline to the 86 gazetted conservancies reported by the Atlas. No learner question or answer teaches 89 as a national total; the dated generalised layer is suitable for the named-location task. [Atlas conservation](https://atlasofnamibia.online/chapter-8/conservation).

The maps are generalised location stimuli, not precision survey sheets. Their equirectangular scale is true north–south and approximate east–west; the printed 5% wording is rounded (the southern extremity approaches 5.7%). Do not repurpose them for precise measured-distance tariffs. CCF's farm position supports the approximate location only. [CCF research with farm coordinates](https://cheetah.org/wp-content/uploads/2021/11/cpab009.pdf).

New claims CL-6137-2.2.04-R1 and CL-6137-2.6.01-R1 are accepted for their stated generalised map readings. Canonical claim verification flags are retained in the form required by the repository checks; this report and its receipt hold the independent verdict.

## Claude's cross-check of the earlier text repairs

F01: Claude correctly rejected my “45% of electricity produced in Namibia” wording. That was my error. The Atlas introductory wording is ambiguous and conflicts with its explicit energy chapter, so restoring the bare 45% does not settle the denominator. Codex now uses the unambiguous dated figure: Ruacana supplied 26% of all electricity used in Namibia in 2018/19. CL-6137-2.4.04-R1 is revision 4; teaching block and card 2.4-025 are consistent. [Atlas energy chapter](https://atlasofnamibia.online/chapter-10/energy).

F04/F05: “Neighbouring suppliers” is correct. However, the 51.6% statistic is for **December 2025**, not the whole calendar year. NSA's primary monthly report states local supply of 213,957 MWh and imports of 201,024 MWh. Codex corrected the claim and teaching block to the monthly period; CL-6137-2.4.10-R1 is revision 3. [NSA Electricity December 2025, PDF page 2](https://nsa.org.na/wp-content/uploads/2026/02/Electricity_December-2025.pdf).

F02/F03 and F06–F11 accepted: restored place-based HIV explanation retains the causal caution; screen material/height agrees with its teaching text; the unsupported religious percentage and Red Line dates are gone; aquifers are named in the answer; the rubric typo and town-plan description are repaired. The new electricity revisions were propagated to every citer. No other Claude repair was reverted.

## Verification and remaining work

- Independent final-resource checker: **328 checks pass** (asset hashes, PNG decoding, region names, named areas/registration, CCF location, practical arithmetic and unchanged sibling images). Receipt: `codex-final-resource-independent-checks-6137.json`.
- All 18 topic reports: **40 PASS, 0 FAIL, C-18 WARN, C-35/C-41/C-43 NOT_RUN**. The runner exits 1 even for a publish decision because it tests for the obsolete string `pass`; decisions and individual results were read directly. No shared tool was edited.
- Full authored audit: **DRAFTS_RECONCILE**, all **801** planned items retained. All 160 sections within budget. No slot, label, contract or work order changed.
- Copied-wording check: **0 runs of 8+ words** against 35 assessment extracts.
- Plan amendment verifier passes; its static closing phrase “Assets not yet authored or accepted” is historical boilerplate, not current asset state.

Exact before/after objects: `codex-final-resource-repairs-6137.json`. Source input manifest: `codex-final-resources-input-manifest-6137.json`. Current resource acceptances: `codex-final-resource-acceptance-6137.json` and the asset manifest.

Claude must cross-check the four Codex repairs, report exact hashes, and return the two tourism resources for Codex acceptance. After both acceptances are current, Claude records the final whole-subject verdict against the final `snapshot()` and manifest hash. Do not rerun either one-time repair script or the original authoring generators.
