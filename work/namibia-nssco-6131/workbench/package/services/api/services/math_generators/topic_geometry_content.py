"""Existing mensuration/geometry examples, with formula substitution and reasons."""
from .topic_teaching import *

LABELS={
'nssco_perimeters_areas_polygons':{1:'Areas and perimeters of basic polygons',2:'Trapezium areas and missing heights',3:'Combining a triangle and rectangle',4:'Combining squares and circles'},
'nssco_circles_arcs_sectors':{1:'Circle area and circumference',2:'Sector area and arc length',3:'Finding a radius or sector angle',4:'Sector perimeters and circular segments',5:'Segments and concentric rings'},
'nssco_surface_area_volume':{1:'Cuboid and cylinder measures',2:'Volumes of spheres, cones and pyramids',3:'Curved surface areas',4:'Combining or halving solids',5:'Missing dimensions and compound solids'},
'nssco_similarity_scale_factors':{1:'Corresponding lengths',2:'Lengths and areas',3:'Lengths and volumes',4:'Converting area and volume ratios'},
'nssco_bisectors_numeric':{1:'Halving or doubling a bisected angle',2:'Using a perpendicular bisector',3:'Angle sums with a bisector'},
'nssco_angles_lines_polygons':{1:'Straight lines, opposite angles and a full turn',2:'Triangle and exterior angles',3:'Angles with parallel lines',4:'Polygon angle sums',5:'Multi-step polygon and ratio angles'},
'nssco_angles_circles':{1:'Centre, circumference and semicircle angles',2:'Same-segment and cyclic angles',3:'Radii, tangents and isosceles triangles',4:'Tangent pairs and alternate segments',5:'Combining circle angle properties'},
}


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];gid=p.generator_id;lines=[];e=''
    if gid=='nssco_perimeters_areas_polygons':
        if t in ('rect_area','rect_perimeter'):
            l,w=m['length'],m['width'];lines=[f'A=lw={l}\\times{w}'] if t=='rect_area' else [f'P=2(l+w)=2({l}+{w})'];e=f'$l={l}$ is length and $w={w}$ width. Area $A$ counts square units; perimeter $P$ is the total boundary length. Choose the formula for the quantity actually requested.'
        elif t in ('triangle_area','parallelogram_area'):
            b,h=m['base'],m['height'];lines=['A='+frac(f'{b}\\times{h}',2)] if t=='triangle_area' else [f'A=bh={b}\\times{h}'];e=f'Base $b={b}$ and perpendicular height $h={h}$ are the matching dimensions. '+('A triangle occupies half the corresponding parallelogram, so include the factor $1/2$.' if t=='triangle_area' else 'Multiply base by perpendicular height. The slant side is not the height.')
        elif t in ('trapezium_area','trapezium_height'):
            a,b=m['a'],m['b'];lines=['A='+frac('(a+b)h',2)]
            if t=='trapezium_area':lines.append('A='+frac(f'({a}+{b})\\times{m["h"]}',2))
            else:lines.append('h='+frac('2A','a+b')+'='+frac(f'2\\times{m["area"]}',f'{a}+{b}'))
            e=f'$a={a}$ and $b={b}$ are the parallel sides; $h$ is their perpendicular separation. The trapezium’s area $A$ is their average length multiplied by $h$. '+('Substitute the given height and keep the half factor.' if t=='trapezium_area' else f'Here $A={m["area"]}$. Rearrange to $h=2A/(a+b)$ before substituting.')
        elif t=='right_triangle_perimeter':
            a,b=m['a'],m['b'];lines=[f'c=\\sqrt{{{a}^2+{b}^2}}',f'P={a}+{b}+\\sqrt{{{a*a+b*b}}}'];e=f'The two perpendicular sides are ${a}$ and ${b}$. Let $c$ name the hypotenuse: $c^2=a^2+b^2$. Find $c$ with Pythagoras, then add all three sides for perimeter $P$. Keep the square root unrounded until the final requested three-significant-figure answer.'
        elif t=='composite_area':
            a,b,c,h=(m[k] for k in ('a','b','c','h'));lines=[f'A_1={a}\\times{b}', 'A_2='+frac(f'{c}\\times{h}',2),f'A={a*b}+'+q(F(c*h)/2)];e=f'The described composite consists of a rectangle ${a}$ by ${b}$ and a triangle of base ${c}$ and perpendicular height ${h}$. $A_1$ and $A_2$ name their separate areas. Their interiors do not overlap, so add the two areas; do not halve the rectangle or add only the boundary lengths.'
        else:
            r=m['r'];lines=[f'r={r},\\quad d=2r={2*r}']
            if t in ('square_in_circle','circle_outside_square'):
                lines.append('A_{square}='+frac(f'({2*r})^2',2)+f'={2*r*r}')
                if t=='circle_outside_square':lines.extend([f'A_{{circle}}=\\pi({r})^2',f'A_{{remaining}}={r*r}\\pi-{2*r*r}'])
                e=f'The circle radius is $r={r}$, so its diameter $d={2*r}$ is the inscribed square’s diagonal. If the square side is $s$, Pythagoras gives $2s^2=d^2$, hence square area $d^2/2$. '+('Subtract this from circle area for the requested region.' if t=='circle_outside_square' else 'The diagonal is not the square side.')
            else:
                lines=[f'A_{{square}}=({2*r})^2',f'A_{{circle}}=\\pi({r})^2',f'A_{{remaining}}={4*r*r}-{r*r}\\pi'];e=f'The circle radius is ${r}$ and its diameter ${2*r}$ equals the containing square’s side. Subtract the circle area from the square area to get the uncovered region. This is different from an inscribed square, whose diagonal would equal the diameter.'
    elif gid=='nssco_circles_arcs_sectors':
        r=m.get('r');theta=m.get('theta')
        if t in ('area','circumference'):
            lines=[f'r={r}'];lines.append(f'A=\\pi r^2=\\pi({r})^2' if t=='area' else f'C=2\\pi r=2\\pi({r})')
            e=f'$r={r}$ is the radius; $A$ names circle area and $C$ circumference. '+('The question supplies a diameter: halve it first to get this radius. ' if m.get('given_diameter') else '')+('Area uses the radius squared and square units.' if t=='area' else 'Circumference is a boundary length and uses ordinary length units.')+' Keep $\\pi$ exact when asked for an answer in terms of pi.'
        elif t in ('sector_area','sector_arc','sector_perimeter'):
            fraction=frac(theta,360);lines=[f'r={r},\\quad\\theta={theta}^\\circ']
            if t=='sector_area':lines.append(f'A={fraction}\\pi({r})^2')
            else:lines.append(f'L={fraction}\\times2\\pi({r})')
            if t=='sector_perimeter':lines.append(f'P={fraction}\\times2\\pi({r})+2({r})')
            e=f'Radius $r={r}$ and centre angle $\\theta={theta}^\\circ$ make this sector ${fraction}$ of a full circle. Use that fraction of $\\pi r^2$ for area $A$ or $2\\pi r$ for arc length $L$. '+('The sector perimeter P also includes its two straight radii, so add $2r$ to the arc.' if t=='sector_perimeter' else 'Distinguish square area units from arc length units.')+' Keep exact pi until the requested final rounding.'
        elif t in ('radius_from_area','radius_from_circumference'):
            if t=='radius_from_area':lines=[f'A={r*r}\\pi','r=\\sqrt{'+frac('A',r'\pi')+'}=\\sqrt{'+frac(f'{r*r}\\pi',r'\pi')+'}']
            else:lines=[f'C={2*r}\\pi','r='+frac('C',r'2\pi')+'='+frac(f'{2*r}\\pi',r'2\pi')]
            e=f'$r$ is the unknown radius. '+('Area $A=\\pi r^2$, so divide the stated area by pi and take the positive square root.' if t=='radius_from_area' else 'Circumference $C=2\\pi r$, so divide the stated circumference by $2\\pi$.')+f' The pi factors cancel, leaving radius ${r}$ in the question’s length unit.'
        elif t in ('angle_from_arc','angle_from_area'):
            fraction=F(theta)/360
            given=q(fraction*(2*r if t=='angle_from_arc' else r*r))+r'\pi'
            denom=f'2\\pi({r})' if t=='angle_from_arc' else f'\\pi({r})^2'
            lines=[r'\frac{\theta}{360}='+frac(given,denom)+'='+q(fraction),r'\theta=360\times'+q(fraction)]
            e=f'The radius is ${r}$. Divide the given '+('arc length by the full circumference' if t=='angle_from_arc' else 'sector area by the full circle area')+f' to recover the fraction of a circle, ${q(fraction)}$. $\\theta$ is the unknown centre angle in degrees; multiply the circle fraction by $360^\\circ$.'
        elif t=='ring':
            R,r=m['big'],m['small'];lines=[f'A=\\pi R^2-\\pi r^2=\\pi({R})^2-\\pi({r})^2'];e=f'$R={R}$ is the outer radius and $r={r}$ the inner radius. The ring consists of the larger circle with the smaller concentric circle removed. Subtract their areas, not their radii, and retain pi if requested.'
        elif t=='segment_square':
            lines=[f'A_{{circle}}={r*r}\\pi',f'A_{{square}}=2({r})^2={2*r*r}','A_{segment}='+frac(f'{r*r}\\pi-{2*r*r}',4)]
            e=f'The inscribed square’s diagonal is the diameter $2r$, where $r={r}$. Its area is $2r^2$. Subtract it from circle area; the four equal circular segments divide the remainder equally. The requested one segment is a quarter of that remainder, not a quarter of the whole circle.'
        else:
            lines=[f'A_{{sector}}='+frac(theta,360)+f'\\pi({r})^2','A_{triangle}='+frac(f'({r})^2\\sin({theta}^\\circ)',2),'A_{segment}=A_{sector}-A_{triangle}']
            e=f'The segment is bounded by a chord and its arc. Radius $r={r}$ and centre angle $\\theta={theta}^\\circ$ define a sector containing an isosceles triangle. Subtract triangle area $r^2\\sin\\theta/2$ from sector area. Use degree mode and carry exact expressions until the final rounding.'
    elif gid=='nssco_surface_area_volume':
        r=m.get('r');h=m.get('h');lines=[]
        if t in ('cuboid_volume','cuboid_area'):
            l,w,h=m['l'],m['w'],m['h'];lines=[f'V=lwh={l}\\times{w}\\times{h}'] if t=='cuboid_volume' else [f'S=2(lw+lh+wh)=2({l}\\times{w}+{l}\\times{h}+{w}\\times{h})'];e=f'The cuboid length is ${l}$, width ${w}$ and height ${h}$. Volume V multiplies its three perpendicular dimensions. Total surface area S instead adds the six face areas, pairing the equal opposite faces. Choose the quantity requested and its cubic or square units.'
        elif t in ('sphere','hemisphere','cone','pyramid'):
            if t=='sphere':lines=['V='+frac(4,3)+f'\\pi({r})^3'];e=f'The sphere’s radius is ${r}$. Use the supplied sphere formula $V=4\\pi r^3/3$. Cube the radius; using the diameter here would multiply the volume by eight.'
            elif t=='hemisphere':lines=['V='+frac(1,2)+r'\times'+frac(4,3)+f'\\pi({r})^3'];e=f'The hemisphere radius is ${r}$. It is half a sphere, so halve $4\\pi r^3/3$. Do not halve the radius, which would change the volume by a cube factor.'
            elif t=='cone':lines=['V='+frac(f'\\pi({r})^2({h})',3)];e=f'The cone radius is ${r}$ and perpendicular height ${h}$. Volume is one third of circular base area times perpendicular height. Slant height belongs to a different formula and must not replace the vertical height here.'
            else:
                s=m['s'];lines=[f'B={s}^2', 'V='+frac(f'({s})^2({h})',3)];e=f'The square pyramid base has side ${s}$, so base area $B={s*s}$. Its perpendicular height is ${h}$. Volume is $Bh/3$, not the enclosing prism volume $Bh$.'
        elif t in ('cylinder_volume','cylinder','height_from_volume'):
            if t=='cylinder_volume':lines=[f'V=\\pi r^2h=\\pi({r})^2({h})'];e=f'Radius $r={r}$ and perpendicular height $h={h}$ define this cylinder. Volume V is circular base area $\\pi r^2$ multiplied by height. Keep the radius rather than diameter in the squared term.'
            elif t=='cylinder':lines=[f'S_{{curved}}=2\\pi rh=2\\pi({r})({h})'];e=f'The cylinder radius is ${r}$ and height ${h}$. Unwrapping its curved surface gives a rectangle with width the circumference $2\\pi r$ and height $h$. Their product is curved surface area; do not add circular ends unless total surface area is requested.'
            else:lines=[f'V={r*r*h}\\pi','h='+frac('V',r'\pi r^2')+'='+frac(f'{r*r*h}\\pi',f'\\pi({r})^2')];e=f'The cylinder radius is ${r}$. Rearrange $V=\\pi r^2h$ to divide the given volume by the circular base area. This gives height $h={h}$ in length units; dividing only by radius would not remove the area factor.'
        elif t in ('cone_height','cone_slant'):
            l=m['l'];lines=([f'l=\\sqrt{{{r}^2+{h}^2}}={l}'] if t=='cone_height' else [f'l={l}'])+[f'S_{{curved}}=\\pi rl=\\pi({r})({l})']
            e=f'The cone radius is $r={r}$ and slant height $l={l}$. '+(f'The stated perpendicular height is ${h}$; Pythagoras gives $l=\\sqrt{{r^2+h^2}}$ before the area calculation. ' if t=='cone_height' else '')+'Curved surface area is pi × radius × slant height. It excludes the circular base; perpendicular height cannot be substituted for slant height.'
        elif t=='cylinder_hemisphere':
            lines=[f'V_1=\\pi({r})^2({h})','V_2='+frac(2,3)+f'\\pi({r})^3','V=V_1+V_2'];e=f'The two solid parts share radius ${r}$: a cylinder of height ${h}$ and a hemisphere. $V_1$ and $V_2$ name their volumes. Add them once each; the hemisphere is half a sphere, not a cone. Use cubic units and round the combined value at the end.'
        elif t=='half_cylinder':
            L=m['length'];lines=['V='+frac(1,2)+f'\\pi({r})^2({L})'];e=f'The original cylinder has radius ${r}$ and length ${L}$. The solid is cut into two equal half-cylinders, so its volume is half the full cylinder volume. Halving the radius instead would give one quarter of the full volume.'
        elif t=='silo_curved':
            lines=[f'S_1=2\\pi({r})({h})',f'S_2=2\\pi({r})^2','S_{curved}=S_1+S_2'];e=f'The cylinder radius is ${r}$ and height ${h}$, with a hemispherical top of the same radius. $S_1$ is the cylinder’s curved area and $S_2$ the hemisphere’s curved area. Add only exposed curved surfaces, excluding the bottom and the internal joining circle.'
        else:
            d=F(m['d']);r=d/2;h=F(h);lines=['r='+frac(q(d),2)+'='+q(r),f'V=\\pi({q(r)})^2({q(h)})',label('Litres')+f'=1000\\pi({q(r)})^2({q(h)})'];e=f'The tank diameter is ${q(d)}$ metres and height ${q(h)}$ metres. Halve the diameter to radius ${q(r)}$, calculate cylinder volume in cubic metres, then multiply by $1000$ litres per cubic metre. Preserve precision before rounding the final capacity.'
        e+=' Keep exact pi where requested; otherwise round only the final requested measure. Volume uses cubic units and surface area square units.'
    elif gid=='nssco_similarity_scale_factors':
        a,b=m['a'],m['b'];k=F(b)/a;lines=['k='+frac(b,a)+'='+q(k)]
        if t=='similar_lengths':lines.append(f'L_2={m["c"]}\\times({q(k)})');e=f'Corresponding lengths ${a}$ and ${b}$ give linear scale factor $k={q(k)}$ in the required direction. The corresponding known length is ${m["c"]}$. Multiply it by this same factor; match corresponding sides before forming the ratio.'
        else:
            inverse=t in ('height_from_areas','height_from_volumes');sourcepower=2 if t=='height_from_areas' or t=='volume_from_area_ratio' else 3 if t in ('height_from_volumes','area_from_volume_ratio') else 1
            if sourcepower>1:lines.insert(0,label('Given measure scale factor')+'='+q(k**sourcepower));lines[1]='k='+ (r'\sqrt{'+q(k**2)+'}' if sourcepower==2 else r'\sqrt[3]{'+q(k**3)+'}')+'='+q(k)
            if inverse:base=m['h'];lines.append(f'h_2={base}\\times({q(k)})')
            elif 'area' in m:base=m['area'];lines.append(f'A_2={base}({q(k)})^2')
            else:base=m['v'];lines.append(f'V_2={base}({q(k)})^3')
            e=f'$k$ is the corresponding linear scale factor from the first similar shape to the second, here ${q(k)}$. Area ratios are $k^2$ and volume ratios $k^3$. '+('Take the square root of a supplied area ratio or cube root of a supplied volume ratio to recover k before changing measure type. ' if sourcepower>1 else '')+f'The known requested-type measure is ${base}$. '+('Multiply its length by k.' if inverse else 'Multiply its area by k squared.' if 'area' in m else 'Multiply its volume by k cubed.')+' Similarity preserves shape, not equal size.'
    else:
        if gid=='nssco_bisectors_numeric':
            if t=='half':lines=[r'\theta='+frac(m['whole'],2)];rule='An angle bisector divides the whole angle into two equal angles.'
            elif t=='double':lines=[f'\\theta=2({m["half"]})'];rule='The supplied angle is one of the two equal halves; double it to recover the whole angle.'
            elif t=='midpoint':lines=[f'AM=BM={m["am"]}'];rule='The perpendicular bisector passes through the midpoint, so the two segment lengths are equal.'
            elif t=='equal_distance':lines=[f'PA=PB={m["pa"]}'];rule='Every point on the perpendicular bisector of AB is equally distant from A and B.'
            elif t=='pythagoras':lines=[f'AM={m["half"]}',f'PM=\\sqrt{{{m["pa"]}^2-{m["half"]}^2}}'];rule='The perpendicular bisector first halves AB. The resulting triangle AMP is right-angled at M; PA is the hypotenuse, so subtract AM squared from PA squared to find PM squared.'
            else:lines=[r'\angle DBC='+frac(str(m['b'])+r'^\circ',2)+f'={m["b"]/2:g}^\\circ',rf'\angle BDC=180^\circ-{m["b"]/2:g}^\circ-{m["c"]}^\circ'];rule='The angle bisector halves angle ABC. Then use the 180-degree angle sum in triangle BDC, including its stated angle at C.'
        elif gid=='nssco_angles_lines_polygons':
            if t=='straight_line':lines=[f'\\theta=180-{m["a"]}-{m["b"]}'];rule='Adjacent angles on a straight line total 180 degrees.'
            elif t=='point':lines=[f'\\theta=360-{m["a"]}-{m["b"]}-{m["c"]}'];rule='The complete turn about a point totals 360 degrees.'
            elif t=='crossing_opposite':lines=[f'\\theta={m["x"]}'];rule='Vertically opposite angles made by two intersecting straight lines are equal.'
            elif t=='crossing_adjacent':lines=[f'\\theta=180-{m["x"]}'];rule='Adjacent angles at an intersection lie on a straight line, so total 180 degrees.'
            elif t=='exterior':lines=[f'\\theta={m["a"]}+{m["b"]}'];rule='An exterior triangle angle equals the sum of the two opposite interior angles.'
            elif t=='isosceles_apex':lines=[r'\theta='+frac(f'180-{m["apex"]}',2)];rule='An isosceles triangle has two equal base angles. Subtract the given apex angle from 180, then share the remainder equally.'
            elif t=='isosceles_base':lines=[f'\\theta=180-2({m["base"]})'];rule='The two base angles are equal. Subtract both from the triangle’s 180-degree total.'
            elif t=='parallel_lines':lines=[f'\\angle {m["find"]}='+('180-' if m['relation']=='sum' else '')+str(m['x'])];rule=p.steps[0].description+'. Use the named rays in the question to distinguish corresponding/alternate equal pairs from supplementary pairs.'
            elif t=='sides_from_exterior':lines=['n='+frac(360,360//m['n'])];rule='Exterior angles of a regular polygon total 360 degrees. Divide that full turn by one exterior angle to find the number of sides n.'
            elif t=='sum_interior':lines=[f'S=({m["n"]}-2)180'];rule='An n-sided polygon can be divided into n minus two triangles, so its interior angle sum S is (n-2) times 180 degrees.'
            elif t=='interior_regular':lines=[r'\theta='+frac(f'({m["n"]}-2)180',m['n'])];rule='The interior angle sum is (n-2) times 180. A regular polygon shares this equally among n equal angles.'
            elif t=='unknown_angle':lines=[f'S=({m["n"]}-2)180',f'{m["k"]}x=S-('+'+'.join(map(str,m['known']))+')','x='+frac(f'({m["n"]}-2)180-('+'+'.join(map(str,m['known']))+')',m['k'])];rule='Subtract all known interior angles from the polygon’s total, then divide the remainder among the k equal angles x. Do not divide by the total number of sides.'
            elif t=='regular_diagonal':lines=[r'\theta='+frac('180-('+frac(f'({m["n"]}-2)180',m['n'])+')',2)];rule='The two consecutive sides of the regular polygon make an isosceles triangle with the diagonal. Its apex is one polygon interior angle; share the remaining triangle angle sum between the two equal base angles.'
            else:
                parts=m['parts'];lines=['u='+frac(360,sum(parts)),r'\theta='+frac(f'360\\times{max(parts)}',sum(parts))];rule='The four interior angles of a quadrilateral total 360 degrees. Divide by the sum of the ratio parts to find one part u, then multiply by the largest part for the largest angle.'
        else:
            x=m.get('x',m.get('y'));calc={
                'at_circumference':frac(x,2),'at_centre':f'2({x})','reflex':f'2({x})',
                'semicircle':f'180-90-{x}','same_segment':str(x),'cyclic_adc':f'180-{x}','cyclic_bcd':f'180-{x}',
                'tangent_triangle':f'180-90-{x}','tangent_chord_radius':f'90-{x}', 'radii_isosceles':frac(f'180-{x}',2),
                'tangent_pair_aob':f'360-90-90-{x}','tangent_pair_pab':frac(f'180-{x}',2),
                'alt_segment_acb':str(x),'alt_segment_oab':f'90-{x}','alt_segment_aob':f'2({x})',
                'oac':frac(f'180-{x}',2),'obt_tangent':f'90-{x}','adc':'180-'+frac(x,2)}
            lines=[r'\theta='+calc[t]];rule=' '.join(step.description+'.' for step in p.steps)
            if t=='obt_tangent':
                lines=[rf'\angle OAB=90^\circ-{x}^\circ={90-x}^\circ',rf'\angle OBA=\angle OAB={90-x}^\circ']
                rule='The radius is perpendicular to the tangent at A. Subtract the given angle from 90 degrees to find angle OAB. Since OA and OB are equal radii, triangle OAB has equal base angles OAB and OBA.'
        data='' # Instance evidence is already stated in the authored operations; do not label derived values as givens.
        e=rule+' '+('$\\theta$ denotes the requested angle in degrees. ' if (gid!='nssco_bisectors_numeric' and t!='obt_tangent') or t in ('half','double') else 'Use the named points to distinguish the requested angle or length from a whole angle or segment. ')+'State the geometric reason with the calculation; do not rely on an imagined diagram being to scale.'
    return finish(p,lines,e)
