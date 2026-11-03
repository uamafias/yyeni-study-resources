# NSSCO Mathematics recipe resources

The historical 3,300-card bulk bank and its importer/builder were deleted on Jeremy’s instruction on 3 November 2026.

Current candidate content is workbench-bank.json (409 recipe settings, 410 assignment choices, 4,022 distinct examples). Build it directly with scripts/build_math_workbench_bank.py, using workbench-authoring-plan.json: recipe IDs, seed/slot plans and lesson metadata, without historical card text. Rebuild the catalogue with scripts/build_workbench_catalogue.py and catalogue-homes.json.

workbench-disposition.json contains only old slot decisions, seed metadata and hashes used to preserve/retire existing Studio assignments. It cannot import or reconstruct the deleted static bank. Existing generators, saved learner questions, retired-card safeguards and prepared image identities remain.

The separate 420-card Statistics static bank and its import path were also removed as unrelated to Workbench. Deletions were verified against Jeremy's Git authorship/committer records. Six power types now have version-9 repairs; their original 60 examples remain preserved outside deployment in the resources repo. Exact duplicates and the overlapping exponential branch remain consolidated. No learner DB records were deleted. Historical audit packets remain evidence, not rebuild or runtime inputs.

workbench-demand-evidence.json binds the 439 authored demand entries to actual question parts. scripts/report_math_workbench_coverage.py generates the traceable review index. These author links and passing checks do not claim independent whole-bank mathematical, tariff or clause-sufficiency approval.
