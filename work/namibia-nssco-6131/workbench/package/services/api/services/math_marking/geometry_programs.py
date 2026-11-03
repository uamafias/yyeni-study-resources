"""Task-specific geometry operations, with instance-bound achievement names."""
from fractions import Fraction
from .operation_reasons import operation_reason
from .solution_programs import Author
from .formatting_adapter import q


def geometry_program(p,content):
    f=p.generator_id.removeprefix('nssco_');m=p.machine;t=m.get('task',p.skill)
    a=Author(p,content);add=a.add;n=len(a.rows);awards=()
    if f=='perimeters_areas_polygons':
        if t=='right_triangle_perimeter':
            add('hypotenuse','Find the missing side','The supplied sides are perpendicular, so their squares sum to the hypotenuse square.',[0])
            add('boundary','Form the complete boundary sum','Perimeter contains all three side lengths; keep the exact root until final rounding.',[1]);awards=('hypotenuse','boundary')
        elif t=='composite_area':
            add('components','Calculate the component areas','The rectangle uses length × width and the triangle uses half base × perpendicular height.',[0,1])
            add('combine','Add the non-overlapping areas','The requested composite consists of these two regions with no overlap.',[2]);awards=('components','combine')
        elif t in ('square_in_circle','circle_outside_square','left_over'):
            r=m['r']
            if t=='left_over':
                add('components','Calculate square and circle areas','The containing square has side equal to the circle diameter.',[0,1])
                add('difference','Subtract the circular region','The remaining square region excludes the circle.',range(2,n));awards=('components','difference')
            else:
                add('diagonal','Relate the square diagonal to the diameter','An inscribed square has diagonal equal to the circle diameter.',[0])
                add('square','Use the diagonal to obtain square area','Pythagoras gives twice the square side squared equal to the diagonal squared.',[1])
                if t=='circle_outside_square':
                    add('circle','Calculate the circle area','Circle area is π times radius squared.',[2])
                    add('difference','Remove the inscribed square','Subtract square area from circle area for the requested region.',[3]);awards=('square','difference')
                else:awards=('diagonal','square')
        elif t in ('trapezium_area','trapezium_height'):
            add('relationship','Use the trapezium area relationship','Area is the average parallel-side length multiplied by perpendicular height.',[0])
            add('apply','Substitute or rearrange for the requested quantity','Use the two parallel sides; a slant side is not the perpendicular height.',range(1,n))
        else:add('measure','Apply the requested polygon measure',operation_reason(f,t),range(n))
    elif f=='circles_arcs_sectors':
        if t=='ring':
            R,r=m['big'],m['small']
            add('circles','Calculate the outer and inner circle areas','Each circle area uses its own radius squared.',expression=rf'A_{{outer}}=\pi({R})^2,\quad A_{{inner}}=\pi({r})^2')
            add('difference','Subtract the inner region','The ring is the outer disc with the inner disc removed.',expression=rf'A=\pi({R})^2-\pi({r})^2');awards=('circles','difference')
        elif t=='sector_perimeter':
            add('arc','Find the sector arc length','The arc is the stated angle fraction of the full circumference.',range(n-1))
            add('boundary','Include both straight radii','A sector boundary contains its arc and two radii.',[n-1]);awards=('arc','boundary')
        elif t=='segment_square':
            add('components','Find the circle and inscribed-square areas','The square diagonal is the diameter, giving square area 2r².',range(n-1))
            add('segment','Take one quarter of the difference','Four congruent circular segments share the region outside the square.',[n-1]);awards=('components','segment')
        elif t=='segment_chord':
            add('sector','Calculate the sector area','The central angle determines its fraction of a full disc.',[0])
            add('triangle','Calculate the isosceles triangle area','Two radii enclose the given angle, so area is half r² sin θ.',[1])
            add('segment','Subtract triangle from sector','The segment is the portion of the sector beyond its chord.',range(2,n));awards=('sector','segment')
        elif t in ('radius_from_area','radius_from_circumference'):
            add('relationship','Write the supplied circle measure','Choose area πr² or circumference 2πr to match the given quantity.',[0])
            add('radius','Isolate the radius','Divide out the full coefficient and take the positive square root only when the radius is squared.',range(1,n))
        elif t in ('angle_from_arc','angle_from_area'):
            add('fraction','Recover the fraction of a full circle','Divide arc by circumference or sector area by full circle area.',[0])
            add('angle','Express that fraction in degrees','A full circle is 360°, so multiply its fraction by 360.',range(1,n))
        elif t in ('sector_area','sector_arc'):
            add('sector','Apply the angle fraction','The sector occupies θ/360 of the full circle; apply this to area or circumference as requested.',range(n))
        else:add('circle','Apply the circle measure',operation_reason(f,t),range(n))
    elif f=='surface_area_volume':
        r=m.get('r');h=m.get('h')
        if t=='cone_height':
            add('slant','Find the slant height','Radius, perpendicular height and slant height form a right triangle.',expression=rf'l=\sqrt{{{r}^2+{h}^2}}={m["l"]}')
            add('curved','Apply the cone curved-area formula','Curved area uses the slant height, not the perpendicular height.',expression=rf'S=\pi r l=\pi({r})({m["l"]})');awards=('slant','curved')
        elif t=='height_from_volume':
            coefficient=r*r*h
            add('volume_equation','Substitute into the cylinder volume relationship','Cylinder volume is circular base area multiplied by perpendicular height.',expression=rf'{coefficient}\pi=\pi({r})^2h')
            add('isolate','Divide by the complete base area','The π factors cancel; divide by radius squared rather than radius.',expression=rf'h=\frac{{{coefficient}\pi}}{{\pi({r})^2}}');awards=('volume_equation','isolate')
        elif t=='half_cylinder':
            length=m['length']
            add('full_volume','Form the complete cylinder volume','A cylinder is a circular cross-section extended through its length.',expression=rf'V_{{full}}=\pi({r})^2({length})')
            add('half','Take half of the complete volume','A longitudinal half-cylinder contains half the full cylinder volume, with unchanged radius.',expression=rf'V=\frac12\pi({r})^2({length})');awards=('full_volume','half')
        elif t=='cylinder_hemisphere':
            add('components','Calculate the two component volumes','Use cylinder πr²h and hemisphere half of 4πr³/3.',range(n-1))
            add('combine','Add the component volumes','The joined components have non-overlapping interiors.',[n-1]);awards=('components','combine')
        elif t=='litres':
            add('radius','Convert diameter to radius','Cylinder volume uses radius, half the supplied diameter.',[0])
            add('volume','Calculate cylinder volume in cubic metres','Multiply the circular base area by the perpendicular height.',[1])
            add('capacity','Convert cubic metres to litres','One cubic metre contains 1000 litres; apply this factor after finding volume.',range(2,n));awards=('volume','capacity')
        elif t=='silo_curved':
            add('components','Calculate the exposed cylinder and dome areas','The cylinder contributes 2πrh and a hemispherical dome contributes 2πr².',range(n-1))
            add('combine','Combine exposed curved surfaces','Include the two exposed curved components, excluding the joined circular interface.',[n-1]);awards=('components','combine')
        else:add('solid','Apply the appropriate solid formula',operation_reason(f,t),range(n))
    elif f=='similarity_scale_factors':
        if t in ('volume_from_heights','area_from_heights'):
            add('linear','Find the corresponding length scale factor','The ratio of corresponding lengths is the linear scale factor.',[0])
            add('measure','Apply the scale factor in the requested dimension','Area scales by the square and volume by the cube of the linear factor.',range(1,n));awards=('linear','measure')
        elif t in ('height_from_volumes','area_from_volume_ratio','volume_from_area_ratio','height_from_areas'):
            add('linear','Recover the linear scale factor','Take the cube root of a volume ratio or square root of an area ratio.',range(n-1))
            add('measure','Scale the requested corresponding measure','Apply k to lengths, k² to areas and k³ to volumes, maintaining the direction of correspondence.',[n-1]);awards=('linear','measure')
        else:add('similarity','Use corresponding lengths',operation_reason(f,t),range(n))
    elif f=='angles_lines_polygons':
        if t=='regular_diagonal':
            N=m['n'];interior=Fraction(180*(N-2),N)
            add('polygon','Find the regular polygon interior angle','A regular n-gon shares its (n−2)180° interior sum equally.',expression=rf'\angle ABC=\frac{{({N}-2)180^\circ}}{{{N}}}={q(interior)}^\circ')
            add('base_angle','Use the isosceles triangle','AB=BC makes the two base angles equal; their sum is 180° minus the angle at B.',expression=rf'2\angle CAB=180^\circ-{q(interior)}^\circ');awards=('polygon','base_angle')
        elif t=='ratio_quadrilateral':
            parts=m['parts'];total=sum(parts)
            add('share','Find the angle represented by one ratio part','The four interior angles total 360° and share it in the given ratio.',expression=rf'k=\frac{{360^\circ}}{{{total}}}')
            add('requested','Apply the requested ratio share','Multiply one equal angle share by the largest ratio term for the greatest angle.',expression=rf'\theta={max(parts)}\times\frac{{360^\circ}}{{{total}}}');awards=('share','requested')
        elif t=='unknown_angle':
            add('angles','Calculate the polygon interior sum','An n-gon divides into n−2 triangles.',[0])
            add('remainder','Subtract the known interior angles','The remaining angles account for all of the unused interior sum.',[1])
            add('share','Divide among the equal unknown angles','Each of the stated equal angles receives the same part of the remainder.',range(2,n))
        else:add('angles','Apply the stated angle relationship',operation_reason(f,t),range(n))
    elif f=='angles_circles':
        if t in ('semicircle','tangent_triangle','tangent_chord_radius','alt_segment_oab'):
            x=m['x']
            theorem='An angle standing on a diameter is a right angle.' if t=='semicircle' else 'A radius meets the tangent at its contact point at 90°.'
            add('circle_angle','Establish the right angle',theorem,expression=r'\text{Known right angle}=90^\circ')
            reason='The other two angles in the right triangle sum to 90°.' if t in ('semicircle','tangent_triangle') else 'The radius splits the tangent-chord right angle into the given angle and the required angle.'
            add('subtract','Subtract the given angle',reason,expression=rf'\theta=90^\circ-{x}^\circ={90-x}^\circ')
        elif t=='obt_tangent':
            x=m['x']
            add('tangent','Find the angle beside the radius','The tangent is perpendicular to the radius at the point of contact.',expression=rf'\angle OAB=90^\circ-{x}^\circ')
            add('isosceles','Relate the equal base angles','OA and OB are radii, so triangle OAB is isosceles.',expression=rf'\angle OBA=\angle OAB=90^\circ-{x}^\circ');awards=('tangent','isosceles')
        elif t=='oac':
            y=m['y']
            add('isosceles','Identify the equal base angles','OA and OC are equal radii of the same circle.',expression=r'OA=OC\quad\Rightarrow\quad\angle OAC=\angle OCA')
            add('triangle','Use the triangle angle sum','The two equal base angles sum to 180° minus the given central angle.',expression=rf'2\angle OAC=180^\circ-{y}^\circ');awards=('isosceles','triangle')
        elif t=='adc':
            y=m['y']
            add('central','Relate centre and circumference angles','The angle at the circumference on the same arc is half the central angle.',expression=rf'\angle ABC=\frac{{{y}^\circ}}2')
            add('cyclic','Use opposite cyclic angles','Opposite angles of a cyclic quadrilateral are supplementary.',expression=rf'\angle ADC=180^\circ-\frac{{{y}^\circ}}2');awards=('central','cyclic')
        else:add('circle_angle','Apply the circle-angle theorem',operation_reason(f,t),range(n))
    elif f in ('geometrical_terms','bisectors_numeric','symmetry_two_dimensions','symmetry_circles','constructions_scale_drawings'):
        add('geometric_property','Apply the defining geometric relationship',operation_reason(f,t),range(n))
    else:return None
    return a.finish(awards)
