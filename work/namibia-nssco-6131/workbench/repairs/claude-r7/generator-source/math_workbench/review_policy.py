"""Correction notices for immutable historical marking evidence."""
HISTORICAL_LP_NOTE=('This saved question used an older explanation of solid and broken boundaries. '
    'For a non-strict inequality the boundary is solid. The original result is preserved; '
    'a teacher must review it before any regrade.')


def historical_lp_notice(contract):
    if not isinstance(contract,dict) or contract.get('generator_id')!='nssco_visual_linear_programming' or contract.get('generator_version')!=1:return ''
    from services.math_generators import generate_problem
    try:problem=generate_problem(contract['generator_id'],contract['seed'],contract['level'])
    except (ValueError,KeyError,TypeError):return HISTORICAL_LP_NOTE
    return HISTORICAL_LP_NOTE if problem.machine.get('strict') is False else ''


def question_notice(question):
    return historical_lp_notice(question.get('grading_contract',{}).get('source_marking_contract'))
