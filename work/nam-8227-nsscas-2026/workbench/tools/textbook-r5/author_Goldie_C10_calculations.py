"""Vector operations,complete named-point work,and geometry255–261."""
import json
import author_Goldie_C10_opening as opening
from author_Goldie_C10_opening import W,SRC,SHA,answers,new,fig,figures,corrections,ev,value,reasoning,compute,expression,equivalent,ADD,GEOM,UNIT,DISP,POS,MAG,NOTATION
answers.clear();new.clear();figures.clear();corrections.clear()
def add(*args,**kwargs):
 row=opening.add(*args,**kwargs)
 row['precision_angle_check']={'source':'Exact vector components/ratios throughout this segment,exceptExample10.7perimeter10.9printed to3significant figures. Midpoint coordinate2.5is exactly5/2.','comparison':'Keep exact components and nonzero unit-vector denominators. Geometric ratios here are internal with positive segment lengths;external division must be an explicit distinct branch. No compass-bearing or angle rounding is used.'}
 return row
def v(label,expr,key,page,method):return value(label,expr,key,page,method)
p=v('sum','Tuple(2+3,-3+5)','Tuple(5,2)',256,'Add the original two vectors component by component. The head-to-tail diagram has the same resultant(5,2)as the component calculation.')
add('Example',4,256,'Add2i−3jand3i+5j. The worked grid joins them head to tail and labels the resultant5i+2j.',[p],[ADD])
p=v('i-difference','Tuple(2-(-1),3-2)','Tuple(3,1)',257,'Subtract every component ofb=(−1,2)froma=(2,3). The negative first component ofbbecomes an addition;resulta−b=(3,1).')
p2=reasoning('ii-diagrams','Show directed arrowsa=(2,3),b=(−1,2),and a−b=(3,1),with a head-to-tail representation ofa+(−b).',
 'The source asks diagrams,so a coordinate answer alone is incomplete. The component displacements,arrowheads and common scale must agree. The key uses two panels:one for the source vectors and one showing the reversedbadded toa. Free vectors may be translated without changing their meaning.',257,'sketch')
row=add('Example',5,257,'Fora=2i+3j,b=−i+2j,finda−banddraw diagrams showinga,b,a−b. The requested visual evidence is retained separately from the arithmetic.',[p,p2],[ADD,GEOM],rep='diagram');row['sketch_response_required']=True

POINTS={'O':['0','0','0'],'A':['6','0','0'],'B':['6','5','0'],'C':['0','5','0'],'D':['0','0','4'],'E':['6','0','4'],'F':['6','5','4'],'G':['0','5','4'],'P':['3','0','0'],'Q':['6','5/2','0'],'R':['6','5/2','4'],'S':['3','5','4'],'T':['0','5/2','4']}
parts=[]
for label,coordinate,key in [('a','Tuple(6,5,4)','F'),('b','Tuple(0,5,0)','C'),('c','Tuple(6,Rational(5,2),0)','Q'),('d','Tuple(0,Rational(5,2),4)','T'),('e','Tuple(3,5,4)','S')]:
 p=v('i-'+label,'0',f"FiniteSet(Symbol('{key}'))",356,'Use the source’s three edge vectors and midpoint conditions to assign coordinates to every named point. Independently reverse-search that coordinate map for the requested position;do not identify a point by its apparent perspective location alone.')
 p['operation']={'kind':'named-point-location','operands':[coordinate],'points':POINTS};parts.append(p)
for label,target,keys in [('a','Tuple(6,5,4)',['OF']),('b','Tuple(6,0,4)',['OE','CF']),('c','Tuple(0,5,4)',['OG','PS','AF']),('d','Tuple(-6,-5,4)',['BD']),('e','Tuple(-3,Rational(5,2),4)',['QS','PT'])]:
 p=v('ii-'+label,'0','FiniteSet('+','.join(f"Symbol('{key}')"for key in keys)+')',356,'Enumerate every ordered pair of the13named points,subtract tail from head,and retain every exact match to the original target vector. This proves completeness within the source’s labelled-point population;it is not enough to find one matching edge. The source key’s list is compared only after the independent search.')
 p['operation']={'kind':'named-point-displacements','operands':[target],'points':POINTS};parts.append(p)
row=add('Activity',1,258,'Activity10.1uses a6×5×4cuboid with five named edge midpoints. Name all five specified positions,and find every labelled displacement for each of five target vectors. The complete13-point coordinate map is retained with the source diagram.',parts,['8227:2020:M1:T7:O01:D01',DISP],rep='diagram')
row['source_named_points']=POINTS

parts=[]
for label,tail,head,key in [('i','A','C','Tuple(1,1,0)'),('ii','A','D','Tuple(0,2,0)'),('iii','H','I','Tuple(-1,1,0)'),('iv','I','J','Tuple(-1,0,0)'),('v','E','F','Tuple(0,-1,0)'),('vi','B','E','Tuple(-2,2,0)'),('vii','A','H','Tuple(1,1,1)'),('viii','F','I','Tuple(1,1,1)')]:
 p=v(label,'0',key,259,'Use head-to-tail vector routes and the regular-hexagon side relations. Independently realise the regular front face in exact Cartesian coordinates,extrude it by a non-orthogonal3Dvector,and solve for the requested displacement’s p,q,rcoefficients. This computational cross-check does not require learners to use matrices or an unprescribed method. The target tuple means the coefficients ofp,q,r,in that order.')
 p['operation']={'kind':'regular-hex-prism-displacement','operands':[],'tail':tail,'head':head};parts.append(p)
row=add('Example',6,258,'For the given regular-hexagonal prism,AB=p,BC=q,BG=r. Express eight directed displacements inp,q,r. Both the front-face symmetry and the translated back face must stay consistent with the labels.',parts,[ADD,GEOM],rep='diagram',continuation=[259])
row['source_vector_basis_labels']=['p=AB','q=BC','r=BG']

expr='Tuple((0-(-2))/sqrt((0-(-2))**2+(1-3)**2+(-3-(-2))**2),(1-3)/sqrt((0-(-2))**2+(1-3)**2+(-3-(-2))**2),(-3-(-2))/sqrt((0-(-2))**2+(1-3)**2+(-3-(-2))**2))'
p=v('i-unit-AB',expr,'Tuple(Rational(2,3),-Rational(2,3),-Rational(1,3))',260,'SubtractA=(−2,3,−2)fromB=(0,1,−3)to obtainAB=(2,−2,−1). Its norm is3>0;divide by3to get the same-direction unit vector. ReversingABwould give the negative unit vector.')
p['source_unit_vector_components']=['2','-2','-1']
expr='sqrt((0-(-2))**2+(1-3)**2+(-3-(-2))**2)+sqrt((-2-(-2))**2+(3-3)**2+(1-(-2))**2)+sqrt((-2-0)**2+(3-1)**2+(1-(-3))**2)'
p2=v('ii-perimeter',expr,'10.9',261,'Compute all three original endpoint differences independently. The side lengths are3,3,√24,so the perimeter is6+√24≈10.898979…;the source prints10.9to3significant figures. Perimeter is the sum of lengths,not the zero vector sum around the closed triangle.')
p2['operation']={'kind':'rounded','operands':[expr],'significant_figures':3};p2['source_perimeter_points']=[['-2','3','-2'],['0','1','-3'],['-2','3','1']]
add('Example',7,260,'Given the3Dposition vectors ofA,B,C,find the unit vector alongABandthe triangle’s perimeter. Keep unit normalisation separate from summing three scalar side lengths.',[p,p2],[UNIT,MAG],[DISP],continuation=[261])
p=v('position-expression','expand(a+Rational(2,5)*(b-a))','3*a/5+2*b/5',261,'InternalAC:CB=2:3meansAC=(2/5)AB. RouteOC=OA+AC=a+(2/5)(b−a)=(3/5)a+(2/5)b. The coefficient ofanumerically comes from the opposite ratio segment;do not reverse the weights.')
add('Example',8,261,'Cinternally dividesABin ratio2:3. FindOCin termsofa=OAandb=OB;preserve the source’s internal ratio rather than using an external-division formula.',[p],[POS,GEOM],rep='diagram')
p=reasoning('internal-ratio-proof','IfAC:CB=s:twiths,t>0andA≠B,thenOC=[t/(s+t)]a+[s/(s+t)]b.',
 'Internal division givesAC=[s/(s+t)]AB. SubstituteAB=b−aandaddOA=a. Collecting coefficients yieldst/(s+t)foraands/(s+t)forb;their sum is1. This proof assumes positive internal segment lengths. External division needs a separately stated directed-ratio convention,not an unlabelled reuse of this formula.',356,'show/prove')
p['additional_operations']={'coefficient_identity':{'kind':'identity','operands':['expand(a+s/(s+t)*(b-a))-(t*a+s*b)/(s+t)']}};p['additional_operation_expected']={'coefficient_identity':'0'}
add('Prompt',3,261,'Prove the internal ratio theorem withpositive lengths s:t. The resulting formula and its nonzero denominator/internal-branch conditions are retained.',[p],[GEOM,POS])

for n,page,label,note,teaches,rep,parent in [
 (18,255,'Figure10.8 positive scalar multiplication','For2a,the length doubles and direction stays the same. The preceding unqualified number-multiplier sentence on254needs the positive-factor condition;negative factors reverse direction and zero has no unique direction.',['8227:2020:M1:T7:O02:D02'],'diagram',None),
 (19,255,'Figure10.9 negative vector','aand−ahave equal magnitude and opposite directions for nonzeroa. Their displayed free arrows may start at different locations;position does not change vector equality.',['8227:2020:M1:T7:O02:D02'],'diagram',None),
 (20,256,'Figure10.10 head-to-tail sum grid','The source adds(2,−3)and(3,5)with a head-to-tail grid route;the resultant is(5,2). Dashed component paths do not add extra vector quantities.',[ADD],'graph','Example:4'),
 (21,256,'Figure10.11 three-leg resultant','The resultant joins the initial tail to the final head across three journey legs. Scalar journey length is not generally the resultant magnitude.',[ADD,GEOM],'diagram',None),
 (22,257,'Figure10.12 vector subtraction panels','The left panel showsa=(2,3),b=(−1,2);the right reversesbandjoins it head to tail withatogivea−b=(3,1). Both panels must preserve the same component scale.',[ADD,GEOM],'graph','Example:5'),
 (23,257,'Figure10.13 position difference','P=(2,1),Q=(3,5),soPQ=q−p=(1,4). The diagram distinguishes the joining displacement from either origin-based position vector.',[POS,DISP],'graph',None),
 (24,258,'Figure10.14 cuboid and five midpoints','EdgesOA6,OC5,OD4define the coordinate axes. P,Q,R,S,Tare midpoints ofOA,AB,EF,GF,DGrespectively. All13labelled coordinates are stored with the activity;perspective lengths are not extra givens.',['8227:2020:M1:T7:O01:D01',DISP],'diagram','Activity:1'),
 (25,258,'Figure10.15 regular-hexagonal prism','The regular front cross-sectionA..FhasAB=p,BC=q,andfront-to-back translationBG=r. Back labelsG,H,I,Jcorrespond toB,C,D,Erespectively. The regular-face condition impliesAD=2qandopposite-side equalities.',[ADD,GEOM],'diagram','Example:6'),
 (26,259,'Figure10.16 three vector-route proof panels','The worked front-face panels showAC=p+q,CD=q−p,andBE=2(q−p)using the same regular-hexagon labels. These are explanatory routes,not separate learner questions.',[ADD,GEOM],'diagram','Example:6'),
 (27,259,'Prism translation reminder','CH=BG=ris the common front-to-back translation. It need not be an unproved right angle to the cross-section for the stated vector routes.',[GEOM],'table','Example:6'),
 (28,259,'Alternative prism path reminder','The pathFI=FE+EJ+JIusesFE=q,EJ=r,JI=p,soFI=p+q+r. Reversing an edge changes its sign;different valid paths must give the same displacement.',[ADD,GEOM],'table','Example:6'),
 (29,260,'Figure10.17 unit normalisation','The unit vector in direction(3,5)is(3/√34,5/√34). It is a positive multiple of the source vector and has length1;zero cannot be normalised.',[UNIT,MAG],'graph',None),
 (30,260,'Example10.7 norm reminder','AB=(2,−2,−1)has squared norm9andnorm3;divide by3rather than by9or by a sum of signed components.',[UNIT,MAG],'table','Example:7'),
 (31,261,'Figure10.18 internal division','Cis on the segmentABwithAC:CB=2:3. The point is a convex combination3a/5+2b/5and does not lie on the external continuation ofAB.',[POS,GEOM],'diagram','Example:8'),
 (32,261,'Internal-ratio fraction reminder','ACis2/5ofABandCBis3/5ofAB. These lengths are positive and sum toAB;the vectorCBpoints in the sameA-to-Bdirection here.',[GEOM],'table','Example:8')]:fig(n,page,label,note,teaches,rep,[],parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
 if f['item_number']=='24':f['source_named_points']=POINTS
notes={255:'Positive-scalar and negative-vector diagrams retained,with sign/zero qualifications;the introduction on254is linked through this reference. All component arithmetic is exposition,not additional learner responses.',256:'Example10.4andboth head-to-tail/resultant figures retained. The source distinguishes a drawn scale resultant from a component calculation.',257:'Example10.5has arithmetic plus a required visual response. Its two-panel subtraction grid and the position-difference reference each have records.',258:'EveryActivity10.1point-name/all-displacement response andthe cuboid figure are recorded. Example10.6andits prism figure begin here and continue259.',259:'All eightExample10.6displacements andthe three explanatory route panels/two translation callouts are retained. Unit-vector definition continues260.',260:'The unit-normalisation figure andExample10.7unit vector/norm reminder are retained;perimeter continues261.',261:'Example10.7perimeter,Example10.8internal ratio diagram/answer,andPrompt3general internal-ratio proof are recorded. The ratio convention is explicit.'}
pages=[]
for page in range(255,262):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 continuation=['8227:TB:Goldie:C10:Example:6']if page==259 else['8227:TB:Goldie:C10:Example:7']if page==261 else[]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':continuation,'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'All operations,geometry,unit and internal-ratio demands are prescribed;no line-equation or skew-line method is introduced.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C10-calculations.json',{'scope':'AllExample10.4–8,Activity10.1andPrompt3responses,with full named-point completeness.','items':answers}),('census-Goldie-C10-calculations.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete255–261with all given/teaching figures and existing IDs retained.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
