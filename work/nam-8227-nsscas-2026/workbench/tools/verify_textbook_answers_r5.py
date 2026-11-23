"""Independent source-item answer checks, not a recipe or question generator.
Questions and printed keys are separate author transcriptions from rendered pages.
SymPy derives from the question operands; no printed key enters compute().
"""
import json
from pathlib import Path
import sympy as sp
from functools import lru_cache
from math import gcd,lcm
from decimal import Decimal,localcontext,ROUND_HALF_UP
from analysis_sources import A,WB,ROOT,write,digest,evidence_path
x=sp.Symbol('x',real=True)
def source_limit(function,variable,point,*args,**kwargs):
    # SymPy1.14misdirects some bare a**x limits at negative infinity.
    # a>0 gives the exact real identity a**u=exp(u*ln(a)). Normalise
    # only fixed positive bases with a variable exponent;do not rewrite
    # trigonometric functions into complex exponentials or unknown bases.
    normalised=function.replace(
        lambda term:isinstance(term,sp.Pow)and term.base.is_number and term.base.is_positive is True and term.exp.has(variable),
        lambda term:sp.exp(term.exp*sp.log(term.base)))
    return sp.limit(normalised,variable,point,*args,**kwargs)
LOCALS={**{c:sp.Symbol(c,real=True)for c in ['a','b','c','p','q','k','n','y','t']},'Abs':sp.Abs,'Interval':sp.Interval,'Union':sp.Union,'oo':sp.oo,'Tuple':sp.Tuple,'FiniteSet':sp.FiniteSet,'x':x,'sqrt':sp.sqrt,'pi':sp.pi,'ln':sp.log,'exp':sp.exp}
LOCALS['limit']=source_limit
def expression(s):return sp.sympify(s,locals=LOCALS,rational=True)

def exact_radical_zero(value):
    value=sp.simplify(value)
    if value==0:return True
    value=sp.simplify(sp.expand_trig(value))
    return value==0 or sp.simplify(sp.sqrtdenest(sp.radsimp(value)))==0

@lru_cache(maxsize=None)
def canonical_atan_constant(atom):
    """Recognise a small exact angle only after an exact ratio proof.

    Numeric proximity selects which identity to TRY; it never establishes
    equality. atan's principal interval makes the proved ratio unambiguous.
    Unrecognised algebraic inputs remain exact atan expressions.
    """
    argument=atom.args[0]
    if not argument.is_number or argument.is_real is not True:return atom
    approximate=float(sp.N(atom,30))
    for k in range(-11,12):
        angle=sp.Rational(k,24)*sp.pi
        if abs(approximate-float(sp.N(angle,30)))<1e-12 and exact_radical_zero(argument-sp.tan(angle)):
            return angle
    return atom

def canonical_angle_constants(value):
    return sp.simplify(value.xreplace({a:canonical_atan_constant(a)for a in value.atoms(sp.atan)}))

def trig_residual(left,right):
    residual=left-right
    arguments={atom.args[0]for atom in residual.atoms(sp.sin,sp.cos,sp.tan,sp.sec,sp.csc,sp.cot)}
    if len(arguments)==1:
        argument=next(iter(arguments))
        if argument.is_real is True:
            # Prove same-angle identities without expanding an affine angle
            # into sin(x),cos(x) and transcendental constant coefficients.
            angle=sp.Dummy('common_real_angle',real=True)
            mapped=residual.subs(argument,angle)
            if sp.simplify(sp.trigsimp(mapped,method='fu'))==0:return sp.S.Zero
    # Normalise reciprocal/quotient notation before rational simplification.
    # This avoids treating a simplifier's choice of tan(2x) as a failed proof.
    for fn,replacement in [(sp.tan,lambda t:sp.sin(t)/sp.cos(t)),
        (sp.cot,lambda t:sp.cos(t)/sp.sin(t)),(sp.sec,lambda t:1/sp.cos(t)),
        (sp.csc,lambda t:1/sp.sin(t))]:
        residual=residual.replace(fn,replacement)
    residual=sp.cancel(sp.expand_trig(residual))
    result=sp.simplify(sp.trigsimp(residual,method='fu'))
    if result!=0:
        # A simplifier can leave an exact rational identity unresolved after
        # expanding sin(4x)/cos(4x). Reduce its polynomial numerator by each
        # unit-circle relation; this is exact algebra,not a numerical sample.
        numerator=sp.fraction(residual)[0]
        atoms=numerator.atoms(sp.sin,sp.cos)
        arguments=sorted({atom.args[0]for atom in atoms},key=str)
        if arguments:
            generators=[fn(t)for t in arguments for fn in[sp.sin,sp.cos]]
            relations=[sp.sin(t)**2+sp.cos(t)**2-1 for t in arguments]
            try:
                remainder=sp.reduced(numerator,relations,*generators)[1]
                if remainder==0:return sp.Integer(0)
            except sp.PolynomialError:pass
    return result

def reduce_even_trig_powers(numerator):
    """Use s²+c²=1 to leave one coordinate where parity permits it."""
    atoms=numerator.atoms(sp.sin,sp.cos)
    arguments={a.args[0]for a in atoms}
    argument=next(iter(arguments))if len(arguments)==1 else x
    s,c=sp.sin(argument),sp.cos(argument)
    try:poly=sp.Poly(numerator,s,c)
    except sp.PolynomialError:return numerator
    candidates=[]
    if all(pc%2==0 for(ps,pc),coef in poly.terms()):
        candidates.append(sp.expand(sum(coef*s**ps*(1-s**2)**(pc//2)for(ps,pc),coef in poly.terms())))
    if all(ps%2==0 for(ps,pc),coef in poly.terms()):
        candidates.append(sp.expand(sum(coef*(1-c**2)**(ps//2)*c**pc for(ps,pc),coef in poly.terms())))
    if not candidates:return numerator
    result=min(candidates,key=lambda e:(sp.Poly(e,s,c).total_degree(),sp.count_ops(e),str(e)))
    assert trig_residual(numerator,result)==0
    return result

def solve_trig_numerator(numerator,domain):
    """Solve every factor, including every algebraic ratio branch explicitly.

    Bounded solveset on a quadratic in tan/sec has lost entire branches in
    this corpus. Polynomial roots/multiplicities give a separate completeness
    check before solving each elementary function equation.
    """
    assert numerator!=0,'equation is an identity,not a finite solution set'
    found=[]
    for factor in sp.Mul.make_args(sp.factor(numerator)):
        if not factor.has(x):continue
        atoms=factor.atoms(sp.sin,sp.cos,sp.tan)
        equations=[factor]
        if len(atoms)==2 and {a.func for a in atoms}=={sp.sin,sp.cos}and len({a.args[0]for a in atoms})==1:
            argument=next(iter(atoms)).args[0]
            s,c=sp.Dummy('sine',real=True),sp.Dummy('cosine',real=True)
            replaced=factor.xreplace({sp.sin(argument):s,sp.cos(argument):c})
            if not replaced.has(x):
                poly=sp.Poly(replaced,s,c)
                degree=poly.total_degree()
                if len({sum(m)for m,coefficient in poly.terms()})==1:
                    # Divide a homogeneous polynomial by cos^degree only
                    # on its nonzero-cosine branch. Preserve the excluded
                    # axis separately whenever the sine-leading term is zero.
                    ratio_poly=sp.Poly(poly.as_expr().subs(c,1),s)
                    algebraic=sp.roots(ratio_poly,s)
                    assert sum(algebraic.values())==ratio_poly.degree(),('incomplete homogeneous ratio roots',ratio_poly)
                    equations=[]
                    for ratio in algebraic:
                        if ratio.is_real is False:continue
                        assert ratio.is_real is True
                        equations.append(sp.tan(argument)-ratio)
                    if poly.coeff_monomial(s**degree)==0:
                        equations.append(sp.cos(argument))
                elif poly.total_degree()==1:
                    # Solve a*sin(t)+b*cos(t)+d=0 independently of R-form
                    # construction. u=tan(t/2) gives a quadratic, but its
                    # missing t=pi mod2pi axis MUST be checked separately.
                    a=poly.coeff_monomial(s);b=poly.coeff_monomial(c);d=poly.coeff_monomial(1)
                    u=sp.Dummy('half_angle_tangent',real=True)
                    quadratic=sp.Poly((d-b)*u**2+2*a*u+(b+d),u)
                    algebraic=sp.roots(quadratic,u)
                    assert sum(algebraic.values())==quadratic.degree(),('incomplete half-angle roots',quadratic)
                    equations=[]
                    for ratio in algebraic:
                        if ratio.is_real is False:continue
                        assert ratio.is_real is True
                        equations.append(sp.tan(argument/2)-ratio)
                    if sp.simplify(d-b)==0:
                        equations.append(sp.cos(argument/2))
        if len(atoms)==1:
            atom=next(iter(atoms));t=sp.Dummy('ratio',real=True)
            replaced=factor.xreplace({atom:t})
            if not replaced.has(x):
                poly=sp.Poly(replaced,t)
                algebraic=sp.roots(poly,t)
                assert sum(algebraic.values())==poly.degree(),('incomplete algebraic factor roots',poly)
                equations=[]
                for ratio in algebraic:
                    if ratio.is_real is False:continue
                    assert ratio.is_real is True,('unresolved real ratio',ratio)
                    if atom.func in[sp.sin,sp.cos]and not bool(-1<=ratio<=1):continue
                    equations.append(atom-ratio)
        for equation in equations:
            result=sp.solveset(equation,x,domain=domain)
            assert isinstance(result,sp.FiniteSet)or result is sp.S.EmptySet,('bounded factor not resolved',equation,result)
            found.extend(result)
    return sp.FiniteSet(*found)

def check_proper_integral_domain(f,lo,hi):
    assert lo.is_real and hi.is_real and lo.is_finite and hi.is_finite
    domain=sp.calculus.util.continuous_domain(f,x,sp.S.Reals)
    interval=sp.Interval(sp.Min(lo,hi),sp.Max(lo,hi))
    def contained_in(target):
        direct=interval.is_subset(target)
        if direct is True:return True
        if isinstance(target,sp.Complement):
            # Resolve trigonometric pole ImageSets inside the exact interval,
            # including domains split at a separate rational-function pole.
            return contained_in(target.args[0]) and sp.Intersection(interval,target.args[1]) is sp.S.EmptySet
        if isinstance(target,sp.Union):return any(contained_in(piece)for piece in target.args)
        if isinstance(target,sp.Intersection):return all(contained_in(piece)for piece in target.args)
        return False
    contained=contained_in(domain)
    assert contained is True,('proper integral crosses original discontinuity',f,interval,domain)
    return True

def compute(operation):
    kind=operation['kind'];v=[expression(s)for s in operation['operands']]
    if kind in ['named-point-location','named-point-displacements']:
        from source_vector_geometry_r5 import named_locations,named_displacements
        points={name:[expression(z)for z in coordinates]for name,coordinates in operation['points'].items()}
        return named_locations(points,v[0])if kind=='named-point-location'else named_displacements(points,v[0])
    if kind=='regular-hex-prism-displacement':
        from source_vector_geometry_r5 import regular_hexagon_prism
        points,basis=regular_hexagon_prism()
        result=basis.inv()*(points[operation['head']]-points[operation['tail']])
        return sp.Tuple(*[sp.simplify(z)for z in result])

    if operation.get('conditions'):
        unknowns=[LOCALS[c]for c in operation['unknowns']]
        solutions=sp.solve([expression(c)for c in operation['conditions']],unknowns,dict=True)
        assert len(solutions)==1,('system needs an explicit branch decision',solutions)
        v=[value.subs(solutions[0])for value in v]
    if kind=='identity':return sp.simplify(v[0])
    if kind in ['bracketed-source-root','supplied-source-iteration']:
        from textbook_numerical_roots_r5 import bracketed_root,supplied_iteration
        result=bracketed_root(operation,expression,check_proper_integral_domain)if kind=='bracketed-source-root'else supplied_iteration(operation,expression)
        if 'rounding'in operation:
            return compute({'kind':'rounded','operands':[str(result)],**operation['rounding']})
        return result
    if kind in ['trapezium-rule','numeric-trapezium-rule']:
        f,lo,hi=v;count=operation['strips']
        assert isinstance(count,int) and count>0 and hi>lo
        check_proper_integral_domain(f,lo,hi)
        h=(hi-lo)/count
        if kind=='numeric-trapezium-rule':
            import mpmath as mp
            with mp.workdps(70):
                fn=sp.lambdify(x,f,'mpmath')
                a=mp.mpf(str(sp.N(lo,69)));step=mp.mpf(str(sp.N(h,69)))
                result=sp.Float(str(step*(fn(a)/2+mp.fsum(fn(a+j*step)for j in range(1,count))+fn(a+count*step)/2)),65)
        else:
            result=sp.simplify(h*(f.subs(x,lo)/2+sum(f.subs(x,lo+j*h)for j in range(1,count))+f.subs(x,hi)/2))
        result=result*expression(operation.get('scale','1'))
        if 'rounding'in operation:
            return compute({'kind':'rounded','operands':[str(result)],**operation['rounding']})
        return result
    if kind=='tabulated-trapezium':
        nodes,ordinates=v
        assert len(nodes)==len(ordinates)>=2
        assert all(b>a for a,b in zip(nodes,nodes[1:]))
        return sp.simplify(sum((b-a)*(u+z)/2 for a,b,u,z in zip(nodes,nodes[1:],ordinates,ordinates[1:])))
    if kind=='real-elementary-antiderivative':
        algorithm=operation.get('integration_algorithm','default')
        assert algorithm in ['default','manual'],'unknown source QA integration algorithm'
        coordinate=operation.get('integration_coordinate')
        if coordinate:
            # Author QA only: a declared affine coordinate avoids pathological
            # half-angle CAS forms for shifted secant squares. The original
            # integrand remains the input, and its derivative is checked below.
            scale=expression(coordinate['scale']);offset=expression(coordinate['offset'])
            assert not (scale.free_symbols|offset.free_symbols) and scale.is_real and scale!=0,'integration coordinate needs real constant nonzero scale'
            u=sp.Dummy('integration_coordinate',real=True)
            transformed=sp.simplify(v[0].subs(x,(u-offset)/scale)/scale)
            primitive=sp.integrate(transformed,u).subs(u,scale*x+offset)
        else:
            primitive=sp.integrate(v[0],x,manual=True)if algorithm=='manual'else sp.integrate(v[0],x)
        assert not primitive.has(sp.Integral),'source integral not resolved'
        assert equivalent(sp.diff(primitive,x),v[0]),'primitive derivative disagrees with original integrand'
        # Real logarithmic primitives live on separate components u!=0.
        # d ln|u|/dx=u'/u there. This replacement does not join components
        # or license endpoint subtraction across a denominator zero.
        for atom in primitive.atoms(sp.log):
            assert atom.args[0].is_real is True,('complex logarithm needs separate branch analysis',atom)
        return primitive.replace(sp.log,lambda u:sp.log(sp.Abs(u)))
    if kind=='proper-definite-integral':
        f,lo,hi=v
        check_proper_integral_domain(f,lo,hi)
        result=sp.integrate(f,(x,lo,hi))
        assert not result.has(sp.Integral) and result.is_finite is True,('finite proper integral unresolved',result)
        return sp.simplify(result)
    if kind in ['parametric-derivative','parametric-tangent','parametric-normal','parametric-stationary-points']:
        parameter=LOCALS[operation.get('variable','t')]
        X,Y=v[:2];dx=sp.diff(X,parameter);dy=sp.diff(Y,parameter)
        if kind=='parametric-derivative':
            assert dx!=0,'parametric x derivative is identically zero'
            result=sp.cancel(dy/dx)  # Preserve the original domain separately from cancellation.
            if 'at' in operation:
                point=expression(operation['at'])
                speedx=sp.simplify(dx.subs(parameter,point))
                assert speedx!=0 and speedx.is_finite,'singular parametric derivative needs branch analysis'
                result=sp.simplify(result.subs(parameter,point))
            return result
        if kind=='parametric-stationary-points':
            domain=v[2]if len(v)>2 else sp.S.Reals
            roots=sp.solveset(dy,parameter,domain=domain)
            assert isinstance(roots,sp.FiniteSet)or roots is sp.S.EmptySet,('parametric stationary roots unresolved',roots)
            found=[]
            for root in roots:
                speedx=sp.simplify(dx.subs(parameter,root))
                assert speedx!=0 and speedx.is_finite,('singular parametric stationary candidate needs branch analysis',root,speedx)
                found.append(sp.Tuple(sp.simplify(X.subs(parameter,root)),sp.simplify(Y.subs(parameter,root))))
            return sp.FiniteSet(*found)
        a,b=(dy,-dx)if kind=='parametric-tangent'else(dx,dy)
        result=sp.Tuple(*(sp.simplify(q)for q in[a,b,-a*X-b*Y]))
        if 'at'in operation:result=sp.simplify(result.subs(parameter,expression(operation['at'])))
        assert result[0]!=0 or result[1]!=0,'parametric line has zero normal vector'
        return result
    if kind=='implicit-expression-derivative':
        return sp.simplify(sp.diff(v[0],x)+sp.diff(v[0],LOCALS['y'])*LOCALS['p'])
    if kind=='implicit-horizontal-points':
        function=v[0];y=LOCALS['y']
        conditions=[sp.Q.nonzero(LOCALS[name])for name in operation.get('nonzero_parameters',[])]
        assumptions=sp.And(*conditions)
        solutions=sp.solve([function,sp.diff(function,x)],(x,y),dict=True)
        assert solutions,'implicit horizontal system has no finite explicit candidate set'
        points=[]
        for solution in solutions:
            assert x in solution and y in solution,'implicit horizontal candidate is not isolated'
            values=[sp.simplify(solution[var])for var in[x,y]]
            real=[]
            for value in values:
                if value.is_real is not None:real.append(value.is_real);continue
                imaginary=sp.simplify(sp.im(value))
                if sp.ask(sp.Q.zero(imaginary),assumptions)is True:real.append(True)
                elif sp.ask(sp.Q.nonzero(imaginary),assumptions)is True:real.append(False)
                else:raise AssertionError(('implicit candidate reality unresolved',values))
            if not all(real):continue
            assert sp.simplify(function.subs(solution,simultaneous=True))==0
            fy=sp.simplify(sp.diff(function,y).subs(solution,simultaneous=True))
            assert sp.ask(sp.Q.nonzero(fy),assumptions)is True,('singular implicit candidate needs branch analysis',values,fy)
            points.append(sp.Tuple(*values))
        return sp.FiniteSet(*points)
    if kind=='implicit-derivative':
        fy=sp.diff(v[0],LOCALS['y']);assert fy!=0,'implicit derivative has no y dependence'
        return sp.simplify(-sp.diff(v[0],x)/fy)
    if kind=='trig-expand':return sp.expand_trig(v[0])
    if kind=='r-form-coefficients':
        from textbook_rform_checks_r5 import coefficients
        result=coefficients(operation,expression)
        if operation.get('phase_decimal_places')is not None:
            phase=compute({'kind':'rounded','operands':[str(result[1])],'decimal_places':operation['phase_decimal_places']})
            return sp.Tuple(result[0],phase)
        return result
    if kind=='trig-identity-residual':return trig_residual(v[0],v[1])
    if kind=='trig-compound-expand':
        a,b=v
        family=operation['family']
        if family=='sin':result=sp.sin(a)*sp.cos(b)+sp.cos(a)*sp.sin(b)
        elif family=='cos':result=sp.cos(a)*sp.cos(b)-sp.sin(a)*sp.sin(b)
        else:
            assert family=='tan'
            result=(sp.tan(a)+sp.tan(b))/(1-sp.tan(a)*sp.tan(b))
        original={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}[family](a+b)
        assert trig_residual(original,result)==0
        # Fully evaluate constant multiple angles, e.g. tan(2 atan(4/3)),
        # while keeping an unknown source argument such as cos(2x) intact.
        return sp.simplify(sp.expand_trig(result))if not result.free_symbols else result
    if kind=='sine-square-form-coefficients':
        a=sp.simplify(v[0].subs(x,0));b=sp.simplify(a-v[0].subs(x,sp.pi/2))
        assert trig_residual(v[0],a-b*sp.sin(x)**2)==0
        return sp.Tuple(a,b)
    if kind=='inverse-principal-affine-trig':
        from textbook_inverse_checks_r5 import inverse_features
        return inverse_features(operation,expression,x)
    if kind=='first-turning-point-right':
        points=sp.solveset(sp.diff(v[0],x),x,domain=sp.Interval.open(v[1],v[2]))
        assert isinstance(points,sp.FiniteSet)and len(points)>0
        first=min(points,key=lambda p:float(sp.N(p,40)))
        assert sp.simplify(sp.diff(v[0],x,2).subs(x,first))!=0
        return first
    if kind in['coordinate-trig-ratios','acute-given-trig-ratio','numeric-given-trig-ratio','quadrant-given-symbolic-ratio','independent-ratio-sum']:
        from textbook_ratio_checks_r5 import check
        return check(operation,expression,x)
    if kind=='trig-features':
        from textbook_trig_checks_r5 import features
        return features(operation,expression)
    if kind=='angle-features':
        original=v[0];turn=sp.Integer(360)if operation['angle_unit']=='degree'else 2*sp.pi
        angle=sp.Mod(original,turn);quarter=turn/4
        quadrant=0 if angle in[0,quarter,2*quarter,3*quarter]else int(sp.floor(angle/quarter))+1
        reference=sp.simplify(min([angle,abs(angle-turn/2),turn-angle],key=lambda p:float(sp.N(p,40))))
        scale=sp.pi/180 if operation['angle_unit']=='degree'else sp.Integer(1)
        return {'original_angle':original,'coterminal_angle':angle,'quadrant':sp.Integer(quadrant),'reference_angle':reference,
          'rotation_sign':sp.sign(original),'complete_turns':sp.floor(abs(original)/turn),
          'terminal_unit_vector':sp.Tuple(sp.cos(original*scale),sp.sin(original*scale))}
    if kind=='reference-angle-solutions':
        beta,quadrant,lo,hi=v;turn=sp.Integer(360)if operation['angle_unit']=='degree'else 2*sp.pi
        assert 0<beta<turn/4 and quadrant in[1,2,3,4]
        base={1:beta,2:turn/2-beta,3:turn/2+beta,4:turn-beta}[int(quadrant)]
        found=[]
        for k in range(int(sp.floor((lo-base)/turn))-1,int(sp.ceiling((hi-base)/turn))+2):
            candidate=sp.simplify(base+k*turn)
            left=candidate>lo if operation.get('left_open',True)else candidate>=lo
            right=candidate<hi if operation.get('right_open',True)else candidate<=hi
            if bool(left)and bool(right):found.append(candidate)
        return sp.FiniteSet(*found)
    if kind=='same-function-reduction':
        theta=v[0];unit=operation['angle_unit'];family=operation['family']
        feature=compute({'kind':'angle-features','angle_unit':unit,'operands':[str(theta)]})
        q=int(feature['quadrant']);beta=feature['reference_angle'];assert q in[1,2,3,4]
        sign=1 if q in({'sin':[1,2],'cos':[1,4],'tan':[1,3]}[family])else-1
        scale=sp.pi/180 if unit=='degree'else sp.Integer(1);fn={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}[family]
        assert sp.trigsimp(fn(theta*scale)-sign*fn(beta*scale))==0
        return sp.Tuple(sign,beta)
    if kind=='trig-given-ratio':
        fn={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}[operation['given_family']]
        result=sp.trigsimp(v[0]).subs(fn(x),v[1])
        assert not result.has(x),('ratio does not determine requested result without further evidence',operation,result)
        return sp.simplify(result)
    if kind=='cos-input-multipliers':
        turn=2*sp.pi if operation['angle_unit']=='radian'else sp.Integer(360)
        magnitude=sp.simplify(turn/v[0])
        return sp.FiniteSet(-magnitude,magnitude)
    if kind=='line-from-relation':
        solutions=sp.solve(v[0],LOCALS['y']);assert len(solutions)==1
        line=solutions[0];assert sp.diff(line,x,2)==0
        return sp.Tuple(sp.diff(line,x),line.subs(x,0))
    if kind=='bounded-trig-equation':
        trig_atoms=v[0].atoms(sp.sin,sp.cos,sp.tan,sp.sec,sp.csc,sp.cot)
        if trig_atoms:
            argument=next(iter(trig_atoms)).args[0]
            if argument!=x and all(atom.args[0]==argument for atom in trig_atoms):
                a=sp.diff(argument,x);b=argument.subs(x,0)
                only_trig=v[0].xreplace({atom:sp.Dummy()for atom in trig_atoms})
                if not only_trig.has(x)and not a.has(x)and bool(a>0):
                    # An invertible change of angle avoids expensive shifted
                    # exponential solving. Transform the full interval too.
                    replacements={atom:atom.func(x)for atom in trig_atoms}
                    normalised=v[0].xreplace(replacements)
                    inner={**operation,'operands':[str(normalised),str(a*v[1]+b),str(a*v[2]+b)]}
                    result=compute(inner)
                    return sp.FiniteSet(*(sp.simplify((root-b)/a)for root in result))
            variable_atoms=[atom for atom in trig_atoms if atom.has(x)]
            slopes=[sp.diff(atom.args[0],x)for atom in variable_atoms]
            outside=v[0].xreplace({atom:sp.Dummy()for atom in trig_atoms})
            if slopes and not outside.has(x)and all(a.is_number and a.is_real is True and a!=0 for a in slopes):
                pieces=[a.as_coeff_Mul()for a in slopes]
                bases={base for coefficient,base in pieces}
                if len(bases)==1 and all(coefficient.is_Rational for coefficient,base in pieces):
                    basis=next(iter(bases))
                    unit=basis*sp.Rational(gcd(*(abs(int(coefficient.p))for coefficient,base in pieces)),
                      lcm(*(int(coefficient.q)for coefficient,base in pieces)))
                    if unit!=1 and unit.is_positive is True:
                        # Degree arguments such as pi*x/90 and pi*x/180
                        # must become 2u and u BEFORE multiple-angle expansion.
                        # Exact rescaling preserves the whole original domain.
                        inner={**operation,'operands':[str(v[0].subs(x,x/unit)),str(unit*v[1]),str(unit*v[2])]}
                        result=compute(inner)
                        return sp.FiniteSet(*(sp.simplify(root/unit)for root in result))
        # Avoid the bounded inverse-sec/cosec intersection path: it can discard
        # valid roots. Solve the equivalent sine/cosine numerator, then check
        # candidates against the ORIGINAL equation and denominator.
        rewritten=v[0]
        families={atom.func for atom in trig_atoms}
        if families and families<={sp.tan,sp.sec}:
            # An even secant polynomial can stay in tangent. Otherwise a CAS
            # may return opaque half-angle roots whose substitution it cannot
            # simplify back to zero. This is the standard exact identity,
            # with the ORIGINAL secant/tangent pole checks retained below.
            candidate=rewritten.subs(sp.sec(x)**2,1+sp.tan(x)**2)
            if not candidate.has(sp.sec):
                assert trig_residual(rewritten,candidate)==0
                rewritten=candidate
        replacements=[(sp.sec,lambda t:1/sp.cos(t)),(sp.csc,lambda t:1/sp.sin(t)),(sp.cot,lambda t:sp.cos(t)/sp.sin(t))]
        # A pure polynomial/rational expression in tangent is already in one
        # function. Preserve it rather than introducing unnecessary sin/cos.
        if rewritten.has(sp.sin,sp.cos,sp.sec,sp.csc,sp.cot)or len({atom.args[0]for atom in rewritten.atoms(sp.tan)})>1:
            replacements.append((sp.tan,lambda t:sp.sin(t)/sp.cos(t)))
        for fn,replacement in replacements:
            rewritten=rewritten.replace(fn,replacement)
        numerator,denominator=sp.together(rewritten).as_numer_denom()
        if any(atom.args[0]!=x for atom in numerator.atoms(sp.sin,sp.cos)):
            numerator=sp.expand_trig(numerator)
        numerator=reduce_even_trig_powers(numerator)
        result=solve_trig_numerator(numerator,sp.Interval(v[1],v[2],left_open=operation.get('left_open',False),right_open=operation.get('right_open',False)))
        assert isinstance(result,sp.FiniteSet)or result is sp.S.EmptySet,('bounded equation not independently resolved',result)
        valid=[]
        for root in result:
            root=canonical_angle_constants(root)
            poles=[sp.cos(atom.args[0]) for atom in v[0].atoms(sp.tan,sp.sec)]
            poles += [sp.sin(atom.args[0]) for atom in v[0].atoms(sp.cot,sp.csc)]
            if any(sp.simplify(pole.subs(x,root))==0 for pole in poles):continue
            if sp.simplify(denominator.subs(x,root))==0:continue
            original=sp.simplify(v[0].subs(x,root))
            if original.has(sp.zoo,sp.nan,sp.oo,-sp.oo):continue
            assert exact_radical_zero(original),('candidate does not satisfy original equation',operation,root,original)
            valid.append(root)
        return sp.FiniteSet(*valid)
    if kind=='polynomial-roots-in-interval':
        result=sp.solveset(v[0],x,domain=sp.Interval(v[1],v[2]))
        assert isinstance(result,sp.FiniteSet)or result is sp.S.EmptySet
        return result
    if kind=='sin-parameter-sign-pairs':
        highest,lowest,observed_period,initial_slope_sign=v
        turn=2*sp.pi if operation['angle_unit']=='radian'else sp.Integer(360)
        amplitude=(highest-lowest)/2;offset=(highest+lowest)/2;frequency=turn/observed_period
        assert amplitude>0 and observed_period>0 and initial_slope_sign in[-1,1]
        return sp.FiniteSet(*(sp.Tuple(sa*amplitude,sb*frequency,offset)for sa in[-1,1]for sb in[-1,1]if sa*sb==initial_slope_sign))
    if kind=='trig-line-root-count':
        a,b,c,m,d,lo,hi=v
        from textbook_trig_checks_r5 import features
        derivative={'kind':'trig-features','family':'cos','angle_unit':'radian','operands':[str(a*b),str(b),str(-m),str(lo),str(hi)]}
        critical=features(derivative,expression)['window_zero_locations']
        boundaries=sorted({lo,hi,*critical},key=lambda p:float(sp.N(p,50)))
        residuals=[sp.simplify(a*sp.sin(b*p)+c-m*p-d)for p in boundaries]
        def sign(v):return 0 if v==0 else 1 if sp.N(v,70)>0 else-1
        signs=[sign(value)for value in residuals]
        # Between consecutive derivative zeros the residual is strictly monotone,
        # so each sign change gives exactly one crossing. Count endpoint roots once.
        return sp.Integer(signs.count(0)+sum(left*right<0 for left,right in zip(signs,signs[1:])))
    if kind=='decimal-prefix':
        from decimal import ROUND_DOWN
        with localcontext()as ctx:
            ctx.prec=70
            number=Decimal(str(sp.N(v[0],65)))
            unit=Decimal(1).scaleb(-operation['decimal_places'])
            return sp.Rational(str(number.quantize(unit,rounding=ROUND_DOWN)))
    if kind=='rounded':
        # Keep source decimal-place/significant-figure requirements explicit.
        # The reference expression comes only from the question values.
        with localcontext()as ctx:
            ctx.prec=70
            number=Decimal(str(sp.N(v[0],65)))
            places=operation.get('decimal_places')
            if places is None:
                assert operation.get('significant_figures')and number!=0
                places=operation['significant_figures']-1-number.adjusted()
            return sp.Rational(str(number.quantize(Decimal(1).scaleb(-places),rounding=ROUND_HALF_UP)))
    if kind=='evaluate-list':return sp.Tuple(*(v[0].subs(x,expression(value))for value in operation['at']))
    if kind=='factor':return sp.factor(v[0])
    if kind=='real-roots':return sp.solveset(v[0],x,domain=sp.S.Reals)
    if kind=='real-function-domain':return sp.calculus.util.continuous_domain(v[0],x,sp.S.Reals)
    if kind=='real-image-range':return sp.calculus.util.function_range(v[0],LOCALS[operation.get('variable','x')],v[1])
    if kind=='stationary-points':
        function=v[0]
        domain=sp.calculus.util.continuous_domain(function,x,sp.S.Reals)
        if len(v)>1:domain=sp.Intersection(domain,v[1])
        derivative=sp.diff(function,x)
        roots=sp.solveset(derivative,x,domain=domain)
        assert isinstance(roots,sp.FiniteSet)or roots is sp.S.EmptySet,('stationary points need an explicit finite source solution',roots)
        points=[]
        for root in roots:
            ordinate=sp.simplify(function.subs(x,root))
            assert ordinate.is_finite and sp.simplify(derivative.subs(x,root))==0
            points.append(sp.Tuple(root,ordinate))
        return sp.FiniteSet(*points)
    if kind=='integer-root-candidates':return sp.FiniteSet(*(sign*d for d in sp.divisors(abs(v[0].subs(x,0)))for sign in [-1,1]))
    if kind=='integer-roots-except':return sp.FiniteSet(*(r for r in sp.polys.polytools.ground_roots(v[0],x)if r.is_integer and r not in [expression(a)for a in operation['except']]))
    if kind=='quadratic-maximum':
        vertex=sp.solve(sp.diff(v[0],x),x);assert len(vertex)==1 and sp.diff(v[0],x,2)<0
        return v[0].subs(x,vertex[0])
    if kind=='inequality':
        relation=v[0];replacements={}
        for name in operation.get('parameters_positive',[]):
            positive=sp.Symbol('positive_'+name,positive=True)
            relation=relation.subs(LOCALS[name],positive);replacements[positive]=LOCALS[name]
        return sp.solve_univariate_inequality(relation,x,relational=False).xreplace(replacements)
    if kind=='modulus-sketch':
        a,b,c=v;vertex=-b/a
        roots=sp.FiniteSet()if c>0 else sp.FiniteSet((-b-c)/a,(-b+c)/a)
        return {'vertex':sp.Tuple(vertex,c),'y_intercept':sp.Abs(b)+c,'x_intercepts':roots,'left_slope':-sp.Abs(a),'right_slope':sp.Abs(a)}
    if kind=='degree':return sp.degree(v[0],x)
    if kind=='expand':return sp.expand(v[0])
    if kind=='quotient':return sp.div(v[0],v[1],x)[0]
    if kind=='factor-quotient':return sp.factor(sp.div(v[0],v[1],x)[0])
    if kind=='remainder':return sp.div(v[0],v[1],x)[1]
    if kind=='polynomial-sketch':
        poly=v[0];roots=sp.roots(poly,x)
        return {'real_roots_with_multiplicities':{str(r):m for r,m in roots.items()if r.is_real},'y_intercept':str(poly.subs(x,0)),
          'degree':int(sp.degree(poly,x)),'leading_coefficient':str(sp.LC(sp.Poly(poly,x))),
          'real_stationary_point_count':int(sp.Poly(sp.diff(poly,x),x).count_roots(-sp.oo,sp.oo))}
    if kind=='affine-sketch':
        a,b=v
        return {'y_intercept':b,'x_intercepts':sp.FiniteSet(-b/a),'slope':a}
    if kind=='cube-pair-list':
        total=int(v[0]);pairs=[(a,b)for a in range(1,13)for b in range(a,13)if a**3+b**3==total]
        return sp.Tuple(*(sp.Tuple(a,b)for a,b in pairs))
    if kind=='cube-pairs':
        total=int(v[0]);pairs=[(a,b)for a in range(1,13)for b in range(a,13)if a**3+b**3==total]
        assert pairs==[(1,12),(9,10)]
        return sp.Integer(total)
    raise AssertionError(('unsupported source-check operation',kind))

def equivalent(a,b):
    if a is None or b is None:return a is b
    if a is sp.nan or b is sp.nan:return False
    if a==b:return True  # In particular, equal one-sided infinities must not be subtracted.
    if isinstance(a,sp.Tuple)and isinstance(b,sp.Tuple):return len(a)==len(b)and all(equivalent(x,y)for x,y in zip(a,b))
    if isinstance(a,sp.Set)and isinstance(b,sp.Set):return a==b
    difference=sp.simplify(a-b)
    if difference==0:return True
    # SymPy may rewrite an exponential quotient derivative into hyperbolic
    # functions. Rewrite those exact functions back to exponentials before
    # rational cancellation; no numeric tolerance or forced power law is used.
    if difference.has(sp.sinh,sp.cosh,sp.tanh,sp.coth,sp.sech,sp.csch):
        if sp.cancel(sp.together(difference.rewrite(sp.exp)))==0:return True
    if difference.has(sp.sin,sp.cos,sp.tan,sp.sec,sp.csc,sp.cot):return trig_residual(a,b)==0
    return False

def component_primitive_derivative(primitive):
    """Differentiate ln|u| on each real component u != 0.

    SymPy retains a spurious zero-case Piecewise when differentiating Abs.
    Here d(ln|u|)/dx = u'/u; the log is undefined at u=0. This local
    derivative identity neither joins those components nor validates a
    definite integral across a pole. Other absolute values are unchanged.
    """
    replacements={}
    for atom in primitive.atoms(sp.log):
        argument=atom.args[0]
        if argument.func is sp.Abs:
            inner=argument.args[0]
            assert inner.is_real is True,'absolute-log primitive needs real component analysis'
            replacements[atom]=sp.log(inner)
    return sp.diff(primitive.xreplace(replacements),x)

def primitive_agrees(operation,derived,printed):
    """Compare primitives through their derivatives, on recorded real components.

    The original integrand alone produces derived. A separately transcribed
    source primitive is then checked; its arbitrary additive constant need not
    equal the CAS choice. This policy never applies to a definite integral.
    """
    assert operation['kind']=='real-elementary-antiderivative','primitive comparison requires an indefinite integral'
    assert not derived.has(sp.Piecewise)and not printed.has(sp.Piecewise),'primitive branch needs component analysis'
    integrand=expression(operation['operands'][0])
    assert equivalent(component_primitive_derivative(derived),integrand),'derived primitive derivative disagrees with original integrand'
    return equivalent(component_primitive_derivative(printed),integrand)

def build():
    entries=[]
    for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
        data=json.loads(path.read_text())
        for item in data['items']:
            for part in item['subparts']:
                assert part['method'] and part['source_evidence']and part['key_evidence']
                for evidence in [part['source_evidence'],part['key_evidence']]:
                    assert digest(evidence_path(evidence['path']))==evidence['sha256']
                if part.get('verification_mode')=='manual-derivation':
                    assert part['author_derivation']and part['author_conclusion']
                    row={**part,'item_id':item['item_id'],'status':part['author_comparison_status'],
                      'derived_answer':part['author_conclusion'],'computation':'Author logical derivation; no mechanical proof claimed',
                      'source_input_path':str(path.relative_to(ROOT)),'source_input_sha256':digest(path),
                      'date':part.get('review_date','2026-11-17'),'reviewer':'Codex author','independent_review':'pending'}
                    if part.get('additional_operations'):
                        row['additional_derived_results']={name:str(compute(op))for name,op in part['additional_operations'].items()}
                        for name,expected in part.get('additional_operation_expected',{}).items():
                            assert name in part['additional_operations']
                            assert equivalent(compute(part['additional_operations'][name]),expression(expected)),('author manual derivation contradicts computed supporting result',item['item_id'],part['subpart'],name)
                        if part.get('additional_operation_expected'):row['supporting_result_assertions_passed']=True
                    entries.append(row)
                    continue
                got=compute(part['operation'])
                if part.get('original_equation_residual'):
                    assert isinstance(got,sp.Set),('original-equation check needs a solution set',item['item_id'])
                    residual=expression(part['original_equation_residual'])
                    assert all(sp.simplify(residual.subs(x,root))==0 for root in got),('root fails original inverse equation',item['item_id'],part['subpart'])
                if part.get('proof_expressions'):
                    chain=[expression(e)for e in part['proof_expressions']]
                    assert part.get('original_common_domain'),('proof has no domain',item['item_id'],part['subpart'])
                    assert all(trig_residual(a,b)==0 for a,b in zip(chain,chain[1:])),('invalid author proof step',item['item_id'],part['subpart'])
                    if part.get('proof_correction'):
                        assert got!=0 and sp.trigsimp(chain[-1]-expression(part['proof_correction']['correct_rhs']))==0
                    else:
                        assert sp.trigsimp(chain[0]-expression(part['operation']['operands'][0]))==0
                        assert sp.trigsimp(chain[-1]-expression(part['operation']['operands'][1]))==0
                for assertion in part.get('assertions',[]):assert equivalent(expression(assertion['expression']),expression(assertion['expected'])),('source assertion false',item['item_id'],part['subpart'])
                if part.get('candidate_check_values'):
                    poly=expression(part['candidate_polynomial'])
                    assert all(poly.subs(x,expression(point))==value for point,value in part['candidate_check_values'].items())
                solution_comparison=None
                if 'printed_key_approximate_values' in part:
                    assert isinstance(got,sp.FiniteSet)or got is sp.S.EmptySet
                    roots=sorted(got,key=lambda z:float(sp.N(z,40)))
                    printed=sorted(part['printed_key_approximate_values'],key=Decimal)
                    comparisons=[];used=set()
                    for key in printed:
                        text=Decimal(key)
                        places=part.get('key_decimal_places')
                        unit=Decimal(10)**(-places)if places is not None else Decimal(10)**text.as_tuple().exponent
                        candidates=[i for i,root in enumerate(roots)if i not in used and abs(Decimal(str(sp.N(root,60)))-text)<=unit/2]
                        matched=len(candidates)==1
                        index=candidates[0]if matched else None
                        if matched:used.add(index)
                        comparisons.append({'derived_exact':str(roots[index])if matched else None,
                          'derived_numeric':str(sp.N(roots[index],60))if matched else None,
                          'printed':key,'last_place_half_unit':str(unit/2),'agrees':matched,
                          'candidate_count_at_written_precision':len(candidates)})
                    same=len(roots)==len(printed)and all(c['agrees']for c in comparisons)
                    solution_comparison={'derived_root_count':len(roots),'printed_root_count':len(printed),'values':comparisons,
                      'missing_exact_roots':[str(root)for i,root in enumerate(roots)if i not in used],
                      'all_printed_values_match':all(c['agrees']for c in comparisons),
                      'basis':'The original equation and interval independently determine all exact roots. Only afterwards are separately transcribed approximations matched one-to-one at their written last place. A missing middle root does not shift the comparison onto a different printed value. Higher precision than a convention is not treated as mathematically wrong.'}
                elif part['operation']['kind']in ['modulus-sketch','affine-sketch','trig-features','angle-features']:
                    if part.get('key_presence')=='no separate key':
                        assert part.get('author_feature_derivation')and not part.get('printed_key_features')
                        feature_checks=[];same=True
                    else:
                        feature_checks=[{'feature':name,'valid':equivalent(got[name],expression(value)if value is not None else None),'derived':str(got[name]),'printed':value}for name,value in part['printed_key_features'].items()]
                        same=all(c['valid']for c in feature_checks)
                elif part['operation']['kind']=='polynomial-sketch':
                    poly=expression(part['operation']['operands'][0]);feature_checks=[{'printed_root_label':label,'substitution_result':str(poly.subs(x,expression(label))),'valid':poly.subs(x,expression(label))==0}for label in part['printed_key_features']['labelled_x_intercepts']]
                    same=all(c['valid']for c in feature_checks)
                else:
                    expected=expression(part.get('printed_key_normalised',part.get('author_check_target_normalised')))
                    same=primitive_agrees(part['operation'],got,expected)if part.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected)
                approximation_check=None
                if part.get('printed_approximation_check'):
                    policy=part['printed_approximation_check']
                    assert policy['source_claim'] and policy['required_rounding'] is None
                    tolerance=expression(policy['absolute_error_strictly_below'])
                    assert tolerance>0
                    difference=abs(sp.N(got-expected,60))
                    same=bool(difference<tolerance)
                    approximation_check={**policy,'absolute_error':str(difference),'agrees':same,
                        'limit':'An explicit author interpretation of an approximate display with no requested decimal-place count; not a claim the source rounds to nearest at its displayed last digit.'}
                extra_comparisons=[]
                for comparison in part.get('additional_comparisons',[]):
                    derived=compute(comparison['operation'])
                    agrees=equivalent(derived,expression(comparison['printed_key_normalised']))
                    extra_comparisons.append({**comparison,'derived_answer':str(derived),'agrees':agrees})
                    same=same and agrees
                unit_comparison=None
                if 'printed_key_units'in part:
                    assert part.get('units')
                    unit_comparison={'required':part['units'],'printed':part['printed_key_units'],'agrees':part['units']==part['printed_key_units']}
                    same=same and unit_comparison['agrees']
                formula_comparison=None
                if part.get('printed_key_formula_normalised'):
                    actual=expression(part['question_formula_normalised']);printed=expression(part['printed_key_formula_normalised'])
                    agrees=equivalent(actual,printed)
                    formula_comparison={'question':part['question_formula_normalised'],'printed_label':part['printed_key_formula_normalised'],'difference':str(sp.simplify(actual-printed)),'agrees':agrees}
                    same=same and agrees
                form_comparison=None
                if part.get('response_form_check'):
                    form=part['response_form_check'];assert form['required_family']==part['operation']['family']
                    agrees=form['printed_family']==form['required_family']and form['acute_angle_unit']==part['operation']['angle_unit']
                    form_comparison={**form,'agrees':agrees};same=same and agrees
                row={k:v for k,v in part.items()if k!='operation'}
                row.update(item_id=item['item_id'],status=('sketch'if part['operation']['kind']in ['polynomial-sketch','modulus-sketch','affine-sketch']else part.get('check_mode','matches'))if same else'key wrong',derived_answer=str(got),
                    derivation_inputs=part['operation'],computation='Independent symbolic/numerical computation from question operands; printed key is not a computation input',
                    source_input_path=str(path.relative_to(ROOT)),source_input_sha256=digest(path),date=part.get('review_date','2026-11-17'),reviewer='Codex author',independent_review='pending')
                if part['operation']['kind']in ['polynomial-sketch','modulus-sketch','affine-sketch','trig-features','angle-features']:row['feature_checks']=feature_checks;row['working']={k:str(v)for k,v in got.items()}
                if isinstance(got,sp.FiniteSet):row['number_of_reported_solutions']=len(got)
                if part.get('additional_operations'):
                    row['additional_derived_results']={name:str(compute(operation))for name,operation in part['additional_operations'].items()}
                    for name,expected_extra in part.get('additional_operation_expected',{}).items():
                        assert name in part['additional_operations']
                        assert equivalent(compute(part['additional_operations'][name]),expression(expected_extra)),('author supporting result contradicts recomputation',item['item_id'],part['subpart'],name)
                    if part.get('additional_operation_expected'):row['supporting_result_assertions_passed']=True
                if extra_comparisons:row['additional_comparison_results']=extra_comparisons
                if approximation_check:row['printed_approximation_comparison']=approximation_check
                if unit_comparison:row['unit_comparison']=unit_comparison
                if formula_comparison:row['formula_comparison']=formula_comparison
                if form_comparison:row['response_form_comparison']=form_comparison
                if solution_comparison:row['solution_key_comparison']=solution_comparison
                if not same and part.get('difference_disposition'):
                    assert part['difference_disposition']=='key incomplete'and part['difference_reason']
                    if 'printed_key_approximate_values'in part:
                        assert solution_comparison['all_printed_values_match']and len(printed)<len(roots),('claimed approximate key is not a proper subset',item['item_id'],part['subpart'])
                        missing=solution_comparison['missing_exact_roots']
                    else:
                        assert isinstance(got,sp.Set)and isinstance(expected,sp.Set)and expected<got,('claimed missing alternative is not a proper key subset',item['item_id'],part['subpart'])
                        missing=str(got-expected)
                    row['status']='key incomplete';row['missing_from_printed_key']=missing
                if part.get('printed_precision_requirement'):
                    precision=part['printed_precision_requirement']
                    assert part['operation']['kind']=='r-form-coefficients'
                    assert precision['requested_decimal_places']==part['operation']['phase_decimal_places']>precision['printed_decimal_places']
                    exact_phase=compute(part['additional_operations']['unrounded_canonical_parameters'])
                    printed_accuracy=sp.Tuple(exact_phase[0],compute({'kind':'rounded','operands':[str(exact_phase[1])],'decimal_places':precision['printed_decimal_places']}))
                    assert equivalent(printed_accuracy,expected),('source precision defect also has a numerical discrepancy',item['item_id'],part['subpart'])
                    row['status']='key incomplete'
                    row['precision_comparison']={**precision,'derived_at_requested_precision':str(got),'derived_at_printed_precision':str(printed_accuracy)}
                if part.get('author_source_working_comparison'):
                    reading=part['author_source_working_comparison']
                    assert reading['status']in['key wrong','key incomplete']and reading['reason']and reading['observed_step']and reading['correct_step']
                    assert same,('source-working-only caveat also has a wrong final value',item['item_id'],part['subpart'])
                    row['status']=reading['status']
                    row['comparison_limit']='Final answer checked symbolically; the additional domain/working limitation is an explicit author reading of the cited source render with a mathematical counterexample.'
                if part.get('author_source_graph_comparison'):
                    reading=part['author_source_graph_comparison']
                    assert reading['status']in['key wrong','key incomplete']and reading['reason']and reading['observed_features']
                    row['status']=reading['status']
                    row['comparison_limit']='Numerical/analytic features are executable; this additional source-render boundary assessment is an explicitly labelled author reading,not a pixel-comparison result.'
                if part['operation']['kind']in ['quotient','remainder','factor-quotient']:
                    a,b=map(expression,part['operation']['operands']);q,r=sp.div(a,b,x)
                    assert sp.expand(a-b*q-r)==0 and (r==0 or sp.degree(r,x)<sp.degree(b,x))
                    row['working']={'identity':f'{a} = ({b})*({q})+({r})','remainder_degree_check':True}
                entries.append(row)
    write(A/'textbook-answer-verification-r5.json',{'status':'working population; only listed subparts verified, not textbook completion','verified_subparts':len(entries),'manual_derivation_subparts':sum(r.get('verification_mode')=='manual-derivation'for r in entries),
        'items_with_any_verified_subpart':len({r['item_id']for r in entries}),'status_counts':dict(__import__('collections').Counter(r['status']for r in entries)),
        'method':'Exact question operands and printed keys separately transcribed from cited rendered pages. Key text is not an input to compute(). Every remaining subpart stays open.','subparts':entries})
    print(len(entries),'subparts;',len({r['item_id']for r in entries}),'items;',dict(__import__('collections').Counter(r['status']for r in entries)))
if __name__=='__main__':build()
