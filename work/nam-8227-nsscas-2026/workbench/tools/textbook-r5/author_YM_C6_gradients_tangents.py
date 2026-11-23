"""YM278–281: point gradients,parameter recovery,tangents and normals."""
import json
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;GRAD=h.GRAD;CHAIN='8227:2020:M1:T8:O02:D02';TANGENT='8227:2020:M1:T8:O03:D01';extra=h.extra
def add(kind,n,page,note,parts,direct,components,powers,new_item=False):
 r=h.add(kind,n,page,note,parts,direct,components,new_item=new_item,powers=powers)
 r['mapping_rationale']='Distinguish curve ordinate from derivative value. Parameter constraints from given gradients belong to gradient interpretation; an actual tangent/normal equation additionally assesses the corresponding line demand. Preserve point membership,nonzero denominators,and both independent equations before solving constants.'
 if new_item:new[-1]['item_kind']='exercise'
 return r
def value(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[]);return p
def grad(label,fn,at,key,kp):
 return value(label,f'diff({fn},x).subs(x,{at})',key,kp,[GRAD],'Differentiate the ORIGINAL function before substituting its specified xcoordinate. This is a gradient,not the point ordinate. Retain original root/denominator domains.',[POWER])
def params(expr,key,kp,method,chain=False):
 return value('a-b',expr,key,kp,[GRAD],method,[CHAIN]if chain else[POWER])
def line(label,fn,at,key,kp,normal=False):
 slope=f'diff({fn},x).subs(x,{at})'
 if normal:slope=f'-1/({slope})'
 p=value(label,f'expand(({fn}).subs(x,{at})+({slope})*(x-({at})))',key,kp,[TANGENT],
  'Read the ORIGINAL curve and xcoordinate. Compute its ordinate and derivative there,then '+('take the negative reciprocal of the NONZERO tangent gradient for this normal.'if normal else'use that derivative as the tangent gradient.')+' Form the full point-gradient line,not just a slope. All points here are in the original domain; vertical-normal exceptions require a different branch,not division byzero.',[POWER,GRAD])
 p.update(original_function=fn,source_x=at,line_kind='normal'if normal else'tangent')
 extra(p,'original-point-on-line',f'({key}).subs(x,{at})-({fn}).subs(x,{at})','0')
 return p

ps=[]
for label,fn,at,g,y in [('a','x**2-2','1','2','-1'),('b','2*x**3-2','3','54','52'),('c','sqrt(x)-1','1','Rational(1,2)','0'),('d','2-1/x','-1','1','3'),('e','2*sqrt(x)*(2-sqrt(x))','4','-1','0'),('f','(x**Rational(1,3)-1)/x**Rational(1,3)','27','Rational(1,243)','Rational(2,3)')]:
 ps.append(grad(label+'-i-gradient',fn,at,g,619))
 ps.append(value(label+'-ii-y',f'({fn}).subs(x,{at})',y,619,[],'Substitute the given xcoordinate into the ORIGINAL curve,not its derivative. This requested companion ordinate supplies the point but doesnotcreate separate gradient-demand coverage.'))
add('Try-Now',8,278,'For six original curves,find both gradient and ordinate at the specified x. Distinguish two outputs;all given inputs satisfy the original real root/reciprocal conditions.',ps,[GRAD],[POWER],['2','3','1/2','−1','1/3','−1/3'])
p=params('Tuple(solve([2*a+b-4,4*a+b-14],[a,b],dict=True)[0][a],solve([2*a+b-4,4*a+b-14],[a,b],dict=True)[0][b])','Tuple(5,-6)',278,'Original y=ax²+bxhas derivative2ax+b. Use BOTH given gradients4atx1and14atx2,solve the simultaneous linear equations,and retain correlateda5,b−6.')
extra(p,'both-original-gradients','Tuple(2*5-6,4*5-6)','Tuple(4,14)')
add('Example',9,278,'Recover the two polynomial coefficients from two separate derivative values,not from two point ordinates.',[p],[GRAD],[POWER],['2','1'])
p=params('Tuple(solve([4*a+2*b+1-3,32*a+4*b+1-53],[a,b],dict=True)[0][a],solve([4*a+2*b+1-3,32*a+4*b+1-53],[a,b],dict=True)[0][b])','Tuple(2,-3)',619,'Original y=ax4+bx²+xhas derivative4ax³+2bx+1. Gradient3atx1and53atx2give a2,b−3. The final linear term contributes1,not0.')
extra(p,'both-gradients','Tuple(4*2+2*(-3)+1,32*2+4*(-3)+1)','Tuple(3,53)')
add('Try-Now-9',1,278,'Finda,bfrom quartic gradients3and53atx1and2,retaining the derivative of the final+xterm.',[p],[GRAD],[POWER],['4','2','1'])
p=params('Tuple(solve([a-2*b-2,a+2*b-14],[a,b],dict=True)[0][a],solve([a-2*b-2,a+2*b-14],[a,b],dict=True)[0][b])','Tuple(8,3)',619,'Original y=ax+b/x²has derivativea−2b/x³. Substitute BOTH signed inputs1and−1;the odd cube changes the sign of the reciprocal contribution. Solvea−2b2,a+2b14.')
extra(p,'both-gradients','Tuple(8-2*3,8+2*3)','Tuple(2,14)')
add('Try-Now-9',2,278,'Recovera8,b3from gradient conditions on opposite sides of the original polex0.',[p],[GRAD],[POWER],['1','−2'])
p=params('Tuple(2*solve(5*b-3*(2*b-1),b)[0]-1,solve(5*b-3*(2*b-1),b)[0])','Tuple(5,3)',279,'Original y=a/(bx−1)passes through(2,1),so a=2b−1with2b−1≠0. Its derivative there is−b/(2b−1)=−3/5. Solve5b=3(2b−1),givingb3,a5. Clearing the full original denominator can create the inadmissibleb1/2,a0pair;it makes the given pointundefined and must be rejected.',True)
extra(p,'valid-point-and-gradient','Tuple(5/(3*2-1),-5*3/(3*2-1)**2)','Tuple(1,-Rational(3,5))')
add('Example',10,279,'Recovera,bfrom a rational curve point and its gradient,explicitly rejecting the zero-denominator candidate introduced by clearing factors.',[p],[GRAD],[CHAIN],['−1','1'])
p=params('Tuple(solve([4*a+2*b+5-15,4*a+b-13],[a,b],dict=True)[0][a],solve([4*a+2*b+5-15,4*a+b-13],[a,b],dict=True)[0][b])','Tuple(4,-3)',619,'Original y=ax²+bx+5passes through(2,15),giving4a+2b=10. Derivative2ax+bthereis13,giving4a+b13. Solveboth simultaneous equations,not two copies of the same condition.')
add('Try-Now-10',1,279,'Recovera4,b−3from one quadratic point and its derivative condition. This numbered item was missing from the earlier heading inventory.',[p],[GRAD],[POWER],['2','1'],new_item=True)
p=params('Tuple(2,36-22*2)','Tuple(2,-8)',619,'Original sqrt(ax+b)passes through(22,6),so22a+b36andtheprincipal square root is positive6. Derivativea/(2sqrt(ax+b))thereequals1/6,so a/12=1/6and a2,b−8. The point lies strictly inside the resulting rootdomain.',True)
extra(p,'point-and-gradient','Tuple(sqrt(2*22-8),2/(2*sqrt(2*22-8)))','Tuple(6,Rational(1,6))')
add('Try-Now-10',2,279,'Recovera2,b−8from a square-root curve point andgradient1/6,using the positive square root6. Recovered missing numbered item.',[p],[GRAD],[CHAIN],['1/2','1'],new_item=True)
add('Example',11,280,'Find the full tangent toy=5x²−7x−1atx−1,using the actual ordinate11andgradient−17.',[line('tangent','5*x**2-7*x-1','-1','-17*x-6',280)],[TANGENT],[POWER,GRAD],['2','1'])
for number,fn,at,key in [(1,'x**3','-1','3*x+2'),(2,'x**2+3*x+1','0','3*x+1'),(3,'2*x**3-9*x**2+12*x+7','Rational(3,2)','-Rational(3,2)*x+Rational(55,4)')]:
 add('Try-Now-11',number,280,f'Find the tangent of the original curve{fn}atx={at};construct its point before the line equation.',[line('tangent',fn,at,key,619 if number==1 else 620)],[TANGENT],[POWER,GRAD],['3','2','1'])
add('Try-Now-11',4,281,'Find two rational-curve tangents at the independently specified inputs1and−1;retain original pole exclusions.',[line('a','4/x+1','1','-4*x+9',620),line('b','(x**3-5)/x','-1','3*x+9',620)],[TANGENT],[POWER,GRAD],['−1','2'])
add('Example',12,281,'Find the normal toy=−6/xat(−2,3). Tangent gradient3/2gives normal−2/3,andthefullnormal is−2x/3+5/3.',[line('normal','-6/x','-2','-Rational(2,3)*x+Rational(5,3)',281,True)],[TANGENT],[POWER,GRAD],['−1'])
for number,fn,at,key in [(1,'x**3','-1','-x/3-Rational(4,3)'),(2,'x**2+3*x+1','0','-x/3+1')]:
 add('Try-Now-12',number,281,f'Find the NORMAL for{fn}atx={at},reusing the preceding tangent point but changing the gradient to its negative reciprocal.',[line('normal',fn,at,key,620,True)],[TANGENT],[POWER,GRAD],['3','2','1'])

refs=[(14,280,'Tangent and normal incidence sketch','AtA(x1,y1)the tangent and normal share the actual curve point. Their slopes multiply to−1when both are finite and nonzero. The normal neednotcross the curve again in the drawn window.',[TANGENT],'diagram'),(15,280,'Point-gradient tangent reference','For finite derivative m=fprime(x1),tangent y−y1=m(x−x1). y1comes from the ORIGINAL curve. This is not a line through(0,0)unless the data imply it.',[TANGENT],'table'),(16,281,'Normal gradient reference','For finite NONZERO tangent gradientm,normalgradient−1/m. At m0the normal is verticalx=x1;do not use a division-by-zero formula. All current numerical normal tasks have nonzero tangent gradients.',[TANGENT],'table')]
for n,page,label,note,teaches,rep in refs:
 fig(n,page,label,note,teaches,rep,[]);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['mathematical_feature_review']['method']='Inspect named point,tangent/normal incidence,and formula notation on the original render. Recompute each line from the original function and its derivative;retain vertical exceptions as constraints for future variation.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllTry8,Examples9–12,Try9/10Q1/2,Try11Q1–4,Try12Q1/2andreference sketch/formulasare recorded over278–281. Try10Q1/2are newly recovered inventory entries. Later normal questions begin282andare not claimed here.',scope_screen='Gradient interpretation,chain components and tangent/normal equations are prescribed. Domain checks precede denominator clearing or normal reciprocals. No implicit derivative method is required.')for page in range(278,282)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-gradients-tangents.json',dict(scope='All278–281explicit tasks.',items=answers)),('census-YM-C6-gradients-tangents.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete278–281page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
