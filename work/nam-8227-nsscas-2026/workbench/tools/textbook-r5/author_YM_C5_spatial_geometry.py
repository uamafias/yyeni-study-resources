"""YM248–251: spatial midpoints, roof geometry and first scalar products."""
import json
import author_YM_C5_magnitude_units as h
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,NOTATION,GEOM
h.prior.answers.clear();h.prior.new.clear();figures.clear();h.prior.corrections.clear()
answers=h.prior.answers;new=h.prior.new;corrections=h.prior.corrections
POS=h.POS;UNIT=h.UNIT;MAG=h.MAG;DISP='8227:2020:M1:T7:O03:D02';ADD='8227:2020:M1:T7:O02:D01';DOT='8227:2020:M1:T7:O04:D02'
extra=h.extra
def add(kind,n,page,note,parts,rep='text',new_item=False):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 r=h.prior.add(kind,n,page,note,parts,direct,new_item=new_item)
 r.update(representation=rep,assessed_8227_demand_ids=direct,component_demand_ids=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct)))
 r['mapping_rationale']='Map requested spatial positions,displacements,midpoint/equality proofs,unit directions and dot products separately. A midpoint must be expressed from the SAME origin before comparing positions; half a displacement from another point is not itself its position. Spatial diagrams supply incidence,not measured perspective lengths.'
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],'qualifier_applicability_note':'Prescribed Cartesian/vector geometry and scalar product; no formal3Dline equation or cross-product learner method is required. All directions normalised here are nonzero. Source diagram conflicts are recorded separately.'}
 r['precision_angle_check']={'source':'Exact components,radicals and midpoint fractions. The scalar-product illustration explicitly uses45degrees; no numerical angle is requested.','comparison':'Retain exact geometry through normalisation. An angle between two vectors is read after putting their arrows consistently into/out of a common vertex; it does not require parallel directions. Do not substitute a drawn supplementary angle without reversing the corresponding vector sign.'}
 for p in parts:p.setdefault('given_representation',rep);p.setdefault('response_format','symbolic')
 if new_item:new[-1].update(scope_check=r['scope_check'],mapping_rationale=r['mapping_rationale'],representation=rep,assessed_8227_demand_ids=direct,component_demand_ids=r['component_demand_ids'])
 return r
def vector(label,expr,key,kp,direct,method):
 p=v(label,expr,key,kp,method);p['assessed_8227_demand_ids']=direct;return p
def displacement(label,tail,head,key,kp):
 p=vector(label,'Tuple('+','.join(f'({b})-({a})'for a,b in zip(tail,head))+')',key,kp,[DISP,NOTATION],'Read ORIGINAL or explicitly reconstructed spatial endpoints,then subtract tail from head in all three components. Preserve the arrow order and the chosen common axes.');p.update(source_arrow_tail=tail,source_arrow_head=head);return p
def proof(label,conclusion,method,kp,checks):
 p=reasoning(label,conclusion,method+' This confirms a textbook proof result,not an official award table.',kp,'show/prove');p.update(assessed_8227_demand_ids=[GEOM],component_demand_ids=[POS,DISP,ADD],response_format='proof/show-that')
 for name,expr,key in checks:extra(p,name,expr,key)
 return p
def directed_unit(label,components,key,kp,method):
 length='sqrt('+'+'.join(f'({c})**2'for c in components)+')'
 p=vector(label,'Tuple('+','.join(f'({c})/({length})'for c in components)+')',key,kp,[UNIT],method+' The original asks for this direction,so the negative unit vector is not an accepted alternative.');p.update(source_unit_vector_components=components,component_demand_ids=[POS,DISP,MAG]);extra(p,'unit-norm','simplify('+ '+'.join(f'(({c})/({length}))**2'for c in components)+')','1');return p

ps=[vector('a-OG','Tuple(0,4,3)','Tuple(0,4,3)',248,[POS],'The ORIGINAL cuboid has OF=5i+4j+3k with axes parallel to OA,OC,OD. G has no x displacement but the full y/z displacements.'),displacement('a-AG',[5,0,0],[0,4,3],'Tuple(-5,4,3)',248)]
p=proof('b','The two midpoints have the same position(5/2,2,3/2).','Midpoint OF has position OF/2. Midpoint AG has position OA+AG/2,or equivalently(OA+OG)/2. Half of AG ALONE starts at A and is not the required position fromO. Compare both full original-coordinate averages.',248,[('two-midpoints','Tuple((0+5)/2,(0+4)/2,(0+3)/2,(5+0)/2,(0+4)/2,(0+3)/2)','Tuple(Rational(5,2),2,Rational(3,2),Rational(5,2),2,Rational(3,2))')]);ps.append(p)
add('Example',10,248,'Cuboid OABCDEFG,OF=5i+4j+3k,axes parallel OA/OC/OD: find OG,AG and prove the OF/AG midpoints coincide using positions fromO.',ps,'diagram')
ps=[vector('a-i-E','Tuple(6,0,10)','Tuple(6,0,10)',616,[POS,NOTATION],'Original OD=6i,OC=8j,OA=10k; E lies directly aboveD in the triangular prism.'),vector('a-i-B','Tuple(0,8,10)','Tuple(0,8,10)',616,[POS,NOTATION],'B lies directly above the ORIGINAL base vertexC by the same vertical edge10.')]
points={'O':[0,0,0],'D':[6,0,0],'C':[0,8,0],'A':[0,0,10],'E':[6,0,10],'B':[0,8,10]}
for label,tail,head,key in[('a-ii-DC','D','C','Tuple(-6,8,0)'),('a-ii-DE','D','E','Tuple(0,0,10)'),('a-ii-DA','D','A','Tuple(-6,0,10)'),('a-ii-DB','D','B','Tuple(-6,8,10)'),('a-ii-EB','E','B','Tuple(-6,8,0)')]:ps.append(displacement(label,points[tail],points[head],key,616))
ps.extend([vector('b-i-M','Tuple((6+0)/2,(0+8)/2,(0+0)/2)','Tuple(3,4,0)',616,[POS],'M is midpoint of ORIGINAL DC; average the two position vectors.'),vector('b-i-N','Tuple((6+0)/2,(0+8)/2,(10+10)/2)','Tuple(3,4,10)',616,[POS],'N is midpoint of ORIGINAL EB; average both full position vectors.')])
p=proof('b-ii','DN=MB=−3i+4j+10k.','Use the actual midpoint positionsM(3,4,0),N(3,4,10),D(6,0,0),B(0,8,10). Both differences are(−3,4,10). Equal FREE vectors can have different initial points; this equality does not claim D=M orN=B.',616,[('two-differences','Tuple(3-6,4-0,10-0,0-3,8-4,10-0)','Tuple(-3,4,10,-3,4,10)')]);ps.append(p)
add('Try-Now-10',1,249,'Triangular prism with OD6i,OC8j,OA10k: read E/B,form five displacements,find midpoint positionsM/N and establish DN=MB.',ps,'diagram')
ps=[displacement('a',[-5,6,1],[7,-2,3],'Tuple(12,-8,2)',616)]
p=proof('b','Both midpoints have position(1,2,2).','Original A(−5,6,1),C(7,−2,3)average to(1,2,2); original O0,B(2,4,4)average to the same point. Equality is checked in one common coordinate frame.',616,[('midpoints','Tuple((-5+7)/2,(6-2)/2,(1+3)/2,2/2,4/2,4/2)','Tuple(1,2,2,1,2,2)')]);ps.append(p)
add('Try-Now-10',2,249,'OA=(−5,6,1),OB=(2,4,4),OC=(7,−2,3): find AC and prove the AC/OB midpoints coincide.',ps)
pts={'A':[1,2,3],'B':[3,8,1],'C':[7,20,-3],'D':[3,20,0]}
ps=[displacement('a-AB',pts['A'],pts['B'],'Tuple(2,6,-2)',616),displacement('a-BC',pts['B'],pts['C'],'Tuple(4,12,-4)',616),displacement('a-BD',pts['B'],pts['D'],'Tuple(0,12,-1)',616)]
p=proof('b','A,B,C are collinear,with BC=2AB.','Original AB=(2,6,−2),BC=(4,12,−4). They share endpointB; equivalently BA=−AB andBC=−2BA share initial pointB. The direction is nonzero,so all three points lie on one line. A shared endpoint suffices; it need not originally be the tail of both named arrows.',616,[('proportional-residual','Tuple((7-3)-2*(3-1),(20-8)-2*(8-2),(-3-1)-2*(1-3))','Tuple(0,0,0)')]);ps.append(p)
p=vector('c','sqrt((3-1)**2+(8-2)**2+(1-3)**2)/sqrt((7-1)**2+(20-2)**2+(-3-3)**2)','Rational(1,3)',616,[GEOM],'The requested ordered magnitude ratio is |AB|:|AC|=1:3. Independently compute both original squared norms44 and396; alternatively AC=AB+BC=3AB. Keep the actual ratio order.');p['canonical_response']='|AB|:|AC|=1:3';ps.append(p)
add('Try-Now-10',3,249,'Four explicit3Dpositions: form AB,BC,BD,prove A/B/C collinear using the shared pointB,and find |AB|:|AC|=1:3.',ps)
roof={'O':[0,0,0],'D':[10,0,0],'E':[10,8,0],'F':[0,8,0],'G':[2,4,3],'H':[8,4,3]}
ps=[vector('a-D','Tuple(10,0,0)','Tuple(10,0,0)',616,[POS],'OD is the given10metre x-directed rectangle side.'),vector('a-E','Tuple(10,8,0)','Tuple(10,8,0)',616,[POS],'E is the opposite corner of the original10-by8horizontal rectangle.'),vector('a-F','Tuple(0,8,0)','Tuple(0,8,0)',616,[POS],'OF is the given8metre y-directed side.'),vector('a-H','Tuple((10+6)/2,8/2,3)','Tuple(8,4,3)',616,[POS,GEOM],'The6metre ridge is CENTRED over the10metre length and8metre width,at height3. Its far endpoint therefore hasx(10+6)/2=8,y4,z3.')]
for label,tail,head,key in[('b-OG','O','G','Tuple(2,4,3)'),('b-DH','D','H','Tuple(-2,4,3)'),('b-EH','E','H','Tuple(-2,-4,3)'),('b-FG','F','G','Tuple(2,-4,3)')]:ps.append(displacement(label,roof[tail],roof[head],key,617))
p=reasoning('c','Each slanted edge has length sqrt29 metres.','The text-derived centred-ridge positions give squared lengths2²+4²+3²=29for all four slanted edges. The key prints |OG|=sqrt29; symmetry makes this one value applicable to every requested slanted edge. The source diagram’s dotted3segment wrongly attaches G to base cornerF: G−F=(2,−4,3)is not a vertical height and its length is sqrt29,not3.',617,'matches');p.update(assessed_8227_demand_ids=[MAG],units='m',printed_key_units='m',response_format='numeric')
extra(p,'all-four-squared-lengths','Tuple(2**2+4**2+3**2,(-2)**2+4**2+3**2,(-2)**2+(-4)**2+3**2,2**2+(-4)**2+3**2)','Tuple(29,29,29,29)');ps.append(p)
r=add('Try-Now-10',4,249,'Symmetric hip roof over rectangle OD10m,OF8m; ridgeGH6m at height3m. Find four positions,four slanted-edge vectors and their common lengthsqrt29m from the stated centred geometry.',ps,'diagram');r['source_label_warning']='The native given diagram draws the dotted3height fromGtoF,contradicting its centred ridge/text/key. G=(2,4,3),F=(0,8,0),so FG is not vertical. A valid future original diagram must dropGto(2,4,0),notF. Correct text-derived/key coordinates remain retained.'
p=directed_unit('unit-OC',['6','-3','6'],'Tuple(Rational(2,3),-Rational(1,3),Rational(2,3))',250,'Original OA=(2,−5,−2),OB=(4,−4,2),andAB=BC force C=2B−A=(6,−3,6). Its norm is9; normalise this reconstructed position,not AB itself.')
extra(p,'original-reconstruction','Tuple(2*4-2,2*(-4)-(-5),2*2-(-2))','Tuple(6,-3,6)')
add('Example',11,250,'Given OA=(2,−5,−2),OB=(4,−4,2),andAB=BC,reconstruct C then find the unit vector in directionOC. This worked example was absent from the older inventory.',[p],new_item=True)
ps=[vector('a-D','Tuple(3,0,-4)','Tuple(3,0,-4)',617,[POS,NOTATION],'Read original OD=3i−4k in the chosen origin frame; the omitted j component is0.'),displacement('b-CD',[4,-1,3],[3,0,-4],'Tuple(-1,1,-7)',617),directed_unit('c-unit-OB',['1','-2','-2'],'Tuple(Rational(1,3),-Rational(2,3),-Rational(2,3))',617,'Original OB=i−2j−2k has norm3. Normalise THAT specified vector; CD from the previous part is a different direction.')]
add('Try-Now-11',1,250,'Original OB=(1,−2,−2),OC=(4,−1,3),OD=(3,0,−4): give Dcoordinates,CD,and unit vector specifically in directionOB.',ps)
ps=[displacement('a-AC',[1,-3,2],[3,1,-2],'Tuple(2,4,-4)',617),directed_unit('b-unit-OM',['2','-1','0'],'Tuple(2/sqrt(5),-1/sqrt(5),0)',617,'Original A(1,−3,2),C(3,1,−2)have midpointM(2,−1,0). Normalise OM,not half the displacementAC. The unused original B(−1,3,5)does not change the requested midpoint.')]
extra(ps[-1],'original-midpoint','Tuple((1+3)/2,(-3+1)/2,(2-2)/2)','Tuple(2,-1,0)')
add('Try-Now-11',2,250,'From given position columns A(1,−3,2),B(−1,3,5),C(3,1,−2),find AC and the unit vector towards midpointMofAC.',ps)
p=vector('dot','sqrt(200)*5*cos(45*pi/180)','50',251,[DOT],'Use the ORIGINAL supplied magnitudes sqrt200 and5 and the explicit angle45DEGREES. Convert45degrees to pi/4for symbolic cosine; the scalar result is50,not a vector.')
add('Unnumbered-scalar-product',1,251,'Inline scalar-product illustration from supplied magnitudes sqrt200,5 and angle45degrees,with exact scalar result50.',[p])
p=vector('dot','8*4+(-6)*(-3)+(-10)*0','50',251,[DOT],'Multiply corresponding ORIGINAL components of a=(8,−6,−10),b=(4,−3,0),then add. A missing k component in b is0; the scalar result is50.')
p['source_dot_vectors']=[['8','-6','-10'],['4','-3','0']]
extra(p,'norms','Tuple(sqrt(8**2+(-6)**2+(-10)**2),sqrt(4**2+(-3)**2))','Tuple(sqrt(200),5)')
add('Unnumbered-scalar-product',2,251,'Inline component scalar-product illustration(8,−6,−10)dot(4,−3,0)=50,paired with the magnitude-angle illustration.',[p])

refs=[
 (45,248,'Spatial basis and cuboid resultant','The generic3Ddiagram resolves OR into ai,bj,ck along the displayed orthogonal axes. Its diagonal is a sum of components,not a sum of their Euclidean magnitudes.',[NOTATION,POS],'diagram',None,'teaching-figure'),
 (46,248,'Example10 given cuboid','Oorigin,axes parallelOA/OC/OD,OF=(5,4,3). Opposite vertices and diagonals must retain consistent labels before midpoint positions are compared.',[POS,DISP,GEOM],'diagram','Example:10','given-figure'),
 (47,248,'Example10 worked spatial route/midpoint panels','The solution diagrams show OG=(0,4,3),AG=(−5,4,3),and the shared midpoint positionOA+AG/2=OF/2. The offset OA cannot be dropped when halving a displacement fromA.',[POS,DISP,GEOM],'diagram','Example:10','teaching-figure'),
 (48,249,'Try10Q1 given triangular prism','OD=(6,0,0),OC=(0,8,0),OA=(0,0,10); the upper triangleAEBis the base triangleODClifted10alongz. Hidden edges/vertex names determine displacements and midpoint positions.',[POS,DISP,GEOM],'diagram','Try-Now-10:1','given-figure'),
 (49,249,'Try10Q4 given roof with height attachment conflict','Text specifies a centred6metre ridge3metres above a10-by8rectangle. Correct G/H=(2,4,3)/(8,4,3). The source dotted height attaches toF(0,8,0),which is not the vertical projection ofG. A consistent new asset must use projection(2,4,0),keeping slantedFG distinct from vertical height3.',[POS,DISP,MAG,GEOM],'diagram','Try-Now-10:4','given-figure'),
 (50,251,'Scalar-product introductory free arrows','The pair illustrates two free vectors,not necessarily parallel. Translate their tails to a common point when reading the between-vector angle; vector placement is irrelevant but orientation is not.',[DOT],'diagram',None,'teaching-figure'),
 (51,251,'Scalar-product formulas and paired inline illustrations','The two-column table gives |a||b|cos(theta)and the component dot sum. Its two explicit Find examples already have separate stable micro-item records; this reference table is not a second pair of problems.',[DOT],'table',None,'teaching-figure'),
 (52,251,'Common-vertex arrow orientation panel','Both arrows directed OUT of a common vertex,or BOTH reversed into it,give the same between-vector angle. One-in/one-out uses the supplement of the drawn angle. The title says vectors must point in the same direction; interpret its diagrams as consistent vertex orientation,not a requirement that vectors be parallel.',[DOT],'diagram',None,'teaching-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C5:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C5:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
 f['mathematical_feature_review']['method']='Read original Cartesian axes,hidden-edge incidence,centering and vector-arrow directions. Verify coordinates and midpoint/vector identities against the stated geometry; explicitly retain the roof diagram conflict rather than treating perspective placement as proof.'
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'Every Example10/11,Try10Q1–4,Try11Q1/2,and both already-indexed scalar-product micro-items is recorded over248–251,with all given/worked spatial and dot-product panels. Example11is a newly recovered source record. Midpoint positions require a common origin; the roof height conflict is preserved separately from valid text/key derivations.','scope_screen':'Elementary3Dposition/displacement/midpoint,unit direction and scalar product are prescribed. No learner cross-product/formal3Dline method is mandated. Exact values and45degree source angle are retained.'}for page in range(248,252)]

if __name__=='__main__':
 for name,data in [('answers-YM-C5-spatial-geometry.json',{'scope':'Every248–251 requested output and explicit scalar-product illustration.','items':answers}),('census-YM-C5-spatial-geometry.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete248–251 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
