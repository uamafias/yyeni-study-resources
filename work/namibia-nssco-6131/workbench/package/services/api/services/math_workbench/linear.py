"""Vector, transformation and matrix exam recipes."""
from copy import deepcopy
from fractions import Fraction as F
import random
import math
from .core import calc, fmt, part, question, step, coordinates
from .diagrams import asset, cartesian, line, polygon, text, arrow, circle

def matrix(rows):
    return '\\begin{pmatrix}' + '\\\\'.join(('&'.join((fmt(x) for x in row)) for row in rows)) + '\\end{pmatrix}'

def build_vector_notations(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    x1, y1 = (rng.randint(-6, 0), rng.randint(-5, 0))
    dx, dy = (rng.randint(2, 8), rng.randint(1, 7))
    x2, y2 = (x1 + dx, y1 + dy)
    q('vector-notations', ['9a.2', '9a.1'], 'Vector notation', f'$A=({x1},{y1})$ and $B=({x2},{y2})$. Let $\\mathbf a=\\overrightarrow{{AB}}$.', [part('Write $\\mathbf a$ as a column vector.', matrix([[dx], [dy]]), [step('Find directed displacement', 'Subtract the starting coordinates from the ending coordinates.', f'({x2}−({x1}), {y2}−({y1})) = ({dx},{dy})')], 2, [(1, 'Correct horizontal component.'), (1, 'Correct vertical component.')]), part('Write $\\overrightarrow{BA}$ in terms of $\\mathbf a$ and as a column vector.', '-\\mathbf a=' + matrix([[-dx], [-dy]]), [step('Reverse the direction', 'Reversing a vector changes the signs of both components.', '\\overrightarrow{BA}=-\\mathbf a=' + matrix([[-dx], [-dy]]))], 2, [(1, 'Correct negative vector relationship.'), (1, 'Correct reversed components.')]), part('Explain what $|\\mathbf a|$ represents.', 'The magnitude (length) of the vector a.', [step('Distinguish a vector from its magnitude', 'Magnitude has size only, while a vector also has direction.', '|a| is the length of AB.')])])
    return out

def build_scalar_vector_geometry(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = seed
    p, qv = (rng.randint(2, 4), rng.randint(2, 4))
    k = [F(-2), F(-1, 2), F(1, 2), F(2)][v % 4]
    end = (k * p, k * qv)
    graph, pt = cartesian(-10, 10, -10, 10, width=140, height=140, xstep=2, ystep=2)
    graph['commands'] += [*arrow(pt(0, 0), pt(p, qv)), text(pt(p + 0.3, qv + 0.3), 'a'), text(pt(-0.8, -0.8), 'O')]
    graph['commands']=[c for c in graph['commands'] if c['kind']!='text' or c['value']!='0']
    sol = deepcopy(graph)
    sol['commands'] += [*arrow(pt(0, 0), pt(*end), color='#006633')]
    place_vertex_label(sol,pt(*end),'ka',[pt(0,0),pt(p,qv),pt(*end)])
    q('scalar-vector-geometry', ['9a.4', '9a.6'], 'Scaling a vector', f'The diagram shows $\\mathbf a={matrix([[p], [qv]])}$. Let $k={fmt(k)}$.', [part('Find $k\\mathbf a$ and draw it from O.', matrix([[end[0]], [end[1]]]), [step('Multiply each component by k', 'Scalar multiplication applies to the entire vector.', matrix([[end[0]], [end[1]]])), step('Represent the result as a directed segment', 'The endpoint gives the horizontal and vertical displacement from O.', f'Endpoint ({fmt(end[0])},{fmt(end[1])}).')], 3, [(1, 'Correct horizontal component.'), (1, 'Correct vertical component.'), (1, 'Correct directed segment from O.')]), part('Compare its length and direction with those of a.', f'Length factor {fmt(abs(k))}; ' + ('opposite direction.' if k < 0 else 'same direction.'), [step('Interpret the scalar', 'Its absolute value scales length; its sign determines whether direction reverses.', f'Length factor {fmt(abs(k))}; ' + ('opposite direction.' if k < 0 else 'same direction.'))], 2, [(1, 'Correct length comparison.'), (1, 'Correct direction comparison.')])], assets=[asset('scalar', graph, sol)])
    return out


def place_vertex_label(diagram,point,label,vertices):
    """Choose a label box clear of existing text, vertices and polygon edges."""
    def distance(p,a,b):
        dx,dy=b[0]-a[0],b[1]-a[1]
        t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy))) if dx or dy else 0
        return math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy)
    segments=[]
    for c in diagram['commands']:
        if c['kind']=='line':segments.append((c['a'],c['b']))
        if c['kind'] in ('polygon','polyline'):
            pts=c['points'];segments.extend(zip(pts,pts[1:]+(pts[:1] if c['kind']=='polygon' else [])))
    def inside(p,pts):
        yes=False
        for a,b in zip(pts,pts[1:]+pts[:1]):
            if (a[1]>p[1])!=(b[1]>p[1]) and p[0]<(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1])+a[0]:yes=not yes
        return yes
    width=max(4,len(label)*2.5*.6);candidates=[]
    for dx,dy in [(3,5),(-width-3,5),(3,-5),(-width-3,-5),(5,0),(-width-5,0),(0,8),(0,-8),(8,8),(-width-8,8),(8,-8),(-width-8,-8)]:
        x,y=point[0]+dx,point[1]+dy
        if x<2 or x+width>diagram['width_mm']-2 or y<4 or y>diagram['height_mm']-2:continue
        probes=[(x,y-1),(x+width/2,y-1),(x+width,y-1)]
        centre=(x+width/2,y-1)
        own=math.dist(centre,point)
        ambiguous=any(math.dist(centre,v)<own+.5 for v in vertices if math.dist(v,point)>.01)
        penalty=1000 if ambiguous else 0
        penalty+=sum(30 for c in diagram['commands'] if c['kind']=='polygon' and inside(centre,c['points']))
        penalty+=sum(max(0,3-distance(v,a,b)) for v in probes for a,b in segments)
        penalty+=sum(max(0,4-math.hypot(v[0]-u[0],v[1]-u[1])) for v in probes for u in vertices)
        for c in diagram['commands']:
            if c['kind']!='text':continue
            tx,ty=c['p'];tw=len(c['value'])*c.get('size',3)*.6
            if x<tx+tw+3 and x+width+3>tx and abs(y-ty)<6:penalty+=10000
        candidates.append((penalty,x,y))
    _,x,y=min(candidates)
    centre=(x+width/2,y-1)
    # Thin leaders connect labels to the intended vertex without changing it.
    diagram['commands'].append(line(point,centre,color='#777777',width=.15))
    diagram['commands'].append(text((x,y),label,size=2.5))

def build_negative_fractional_enlargement(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    ax, ay = (rng.randint(4, 5), rng.randint(4, 5))
    k = rng.choice([F(-2), F(-1, 2), F(1, 2)])
    cx, cy = (rng.randint(-1, 0), rng.randint(-1, 0))
    points = [(ax, ay), (ax + 4, ay), (ax, ay + 4)]
    image = [(F(cx) + k * (x - cx), F(cy) + k * (y - cy)) for x, y in points]
    all_points=points+image+[(cx,cy),(0,0)]
    xmin,xmax=math.floor(min(p[0] for p in all_points))-2,math.ceil(max(p[0] for p in all_points))+2
    ymin,ymax=math.floor(min(p[1] for p in all_points))-2,math.ceil(max(p[1] for p in all_points))+2
    unit_step=1 # Half-unit vertices can be placed between readable integer ticks.
    graph, pt = cartesian(xmin,xmax,ymin,ymax,width=190,height=190,xstep=unit_step,ystep=unit_step)
    graph['commands'].append(polygon([pt(*p) for p in points]))
    for label, p in zip('ABC', points):
        place_vertex_label(graph,pt(*p),label,[pt(*v) for v in points+image])
    graph['commands'].append(circle(pt(cx,cy),0.7,fill='black'))
    place_vertex_label(graph,pt(cx,cy),'E',[pt(*v) for v in points+image])
    sol = deepcopy(graph)
    sol['commands'].append(polygon([pt(*p) for p in image], color='#006633'))
    for label, p in zip(["A'", "B'", "C'"], image):
        place_vertex_label(sol,pt(*p),label,[pt(*v) for v in points+image])
    q('negative-fractional-enlargement', ['9b.3'], 'Enlargement', f"Triangle ABC has vertices {coordinates(points, 'ABC')}. Enlarge it by scale factor ${fmt(k)}$ with centre $E=({cx},{cy})$.", [part('Draw and label the image of ABC on a coordinate grid.', coordinates(image, ['A′', 'B′', 'C′']), [step('Find each displacement from the centre', 'The enlargement acts on the centre-to-vertex vector.', coordinates([(x - cx, y - cy) for x, y in points])), step('Scale and return to the coordinate plane', 'Multiply each displacement by k, then add the centre back.', coordinates(image, ['A′', 'B′', 'C′']))], 3, [(1, 'Correct use of centre and scale factor.'), (1, 'Two accurate image vertices.'), (1, 'Complete accurately labelled image.')], checks=[(all((x2 - cx == k * (x1 - cx) and y2 - cy == k * (y1 - cy) for (x1, y1), (x2, y2) in zip(points, image))), 'Every enlargement vertex satisfies the centre-displacement definition')])], assets=[asset('enlargement', graph, sol)])
    return out

def build_combined_transformations(seed,rng,requested_key=None):
    x,y=-rng.randint(4,6),-rng.randint(4,6);w,h=rng.randint(2,3),rng.randint(2,3)
    points=[(x,y),(x+w,y),(x,y+h)];tx=rng.randint(10,12)
    def translation(dx,dy):return {'name':f'translation by ({dx},{dy})','apply':lambda p:(p[0]+dx,p[1]+dy),'inverse':f'translation by ({-dx},{-dy})'}
    reflect_y={'name':'reflection in the y-axis','apply':lambda p:(-p[0],p[1]),'inverse':'reflection in the y-axis'}
    reflect_x={'name':'reflection in the x-axis','apply':lambda p:(p[0],-p[1]),'inverse':'reflection in the x-axis'}
    rotation={'name':'rotation 90° anticlockwise about O','apply':lambda p:(-p[1],p[0]),'inverse':'rotation 90° clockwise about O'}
    k=rng.choice((F(-1,2),F(-1)))
    enlargement={'name':f'enlargement with scale factor {fmt(k)} and centre E=(0,-5)','apply':lambda p:(k*p[0],-5+k*(p[1]+5)),'inverse':f'enlargement with scale factor {fmt(1/k)} and centre E=(0,-5)'}
    negative={'name':'enlargement with scale factor -1 and centre O','apply':lambda p:(-p[0],-p[1]),'inverse':'enlargement with scale factor -1 and centre O'}
    pairs=[(translation(tx,0),rotation),(reflect_y,translation(0,10)),(enlargement,reflect_x),(translation(tx,0),reflect_x),(reflect_y,negative),(enlargement,rotation)]
    op1,op2=pairs[seed%len(pairs)];first=[op1['apply'](p) for p in points];second=[op2['apply'](p) for p in first]
    # Draw separate labelled stages instead of selecting transformations with
    # ambiguous shared edges. All three use the same coordinate scale.
    all_points=points+first+second
    xmin=min(-8,math.floor(min(p[0] for p in all_points))-2);xmax=max(8,math.ceil(max(p[0] for p in all_points))+2)
    ymin=min(-8,math.floor(min(p[1] for p in all_points))-2);ymax=max(8,math.ceil(max(p[1] for p in all_points))+2)
    graph,pt=cartesian(xmin,xmax,ymin,ymax,width=190,height=190,xstep=2,ystep=2)
    graph['commands'].append(polygon([pt(*p) for p in points]))
    sol=deepcopy(graph)  # Reference labels are placed afresh, with no orphan leaders.
    for name,p in zip('ABC',points):place_vertex_label(graph,pt(*p),name,[pt(*v) for v in all_points])
    sol['commands'] += [polygon([pt(*p) for p in first],color='#3333aa'),polygon([pt(*p) for p in second],color='#006633')]
    labels={}
    for suffix,vertices in [('',points),('′',first),('″',second)]:
        for name,vertex in zip('ABC',vertices):labels.setdefault(tuple(vertex),[]).append(name+suffix)
    for vertex,names in labels.items():place_vertex_label(sol,pt(*vertex),', '.join(names),[pt(*v) for v in all_points])
    article=lambda name:'an' if name.startswith('enlargement') else 'a'
    stem=f'Triangle ABC undergoes {article(op1["name"])} {op1["name"]}, followed by {article(op2["name"])} {op2["name"]}.'
    reference=f'{op2["inverse"]}, then {op1["inverse"]}.'
    q=question('combined-transformations',['9b.5'],'Two transformations',stem,[
      part('Draw the first image, labelling it A′B′C′.',coordinates(first,['A′','B′','C′']),[step('Apply the first transformation to every vertex','Use the stated rule and the same centre, axis or displacement for every vertex.',coordinates(first,['A′','B′','C′']))],2,[(1,'Correct first transformation rule applied.'),(1,'Complete correctly labelled first image.')]),
      part('Draw the final image, labelling it A″B″C″.',coordinates(second,['A″','B″','C″']),[step('Transform the first image','The second operation acts on A′B′C′, not on the original triangle.',coordinates(second,['A″','B″','C″']))],2,[(1,'Correct second transformation of the first image.'),(1,'Complete correctly labelled final image.')]),
      part('Describe two transformations, in order, which return the final image to ABC.',reference,[step('Undo the operations in reverse order','Invert the second operation first, then invert the first. Other equivalent compositions are accepted.',reference)],2,[(1,'Both inverse operations with correct axes/centres/vectors/factors.'),(1,'A composition order that maps every final vertex back to its original position.')])],variant=seed,assets=[asset('combined',graph,sol)])
    q['structural_case']=['translation_rotation','reflection_translation','enlargement_reflection','translation_reflection','reflection_enlargement','enlargement_rotation'][seed%len(pairs)]
    q['parameter_evidence']={'object':points,'first_image':[[float(v) for v in p] for p in first],'final_image':[[float(v) for v in p] for p in second],'case':seed%len(pairs)}
    return [q]

def build_contextual_matrix_representation(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    rows = [[rng.randint(10, 70), rng.randint(10, 70)] for _ in range(3)]
    q('contextual-matrix-representation', ['10main.1'], 'Representing stock', '| Shop | Notebooks | Pens |\n|---|---:|---:|\n' + '\n'.join((f'| Shop {i + 1} | {a} | {b} |' for i, (a, b) in enumerate(rows))), [part('Represent the stock as a matrix M, with shops as rows and items as columns in the order shown.', matrix(rows), [step('Match each row and column to the stated categories', 'The row-column convention fixes where each count belongs.', matrix(rows))], 2, [(1, 'Correct 3 × 2 arrangement.'), (1, 'All data correctly placed.')]), part('State the order of M and explain what its entry in row 2, column 1 represents.', f'3 × 2; Shop 2 has {rows[1][0]} notebooks.', [step('Read the row and column meanings', 'Matrix order is rows × columns; row 2 is Shop 2 and column 1 is notebooks.', f'3 × 2; {rows[1][0]} notebooks at Shop 2.')], 2, [(1, 'Correct order.'), (1, 'Correct contextual interpretation.')])])
    return out

def build_three_by_three_matrix_arithmetic(seed, rng, requested_key=None):
    out = []
    def q(key,objs,title,stem,ps,**kw):
        row=[rng.randint(-6,6),rng.randint(-6,6)];column=[rng.randint(1,6),rng.randint(1,6)]
        inner=sum(x*y for x,y in zip(row,column));outer=[[x*y for y in row] for x in column]
        stem+=f' Also, $R={matrix([row])}$ and $C={matrix([[x] for x in column])}$.'
        ps.extend([
            part('Find RC and state its order.',matrix([[inner]])+'; order 1 × 1.',[
                step('Check the product order','A 1 × 2 row times a 2 × 1 column gives a 1 × 1 matrix.','Order 1 × 1.'),
                step('Take the row-column dot product','Multiply corresponding entries and add the two products.',f'({row[0]})({column[0]})+({row[1]})({column[1]})={inner}')],3,[(1,'Correct row-column multiplication method.'),(1,'Correct value, as a scalar or 1 × 1 matrix.'),(1,'Correct order 1 × 1.')]),
            part('Find CR and state its order.',matrix(outer)+'; order 2 × 2.',[
                step('Check the reverse product order','A 2 × 1 column times a 1 × 2 row gives a 2 × 2 matrix.','Order 2 × 2.'),
                step('Form each row of the outer product','Each entry of C scales the entire row R.',matrix(outer))],3,[(1,'Correct column-by-row multiplication method.'),(1,'All four entries correct.'),(1,'Correct order 2 × 2.')])])
        result=question(key,objs,title,stem,ps,variant=seed,**kw)
        result['parameter_evidence']={'row_vector':row,'column_vector':column,'inner_product':inner,'outer_product':outer}
        out.append(result)
    A = [[rng.randint(-5, 8) for _ in range(3)] for _ in range(3)]
    B = [[rng.randint(-5, 8) for _ in range(3)] for _ in range(3)]
    plus = [[a + b for a, b in zip(ar, br)] for ar, br in zip(A, B)]
    minus = [[a - b for a, b in zip(ar, br)] for ar, br in zip(A, B)]
    q('three-by-three-matrix-arithmetic', ['10main.3'], 'Matrix arithmetic', f'$A={matrix(A)}$ and $B={matrix(B)}$.', [part('Find A + B.', matrix(plus), [step('Add corresponding entries', 'Matrix addition combines entries in the same row and column.', matrix(plus))], 3, [(1, f'Correct row {i + 1}: {', '.join(fmt(x) for x in row)}.') for i, row in enumerate(plus)]), part('Find A − B.', matrix(minus), [step('Subtract corresponding entries', 'Keep the order A minus B, including negative entries.', matrix(minus))], 3, [(1, f'Correct row {i + 1}: {', '.join(fmt(x) for x in row)}.') for i, row in enumerate(minus)])])
    return out

def build_zero_and_identity_matrices(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.randint(2, 40)
    A = [[1, t], [0, 1]]
    B = [[1, -t], [0, 1]]
    I = [[1, 0], [0, 1]]
    Z = [[0, 0], [0, 0]]
    q('zero-and-identity-matrices', ['10main.4', '10main.3'], 'Zero and identity matrices', f'$A={matrix(A)}$ and $B={matrix(B)}$.', [part('Write down the identity matrix I of order 2 and the zero matrix Z of order 2.', matrix(I) + '; ' + matrix(Z), [step('Use the defining entries', 'The identity has 1 on its diagonal and 0 elsewhere; the zero matrix has only zeros.', matrix(I) + '; ' + matrix(Z))], 2, [(1, 'Correct identity matrix.'), (1, 'Correct zero matrix.')]), part('Calculate AB and state what this tells you about B.', matrix(I) + '; B is the inverse of A.', [step('Multiply rows by columns', 'Each product entry is a row-column dot product.', matrix([[1 * 1 + t * 0, 1 * -t + t * 1], [0 * 1 + 1 * 0, 0 * -t + 1 * 1]])), step('Interpret the identity product', 'A square matrix that multiplies A to give I is its inverse.', 'B = A⁻¹')], 3, [(1, 'Correct row-column multiplication.'), (1, 'AB = I.'), (1, 'B identified as the inverse of A.')]), part('State AI and AZ.', matrix(A) + '; ' + matrix(Z), [step('Use identity and zero multiplication', 'Multiplication by I leaves a matrix unchanged; multiplication by Z gives a zero matrix.', matrix(A) + '; ' + matrix(Z))], 2, [(1, 'AI = A.'), (1, 'AZ = Z.')])])
    return out
BUILDERS = [build_vector_notations, build_scalar_vector_geometry, build_negative_fractional_enlargement, build_combined_transformations, build_contextual_matrix_representation, build_three_by_three_matrix_arithmetic, build_zero_and_identity_matrices]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
