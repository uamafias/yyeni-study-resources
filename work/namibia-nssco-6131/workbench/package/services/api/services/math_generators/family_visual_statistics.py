"""Visual distributions, charts, Venn regions and probability diagrams."""
import math
from fractions import Fraction
from .visual_common import *


def charts(g,r,s,l):
    labels=['A','B','C'];counts=[r.randint(2,8)*2 for _ in labels]
    bars=[]
    for i,(name,n) in enumerate(zip(labels,counts)):
        bars += [closed([(i+.2,0),(i+.8,0),(i+.8,n),(i+.2,n)],'blue',True),text(i+.5,-1,name)]
    bound=(0,3,-2,max(counts)+2);chart=grid(bound,bars,'Category counts',x_label='Category',y_label='Frequency',x_step=1,y_step=2,equal_scale=False)
    if l==1:
        if s%2==0:
            k=r.randint(0,2)
            return make(g,s,l,'read_bar',f'Use the bar chart to state the frequency for category {labels[k]} and identify a category with the largest frequency.',f'{labels[k]}: {counts[k]}; largest: '+', '.join(labels[i] for i,n in enumerate(counts) if n==max(counts))+'.',chart,None,
                'Read the numerical height on the frequency axis. Compare bar heights, not widths. Equal maximum heights give a tie, so either tied category is a correct largest category.',[(1,f'Correct frequency {counts[k]} for {labels[k]}.'),(1,'Correct largest category: '+', '.join(labels[i] for i,n in enumerate(counts) if n==max(counts))+'.')],['NSSCO-6131-2018-visual-p13-26'],{'counts':counts,'selected':k},False)
        return make(g,s,l,'draw_bar','Draw a bar chart for these frequencies: '+', '.join(f'{name}: {n}' for name,n in zip(labels,counts))+'.',
            'Use equal-width separated bars with the listed category frequencies.',grid(bound,caption='Blank chart axes',x_label='Category',y_label='Frequency',y_step=2,equal_scale=False),chart,
            'Categories are discrete, so use equal-width bars with gaps. Heights represent frequencies; include category names and a uniform frequency scale. This differs from a histogram, where bars span continuous class intervals.',
            [(1,'Clearly labelled categories/frequency axis and uniform scale.'),(1,'All three bar heights match the supplied frequencies.'),(1,'Equal-width separated bars with no missing category.')],['NSSCO-6131-2018-visual-p13-26'],{'counts':counts})
    if l==2:
        weights=[r.randint(1,5),r.randint(1,5)];weights.append(12-sum(weights));unit=r.randint(5,20);counts=[unit*w for w in weights];angles=[30*w for w in weights];els=[];start=0
        for name,angle,color in zip(labels,angles,('blue','green','purple')):
            pts=[(0,0)]+[(4*math.cos(math.radians(start+angle*i/60)),4*math.sin(math.radians(start+angle*i/60))) for i in range(61)]+[(0,0)]
            mid=math.radians(start+angle/2);els += [line(pts,color,fill=True),text(2.7*math.cos(mid),2.7*math.sin(mid),name)];start+=angle
        q=spec((-5,5,-5,5),'Circle for a pie chart',[circle(0,0,4)])
        ans=spec(q['bounds'],'Completed pie chart',els)
        return make(g,s,l,'draw_pie','Construct a pie chart for '+', '.join(f'{name}: {n}' for name,n in zip(labels,counts))+'. Show your sector-angle calculations and label the categories.',
            f'Total {sum(counts)}. Sector angles for A, B, C: {angles} degrees.',q,ans,
            'Each sector angle is its frequency divided by the total, multiplied by 360°. The angles must sum to one complete turn. Start consecutive sectors from the previous boundary and label them or provide a clear key.',
            [(1,f'Correct sector-angle calculations {angles}, in category order.'),(1,'Pie sectors drawn with the correct relative angles, filling exactly one circle.'),(1,'All categories correctly labelled or keyed.')],['NSSCO-6131-2018-visual-p13-26'],{'counts':counts,'angles':angles})
    unit=2*r.randint(1,3);halves=[r.randint(3,11) for _ in labels];counts=[Fraction(n*unit,2) for n in halves]
    def symbols(show):
        els=[]
        for row,(name,halfcount) in enumerate(zip(labels,halves)):
            y=3-row*2;els.append(text(-1,y,name))
            if not show:continue
            for j in range(halfcount//2):els.append(circle(j+1,y,.32,'blue',fill=True))
            if halfcount%2:
                x=halfcount//2+1;els += [circle(x,y,.32,'blue'),line([(x,y-.32)]+[(x+.32*math.cos(math.radians(a)),y+.32*math.sin(math.radians(a))) for a in range(-90,91,10)]+[(x,y-.32)],'blue',fill=True)]
        return els
    q=spec((-2,8,-2,5),'Pictogram rows; one whole symbol represents '+str(unit),symbols(s%2==0))
    if s%2==0:
        k=r.randint(0,2)
        return make(g,s,l,'read_pictogram',f'One whole circle represents {unit} learners; a half-circle represents half that number. How many learners are in category {labels[k]}?',f'{int(counts[k])} learners.',q,None,
            'Count whole symbols and any half-symbol separately, then multiply by the key. The key gives learners per whole symbol; a half-symbol is not one extra learner unless the key is two.',[(1,'Correct use of the whole/half-symbol key.'),(1,f'Correct count {int(counts[k])} learners for {labels[k]}.')],['NSSCO-6131-2018-visual-p13-26'],{'unit':unit,'half_symbols':halves,'counts':[int(v) for v in counts],'selected':k},False)
    ans=spec(q['bounds'],'Completed pictogram: one whole circle represents '+str(unit),symbols(True))
    return make(g,s,l,'draw_pictogram',f'Draw a pictogram for '+', '.join(f'{name}: {int(n)} learners' for name,n in zip(labels,counts))+f'. Use one whole circle for {unit} learners and a half-circle where needed.',
        'The rows need '+', '.join(f'{name}: {n/2:g} symbols' for name,n in zip(labels,halves))+'.',q,ans,
        'Divide each frequency by the key to find its symbol count. Use a consistent symbol size and distinguish halves clearly. Keep category labels and the key with the drawing.',[(1,'Correct key and consistent symbol size.'),(1,'All whole/half-symbol counts correct for the three labelled categories.')],['NSSCO-6131-2018-visual-p13-26'],{'unit':unit,'half_symbols':halves,'counts':[int(v) for v in counts]})


def histogram(g,r,s,l):
    widths=[r.randint(2,4)]*4 if l==1 else [2,3,5,4];n=3 if l==3 else 4;widths=widths[:n];densities=[r.randint(2,8) for _ in widths];freqs=[w*d for w,d in zip(widths,densities)]
    edges=[0]
    for w in widths:edges.append(edges[-1]+w)
    els=[closed([(edges[i],0),(edges[i+1],0),(edges[i+1],d),(edges[i],d)],'blue',True) for i,d in enumerate(densities)]
    kwargs={'x_label':'Time (minutes)','y_label':'Frequency density (learners/minute)','x_step':1,'y_step':1,'equal_scale':False}
    chart=grid((0,edges[-1]+1,0,max(densities)+2),els,'Histogram with continuous class intervals',**kwargs)
    data={'edges':edges,'widths':widths,'densities':densities,'frequencies':freqs}
    if l==3:
        return make(g,s,l,'read_histogram','Read the histogram and give the frequencies for the three intervals, in increasing interval order. Show the area calculation for each.','; '.join(f'${edges[i+1]-edges[i]}\\times{densities[i]}={f}$' for i,f in enumerate(freqs)),chart,None,
            'In a histogram, bar area represents frequency. Read each class width from the horizontal scale and its density from the vertical scale, then multiply. For unequal widths the tallest bar need not contain the largest frequency.',[(1,f'Correct frequency {f} for interval {edges[i]} to {edges[i+1]}, from width × density.') for i,f in enumerate(freqs)],['2024-P2-Q31'],data,False)
    table='| Time interval (minutes) | Frequency |\n|---|---|\n'+'\n'.join(f'| ${edges[i]}\\le t<{edges[i+1]}$ | {f} |' for i,f in enumerate(freqs))
    return make(g,s,l,'draw_histogram','Draw a histogram for this distribution. Use frequency density on the vertical axis.\n\n'+table,
        f'Class widths: {widths}; frequency densities: {densities}. Bars span their complete class intervals with no gaps.',grid(chart['bounds'],caption='Axes for the histogram',**kwargs),chart,
        'Calculate frequency density as frequency divided by class width. The full width of each bar is its actual interval, so unequal widths must not be replaced by equal-width category bars. Adjacent intervals touch. Check that each width multiplied by its height recovers its frequency.',[(1,f'Correct bar over [{edges[i]},{edges[i+1]}] with density {d} and its actual class width.') for i,d in enumerate(densities)],['2021-P2-Q15c'],data)


def cumulative(g,r,s,l):
    widths=[r.choice((5,10))]*4;edges=[0]
    for w in widths:edges.append(edges[-1]+w)
    fs=[r.randint(4,12) for _ in widths];cf=[0]
    for f in fs:cf.append(cf[-1]+f)
    pts=list(zip(edges,cf));q=grid((0,edges[-1]+5,0,cf[-1]+5),caption='Cumulative frequency axes',x_label='Time (minutes)',y_label='Cumulative frequency',x_step=5,y_step=5,equal_scale=False)
    chart=grid(q['bounds'],[line(pts,'blue')]+[point(x,y,'blue') for x,y in pts],'Cumulative frequency polygon',x_label='Time (minutes)',y_label='Cumulative frequency',x_step=5,y_step=5,equal_scale=False)
    if l==1:
        table='| Upper class boundary (minutes) | '+' | '.join(str(x) for x in edges)+' |\n|---|'+'---|'*len(edges)+'\n| Cumulative frequency | '+' | '.join(str(v) for v in cf)+' |'
        return make(g,s,l,'draw_cumulative','Draw the cumulative frequency diagram from this table.\n\n'+table,
            'Plot cumulative totals at the corresponding upper class boundaries, including the initial zero, then join in increasing order.',q,chart,
            'Use upper class boundaries rather than midpoints. Cumulative frequency never decreases. A clear increasing curve or correctly joined polygon is appropriate here; the cited report explicitly accepts ruled joins. It is not a bar chart or histogram.',
            [(1,'At least three non-origin cumulative points correctly plotted at upper boundaries.'),(1,'All supplied points correctly plotted, including the initial zero.'),(1,'Correct increasing joined graph, with sensible labelled axes; ruled joins are accepted for this task.')],['2024-P2-Q30b'],{'edges':edges,'frequencies':fs,'cumulative':cf})
    def quantile(target):
        for i in range(4):
            if cf[i]<=target<=cf[i+1]:return edges[i]+(edges[i+1]-edges[i])*(target-cf[i])/fs[i]
    q1=quantile(cf[-1]/4);median=quantile(cf[-1]/2);q3=quantile(3*cf[-1]/4)
    rounded=[math.floor(v+.5) for v in (q1,median,q3)]
    return make(g,s,l,'read_cumulative','Use the cumulative frequency diagram to estimate the median and interquartile range. Give your readings to the nearest minute.',
        f'$Q_1\\approx{rounded[0]}$, median $\\approx{rounded[1]}$, $Q_3\\approx{rounded[2]}$ minutes; $IQR\\approx{rounded[2]-rounded[0]}$ minutes using the rounded quartile readings.',chart,None,
        f'The total is {cf[-1]}. Read across at half the total for the median and at one quarter and three quarters for Q1 and Q3, then down to the time axis. Subtract Q1 from Q3 for the interquartile range; do not subtract the cumulative-frequency positions.',
        [(1,f'Median reading consistent with the displayed polygon, reference {median:.2f} minutes, rounded to the nearest minute.'),(1,f'Correct quartile readings from the graph (reference {q1:.2f} and {q3:.2f}) and their difference, approximately {q3-q1:.2f} minutes, with rounding consistent with the learner’s readings.')],['2024-P2-Q30c.i','2024-P2-Q30c.ii'],{'edges':edges,'frequencies':fs,'cumulative':cf,'q1':q1,'median':median,'q3':q3},False)


def tree(g,r,s,l):
    red=r.randint(3,9);blue=r.randint(3,9);total=red+blue
    branches=[((0,0),(3,2),'R',Fraction(red,total)),((0,0),(3,-2),'B',Fraction(blue,total)),((3,2),(6,3),'R',Fraction(red-1,total-1)),((3,2),(6,1),'B',Fraction(blue,total-1)),((3,-2),(6,-1),'R',Fraction(red,total-1)),((3,-2),(6,-3),'B',Fraction(blue-1,total-1))]
    def diagram(complete):
        els=[]
        for a,b,outcome,p in branches:
            els += [line([a,b]),text(b[0]+.35,b[1],outcome),text((a[0]+b[0])/2,(a[1]+b[1])/2+.35,str(p) if complete else '?')]
        return spec((-1,7,-4,4),'Two-stage tree: R means red, B means blue',els)
    q=diagram(l==2);ans=diagram(True);probs=[str(b[-1]) for b in branches]
    if l==1:
        return make(g,s,l,'complete_tree',f'A bag contains {red} red and {blue} blue counters. Two are drawn without replacement. Copy the tree and replace every ? with its branch probability.',
            'First branches: '+', '.join(probs[:2])+'. After R: '+', '.join(probs[2:4])+'. After B: '+', '.join(probs[4:])+'.',q,ans,
            f'The first denominator is {total}. After removing one counter the denominator is {total-1}; reduce the count of the colour actually removed. Probabilities leaving any node sum to one. Outcomes belong at branch ends and probabilities alongside branches.',
            [(1,'At least two of the six branch probabilities correct in their proper branches.'),(1,'At least four branch probabilities correct.'),(1,'All six branch probabilities correct in position, using without-replacement denominators.')],['2020-P2-Q18b','2023-P2-Q16a'],{'red':red,'blue':blue,'probabilities':probs})
    probability=Fraction(red,total)*Fraction(blue,total-1)+Fraction(blue,total)*Fraction(red,total-1)
    return make(g,s,l,'read_tree','Use the tree to find the probability of drawing one red and one blue counter in either order. Show both paths.',
        f'$P(RB)+P(BR)=\\frac{{{red}}}{{{total}}}\\frac{{{blue}}}{{{total-1}}}+\\frac{{{blue}}}{{{total}}}\\frac{{{red}}}{{{total-1}}}={probability}$.',q,None,
        'Multiply probabilities along a path. The RB and BR paths are mutually exclusive, so add their products to include both orders. Do not multiply the two path probabilities together or ignore the condition on the second draw.',
        [(1,'Correct product for RB.'),(1,'Correct product for BR.'),(1,f'Correct sum of those disjoint paths, {probability}.')],['2020-P2-Q18c.ii'],{'red':red,'blue':blue,'probability':str(probability)},False)


def possibility(g,r,s,l):
    sides=r.choice((3,4,5,6));target=r.randint(3,2*sides-1)
    els=[point(x,y,'blue') for x in range(1,sides+1) for y in range(1,sides+1)]
    q=grid((0,sides+1,0,sides+1),els,'Each grid point is one ordered outcome',x_label='First spinner',y_label='Second spinner')
    selected=[(x,y) for x in range(1,sides+1) for y in range(1,sides+1) if x+y==target];p=Fraction(len(selected),sides*sides)
    ans=grid(q['bounds'],els+[circle(x,y,.18,'red') for x,y in selected],'Circled outcomes have the required sum',x_label='First spinner',y_label='Second spinner')
    return make(g,s,l,'possibility_diagram',f'Two independent fair spinners each show the integers 1 to {sides}. Copy the possibility diagram, circle all outcomes with total {target}, then state the probability.',
        f'Circled outcomes: {selected}. Probability ${len(selected)}/{sides*sides}={p}$.',q,ans,
        f'Each ordered pair is equally likely, giving {sides*sides} grid points. Circle every point whose two coordinates add to {target}; reversed unequal pairs count separately. Probability is favourable points divided by all points.',
        [(1,f'All and only the outcomes {selected} circled on the diagram.'),(1,f'Correct probability {p}, as a fraction or equivalent decimal, from the equally likely outcomes.')],['2021-P2-Q14a.i','2021-P2-Q14a.ii'],{'sides':sides,'target':target,'selected':selected,'probability':str(p)})


def venn(g,r,s,l):
    # Use disjoint labelled regions as data; draw shading by a dense clipped-in-code
    # point lattice instead of exposing arbitrary SVG paths or client execution.
    outside=r.randint(1,8);a=r.randint(1,8);both=r.randint(1,8);b=r.randint(1,8)
    op=('intersection','union','outside_union','A_only')[(s-1)%4]
    radius=r.randint(20,30)/10;offset=r.randint(10,18)/10
    base=[closed([(-6,-4),(6,-4),(6,4),(-6,4)]),circle(-offset,0,radius),circle(offset,0,radius),text(-3.8,2.9,'A'),text(3.8,2.9,'B'),text(-5.4,3.4,'U')]
    loc=[(-offset-radius*.55,0,a),(0,0,both),(offset+radius*.55,0,b),(5,-3,outside)]
    if l==2:
        base += [text(x,y,n) for x,y,n in loc];p=Fraction(both,a+both+b+outside)
        return make(g,s,l,'read_venn','The Venn regions contain learner counts. Find the number in A union B and the probability that a randomly selected learner belongs to both A and B.',
            f'$n(A\\cup B)={a}+{both}+{b}={a+both+b}$; $P(A\\cap B)={both}/{a+both+b+outside}={p}$.',spec((-7,7,-5,5),'Two-set Venn diagram of learner counts',base),None,
            'The overlap belongs to both sets but is counted only once in the union. For probability the denominator is the whole universal set, including the count outside both circles.',[(1,f'Correct union count {a+both+b}.'),(1,f'Correct intersection probability {p} over the full universal total.')],['2020-P1-Q6c','2023-P2-Q6b'],{'A_only':a,'intersection':both,'B_only':b,'outside':outside},False)
    def selected(x,y):
        ia=(x+offset)**2+y*y<=radius**2;ib=(x-offset)**2+y*y<=radius**2
        return ia and ib if op=='intersection' else ia or ib if op=='union' else not ia and not ib if op=='outside_union' else ia and not ib
    shading=[]
    for xi in range(-22,23):
        for yi in range(-16,17):
            x,y=xi*.25,yi*.25
            if selected(x,y):shading.append((x,y))
    # 0.1-unit horizontal hatch marks are fixed numeric polylines, packed into
    # fewer than 250 primitives by using horizontal runs within each region.
    hatch=[]
    for yi in range(-16,17):
        run=[]
        for xi in range(-24,26):
            x,y=xi*.25,yi*.25
            if xi<=24 and selected(x,y):run.append((x,y))
            elif run:
                if len(run)>1:hatch.append(line([run[0],run[-1]],'blue'))
                run=[]
    expr={'intersection':r'A\cap B','union':r'A\cup B','outside_union':r'(A\cup B)\prime','A_only':r'A\cap B\prime'}[op]
    q=spec((-7,7,-5,5),'Two-set Venn diagram',base);ans=spec(q['bounds'],'Required region shaded',hatch+base)
    return make(g,s,l,'shade_venn',f'Copy the Venn diagram and shade only ${expr}$.',f'Shade the {op.replace("_"," ")} region.',q,ans,
        'Intersection means inside both sets, union inside either set or both, and a prime means complement within U. For A intersect B-prime, shade A while excluding its overlap with B. Include the part outside both circles only when the stated expression requires it.',[(1,f'All and only the {op} region shaded within U.')],['2021-P2-Q4c','2022-P2-Q6c.i','2023-P1-Q15a'],{'operation':op})

GENERATORS=[
 VisualGenerator('charts',120006,'Chart Calculations in Text Form',{1:charts,2:charts,3:charts},{1:'Drawing and reading bar charts',2:'Constructing a pie chart',3:'Drawing and reading pictograms'}),
 VisualGenerator('histograms',120007,'Histogram Width, Density and Frequency',{1:histogram,2:histogram,3:histogram},{1:'Drawing equal-width histograms',2:'Drawing unequal-width histograms',3:'Reading frequencies from histogram areas'}),
 VisualGenerator('cumulative',120005,'Cumulative Frequency Calculations',{1:cumulative,2:cumulative},{1:'Drawing a cumulative frequency diagram',2:'Reading median and quartiles from a graph'}),
 VisualGenerator('trees',120004,'Combined Events and Tree Calculations',{1:tree,2:tree},{1:'Completing a tree diagram',2:'Reading and combining tree paths'}),
 VisualGenerator('possibility',120003,'Simple Probability',{1:possibility},{1:'Constructing and using possibility diagrams'}),
 VisualGenerator('venn',15802,'Venn Diagrams in Text Form',{1:venn,2:venn},{1:'Shading Venn regions',2:'Reading counts and probability from Venn regions'}),
]
