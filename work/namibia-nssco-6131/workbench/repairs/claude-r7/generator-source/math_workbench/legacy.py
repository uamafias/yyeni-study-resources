"""Screen and reuse complete exam demands from the historical generator bank."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import random
import re

from services.math_generators import generate_problem
from services.math_generators.graph_bank import problem_references
from services.math_marking.grading_contract import build_contract
from .legacy_objectives import classify,SETTING_SPECS
from .core import part,question,step

DATA=Path(__file__).resolve().parents[2]/'data/imports/nam-6131-nssco-2026'

PRINCIPLES={
 'advanced_graphs':'Function values come from substituting into the full rule; algebraic solutions must satisfy the original domain.',
 'advanced_percentages':'Percentages compare an amount with its stated base; a percentage change uses a multiplicative factor, while reversing it requires division by that factor.',
 'algebraic_manipulation_expansion':'The distributive law multiplies every term in a bracket; only terms with identical variable powers can be collected.',
 'angles_circles':'Apply the stated circle-angle property, keeping the centre/circumference roles and minor/reflex angles distinct.',
 'angles_lines_polygons':'Straight-line angles sum to 180°, angles at a point to 360°, and polygon sums follow from triangle decomposition.',
 'bearings_right_angled_triangles':'Bearings are clockwise from north; right-triangle side and angle relationships depend on which sides are opposite, adjacent and hypotenuse.',
 'bisectors_numeric':'A bisector divides an angle into equal parts; a perpendicular bisector gives equal distances from the endpoints.',
 'circles_arcs_sectors':'A sector is the angle fraction of a full circle; distinguish an arc length from the full boundary and an area from a perimeter.',
 'constructions_scale_drawings':'A scale compares drawing and actual lengths in consistent units.',
 'cumulative_frequency_reading':'Cumulative frequencies are running totals; subtract boundary totals to recover an interval count, and use the appropriate fraction of the total to locate a quantile.',
 'defining_sets_notation':'Union collects elements in either set, intersection keeps common elements, and complements are taken relative to the stated universal set.',
 'determinants_inverses':'For a 2×2 matrix the determinant is ad−bc; a nonzero determinant permits the adjugate divided by the determinant to give the inverse.',
 'directed_numbers_in_action':'A signed change is added to the starting quantity; the change itself is final minus initial, with the ordinary order of operations preserved.',
 'distance_midpoint_gradient':'Coordinate differences give displacement; distance uses Pythagoras, midpoint averages corresponding coordinates, and gradient is vertical change divided by horizontal change.',
 'elevation_depression_extended_ratios':'Choose the trigonometric ratio from the sides or angle involved; signs in extended quadrants determine the valid angle solutions.',
 'equations_of_straight_lines':'A line is fixed by its gradient and a point; substitute the known point into y=mx+c to determine the intercept.',
 'expressions_formulae':'Substitution replaces every occurrence of a variable; rearrangement applies reversible operations to the whole equation.',
 'factorisation_basics':'Factorisation reverses expansion; every term must retain its original value when the factors are multiplied back.',
 'factorising_quadratics':'For a quadratic, expanding candidate factors must reconstruct every coefficient; completing the square uses half the internal linear coefficient and compensates for the added square.',
 'fractions_decimals_percentages':'Equivalent fractions have the same numerator-to-denominator ratio; multiplication, common denominators and reciprocal division preserve that value.',
 'functions':'Function notation fixes the input; an inverse reverses input and output, while a composite applies the inner function before the outer one.',
 'functions_concepts':'A function assigns exactly one output to every allowed input; an inverse function needs distinct inputs to have distinct outputs, and composition preserves the stated order.',
 'geometrical_terms':'Use the defining angle, face or side relationships of the named figure rather than its apparent drawing size.',
 'grouped_data_mean':'A grouped mean estimates each observation by its class midpoint and weights that midpoint by the class frequency; cumulative positions locate medians and modal classes use frequencies.',
 'histograms_text':'Histogram bar area represents frequency, so frequency density equals frequency divided by class width.',
 'income_taxes_bills':'Apply the supplied exercise rates to the correct period and quantity; separate fixed charges, usage charges, basic pay and commission.',
 'inequalities_indices':'A negative multiplier reverses an inequality; index products add exponents, quotients subtract them and powers multiply them, within the stated domain.',
 'introduction_functions':'Evaluate a function by replacing its input consistently; finding an input reverses the rule through valid equation operations.',
 'introduction_vectors':'A directed displacement is endpoint minus start point, and reversing direction negates every component.',
 'kinematics_rate_change':'Distance-time gradient gives speed, speed-time gradient gives acceleration, and area under a speed-time graph gives distance.',
 'limits_of_accuracy':'Rounding to a stated unit creates a half-unit interval; choose the extreme permissible inputs that minimise or maximise the complete requested expression.',
 'linear_programming':'Each constraint defines a half-plane; a feasible point satisfies every constraint, and a linear objective is compared at feasible vertices.',
 'linear_simultaneous_equations':'Apply equivalent operations to equations; elimination or substitution must produce values satisfying every original equation and any denominator restrictions.',
 'locus_numeric':'A locus is the complete set satisfying the stated distance condition; a single calculated coordinate is only a component of that geometric condition.',
 'logarithms':'A logarithm records an exponent; products become sums, quotients become differences and powers become multipliers, for positive logarithm arguments.',
 'matrix_basics':'Matrix addition and scalar multiplication act on corresponding entries, with row and column positions retaining their meaning.',
 'matrix_multiplication':'A matrix-product entry is a row-column dot product; multiplication order matters and dimensions must be compatible.',
 'mean_median_mode_range':'Mean is total divided by count, median is the middle ordered position, mode is the most frequent value, and range is maximum minus minimum.',
 'metric_units_conversions':'Length conversion factors are squared for areas and cubed for volumes; compound rates require converting both numerator and denominator units.',
 'number_classifications_properties':'Use the defining factors, integer properties or rationality of the complete expression; a superficial appearance does not determine its number class.',
 'parallel_perpendicular_quadrilaterals':'Parallel lines have equal gradients and nonvertical perpendicular gradients have product −1; quadrilateral calculations must preserve the vertex order.',
 'perimeters_areas_polygons':'Perimeter totals boundary lengths; area combines non-overlapping component regions with their correct perpendicular dimensions.',
 'personal_finance_currency':'Use the supplied exchange or interest rate with the stated currency and period; simple interest uses the original principal and compound interest updates the balance.',
 'polynomials_algebraic_fractions':'Factor before cancelling only nonzero common factors; polynomial division must reconstruct dividend = divisor × quotient + remainder.',
 'position_vectors':'A displacement is the difference of position vectors; a ratio point is a weighted position on the directed segment.',
 'prepared_line_graphs':'Read two actual plotted coordinates; gradient is vertical change divided by horizontal change on the labelled scales.',
 'quadratic_graphs':'Quadratic roots locate x-intercepts, x=0 locates the y-intercept, and the turning point lies on the axis of symmetry.',
 'ratios_scales_rates':'A ratio uses equal-sized parts; a rate compares quantities with different units, and an average speed uses total distance divided by total time.',
 'reading_charts_text':'Use the chart key or stated frequency scale consistently; a whole pie represents the complete frequency total.',
 'sequences':'Arithmetic terms use a constant difference, geometric terms a constant ratio; a finite sum must include exactly the specified number of terms.',
 'similarity_scale_factors':'Corresponding lengths scale by k, areas by k² and volumes by k³; use roots when recovering a length factor.',
 'simple_probability':'For equally likely outcomes, probability is favourable outcomes divided by total outcomes; complements subtract from one and expected counts multiply by trial count.',
 'sine_cosine_rules':'Choose the sine rule, cosine rule or half-ab-sin-C area relation from the known sides and angles; preserve opposite side-angle pairings.',
 'sketching_quadratics_gradients':'Intercepts and turning points constrain a quadratic sketch; a chord uses two points, while a tangent describes the instantaneous gradient.',
 'solving_quadratic_equations':'Rearrange to an equivalent quadratic, use a valid solving method, and retain both real branches unless the domain or context rules one out.',
 'standard_form_estimates_approximations':'Standard form separates a coefficient from a power of ten; rounding changes only the final retained digit and estimates use intentionally simplified values.',
 'straight_line_graphs_gradients':'In y=mx+c, m is the gradient and c the y-intercept; intercepts set the opposite coordinate to zero.',
 'surface_area_volume':'Volume multiplies cross-sectional area by length for a prism; surface area counts the exposed faces, and compound solids must not count an internal joined face.',
 'symmetry_circles':'Equal tangents, chord bisectors and equal chord distances follow from the circle’s reflection symmetry.',
 'symmetry_two_dimensions':'A symmetry maps the complete figure onto itself; rotational order counts matching positions in one full turn.',
 'time_clocks_timetables':'Convert hours and minutes consistently, account for any day boundary, and include waiting time when the requested interval includes it.',
 'transformations_coordinates':'Apply the specified centre, line, vector or angle to every vertex; a complete description includes all parameters of the transformation.',
 'tree_diagrams':'Multiply probabilities along one path and add mutually exclusive qualifying paths; update counts after a draw without replacement.',
 'vector_operations_magnitude':'Add or subtract vector components in corresponding positions; magnitude is the nonnegative length found by Pythagoras.',
 'venn_diagrams':'Separate disjoint Venn regions so that overlaps are not double-counted; probabilities divide the required region count by the universal total.',
}


@lru_cache(maxsize=1)
def retired():
    rows=json.loads((DATA/'retired-cards.json').read_text())['cards']
    return {c['card_key'] for c in rows},{c['question_sha256'] for c in rows}


def mapping(problem):
    gid,level=problem.generator_id,problem.level
    return classify(gid.removeprefix('nssco_'),level,problem.skill,problem.machine,SETTING_SPECS[f'{gid}:{level}'])


def rejection_reasons(problem,card_key=None):
    mapped=mapping(problem);reasons=list(mapped['review_flags'])
    if card_key in retired()[0] or hashlib.sha256(problem.question.encode()).hexdigest() in retired()[1]:
        reasons.append('authorised_retirement: one of the 41 flagged canonical examples')
    if not mapped['assessed_objective_ids']:
        reasons.append('guided_only: no directly assessed syllabus demand in this question')
    if problem.generator_id=='nssco_reading_charts_text':
        reasons.append('representation_gap: numerical prose substitutes for the chart being assessed')
    q=problem.question.lower();m=problem.machine
    if any(word in q for word in ('garden','pond','flagpole')) and re.search(r'\bcm\b',q):
        reasons.append('context_range: centimetre dimensions used for a full-size garden, pond or flagpole')
    if 'water tank' in q and 'cm' in q and 'model' not in q:
        reasons.append('context_range: centimetre-scale water tank is not identified as a model')
    if 'recruits' in q and any(lo>=220 and freq>0 for (lo,hi),freq in zip(m.get('classes',[]),m.get('freqs',[]))):
        reasons.append('context_range: recruit-height observations extend beyond the authored 220 cm plausibility limit')
    if 'bicycle' in q and m.get('task')=='convert' and m.get('from')=='m/s' and float(m.get('value',0))>20:
        reasons.append('context_range: bicycle speed exceeds the authored 20 m/s plausibility limit')
    return reasons


def authored_content(problem):
    """Use the authored operation explanations, never infer reasons from keywords."""
    from services.math_generators.presentation import (algebra_content, number_content,
        functions_content, functions_concepts_content, graph_content, topic_content)
    return (algebra_content(problem) or number_content(problem) or functions_content(problem)
            or functions_concepts_content(problem) or graph_content(problem) or topic_content(problem))


def retained_steps(problem, teaching):
    from services.math_marking.solution_programs import program_for
    program=program_for(problem)
    if program is None:raise ValueError('No authored retained solution program')
    return program.steps


def adapt(problem,*,source_key=None):
    rejected=rejection_reasons(problem,source_key)
    if rejected:raise ValueError('; '.join(rejected))
    c=build_contract(problem);mapped=mapping(problem);steps=[]
    from services.math_generators.presentation import worked_example
    teaching=worked_example(problem)
    blocks=[] if problem.generator_id in ('nssco_factorisation_basics','nssco_factorising_quadratics','nssco_factorisation_extension') else re.split(r'(?m)^\d+\.\s+',teaching)[1:]
    for block in blocks:
        heading=re.match(r'\*\*([^*]+)\*\*\s*(.*)',block,re.S)
        if not heading:
            continue
        action,body=heading.groups()
        if re.search(r'name the quantities|what are we looking for',action,re.I):
            continue
        maths=re.findall(r'\$([^$]+)\$',body)
        if body.strip():
            steps.append(step(action.rstrip('.'),body.strip(),maths[-1] if maths else problem.answer))
    if problem.generator_id in ('nssco_factorisation_basics','nssco_factorising_quadratics','nssco_factorisation_extension') or not steps:
        steps = retained_steps(problem, teaching)
    if problem.generator_id in ('nssco_factorisation_basics','nssco_factorising_quadratics','nssco_factorisation_extension'):
        teaching='\n\n'.join(s['action']+'. '+s['reason']+'\n\n'+(s['result'] if '$' in s['result'] else '$'+s['result']+'$') for s in steps)
    criteria=[(r['marks_available'],r['criterion']) for r in c['criteria']]
    p=part(problem.question,problem.answer,steps,c['marks'],criteria)
    p['teaching_context']=teaching
    p['objective_ids']=mapped['assessed_objective_ids']
    refs=problem_references(problem)
    assets=[{'asset_id':'prepared','role':'question_and_solution','prepared_question_reference':refs['question'],'prepared_solution_reference':refs['answer']}] if refs else []
    # Bypass the shorthand objective converter because the references are
    # already complete IDs resolved for the actual branch.
    result={'recipe_id':f'wb6131:legacy:{problem.generator_id}:{problem.level}',
            'title':problem.skill.replace('_',' ').capitalize(),'stem':'','parts':[p],
            'objective_ids':mapped['assessed_objective_ids'],'assets':assets,
            'paper_style':'short_answer_or_compound_exam_demand','proposed_total_marks':c['marks'],
            'tariff_status':c['tariff_status'],'content_status':'draft_for_independent_review',
            'legacy_source_contract':c,'source_card_key':source_key,
            'source_branch':{'task':problem.machine.get('task'),'skill':problem.skill,'shape':problem.machine.get('shape')},
            'exam_style_basis':c.get('evidence_relation'),'exam_evidence_ids':c['source_ids']}
    return result


@lru_cache(maxsize=1)
def recipe_definitions():
    path=DATA/'workbench-legacy-settings.json'
    return json.loads(path.read_text())['recipes'] if path.exists() else []


def generate(recipe_id,seed):
    definition=next((d for d in recipe_definitions() if d['recipe_id']==recipe_id),None)
    if definition is None:raise ValueError('Retired or unknown legacy recipe')
    stream=random.Random(int.from_bytes(hashlib.sha256(f'{recipe_id}:{seed}'.encode()).digest()[:16],'big'))
    for attempt in range(128):
        draw_seed=seed if attempt==0 else stream.randrange(2**62)
        p=generate_problem(definition['generator_id'],draw_seed,definition['legacy_setting'])
        if not rejection_reasons(p):return adapt(p)
    raise ValueError('No eligible exam-style question found within the bounded draw budget')
