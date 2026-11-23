"""YM232–235: vector notation and all original prism/cube coordinates.

Coordinate constructions use axes and edges read from the ORIGINAL diagram.
The printed key is a separate comparison; diagram reading remains manual.
"""
import hashlib,json
import author_YM_C1_opening as common
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent
LOCATE='8227:2020:M1:T7:O01:D01';NOTATION='8227:2020:M1:T7:O01:D02';GEOM='8227:2020:M1:T7:O02:D03';SCALE='8227:2020:M1:T7:O02:D02'
def pp(page):return page-12
def ev(page):
 name='YM-C5-keys-615-source'if 615<=page<=618 else f'YM-C5-{232+4*((page-232)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
common.base.ev=ev;common.base.answers.clear();common.base.new.clear();figures.clear()
answers=common.base.answers;new=common.base.new;corrections=[]

def add(kind,n,page,note,parts,direct=None,new_item=False):
 r=common.add(kind,n,page,note,parts,direct or[LOCATE]);r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C5:');meta=new.pop();meta['item_id']=r['item_id']
 if not new_item:corrections.append({'item_id':r['item_id'],'pdf_page':page,'printed_page':pp(page),'continuation_pdf_pages':[]})
 r.update(representation='diagram',component_demand_ids=[],mapping_rationale='These outputs locate POINTS from displayed Cartesian axes and geometric edge relations. A coordinate triple is not automatically a separately assessed displacement/position-vector or magnitude demand. Vector-notation teaching diagrams have separate supporting records.',value_level_scope_decisions=[])
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],'qualifier_applicability_note':'Original 3D axes and positive side lengths are explicit. No calculus,modulus or inverse-branch qualifier applies to point-coordinate reading.'}
 r['precision_angle_check']={'source':'Exact integer Cartesian coordinates in order(x,y,z); no rounding or trigonometric angle units.','comparison':'Read the displayed axis labels and origin,not apparent perspective lengths or page orientation. Centre-origin cubes use HALF the side length with appropriate signs; projected overlap with an axis does not prove a point lies on that spatial axis.'}
 if new_item:
  meta.update(printed_page=pp(page),scope_check=r['scope_check'],mapping_rationale=r['mapping_rationale'],value_level_scope_decisions=[],component_demand_ids=r['component_demand_ids']);new.append(meta)
 return r

def coordinate(label,origin,edges,bits,printed,kp,missing=False):
 assert len(origin)==len(edges)==len(bits)==3
 expr='Tuple('+','.join(str(origin[j])+'+'+'+'.join(f'({edges[i][j]})*({bits[i]})'for i in range(3))for j in range(3))+')'
 derived=tuple(origin[j]+sum(edges[i][j]*bits[i]for i in range(3))for j in range(3))
 method='Read origin,axis orientation and vertex-edge incidence from the ORIGINAL rendered diagram. Add the signed axis-aligned edge displacements to the base point; compare the independently transcribed key only afterwards. The arithmetic is recomputable; the vertex-to-edge incidence is a manual source reading,not an automated pixel proof.'
 if missing:
  p=reasoning(label,str(derived),method+' The key under(b) repeats(a)’s different vertex list and has no answer for this named cube vertex; no invented numeric key is compared.',kp,'key incomplete')
  p['additional_operations']={'coordinate-from-edges':{'kind':'identity','operands':[expr]}};p['additional_operation_expected']={'coordinate-from-edges':'Tuple('+','.join(map(str,derived))+')'}
 else:p=v(label,expr,'Tuple('+','.join(map(str,printed))+')',kp,method)
 p.update(given_representation='diagram',response_format='numeric',assessed_8227_demand_ids=[LOCATE],canonical_response='('+','.join(map(str,derived))+')',independent_coordinate_construction={'origin_or_base_point':origin,'axis_aligned_edges':edges,'vertex_edge_multipliers':bits,'derived_coordinate':list(derived),'basis':'Axes,edge lengths and labelled vertex incidence on original question render; key does not supply these input relations.'})
 return p

edges=[[5,0,0],[0,2,0],[0,0,3]]
data=[('O',[0,0,0],[0,0,0]),('A',[0,0,1],[0,0,3]),('B',[0,1,1],[0,2,3]),('C',[1,1,1],[5,2,3]),('D',[1,0,1],[5,0,3]),('E',[1,0,0],[5,0,0]),('F',[1,1,0],[5,2,0]),('G',[0,1,0],[0,2,0])]
add('Example',1,234,'Read every vertex of the original cuboid with origin O and axis-aligned sides x5,y2,z3, preserving source labels O,A–G.',[coordinate(name,[0,0,0],edges,bits,key,234)for name,bits,key in data])
edges=[[3,0,0],[0,7,0],[0,0,2]]
data=[('O',[0,0,0],[0,0,0]),('P',[1,0,0],[3,0,0]),('J',[0,0,1],[0,0,2]),('G',[1,0,1],[3,0,2]),('K',[0,1,1],[0,7,2]),('L',[1,1,1],[3,7,2]),('N',[0,1,0],[0,7,0]),('M',[1,1,0],[3,7,0])]
ps=[coordinate('a-'+name,[0,0,0],edges,bits,key,615)for name,bits,key in data]
edges=[[2,0,0],[0,2,0],[0,0,2]]
data=[('A',[0,0,0]),('B',[1,0,0]),('C',[1,1,0]),('D',[0,1,0]),('E',[0,1,1]),('F',[1,1,1]),('G',[1,0,1]),('H',[0,0,1])]
for name,bits in data:
 # G alone happens to share a label with the copied(a)key, but its value is wrong.
 p=coordinate('b-'+name,[2,0,0],edges,bits,[3,0,2]if name=='G'else None,615,missing=name!='G')
 if name=='G':p['author_expected_normalised']='Tuple(4,0,2)'
 ps.append(p)
r=add('Try-Now',1,235,'Read all vertices in two different prisms: (a)origin cuboid x3,y7,z2; (b)side2cube spanning x2..4,y0..2,z0..2 with vertices A–H. The answer list under(b) was copied from(a).',ps)
r['source_label_warning']='The key(b) repeats O,P,J,G,K,L,N,M and coordinates from(a),rather than answering the cube A–H. Seven requested named vertices have no corresponding key; its coincident G label has the wrong coordinate(3,0,2),not(4,0,2).'
edges=[[2,0,0],[0,2,0],[0,0,2]]
corners=[('A',[-1,-1,1],[-2,-2,2]),('B',[-1,1,1],[-2,2,2]),('C',[1,1,1],[2,2,2]),('D',[1,-1,1],[2,-2,2]),('E',[-1,-1,-1],[-2,-2,-2]),('F',[-1,1,-1],[-2,2,-2]),('G',[1,1,-1],[2,2,-2]),('H',[1,-1,-1],[2,-2,-2])]
add('Example',2,235,'Read all eight vertices A–H of a side4cube CENTRED at the origin, with x/y/z axes parallel to its edges. Coordinates use±2,not±4.',[coordinate(name,[0,0,0],edges,bits,key,235)for name,bits,key in corners])
edges=[[3,0,0],[0,3,0],[0,0,3]]
corners=[('P',[-1,-1,1],[-3,-3,3]),('Q',[-1,1,1],[-3,3,3]),('R',[1,1,1],[3,3,3]),('S',[1,-1,1],[3,-3,3]),('T',[-1,-1,-1],[-3,-3,-3]),('U',[-1,1,-1],[-3,3,-3]),('V',[1,1,-1],[3,3,-3]),('W',[1,-1,-1],[3,-3,-3])]
add('Try-Now-2',1,235,'Read all P–W vertices of a side6cube centred at the origin with shown positive axis directions; half-side coordinates are±3.',[coordinate(name,[0,0,0],edges,bits,key,615)for name,bits,key in corners])
edges=[[7,0,0],[0,4,0],[0,0,5]]
data=[('O',[0,0,0],[0,0,0]),('A',[1,0,0],[7,0,0]),('B',[1,1,0],[7,4,0]),('C',[0,1,0],[0,4,0]),('D',[0,1,1],[0,4,5]),('E',[1,1,1],[7,4,5])]
add('Try-Now-2',2,235,'Read the six vertices of the triangular prism with horizontal face OABC,vertical triangular faces OCD/ABE,and OA7,OC4,CD5 along the displayed x/y/z directions.',[coordinate(name,[0,0,0],edges,bits,key,615)for name,bits,key in data])

refs=[
 (1,233,'Equal translated displacement arrows','The grid shows arrows AtoB andLtoM with equal length and direction at different positions. Equality of free vectors preserves both magnitude and orientation; reversing the endpoints negates the vector.',[NOTATION,GEOM],'diagram',None,'teaching-figure'),
 (2,233,'Scalar multiple and opposite-direction arrows','The three parallel arrows illustrate b=2a andc=−(3/4)b. Positive scaling preserves direction; negative scaling reverses it. Equal direction alone is not equality without equal magnitude.',[NOTATION,SCALE,GEOM],'diagram',None,'teaching-figure'),
 (3,234,'Two-dimensional coordinate grid','The labelled pointK is(3,2) in the displayed x/y plane. This is supporting orientation for the following3D construction,not a separately asked vector-operation task.',[LOCATE],'graph',None,'teaching-figure'),
 (4,234,'Lifted 3D Cartesian grid','The original flat pointK is(3,2,0);P is four units directly above it at(3,2,4). The coordinate order remains(x,y,z) as the page perspective changes.',[LOCATE],'diagram',None,'teaching-figure'),
 (5,234,'Rotated axis-orientation pair','The two miniature drawings rotate the visual positions of x,y,z and mark positive directions. Read labels,not a fixed convention that vertical on the page always meansz.',[LOCATE],'diagram',None,'teaching-figure'),
 (6,234,'Example1 given cuboid','OriginO, x-edge5,y-edge2,z-edge3; labelled vertices O,A–G. Hidden/dotted edges retain the same right-angle Cartesian geometry. No length is inferred by measuring the perspective.',[LOCATE],'diagram','Example:1','given-figure'),
 (7,235,'Try1(a) given cuboid','OriginO,frontx-edge3,depthy-edge7,heightz2. Vertex labels O/P/J/G/K/L/N/M determine which edges are traversed to each coordinate.',[LOCATE],'diagram','Try-Now:1','given-figure'),
 (8,235,'Try1(b) given offset cube','A–H form a side2cube, front lower edgeAB on the x-axis with B at4,soA at2. Depth and height are2. Read actual labels; the printed key incorrectly repeats the previous cuboid list.',[LOCATE],'diagram','Try-Now:1','given-figure'),
 (9,235,'Example2 given centre-origin cube','Side4cube centred atO uses±2 coordinate components. Positive y points into the page’s back-right direction; x andz match the shown arrows. Cube-face labels remain essential.',[LOCATE],'diagram','Example:2','given-figure'),
 (10,235,'Try2Q1 given centre-origin cube','Side6cube centred atO uses±3 components for verticesP–W. Preserve the rotated perspective,hidden edges and sign of each labelled coordinate direction.',[LOCATE],'diagram','Try-Now-2:1','given-figure'),
 (11,235,'Try2Q2 given triangular prism','OABC is the horizontal rectangular face; triangular end facesOCD andABE are vertical. The six vertices are consistent with OA7 alongx,OC4 alongy,andCD5 alongz. A rectangular face can be called the base of this triangular prism.',[LOCATE],'diagram','Try-Now-2:2','given-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C5:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C5:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
 f['mathematical_feature_review']['method']='Read source arrow directions,axis labels,hidden-edge incidence and vertex names. Recompute any explicit coordinate construction from original lengths; this is manual rendered-source interpretation plus arithmetic,not an automated perspective-image proof.'
notes={232:'Chapter title,scope list and biographical portrait only; no mathematical learner task or quantitative teaching diagram starts here. Decorative source furniture is not a teaching asset.',233:'Both displacement/notation and scalar-arrow teaching diagrams are enumerated. Vector positions may differ while the free vectors agree; endpoint order and magnitude still matter.',234:'Both coordinate grids,rotated-axis pair,and all eight Example1 vertex outputs/given cuboid are recorded.',235:'Every Try1(a/b),Example2,Try2Q1/Q2 vertex output and all five given figures are recorded. The copied(b)key is explicit; offset and centred cubes are not interchangeable.'}
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':5,'page_status':'items enumerated'if page!=232 else'prose only','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],'scope_screen':'Cartesian3D coordinate location and vector notation are within scope. Point triples do not automatically assess vector magnitude/displacement or scalar product. No unrelated qualifier is imposed.'}for page in range(232,236)]

if __name__=='__main__':
 for name,data in [('answers-YM-C5-opening.json',{'scope':'Every232–235 original requested vertex output.','items':answers}),('census-YM-C5-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete232–235 source census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
