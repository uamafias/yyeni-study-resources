"""Explicit applied-method achievement for each two-mark calculation branch.

These names refer to mathematical operations, independently of display-step or
dictionary order. Three-mark branches declare their own two named achievements.
"""
SETUP={
 'number_classifications_properties':{'*':'division'},
 'directed_numbers_in_action':{'*':'signed_change'},
 'fractions_decimals_percentages':{'*':'conversion','fraction_add':'denominator','fraction_sub':'denominator','whole_from_fraction':'unit'},
 'advanced_percentages':{'*':'percentage','increase':'part','decrease':'part','percentage_remaining':'part','reverse_increase':'reverse','reverse_decrease':'reverse','compound_amount':'compound','compound_interest':'compound','depreciation':'compound'},
 'standard_form_estimates_approximations':{'*':'evaluate','std_mul':'calculate','std_div':'calculate','ordinary_mul':'calculate','ordinary_div':'calculate'},
 'limits_of_accuracy':{'*':'extremise'},
 'ratios_scales_rates':{'*':'apply_rate','share_in_ratio':'unit','ratio_find_other':'unit','ratio_find_total':'unit','actual_to_map':'scale','map_to_actual':'scale','speed_unit_conversion':'rate','total_distance':'leg_distances'},
 'personal_finance_currency':{'change':'costs','compound_interest':'compound','currency':'convert','simple_interest':'interest'},
 'income_taxes_bills':{'*':'charge'},
 'venn_diagrams':{'find_both':'union'},
 'metric_units_conversions':{'*':'convert','density':'compound','density_back':'compound'},
 'time_clocks_timetables':{'*':'duration'},
 'perimeters_areas_polygons':{'*':'measure','trapezium_area':'apply','trapezium_height':'apply'},
 'circles_arcs_sectors':{'*':'circle','radius_from_area':'radius','radius_from_circumference':'radius','angle_from_arc':'fraction','angle_from_area':'fraction','sector_arc':'sector','sector_area':'sector'},
 'surface_area_volume':{'*':'solid'},
 'similarity_scale_factors':{'similar_lengths':'similarity','area_from_heights':'measure','height_from_areas':'linear'},
 'constructions_scale_drawings':{'*':'geometric_property'},
 'bisectors_numeric':{'*':'geometric_property','pythagoras':'right_triangle','bdc':'triangle'},
 'symmetry_two_dimensions':{'*':'geometric_property'},
 'symmetry_circles':{'*':'geometric_property'},
 'angles_lines_polygons':{'*':'angles'},
 'angles_circles':{'*':'circle_angle'},
 'expressions_formulae':{'expand_and_simplify':'expand','substitute':'substitution','change_subject':'undo'},
 'algebraic_manipulation_expansion':{'*':'distribute','divide_algebraic_fraction':'reciprocal'},
 'linear_simultaneous_equations':{'*':'equation'},
 'solving_quadratic_equations':{'solve_square':'square'},
 'inequalities_indices':{'*':'bounds','exponential_linear':'base','exponential_simple':'base'},
 'sequences':{'ap_sum':'sum','nth_term':'difference'},
 'logarithms':{'split_log':'product_quotient','log_in_terms_of_m':'power'},
 'functions':{'inverse_linear':'swap','composite_value':'inner','composite_linear':'inner','solve_function_equation':'equate'},
 'kinematics_rate_change':{'*':'rate_or_area'},
 'introduction_functions':{'*':'equation'},
 'linear_programming':{'test_points':'conditions'},
 'histograms_text':{'*':'histogram_measure'},
 'reading_charts_text':{'*':'read_or_calculate','pictogram_key':'key'},
 'prepared_line_graphs':{'*':'read'},
 'straight_line_graphs_gradients':{'*':'line','gradient_two_points':'changes','gradient_general_form':'rearrange','intercept_general_form':'rearrange','find_intercept_constant':'point'},
 'sketching_quadratics_gradients':{'chord_gradient':'values'},
 'advanced_graphs':{'*':'relationship'},
 'distance_midpoint_gradient':{'*':'differences','find_missing_coordinate_gradient':'displacement'},
 'equations_of_straight_lines':{'*':'point'},
 'parallel_perpendicular_quadrilaterals':{'*':'relationship'},
 'vector_operations_magnitude':{'*':'vector'},
 'position_vectors':{'*':'ratio'},
 'matrix_multiplication':{'*':'entry'},
 'determinants_inverses':{'*':'det_equation'},
 'bearings_right_angled_triangles':{'*':'relationship'},
 'elevation_depression_extended_ratios':{'*':'ratio','calculator_difference':'evaluate','calculator_fraction':'evaluate'},
 'sine_cosine_rules':{'*':'rule','area':'area_or_diagonal','area_exact':'area_or_diagonal','pyramid_diagonal':'area_or_diagonal'},
 'mean_median_mode_range':{'mean':'total','missing_value':'totals'},
 'grouped_data_mean':{'*':'count'},
 'cumulative_frequency_reading':{'*':'cumulative'},
 'simple_probability':{'*':'counts'},
 'tree_diagrams':{'*':'branches','all_three':'event','at_least_one':'event','both_same':'event','joint_late':'event'},
}


def setup_key(problem):
    family=problem.generator_id.removeprefix('nssco_');task=problem.machine.get('task',problem.skill)
    if family=='expressions_formulae' and task=='change_subject':
        if problem.machine['form']=='t = k sqrt(y)':return 'divide'
        if problem.machine['form'].startswith('A = sqrt'):return 'square'
    mapping=SETUP.get(family,{})
    key=mapping.get(task,mapping.get('*'))
    if key is None:raise ValueError(f'Unmapped applied-method achievement: {family}/{task}')
    return key
