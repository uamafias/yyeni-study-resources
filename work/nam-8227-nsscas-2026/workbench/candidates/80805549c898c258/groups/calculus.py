"""NSSCAS 8227 author-verified Stage E calculus generators.

No learner attempts are interpreted here. Criterion expectations are a memo for a
trusted marking orchestration layer, not a claim to read free-text/photographs.
The finite domains were selected in the owner-approved Stage D design. Parameter
validation is strict; exposure identities intentionally contain no recipe version.
"""
from copy import deepcopy
from fractions import Fraction
from itertools import product
import json
from math import comb, exp
from pathlib import Path

RECIPES = ['WB8227-implicit-normal', 'WB8227-stationary-inflexion', 'WB8227-motion-integration']
DATA_PATH = Path(__file__).resolve().parents[1] / 'domains' / 'calculus.json'
_DATA = json.loads(DATA_PATH.read_text(encoding='utf-8'))


def choices():
    return deepcopy(_DATA['choices'])


def _key(*parts):
    return json.dumps(parts, separators=(',', ':'), ensure_ascii=False)


def _frac(value):
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    sign = '-' if value < 0 else ''
    return rf'{sign}\frac{{{abs(value.numerator)}}}{{{value.denominator}}}'


def _poly(coefficients, variable='x'):
    """Descending coefficients; remove zero/one terms and doubled signs."""
    terms = []
    degree = len(coefficients) - 1
    for index, coefficient in enumerate(coefficients):
        coefficient = Fraction(coefficient)
        if coefficient == 0:
            continue
        power = degree - index
        atom = variable if power == 1 else (rf'{variable}^{{{power}}}' if power else '')
        magnitude = '' if abs(coefficient) == 1 and power else _frac(abs(coefficient))
        term = magnitude + atom
        if not terms:
            terms.append(('-' if coefficient < 0 else '') + term)
        else:
            terms.append((' - ' if coefficient < 0 else ' + ') + term)
    return ''.join(terms) or '0'


def _shift(h, variable='x'):
    return variable if h == 0 else (rf'({variable} - {h})' if h > 0 else rf'({variable} + {-h})')


def _multiple(coefficient, atom):
    coefficient = Fraction(coefficient)
    return atom if coefficient == 1 else ('-' + atom if coefficient == -1 else _frac(coefficient) + atom)


def _step(action, reason, result):
    return {'action': action, 'reason': reason, 'result': result}


_RULES = {
 'G1': ('M', 'Attempt the exponential product derivative, with both contributions; one numerical slip is allowed, an omitted factor is not.', []),
 'G2': ('A', 'Correct complete exponential product derivative, including the chain factor.', ['G1']),
 'G3': ('B', 'Show the implicit derivative of y squared and the zero derivative of the constant.', []),
 'G4': ('M', 'Substitute the given point into a credible differentiated relation and solve; substitution before isolation is allowed.', ['G1|G3']),
 'G5': ('A', 'Canonical exact or correctly rounded 3 s.f. gradient, from correct derivative working and credible substitution; no ordinary final-accuracy follow-through, without wrong working.', ['G4']),
 'S1': ('M', 'Attempt a complete differentiation of the product (or an approved equivalent relation), allowing one numerical slip but no omitted contribution.', []),
 'S2': ('A', 'Correct exponential/product/composite differentiation on the selected valid route.', ['S1']),
 'S3': ('B', 'Correct remaining implicit derivative and constant zero; on the explicit-root route justify the root/y identity.', []),
 'S4': ('A', 'Complete correct forward derivation establishes the supplied target or a demonstrated equivalent; all preceding proof evidence is correct and complete. No follow-through into the supplied result.', ['S1','S2','S3']),
 'H1': ('M', 'Substitute the point into the displayed derivative or a credible derivative from the proof, respecting hence.', []),
 'H2': ('A', 'Canonical exact or 3 s.f. gradient after valid substitution; no ordinary final-accuracy follow-through.', ['H1']),
 'N1': ('M', 'Show or state a labelled perpendicular gradient equal to minus the reciprocal of their credible finite nonzero tangent gradient.', []),
 'N2': ('DM', 'Construct the line through the supplied point using their perpendicular gradient; limited method follow-through.', ['N1']),
 'N3': ('A', 'Canonical exact normal in any equivalent line form after visible normal working; ordinary final accuracy is not follow-through.', ['N1','N2']),
 'P1': ('M', 'Visible power differentiation attempt on the supplied expanded polynomial.', []),
 'P2': ('A', 'Correct complete derivative.', []),
 'P3': ('DM', 'Set a credible derivative equal to zero and show valid factorisation or a complete quadratic-formula substitution.', ['P1']),
 'P4': ('A', 'Both complete canonical stationary coordinates, with the x solve and evaluation of the original function shown.', ['P3']),
 'C1': ('M', 'Show a valid local test at both credible stationary roots, using substitutions or a coherent sign argument; limited own-derivative/point follow-through.', []),
 'C2': ('A', 'Both canonical types justified by the shown local test; no ordinary final-accuracy follow-through.', ['C1']),
 'I1': ('B', 'Correct polynomial derivative, including its coefficient.', []),
 'I2': ('M', 'Set a credible derivative equal to zero and visibly solve its repeated-factor equation; a binomial-cube or valid factor-theorem/division route is accepted.', []),
 'I3': ('A', 'Exact full canonical point after a visible stationary solve and substitution in the original polynomial.', ['I2']),
 'I4': ('B', 'Correct actual two-sided derivative behaviour, with stated point substitutions or valid power/sign reasoning.', []),
 'I5': ('M', 'Apply a valid local classification test to that evidence, ruling out the other types; limited follow-through from credible prior work.', []),
 'I6': ('A', 'Canonical type justified by the valid test, not merely f second equal to zero.', ['I5']),
 'V1': ('M', 'Visible acceleration integration attempt with at least one correct term.', []),
 'V2': ('A', 'Correct velocity primitive before fixing its constant.', ['V1']),
 'V3': ('A', 'Correct use of the given initial velocity to fix the integration constant.', ['V1']),
 'S1-motion': ('M', 'Visible integration of their credible velocity with at least one correct term.', []),
 'S2-motion': ('A', 'Correct integration of that velocity, with limited own-answer follow-through.', ['S1']),
 'S3-motion': ('A', 'Canonical exact or 3 s.f. total distance with both bounds and metres; depends on the integration method and primitive accuracy. Eligible MR03 misreads are the explicit final-accuracy exception.', ['S1','S2']),
 'E1': ('B', 'Correct coefficient minus k times V, with differentiation working.', []),
 'E2': ('B', 'Retain the exponential factor in an attempted derivative whose coefficient is not plus or minus V/k; the integrated-coefficient error is excluded.', []),
 'E3': ('B', 'Correct exponential primitive minus V/k times the exponential.', []),
 'E4': ('M', 'Use both bounds in an attempted integral with coefficient not minus kV, or impose d(0)=0 on that primitive; correct integration constant may imply the zero-time substitution.', []),
 'E5': ('A', 'Canonical exact or 3 s.f. travelled length in metres, with the required integration working.', ['E4']),
 'R1': ('M', 'Solve v=0 with at most one algebra/arithmetic slip and coherently compare roots/signs with the interval, or give a complete valid constant-sign argument. A vertex value alone is insufficient.', []),
 'R2': ('B', 'Correct cubic primitive.', []),
 'R3': ('DM', 'Using an attempted primitive, evaluate both bounds on every chosen sign-constant leg and combine nonnegative lengths. Limited own-root follow-through after a credible solve/decision.', ['R1']),
 'R4': ('A', 'Canonical total distance in metres, with correct primitive, valid leg construction and without wrong working. A false-root numerical coincidence does not qualify.', ['R2','R3']),
 'R5': ('M', 'Signed whole-interval integration with an attempted primitive and both bounds, or the signed sum of evaluated primitive legs from distance working.', []),
 'R6': ('A', 'Canonical signed displacement in metres after the signed integration method.', ['R5']),
}


def _criteria(suffixes, motion=False):
    out=[]
    for suffix in suffixes:
        rule_key = suffix+'-motion' if motion and suffix in ('S1','S2','S3') else suffix
        mark_type, achievement, depends = _RULES[rule_key]
        out.append({'criterion_id':suffix, 'marks':1, 'mark_type':mark_type, 'achievement':achievement,
                    'depends_on':depends, 'dependencies_use':'gross-earned-before-MR03-net-deduction',
                    'answer_only_credit':0,
                    'misread_policy_id':'MR03-OPS-D4',
                    'mr09_supplied_result_exclusion':suffix=='S4' and not motion})
    return out


def _part(local, prompt, answer, steps, suffixes, *, motion=False, alternatives=None):
    return {'local_part_id':local,'prompt':prompt,'reference_answer':answer,
            'worked_steps':steps,'criteria':_criteria(suffixes,motion),
            'accepted_alternatives':alternatives or [],'answer_only_credit':0}


def _base(stem, parts, keys, private, prompts):
    return {'stem':stem,'parts':parts,'assets':[], 'exposure_keys':keys,
            'private_math':private,
            'practice_help':{'title':'Plan your working','prompts':prompts},
            'misread_policy':{
                'operational_policy_id':'MR03-OPS-D4','approval':'Vitalis exact Stage-D manifest 4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec',
                'rule':'Judge gross evidence and dependencies first; an eligible question-data misread costs one earned A/B mark once per datum, in question/criterion order, carrying forward if needed. Never deduct from M/DM. Eligible follow-through does not override MR09 supplied-result proof requirements or OD-1 required working.',
                'eligibility':'Decide once at first use for the connected question; a changed object/difficulty or own-figure slip remains canonical throughout.',
                'competing_datum_settlement':'Unresolved E/F carry: competing eligible data sharing an earned mark require an explicit accepted settlement; do not infer a grade from datum list order.'},
            'exposure_policy':'All assessed-part and shared exposure keys must be unseen for wholly fresh use, across output-affecting revisions. Version is provenance and never resets exposure. Disclosed repeated-component practice is separate; do not silently switch branches on exhaustion.'}


def _implicit(branch,p):
    a,k,q=(p[x] for x in ('a','k','q'));C=q*(a+q)
    m=Fraction(-a*k*q,a+2*q);normal=-1/m
    exponential=rf'e^{{{k}x}}'
    ae=_multiple(a,exponential)
    ak_e=_multiple(a*k,exponential)
    target=rf'-\frac{{{a*k}{exponential}y}}{{{ae}+2y}}'
    stem=rf'A curve has equation ${ae}y+y^2={C}$. The point $P=(0,{q})$ lies on the curve.'
    differentiated=rf'${ak_e}y+{ae}y\prime+2yy\prime=0$'
    proof_steps=[
      _step('Differentiate the exponential product','Both factors depend on x; include the exponential chain factor.',rf'${ak_e}y+{ae}y\prime$'),
      _step('Differentiate the remaining terms','y depends on x; the right-hand side is constant.',r'$\frac{d}{dx}(y^2)=2yy\prime$, $\frac{dC}{dx}=0$'),
      _step('Collect terms containing the derivative','Isolate the requested derivative by forward algebra.',rf'$({ae}+2y)y\prime=-{ak_e}y$'),
      _step('Divide by the nonzero coefficient','The expression is valid on a local branch where the denominator is nonzero.',rf'$y\prime={target}$')]
    substitution=_step('Substitute the supplied point','Use the derivative at P, keeping exact arithmetic.',rf'$m=-\frac{{({a})({k})({q})}}{{{a}+2({q})}}={_frac(m)}$')
    alternatives=[{'method':'local explicit quadratic root','requirements':'Solve the original quadratic for its local y branch, differentiate correctly, substitute P. Alternative fills the same slots, never adds credit.',
                   'formula':r'$y=\frac{-'+ae+r'+\sigma\sqrt{'+str(a*a)+rf'e^{{{2*k}x}}'+(' + ' if C>0 else ' - ')+str(abs(4*C))+r'}}{2}$, $\sigma=\operatorname{sign}('+str(a+2*q)+')$'},
                  {'method':'divided relation','requirements':'C is nonzero so y is nonzero; differentiate ae^(kx)+y=C/y then back-substitute C to establish the target. Missing back-substitution loses S4 only after correct S1/S2/S3.'},
                  {'method':'log-absolute relation','requirements':'Use ln a+kx=ln|C-y²|-ln|y| and complete correct back-substitution. ln y is invalid on the negative-y branch; at most independent S3 is possible.'}]
    if branch=='gradient':
        parts=[_part('gradient','Find the gradient at P, showing all working. Give an exact value or a correctly rounded 3 significant figure decimal.',rf'${_frac(m)}$',proof_steps+[substitution],['G1','G2','G3','G4','G5'],alternatives=alternatives)]
    else:
        parts=[_part('show-derivative',rf'Show that $y\prime={target}$ where the denominator is nonzero, showing all necessary working.',rf'$y\prime={target}$',proof_steps,['S1','S2','S3','S4'],alternatives=alternatives),
               _part('gradient','Hence, using your derivative or the displayed formula, find the gradient at P. Show your substitution; give an exact value or a correctly rounded 3 significant figure decimal.',rf'${_frac(m)}$',[substitution],['H1','H2']),
               _part('normal','Find the exact equation of the normal at P. Show the perpendicular-gradient and line-construction steps.',rf'$y={_poly([normal,q])}$',[
                 _step('Find the perpendicular gradient','A finite nonzero tangent gradient has perpendicular gradient minus its reciprocal.',rf'$m_\perp=-\frac{{1}}{{{_frac(m)}}}={_frac(normal)}$'),
                 _step('Construct the line through P','Use point-gradient form with the perpendicular gradient.',rf'$y-({q})={_frac(normal)}(x-0)$'),
                 _step('Simplify the equation','Equivalent exact affine forms describe the same line.',rf'$y={_poly([normal,q])}$')],['N1','N2','N3'])]
    keys=[_key('implicit-curve',a,k,C),_key('implicit-point',a,k,C,q)]
    if branch=='normal': keys += [_key('implicit-show',a,k),_key('implicit-normal',a,k,C,q)]
    private={'parameters':p,'C':C,'gradient':str(m),'normal_slope':str(normal),'normal_intercept':q,
             'derivative_math':{'numerator_coefficient':-a*k,'exponent_coefficient':k,'denominator_coefficients':[a,2]},
             'misread_eligibility':'Finite AND nonzero gradient required; preserve the supplied point on the curve and the genuine nonunit exponential-chain demand. A supplied proof target remains fixed under MR09.',
             'nondiagnostic_numeric_collision':'The wrong exponential index derivative coincides at x=0 in every admitted tuple; visible wrong working loses G2/G5, so no diagnosis is inferred from the number alone.',
             'open_fixture':'Ineligible C misread product route can still score canonical 9/9 because C is never used. Divided/log-absolute/explicit-root routes remain E/F fixtures without a new score ruling.'}
    return _base(stem,parts,keys,private,['Which factors depend on x?','Differentiate before substituting a point.']+(['For a normal, how is its gradient related to the tangent gradient?'] if branch=='normal' else []))


def _stationary(branch,p):
    a,h,c=p['a'],p['h'],p['c']
    if branch=='two-extrema':
        r=p['r']; coeff=[a,-3*a*h,3*a*h*h-3*a*r*r,-a*h**3+3*a*r*r*h+c]
        d=[3*a,-6*a*h,3*a*h*h-3*a*r*r]
        xs=[h-r,h+r];ys=[c+2*a*r**3,c-2*a*r**3]
        types=['maximum','minimum'] if a>0 else ['minimum','maximum']
        factor=_multiple(3*a,_shift(xs[0])+_shift(xs[1]))
        pts=' and '.join(rf'$({x},{y})$' for x,y in zip(xs,ys))
        location=[_step('Differentiate the expanded polynomial','At a stationary point the first derivative is zero.',rf'$f\prime(x)={_poly(d)}$'),
                  _step('Set the derivative equal to zero and factorise','Visible algebra is needed to locate every stationary abscissa.',rf'${factor}=0$, so $x={xs[0]}$ or $x={xs[1]}$'),
                  _step('Evaluate the original function at both roots','The derivative gives x; y comes from the original polynomial.',pts)]
        second=[-6*a*r,6*a*r]
        classification=[_step('Apply a local test at both points','A negative second derivative gives a maximum and a positive value gives a minimum.',rf'$f\prime\prime(x)={_poly([6*a,-6*a*h])}$; $f\prime\prime({xs[0]})={second[0]}$, $f\prime\prime({xs[1]})={second[1]}$'),
                        _step('Conclude each type from its test','Link both classifications to the signs shown.',f'The point {pts.split(" and ")[0]} is a {types[0]}; {pts.split(" and ")[1]} is a {types[1]}.')]
        parts=[_part('points','Find the exact coordinates of both stationary points, showing all working.',pts,location,['P1','P2','P3','P4']),
               _part('nature','Classify both stationary points and justify each type with sufficient evidence.',f'Left point: {types[0]}; right point: {types[1]}.',classification,['C1','C2'],alternatives=[{'method':'first-derivative signs','requirements':'Show correct local signs at both credible roots and connect each sign transition to the type. No extra second-derivative test is needed.'}])]
        canonical=min((a,h,r),(-a,-h,r));keys=[_key('stationary-points',*coeff),_key('two-extrema-shape',canonical)]
        private={'parameters':p,'polynomial_coefficients':coeff,'derivative_coefficients':d,'stationary_points':list(map(list,zip(xs,ys))),'types':types,'classification_key':keys[1]}
    else:
        n=p['power'];coeff=[a*comb(n,j)*(-h)**j for j in range(n+1)];coeff[-1]+=c
        d=[coeff[i]*(n-i) for i in range(n)]
        factor=_multiple(n*a,_shift(h)+rf'^{{{n-1}}}')
        left=n*a*(-1)**(n-1);right=n*a
        typename='stationary point of inflexion' if n==3 else ('minimum' if a>0 else 'maximum')
        evidence='the derivative keeps the same sign on both sides and is zero at the point, so there is no local extremum and this polynomial has a stationary point of inflexion' if n==3 else ('the derivative changes from negative to positive, so the point is a minimum' if a>0 else 'the derivative changes from positive to negative, so the point is a maximum')
        location=[_step('Differentiate the supplied expanded polynomial','Stationary points satisfy f prime equal to zero.',rf'$f\prime(x)={_poly(d)}$'),
                  _step('Set the derivative equal to zero and show the repeated factor','Recognise the binomial power, or verify and divide out the repeated factor.',rf'${factor}=0$, so $x={h}$'),
                  _step('Substitute in the original function','Use f, rather than f prime, for the ordinate.',rf'$f({h})={c}$, so the point is $({h},{c})$.')]
        classification=[_step('Check the derivative on both sides','This polynomial has no other derivative root; a two-sided first-derivative test suffices.',rf'$f\prime({h-1})={left}$, $f\prime({h})=0$, $f\prime({h+1})={right}$'),
                        _step('Use the local sign behaviour','A zero second derivative alone would not settle the type.',evidence[0].upper()+evidence[1:]+'.'),
                        _step('State the justified type','The test rules out the other stationary types.',rf'$({h},{c})$ is a {typename}.')]
        parts=[_part('point','Find the exact coordinates of every stationary point, showing all working.',rf'$({h},{c})$',location,['I1','I2','I3']),
               _part('classification','Classify each stationary point as a maximum, minimum or stationary point of inflexion. Give sufficient evidence to justify the type and rule out the other types.',typename.capitalize()+'.',classification,['I4','I5','I6'],alternatives=[{'method':'second-derivative neighbourhood, local increments, or higher derivative','requirements':'A complete valid local argument fills the same slots. f second at the stationary point equal to zero alone earns no classification credit.'}])]
        canonical=min((n,a,h),(n,(-1)**n*a,-h));keys=[_key('flat-point',*coeff),_key('flat-shape',canonical)]
        private={'parameters':p,'polynomial_coefficients':coeff,'derivative_coefficients':d,'stationary_points':[[h,c]],'types':[typename], 'derivative_sample_values':[left,0,right],'classification_key':keys[1]}
    stem=rf'For the function $f(x)={_poly(coeff)}$, answer the following.'
    return _base(stem,parts,keys,private,['Find stationary abscissae from the derivative, then use the original function for their ordinates.','Which local test justifies the type?','Show the algebra and the evidence supporting your conclusion.'])


def _motion(branch,p):
    if branch=='polynomial-chain':
        A,B,u,T=(p[x] for x in ('A','B','u','T'));v=[A,B,u];F=[Fraction(A,3),Fraction(B,2),u,0]
        d=Fraction(A*T**3,3)+Fraction(B*T*T,2)+u*T
        stem=rf'A particle moves along a straight line. Its acceleration is $a(t)={_poly([2*A,B],"t")}$ m/s², its initial velocity is ${u}$ m/s, and its position is $s(0)=0$. Time $t$ is in seconds.'
        parts=[_part('velocity','Find v in terms of t, showing your integration and use of the initial condition.',rf'$v(t)={_poly(v,"t")}$ m/s',[
             _step('Integrate the acceleration','Velocity is a primitive of acceleration.',rf'$v(t)={_poly([A,B,0],"t")}+C$'),
             _step('Use the initial velocity','The initial condition determines the integration constant.',rf'$v(0)={u}$ gives $C={u}$'),
             _step('Write the velocity function','Retain the constant term for later distance calculation.',rf'$v(t)={_poly(v,"t")}$ m/s')],['V1','V2','V3']),
            _part('distance',f'Find the distance travelled in the first {T} seconds, in metres, showing your working. Give an exact answer or a value correct to 3 significant figures.',rf'${_frac(d)}$ m',[
             _step('Check the sign of velocity','All terms are nonnegative for t at least zero and the constant is positive, so no direction change occurs.',rf'$v(t)>0$ for $0\le t\le {T}$'),
             _step('Integrate velocity','For positive velocity the integral gives total travelled length.',rf'$F(t)={_poly(F,"t")}$'),
             _step('Evaluate both bounds','Use F(T) minus F(0), retaining exact arithmetic.',rf'$d=F({T})-F(0)={_frac(d)}$ m')],['S1','S2','S3'],motion=True)]
        keys=[_key('motion-velocity',A,B,u),_key('motion-polynomial-distance',A,B,u,T)]
        private={'parameters':p,'velocity_coefficients':v,'primitive_coefficients':[str(v) for v in F],'distance':str(d),'displacement':str(d),'velocity_positive':True}
    elif branch=='exponential-positive':
        V,T=p['V'],p['T'];k=Fraction(p['k']);coef=-V*k;primitive=-Fraction(V,1)/k
        exponential=rf'e^{{-{_frac(k)}t}}'
        distance=rf'{_frac(-primitive)}\left(1-e^{{-{_frac(k*T)}}}\right)'
        stem=rf'A particle moves along a straight line with velocity $v(t)={V}{exponential}$ m/s for $t\ge0$. Time $t$ is in seconds.'
        parts=[_part('acceleration','Find the acceleration a(t), showing your differentiation.',rf'$a(t)={_multiple(coef,exponential)}$ m/s²',[
             _step('Differentiate the exponential velocity','Apply the exponential chain rule.',rf'$a(t)={V}\left(-{_frac(k)}\right){exponential}$'),
             _step('Simplify the coefficient','Acceleration retains the exponential factor.',rf'$a(t)={_multiple(coef,exponential)}$ m/s²')],['E1','E2']),
            _part('distance',f'Find the distance travelled in the first {T} seconds, in metres. Show your integration and use of both boundary conditions. Give an exact answer or a value correct to 3 significant figures.',rf'${distance}$ m',[
             _step('Check velocity remains positive','The exponential and its amplitude are positive, so distance is the velocity integral.',rf'$v(t)>0$ on $[0,{T}]$'),
             _step('Integrate the exponential','Divide its amplitude by the exponent coefficient.',rf'$F(t)={_multiple(primitive,exponential)}$'),
             _step('Use both bounds','The zero-time exponential equals one.',rf'$d=F({T})-F(0)={distance}$ m')],['E3','E4','E5'])]
        keys=[_key('motion-exponential-acceleration',V,str(k)),_key('motion-exponential-distance',V,str(k),T)]
        private={'parameters':p,'acceleration_coefficient':str(coef),'primitive_coefficient':str(primitive),'distance_exact_form':{'amplitude':str(-primitive),'exponent':str(-k*T)},'distance_numeric':float(-primitive)*(1-exp(float(-k*T))),
                 'misread_eligibility':'MR03-OPS-D4: preserve V>0 and nonzero, nonunit k. Reading k as 1 removes the chain-factor demand and changes difficulty, so it is ineligible.'}
    else:
        k,r,c,T=(p[x] for x in ('k','r','c','T'));v=[k,k*(c-r),-k*r*c];F=[Fraction(k,3),Fraction(k*(c-r),2),-k*r*c,0]
        def at(t):return Fraction(k*t**3,3)+Fraction(k*(c-r)*t*t,2)-k*r*c*t
        cuts=[0]+([r] if 0<r<T else [])+[T];legs=[at(b)-at(a) for a,b in zip(cuts,cuts[1:])]
        d=sum(abs(z) for z in legs);s=at(T)
        stem=rf'A particle moves along a straight line with velocity $v(t)={_poly(v,"t")}$ m/s for $0\le t\le {T}$, with $t$ in seconds. Positive velocity is motion in the positive direction.'
        rootline=rf'$v(t)={_multiple(k,_shift(r,"t")+_shift(-c,"t"))}=0$, so $t={-c}$ or $t={r}$'
        decision=(rf'Only $t={r}$ lies in $(0,{T})$; the simple root changes the velocity sign.' if r<T else rf'Neither root lies in $(0,{T})$; $v(0)={-k*r*c}$ and velocity keeps this sign throughout.')
        terms=' + '.join(rf'\left|F({b})-F({a})\right|' for a,b in zip(cuts,cuts[1:]))
        parts=[_part('distance',f'Find the total distance travelled in the first {T} seconds, in metres, justifying your working. Give an exact answer or a value correct to 3 significant figures.',rf'${_frac(d)}$ m',[
             _step('Find the velocity zeros','Direction can change only where velocity is zero.',rootline),
             _step('Compare the roots with the interval and check signs','Distance adds positive leg lengths; a root outside the interval does not require a direction split.',decision),
             _step('Find a primitive of the expanded velocity','Use the same velocity for each travelled leg.',rf'$F(t)={_poly(F,"t")}$'),
             _step('Evaluate both bounds on each sign-constant leg','Take the absolute value of each signed leg integral.',rf'$d={terms}={_frac(d)}$ m')],['R1','R2','R3','R4'],alternatives=[{'method':'integral of absolute velocity','requirements':'Justify the sign decomposition and evaluate primitive bounds on all legs; same four slots.'},{'method':'constant-sign argument','requirements':'When valid, endpoint signs plus appropriate concavity, or a complete root/sign argument, replaces the root-solve route in R1. A vertex value alone is insufficient.'}]),
            _part('displacement',f'Find the signed displacement in the first {T} seconds, in metres, showing your working. Give an exact answer or a value correct to 3 significant figures.',rf'${_frac(s)}$ m',[
             _step('Use a signed whole-interval integral','Displacement preserves signs rather than adding unsigned distances.',rf'$s({T})-s(0)=F({T})-F(0)$'),
             _step('Evaluate the bounds','The previously found primitive may be reused.',rf'$F({T})-F(0)={_frac(s)}$ m')],['R5','R6'],alternatives=[{'method':'signed sum of travel legs','requirements':'Reuse evaluated primitive legs with their signs, not calculator-only unworked values.'}])]
        task=_key('motion-quadratic-bounded',k,r,c,T)
        keys=[task]
        private={'parameters':p,'velocity_coefficients':v,'primitive_coefficients':[str(x) for x in F],'roots':[-c,r],'interior_roots':([r] if r<T else []),'signed_legs':[str(x) for x in legs],'distance':str(d),'displacement':str(s),'sign_change':r<T,
                 'polynomial_model_key':_key('motion-quadratic-model',*v),'part_semantic_keys':{'distance':task,'displacement':task},
                 'model_exposure_note':'Track the polynomial model, but do not impose a new model-no-repeat restriction reducing the approved 168 bounded tasks.'}
    return _base(stem,parts,keys,private,['Distinguish acceleration, velocity and position.','Write a primitive and use the stated initial or boundary conditions.','For total distance, justify whether velocity changes sign in the given interval.'])


def build(recipe_id,branch_id,parameters):
    branch=branch_id.split(':')[-1]
    choice=next((x for x in _DATA['choices'] if x['recipe_id']==recipe_id and x['branch_id']==branch),None)
    if choice is None:
        raise ValueError('Unknown calculus recipe branch')
    if not isinstance(parameters,dict) or parameters not in choice['parameters']:
        raise ValueError('Parameters are outside the owner-approved finite calculus domain')
    # Prevent bool/int equivalence and accidental extra/coerced fields.
    if any(type(parameters[k]) is not type(choice['parameters'][0][k]) for k in parameters):
        raise ValueError('Parameter types must match the approved domain')
    p=deepcopy(parameters)
    if recipe_id=='WB8227-implicit-normal':result=_implicit(branch,p)
    elif recipe_id=='WB8227-stationary-inflexion':result=_stationary(branch,p)
    else:result=_motion(branch,p)
    result.update(recipe_id=recipe_id,branch_id=branch,selection_id=choice['selection_id'],recipe_version='0.1.4',parameters=p)
    local_key = {
      'gradient':lambda:{'gradient':result['exposure_keys'][1]},
      'normal':lambda:{'show-derivative':result['exposure_keys'][2],'gradient':result['exposure_keys'][1],'normal':result['exposure_keys'][-1]},
      'two-extrema':lambda:{'points':result['exposure_keys'][0],'nature':result['exposure_keys'][-1]},
      'flat-classification':lambda:{'point':result['exposure_keys'][0],'classification':result['exposure_keys'][-1]},
      'polynomial-chain':lambda:{'velocity':result['exposure_keys'][0],'distance':result['exposure_keys'][-1]},
      'exponential-positive':lambda:{'acceleration':result['exposure_keys'][0],'distance':result['exposure_keys'][-1]},
      'interior-reversal':lambda:{'distance':result['exposure_keys'][0],'displacement':result['exposure_keys'][0]}}[branch]()
    suffix_to_id={c['criterion_id']:f"{recipe_id}@0.1.4:{branch}:{part['local_part_id']}:{c['criterion_id']}" for part in result['parts'] for c in part['criteria']}
    for part in result['parts']:
        for criterion in part['criteria']:
            criterion['suffix']=criterion['criterion_id']
            criterion['criterion_id']=suffix_to_id[criterion['suffix']]
            dependencies=criterion.pop('depends_on')
            criterion['depends_on']=[suffix_to_id[d] for d in dependencies if '|' not in d]
            criterion['depends_on_any']=[[suffix_to_id[alt] for alt in d.split('|')] for d in dependencies if '|' in d]
        part['proposed_marks']=sum(c['marks'] for c in part['criteria'])
        part['semantic_key']=local_key[part['local_part_id']]
    result['proposed_total_marks']=sum(p['proposed_marks'] for p in result['parts'])
    return result
