"""Versioned teaching estimates of mathematical demand; independent of level count.

Authoring anchors and scope: docs/plans/2026-10-maths-deck-difficulty.md.
Explicit ratings describe the most complex demand available within each level.
Do not normalise by a recipe's number of levels or infer from ordinal numbers.
"""
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

VERSION = 1
SCALE_MIN, SCALE_MAX = 1, 10
SNAPSHOT_KEY = 'difficulty_snapshot'

# In actual recipe-level order, except explicit sparse levels below. Ratings can
# decrease: number-properties L5 is simpler than HCF/LCM L4, for example.
_DEMAND = {
    'advanced_graphs': [3,3,3,4,6],
    'advanced_percentages': [3,4,5,5,6],
    'algebraic_manipulation_expansion': [2,4,4,5,6],
    'angles_circles': [4,4,5,6,7],
    'angles_lines_polygons': [2,3,4,4,6],
    'bearings_right_angled_triangles': [4,4,4,4,7],
    'bisectors_numeric': [1,2,4],
    'circles_arcs_sectors': [3,4,5,6,7],
    'constructions_scale_drawings': [3,1,2],
    'cumulative_frequency_reading': [2,3,4,4],
    'defining_sets_notation': [2,3,3],
    'determinants_inverses': [3,5,4,7,5],
    'directed_numbers_in_action': [2,2,1,3,4],
    'distance_midpoint_gradient': [3,4,3,5,5],
    'elevation_depression_extended_ratios': [5,5,4,7,7],
    'equations_of_straight_lines': [4,5,5,5,7],
    'expressions_formulae': [2,3,5,6,7],
    'factorisation_basics': [2,3,4,5],
    'factorising_quadratics': [4,5,6,7,8],
    'fractions_decimals_percentages': [2,3,3,4,5],
    'functions': [3,5,5,5,6],
    'geometrical_terms': [1,2,3],
    'grouped_data_mean': [2,4,5,6,7],
    'histograms_text': [2,3,3,5],
    'income_taxes_bills': [4,4,5],
    'inequalities_indices': [3,4,3,5,6],
    'introduction_functions': [2,3,3],
    'introduction_vectors': [2,2,3],
    'kinematics_rate_change': [3,4,5,4],
    'limits_of_accuracy': [3,3,5,5,7],
    'linear_programming': [3,4,5,6],
    'linear_simultaneous_equations': [3,4,5,6,8],
    'locus_numeric': [3,3,3],
    'logarithms': [2,4,5,6,7],
    'matrix_basics': [2,3,3,4],
    'matrix_multiplication': [3,4,5,5],
    'mean_median_mode_range': [2,3,4,5],
    'metric_units_conversions': [2,3,4,5],
    'number_classifications_properties': [1,2,3,4,2],
    'parallel_perpendicular_quadrilaterals': [3,4,4,6,7],
    'perimeters_areas_polygons': [3,4,5,6],
    'personal_finance_currency': [3,4,4,5,6],
    'polynomials_algebraic_fractions': [5,6,6,6,7],
    'position_vectors': [5,3,5,6],
    'quadratic_graphs': [3,4,5,6],
    'ratios_scales_rates': [3,4,4,5,5],
    'reading_charts_text': [1,2,4,4],
    'sequences': [2,4,5,7,9],
    'similarity_scale_factors': [3,4,5,6],
    'simple_probability': [2,3,4,4,5],
    'sine_cosine_rules': [4,5,5,5,8],
    'sketching_quadratics_gradients': [4,3,5,5],
    'solving_quadratic_equations': [3,3,5,6,7],
    'standard_form_estimates_approximations': [2,2,3,4,4],
    'straight_line_graphs_gradients': [2,3,4,4,4],
    'surface_area_volume': [3,4,4,6,7],
    'symmetry_circles': [2,3,2],
    'symmetry_two_dimensions': [1,2,3],
    'time_clocks_timetables': [2,2,3,4,5],
    'transformations_coordinates': [2,3,4,4,5],
    'tree_diagrams': [4,5,6,7,7],
    'vector_operations_magnitude': [3,4,5,5],
    'venn_diagrams': [3,4,5,5],
    'visual_advanced_graphs': [5,7],
    'visual_bearings': [3,3],
    'visual_bisectors': [4,4],
    'visual_charts': [3,4,3],
    'visual_clocks': [2],
    'visual_constructions': [1,4],
    'visual_cumulative': [5,5],
    'visual_geometry': [1,2],
    'visual_histograms': [4,6,5],
    'visual_linear_programming': [6,5,7],
    'visual_loci': [3,3,4,6],
    'visual_possibility': [4],
    'visual_practical_graphs': [3,4,5],
    'visual_quadratics': [4,5,4],
    'visual_straight_lines': [3,3],
    'visual_symmetry': [2,2],
    'visual_transformations': [3,2,4,5,5],
    'visual_trees': [5,6],
    'visual_vectors': [3,4],
    'visual_venn': [3,4],
}
RATINGS = {'nssco_'+slug:dict(enumerate(scores,1)) for slug,scores in _DEMAND.items()}
RATINGS['nssco_functions_concepts'] = {1:3,2:5,4:5}
RATINGS['nssco_prepared_line_graphs'] = {2:3}


def current_rating(generator_id, level):
    if type(level) is not int:
        return None
    score = RATINGS.get(generator_id,{}).get(level)
    return {'version':VERSION,'rating':score,'level':level,'generator_id':generator_id} if score is not None else None


def freeze_params(generator_id, params):
    """Never mutate source params or trust a rating carried by an editable card."""
    if not generator_id or not isinstance(params,dict):
        return params
    frozen = {k:v for k,v in params.items() if k!=SNAPSHOT_KEY}
    rating = current_rating(generator_id,params.get('level'))
    if rating:
        from .presentation import CONTENT_LABELS, FACTORISING_LABELS
        labels = FACTORISING_LABELS if generator_id=='nssco_factorising_quadratics' else CONTENT_LABELS.get(generator_id,{})
        frozen[SNAPSHOT_KEY] = {**rating,'generator_id':generator_id,
                                'label':labels.get(rating['level'],f"Level {rating['level']}")}
    return frozen


def saved_rating(generator_id, params):
    snapshot = params.get(SNAPSHOT_KEY) if isinstance(params,dict) else None
    if (not isinstance(snapshot,dict) or type(snapshot.get('version')) is not int
            or snapshot['version']<1 or snapshot.get('generator_id')!=generator_id
            or type(snapshot.get('rating')) is not int
            or not SCALE_MIN<=snapshot['rating']<=SCALE_MAX
            or snapshot.get('level')!=params.get('level')
            or type(snapshot.get('level')) is not int):
        return None
    return dict(snapshot)


def summarise(cards):
    """Cards are small dicts with generator_id, params, lesson and lesson_key."""
    cards = list(cards)
    maths = [c for c in cards if c.get('generator_id')]
    if not maths:
        return None
    rated = [(c,c.get('rating')) for c in maths if c.get('rating')]
    scores = [r['rating'] for c,r in rated]
    complete = len(rated)==len(maths)
    groups = {}
    for card,rating in rated:
        key = (card.get('lesson_key'),card['generator_id'],rating['level'],rating['version'],rating['rating'])
        if key not in groups:
            groups[key] = {'lesson':card.get('lesson') or 'Maths','generator_id':card['generator_id'],
                'level':rating['level'],'label':rating.get('label') or f"Level {rating['level']}",
                'rating':rating['rating'],'version':rating['version'],'count':0}
        groups[key]['count'] += 1
    score = float((Decimal(sum(scores))/Decimal(len(scores))).quantize(Decimal('.1'),rounding=ROUND_HALF_UP)) if scores and complete else None
    return {'score':score,'scale_min':SCALE_MIN,'scale_max':SCALE_MAX,
            'card_min':min(scores) if scores else None,'card_max':max(scores) if scores else None,
            'rated_count':len(scores),'maths_count':len(maths),'total_count':len(cards),
            'versions':sorted({r['version'] for c,r in rated}), 'coverage_complete':complete,
            'breakdown':sorted(groups.values(),key=lambda g:(g['lesson'],g['level'],g['generator_id']))}


def deck_summaries(db, deck_ids):
    """One narrow metadata query for any number of authorised decks."""
    from models import FlashcardStudioDeckCard as Card
    by_deck = defaultdict(list)
    if not deck_ids:
        return {}
    for row in db.query(Card.deck_id,Card.generator_id,Card.generator_params,
                        Card.source_classroom_id,Card.source_topic_bucket_id,
                        Card.topic_title_snapshot).filter(Card.deck_id.in_(deck_ids)).all():
        by_deck[row.deck_id].append({'generator_id':row.generator_id,
            'rating':saved_rating(row.generator_id,row.generator_params),
            'lesson_key':(row.source_classroom_id,row.source_topic_bucket_id),
            'lesson':row.topic_title_snapshot})
    return {deck_id:summarise(cards) for deck_id,cards in by_deck.items()}
