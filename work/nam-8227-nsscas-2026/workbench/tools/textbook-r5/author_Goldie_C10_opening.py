"""Rendered vector opening248–254. Fixed-source evidence,not runtime assets."""
import json,hashlib
import author_Goldie_C8_opening as base
from author_Goldie_C8_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
NOTATION='8227:2020:M1:T7:O01:D02';MAG='8227:2020:M1:T7:O04:D01';ANGLE='8227:2020:M1:T7:O05:D01'
POS='8227:2020:M1:T7:O03:D03';DISP='8227:2020:M1:T7:O03:D02';GEOM='8227:2020:M1:T7:O02:D03';ADD='8227:2020:M1:T7:O02:D01';UNIT='8227:2020:M1:T7:O03:D01'
def ev(page):
 name='Goldie-C10-keys-357-source'if page in[357,358,359,360]else'Goldie-C9-end-keys-source'if page in[355,356]else f'Goldie-C10-{248+4*((page-248)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
base.ev=ev;base.answers.clear();base.new.clear();answers=base.answers;new=base.new;figures.clear();corrections=[]
def add(*args,**kwargs):
 row=base.add(*args,**kwargs);row['item_id']=row['item_id'].replace(':C8:',':C10:')
 # All opening task IDs already exist in the R4inventory. Only newly censused
 # figures are new population. Preserve the old IDs and correct continuations.
 generated=base.new.pop();corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':generated['continuation_pdf_pages']})
 row['mapping_rationale']='Read an arrow/coordinate pair before computing its displacement. Magnitude,direction,position,notation and geometric conclusions are separate requested outputs;an incidental subtraction is a component unless it is the actual task.'
 row['value_level_scope_decisions']=[]
 row['scope_check'].update(limits_considered=[],qualifier_applicability_note='None of QUAL01–11orLIMIT01–08governs these fixed vector tasks. Apply the actualM1:T7objective,angle-method,dimension,nonzero-direction and source-precision boundaries instead.')
 row['precision_angle_check']={'source':'Example10.1rounds magnitude and angle to3significant figures;Example10.3explicitly rounds magnitude to2decimal places. Exercise10A2key keeps exact magnitudes and angles to1decimal place;10A3key uses3significant figures.','comparison':'Angles here are degrees anticlockwise from the positivexaxis,with negative principal directions allowed;they are not clockwise bearings from north. Equivalent directions may differ by360°. Original task precision must remain visible when comparing NSSCAS conventions.'}
 return row
def v(label,expr,key,page,method):return value(label,expr,key,page,method)
def magnitude(label,components,key,page,dp=None,sf=None):
 expr='sqrt('+ '+'.join(f'({c})**2'for c in components)+')'
 p=v(label,expr,key,page,'Compute the Euclidean norm from the original signed components;negative components are squared before summation. Keep the exact radical internally and apply only the specifically recorded source rounding.')
 if dp is not None or sf is not None:
  op={'kind':'rounded','operands':[expr]}
  if dp is not None:op['decimal_places']=dp
  if sf is not None:op['significant_figures']=sf
  p['operation']=op
 p['source_vector_components']=components;p['source_vector_output']='magnitude';return p
def direction(label,components,key,page,dp=1,sf=None):
 a,b=components;expr=f'180*atan2({b},{a})/pi'
 p=v(label,expr,key,page,'Use both component signs to determine the quadrant,then convert the principalatan2angle to degrees. A plain arctangent ofb/acould lose180°. The vector must be nonzero;zero has no unique direction.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})}
 p['source_vector_components']=components;p['source_vector_output']='direction-degrees';return p

p=reasoning('information','For each trail,need3Dposition information defining its straight path;for aircraft closest approach also need contemporaneous positions/timestamps and velocities.',
 'Two points,or one point and a direction,define a straight path in three dimensions. Closest separation of the two geometric trails is different from the closest simultaneous aircraft positions. The source key explicitly adds time and speed for the latter under constant speeds/directions. This is contextual specification support,not a requirement to author vector line equations or skew-line distance methods for8227.',355,'matches')
add('Prompt',1,248,'Ask what information is needed to decide how closely the aircraft behind two photographed trails passed. Separate geometric trail separation from simultaneous aircraft motion,and note the constant-velocity assumptions.',[p],teaches=[NOTATION],rep='diagram')
add('Example',1,250,'Find magnitude and direction of4i+2j. The printed solution gives4.47and26.6°to3significant figures;the angle is anticlockwise from+x,not a north bearing.',[
 magnitude('magnitude',['4','2'],'4.47',250,sf=3),direction('direction',['4','2'],'26.6',250,sf=3)],[MAG],teaches=[ANGLE])
p=v('i-position','Tuple(4,3)','Tuple(4,3)',252,'The position vector ofL=(4,3)is the origin-to-Lvector(4,3);unlike a free vector,it has the specified origin as its tail.')
p2=v('i-displacement','Tuple(2-(-2),2-(-1))','Tuple(4,3)',252,'ReadM=(−2,−1),N=(2,2),then subtracthead−tailto obtainMN=(4,3). Preserve the orderMN;reversing it changes the signs.')
p3=reasoning('ii-geometric-relation','OLandMNare parallel segments of equal length,with the same directed vector.',
 'Both directed vectors equal(4,3),so their magnitudes and directions coincide even though their starting points differ. A vector equality does not identify the pointsLorNwith one another. The source uses lines informally here;the equal finite quantities are the segments.',252,'matches')
add('Example',2,252,'ForL(4,3),M(−2,−1),N(2,2),giveOLandMNin component form and interpret their equality geometrically. The coordinate grid is a given representation,not a requested sketch.',[p,p2,p3],[POS,DISP,GEOM],[ADD],rep='graph')
p=reasoning('three-dimensional-length','For mutually perpendicular coordinate componentsa₁,a₂,a₃,the length is√(a₁²+a₂²+a₃²).',
 'First project to the coordinate plane,where the projected length is√(a₁²+a₂²). Apply Pythagoras again with the perpendicular third component:|a|²=(a₁²+a₂²)+a₃². Length is the nonnegative square root. The source key draws these two right triangles. This derivation is supporting magnitude teaching,not an independent new vector skill or extra recipe family.',355,'show/prove')
p['additional_operations']={'nested_pythagoras':{'kind':'identity','operands':['sqrt(sqrt(a**2+b**2)**2+c**2)-sqrt(a**2+b**2+c**2)']}};p['additional_operation_expected']={'nested_pythagoras':'0'}
add('Prompt',2,253,'Show the3Dlength formula using two perpendicular right triangles. Retain the conceptual derivation separately from numeric magnitude calculations.',[p],teaches=[MAG])
add('Example',3,253,'Find the magnitude of the3Dvector(2,−5,3),with the source explicitly giving6.16to2decimal places.',[magnitude('magnitude',['2','-5','3'],'6.16',253,dp=2)],[MAG])

parts=[]
for label,tail,head,key,kp in [('i',[1,1],[4,3],'Tuple(3,2)',355),('ii',[-2,3],[3,-1],'Tuple(5,-4)',355),('iii',[1,2],[4,2],'Tuple(3,0)',355),('iv',[4,2],[1,1],'Tuple(-3,-1)',355)]:
 expr='Tuple('+','.join(f'{b}-({a})'for a,b in zip(tail,head))+')'
 p=v(label,expr,key,kp,'Read the arrowhead and tail from the rendered coordinate grid,then computeheadminus tail. A free arrow need not start at the origin. Horizontal components do not depend on the arrow’s drawn vertical location;direction reversal changes every component sign.')
 p['source_arrow_tail']=tail;p['source_arrow_head']=head;parts.append(p)
add('Exercise-10A',1,253,'Read four given2Dgrid arrows in component form:two start on253andtwo continue254. Preserve all head/tail locations and reverse-direction signs.',parts,[NOTATION,DISP],rep='graph',continuation=[254])

parts=[]
for label,components,mag,angle in [('i',['2','3'],'sqrt(13)','56.3'),('ii',['3','-2'],'sqrt(13)','-33.7'),('iii',['-4','-4'],'4*sqrt(2)','-135'),('iv',['-1','2'],'sqrt(5)','116.6'),('v',['3','-4'],'5','-53.1')]:
 p=reasoning(label+'-diagram','Draw a directed arrow with components('+','.join(components)+'),for example from the origin to that point,on consistently scaled perpendicular axes.',
  'The source asks for a diagram,not only a number. The arrow’s horizontal/vertical displacements and quadrant must agree with the signed components. Translating both endpoints equally is valid because the vector is free. The key’s grid arrows have these displacements;no particular drawing origin is required.',355 if label=='i'else 356,'sketch');parts.append(p)
 parts.append(magnitude(label+'-magnitude',components,mag,355 if label=='i'else 356))
 parts.append(direction(label+'-direction',components,angle,355 if label=='i'else 356))
row=add('Exercise-10A',2,254,'For five2Dcomponent vectors,draw a diagram and find both magnitude and direction. The key retains exact radical magnitudes and uses1decimal degree directions,including quadrantsIIandIII. Each requested drawing is a separate response.',parts,[NOTATION,MAG],teaches=[ANGLE],rep='text');row['sketch_response_required']=True
row['direct_demand_aspects']=[{'demand_id':MAG,'assessed_facet':'Each magnitude response.'},{'demand_id':NOTATION,'assessed_facet':'Each requested directed-arrow representation.'}]
row['scope_check']['excluded_or_qualified_parts'].append('Signed polar direction is supporting orientation practice. The official O05requires scalar-product angle determination between directions;the source atan2-style polar task doesnot by itself establish that full demand.')
parts=[]
for label,components,key in [('i',['1','-2','3'],'3.74'),('ii',['4','0','-2'],'4.47'),('iii',['2','4','2'],'4.90'),('iv',['1','1','-3'],'3.32'),('v',['6','-2','-3'],'7'),('vi',['1','0','-2'],'2.24')]:parts.append(magnitude(label,components,key,356,sf=3))
add('Exercise-10A',3,254,'Find six3Dvector magnitudes from column andi,j,kforms. Zero components are retained;the key displays3significant figures where needed.',parts,[MAG],[NOTATION])
parts=[]
for label,tail,head,key in [
 ('i',[2,3],[4,1],'Tuple(2,-2)'),('ii',[4,0],[6,0],'Tuple(2,0)'),('iii',[0,0],[0,-4],'Tuple(0,-4)'),('iv',[0,-4],[0,0],'Tuple(0,4)'),
 ('v',[0,0,0],[0,0,5],'Tuple(0,0,5)'),('vi',[0,0,0],[-1,-2,3],'Tuple(-1,-2,3)'),('vii',[-1,-2,3],[0,0,0],'Tuple(1,2,-3)'),('viii',[0,2,0],[4,0,4],'Tuple(4,-2,4)'),('ix',[1,2,3],[3,2,1],'Tuple(2,0,-2)'),('x',[4,-5,0],[-4,5,1],'Tuple(-8,10,1)')]:
 expr='Tuple('+','.join(f'{b}-({a})'for a,b in zip(tail,head))+')';p=v(label,expr,key,356,'For the ordered source endpoints,compute destination minus origin independently in every coordinate. The question’s joining order fixes the directed displacement. Do not confuse a zero component with a zero whole vector.');p['source_arrow_tail']=tail;p['source_arrow_head']=head;parts.append(p)
add('Exercise-10A',4,254,'Write the directed components for ten ordered endpoint pairs,including2Dand3Daxis-aligned cases,reversals and non-origin displacements.',parts,[DISP],[ADD])
parts=[v('i-position-A','Tuple(2,3)','Tuple(2,3)',356,'Position vectorOAuses the source coordinatesA=(2,3)relative toO.'),v('i-position-C','Tuple(-2,1)','Tuple(-2,1)',356,'Position vectorOCusesC=(−2,1).'),v('ii-AB','Tuple(0-2,4-3)','Tuple(-2,1)',356,'SubtractAfromB=(0,4)to obtainAB.'),v('ii-CB','Tuple(0-(-2),4-1)','Tuple(2,3)',356,'SubtractCfromBto obtainCB;the order is important.')]
for label,text,why in [('iii-a','AB=OC.','Both equal(−2,1). They are equal free vectors,not coincident segments.'),('iii-b','CB=OA.','Both equal(2,3),so the corresponding opposite sides are equal and parallel.'),('iv','OABCis a parallelogram.','Both pairs of opposite directed sides agree. The points are noncollinear here:det[(2,3),(−2,1)]=8≠0,so the quadrilateral is nondegenerate.')]:parts.append(reasoning(label,text,why,356,'matches'))
add('Exercise-10A',5,254,'FromA(2,3),B(0,4),C(−2,1),give position/displacement vectors,interpret two equalities,and identifyOABC. The final answer needs a geometric explanation,not just four coordinate tuples.',parts,[POS,DISP,GEOM],[ADD])

for n,page,label,note,teaches,rep,checks,parent in [
 (1,248,'Aircraft-trail photograph','A2Dphoto does not give the two3Dpaths or simultaneous aircraft positions. It is contextual motivation,not measurable separation data.',[],'diagram',[],'Prompt:1'),
 (2,249,'Figure10.1 magnitude-direction arrow','The vector has magnitude5andangle+30°anticlockwise from+x. Its components are(5√3/2,5/2),not a30°bearing from north.',[MAG,ANGLE],'diagram',[('Tuple(5*cos(pi/6),5*sin(pi/6))','Tuple(5*sqrt(3)/2,Rational(5,2))')],None),
 (3,249,'Bearing-convention warning','The chapter’s polar direction is anticlockwise from+x. Real-travel compass bearings are clockwise from north;the source explicitly says it is not using those bearings here.',[ANGLE],'table',[],None),
 (4,249,'Figure10.2 vector component triangle','The free arrow has horizontal component4andvertical2;its magnitude√20does not equal the sum6.',[NOTATION,MAG],'diagram',[('sqrt(4**2+2**2)','2*sqrt(5)')],None),
 (5,249,'Figure10.3 unit-axis vectors','iandjare perpendicular unit directions along the chosen positivexandyaxes. They name vectors,not point positions.',[UNIT,NOTATION],'diagram',[],None),
 (6,250,'Figure10.4 magnitude-angle worked triangle','The worked4i+2jtriangle preserves base4,height2andacute direction angle;its hypotenuse is√20. Source rounding is3significant figures for this example.',[MAG,ANGLE],'diagram',[],'Example:1'),
 (7,250,'Three-dimensional scaffolding photograph','The unprompted photo motivates3Drelationships but fixes no mathematical vector coordinates or assessed response.',[],'diagram',[],None),
 (8,251,'Figure10.5 point and projections','The marked point is(3,4,1)on the displayed3Daxes. Dashed projections show coordinate reading;perspective lengths are not numerical scale measurements.',['8227:2020:M1:T7:O01:D01'],'diagram',[],None),
 (9,251,'Figure10.6 equal free vectors','Translated arrows can represent the same3i+4j+kvector. Equality fixes components,magnitude and direction but does not fix location;position vectors are a separate origin-anchored case.',[NOTATION,POS],'diagram',[],None),
 (10,252,'Distance versus displacement example','A5kmeast then12kmnorth route has travelled distance17kmanddisplacement magnitude13km. The two scalars answer different questions.',[DISP,MAG],'table',[('Tuple(5+12,sqrt(5**2+12**2))','Tuple(17,13)')],None),
 (11,252,'Figure10.7 equal directed segments on a grid','OLfrom(0,0)to(4,3)andMNfrom(−2,−1)to(2,2)have the same components(4,3). The points and grid,not guessed arrow length,fix the given vectors.',[POS,DISP,GEOM],'graph',[],'Example:2'),
 (12,253,'Line-segment versus infinite-line note','A joining segment is bounded by its endpoints. Its directed vector has finite length;the infinite supporting line does not have that finite length.',[GEOM],'table',[],None),
 (13,253,'2Dand3D Pythagorean magnitude reference','Perpendicular components give√(a₁²+a₂²)in2Dand√(a₁²+a₂²+a₃²)in3D. Take the nonnegative square root;direction needs separate nonzero-vector information.',[MAG],'table',[],None),
 (14,253,'Exercise10A1(i)given arrow','Grid arrow tail(1,1),head(4,3),so vector(3,2). This is a displaced free arrow,not an origin-position vector.',[DISP,NOTATION],'graph',[],'Exercise-10A:1'),
 (15,253,'Exercise10A1(ii)given arrow','Grid arrow tail(−2,3),head(3,−1),so vector(5,−4). The arrowhead determines the signs.',[DISP,NOTATION],'graph',[],'Exercise-10A:1'),
 (16,254,'Exercise10A1(iii)given horizontal arrow','Grid arrow tail(1,2),head(4,2),so vector(3,0). Height2does not become a vertical displacement component.',[DISP,NOTATION],'graph',[],'Exercise-10A:1'),
 (17,254,'Exercise10A1(iv)given reversed arrow','Grid arrow tail(4,2),head(1,1),so vector(−3,−1). Preserve the left/down arrow direction.',[DISP,NOTATION],'graph',[],'Exercise-10A:1')]:
 fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={248:'Opening specification prompt and photo retained. Defining or finding distances between skew vector lines is not commissioned by this contextual question.',249:'Three numbered vector diagrams and the angle-versus-bearing convention note are separately recorded.',250:'Example10.1andits triangle,plus the unprompted3Dcontext photo,are recorded.',251:'Both3Dpoint/projection and translated-free-vector diagrams are recorded;the prose distinguishes equal vectors from an origin-anchored position vector.',252:'Distance/displacement reference,allExample10.2responses,andthe equal-segment grid are recorded.',253:'The segment note,magnitude reference,3Dproof prompt andExample10.3are recorded.10A1(i)/(ii)given arrows start here and continue254.',254:'All remaining10A1arrows and every10A2–5requested sketch,scalar,vector and geometric conclusion are recorded. The scalar-multiplication introductory wording belongs to the next page’s combined reference record.'}
pages=[]
for page in range(248,255):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:Goldie:C10:Exercise-10A:1']if page==254 else[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Vector magnitudes,positions,displacements,notation,angles and geometric relations are retained;context does not extend scope to skew-line equations.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C10-opening.json',{'scope':'Every original opening/10Aresponse,including all requested diagrams and their signs/angle units.','items':answers}),('census-Goldie-C10-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete248–254with all given/teaching figures and existing task IDs retained.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
