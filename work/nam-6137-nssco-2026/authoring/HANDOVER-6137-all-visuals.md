# Claude visual handover — all 54 NSSCO Geography 6137 resource sets

Owner Vitalis P Haupindi. Workspace `work/nam-6137-nssco-2026/`. Role: visual AUTHOR. The approved plan is committed; the complete text draft is local and uncommitted. This supersedes the earlier first-six handover. Read AGENTS.md, TEAM-PLAYBOOK.md, only AUTHOR.md, the subject HANDOVER and PLAN. Read the actual saved work order, claims, notes and items for each topic before working on its visuals. No need to author remaining text slots: all 801 are filled, including six explicitly provisional photo answers.

## Your job and boundaries

Create all 54 approved resource sets (48 generated resources, six real licensed photographs), strictly ONE resource at a time in the order below. Continue through the whole approved batch without asking Vitalis to approve each image. Stop only for a genuine unapproved scope change; continue independent approved resources while that decision is pending. Do not spawn parallel visual authors. Do not edit standard/, another subject, curriculum, contracts, work orders or planning files. Do not publish, commit, push, upload or import. No cloud URLs or invented YYeni asset IDs.

`planning/visual-resource-plan-6137.json` is the authoritative list of exact targets and question/answer/master/spec paths. `authoring/visual-authoring-index-6137.json` collects all 54 targets, draft prompts/answers/rubrics, notes paths, recorded reuses, practical stimulus requirements and the two unapproved map concerns. Read source files again: the index becomes stale after edits. Do not rerun any author_*.py script: it would overwrite your work.

## One-resource procedure

1. Read the card, full notes section and related claims. Specify data, geometry, units, scale, orientation, key, intended physical size and the evidence needed to answer. Independently solve the task before drawing. Explain assumptions in the internal specification.
2. Generate the original geometry using code (SVG/vector, plotting or mapping software as appropriate). Geography includes process diagrams, plan views, thematic maps and photographs; many resources are not Cartesian graphs. Do not trace examination figures or use an AI illustration as evidence of a real photographed scene.
3. Render a question PNG and an annotated answer PNG from the same underlying data/geometry. The question must supply the evidence needed without printing the answer, classification or missing labels being tested. Preserve editable masters, code and machine-readable data specifications at planned paths.
4. Inspect both images at full size, phone width and greyscale. Independently recalculate quantities; read every arrow, label, unit, scale and key. Inspect the card wording, answer, rubric and notes too: geometry tests cannot detect semantic errors. Record the result and SHA-256 hashes in a per-resource checklist before starting the next resource.
5. Link actual question and answer images into their respective card fields and worked teaching notes. Use Markdown image links relative to the source JSON directory (`topics/T/learning-items/`) or notes directory respectively. Record all reuses/variants as exact item-ID bindings; no ambiguous matching by title. Restamp changed items/blocks. Change claim revisions only when the proposition changes and propagate affected dependencies. Keep claims unverified/non-publishable pending independent review.
6. Mark assets self-reviewed and awaiting Codex acceptance. Never write a Codex acceptance record yourself. Run render_notes.py and checks for each changed topic; inspect qa_report.json rather than relying on run_checks.py's known exit-code bug. Preserve C-18 WARN and C-35/C-41/C-43 NOT_RUN.

## Specific requirements and traps

- First six: retain the detailed economics-free process/geometry instructions in `authoring/HANDOVER-6137-first-six-visuals.md`, but ignore its old statement that later text does not exist. A conservative plate margin is a plan view, with motion parallel to the fault; subduction melting is not blanket friction melting. Freeze-thaw, exfoliation and carbonation have distinct material/sequence evidence.
- River profiles: consistently distinguish downstream position, bed elevation and slope; do not infer every local landform from a smooth idealised profile. Longshore drift: oblique swash, gravity-driven downslope backwash, coherent net sediment direction. Dune plan views must support the stated long-term wind regime rather than one present arrow.
- Weather: source-derived instrument geometry; weather elements retain their own units and recording periods. Climate graphs use twelve consistent months and separate rainfall/temperature axes. Distinguish synoptic observation from a forecast.
- All twelve 30-mark investigations: four in 1.5, four in 2.3, four in 4.1. Read every `performance_parts.assets_required` entry. Supply record sheets, source data and genuinely blank/incomplete axes where learners must Complete/Plot; do not show the worked plot in the question image. Preserve each package's A6/B6/C6/D12 split. Add exact bindings for every required variant/reuse, not merely the originally assigned procedure card. A multi-panel resource may contain variants, but each must have its own indexed path and hash.
- Tourism EQ score: higher means better in 2.3; pollution scores in 4.1 P07 run the other way. Keep labels explicit. Non-monotonic path widths do not support an every-step increase. Missing drift pebbles are not stationary observations; the mean is for recovered pieces only.
- Population: the age-sex pyramids require equal five-year bands with a separately labelled 80+ open band. Topic 3.1 notes give the full paired A/B sex counts; resource 01 is reused by card035. Keep common scales and proportional bars. Do not substitute unequal-width broad age groups. DTM uses birth/death rates, not population totals.
- HIV chart: preserve the exact dated NAMPHIA2017 population ages15–64, regional percentages and confidence intervals in topics/3.2/authoring_notes.json; no current-prevalence claim. Recheck the original primary PDF cited there.
- Settlement: complete the nine documented reuses of rural/urban panels; stylised MEDC/LEDC models are not measured Windhoek maps.
- Map Reading: follow `topics/4.2/authoring_notes.json.map_geometry`, then independently verify every dependent calculation. At declared 1:50,000 physical scale, A(2000,2000), B(4000,2000), C(4000,4000), D(2000,4000), x east/y north; A1500m, B1540m. AB2km, curved route3km (must be geometrically drawn to that length), square4km², average gradient1:50. Bearings A→B090°, A→C045°, reverseB→A270°. SchoolD, clinicC. Contours and spot heights must derive from internally consistent terrain per panel. The coordinate-panel P/Q DMS positions are in the notes metadata; use a real projection/graticule, not arbitrary degrees pasted on a metre grid. Resized screen images need valid scale bars and a clear physical-size warning. Independent review must measure rendered output too.
- Six photographs (4.2 resources05–10): acquire actual photos with documented permission for redistribution and derivatives. Record source URL, creator, licence URL, attribution, derivative permission, retrieval date and original-file hash. Inspect the actual image; THEN reconcile prompt, answer, rubric and relevant claims. The existing six canonical answers are provisional scene requirements and must be replaced with observed scene-specific answers. Never infer feature positions from those placeholders. If a licensed suitable scene is unavailable, report it rather than pretending a generated illustration is a photo. The proposed scenes are coastal beach/sea/cliff, oblique cultivated plots, horizontal valley, sparse shrubs, oblique settlement at junction, and valley transport route.

## Two unapproved map-stimulus repairs — do not silently expand the plan

Agriculture cards013–016 need a Namibia farming-distribution map; Wildlife card002 needs a conservation-location map. Neither is assigned in the current54-resource plan. Exact IDs, reasons and suggested overlays/reuse are in the index and the two authoring_notes files. Prepare a concrete sourced repair proposal for planner/Vitalis approval, preserving slots and labels. Do not invent an approved resource ID, change a recorded approval hash, count those maps as delivered, or substitute prose for the missing stimulus. Continue the existing54 while this separate decision is pending. A genuine approved reuse still needs the appropriate visible map content, exact bindings and independent review.

## Delivery interface and publication guard

Write `assets/asset-manifest-6137.json` with `resources` (exact active resource IDs) and `item_bindings`. Each resource entry carries the four planned paths, `file_hashes` mapping every master/spec/image/variant relative path to SHA-256, code/checklist paths, and photo `licence` when applicable. Add no fake acceptance: leave `independent_review` absent until Codex inspects it. Later Codex supplies `{reviewer:"Codex", verdict:"accept", file_hashes:<exact same map>, report_path:<workspace-relative report>}`. Each binding is `{item_id,resource_id,question_path,answer_path,yyeni_asset_id:null}`; include every assigned target, reuse and practical package variant. Store all files inside this workspace.

`authoring/publish_guarded_6137.py` defaults to a read-only preflight and currently refuses publication. Its publication branch has not been run because assets and reviews do not exist. It needs all slots/labels/budgets, actual image links and hashes, Codex visual acceptance, licensed photos, resolved map concerns and Claude whole-subject semantic acceptance. After independent image review and any text repairs, Claude writes `review/subject-acceptance-6137.json` only after actually reviewing the whole subject: `{reviewer:"Claude",verdict:"publish",source_hashes:<snapshot() from helper>,manifest_sha256:<manifest hash>,report_path:<actual report>}`. This is a separate Step6 review, not implied by making the images. Do not create this acceptance during visual authoring. Changes afterward invalidate the hashes. YYeni asset IDs stay null until a separately approved import.

Report exact resources completed, paths/hashes, all changed text/claims, self-check results and unresolved issues. Supply a contact sheet after individual checks, not as their replacement. No learner-ready or independent-review claim until the relevant reviewer has actually accepted the exact files.

## Fixed resource order

| # | Resource | Assigned card/package | Objective |
|---:|---|---|---|
| 1 | VIS-6137-1.1-01 | ITEM-6137-1.1-012-INTERP | Interpret convergent/destructive margins from a supplied original resource |
| 2 | VIS-6137-1.1-02 | ITEM-6137-1.1-013-INTERP | Interpret divergent/constructive margins from a supplied original resource |
| 3 | VIS-6137-1.1-03 | ITEM-6137-1.1-014-INTERP | Interpret conservative/transform margins from a supplied original resource |
| 4 | VIS-6137-1.2-01 | ITEM-6137-1.2-019-INTERP | Freeze-thaw weathering |
| 5 | VIS-6137-1.2-02 | ITEM-6137-1.2-021-INTERP | Exfoliation |
| 6 | VIS-6137-1.2-03 | ITEM-6137-1.2-015-INTERP | Carbonation and its conditions |
| 7 | VIS-6137-1.3-01 | ITEM-6137-1.3-002-INTERP | identify and describe the main features of a drainage basin with reference to river channel, watershed area and catchment area |
| 8 | VIS-6137-1.3-02 | ITEM-6137-1.3-007-INTERP | describe the characteristics of a river valley in terms of the upper, middle and lower course (longitudinal profile) |
| 9 | VIS-6137-1.3-03 | ITEM-6137-1.3-018-INTERP | name and describe landforms associated with river erosion with reference to waterfalls, rapids, meanders, potholes and gorges |
| 10 | VIS-6137-1.4-01 | ITEM-6137-1.4-007-INTERP | describe and explain the landforms associated with wind erosion such as rock pedestals, deflation hollow and desert pavements |
| 11 | VIS-6137-1.4-02 | ITEM-6137-1.4-012-INTERP | name and describe the wind transport processes for example suspension, saltation and surface creep |
| 12 | VIS-6137-1.4-03 | ITEM-6137-1.4-017-INTERP | describe and explain the landforms and features associated with wind deposition in Namibia, e.g. star dunes at Sossusvlei and seif dunes at Swakopmund |
| 13 | VIS-6137-1.5-01 | ITEM-6137-1.5-010-APP | distinguish the types of waves such as constructive and destructive and explain the energy of the waves, swash and backwash |
| 14 | VIS-6137-1.5-02 | ITEM-6137-1.5-020-INTERP | describe and explain erosional landforms such as cliffs, stacks, arch, stump, caves, wave-cut notch, wave-cut platform, headland and bays |
| 15 | VIS-6137-1.5-03 | ITEM-6137-1.5-029-INTERP | describe the transportation of materials along the coastline by means of longshore drift |
| 16 | VIS-6137-1.5-04 | ITEM-6137-1.5-033-INTERP | name and describe depositional landforms such as beaches, bars, tombolo and spits |
| 17 | VIS-6137-1.5-05 | ITEM-6137-1.5-046-PROC | Beach-profile measurement |
| 18 | VIS-6137-1.5-06 | ITEM-6137-1.5-048-PROC | Pebble size/shape and selection |
| 19 | VIS-6137-1.5-07 | ITEM-6137-1.5-050-PROC | Beach-material movement investigation |
| 20 | VIS-6137-1.5-08 | ITEM-6137-1.5-P03 | Five-mark judgement on a precise geographical claim with a verified named case where appropriate. Use How far do you agree; judge relevant facts and reach a supported decision. Four marks judge relevant facts and one credits the supported decision, which may be implied. Apply the 2024 demand without forcing equal-sided essays. In integrated enquiry apply the judgement to the supplied investigation evidence. |
| 21 | VIS-6137-1.6-01 | ITEM-6137-1.6-008-INTERP | name and describe the instruments used to measure weather elements such as: the rain gauge, minimum and maximum thermometer/ six’s thermometer, wet and dry bulb thermometer /hygrometer, barometer/barograph, anemometer, wind vane and sunshine recorder |
| 22 | VIS-6137-1.6-02 | ITEM-6137-1.6-017-INTERP | demonstrate the ability to measure, record and analyse weather statistics such as: temperature, rainfall, humidity, air pressure, cloud cover, sunshine, wind speed and wind direction |
| 23 | VIS-6137-1.6-03 | ITEM-6137-1.6-036-INTERP | analyse synoptic charts and interpret weather satellite image |
| 24 | VIS-6137-1.6-04 | ITEM-6137-1.6-040-INTERP | describe the factors influencing climate such as latitude, altitude, ocean current, distance from the sea, prevailing wind, pressure systems |
| 25 | VIS-6137-1.7-01 | ITEM-6137-1.7-002-INTERP | identify and locate on a world map the following vegetation regions: - tropical rain or equatorial forest (evergreen) - tropical grassland (savannah) - tropical deserts |
| 26 | VIS-6137-1.7-02 | ITEM-6137-1.7-017-INTERP | analyse and interpret the climatic graphs showing the main characteristics of temperatures and rainfall of each of the regions |
| 27 | VIS-6137-2.1-01 | ITEM-6137-2.1-038-INTERP | describe the inputs, processes and outputs of a fish processing plant in Namibia |
| 28 | VIS-6137-2.2-01 | ITEM-6137-2.2-004-INTERP | describe farming as a system with reference to inputs, processes and outputs |
| 29 | VIS-6137-2.3-01 | ITEM-6137-2.3-036-PROC | Tourism environmental-quality assessment |
| 30 | VIS-6137-2.3-02 | ITEM-6137-2.3-038-PROC | Tourism footpath-erosion investigation |
| 31 | VIS-6137-2.3-03 | ITEM-6137-2.3-040-PROC | Tourism questionnaire and seasonal-impact survey |
| 32 | VIS-6137-2.3-04 | ITEM-6137-2.3-014-INTERP | discuss the advantages of the tourist industry such as growth in income, increase in foreign exchange earnings, employment opportunities, the development of infrastructure and facilities and cultural advantages |
| 33 | VIS-6137-2.4-01 | ITEM-6137-2.4-012-INTERP | describe the growing significance of renewable energy supplies to reduce dependence on fossil fuels, geothermal, waves, tides, running water, solar and biogas |
| 34 | VIS-6137-2.5-01 | ITEM-6137-2.5-014-INTERP | discuss how the processes operating within the hydrological cycle may affect supplies, with special reference to causes and effects of flooding and drought |
| 35 | VIS-6137-2.6-01 | ITEM-6137-2.6-011-INTERP | discuss the impact of environmental change on the wildlife animals such as desertification, deforestation and global warming |
| 36 | VIS-6137-3.1-01 | ITEM-6137-3.1-033-INTERP | identify and discuss with reasons the different types of population structures as shown by age-sex pyramids |
| 37 | VIS-6137-3.1-02 | ITEM-6137-3.1-027-INTERP | describe and explain different stages of the Demographic Transition Model |
| 38 | VIS-6137-3.1-03 | ITEM-6137-3.1-037-INTERP | identify major influences on population density and population distribution. Reference should be made to physical, economic and human factors |
| 39 | VIS-6137-3.2-01 | ITEM-6137-3.2-006-INTERP | interpret Namibia’s HIV and AIDS statistics and account for its spatial distribution |
| 40 | VIS-6137-3.3-01 | ITEM-6137-3.3-002-INTERP | describe the patterns of rural settlement such as dispersed, linear and nucleated |
| 41 | VIS-6137-3.3-02 | ITEM-6137-3.3-015-INTERP | discuss the internal structure (morphology) of towns and cities of Less Economically Developed Countries (LEDCs) and More Economically Developed Countries (MEDCs) by focusing on the Central Business District (CBD), residential areas, industrial areas, shopping areas/strip malls, the provision of open space and transport routes |
| 42 | VIS-6137-4.1-01 | ITEM-6137-4.1-021-PROC | differentiate between random, systematic and stratified sampling |
| 43 | VIS-6137-4.1-02 | ITEM-6137-4.1-034-INTERP | demonstrate the ability to analyse and present data collected in appropriate form using for instance maps, graphs, tables, isolines and flow charts |
| 44 | VIS-6137-4.1-03 | ITEM-6137-4.1-046-INTERP | make effective conclusions and evaluations, suggesting solutions were appropriate |
| 45 | VIS-6137-4.2-01 | ITEM-6137-4.2-002-INTERP | identify the characteristics of a map such as the title, key, scale and direction |
| 46 | VIS-6137-4.2-02 | ITEM-6137-4.2-008-INTERP | demonstrate the ability to use the scale in measuring distance, calculating area and gradient |
| 47 | VIS-6137-4.2-03 | ITEM-6137-4.2-016-INTERP | demonstrate the ability to find direction and calculate bearings |
| 48 | VIS-6137-4.2-04 | ITEM-6137-4.2-034-INTERP | locate features on a map using latitude and longitude coordinate system |
| 49 | VIS-6137-4.2-05 | ITEM-6137-4.2-027-INTERP | recognise and interpret horizontal/oblique photographs (landforms, natural vegetation, land-use and settlement) |
| 50 | VIS-6137-4.2-06 | ITEM-6137-4.2-028-APP | recognise and interpret horizontal/oblique photographs (landforms, natural vegetation, land-use and settlement) |
| 51 | VIS-6137-4.2-07 | ITEM-6137-4.2-029-INTERP | Explain or use horizontal photograph interpretation |
| 52 | VIS-6137-4.2-08 | ITEM-6137-4.2-030-APP | Explain or use horizontal photograph interpretation |
| 53 | VIS-6137-4.2-09 | ITEM-6137-4.2-031-INTERP | Explain or use oblique photograph interpretation |
| 54 | VIS-6137-4.2-10 | ITEM-6137-4.2-032-APP | Explain or use oblique photograph interpretation |
