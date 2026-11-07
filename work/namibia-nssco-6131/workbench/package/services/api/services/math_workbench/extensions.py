"""Explicit renewable demands closing the independent R6 scope findings."""
from copy import deepcopy
from fractions import Fraction as F
import math
from .core import question,part,step,fmt,polynomial
from .diagrams import spec,line,text,polyline,asset,circle,cartesian


def build_general_intersecting_lines(seed,rng,requested_key=None):
    theta=math.radians(rng.choice((40,50,60,70,80,100,110,120,130,140)))
    rotation=math.radians(rng.choice((10,20,30,40)))
    O=(90,85);radius=rng.randint(20,28);locus_radius=rng.choice((36,40,45,48))
    direction=lambda angle:(math.cos(angle),math.sin(angle))
    point=lambda angle,length:(O[0]+length*math.cos(angle),O[1]+length*math.sin(angle))
    u,v=point(rotation,radius),point(rotation+theta,radius)
    P=point(rotation,locus_radius)
    label_point=point(rotation,54)
    label_point=(label_point[0]+7*math.sin(rotation),label_point[1]-7*math.cos(rotation))
    graph=spec(180,170,[line(point(rotation,-65),point(rotation,65)),line(point(rotation+theta,-65),point(rotation+theta,65)),text((O[0]+3,O[1]-5),'O'),text(point(rotation,68),'L'),text(point(rotation+theta,68),'M'),circle(P,.8,fill='black'),text(label_point,'P'),line(P,(label_point[0]-1,label_point[1]+1),color='#777777',width=.15)])
    sol=deepcopy(graph)
    for angle in (rotation+theta/2,rotation+theta/2+math.pi/2):sol['commands'].append(line(point(angle,-65),point(angle,65),color='#005522',width=.65))
    # Compass marks: equal initial radii locate crossings on each ray. Equal
    # radii from those crossings intersect on each of the two angle bisectors.
    sol['commands'].append(polyline([point(rotation-.15+(theta+math.pi+.3)*i/160,radius) for i in range(161)],color='#888888'))
    for second in (v,point(rotation+theta+math.pi,radius)):
        crossing=(u[0]+second[0]-O[0],u[1]+second[1]-O[1])
        for centre in (u,second):
            angle=math.atan2(crossing[1]-centre[1],crossing[0]-centre[0])
            sol['commands'].append(polyline([(centre[0]+radius*math.cos(angle+d),centre[1]+radius*math.sin(angle+d)) for d in (-.18,-.12,-.06,0,.06,.12,.18)],color='#888888'))
    intersections=[point(angle,locus_radius) for angle in (rotation+theta/2,rotation+theta/2+math.pi/2,rotation+theta/2+math.pi,rotation+theta/2+3*math.pi/2)]
    sol['commands'].append(circle(O,locus_radius,color='#005522',width=.55))
    sol['commands'] += [circle(p,1.1,fill='black') for p in intersections]
    answer='Both complete angle bisectors of lines L and M, including the bisector of the adjacent angle, with compass arcs retained.'
    q=question('general-intersecting-line-loci',['5e.1'],'Intersecting angle-bisector loci','Two straight lines L and M intersect at O. Point P is on L. Use a straight edge and compasses only.',[
      part('Construct the complete locus of points equidistant from L and M. Keep all construction arcs.',answer,[
        step('Mark equal distances along the rays','One compass radius from O locates points equally far from the angle vertex.','Keep the compass radius fixed when crossing both rays.'),
        step('Construct the first angle bisector','Equal-radius arcs from the two ray crossings meet at a point equally inclined to both rays.','Join their intersection to O and extend the line in both directions.'),
        step('Construct the adjacent angle bisector','The full locus includes points in both pairs of opposite angles, not only the first angle.','Repeat using an opposite ray to construct the second, perpendicular bisector.')],3,[(1,'Correct equal-radius ray and intersection arcs for a valid bisector.'),(1,'One correct complete angle-bisector line.'),(1,'Both complete perpendicular angle-bisector lines and no extra locus.')]),
      part('Construct the locus of points at distance OP from O. Mark every point that also belongs to the locus in part (a).','A circle with centre O through P; the four intersections of this circle with the two angle bisectors.',[
        step('Construct the fixed-distance locus','Every point at distance OP from O lies on a circle with centre O and radius OP.','Set the compass to OP and draw the complete circle.'),
        step('Intersect the two loci','Both conditions must hold at the same point. Each complete bisector cuts the circle twice.','Mark all four circle–bisector intersections, and no other points.')],3,[(1,'Circle centred at O through P.'),(1,'Both intersections on one complete bisector.'),(1,'Both intersections on the other bisector, with no extra points.')]),
      part('Explain why both bisectors belong to the first locus.','Distance is measured perpendicularly to each line; points on either angle bisector have equal perpendicular distances to l and m.',[step('Compare perpendicular distances','Distance to a straight line is the shortest, perpendicular distance.','Both the internal and external angle bisectors satisfy the same equality.')])],variant=seed,assets=[asset('general-bisectors',graph,sol)])
    q['structural_case']='general_intersecting_lines';q['parameter_evidence']={'angle_degrees':round(math.degrees(theta)),'rotation_degrees':round(math.degrees(rotation)),'centre':O,'circle_radius':locus_radius,'intersections':intersections}
    return [q]


def build_ratio_all_shares(seed,rng,requested_key=None):
    a,b,c=[rng.randint(2,9) for _ in range(3)];unit=rng.randint(12,40)
    if a==b:b+=1
    total=(a+b)*unit;total3=(a+b+c)*unit
    tank_unit=unit+rng.randint(1,8);total3=(a+b+c)*tank_unit
    length_unit=tank_unit+rng.randint(1,8);mass_unit=length_unit+rng.randint(1,8)
    length_total=(a+b)*length_unit;difference=abs(a-b)*mass_unit
    specs=[(f'Divide N${total} in the ratio {a}:{b}. Give both shares.',f'N${a*unit} and N${b*unit}.',total,a+b,[a,b]),
      (f'Divide {total3} litres among three tanks in the ratio {a}:{b}:{c}. Give all three amounts.',f'{a*tank_unit}, {b*tank_unit} and {c*tank_unit} litres.',total3,a+b+c,[a,b,c])]
    ps=[]
    for prompt,answer,whole,parts,weights in specs:
        share=whole//parts
        ps.append(part(prompt,answer,[step('Find one ratio part','The total is shared among the sum of the ratio parts.',rf'\frac{{{whole}}}{{{parts}}}={share}'),step('Find every requested share','Multiply one part by each ratio number, and check that the shares sum to the total.','; '.join(f'{w}\\times{share}={w*share}' for w in weights))],2,[(1,'Correct unit share from the sum of ratio parts.'),(1,'All correct shares, with their units.')]))
    ps.append(part(f'Two lengths are in the ratio {a}:{b}. The first is {a*length_unit} cm. Find the second and their total length.',f'{b*length_unit} cm; total {length_total} cm.',[step('Recover the unit share','The first length contains the first ratio number of equal parts.',rf'\frac{{{a*length_unit}}}{{{a}}}={length_unit}'),step('Scale to the unknown amounts','The second length uses the second ratio number; the total uses the sum.',f'{b}\\times{length_unit}={b*length_unit}; ({a}+{b})\\times{length_unit}={length_total}')],2,[(1,'Correct unit share.'),(1,'Correct second length and total.')]))
    ps.append(part(f'Two masses are in the ratio {a}:{b} and differ by {difference} kg. Find both masses.',f'{a*mass_unit} kg and {b*mass_unit} kg.',[step('Relate the difference to ratio parts','The difference between the masses is the difference between their numbers of parts.',rf'\text{{One part}}=\frac{{{difference}}}{{{abs(a-b)}}}={mass_unit}'),step('Calculate both masses','Use the same unit share for each side of the ratio.',f'{a}\\times{mass_unit}={a*mass_unit}; {b}\\times{mass_unit}={b*mass_unit}')],2,[(1,'Correct use of the difference of ratio parts.'),(1,'Both masses correct.')]))
    return [question('ratio-all-shares',['1j.2'],'Sharing in a ratio','Show your working.',ps,variant=seed)]


def build_monomial_products(seed,rng,requested_key=None):
    a,b,c,d=[rng.randint(2,8) for _ in range(4)]
    from ..math_generators.algebra_content import _sum
    specs=[(rf'{a}x({b}x^2-{c}x+{d})',polynomial([a*b,-a*c,a*d,0]),rf'{a*b}x^3-{a*c}x^2+{a*d}x'),
      (rf'-{a}y^2({b}y^3-{c}y+{d})',_sum((-a*b,'y^5'),(a*c,'y^3'),(-a*d,'y^2')),rf'-{a*b}y^5+{a*c}y^3-{a*d}y^2'),
      (rf'{a}xy({b}x^2-{c}y^2)',_sum((a*b,'x^3y'),(-a*c,'xy^3')),rf'{a*b}x^3y-{a*c}xy^3')]
    return [question('monomial-polynomial-products',['6b.1'],'Distributing a monomial','Expand each product and simplify.',[
      part('$'+expression+'$',answer,[step('Multiply the monomial by every term','The distributive law applies to every term, including its sign. Multiply coefficients and add powers of matching letters.',working),step('Check powers and signs','Only like terms can be collected; different monomials remain separate.',answer)],2,[(1,'Correct distribution to all polynomial terms.'),(1,'All signs, coefficients and powers correct.')]) for expression,answer,working in specs],variant=seed)]


def build_exponential_equation_forms(seed,rng,requested_key=None):
    b=rng.choice((2,3,5));u=rng.randint(2,5);v=rng.randint(-5,5);k=rng.randint(1,6);p=rng.randint(3,6);q=rng.randint(1,p-1);r=rng.randint(1,8)
    from .core import polynomial
    linear=polynomial([u,v])
    reciprocal_power=k+rng.randint(1,4)
    specs=[(rf'{b}^{{{linear}}}={b**k}',rf'{linear}={k}',F(k-v,u)),
      (rf'{b}^{{{linear}}}=\frac{{1}}{{{b**k}}}',rf'{linear}=-{k}',F(-k-v,u)),
      (rf'(\frac{{1}}{{{b}}})^{{{linear}}}={b**reciprocal_power}',rf'-({linear})={reciprocal_power}',F(-reciprocal_power-v,u)),
      (rf'{b**p}^x={b}^{{{polynomial([q,r])}}}',rf'{p}x={polynomial([q,r])}',F(r,p-q))]
    return [question('exponential-equation-forms',['6e.3'],'Solving with a common base','Solve each equation using the laws of indices.',[
      part('$'+expression+'$',f'x={fmt(answer)}',[step('Write both sides with the same base','Express the number or reciprocal as a power of the same positive base. Then equate exponents.',equation),step('Solve the linear exponent equation','Collect the x terms, then divide by the nonzero coefficient.',f'x={fmt(answer)}')],2,[(1,'Correct common-base equation in the exponents.'),(1,'Correct value of x.')]) for expression,equation,answer in specs],variant=seed)]

def build_bills_and_receipts(seed,rng,requested_key=None):
    """Invented exercise tariffs and receipts; all monetary arithmetic is cents."""
    keys=['telephone-bill','cell-phone-bill','till-receipt','payment-receipt','clothing-account']
    out=[]
    money=lambda cents:f'N${cents/100:.2f}'
    for key in ([requested_key] if requested_key else keys):
        if key not in keys:raise ValueError('Unknown bill/receipt recipe')
        fixed=rng.randint(60,180)*100;rate=rng.choice((40,60,80,120));minutes=rng.randint(35,190)
        credit=rng.randint(10,40)*100;ps=[]
        if key=='telephone-bill':
            rate=(40,60,80,120)[seed%4]
            variable=minutes*rate;total=fixed+variable
            stem=f'A fictional household telephone bill uses these exercise tariffs.\n\n| Item | Amount |\n|---|---:|\n| Monthly rental | {money(fixed)} |\n| Charged call minutes | {minutes} |\n| Price per minute | {money(rate)} |\n| Credit already paid | {money(credit)} |'
            ps=[part('Calculate the charge for the calls.',money(variable),[step('Multiply usage by the tariff','Every charged minute costs the stated amount.',f'{minutes} × {money(rate)} = {money(variable)}')]),
                part('Calculate the balance payable, including rental and credit.',money(total-credit),[step('Add the monthly charges','Rental is fixed; calls add a usage charge.',f'{money(fixed)} + {money(variable)} = {money(total)}'),step('Deduct the credit once','The amount already paid reduces the outstanding bill.',f'{money(total)} − {money(credit)} = {money(total-credit)}')],2,[(1,'Rental plus the correct call charge.'),(1,'Credit deducted to give the correct balance.')])]
            evidence={'fixed_cents':fixed,'minutes':minutes,'rate_cents':rate,'credit_cents':credit,'answers_cents':[variable,total-credit]}
        elif key=='cell-phone-bill':
            included=rng.choice((50,75,100));excess=rng.randint(15,95);used=included+excess;total=fixed+excess*rate
            stem=f'A fictional cell-phone package costs {money(fixed)} per month and includes {included} call minutes. Additional minutes cost {money(rate)} each. This month {used} minutes were used. A payment of {money(credit)} is credited to this bill. These are exercise tariffs.'
            ps=[part('Calculate the number of chargeable additional minutes.',str(excess),[step('Deduct the included allowance','Included minutes have already been paid for in the package fee.',f'{used} − {included} = {excess}')]),
                part('Calculate the balance payable.',money(total-credit),[step('Calculate the additional charge','Only minutes beyond the allowance attract the extra tariff.',f'{excess} × {money(rate)} = {money(excess*rate)}'),step('Combine the bill and payment','Add the package fee and extra usage, then deduct the credited payment.',f'{money(fixed)} + {money(excess*rate)} − {money(credit)} = {money(total-credit)}')],2,[(1,'Correct additional-minute charge.'),(1,'Correct balance after package fee and payment.')])]
            evidence={'included_minutes':included,'used_minutes':used,'fixed_cents':fixed,'rate_cents':rate,'credit_cents':credit,'answers_cents':[total-credit]}
        elif key=='till-receipt':
            quantity=rng.randint(2,7);price=rng.randint(12,45)*100+50;other=rng.randint(20,80)*100
            subtotal=quantity*price;total=subtotal+other;tendered=((total//10000)+1)*10000
            shop,item,other_item=(('Moringa School Supplies','Exercise books','School supplies pack'),('Omatako Grocer','Bags of rice','Cooking oil'),('Acacia Hardware','Paint brushes','Paint tray'),('Etosha Clothing','School shirts','Pair of socks'),('Marula Bookshop','Story books','Dictionary'))[seed%5]
            stem=f'The fictional {shop} till receipt shows:\n\n| Item | Quantity | Unit price | Line total |\n|---|---:|---:|---:|\n| {item} | {quantity} | {money(price)} | ? |\n| {other_item} | 1 | {money(other)} | {money(other)} |\n| Cash tendered | | | {money(tendered)} |'
            ps=[part('Calculate the missing line total.',money(subtotal),[step('Extend the unit price','A line total is quantity multiplied by price per item.',f'{quantity} × {money(price)} = {money(subtotal)}')]),
                part('Calculate the receipt total and the change due.',f'Total {money(total)}; change {money(tendered-total)}.',[step('Add the line totals','Each purchase contributes once to the receipt total.',f'{money(subtotal)} + {money(other)} = {money(total)}'),step('Subtract the total from cash tendered','Change is the cash remaining after paying for the purchases.',f'{money(tendered)} − {money(total)} = {money(tendered-total)}')],2,[(1,'Correct receipt total.'),(1,'Correct change.')])]
            evidence={'quantity':quantity,'unit_price_cents':price,'other_cents':other,'tendered_cents':tendered,'answers_cents':[subtotal,total,tendered-total]}
        elif key=='payment-receipt':
            balance=rng.randint(60,150)*100;tendered=rng.randint(25,45)*100;change=rng.choice((150,250,350));paid=tendered-change
            stem=f'A fictional payment receipt for a school account shows:\n\n| Entry | Amount |\n|---|---:|\n| Balance before payment | {money(balance)} |\n| Cash tendered | {money(tendered)} |\n| Change returned | {money(change)} |\n| Amount credited to account | ? |'
            ps=[part('Calculate the amount actually credited to the account.',money(paid),[step('Deduct returned change','Only the cash kept pays down the account.',f'{money(tendered)} − {money(change)} = {money(paid)}')]),
                part('Calculate the remaining account balance.',money(balance-paid),[step('Subtract the actual payment','Returned change is not part of the payment received.',f'{money(balance)} − {money(paid)} = {money(balance-paid)}')])]
            evidence={'balance_cents':balance,'tendered_cents':tendered,'change_cents':change,'answers_cents':[paid,balance-paid]}
        else:
            opening=rng.randint(180,450)*100;purchases=rng.randint(80,220)*100;returned=rng.randint(10,60)*100;payment=rng.randint(30,90)*100
            closing=opening+purchases-returned-payment
            stem=f'A fictional clothing account statement has no interest or other charges this month.\n\n| Entry | Amount |\n|---|---:|\n| Opening amount owed | {money(opening)} |\n| New purchases | {money(purchases)} |\n| Credit for returned clothing | {money(returned)} |\n| Payment received | {money(payment)} |'
            ps=[part('Calculate the amount owed before deducting the return and payment.',money(opening+purchases),[step('Add the new purchases','Purchases increase the amount owed on the account.',f'{money(opening)} + {money(purchases)} = {money(opening+purchases)}')]),
                part('Calculate the closing balance still owed.',money(closing),[step('Deduct both credits','Returned goods and a payment both reduce the amount owed.',f'{money(opening+purchases)} − {money(returned)} − {money(payment)} = {money(closing)}')],2,[(1,'Both credits correctly deducted.'),(1,'Correct closing balance.')])]
            evidence={'opening_cents':opening,'purchases_cents':purchases,'return_cents':returned,'payment_cents':payment,'answers_cents':[opening+purchases,closing]}
        q=question(key,['1l.5'],key.replace('-',' ').capitalize(),stem,ps,variant=seed)
        q['structural_case']=key;q['parameter_evidence']=evidence;out.append(q)
    return out


def build_contextual_variation(seed,rng,requested_key=None):
    mass=rng.randint(2,8);price=rng.randint(12,40);new_mass=mass+rng.randint(1,6)
    workers=rng.randint(3,9);hours=2*rng.randint(3,8);work=workers*hours;new_workers=rng.choice([n for n in range(2,19) if n!=workers and work%n==0]);new_hours=work//new_workers
    q=question('contextual-direct-inverse-variation',['1j.7'],'Direct and inverse variation in context',
        f'At a fictional market, the cost C Namibian dollars of m kg of mahangu varies directly with its mass. A bag with mass {mass} kg costs N${mass*price}. Separately, n equally productive workers take t hours to complete a fixed packing job. They work at constant rates without interfering with each other. With {workers} workers, the job takes {hours} hours.',[
        part('Express C in terms of m.',f'C={price}m',[
            step('Choose the direct-variation model','A direct proportionality has constant cost per kilogram.','C=km'),
            step('Determine the constant from the bag','Divide its cost by its mass.',f'k={mass*price}/{mass}={price}; C={price}m')],2,[(1,'Correct direct-variation model C=km.'),(1,'Correct constant and algebraic relation.')]),
        part(f'Calculate the cost of {new_mass} kg of the same mahangu.',f'N${new_mass*price}',[step('Substitute the new mass','The cost per kilogram remains constant.',f'C={price} × {new_mass}={new_mass*price}')]),
        part('Express t in terms of n for this packing job.',rf't=\frac{{{work}}}n',[
            step('Choose the inverse-variation model','More equally productive workers reduce the time for a fixed job; worker-hours remain constant.','t=k/n'),
            step('Determine the fixed workload','Multiply the known number of workers by their completion time.',f'k={workers} × {hours}={work}; t={work}/n')],2,[(1,'Correct inverse model t=k/n.'),(1,'Correct constant and algebraic relation.')]),
        part(f'Calculate the time needed with {new_workers} workers.',f'{new_hours} hours',[step('Substitute the new workforce','The workload stays fixed when the number of equally productive workers changes.',f't={work}/{new_workers}={new_hours} hours')])],variant=seed)
    q['parameter_evidence']={'mass':mass,'price_per_kg':price,'new_mass':new_mass,'workers':workers,'hours':hours,'new_workers':new_workers,'worker_hours':work,'new_hours':new_hours}
    return [q]


def build_speed_time_rates(seed,rng,requested_key=None):
    u=rng.randint(4,15);acceleration=rng.randint(1,4);first_time=rng.randint(3,8);braking_time=rng.randint(3,8)
    peak=u+acceleration*first_time;duration=first_time+braking_time
    deceleration=F(peak,braking_time);distance=F((u+peak)*first_time+peak*braking_time,2)
    graph,pt=cartesian(0,duration+1,0,5*math.ceil(peak/5)+5,width=170,height=125,xstep=1,ystep=5)
    graph['commands']=[c for c in graph['commands'] if not(c['kind']=='text' and c['value'] in ('x','y'))]
    graph['commands'] += [polyline([pt(0,u),pt(first_time,peak),pt(duration,0)]),text((105,5),'Time (seconds)'),text((17,116),'Speed (m/s)')]
    reference=deepcopy(graph)
    reference['commands'].append(line(pt(first_time,0),pt(first_time,peak),dash=True,color='#006633'))
    q=question('speed-time-rates',['7a.4','7a.5'],'Acceleration and braking',
        f'A test vehicle changes speed uniformly from {u} m/s to {peak} m/s in the first {first_time} seconds. It then slows uniformly to rest over the next {braking_time} seconds. The speed–time graph shows this motion.',[
        part('Calculate the acceleration during the first section.',f'{acceleration} m/s²',[
            step('Find the change in speed','Acceleration is change in velocity divided by the time taken.',f'{peak} − {u} = {peak-u} m/s'),
            step('Divide by elapsed time','Use the duration of this section only.',f'{peak-u}/{first_time} = {acceleration} m/s²')],2,[(1,'Correct change in speed divided by first-section time.'),(1,'Correct acceleration and units.')],objectives=['7a.4']),
        part('Calculate the magnitude of the deceleration during braking. Give an exact value.',fmt(deceleration)+' m/s²',[
            step('Find the signed acceleration','The final speed is zero, so the velocity change is negative.',rf'a=\frac{{0-{peak}}}{{{braking_time}}}={fmt(-deceleration)}'),
            step('State the magnitude of the deceleration','The question asks for the positive magnitude of the decrease in speed per second.',fmt(deceleration)+' m/s²')],2,[(1,'Correct velocity decrease divided by braking time.'),(1,'Correct positive magnitude and units.')],objectives=['7a.4']),
        part('Calculate the total distance travelled during the two sections.',fmt(distance)+' m',[
            step('Find the first area','Distance is area under the speed–time graph; the first region is a trapezium.',rf'\frac{{{u}+{peak}}}2\times{first_time}={fmt(F((u+peak)*first_time,2))}'),
            step('Add the braking area','The second region is a triangle, and the two time intervals do not overlap.',rf'{fmt(F((u+peak)*first_time,2))}+\frac12\times{braking_time}\times{peak}={fmt(distance)}\text{{ m}}')],3,[(1,'Correct first-section trapezium area.'),(1,'Correct braking triangle area.'),(1,'Correct total distance and units.')],objectives=['7a.5'])],variant=seed,assets=[asset('speed-time',graph,reference)])
    q['parameter_evidence']={'initial_speed':u,'peak_speed':peak,'first_time':first_time,'braking_time':braking_time,'distance':[distance.numerator,distance.denominator],'deceleration':[deceleration.numerator,deceleration.denominator]}
    return [q]


def build_line_equation_from_graph(seed,rng,requested_key=None):
    slope=rng.choice((-4,-3,-2,2,3,4));intercept=rng.randint(-5,5)
    lo=min(-3*slope+intercept,4*slope+intercept,0)-1;hi=max(-3*slope+intercept,4*slope+intercept,0)+1
    graph,pt=cartesian(-3,4,lo,hi,width=150,height=145)
    graph['commands'].append(line(pt(-3,-3*slope+intercept),pt(4,4*slope+intercept)))
    equation='y='+polynomial([slope,intercept])
    q=question('line-equation-from-graph',['7d.3'],'Equation from a line graph','Use the labelled scales on the straight-line graph.',[
        part('Calculate the gradient. Show the two points you use.',str(slope),[
            step('Choose two points on the drawn line','The points must be read using the same coordinate scales.',f'(0,{intercept}) and (1,{slope+intercept})'),
            step('Divide vertical change by horizontal change','Gradient is rise divided by run, with the sign preserved.',rf'm=\frac{{{slope+intercept}-({intercept})}}{{1-0}}={slope}')],2,[(1,'Two correctly read points and rise/run.'),(1,'Correct signed gradient.')]),
        part('Find the equation of the line in the form y = mx + c.',equation,[
            step('Read the vertical intercept','At the y-intercept x=0, so its y-coordinate is c.',f'c={intercept}'),
            step('Combine gradient and intercept','The same equation must describe every point on the drawn line.',equation)],2,[(1,'Correct vertical intercept.'),(1,'Correct complete line equation, accepting equivalent forms.')])],variant=seed,assets=[asset('line-equation',graph)])
    q['parameter_evidence']={'gradient':slope,'intercept':intercept}
    return [q]


BUILDERS=[build_general_intersecting_lines,build_ratio_all_shares,build_monomial_products,build_exponential_equation_forms,build_bills_and_receipts,build_contextual_variation,build_speed_time_rates,build_line_equation_from_graph]
