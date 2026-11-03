"""Standard form, rounding and rate calculations for fixed number examples."""
from decimal import Decimal
from math import gcd
import re
from .number_teaching import F,n,frac,work,ratio,math_spans

STANDARD_LABELS={1:'Converting to and from standard form',2:'Rounding to a specified accuracy',
                 3:'Estimating with rounded numbers',4:'Calculating with standard form',5:'Calculator answers and significant figures'}
RATIO_LABELS={1:'Simplifying ratios and sharing a total',2:'Finding amounts from one known ratio share',
              3:'Using map scales with consistent units',4:'Unit rates and direct or inverse proportion',
              5:'Distance, time and average speed'}


def standard_parts(text):
    match=re.fullmatch(r'([\d.]+) x 10\^(-?\d+)',text)
    if not match:raise ValueError(text)
    return F(match[1]),int(match[2])


def standard(problem):
    m=problem.machine;task=m['task'];lines=[]
    if task=='to_standard_form':
        coefficient,exponent=standard_parts(m['answer']);value=m['value']
        lines=[f'{value}={n(coefficient)}\\times10^{{{exponent}}}',f'1\\le {n(coefficient)}<10']
        explanation=f'In standard form $A\\times10^n$, $A$ is the coefficient and $n$ an integer exponent. Here $A={n(coefficient)}$ and $n={exponent}$. Moving the point changes the coefficient; the power of ten restores the original value. Check that $1\\le A<10$. A small positive number uses a negative exponent.'
    elif task=='from_standard_form':
        a,e=m['mantissa'],m['exponent'];value=F(a)*F(10)**e
        lines=[f'{a}\\times10^{{{e}}}={n(value)}']
        explanation=f'The coefficient is ${a}$ and exponent ${e}$. '+('Divide' if e<0 else 'Multiply')+f' by $10^{{{abs(e)}}}$, moving the decimal point ${abs(e)}$ places '+('left' if e<0 else 'right')+'. Add placeholder zeros as needed and check the order of magnitude.'
    elif task in ('round','round_nearest'):
        value=F(m['value'])
        if task=='round_nearest':unit=F(m['unit']);request=f'the nearest ${n(unit)}$'
        else:
            digits=m['digits'];mode=m['mode'];exponent=-digits if mode=='decimal_places' else Decimal(m['value']).adjusted()-digits+1
            unit=F(10)**exponent;request=f'${digits}$ '+('decimal places' if mode=='decimal_places' else 'significant figures')
        lower=(value//unit)*unit;upper=lower+unit;mid=(lower+upper)/2
        lines=[f'{n(lower)}\\le {m["value"]}<{n(upper)}',r'\text{Midpoint}='+frac(f'{n(lower)}+{n(upper)}',2)+f'={n(mid)}',f'{m["value"]}\\approx{m["answer"]}']
        explanation=f'We are rounding ${m["value"]}$ to {request}. The two neighbouring values at that accuracy are ${n(lower)}$ and ${n(upper)}$; their midpoint is ${n(mid)}$. '+('The value is below the midpoint, so choose the lower neighbour. ' if value<mid else 'The value is at or above the midpoint, so round up to the upper neighbour. ')+('Count significant figures from the first nonzero digit. ' if m.get('mode')=='sig_figs' else '')+'Keep any trailing decimal zeros required to show the stated accuracy.'
    elif task=='estimate':
        values=m['numbers'];rounded=[step.value for step in problem.steps[:3]];a,b,c=rounded
        lines=[f'{old}\\approx{new}' for old,new in zip(values,rounded)]
        calculation={'mul_div':frac(f'{a}\\times{b}',c),'add_div':frac(f'{a}+{b}',c),'div_mul':frac(a,f'{b}\\times{c}')}[m['shape']]
        lines.append(r'\text{Estimate}='+calculation)
        explanation='Round each of the three given numbers to one significant figure before doing the calculation. Here the replacements are '+', '.join(f'${old}\\to{new}$' for old,new in zip(values,rounded))+'. Preserve the original brackets and order of operations. This is an estimate from the rounded inputs, not the exact original calculation rounded at the end.'
    elif task in ('std_mul','std_div'):
        pairs=re.findall(r'([\d.]+)\s*\\times\s*10\^\{(-?\d+)\}',problem.question);(a,e),(b,f)=pairs;e,f=int(e),int(f)
        divide=task=='std_div';coefficient=F(a)/F(b) if divide else F(a)*F(b);exponent=e-f if divide else e+f
        coeff=frac(a,b) if divide else f'{a}\\times{b}';op='-' if divide else '+'
        lines=[f'({coeff})\\times10^{{({e}){op}({f})}}',f'={n(coefficient)}\\times10^{{{exponent}}}']
        explanation=f'The coefficients are ${a}$ and ${b}$ and the powers of ten are ${e}$ and ${f}$. '+('Divide coefficients and subtract the denominator exponent.' if divide else 'Multiply coefficients and add exponents.')+f' This gives ${n(coefficient)}\\times10^{{{exponent}}}$. Adjust its coefficient and exponent together if necessary so the final coefficient is at least $1$ and below $10$.'
    elif task in ('ordinary_mul','ordinary_div'):
        a,b=math_spans(problem.question)[:2];operation=f'{a}\\times{b}' if task=='ordinary_mul' else frac(a,b)
        coefficient,exponent=standard_parts(m['answer']);value=coefficient*F(10)**exponent
        lines=[operation+f'={n(value)}',f'{n(value)}={n(coefficient)}\\times10^{{{exponent}}}']
        explanation=f'Calculate the '+('product' if task=='ordinary_mul' else 'quotient')+f' of ${a}$ and ${b}$ first. Then express that value as a coefficient between $1$ inclusive and $10$ exclusive, times a power of ten. Here those are ${n(coefficient)}$ and $10^{{{exponent}}}$. Check that their product has the same value as the ordinary number.'
    elif task in ('root_plus_cube_root','cube_of_sum','root_over','product_roots'):
        lines=[m['expression']+r'\approx '+problem.steps[0].value,f'\\text{{To 3 significant figures: }}{m["answer"]}']
        explanation='Use the entire displayed expression, including root and bracket scopes, in the calculator. '+('The outer cube applies to the whole bracket, not just to its last term. ' if task=='cube_of_sum' else '')+'The first displayed decimal is an approximation for reading the calculation; retain the calculator’s full precision for rounding. Count three significant figures from the first nonzero digit and preserve a final zero if it is significant.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation


def rates(problem):
    m=problem.machine;task=m['task'];lines=[]
    if task=='simplify_ratio':
        a,b=m['x'],m['y'];g=gcd(a,b);lines=[f'{a}:{b}=({a}\\div{g}):({b}\\div{g})={a//g}:{b//g}']
        explanation=f'The quantities are in the stated order, ${a}:{b}$. Their highest common factor is ${g}$. Divide both parts by ${g}$; simplifying changes the numbers in the ratio but preserves their relative sizes. Keep the original order.'
    elif task in ('share_in_ratio','ratio_find_other','ratio_find_total'):
        parts=m['ratio'];total=sum(parts)
        if task=='share_in_ratio':one=F(m['total'])/total;known=f'The given total is ${m["total"]}$ for all ${total}$ parts.';first=frac(m['total'],total);target=parts[m['index']]
        else:
            one=F(m['given'])/parts[m['index']];known=f'The given amount ${m["given"]}$ represents ${parts[m["index"]]}$ parts, not all ${total}$ parts.';first=frac(m['given'],parts[m['index']]);target=total if task=='ratio_find_total' else parts[m['other']]
        lines=[r'\text{Total ratio parts}='+'+'.join(map(str,parts))+f'={total}',r'\text{One part}='+first+f'={n(one)}',r'\text{Requested amount}='+f'{n(one)}\\times{target}={n(one*target)}']
        explanation=f'The ratio is ${ratio(parts)}$. '+known+f' Find the value of one part, ${n(one)}$, then multiply by ${target}$ parts for the requested amount. Match each ratio position to the person or material named in the question.'
    elif task in ('map_to_actual','actual_to_map'):
        scale=m['scale'];lines=[r'1\text{ cm on map}='+f'{scale}\\text{{ cm in reality}}',r'1\text{ km}=100000\text{ cm}']
        if task=='map_to_actual':
            length=F(m['length_cm']);actual=length*scale
            lines.extend([r'\text{Actual cm}='+f'{n(length)}\\times{scale}={n(actual)}',r'\text{Actual km}='+frac(n(actual),100000)])
            method=f'Multiply the map distance ${n(length)}$ cm by ${scale}$ to find real centimetres, then divide by $100000$ for kilometres.'
        else:
            actual=F(m['actual_km']);cm=actual*100000
            lines.extend([r'\text{Actual cm}='+f'{n(actual)}\\times100000={n(cm)}',r'\text{Map cm}='+frac(n(cm),scale)])
            method=f'Convert the real ${n(actual)}$ km to centimetres first, then divide by ${scale}$ to get map centimetres.'
        explanation=f'The scale $1:{scale}$ compares lengths measured in the same unit. '+method+' Reversing map-to-real and real-to-map reverses the scaling operation; do not mix kilometres with centimetres inside the ratio.'
    elif task=='cost_per_100kg':
        kg,cost=F(m['kg']),F(m['cost']);one=cost/kg
        lines=[r'\text{Cost per kg}='+frac(n(cost),n(kg))+f'={n(one)}',r'\text{Cost for 100 kg}='+f'{n(one)}\\times100']
        explanation=f'${n(kg)}$ kg costs N${n(cost)}. Divide cost by mass to get the unit rate, N${n(one)} per kg. Multiply that rate by $100$ kg. Stopping at the price per kilogram does not answer the requested quantity.'
    elif task=='direct_proportion':
        k,t=m['k'],m['m'];one=F(problem.steps[0].value);total=one*k
        lines=[r'\text{Unit cost}='+frac(n(total),k)+f'={n(one)}',r'\text{Requested cost}='+f'{n(one)}\\times{t}']
        explanation=f'${k}$ items cost N${n(total)}, so one item costs N${n(one)}. Assuming the stated fixed unit price, ${t}$ items cost ${t}$ times that unit price. The cost increases in the same proportion as the number of items.'
    elif task=='inverse_proportion':
        workers,hours,new=m['workers'],m['hours'],m['new_hours'];effort=workers*hours
        lines=[r'\text{Worker-hours}='+f'{workers}\\times{hours}={effort}',r'\text{New workers}='+frac(effort,new)]
        explanation=f'The same job needs ${effort}$ worker-hours, from ${workers}$ workers for ${hours}$ hours. The problem assumes equal work rates. Divide that unchanged work by the new ${new}$ hours. Less time requires more workers, not fewer.'
    elif task in ('total_distance','average_speed_two_legs'):
        s1,s2,t1,t2=F(m['s1']),F(m['s2']),F(m['t1']),F(m['t2']);d1,d2=s1*t1,s2*t2
        lines=[f'd_1={n(s1)}\\times{n(t1)}={n(d1)}',f'd_2={n(s2)}\\times{n(t2)}={n(d2)}',r'\text{Total distance}='+f'{n(d1)}+{n(d2)}={n(d1+d2)}']
        explanation=f'$d_1$ and $d_2$ name the distances in the first and second parts, in kilometres. Use distance = speed × time for each part: ${n(s1)}$ km/h for ${n(t1)}$ hours and ${n(s2)}$ km/h for ${n(t2)}$ hours. Add their distances. '
        if task=='average_speed_two_legs':
            lines.extend([r'\text{Total time}='+f'{n(t1)}+{n(t2)}={n(t1+t2)}',r'\text{Average speed}='+frac(n(d1+d2),n(t1+t2))])
            explanation+='For average speed, divide total distance by total time. An unweighted average of the two speeds is not generally correct when their durations differ. Round the final answer to three significant figures.'
    elif task in ('average_speed','speed_unit_conversion'):
        if task=='average_speed':distance=F(m['distance']);time=F(m['hours'])+F(m['minutes'])/60;conversion=f'{m["hours"]}+'+frac(m['minutes'],60)
        else:
            distance=F(m['metres'])/1000;time=F(m['minutes'])/60;conversion=frac(m['minutes'],60)
            lines.append(r'\text{Distance in km}='+frac(m['metres'],1000)+f'={n(distance)}')
        lines.extend([r'\text{Time in hours}='+conversion+f'={n(time)}',r'\text{Average speed in km/h}='+frac(n(distance),n(time))])
        explanation=f'The distance is ${n(distance)}$ km and the duration ${n(time)}$ hours after converting the supplied units. Divide distance by time for speed. Minutes are sixtieths of an hour, not hundredths; convert metres to kilometres using $1000$ metres per kilometre. Keep full precision before the requested final rounding.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
