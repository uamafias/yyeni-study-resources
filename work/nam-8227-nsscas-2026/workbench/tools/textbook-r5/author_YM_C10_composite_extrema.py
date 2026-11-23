"""YM476–477: nonlinear range maps and half-angle least-positive attainment."""
import json
import author_YM_C10_rform_cycles_extrema as m
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
import author_YM_C9_opening as g
import author_YM_C10_opening as o
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
RFORM=m.RFORM;RANGE=m.RANGE
form=m.form;value=m.value

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts)
 r.update(mapping_rationale='R-form coefficient recovery and the requested extrema are direct. A square has an interior minimum at zero; a cube is monotone on the entire attainable inner range. A half-angle argument changes the attainment period to720degrees. No unasked full solution set or assumed0..360restriction is added.',value_level_scope_decisions=[],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=[]),precision_angle_check=dict(source='Example25/Try25explicitly request phase2dp; earlier nearby R-form workings display2dp. Attainingangles shown1dp are source display conventions where no precision is asked.',comparison='Use exact coefficient norm and phase internally. Retain periodic nonuniqueness for Try23, and the smallest positive half-angle argument for Example25. Never substitute rounded phase into an exact identity.'))
 return r

def extrema(label,radius,polynomial,maxkey,minkey,kp):
 ps=[]
 for suffix,func,key in [('maximum','maximum',maxkey),('minimum','minimum',minkey)]:
  p=value(label+'-'+suffix,f'{func}({polynomial},x,Interval(-({radius}),{radius}))',key,kp,[RFORM,RANGE],'Independently optimize the actual OUTER polynomial on the CLOSED attainable inner interval[-R,R], including interior stationary points and endpoints. Original sine/cosine reaches every inner value in this interval. A square minimum is at inner0,while a cubic preserves order.')
  p.update(inner_attainable_interval='[-'+radius+','+radius+']',outer_polynomial=polynomial);ps.append(p)
 return ps
ps=[]
for label,a,b,target,r,maxx,minx,kmax,kmin,phasekey in [('a','sqrt(3)','1','sin-plus','2','60','240','60','240','30'),('b','-2','3','cos-plus','sqrt(13)','360-180*atan(Rational(2,3))/pi','180-180*atan(Rational(2,3))/pi','Rational(3263,10)','Rational(1463,10)','Rational(3369,100)')]:
 ps.append(form(label+'-R-phase',a,b,target,'Tuple('+r+','+phasekey+')',644))
 ps+=extrema(label,r,'x',r,'-('+r+')',644)
 for suffix,expr,key in [('maximum-x',maxx,kmax),('minimum-x',minx,kmin)]:
  p=value(label+'-'+suffix,expr,key,644,[RFORM,RANGE],'Recover the original argument from the unit sine/cosine extremum. The question gives no interval; the printed positive-cycle representative is one valid answer,with all coterminal arguments also valid.',1 if label=='b'else None);p['attaining_angle_convention']='Degree source working; positive-cycle representative,not a unique real argument.';ps.append(p)
  arg='('+expr+')*pi/180';original=f'({a})*sin(x)+({b})*cos(x)';expected=r if suffix=='maximum-x'else'-('+r+')'
  extra(p,'original-at-attainment','('+original+').subs(x,'+arg+')',expected);extra(p,'original-stationary-attainment','diff('+original+',x).subs(x,'+arg+')','0')
add('Try-Now',23,476,'Two requested R-forms and extremum arguments: √3sinx+cosx has ±2 at60/240degrees;3cosx−2sinx has ±√13 at326.3/146.3. No explicit angle interval; retain coterminal alternatives.',ps)
for kind,n,page,a,b,target,r,phasekey,kp,offset,keys in [('Example',24,476,'3','4','sin-plus','5','Rational(5313,100)',476,'2',[('5','-5'),('7','-3'),('27','2'),('127','-123')]),('Try-Now',24,477,'5','-12','sin-minus','13','Rational(6738,100)',644,'-3',[('13','-13'),('10','-16'),('166','-3'),('2194','-2200')])]:
 ps=[form('R-phase',a,b,target,'Tuple('+r+','+phasekey+')',kp)]
 for label,poly,(maxk,mink)in zip(['a','b','c','d'],['x','x+('+offset+')','x**2+('+offset+')','x**3+('+offset+')'],keys):ps+=extrema(label,r,poly,maxk,mink,kp)
 row=add(kind,n,page,f'Original {a}sinθ+({b})cosθ has attainable inner interval[−{r},{r}]. Find maximum/minimum of the original inner value,its shift by{offset},its square shifted by{offset},and its cube shifted by{offset}. Square minimum requires inner0; do not substitute the negative endpoint blindly.',ps)
 row['original_domain']='All real θ; source degree phase convention. No angles attaining the extrema requested.'
p=form('a-R-phase','-12','5','cos-plus','Tuple(13,Rational(6738,100))',477)
q=value('b-greatest-value','7+sqrt(5**2+12**2)','20',477,[RFORM,RANGE],'The ORIGINAL half-angle linear combination has amplitude13 and full real input,so shifted maximum is7+13. The half-angle changes the attaining argument,not the amplitude.')
r=value('b-smallest-positive-phi','2*(360-180*atan(Rational(12,5))/pi)','Rational(5852,10)',477,[RFORM,RANGE],'For the ORIGINAL expression7+5cos(φ/2)−12sin(φ/2),maximum requires φ/2+α=360n degrees. α=atan(12/5) is acute. n0 yields negativeφ; n1 is the least positiveφ,approximately585.2397degrees. Period is720degrees,so an invented0..360window would lose it.',1)
r.update(attainment_period='720degrees',least_positive_proof='All maximizers φ=720n−2α. Since0<α<90degrees,n=0 gives negative and n=1 gives the smallest positive.');arg='2*(2*pi-atan(Rational(12,5)))';extra(r,'original-half-angle-maximum',f'(7+5*cos(x/2)-12*sin(x/2)).subs(x,{arg})','20');extra(r,'original-half-angle-derivative',f'diff(7+5*cos(x/2)-12*sin(x/2),x).subs(x,{arg})','0')
add('Example',25,477,'R-form5cosθ−12sinθ=13cos(θ+α),phase67.38°2dp; greatest7+5cos(φ/2)−12sin(φ/2)is20,first positiveattainingφ585.2degrees. Actual half-angle period720degrees is retained.',[p,q,r])
p=form('a-R-phase','-3','5','cos-plus','Tuple(sqrt(34),Rational(3096,100))',644)
q=value('b-smallest-value','-sqrt(15**2+9**2)','-3*sqrt(34)',644,[RFORM,RANGE],'The ORIGINAL requested expression is THREE times the part(a)linear combination. Its minimum is negative norm√(15²+9²)=3√34,not just the unscaled part(a)amplitude.')
add('Try-Now',25,477,'R-form5cosθ−3sinθhas√34/phase30.96°2dp; requested15cosθ−9sinθis triple the original expression and has minimum−3√34.',[p,q])
refs=[(110,476,'Example24 coefficient comparison','3sinθ+4cosθ givesR5/acutephaseatan4/3; exact phase used internally.',RFORM,'table','Example:24'),(111,476,'Example24a maximum comparison','Inneru attains5 whenunit sine1.',RANGE,'table','Example:24'),(112,476,'Example24a minimum comparison','Inneru attains−5 whenunit sine−1.',RANGE,'table','Example:24'),(113,476,'Example24b shifted maximum','u+2 reaches7.',RANGE,'table','Example:24'),(114,476,'Example24b shifted minimum','u+2 reaches−3.',RANGE,'table','Example:24'),(115,476,'Example24c square minimum caution','Minimum ofu²+2is2 atinner0,not atinner−5.',RANGE,'table','Example:24'),(116,476,'Example24c squared maximum','u²+2 reaches27 at eitherinner+5or−5; source shows a valid+5attainment.',RANGE,'table','Example:24'),(117,476,'Example24c squared minimum','u0gives2; fullinnerinterval includes0.',RANGE,'table','Example:24'),(118,476,'Example24d cube monotonicity caution','Oddcube retains the ordering ofinneru,includingnegativevalues.',RANGE,'table','Example:24'),(119,476,'Example24d cubed maximum','u³+2 reaches127 atinner5.',RANGE,'table','Example:24'),(120,476,'Example24d cubed minimum','u³+2 reaches−123 atinner−5.',RANGE,'table','Example:24'),(121,477,'Example25 coefficient comparison','Cos-plus form has coefficient5oncosθ and−12onsinθ;norm13.',RFORM,'table','Example:25'),(122,477,'Example25 half-angle maximum working','Inputφ/2 keepsamplitude13 and shiftsmaximumto20; leastpositiveargumentrequiresnextunitcosinecycle.',RANGE,'table','Example:25'),(123,477,'Example25 SOLUTION cosine extrema guide','Unitcosine maxima0/360 andminimum180; originalhalf-angleperiod720. Thisis a solutionguide,not a givendiagram.',RANGE,'graph','Example:25')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Read each actual displayed extrema table and square/cube caution. Independently optimize outerpolynomials on full attainableinterval,check original extremum values/derivatives,and retain the half-angle720degreeperiod.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='EveryTry23,Example24/Try24,Example25/Try25and14solutionpanelsenumerated. Full nonlinear ranges and original half-angle attainment preserved.',scope_screen='No angle interval invented for unrestrictedextrema. R-form coefficients and requested compound outerexpressions within syllabus.')for page in[476,477]]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C10-composite-extrema.json',dict(scope='Complete476–477 original/composite extrema and least-positive half-angle attainment.',items=answers)),('census-YM-C10-composite-extrema.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete476–477page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
