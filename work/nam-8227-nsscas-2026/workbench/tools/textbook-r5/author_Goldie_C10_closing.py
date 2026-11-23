"""Read280–293at part level; preserve useful geometry within additional representations."""
import hashlib,json
import author_Goldie_C10_line_opening as opening
from author_Goldie_C10_line_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent,ADD,GEOM,DISP,POS,MAG,SCALE
from author_Goldie_C10_dot_opening import angle,dot,ANGLE,DOT,PERP

base=opening.base
base.answers.clear();base.new.clear();figures.clear()
answers=base.answers;new=base.new

def ev(page):
    if page in[292,293]:name='Goldie-C10-end-C11-start-source'
    else:return opening.ev(page)
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
base.ev=ev

def add(*args,**kwargs):
    row=opening.add(*args,**kwargs)
    row['mapping_rationale']='Map the retained original output,not the chapter heading. Ordinary2Dintersection can use prescribed Cartesian methods when no vector method is forced. Supplied position combinations support vector arithmetic/geometry;formal line construction,skew classification and projection methods remain explicitly separate.'
    row['precision_angle_check']={'source':'Numeric source angles are in degrees.10F3key uses2decimal places;other angle keys use1decimal place.10E3distance uses3significant figures;its constant speeds and collision time are exact.',
      'comparison':'Keep exact quantities until the individual final display comparison. An acute angle between unoriented lines may require the supplement of a directed-vector angle;retain both source directions and the source goal. A common time parameter for two moving objects cannot be replaced with two unrelated path parameters.'}
    new[-1]['mapping_rationale']=row['mapping_rationale']
    return row

INTERSECT='8227:2020:M1:T4:O02:D01';LINE='8227:2020:M1:T4:O01:D01';RATE='8227:2020:M1:T8:O03:D03'

p=v('intersection','Tuple(solve(Eq(8-2*x,(x+1)/2),x)[0],(solve(Eq(8-2*x,(x+1)/2),x)[0]+1)/2)','Tuple(3,2)',281,
 'The original asks the intersection of the2Dlines throughA(1,6),B(4,0)andC(1,1),D(5,3),without forcing a vector method. DeriveAB:y=8−2xandCD:y=(x+1)/2from the actual endpoints,then solve the two Cartesian equations. The source’s vector-parameter solution is an additional alternative,not a requirement of this original task.')
p['additional_operations']={'original_AB_endpoints':{'kind':'identity','operands':['Tuple(6-(8-2*1),0-(8-2*4))']},'original_CD_endpoints':{'kind':'identity','operands':['Tuple(1-(1+1)/2,3-(5+1)/2)']}}
p['additional_operation_expected']={'original_AB_endpoints':'Tuple(0,0)','original_CD_endpoints':'Tuple(0,0)'}
row=add('Example',14,280,'Find the intersection of the2Dlines joiningA(1,6)toB(4,0),andC(1,1)toD(5,3). A prescribed Cartesian alternative gives(3,2);the source illustrates vector parameters.',[p],[INTERSECT],[LINE],rep='graph',continuation=[281])
row['direct_demand_aspects']=[{'demand_id':INTERSECT,'assessed_facet':'The line-line intersection case only;not fullcurve/line or tangency coverage.'}]

p=v('i-initial-separation','sqrt((10-0)**2+(8-0)**2)','12.8',359,
 'At the sharedt=0,the cargo vessel is at(0,0)andthe fishing boat at(10,8)km. Their separation is√164km,displayed12.8to3significant figures in the key.')
p['operation']={'kind':'rounded','operands':['sqrt((10-0)**2+(8-0)**2)'],'significant_figures':3};p['source_vector_components']=['10','8'];p['source_vector_output']='magnitude';p['answer_unit']='km'
parts=[p]
for label,components,key in [('cargo',['12','16'],'20'),('fishing',['-3','4'],'5')]:
    p=v('ii-speed-'+label,'sqrt('+'+'.join(f'({z})**2'for z in components)+')',key,359,
      'The supplied position components are linear in the shared time in hours. Their constant velocity components are the coefficients of t;speed is the nonnegative Euclidean magnitude,not a signed coordinate rate. The basis vectors each represent1km.');p['source_vector_components']=components;p['source_vector_output']='magnitude';p['answer_unit']='km/h';parts.append(p)
p=reasoning('iii-shared-time-collision','They collide after40minutes(at t=2/3hours),at(8,32/3)km.',
 'Equate the east components12t=10−3t,givingt=2/3. Check the north components at that same time:16t=8+4t=32/3. Both objects occupy exactly the same position at the same nonnegative time. This is stronger than geometric path intersection with independent parameters;the source key expressly says collision after40minutes.',359,'matches')
p['additional_operations']={'east_time':{'kind':'identity','operands':['solve(Eq(12*t,10-3*t),t)[0]']},'north_time':{'kind':'identity','operands':['solve(Eq(16*t,8+4*t),t)[0]']},'common_point':{'kind':'identity','operands':['Tuple(12*Rational(2,3),16*Rational(2,3))']}}
p['additional_operation_expected']={'east_time':'Rational(2,3)','north_time':'Rational(2,3)','common_point':'Tuple(8,Rational(32,3))'};parts.append(p)
row=add('Exercise-10E',3,284,'Given cargo positionr₁=(12t,16t)andfishing positionr₂=(10−3t,8+4t),withshared time in hours andkilometre E/Nbasis,find initial separation,speeds,andwhat happens. Preserve simultaneous motion rather than unconstrained path crossing.',parts,[MAG,GEOM],[POS,ADD,RATE])
row['direct_demand_aspects']=[{'demand_id':MAG,'assessed_facet':'Initial distance and scalar speeds from supplied vector positions/constant velocity components.'},{'demand_id':GEOM,'assessed_facet':'Same-time equality of the supplied positions;not construction/classification of arbitrary vector line equations.'}]

parts=[]
for label,p1,p2,key in [('L',[7,2],[13,7],'Tuple(10,Rational(9,2))'),('M',[13,7],[1,0],'Tuple(7,Rational(7,2))'),('N',[1,0],[7,2],'Tuple(4,1)')]:
    parts.append(v('i-'+label,'Tuple('+','.join(f'(({a})+({b}))/2'for a,b in zip(p1,p2))+')',key,359,'Average the actual endpoint coordinates of the specified side. LabelsL,M,Nrefer respectively toBC,CA,AB;do not permute the sides.'))
parts.append(v('iii-a-AL-BM','Tuple(7,(7-1)/2)','Tuple(7,3)',359,
 'Use the retained midpointL=(10,9/2):lineALhas slope1/2and equationy=(x−1)/2. B=(7,2),M=(7,7/2)give the vertical linex=7. Their Cartesian intersection is(7,3). Part(ii)requests vector equations,but(iii)doesnot force their use.'))
parts.append(v('iii-b-BM-CN','Tuple(7,Rational(2,3)*7-Rational(5,3))','Tuple(7,3)',359,
 'C=(13,7),N=(4,1)give slope2/3and equationy=2x/3−5/3. Intersect withBM:x=7toobtain(7,3). Check the derived equations against both original endpoints.'))
parts.append(reasoning('iv-concurrence','The three mediansAL,BM,CNare concurrent at(7,3).',
 'Both computed intersections lie on the same vertical medianBMandare identical,so allthree lines share this point. The source additionally says the result holds for alltriangles;one numerical triangle alone is evidence of this instance,not a proof of the general theorem.',359,'matches'))
row=add('Exercise-10E',4,285,'FortriangleA(1,0),B(7,2),C(13,7),retain three midpoint vectors,the two median intersections,andthe instance-level concurrence observation. Prescribed Cartesian equations are valid for the intersection goals.',parts,[POS,INTERSECT,GEOM],[LINE,ADD],
 excluded=['Part(ii)explicitly asks vector equations ofAL,BM,CNandremains additional representation. The unforced intersection goals are retained via ordinary Cartesian alternatives.'])
row['direct_demand_aspects']=[{'demand_id':INTERSECT,'assessed_facet':'The two specified line-line intersections;not all graph-intersection structures.'}]

p=dot('direction-perpendicularity',['-9','-2','4'],['2','-3','3'],'0',286,
 'The explicitly supplied directions are(−9,−2,4)and(2,−3,3);both nonzero,andtheir scalar product is−18+6+12=0. The given line basepoint is the same(1,2,3),so the lines also meet. This records the prescribed perpendicular-vector facet separately from the additional vector-line notation.');p['check_mode']='show/prove'
add('Example',16,286,'Verify perpendicularity for two supplied lines sharing(1,2,3),using their given direction vectors. The scalar-product result is retained;formal line-equation fluency is additional.',[p],[],[DOT],
 excluded=['Original givens are formal vector equations of lines,an additional representation. The numerical perpendicularity is supporting evidence forM1:T7:O05:D02,not standalone full-scope original practice.'])['teaches_8227_demand_ids']=[PERP]
p=angle('direction-angle',['2','-1','-1'],['3','0','1'],'49.8',287,
 method='Read the two given direction triples from the source. Their dot is5andnorms√6,√10,so the acute angle isacos(5/√60)≈49.8°. Locations/skew classification do not enter this angle calculation;the original formal line representation remains additional.')
add('Example',17,287,'Calculate the angle between two supplied skew lines. Retain the scalar-product calculation between the given directions as supporting angle evidence;do not claim skew-line representation as prescribed.',[p],[],[DOT,MAG],
 excluded=['Vector-line-equation/skew-line representation is additional;the provided direction-pair calculation supports the prescribed scalar-product angle demand.'])['teaches_8227_demand_ids']=[ANGLE]

for n,u,w,key,dp in [(1,['1','4','0'],['2','1','1'],'53.6',1),(2,['4','1','4'],['1','2','-1'],'81.8',1),(3,['3','7','-4'],['2','8','-5'],'8.72',2),(4,['1','1','-1'],['1','0','-1'],'35.3',1),(5,['2','3','2'],['0','0','1'],'61.0',1)]:
    p=angle('given-direction-angle',u,w,key,359,dp=dp,
      method='Extract the explicit parameter coefficient direction from each supplied source equation,then independently apply the dot/norm angle formula. Both directions are nonzero. For this source pair the dot ispositive,so the between-vector angle is already the acute line angle. Source locations are not needed. Original formal vector-line notation remains additional.')
    row=add('Exercise-10F',n,289,f'10F{n}:find the angle between the two supplied vector lines. Retain the actual given direction pair{u},{w}andits scalar-product calculation as supporting practice;the formal representation is additional.',[p],[],[DOT,MAG],
      excluded=['Source vector-line-equation representation is additional;this item supports the direction-pair calculation only anddoesnot establish directly assessed8227coverage.'])
    row['teaches_8227_demand_ids']=[ANGLE]

parts=[reasoning('i-A-F','A=(4,0,0),F=(4,0,3).',
 'The base and walls are rectangular. GivenO=(0,0,0),B=(4,5,0),E=(0,0,3),G=(4,5,3)fix the lower front-right vertexAandits vertical roof-edge pointF. The ridge is higher atP(2,1,4),butFremains at wallheight3.',359,'matches')]
parts.append(angle('ii-FPQ',['2','-1','-1'],['0','4','0'],'114.1',359,
 method='The vertex isP=(2,1,4). PF=F−P=(2,−1,−1),PQ=Q−P=(0,4,0),withQ=(2,5,4). Their negative dot−4gives the obtuse angle114.1°. Do not return the acute supplement.'))
parts.append(angle('ii-EPF',['-2','-1','-1'],['2','-1','-1'],'109.5',359,
 method='The vertex isagainP. PE=E−P=(−2,−1,−1),PF=(2,−1,−1),withdot−2andboth norms√6. The angle isacos(−1/3)≈109.5°.'))
p=reasoning('iii-touch-and-perpendicular','The two streamers touch at(2,5/2,3/2),but they are not perpendicular.',
 'Rectangular walls giveH=(0,5,3). The midpoints ofOGandAHare both(2,5/2,3/2),andboth streamers are the full straight segments,so they touch. Their direction vectors areOG=(4,5,3),AH=(−4,5,3),withscalar product18≠0. Therefore the owner’s combined claim is false:the touch statement is true,the perpendicular statement false. No vector-line-equation construction is needed.',359,'matches')
p['additional_operations']={'common_midpoints':{'kind':'identity','operands':['Tuple((0+4)/2,(0+5)/2,(0+3)/2,(4+0)/2,(0+5)/2,(0+3)/2)']},'dot_original_streamers':{'kind':'identity','operands':['(4-0)*(0-4)+(5-0)*(5-0)+(3-0)*(3-0)']}}
p['additional_operation_expected']={'common_midpoints':'Tuple(2,Rational(5,2),Rational(3,2),2,Rational(5,2),Rational(3,2))','dot_original_streamers':'18'};parts.append(p)
add('Exercise-10F',9,290,'Read the house-extension coordinate diagram,locateAandF,find two roof angles atPusing vectors,andassess the combined streamer touch/perpendicularity claim. A shared midpoint proves touching without extra formal line methods.',parts,['8227:2020:M1:T7:O01:D01',ANGLE,PERP,GEOM],[DOT,MAG,DISP],rep='diagram')

p=reasoning('ii-angle-quadratic','The angle condition implies3t²+7t+2=0.',
 'A=(1,2,3),B=(2,1,3),soAB=(1,−1,0). The suppliedP(t)givesAP=(−2t,3+t,−1−t),withdotAP·AB=−3t−3and|AP|²=6t²+8t+10. Fromcos60°=1/2,2(−3t−3)=√2√(6t²+8t+10). Squaring and simplifying gives8(3t²+7t+2)=0. The unsquared positive-right-side condition additionally requirest<−1.',291,'show/prove')
p['additional_operations']={'squared_condition':{'kind':'identity','operands':['expand(4*(-3*t-3)**2-2*((-2*t)**2+(3+t)**2+(-1-t)**2))']}}
p['additional_operation_expected']={'squared_condition':'8*(3*t**2+7*t+2)'}
p2=reasoning('ii-only-position','Onlyt=−2is valid,soOP=5i+3j+4k.',
 'Factor the derived quadratic:(3t+1)(t+2)=0gives−1/3and−2. The original60°condition needs positiveAP·AB,so−1/3(withnegative dot)would give120°andisextraneous. Att=−2,P=(5,3,4),AP=(4,1,1);dot3andnorm√18givecos=3/(√18√2)=1/2. The rejected parameter would giveP=(5/3,14/3,7/3).',359,'matches')
p2['additional_operations']={'candidate_roots':{'kind':'identity','operands':['FiniteSet(*solve(3*t**2+7*t+2,t))']},'valid_point':{'kind':'identity','operands':['Tuple(1-2*(-2),5+(-2),2-(-2))']},'valid_cosine':{'kind':'identity','operands':['3/(sqrt(4**2+1**2+1**2)*sqrt(1**2+(-1)**2))']},'rejected_cosine':{'kind':'identity','operands':['(-3*(-Rational(1,3))-3)/(sqrt(6*(-Rational(1,3))**2+8*(-Rational(1,3))+10)*sqrt(2))']}}
p2['additional_operation_expected']={'candidate_roots':'FiniteSet(-2,-Rational(1,3))','valid_point':'Tuple(5,3,4)','valid_cosine':'Rational(1,2)','rejected_cosine':'-Rational(1,2)'}
row=add('Exercise-10F',10,291,'Retain(ii):from the explicitly givenP(t)andA/Bpositions,use∠PAB=60°toestablish the quadratic andselect the only valid position vector. Preserve the unsquared sign condition;do not accept both polynomial roots.',[p,p2],[ANGLE],[DOT,MAG,DISP],
 excluded=['Part(i)asks a skew/nonintersection proof for vector lines andremains additional. The independently suppliedP(t)in(ii)allows its vector-angle constraint without requiring that proof.'])
row['exam_style']=True;row['exam_style_basis']='The textbook prints Cambridge9709Paper3Q10June2008. Only the explicitly retained part(ii)is mapped;primary examination source not re-read in this textbook pass.'

p=v('i-position-identity','Tuple(1+q*(3-1),2+q*(4-2),2+q*(0-2))','Tuple(1+2*q,2+2*q,2-2*q)',291,
 'The source suppliesAP=λAB. ComputeAB=(2,2,−2)fromA=(1,2,2),B=(3,4,0),thenaddOA. This is ordinary vector addition/scaling,not a request to invent a line equation.');p['check_mode']='show/prove'
p2=v('ii-bisector-multiplier','solve(Eq(5*(1*(1+2*q)+2*(2+2*q)+2*(2-2*q)),3*(3*(1+2*q)+4*(2+2*q))),q)[0]','Rational(3,8)',359,
 'Independently compute|OA|=3,|OB|=5. Equality of the requested cosines is(a·p)/(3|p|)=(b·p)/(5|p|);pneverzero becauseAandBare independent. Cancel the positive commonnormandcross-multiply5a·p=3b·p,giving45+10λ=33+42λandλ=3/8. Cosine is one-to-one for the0..πbetween-ray angles,so equal cosines give the intended internal bisector.')
p3=reasoning('iii-ratio-verification','AP:PB=3:5=OA:OB.',
 'Withλ=3/8,Pis strictly betweenAandB. Thus|AP|=(3/8)|AB|and|PB|=(5/8)|AB|,giving3:5. Independently|OA|=√(1+4+4)=3and|OB|=√(9+16)=5. The original directed relation and positive internal coefficients justify using these length ratios.',291,'show/prove')
p3['additional_operations']={'point_at_bisector':{'kind':'identity','operands':['Tuple(1+2*Rational(3,8),2+2*Rational(3,8),2-2*Rational(3,8))']},'original_origin_norms':{'kind':'identity','operands':['Tuple(sqrt(1**2+2**2+2**2),sqrt(3**2+4**2+0**2))']}}
p3['additional_operation_expected']={'point_at_bisector':'Tuple(Rational(7,4),Rational(11,4),Rational(5,4))','original_origin_norms':'Tuple(3,5)'}
row=add('Exercise-10F',11,291,'ForA=(1,2,2),B=(3,4,0)andthe suppliedAP=λAB,establishOP,equate two scalar-product cosine expressions to locate the internal bisector,andverify the two length ratios. Allthree original parts use prescribed vector operations.',[p,p2,p3],[POS,ANGLE,GEOM],[ADD,SCALE,DOT,MAG])
row['exam_style']=True;row['exam_style_basis']='The textbook prints Cambridge9709Paper31Q7November2011. This is textbook-attributed evidence;the primary paper was not read here.'
p=angle('ii-x-axis-direction',['1','2','5'],['1','0','0'],'79.5',359,
 method='The original(ii)explicitly asks the acute angle of the supplied line direction(1,2,5)to the xaxis(1,0,0). Their dot is1andnorms√30,1,soθ=acos(1/√30)≈79.5°. Source line locations andpart(i)skew proof are unnecessary for this direction-only result.')
row=add('Exercise-10F',13,291,'Retain(ii):the acute angle between the given direction ofl₂andthexaxis. Its direction is explicitly supplied in the source equation;the earlier skew-line proof is additional.',[p],[ANGLE],[DOT,MAG],
 excluded=['Part(i)asks a skew-line proof,additional. The given direction-pair facet in(ii)is retained;it doesnot establish general vector-line-equation fluency.'])
row['exam_style']=True;row['exam_style_basis']='The textbook prints Cambridge9709Paper31Q6June2015. Only(ii)is retained;primary source was not read in this pass.'

for n,page,label,note,teaches,rep,checks,parent in [
 (53,280,'Figure10.24 two Cartesian lines','A(1,6),B(4,0)lieony=8−2x;C(1,1),D(5,3)lieony=(x+1)/2. The common point is(3,2). The original task permits this Cartesian route even though the worked source chooses vector parameters.',[LINE,INTERSECT],'graph',[('Tuple(8-2*3,(3+1)/2)','Tuple(2,2)')],'Example:14'),
 (54,282,'Negative-direction parallel-line caution','Source directions(−3,2,1)and(6,−4,−2)are opposite directed vectors with scalar−2,butparallelunorientedlines. Different source basepoints alone wouldnot prove distinct lines;here their difference(0,5,−3)isnot a multiple of the direction,so the stated distinct-parallel conclusion is true.',[SCALE,GEOM],'table',[('Tuple(6,-4,-2)','Tuple(-2*(-3),-2*2,-2*1)')],None),
 (55,285,'Tree-guy illustration','Two straight supports join(2,0,3)to(−1,2,6)and(0,3,5)to(−2,−2,4). The2Dpicture crossing doesnot prove a3Dintersection. The original meeting test is additional line-intersection method evidence;the picture supplies contextual spatial interpretation only.',[],'diagram',[],None),
 (56,286,'Figure10.25 common-tail angle and dot formula','The two direction arrows must have a common tail to readθ. Dot-product angle requires nonzero vectors;the reference formula alone is not an assessed new task.',[ANGLE,DOT],'diagram',[],None),
 (57,287,'Figure10.26 translated skew-line angle','The line m is translated to m′to compare directions withl. Translation preserves its direction. Distinguish directed-vectorθfrom the chosen acute/unoriented line angle. Skew-line geometry remains additional representation.',[ANGLE],'diagram',[],None),
 (58,288,'Figure10.27 perpendicular-foot construction','NliesonthelineandPNis perpendicular;the right-angle mark distinguishes a true shortest distance from an arbitrary joining distance. Construction ofNfrom a formal vector line is additional source method,not claimed as prescribed direct coverage.',[PERP,MAG],'diagram',[],None),
 (59,288,'Projection scalar-product callouts','For the supplied direction(−3,1,4),the original extra projection method setsNP·direction=0. This supports the perpendicularity meaning of dot zero;it doesnot by itself certify a prescribed general projection/point-line-distance recipe.',[PERP,DOT],'table',[],None),
 (60,290,'10F9 house-extension coordinates','Rectangular base/walls giveO(0,0,0),A(4,0,0),B(4,5,0),E(0,0,3),F(4,0,3),G(4,5,3),H(0,5,3). Roof ridge endpointsP(2,1,4),Q(2,5,4)fix the two angles atP. StreamersOGandAHshare a midpoint buttheir dot product18isnonzero.',['8227:2020:M1:T7:O01:D01',ANGLE,PERP],'diagram',[],'Exercise-10F:9'),
 (61,292,'Chapter10 prescribed vector summary','Definitions/notations,origin-based position,joining vectorb−a,unitnormalisation,scalar multiplication,addition,positive magnitudes andnonzero-vector dot/angle formulas are useful reference support. Items12–15andthe line/skew learning outcomes extend to formal vector equations andarenot automatically8227requirements.',[POS,DISP,MAG,DOT,ANGLE,SCALE,ADD],'table',[],None)]:
    fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
    f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:')if f['parent_item_id']else None
    f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]

notes={280:'Example13is formal vector-line intersection,additional. Example14andFigure10.24retain a2Dunforced intersection goal via an ordinary Cartesian alternative.',
 281:'Example14worked vector solution/alternative parameter note continues;the same point(3,2)is independently checked with prescribed Cartesian equations.',
 282:'Example15classifiesparallel/skewformalvectorlines,additional. Its negative-scalar wording is retained as supporting caution withoutclaiming the true final parallel conclusion iswrong.',
 283:'Example15continueswith an altered-basepoint intersection note;10E1(i–v)asksintersectionsfromformalvectorlines,additional. No retained original task starts.',
 284:'10E2(i–vii)formal3Dlineclassificationisadditional.10E3suppliedtime-positionfunctionsallowdirect magnitude/same-time geometry facets,allretained.',
 285:'10E4midpoints,unforcedCartesianintersectionsandinstanceconcurrence retained;its explicitly requested vector equations remain extra.10E5and7dependonformal3Dlineintersectionsandremainadditional.10E6tree-guy meeting problem is additional line-intersection evidence;its diagram is separately recorded.',
 286:'Figure10.25andExample16given-direction perpendicularity facet retained as supporting evidence;formal vector-line notation stays additional.',
 287:'Figure10.26andExample17given-direction angle facet retained as supporting evidence. The10.8point-line-distance introduction is an additional projection-method boundary.',
 288:'Example18andits continuation289construct a perpendicular foot on a formal vector line;additional method. Figure10.27andtwo dot/perpendicularity callouts retained separately as supporting figures,not assessed projection coverage.',
 289:'Example18continues;10F1–5direction-pair calculations retained as supporting evidence with exact source directions/rounding.10F6(i)starts formal projection task;it andthe(ii)/(iii)continuationon290are additional.',
 290:'10F6(ii)/(iii),7and8require point-line projections,andremainadditional.10F9allparts retained via coordinate/dot/midpoint geometry;the original house diagram has its own record.',
 291:'10F10(i)skewproofextra;(ii)explicitly suppliedP(t)angle constraint retained with both squared roots andoriginal-angle rejection.10F11allthree ordinary vector/bisector/ratioparts retained.10F12intersection-for-all-parameter question remainsadditional;itsnormconstraintdependsontheextra intersection.10F13(i)skewproofextra;(ii)supplieddirection/xaxisangle retained.',
 292:'Chapter keypoints1–11andprescribedvectorfacets retained as one reference block.12–14line-equation statements additional;thereisno new assessedtask.',
 293:'Keypoint15andline/skewlearningoutcomesareadditional. Otherlearningoutcomesrestatepreviousprescribedvectors;linkedtosummary61on292. No independently asked task ornewgivenfigure starts.'}
pages=[]
for page in range(280,294):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    continuation=['8227:TB:Goldie:C10:Example:14']if page==281 else['8227:TB:Goldie:C10:Teaching-figure:61']if page==293 else[]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated'if ids else'scope-screened; no in-scope item starts','item_ids':ids,'continuation_item_ids':continuation,
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],
      'scope_screen':'Original tasks screened by required output/method,not a blanket chapter exclusion. Supplied-direction calculations in formal-line originals are supporting;independently ordinary vector/Cartesian outputs carry direct facets. Author scope judgement awaits independent acceptance.'})
next(f for f in figures if f['item_number']=='61')['continuation_pdf_pages']=[293]

if __name__=='__main__':
    for name,data in [('answers-Goldie-C10-closing.json',{'scope':'Every retained280–293original response andsupportingdirectioncalculation;extra3Dline/projectionmethodsremainexplicit.','items':answers}),
      ('census-Goldie-C10-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete280–293renderedpage/partscopeauditwithallretainedfigures.','new_items':new+figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for r in answers:
        for p in r['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
