"""8227 author-record helpers. Membership and educational claims remain explicit."""
import json
from pathlib import Path
W = Path(__file__).resolve().parents[2]

def D(short):
    return '8227:2020:' + short

def members(book, chapter, kind, numbers, parts='*'):
    return [dict(item_id=f'8227:TB:{book}:C{chapter}:{kind}:{n}', parts=parts,
                 membership_reason='Explicit author comparison of the requested decisions and responses. Preserve the connected source item, actual givens, domain, diagrams and registered defects; this is internal evidence, not an approved recipe.') for n in numbers]

def family(slug, title, decisions, givens, constraints, representation, scaffold,
           alternatives, answer, difficulty, distinction, demands, member_specs):
    return dict(family_id='8227:TEXTBOOK-FAMILY:'+slug, title=title,
                learner_decisions=decisions, givens_and_unknowns=givens,
                constraints=constraints, representation_and_response=representation,
                scaffolding_and_connected_parts=scaffold, alternative_methods=alternatives,
                units_and_precision='Preserve the literal angular unit, original interval endpoints, exact-form or decimal instruction and physical dimensions. Intermediate approximations must not change the final rounding or admissibility.',
                answer_form=answer, difficulty_progression=difficulty,
                distinction_basis=distinction, assessed_demand_ids=demands,
                member_specs=member_specs,
                examination_relation=dict(kind='textbook-only', pattern_ids=[], part_ids=[],
                    evidence_label='textbook-derived', reason='Textbook-derived candidate breadth. No complete examination-type equivalence or official marking criteria are inferred from this source grouping. Demand-level examination comparisons are recorded separately in the insights.'))

def insight(slug, title, demands, teaching, exams, bounds, pitfalls, gaps,
            proposals, evidence, exam_parts=(), grades=(), rules=(), errors=()):
    return dict(insight_id='8227:TEXTBOOK-INSIGHT:'+slug, title=title,
                demand_ids=demands, teaching_comparison=teaching,
                examination_comparison=exams, difficulty_and_grade_bounds=bounds,
                pitfalls=pitfalls, gaps_and_representations=gaps,
                implications_for_step3=proposals, evidence_item_ids=evidence,
                examination_part_ids=list(exam_parts), grade_descriptor_ids=list(grades),
                marking_rule_ids=list(rules), examiner_error_ids=list(errors))

def emit(name, scope, families, insights, extensions=(), exclusions=()):
    from synthesis_examination_links_r5 import LINKS
    for row in families:
        slug=row['family_id'].split(':TEXTBOOK-FAMILY:')[1]
        if slug in LINKS:
            row['examination_relation']=dict(LINKS[slug])
            row['examination_comparison_author_input']='tools/textbook-r5/synthesis_examination_links_r5.py'
    target=W/f'tools/textbook-r5/synthesis-{name}.json'
    target.write_text(json.dumps(dict(authorship='Codex author; independent review pending',
        scope=scope, families=families, insights=insights, family_extensions=list(extensions),
        response_exclusions=list(exclusions)), ensure_ascii=False, indent=2)+'\n')
    print(name, len(families), 'authored families;', len(insights), 'insight sections')
