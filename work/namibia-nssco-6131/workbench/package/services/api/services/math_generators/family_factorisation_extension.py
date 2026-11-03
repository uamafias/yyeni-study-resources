"""Explicit missing NSSCO 6131 factorisation forms (syllabus printed p.18).

Each setting guarantees its facet; coverage never depends on a lucky draw.
These are original parameterised questions, not copied past-paper items.
"""
from math import gcd
from .base import MathGenerator, GeneratedProblem, Step, Distractor, GeneratorError
from .algebra_content import _sum, _term, _power
from .formatting import quadratic_latex, factors_latex
from .factorisation_forms import perfect_square_form, grouping_form, factor_product, outside_product


class FactorisationExtensionGenerator(MathGenerator):
    generator_id='nssco_factorisation_extension'
    version=2
    quadratic_dependency_version=2
    levels=(1,2,3,4,5,6)
    level_skills={1:('perfect_square_positive',),2:('perfect_square_negative',),
        3:('common_factor_quadratic',),4:('group_four_variables',),5:('common_multivariable',),6:('negative_leading_quadratic',)}
    error_notes={}

    def _build(self,rng,seed,level):
        r,s=rng.choice([(r,s) for r in range(1,8) for s in range(1,8) if gcd(r,s)==1])
        if level in (1,2):
            sign=1 if level==1 else -1
            x,y=rng.choice([('x','y'),('a','b'),('m','n'),('p','q')])
            expression,answer,_=perfect_square_form(r,s,x,y,sign)
            machine=dict(task=self.level_skills[level][0],r=r,s=s,sign=sign,letters=[x,y])
            distractor=f'({_sum((r,x),(-sign*s,y))})^2'
        elif level in (3,6):
            g=rng.randint(2,9) if level==3 else -rng.randint(1,6)
            # Reuse the vetted quadratic generator; only the outside factor is new.
            from .factorising_quadratics import FactorisingQuadraticsGenerator
            generator=FactorisingQuadraticsGenerator()
            if generator.version!=self.quadratic_dependency_version:
                raise GeneratorError('Quadratic dependency changed; review and version the extension before generating new questions.')
            base_level=rng.choice((1,2,3))
            for _ in range(1000):
                base=generator.generate(rng.randint(0,2**31-1),base_level)
                aa,bb,cc=base.machine['quadratic']
                if max(abs(pair[1]) for pair in base.machine['factors'])<=7 and abs(g*cc)<=150 and abs(g*bb)<=120:
                    break
            else:raise GeneratorError('No quadratic within the authored coefficient limits.')
            a,b,c=base.machine['quadratic'];(m,p),(n,q)=base.machine['factors']
            expression=quadratic_latex(g*a,g*b,g*c)
            inner=factor_product([(m,p),(n,q)]);answer=outside_product(g,inner)
            machine=dict(task='common_factor_quadratic' if level==3 else 'negative_leading_quadratic',g=g,quadratic=[a,b,c],factors=[[m,p],[n,q]],shape='monic' if a==1 else 'non_monic')
            distractor=inner
        elif level==4:
            k=rng.randint(2,12)
            a,b,x,y=rng.choice([('a','b','x','y'),('p','q','m','n'),('u','v','s','t')])
            expression,answer,_=grouping_form(r,s,k,(a,b,x,y))
            machine=dict(task='group_four_variables',r=r,s=s,k=k,letters=[a,b,x,y])
            distractor=f'({_sum((r,a),(s,b))})({x}-{k}{y})'
        else:
            g=rng.randint(1,7);power=rng.randint(1,2);sign=rng.choice([-1,1])
            u,v,w=rng.choice([('a','b','c'),('x','y','z'),('p','q','r')])
            common=_power(u,power)
            expression=_sum((g*r,common+v),(sign*g*s,common+w))
            answer=_term(g,common)+f'({_sum((r,v),(sign*s,w))})'
            machine=dict(task='common_multivariable',g=g,r=r,s=s,sign=sign,power=power,letters=[u,v,w])
            distractor=_term(g,common)+f'({_sum((r,v),(-sign*s,w))})'
        machine['expression']=expression
        if level in (1,2):
            code,description='middle_sign','Used the opposite sign in the squared bracket, changing the middle term.'
        elif level in (3,6):
            code,description='outside_factor_lost','Factorised the inner quadratic but omitted its outside factor.'
        else:
            code,description='inside_sign','Changed a sign in a bracket, so expansion does not recover the original terms.'
        return GeneratedProblem(generator_id=self.generator_id,generator_version=self.version,seed=seed,level=level,
            skill=machine['task'],question=f'Factorise completely ${expression}$.',answer=f'${answer}$',
            machine=machine,steps=(Step('Write the complete product',answer),),
            distractors=(Distractor(f'${distractor}$',code,description),),
            marking={'answer_type':'expression','expected':[answer],'form':'factorised','typed':answer})


GENERATORS=[FactorisationExtensionGenerator()]
