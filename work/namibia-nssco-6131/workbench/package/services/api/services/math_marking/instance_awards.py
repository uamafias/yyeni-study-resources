"""Instance-bound achievements, authored independently of reference-step order."""



def instantiate(problem, profile, awards, demand):
    family=problem.generator_id.removeprefix('nssco_')
    alternative=(' Accept an equivalent valid route. Judge mathematical evidence, not a count or order of reference steps; a later arithmetic slip does not erase a correct method achievement.')
    if profile == 'estimate3':
        rounded=problem.steps[:-1]
        examples='; '.join(f'{s.description} = {s.value}' for s in rounded)
        return [
            {'marks':1,'achievement':f'Any {len(rounded)-1} operands correctly rounded as instructed (one mark total for this stage): {examples}.'},
            {'marks':1,'achievement':f'All {len(rounded)} operands correctly rounded (one additional mark; the preceding partial stage alone cannot earn it). Reference values: {examples}.'},
            {'marks':1,'achievement':f'Correct estimate calculated from the rounded inputs: {problem.answer}.'}]
    if profile == 'algebra_fraction3' and family == 'polynomials_algebraic_fractions' and problem.machine.get('task') == 'single_fraction':
        from services.math_generators.formatting import linear_latex
        m=problem.machine; op='−' if m['subtract'] else '+'
        if 'dens' in m:
            (a,b),(c,d)=m['dens'];left,right=linear_latex(a,b),linear_latex(c,d)
            A,B=m['tops'];den=f'({left})({right})';numerator=f'{A}({right}) {op} {B}({left})'
        elif m['form']=='x_over_x_plus_p':
            left=linear_latex(1,m['p']);den=f'x({left})';numerator=f'x² {op} {m["q"]}({left})'
        else:
            left,right=linear_latex(1,m['p']),linear_latex(1,-m['p'])
            den=f'({right})({left})';numerator=f'{m["u"]}({right}) {op} {m["v"]}'
        return [
            {'marks':1,'achievement':'Establish an appropriate common denominator: '+den+'. Equivalent expanded denominators accepted.'},
            {'marks':1,'achievement':'Combine the complete numerator expressions with correct signs: '+numerator+'. Equivalent expansions accepted.'},
            {'marks':1,'achievement':f'Correct simplified single fraction: {problem.answer}. Do not accept cancellation at an excluded input, but do not require an unasked list of restrictions.'}]
    if profile in ('calculation2','calculation3'):
        from .solution_programs import program_for
        program=program_for(problem)
        if program is None:raise ValueError('An applied-method profile requires an authored semantic program')
        if profile=='calculation3':
            if len(program.method_awards)!=2:
                raise ValueError(f'Unmapped branch achievements: {family}/{problem.machine.get("task")}/{problem.skill}')
            keys=program.method_awards
        else:
            from .method_achievements import setup_key
            keys=(setup_key(problem),)
        result=[]
        for key in keys:
            achievement=program.achievements[key]
            result.append({'marks':1,'achievement':achievement['action']+'. '+achievement['reason']+' Applied reference: '+achievement['result']+'. Award the applied method even if later arithmetic slips; this is not another final-answer accuracy award.'+alternative})
        result.append({'marks':1,'achievement':f'Correct complete requested result: {problem.answer}. Apply the required form, precision and units.'})
        return result
    return awards
