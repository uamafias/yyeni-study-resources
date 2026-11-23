"""YM282–285: real-root sign,normal constraints,and tangent angles."""
import json
import author_YM_C6_gradients_tangents as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;GRAD=h.GRAD;CHAIN=h.CHAIN;TANGENT=h.TANGENT;extra=h.extra;line=h.line;value=h.value
def add(kind,n,page,note,parts,components=None,rep='text'):
 r=h.add(kind,n,page,note,parts,[TANGENT],components or[POWER,GRAD],[p.get('source_original_function',p['original_function'])for p in parts if 'original_function'in p])
 r.update(representation=rep,mapping_rationale='Preserve the literal tangent/normal request,real root sign and named point. Given derivative data doesnotrequire differentiating again or reconstructing the full curve. Distinguish positive-axis inclination from acute angle between lines. Source conflicts retain both literal and context-intended interpretations.')
 for p in parts:p['given_representation']=rep
 return r
def supplied_normal(label,derivative,x0,y0,key,kp):
 p=value(label,f'expand(({y0})-1/(({derivative}).subs(x,{x0}))*(x-({x0})))',key,kp,[TANGENT],'The ORIGINAL expression is ALREADY dy/dx. Substitute the given xcoordinate once,then take its negative reciprocal and use the GIVEN curve point. Do not differentiate this supplied gradient again or invent a missing integration constant.',[GRAD])
 return p
def angle(label,expr,key,kp,method):
 p=value(label,expr,key,kp,[TANGENT],method,[GRAD]);p['operation']={'kind':'rounded','operands':[expr],'decimal_places':1};p['source_angle_unit']='degree';return p

add('Try-Now-12',3,282,'Normal of2x³−9x²+12x+7atx3/2;the nonzero tangent gradient−3/2gives normal2/3.',[line('normal','2*x**3-9*x**2+12*x+7','Rational(3,2)','Rational(2,3)*x+Rational(21,2)',620,True)])
ps=[]
for label,fn,at,printed,correct in [('a','4/x+1','1','x/4+Rational(19,4)','-4*x+9'),('b','(x**3-5)/x','-1','-x/3+Rational(17,3)','3*x+9')]:
 p=line(label,fn,at,printed,620,False);p['author_expected_normalised']=correct
 p.update(source_prompt_conflict='The literal item says TANGENT,but its surrounding Try12normal section and printed key imply NORMAL. The printed answer is valid for that context-intended normal,not for the literal tangent request.',context_intended_normal=printed,literal_requested_tangent=correct)
 # The two compared lines share the original point,so separately check slopes.
 extra(p,'literal-tangent-slope',f'diff({correct},x)-diff({fn},x).subs(x,{at})','0');ps.append(p)
add('Try-Now-12',4,282,'Literal stem repeats TANGENT while the section/key give NORMAL answers. Retain literal tangent corrections and the context-intended normal branch;do not silently rewrite the source.',ps)
ps=[]
for label,key,correct,normal in [('tangent','x-1','-x-5',False),('normal','-x-5','x-1',True)]:
 # On x<-1,the REAL reciprocal cube root is this negative real expression.
 p=line(label,'-3*(-x-1)**(-Rational(1,3))','-2',key,282,normal);p['author_expected_normalised']=correct
 p.update(source_original_function='3/real_cube_root(x+1)',real_domain='Use the real negative branch aroundx−2;original excludesx−1.',source_sign_defect='The source correctly writes the general negative derivative,then drops the minus atx−2. Its tangent and normal answers are swapped.')
 extra(p,'actual-gradient','diff(-3*(-x-1)**(-Rational(1,3)),x).subs(x,-2)','-1');ps.append(p)
add('Example',13,282,'For3/cuberoot(x+1)atx−2,the real ordinate is−3andtangent gradient−1. The source drops the negative sign and swaps its tangent/normal lines.',ps,[CHAIN,GRAD])
ps=[]
for label,fn,at,tk,nk in [('a','(2*x-5)**4','2','-8*x+17','x/8+Rational(3,4)'),('b','2*sqrt(x-5)','9','x/2-Rational(1,2)','-2*x+22'),('c','20/(x**2+1)','3','-Rational(6,5)*x+Rational(28,5)','Rational(5,6)*x-Rational(1,2)')]:
 ps.extend([line(label+'-tangent',fn,at,tk,620),line(label+'-normal',fn,at,nk,620,True)])
add('Try-Now-13',1,283,'Find both tangent and normal for a fourth power,a translated square root,and a rational curve at valid given inputs.',ps,[CHAIN,GRAD])
ps=[]
for label,fn,at,tk,nk in [('a','sqrt(2*x+1)','4','x/3+Rational(5,3)','-3*x+15'),('b','sqrt(3*x+1)','5','Rational(3,8)*x+Rational(17,8)','-Rational(8,3)*x+Rational(52,3)')]:
 ps.extend([line(label+'-tangent',fn,at,tk,620),line(label+'-normal',fn,at,nk,620,True)])
add('Try-Now-13',2,283,'Find tangent and normal equations at explicitly given points on two square-root curves,checking both point coordinates.',ps,[CHAIN,GRAD])
p=value('midpoint','Tuple((1+8*2)/2,(8+Rational(1,2))/2)','Tuple(Rational(17,2),Rational(17,4))',283,[TANGENT],'Original derivative4/sqrt(6−2x)atP(1,8)gives tangent2,normal−1/2. The normal is y=−x/2+17/2,with interceptsQ(17,0),R(0,17/2). Average those actual intercept positions;the requested answer is their midpoint,notP.',[GRAD,'8227:PRIOR:NSSCO:coordinate-geometry'])
extra(p,'given-gradient','(4/sqrt(6-2*x)).subs(x,1)','2')
add('Example',14,283,'Given a derivative and a curve point,find the midpoint of the normal intercepts without reconstructing a whole curve.',[p],[GRAD,'8227:PRIOR:NSSCO:coordinate-geometry'])
add('Try-Now-14',1,284,'Given dy/dx6/sqrt(3x−2)andP(2,11),find the normal directly from the supplied gradient.',[supplied_normal('normal','6/sqrt(3*x-2)','2','11','-x/3+Rational(35,3)',620)],[GRAD])
add('Try-Now-14',2,284,'Given dy/dx12/(x²+3)andP(1,3),find the normal;the supplied derivative isnotan equation fory.',[supplied_normal('normal','12/(x**2+3)','1','3','-x/3+Rational(10,3)',620)],[GRAD])
p=angle('angle','atan(Rational(1,7))*180/pi','8.1',284,'Original curve xy12gives y12/x,tangent gradient−12/x²atP(2,6)is−3. The supplied straight line2x+y10has slope−2. The acute line-angle has tangent|(-3+2)/(1+6)|=1/7. Use degrees andround ONLY the final angle to the explicit1decimal place. Both individual positive-axis inclinations are obtuse;their smaller difference is8.1degrees.')
extra(p,'original-point','Tuple(2*6,2*2+6)','Tuple(12,10)')
add('Example',15,284,'Find the angle between a given straight line and the tangent toxy12at their actual intersectionP(2,6),with explicit degree precision.',[p])
ps=[line('a-tangent','4/(3*x-4)','2','-3*x+8',620),angle('b-inclination','(pi-atan(3))*180/pi','108.4',620,'The tangent gradient is−3. The source asks the angle the tangent makes with the xaxis and its key uses the positive-axis inclination in[0,180). Thus pi−atan3gives108.4degrees;the acute complement71.6is a different convention and mustnotbe silently substituted.')]
add('Try-Now-15',1,285,'Find a rational-curve tangent then its positive-axis inclination;negative slope requires the obtuse inclination.',ps,[CHAIN,GRAD])
p=angle('angle','(atan(Rational(3,2))-atan(Rational(3,4)))*180/pi','19.4',620,'Original y=sqrt(3x+1)has derivative3/(2sqrt(3x+1)). AtP(0,1)andQ(1,2),tangent gradients are3/2and3/4. Both inclinations are acute;subtract their exact atanvalues and round the final smaller angle to1decimal place. The diagram fixes the two curve points,not two guessed drawn slopes.')
extra(p,'both-original-gradients','Tuple((3/(2*sqrt(3*x+1))).subs(x,0),(3/(2*sqrt(3*x+1))).subs(x,1))','Tuple(Rational(3,2),Rational(3,4))')
add('Try-Now-15',2,285,'Use two points on a square-root graph to find the angle between their tangents,not the joining chord.',[p],[CHAIN,GRAD],'graph')
p=value('a-intersections','Tuple(*solve(2*(x**2-4*x+7)-(x+5),x))','Tuple(Rational(3,2),3)',620,[],'Equate the ORIGINAL line2y=x+5andcurvey=x²−4x+7. Solve2x²−9x+9=0anduse the diagram orderingAleft,Bright. This is prerequisite simultaneous/quadratic work,not additional tangent coverage.',['8227:PRIOR:NSSCO:quadratic'])
ps=[p,line('b-tangent-B','x**2-4*x+7','3','2*x-2',620),angle('c-acute-angle','(atan(2)-atan(Rational(1,2)))*180/pi','36.9',620,'The right intersectionBhasx3andthe curve gradient2. The original line has slope1/2. Subtract their exact acute inclinations for the explicitly requested acute angle,thenround to1decimal place.')]
add('Try-Now-15',3,285,'Read ordered intersections from a quadratic/line graph,find tangent atB,andcalculate its acute angle with the given line.',ps,[POWER,GRAD,'8227:PRIOR:NSSCO:quadratic'],'graph')

refs=[(17,284,'Positive-axis inclination sign diagrams','m=tanθwithθin[0,180)for nonvertical lines;negative slope has obtuse positive-axis inclination. Do not confuse this with the acute angle between two lines. Vertical slope is not a finite tanvalue.',[TANGENT],'diagram',None),(18,284,'Example15 two inclination sketches','Tangent slope−3has inclination108.43degrees;straight line slope−2has116.57degrees. Their difference is8.1degrees,rounded at the final step.',[TANGENT],'diagram','Example:15'),(19,285,'Try15Q2 given square-root graph','y=sqrt(3x+1),P(0,1),Q(1,2);source axes and dotted projections identify exact coordinates. Tangents are requested,not supplied as measured straight lines.',[TANGENT],'graph','Try-Now-15:2'),(20,285,'Try15Q3 given quadratic and line','y=x²−4x+7and2y=x+5intersect atAleft(x3/2),Bright(x3). The drawing supplies ordering and representation;solve actual equations rather than measure the crossings.',[TANGENT],'graph','Try-Now-15:3')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:')if r['parent_item_id']else None
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if n in[19,20]else'teaching-figure')
 r['mathematical_feature_review']['method']='Read exact functions,point labels,axis projections and which angle is requested. Verify coordinates/slopes algebraically and preserve inclination versus acute-line-angle conventions;do not infer quantitative slopes from drawing tilt.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllTry12Q3/4,Examples13–15,Try13Q1/2,Try14Q1/2,Try15Q1–3andinclination/given graph panels are enumerated over282–285. The Try12Q4tangent/normal stem-key conflict andExample13minus-sign error are recorded explicitly.',scope_screen='Prescribed tangent/normal applications and gradient interpretation. Given derivative data mustnotbe differentiated again. Real cube-root branches,nonzero normal gradient,and angle conventions are preserved.')for page in range(282,286)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-normals-angles.json',dict(scope='All282–285explicit tasks.',items=answers)),('census-YM-C6-normals-angles.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete282–285page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
