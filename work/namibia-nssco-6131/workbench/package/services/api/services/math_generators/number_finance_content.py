"""Percentages and household finance: NSSCO pp.10,12; Basics commercial arithmetic."""
import re
from .number_teaching import F,n,frac,work

PERCENT_LABELS={1:'Applying percentage increases, decreases and remainders',2:'Calculating percentage profit or loss',
                3:'Finding an original amount from a changed amount',4:'Calculating percentage change and proportions',
                5:'Compound growth, interest and depreciation'}
FINANCE_LABELS={1:'Finding costs and change',2:'Calculating simple interest',3:'Converting currencies using a given rate',
                4:'Finding an unknown in simple interest',5:'Calculating compound amounts and interest'}
INCOME_LABELS={1:'Combining wages and commission',2:'Calculating a bill from meter readings',3:'Using a fictional income-tax table'}


def compound(problem):
    m=problem.machine
    personal='p' in m
    principal=F(m['p'] if personal else m['principal']);rate=F(m['r'] if personal else m['rate']);years=m['n'] if personal else m['years']
    depreciation=m.get('task')=='depreciation';interest=(m.get('ask')=='interest earned') if personal else m['task']=='compound_interest'
    multiplier=1+(-rate if depreciation else rate)/100;amount=principal*multiplier**years
    sign='-' if depreciation else '+'
    lines=[f'P={n(principal)},\\quad r={n(rate)},\\quad t={years}',
           f'M=1{sign}'+frac(n(rate),100)+f'={n(multiplier)}',f'A=P M^t={n(principal)}({n(multiplier)})^{{{years}}}']
    if interest:lines.append(f'I=A-P={n(principal)}({n(multiplier)})^{{{years}}}-{n(principal)}')
    explanation=(f'$P$ is the starting amount, N${n(principal)}; $r$ is the annual percentage rate, ${n(rate)}$; '
                 f'$t={years}$ is the number of years. $M={n(multiplier)}$ is the multiplier for one year and $A$ the final amount. '
                 +('A fall in value uses $1-r/100$, not a growth multiplier. ' if depreciation else 'Each year earns interest on the updated balance, not just the initial investment. ')
                 +f'Apply the same multiplier ${years}$ times. '
                 +('$I$ is the interest alone, so subtract the original amount $P$ from the final amount $A$. ' if interest else 'The requested amount includes the original investment or asset value. ')
                 +'Keep full precision throughout and round the final money answer to two decimal places.')
    return work(lines,problem.answer),explanation


def percentages(problem):
    m=problem.machine;task=m['task']
    if task in ('compound_amount','compound_interest','depreciation'):return compound(problem)
    if task in ('increase','decrease','percentage_remaining'):
        amount=m['total'] if task=='percentage_remaining' else m['amount'];pct=m['percent'];change=F(amount)*pct/100
        add=task=='increase';sign='+' if add else '-';result=amount+change if add else amount-change
        lines=[r'\text{Percentage part}='+frac(pct,100)+f'\\times{amount}={n(change)}',
               r'\text{Requested amount}='+f'{amount}{sign}{n(change)}={n(result)}']
        explanation=(f'The original whole is ${amount}$ and the percentage is ${pct}\\%$. Find that percentage of the original amount first. '
                     +('Add the change for an increase.' if add else 'Subtract the change for a decrease or to find what remains.')
                     +' Read whether the question wants the change itself or the final amount; these are different quantities.')
    elif task in ('profit','loss'):
        cost,selling=m['cost'],m['selling'];change=abs(selling-cost)
        lines=[r'\text{'+task+'}='+f'{max(cost,selling)}-{min(cost,selling)}={change}',
               r'\text{Percentage '+task+'}='+frac(change,cost)+r'\times100']
        explanation=f'The cost price is N${cost} and selling price N${selling}. The {task} is N${change}. Express it as a percentage of the cost price, which is the original investment in the item. Using the selling price as denominator answers a different question. Keep precision and round the requested percentage to three significant figures.'
    elif task in ('reverse_increase','reverse_decrease'):
        given=F(m['given']);p=m['percent'];multiplier=1+(F(p) if task=='reverse_increase' else -F(p))/100;sign='+' if task=='reverse_increase' else '-'
        lines=[f'M=1{sign}'+frac(p,100)+f'={n(multiplier)}',f'Mx={n(given)}',f'x='+frac(n(given),n(multiplier))]
        explanation=f'$x$ is the original amount. $M={n(multiplier)}$ is the multiplier for the stated ${p}\\%$ '+('increase' if task=='reverse_increase' else 'reduction')+f'. The given N${n(given)} is the changed amount, so divide it by $M$ to recover $x$. Applying the opposite percentage to the changed amount would use the wrong whole.'
    elif task in ('percentage_increase','percentage_decrease'):
        old,new=m['old'],m['new'];change=abs(new-old)
        lines=[r'\text{Size of change}='+f'{max(old,new)}-{min(old,new)}={change}',r'\text{Percentage change}='+frac(change,old)+r'\times100']
        explanation=f'The original amount is ${old}$ and the new amount is ${new}$. The size of the change is ${change}$. Divide by the original ${old}$, then multiply by $100$. State whether this is an increase or decrease, and round only the final percentage as requested.'
    elif task=='express_as_percentage':
        part,whole=m['part'],m['whole'];lines=[r'\text{Percentage}='+frac(part,whole)+r'\times100']
        explanation=f'The part is ${part}$ out of a whole of ${whole}$. Use part ÷ whole × $100$, then round to three significant figures. Keep the denominator as the total available, not the amount missing from it.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation


def finance(problem):
    m=problem.machine;task=m['task']
    if task=='compound_interest':return compound(problem)
    if task=='change':
        a,b,pa,pb,paid=m['na'],m['nb'],F(m['pa']),F(m['pb']),m['paid'];total=a*pa+b*pb
        lines=[r'\text{First cost}='+f'{a}\\times{n(pa)}={n(a*pa)}',r'\text{Second cost}='+f'{b}\\times{n(pb)}={n(b*pb)}',
               r'\text{Total cost}='+f'{n(a*pa)}+{n(b*pb)}={n(total)}',r'\text{Change}='+f'{paid}-{n(total)}={n(paid-total)}']
        explanation=f'All amounts here are in Namibian dollars. The two quantities are ${a}$ and ${b}$, at unit prices N${n(pa)} and N${n(pb)}. Multiply each quantity by its own price, add the costs, then subtract that total from N${paid} paid. The change is the amount returned, not the purchase total.'
    elif task=='currency':
        amount,rate=F(m['amount']),F(m['rate']);divide=m['to_foreign']
        operation=frac(n(amount),n(rate)) if divide else f'{n(amount)}\\times{n(rate)}'
        lines=[r'1\text{ foreign unit}='+f'{n(rate)}\\text{{ Namibian dollars}}',r'\text{Converted amount}='+operation]
        explanation=f'The supplied exercise rate is N${n(rate)} for one foreign currency unit. '+(f'The given N${n(amount)} must be divided by ${n(rate)}$ to count foreign units.' if divide else f'There are ${n(amount)}$ foreign units, so multiply by ${n(rate)}$ Namibian dollars per unit.')+' Use the rate stated in this question and round the final money answer to two decimal places.'
    elif task in ('simple_interest','rate','principal','time'):
        p,r,t=F(m['p']),F(m['r']),F(m['t']);interest=p*r*t/100
        lines=['I='+frac('Prt',100)]
        if task=='simple_interest':
            months=re.search(r'(\d+) months',problem.question)
            if months:lines.append('t='+frac(months[1],12)+f'={n(t)}\\text{{ years}}')
            else:lines.append(f't={n(t)}\\text{{ years}}')
            lines.extend(['I='+frac(f'{n(p)}\\times{n(r)}\\times{n(t)}',100)])
            known=f'$P={n(p)}$, $r={n(r)}$ and $t={n(t)}$.'
            method='Simple interest is based on the original principal in every year. The question asks for interest alone, so do not add the principal to it.'
        elif task=='rate':
            amount=F(m['amount']);lines.extend([f'I={n(amount)}-{n(p)}={n(interest)}','r='+frac(f'{n(interest)}\\times100',f'{n(p)}\\times{n(t)}')])
            known=f'$P={n(p)}$, $t={n(t)}$ and the final amount is N${n(amount)}.';method='Subtract the principal from the final amount to find interest, then solve the simple-interest formula for the annual percentage rate.'
        elif task=='principal':
            lines.extend([f'I={n(interest)},\\quad r={n(r)},\\quad t={n(t)}','P='+frac(f'{n(interest)}\\times100',f'{n(r)}\\times{n(t)}')])
            known=f'$I={n(interest)}$, $r={n(r)}$ and $t={n(t)}$.';method='The question supplies the interest, not the final amount. Rearrange the formula to divide interest × $100$ by rate × time.'
        else:
            amount=F(m['amount']);lines.extend([f'I={n(amount)}-{n(p)}={n(interest)}','t='+frac(f'{n(interest)}\\times100',f'{n(p)}\\times{n(r)}')])
            known=f'$P={n(p)}$, $r={n(r)}$ and the final amount is N${n(amount)}.';method='Find the interest by subtracting the principal, then divide interest × $100$ by principal × annual percentage rate.'
        explanation='$I$ is simple interest in Namibian dollars, $P$ the original investment, $r$ the numerical annual percentage rate and $t$ time in years. Here '+known+' '+method+' Convert months to a fraction of a year before using an annual rate.'
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation


def income(problem):
    m=problem.machine;skill=problem.skill
    if skill=='wages_commission':
        h,r,s,p=m['hours'],m['rate'],m['sales'],m['pct'];wages=h*r;commission=F(s)*p/100
        lines=[r'\text{Wages}='+f'{h}\\times{r}={wages}',r'\text{Commission}='+frac(p,100)+f'\\times{s}={n(commission)}',r'\text{Total earnings}='+f'{wages}+{n(commission)}']
        explanation=f'The worker earns N${r} for each of ${h}$ hours, plus ${p}\\%$ of N${s} sales. Calculate hourly pay and commission separately, then add them. Commission is a percentage of sales, not of the hourly wage.'
    elif skill=='meter_bill':
        old,current,charge,fixed=(m[k] for k in ('previous','current','charge','fixed'));used=current-old
        lines=[r'\text{Units used}='+f'{current}-{old}={used}',r'\text{Usage charge}='+f'{used}\\times{charge}={used*charge}',r'\text{Bill}='+f'{used*charge}+{fixed}']
        explanation=f'The previous meter reading is ${old}$ and the current reading ${current}$. Their difference, ${used}$, is the number of units used. Multiply by N${charge} per unit, then add the fixed charge of N${fixed} once. A meter reading is cumulative; it is not itself this bill’s consumption.'
    elif skill=='fictional_tax_table':
        threshold,earned,rate,base=(m[k] for k in ('threshold','income','pct','base'));excess=earned-threshold
        lines=[r'\text{Income above threshold}='+f'{earned}-{threshold}={excess}',r'\text{Tax on excess}='+frac(rate,100)+f'\\times{excess}={n(F(excess)*rate/100)}',r'\text{Total tax}='+f'{base}+{n(F(excess)*rate/100)}']
        explanation=f'Use only the fictional table supplied in this exercise. Annual income is N${earned}, the threshold N${threshold}, and the fixed base tax N${base}. The ${rate}\\%$ marginal rate applies only to the N${excess} above the threshold. Add that tax to the base tax; applying the rate to all income would overcharge this exercise taxpayer.'
    else:raise ValueError(skill)
    return work(lines,problem.answer),explanation
