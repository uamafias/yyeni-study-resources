"""Written conceptual responses and teaching explanations for fixed examples."""
from .family_functions_concepts import GENERATOR_ID


def content(problem):
    if problem.generator_id != GENERATOR_ID:
        return None
    return problem.answer, problem.machine['explanation']


def marking_achievements(problem):
    """Authored achievements, bound to the actual mapping; no keyword marker."""
    m=problem.machine; task=m['task']
    if task=='relation_function':
        return [
            'Defines a function as assigning exactly one output in B to every input in A; equivalent wording is accepted.',
            'Correctly states that this relation '+('is' if m['is_function'] else 'is not')+' a function from A to B.',
            'Justifies the decision using this mapping: '+m['reason']+' Do not reject a function merely for shared outputs or unused codomain elements.']
    if task=='mapping_notation':
        return [
            f'Rewrites the complete rule in the requested notation: ${m["written"]}$. Equivalent spacing, arrow glyph or algebra is accepted; the assignment direction and function name must be clear.',
            f'Correct output ${m["output"]}$ for input ${m["input"]}$. This is an independent value award, not a method/result calculation tariff.']
    if task=='one_one_mapping':
        return [
            'Explains one-one as different inputs producing different outputs; equivalent definition or a clear instance-specific explanation is accepted.',
            'Correctly classifies this function as '+('one-one' if m['one_one'] else 'not one-one')+' and supports it from the complete mapping: '+m['reason'],
            'Correct inverse-function conclusion, including why reversing these arrows is '+('unambiguous' if m['one_one'] else 'not single-valued')+'. '+m['inverse_reason']]
    if task=='one_one_domain':
        return [
            'Correctly classifies the rule on the stated domain as '+('one-one' if m['one_one'] else 'not one-one')+'.',
            'Gives a valid domain-aware reason: '+m['reason']+' Equivalent valid distinct-input examples or monotonicity reasoning are accepted. A single evaluated input does not prove one-one.',
            'Correctly concludes that an inverse function '+('exists' if m['one_one'] else 'does not exist')+' on the range, linking this to unique recovery of the original input.']
    if task=='inverse_meaning':
        return [
            'Explains that the inverse reverses the original function, taking each reached output back to its unique original input; it is not the reciprocal.',
            f'Correct inverse value $f^{{-1}}({m["output"]})={m["input"]}$. Accept reversal, solving an equation or an equivalent valid inverse rule. This is an independent requested value award.']
    if task=='composite_meaning':
        outer,inner=m['order']
        return [
            f'Explains composition as using the output of ${inner}$ as the input to ${outer}$, in that order; identifies the composite as ${m["order"]}$. Equivalent arrow-chain descriptions accepted.',
            f'Correct mapping rule for ${m["order"]}$, with coefficient ${m["coefficient"]}$ and constant ${m["constant"]}$. Equivalent expanded or unexpanded forms accepted; function name and mapping direction must be clear.',
            f'Correct final composite output ${m["output"]}$ for input ${m["input"]}$. Do not award for the intermediate output ${m["intermediate"]}$ alone.']
    raise ValueError(f'Unsupported Functions concepts task: {task}')
