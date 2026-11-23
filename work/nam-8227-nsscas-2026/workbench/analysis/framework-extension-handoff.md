# Framework extension handoff from the 8227 repair

16 November 2026. These are subject-local analysis shapes and proposals to extend
Jeremy's existing framework through versioned review. No second framework, runtime
recipe schema or app implementation is introduced by this repair.

| Extension | Current evidence/example | Shared-framework/app acceptance check |
|---|---|---|
| Per-year assessment conditions | `curriculum/assessment-conditions.json`: formula/data support, precision, angle units, calculator and source pages | Another subject can attach its data booklet without inheriting Maths formulae; supplied support never expands syllabus scope |
| Level descriptors | `curriculum/grade-descriptions.json`; family `grade_variation_bounds` with exact statement IDs | Floor and ceiling are traceable; arbitrary numerical difficulty is not called grade a |
| Source defects | `source-defects.json`: locator, recomputation, hold/correction and owner decision | A held source exemplar cannot silently reappear as an original or approved branch; valid syllabus demand remains visible |
| Textbook completion/conflicts | `textbook-completion-method.md`, TB14/TB15/TB19 | Exam-style/visual/gap populations reconciled separately from routine samples; official conventions and book advice stay distinct |
| Bloom storage | Author evidence: per-part label and rationale, reviewed recipe version/branch; safe display: complete whole-card highest level plus part labels; private marking: criteria supporting that judgement | Apply+Analyse+Evaluate displays Level5 once; any unclassified part prevents a verified maximum; no answer/criterion leakage before reveal. This analysis remains unclassified |
| Attributed examination references | Part/item `examination_references`; source hashes, printed/PDF pages, board/session/component, relation, generated learner label | Only original/same-type labels display; related remains internal; exact demand/response match for same-type; held exemplars excluded. Preserve identity across saved selections and delivery |
| Visual input and response | Per-part `given_representation`, `diagram_assets`, `diagram_parameters`, `response_format`, sketch features | Generate diagram/question/solution from identical values; grade correct/partial/alternative/wrong/ambiguous sketches against feature-level marks and ask for clarification where needed |

Example safe teacher metadata (illustrative, not installed):

```json
{
  "curriculum_id": "nam-8227-nsscas-dec2020",
  "recipe_version": "reviewed-version-required",
  "part_id": "b",
  "directly_assessed_demand_ids": [
    "8227:2020:M1:T2:O05:D01"
  ],
  "response_format": "symbolic",
  "bloom": {
    "level": null,
    "status": "unclassified"
  },
  "examination_references": [
    {
      "board": "NSSCAS",
      "syllabus_code": "8227",
      "year": 2023,
      "session": null,
      "paper": "1",
      "question": "5",
      "part": "b",
      "printed_page": 8,
      "pdf_page": 8,
      "source_path": "Question Banks/Namibian Curricula/NSSCAS/Mathematics (8227)/2023/AS - Mathematics Paper 1 8227-1 - First Proof 10.03.2023.pdf",
      "source_sha256": "60846eaf80816c2a24802cf63a6d1b0cfdf53c079c5c5de669c384c04237c411",
      "relation": "same-type",
      "verified_by": "Source page checked by author; a future generated branch still requires reviewed demand/response equality"
    }
  ]
}
```
The source identity and demands above come from the actual 2023P1Q5(b) record.
The future recipe/version remains a placeholder: same-type display requires a
reviewed generated branch preserving those demands and its response format. Runtime solutions, original question text and private
marking references require appropriate reveal/access controls. App-owned attempts,
assignments, school/classroom isolation and progress remain outside resources.

Vitalis announced sketch reading and diagram generation for 17 November 2026.
This owner decision includes visual demands; it is not evidence of runtime testing
on 16 November. MCP installation, classroom availability and learner assignment
remain separate, untested operations with no target selected. Final local website
acceptance must use reviewed real resources before merge/deployment.
