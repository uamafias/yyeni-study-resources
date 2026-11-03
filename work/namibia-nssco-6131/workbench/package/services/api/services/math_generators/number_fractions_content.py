"""Fractions, decimals, percentages: NSSCO p.10; Basics PDF pp.4–6."""
from fractions import Fraction
from math import lcm,gcd
import re
from .number_teaching import F,n,frac,work,math_spans
from .formatting import number_latex

LABELS={1:'Converting fractions, decimals and percentages',2:'Equivalent fractions, mixed numbers and recurring decimals',
        3:'Ordering and comparing numbers in different forms',4:'Calculating with fractions and mixed numbers',
        5:'Finding a whole and applying successive fractions'}


def content(problem):
    m=problem.machine;task=m['task'];lines=[]
    if task=='fraction_to_decimal':
        a,b=m['n'],m['d'];lines=[frac(a,b)+f'={a}\\div{b}={m["answer"]}']
        explanation=f'The numerator is ${a}$ and the denominator is ${b}$. A fraction means numerator divided by denominator. This decimal terminates, so keep its exact value rather than rounding it.'
    elif task=='decimal_to_fraction':
        text=m['decimal'];places=len(text.split('.')[1]);den=10**places;top=int(F(text)*den);g=gcd(top,den)
        lines=[text+'='+frac(top,den)+'='+number_latex(F(text))]
        explanation=f'The decimal ${text}$ has ${places}$ places after the point, so write it over ${den}$. Divide numerator ${top}$ and denominator ${den}$ by their highest common factor, ${g}$, to get the simplest fraction.'
    elif task=='fraction_to_percentage':
        a,b=m['n'],m['d'];lines=[frac(a,b)+r'\times100'+f'={n(F(a)/b*100)}',r'\text{Percentage}='+f'{m["answer"]}\\%']
        explanation=f'The fraction is ${frac(a,b)}$. A percentage counts parts per hundred: multiply the fraction by $100$, then attach the percent sign. Do not multiply or divide by $100$ a second time.'
    elif task=='percentage_to_fraction':
        p=m['percent'];value=F(p)/100;lines=[f'{p}\\%='+frac(p,100)+'='+number_latex(value)]
        explanation=f'Percent means “out of one hundred”, so ${p}\\%$ is ${frac(p,100)}$. Simplify numerator and denominator by the same common factor. The final fraction no longer carries a percent sign.'
    elif task=='improper_to_mixed':
        a,b=m['n'],m['d'];whole,rest=divmod(a,b);lines=[f'{a}={whole}\\times{b}+{rest}',frac(a,b)+f'={whole}+'+frac(rest,b)]
        explanation=f'Dividing ${a}$ by ${b}$ gives ${whole}$ whole units and a remainder of ${rest}$. The remainder is still in ${b}$ths. Write the whole number and that fraction together; this notation means addition, not multiplication.'
    elif task=='equivalent_fraction':
        a,b,big=m['a'],m['b'],m['big'];scale=big//b
        lines=[frac(big,b)+f'={scale}',frac(a,b)+'='+frac(f'{a}\\times{scale}',f'{b}\\times{scale}')+'='+frac(a*scale,big)]
        explanation=f'The denominator changes from ${b}$ to ${big}$ by multiplying by ${scale}$. Multiply the numerator ${a}$ by that same ${scale}$ so the value of the fraction stays unchanged. The missing number is the new numerator.'
    elif task=='fraction_of_quantity':
        q,a,b=m['quantity'],m['n'],m['d'];one=F(q)/b
        lines=[f'{q}\\div{b}={n(one)}',frac(a,b)+f'\\times{q}={a}\\times{n(one)}={n(one*a)}']
        explanation=f'The whole quantity is ${q}$. Dividing by denominator ${b}$ gives one equal part, ${n(one)}$. The numerator ${a}$ tells us to take ${a}$ of these parts. Keep the item being counted clear in the answer.'
    elif task=='recurring_to_fraction':
        digits=re.findall(r'\\dot\{(\d)\}',m['shown']);block=int(''.join(digits));scale=10**len(digits)
        lines=[f'x={m["shown"]}',f'{scale}x={block}+x',f'({scale}-1)x={block}',f'x='+frac(block,scale-1)]
        explanation=f'Let $x$ name the entire recurring decimal ${m["shown"]}$. Its repeating block has ${len(digits)}$ digits, so multiplying by ${scale}$ lines up the recurring tails. Subtract the original $x$ to cancel those tails, then divide by ${scale-1}$ and simplify. A terminating decimal would use a power-of-ten denominator instead.'
    elif task=='order_fractions':
        values=[F(x) for x in m['shown']];den=lcm(*(x.denominator for x in values))
        lines=[number_latex(v)+'='+frac(v.numerator*(den//v.denominator),den) for v in values]
        lines.append(' < '.join(number_latex(F(v)) for v in m['ascending']))
        explanation=f'The common denominator is ${den}$. Rewrite each fraction with that denominator; then compare the numerators. The question asks for smallest first, so list the original fractions in ascending order. Comparing only original numerators or denominators would not compare equal-sized parts.'
    elif task in ('pick_smallest','pick_largest'):
        values=[]
        for item in m['items']:
            value=F(item.rstrip('%'))/(100 if item.endswith('%') else 1);values.append(value)
            original=item.replace('%',r'\%') if '/' not in item else number_latex(F(item))
            lines.append(original+'='+n(value))
        which='smallest' if task=='pick_smallest' else 'largest'
        lines.append(r'\text{'+which+r' value}='+n(min(values) if which=='smallest' else max(values)))
        explanation=f'Put every item on the same scale. Divide percentages by $100$; convert terminating fractions to exact decimals and retain exact fractions when they recur. Compare these values and select the {which}. Give the selected item in its original displayed form.'
    elif task=='compare_with_symbol':
        a,b=problem.steps[0].value.split(' and ');lines=[f'{a} {m["symbol"]} {b}']
        explanation=f'Convert both sides to the same form before choosing a sign. Here the values are ${a}$ and ${b}$. Match decimal places and remember that a negative number farther below zero is smaller. The open side of $>$ or $<$ faces the larger number.'
    elif task in ('fraction_add','fraction_sub','fraction_mul','fraction_div'):
        a,b=F(m['x']),F(m['y']);op=task.split('_')[1]
        sign={'add':'+','sub':'-','mul':r'\times','div':r'\div'}[op]
        original=number_latex(a)+sign+number_latex(b)
        if op in ('add','sub'):
            den=lcm(a.denominator,b.denominator);A=a.numerator*(den//a.denominator);B=b.numerator*(den//b.denominator)
            result=a+b if op=='add' else a-b
            lines=[original+'='+frac(A,den)+sign+frac(B,den),frac(f'{A}{sign}{B}',den)+'='+number_latex(result)]
            method=f'Use the common denominator ${den}$, scale each numerator accordingly, then '+('add' if op=='add' else 'subtract')+' the numerators. The denominator stays the same.'
        elif op=='mul':
            lines=[original+'='+frac(f'{a.numerator}\\times{b.numerator}',f'{a.denominator}\\times{b.denominator}')+'='+number_latex(a*b)]
            method='Multiply the numerators together and multiply the denominators together. Cancel common factors before or after multiplying.'
        else:
            lines=[original+'='+number_latex(a)+r'\times'+number_latex(1/b),number_latex(a)+r'\times'+number_latex(1/b)+'='+number_latex(a/b)]
            method='Replace division by multiplication by the reciprocal of the second fraction. Leave the first fraction unchanged, then multiply and simplify.'
        explanation='First convert every mixed number to an improper fraction: whole × denominator + numerator, over the original denominator. '+method+' Use the requested mixed-number or simplest-fraction form for the final answer.'
    elif task=='whole_from_fraction':
        part,a,b=m['part'],m['n'],m['d'];one=F(part)/a
        lines=[f'{a}\\text{{ parts}}={part}',f'1\\text{{ part}}='+frac(part,a)+f'={n(one)}',r'\text{Whole}='+f'{b}\\times{n(one)}={n(b*one)}']
        explanation=f'The known amount ${part}$ represents ${a}$ of the ${b}$ equal parts of the whole. Divide by ${a}$ to find one part, then multiply by ${b}$ to reconstruct the whole. Taking the same fraction of the known part would make it smaller instead.'
    elif task=='successive_fractions':
        total,a,b,c,d=(m[k] for k in ('total','a','b','c','d'));first=F(total)*a/b;remaining=total-first;second=remaining*c/d;left=remaining-second
        lines=[r'\text{First share}='+frac(a,b)+f'\\times{total}={n(first)}',r'\text{Remaining}='+f'{total}-{n(first)}={n(remaining)}',
               r'\text{Second share}='+frac(c,d)+f'\\times{n(remaining)}={n(second)}',r'\text{Left}='+f'{n(remaining)}-{n(second)}={n(left)}']
        if m.get('ask')=='percentage':lines.append(r'\text{Percentage left}='+frac(n(left),total)+r'\times100')
        explanation=f'The original whole is ${total}$. The first fraction ${frac(a,b)}$ applies to this whole, leaving ${n(remaining)}$. The second fraction ${frac(c,d)}$ applies only to that remainder, giving a second share of ${n(second)}$. Subtract it to leave ${n(left)}. '+('For the requested percentage, divide the amount left by the original whole, not by the remainder, and multiply by $100$. Round only at the end.' if m.get('ask')=='percentage' else 'The two fractions refer to different wholes, so do not add them as if both were fractions of the original total.')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
