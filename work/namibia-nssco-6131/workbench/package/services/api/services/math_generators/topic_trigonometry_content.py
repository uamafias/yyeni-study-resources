"""Trig setup, degree-mode calculation and explicit geometry-to-formula links."""
import re
from .topic_teaching import *

LABELS={
'nssco_bearings_right_angled_triangles':{1:'Finding a side using a trig ratio',2:'Finding an angle using an inverse ratio',3:'Pythagoras with longer or shorter sides',4:'Back bearings and changes of course',5:'Right-angle journeys and bearings'},
'nssco_elevation_depression_extended_ratios':{1:'Elevation heights and horizontal distances',2:'Depression distances and angles',3:'Calculator expressions in degree mode',4:'All trig-equation solutions in a range',5:'Exact signed ratios and expressions'},
'nssco_sine_cosine_rules':{1:'Triangle area from two sides and an angle',2:'Cosine rule for an unknown side',3:'Sine rule for a side or angle',4:'Cosine rule for an unknown angle',5:'Area-to-angle and three-dimensional triangles'},
}


def trig_math(text):
    text=authored_math(text.replace(' x ',r'\times '))
    text=re.sub(r'(?<![\\a-z])(sin|cos|tan)\^-1',r'\\\1^{-1}',text)
    text=re.sub(r'(?<![\\a-z])(sin|cos|tan)\s+(-?\d+(?:\.\d+)?)',r'\\\1(\2^\\circ)',text)
    text=re.sub(r'(?<![\\a-z])(sin|cos|tan)\s+([A-Za-z])',r'\\\1(\2)',text)
    return text


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];lines=[]
    if t in ('area','area_exact'):
        a,b,C=m['a'],m['b'],m['C'];lines=['S='+frac('ab\\sin C',2)+'='+frac(f'{a}\\times{b}\\times\\sin({C}^\\circ)',2)]
        e=f'$S$ is triangle area. The given sides are $a={a}$ and $b={b}$, with included angle $C={C}^\\circ$ between them. Use $S=ab\\sin C/2$; the included angle requirement matters. '+('The sine of 30 or 150 degrees is exactly one half, so an exact result is possible.' if t=='area_exact' else 'Use degree mode and retain full calculator precision until the final answer.')
    elif t=='cosine_rule_side':
        a,b,C=m['a'],m['b'],m['C'];lines=[f'c^2={a}^2+{b}^2-2({a})({b})\\cos({C}^\\circ)',f'c=\\sqrt{{{a}^2+{b}^2-2({a})({b})\\cos({C}^\\circ)}}']
        e=f'The known sides are $a={a}$ and $b={b}$ and their included angle $C={C}^\\circ$. The unknown c is opposite C. Apply the cosine rule, including the whole subtracted $2ab\\cos C$ term, then take the positive square root. Omitting that term would incorrectly assume a right angle.'
    elif t=='sine_rule_side':
        a,A,B=m['a'],m['A'],m['B'];lines=[frac('b',f'\\sin({B}^\\circ)')+'='+frac(a,f'\\sin({A}^\\circ)'), 'b='+frac(f'{a}\\sin({B}^\\circ)',f'\\sin({A}^\\circ)')]
        e=f'Side $a={a}$ is opposite angle $A={A}^\\circ$. Unknown b is opposite $B={B}^\\circ$. Keep each side paired with its own opposite angle in the sine rule. Rearrange for b before calculating; reversing one fraction alone changes the relationship.'
    elif t=='sine_rule_angle':
        a,b,A=m['a'],m['b'],m['A'];lines=[r'\sin B='+frac(f'{b}\\sin({A}^\\circ)',a),r'B=\sin^{-1}\left('+frac(f'{b}\\sin({A}^\\circ)',a)+r'\right)']
        e=f'Sides $a={a}$ and $b={b}$ are opposite angles $A={A}^\\circ$ and B. The sine rule first gives sin B, not B itself; use inverse sine in degree mode. The supplementary sine angle must also fit the triangle’s remaining-angle sum; use the problem’s angle conditions to choose the valid result.'
    elif t=='cosine_rule_angle':
        a,b,c=m['a'],m['b'],m['c'];ratio=frac(f'{a}^2+{b}^2-{c}^2',f'2({a})({b})');lines=[r'\cos C='+ratio,r'C=\cos^{-1}\left('+ratio+r'\right)']
        e=f'The three sides are $a={a}$, $b={b}$ and $c={c}$; C is opposite side c. Rearrange the cosine rule to $\\cos C=(a^2+b^2-c^2)/(2ab)$. Use inverse cosine to obtain the angle. A negative cosine correctly gives an obtuse angle; do not remove its sign.'
    elif t=='area_to_angle':
        a,b,S=m['a'],m['b'],m['area'];ratio=frac(f'2({S})',f'{a}({b})');lines=[f'{S}='+frac(f'{a}({b})\\sin C',2),r'\sin C='+ratio,r'C=\sin^{-1}\left('+ratio+r'\right)']
        e=f'Triangle area is $S={S}$ and the two enclosing sides are $a={a}$ and $b={b}$. Rearrange $S=ab\\sin C/2$ to isolate sin C, then use inverse sine in degree mode. The question asks for the specified acute included angle; its supplementary angle would have the same sine but fail that condition.'
    elif t in ('pyramid_diagonal','pyramid_height'):
        l,w=m['l'],m['w'];lines=[f'd=\\sqrt{{{l}^2+{w}^2}}']
        e=f'The rectangular base has side lengths ${l}$ and ${w}$. Its diagonal d follows from Pythagoras in the base plane. '
        if t=='pyramid_height':
            edge=m['e'];lines+=['r='+frac('d',2),f'h=\\sqrt{{{edge}^2-('+frac(f'{l}^2+{w}^2',4)+')}']
            e+=f'The apex is above the base centre and its sloping edge has length ${edge}$. The centre-to-corner distance r is half the base diagonal. In the vertical right triangle, that edge is the hypotenuse: subtract r squared to find height h squared. Keep the diagonal exact; do not substitute a rounded intermediate distance.'
        else:e+='This is the full corner-to-corner diagonal, not the distance from the base centre to a corner. Use the positive root and requested length units.'
    elif t in ('right_angle_side','right_angle_angle','elevation_height','elevation_distance','depression_distance','depression_angle'):
        lines=[trig_math(step.value) for step in p.steps if step.description!='Round the answer']
        names={'h':'vertical height','d':'horizontal ground distance','L':'sloping hypotenuse length','A':'requested angle'}
        used=[f'${k}$ is {v}' for k,v in names.items() if re.search(r'\b'+k+r'\b',' '.join(step.value for step in p.steps))]
        e='; '.join(used)+'. In the stated right triangle, label opposite and adjacent relative to the given angle; the hypotenuse is opposite the right angle. Use sine = opposite/hypotenuse, cosine = adjacent/hypotenuse, or tangent = opposite/adjacent according to the known and requested sides. '
        if t.startswith('depression'):e+='The two horizontals are parallel, so the angle of depression equals the corresponding angle of elevation. '
        if t in ('right_angle_angle','depression_angle'):e+='The side quotient is a trig ratio; apply the appropriate inverse function to recover the angle. '
        e+='The equations show this instance’s actual values. Use degree mode and round only the final requested length or angle.'
    elif t=='pythagoras':
        lines=[trig_math(p.steps[0].value), 'd=\\sqrt{'+p.steps[1].value+'}']
        e='The described sides form a right triangle. $d$ is the unknown length. '+('To find the longest side, add the squares of the two perpendicular sides.' if p.skill=='pythagoras_hypotenuse' else 'To find a shorter side, subtract the known shorter side squared from the hypotenuse squared.')+' The first equation substitutes the actual lengths. Take the positive square root, retain full precision, and include the requested length unit.'
    elif t in ('back_bearing','bearing_turn'):
        lines=[trig_math(p.steps[0].value),label('Reduce by whole turns if necessary'),label('Bearing')+f'={int(m["answer"]):03d}^\\circ']
        e='A bearing is measured clockwise from north and lies in the 0-to-360-degree turn. '+('Reversing direction changes a bearing by 180 degrees: add 180 if below 180, otherwise subtract 180.' if t=='back_bearing' else 'Add a clockwise course change or subtract an anticlockwise change, as stated in the question.')+' Remove whole 360-degree turns if necessary. Write a whole-degree bearing using three digits, including leading zeros.'
    elif t in ('journey_distance','journey_bearing'):
        a,b=m['legs']
        if t=='journey_distance':
            lines=[f'd^2={a}^2+{b}^2',f'd=\\sqrt{{{a*a+b*b}}}'];e=f'The journey legs are ${a}$ and ${b}$ in perpendicular directions. Their sum is the travelled distance, but d is the direct start-to-finish separation. Use Pythagoras for that right-triangle hypotenuse, keeping full precision before rounding.'
        else:
            bearing=m['bearing'];sign='+' if m['right'] else '-';lines=[r'A=\tan^{-1}\left('+frac(b,a)+r'\right)',f'B_{{forward}}={bearing}^\\circ{sign}A',r'B_{back}=B_{forward}+180^\circ',label('Reduce into the 0 to 360 degree range')]
            e=f'The first leg is ${a}$ on bearing ${bearing}^\\circ$, followed by a perpendicular leg ${b}$. A names the angle between the first leg and the direct route, found by tan A = second leg / first leg. Turn from the original bearing '+('clockwise' if m['right'] else 'anticlockwise')+' by A for the forward bearing, then reverse it by 180 degrees because the question asks for the start from the finish. Reduce by whole turns and round the requested angle.'
    elif t in ('calculator_difference','calculator_fraction'):
        expression=re.findall(r'\$([^$]+)\$',p.question)[0];lines=[expression]
        e=f'The required expression is ${expression}$. Use degree mode, preserve the displayed fraction and subtraction order, and keep full calculator precision. Individual function values can be negative outside the first quadrant; do not replace them with positive reference-angle values. Round the whole expression only at the final requested decimal place.'
    elif t=='solve_trig_equation':
        fn=m['fn'];k=m['k'];signed=-m['m'] if m['negative'] else m['m'];ratio=F(signed)/k
        lines=[f'\\{fn} x='+q(ratio),label('Solutions in the stated inclusive range')+':\\quad '+r',\quad '.join(f'x={v}^\\circ' for v in m['solutions'])]
        e=f'$x$ is the unknown angle, and the given equation reduces to ${fn}\\,x={q(ratio)}$. The scalar coefficient is ${k}$, not an angle multiplier. Use an inverse function for a reference/principal angle, then use the trig function’s signs and symmetries to find every solution between $0^\\circ$ and $360^\\circ$ inclusive. Sine is positive in quadrants I/II, cosine in I/IV, and tangent in I/III. Include endpoints only if they satisfy the original equation.'
    elif t in ('exact_ratio','exact_expression'):
        if t=='exact_ratio':
            sine,cosine=F(m['sin']),F(m['cos']);lines=[r'\sin\theta='+q(sine),r'\cos\theta='+q(cosine),r'\tan\theta='+frac(q(sine),q(cosine))]
        else:
            tangent=F(p.steps[0].value);sine=F(p.steps[1].value);a,b=m['p'],m['q'];lines=[r'\tan\theta='+q(tangent),r'\sin\theta='+q(sine),f'{a}\\tan\\theta+{b}\\sin\\theta=({a})({q(tangent)})+({b})({q(sine)})']
        e=f'The angle $\\theta$ lies in quadrant {m["quadrant"]}, as specified by the given range. Use the given exact ratio and Pythagoras to obtain any missing reference-triangle side, then assign sine/cosine signs from that quadrant. Tangent is sin θ divided by cos θ. Keep signed fractions exact; '+('substitute both exact ratios into the displayed expression before combining.' if t=='exact_expression' else 'simplify the resulting common fraction rather than using a rounded inverse angle.')
    else:raise ValueError(t)
    return finish(p,lines,e)
