"""Every10Bresponse;linear arithmetic,geometric proofs,units and parameters."""
import json
from author_Goldie_C10_calculations import W,SRC,SHA,opening,add as source_add,answers,new,fig,figures,corrections,ev,v,reasoning,compute,expression,equivalent,ADD,GEOM,UNIT,DISP,POS,MAG,NOTATION
answers.clear();new.clear();figures.clear();corrections.clear()
SCALE='8227:2020:M1:T7:O02:D02'
def add(*args,**kwargs):
 row=source_add(*args,**kwargs);row['precision_angle_check']={'source':'Exact components,unit vectors,parameters and symbolic geometric relations. Q8key displays perimeter11.74without an explicit rounding instruction in the question.','comparison':'Retain exact8+√14forQ8and compare its displayed key at2decimal places;that comparison is not an invented learner precision requirement. No angular response occurs in10B.'};return row
def tuple_matrix(expr):return 'Tuple(*('+expr+'))'
parts=[]
for label,expr,key in [('i','Matrix([2,3])+Matrix([4,5])','Tuple(6,8)'),('ii','Matrix([2,-1])+Matrix([-1,2])','Tuple(1,1)'),('iii','Matrix([3,4])+Matrix([-3,-4])','Tuple(0,0)'),('iv','3*Matrix([2,1])+2*Matrix([1,-2])','Tuple(8,-1)'),('v','6*Matrix([3,-2])-9*Matrix([2,-1])','Tuple(0,-3)')]:
 parts.append(v(label,tuple_matrix(expr),key,356,'Calculate the original source sum/scaled difference independently in each coordinate. The opposite-vector sum in(iii)is exactly the zero vector;do not assign it a direction or try to normalise it.'))
add('Exercise-10B',1,262,'Simplify five2Dvector sums and scaled differences,including an exact zero-vector result and a subtraction of two scaled vectors.',parts,[ADD,SCALE])
p='Matrix([3,2,1])';q='Matrix([2,2,2])';r='Matrix([-3,-1,-2])'
parts=[]
for label,expr,key in [('i',f'{p}+{q}+{r}','Tuple(2,3,1)'),('ii',f'{p}-{q}','Tuple(1,0,-1)'),('iii',f'{p}+{r}','Tuple(0,1,-1)'),('iv',f'3*({p}-{q})+2*({p}+{r})','Tuple(3,2,-5)'),('v',f'4*{p}-3*{q}+2*{r}','Tuple(0,0,-6)')]:
 parts.append(v(label,tuple_matrix(expr),key,356,'Use the separately transcribed original3Dcomponent vector values. Native4xreading confirmsr=−3i−j−2k;retain its negativejcomponent. Expand the linear combination and independently check every resulting coordinate.'))
add('Exercise-10B',2,262,'Withp=(3,2,1),q=(2,2,2),r=(−3,−1,−2),find five specified3Dlinear combinations. The inputrhas a negative unitjcomponent,not a zero one.',parts,[ADD,SCALE])
parts=[]
for label,expr,key,why in [('i-a-QR','b','b','Opposite sides of the given parallelogram have equal directed vectors.'),('i-b-PR','a+b','a+b','FollowP→Q→R.'),('i-c-QS','b-a','b-a','UseQ→P→S,so reversePQthenaddPS.'),('ii-a-PM','(a+b)/2','(a+b)/2','MmidpointsPR,soPMis half the diagonalPR.'),('ii-b-QM','-a+(a+b)/2','(b-a)/2','FollowQ→P→Mand simplify.')]:parts.append(v(label,expr,key,356,why+' Herea,bare formal independent vector coefficients;scalar-symbol collection checks the corresponding linear combination.'))
p=reasoning('iii-diagonal-bisection','Malso lies halfway alongQS,so both diagonals meet at their common midpoint.',
 'Part(ii)givesPM=½PRandQM=½(b−a)=½QS. Thus the midpoint ofPRis also the midpoint ofQS. The source is a nondegenerate parallelogram,so these two diagonals intersect uniquely atM. A sketch alone is not the required explanatory evidence.',356,'show/prove')
p['source_dependency_edges']=[{'from':s,'type':'cue','cue':'this shows','role':'Use the two midpoint vector relations.'}for s in['ii-a-PM','ii-b-QM']];parts.append(p)
row=add('Exercise-10B',3,262,'From a given parallelogram withPQ=a,PS=b,write three joining vectors,find two midpoint vectors,and explain why the diagonals bisect one another. The final explanation is separate from arithmetic.',parts,[ADD,DISP,GEOM],rep='diagram')

parts=[]
for label,expr,key,why in [('i-a-AM','Tuple(1,0)','Tuple(1,0)','The perpendicular diagonals meet atM,which is the midpoint ofAC. Project the givenAB=(1,1)onto the horizontalACdirection to obtainAM=i.'),('i-b-AC','Tuple(2,0)','Tuple(2,0)','SinceMmidpointsAC,the whole vectorAC=2AM=2i.'),('i-c-BC','Tuple(2-1,0-1)','Tuple(1,-1)','UseAas a temporary origin:B=(1,1),C=(2,0),soBC=C−B.'),('i-d-CD','Tuple(1-2,-2-0)','Tuple(-1,-2)','The givenAD=(1,−2)fixesDrelative toA;subtractC=(2,0)to findCD.')]:parts.append(v(label,expr,key,356,why))
for label,expr,key,why in [('ii-short-pair','Tuple(sqrt(1**2+1**2),sqrt(1**2+(-1)**2))','Tuple(sqrt(2),sqrt(2))','ComputeABandBCnorms from their own signed components.'),('ii-long-pair','Tuple(sqrt(1**2+(-2)**2),sqrt((-1)**2+(-2)**2))','Tuple(sqrt(5),sqrt(5))','ComputeADandCDnorms;the differing horizontal signs do not change length.')]:
 p=v(label,expr,key,356,why+' The equal norms verify the two adjacent equal-side pairs.');p['check_mode']='show/prove';parts.append(p)
add('Exercise-10B',4,262,'Use the given kite’s perpendicular diagonals and midpoint property to find four directed vectors,then verify both pairs of equal adjacent lengths. Neither diagonal equality nor right-angle side assumptions are supplied.',parts,[DISP,GEOM,MAG],rep='diagram')

parts=[]
for label,expr,key,why in [('i-BC','q-p','q-p','FollowB→A→C.'),('i-MN','p/2-q/2','(p-q)/2','WithAas temporary origin,N=p/2andM=q/2.'),('i-LM','q/2-(p+q)/2','-p/2','L=(p+q)/2is midpointBC;subtractLfromM.'),('i-LN','p/2-(p+q)/2','-q/2','SubtractLfromNand retain the directed sign.')]:parts.append(v(label,expr,key,356,why))
p=reasoning('ii-midpoint-triangle','NM=½BC,NL=½ACandML=½AB;therefore the corresponding sides are parallel and half as long.',
 'Reverse the part(i)vectors where needed:NM=−MN=(q−p)/2,NL=−LN=q/2,andML=−LM=p/2. Each is a positive half of the corresponding original side vector. The source triangle is nondegenerate;the conclusion concerns parallel directions and scalar lengths,not equality of the two triangles.',356,'show/prove')
p['source_dependency_edges']=[{'from':s,'type':'cue','cue':'your results from part(i)','role':'Reverse directed sides where necessary before comparing them.'}for s in['i-BC','i-MN','i-LM','i-LN']];parts.append(p)
add('Exercise-10B',5,262,'For the triangle with side-midpoint labelsL,M,N,find four directed vector expressions and use them to prove the midpoint triangle’s sides are parallel and half-length. Preserve all midpoint labels and arrow orders.',parts,[ADD,GEOM,DISP],rep='diagram')

for n,values in [(6,[('i',['2','3'],'Tuple(2/sqrt(13),3/sqrt(13))'),('ii',['3','4'],'Tuple(Rational(3,5),Rational(4,5))'),('iii',['-2','-2'],'Tuple(-1/sqrt(2),-1/sqrt(2))'),('iv',['5','-12'],'Tuple(Rational(5,13),-Rational(12,13))')]),(7,[('i',['1','2','3'],'Tuple(1/sqrt(14),2/sqrt(14),3/sqrt(14))'),('ii',['2','-2','1'],'Tuple(Rational(2,3),-Rational(2,3),Rational(1,3))'),('iii',['3','0','-4'],'Tuple(Rational(3,5),0,-Rational(4,5))'),('iv',['-2','4','-3'],'Tuple(-2/sqrt(29),4/sqrt(29),-3/sqrt(29))'),('v',['5','-3','2'],'Tuple(5/sqrt(38),-3/sqrt(38),2/sqrt(38))'),('vi',['4','0','0'],'Tuple(1,0,0)')])]:
 parts=[]
 for label,components,key in values:
  norm='sqrt('+ '+'.join(f'({v})**2'for v in components)+')';expr='Tuple('+','.join(f'({v})/({norm})'for v in components)+')'
  p=v(label,expr,key,357,'Use the original vector’s positive Euclidean norm and divide every signed component by it. Confirm length1and the same direction. All source vectors here are nonzero,including the axis vector with two zero components.');p['source_unit_vector_components']=components;parts.append(p)
 add('Exercise-10B',n,263,'Find same-direction unit vectors for '+('four2D'if n==6 else'six3D')+'source vectors. Signs,zero components and nonzero total norms are explicit;retain exact radicals/fractions.',parts,[UNIT],[MAG])

points=[['2','1','3'],['-2','4','3'],['-1','2','1']]
expr='sqrt((-2-2)**2+(4-1)**2+(3-3)**2)+sqrt((-1-(-2))**2+(2-4)**2+(1-3)**2)+sqrt((2-(-1))**2+(1-2)**2+(3-1)**2)'
p=v('perimeter',expr,'11.74',357,'Derive the three endpoint differences and their lengths:5,3,√14. Exact perimeter is8+√14. The question gives no explicit precision;the key’s11.74is a2decimal-place display,compared only as such rather than imposed on later learner marking.')
p['operation']={'kind':'rounded','operands':[expr],'decimal_places':2};p['source_perimeter_points']=points;p['author_answer_form']='8+√14units;printed key approximation11.74.'
add('Exercise-10B',8,263,'Find the perimeter of the3Dtriangle from its position vectors. The exact value8+√14is retained independently of the book’s11.74display.',[p],[MAG],[DISP])
p=v('parameter-values','FiniteSet(*solve((-2)**2+(x-1)**2+(-6)**2-7**2,x))','FiniteSet(-2,4)',357,'PQ=(1−3,x−1,−2−4)=(−2,x−1,−6). Its squared norm49gives(x−1)²=9,hencex=−2or4. Both satisfy the original positive length7;no positivity restriction onxis stated.')
p['additional_operations']={'original_squared_lengths':{'kind':'identity','operands':['Tuple((4+(x-1)**2+36).subs(x,-2),(4+(x-1)**2+36).subs(x,4))']}};p['additional_operation_expected']={'original_squared_lengths':'Tuple(49,49)'}
add('Exercise-10B',9,263,'ForP=(3,1,4),Q=(1,x,−2),find everyrealxgiving|PQ|=7. Retain both parameter roots rather than silently choosing the positive one.',[p],[MAG],[DISP])

parts=[]
for label,expr,key,why in [('i-a-GF','q','q','GFis the same depth translation asOE.'),('i-b-CF','-p','-p','CFgoes down the opposite direction toOA.'),('i-c-OB','p+q','p+q','RouteO→A→B.'),('i-d-OD','p+r','p+r','RouteO→A→D.'),('i-e-OC','p+q+r','p+q+r','RouteO→A→B→C.'),('ii-OM','p+Rational(3,5)*r','p+3*r/5','MdividesADin the internal ratio3:2,soAM=3r/5andOM=p+3r/5.')]:parts.append(v(label,expr,key,357,why+' The diagram’sp,q,rare independent edge vectors;they are not position coordinates to be mixed with scalar lengths.'))
p=reasoning('iii-diagonal-bisection','The midpoint ofOCandthe midpoint ofBGboth have position½(p+q+r),so the diagonals bisect one another.',
 'The supplied originOhas vector0,C=p+q+r,B=p+q,G=r. Average each pair of endpoint position vectors:½(0+C)=½(B+G). A nondegenerate cuboid’s diagonals therefore share the same midpoint. The source asks a vector proof,not visual coincidence alone.',263,'show/prove')
p['additional_operations']={'midpoint_identity':{'kind':'identity','operands':['(p+q+r)/2-((p+q)+r)/2']}};p['additional_operation_expected']={'midpoint_identity':'0'};parts.append(p)
add('Exercise-10B',10,263,'Use the cuboid’s three edge vectors to find five displacements,an internal3:2edge-division point,and a proof that two body diagonals bisect each other. Preserve the source’s differently oriented cuboid labels.',parts,[ADD,GEOM,POS],rep='diagram')

p=reasoning('parallelogram-proof','AB=DC=(2,4,8)andAD=BC=(3,−3,−6);thereforeABCDis a parallelogram.',
 'Subtract the original3Dpoint coordinates in the directed orders. Both pairs of opposite sides are equal as vectors. Adjacent sides are not scalar multiples here,so the quadrilateral is nondegenerate. This vector argument does not require a cross-product formula or line equations.',263,'show/prove')
p['additional_operations']={'four_sides':{'kind':'identity','operands':['Tuple(Tuple(5-3,5-1,13-5),Tuple(8-6,2-(-2),7-(-1)),Tuple(6-3,-2-1,-1-5),Tuple(8-5,2-5,7-13))']},'midpoint_identity':{'kind':'identity','operands':['Tuple(3+8-(5+6),1+2-(5-2),5+7-(13-1))']}}
p['additional_operation_expected']={'four_sides':'Tuple(Tuple(2,4,8),Tuple(2,4,8),Tuple(3,-3,-6),Tuple(3,-3,-6))','midpoint_identity':'Tuple(0,0,0)'}
add('Exercise-10B',11,263,'ProveABCDa parallelogram from four3Dposition vectors,using directed differences and a stated geometric reason. The alternative matching-diagonal-midpoint check is also recorded.',[p],[GEOM],[DISP])

p=v('i-unit-OC','Tuple((2*3-4)/sqrt((2*3-4)**2+(2*2-1)**2+(2*(-4)-(-2))**2),(2*2-1)/sqrt((2*3-4)**2+(2*2-1)**2+(2*(-4)-(-2))**2),(2*(-4)-(-2))/sqrt((2*3-4)**2+(2*2-1)**2+(2*(-4)-(-2))**2))','Tuple(Rational(2,7),Rational(3,7),-Rational(6,7))',357,'The source explicitly givesAC=2AB,soC=A+2(B−A)=2B−A=(2,3,−6),beyondBon theA→Bline. This is not internal2:1division. Its norm is7andits same-direction unit vector is(2/7,3/7,−6/7).')
p['source_unit_vector_components']=['2','3','-6']
solution='solve([4*a+3*b-1,a+2*b-4],(a,b))';expr='Tuple('+solution+'[a],'+solution+'[b],-2*'+solution+'[a]-4*'+solution+'[b])'
p2=v('ii-coefficients',expr,'Tuple(-2,3,-8)',357,'FromD=mA+nBandD=(1,4,k),the first two coordinates give4m+3n=1andm+2n=4. Solve simultaneously:m=−2,n=3. Then the third coordinate isk=−2m−4n=−8. Retain the negative linear-combination coefficient;this is not a convex/internal-ratio point.')
add('Exercise-10B',12,264,'GivenAandB,first use the explicitly external relationAC=2ABto normaliseOC. Independently solve for m,n,kinthe supplied position-vector relationD=mA+nB. Both are prescribed vector geometry despite negative coefficients.',[p,p2],[UNIT,POS,GEOM],[DISP],exam_attribution='Cambridge9709Paper1Q9June2007')

for n,page,label,note,teaches,parent in [
 (33,262,'Exercise10B3 parallelogram','PQ=a,PS=bfix the edge orientations;Mmidpoints diagonalPR. The diagram must not silently swapQandSwhen comparingQMwithQS.',[GEOM,DISP],'Exercise-10B:3'),
 (34,262,'Exercise10B4 kite','AandCare the left/right diagonal endpoints,Btop,Dbottom. Mis midpointACanddiagonals are perpendicular. AB=(1,1),AD=(1,−2)fix unequal upper/lower heights;do not assumeMis midpointBD.',[GEOM,DISP],'Exercise-10B:4'),
 (35,262,'Exercise10B5 midpoint triangle','NmidpointsAB,MmidpointsAC,LmidpointsBC. GivenAB=p,AC=qfix directed routes and midpoint positions;the smaller triangle’s side directions may need reversing before comparison.',[GEOM,DISP],'Exercise-10B:5'),
 (36,263,'Exercise10B10 cuboid','Ois the lower near-left origin,OA=pupwards,OE=qbackwards,OG=rrightwards. ThenB=p+q,C=p+q+r,D=p+r,F=q+r. Mlies onADin ratio3:2. These labels differ from Activity10.1and must not be copied from that earlier diagram.',[GEOM,POS],'Exercise-10B:10')]:fig(n,page,label,note,teaches,'diagram',[],parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:');f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
pages=[]
for page in[262,263]:
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every10B1–11requested response and all four given geometric diagrams are recorded.10B12starts264andis linked by the following scalar-product census.','scope_screen':'Vector arithmetic,unit vectors,magnitude constraints,positions and geometric reasoning;no line-equation method.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C10-10B.json',{'scope':'Every10B1–12response,including explicit geometric proofs and all parameter roots.','items':answers}),('census-Goldie-C10-10B.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete262–263;12on264is linked by the next census.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
