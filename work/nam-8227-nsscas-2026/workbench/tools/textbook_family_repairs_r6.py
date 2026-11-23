"""Explicit author repairs to R5 families; never relabel accepted source items.

Applied after the original authored groups and extensions are assembled. Splits
name source responses, preserve their connected items, and record the changed
learner decision. This is an analysis repair, not a recipe taxonomy generator.
"""
import copy
import hashlib
import json

PREFIX = '8227:TEXTBOOK-FAMILY:'


def D(s):
    return '8227:2020:' + s


def member_id(family_id, item_id, labels):
    body=json.dumps([family_id,item_id,sorted(labels)],ensure_ascii=False,separators=(',',':'))
    return '8227:TB-EXAM-MEMBER:'+hashlib.sha256(body.encode()).hexdigest()[:20]


def validate_member_demands(family, item):
    """A family union cannot conceal an unsupported per-member claim."""
    missing=set(family['assessed_demand_ids'])-set(item['assessed_8227_demand_ids'])
    if missing:
        from pathlib import Path
        wb=Path(__file__).resolve().parents[1]
        specs=json.loads((wb/'tools/textbook-family-repairs-r7.json').read_text()).get('family_response_demand_exceptions',[]) if (wb/'tools/textbook-family-repairs-r7.json').exists() else []
        matches=[m for m in family.get('members',[]) if m['item_id']==item['item_id']]
        approved=bool(matches) and all(m.get('family_response_demand_evidence_r7') in specs and set(m.get('family_response_demand_evidence_r7',{}).get('demand_ids',[]))==missing for m in matches)
        if approved:
            from apply_textbook_family_repairs_r7 import _verify_native
            for m in matches:_verify_native(m['family_response_demand_evidence_r7']['native_evidence'],wb)
            return
    assert not missing, ('family demand unsupported by member',family['family_id'],item['item_id'],sorted(missing))


def validate_response_disposition(family, member, item):
    selected=set(member['part_labels'])
    for response in item.get('answer_verification_r5',[]):
        if response['subpart'] not in selected:
            continue
        if 'defective finite' in response.get('source_interpretation','').lower():
            assert not family['assessed_demand_ids'], \
                'defective finite-integral response counted as valid practice'


def apply_repairs(raw, items):
    raw = copy.deepcopy(raw)
    changes = []

    def row(slug):
        return raw[PREFIX + slug]

    def labels(spec):
        return ([a['subpart'] for a in items[spec['item_id']]['answer_verification_r5']]
                if spec['parts'] == '*' else list(spec['parts']))

    def revise(slug, reason, demands=None, **fields):
        f = row(slug)
        if demands is not None:
            f['assessed_demand_ids'] = [D(d) for d in demands]
        f.update(fields)
        f.setdefault('membership_repairs_r6', []).append(reason)
        changes.append(dict(family_id=f['family_id'], action='revise', reason=reason))

    def fork(source, target, title, decisions, demands, distinction, **fields):
        assert PREFIX + target not in raw, target
        f = copy.deepcopy(row(source))
        f.update(family_id=PREFIX + target, title=title,
                 learner_decisions=decisions, assessed_demand_ids=[D(d) for d in demands],
                 member_specs=[], distinction_basis=distinction,
                 r6_origin_family_id=f.get('r6_origin_family_id', PREFIX + source),
                 membership_repairs_r6=[distinction],
                 difficulty_progression='single item')
        # R5 exam links are not transferable to a task created by a split.
        f['examination_relation'] = dict(kind='textbook-only', part_ids=[], pattern_ids=[],
            evidence_label='textbook-derived',
            reason='Uncompared R6 split; no examination equivalence claimed at this checkpoint.')
        f['r6_comparison_status'] = 'not yet compared; not a final textbook-only disposition'
        f.update(fields)
        raw[f['family_id']] = f
        changes.append(dict(family_id=f['family_id'], action='create split', source=PREFIX+source,
                            reason=distinction))

    def move(source, target, iid, reason, selected=None):
        matches=[s for s in row(source)['member_specs'] if s['item_id']==iid]
        assert len(matches)==1, (source, iid, len(matches))
        spec=matches[0]
        old=labels(spec)
        chosen=old if selected is None else list(selected)
        assert chosen and set(chosen)<=set(old), (source,iid,chosen,old)
        dest=copy.deepcopy(spec)
        dest.update(parts=chosen, membership_reason=reason)
        row(target)['member_specs'].append(dest)
        rest=[s for s in old if s not in chosen]
        if rest:
            spec['parts']=rest
        else:
            row(source)['member_specs'].remove(spec)
        changes.append(dict(action='move responses', source=PREFIX+source, target=PREFIX+target,
                            item_id=iid, part_labels=chosen, reason=reason))

    # B.1 numerical execution is distinct from justifying a supplied equation.
    source='numerical-supplied-map-chain'
    fork(source, 'numerical-supplied-map-execution',
         'Execute a supplied recurrence without a rearrangement proof',
         'Use the given recurrence on its real domain, retain the prescribed start '
         'and intermediate precision, and certify the selected root at the final precision.',
         ['M2:T6:O04:D01','M2:T6:O04:D02'],
         'Unlike numerical-supplied-map-chain, the selected responses do not ask the learner '
         'to establish the supplied rearrangement; graph and bracket preparation stays connected.',
         scaffolding_and_connected_parts='Retain any preceding graph or sign bracket. '
         'The iteration is assessed; an unasked rearrangement proof is not added.',
         answer_form='Required iterates and correctly rounded target root, with any preceding source responses.',
         difficulty_progression='Begin with the explicit cube-root map in Goldie 6B Q1, '
         'then an exponential map in Q3; the radian map and longer stopping trace add domain/precision demands.')
    no_proof=[
        'Goldie:C6:Exercise-6B:1','Goldie:C6:Exercise-6B:3',
        'Goldie:C6:Exercise-6B:7','Goldie:C6:Exercise-6B:14',
        'Goldie:C6:Exercise-6B:5','YM:C13:Try-Now-5:2',
        'YM:C13:Exercise-13:1','YM:C13:Try-Now:11',
        'Goldie:C8:Exercise-8G:9']
    for short in no_proof:
        move(source,'numerical-supplied-map-execution','8227:TB:'+short,
             'The selected source responses execute a supplied recurrence and round the root; '
             'they do not request an algebraic rearrangement proof.')
    fork(source,'numerical-conditional-limit-chain',
         'Infer a fixed-point relation from a convergent supplied iteration',
         'After the graph/bracket tasks, assume the stated sequence converges, pass to '
         'its limit and recover the original equation before carrying out the iterations.',
         ['M2:T6:O03:D01','M2:T6:O04:D01','M2:T6:O04:D02'],
         'A conditional limit implication is required; unlike the sibling rearrangement '
         'family, the task does not ask for globally equivalent equation rearrangement.')
    for short in ['Goldie:C6:Exercise-6B:10','Goldie:C6:Exercise-6B:13','Goldie:C6:Exercise-6B:15']:
        move(source,'numerical-conditional-limit-chain','8227:TB:'+short,
             'The source asks what the given iteration implies if it converges, then '
             'requires its numerical execution; retain that direction of reasoning.')
    revise(source,'Execution-only and conditional-limit tasks moved to their own siblings.',
           demands=['M2:T6:O03:D02','M2:T6:O04:D01','M2:T6:O04:D02'],
           learner_decisions='Establish the requested supplied rearrangement on its '
           'admissible branch, then execute the recurrence and certify the target-root precision.')

    # B.1 factor-to-roots, count by discriminant, and roots-to-equation are distinct.
    source='polynomial-factor-solve'
    fork(source,'polynomial-equation-from-roots',
         'Construct a polynomial equation from its prescribed roots',
         'Expand the given root factors and identify the polynomial whose zero set '
         'has those roots; preserve the coefficient of the leading term.',
         ['M1:T1:O05:D01'],
         'This reverses polynomial-factor-solve: roots are given and coefficients '
         'are the output, rather than roots being recovered from a polynomial.',
         givens_and_unknowns='Given root symbols alpha and beta; unknown expanded '
         'monic quadratic equation. Only the retained real-root facet is used.',
         representation_and_response='Symbolic root factors to an expanded polynomial equation.',
         scaffolding_and_connected_parts='Expansion precedes the equation deduction; '
         'later excluded complex-root examples remain outside this membership.',
         alternative_methods='Direct multiplication or coefficient comparison from '
         '(z-alpha)(z-beta); no solving for unknown roots.',
         answer_form='z^2-(alpha+beta)z+alpha beta=0.')
    move(source,'polynomial-equation-from-roots','8227:TB:Goldie:C11:Exercise-11B:9',
         'The retained part expands prescribed root factors to deduce their equation, '
         'the reverse of finding roots of a supplied polynomial.')
    fork(source,'polynomial-one-real-factor-proof',
         'Prove a cubic has no other real linear factor',
         'Establish the supplied real factor, divide it out, and use the remaining '
         'quadratic discriminant to prove that no further real linear factor exists.',
         ['M2:T1:O04:D02','M1:T1:O02:D02'],
         'Unlike listing polynomial roots, the final requested evidence is a '
         'negative-discriminant proof excluding further real factors.',
         answer_form='Factor confirmation, remaining quadratic and no-other-real-root proof.',
         scaffolding_and_connected_parts='Keep factor proof before the discriminant conclusion.')
    for short in ['YM:C8:Example:25','YM:C8:Try-Now-25:1']:
        move(source,'polynomial-one-real-factor-proof','8227:TB:'+short,
             'The supplied factor is proved, then irreducibility of the residual '
             'quadratic is established; the source asks for a proof, not three root values.')
    move(source,'polynomial-factorisation','8227:TB:YM:C8:Revision-Exercise-8:5',
         'The requested final output is a complete factorisation after coefficient '
         'recovery and a supplied-factor proof; no root list is requested.')
    revise(source,'Reverse construction, irreducibility proofs and factorisation-only '
           'outputs moved; all remaining items ask for a complete root set.',
           demands=['M2:T1:O04:D04'])

    # B.1 only the identity-dependent responses belong to the secant family.
    for short in ['Goldie:C5:Exercise-5B:9','Goldie:C5:Exercise-5B:10']:
        target='elementary-trig-definite' if short.endswith(':9') else 'elementary-exponential-primitives'
        move('secant-identity-integral',target,'8227:TB:'+short,
             'Part (i) is an elementary integral without an identity choice; '
             'part (ii), which chooses tan-squared = sec-squared minus one, stays in the identity family.',
             selected=['i'])
    for short in ['YM:C12:Example:12','YM:C12:Try-Now:12']:
        move('secant-identity-integral','elementary-trig-primitives','8227:TB:'+short,
             'Part (b) rewrites reciprocal cosine-squared and reverses the affine '
             'secant-squared derivative; it does not choose a Pythagorean identity.', selected=['b'])
    revise('secant-identity-integral','Named identity-free responses moved to elementary '
           'trig/exponential siblings; membership now names the actual identity choice.')

    # B.1 parameter elimination does not require a plot or derivative.
    fork('parametric-point-plot-support','parametric-elimination-support',
         'Eliminate a parameter without plotting or differentiating',
         'Solve the directly invertible coordinate for the parameter and substitute '
         'into the other coordinate, keeping the requested dependent-variable direction.',[],
         'Unlike parametric-point-plot-support, the requested output is one Cartesian '
         'relation and no points, sketch or derivative are required.',
         givens_and_unknowns='x=t^3-2t^2 and y=t/2; unknown x as an expression in y.',
         representation_and_response='Two symbolic parametric rules to one Cartesian rule.',
         scaffolding_and_connected_parts='One elimination response; do not attach the '
         'following parametric differentiation exposition to this worked example.',
         alternative_methods='Substitute t=2y into the x rule.',
         answer_form='x=8y^3-8y^2; supporting manipulation, not an assessed derivative demand.')
    move('parametric-point-plot-support','parametric-elimination-support',
         '8227:TB:Goldie:C4:Example:21',
         'Example 4.21 asks only to eliminate t; it supplies no plotting task.')

    # B.2 split three genuinely different responses previously grouped by topic.
    source='natural-log-exponential-values'
    fork(source,'natural-exponential-supplied-model-evaluation',
         'Evaluate a supplied exponential model at stated times',
         'Substitute each stated time into the given exponential model and interpret '
         'the output in its original physical unit; no model fitting is asked.',
         ['M2:T2:O02:D01'],
         'Unlike natural-log-exponential-values, the input is a named model and '
         'the response must interpret a physical quantity and its scale.',
         units_and_precision='Keep P in millions and M in grams, with t in years; '
         'do not turn the population scale into individual units without conversion.',
         answer_form='Initial and later model values with their original units.')
    fork(source,'natural-inverse-exact-simplification',
         'Use the natural inverse relation without a calculator',
         'Cancel exp and ln on their valid positive domain, while retaining outside '
         'multipliers, negative signs and fractional exponent factors.',
         ['M2:T2:O02:D01'],
         'Unlike calculator evaluation, the requested evidence is exact inverse-law '
         'simplification with no decimal approximation.',
         representation_and_response='Symbolic expressions to exact simplified values.',
         units_and_precision='Dimensionless natural exponent/log arguments; exact '
         'answers and y>0 for exp(ln y), with no significant-figure rounding.',
         answer_form='Exact numbers or the original positive symbol.')
    for n in [18,20]:
        for kind in ['Example','Try-Now']:
            target=('natural-exponential-supplied-model-evaluation' if n==18
                    else 'natural-inverse-exact-simplification')
            move(source,target,f'8227:TB:YM:C9:{kind}:{n}',
                 'The selected source asks for '+('time substitution and physical '
                 'interpretation of a fully supplied model.' if n==18 else
                 'exact exp/ln inverse simplification without a calculator.'))
    revise(source,'Model evaluation and exact inverse-law tasks moved to separate '
           'decision families; this sibling contains calculator evaluations only.',
           title='Evaluate natural exponentials and logarithms with a calculator',
           learner_decisions='Enter the given exponential or natural logarithm '
           'correctly, admit positive log arguments below one, and round nonexact values to 3 significant figures.',
           units_and_precision='Dimensionless arguments; 3 significant figures '
           'for nonexact values. ln(e)=1 and ln(1)=0 remain exact.',
           answer_form='Requested calculator values; exact zero is not an instruction to invent trailing significant figures.')

    source='mixed-retained-definite-integrals'
    # Preserve the four eligible responses, but compare their actual operations.
    fork(source,'rational-linear-numerator-definite-integral',
         'Reduce a proper linear-over-linear definite integral before evaluating',
         'Divide the affine numerator by its affine denominator to obtain a '
         'constant plus reciprocal-linear term, then evaluate the exact endpoint difference.',
         ['M1:T9:O03:D01','M2:T5:O01:D01'],
         'Unlike the plain reciprocal-linear integral, a nonconstant numerator '
         'requires division before the logarithmic primitive.',
         givens_and_unknowns='9x/(3x-8) integrated from 8 to 24; unknown exact integral.',
         representation_and_response='A proper definite rational integral to algebraic '
         'reduction and an exact value.',
         alternative_methods='9x/(3x-8)=3+24/(3x-8); integrate the constant and logarithmic term.',
         answer_form='Exact polynomial-plus-log endpoint result.',
         units_and_precision='Exact result with ln 4; no physical units or decimal rounding required.')
    move(source,'proper-power-definite-integral','8227:TB:Goldie:C8:Exercise-8H:2',
         'Part (i) is a proper affine reciprocal-square-root integral on 8..24; '
         'its radicand never vanishes on this interval.', selected=['i'])
    move(source,'elementary-reciprocal-definite-logform','8227:TB:Goldie:C8:Exercise-8H:2',
         'Part (ii) is a proper reciprocal-linear exact logarithmic integral; '
         'it requires no trig identity or numerator division.', selected=['ii'])
    move(source,'rational-linear-numerator-definite-integral','8227:TB:Goldie:C8:Exercise-8H:2',
         'Part (iii) requires reducing 9x/(3x-8) before exact evaluation.', selected=['iii'])
    move(source,'trig-square-power-reduction-integral','8227:TB:Goldie:C8:Exercise-8H:2',
         'Part (iv) integrates sin^3 x over 0..pi/2 by a finite harmonic identity; '
         'it is not a rational/logarithmic integral.', selected=['iv'])
    assert not row(source)['member_specs']
    del raw[PREFIX+source]
    changes.append(dict(action='retire mixed revision grouping', family_id=PREFIX+source,
                        reason='All four eligible responses moved to decision-specific families.'))

    # Explicit common assessed outputs, rather than a union of every method used
    # somewhere in the group. Component/secondary support remains on the source
    # item and is not erased by narrowing a family's common demand claim.
    common_outputs = [
        ('reciprocal-sign-and-graph',['M2:T3:O01:D02'],
         'All members interpret reciprocal-function properties or draw their branches; a separate reciprocal-ratio calculation is not requested by every sketch.'),
        ('compound-parameter-ratio-chain',['M2:T3:O02:D02'],
         'Compound-angle use is common. Some members solve ordered angle pairs rather than request the general exact-evaluation demand as a separate output.'),
        ('quadratic-parameter-conditions',['M1:T1:O02:D02','M1:T1:O02:D03'],
         'Every member interprets root nature to restrict a parameter; not every member asks for a separately reported discriminant value.'),
        ('trig-formula-restricted-sketch',['M1:T6:O02:D03'],
         'The common assessed output is the restricted sketch. Amplitude and period are not separate outputs for every tangent or shifted-cosine member.'),
        ('trig-given-graph-reading',['M1:T6:O02:D02'],
         'All members recover information from a given transformed graph; amplitude/period is not requested by the fixed-frequency sine-parameter task.'),
        ('sector-perimeter-inverse',['M1:T5:O02:D01'],
         'The common requested result is an arc-based perimeter. A supplied sector area may be used to recover the angle without being a separate area output.'),
        ('elementary-composite-derivative',['M2:T4:O01:D02'],
         'Every selected response differentiates a composite elementary function; separate standard-rule recall is not an additional requested output in all items.'),
        ('reciprocal-trig-derivation',['M2:T4:O02:D02'],
         'The requested derivation uses the quotient rule. Do not require each source to carry a second direct standard-derivative output.'),
        ('function-natural-inverse',['M1:T3:O03:D02'],
         'Finding the inverse is common; a separately stated original-function domain is not requested in all source items.'),
        ('function-quadratic-branch-inverse',['M1:T3:O03:D02'],
         'The common target is the correctly restricted inverse. Some sources ask injectivity, others give the branch and ask the image; neither is universal.'),
        ('function-composition-admissibility',['M1:T3:O04:D02'],
         'Admissibility of the composition is common. Domain determination and explicit range calculation vary with the source scaffolding.'),
        ('implicit-point-gradient-line',['M2:T4:O03:D03'],
         'The requested common output is a geometric slope or line on an implicit curve, not a separately reported general derivative in every source.'),
        ('implicit-horizontal-and-singular',['M2:T4:O03:D03'],
         'The source asks for stationary/horizontal evidence on the original implicit curve; an extra general derivative output is not imposed.'),
        ('parametric-fixed-parameter-line',['M2:T4:O03:D03'],
         'Every member applies a parametric gradient geometrically at a specified parameter; not every task requests the derivative formula separately.'),
        ('parametric-prescribed-gradient',['M2:T4:O03:D03'],
         'Every member imposes a prescribed parametric gradient; the parameter versus coordinate output remains an explicit source response distinction.'),
        ('parametric-horizontal-vertical-stationary',['M2:T4:O03:D03'],
         'The common demand is a geometric stationary/tangent condition with the actual parameter regularity tests, not a separate derivative-formula output.'),
        ('logarithm-data-model-fit',['M2:T2:O04:D02'],
         'All members recover constants from straight-line information; the supplied semi-log graph does not ask the learner to perform a separate linearisation.'),
        ('numerical-graph-count-bracket',['M2:T6:O01:D01'],
         'The common assessed evidence is a graph-based root location/count; some source members contain no sign-bracket request.'),
        ('numerical-search-and-bisection',['M2:T6:O01:D02'],
         'Every member locates/refines a continuous bracket; the pure three-root cubic task does not ask for graphical estimation.'),
        ('numerical-given-map-to-equation',['M2:T6:O03:D01','M2:T6:O04:D01','M2:T6:O04:D02'],
         'All members execute the given map and infer its fixed-point equation. Supplied convergence is not an independently assessed convergence interpretation.'),
        ('polynomial-linear-division',['M2:T1:O03:D03'],
         'Quotient/remainder identification is common; some members request only the remainder and cannot inherit a separately requested full-division output.'),
        ('polynomial-quadratic-division',['M2:T1:O03:D03'],
         'The common requested output is the quotient and/or permissible-degree remainder under a quadratic divisor, not necessarily every worked division line.'),
        ('polynomial-inverse-remainder-constraints',['M2:T1:O04:D03'],
         'Every member determines coefficients from factor/remainder conditions; neither a factor proof nor a newly evaluated remainder is requested by all.'),
        ('polynomial-factor-sketch-chain',['M2:T1:O04:D04'],
         'Factoring to recover the real zeros is common before the sketch; a separately requested factor-theorem proof is not present in every source.'),
        ('modulus-equation-to-sketch',['M2:T1:O02:D01'],
         'The common response constructs a modulus graph from its formula. Reading unknown values from a supplied graph is not universal.'),
        ('stationary-analytic-targets',['M1:T8:O04:D01'],
         'All members locate stationary inputs/points. Nature may be given or not requested, so classification is no longer a blanket assessed claim.'),
        ('stationary-parameter-graph-recovery',['M1:T8:O04:D01'],
         'Every member uses a stationary constraint to recover coefficients; a given minimum does not automatically ask for a new classification proof.'),
        ('curve-first-derivative-point',['M1:T9:O02:D02'],
         'The common output is the curve through the prescribed point. Determining its constant is part of that recovery, not a separate universal response.'),
        ('binomial-product-coefficient',['M1:T2:O01:D03'],
         'Every member combines expansion contributions. Some ask selected coefficients directly, others supply ascending expansions first; those preliminary outputs differ.'),
        ('binomial-parameter-coefficients',['M1:T2:O01:D03'],
         'The common decision constructs and solves coefficient constraints. A separately requested chosen-term output is absent from several parameter-only sources.'),
        ('vector-endpoints-and-notation',['M1:T7:O03:D02'],
         'All members form a directed displacement. A position vector and explicit conversion between notation systems are not requested by every endpoint task.'),
        ('vector-polar-direction-and-drawing',['M1:T7:O04:D01'],
         'Magnitude and direction are requested; a supplied i,j expression is not automatically a separate notation-reading assessment.'),
        ('vector-linear-combinations',['M1:T7:O02:D01'],
         'All members add/subtract directed vectors; the pure sum and difference examples do not separately assess a scalar multiplier.'),
        ('vector-parallel-parameter',['M1:T7:O02:D03'],
         'All members impose geometric parallelism. Scaling is a valid internal method but is not a separate common requested output.'),
        ('vector-prescribed-angle-parameter',['M1:T7:O05:D01'],
         'Every member imposes a specified non-right angle or angle-bisector condition; perpendicularity is a distinct sibling, not a universal demand.')
    ]
    for slug,ds,reason in common_outputs:
        revise(slug,reason,demands=ds)

    def separate(source,target,title,decisions,demands,short_ids,reason,**fields):
        """An authored list, not a demand-signature clustering rule."""
        fork(source,target,title,decisions,demands,reason,**fields)
        for short in short_ids:
            move(source,target,'8227:TB:'+short,reason)

    separate('reciprocal-pythagorean-equations','reciprocal-standard-bounded-equations',
        'Solve a standard reciprocal-ratio equation on a full cycle',
        'Invert the given secant, cosecant or cotangent value and enumerate all '
        'admissible full-cycle roots; exclude the original poles.',
        ['M2:T3:O01:D01','M1:T6:O06:D01','M1:T6:O06:D02'],
        ['Goldie:C3:Exercise-3A:1'],
        'Unlike reciprocal-pythagorean-equations, the ratio is already isolated '
        'and no Pythagorean identity choice is required.')
    separate('compound-bounded-equations','trig-equation-witness-investigation',
        'Find one angle satisfying a shifted trigonometric equality',
        'Find a witness for the supplied shifted-angle equality; distinguish '
        'one successful angle from a complete bounded solution set.',
        ['M1:T6:O06:D01'],['Goldie:C3:Activity:1'],
        'The exploratory activity asks for an angle, not every root on a stated '
        'interval or a prescribed compound-angle derivation.')
    move('advanced-double-triple-proof','compound-identity-proof',
        '8227:TB:YM:C10:Example:15',
        'The triple-tangent identity is a compound-angle proof on its common '
        'domain; the accepted mapping does not assess double-angle recall separately.')
    separate('inverse-tangent-retained-facets','inverse-tangent-identity-proof',
        'Prove an exact inverse-tangent identity with range justification',
        'Use the allowed ordinary-trig route and check the principal range '
        'when proving the exact inverse-tangent identity.',
        ['M2:T3:O02:D05'],['Goldie:C11:Exercise-11E:8'],
        'This is a general identity proof, unlike direct evaluation of a '
        'principal inverse value; the excluded complex-number lead-in is retained as a scope boundary.')
    separate('inverse-tangent-retained-facets','complex-context-trig-conclusion-support',
        'Retain ordinary-trig conclusions from a complex-number source',
        'Check the exact sine/cosine or inverse-tangent conclusion as supporting '
        'evidence while preserving the source-forced complex method exclusion.',[],
        ['Goldie:C11:Exercise-11G:5','Goldie:C11:Exercise-11G:9'],
        'These are retained conclusion checks with no accepted direct 8227 demand; '
        'they must not inherit principal-value assessment from the neighbouring item.')
    separate('completed-square-interpretation','quadratic-completion-coefficients',
        'Complete a square and report its prescribed constants',
        'Match the scaled completed-square template and identify its constants '
        'without adding an unasked vertex or extremum output.',
        ['M1:T1:O01:D01'],['YM:C1:Exercise-1:13'],
        'Unlike completed-square-interpretation, the source stops at the '
        'completed form and constants rather than asking for the vertex.')
    separate('completed-square-interpretation','quadratic-difference-extreme',
        'Find the greatest value of a difference after coefficient recovery',
        'Use the previously recovered coefficients, cancel the cubic terms '
        'and find the extreme ordinate of the resulting quadratic.',
        ['M1:T1:O01:D02'],['Goldie:C1:Exercise-1B:23'],
        'The quadratic is derived from two recovered polynomials rather than '
        'supplied for an explicitly requested square completion.')

    # Intersection cardinality changes the discriminant decision: equality,
    # positive, and negative conditions are not one undifferentiated task.
    source='line-curve-parameter-contact'
    tangencies=['YM:C1:Example:31','YM:C1:Try-Now-31:1','YM:C1:Try-Now-31:2',
                'YM:C1:Try-Now-31:3','YM:C1:Exercise-1:20','YM:C1:Example:38']
    separate(source,'line-curve-tangency-parameter',
        'Recover a parameter from a repeated intersection root',
        'Eliminate one variable, impose a repeated real root and check any '
        'exceptional parameter that changes the eliminated equation degree.',
        ['M1:T4:O02:D02'],tangencies,
        'Tangency requires discriminant zero and geometric validity; unlike '
        'the nonintersection sibling it does not require a negative discriminant.')
    separate(source,'line-curve-no-intersection-parameter',
        'Find all parameter values giving no real intersection',
        'Eliminate one coordinate, impose no real root on the original domain '
        'and express the full strict parameter range.',
        ['M1:T4:O02:D01'],
        ['YM:C1:Example:33','YM:C1:Try-Now-33:1','YM:C1:Try-Now-33:2',
         'YM:C1:Try-Now-33:3','YM:C1:Try-Now-33:4',
         'YM:C1:Revision-Exercise-1:2','YM:C3:Try-Now:22'],
        'No intersection is an absence-of-real-root condition, unlike the '
        'tangency equality or the two-distinct-intersections inequality.')
    revise(source,'Tangency-only and no-intersection tasks moved; the retained '
           'family imposes two distinct intersections.',demands=['M1:T4:O02:D01'],
           title='Find parameters giving two distinct curve-line intersections',
           learner_decisions='Eliminate one coordinate, require two distinct '
           'admissible real roots and retain exceptional-degree and domain restrictions.')
    separate('rational-specified-identity','given-rational-identity-verification-support',
        'Verify a fully supplied rational identity',
        'Clear the original nonzero denominators and check the fully supplied '
        'numerators; do not invent a request to determine unknown coefficients.',[],
        ['Goldie:C9:Exercise-9C:8'],
        'Unlike rational-specified-identity, all identity coefficients are '
        'supplied. This is retained algebra support, not a coefficient-solving demand.')
    separate('radical-equation-domain-filter','radical-original-domain-test',
        'Filter a radical equation using its original real domain',
        'Use the radicand and sign restrictions to rule out impossible values '
        'and verify all original-variable candidates.',
        ['M1:T1:O04:D03'],['YM:C1:Try-Now-10:2'],
        'The source includes a no-solution domain argument; it need not reduce '
        'every part to a quadratic transformed equation.')

    source='trig-graph-investigation'
    separate(source,'trig-basic-graph-feature-investigation',
        'Plot basic trig functions and read their feature tables',
        'Construct the basic graph on the given viewport and read its '
        'amplitude where defined, period, extrema and range.',
        ['M1:T6:O01:D01','M1:T6:O02:D01','M1:T6:O02:D02'],
        ['YM:C4:Investigation-basic-trig-graphs:1','YM:C4:Investigation-basic-trig-graphs:2'],
        'This plots the basic functions, unlike changing a scale or shift '
        'parameter and comparing transformed graphs.')
    separate(source,'trig-wide-window-periodicity-investigation',
        'Test periodicity by widening the graph viewport',
        'Compare repeated cycles on a wider viewing interval and explain why '
        'viewing more cycles does not change the period.',
        ['M1:T6:O01:D01','M1:T6:O02:D01'],
        ['YM:C4:Investigation-basic-trig-graphs:3'],
        'Changing the viewport asks for periodicity interpretation, not a '
        'change to the function or an algebraic transformation.')
    separate(source,'trig-output-shift-explanation',
        'Explain an output multiplier or vertical shift',
        'Use the compared source graphs to explain the specified positive '
        'output factor or vertical translation without claiming a changed period.',
        ['M1:T6:O02:D02'],
        ['YM:C4:Investigation-transformed-trig-graphs:3',
         'YM:C4:Investigation-transformed-trig-graphs:7'],
        'The requested response is an explanation, unlike the sibling '
        'investigation whose responses construct graphs and fill feature tables.')
    separate(source,'trig-input-scale-explanation',
        'Explain how an input multiplier changes the period',
        'Relate the supplied positive input multipliers to the new period '
        'and horizontal scale.',
        ['M1:T6:O02:D01','M1:T6:O02:D02'],
        ['YM:C4:Investigation-transformed-trig-graphs:5'],
        'Input scaling changes the period; this explanation differs from '
        'output scaling or translating the entire graph vertically.')
    revise(source,'Basic plots, wider-window exploration and explanation-only '
           'responses moved; retained members construct transformed plots/tables.',
           demands=['M1:T6:O02:D01','M1:T6:O02:D02','M1:T6:O02:D03'])
    separate('ratio-recovery-quadrant','inverse-angle-squared-ratio-evaluation',
        'Recover exact squared ratios from a supplied inverse angle',
        'Use the given sine ratio to calculate cosine-squared and tangent-squared; '
        'do not add an unasked signed quadrant choice.',
        ['M2:T3:O02:D05'],['YM:C4:Exercise-4.2:8'],
        'Squared ratios remove the sign ambiguity which distinguishes '
        'ratio-recovery-quadrant.')
    separate('bounded-affine-argument','trig-input-output-multiplier-illustrations',
        'Compare an acute solution under input versus output multiplication',
        'Track whether the multiplier acts on the ratio or its angle when '
        'recovering the single acute representative.',[],
        ['YM:C4:Illustration-multiplier-comparison:1','YM:C4:Illustration-multiplier-comparison:2'],
        'These are supporting acute illustrations with no stated full-solution '
        'interval; they cannot inherit bounded complete-root enumeration.')
    separate('trig-quadratic-reduction','trig-quadratic-unspecified-interval',
        'Reduce a trig equation when the source omits the solution interval',
        'Derive the requested quadratic in a trig ratio and distinguish '
        'admissible ratios from a complete angle solution set without given bounds.',
        ['M1:T6:O05:D02'],['YM:C4:Exercise-4.2:3'],
        'The source supplies no interval or angular unit; unlike the bounded '
        'sibling its one-cycle answer key cannot establish a complete root set.')
    separate('principal-inverse-values','principal-inverse-calculator-illustrations',
        'Read the single principal output in a calculator illustration',
        'Interpret the displayed asin, acos or atan calculator output as a '
        'principal value, without turning an unposed illustration into an assessed item.',[],
        ['YM:C4:Illustration-principal-value:1','YM:C4:Illustration-principal-value:2',
         'YM:C4:Illustration-principal-value:3'],
        'These are worked calculator demonstrations; principal-inverse-values '
        'contains explicitly posed principal-value responses.')
    separate('restricted-trig-function-inverse','restricted-trig-inverse-existence',
        'Decide inverse existence from a restricted trig graph',
        'Use the source interval, range and graph to decide one-to-one status '
        'rather than derive an unasked inverse formula.',
        ['M1:T3:O03:D01'],['YM:C4:Try-Now-55:3'],
        'The source asks whether an inverse exists; the sibling '
        'restricted-trig-function-inverse requires obtaining the inverse rule.')

    separate('elementary-reciprocal-definite-logform','cancelled-rational-definite-integral',
        'Cancel an original rational integrand before exact evaluation',
        'Factor and cancel the common factor on the proper original interval, '
        'then evaluate the resulting reciprocal-linear definite integral.',
        ['M1:T9:O03:D01'],['Goldie:C8:Exercise-8C:2'],
        'Unlike a supplied reciprocal-linear integrand, the original denominator '
        'is quadratic and must first be factored and cancelled.')
    revise('trig-square-power-reduction-integral',
        'The common operation is choosing a finite trig identity before integrating. '
        'The sin-cubed response uses harmonic reduction, not a separately universal double-angle formula output.',
        demands=['M2:T5:O02:D01'])
    revise('identity-hence-integral-chain',
        'All members prove a double-angle-based identity and use it for an exact '
        'definite integral. A free identity choice is not claimed where the identity is prescribed.',
        demands=['M2:T3:O02:D03','M1:T9:O03:D01'])
    separate('given-derivative-product-reversal','trig-derivative-hence-integrals',
        'Use a trig derivative and prescribed identities in connected integrals',
        'Differentiate tan(2x), reuse its scaled secant-squared primitive, then '
        'handle tangent-squared and the separately supplied double-angle identity.',
        ['M2:T5:O01:D02','M2:T5:O02:D01'],['YM:C12:Try-Now-17:1'],
        'This connected trig task does not isolate a target from a given product '
        'derivative, which is the defining reversal in given-derivative-product-reversal.')
    separate('elementary-area-inverse-bound','elementary-graph-area-bound-recovery',
        'Derive an area condition from a graph and recover its endpoint',
        'Read the actual region from the supplied graph, construct the signed '
        'area gap and impose the given area before solving or showing the endpoint relation.',
        ['M1:T9:O04:D01'],
        ['YM:C12:Example:5','YM:C12:Try-Now-5:1','YM:C12:Try-Now-5:2'],
        'Unlike the supplied-integral sibling, the learner must construct '
        'the integral from a region and choose the correct upper/lower boundary.')
    revise('elementary-area-inverse-bound',
        'Graph-derived areas moved; retained source members begin with an explicit integral condition.',
        title='Recover a bound from a supplied elementary integral condition',
        learner_decisions='Integrate the supplied expression, substitute its '
        'unknown bound and impose the given value before isolating the bound or proving the requested relation.')
    separate('trapezium-graph-bias-chain','trapezium-given-graph-bias-only',
        'Explain trapezium bias from supplied chord and curve graphs',
        'Compare trapezium chord tops with the given curve and decide '
        'underestimate, overestimate or insufficient evidence.',
        ['M2:T5:O04:D02'],['Goldie:C5:Prompt:4'],
        'This asks only for a bias explanation from a given graph, unlike '
        'setting ordinates and computing the estimate.')
    revise('trapezium-graph-bias-chain',
        'Given-graph bias-only response moved. Not every remaining source asks '
        'the learner to produce an integrand sketch.',
        demands=['M2:T5:O03:D01','M2:T5:O03:D02','M2:T5:O04:D02'])
    revise('trapezium-stationary-preparation',
        'All members prepare a stationary point then compute an estimate; '
        'bias justification is retained only where actually asked.',
        demands=['M1:T8:O04:D01','M2:T5:O03:D01','M2:T5:O03:D02'])
    separate('trapezium-exact-comparison','exact-integral-sketch-bias-without-estimate',
        'Use an exact integral and sketch to infer trapezium bias',
        'Evaluate the given exponential integral exactly, sketch its integrand '
        'and infer bias without adding an unasked numerical trapezium estimate.',
        ['M1:T9:O03:D01','M2:T5:O01:D01','M2:T5:O04:D01','M2:T5:O04:D02'],
        ['YM:C12:Exercise-12:10'],
        'The source asks no strip count or approximate total; unlike '
        'trapezium-exact-comparison, there are no two numerical results to compare.')
    separate('trapezium-refinement-limitations','trapezium-unposed-refinement-demonstration',
        'Follow a worked trapezium-refinement exposition',
        'Read the worked strip areas and successive refinements as teaching '
        'support, without turning an unposed demonstration into assessed questions.',[],
        ['Goldie:C5:Worked-illustration:1'],
        'The exposition supplies its calculation, whereas the refinement '
        'exercise family requires the learner to construct and justify estimates.')
    separate('trapezium-refinement-limitations','trapezium-geometric-reference-error',
        'Compare a supplied estimate with an independently found geometric area',
        'Recover the circle-segment area geometrically, then quantify the '
        'error of the already supplied sixteen-strip estimate.',
        ['M1:T9:O04:D01','M2:T5:O03:D02'],['Goldie:C5:Prompt:3'],
        'Unlike executing a refinement sequence, the estimate is given and '
        'the new decision is constructing an exact geometric reference.')
    separate('function-natural-domain-range','function-continuity-domain-explanation',
        'Explain denominator discontinuities and polynomial continuity',
        'Identify original denominator restrictions and explain why the '
        'given polynomial has no corresponding discontinuity.',
        ['M1:T3:O02:D01','M1:T3:O01:D01'],['Goldie:C5:Prompt:2'],
        'The prompt asks for continuity reasoning, not the attained image '
        'range required by function-natural-domain-range.')
    separate('function-decomposition-and-restricted-composite','function-known-composite-inverse-chain',
        'Compose known functions, invert the composite and solve their equality',
        'Form both ordered compositions from supplied rules, obtain the '
        'restricted composite inverse, then solve the specified composite equation.',
        ['M1:T3:O04:D01','M1:T3:O03:D02'],['YM:C3:Try-Now-14:2'],
        'Both original functions are supplied; unlike the decomposition '
        'sibling there is no missing inner rule to recover.')
    separate('function-decomposition-and-restricted-composite','function-composite-coefficient-recovery',
        'Recover function coefficients from composite values and injectivity',
        'Determine an injective branch of the quadratic, form the given '
        'composite value conditions and solve the correlated positive coefficients.',
        ['M1:T3:O04:D01','M1:T3:O03:D01'],['YM:C3:Exercise-3.1:4'],
        'The output is a coefficient pair from composite values; no composite '
        'inverse is requested, unlike function-decomposition-and-restricted-composite.')
    separate('function-piecewise-image-inverse','function-piecewise-sketch-domain-image',
        'Sketch a piecewise function and state its domain and image',
        'Draw each rule on its source interval, reconcile the shared endpoint '
        'and read the union of attained inputs and outputs.',
        ['M1:T3:O02:D01','M1:T3:O02:D02','M1:T3:O05:D01'],['YM:C3:Try-Now:15'],
        'This constructs the original graph; the inverse sibling starts '
        'from a supplied original graph and requires inverse rules and reflection.')
    revise('function-piecewise-image-inverse',
        'The sole inverse example starts with its original graph supplied; '
        'it does not ask for that original graph to be constructed.',
        demands=['M1:T3:O02:D02','M1:T3:O03:D02','M1:T3:O05:D02'])
    for slug in ['coordinate-midpoint-shape-recovery','coordinate-projection-ratio']:
        revise(slug,'The common source task solves intersections of constructed '
               'coordinate lines; source item mappings retain equation-translation support separately.',
               demands=['M1:T4:O02:D01'])
    move('explicit-prescribed-gradient-points','elementary-product-derivative',
        '8227:TB:Goldie:C8:Exercise-8G:11',
        'The retained part directly evaluates the derivative of a product at '
        'a prescribed input; it does not solve for a point with a prescribed gradient.')
    move('explicit-stationary-bounded-trig','explicit-prescribed-gradient-points',
        '8227:TB:YM:C11:Exercise-11:10',
        'The prescribed gradient is 3, not zero; R-form reduction recovers '
        'its bounded point inputs rather than stationary points.')
    separate('power-area-sign-and-shift','worked-radical-area-support',
        'Read a worked shifted-radical area illustration',
        'Follow the supplied proper-area calculation as teaching support; '
        'do not import the following optional substitution as a required method.',[],
        ['Goldie:C8:Worked-illustration:1'],
        'An unposed worked illustration has no accepted direct assessment '
        'link; the area-exercise sibling asks the learner to choose and evaluate the region.')
    move('logarithm-equation-domain-filter','exponential-logarithmic-solve',
        '8227:TB:Goldie:C2:Exercise-2D:12',
        'The natural logarithm is undone, then the remaining exponential '
        'equation is solved; this is not a multi-log combination task.')
    separate('logarithm-change-subject','exponential-natural-inverse-subject',
        'Isolate a subject by undoing an exponential or natural logarithm',
        'Isolate the natural exponential/log term and apply its inverse, '
        'retaining nonzero scale and positive log-ratio conditions.',
        ['M2:T2:O02:D01'],
        ['Goldie:C2:Exercise-2D:2','Goldie:C2:Exercise-2D:3','Goldie:C2:Exercise-2D:4'],
        'These use a natural inverse directly; the logarithm-change-subject '
        'sibling must combine multiple log terms before exponentiating.')
    revise('logarithm-change-subject',
        'Direct natural-inverse tasks moved; the retained sources apply log '
        'laws to isolate the requested subject.',demands=['M2:T2:O01:D02'])
    separate('exponential-logarithm-graph-transform','exponential-log-formula-sketch',
        'Construct transformed exponential or logarithmic graphs from formulas',
        'Transform the actual base graph, locate its shifted asymptote and '
        'axis crossing, and preserve the original log argument domain.',
        ['M1:T3:O05:D01'],
        ['Goldie:C2:Prompt:4','Goldie:C2:Exercise-2A:1','Goldie:C2:Exercise-2A:2',
         'Goldie:C2:Exercise-2B:6','Goldie:C2:Activity:3'],
        'These ask for constructing transformed formula graphs; the '
        'inverse-relation sibling directly interprets the exp/log inverse pair.')
    separate('exponential-logarithm-graph-transform','logarithm-graph-domain-properties',
        'Explain the domain and limiting properties of a logarithmic graph',
        'Justify the log-base graph domain, crossing, limiting sign and '
        'base point using the actual positive base restriction.',
        ['M2:T2:O01:D01','M1:T3:O02:D01'],['Goldie:C2:Prompt:2'],
        'This asks why graph properties hold rather than constructing a '
        'transformed curve or identifying its exponential inverse.')
    revise('exponential-log-inverse-chain',
        'The common assessed output is a restricted algebraic inverse; '
        'a graph or separate exp/log inverse-relation explanation is not universal.',
        demands=['M1:T3:O03:D02'])
    separate('exponential-graph-root-count','exponential-power-intersection-investigation',
        'Test intersection and ordering claims for exponential and power curves',
        'Compare the source graph pairs, count their intersections on the '
        'declared positive plotting domain and test the general parameter assertions.',
        ['M1:T4:O02:D01','M1:T3:O05:D01'],['Goldie:C2:Activity:1'],
        'This is a graph-comparison investigation with claims to test, '
        'rather than interpretation of an exponential/logarithmic inverse pair.')
    separate('numerical-iteration-fates','numerical-convergent-process-interpretation',
        'Interpret fixed points of supplied convergent calculator processes',
        'Track the three given real-domain processes and explain the '
        'limiting value, including special starts.',
        ['M2:T6:O02:D01'],['Goldie:C6:Investigation:1'],
        'The source compares convergent processes; it does not separately '
        'ask the failure-to-converge decision of numerical-iteration-fates.')
    separate('numerical-iteration-fates','numerical-divergence-graph-feature',
        'Explain divergence from a supplied iteration graph',
        'Read the displayed curve feature responsible for divergence '
        'without adding a formal derivative convergence theorem.',
        ['M2:T6:O02:D02'],['Goldie:C6:Prompt:5'],
        'The response identifies a graph feature causing failure, not '
        'a separately computed convergent sequence or its limiting root.')

    source='polynomial-direct-remainder'
    separate(source,'polynomial-supplied-factor-test',
        'Test or prove a supplied polynomial factor',
        'Use zero-remainder/root evidence to establish or refute the '
        'supplied factor, respecting the distinction between linear and quadratic divisors.',
        ['M2:T1:O04:D02'],
        ['Goldie:C1:Exercise-1B:9','Goldie:C1:Exercise-1B:12',
         'YM:C8:Example:21','YM:C8:Try-Now-21:1'],
        'Testing whether the remainder is zero asks a factor claim, unlike '
        'polynomial-direct-remainder, whose requested output is the remainder value.')
    revise(source,'Factor-test tasks moved; the retained family calculates a '
           'remainder without adding a separately requested factor proof.',
           demands=['M2:T1:O04:D01'])
    separate('polynomial-root-discovery','polynomial-no-integer-root-support',
        'Show that a cubic has no integer root',
        'Exhaust the finite signed integer-divisor candidates and reject '
        'the integer-root claim without claiming absence of real roots.',[],
        ['Goldie:C1:Example:9'],
        'A failed integer-root search is supporting evidence; the positive '
        'root-discovery sibling must actually identify a factor/root.')
    separate('polynomial-root-discovery','polynomial-bounded-integer-root',
        'Find the requested integer root within a supplied interval',
        'Test the permitted real integer candidates in the original cubic '
        'and return the specified root without importing later complex-root parts.',
        ['M2:T1:O04:D04'],['Goldie:C11:Exercise-11H:8'],
        'The retained source asks for one real integer root in a bounded '
        'interval, not an unrestricted factor-theorem demonstration.')
    separate('polynomial-factorisation','polynomial-supplied-factor-completion',
        'Complete a factorisation after a factor is supplied or already established',
        'Divide out the factor already given or established in the preceding '
        'part, then factor the residual quadratic over the reals as far as possible.',
        ['M2:T1:O04:D04'],
        ['Goldie:C1:Exercise-1B:11','Goldie:C1:Exercise-1B:19','Goldie:C1:Exercise-1B:20'],
        'Unlike factor discovery, the initial root/factor is supplied or '
        'recovered in the connected coefficient part; the new response completes the factors.')
    separate('polynomial-factorisation','polynomial-quartic-squared-variable',
        'Factor a quartic through a quadratic in the squared variable',
        'Use x-squared as the intermediate variable, factor the resulting '
        'quadratic and distinguish real from nonreal factors when counting zeros.',
        ['M2:T1:O04:D04'],['Goldie:C1:Exercise-1B:8'],
        'Choosing a squared-variable transformation differs from searching '
        'for a linear factor of the original cubic.')
    revise('polynomial-composed-recovery',
        'The shared polynomial factor-theorem preparation is retained. The '
        'final response may factor a composition or solve transformed roots, '
        'so polynomial root-solving is not a universal family claim.',
        demands=['M2:T1:O04:D02'])
    separate('stationary-classify-sketch','stationary-absence-and-sketch',
        'Prove absence of stationary points and sketch the original curve',
        'Show that the original-domain derivative cannot vanish, preserve '
        'the pole and use this information in the curve sketch.',
        ['M1:T8:O04:D01','M1:T3:O05:D01'],['Goldie:C4:Exercise-4A:4'],
        'There is no stationary point to classify; this differs from '
        'stationary-classify-sketch, which locates and classifies existing points.')
    revise('optimise-cylinder-in-cone',
        'The common source request is the stationary feasible volume. A '
        'separate second-derivative/nature demonstration is not universally asked.',
        demands=['M1:T8:O04:D01'])
    separate('power-antiderivative-family','power-reverse-derivative-recognition',
        'Recognise a standard reverse derivative in a power sum',
        'Identify the matching derivative of each original reciprocal power '
        'and combine its primitive with an arbitrary constant.',
        ['M1:T9:O01:D01'],['Goldie:C8:Exercise-8B:7'],
        'This retained response is mapped to reverse-derivative recognition, '
        'not to a separately requested rational-power rewriting exercise.')
    revise('power-antiderivative-family',
        'The common source output integrates powers or their combinations; '
        'a separate reverse-derivative recognition output is not universal.',
        demands=['M1:T9:O01:D02'])
    separate('area-horizontal-inverse-branch','defective-radical-region-support',
        'Record an inconsistent radical formula and shaded region',
        'Compare the stated nonnegative square-root branch with the '
        'drawn negative-y region and identify why the printed area is unsupported.',[],
        ['YM:C7:Try-Now-20:2'],
        'The source givens conflict; unlike a valid horizontal-area exercise '
        'this cannot supply an unqualified assessed-demand exemplar.')
    separate('area-tangent-normal-boundaries','tangent-triangle-area-chain',
        'Recover a tangent and the area of its axis triangle',
        'Find the tangent intercepts, form the specified triangle and '
        'establish its area without integrating a curve-line gap.',
        ['M1:T8:O03:D01'],['YM:C7:Try-Now-41:2'],
        'This selected response is a straight-sided triangle area following '
        'a tangent; the later volume concerns a different source region.')

    source='progression-condition-recovery'
    separate(source,'ap-three-term-condition',
        'Recover parameters from the three-term AP condition',
        'Impose equal successive differences, solve the parameter and '
        'return the requested source terms.',
        ['M1:T2:O03:D01'],['YM:C2:Example:2','YM:C4:Revision-Exercise-4:2'],
        'The selected response imposes an AP condition only; it does not '
        'inherit a GP demand from another part of the connected source question.')
    separate(source,'gp-three-term-condition',
        'Recover parameters from the three-term GP condition',
        'Impose the consecutive-term GP relation and verify every '
        'correlated parameter branch in the original terms.',
        ['M1:T2:O03:D02'],['YM:C2:Try-Now-2:1'],
        'A multiplicative GP condition differs from equal AP differences '
        'and from imposing both conditions jointly on one connected set.')
    source='sigma-read-write-evaluate'
    separate(source,'sigma-evaluate-without-required-expansion',
        'Evaluate a finite sigma expression',
        'Respect the actual lower/upper bounds and inclusive term count '
        'when calculating the finite sum; an expanded-series response is not added.',
        ['M1:T2:O04:D02'],
        ['YM:C2:Example:26','YM:C2:Try-Now-25:2','YM:C2:Try-Now:26','YM:C2:Exercise-2.1:2'],
        'Unlike sigma-read-write-evaluate, the source asks only for the sum '
        'rather than requiring expanded terms as a separate response.')
    separate(source,'sigma-compose-notation-from-series',
        'Write a listed series in sigma notation',
        'Choose an index rule and bounds reproducing every ordered term '
        'of the original finite series, allowing equivalent index shifts.',
        ['M1:T2:O04:D01'],
        ['YM:C2:Example:27','YM:C2:Try-Now-27:1','YM:C2:Try-Now-27:2'],
        'This reverses reading/evaluating a supplied sigma expression: '
        'the notation and bounds are the output.')
    separate('sigma-inverse-bound','gp-sigma-upper-bound-recovery',
        'Recover the upper index from a finite GP sum',
        'Interpret the given lower index, write the finite geometric sum '
        'and solve for its positive integer upper bound.',
        ['M1:T2:O03:D02'],['YM:C2:Example:28'],
        'The unknown is a finite GP term count, rather than evaluating a '
        'fully bounded sigma sum.')
    source='gp-convergence-and-infinite'
    separate(source,'gp-convergence-interval-only',
        'Find every parameter value giving a convergent GP',
        'Form the original ratio, impose its strict absolute-value '
        'condition and solve over the supplied angle interval.',
        ['M1:T2:O05:D01'],['YM:C4:Example:51'],
        'This asks only for the convergence interval; no sum to infinity '
        'is requested in the selected part.')
    infinite_only=['YM:C2:Example:29','YM:C2:Example:30','YM:C2:Example:31',
        'YM:C2:Try-Now-29:1','YM:C2:Try-Now-29:2','YM:C2:Try-Now-30:1',
        'YM:C2:Try-Now-30:2','YM:C2:Try-Now-31:1','YM:C2:Try-Now-31:2',
        'YM:C2:Try-Now-31:3','YM:C2:Exercise-2.1:1','YM:C2:Exercise-2.1:3',
        'YM:C2:Exercise-2.1:4','YM:C2:Exercise-2.1:8','YM:C2:Example:50',
        'YM:C4:Revision-Exercise-4:2']
    separate(source,'gp-infinite-sum-and-inverse-conditions',
        'Use a convergent GP sum to infinity or recover its parameters',
        'Identify the actual first term and ratio, use the convergent '
        'sum formula and solve the particular requested sum/parameter/remaining-tail condition.',
        ['M1:T2:O05:D02'],infinite_only,
        'Unlike the convergence-and-sum sibling, these sources do not all '
        'require an independent convergence explanation before the infinite-sum calculation.')

    source='vector-division-position'
    separate(source,'vector-midpoint-position',
        'Find a midpoint position vector',
        'Average the two given endpoint positions, preserving dimensions '
        'and distinguishing the midpoint from the displacement or its length.',
        ['M1:T7:O03:D03'],
        ['Goldie:C10:Exercise-10D:1','Goldie:C10:Exercise-10D:5'],
        'Midpoint averaging does not require choosing an internal/external '
        'division ratio, which is the sibling family decision.')
    separate(source,'vector-supplied-position-identity',
        'Rewrite a supplied affine position-vector identity',
        'Replace AB by OB-OA and collect coefficients in the given '
        'position relation without deriving an arbitrary vector line.',
        ['M1:T7:O02:D01','M1:T7:O02:D02'],['Goldie:C10:Prompt:7'],
        'The relation is supplied and only its equivalent algebraic form '
        'is requested; selecting a geometric division ratio is not asked.')
    separate(source,'vector-basis-division-displacement',
        'Use a division ratio to recover relative basis displacements',
        'Orient the source side correctly, apply its internal division '
        'ratio and construct the required non-origin displacement in the given basis.',
        ['M1:T7:O02:D03','M1:T7:O03:D02'],
        ['YM:C5:Example:8','YM:C5:Try-Now-8:1'],
        'The output is a relative displacement in a triangle basis, unlike '
        'the origin-based position vector in vector-division-position.')
    separate('vector-between-directions-angle','vector-supplied-line-direction-angle-support',
        'Retain the angle calculation between supplied line directions',
        'Extract the already supplied directions, compute their scalar '
        'product and select the actual line-angle convention as supporting practice.',[],
        ['Goldie:C10:Example:17']+[f'Goldie:C10:Exercise-10F:{n}'for n in range(1,6)],
        'Formal skew/vector line representation is outside the retained '
        'scope; these are supporting angle facets, not directly assessed 8227 line problems.')
    separate('vector-spatial-model-angle-chain','vector-spatial-edge-length-chain',
        'Recover hidden spatial positions and sloping edge lengths',
        'Read the symmetric roof geometry, recover the required positions '
        'and displacements, then calculate their actual lengths.',
        ['M1:T7:O03:D02','M1:T7:O04:D01'],['YM:C5:Try-Now-10:4'],
        'The source asks for edge vectors and lengths, not an angle; '
        'it cannot inherit the angle demand from the spatial-angle family.')
    revise('vector-spatial-model-angle-chain',
        'The shared assessed output is the spatial angle. Particular '
        'coordinate, displacement and magnitude outputs depend on each diagram and are not universal.',
        demands=['M1:T7:O05:D01'])
    separate('vector-perpendicularity-parameter','vector-supplied-line-perpendicularity-support',
        'Check perpendicularity of two supplied line directions',
        'Use the given nonzero directions to verify a zero scalar '
        'product without requiring construction of a formal vector line equation.',[],
        ['Goldie:C10:Example:16'],
        'This retains only a supporting calculation from an additional '
        'line-representation context; the in-scope sibling starts from prescribed vector data.')

    # An item-level mapping can be supported by its other part. Check the
    # actual selected response too: 5B13(ii) has no trigonometric identity.
    move('trig-square-power-reduction-integral','elementary-reciprocal-definite-logform',
        '8227:TB:Goldie:C5:Exercise-5B:13',
        'Part (ii) is a separate proper reciprocal-linear logarithmic integral; '
        'only part (i) chooses a half-angle power reduction.',selected=['ii'])
    move('elementary-reciprocal-definite-logform','elementary-proper-exponential-integrals',
        '8227:TB:Goldie:C5:Exercise-5A:3',
        'Parts (i), (iii) and (iv) are proper exponential definite integrals; '
        'only part (ii) belongs to the reciprocal-linear logarithmic family.',
        selected=['i','iii','iv'])
    fork('elementary-reciprocal-definite-logform','defective-internal-pole-integral-support',
        'Diagnose an invalid finite integral crossing an internal pole',
        'Check continuity over the whole stated interval and explain why '
        'subtracting endpoint logarithms across an internal pole does not give an ordinary integral.',[],
        'Unlike the proper-logarithmic-integral family, this source has no '
        'ordinary finite answer and is retained only as internal defect evidence.',
        answer_form='Diagnosis of the internal pole; the printed finite value is invalid.')
    move('elementary-reciprocal-definite-logform','defective-internal-pole-integral-support',
        '8227:TB:YM:C12:Example:8',
        'Part (b) crosses x=3/2. It has no ordinary finite integral and cannot '
        'serve as practice coverage of a proper logarithmic integral.',selected=['b'])
    move('proper-power-definite-integral','defective-internal-pole-integral-support',
        '8227:TB:YM:C7:Try-Now:14',
        'The accepted answer analysis already identifies (e) as divergent '
        'across x=-2/3. Its printed finite key must not support the proper '
        'finite-integral family; retain the original source response as '
        'internal defect evidence.',selected=['e'])
    revise('defective-internal-pole-integral-support',
           'Includes both logarithmic and reciprocal-square pole defects.',
           learner_decisions='Check continuity on the whole original '
           'interval and diagnose why a finite endpoint subtraction '
           'across its internal pole is invalid.',
           difficulty_progression='First identify the logarithmic '
           'primitive crossing its pole; then distinguish the '
           'reciprocal-square example whose two one-sided areas both diverge.')

    # Fixed perpendicularity verification and inverse parameter recovery
    # have different unknowns and required evidence.
    fork('vector-perpendicularity-parameter','vector-perpendicularity-verification',
        'Verify perpendicularity of fixed supplied vectors or point-defined arms',
        'Form the fixed nonzero directions where needed, calculate their '
        'scalar product and state the perpendicularity conclusion; no '
        'unknown scalar is solved from that condition.',
        ['M1:T7:O05:D02'],
        'Unlike vector-perpendicularity-parameter, the directions are '
        'already fixed and the required output is a verified geometric '
        'claim rather than a parameter value.',
        answer_form='Zero scalar product and perpendicularity conclusion, '
        'with any connected source geometry kept explicit.')
    for short in ['Goldie:C10:Example:10','Goldie:C10:Exercise-10C:2',
                  'YM:C5:Try-Now-14:1','YM:C5:Try-Now-16:3']:
        move('vector-perpendicularity-parameter','vector-perpendicularity-verification',
            '8227:TB:'+short,
            'The perpendicularity response verifies fixed numerical vectors '
            'or point-defined arms. No parameter is determined by that test; '
            'the connected equal-length/square tasks remain attached where present.')
    fork('vector-perpendicularity-parameter','vector-perpendicular-pair-selection',
        'Select every supplied vector perpendicular to a fixed direction',
        'Test each fixed candidate by a scalar product, distinguish zero '
        'from nonzero results and return the complete selected subset.',
        ['M1:T7:O05:D02'],
        'Unlike parameter recovery, no direction is adjusted; unlike a '
        'single verification, the response must select all qualifying '
        'vectors from several candidates.',
        answer_form='The complete subset of perpendicular supplied vectors.')
    move('vector-perpendicularity-parameter','vector-perpendicular-pair-selection',
         '8227:TB:YM:C5:Try-Now-14:2',
         'The rendered prompt supplies four fixed candidates and asks which '
         'are perpendicular, without an unknown scalar.')
    fork('vector-perpendicularity-parameter','vector-perpendicularity-impossibility',
        'Show that no real parameter can make the directions perpendicular',
        'Express the scalar product as a function of the parameter, '
        'recognise its strictly positive square-plus-constant form, and '
        'justify that a zero scalar product is impossible over the reals.',
        ['M1:T7:O05:D02'],
        'Unlike finding an admissible parameter, the response proves that '
        'the orthogonality condition has no real solution.',
        answer_form='Parameter-dependent scalar product and a real-domain '
        'impossibility argument, not an invented parameter value.')
    move('vector-perpendicularity-parameter','vector-perpendicularity-impossibility',
         '8227:TB:YM:C5:Try-Now-16:4',
         'The selected (a)–(b) chain obtains 25+p^2 and proves it cannot '
         'vanish for real p. The prescribed 60-degree task remains separate.')

    # B.1: Goldie3C Q12 has a proof followed by a supplied-identity
    # solve. The angle-answer response must not inherit proof equivalence.
    move('compound-identity-proof','double-angle-bounded-equations',
        '8227:TB:Goldie:C3:Exercise-3C:12',
        'Part (ii) applies the identity established in (i) to return '
        'bounded angles; it is not itself a general identity proof.',selected=['ii'])

    # B.2: an extreme ordinate is not an extremum argument.
    fork('rform-extrema-arguments','rform-extrema-values-only',
        'Use an R form to state extreme values without solving their angles',
        'Match coefficients to obtain the amplitude and phase, recognise '
        'any outer scale, and state the requested extreme ordinate without '
        'adding an unasked extremum-angle equation.',
        ['M2:T3:O02:D04'],
        'Unlike rform-extrema-arguments, the selected exercise does not ask '
        'where an extremum occurs; the output is an ordinate only.',
        answer_form='R and phase followed by the requested extreme ordinate.')
    move('rform-extrema-arguments','rform-extrema-values-only',
        '8227:TB:YM:C10:Try-Now:25',
        'Part (b) only writes down the smallest scaled value; no smallest '
        'positive argument or other extremum angle is requested.')

    # Rendered compound-angle tasks: symbolic compression is not a
    # numerical exact-angle value, and an independent solve response is
    # not a parameter-ratio output merely because it shares an example.
    move('compound-exact-angle','compound-expand-simplify',
        '8227:TB:Goldie:C3:Example:3',
        'The source simplifies cos(theta)cos(3theta)-sin(theta)sin(3theta) '
        'to cos(4theta); it returns a symbolic expression, not a numerical exact value.')
    move('compound-parameter-ratio-chain','compound-bounded-equations',
        '8227:TB:YM:C10:Example:12',
        'Part (b) solves 2tan(45-x)=3tan(x) over an explicit interval; '
        'the requested output is an angle set, not the parameter formula in (a).',
        selected=['b-roots'])

    # The shared item contains Pythagorean tasks, but these selected
    # responses use reciprocal definitions alone, not that identity demand.
    move('reciprocal-pythagorean-equations','bounded-squared-ratio',
        '8227:TB:Goldie:C3:Exercise-3A:7',
        'Part (i) clears cos(x)=1/cos(x) on its original domain, giving '
        'cos-squared(x)=1 and both ratio signs; no Pythagorean identity is used.',selected=['i'])
    move('reciprocal-pythagorean-equations','bounded-basic-trig-roots',
        '8227:TB:Goldie:C3:Exercise-3A:7',
        'Part (ii) clears the nonzero sine/cosine denominators in '
        'cosec(x)=sec(x), obtains tan(x)=1 and enumerates its basic roots; '
        'no Pythagorean identity is required.',selected=['ii'])

    # B.1: these printed equations reduce to ONE trig ratio, not a quadratic.
    move('trig-quadratic-reduction','bounded-basic-trig-roots',
        '8227:TB:YM:C4:Exercise-4.2:6',
        'Part (a) multiplies by the nonzero cosine on the stated interval '
        'to obtain 3 sin(x)=2; no quadratic ratio equation occurs.',selected=['a'])
    move('trig-quadratic-reduction','bounded-affine-argument',
        '8227:TB:YM:C4:Exercise-4.2:6',
        'Part (b) is tan(2y/3)=-1 and requires interval transformation '
        'and back-substitution, not a quadratic reduction.',selected=['b'])

    # Further B.2 distinctions exposed by rendered equation comparisons.
    # An exponential inverse, principal square root and rational composite
    # cannot inherit one another's answer/admissibility rules.
    source='quadratic-transformation-recovery'
    fork(source,'quadratic-square-root-recovery',
        'Reduce an equation in the principal square root and recover its roots',
        'Let the intermediate variable be the principal square root, solve '
        'its quadratic, reject negative intermediate values, and check any '
        'denominator restrictions before returning original real roots.',
        ['M1:T1:O04:D01','M1:T1:O04:D02','M1:T1:O04:D03'],
        'Unlike the even-power sibling, the intermediate square root must '
        'be nonnegative; squaring a negative intermediate root creates a false solution.',
        representation_and_response='Equations containing square roots; original real roots, '
        'with explicit rejection of inadmissible intermediate roots.',
        answer_form='Admissible original real roots, preserving exact or source-specified decimal form.')
    for short in ['YM:C1:Example:13','YM:C1:Revision-Exercise-1:7']:
        move(source,'quadratic-square-root-recovery','8227:TB:'+short,
             'The retained response uses a principal square-root substitution and '
             'must filter its sign before recovering the original unknown.')
    move(source,'quadratic-square-root-recovery','8227:TB:YM:C1:Try-Now:13',
         'These four square-root responses require nonnegative intermediate values; '
         'part (d) also excludes a zero denominator.',selected=['a','b','c','d'])
    fork(source,'quadratic-exponential-recovery',
        'Reduce an exponential equation to a quadratic and recover the exponent',
        'Choose the positive exponential intermediate variable, solve its '
        'quadratic, reject nonpositive values, and recover the exponent with '
        'known powers or logarithms as actually requested.',
        ['M1:T1:O04:D01','M1:T1:O04:D02','M1:T1:O04:D03'],
        'The intermediate variable is strictly positive and its inverse is '
        'exponential/logarithmic, not the signed square root of the even-power sibling.',
        representation_and_response='Exponential equation to original exponent solutions.',
        answer_form='Original exponent values in the requested exact/logarithmic form.')
    for short,parts in [('YM:C1:Try-Now:13',['f']),('YM:C1:Exercise-1:1',['c'])]:
        move(source,'quadratic-exponential-recovery','8227:TB:'+short,
             'This selected response solves a quadratic in a positive exponential '
             'and returns exponent values; neighbouring radical equations do not join it.',selected=parts)
    fork(source,'quadratic-rational-composite-recovery',
        'Solve a quadratic in a supplied rational composite and recover its inputs',
        'Set the rational composite equal to a new variable, solve its '
        'quadratic, then solve every resulting input equation while excluding '
        'the original zero denominator.',
        ['M1:T1:O04:D01','M1:T1:O04:D02','M1:T1:O04:D03'],
        'Unlike a power substitution, each intermediate value requires a '
        'second rational-to-quadratic recovery with an original denominator restriction.',
        representation_and_response='Quadratic in 2x+1/x, followed by all permitted real x.',
        answer_form='All real original roots with x=0 excluded.')
    move(source,'quadratic-rational-composite-recovery','8227:TB:YM:C1:Try-Now:13',
         'Part (h) uses the rational composite 2x+1/x and requires a second '
         'quadratic recovery for each intermediate root.',selected=['h'])
    fork(source,'quadratic-affine-recovery-chain',
        'Use established quadratic roots to recover an affine-transformed unknown',
        'Solve the base quadratic, match each established root to the '
        'affine expression in the second equation, and invert that one-to-one '
        'map without inventing a square-root sign restriction.',
        ['M1:T1:O04:D01','M1:T1:O04:D02','M1:T1:O04:D03'],
        'Unlike square-root or even-power recovery, the affine inverse is '
        'one-to-one and imposes no sign-based rejection.',
        representation_and_response='Connected base quadratic then quadratic in 2y-3.',
        answer_form='Base roots followed by every correlated transformed-variable root.')
    move(source,'quadratic-affine-recovery-chain','8227:TB:YM:C1:Exercise-1:11',
         'Keep the solved quadratic in (a) as the explicit scaffold for the '
         'one-to-one affine recovery in (b).')
    revise(source,'Square-root, exponential, rational-composite and affine '
           'responses split after page reading; retained sources use pure powers '
           'or reciprocal powers and recover all real preimages.',
           title='Reduce a pure-power equation to a quadratic and recover all real preimages',
           learner_decisions='Choose the actual power or reciprocal-power intermediate '
           'variable, solve its quadratic, enforce its real range and excluded zero, '
           'then recover all real original roots.',
           representation_and_response='Equation in a power or reciprocal power; '
           'complete real root set, retaining any original nonzero restriction.')

    fork('numerical-stationary-constraint-chain',
         'numerical-level-intersection-after-analytic-stationarity',
         'Find a stationary point analytically, then iterate to a separate level intersection',
         'Differentiate to obtain the exact stationary point first; '
         'independently impose the stated ordinate on the curve, derive '
         'the supplied fixed-point form and iterate to the selected '
         'intersection, preserving any smaller-root graph selection.',
         ['M1:T8:O04:D01','M2:T6:O03:D02',
          'M2:T6:O04:D01','M2:T6:O04:D02'],
         'Unlike numerical-stationary-constraint-chain, the iterated '
         'unknown is a different level intersection: the stationary '
         'point has already been obtained exactly.',
         givens_and_unknowns='An exponential-product curve, its named '
         'extremum and a specified ordinate; exact stationary coordinates '
         'and the selected numerical level-intersection input.',
         scaffolding_and_connected_parts='Retain the complete source '
         'question. The preceding stationary response supplies curve '
         'context but is not the equation solved by the subsequent iteration.',
         answer_form='Exact stationary coordinates, the level equation '
         'and the requested selected numerical root.')
    for short in ['Goldie:C6:Exercise-6B:12','YM:C13:Exercise-13:4']:
        move('numerical-stationary-constraint-chain',
             'numerical-level-intersection-after-analytic-stationarity',
             '8227:TB:'+short,
             'Rendered parts find the extremum analytically, then impose '
             'a separate ordinate and iterate to that intersection. '
             'The iteration does not locate the stationary point.')

    fork('reciprocal-sign-and-graph','reciprocal-sign-possibility',
         'Decide which simultaneous reciprocal-ratio sign patterns are possible',
         'Combine quadrant signs with reciprocal definitions to identify '
         'possible simultaneous signs and justify impossible or equal-ratio cases.',
         ['M2:T3:O01:D02'],
         'Unlike reciprocal graph construction, the required response is '
         'a global possibility argument across quadrants, not plotted '
         'branches and asymptotes.',
         answer_form='Permitted angle sets and justified possibility conclusions.')
    move('reciprocal-sign-and-graph','reciprocal-sign-possibility',
         '8227:TB:Goldie:C3:Exercise-3A:6',
         'The three rendered responses ask about all-positive, '
         'all-negative and equal reciprocal ratios; none requests a graph.')
    revise('reciprocal-sign-and-graph',
           'The sign-possibility exercise moved to its own sibling.',
           title='Construct reciprocal trigonometric graphs from zeros and extrema',
           learner_decisions='Use the base sine, cosine or tangent zeros '
           'and signs to place the reciprocal poles, extrema and branches '
           'on the stated interval.')

    # A rendered mixed exercise is not one learner-decision family.
    source='trig-mixed-revision-equations'
    iid='8227:TB:Goldie:C3:Exercise-3E:4'
    move(source,'bounded-affine-argument',iid,
         'Selected (i) and (iii) invert a known shifted sine/cosine '
         'argument and enumerate its bounded preimages.',selected=['i','iii'])
    move(source,'trig-quadratic-reduction',iid,
         'Selected (ii) uses cos^2=1-sin^2 and (vii) is already a '
         'quadratic in tan; both solve and filter a one-ratio quadratic.',
         selected=['ii','vii'])
    fork(source,'unscaffolded-compound-angle-equation',
         'Choose compound-angle expansion in an unscaffolded mixed exercise',
         'Recognise the two shifted arguments, expand both, collect '
         'sine and cosine coefficients, then return every angle in '
         'the stated interval.',
         ['M1:T6:O06:D01','M1:T6:O06:D02'],
         'Unlike known-shift inversion, neither side is one isolated '
         'ratio; an addition-formula reduction must be selected first.',
         answer_form='All bounded angle solutions after expansion.',
         constraints='Preserve the given angle units and interval. '
         'R5 accepted source links stay fixed; their broad basic-angle '
         'labels do not assert a complete advanced-demand classification.')
    move(source,'unscaffolded-compound-angle-equation',iid,
         'Part (iv) has cos(45-theta)=2sin(30+theta); compound '
         'expansion precedes the bounded-angle solve.',selected=['iv'])
    fork(source,'unscaffolded-double-angle-quadratic',
         'Select a double-angle form that creates a one-ratio quadratic',
         'Replace cos(2theta) by 1-2sin^2(theta), solve the resulting '
         'quadratic, filter the sine range and enumerate bounded roots.',
         ['M1:T6:O05:D02','M1:T6:O06:D01','M1:T6:O06:D02'],
         'Unlike the ordinary quadratic sibling, the learner first '
         'chooses a double-angle identity to expose that quadratic.',
         answer_form='All bounded angles after admissible ratio roots.')
    move(source,'unscaffolded-double-angle-quadratic',iid,
         'Part (v) has cos(2theta)+3sin(theta)=2 and requires '
         'selecting the compatible double-angle form.',selected=['v'])
    revise(source,'The mixed exercise has been partitioned by its actual '
           'selected learner decisions. Only part (vi) remains.',
           demands=['M1:T6:O06:D01','M1:T6:O06:D02'],
           title='Choose an R form to solve an unscaffolded sine–cosine equation',
           learner_decisions='Recognise that cos(theta)+3sin(theta)=2 '
           'requires combining the unequal sine and cosine coefficients, '
           'choose a valid R form and enumerate all bounded roots.',
           representation_and_response='One unscaffolded equation to all '
           'angles in degrees, rather than an authored R-form show-that chain.',
           distinction_basis='Unlike an explicit R-form coefficient task, '
           'the learner must choose the reduction without a named scaffold.',
           answer_form='Complete bounded angle list, not amplitude or extrema.',
           difficulty_progression='single item')

    # Make the modelling decision visible before comparing optimisation
    # families. These source constraints are analysis, not recipe domains.
    model_decisions={
        'optimise-closed-cuboid-area':
            'Use the fixed volume and stated base-side ratio to eliminate '
            'height; count both bases and four side faces; minimise the '
            'resulting Cx^2+D/x on positive dimensions and return the '
            'particular input, area and verification actually requested.',
        'optimise-closed-cuboid-volume':
            'Use the fixed total area of a closed square-base cuboid to '
            'eliminate height, maximise its linear-minus-cubic volume '
            'on positive dimensions and classify the stationary volume.',
        'optimise-open-square-tank':
            'Convert the given capacity into cubic centimetres, eliminate '
            'height with the square-base volume, count five material faces '
            'without a lid, minimise x^2+D/x and recover all three tank dimensions.',
        'optimise-closed-cylinder-area':
            'Eliminate height from the fixed cylinder volume, include two '
            'circular ends and the curved side, obtain 2pi*r^2+2V/r and '
            'solve its positive stationary radius; distinguish the member '
            'asking for radius/verification from the one asking for area/nature.',
        'optimise-split-wire-loops':
            'Split one fixed wire between a square perimeter and circle '
            'circumference, eliminate the radius and find the stationary '
            'square side of their total-area quadratic. Do not import the '
            'source working sentence that incorrectly calls this a maximum.',
        'optimise-quarter-disc-plate':
            'Count the external straight edges and quarter-circle arc in '
            'the fixed perimeter, eliminate rectangle length, add rectangle '
            'and quarter-disc areas and locate/classify the maximum quadratic area.',
        'optimise-L-garden':
            'Count the external boundary of the proportioned L shape, '
            'eliminate one length, add its two nonoverlapping rectangles '
            'and calculate/prove the maximum area.',
        'optimise-cylinder-in-cone':
            'Use similar triangles in the cone cross-section to relate '
            'cylinder height and radius, form its cubic volume, exclude '
            'degenerate radii and return the maximum feasible volume.',
        'optimise-rectangle-under-line':
            'Form the line through its two given axis intercepts, use '
            'the moving point to express rectangle height, maximise the '
            'resulting quadratic area and classify it inside the finite segment.',
        'optimise-shared-fences':
            'Count internal shared fence lengths once along with the '
            'external boundary, eliminate one pen dimension, maximise '
            'total enclosed area and return dimensions of one pen.',
        'optimise-open-triangular-container':
            'Use the 5:5:8 isosceles cross-section to obtain its height '
            'and area, count two triangular ends and two rectangular '
            'sides without a top, eliminate container length from fixed '
            'card area and locate/classify the feasible cubic-volume extremum.'}
    for slug,decisions in model_decisions.items():
        revise(slug,'Rendered geometry and requested target now state '
               'the actual modelling decisions rather than a shared template.',
               learner_decisions=decisions)

    # Binomial preparation responses must not inherit a later coefficient task.
    for short,parts in [
        ('Example:39',['a-through-a-squared']),('Example:47',['a']),
        ('Try-Now-39:1',['a']),('Try-Now-39:2',['a']),
        ('Try-Now-39:3',['a','b']),('Try-Now-39:4',['a']),
        ('Try-Now-47:1',['a-four-nonzero-terms']),('Try-Now-47:2',['a','b'])]:
        move('binomial-product-coefficient','binomial-direct-expansion',
             '8227:TB:YM:C2:'+short,
             'The selected earlier response expands a binomial only; '
             'the later product coefficient remains separately grouped.',selected=parts)
    for source,short in [('binomial-product-coefficient','Example:48'),
                         ('binomial-parameter-coefficients','Try-Now-48:3')]:
        move(source,'binomial-chosen-term','8227:TB:YM:C2:'+short,
             'Part (a) obtains two specified coefficients of one known '
             'binomial; no product assembly or parameter equation is asked there.',
             selected=['a-quadratic','a-cubic'])
    for short in ['Try-Now-51:2','Try-Now-51:3']:
        move('binomial-parameter-coefficients','binomial-direct-expansion',
             '8227:TB:YM:C2:'+short,
             'Part (a) requests the first three terms, not the '
             'coefficient condition and parameter recovery in (b).',selected=['a-first-three'])
    src='binomial-parameter-coefficients';bd=['M1:T2:O01:D03']
    fork(src,'binomial-unknown-power-coefficients',
         'Recover an unknown positive integer binomial power from coefficients',
         'Express coefficients in n using n and n(n-1)/2, '
         'combine any prefactor, solve the coefficient conditions '
         'and retain correlated parameters with positive integer n.',bd,
         'Unlike a fixed-power scale parameter, the exponent is unknown; '
         'the binomial coefficients themselves depend on it and need an integer check.',
         answer_form='All admitted exponent/scale/coefficient values.')
    for short in ['Example:49','Try-Now-49:1','Try-Now-49:2',
                  'Try-Now-49:3','Exercise-2.2:8']:
        move(src,'binomial-unknown-power-coefficients','8227:TB:YM:C2:'+short,
             'The requested exponent n is unknown and constrained '
             'to be a positive integer; fixed-power coefficient recovery is different.')
    fork(src,'binomial-parameter-from-aligned-sum-coefficient',
         'Recover a parameter from one coefficient of a sum of expansions',
         'Extract the same target degree from each separate binomial, '
         'add or subtract those aligned coefficients and solve/filter '
         'the resulting parameter equation.',bd,
         'Unlike a product coefficient, only equal-degree coefficients '
         'are combined; cross-degree pair products must not be included.',
         answer_form='All parameters satisfying the specified aligned-coefficient condition.')
    for short in ['Example:51','Try-Now-51:1']:
        move(src,'binomial-parameter-from-aligned-sum-coefficient',
             '8227:TB:YM:C2:'+short,
             'The source combines coefficients of a sum of two '
             'expansions, not a product.')
    fork(src,'binomial-equal-coefficients-parameter',
         'Recover a nonzero parameter by equating two binomial coefficients',
         'Select both stated degrees in the same expansion, equate '
         'their coefficient expressions and cancel only after '
         'enforcing the nonzero parameter restriction.',bd,
         'Unlike matching one coefficient to a supplied target, two '
         'different coefficient expressions from the same expansion are equated.',
         answer_form='Admitted nonzero parameter values.')
    move(src,'binomial-equal-coefficients-parameter','8227:TB:YM:C2:Try-Now-48:5',
         'The source equates its x^4/x^5 coefficients; the condition '
         'is neither an aligned sum nor a product coefficient target.')
    fork(src,'binomial-scale-from-one-coefficient',
         'Recover a binomial scale from one coefficient then obtain another',
         'Use the given first-degree coefficient to recover the '
         'scale, then use it in the requested higher-degree coefficient.',bd,
         'Unlike a product/sum condition, one binomial and one '
         'initial coefficient determine the scale before another coefficient is requested.',
         answer_form='The requested higher-degree coefficient after scale recovery.')
    move(src,'binomial-scale-from-one-coefficient','8227:TB:YM:C2:Revision-Exercise-2:2',
         'The source first recovers a from the linear coefficient '
         'of one expansion, then asks its cubic coefficient.')
    revise(src,'Unknown powers, sums, equal-coefficient and single-coefficient '
           'inverse tasks moved; expansion prelude responses also moved.',
           title='Recover a parameter from a product coefficient condition',
           learner_decisions='Collect every cross-degree contribution '
           'to the requested product coefficient, set the given '
           'condition and solve/filter all allowed parameter values.')

    # Progression givens/unknowns select different learner operations.
    ap='ap-term-and-membership';ad=['M1:T2:O03:D01']
    fork(ap,'ap-index-and-membership',
         'Recover an arithmetic term index and test sequence membership',
         'Use the known first term/difference in T_n=a+(n-1)d, solve '
         'for n and accept a term only when its index is a positive integer.',ad,
         'Unlike direct term evaluation, the index is unknown and its '
         'integer admissibility is part of the answer.',
         answer_form='A positive integer index or a justified nonmembership conclusion.')
    for short in ['Example:5','Try-Now:5','Try-Now-8:5','Try-Now-8:8']:
        move(ap,'ap-index-and-membership','8227:TB:YM:C2:'+short,
             'The source solves for the term index or tests whether a '
             'specified value is a term; it does not merely evaluate T_n.')
    move(ap,'ap-index-and-membership','8227:TB:YM:C2:Try-Now-8:6',
         'Part (b) asks membership of -310 via its integer index.',selected=['b-index'])
    move(ap,'ap-term-threshold','8227:TB:YM:C2:Try-Now-8:6',
         'Part (a) counts positive terms by the zero-crossing inequality '
         'and integer boundary, rather than testing one prescribed value.',selected=['a-positive-count'])
    fork(ap,'ap-parameters-from-term-conditions',
         'Recover arithmetic parameters from term-position conditions',
         'Translate the supplied indexed terms or term relations into '
         'equations for first term/difference, solve them and use the '
         'recovered progression for the source requested follow-up.',ad,
         'Unlike known-parameter term evaluation, a and/or d must first '
         'be reconstructed from indexed conditions.',
         answer_form='Recovered a/d and the particular requested terms or index.')
    for short in ['Example:7','Example:8','Try-Now-7:1','Try-Now-7:2','Try-Now-7:3',
                  'Try-Now-8:1','Try-Now-8:2','Try-Now-8:3','Try-Now-8:7',
                  'Try-Now-8:9','Try-Now-8:10','Try-Now-8:11','Try-Now-8:12']:
        move(ap,'ap-parameters-from-term-conditions','8227:TB:YM:C2:'+short,
             'The source must recover progression parameters from '
             'indexed term constraints before its requested follow-up.')
    revise(ap,'Inverse index and parameter reconstruction members moved.',
           title='Evaluate arithmetic terms from the given progression',
           learner_decisions='Read a and d from the supplied progression '
           'and evaluate the requested T_n or general term using n-1 increments.',
           answer_form='Requested term values or an explicit nth-term rule.')
    src='ap-finite-sum'
    fork(src,'ap-parameters-from-sum-conditions',
         'Recover arithmetic parameters from term and block-sum conditions',
         'Express given partial/block sums and indexed terms in a/d, '
         'solve the resulting equations, then compute the requested '
         'follow-up sum, term or count.',ad,
         'Unlike the term-condition sibling, at least one given '
         'constraint is a sum of several terms, not a single T_n value.',
         answer_form='Recovered progression parameters and the source follow-up.')
    for short in ['Example:17','Example:18','Try-Now-17:1','Try-Now-17:2',
                  'Try-Now-18:1','Try-Now-18:2','Try-Now-19:4','Try-Now-19:6',
                  'Try-Now-19:7','Exercise-2.1:5']:
        move(src,'ap-parameters-from-sum-conditions','8227:TB:YM:C2:'+short,
             'The source gives term/block-sum information and requires '
             'parameter recovery before any subsequent evaluation.')
    move(src,'ap-inverse-sum-and-threshold','8227:TB:YM:C2:Try-Now-17:3',
         'Given first/last terms and total, the requested count comes '
         'from the finite-sum relation; difference is a later recovery.')
    src='ap-inverse-sum-and-threshold'
    fork(src,'ap-partial-sum-threshold',
         'Select the first or last count meeting an arithmetic sum bound',
         'Form the quadratic partial sum, solve its strict/non-strict '
         'inequality and check neighbouring positive integer counts.',ad,
         'Unlike equality inversion, a least/greatest integer boundary '
         'must satisfy the stated partial-sum inequality.',
         answer_form='The requested extremal integer count with its boundary check.')
    for short in ['Try-Now-19:1','Try-Now-19:2']:
        move(src,'ap-partial-sum-threshold','8227:TB:YM:C2:'+short,
             'The source asks for an extremal count under a sum inequality, '
             'not an integer solving a sum equality.')
    fork(src,'ap-sign-count-and-positive-block',
         'Count positive/negative terms and sum the positive arithmetic block',
         'Locate the sign boundary by a term inequality, use the stated '
         'positive-to-negative term-count ratio and subtract partial '
         'sums to obtain only the positive block total.',ad,
         'Unlike inverse total-sum counting, the finite length follows '
         'from sign counts and their ratio; the requested sum is a selected block.',
         answer_form='Total count and sum of the positive terms.')
    move(src,'ap-sign-count-and-positive-block','8227:TB:YM:C2:Example:19',
         'The source gives a ratio of positive/negative term counts, '
         'not a partial-sum total equation.')
    revise(src,'Sign-count and inequality-threshold tasks moved.',
           title='Recover an arithmetic term count from a finite total',
           learner_decisions='Use the actual first/last-term or nth-term '
           'sum relation to solve for the finite count, retaining all '
           'admissible positive integer solutions and requested follow-up values.')
    gp='gp-terms-and-parameters';gd=['M1:T2:O03:D02']
    fork(gp,'gp-index-and-membership',
         'Recover a geometric term index from a specified term value',
         'Use the known first term/ratio to solve a*r^(n-1)=T, '
         'checking positive integer n and sign/parity for negative ratios.',gd,
         'Unlike direct term evaluation, the exponent/index is unknown '
         'and must satisfy integer and sign constraints.',
         answer_form='A valid integer position or a justified nonmembership conclusion.')
    for short in ['Example:11','Try-Now-11:1','Try-Now-11:2','Try-Now-11:3',
                  'Try-Now-11:4','Try-Now-13:6','Try-Now-13:11']:
        move(gp,'gp-index-and-membership','8227:TB:YM:C2:'+short,
             'The source recovers the index/count from a known terminal term.')
    for short in ['Goldie:C2:Exercise-2B:11','Goldie:C2:Exercise-2B:12']:
        move(gp,'gp-index-and-membership','8227:TB:'+short,
             'The accepted R5 source working solves an unknown exponent/index '
             'and checks negative-ratio parity where applicable.')
    fork(gp,'gp-parameters-from-indexed-terms',
         'Recover geometric parameters from indexed term conditions',
         'Write the supplied term conditions as equations in a/r, '
         'use their index gap to isolate r and preserve correlated '
         'real branches before recovering the requested terms.',gd,
         'Unlike known-ratio evaluation, the common ratio and possibly '
         'first term are unknown and must satisfy several term conditions.',
         answer_form='All admissible correlated a/r branches and requested source terms.')
    for short in ['Example:13','Try-Now-13:1','Try-Now-13:2','Try-Now-13:3',
                  'Try-Now-13:4','Try-Now-13:7','Try-Now-13:10']:
        move(gp,'gp-parameters-from-indexed-terms','8227:TB:YM:C2:'+short,
             'The source reconstructs the ratio/first term from '
             'indexed terms or sums of indexed terms.')
    move(gp,'gp-three-term-condition','8227:TB:YM:C2:Try-Now-13:8',
         'The three consecutive p-dependent terms impose equal ratios, '
         'not a known-ratio term-index calculation.')
    fork(gp,'gp-ratio-from-two-term-sum',
         'Recover a geometric ratio from a sum of specified adjacent terms',
         'Write T_2+T_3 as a*r+a*r^2, divide only by the '
         'admitted nonzero first term and filter the quadratic ratio roots.',gd,
         'Unlike a quotient of two known indexed terms, their given '
         'sum produces a quadratic in r and requires the stated sign filter.',
         answer_form='The admitted common ratio from the quadratic relation.')
    for short in ['Example:24','Try-Now-24:1']:
        move(gp,'gp-ratio-from-two-term-sum','8227:TB:YM:C2:'+short,
             'The given sum T_2+T_3 leads to r+r^2 and a sign-filtered quadratic.')
    revise(gp,'Index inversion, parameter reconstruction and two-term sum '
           'ratio tasks moved to their own decision families.',
           title='Evaluate geometric terms from a given progression',
           learner_decisions='Read the given ratio/first-term information '
           'and use T_n=a*r^(n-1) for the requested term or explicit nth-term rule.')
    src='gp-finite-sums'
    fork(src,'gp-count-from-finite-total',
         'Recover a geometric term count from a finite total',
         'Use the finite GP sum relation with the actual first term and '
         'ratio, isolate r^n and recover/check the positive integer count.',gd,
         'Unlike direct finite-sum evaluation, the count is the unknown '
         'and comes from inverting the sum equation.',
         answer_form='A positive integer count satisfying the original finite total.')
    for short in ['Example:22','Try-Now:22','Try-Now-24:2']:
        move(src,'gp-count-from-finite-total','8227:TB:YM:C2:'+short,
             'The source gives the total and asks for the number of terms.')
    move('gp-infinite-sum-and-inverse-conditions',src,'8227:TB:YM:C2:Example:29',
         'Parts (a,b,c) request finite sums for 10/15/20 terms; '
         'only part (d) requests the sum to infinity.',selected=['a','b','c'])
    src='gp-infinite-sum-and-inverse-conditions'
    fork(src,'gp-parameters-from-infinite-total',
         'Recover geometric parameters from a stated convergent infinite total',
         'Use S_infinity=a/(1-r) as a constraint, solve for '
         'the unknown a/r/parameter, retain convergence and recover '
         'the requested terms from the admitted progression.',
         ['M1:T2:O05:D02'],
         'Unlike calculating an unknown infinite sum from known terms, '
         'the infinite total is given and constrains the progression parameters.',
         answer_form='Admissible parameters and the source requested term values.')
    for short in ['Example:31','Try-Now-29:2','Try-Now-31:1','Try-Now-31:2',
                  'Try-Now-31:3','Exercise-2.1:4']:
        move(src,'gp-parameters-from-infinite-total','8227:TB:YM:C2:'+short,
             'The infinite total is given and must be inverted to recover '
             'progression parameters or a requested term.')

    fork('ap-gp-connected-sums','gp-terms-to-ap-finite-sum',
         'Recover a geometric progression then use its terms to form an arithmetic sum',
         'Recover the GP ratio from its first/fourth terms, find its '
         'infinite total, then use its second/third terms as indexed '
         'AP terms and recover the requested arithmetic finite total.',
         ['M1:T2:O03:D01','M1:T2:O03:D02','M1:T2:O05:D02'],
         'Unlike equating two finite totals to find an AP count, '
         'the connection uses individual GP terms as indexed AP '
         'terms; an infinite GP total is also explicitly requested.',
         answer_form='GP ratio/infinite total and the requested AP finite sum.')
    move('ap-gp-connected-sums','gp-terms-to-ap-finite-sum',
         '8227:TB:YM:C2:Revision-Exercise-2:1',
         'This chain uses GP term positions to determine an AP and '
         'explicitly asks the GP infinite total; it does not equate '
         'finite totals to recover an AP count.')
    revise('ap-gp-connected-sums','GP-term-to-AP construction moved.',
           title='Equate a finite geometric total to an arithmetic total to recover its count',
           learner_decisions='Compute the finite GP total, equate it '
           'to the AP finite-sum expression and solve/filter the '
           'resulting positive integer arithmetic count.',
           difficulty_progression='single item')

    # Existence for all parameters and non-strict meeting are not two-distinct-root tasks.
    source='line-curve-parameter-contact'
    fork(source,'line-curve-universal-meeting-proof',
         'Prove a parameterised line and curve always meet',
         'Eliminate the line, express the discriminant as a nonnegative square '
         'and conclude meeting for every real parameter, including the tangent equality case.',
         ['M1:T4:O02:D01'],
         'Unlike finding a range for two distinct intersections, this proves '
         'universal existence and explicitly allows a repeated root.',
         answer_form='A nonnegative-discriminant argument valid for all real k.',
         scaffolding_and_connected_parts='Part (b) tangent parameter/contact '
         'remains connected in the original source and is separately grouped.')
    move(source,'line-curve-universal-meeting-proof','8227:TB:YM:C1:Try-Now:38',
         'Part (a) proves meeting for every k; it does not solve a strict '
         'two-intersection parameter inequality.',selected=['a-universal-meeting'])
    move(source,'line-curve-tangency-parameter','8227:TB:YM:C1:Try-Now:38',
         'Part (b) selects discriminant equality, then recovers the repeated '
         'contact point; these are tangent, not two-distinct-point responses.',
         selected=['b-tangent-k','b-contact'])
    fork(source,'line-curve-at-least-one-intersection',
         'Find parameters allowing a line and curve to meet or touch',
         'Substitute the line into the curve and solve the nonnegative '
         'discriminant condition, retaining tangent endpoints and original domains.',
         ['M1:T4:O02:D01'],
         'Unlike the two-distinct-intersection sibling, equality is admitted '
         'and parameter boundary values must be included.',
         answer_form='Closed parameter range with tangent endpoints included.')
    move(source,'line-curve-at-least-one-intersection','8227:TB:YM:C1:Try-Now-32:4',
         'The source asks whether the line meets the curve and explicitly '
         'allows tangency; its condition is discriminant >=0, not >0.')
    move('coordinate-midpoint-shape-recovery','coordinate-perpendicular-bisector',
         '8227:TB:YM:C3:Try-Now-21:2',
         'The rhombus first asks for the perpendicular bisector of AC, then '
         'its y-axis vertex and the opposite vertex, followed by area. '
         'Keep that connected bisector/axis chain; it is not a generic '
         'midpoint recovery from two already supplied side lines.')

    # Region decomposition is not automatically an overlapping-sector task.
    circle_splits=[
        ('triangle-minus-one-sector','Subtract a sector from its containing right triangle',
         'Use the given perpendicular sides to obtain the containing triangle and '
         'its acute angle, then subtract the single sector from that triangle.',
         'YM:C4:Try-Now-7:1',
         'Unlike overlapping-sector-area, this diagram has one sector inside '
         'one right triangle, so there is no overlap inclusion/exclusion decision.'),
        ('single-circle-sector-plus-triangles','Combine a residual sector with two inscribed triangles',
         'Use angles around one centre to recover the residual sector angle and '
         'add that sector to two equal central triangles for the shaded region.',
         'YM:C4:Exercise-4.1:5',
         'Unlike overlapping-sector-area, all arcs belong to one centre; '
         'the required region adds a residual sector and triangles rather than '
         'correcting the overlap of two sectors.'),
        ('three-tangent-sector-gap','Find the triangular gap between three externally tangent circles',
         'Recover the three right-triangle angles, verify the tangent radii '
         'fit its sides and subtract all three corner sectors from the triangle.',
         'YM:C4:Revision-Exercise-4:4',
         'Unlike overlapping-sector-area, three disjoint corner sectors '
         'are removed from a containing triangle; the gap depends on '
         'three-radius tangency and all three corner angles.')]
    for target,title,decisions,short,distinction in circle_splits:
        fork('overlapping-sector-area',target,title,decisions,
             ['M1:T5:O02:D02'],distinction,
             answer_form='Area of the specifically shaded region in square centimetres.',
             representation_and_response='Given labelled geometry to an explicit area decomposition and numerical area.')
        move('overlapping-sector-area',target,'8227:TB:'+short,
             'Rendered region and its independent R5 working establish this '
             'specific geometry/decomposition; sharing sector-area arithmetic '
             'does not make it a two-sector overlap task.')
    revise('overlapping-sector-area','Single-sector, single-centre and '
           'three-tangent-sector tasks moved to discriminating geometry families.',
           learner_decisions='Identify the two distinct sector centres and their '
           'overlap, recover their angles from the enclosing right-angle geometry '
           'and use sector-plus-sector-minus-polygon inclusion/exclusion.')

    # The composite-root label cannot absorb earlier independent quadratic tasks.
    iid='8227:TB:YM:C3:Try-Now:23'
    move('function-composite-root-condition','quadratic-completion-coefficients',iid,
         'Part (a) completes the square and identifies coefficients; the composite '
         'and repeated-root condition appear only in (d).',selected=['a'])
    move('function-composite-root-condition','function-quadratic-restricted-image',iid,
         'Part (b) reads the full-real-domain quadratic image from its completed '
         'square; it does not form or constrain a composite.',selected=['b'])
    fork('function-composite-root-condition','quadratic-completed-square-inequality-interval',
         'Use the established quadratic vertex form to solve a level inequality',
         'Reuse the completed-square expression, isolate its squared term and '
         'return the interval satisfying the strict height bound with open endpoints.',
         ['M1:T1:O06:D02'],
         'Unlike the composite repeated-root sibling, this response solves an '
         'ordinary quadratic height inequality using the already established vertex form; '
         'unlike a fresh factor/sign-chart task, completion is explicitly available.',
         answer_form='Open solution interval for f(x)<21.',
         scaffolding_and_connected_parts='Keep preceding completion/range parts as context. '
         'Only part (c) belongs to this inequality response family.',
         constraints='R5 accepted direct links are retained; this family claims only '
         'the interval/end-inclusion demand, not a newly relabelled critical-value demand.')
    move('function-composite-root-condition','quadratic-completed-square-inequality-interval',iid,
         'Part (c) solves f(x)<21 and gives an interval; it has no composite parameter '
         'or discriminant condition.',selected=['c'])
    revise('function-composite-root-condition','The earlier completion/range/inequality '
           'parts of Try Now 23 moved; only its repeated-root composite part (d) remains.')

    fork('implicit-point-gradient-line','implicit-given-point-gradient',
         'Evaluate an implicit gradient at a given point',
         'Differentiate the original implicit relation, collect its dy/dx '
         'terms and evaluate at the supplied point. No tangent/normal '
         'equation or unknown gradient-point search is requested.',
         ['M2:T4:O03:D03'],
         'Unlike implicit-point-gradient-line, the requested response is '
         'only the gradient, without a line equation or negative-reciprocal slope.')
    for short in ['Goldie:C4:Exercise-4D:2','Goldie:C4:Exercise-4D:3',
                  'YM:C11:Example:29','YM:C11:Try-Now-29:1',
                  'YM:C11:Try-Now-29:2','YM:C11:Try-Now-29:3']:
        move('implicit-point-gradient-line','implicit-given-point-gradient',
             '8227:TB:'+short,'The requested output is only the gradient '
             'at the supplied point, not a tangent or normal equation.')
    fork('implicit-point-gradient-line','implicit-prescribed-gradient-points',
         'Find points on an implicit curve with a prescribed gradient',
         'Use the established implicit derivative, impose the given slope '
         'and solve it jointly with the original curve for all admissible points.',
         ['M2:T4:O03:D03'],
         'Unlike given-point gradient evaluation, the coordinates are unknown '
         'and must satisfy both the original curve and the prescribed derivative.')
    move('implicit-point-gradient-line','implicit-prescribed-gradient-points',
         '8227:TB:YM:C11:Try-Now-29:4',
         'Only (b) recovers the two points with gradient -1; '
         'the preceding derivative proof is separately grouped.',
         selected=['b-gradient-minus-one-points'])
    move('implicit-point-gradient-line','implicit-curve-derivative',
         '8227:TB:YM:C11:Try-Now-29:4',
         'Part (a) only establishes the implicit derivative formula.',
         selected=['a-shown-derivative'])
    fork('implicit-point-gradient-line','implicit-coefficient-recovery',
         'Recover implicit-curve coefficients from a point and gradient',
         'Substitute the supplied point into the original implicit '
         'exponential relation, differentiate it and use the supplied '
         'gradient to solve the resulting coefficient conditions.',
         ['M2:T4:O03:D03'],
         'Unlike a given-point line calculation, unknown coefficients '
         'must first satisfy both incidence and derivative conditions.')
    move('implicit-point-gradient-line','implicit-coefficient-recovery',
         '8227:TB:Goldie:C4:Exercise-4D:9',
         'The question recovers k and c from point incidence and gradient; '
         'it does not ask for a tangent/normal equation.')
    revise('implicit-point-gradient-line','Gradient-only, prescribed-slope '
           'coordinate search and coefficient recovery moved to discriminating siblings.')

    fork('parametric-fixed-parameter-line','parametric-fixed-parameter-gradient',
         'Evaluate the parametric gradient at a prescribed parameter',
         'Differentiate x and y with respect to the parameter, divide '
         'dy/dt by dx/dt at a regular point and evaluate using the '
         'stated parameter and angle unit; no line equation is requested.',
         ['M2:T4:O03:D03'],
         'Unlike the fixed-parameter tangent/normal sibling, the response '
         'stops at the gradient and does not require coordinates or a line equation.')
    move('parametric-fixed-parameter-line','parametric-fixed-parameter-gradient',
         '8227:TB:Goldie:C4:Exercise-4E:2',
         'Only (i) asks for the gradient at pi/6; (ii) and (iii) ask '
         'for the tangent and normal and remain in the line family.',selected=['i'])
    move('parametric-horizontal-vertical-stationary','parametric-fixed-parameter-gradient',
         '8227:TB:YM:C11:Example:37',
         'Part (a) evaluates the regular gradient at one radian; '
         'the vertical-tangent search is the distinct part (b).',
         selected=['a-gradient-at-one'])
    fork('parametric-horizontal-vertical-stationary','parametric-vertical-tangent-existence',
         'Find or rule out vertical tangents of a parametric curve',
         'Test dx/dt=0 on the admitted parameter interval while checking '
         'dy/dt is nonzero, then recover the requested ratio/parameter '
         'or prove no such admissible point exists.',
         ['M2:T4:O03:D03'],
         'Unlike horizontal stationarity, the defining condition is '
         'a zero x derivative with nonzero y derivative, not dy/dt=0.')
    move('parametric-horizontal-vertical-stationary','parametric-vertical-tangent-existence',
         '8227:TB:YM:C11:Example:37',
         'Part (b) sets dx/dtheta=0 and recovers sin(theta) for a '
         'vertical tangent, not a stationary point.',selected=['b-vertical-sine'])
    move('parametric-horizontal-vertical-stationary','parametric-vertical-tangent-existence',
         '8227:TB:YM:C11:Try-Now-37:1',
         'The requested proof rules out dx/dt=0 for every real t; '
         'it is a vertical-tangent existence test, not horizontal stationarity.')
    revise('parametric-horizontal-vertical-stationary','Regular fixed-parameter '
           'evaluation and vertical-tangent tests moved to their own siblings.',
           title='Find and classify horizontal stationary points of a parametric curve',
           learner_decisions='Set dy/dt=0 while checking dx/dt is nonzero, '
           'recover the requested point coordinates or parameters, and '
           'classify the point where the selected source asks for its nature.')

    # Positive-exponential quadratics do not include modulus preimages or
    # a preceding independently assessed cubic coefficient/factor task.
    exponential_splits=[
        ('exponential-polynomial-hence-chain','Factor a preparatory cubic then recover exponential preimages',
         'Determine the requested cubic coefficients/zeros, factor the established '
         'polynomial and reuse its positive roots as exponential inputs before '
         'recovering all admissible exponents.',
         ['Goldie:C2:Exercise-2B:19','Goldie:C2:Exercise-2B:20'],
         'Unlike a direct exponential quadratic, the learner must first '
         'establish and factor a separate cubic before its exponential preimages.'),
        ('modulus-exponential-hence-chain','Reuse a linear modulus equation for exponential inputs',
         'Solve the initial two-modulus linear equation, reuse its admissible '
         'positive input as an exponential value and take logs to recover '
         'the exponent requested by the connected hence part.',
         ['YM:C9:Example:34','YM:C9:Try-Now-34:1'],
         'Unlike a positive-exponential quadratic, the preceding algebraic '
         'equation has two absolute values and requires sign branches, '
         'not polynomial factorisation in an exponential intermediate.'),
        ('modulus-positive-exponential-equation','Solve a modulus around a positive exponential expression',
         'Treat the exponential value as positive, open the absolute-value '
         'branches of its affine expression, solve the admissible intermediate '
         'values and recover the exponent by logarithms.',
         ['Goldie:C2:Exercise-2B:16'],
         'Unlike a quadratic in an exponential, the branch decision comes '
         'from the absolute value of its affine expression, not a square term.')]
    for target,title,decisions,shorts,distinction in exponential_splits:
        fork('exponential-positive-substitution',target,title,decisions,
             ['M2:T2:O03:D01'],distinction)
        for short in shorts:
            move('exponential-positive-substitution',target,'8227:TB:'+short,distinction)
    fork('exponential-positive-substitution','exponential-absolute-exponent-recovery',
         'Recover both signs when an earlier exponential equation uses an absolute exponent',
         'Reuse the preceding positive exponential root for 3^|x|, '
         'recover the nonnegative absolute exponent and return both permitted '
         'signs of x; an absolute value in the exponent is not an outer modulus.',
         ['M2:T2:O03:D01'],
         'Unlike the positive-exponential quadratic, this selected hence '
         'response adds the two-sided preimage of |x| after the exponential root is known.')
    move('exponential-positive-substitution','exponential-absolute-exponent-recovery',
         '8227:TB:YM:C9:Try-Now-34:3',
         'Only (b) replaces x by |x| and must recover both signs; '
         'the preceding ordinary quadratic in 3^x remains its scaffold.',
         selected=['b-absolute-x'])
    for slug in ['modulus-exponential-hence-chain',
                 'modulus-positive-exponential-equation',
                 'exponential-absolute-exponent-recovery']:
        revise(slug,'The selected source responses explicitly solve an absolute-value '
               'equation as well as exponential preimages; both demands are already '
               'accepted on every source item. No source-item tag is changed.',
               demands=['M2:T1:O01:D02','M2:T2:O03:D01'])
    revise('exponential-positive-substitution','Cubic preparation, outer-modulus '
           'and absolute-exponent tasks moved to their discriminating siblings.')

    fork('logarithm-given-graph-parameters','logarithm-base-from-point',
         'Recover a logarithm base from a stated point',
         'Substitute the stated point into y=log_a(x), rewrite in exponential '
         'form and recover the admissible positive non-unit base.',
         ['M2:T2:O02:D02'],
         'Unlike logarithm-given-graph-parameters, these questions give a '
         'point in text and request only the base; they do not ask for '
         'graph reading, reflections or another point on the drawn curve.')
    for short in ['YM:C9:Example:27','YM:C9:Try-Now-27:1']:
        move('logarithm-given-graph-parameters','logarithm-base-from-point',
             '8227:TB:'+short,'The point is given in text and the only '
             'requested response is a recovered logarithm base.')
    revise('logarithm-given-graph-parameters','Text-only base recovery moved; '
           'the given-graph, point/base and reflection chain remains.',
           difficulty_progression='single item')

    fork('motion-distance-with-reversal','motion-positive-velocity-interval',
         'Integrate a positive velocity over a stated interval',
         'Use the supplied positive rational velocity, obtain its initial '
         'signed acceleration, then integrate speed over the stated finite '
         'time interval without inserting a nonexistent reversal.',
         ['M1:T9:O04:D03'],
         'Unlike motion-distance-with-reversal, 54/(t+3)^2 stays positive on '
         'the whole journey interval, so no rest root or absolute-value '
         'piecewise distance sum is required.')
    move('motion-distance-with-reversal','motion-positive-velocity-interval',
         '8227:TB:YM:C7:Try-Now-38:2',
         'The rendered source velocity 54/(t+3)^2 is positive on [3,6]; '
         'the task requests initial acceleration and one finite distance, '
         'not rest or direction reversal.')
    revise('motion-distance-with-reversal','Positive rational-velocity '
           'task moved; only the actual reversal question remains.',
           difficulty_progression='single item')
    revise('elementary-trig-washer-volume','The given region reaches '
           'the x-axis, so its rotation uses discs, not washers.',
           title='Rotate a trig-sum region using discs and a prior identity',
           learner_decisions='Read the x-axis rotation and given finite region, '
           'form pi times the whole squared trig radius, expand its cross term '
           'and reuse the preceding square-sum identity before exact evaluation.',
           distinction_basis='Unlike an algebraic x-axis disc, the squared '
           'trig sum requires a mixed cross-term primitive and reuse of '
           'the preceding identity. There is no inner hole or radius subtraction.')

    # A domain explanation and an algebraic expansion are assessed decisions,
    # not interchangeable labels for every logarithmic primitive.
    fork('elementary-log-primitives-domains','log-primitive-explicit-validity',
         'Integrate an affine reciprocal and state the logarithm branch validity',
         'Obtain the scaled logarithmic primitive and explicitly state the input '
         'interval on which the chosen ordinary-log expression is valid; distinguish '
         'that branch from the full absolute-log primitive.',
         ['M2:T5:O01:D01'],
         'Unlike the direct-primitive sibling, the source explicitly requests '
         'the validity interval as an additional response.')
    for short in ['YM:C12:Example:6','YM:C12:Try-Now:6']:
        move('elementary-log-primitives-domains','log-primitive-explicit-validity',
             '8227:TB:'+short,'The question explicitly asks for the values of x '
             'for which the stated ordinary-log primitive is valid.')
    fork('elementary-log-primitives-domains','rational-expanded-power-log-primitive',
         'Expand a rational expression into powers and a reciprocal before integrating',
         'Expand the numerator, divide each term by the original denominator, '
         'separate the reciprocal term from ordinary powers and integrate with '
         'the original nonzero-domain exclusions retained.',
         ['M1:T9:O01:D02','M2:T5:O01:D01'],
         'Unlike the direct affine-reciprocal sibling, polynomial expansion and '
         'termwise division are needed before selecting both power and logarithm rules.')
    for short in ['YM:C12:Example:7','YM:C12:Try-Now:7']:
        move('elementary-log-primitives-domains','rational-expanded-power-log-primitive',
             '8227:TB:'+short,'The actual numerator/quotient must first be expanded '
             'and separated into power and reciprocal terms; it is not a direct log primitive.')
    revise('elementary-log-primitives-domains','Explicit validity and expansion tasks '
           'moved to their discriminating siblings.',title='Find a direct affine-reciprocal primitive',
           learner_decisions='Compensate for the denominator slope, retain the original '
           'pole exclusion and return a logarithmic primitive with an arbitrary constant. '
           'No separately requested validity explanation or numerator expansion is added.')

    # Quotient-derived trig identities are not product-derivative reversals.
    for target,title,decisions,shorts,distinction in [
        ('cotangent-quotient-hence-integrals','Derive cotangent by the quotient rule and reuse it in integrals',
         'Differentiate cos(x)/sin(x), establish the cosecant-square primitive, '
         'choose the cotangent-square identity and reuse a supplied double-angle '
         'rewrite for a further reciprocal integral.', ['YM:C12:Example:17'],
         'Unlike product reversal, the defining derivative is a quotient; '
         'the linked integrations depend on reciprocal and double-angle identities.'),
        ('secant-derived-identity-integral-chain','Derive secant and reuse identities for exact integrals',
         'Differentiate 1/cos(x), retain the derived secant-tangent primitive '
         'and combine it with the requested identity/derivative scaffolding '
         'to evaluate the original exact integral.',
         ['YM:C12:Try-Now-17:2','YM:C12:Try-Now-17:3'],
         'Unlike product reversal, the key supplied-function derivative comes '
         'from a reciprocal cosine; its integration target is a sum of known '
         'trig derivatives rather than isolating an unknown product integral.'),
        ('product-reversal-curve-conversion-chain','Reuse a product derivative through a connected curve and conversion chain',
         'Differentiate (x+3)exp(-x), reverse that result for its integral, '
         'find and classify the stationary point, and keep the requested '
         'conversion proof and its conditional final integral separately scoped.',
         ['Goldie:C8:Exercise-8C:5'],
         'Unlike the short product-reversal activity, this connected item '
         'also assesses stationary geometry and an explicitly additional '
         'general-substitution proof; the latter is not prescribed 8227 practice.')]:
        fork('given-derivative-product-reversal',target,title,decisions,
             ['M2:T5:O01:D03'],distinction)
        for short in shorts:
            move('given-derivative-product-reversal',target,'8227:TB:'+short,distinction)
    revise('given-derivative-product-reversal','Quotient-derived and extended '
           'curve/conversion chains moved; the short product isolation activity remains.',
           learner_decisions='Differentiate the given product, rearrange its '
           'derivative to isolate the target integral, then integrate the remaining '
           'standard term. No self-selected integration-by-parts method is required.')

    # Goldie 5C Q11 has different integrals, not an exact/estimate comparison.
    fork('trapezium-exact-comparison','affine-reciprocal-proper-definite-integral',
         'Evaluate a proper definite reciprocal-affine integral exactly',
         'Recognise the reciprocal-affine logarithmic primitive, retain its scale '
         'factor and evaluate the stated proper endpoints to the required exact logarithm.',
         ['M1:T9:O03:D01','M2:T5:O01:D01'],
         'Unlike rational-linear-numerator integration, the numerator is constant '
         'and no polynomial division is required; unlike trapezium estimation, '
         'the response establishes an exact logarithmic integral.',
         givens='The proper integral of 6/(2x-7) from 6 to 16, with exact target ln(125).',
         answer_form='Exact logarithmic endpoint evaluation, establishing ln(125).',
         scaffolding_and_connected_parts='Only Goldie 5C Q11(i). Part (ii) estimates '
         'a different common-log integral; no comparison between the integrals is requested.',
         units_and_precision='Dimensionless; exact natural logarithms, no decimal replacement.',
         representation_and_response='Symbolic definite integral to a justified exact logarithmic value.')
    move('trapezium-exact-comparison','affine-reciprocal-proper-definite-integral',
         '8227:TB:Goldie:C5:Exercise-5C:11',
         'Rendered PDF154 Q11(i) evaluates a reciprocal-affine exact integral; '
         'the numerical part has a different integrand and different endpoints.',selected=['i'])
    move('trapezium-exact-comparison','trapezium-prescribed-estimate',
         '8227:TB:Goldie:C5:Exercise-5C:11',
         'Rendered PDF154 Q11(ii) uses four trapezia on log10(x), from 1 to 17, '
         'and reports 3 significant figures. It does not compare with part (i).',selected=['ii'])
    retired=raw.pop(PREFIX+'trapezium-exact-comparison')
    assert not retired['member_specs']
    changes.append(dict(family_id=retired['family_id'],action='retire empty erroneous family',
                        reason='Goldie 5C Q11(i) and (ii) have different integrals; '
                        'there is no assessed exact-versus-approximate comparison.'))

    # Native core-calculus review: output and inverse conditions are distinct.
    fork('curve-first-derivative-point','curve-recovery-intercept-target',
         'Recover an axis intercept from a derivative and a known curve point',
         'Integrate the supplied derivative, fix the integration constant from '
         'the given point, then evaluate at x=0 to return the requested ordinate.',
         ['M1:T9:O02:D02'],
         'Unlike curve-first-derivative-point, the final requested response is an '
         'axis intercept, not the equation of the curve; the recovery is an intermediate step.',
         answer_form='The requested y-axis ordinate after particular-curve recovery.')
    move('curve-first-derivative-point','curve-recovery-intercept-target',
         '8227:TB:YM:C7:Example:9',
         'Rendered PDF331 asks only for the y-coordinate of B. The affine-power '
         'singularity and accepted source interpretation remain in its item record.')
    fork('gradient-function-extremum','stationary-polynomial-read-and-recover',
         'Read a repeated axis root and recover the other stationary abscissa',
         'Read the repeated x-axis minimum from the factorised cubic and use '
         'its derivative to find the distinct maximum abscissa.',
         ['M1:T8:O04:D01'],
         'Unlike gradient-function-extremum, these preparatory responses concern '
         'the original curve; they do not minimise its gradient function.')
    move('gradient-function-extremum','stationary-polynomial-read-and-recover',
         '8227:TB:YM:C6:Revision-Exercise-6:4',
         'Rendered PDF319 (a)-(b) concern the cubic curve; (c) alone minimises f-prime.',
         selected=['a','b'])
    revise('gradient-function-extremum','Only the minimum-gradient response remains.',
           learner_decisions='Differentiate the given cubic to obtain its quadratic '
           'gradient function, minimise that derivative and return the least gradient value.',
           answer_form='Minimum value of dy/dx, not a coordinate or value of the original curve.')
    fork('connected-rate-inverse','connected-rate-location-from-ratio',
         'Recover a curve location from a prescribed ratio of changing rates',
         'Relate the two changing rates through dy/dx, impose their given ratio '
         'and solve for all admissible curve inputs.',
         ['M1:T8:O03:D03'],
         'Unlike connected-rate-inverse, the unknown is a location satisfying a '
         'rate ratio, not the instantaneous input rate at a known location.')
    for short in ['YM:C6:Example:24','YM:C6:Try-Now-24:1']:
        move('connected-rate-inverse','connected-rate-location-from-ratio','8227:TB:'+short,
             'The requested x-values are obtained from the given rate ratio; no '
             'unknown instantaneous rate is the final response.')
    revise('connected-rate-inverse','Location recovery moved to its own inverse-condition sibling.',
           learner_decisions='Differentiate the known geometric/function relation '
           'and invert the chain-rate equation to recover the requested input rate '
           'from a known output rate at a specified location.')
    fork('motion-derivative-chain','motion-rest-and-extremum-sketch-chain',
         'Derive motion quantities, find rest/extrema and sketch acceleration',
         'Differentiate displacement for velocity and acceleration, identify '
         'rest and the greatest velocity, and sketch the acceleration-time graph.',
         ['M1:T8:O03:D04'],
         'Unlike motion-derivative-chain, this item also requires inverse rest '
         'and extremum conditions and a graph, rather than evaluation at a supplied time.')
    move('motion-derivative-chain','motion-rest-and-extremum-sketch-chain',
         '8227:TB:YM:C7:Try-Now-39:3',
         'The original accepted labels explicitly require rest, maximum velocity '
         'and an acceleration sketch in addition to derivative expressions.')

    # B.3: the optimisation neighbours differ in the model decision, not topic.
    optimisation_neighbours = {
        'optimise-closed-cuboid-area': ('optimise-open-square-tank',
            'Count six closed-box faces, retain the specified base-side ratio and '
            'fixed volume, rather than five open-tank faces after a capacity conversion.'),
        'optimise-closed-cuboid-volume': ('optimise-closed-cuboid-area',
            'Use fixed total area to eliminate height and maximise volume, rather '
            'than use fixed volume to eliminate height and minimise material area.'),
        'optimise-open-square-tank': ('optimise-closed-cuboid-area',
            'Convert capacity to cubic centimetres and omit the lid from material '
            'area; the closed cuboid includes both bases and a stated base-side ratio.'),
        'optimise-closed-cylinder-area': ('optimise-closed-cuboid-area',
            'Count two circular ends and curved lateral area using circumference, '
            'rather than six flat cuboid faces, before eliminating fixed-volume height.'),
        'optimise-split-wire-loops': ('optimise-quarter-disc-plate',
            'Allocate one wire between two separate closed loops; the plate instead '
            'counts the external boundary of two joined regions and omits their shared edge.'),
        'optimise-quarter-disc-plate': ('optimise-rectangle-under-line',
            'Eliminate length using an external perimeter containing a circular arc; '
            'the rectangle uses a line through known intercepts to supply its height.'),
        'optimise-L-garden': ('optimise-shared-fences',
            'Count the concave external boundary and combine two nonoverlapping '
            'rectangles; the pen model additionally counts interior shared fences once.'),
        'optimise-cylinder-in-cone': ('optimise-closed-cuboid-volume',
            'Derive the height-radius constraint from similar triangles inside a '
            'cone; the cuboid uses fixed material area and has no containment constraint.'),
        'optimise-rectangle-under-line': ('optimise-quarter-disc-plate',
            'Derive height from the line through two intercepts and optimise inside '
            'that segment, rather than eliminate length using an arc-containing perimeter.'),
        'optimise-shared-fences': ('optimise-L-garden',
            'Include interior pen-dividing fences exactly once and recover one '
            'pen dimension; the garden counts only its concave external boundary.'),
        'optimise-open-triangular-container': ('optimise-closed-cuboid-volume',
            'Recover the 5:5:8 cross-section height, count triangular ends and two '
            'open-top lateral faces, then eliminate length using card area; the closed '
            'square-base cuboid counts six rectangular faces.')}
    for slug, (sibling, difference) in optimisation_neighbours.items():
        revise(slug, 'B.3 nearest-sibling decision comparison.',
               nearest_sibling_family_id=PREFIX+sibling,
               distinction_basis='Compared with '+sibling+': '+difference)

    # B.3-B.5 explicit prose edits are versioned author inputs, not inferred
    # from a broad topic or generated from a repeated disclaimer.
    from analysis_sources import WB
    prose=json.loads((WB/'tools/textbook-family-prose-r6.json').read_text())
    for patch in prose['entries']:
        fid=patch['family_id'];assert fid in raw
        if 'nearest_sibling_family_id'in patch:assert patch['nearest_sibling_family_id']in raw
        fields={k:v for k,v in patch.items()if k!='family_id'}
        revise(fid.removeprefix(PREFIX),'Explicit R6 family prose review.',**fields)

    for f in raw.values():
        assert f['member_specs'], ('empty family after R6 repair', f['family_id'])
    return raw, changes
