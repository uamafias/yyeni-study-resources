"""Sequences: NSSCO p.20; local AP/GP notes, limited to existing NSSCO tasks."""
from fractions import Fraction
from .algebra_teaching import frac,num,work
from .formatting import linear_latex

LABELS={1:'Finding the next term from a common difference',2:'Writing the nth-term expression',
        3:'Finding how many terms a progression contains',4:'Finding a progression or its sum',
        5:'Linking arithmetic terms to a geometric progression'}


def content(problem):
    m=problem.machine;task=m['task']
    if task=='ap_to_gp':
        j,k,l=m['j'],m['k'],m['l'];J,K,L=j-1,k-1,l-1;u=Fraction(*m['a_over_d']);r=Fraction(*m['ratio'])
        first,middle,last=f'a+({J})d',f'a+({K})d',f'a+({L})d'
        net=2*K-J-L;constant=J*L-K*K
        lines=[f'T_{{{j}}}={first},\\quad T_{{{k}}}={middle},\\quad T_{{{l}}}={last}',
               f'({middle})^2=({first})({last})',
               f'a^2+({2*K})ad+({K*K})d^2=a^2+({J+L})ad+({J*L})d^2',
               f'({net})ad=({constant})d^2',f'a=({num(u)})d',
               'r='+frac(f'({num(u+K)})d',f'({num(u+J)})d')+f'={num(r)}']
        explanation=(f'$a$ is the first arithmetic term, $d$ its nonzero common difference, and $T_n$ the term at position $n$. '
                     f'Here the selected positions are ${j}$, ${k}$ and ${l}$, so their terms are ${first}$, ${middle}$ and ${last}$. '
                     'For three nonzero geometric terms, the middle term squared equals the product of its neighbours. '
                     f'Expanding and cancelling gives $a=({num(u)})d$; this is a relationship, not a numerical value for $a$ or $d$. '
                     f'$r$ is the geometric common ratio: divide the second selected term by the first. The factor $d$ cancels because $d\\ne0$, giving $r={num(r)}$.')
    else:
        a,d=m['a'],m['d'];prefix=f'$a$ is the first term, here ${a}$; $d$ is the common difference, here ${d}$. '
        if task=='next_term':
            last=a+3*d
            lines=[f'd=({a+d})-({a})={d}',f'T_5=({last})+({d})']
            explanation=(prefix+f'The four displayed terms change by ${d}$ each time. Add that signed difference to '
                         f'the last shown term, ${last}$, to find the fifth term $T_5$. Do not add two neighbouring terms together.')
        elif task=='nth_term':
            lines=[f'd=({a+d})-({a})={d}',f'T_n=a+(n-1)d={a}+(n-1)({d})',f'T_n={linear_latex(d,a-d,"n")}',f'T_1={a}']
            explanation=(prefix+'$n$ is the position number, starting at $1$, and $T_n$ is the value at that position. '
                         f'From the first term there are $n-1$ changes, so $T_n={a}+(n-1)({d})$. '
                         f'Collecting terms gives ${linear_latex(d,a-d,"n")}$. '
                         +('In this context, this expression gives the amount or charge for position $n$ in Namibian dollars. ' if m['context'] else '')
                         +'Check at $n=1$ and $n=2$. The requested result is a formula for any position, not just the next term.')
        elif task in ('number_of_terms','ap_sum'):
            n=m['n'];last=a+(n-1)*d
            lines=[f'{last}={a}+(n-1)({d})',f'n-1='+frac(last-a,d)+f'={n-1}',f'n={n}']
            explanation=(prefix+f'$n$ is the number of terms and the final term is ${last}$. '
                         f'Use $T_n=a+(n-1)d$: the difference ${last-a}$ counts ${n-1}$ gaps of size ${d}$. '
                         'Add one to the number of gaps to count the terms themselves. ')
            if task=='ap_sum':
                lines.extend(['S_n='+frac('n(a+T_n)',2),f'S_{{{n}}}='+frac(f'{n}({a}+{last})',2)])
                explanation+=f'$S_n$ is the sum of the first $n$ terms. Pair the first and last terms, whose sum is ${a+last}$; '
                explanation+=f'multiplying by $n/2={n}/2$ gives the total. The question asks for the sum, so finding $n$ alone is not the final answer.'
        elif task=='ap_a_and_d':
            j,k=m['j'],m['k'];tj=a+(j-1)*d;tk=a+(k-1)*d
            lines=[f'a+{j-1}d={tj}',f'a+{k-1}d={tk}',f'{k-j}d={tk}-({tj})={tk-tj}',
                   f'd='+frac(tk-tj,k-j)+f'={d}',f'a={tj}-({j-1})({d})={a}']
            explanation=('$a$ is the unknown first term and $d$ the unknown common difference. '
                         f'The given terms are $T_{{{j}}}={tj}$ and $T_{{{k}}}={tk}$. '
                         f'Write each using $T_n=a+(n-1)d$. Subtract the equations to cancel $a$: there are ${k-j}$ gaps '
                         f'between the given positions. This gives $d={d}$. Substitute back to get $a={a}$ and check both given terms.')
        else:raise ValueError(task)
    return work(lines,problem.answer),explanation
