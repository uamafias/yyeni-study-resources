"""NSSCO 6131 7(c) conceptual questions, alongside lesson 15827 calculations.

A separate recipe identity preserves every existing nssco_functions draw. All
relations have explicit domains; conceptual responses are judged by the existing
AI contract, never by literal prose matching. No learner drawing is required.
"""
from .base import GeneratedProblem, MathGenerator, Step
from .formatting import linear_latex

GENERATOR_ID = 'nssco_functions_concepts'



def _set(values):
    return r'\{' + ', '.join(str(v) for v in sorted(set(values))) + r'\}'


def _make(g, seed, level, skill, question, answer, facts, explanation):
    facts = dict(facts, explanation=explanation)
    return GeneratedProblem(g.generator_id, g.version, seed, level, skill,
        question, answer, machine=facts,
        steps=(Step('Give the requested conceptual response and apply it to the given mapping', answer, 'text_description'),),
        marking={'answer_type':'text_description', 'expected':[answer], 'typed':answer})


def _relation(g, r, seed, level):
    start=r.randint(-15,10); gap=r.randint(1,4)
    inputs=[start+i*gap for i in range(4)]
    out=r.randint(-12,12); output_gap=r.randint(1,3); ys=[out+i*output_gap for i in range(4)]
    shape=('one_one','many_one','missing','split')[((seed-1)//2)%4]
    if shape=='many_one': ys[1]=ys[0]
    pairs=list(zip(inputs,ys))
    if shape=='missing': pairs.pop()
    if shape=='split': pairs.append((inputs[0],max(ys)+3))
    outputs=sorted({v for _,v in pairs}|{max(ys)+7})
    mapping=r',\quad '.join(f'{u}\\mapsto {v}' for u,v in pairs)
    question=(f'A relation from $A={_set(inputs)}$ to $B={_set(outputs)}$ is listed by all its arrows: '
              f'${mapping}$. Explain what is meant by a function from $A$ to $B$. '
              'Does this relation define such a function? Give a reason using the listed arrows.')
    valid=shape in ('one_one','many_one')
    reason=(f'Input ${inputs[-1]}$ has no output.' if shape=='missing' else
            f'Input ${inputs[0]}$ has two different outputs, ${ys[0]}$ and ${max(ys)+3}$.' if shape=='split' else
            'Every member of $A$ has exactly one output in $B$.')
    answer=('A function assigns exactly one output in $B$ to every input in $A$. '
            + ('Yes. ' if valid else 'No. ')+reason)
    explanation=(f'$A$ is the stated input set and $B$ the possible output set; an arrow $u\\mapsto v$ means input $u$ is assigned output $v$. '
                 +reason+' Different inputs may share an output and unused members of $B$ are allowed. '
                 'Neither makes a relation cease to be a function. An input with no output or two different outputs does.')
    return _make(g,seed,level,'function_definition',question,answer,
                 {'task':'relation_function','shape':shape,'inputs':inputs,'codomain':outputs,'pairs':pairs,'is_function':valid,'reason':reason},explanation)


def _notation(g,r,seed,level):
    a=r.choice((-5,-4,-3,-2,2,3,4,5)); b=r.randint(-12,12); x=r.randint(-9,9)
    rule=linear_latex(a,b); y=a*x+b; direction=r.choice(('to_mapping','from_mapping'))
    given=f'f(x)={rule}' if direction=='to_mapping' else f'f:x\\mapsto {rule}'
    required='mapping notation' if direction=='to_mapping' else 'function-value notation'
    written=f'f:x\\mapsto {rule}' if direction=='to_mapping' else f'f(x)={rule}'
    question=(f'The function $f$ has all real numbers as inputs and is written ${given}$. '
              f'Rewrite its rule in {required}. Then state the output corresponding to input ${x}$.')
    answer=f'${written}$.\n\n$f({x})={a}({x})+({b})={y}$.'
    explanation=(f'$f$ names the function, $x$ is its input, and ${rule}$ is its output rule. '
                 f'The notations $f(x)={rule}$ and $f:x\\mapsto {rule}$ describe the same assignment. '
                 f'The arrow is read “maps to”; it is not an equation between $f$ and $x$. '
                 f'For input ${x}$, substitute the whole number into the rule: ${a}({x})+({b})={y}$. '
                 '$f(x)$ does not mean $f$ multiplied by $x$.')
    return _make(g,seed,level,'mapping_notation',question,answer,
                 {'task':'mapping_notation','direction':direction,'a':a,'b':b,'input':x,'output':y,'written':written},explanation)


def _one_one(g,r,seed,level):
    start=r.randint(-20,10); gap=r.randint(1,5); inputs=[start+i*gap for i in range(4)]
    base=r.randint(-15,15); ys=[base+i*r.randint(1,4) for i in range(4)]
    # Distinct by construction, before the deliberate many-one collision.
    ys=sorted(set(ys))
    while len(ys)<4: ys.append(max(ys)+r.randint(1,4))
    one=((seed-1)//3)%2==0
    if not one:ys[1]=ys[0]
    pairs=list(zip(inputs,ys)); mapping=r',\quad '.join(f'{u}\\mapsto {v}' for u,v in pairs)
    question=(f'The function $f$ has domain $A={_set(inputs)}$ and its complete mapping is ${mapping}$. '
              'Is $f$ one-one? Explain what one-one means and justify your answer. '
              'Can the reversed arrows define an inverse function on the range of $f$?')
    reason=('All four outputs are different.' if one else
            f'The different inputs ${inputs[0]}$ and ${inputs[1]}$ both map to ${ys[0]}$.')
    inverse=('The reversed arrows do define an inverse function on the range: each output returns to exactly one original input.' if one else
             f'The reversed arrows do not define an inverse function: input ${ys[0]}$ would have outputs ${inputs[0]}$ and ${inputs[1]}$.')
    answer=('One-one means that different inputs have different outputs. '+('Yes. ' if one else 'No. ')+reason+' '+inverse)
    explanation=(f'$A$ contains the four allowed inputs. The range is the set of outputs actually reached, ${_set(ys)}$. '
                 +reason+' A many-one mapping can still be a function, because each original input has just one output. '
                 +inverse+' The requirement is about distinct inputs, not whether every real number appears as an output.')
    return _make(g,seed,level,'one_one_mapping',question,answer,
                 {'task':'one_one_mapping','inputs':inputs,'pairs':pairs,'one_one':one,'reason':reason,'inverse_reason':inverse},explanation)


def _domain(g,r,seed,level):
    a=r.randint(1,6); b=r.randint(-10,10); n=r.randint(1,8)
    domain=('all_real','nonnegative','nonpositive')[((seed-1)//3)%3]; one=domain!='all_real'
    rule=(str(a) if a!=1 else '')+'x^2'+(f'+{b}' if b>0 else str(b) if b<0 else '')
    domain_text={'all_real':'all real numbers','nonnegative':'all real numbers satisfying $x\\ge 0$','nonpositive':'all real numbers satisfying $x\\le 0$'}[domain]
    question=(f'The function $f(x)={rule}$ has domain {domain_text}. '
              'Is $f$ one-one on this stated domain? Give a reason. '
              'Would it have an inverse function defined on its range?')
    y=a*n*n+b
    reason=(f'The allowed inputs ${-n}$ and ${n}$ are different, but $f({-n})=f({n})={y}$.' if not one else
            'On the stated domain, squaring different inputs gives different outputs; multiplying by a positive number and adding a constant preserves this.')
    answer=('Yes, it is one-one. ' if one else 'No, it is many-one. ')+reason+(' Therefore an inverse function exists on its range.' if one else ' Therefore reversing the whole mapping does not give an inverse function on its range.')
    explanation=(f'$x$ is restricted to {domain_text}; the domain is part of the function, not optional information. '
                 +reason+' On all real inputs a square rule combines positive and negative inputs. Restricting to one side of zero removes those pairs. '
                 'An inverse function must recover one original input from each output. Do not decide one-one status from the formula while ignoring the domain.')
    return _make(g,seed,level,'one_one_domain',question,answer,
                 {'task':'one_one_domain','a':a,'b':b,'witness':n,'domain':domain,'one_one':one,'reason':reason},explanation)


def _inverse(g,r,seed,level):
    a=r.choice((-6,-5,-3,-2,2,3,5,6)); b=r.randint(-15,15); x=r.randint(-8,8); y=a*x+b
    question=(f'The one-one function $f$ is defined by $f(x)={linear_latex(a,b)}$ for all real inputs. '
              f'Explain what the inverse function $f^{{-1}}$ does, then find $f^{{-1}}({y})$.')
    answer=(f'The inverse reverses $f$: it maps each output of $f$ back to its original input. '
            f'$f({x})={a}({x})+({b})={y}$, so $f^{{-1}}({y})={x}$.')
    explanation=(f'$f$ is the original rule and $f^{{-1}}$ reverses it. Here input ${x}$ produces output ${y}$, '
                 f'so the inverse takes input ${y}$ and returns ${x}$. Equivalently solve ${a}x+({b})={y}$. '
                 'The superscript $-1$ denotes an inverse function, not the reciprocal $1/f(x)$. '
                 'The nonzero linear coefficient makes the original function one-one, so this reversal is unambiguous.')
    return _make(g,seed,level,'inverse_meaning',question,answer,
                 {'task':'inverse_meaning','a':a,'b':b,'input':x,'output':y},explanation)


def _composite(g,r,seed,level):
    a=r.choice((-4,-3,-2,2,3,4)); c=r.choice((-5,-3,-2,2,3,5)); b=r.randint(-10,10); d=r.randint(-10,10); x=r.randint(-7,7)
    order=r.choice(('gf','fg')); rules={'f':(a,b),'g':(c,d)}; outer,inner=order
    u,v=rules[inner]; w,z=rules[outer]; mid=u*x+v; result=w*mid+z; rule=linear_latex(w*u,w*v+z)
    shape=r.choice(('notation','arrows'))
    prompt=(f'Explain what the composite ${order}$ means, including which function is applied first.' if shape=='notation' else
            f'Inputs pass first through ${inner}$ and then through ${outer}$. Explain why this is a composite function and name it using the given function letters.')
    question=(f'For real inputs, $f(x)={linear_latex(a,b)}$ and $g(x)={linear_latex(c,d)}$. '+prompt+
              f' Write its rule in mapping notation, then find its output for input ${x}$.')
    answer=(f'A composite uses the output of one function as the input to the next: apply ${inner}$ first, then ${outer}$. '
            f'${order}(x)={outer}({inner}(x))$.\n\n'
            f'${order}:x\\mapsto {w}({linear_latex(u,v)})+({z})={rule}$.\n\n'
            f'${inner}({x})={mid}$, so ${order}({x})={outer}({mid})={result}$.')
    explanation=(f'$f$ and $g$ name two rules. In ${order}$ the right-hand function ${inner}$ acts on $x$ first. '
                 f'Its whole output ${linear_latex(u,v)}$ becomes the input to ${outer}$; the result is ${rule}$. '
                 f'For the actual input ${x}$, the intermediate output is ${mid}$ and the final output is ${result}$. '
                 'Mapping notation describes this combined rule. Composition is not multiplication, and reversing the order generally changes the rule.')
    return _make(g,seed,level,'composite_meaning',question,answer,
                 {'task':'composite_meaning','shape':shape,'f':[a,b],'g':[c,d],'order':order,'input':x,'intermediate':mid,'output':result,'coefficient':w*u,'constant':w*v+z},explanation)


class FunctionsConceptsGenerator(MathGenerator):
    generator_id=GENERATOR_ID
    version=1
    levels=(1,2,4)
    level_skills={1:('function_definition','mapping_notation'),2:('one_one_mapping','one_one_domain','inverse_meaning'),4:('composite_meaning',)}
    error_notes={skill:{'misread_mapping':'Confused the input/output direction or ignored the stated domain.'} for skills in level_skills.values() for skill in skills}

    def _build(self,rng,seed,level):
        builders={1:(_relation,_notation),2:(_one_one,_domain,_inverse),4:(_composite,)}[level]
        # Balance canonical teaching slots without per-skill selection machinery.
        # Recall seeds still produce fresh numerical inputs for every task.
        builder=builders[(seed-1)%len(builders)]
        return builder(self,rng,seed,level)


GENERATORS=[FunctionsConceptsGenerator()]
