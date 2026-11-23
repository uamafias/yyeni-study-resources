"""All10Cresponses;spatial reference choices and independent parameter cases."""
import json
from author_Goldie_C10_dot_opening import W,SRC,SHA,add as source_add,answers,new,fig,figures,corrections,ev,v,reasoning,compute,expression,equivalent,angle,dot,dot_expr,norm_expr,DOT,ANGLE,PERP,MAG,DISP
answers.clear();new.clear();figures.clear();corrections.clear()
UNIT='8227:2020:M1:T7:O03:D01';POS='8227:2020:M1:T7:O03:D03';GEOM='8227:2020:M1:T7:O02:D03'
def add(n,page,note,parts,direct,components=None,rep='text',attr=None):
 row=source_add('Exercise-10C',n,page,note,parts,direct,components,rep=rep,exam_attribution=attr)
 row['precision_angle_check']={'source':'Q6(ii)/8(i)explicitly ask nearest degree;Q12(iii)explicitly asks1decimal place. Other numeric angles use the cited1decimal-degree key displays. Q11key also accepts0.763radians. Exact vectors,unit vectors,cosines and parameter roots are retained.','comparison':'Keep each original instruction distinct from a chosen display comparison. Select both rays from the requested vertex;for elevation first select the horizontal projection. A temporary parameter value in one part doesnot constrain the next general case.'};return row
def unit(label,components,key,kp,method):
 norm=norm_expr(components);expr='Tuple('+','.join(f'({z})/({norm})'for z in components)+')'
 p=v(label,expr,key,kp,method);p['source_unit_vector_components']=components;return p
def perimeter(label,points,key,kp,dp=None,sf=None,method=None):
 lengths=[]
 for a,b in zip(points,points[1:]+points[:1]):lengths.append('sqrt('+ '+'.join(f'(({y})-({x}))**2'for x,y in zip(a,b))+')')
 expr='+'.join(lengths);p=v(label,expr,key,kp,method or'Compute every original side displacement,then sum its positive Euclidean length. Apply only the individually recorded final rounding;the vector sum around a triangle is not its perimeter.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})};p['source_perimeter_points']=points;return p

parts=[]
for label,a,b,key in [('i',['2','3'],['4','1'],'42.3'),('ii',['2','-1'],['1','2'],'90'),('iii',['-1','-1'],['-1','-2'],'18.4'),('iv',['4','1'],['1','1'],'31.0'),('v',['2','3'],['-6','4'],'90'),('vi',['3','-1'],['-6','2'],'180')]:parts.append(angle(label,a,b,key,357))
add(1,268,'Find six2Dbetween-vector angles,including perpendicular and opposite cases. The last answer is180°,not a zero angle between unoriented supporting lines.',parts,[ANGLE],[DOT,MAG])

parts=[v('i-AB','Tuple(6-3,3-2)','Tuple(3,1)',357,'SubtractA=(3,2)fromB=(6,3).'),v('i-BC','Tuple(5-6,6-3)','Tuple(-1,3)',357,'SubtractBfromC=(5,6);retain the joining orderBC.')]
p=dot('ii-right-angle',['-3','-1'],['-1','3'],'0',357,'The angleABCis atB,so useBA=(−3,−1)andBC=(−1,3). Their scalar product is0andboth are nonzero;thereforethe angle is90°.');p['check_mode']='show/prove';parts.append(p)
p=v('iii-equal-lengths','Tuple(sqrt(3**2+1**2),sqrt((-1)**2+3**2))','Tuple(sqrt(10),sqrt(10))',357,'Compute the independent component norms ofABandBC. Both equal√10,which establishes the stated equality.');p['check_mode']='show/prove';parts.append(p)
parts.append(v('iv-D','Tuple(3+5-6,2+6-3)','Tuple(2,5)',357,'For consecutive square verticesA,B,C,the fourth point isD=A+C−B=(2,5). This also follows from equal opposite side vectors;the preceding right-angle/equal-side results justify the square geometry.'))
add(2,268,'From three2Dpoints,writeABandBC,prove a right angle and equal adjacent lengths,and find the fourth square vertex. Numerical joining vectors and geometric conclusions remain separate responses.',parts,[DISP,PERP,MAG,GEOM],[DOT])
parts=[]
for label,a,b,key in [('i',['2','1','3'],['2','-1','4'],'29.0'),('ii',['1','-1','0'],['3','1','5'],'76.2'),('iii',['3','2','-2'],['-4','-1','3'],'162.0')]:parts.append(angle(label,a,b,key,357))
add(3,269,'Find three3Dangles between pairs of vectors in column andi,j,kforms,including an obtuse angle. Preserve each ordered component and signed dot product.',parts,[ANGLE],[DOT,MAG])

parts=[reasoning('i-G','G=(0,4,3)m.',
 'The room’s rectangular coordinate edges placeCabove the yaxis at(0,4,0)andDaboveOat(0,0,3). Gisthe upper back-left corner,so add those independent edge displacements. Do not read its perspective position as a newxcoordinate.',357,'matches'),v('ii-AG','Tuple(0-5,4-0,3-0)','Tuple(-5,4,3)',357,'UseA=(5,0,0)andG=(0,4,3). The direction fromAtoGis(−5,4,3),not its negative.')]
p=v('ii-distance','sqrt((-5)**2+4**2+3**2)','5*sqrt(2)',357,'The straight string length is|AG|=√50=5√2metres. It is not the sum of room edge lengths.');p['source_vector_components']=['-5','4','3'];p['source_vector_output']='magnitude';p['answer_unit']='m';parts.append(p)
parts.append(angle('iii-elevation',['-5','4','3'],['-5','4','0'],'25.1',357,method='The requested elevation is the angle betweenAGand its horizontal projection(−5,4,0). Their dot product is41,the norms are√50and√41,andthe angle is about25.1°. Equivalently use sinθ=3/√50. The angle to the vertical is its complement,not the requested answer. The source doesnot explicitly force a scalar-product method in this part.'))
add(4,269,'Read the rectangular-room coordinates,find the string vector/length,and calculate the spider journey’s elevation. Selecting the horizontal reference direction is an additional geometric decision.',parts,['8227:2020:M1:T7:O01:D01',DISP,MAG,ANGLE],rep='diagram')

parts=[v('i-OQ','Tuple((0+6)/2,(0+6)/2,(6+6)/2)','Tuple(3,3,6)',357,'The6-unit cube givesD=(0,0,6),F=(6,6,6). Their midpoint isQ=(3,3,6).'),v('i-PQ','Tuple(3-6,3-2,6-0)','Tuple(-3,1,6)',357,'AP=(1/3)ABplacesP=(6,2,0). SubtractPfromQto obtainPQ=(−3,1,6).')]
parts.append(angle('ii-OQP',['-3','-3','-6'],['3','-1','-6'],'53.0',357,method='The vertex isQ,so useQO=(−3,−3,−6)andQP=(3,−1,−6). Their dot product is30andnorms√54,√46. Reversing both vectors gives the same angle;reversing only one gives the supplementary angle. The requested answer is about53.0°.'))
add(5,269,'Use a cube,one trisection point and one face-diagonal midpoint to deriveOQ/PQandfind∠OQP. All constructed points share the same cube data.',parts,[POS,DISP,ANGLE],[DOT,MAG],rep='diagram',attr='Cambridge9709Paper12Q6November2009')

parts=[v('i-perpendicular-p','solve(2*3+1*(-2)+2*p,p)[0]','-2',357,'For generalp,the dot product is4+2p. Set it to0to establish perpendicularity;both original vectors are nonzero for allrealp.')]
p=angle('ii-angle-p6',['2','1','2'],['3','-2','6'],'40',357,dp=0,method='This part explicitly sets p=6andrequires a scalar product. The dot is16andnorms3and7,soθ=acos(16/21),rounded at the end to the nearest degree:40°. Do not carry p=−2from(i).');p['case_condition']='p=6only for(ii)';parts.append(p)
parts.append(v('iii-AB','Tuple(3-2,-2-1,p-2)','Tuple(1,-3,p-2)',357,'Return to generalp,as the source does. The joining vector isAB=(1,−3,p−2).'))
p=v('iii-p-values','FiniteSet(*solve(1+9+(p-2)**2-Rational(7,2)**2,p))','FiniteSet(Rational(1,2),Rational(7,2))',357,'The specified length3.5gives10+(p−2)²=49/4,so(p−2)²=9/4. Bothp=1/2and7/2satisfy the original length. No sign restriction removes either root.')
p['source_dependency_edges']=[{'from':'iii-AB','type':'cue','cue':'hence find the values','role':'Use the general-pjoining vector,not the special case from(ii).'}];parts.append(p)
add(6,270,'A common vector pair has three separate cases:perpendicular parameter,an explicitp6angle,and a general-pdistance constraint. Preserve these case boundaries and both length roots.',parts,[PERP,ANGLE,DISP,MAG],[DOT],attr='Cambridge9709Paper1Q10June2008')

parts=[dot('i-dot',['2','-8','4'],['7','2','-1'],'-6',357)]
parts.append(reasoning('i-angle-type','The angleAOBis obtuse.',
 'The original vectors are nonzero and their scalar product is−6<0. Thuscosθ<0for the non-reflex between-ray angle,so90°<θ<180°. A numerical inverse-cosine calculation is unnecessary for this classification.',357,'matches'))
parts.append(unit('ii-unit-OX',['4','-4','2'],'Tuple(Rational(2,3),-Rational(2,3),Rational(1,3))',357,'Native4xsource confirmsAX=(2/5)AB. HenceOX=a+(2/5)(b−a)=(4,−4,2),withnorm6. Divide by6to obtain its same-direction unit vector. The multiplier is not2/3.'))
parts[-1]['additional_operations']={'source_OX':{'kind':'identity','operands':['Tuple(2+Rational(2,5)*(7-2),-8+Rational(2,5)*(2-(-8)),4+Rational(2,5)*(-1-4))']}};parts[-1]['additional_operation_expected']={'source_OX':'Tuple(4,-4,2)'}
add(7,270,'Calculate a dot product and classify the angle by its sign,then find the unit vector of an internally defined pointX. The2/5fraction is verified on the native source enlargement.',parts,[DOT,ANGLE,UNIT],[POS,MAG],attr='Cambridge9709Paper1Q6June2009')

parts=[angle('i-angle',['2','3','-1'],['4','-3','2'],'99',357,dp=0,method='Use the explicitly required scalar product. It is−3;the norms are√14and√29. The obtuse angle rounds to99°at the nearest degree,as the source requires.')]
parts.append(unit('ii-unit-AB',['2','-6','3'],'Tuple(Rational(2,7),-Rational(6,7),Rational(3,7))',357,'The joining vectorB−A=(2,−6,3)hasnorm7. Divide by7;the source asks the directionAB,notBA.'))
parts[-1]['additional_operations']={'original_AB':{'kind':'identity','operands':['Tuple(4-2,-3-3,2-(-1))']}};parts[-1]['additional_operation_expected']={'original_AB':'Tuple(2,-6,3)'}
p=v('iii-p-values','FiniteSet(*solve((0-2)**2+(6-3)**2+(p-(-1))**2-((4-2)**2+(-3-3)**2+(2-(-1))**2),p))','FiniteSet(-7,5)',357,'Native4xsource confirmsOC=6j+pk,with noicomponent. ThusAC=(−2,3,p+1),while|AB|²=49. Equality gives13+(p+1)²=49,hencep=−7or5. Both original lengths are7.')
parts.append(p)
add(8,270,'Find a nearest-degree angle,a unit joining vector,and both parameters making two lengths equal. Preserve the zeroicomponent of the givenCposition vector.',parts,[ANGLE,UNIT,MAG],[DOT,DISP],attr='Cambridge9709Paper1Q11June2005')

expr='((-2)*2+3*1+1*3)/(sqrt((-2)**2+3**2+1**2)*sqrt(2**2+1**2+3**2))'
p=v('i-cosine-q3',expr,'Rational(1,7)',270,'This part explicitly setsq=3. The scalar product is2andboth norms are√14,so cos∠POQ=1/7. The requested evidence is the exact cosine ratio,not a rounded inverse-cosine angle.');p['check_mode']='show/prove';p['source_cosine_vectors']=[['-2','3','1'],['2','1','3']];p['case_condition']='q=3only for(i)'
p2=v('ii-q-values','FiniteSet(*solve((2-(-2))**2+(1-3)**2+(q-1)**2-6**2,q))','FiniteSet(-3,5)',357,'Return to generalq. The joining vectorPQ=(4,−2,q−1)has specified length6,so20+(q−1)²=36. Henceq=−3or5;do not retain the earlier special valueq=3.')
add(9,270,'Establish an exact cosine for an explicit parameter case,then solve a separate general-parameter length condition. Exact ratio evidence and two-root solving are retained as distinct responses.',[p,p2],[ANGLE,MAG],[DOT,DISP],attr='Cambridge9709Paper1Q4November2005')

parts=[v('i-PA','Tuple(-6-0,0-8,0-6)','Tuple(-6,-8,-6)',357,'TakeO=(0,0,0),ODalongi,OMalongj,andOEalongk. ThenA=(−6,0,0),P=(0,8,6),soPA=A−P.'),v('i-PN','Tuple(6-0,20/2-8,0-6)','Tuple(6,2,-6)',357,'D=(6,0,0),C=(6,20,0),so their midpointN=(6,10,0). SubtractP=(0,8,6)to obtainPN=(6,2,−6).')]
parts.append(angle('ii-APN',['-6','-8','-6'],['6','2','-6'],'99.1',357,method='The requested angleAPNis atP. Use the two outward vectorsPAandPN;their dot product is−16andnorms√136,√76. A semicircular solid is the representation,but the demanded calculation is coordinate/vector geometry,not circle area or prism volume.'))
add(10,271,'Derive two joining vectors from a semicircular-prism diagram and use the scalar product for∠APN. Radius,length,midpoint andalong-ridge distance fix one shared coordinate model.',parts,[DISP,ANGLE],[DOT,MAG],rep='diagram',attr='Cambridge9709Paper1Q4October2008')

parts=[reasoning('i-OD','OD=4i+4j+5km.',
 'All four sloping edges are equal,the base is14×8,andthe level ridge is6long atheight5. Equal side slopes centre the ridge across width8,givingy4;equal end slopes split the leftover14−6into4at each end. ThusD=(4,4,5). Do not placeDabove the full base midpointx7.',358,'matches')]
p=v('i-length','sqrt(((14-6)/2)**2+(8/2)**2+5**2)','7.55',358,'The derivedODvector has exact norm√57metres. The source key’s7.55is a3significant-figure display;retain√57internally.');p['operation']={'kind':'rounded','operands':['sqrt(((14-6)/2)**2+(8/2)**2+5**2)'],'significant_figures':3};p['source_vector_components']=['4','4','5'];p['source_vector_output']='magnitude';p['answer_unit']='m';parts.append(p)
p=angle('ii-DOB',['4','4','5'],['14','8','0'],'43.7',358,method='The angle is atO. UseOD=(4,4,5)andOB=(14,8,0). Their dot is88andnorms√57,√260. The source key gives43.7°or0.763radians;both units express the same angle.')
p['additional_operations']={'radian_display':{'kind':'rounded','operands':['acos(88/(sqrt(57)*sqrt(260)))'],'significant_figures':3}};p['additional_operation_expected']={'radian_display':'0.763'};parts.append(p)
add(11,271,'Infer the centred roof-ridge coordinates from equal slope lengths,findODandits magnitude,and use a scalar product for∠DOB. The coordinate reconstruction is essential evidence before the angle calculation.',parts,['8227:2020:M1:T7:O01:D01',POS,MAG,ANGLE],[DOT],rep='diagram',attr='Cambridge9709Paper1Q8June2006')

parts=[v('i-PR','Tuple(4-4/2,4/2-0,4/2-0)','Tuple(2,2,2)',358,'In the4-unit cube,PmidpointsOAsoP=(2,0,0). RcentresABFEsoR=(4,2,2). SubtractPfromR.'),v('i-PQ','Tuple(0-4/2,4/2-0,4-0)','Tuple(-2,2,4)',358,'QmidpointsDGwithD=(0,0,4),G=(0,4,4),soQ=(0,2,4). SubtractP=(2,0,0).')]
parts.append(angle('ii-QPR',['-2','2','4'],['2','2','2'],'61.9',358,method='UsePQandPRfrom the common vertexP. Their dot product is8,the norms are√24and√12,andthe included angle isabout61.9°. The source explicitly requires a scalar product.'))
parts.append(perimeter('iii-perimeter',[['2','0','0'],['0','2','4'],['4','2','2']],'12.8',358,dp=1,method='The three side lengths are√24,√12,√20. Sum them before rounding to the explicitly required1decimal place:12.8units. The third sideQRmust be included even though the angle uses only the first two.'))
add(12,272,'Use the cube’s two edge midpoints and one face centre to find joining vectors,an explicitly scalar-product angle,andthe triangle perimeter to1decimal place. The given construction fixes all three side lengths.',parts,[DISP,ANGLE,MAG],[DOT],rep='diagram',attr='Cambridge9709Paper1Q10November2007')

for n,page,label,note,teaches,parent in [
 (43,268,'Figure10.20 common-vertex3Dangle','P=(1,0,−1),Q=(2,4,1),R=(3,5,6). The requested∠QPRusesPQandPR,both directed fromP. The2Dprojection of the drawing is not the true3Dangle.',[ANGLE,DISP],'Example:11'),
 (44,268,'Figure10.21 supplementary-angle warning','Reversing onlyPQtoQPchanges the measured angle to its supplement. Reversing both rays preserves their angle. The dot-product sign must match the chosen vertex/rays.',[ANGLE,DISP],None),
 (45,269,'Exercise10C4 room/string diagram','Room coordinatesA(5,0,0),C(0,4,0),D(0,0,3)metres fixG=(0,4,3). The spider follows the straight stringAG;its elevation comparesAGwithits horizontal projection,not with the vertical edge.',[DISP,MAG,ANGLE],'Exercise-10C:4'),
 (46,269,'Exercise10C5 cube with trisection/midpoint','Cube side6;P=A+(1/3)AB=(6,2,0),Q=(D+F)/2=(3,3,6). ∠OQPis atQ. Do not mix this diagram’s point labels with the4-unit cube in10C12.',[POS,DISP,ANGLE],'Exercise-10C:5'),
 (47,271,'Exercise10C10 semicircular prism','Radius6,length20,andEP8giveP=(0,8,6). The DCmidpoint isN=(6,10,0),with axes alongOD,OM,OE. Circle/prism context fixes coordinates;no circle-area/volume calculation is requested.',[DISP,ANGLE],'Exercise-10C:10'),
 (48,271,'Exercise10C11 centred roof ridge','BaseOA14,OC8,ridgeheight5,length6,andequal four slope lengths implyD=(4,4,5),E=(10,4,5). The ridge endpoints are not above the base centre(7,4). Equal-edge constraints must remain coupled if varied.',[POS,MAG,ANGLE],'Exercise-10C:11'),
 (49,272,'Exercise10C12 cube/triangle cross-section','Side4;P=(2,0,0),Q=(0,2,4),R=(4,2,2)derive from the stated edge midpoints/face centre. The shaded triangle isPQR;perimeter needsQRaswellas the two angle rays.',[DISP,ANGLE,MAG],'Exercise-10C:12')]:fig(n,page,label,note,teaches,'diagram',[],parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
pages=[]
for page in range(268,272):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:Goldie:C10:Example:11']if page==268 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every10C1–11response and given/reference diagram recorded.10C12andits figure start272andmust be linked by the following line-boundary census. The native270crop resolves2/5andthe missingicomponent in7/8.','scope_screen':'All requested vector calculations/proofs are within8227;spatial givens and independent parameter cases are preserved.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C10-10C.json',{'scope':'Every10C1–12response,with all spatial diagrams,method instructions and independent parameter cases.','items':answers}),('census-Goldie-C10-10C.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete268–271;12andits figure on272are linked by the next census.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
