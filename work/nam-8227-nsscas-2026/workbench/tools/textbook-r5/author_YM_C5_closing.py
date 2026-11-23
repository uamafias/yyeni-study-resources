"""YM260–265: remaining vector exercises,revision and source summary."""
import json
import author_YM_C5_spatial_angles as h
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
MAG=h.MAG;POS=h.POS;DISP=h.DISP;GEOM=h.GEOM;DOT=h.DOT;ANGLE=h.ANGLE;PERP=h.PERP;UNIT=h.UNIT
extra=h.extra;vector=h.vector;parameter=h.parameter;proof=h.proof;angle=h.angle
def add(kind,n,page,note,parts,representation='text'):
 r=h.add(kind,n,page,note,parts,representation)
 if page>=261:r.update(exam_style=True,exam_style_basis='Source section5.4Exam-StyleQuestions startsPDF261;PDF263–264continueswith the tariffed30-markRevisionExercise5. This is textbook-labelled practice,not an examination-observed attribution.')
 return r
def rounded(label,expr,key,kp,dp,direct,method):
 p=v(label,expr,key,kp,method);p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp};p.update(assessed_8227_demand_ids=direct);return p

p=proof('a','a=4cm.','A horizontal section of the side10square pyramid has side6. Similar triangles give PD/PO=6/10,so PD6 andOD10−6=4. This uses a positive interior section,not an arbitrary slice of a different orientation.',618,[GEOM]);extra(p,'similar-section-height','10-10*Rational(6,10)','4')
ps=[p,vector('b-BG','Tuple(0-10,6-10,4-0)','Tuple(-10,-4,4)',618,[DISP],'Original O0,A(10,0,0),B(10,10,0),C(0,10,0),P(0,0,10). At height4,the section pointG onPC is(0,6,4). BG=G−B.'),angle('c-angle-GBA',['-10','-4','4'],['0','-10','0'],'69.6',618,method='Both BG andBA start atB. Dot40,squared norms132 and100. The named angleGBA is atB,not the pyramid apex or section corner. Retain exact values to final1decimal-degree display.')]
add('Exercise-5',4,260,'Side10square pyramid,height10,with horizontal side6section: prove its height4,formBG and calculateGBA.',ps,'diagram')
ps=[angle('a-AOB',['-3','6','3'],['-1','2','4'],'36.7',618),h.directed_unit('b-unit-OC',['3','-6','6'],'Tuple(Rational(1,3),-Rational(2,3),Rational(2,3))',618,'Original A=(−3,6,3),B=(−1,2,4),AC=3AB. Thus C=A+3(B−A)=(3,−6,6),norm9. Normalise its POSITION vectorOC in the same direction,not the displacementAC.')]
extra(ps[1],'original-point-construction','Tuple(-3+3*((-1)-(-3)),6+3*(2-6),3+3*(4-3))','Tuple(3,-6,6)')
add('Exercise-5',5,260,'FindAOB,then construct C throughAC=3AB and normaliseOC. Native key confirms its middle component isNEGATIVE,not a key error.',ps)
p=h.directed_unit('a-unit-OB',['4','2','4'],'Tuple(4,2,4)',618,'In original parallelogramOABC,OA=(1,3,3),OC=(3,−1,1),so OB=OA+OC=(4,2,4),norm6. The question asks a UNIT vector,so divide by6. The printed key stops at the unnormalised diagonal.')
p['author_expected_normalised']='Tuple(Rational(2,3),Rational(1,3),Rational(2,3))'
ps=[p,angle('b-acute-diagonals',['4','2','4'],['-2','4','2'],'74.2',618,method='Original diagonals have directionsOB=(4,2,4),AC=(2,−4,−2). Their ordinary vector angle is obtuse105.8degrees,but the question explicitly asks the ACUTE angle between the diagonal LINES. Reverse AC toCA=(−2,4,2); dot8 gives74.2degrees. Keep this line-angle choice explicit rather than taking absolute dot products in every vector-angle question.'),rounded('c-perimeter','2*(sqrt(1**2+3**2+3**2)+sqrt(3**2+(-1)**2+1**2))','15.4',618,1,[GEOM,MAG],'A parallelogram has two copies of each ORIGINAL adjacent side OA andOC. Compute2(sqrt19+sqrt11) and round only the final perimeter to the explicitly requested1decimal place.')]
add('Exercise-5',6,260,'Parallelogram from adjacent vectors: requested unit diagonal,acute angle between diagonal lines,and1decimal-place perimeter. The key diagonal lacks the required normalisation.',ps,'diagram')

p=proof('a','cos(POQ)=1/7.','Set originalq3 as requested. OP=(−2,3,1),OQ=(2,1,3); dot2 and both norms sqrt14 give cosine2/14=1/7. The generalq has not been permanently fixed for the next part.',261,[DOT,ANGLE]);extra(p,'cosine','((-2)*2+3*1+1*3)/sqrt((4+9+1)*(4+1+9))','Rational(1,7)')
ps=[p,parameter('b-q','FiniteSet(*solve((2-(-2))**2+(1-3)**2+(q-1)**2-6**2,q))','FiniteSet(-3,5)',261,[MAG,DISP],'Resetq. Original PQ=(4,−2,q−1) and length6 give20+(q−1)²=36. Bothq−3and5 satisfy the positive length condition; retain both values.')]
add('Example',17,261,'Show a cosine atq3,then independently solve for bothqvalues makingPQlength6.',ps)
ps=[parameter('a-p','solve((-2)*4+3*1+p,p)[0]','5',618,[PERP],'Original OA=(−2,3,1),OB=(4,1,p) give dotp−5. Zero is necessary and sufficient since neither vector vanishes.'),parameter('b-p','FiniteSet(*solve((4-(-2))**2+(1-3)**2+(p-1)**2-7**2,p))','FiniteSet(-2,4)',618,[MAG,DISP],'Independently resetp. AB=(6,−2,p−1),so40+(p−1)²=49. Bothp−2and4 satisfy the required length7; this is not a perpendicularity continuation.')]
add('Try-Now',17,261,'Given two position columns,choose a parameter for perpendicularity and reset it for prescribed joining-vector length7.',ps)
p=proof('a','BAC=acos(1/3).','Original A=(2,1,3),B=(6,−1,7),C=(2,4,7) give AB=(4,−2,4),AC=(0,3,4). Their dot10 and norms6/5 give cosine1/3. Both rays start at the requested vertexA.',262,[ANGLE]);extra(p,'cosine','(4*0+(-2)*3+4*4)/sqrt((16+4+16)*(0+9+16))','Rational(1,3)')
p2=vector('b-area','sqrt((16+4+16)*(0+9+16)-(4*0+(-2)*3+4*4)**2)/2','10*sqrt(2)',262,[GEOM],'Use the preceding exact cosine1/3 and the positive sine sqrt(1−1/9),with side lengths6and5,in the prior triangle-area formula. Gram determinant independently recomputes the area without a rounded inverse cosine. This area extension does not add another directly assessed between-vector-angle task.')
p2['component_demand_ids']=[MAG,DOT,'8227:PRIOR:NSSCO:mensuration'];extra(p2,'sine-area','Rational(1,2)*6*5*sqrt(1-Rational(1,3)**2)','10*sqrt(2)')
add('Example',18,262,'From three point positions prove the angle has exact cosine1/3,then retain exact sine to obtain area10sqrt2 instead of rounding the angle.',[p,p2])
p=parameter('p','FiniteSet(*solve(4**2*25-(1**2+2**2)*(4**2+p**2),p))','FiniteSet(-8,8)',618,[ANGLE],'Original OA=(1,2,0),OB=(4,0,p) have dot4. The required cosine isPOSITIVE1/5. Squaring givesp²64; both signs retain nonzero norms and the original positive cosine.')
extra(p,'original-cosine','4/sqrt(5*(16+64))','Rational(1,5)')
add('Try-Now-18',1,262,'Find both vertical-component parameters forAOB=acos(1/5),checking the unsquared positive cosine.',[p])
ps=[angle('a-OAB',['-1','-3','-5'],['6','1','-2'],'88.5',618,method='Original O0,A(1,3,5),B(7,4,3). The angleOAB is atA,so useAO=(−1,−3,−5),AB=(6,1,−2). Their dot1 and squared norms35/41 make the angle just below90degrees. Using OA would produce the supplement.'),rounded('b-area','sqrt((1+9+25)*(36+1+4)-((-1)*6+(-3)*1+(-5)*(-2))**2)/2','18.9',618,1,[GEOM],'Use half the product of the exact adjacent lengths and positive sine ofOAB. Recompute by the Gram determinant(35*41−1)/4 under the square root. Source key displays18.9square units; no source precision instruction is inferred from display alone.')]
ps[1]['component_demand_ids']=[MAG,DOT,'8227:PRIOR:NSSCO:mensuration']
add('Try-Now-18',2,262,'Use a scalar product at vertexA,then calculate triangleOABarea from exact side/dot values.',ps)

ps=[parameter('a-p','solve(5*2+1*7+2*p,p)[0]','-Rational(17,2)',618,[PERP],'Original OA=(5,1,2),OB=(2,7,p),so zero dot gives17+2p=0.'),vector('b-vector','Tuple(28*(-3)/7,28*6/7,28*2/7)','Tuple(-12,24,8)',618,[UNIT,DISP],'Part(b)RESETSp4. Then AB=(−3,6,2),norm7. Multiply its positive unit direction by28; this is a length28vector in the SAME direction,not a unit output.')]
add('Revision-Exercise-5',1,263,'Choose perpendicularity parameter,then resetp4and construct the same-directionABvector of magnitude28.',ps)
p=vector('m-n-k','Tuple(solve([4*a+3*b-1,a+2*b-4],[a,b],dict=True)[0][a],solve([4*a+3*b-1,a+2*b-4],[a,b],dict=True)[0][b],-2*(-2)-4*3)','Tuple(-2,3,-8)',618,[GEOM,POS],'Original OA=(4,1,−2),OB=(3,2,−4),OD=(1,4,k)=mOA+nOB. Solve the first two component equations for m,n,then substitute both into the third to obtaink. All three must hold simultaneously.')
extra(p,'all-original-components','Tuple(4*(-2)+3*3,(-2)+2*3,(-2)*(-2)+3*(-4))','Tuple(1,4,-8)')
add('Revision-Exercise-5',2,263,'Resolve OD=mOA+nOB in3components with an unknown third coordinate; find the correlated triplem−2,n3,k−8.',[p])
p=vector('OD','Tuple(2+10-4,3+0-2,5+6-3)','Tuple(8,1,8)',618,[POS,GEOM],'ABCD is a parallelogram in that cyclic order. Thus D=A+C−B,notA+B−C. Use ORIGINAL A(2,3,5),B(4,2,3),C(10,0,6).')
add('Revision-Exercise-5',3,263,'Recover fourth vertexDfrom cyclic parallelogramABCD using A+C−B.',[p])
ps=[vector('a-PR','Tuple(4-2,2-0,2-0)','Tuple(2,2,2)',618,[DISP],'Original side4cube axesOA,OC,OD give midpointP=(2,0,0),face-centreR=(4,2,2). SubtractPfromR.'),vector('a-PQ','Tuple(0-2,2-0,4-0)','Tuple(-2,2,4)',618,[DISP],'Q is midpointDG with D(0,0,4),G(0,4,4),soQ=(0,2,4). Preserve PtoQ.'),angle('b-QPR',['-2','2','4'],['2','2','2'],'61.9',618),rounded('c-perimeter','sqrt(12)+sqrt(24)+sqrt(20)','12.8',618,1,[GEOM,MAG],'Original midpoint/face-centre triangle hasPRsqrt12,PQsqrt24,QRsqrt20. Add all three positive lengths,then round the final perimeter to the explicit1decimal place.')]
add('Revision-Exercise-5',4,264,'Side4cube with two edge midpoints and a face centre: derivePR/PQ,angleQPR,and1decimal-place triangle perimeter.',ps,'diagram')
p=vector('angle-OBF','acos(((-8)*(-4)+(-6)*(-4)+0*7)/(10*9))','acos(Rational(28,45))',618,[ANGLE],'Original B=(8,6,0),topF=(4,2,7),O0. Both BO=(−8,−6,0) andBF=(−4,−4,7) start atB; dot56,norms10and9 give exactacos(28/45). The source requests inverse-cosine rational form,so a rounded decimal alone is insufficient.')
p['component_demand_ids']=[DISP,DOT,MAG];p['source_answer_requirement']='cos^-1(a/b),a,b integers'
add('Revision-Exercise-5',5,264,'Two horizontal rectangles with vertical height7: use the actual vertexB and return OBF in exact inverse-cosine rational form.',[p],'diagram')

refs=[
 (62,260,'Exercise5Q4 horizontal pyramid section','O0,A(10,0,0),B(10,10,0),C(0,10,0),P(0,0,10). Horizontal side6section atheight4 hasG(0,6,4).',[GEOM,DISP,ANGLE],'diagram','Exercise-5:4'),
 (63,260,'Exercise5Q6 parallelogram and diagonals','OA=(1,3,3),OC=(3,−1,1),OB=(4,2,4),AC=(2,−4,−2). Adjacent sides determine perimeter; acute angle between lines requires choosing the acute supplement.',[GEOM,UNIT,ANGLE],'diagram','Exercise-5:6'),
 (64,262,'Example18 exact triangle area formula','Area=(1/2)ab sinC uses positive lengths and the included interior angle. WithcosC1/3,positive sinCsqrt8/3. Preserve exact radicals rather than rounded inverse cosine.',[GEOM],'table','Example:18'),
 (65,264,'Revision5Q4 cube and internal triangle','Side4cube O0,A(4,0,0),C(0,4,0),D(0,0,4). P(2,0,0),Q(0,2,4),R(4,2,2); shaded triangle isPQR.',[GEOM,DISP,ANGLE],'diagram','Revision-Exercise-5:4'),
 (66,264,'Revision5Q5 unequal rectangular levels','Base8by6,top4by2,height7; DverticallyaboveO andDEparallelOA. Thus F(4,2,7),B(8,6,0). Top sides are not centred offsets invented from perspective.',[DISP,ANGLE],'diagram','Revision-Exercise-5:5'),
 (67,265,'Vector magnitude summary','For orthogonal3Dcomponents,positive normsqrt(x²+y²+z²). Zero has magnitude0,but no normalised direction.',[MAG],'table',None),
 (68,265,'Unit vector summary','Divide every component of a NONZERO vector by its positive norm. A sign change in only one component can preserve length while destroying parallelism.',[UNIT],'table',None),
 (69,265,'Displacement and Cartesian components summary','AB=OB−OA andOQ=xi+yj+zk. The source3Daxes and pointQ(x,y,z)fix coordinate order; scalar coefficients are not separate vectors.',[POS,DISP],'diagram',None),
 (70,265,'Scalar product and angle summary','Component dot equals product of norms timescosθ. Perpendicularity converse and division to find cosθ require nonzero vectors. Preserve signed dot for the non-reflex angle; diagonal-line acute angles are an explicit different answer requirement.',[DOT,ANGLE,PERP],'table',None)]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1]
 r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C5:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C5:')if r['parent_item_id']else None
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if n in[62,63,65,66]else'teaching-figure')
 r['mathematical_feature_review']['method']='Read actual labels,axis orientations,midpoints and horizontal section constraints; reconstruct coordinates and exact algebra. Source summary formulas are checked with their nonzero/positive-length conditions,not treated as separately asked learner tasks.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=5,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All remainingExercise5Q4–6,Examples17/18,Try17/18,Revision5Q1–5 and summary panels are individually recorded. Revision tariffs3+4+4+2+3+4+4+6=30. Summary recurrence is a source occurrence,not extra problem-type breadth.',scope_screen='Elementary3Dvector geometry only. Triangle area is a prior-knowledge extension and does not create extra vector-angle coverage. Acute diagonal-line angle is distinguished from ordinary directed-vector angle; exact inverse-cosine output is retained.')for page in range(260,266)]
if __name__=='__main__':
 for name,data in [('answers-YM-C5-closing.json',dict(scope='All260–265explicit responses.',items=answers)),('census-YM-C5-closing.json',dict(book='YM',book_id='8227-SRC-017',chapter=5,source_path=SRC,source_sha256=SHA,scope='Complete260–265page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
