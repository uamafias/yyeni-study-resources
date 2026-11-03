"""Actual-data statistics and event-specific probability working for fixed examples."""
from collections import Counter
from itertools import accumulate
from .topic_teaching import *

LABELS={
'nssco_mean_median_mode_range':{1:'Mode, median and range of a short list',2:'Mean and ordered-list statistics',3:'Finding a missing value from a mean',4:'Using totals when a mean changes'},
'nssco_grouped_data_mean':{1:'Identifying a modal class',2:'Median classes and grouped percentages',3:'Estimating a grouped mean',4:'Grouped means with unequal class widths',5:'Recovering frequencies from densities before estimating a mean'},
'nssco_simple_probability':{1:'Counting favourable objects',2:'Number properties and repeated letters',3:'Events in a two-way table',4:'Complements and expected frequency',5:'Equally likely two-dice outcomes'},
'nssco_tree_diagrams':{1:'Independent pass and fail events',2:'Two draws without replacement',3:'Both orders and at least one in two draws',4:'Three draws without replacement',5:'Combining conditional routes'},
'nssco_cumulative_frequency_reading':{1:'Building a running total',2:'Recovering frequencies by subtraction',3:'Counts above, below or between boundaries',4:'Median class and interquartile range'},
}


def class_tex(bounds,var):return f'{bounds[0]}\\le {var}<{bounds[1]}'


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];gid=p.generator_id;lines=[]
    if gid=='nssco_mean_median_mode_range':
        if 'values' in m:
            values=m['values'];ordered=sorted(values);N=len(values);lines=[label('In ascending order')+': '+', '.join(map(str,ordered))]
            if t=='mean':lines+=['T='+'+'.join(map(str,values))+f'={sum(values)}',r'\bar x='+frac('T','N')+'='+frac(sum(values),N)];method='Mean adds all N observations, then divides that total T by N. Repeated values count each time they occur.'
            elif t=='median':
                if N%2:lines.append(label('Median')+f'=x_{{{(N+1)//2}}}={ordered[N//2]}')
                else:lines.append(label('Median')+'='+frac(f'{ordered[N//2-1]}+{ordered[N//2]}',2))
                method='Median is the middle value of the sorted list. For even N, average the two central observations; do not average the largest and smallest or use an unsorted position.'
            elif t=='mode':
                common=Counter(values).most_common(1)[0];lines.append(label('Most frequent value')+f'={common[0]},\\quad '+label('frequency')+f'={common[1]}');method='Mode is the value occurring most often, not its frequency or its position in the list.'
            else:lines.append(label('Range')+f'={max(values)}-{min(values)}');method='Range is maximum minus minimum. Sorting makes those endpoints clear; counting the number of observations does not measure spread.'
            e=f'There are $N={N}$ observations. '+method+' Preserve the question’s data units, and use the requested accuracy for any final decimal.'
        elif t=='missing_value':
            known=m['known'];N=len(known)+1;mean=m['mean'];total=N*mean
            lines=[f'T=N\\bar x={N}({mean})={total}',label('Known total')+'='+'+'.join(map(str,known))+f'={sum(known)}',f'x={total}-{sum(known)}']
            e=f'$x$ is the missing observation. The complete list contains $N={N}$ numbers and has mean ${mean}$. Recover its total T as N times mean, then subtract the sum of the ${len(known)}$ known values. Do not take the mean of only the known observations.'
        else:
            a,b=m['n_before'],m['n_after'];u,v=F(m['mean_before']),F(m['mean_after']);lines=[f'T_{{old}}={a}({q(u)})={q(a*u)}',f'T_{{new}}={b}({q(v)})={q(b*v)}',f'x=T_{{new}}-T_{{old}}={q(b*v)}-{q(a*u)}']
            e=f'The old group has ${a}$ observations with mean ${q(u)}$; the new group has ${b}$ with mean ${q(v)}$. $T_{{old}}$ and $T_{{new}}$ name their totals. Multiply each mean by its own group size before subtracting to recover the added observation x. A difference between means alone is not the new observation.'
    elif gid=='nssco_grouped_data_mean':
        classes,freqs=m['classes'],m['freqs'];N=sum(freqs);cum=list(accumulate(freqs));var=m['var']
        if t=='modal_class':
            i=freqs.index(max(freqs));lines=[label('Largest frequency')+f'={freqs[i]}',class_tex(classes[i],var)]
            e=f'The class frequencies are ${", ".join(map(str,freqs))}$. The modal class is the interval with the largest frequency, here ${freqs[i]}$. Give its full interval ${class_tex(classes[i],var)}$, not a midpoint or the frequency itself. These are the supplied frequency counts, not histogram densities.'
        elif t=='median_class':
            position=F(N+1)/2;i=next(i for i,c in enumerate(cum) if c>=position);lines=[f'N={N}',label('Median position')+'='+frac(f'{N}+1',2),label('Cumulative frequencies')+': '+', '.join(map(str,cum)),class_tex(classes[i],var)]
            e=f'There are ${N}$ observations. Locate middle position ${q(position)}$ in the cumulative counts: the first class whose cumulative frequency reaches it contains the median. Give that class interval, rather than pretending the unknown individual median equals the midpoint.'
        elif t=='percentage_at_least':
            boundary=m['boundary'];selected=[f for bounds,f in zip(classes,freqs) if bounds[0]>=boundary];count=sum(selected);lines=[label('Count at or above boundary')+'='+'+'.join(map(str,selected))+f'={count}',label('Percentage')+'='+frac(count,N)+r'\times100']
            e=f'The threshold is ${boundary}$ for variable ${var}$. Include all classes whose lower boundary is at least this threshold. Their combined count is ${count}$ out of all ${N}$. Divide by the total frequency and multiply by 100; a percentage denominator is not the number of classes.'
        else:
            mids=[F(a+b)/2 for a,b in classes];products=[F(f)*x for f,x in zip(freqs,mids)];total=sum(products)
            if 'densities' in m:
                for i,((a,b),d) in enumerate(zip(classes,m['densities'])):lines.append(f'f_{{{i+1}}}=({q(F(d))})({b}-{a})={freqs[i]}')
            for i,((a,b),x,f,fx) in enumerate(zip(classes,mids,freqs,products)):lines.append(f'x_{{{i+1}}}='+frac(f'{a}+{b}',2)+f'={q(x)},\\quad f_{{{i+1}}}x_{{{i+1}}}={f}({q(x)})={q(fx)}')
            lines += [r'\sum f='+str(N),r'\sum fx='+q(total),r'\bar x\approx'+frac(q(total),N)]
            e=f'Each $x_i$ is the midpoint of class i and $f_i$ its frequency. Use those midpoints as representative values, multiply each by its own frequency, then divide total $\\sum fx={q(total)}$ by $\\sum f={N}$. '+('The given heights are densities, so first recover each frequency as density times class width. ' if 'densities' in m else '')+'This is an estimate because the individual observations within each class are unknown. Unequal widths change midpoint/density calculations; they do not change the frequency-weighted mean formula. Round only the final estimate.'
    elif gid=='nssco_cumulative_frequency_reading':
        if t=='iqr':
            lo,hi=m['lq'],m['uq'];lines=[f'IQR=Q_3-Q_1={hi}-{lo}'];e=f'The lower quartile is $Q_1={lo}$ and upper quartile $Q_3={hi}$. Their difference is the interquartile range, the spread of the middle half of the data. The median is not needed for this subtraction; do not confuse IQR with maximum minus minimum.'
        else:
            freqs,cum=m['freqs'],m['cum'];N=sum(freqs)
            if t=='complete_cumulative':
                for i,f in enumerate(freqs):lines.append(f'F_{{{i+1}}}='+('0' if i==0 else str(cum[i-1]))+f'+{f}={cum[i]}')
                e=f'$F_i$ is the cumulative frequency through class i. Add the next class count to the running total, preserving class order. The final total is ${N}$; cumulative counts cannot decrease and are not the same as the separate class frequencies.'
            elif t=='frequencies_from_cumulative':
                for i,Fc in enumerate(cum):lines.append(f'f_{{{i+1}}}={Fc}-'+('0' if i==0 else str(cum[i-1]))+f'={freqs[i]}')
                e=f'The final cumulative count is ${N}$. Recover each class frequency $f_i$ by subtracting the preceding cumulative total from the current one; use zero before the first class. The resulting separate frequencies sum to ${N}$. Do not add the cumulative totals together.'
            elif t=='median_class':
                position=F(p.steps[0].value);i=next(i for i,c in enumerate(cum) if c>=position);lines=[label('Median position')+'='+q(position),label('Cumulative counts')+': '+', '.join(map(str,cum)),class_tex(m['classes'][i],m['var'])]
                e=f'The table contains ${N}$ observations. The requested grouped median position is ${q(position)}$. Find the first cumulative count that reaches that position and report its class interval. This identifies a class, not an exact median value or a drawn-curve estimate.'
            else:
                if t=='less_than':lines=[label('Count below boundary')+'='+p.steps[0].value]
                elif t=='at_least':lines=[label('Count at or above boundary')+f'={N}-{p.steps[1].value}']
                else:lines=[label('Count in the interval')+f'={p.steps[0].value}-{p.steps[1].value}']
                e=f'The total number of observations is ${N}$. A cumulative table gives the number below each upper boundary. '+('Read the stated boundary’s cumulative count directly.' if t=='less_than' else 'Subtract the number below the threshold from the total for an at-least count.' if t=='at_least' else 'Subtract the lower boundary’s cumulative count from the upper boundary’s cumulative count.')+' Keep the question’s boundary inclusion: the supplied classes include the lower boundary and exclude the upper.'
    elif gid=='nssco_simple_probability':
        if t in ('one','two','not','impossible'):
            counts=m['counts'];total=sum(counts);favourable=int(p.steps[1].value);lines=[f'N='+ '+'.join(map(str,counts))+f'={total}',label('Favourable objects')+f'={favourable}','P(E)='+frac(favourable,total)]
            e='E denotes the exact event requested in the question. The bag contains '+', '.join(f'${v}$ {c}' for c,v in zip(m['colours'],counts))+f', so its total is $N={total}$. Count every object fitting E, including each named alternative for “or”, then divide by N. '+('The requested colour is absent, so the favourable count and probability are zero.' if t=='impossible' else 'For “not”, subtract the unwanted colour count from the whole bag, not from one other colour.') if t in ('not','impossible') else 'E denotes the requested event. Count the favourable objects among '+', '.join(f'${v}$ {c}' for c,v in zip(m['colours'],counts))+f', total $N={total}$. The colours are mutually exclusive for one draw, so add the counts when either of two colours is allowed. Divide the favourable count by all objects and simplify.'
        elif t in ('beads','letters'):
            total=m['top'] if t=='beads' else m['total'];fav=len(m['favourable']) if t=='beads' else m['favourable'];lines=[label('Favourable count')+f'={fav}','P(E)='+frac(fav,total)]
            if t=='beads':lines.insert(0,label('Qualifying labels')+': '+', '.join(map(str,m['favourable'])));e=f'The ${total}$ numbered objects are equally likely. E means the requested property, “{m["property"]}”. List all qualifying labels first, count them, and divide by ${total}$. A list of labels and its cardinality are different things.'
            else:e=f'The cards spell {m["word"]}; each letter occurrence is a separate equally likely card, even when letters repeat. There are ${total}$ cards, of which ${fav}$ fit the requested event E. Divide those counts and simplify; counting only distinct letter types gives the wrong sample space.'
        elif t=='two_way':
            counts=m['counts'];total=m['total'];fav=m['favourable'];lines=[f'N='+ '+'.join(str(x) for row in counts for x in row)+f'={total}',f'n(E)={fav}','P(E)='+frac(fav,total)]
            e='The table rows are '+', '.join(m['rows'])+' and columns '+', '.join(m['cols'])+f'. E is the requested event. A joint event uses the single matching cell; a row or column event sums all matching cells, and a complement uses all remaining cells. Here ${fav}$ of ${total}$ individuals qualify. The selection is from the whole table, so use the whole-table total as denominator; do not accidentally make it conditional on a row.'
        elif t=='expected':
            probability=F(m['p']);N=m['n'];lines=[label('Expected count')+f'={N}\\times{q(probability)}'];e=f'The event probability is ${q(probability)}$ and there are ${N}$ trials/days. Expected count is number of trials times probability. It is a long-run average prediction, not a guarantee that the event occurs exactly this often in one set of trials.'
        elif t=='missing_probability':
            values=[F(x) for i,x in enumerate(m['probs']) if i!=m['missing']];lines=['y=1-('+'+'.join(q(x) for x in values)+')'];e='The outcomes listed in the probability table are exhaustive and mutually exclusive, so their probabilities sum to one. Let y name the missing probability. Subtract the sum of all given probabilities from one; check the result lies between zero and one.'
        elif t=='not_event':
            probability=F(m['probs'][m['index']]);lines=['P(E^c)=1-P(E)=1-'+q(probability)];e=f'The given event E has probability ${q(probability)}$. E and “not E” together cover every possible outcome without overlap, so their probabilities total one. Subtract from one, retaining the original event definition rather than complementing an unrelated entry.'
        else:
            fav=m['favourable'];lines=[f'N=6\\times6=36',f'n(E)={fav}','P(E)='+frac(fav,36)];e=f'Two fair dice have $36$ equally likely ordered outcomes. E is “{m["event"]}”; ${fav}$ ordered pairs fit it. Count (a,b) and (b,a) separately when a and b differ. The possible sums are not equally likely, so dividing by the number of sums would be invalid.'
    else:
        if 'branches' in m:
            a,b=map(F,m['branches']);pa,pb=F(m['p_first']),F(m['p_second']);lines=[f'P_1={q(a)},\\quad P_2={q(b)}','P(E)=P_1P_2='+mul(a,b)]
            e=f'The two pass probabilities are ${q(pa)}$ and ${q(pb)}$. Use their complements for a requested failure. Here the requested first and second branches have probabilities $P_1={q(a)}$ and $P_2={q(b)}$. The tests are independent, so multiply along this combined event; adding would not give the probability of both.'
        elif 'r' in m:
            r,b=m['r'],m['b'];N=r+b;draws=3 if p.level==4 else 2
            if t=='second_given_first':
                remaining=int(p.steps[1].value);lines=[label('Total left')+f'={N}-1={N-1}','P(E\\mid first)='+frac(remaining,N-1)]
                e=f'The original bag has ${r}$ of the first colour and ${b}$ of the second. One item has already been removed and its colour is known ({m["first"]}). There are ${N-1}$ objects left, of which ${remaining}$ have the requested colour. This is conditional probability after that first draw; do not multiply by the probability of a condition already supplied.'
            elif t=='one_each':
                first=frac(r,N)+r'\times'+frac(b,N-1);second=frac(b,N)+r'\times'+frac(r,N-1);lines=['P(E)='+first+'+'+second]
                e=f'The bag has ${r}$ of the first colour and ${b}$ of the second. “One of each” permits two mutually exclusive orders. Multiply conditional probabilities along each order, reducing the second total to ${N-1}$, then add the two routes. Each route’s second-colour count is unchanged because a different colour was removed first.'
            else:
                want=r if m.get('want',0)==0 else b;count=(N-want) if t=='at_least_one' else want
                factors=[frac(count-i,N-i) for i in range(draws)];route=r'\times'.join(factors);lines=[('P(E)=1-(' if t=='at_least_one' else 'P(E)=')+route+(')' if t=='at_least_one' else '')]
                e=f'The original bag contains ${r}$ of the first colour and ${b}$ of the second, total ${N}$. There are ${draws}$ draws without replacement. '+('For at least one of the target colour, calculate the complementary route with none of it, then subtract that entire route probability from one.' if t=='at_least_one' else 'The requested event takes the target colour every time. Multiply the successive conditional probabilities.')+' Both the total and the chosen-colour count decrease after each draw of that colour. Do not reuse the original denominator as if objects were replaced.'
        else:
            a,b,c=F(m['p']),F(m['q1']),F(m['q2']);route1=a*b;route2=(1-a)*c
            lines=[f'P(R_1\\cap L)={mul(a,b)}={q(route1)}']
            if t!='joint_late':lines.extend([f'P(R_2\\cap L)={mul(1-a,c)}={q(route2)}',f'P(L)={q(route1)}+{q(route2)}'])
            if t=='not_late':lines.append(f'P(L^c)=1-({q(route1+route2)})')
            e=f'Let R₁ and R₂ denote the two travel methods in the question, and L being late. The first method has probability ${q(a)}$, its conditional late probability ${q(b)}$; the second method has probability ${q(1-a)}$ and conditional late probability ${q(c)}$. Multiply each method probability by its own conditional late probability. '+('Keep the first route only for this joint event.' if t=='joint_late' else 'Add the two mutually exclusive late routes to obtain the overall late probability.')+(' Finally subtract overall lateness from one for not late.' if t=='not_late' else '')
    return finish(p,lines,e)
