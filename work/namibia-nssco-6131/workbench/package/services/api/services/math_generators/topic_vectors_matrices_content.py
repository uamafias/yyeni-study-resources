"""Coordinate transformations, vector routes and explicit matrix operations."""
import re
from .topic_teaching import *
from .formatting import number_latex

def q(value):
    if isinstance(value,(tuple,list)) and len(value)==2:value=F(*value)
    return number_latex(F(value))

from .family_trig_vectors_matrices import _reflect_one, _apply_rotate, _apply_enlarge

LABELS={
'nssco_vector_operations_magnitude':{1:'Adding, subtracting and scaling vectors',2:'Finding a vector magnitude',3:'Combining vectors before finding magnitude',4:'Vector routes in a parallelogram'},
'nssco_position_vectors':{1:'Dividing a segment in a ratio',2:'Position vector of a midpoint',3:'Position vectors in named-vector form',4:'Displacements between points in a triangle'},
'nssco_transformations_coordinates':{1:'Translating coordinates',2:'Reflecting coordinates',3:'Rotating about a stated centre',4:'Enlarging about a stated centre',5:'Describing a complete transformation'},
'nssco_matrix_basics':{1:'Adding and subtracting corresponding entries',2:'Scaling and combining matrices',3:'Equating corresponding matrix entries',4:'Interpreting stock matrices'},
'nssco_matrix_multiplication':{1:'Matrix times a column vector',2:'Row-by-column matrix multiplication',3:'Reversing order and squaring a matrix',4:'Finding an unknown product entry'},
'nssco_determinants_inverses':{1:'Calculating a determinant',2:'Finding a two-by-two inverse',3:'Finding an entry from a determinant',4:'Solving equations by a matrix inverse',5:'Finding when a matrix is singular'},
}


def read_matrix(text):return [[F(v.strip()) for v in row.split(',')] for row in text.strip('() ').split(';')]
def read_point(text):return tuple(F(x.strip()) for x in text.strip('() ').split(','))
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def inverse(A):
    a,b=A[0];c,d=A[1];D=det(A);return [[d/D,-b/D],[-c/D,a/D]]
def product(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def product_rows(A,B):
    result=product(A,B)
    return [f'c_{{{i+1}{j+1}}}='+ '+'.join(f'({q(A[i][k])})({q(B[k][j])})' for k in range(len(B)))+'='+q(result[i][j]) for i in range(len(A)) for j in range(len(B[0]))]+['C='+matrix(result)]


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];lines=[];gid=p.generator_id
    if gid=='nssco_vector_operations_magnitude':
        names=re.findall(r'\\mathbf\{([a-z])\}',p.question)
        if t in ('vector_add','vector_subtract','vector_scalar'):
            a=m['a'];name=names[0]
            if t=='vector_scalar':
                k=int(re.search(r'\$(-?\d+)\\mathbf',p.question)[1]);lines=[f'{k}\\mathbf{{{name}}}='+r'\begin{pmatrix}'+f'{k}({a[0]})'+r'\\'+f'{k}({a[1]})'+r'\end{pmatrix}'];e=f'The given vector ${name}$ has horizontal component ${a[0]}$ and vertical component ${a[1]}$. Scalar ${k}$ multiplies both components. A negative scalar also reverses direction; multiplying only one component changes the vector incorrectly.'
            else:
                b=m['b'];sign='+' if t=='vector_add' else '-';lines=[vector(a)+sign+vector(b)+'='+r'\begin{pmatrix}'+f'({a[0]}){sign}({b[0]})'+r'\\'+f'({a[1]}){sign}({b[1]})'+r'\end{pmatrix}'];e=f'The first vector ${names[0]}$ is ${vector(a)}$ and the second ${names[1]}$ is ${vector(b)}$. '+('Add' if sign=='+' else 'Subtract')+' components in matching positions: horizontal with horizontal and vertical with vertical. Keep subtraction order and bracket negative components.'
        elif t in ('magnitude','combination','combination_magnitude'):
            a=m['a']
            if t in ('combination','combination_magnitude'):
                b=m['b'];k,l=m['k'],m['l'];result=[k*a[i]-l*b[i] for i in (0,1)];lines=[f'{k}\\mathbf{{a}}={vector([k*v for v in a])}',f'{l}\\mathbf{{b}}={vector([l*v for v in b])}',f'{k}\\mathbf{{a}}-{l}\\mathbf{{b}}='+vector(result)]
                e=f'The given vectors are $a={vector(a)}$ and $b={vector(b)}$. Scale both components of each vector, then subtract the scaled vectors in the stated order. '
            else:result=a;e=f'The vector ${names[0]}={vector(a)}$ gives perpendicular horizontal and vertical changes. '
            if t!='combination':lines.append(r'|\mathbf{'+(names[0] if t=='magnitude' and names else 'v')+r'}|=\sqrt{'+f'({result[0]})^2+({result[1]})^2'+'}');e+='Here $v$ denotes '+('the resulting combined vector. Combine components before taking the magnitude; magnitudes cannot generally be subtracted.' if t=='combination_magnitude' else 'the given vector. Its magnitude is the positive length from Pythagoras, not the sum of its signed components.')
        else:
            verts=re.match(r'([A-Z]{4}) is a parallelogram',p.question)[1];u,v=list(m['coefs']);pos={verts[0]:(0,0),verts[1]:(1,0),verts[2]:(1,1),verts[3]:(0,1)};start,end=m['start'],m['end'];a,b=pos[start],pos[end]
            lines=[f'\\overrightarrow{{{start}{end}}}=({b[0]}-({a[0]}))\\mathbf{{{u}}}+({b[1]}-({a[1]}))\\mathbf{{{v}}}']
            e=f'Use {verts[0]} as the reference point. The first side vector ${u}$ leads to {verts[1]}, the second ${v}$ to {verts[3]}, and their sum to {verts[2]}. The requested vector starts at {start} and ends at {end}, so subtract the starting position vector from the ending one. This keeps the direction and signs of both side contributions.'
    elif gid=='nssco_position_vectors':
        if t=='midpoint':
            a,b=m['a'],m['b'];result=[F(a[i]+b[i])/2 for i in (0,1)];lines=[r'\overrightarrow{OM}='+frac(1,2)+'('+vector(a)+'+'+vector(b)+')='+vector(result)]
            e=f'The given position vectors locate A at ${point(a)}$ and B at ${point(b)}$ relative to origin O. Their midpoint M averages both corresponding coordinates. Halve the sum of the two position vectors; halving displacement AB without adding OA would locate the wrong point.'
        else:
            a,n=m['m'],m['n'];ratio=F(a)/(a+n)
            if t=='ratio_point':
                A,B=m['a'],m['b'];delta=[B[i]-A[i] for i in (0,1)];partial=[ratio*x for x in delta];lines=[r'\overrightarrow{AB}='+vector(delta),r'\overrightarrow{AP}='+q(ratio)+vector(delta)+'='+vector(partial),r'\overrightarrow{OP}='+vector(A)+'+'+vector(partial)]
                e=f'The given position vectors are OA=${vector(A)}$ and OB=${vector(B)}$. The ratio AP:PB is ${a}:{n}$, so AP is ${frac(a,a+n)}$ of the directed segment AB. Find AB = OB − OA, scale it, then add OA to obtain OP. AP alone is a displacement, not the requested position vector.'
            else:
                u=m.get('a','a');v=m.get('b','b');u=u if isinstance(u,str) else 'a';v=v if isinstance(v,str) else 'b'
                lines=[r'\overrightarrow{AB}=\mathbf{b}-\mathbf{a}',r'\overrightarrow{AM}='+q(ratio)+r'(\mathbf{b}-\mathbf{a})'] if t!='position_letters' else [f'\\overrightarrow{{PQ}}=\\mathbf{{{v}}}-\\mathbf{{{u}}}',r'\overrightarrow{PM}='+q(ratio)+f'(\\mathbf{{{v}}}-\\mathbf{{{u}}})']
                if t=='position_letters':lines.append(r'\overrightarrow{OM}=\mathbf{'+u+'}+'+q(ratio)+f'(\\mathbf{{{v}}}-\\mathbf{{{u}}})')
                elif t=='vector_MN':lines.extend([r'\overrightarrow{OM}=\mathbf{a}+'+q(ratio)+r'(\mathbf{b}-\mathbf{a})',r'\overrightarrow{ON}='+frac(1,2)+r'\mathbf{b}',r'\overrightarrow{MN}='+frac(1,2)+r'\mathbf{b}-\left[\mathbf{a}+'+q(ratio)+r'(\mathbf{b}-\mathbf{a})\right]'])
                e=f'The named lower-case vectors are position vectors from O to the given endpoints. The segment is divided in ratio ${a}:{n}$, so the part measured from the first endpoint is ${frac(a,a+n)}$ of endpoint minus starting point. '+('Add the first endpoint’s position vector to obtain OM.' if t=='position_letters' else 'For MN, subtract OM from ON; N is halfway from O to B.' if t=='vector_MN' else 'AM is a displacement from A, so do not add OA when AM itself is requested.')+' Expand and collect coefficients of the same named vector, retaining direction signs.'
    elif gid=='nssco_transformations_coordinates':
        points=[read_point(x) for x in m['points']];desc=m['transform'] if t=='describe_transformation' else m
        kind=desc.get('type',t);kind={'translation':'translate','reflection':'reflect','rotation':'rotate','enlargement':'enlarge'}.get(kind,kind)
        if kind=='translate':
            v=desc['vector'];images=[(x+v[0],y+v[1]) for x,y in points];lines=[f"x'=x+({v[0]}),\\quad y'=y+({v[1]})"]
            e=f'The translation vector is ${vector(v)}$. Its first component moves horizontally and its second vertically; add the same pair to every point. Size and orientation are preserved. To describe a translation fully, give the vector, not just the transformation name.'
        elif kind=='reflect':
            axis,c=desc['line'];c=F(c);images=[_reflect_one(pt,(axis,c)) for pt in points];rule={ 'x':f"x'=2({q(c)})-x,\\quad y'=y",'y':f"x'=x,\\quad y'=2({q(c)})-y",'y=x':"x'=y,\\quad y'=x",'y=-x':"x'=-y,\\quad y'=-x"}[axis];lines=[rule]
            e='The mirror line is $'+(f'{axis}={q(c)}' if axis in ('x','y') else axis)+'$. Each point and its image lie on opposite sides at the same perpendicular distance from this line. A point on the mirror stays fixed. Apply the corresponding-coordinate rule to every point, retaining their labels. A full reflection description includes the line equation.'
        elif kind=='rotate':
            C=tuple(map(F,desc['centre']));turns=desc.get('quarters',0);images=_apply_rotate(points,C,turns);rules={1:"(u,v)\\mapsto(-v,u)",2:"(u,v)\\mapsto(-u,-v)",3:"(u,v)\\mapsto(v,-u)"}
            offset=lambda symbol,c:symbol if not c else symbol+('+' if c<0 else '-')+q(abs(c))
            lines=[label('Rotation centre')+'='+point(C),f'u={offset("x",C[0])},\\quad v={offset("y",C[1])}',rules[turns],label('Add the centre coordinates back')]
            e=f'The rotation centre is ${point(C)}$. Relative offset $(u,v)$ means the point minus the centre. Turn the offset '+{1:'90 degrees anticlockwise',2:'180 degrees',3:'90 degrees clockwise'}[turns]+', then add the centre back. Rotating the original coordinates directly would rotate about the origin. A full description needs angle, direction when relevant, and centre.'
        else:
            C=tuple(map(F,desc['centre']));k=F(desc['k']);images=_apply_enlarge(points,C,k);lines=[label('Enlargement centre')+f'={point(C)},\\quad k={q(k)}',f"x'={q(C[0])}+({q(k)})(x-({q(C[0])}))",f"y'={q(C[1])}+({q(k)})(y-({q(C[1])}))"]
            e=f'The enlargement centre is ${point(C)}$ and signed scale factor $k={q(k)}$. Subtract the centre coordinates to get a centre-to-point vector, multiply both components by k, then add the centre coordinates back. A negative factor places the image on the opposite side of the centre; a fractional magnitude reduces size. Describe both factor and centre.'
        lines += [f'{chr(65+i)}{point(pt)}\\mapsto {chr(65+i)}^\\prime{point(image)}' for i,(pt,image) in enumerate(zip(points,images))]
        if t=='describe_transformation':e+=' Check the same single transformation against every corresponding point, not only one pair.'
    else:
        if t in ('add','subtract','scalar','combination','stock_left','stock_total'):
            A=read_matrix(m.get('A',m.get('S')))
            if t=='stock_total':lines=[label('Total stock')+'='+'+'.join(q(v) for row in A for v in row)];e='S is the stock matrix. Each entry counts one category/location combination. The requested total is the sum of all entries, not the determinant or the number of rows.'
            else:
                B=read_matrix(m.get('B',m.get('R'))) if t!='scalar' else [[F(0) for x in row] for row in A];k=m.get('k',1);sign=-1 if t in ('subtract','stock_left') else m.get('sign',1)
                entries=[[f'({k})({q(x)})'+(('+' if sign==1 else '-')+f'({q(B[i][j])})' if t!='scalar' else '') for j,x in enumerate(row)] for i,row in enumerate(A)]
                lines=[r'\begin{pmatrix}'+r'\\'.join(' & '.join(row) for row in entries)+r'\end{pmatrix}']
                e=f'The first displayed matrix is ${matrix(A)}$'+(f' and the second ${matrix(B)}$.' if t!='scalar' else '.')+' Matrix addition/subtraction combines entries in matching row and column positions. '+(f'Multiply every entry of the first matrix by scalar ${k}$ before combining.' if t in ('scalar','combination') else 'Subtract sales from original stock for remaining stock.' if t=='stock_left' else 'Keep the stated subtraction order and signs.')+' These operations are not row-by-column matrix multiplication.'
        elif t=='equal_matrices':
            a,b,c,d=m['p'],m['q'],m['c1'],m['c2'];rhs1=a*m['x']+c;rhs2=b*m['y']+d
            lines=[f'{a}x+({c})={rhs1}','x='+frac(f'{rhs1}-({c})',a),f'{b}y+({d})={rhs2}','y='+frac(f'{rhs2}-({d})',b)]
            e='Equal matrices have equal entries in every corresponding position. Equate the two top-left entries for x and the two bottom-right entries for y, then solve those separate linear equations. Preserve which variable belongs to which position; matching diagonal products instead would compare determinants, not matrices.'
        elif t in ('matrix_times_column','matrix_product','matrix_BA','matrix_square'):
            A=read_matrix(m['A']);B=read_matrix(m['v'] if t=='matrix_times_column' else m['B']) if t!='matrix_square' else A
            if t=='matrix_BA':A,B=B,A
            lines=product_rows(A,B);e=f'The required left matrix is ${matrix(A)}$ and right matrix ${matrix(B)}$. Each output entry $c_{{ij}}$ is row i of the left matrix dotted with column j of the right: multiply matching entries and add. Inner dimensions must agree. Order matters; a square A² means A times A, not squaring each individual entry.'
        elif t=='unknown_in_product':
            first=p.steps[0].value.replace(' x ',r'\times ');lines=[first]+[authored_math(step.value) for step in p.steps[1:3]]
            e='Let k denote the unknown entry in the given matrix. Use the stated entry of the product: take the matching row of the first matrix and column of the second, multiply corresponding entries and add. Equate this to the given product entry, then solve the resulting linear equation. Element-by-element matrix multiplication would use the wrong equation.'
        elif t in ('determinant','inverse','matrix_method'):
            A=read_matrix(m['A']);a,b=A[0];c,d=A[1];D=det(A);lines=[r'\det A='+f'({q(a)})({q(d)})-({q(b)})({q(c)})={q(D)}']
            e=f'The matrix is A=${matrix(A)}$. For a two-by-two matrix the determinant is top-left × bottom-right minus top-right × bottom-left, giving ${q(D)}$. Keep the subtraction order and signed products.'
            if t in ('inverse','matrix_method'):
                adj=[[d,-b],[-c,a]];inv=inverse(A);lines.append('A^{-1}='+frac(1,q(D))+matrix(adj)+'='+matrix(inv));e+=' The nonzero determinant permits an inverse: swap the main diagonal entries, negate the other two, then divide every entry by the determinant.'
                if t=='matrix_method':
                    rhs=[[F(x)] for x in m['rhs']];lines.append(matrix(A)+r'\begin{pmatrix}x\\y\end{pmatrix}='+matrix(rhs));lines+=product_rows(inv,rhs);e+=' The unknown column is (x,y)ᵀ in that order. Multiply the right-hand column by A⁻¹ on the left to recover x and y; check in both original equations.'
        elif t=='missing_element':
            cell={key:'x' if key==m['which'] else str(v) for key,v in m['cells'].items()};a,b,c,d=(cell[k] for k in 'abcd');lines=[f'({a})({d})-({b})({c})={m["det"]}']+[authored_math(step.value) for step in p.steps[1:3]]
            e=f'The unknown x occupies the {m["which"]} position in the usual matrix layout (a,b;c,d). Its determinant must be ${m["det"]}$. Apply ad−bc with x in its actual position, then rearrange and divide by the nonzero coefficient. An off-diagonal x lies inside the subtracted product, so its sign needs particular care.'
        else:
            a,b,c=m['a'],m['b'],m['c'];lines=[r'\det N=0',f'({a})k-({b})({c})=0','k='+frac(f'({b})({c})',a)]
            e=f'The matrix N has entries ({a},{b};{c},k). Having no inverse means its determinant is zero. Thus ${a}k-({b})({c})=0$. Solve for the unknown k; setting determinant to one would instead describe some invertible matrices.'
    return finish(p,lines,e)
