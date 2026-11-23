"""Rebuild the repaired 8227 analysis. No recipes, runtime generators or publication.

Author annotations are separate from PDF scans and family grouping. Run from repo
root; source documents and the independent review directory are read-only inputs.
"""
import json
import argparse
from analysis_sources import A, WB, write
from build_curriculum import build_curriculum, build_assessment_conditions
from build_mapping import build_questions
from build_visual_records import attach_visuals_and_references
from build_families import build_families
from demand_coverage import compute, objective_rows
from source_defects import build_defects


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative-fixture',choices=['tariff','label','crop','held-reference'],help='Corrupt an in-memory first-part fixture; build must fail without changing author inputs')
    args=parser.parse_args()
    if args.negative_fixture=='crop':
        from check_crop_containment import validate
        record=next(a for a in json.loads((A/'asset-index.json').read_text())['assets'] if a['asset_id']=='2024-1-q9-given')
        validate(record['source_path'],record['pdf_page'],[65,55,510,245],'seeded-text-cut')
        raise AssertionError('seeded crop unexpectedly passed')
    objectives, demands = build_curriculum()
    questions, paper_checks = build_questions(demands,args.negative_fixture if args.negative_fixture in ['tariff','label'] else None)
    assets = attach_visuals_and_references(questions,args.negative_fixture)
    comparable_path = A / 'cambridge-evidence.json'
    comparable = json.loads(comparable_path.read_text())['items'] if comparable_path.exists() else []
    index=json.loads((A/'asset-index.json').read_text())
    index['assets']=assets+[a for i in comparable for a in i['diagram_assets']]
    index['crop_review']='Codex author inspected all 39 regenerated crops and the two required source overlays, 2026-11-17; checks/r3/crops-00..04.png. Focused cross-vendor check pending'
    index['scope']='All 39 rendered source crops: 26 NSSCAS givens, 6 response frames, 7 Cambridge givens'
    write(A/'asset-index.json',index)
    from check_crop_containment import check_all
    check_all()
    from build_provenance import build as build_provenance
    build_provenance(questions)
    from build_awards_r4 import attach_question_award_links
    attach_question_award_links(questions)
    families = build_families(questions, demands, comparable)
    parts = [p for q in questions for p in q['parts']]
    rows = compute(demands, parts, comparable)
    coverage = objective_rows(objectives, rows)
    write(A/'question-analysis.json', {'schema_version':'workbench-analysis-8227-r2','questions':questions})
    write(A/'demand-dispositions.json', {'schema_version':'workbench-analysis-8227-r2','rows':rows})
    write(A/'coverage-matrix.json', {'schema_version':'workbench-analysis-8227-r2','rows':coverage})
    build_assessment_conditions(questions)
    build_defects(questions)
    counts = {'objectives':len(objectives),'demands':len(demands),
              'connected_questions':len(questions),'assessed_parts':len(parts),
              'analysis_groups_not_recipe_count':len(families),
              'paper_checks':paper_checks,'marks':sum(p['printed_marks'] for p in parts),
              'questions_with_transcribed_award_table':sum(bool(q['transcribed_award_pdf_pages'])for q in questions),
              'questions_with_embedded_marking_excerpt':sum(bool(q['marking_excerpt_pdf_pages']) for q in questions),
              'visual_response_parts':sum(p['requires_sketch_response'] for p in parts),
              'sketch_dependent_parts':sum(p['requires_learner_sketch_reading'] for p in parts),
              'input_diagram_crops':sum(a['purpose']=='given source diagram/graph' for a in assets), 'response_frame_crops':sum('blank response axes' in a['purpose'] for a in assets), 'cambridge_items':len(comparable),
              'zero_usable_nsscas_demand_ids':[r['demand_id'] for r in rows if not r['observed_part_links']],
              'checks':{'full_ordered_tariffs_and_labels':'pass after actual scans',
                        'direct_demand_references':'pass after annotated ID resolution',
                        'coverage_independent_of_families':'separate module with no family input'},
              'does_not_certify':['independent repair acceptance','independent acceptance of the119question award records',
                                  'exhaustive textbook analysis','app implementation/testing','recipe correctness']}
    write(A/'analysis-checks.json',counts)
    # Narrative records are generated from the same authoritative repaired data.
    from build_gap_reconciliation import build as build_gaps
    build_gaps()
    from render_analysis_records import render_records
    render_records(objectives,demands,questions,families,rows,coverage,comparable)
    print(json.dumps(counts,indent=2))


if __name__=='__main__':
    main()
