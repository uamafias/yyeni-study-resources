"""YM488–490: quotient derivatives, real radical branches and complete coordinates."""
import json
import author_YM_C11_opening as a
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
import author_YM_C9_opening as g
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=a.ev;h.common.base.ev=ev
PROD=a.PROD;QUOT=a.QUOT;CHAIN=a.CHAIN;GRAD=a.GRAD;TANG=a.TANG;STAT=a.STAT
add=a.add;val=a.val

def deriv(label,fn,key,kp,chain=False,domain='Original denominator nonzero.'):
 return a.deriv(label,fn,key,kp,chain=chain,quot=True,domain=domain)
add('Try-Now',6,488,'Differentiate three original rational functions3x/(4x−6),(2x+5)/(3x−4),(x²−3)/(2x−1),retaining their separate poles3/2,4/3,1/2.',[deriv('a','3*x/(4*x-6)','-9/(2*(2*x-3))',645),deriv('b','(2*x+5)/(3*x-4)','-23/(3*x-4)**2',645),deriv('c','(x**2-3)/(2*x-1)','(2*x**2-2*x+6)/(2*x-1)**2',645)])
p=answers[-1]['subparts'][0]
p.update(author_expected_normalised='-9/(2*(2*x-3)**2)',source_reading_resolution='Native key645 omits the SQUARE on(2x−3). Original rationalderivative requires it; the positive/negativecomponent derivative sign is alwaysnegative.')
extra(p,'original-derivative-at-zero','diff(3*x/(4*x-6),x).subs(x,0)','-Rational(1,2)')
extra(p,'printed-key-at-zero','(-9/(2*(2*x-3))).subs(x,0)','Rational(3,2)')
p=deriv('ds-dt','(8*x**3+1)/(5*x**3-2*x-6)','(-32*x**3-159*x**2+2)/(5*x**3-2*x-6)**2',488);p['source_variable_mapping']='Checkerx denotes ORIGINALt; required notationds/dt,not a different source variable.'
add('Example',7,488,'Differentiate s=(8t³+1)/(5t³−2t−6)WITHRESPECTTOt. Leading t⁵quotient terms cancel; retain the original denominatorpoles andds/dtnotation.',[p])
ps=[]
for label,fn,key in [('a','(7*x**2-3)/(x**3-4*x**2+5)','(-7*x**4+9*x**2+46*x)/(x**3-4*x**2+5)**2'),('b','(x**2+2*x+1)/(3*x-4)','(3*x**2-8*x-11)/(3*x-4)**2')]:
 p=deriv(label,fn,key,645);p['source_variable_mapping']='Checkerx denotes ORIGINALt; response isds/dt.';ps.append(p)
add('Try-Now',7,489,'Differentiate two original s(t)quotients: (7t²−3)/(t³−4t²+5)and(t²+2t+1)/(3t−4). Retain quotient subtraction and originalvariablet.',ps)
p=deriv('derivative','(2-x**2)/sqrt(x**2-3)','(-x**3+4*x)/(x**2-3)**Rational(3,2)',489,True,'Original denominator√(x²−3)requiresx²>3,sox<−√3orx>√3. Both components valid.')
add('Example',8,489,'Differentiate original(2−x²)/√(x²−3). Denominatorradicalrequiresx²>3; both positive and negativeouter components remain. Sourcefactored andsinglefraction forms equivalent there.',[p])
ps=[deriv('a','(x-2)/sqrt(2*x+3)','(x+5)/(2*x+3)**Rational(3,2)',646,True,'Original denominator2x+3>0; x>−3/2.')]
p=reasoning('b','(8x−16)/(3∛((2x−5)^4)),validfor allrealxexcept5/2.','Use the REAL cube root in ORIGINAL(2x−7)/∛(2x−5). Onu=2x−5>0 useu^(1/3); on u<0use−(−u)^(1/3),then differentiate each. Both simplify to(8x−16)/(3|2x−5|^(4/3)). The native key uses∛((2x−5)^4),which is positive on either component and therefore correct; principal complex powers would give a false defect.',646,'matches');p.update(assessed_8227_demand_ids=[QUOT,CHAIN],component_demand_ids=[a.POWER],response_format='symbolic',original_function='(2x−7)/realcuberoot(2x−5)',original_domain='Allrealxexcept5/2.')
extra(p,'positive-component-derivative','simplify(diff((2*x-7)/(2*x-5)**Rational(1,3),x)-(8*x-16)/(3*(2*x-5)**Rational(4,3)))','0');extra(p,'negative-component-derivative','simplify(diff(-(2*x-7)/(5-2*x)**Rational(1,3),x)-(8*x-16)/(3*(5-2*x)**Rational(4,3)))','0');extra(p,'real-negative-point','diff(-(2*x-7)/(5-2*x)**Rational(1,3),x).subs(x,1)','-8/(3*3**Rational(4,3))');ps.append(p)
p=reasoning('c','Derivative(−6x²−3x−14)/((3x²−7)²√((4x+1)/(3x²−7)))on both differentiable realcomponents.','ORIGINALsourcehasONEsquare root around theWHOLE quotient(4x+1)/(3x²−7). Its realdomain is(−√(7/3),−1/4]union(√(7/3),∞);finite derivativeusesopenfirstendpoint−1/4. Differentiate as a compositionWITHOUTsplitting the root over numerator/denominator. Native key instead splits to√(4x+1)√((3x²−7)^3),which is not a real expression on the valid negativecomponent. It is correct only on the positivecomponent; the missing negativecomponent is explicit.',646,'key incomplete');p.update(assessed_8227_demand_ids=[QUOT,CHAIN],component_demand_ids=[a.POWER],response_format='symbolic',original_function='sqrt((4*x+1)/(3*x**2-7))',printed_key_expression='(-6*x**2-3*x-14)/(sqrt(4*x+1)*sqrt((3*x**2-7)**3))',original_domain='(−√(7/3),−1/4]union(√(7/3),∞);finite derivative excludes−1/4.',source_domain_caution='Splitting a real quotientroot removes the valid both-negative numerator/denominator interval.')
extra(p,'global-original-derivative','simplify(diff(sqrt((4*x+1)/(3*x**2-7)),x)-(-6*x**2-3*x-14)/((3*x**2-7)**2*sqrt((4*x+1)/(3*x**2-7))))','0');extra(p,'original-valid-negative-point','diff(sqrt((4*x+1)/(3*x**2-7)),x).subs(x,-1)','-17/(8*sqrt(3))');extra(p,'original-valid-negative-radicand','((4*x+1)/(3*x**2-7)).subs(x,-1)','Rational(3,4)');ps.append(p)
ps.append(deriv('d','(1-2*x**2)/(4+x)**2','-2*(8*x+1)/(4+x)**3',646,True,'Originalx≠−4.'))
add('Try-Now',8,489,'Four original quotient derivatives: affineover√(2x+3),affineoverREAL∛(2x−5),WHOLE√((4x+1)/(3x²−7)),and(1−2x²)/(4+x)². Cube-root key is valid on bothcomponents; split-square-root key loses a valid negativecomponent.',ps)
p=val('stationary-x','solveset(diff(4*x**2/(x+1),x),x,domain=Complement(S.Reals,FiniteSet(-1)))','FiniteSet(0,-2)',490,[STAT],'Differentiate the ORIGINAL explicit rationalcurve,retainx≠−1,thenfactor4x(x+2). Requested x-coordinates0,−2 only; no ordinates/nature asked.',[QUOT])
add('Example',9,490,'Find x-coordinates of stationarypoints of4x²/(x+1). Originalpole−1excluded;roots0,−2. Explicit function has no implicit/parametric demand.',[p])
p=val('stationary-x','solveset(diff((x**2-2*x+1)/(x-3),x),x,domain=Complement(S.Reals,FiniteSet(3)))','FiniteSet(1,5)',646,[STAT],'Differentiate ORIGINAL(x²−2x+1)/(x−3),factor numeratorx²−6x+5,and keep originalx≠3. Requested x-values1,5 only.',[QUOT])
add('Try-Now-9',1,490,'Find x-coordinates of stationarypoints of ORIGINAL(x²−2x+1)/(x−3),explicitlyx≠3. Correct1,5; no coordinates/nature extension invented.',[p])
p=reasoning('gradient-minus-four-coordinates','Points(3,−5)and(7,11).','The ORIGINAL curve(3x+1)/(x−5)has derivative−16/(x−5)². Set equalto−4,obtainx3or7,and then evaluate BOTH original ordinates−5and11because the source asksCOORDINATES. Nativekey stops atx7or3;thoseabscissasarevalid but omit requestedordinates.',646,'key incomplete');p.update(assessed_8227_demand_ids=[GRAD],component_demand_ids=[QUOT],response_format='symbolic',printed_key_partial_answer='x7or3; no ordinates.',original_function='(3*x+1)/(x-5)')
extra(p,'original-gradient-abscissas','solveset(diff((3*x+1)/(x-5),x)+4,x,domain=Complement(S.Reals,FiniteSet(5)))','FiniteSet(3,7)');extra(p,'original-point-ordinates','Tuple(((3*x+1)/(x-5)).subs(x,3),((3*x+1)/(x-5)).subs(x,7))','Tuple(-5,11)')
add('Try-Now-9',2,490,'Find COORDINATESon original(3x+1)/(x−5)wheregradient−4. Completeanswer(3,−5),(7,11);key suppliesonly thecorrectx-values3,7.',[p])
p=val('gradient','diff((x-1)/(x+1),x).subs(x,4)','Rational(2,25)',646,[GRAD],'Independently differentiate ORIGINAL quotient and evaluate atx4; originalpole−1irrelevantto this admissiblepoint.',[QUOT])
add('Try-Now-9',3,490,'Find derivativeVALUEof(x−1)/(x+1)atx4,exact2/25. An unasked generalfunction doesnot replace the scalaroutput.',[p])
p=val('tangent','((x-1)/(x+1)).subs(x,1)+diff((x-1)/(x+1),x).subs(x,1)*(x-1)','(x-1)/2',646,[TANG],'ORIGINALpoint(1,0)andfinitegradient1/2givey=(x−1)/2; check incidenceandslope.',[QUOT])
add('Try-Now-9',4,490,'Find tangent to ORIGINAL(x−1)/(x+1)atx1. Exactliney(x−1)/2.',[p])
p=val('normal','-1/(diff((x-2)/(2*x+1),x).subs(x,2))*(x-2)','-5*x+10',646,[TANG],'ORIGINALx-axisinterceptx2givespoint(2,0),tangentgradient1/5nonzero,andnormalgradient−5. Formnormal−5(x−2),not tangent(1/5)(x−2).',[QUOT])
extra(p,'original-intercept','((x-2)/(2*x+1)).subs(x,2)','0');extra(p,'perpendicular-gradients','diff(-5*x+10,x)*diff((x-2)/(2*x+1),x).subs(x,2)','-1')
add('Try-Now-9',5,490,'Find NORMALto original(x−2)/(2x+1)where itcutsx-axis. Solveinterceptx2,then usefinite nonzerotangentgradient1/5;normaly−5x+10.',[p])
refs=[(14,488,'Example6 alternate product-plus-chain route','Originalquotient becomes(2x³−1)(3x+1)^−1 onx≠−1/3; same derivative,valid alternative.',PROD,'Example:6'),(15,488,'Example7 variable-t quotient working','Correct24t²/15t²−2derivatives; t⁵termscancel,retaining−32t³−159t²+2.',QUOT,'Example:7'),(16,489,'Example8 radical quotient working','Originalradicaldenominator requiresx²>3; chainfactor2xkept.',CHAIN,'Example:8'),(17,489,'Example8 fractional simplification panel','Combine fractions without multiplying byzerooriginalradical; final(−x³+4x)/(x²−3)^(3/2)validon bothcomponents.',QUOT,'Example:8'),(18,490,'Example9 rational derivative panel','Original4x²/(x+1)gives(4x²+8x)/(x+1)²withpole−1excluded.',QUOT,'Example:9'),(19,490,'Example9 stationary-root factoring','4x(x+2)=0 yields0,−2;not the pole−1. Onlyxasked.',STAT,'Example:9')]
for n,page,label,note,d,parent in refs:
 fig(n,page,label,note,[d],'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C11:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C11:'+parent);figures[-1]['mathematical_feature_review']['method']='Read original numerator/denominator,root grouping,source variable and exact requestedoutputs. Independentlycheck rational derivatives and originalreal-domainbranches; do not split square roots across a both-negative quotient.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=11,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C11:Example:6']if page==488 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry6,Example7/Try7,Example8/Try8,Example9/Try9Q1–5and sixactual solutionpanelsenumerated. Example6alternateworkingcontinues488;distinctsourceoccurrencepreserved.',scope_screen='Allcurvesexplicit. Realcube roots retainnegativecomponent; wholesquare-rootquotient has a validboth-negativecomponent thatthekey omits. Originalrationalpolesandaskedordinateskept.')for page in range(488,491)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C11-quotients.json',dict(scope='Complete488–490explicitquotientderivativesandgeometry.',items=answers)),('census-YM-C11-quotients.json',dict(book='YM',book_id='8227-SRC-017',chapter=11,source_path=SRC,source_sha256=SHA,scope='Complete488–490page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
