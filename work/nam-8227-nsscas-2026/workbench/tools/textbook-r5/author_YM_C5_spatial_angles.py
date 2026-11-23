"""YM256–259: spatial angles, parameter constraints and Exercise5 opening.

Fixed original source operands, independently compared with the printed keys.
This is textbook source analysis, not a runtime recipe generator.
"""
import json
import author_YM_C5_dot_angles as h
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
from author_YM_C5_spatial_geometry import directed_unit

h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
MAG=h.MAG;POS=h.POS;DISP=h.DISP;GEOM=h.GEOM;DOT=h.DOT;ANGLE=h.ANGLE;PERP=h.PERP
UNIT='8227:2020:M1:T7:O03:D01';PARALLEL='8227:2020:M1:T7:O02:D03'
extra=h.extra
def add(kind,n,page,note,parts,representation='text'):
    return h.add(kind,n,page,note,parts,representation)
def vector(label,expr,key,kp,direct,method):
    p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,response_format='symbolic');return p
def proof(label,result,method,kp,direct):
    p=reasoning(label,result,method,kp,'show/prove');p.update(assessed_8227_demand_ids=direct,response_format='proof/show-that');return p
def angle(label,u,w,key,kp,dp=1,method=None):
    p=h.angle(label,u,w,key,kp,dp=dp,method=method)
    p.update(assessed_8227_demand_ids=[ANGLE],component_demand_ids=[DOT,MAG]);return p
def parameter(label,expr,key,kp,direct,method):
    p=vector(label,expr,key,kp,direct,method);p['component_demand_ids']=[DOT,MAG]if ANGLE in direct else[DOT];return p

add('Try-Now-15',1,256,'Pyramid with OA6cm,OB8cm,OC10cm along orthogonal axes: use a scalar product for the angle ACB at the top vertex,not the base angle.',[
 angle('angle-ACB',['6','0','-10'],['0','8','-10'],'48.0',617,method='Original A=(6,0,0),B=(0,8,0),C=(0,0,10). Both CA=(6,0,−10) andCB=(0,8,−10) start atC. Dot100,norms sqrt136/sqrt164. Retain these values to the final degree-mode angle.')],'diagram')
p=vector('a-OD','Tuple((14-6)/2,8/2,5)','Tuple(4,4,5)',617,[DISP,GEOM],'The rectangular base is14by8,the centred ridge is6 at height5,and the four sloping edges are equal. Symmetry gives the ridge startD=(4,4,5),not a base corner. Keep the height separate from sloping OD.')
ps=[p,h.h.norm('a-magnitude',['4','4','5'],'sqrt(57)',617),angle('b-angle-DOB',['4','4','5'],['14','8','0'],'43.7',617,method='Original roof vertexD=(4,4,5),opposite base cornerB=(14,8,0). Both requested raysOD andOB start atO. Their dot is88 and squared norms57/260. The roof edge slope or a projected plan angle is not DOB.')]
add('Try-Now-15',2,256,'Equal-sloping-edge hip roof: derive OD=(4,4,5),its magnitude sqrt57,and the spatial angle DOB43.7degrees from the rectangular base and centred ridge.',ps,'diagram')
ps=[vector('a-MO','Tuple(0-(-4),0-0,0-6)','Tuple(4,0,-6)',617,[DISP],'Radius4,height12 and diameterBA give B=(−4,0,0),Bprime=(−4,0,12),so midpointM=(−4,0,6). Subtract M fromO for the requested arrow MO.'),vector('a-MC-prime','Tuple(0-(-4),4-0,12-6)','Tuple(4,4,6)',617,[DISP],'Original OC is perpendicular toOA and points along positivej. Thus Cprime=(0,4,12); subtract the actual midpointM=(−4,0,6).'),angle('b-angle-OMC-prime',['4','0','-6'],['4','4','6'],'109.7',617,method='Both MO andMCprime start atM. Their dot16−36=−20 is NEGATIVE,so angleOMCprime is obtuse. Squared norms52 and68. Do not discard the sign or use the acute supplement.')]
add('Try-Now-15',3,256,'Cylinder radius4,height12,with midpointM of the back diameter-end vertical: derive MO,MCprime and their obtuse angle atM.',ps,'diagram')

ps=[h.h.norm('a',['2','-1','sqrt(11)'],'4',257)]
# The independent Fraction vector checker cannot parse radical source inputs.
ps[0].pop('source_vector_components');ps[0].pop('source_vector_output')
ps.append(vector('b-B','Tuple(8*2/4,8*(-1)/4,8*sqrt(11)/4)','Tuple(4,-2,2*sqrt(11))',257,[POS,UNIT],'Original OA=(2,−1,sqrt11) has length4. Producing OA to B with OB8 uses the POSITIVE multiplier2; a point on the opposite ray would not satisfy produced.'))
ps.append(parameter('c-i-p','solve(2-p,p)[0]','2',257,[PERP],'Original OC=(1,p,0). Its dot with OA is2−p. Both vectors are nonzero for every realp,so perpendicularity is equivalent to2−p=0.'))
p=parameter('c-ii-p','FiniteSet(*solve((2-p)**2-4*(1+p**2),p))','FiniteSet(0,-Rational(4,3))',257,[ANGLE],'Original cosine equation is(2−p)/(4sqrt(1+p²))=1/2. Before squaring require2−p>=0. Squaring givesp(3p+4)=0; both candidates0,−4/3 satisfy the ORIGINAL positive-cosine equation and nonzero norms.')
extra(p,'original-cosine-at-both-roots','Tuple((2-0)/(4*sqrt(1+0**2)),(2+Rational(4,3))/(4*sqrt(1+Rational(16,9))))','Tuple(Rational(1,2),Rational(1,2))');ps.append(p)
add('Example',16,257,'Magnitude and extended-ray position from OA=(2,−1,sqrt11),then determine OC=(1,p,0) at90 and60degrees. Check squared-equation roots in the original cosine condition.',ps)

ps=[angle('a',['2','-2','1'],['2','6','3'],'103.8',617),parameter('b-p','solve(2*p+6*p+3*(p+1),p)[0]','-Rational(3,11)',617,[PERP],'For original b=(2,6,3),c=(p,p,p+1),zero dot product gives11p+3=0. c cannot be zero since p andp+1 cannot both vanish.')]
add('Try-Now-16',1,258,'For three given columns,find the obtuse angle betweena,b and the parameter makingb,c perpendicular; the changing vector is not used in the first angle.',ps)
ps=[vector('a-B','Tuple(-3+2,3-3,3+6)','Tuple(-1,0,9)',617,[POS,DISP],'Original A=(−3,3,3),AB=(2,−3,6). Add the displacement to the actual initial point.'),parameter('b-i-q','solve(6*q+72,q)[0]','-12',617,[PARALLEL],'Original CD=(−4,6,q) is parallel toAB=(2,−3,6). The first two component ratios are−2,so the third isq=−12. Verify all three ratios rather than using a zero dot product.'),parameter('b-ii-q','solve(-8-18+6*q,q)[0]','Rational(13,3)',617,[PERP],'The independently reset q now makes the SAME given components perpendicular:−8−18+6q=0. Do not carry the parallel branch q−12 into this part.')]
extra(ps[1],'parallel-residual','Tuple(-4-(-2)*2,6-(-2)*(-3),-12-(-2)*6)','Tuple(0,0,0)')
add('Try-Now-16',2,258,'Recover endpointB,then independently choose q for parallel and perpendicular AB/CD. This explicitly contrasts the two vector decisions with the same known components.',ps)
ps=[h.h.norm('a-a',['2','4','-4'],'6',617),h.h.norm('a-b',['0','-4','3'],'5',617),angle('b-angle-AOB',['2','4','-4'],['0','-4','3'],'159',617,dp=0,method='Original a=(2,4,−4),b=(0,−4,3) have dot−28 and norms6,5. Compute acos(−28/30) and round only the final angle to the explicitly requested NEAREST DEGREE. The key prints159.0 but the original precision is integer degrees.'),h.perpendicular('c',['2','4','-4'],['0','1','1'],617)]
p=vector('d','Tuple(0,10*(-3)/5,10*4/5)','Tuple(0,-6,8)',617,[UNIT],'Original b+c=(0,−3,4) has norm5. Scale by positive2 to get one requested PARALLEL vector of length10; its negative(0,6,−8) is also allowed by parallel-only wording. A key giving one valid vector is complete.')
p.update(valid_alternatives=['Tuple(0,6,-8)'],component_demand_ids=[MAG]);extra(p,'required-length','sqrt(0**2+(-6)**2+8**2)','10');ps.append(p)
add('Try-Now-16',3,258,'Triangular pyramid from three position columns: magnitudes,nearest-degree AOB,perpendicular AOC,and a length10vector parallel tob+c.',ps)
ps=[vector('a-dot','4*8+7*(-1)+(-p)*(-p)','25+p**2',617,[DOT],'Read the native source carefully: A=4i+SEVEN j−pk,not4i+j−pk. B=8i−j−pk. The original dot is32−7+p²=25+p²; the key is correct.')]
p=proof('b','No real p makes OA perpendicular toOB.','The preceding dot is25+p²>=25>0 for every realp. Neither vector is zero. Thus zero dot product is impossible over the real parameter domain; no imaginary parameter is admissible.',617,[PERP]);extra(p,'real-zero-set','solveset(25+p**2,p,domain=S.Reals)','EmptySet');ps.append(p)
p=parameter('c-p','FiniteSet(*solve(2*(25+p**2)-(65+p**2),p))','FiniteSet(-sqrt(15),sqrt(15))',617,[ANGLE],'Both ORIGINAL norms equal sqrt(65+p²). The60degree equation is(25+p²)/(65+p²)=1/2,with denominator strictlypositive. It givesp²15,so retain both real signs. No squaring or extraneous-sign branch is needed.');extra(p,'original-cosine','(25+15)/(65+15)','Rational(1,2)');ps.append(p)
add('Try-Now-16',4,258,'For A=(4,7,−p),B=(8,−1,−p),derive dot25+p²,prove no perpendicular real parameter and find both60degree parameters±sqrt15.',ps)

ps=[vector('a-C','Tuple(3,0,-4)','Tuple(3,0,-4)',617,[POS],'The original OC=3i−4k has zero j component. Read its point coordinates in(x,y,z)order.'),vector('b-BC','Tuple(3-4,0-(-1),-4-3)','Tuple(-1,1,-7)',617,[DISP],'Original B=(4,−1,3),C=(3,0,−4). BC=C−B,not the reverse.')]
p=directed_unit('c',['1','-2','-2'],'Tuple(Rational(1,3),-Rational(2,3),Rational(2,3))',617,'The original OA=i−2j−2k has norm3. SAME DIRECTION requires(1/3,−2/3,−2/3). The printed key changes only the last sign,so it is not parallel toOA.')
p['author_expected_normalised']='Tuple(Rational(1,3),-Rational(2,3),-Rational(2,3))';ps.append(p)
ps.extend([h.perpendicular('d-i',['1','-2','-2'],['4','-1','3'],617),angle('d-ii-AOC',['1','-2','-2'],['3','0','-4'],'42.8',617)])
add('Exercise-5',1,259,'Read C,form BC,normalise OA in its SAME direction,then prove OAperpendicularOB and calculate AOC. The unit key has an isolated final-component sign error.',ps)
ps=[parameter('a-p','FiniteSet(*solve(2*p**2-2*(p-1)+6*(2*p+1),p))','FiniteSet(-1,-4)',617,[PERP],'Original u=(p²,−2,6),v=(2,p−1,2p+1). Their dot is2p²+10p+8=2(p+1)(p+4). Both vectors are always nonzero,so both roots are valid.'),angle('b-p1',['1','-2','6'],['2','0','3'],'30.0',617,method='Part(b) independently sets p=1; it does not select a preceding perpendicular root. Substitute into the ORIGINAL two columns to get(1,−2,6),(2,0,3),dot20,norms sqrt41/sqrt13. Compute the non-reflex angle.')]
add('Exercise-5',2,259,'Solve the quadratic parameter condition for perpendicular vectors,then RESET p=1 for a separate between-directions angle.',ps)
ps=[v('a-OB','sqrt(5**2-(6/2)**2)','4',617,'The ORIGINAL isosceles vertical end has sidesAB=BC5 and baseAC=DF6. O is midpointAC,so its altitudeOB=sqrt(25−9)=4. The longitudinal prism edge12 is not the triangle base.')];ps[0]['assessed_8227_demand_ids']=[GEOM,MAG]
ps.extend([vector('b-MC','Tuple(3-0,0-6,0-4)','Tuple(3,-6,-4)',617,[DISP],'Original O0,C=(3,0,0),B=(0,0,4),E=(0,12,4); midpointM ofBE=(0,6,4). Thus MC=(3,−6,−4).'),vector('b-MN','Tuple(0-0,12-6,0-4)','Tuple(0,6,-4)',617,[DISP],'The base midpointN ofDF is(0,12,0). Subtract midpointM=(0,6,4),notB.'),h.scalar('c-dot',['3','-6','-4'],['0','6','-4'],'-20',617),angle('c-angle-CMN',['3','-6','-4'],['0','6','-4'],'111',617,dp=0,method='Both MC andMN start at the required vertexM. Dot−20,squared norms61/52. The requested nearest-degree angle is obtuse111degrees; the negative numerator must survive inverse cosine.')])
add('Exercise-5',3,259,'Isosceles-ended triangular prism with longitudinal length12,end-base6,sides5: derive altitude4,midpoint displacementsMC/MN,dot−20,and nearest-degree angleCMN.',ps,'diagram')

references=[
 (58,256,'Try15Q1 orthogonal-axis pyramid','O0,A(6,0,0),B(0,8,0),C(0,0,10); target angleACB uses both arrows fromC,not the apparent page angle.',[DISP,ANGLE],'Try-Now-15:1'),
 (59,256,'Try15Q2 equal-edge roof','BaseOABC14by8,ridgeDE6,height5,four equal sloping edges imply D(4,4,5),E(10,4,5). Base diagonalOB=(14,8,0).',[GEOM,DISP,ANGLE],'Try-Now-15:2'),
 (60,256,'Try15Q3 cylinder and midpoint','Radius4,height12; B oppositeA on diameterBA,OCperpendicularOA. M midpointBBprime lies at(−4,0,6),Cprime(0,4,12).',[GEOM,DISP,ANGLE],'Try-Now-15:3'),
 (61,259,'Exercise5Q3 triangular prism','O midpointAC,unitaxes parallelOC,ON,OB. A(−3,0,0),C(3,0,0),B(0,0,4),D(−3,12,0),F(3,12,0),E(0,12,4); M midpointBE,N midpointDF.',[GEOM,DISP,ANGLE],'Exercise-5:3')]
for number,page,label,note,teaches,parent in references:
 fig(number,page,label,note,teaches,'diagram',[],parent)
 r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C5:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C5:')
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure')
 r['mathematical_feature_review']['method']='Read original point labels,orthogonal directions,midpoint/equal-edge marks and lengths. Reconstruct Cartesian coordinates before forming the two rays at the named angle vertex. Perspective lengths are not measured.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=5,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All Try15Q1–3,Example16,Try16Q1–4,andExercise5Q1–3 outputs are enumerated over256–259. Four source geometry figures are separate. Example16 norm work and intermediate parameter algebra are solution steps,not separately asked questions.',scope_screen='Prescribed3Dvector geometry,magnitude,unit direction,dot product,perpendicularity and between-vector angle. Preserve real parameter restrictions and original nearest-degree requests. No formal3Dline/cross-product demand.')for page in range(256,260)]
if __name__=='__main__':
 for name,data in [('answers-YM-C5-spatial-angles.json',dict(scope='All explicit256–259outputs.',items=answers)),('census-YM-C5-spatial-angles.json',dict(book='YM',book_id='8227-SRC-017',chapter=5,source_path=SRC,source_sha256=SHA,scope='Complete256–259page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
