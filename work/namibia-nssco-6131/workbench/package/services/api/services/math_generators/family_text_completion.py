"""Text-answer coverage for the remaining NSSCO 6131 lessons.

Aligned to syllabus sections 1, 5(a,b,c,e), 7(a,c), 9(a), 12(a).
These assess calculations and properties described in words or tables. They do
not assess constructing, drawing, recognising a pictured shape, or reading a
plotted chart. Tax tables are fictional exercise data, never current tax advice.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Callable

from .base import GeneratedProblem, MathGenerator, SeededRandom, Step, Distractor
from .formatting import math as tex, number_latex


def _t(x):
    if isinstance(x, (tuple, list)):
        return "(" + ", ".join(_t(v) for v in x) + ")"
    if isinstance(x, str):
        return x
    v = Fraction(x)
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def _problem(g, seed, level, skill, question, value, steps, data, wrong=None, kind="number_exact"):
    typed = _t(value)
    display = tex(number_latex(Fraction(value))) if kind == "number_exact" else tex(typed)
    distractors = ()
    if wrong is not None and _t(wrong) != typed:
        distractors = (Distractor(tex(_t(wrong)), "wrong_operation", g.error_notes[skill]["wrong_operation"], _t(wrong)),)
    return GeneratedProblem(g.generator_id, g.version, seed, level, skill, question, display,
                            distractors, data, tuple(Step(d, _t(v)) for d, v in steps),
                            {"answer_type": kind, "expected": [typed], "typed": typed})


def _geometry(g, r, s, l):
    if l == 1:
        angle = r.choice(tuple(range(1, 90)) + tuple(range(91, 180)) + tuple(range(181, 360)))
        name = "acute" if angle < 90 else "obtuse" if angle < 180 else "reflex"
        return _problem(g,s,l,"angle_vocabulary",f"Write down whether an angle of {tex(str(angle))} degrees is acute, obtuse or reflex.",name,
                        [("Compare with 90 and 180 degrees",name)],{"angle":angle},kind="text_reason")
    if l == 2:
        n = r.randint(3, 30)
        return _problem(g,s,l,"prism_faces",f"A prism has two congruent {n}-sided polygon bases. Write down its total number of faces.",n+2,
                        [("One lateral face for each base edge",n),("Add the two bases",n+2)],{"sides":n},n)
    a = r.randint(12, 84)
    return _problem(g,s,l,"isosceles_angles",f"An isosceles triangle has equal base angles of {tex(str(a))} degrees each. Calculate its vertex angle, in degrees.",180-2*a,
                    [("Add the two equal base angles",2*a),("Subtract from 180 degrees",180-2*a)],{"base_angle":a},180-a)


def _construction(g,r,s,l):
    if l == 1:
        scale = r.choice((50,100,200,250,500,1000)); cm = r.randint(2,120)
        value=Fraction(cm*scale,100)
        return _problem(g,s,l,"scale_length",f"A scale drawing uses scale {tex(f'1 : {scale}')}. A line measures {tex(str(cm))} cm on the drawing. Calculate its actual length, in metres.",value,
                        [("Multiply the drawn length by the scale denominator",cm*scale),("Convert centimetres to metres",value)],{"scale":scale,"cm":cm},Fraction(cm,scale))
    if l == 2:
        a=r.randint(22,170)
        return _problem(g,s,l,"angle_bisection",f"An angle of {tex(str(a))} degrees is bisected with compasses. Calculate either of the two equal angles, in degrees.",Fraction(a,2),
                        [("Divide the angle into two equal parts",Fraction(a,2))],{"angle":a},2*a)
    length=2*r.randint(5,80)
    return _problem(g,s,l,"perpendicular_bisection",f"A line segment AB is {tex(str(length))} cm long. Its perpendicular bisector meets AB at M. Calculate AM, in centimetres.",length//2,
                    [("The perpendicular bisector passes through the midpoint",length//2)],{"length":length},length)


def _symmetry(g,r,s,l):
    n=r.randint(3,40)
    if l==1:
        return _problem(g,s,l,"regular_polygon_symmetry",f"A regular polygon has {n} sides. Write down the number of lines of symmetry.",n,
                        [("Each side corresponds to one symmetry axis in a regular polygon",n)],{"n":n},2*n)
    if l==2:
        value=Fraction(360,n)
        return _problem(g,s,l,"rotation_angle",f"A regular {n}-sided polygon is rotated about its centre. Calculate its smallest positive angle of rotational symmetry, in degrees.",value,
                        [("Divide a full turn by the rotational order",value)],{"n":n},Fraction(180,n))
    k=r.randint(1,n-1)
    value=Fraction(360*k,n)
    return _problem(g,s,l,"repeated_rotation",f"A regular {n}-sided polygon is turned through {k} successive smallest positive symmetry rotations in the same direction. Calculate the total angle turned, in degrees.",value,
                    [("Smallest symmetry rotation",Fraction(360,n)),("Multiply by the number of rotations",value)],{"n":n,"k":k},Fraction(360,n))


def _circle(g,r,s,l):
    if l==1:
        a=r.randint(2,9); x=r.randint(2,30); b=r.randint(1,25); v=a*x+b
        return _problem(g,s,l,"equal_tangents",f"PA and PB are tangents from the same point P to a circle. PA is {tex(f'{a}x + {b}')} cm and PB is {tex(str(v))} cm. Calculate x.",x,
                        [("Tangents from the same external point have equal lengths",f"{a}x + {b} = {v}"),("Subtract the constant",v-b),("Divide by the coefficient",x)],{"a":a,"b":b,"length":v},Fraction(v+b,a))
    if l==2:
        length=2*r.randint(2,90)
        return _problem(g,s,l,"chord_midpoint",f"AB is a chord of length {tex(str(length))} cm. The line through the centre perpendicular to AB meets it at M. Calculate AM, in centimetres.",length//2,
                        [("The perpendicular from the centre bisects a chord",length//2)],{"length":length},length)
    d=r.randint(2,100)
    return _problem(g,s,l,"equal_chord_distances",f"Two equal chords of a circle have perpendicular distances d and {tex(str(d))} cm from its centre. Calculate d, in centimetres.",d,
                    [("Equal chords are equidistant from the centre",d)],{"distance":d},2*d)


def _locus(g,r,s,l):
    if l==1:
        a=r.randint(-50,10); gap=2*r.randint(1,35); b=a+gap
        return _problem(g,s,l,"equidistant_points",f"A has coordinates {tex(f'({a}, 0)')} and B has coordinates {tex(f'({b}, 0)')}. Points equidistant from A and B lie on a vertical line. Calculate its x-coordinate.",Fraction(a+b,2),
                        [("The equidistant line passes through the midpoint",Fraction(a+b,2))],{"a":a,"b":b},b-a)
    if l==2:
        h=r.randint(-15,15); k=r.randint(-15,15); radius=r.randint(1,30)
        return _problem(g,s,l,"point_distance_locus",f"P moves at a distance of {tex(str(radius))} units from C{tex(f'({h}, {k})')}. Calculate the greatest possible x-coordinate of P.",h+radius,
                        [("The locus is a circle; the rightmost point is one radius right of C",h+radius)],{"h":h,"k":k,"r":radius},h-radius)
    c=r.randint(-30,30); d=r.randint(1,30)
    return _problem(g,s,l,"line_distance_locus",f"P is {tex(str(d))} units from the line {tex(f'y = {c}')} and lies above that line. Calculate the y-coordinate of P.",c+d,
                    [("Use the parallel locus above the line",c+d)],{"c":c,"d":d},c-d)


def _kinematics(g,r,s,l):
    u=r.randint(2,25); a=r.randint(1,6); t=r.randint(2,25); v=u+a*t
    if l==1:
        distance=r.randint(20,200); time=r.randint(2,25)
        value=Fraction(distance,time)
        return _problem(g,s,l,"distance_time_gradient",f"A straight section of a distance-time graph represents {tex(str(distance))} metres travelled in {tex(str(time))} seconds. Calculate the speed, in metres per second.",value,
                        [("Gradient = change in distance divided by change in time",value)],{"distance":distance,"time":time},distance*time)
    if l==2:
        return _problem(g,s,l,"acceleration",f"Speed increases uniformly from {tex(str(u))} m/s to {tex(str(v))} m/s in {tex(str(t))} seconds. Calculate the acceleration, in metres per second squared.",a,
                        [("Change in speed",v-u),("Divide by elapsed time",a)],{"u":u,"v":v,"t":t},Fraction(v,t))
    if l==3:
        value=Fraction((u+v)*t,2)
        return _problem(g,s,l,"trapezium_distance",f"On a speed-time graph, speed increases in a straight line from {tex(str(u))} m/s at time 0 to {tex(str(v))} m/s at {tex(str(t))} seconds. Calculate the distance travelled in this interval, in metres.",value,
                        [("Mean speed for uniform acceleration",Fraction(u+v,2)),("Area of the trapezium = mean speed times time",value)],{"u":u,"v":v,"t":t},v*t)
    value=Fraction(v*t,2)
    return _problem(g,s,l,"braking_distance",f"Hilma records the motion of a test vehicle on a straight track. It slows uniformly from {tex(str(v))} m/s to rest in {tex(str(t))} seconds. Calculate the distance travelled while slowing, in metres.",value,
                    [("Mean speed while slowing uniformly to rest",Fraction(v,2)),("Multiply by the braking time",value)],{"v":v,"t":t},v*t)


def _functions(g,r,s,l):
    a=r.randint(2,9); b=r.randint(-20,20); x=r.randint(-20,20)
    if l==1:
        value=a*x+b
        return _problem(g,s,l,"function_value",f"The function f maps x to {tex(f'{a}x + ({b})')}. Calculate f({x}).",value,
                        [("Multiply the input by the coefficient",a*x),("Add the constant",value)],{"a":a,"b":b,"x":x},a*(x+b))
    if l==2:
        value=a*x+b
        return _problem(g,s,l,"function_input",f"Given {tex(f'f(x) = {a}x + ({b})')} and {tex(f'f(x) = {value}')}, calculate x.",x,
                        [("Subtract the constant from the output",value-b),("Divide by the coefficient",x)],{"a":a,"b":b,"output":value},Fraction(value+b,a))
    value=a*x*x+b
    return _problem(g,s,l,"nonlinear_function_value",f"Given {tex(f'f(x) = {a}x^2 + ({b})')}, calculate f({x}).",value,
                    [("Square the input first",x*x),("Multiply then add the constant",value)],{"a":a,"b":b,"x":x},(a*x)**2+b)


def _vectors(g,r,s,l):
    x1,y1,x2,y2=(r.randint(-30,30) for _ in range(4))
    if l==1:
        value=(x2-x1,y2-y1)
        return _problem(g,s,l,"displacement_components",f"A is {tex(f'({x1}, {y1})')} and B is {tex(f'({x2}, {y2})')}. Write down vector AB as an ordered pair of horizontal and vertical components.",value,
                        [("Horizontal displacement",x2-x1),("Vertical displacement",y2-y1)],{"A":[x1,y1],"B":[x2,y2]},(x1-x2,y1-y2),"vector")
    if l==2:
        return _problem(g,s,l,"reverse_vector",f"Vector AB has components {tex(f'({x1}, {y1})')}. Write down vector BA as an ordered pair.",(-x1,-y1),
                        [("Reverse the direction by negating both components",(-x1,-y1))],{"AB":[x1,y1]},(x1,y1),"vector")
    return _problem(g,s,l,"endpoint_from_displacement",f"A is {tex(f'({x1}, {y1})')} and vector AB has components {tex(f'({x2}, {y2})')}. Calculate the coordinates of B.",(x1+x2,y1+y2),
                    [("Add the horizontal component to A's x-coordinate",x1+x2),("Add the vertical component to A's y-coordinate",y1+y2)],{"A":[x1,y1],"AB":[x2,y2]},(x1-x2,y1-y2),"coordinates")


def _income(g,r,s,l):
    if l==1:
        hours=r.randint(20,50); rate=r.randint(20,80); sales=100*r.randint(10,90); pct=r.randint(1,9)
        value=hours*rate+sales*pct//100
        return _problem(g,s,l,"wages_commission",f"Selma works at Kudu Stationers. This week she works {hours} hours at N${rate} per hour and earns {pct}% commission on her sales of N${sales}. Calculate her total earnings for the week, in Namibian dollars.",value,
                        [("Hourly earnings",hours*rate),("Commission on sales",sales*pct//100),("Add both earnings",value)],{"hours":hours,"rate":rate,"sales":sales,"pct":pct},hours*rate)
    if l==2:
        old=r.randint(100,900); units=r.randint(10,190); charge=r.randint(2,8); fixed=r.randint(20,100)
        value=units*charge+fixed
        return _problem(g,s,l,"meter_bill",f"Tangeni’s household receives a water bill for one month. The previous meter reading is {old} and the current reading is {old+units}, both in cubic metres. The supplied tariff charges N${charge} per cubic metre and a fixed monthly charge of N${fixed}. Calculate the bill for the month, in Namibian dollars.",value,
                        [("Subtract the meter readings",units),("Cost of units used",units*charge),("Add the fixed charge",value)],{"previous":old,"current":old+units,"charge":charge,"fixed":fixed},units*charge)
    threshold=1000*r.randint(20,80); excess=100*r.randint(1,300); pct=r.randint(10,35); base=100*r.randint(0,50)
    value=base+excess*pct//100
    return _problem(g,s,l,"fictional_tax_table",f"Petrus earns N${threshold+excess} in one year. For this exercise, use the following annual tax rule: up to N${threshold}, tax is N${base}; above N${threshold}, tax is N${base} plus {pct}% of income above N${threshold}. Calculate Petrus’s annual income tax, in Namibian dollars.",value,
                    [("Income above the threshold",excess),("Tax on the excess",excess*pct//100),("Add the base tax",value)],{"threshold":threshold,"income":threshold+excess,"pct":pct,"base":base},(threshold+excess)*pct//100+base)


def _charts(g,r,s,l):
    counts=[r.randint(2,40) for _ in range(4)]
    if l==1:
        i=r.randbelow(4); value=counts[i]
        return _problem(g,s,l,"frequency_table",f"A bar chart records the numbers of learners at Kudu School choosing athletics (A), basketball (B), cricket (C) and dancing (D). The frequencies, in that order, are {tex(', '.join(map(str,counts)))}. Write down the frequency for category {chr(65+i)}.",value,
                        [("Use the entry corresponding to the named category",value)],{"counts":counts,"i":i},sum(counts))
    if l==2:
        symbols=r.randint(2,20); key=r.randint(2,12); half=r.randbelow(2)
        if half and key % 2:
            key += 1  # a half symbol must still represent a whole number of learners
        value=Fraction(2*symbols+half,2)*key
        return _problem(g,s,l,"pictogram_key",f"In a pictogram one full symbol represents {key} learners. A row has {symbols} full symbols"+(" and one half symbol" if half else "")+". Calculate the number of learners represented.",value,
                        [("Count symbols including any half symbol",Fraction(2*symbols+half,2)),("Multiply by the key",value)],{"symbols":symbols,"key":key,"half":half},symbols+key)
    if l==3:
        total=12*r.randint(3,25); n=r.randint(1,11); value=30*n
        return _problem(g,s,l,"pie_sector_angle",f"At Kudu School, {total} learners each choose their favourite sport. Of these, {total*n//12} choose football. Calculate the angle of the football sector in a pie chart, in degrees.",value,
                        [("Fraction choosing football",Fraction(n,12)),("Multiply by 360 degrees",value)],{"total":total,"football":total*n//12},total*n//12)
    start=r.randint(10,80); end=r.randint(10,80); dt=r.randint(2,12)
    value=Fraction(end-start,dt)
    return _problem(g,s,l,"line_chart_change",f"A line chart shows the number of bicycles available at Dune Cycle Hire. There are {start} bicycles at the start of a {dt}-hour period and {end} at the end. Calculate the average change in the number available per hour over this interval.",value,
                    [("Subtract the first reading from the last",end-start),("Divide by elapsed hours",value)],{"start":start,"end":end,"dt":dt},Fraction(start-end,dt))


def _histogram(g,r,s,l):
    left=5*r.randint(0,15); width=r.choice((5,10,15,20)); density=r.randint(1,18); freq=width*density
    if l==1:
        return _problem(g,s,l,"class_width",f"A histogram shows learners’ journey times to Kudu School, where x is the time in minutes. One class interval is {tex(f'{left} <= x < {left+width}')}. Calculate its class width.",width,
                        [("Upper class boundary minus lower class boundary",width)],{"left":left,"right":left+width},left+width)
    if l==2:
        return _problem(g,s,l,"frequency_density",f"A histogram shows learners’ journey times to Kudu School, where x is the time in minutes. The class {tex(f'{left} <= x < {left+width}')} has frequency {freq}. Calculate its frequency density.",density,
                        [("Class width",width),("Frequency divided by class width",density)],{"left":left,"right":left+width,"frequency":freq},freq)
    if l==3:
        return _problem(g,s,l,"frequency_from_density",f"A histogram shows learners’ journey times to Kudu School, where x is the time in minutes. One bar spans {tex(f'{left} <= x < {left+width}')} and has frequency density {density}. Calculate the frequency for this class.",freq,
                        [("Class width",width),("Bar area = width times frequency density",freq)],{"left":left,"right":left+width,"density":density},density)
    w2=r.choice(tuple(w for w in (5,10,15,20) if w != width)); d2=r.randint(1,18); total=freq+w2*d2
    return _problem(g,s,l,"unequal_width_total",f"Tangeni records journey times, in minutes, for a group of learners. The histogram of these times has exactly two classes. The first has width {width} and frequency density {density}; the second has width {w2} and frequency density {d2}. Calculate the total frequency.",total,
                    [("Area of first bar",freq),("Area of second bar",w2*d2),("Add the bar areas",total)],{"widths":[width,w2],"densities":[density,d2]},density+d2)


class TextLessonGenerator(MathGenerator):
    def __init__(self, slug, lesson_id, builder: Callable, skills, notes):
        self.generator_id="nssco_"+slug
        self.lesson_id=lesson_id
        self.version=1
        self.levels=tuple(range(1,len(skills)+1))
        self.level_skills={i:(skill,) for i,skill in enumerate(skills,1)}
        self.error_notes={skill:{"wrong_operation":note} for skill,note in zip(skills,notes)}
        self.builder=builder

    def _build(self,rng,seed,level):
        return self.builder(self,rng,seed,level)


GENERATORS = [
    TextLessonGenerator("geometrical_terms",15808,_geometry,("angle_vocabulary","prism_faces","isosceles_angles"),
                        ("used the wrong angle category","counted only the lateral faces","subtracted only one base angle")),
    TextLessonGenerator("constructions_scale_drawings",15810,_construction,("scale_length","angle_bisection","perpendicular_bisection"),
                        ("divided by the scale denominator","doubled instead of halving the angle","used the whole segment instead of half")),
    TextLessonGenerator("symmetry_two_dimensions",15812,_symmetry,("regular_polygon_symmetry","rotation_angle","repeated_rotation"),
                        ("doubled the number of sides","divided a half turn instead of a full turn","gave one rotation rather than all the rotations")),
    TextLessonGenerator("symmetry_circles",15813,_circle,("equal_tangents","chord_midpoint","equal_chord_distances"),
                        ("added the constant instead of subtracting it","used the entire chord instead of half","doubled the distance despite the chords being equal")),
    TextLessonGenerator("locus_numeric",15816,_locus,("equidistant_points","point_distance_locus","line_distance_locus"),
                        ("used the separation rather than the midpoint","used the leftmost point instead of the rightmost","used the locus below the line instead of above")),
    TextLessonGenerator("kinematics_rate_change",15828,_kinematics,("distance_time_gradient","acceleration","trapezium_distance","braking_distance"),
                        ("multiplied distance by time instead of dividing","used final speed rather than change in speed","used final speed throughout","used initial speed throughout the braking interval")),
    TextLessonGenerator("introduction_functions",15830,_functions,("function_value","function_input","nonlinear_function_value"),
                        ("added the constant before multiplying","added the constant instead of subtracting it","squared the coefficient as well as the input")),
    TextLessonGenerator("introduction_vectors",15838,_vectors,("displacement_components","reverse_vector","endpoint_from_displacement"),
                        ("reversed the direction of the displacement","kept the original direction","subtracted the displacement instead of adding it")),
    TextLessonGenerator("income_taxes_bills",15800,_income,("wages_commission","meter_bill","fictional_tax_table"),
                        ("omitted the commission","omitted the fixed charge","applied the marginal rate to all the income")),
    TextLessonGenerator("reading_charts_text","topic12_charts",_charts,("frequency_table","pictogram_key","pie_sector_angle","line_chart_change"),
                        ("gave the total instead of the named category","added symbol count and key","gave the frequency instead of the sector angle","reversed the subtraction")),
    TextLessonGenerator("histograms_text","topic12_histograms",_histogram,("class_width","frequency_density","frequency_from_density","unequal_width_total"),
                        ("gave the upper boundary instead of the width","used frequency without dividing by width","used height without multiplying by width","added heights instead of bar areas")),
]
