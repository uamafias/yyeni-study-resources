"""Real numbers and directed arithmetic: syllabus pp.9–10; Basics PDF pp.3–4."""
from math import isqrt,gcd
import re
from .number_teaching import F,n,frac,work,math_spans

CLASS_LABELS={1:'Identifying numbers with a given property',2:'Classifying rational, irrational and non-real numbers',
              3:'Writing prime factorisations',4:'Finding highest common factors and lowest common multiples',
              5:'Place value, number words and prime numbers'}
DIRECTED_LABELS={1:'Finding a temperature rise or fall',2:'Applying a change to a temperature',
                 3:'Comparing negative numbers',4:'Calculating with signed numbers',5:'Following changes in balances and positions'}


def factors(value):
    parts=[];p=2
    while p*p<=value:
        count=0
        while value%p==0:value//=p;count+=1
        if count:parts.append((p,count))
        p+=1
    if value>1:parts.append((value,1))
    return parts


def factor_tex(value):
    return r'\times'.join(f'{p}^{{{e}}}' if e>1 else str(p) for p,e in factors(value)) or '1'


def classification(problem):
    m=problem.machine;task=m['task'];lines=[]
    if task=='pick_from_list':
        value=int(m['answer']);kind=m['kind']
        if kind in ('square','cube'):
            power=2 if kind=='square' else 3;root=isqrt(value) if power==2 else round(value**(1/3))
            lines=[f'{root}^{power}={value}']
            explanation=f'The requested {kind} number is the result of multiplying a whole number by itself '+('twice.' if power==3 else 'once.')
            explanation+=f' Here ${root}^{power}={value}$, so ${value}$ has the requested property.'
        elif kind=='prime':
            primes=[p for p in range(2,isqrt(value)+1) if len(factors(p))==1 and factors(p)[0]==(p,1)]
            lines=[f'\\sqrt{{{value}}}<{isqrt(value)+1}',r'\text{No prime divisor up to }'+str(isqrt(value))]
            explanation=(f'A prime number is an integer greater than $1$ with only two positive divisors, $1$ and itself. '
                         f'For ${value}$ it is enough to test the primes '+', '.join(f'${p}$' for p in primes)
                         +f' up to its square root. None divides ${value}$ exactly; the other list entries fail the requested property.')
        elif kind=='multiple':
            divisor=int(re.search(r'multiple of (\d+)',problem.question)[1])
            lines=[f'{divisor}\\times{value//divisor}={value}']
            explanation=f'A multiple of ${divisor}$ is ${divisor}$ times an integer. Here ${value}={divisor}\\times{value//divisor}$ with no remainder.'
        else:
            lines=[f'{value}<0',f'{value}\\in\\mathbb{{Z}}']
            explanation=f'${value}$ is negative and has no fractional part, so it is a negative integer. A negative decimal with a nonzero fractional part is not an integer.'
    elif task=='classify_number':
        original=m['expression'];kind=m['kind'];roots=[int(x) for x in re.findall(r'\\sqrt\{(-?\d+)\}',original)]
        if kind=='negative_root':
            lines=[f'({roots[0]})<0',r'\text{No real square root}']
            explanation='The square of any real number is nonnegative. The number under this square root is negative, so the expression is non-real; it is not classified as a real irrational number.'
        elif kind=='recurring':
            digit=int(re.search(r'\\dot\{(\d)\}',original)[1])
            lines=[original+'='+frac(digit,9)]
            explanation=f'The dot means the digit ${digit}$ repeats indefinitely. This decimal equals ${frac(digit,9)}$, a ratio of integers, so it is rational.'
        elif kind in ('root','sum'):
            value=roots[0];r=isqrt(value)
            if r*r==value:
                lines=[original+f'={r}={frac(r,1)}']
                explanation=f'${value}={r}^2$ is a perfect square. Its square root is the integer ${r}$, which can be written as a ratio of integers, so it is rational.'
            else:
                if kind=='sum':lines=[original+f'=2\\sqrt{{{value}}}']
                lines.append(f'{r}^2<{value}<({r+1})^2')
                explanation=(f'${value}$ is not a perfect square. Its square root is irrational. '
                             +('Adding the two identical roots gives twice the same irrational root, which is still irrational.' if kind=='sum' else 'A non-repeating, non-terminating square root cannot be written as a ratio of integers.'))
        elif kind=='two_roots':
            a,b=roots;product=a*b;r=isqrt(product);lines=[original+f'=\\sqrt{{{product}}}']
            if r*r==product:
                lines.append(f'\\sqrt{{{product}}}={r}')
                explanation=f'Multiply under one square root: ${a}\\times{b}={product}$. This is a perfect square, so the expression simplifies to the integer ${r}$, which is rational.'
            else:
                lines.append(f'{r}^2<{product}<({r+1})^2')
                explanation=f'Multiply under one square root: ${a}\\times{b}={product}$. This is not a perfect square, so its square root remains irrational. Two irrational roots do not always have an irrational product; check the product first.'
        else:
            value={'product':roots[0],'quotient':1,'difference':0}[kind];lines=[original+f'={value}={frac(value,1)}']
            explanation=f'Simplify the entire expression before classifying it. Here it equals ${value}$, which can be written as ${frac(value,1)}$. It is therefore rational even though individual roots in it may be irrational.'
    elif task=='prime_factorisation':
        value=m['n'];running=value
        for p,e in m['factors']:
            for _ in range(e):lines.append(f'{running}\\div{p}={running//p}');running//=p
        lines.append(f'{value}={factor_tex(value)}')
        explanation=f'Start with ${value}$ and divide by prime factors until the remaining quotient is $1$. Count how often each prime occurs; that count becomes its exponent. A list of distinct primes alone would lose repeated factors.'
    elif task in ('hcf','lcm'):
        a,b=m['a'],m['b'];lines=[f'{a}={factor_tex(a)}',f'{b}={factor_tex(b)}']
        label='HCF' if task=='hcf' else 'LCM';result=gcd(a,b) if task=='hcf' else a*b//gcd(a,b)
        lines.append(r'\operatorname{'+label+f'}}({a},{b})={result}')
        explanation=(f'The two numbers are ${a}$ and ${b}$. '+('For the highest common factor, keep only primes present in both factorisations, using the smaller exponent for each.' if task=='hcf' else 'For the lowest common multiple, include every prime present in either factorisation, using the larger exponent for each.')
                     +f' This gives ${result}$. '+('It divides both original numbers.' if task=='hcf' else 'Both original numbers divide it exactly.'))
    elif task=='number_words':
        value=m['n'];parts=[]
        for power in range(len(str(value))-1,-1,-1):
            digit=int(str(value)[-power-1])
            if digit:parts.append(str(digit*10**power))
        lines=[f'{value}='+'+'.join(parts)]
        explanation=f'Place each part of the spoken number in its correct column. Here ${value}$ has the place-value expansion shown. Put zero in any unfilled column so the other digits keep their values.'
    elif task=='place_value':
        number,digit=m['number'],m['digit'];places={'tenth':1,'hundredth':2,'thousandth':3};position=places[m['answer']]
        lines=[f'{number}=\\text{{given decimal}}',f'\\text{{Value of the digit {digit}: }}'+frac(digit,10**position)]
        explanation=f'The first, second and third places after the decimal point are tenths, hundredths and thousandths. In ${number}$ the digit ${digit}$ is in the {m["answer"]} column. The question asks for the column name, not just the digit.'
    elif task=='primes_in_range':
        primes=m['primes'];lines=[r'\text{Primes: }'+', '.join(map(str,primes))]
        explanation=f'Test the integers strictly between ${m["lo"]}$ and ${m["hi"]}$. A prime has exactly two positive divisors. Exclude $1$, even numbers above $2$, and numbers with a smaller prime factor. The qualifying numbers are '+', '.join(f'${p}$' for p in primes)+'.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation


def directed(problem):
    m=problem.machine;task=m['task']
    if task=='temperature_change':
        hi,lo=m['hi'],m['lo'];lines=[r'\text{Size of change}='+f'{hi}-({lo})={hi-lo}']
        explanation=f'The temperatures are ${hi}$ and ${lo}$ degrees Celsius. The question asks how many degrees the temperature changed, so use the positive distance between them: higher minus lower. Crossing zero adds the distances on either side of zero.'
    elif task=='temperature_after_change':
        start,change=m['start'],m['change'];lines=[r'\text{New temperature}='+f'({start})+({change})={start+change}'+r'^\circ\text{C}']
        explanation=f'The starting temperature is ${start}$ degrees Celsius. Represent the stated change by the signed number ${change}$: a rise is positive and a fall negative. Add that change to the starting value; keep a negative sign if the final temperature is below zero.'
    elif task=='compare_negatives':
        a,b=m['left'],m['right'];lines=[f'{a} {m["answer"]} {b}']
        explanation=f'Compare ${a}$ and ${b}$ at matching decimal places, padding with zeros if needed. Among negative numbers, the number closer to zero is greater. The comparison direction is reversed from that of their positive magnitudes.'
    elif task=='directed_arithmetic':
        values=[F(v) for v in m['nums']];ops=list(m['ops']);lines=[];symbols={'+':'+','-':'-', '*':r'\times','/':r'\div'}
        def shown():
            return ''.join(('' if i==0 else symbols[ops[i-1]])+f'({n(v)})' for i,v in enumerate(values))
        lines.append(shown());i=0
        while i<len(ops):
            op=ops[i]
            if op in ('*','/'):
                a,b=values[i:i+2];result=a*b if op=='*' else a/b
                lines.append(f'({n(a)}){symbols[op]}({n(b)})={n(result)}')
                values[i:i+2]=[result];ops.pop(i)
            else:i+=1
        lines.append(shown())
        explanation='Bracketed negative numbers are signed values, not instructions to change the order of operations. Multiply and divide first, working left to right among equal-priority operations. Then add and subtract from left to right. A product or quotient of two negatives is positive; subtracting a negative adds its opposite.'
    elif task=='balance_and_position':
        running=m['start'];lines=[r'\text{Start}='+str(running)]
        for change in m['changes']:
            lines.append(f'({running})+({change})={running+change}');running+=change
        explanation=(f'The starting signed value is ${m["start"]}$. '+('Deposits increase a balance; withdrawals decrease it. A negative balance is an overdraft.' if m['kind']=='bank' else 'Take sea level as zero. Descending decreases the signed position and rising increases it; a negative position is below sea level.')
                     +' Apply each signed change in order, keeping the running total. The final sign is part of the answer.')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
