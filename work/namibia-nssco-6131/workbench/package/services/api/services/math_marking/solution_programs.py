"""Authored mathematical operations for retained questions.

Source presenters supply instance equations. Plans group routine applications and
attach a reason to each change of principle. Marking references named semantic
achievements explicitly; neither row order nor displayed step count sets marks.
"""
from dataclasses import dataclass
from fractions import Fraction
from .operation_reasons import operation_reason
import re


@dataclass
class SolutionProgram:
    steps: list
    achievements: dict
    method_awards: tuple = ()


def mathematical_rows(work):
    match=re.search(r'\\begin\{(gathered|aligned)\}',work)
    if not match:return [work.strip()]
    depth=1;ending=None
    for token in re.finditer(r'\\begin\{[^}]+\}|\\end\{[^}]+\}',work[match.end():]):
        depth += 1 if token[0].startswith(r'\begin') else -1
        if depth==0:
            ending=match.end()+token.start();break
    if ending is None:raise ValueError('Unbalanced authored mathematics environment')
    body=work[match.end():ending];
    rows=[];start=0;depth=0
    for token in re.finditer(r'\\begin\{[^}]+\}|\\end\{[^}]+\}|\\\\',body):
        text=token[0]
        if text.startswith(r'\begin'):depth+=1
        elif text.startswith(r'\end'):depth-=1
        elif depth==0:
            rows.append(body[start:token.start()].strip());start=token.end()
    rows.append(body[start:].strip())
    cleaned=[];lhs=''
    for row in rows:
        # Alignment tabs belong to the enclosing aligned environment only.
        # Tabs inside pmatrix/bmatrix/nested aligned must retain their columns.
        row=re.sub(r'\\begin\{[^}]+\}|\\end\{[^}]+\}|&',_alignment_tab_filter(),row).strip()
        if not row:continue
        if row.startswith('=') and lhs:row=lhs+row
        elif '=' in row:lhs=row.split('=',1)[0]
        cleaned.append(row)
    return cleaned


def _alignment_tab_filter():
    depth=0
    def replace(match):
        nonlocal depth
        token=match[0]
        if token.startswith(r'\begin'):depth+=1
        elif token.startswith(r'\end'):depth-=1
        elif depth==0:return ''
        return token
    return replace


def math_text(value):
    from services.math_generators.prose_formatting import normalise_notation
    text=str(value).strip()
    # Results are Markdown/LaTeX fragments, not assumed to be a single formula.
    # Strip only a whole outer display wrapper; preserve inline math in prose.
    if text.startswith('$$') and text.endswith('$$') and text.count('$')==4:text=text[2:-2].strip()
    elif text.startswith('$') and text.endswith('$') and text.count('$')==2:text=text[1:-1].strip()
    return normalise_notation(text)



class Author:
    def __init__(self,problem,content):
        self.problem=problem;self.rows=[math_text(x) for x in mathematical_rows(content[0])]
        self.steps=[];self.achievements={};self.used=set();self.step_keys=[]
    def add(self,key,action,reason,indices=None,expression=None):
        if expression is None:
            indices=list(range(len(self.rows))) if indices is None else list(indices)
            if any(i>=len(self.rows) for i in indices):raise ValueError(f'Authored row mapping changed: {self.problem.generator_id}/{self.problem.machine.get("task")}/{key}')
            expression=r' \\ '.join(self.rows[i] for i in indices);self.used.update(indices)
        if indices is not None:self.used.update(indices)
        expression=math_text(expression)
        self.steps.append(dict(action=action,reason=reason,result=expression));self.step_keys.append(key)
        self.achievements[key]=dict(action=action,reason=reason,result=expression)
    def finish(self,method_awards=()):
        if self.used and len(self.used)!=len(self.rows):
            raise ValueError(f'Unexplained authored rows: {self.problem.generator_id}/{self.problem.machine.get("task")}: {set(range(len(self.rows)))-self.used}')
        answer=math_text(self.problem.answer)
        # An explicit final-result row avoids guessing whether an answer occurs
        # as a digit substring in an unevaluated expression. It earns no method
        # mark and cannot change any named achievement.
        if answer and (not self.steps or self.steps[-1]['result'] != answer):
            self.steps.append(dict(action='State the requested result',
                reason='Report the evaluated result in the form and units requested by the question.',
                result=answer))
        return SolutionProgram(self.steps,self.achievements,tuple(method_awards))


def numeric_program(p,content):
    a=Author(p,content);m=p.machine;t=m.get('task',p.skill);f=p.generator_id.removeprefix('nssco_');n=len(a.rows)
    add=a.add
    if f=='fractions_decimals_percentages' and t in ('pick_smallest','pick_largest','compare_with_symbol'):
        from math import lcm
        from services.math_generators.formatting import number_latex
        if t=='compare_with_symbol':
            left,right=p.steps[0].value.split(' and ')
            values=[Fraction(left),Fraction(right)]
            # Read the authored operands, including their original percentage
            # or decimal notation; do not replace them with converted values.
            import re
            expression=re.findall(r'\$([^$]+)\$',p.question)[-1]
            shown=expression.split(r'\; \square \; ')
            if len(shown)!=2:raise ValueError('Missing comparison operands')
        else:
            shown=[number_latex(Fraction(x)) if '/' in x else x.replace('%',r'\%') for x in m['items']]
            values=[Fraction(x.rstrip('%'))/(100 if x.endswith('%') else 1) for x in m['items']]
        denominator=lcm(*(x.denominator for x in values))
        for i,(original,value) in enumerate(zip(shown,values)):
            equivalent=rf'\frac{{{value.numerator*(denominator//value.denominator)}}}{{{denominator}}}'
            # Equality here is exact, including recurring fractions.
            conversion=original+' = '+number_latex(value)
            if original==number_latex(value):conversion=original
            if equivalent!=number_latex(value):conversion+=' = '+equivalent
            add('comparable_'+str(i),'Write the next value with the common denominator',
                ('Divide this percentage by 100, then express it with the common denominator.' if r'\%' in original else 'Express this value as a fraction, then multiply numerator and denominator by the same number to reach the common denominator.'),expression=conversion)
        if t=='compare_with_symbol':
            result=shown[0]+' '+m['symbol']+' '+shown[1]
        else:
            order=sorted(range(len(values)),key=lambda i:values[i])
            result=''.join(((' = ' if values[order[j-1]]==values[i] else ' < ') if j else '')+shown[i] for j,i in enumerate(order))
        add('conversion','Compare the numerators on the shared scale',
            'With equal positive denominators, the smaller numerator gives the smaller value.'+(' Negative numerators farther below zero give smaller values.' if min(values)<0 else ''),expression=result)
        return a.finish()
    if f=='number_classifications_properties':
        if t in ('hcf','lcm'):
            add('prime_factors','Express both integers as prime products','Prime factorisation identifies each prime and its multiplicity.',range(n-1))
            add('selection','Choose the required prime powers',('The HCF uses only shared primes with their smaller exponents.' if t=='hcf' else 'The LCM uses every prime needed by either integer with its larger exponent.'),[n-1])
        elif t=='prime_factorisation':
            add('division','Divide successively by prime factors','Each exact prime divisor contributes a factor; continue until the quotient is one.',range(n-1))
            add('product','Write the prime-power product','Repeated occurrences of a prime are recorded by its exponent.',[n-1])
        else:add('classification','Check the defining number property',operation_reason(f,t),range(n))
    elif f=='directed_numbers_in_action':
        if t=='directed_arithmetic':
            add('product','Evaluate the multiplication and division first','Carry out multiplication and division from left to right before addition and subtraction. A product or quotient is negative when its two inputs have different signs.',range(n-1))
            add('combine','Combine the signed terms',('Subtract by adding the opposite, then combine signed terms from left to right.' if '-' in m['ops'] else 'Add the signed quantities from left to right, keeping each sign.'),[n-1])
        else:add('signed_change','Apply the signed comparison or change',operation_reason(f,t),range(n))
    elif f=='fractions_decimals_percentages':
        if t=='recurring_to_fraction':
            add('shift','Align the repeating decimal tails','Multiplying by ten shifts a one-digit recurring block one place.',range(2))
            add('cancel_tail','Subtract the two equations','The identical recurring tails cancel, leaving an integer multiple of the unknown.',[2])
            add('isolate','Divide and reduce','Divide both sides by the nonzero coefficient and cancel common factors.',[3])
        elif t in ('fraction_add','fraction_sub'):
            add('denominator','Express both fractions in equal-sized parts','Rescale numerator and denominator together to obtain a common denominator.',[0])
            add('combine','Combine the numerators and reduce','Equal denominators describe the same part size, so add or subtract only the numerators.',range(1,n))
        elif t=='fraction_div':
            add('reciprocal','Replace division by multiplication','Dividing by a nonzero fraction multiplies by its reciprocal; invert only the divisor.',[0])
            add('multiply','Multiply and reduce','Multiply numerators and denominators, then cancel common nonzero factors.',range(1,n))
        elif t=='successive_fractions':
            add('first_share','Find the first share','Multiply the original whole by the first fraction.',[0])
            add('remaining','Find the new whole','Subtract the first share; the next fraction applies to what remains.',[1])
            add('second_share','Find the second share','Multiply the remaining amount by the second fraction.',[2])
            add('left','Subtract the second share','The final remainder excludes both allocated shares.',[3])
            if n>4:add('percentage','Compare what is left with the original whole','Divide the final remainder by the original total and multiply by 100.',range(4,n))
        elif t=='whole_from_fraction':
            add('unit','Recover one equal part','Divide the known amount by the numerator counting its equal parts.',range(n-1))
            add('whole','Recover the complete quantity','Multiply one part by the denominator counting all parts.',[n-1])
        elif t in ('order_fractions','pick_smallest','pick_largest'):
            add('common_form','Put the values in a comparable form','Use equivalent fractions with a common denominator or equivalent decimals without changing values.',range(n-1))
            add('order','Compare the equivalent values','On a common scale, numerator or decimal size determines numerical order.',[n-1])
        else:add('conversion','Apply the fraction or place-value relationship',operation_reason(f,t),range(n))
    elif f=='advanced_percentages' or (f=='personal_finance_currency' and t=='compound_interest'):
        if t in ('reverse_increase','reverse_decrease'):
            add('multiplier','Find the multiplier relating the original and changed amounts','A percentage increase/decrease multiplies the original by one plus/minus the percentage as a fraction of 100. Here x is the original amount and M is the multiplier.',[0])
            add('equation','Relate the changed amount to the original','The supplied changed amount equals the unknown original multiplied by that factor.',[1])
            add('reverse','Recover the original','Divide the changed amount by its multiplier; applying the opposite percentage would use the wrong base.',[2])
        elif t in ('compound_amount','compound_interest','depreciation'):
            add('multiplier','Form the multiplier for one period','Each period changes the current balance by the supplied percentage, using subtraction for depreciation.',range(2))
            add('compound','Apply the multiplier for every period','Repeated equal percentage changes use a power of the multiplier, not a multiple of the percentage.',[2])
            if n>3:add('interest','Separate interest from the final balance','Interest earned excludes the original investment.',range(3,n))
        elif t in ('profit','loss','percentage_increase','percentage_decrease'):
            add('change','Calculate the size of the change','Subtract the smaller price or amount from the larger to find the magnitude of the change.',[0])
            add('percentage','Compare with the original base','Percentage profit/loss uses cost price; percentage change uses the original amount. Multiply the ratio by 100.',range(1,n))
        elif t in ('increase','decrease','percentage_remaining'):
            add('part','Calculate the percentage part','Percent means per hundred of the stated original whole.',[0])
            add('apply_change','Apply the change to the original',('Add the percentage part for an increase.' if t=='increase' else 'Subtract the percentage part to find the decreased or remaining amount.'),range(1,n))
        else:add('percentage','Express the part per hundred','Divide the part by the stated whole and multiply by 100.',range(n))
    elif f=='standard_form_estimates_approximations':
        if t=='estimate':
            add('round_inputs','Round all inputs first','An estimate deliberately simplifies the inputs before calculation, preserving the original operations.',range(n-1))
            add('evaluate','Calculate with the rounded inputs','The estimate comes from the rounded numbers, rather than rounding the exact original result.',[n-1])
        elif t in ('round','round_nearest'):
            add('neighbours','Locate the neighbouring rounded values','The requested precision determines the spacing between permissible rounded values.',[0])
            add('midpoint','Locate the halfway point','The midpoint decides which neighbouring value is nearer.',[1])
            add('round','Choose the rounded value','Choose the nearer value, applying the stated halfway convention at equality.',range(2,n))
        elif t.startswith('std_') or t.startswith('ordinary_'):
            add('calculate','Perform the indicated calculation','Multiply/divide coefficients and add/subtract powers of ten as appropriate; retain the complete value.',[0])
            add('normalise','Write the result in standard form','Adjust coefficient and exponent together so the coefficient is at least one and below ten.',range(1,n))
        elif n==2 and t not in ('to_standard_form',):
            add('evaluate','Evaluate the complete expression','Retain sufficient calculator accuracy through the original brackets and operations.',[0])
            add('round','Apply the requested precision','Round only after the complete calculation, preserving significant zeros.',[1])
        else:add('place_value','Use the power-of-ten place-value relationship',operation_reason(f,t),range(n))
    elif f=='limits_of_accuracy':
        if t in ('bounds_inequality','single_bound'):
            add('half_unit','Find half the rounding unit','The true value lies within half a rounding unit of the reported value.',[0])
            add('endpoints','Calculate both endpoints','Subtract and add the half-unit; lower endpoints are included and upper endpoints excluded under the stated rounding convention.',range(1,n))
        else:
            add('input_bounds','Establish the bounds of every measured input','Use half of each stated rounding unit, preserving the appropriate endpoint inclusion.',range(n-1))
            add('extremise','Choose endpoints for the complete requested expression',{'max_diff':'The greatest difference uses the upper minuend and lower subtrahend.','min_diff':'The least difference uses the lower minuend and upper subtrahend.','speed_max':'For positive distance and time, speed is greatest at upper distance divided by lower time.'}.get(t,'For positive lengths, sums/products increase with each input: choose all lower inputs for a minimum and all upper inputs for a maximum.'),[n-1])
    elif f=='ratios_scales_rates':
        if t in ('share_in_ratio','ratio_find_other','ratio_find_total'):
            add('parts','Count the total ratio parts','A ratio represents equal-sized shares, whose counts add to the whole.',[0])
            add('unit','Find one equal share','Divide the known amount by the number of shares it represents.',[1])
            add('requested','Scale to the requested shares','Multiply one share by the required share count.',[2])
        elif t in ('average_speed_two_legs','total_distance'):
            add('leg_distances','Find each leg distance','Each leg uses its own speed multiplied by its own duration.',range(2))
            if t=='average_speed_two_legs':
                add('totals','Combine journey distance and time','A journey average uses total distance divided by total elapsed travel time, not the mean of speeds.',[2,3])
                add('average','Apply the average-speed ratio','Divide the combined distance by the combined duration in matching units.',[4])
            else:add('total','Add the leg distances','Successive leg distances contribute once each to the complete distance.',range(2,n))
        elif t in ('actual_to_map','map_to_actual'):
            add('units','Express the scale in matching units','A map scale compares lengths in the same units; one kilometre is 100000 centimetres.',range(n-2))
            add('scale','Apply the scale factor in the correct direction','Multiply drawing length for actual length, or divide actual length for drawing length; then convert to the requested unit.',range(n-2,n))
        elif t=='speed_unit_conversion':
            add('units','Convert distance and time separately','A compound rate needs both the distance unit and time unit converted.',range(n-1))
            add('rate','Divide distance by time','The converted distance and duration now give the requested speed unit.',[n-1])
        elif n>1:
            add('unit_rate','Establish the unit rate or invariant','Use the stated proportional relationship to obtain a per-unit value, common work total or duration in hours.',range(n-1))
            add('apply_rate','Apply the relationship to the requested quantity','Scale the unit rate or divide the invariant total by the requested quantity, keeping units consistent.',[n-1])
        else:add('ratio','Reduce the ratio without changing its value','Divide every term by the same greatest common factor.',range(n))
    elif f=='personal_finance_currency':
        if t in ('rate','principal','time'):
            from .formatting_adapter import simple_interest_program
            return simple_interest_program(p)
        if t=='change':
            add('costs','Calculate both purchase costs','Multiply each count by its own unit price.',range(2))
            add('total','Combine the purchase costs','The purchase total contains each item cost exactly once.',[2])
            add('change','Subtract the purchase total from payment','Change is the amount paid minus the amount spent.',[3])
        elif t=='simple_interest':
            add('time','Express time in years','The annual interest rate requires time in years; divide a month count by twelve.',[1])
            add('interest','Substitute in the simple-interest relationship','Simple interest uses the original principal for every year, so I=Prt/100.',[0,2])
        else:
            add('rate','Read the supplied exchange relationship','The question states how many Namibian dollars equal one foreign unit.',[0])
            add('convert','Convert in the requested direction','Multiply foreign units by dollars per unit, or divide Namibian dollars by dollars per foreign unit.',range(1,n))
    elif f=='income_taxes_bills':
        if p.skill=='wages_commission':
            add('wages','Calculate basic wages','Basic wages equal hours worked multiplied by the hourly rate.',[0])
            add('commission','Calculate commission separately','Commission is the stated percentage of sales, not of basic wages.',[1])
            add('combine','Add the two earning components','Total earnings include both wages and commission.',[2])
        elif p.skill=='fictional_tax_table':
            add('excess','Find income above the supplied threshold','The marginal rate applies only to income above this exercise threshold.',[0])
            add('tax','Apply the supplied marginal rate','Calculate the specified percentage of the excess income only.',[1])
            add('total_tax','Add the fixed base tax','The fixed base and marginal excess tax are separate components.',range(2,n))
        else:
            add('usage','Subtract the earlier meter reading','Cumulative meter readings differ by the units used.',[0])
            add('charge','Price the measured usage','Multiply consumed units by the supplied rate per unit.',[1])
            add('bill','Add the fixed charge once','The fixed charge is separate from the usage charge.',range(2,n))
    elif f=='defining_sets_notation':
        if t in ('set_list','set_count'):return set_program(p,content)
        add('membership','Apply the defining set condition',operation_reason(f,t),range(n))
    elif f=='venn_diagrams':
        if t=='three_set_list':return set_program(p,content)
        only_a,only_b,both,neither=(m[k] for k in ('only_a','only_b','both','neither'))
        A,B=only_a+both,only_b+both;total=only_a+only_b+both+neither;union=total-neither
        if t=='find_both':
            add('union','Find the number studying at least one subject','Remove learners studying neither subject from the whole class.',expression=rf'n(A\cup B)={total}-{neither}={union}')
            add('intersection','Recover the overlap by inclusion–exclusion','Adding both subject totals counts their intersection twice; subtract the union once.',expression=rf'n(A\cap B)={A}+{B}-{union}={both}')
            if p.question.rstrip().endswith('only.'):
                add('exclusive','Remove the overlap from the second subject total','Only the second subject excludes learners counted in both subjects.',expression=rf'n(B\setminus A)={B}-{both}={only_b}')
        else:
            add('exclusive_regions','Find the two exclusive regions','Subtract the given intersection from each subject total.',expression=rf'n(A\setminus B)={A}-{both}={only_a},\quad n(B\setminus A)={B}-{both}={only_b}')
            add('union','Combine the subject totals without double-counting','The intersection contributes once to the union.',expression=rf'n(A\cup B)={A}+{B}-{both}={union}')
            formulas={'only_a':f'{A}-{both}','both':str(both),'sb':str(B),
                'neither':f'{total}-{union}','not_b':f'{total}-{B}','union':f'{A}+{B}-{both}'}
            values={'only_a':only_a,'both':both,'sb':B,'neither':neither,'not_b':only_a+neither,'union':union}
            ask=m['ask'];value=values[ask]
            add('requested','Select the requested count','Use all and only the disjoint regions named by the event; a complement is relative to the complete class.',expression=r'\text{Requested count}='+formulas[ask]+f'={value}')
            if t=='venn_probability':
                add('probability','Convert the event count to a probability','The learner is selected from the whole class, so divide by its total rather than by the union.',expression=rf'P=\frac{{{value}}}{{{total}}}')
    elif f=='metric_units_conversions':
        if t in ('density','density_back'):
            add('units','Convert mass and volume independently','A centimetre-to-metre factor is cubed for a cubic volume unit.',range(2))
            add('compound','Form the density conversion factor','Density is mass divided by volume, so divide the mass conversion by the volume conversion.',[2])
            add('convert','Apply the requested conversion direction','Multiply by the factor in the forward direction or its reciprocal in the reverse direction.',range(3,n))
        elif n>1:
            add('units','Establish the component-unit conversion','A rate conversion changes both numerator and denominator units.',range(n-1))
            add('convert','Apply the compound conversion factor','Apply the factor in the direction required by the question.',[n-1])
        else:add('units','Convert the quantity in consistent units',operation_reason(f,t),range(n))
    elif f=='time_clocks_timetables':
        if t in ('duration_minutes','duration_hours_minutes'):
            add('clock_values','Convert the two clock readings to minutes','Hours contribute sixty minutes each; add a day to the end reading when the journey crosses midnight.',range(2))
            add('elapsed','Subtract start from end','Elapsed time is the difference between the two readings on the same continuous time scale.',[2])
            if n>3:add('hours_minutes','Convert the duration to hours and minutes','Divide by sixty to obtain whole hours and the remaining minutes.',range(3,n))
        elif t in ('arrive','early_midnight','late','latest_departure'):
            add('clock_value','Express the given clock reading in minutes','A common minute scale allows durations to be added or subtracted consistently.',[0])
            add('shift','Apply the signed duration',('Subtract travel/lead time to recover an earlier clock reading.' if t in ('early_midnight','latest_departure') else 'Add the journey duration or delay to the supplied clock reading.'),[1])
            add('clock','Return to the 24-hour clock','A day contains 1440 minutes; wrap across midnight and express the remaining minutes as hours and minutes.',range(2,n))
        elif t in ('total_time','arrival_time'):
            add('duration','Add the travel and waiting durations','Elapsed journey time includes waiting between its travel legs.',[0])
            add('hours_minutes','Express the total duration in hours and minutes','Divide minutes by sixty, keeping the remainder as minutes.',[1])
            if n>2:add('arrival','Add the duration to departure','The arrival clock follows departure by the complete elapsed duration.',range(2,n))
        else:add('units','Convert between decimal hours and hours/minutes','The fractional part of an hour is multiplied by sixty for minutes; minutes are divided by sixty for decimal hours.',range(n))
    else:return None
    awards=('leg_distances','average') if t=='average_speed_two_legs' else ('wages','combine') if f=='income_taxes_bills' and p.skill=='wages_commission' else ('excess','tax') if f=='income_taxes_bills' and p.skill=='fictional_tax_table' else ()
    return a.finish(awards)


def source_content(problem):
    from services.math_generators.presentation import (algebra_content,number_content,
        functions_content,functions_concepts_content,graph_content,topic_content)
    return (algebra_content(problem) or number_content(problem) or functions_content(problem)
            or functions_concepts_content(problem) or graph_content(problem) or topic_content(problem))


def program_for(problem, *, strict=True):
    if problem.generator_id=='nssco_factorisation_basics':
        from .factorising_program import basics_program
        return basics_program(problem)
    if problem.generator_id=='nssco_factorisation_extension':
        from .factorising_program import extension_program
        return extension_program(problem)
    if problem.generator_id=='nssco_factorising_quadratics':
        from .factorising_program import quadratic_program
        return quadratic_program(problem)
    content=source_content(problem)
    if content is None:return None
    from .elementary_programs import elementary_program
    from .visual_programs import visual_program
    from .geometry_programs import geometry_program
    from .algebra_programs import algebra_program
    from .applied_programs import applied_program
    for builder in (elementary_program,visual_program,numeric_program,geometry_program,algebra_program,applied_program):
        program=builder(problem,content)
        if program is not None:return program
    if not strict:return None
    raise ValueError(f'Missing authored solution program: {problem.generator_id}/{problem.skill}/{problem.machine.get("task")}')


def set_program(p,content):
    """Follow the exact set-expression tree, explaining its actual operators."""
    from services.math_generators.family_sets_graphs import _TWO_SET_EXPRS,_THREE_SET_EXPRS,_lx,_eval_set,_members
    from services.math_generators.topic_sets_graphs_content import set_tex
    m=p.machine;a=Author(p,content)
    universe_text=re.search(r'\\xi = \\\{(.*?)\\\}',p.question)[1]
    universe=list(map(int,re.findall(r'\d+',universe_text)));members=_members(universe,m['sets'])
    tree=next(t for t in (*_TWO_SET_EXPRS,*_THREE_SET_EXPRS) if _lx(t)==m['expression'])
    seen=set()
    operations={'and':('Intersect the indicated sets','Keep exactly the elements belonging to every operand set.'),
                'or':('Form the indicated union','Keep elements belonging to any operand set, listing each element once.'),
                'not':('Take the complement in the universal set','Keep universal-set elements outside the complete operand set.')}
    def visit(node):
        if node[0]=='set' or node in seen:return
        for child in node[1:]:visit(child)
        action,reason=operations[node[0]]
        a.add('operation_'+str(len(seen)),action,reason,expression=_lx(node)+'='+set_tex(_eval_set(node,universe,members)))
        seen.add(node)
    visit(tree)
    if m['task']=='set_count':
        a.add('cardinality','Count the distinct qualifying members','Cardinality is the number of set elements, not their sum.',
            expression='n('+m['expression']+')='+str(len(_eval_set(tree,universe,members))))
    return a.finish()
