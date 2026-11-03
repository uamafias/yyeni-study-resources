"""Frozen semantic rules from the local objective audit, shared by fresh draws.
Generated from the authored audit; objective IDs are internal syllabus locators.
"""
import json
from pathlib import Path
_DATA=json.loads(Path(__file__).with_name('legacy_rules.json').read_text())
SETTING_SPECS=_DATA['settings']
SKILL_OVERRIDES={(r['family'],r['skill']):r['spec'] for r in _DATA['skill_overrides']}
def oid(short):
    section, number = short.split('.')
    return f'6131:{section}:{int(number):02d}'

def parse_spec(spec):
    direct, support = [], []
    for token in spec.split('+'):
        (support if token.startswith('~') else direct).append(oid(token.lstrip('~')))
    return direct, support

def classify(family, level, skill, machine, spec):
    spec = SKILL_OVERRIDES.get((family, skill), spec)
    flags = []
    if family == 'factorising_quadratics' and machine.get('turning_point') is not None:
        spec += '+7d.8'
    if family == 'functions' and machine.get('task') == 'cube_equation':
        spec = '1b.1'
        flags.append('lesson_alignment: cube-root equation stored in Functions but does not elicit function notation')
    if family == 'standard_form_estimates_approximations' and level == 5:
        spec += '+1b.1'
    if family == 'advanced_graphs':
        if skill == 'reciprocal_values' and not machine.get('squared'):
            spec = '7d.1+7d.5'
        elif skill == 'reciprocal_values':
            spec = '7d.5'
        elif skill == 'exponential_intercept':
            spec = '~7d.6'
        elif skill == 'solve_reciprocal':
            spec = '6d.5+~7d.6'
        elif skill == 'solve_reciprocal_square':
            spec = '1b.1+~7d.6'
        elif skill == 'solve_exponential':
            spec = '6e.3+~7d.6'
        elif skill == 'solve_cubic':
            spec = '1b.1+~7d.6'
        elif skill == 'asymptotes':
            flags.append('scope_review: asymptote terminology/shifted curves not explicit in syllabus bullets')
        if skill == 'exponential_values' and machine.get('a', 1) != 1:
            flags.append('scope_review: scaled exponential differs from the explicit y=a^x table form')
    if family == 'angles_circles' and str(machine.get('task', '')).startswith('alt_segment'):
        flags.append('scope_review: alternate-segment theorem is not in the explicit angle-property list')
    if family == 'number_classifications_properties' and machine.get('kind') == 'negative_root':
        spec = '~1a.1'
        flags.append('scope_review: non-real-number classification extends explicit real-number objective')
    if family == 'income_taxes_bills' and level == 3:
        spec = '~1l.6'
        flags.append('response_mode_gap: prose tax rule does not assess tax-table interpretation')
    if family == 'expressions_formulae' and level == 1:
        spec = '~6a.1'
    if family == 'algebraic_manipulation_expansion' and skill == 'collect_like_terms':
        spec = '~6a.1'
    if family == 'simple_probability':
        if machine.get('task') in ('not_event',) or machine.get('kind') == 'complement':
            spec = '12b.1+12b.3'
        elif machine.get('task') == 'missing_probability':
            spec = '12b.3+12b.4'
        elif machine.get('task') == 'impossible':
            spec += '+12b.2'
    if family == 'elevation_depression_extended_ratios' and level == 3:
        angles = machine.get('angles', [machine.get('angle', 0)])
        if any(a > 90 for a in angles):
            spec += '+11main.4'
    if family == 'transformations_coordinates' and skill == 'reflect_points':
        line = str(machine.get('line', [''])[0])
        if line in ('y=x', 'y=-x'):
            spec = '9b.5+~9b.1'
            flags.append('scope_review: diagonal reflection exceeds explicitly named horizontal/vertical reflection sub-bullet')
    if family == 'circles_arcs_sectors' and skill == 'segment_area':
        spec = '4main.2+11main.5'
    if family == 'surface_area_volume':
        task = machine.get('task')
        if task == 'cylinder':
            spec = '4main.1'
        if task in ('cylinder_hemisphere', 'silo_curved'):
            spec += '+4main.3'
        if task == 'litres':
            spec += '+3main.2'
    if family == 'ratios_scales_rates' and skill == 'share_in_ratio':
        spec = '1j.1+1j.2'
    if family == 'time_clocks_timetables' and level == 5:
        spec = '3main.3+~3main.4'
    if family == 'symmetry_circles':
        spec += '+5c.2'
    if family in ('visual_practical_graphs', 'visual_straight_lines', 'visual_quadratics',
                  'visual_advanced_graphs', 'visual_transformations', 'visual_linear_programming'):
        # These explicitly use Cartesian plots, not just numeric coordinate formulae.
        spec += '+~7a.1'
    direct, support = parse_spec(spec)
    support = [x for x in support if x not in direct]
    return {'assessed_objective_ids': sorted(set(direct)),
            'supporting_objective_ids': sorted(set(support)), 'review_flags': flags}
