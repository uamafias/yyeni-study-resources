"""YM482–487: original explicit product/quotient derivatives and their geometry.

Fixed-source analysis only. This draft remains unwired until C10 full rebuild ends.
"""
import hashlib,json
import author_YM_C10_opening as o
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
PROD='8227:2020:M2:T4:O02:D01';QUOT='8227:2020:M2:T4:O02:D02';CHAIN='8227:2020:M2:T4:O01:D02';POWER='8227:2020:M1:T8:O02:D01';GRAD='8227:2020:M1:T8:O01:D01';TANG='8227:2020:M1:T8:O03:D01';STAT='8227:2020:M1:T8:O04:D01'
def ev(page):
 name='YM-C11-key-649'if 649<=page<=652 else'YM-C10-key-645'if 645<=page<=648 else'YM-C10-480-source'if page in[482,483]else f'YM-C11-{484+4*((page-484)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts);r['item_id']=r['item_id'].replace(':YM:C10:',':YM:C11:');corrections[-1]['item_id']=r['item_id']
 r.update(mapping_rationale='These original functions are EXPLICIT. Product/quotient/composite derivative and requested gradient/tangent outputs are separated. No implicit/parametric geometric demand is attached. In polynomial products expansion is a valid alternative; the section demonstrates the product method rather than forbidding that alternative. Intermediate coordinates/derivatives used for a tangent are components unless separately requested.',value_level_scope_decisions=[dict(rule_id='8227:QUAL10',status='within',quoted_value=note,reason='Actual powers are integers or square roots of affine expressions. Even-root domains and original rational denominator exclusions are kept; no irrational power scope is inferred.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL10']),precision_angle_check=dict(source='All derivative,gradient,root and line outputs are exact. No angle or numerical rounding is requested.',comparison='Accept algebraically equivalent expanded/factored derivatives on the ORIGINAL domain. Keep all zero factors,finite derivative conditions and the original requested output.'))
 return r

def val(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[],response_format='symbolic',given_representation='text');return p

def deriv(label,fn,key,kp,chain=False,quot=False,domain='All realx.'):
 p=val(label,'diff('+fn+',x)',key,kp,[QUOT if quot else PROD]+([CHAIN]if chain else[]),'Differentiate the separately transcribed ORIGINAL function. Independently check the printed expanded/factored expression by symbolic equivalence; retain the original domain. For polynomial products,expansion then termwise differentiation is a valid alternative to the displayed product-rule route.',[POWER]);p.update(original_function=fn,original_domain=domain);return p

def point_gradient(label,fn,x0,key,kp):
 return val(label,'diff('+fn+',x).subs(x,'+x0+')',key,kp,[GRAD],'Differentiate the ORIGINAL function and evaluate at the specified ORIGINAL abscissa. A finite gradient requires differentiability there; do not replace the requested scalar by an unasked general derivative.',[PROD,CHAIN,POWER])

def tangent(label,fn,x0,key,kp):
 expr='('+fn+').subs(x,'+x0+')+diff('+fn+',x).subs(x,'+x0+')*(x-('+x0+'))'
 p=val(label,expr,key,kp,[TANG],'Independently compute the ORIGINAL ordinate and derivative at the source point,then form y−y0=m(x−x0). For a y-axis intercept,usex0. Check both incidence and slope; incidence alone cannot distinguish a wrong tangent.',[PROD,CHAIN,POWER]);p.update(original_function=fn,original_point_abscissa=x0);extra(p,'line-slope','diff('+key+',x)','diff('+fn+',x).subs(x,'+x0+')');return p
p=deriv('derivative','(7-3*x+x**2)*(2*x**3+1)','10*x**4-24*x**3+42*x**2+2*x-3',483)
add('Example',1,483,'Differentiate explicit polynomial product(7−3x+x²)(2x³+1). Source also expands it first as an explicitly valid alternative; both give10x⁴−24x³+42x²+2x−3.',[p])
data=[('a','(x**2-2*x+6)*(x**3-4)','5*x**4-8*x**3+18*x**2-8*x+8'),('b','(1-2*x)*(x**2-8*x+7)','-6*x**2+34*x-22'),('c','(x**2-4)*(x**2-4)','4*x**3-16*x'),('d','(x**2+3*x+5)*(9*x**2-2*x-6)','36*x**3+75*x**2+66*x-28')]
add('Try-Now',1,484,'Four explicit polynomial product derivatives,including repeated equal factors(x²−4)(x²−4). Expanded answers are accepted; the repeated-factor version can also use a chain-rule square.',[deriv(l,f,k,645)for l,f,k in data])
p=deriv('derivative','(x-3)**2*(x+2)**5','(x-3)*(x+2)**4*(7*x-11)',484,True)
add('Example',2,484,'Differentiate explicit(x−3)²(x+2)⁵ and factor the common powers. Both factors are differentiable for allrealx; no root factor is cancelled away.',[p])
add('Try-Now',2,484,'Differentiate two products of affine powers,retaining both product terms and the inner factors4,2,3,2 respectively.',[deriv('a','(4*x-3)*(2*x+7)**6','12*(4*x-3)*(2*x+7)**5+4*(2*x+7)**6',645,True),deriv('b','(3*x+4)**4*(2*x-1)**5','10*(3*x+4)*(2*x-1)**4+3*(2*x-1)**5',645,True)])
p=answers[-1]['subparts'][1]
p.update(author_expected_normalised='10*(3*x+4)**4*(2*x-1)**4+12*(3*x+4)**3*(2*x-1)**5',source_reading_resolution='Native source484 retains power4 on(3x+4),while native key645 drops that power and differentiates as if the firstfactor were linear. Actual source is preserved; key is wrong.')
extra(p,'original-derivative-at-one','diff((3*x+4)**4*(2*x-1)**5,x).subs(x,1)','28126')
extra(p,'printed-key-at-one','(10*(3*x+4)*(2*x-1)**4+3*(2*x-1)**5).subs(x,1)','73')
p=deriv('derivative','(3-x**2)*sqrt(5*x+4)','(15-25*x**2-16*x)/(2*sqrt(5*x+4))',484,True,domain='Originalx≥−4/5; finite interior derivative forx>−4/5.')
add('Example',3,484,'Differentiate explicit(3−x²)√(5x+4). The square-root factor requiresx≥−4/5,and the finite derivative formula usesx>−4/5. Original endpoint derivative is not silently admitted.',[p])
ps=[deriv('a','(x-1)*sqrt(x+5)','(3*x+9)/(2*sqrt(x+5))',645,True,domain='Originalx≥−5,finite derivativex>−5.'),deriv('b','(3-x**2)*sqrt(5*x+4)','(-25*x**2-16*x+15)/(2*sqrt(5*x+4))',645,True,domain='Originalx≥−4/5,finite derivativex>−4/5.')]
r=add('Try-Now',3,485,'Two explicit radical-product derivatives:(x−1)√(x+5),then the exact(3−x²)√(5x+4)expression already worked inExample3. Preserve the second occurrence without treating its values as a new problem structure.',ps);r['source_interpretation']='Part(b) duplicates Example3 exactly; part(a) has its own affine radical and coefficient calculation.'
p=val('zero-gradient-x','solveset(diff((x+3)**4*(x-5)**7,x),x,domain=S.Reals)','FiniteSet(-3,5,-Rational(1,11))',485,[STAT],'Differentiate the ORIGINAL explicit product,then solve its FACTORED derivative without dividing away(x+3)³or(x−5)⁶. Only x-coordinates are requested; no ordinates or classification is added.',[PROD,CHAIN,POWER]);p['original_function']='(x+3)**4*(x-5)**7'
add('Example',4,485,'Find all x-coordinates where the original explicit(x+3)⁴(x−5)⁷ curve has zero gradient. Preserve all three derivative factors and their roots−3,5,−1/11.',[p])
p=deriv('derivative','(2*x-3)**2*(x+5)**3','(2*x-3)*(x+5)**2*(10*x+11)',645,True)
q=val('zero-derivative-x','solveset(diff((2*x-3)**2*(x+5)**3,x),x,domain=S.Reals)','FiniteSet(Rational(3,2),-5,-Rational(11,10))',645,[STAT],'Solve the independently differentiated ORIGINAL product. Retain zero factors2x−3,x+5,10x+11; requested x-values are3/2,−5,−11/10.',[PROD,CHAIN]);q['depends_on_source_parts']=['derivative']
add('Try-Now-4',1,485,'Explicitly find derivative of(2x−3)²(x+5)³ AND allxwhere it iszero. These are two requested outputs; retain all repeatedfactor roots.',[p,q])
add('Try-Now-4',2,485,'Find only the gradient of(2x+3)⁵(x+2)⁸atx−1. Exact gradient18; a general derivative is supporting working,not an extra askedoutput.',[point_gradient('gradient','(2*x+3)**5*(x+2)**8','-1','18',645)])
p=point_gradient('gradient','x**2*sqrt(x+4)','-3','-Rational(3,2)',645);extra(p,'original-given-point','(x**2*sqrt(x+4)).subs(x,-3)','9')
add('Try-Now-4',3,485,'Find gradient ofx²√(x+4) at ORIGINALpoint(−3,9). Pointliesonthecurve and interiorradicaldomain; exactgradient−3/2.',[p])
p=val('zero-gradient-x','solveset(diff((x-5)*sqrt(2*x-1),x),x,domain=Interval.open(Rational(1,2),oo))','FiniteSet(2)',645,[STAT],'Use the ORIGINAL radicaldomainx≥1/2,and finite derivativeinteriorx>1/2. Derivative3(x−2)/√(2x−1)vanishesonlyat2;endpoint1/2isnot a finite zero gradient.',[PROD,CHAIN,POWER])
add('Try-Now-4',4,485,'Findx-coordinate where explicit(x−5)√(2x−1)hasgradient0. The validinteriorroot2 is retained; originalradicalendpoint1/2 is not differentiable.',[p])
p=val('gradient-minus-five-x','solveset(diff((x-2)**2*(3*x+1),x)+5,x,domain=S.Reals)','FiniteSet(1,Rational(13,9))',645,[GRAD],'Differentiate the ORIGINAL function and setitsgradient to−5,not0. Solve9x²−22x+13=0; bothx1and13/9 valid.',[PROD,CHAIN,POWER])
add('Try-Now-4',5,486,'For originalf(x)=(x−2)²(3x+1),find allxwheregradientis−5. This is a prescribed nonzero gradient,not a stationarypoint request.',[p])
add('Example',5,486,'Find tangent to explicit(x+1)⁴(2−x)³atx1. Originalpoint(1,16),gradient−16,correcttangenty−16x+32; negativeinnerderivativekept.',[tangent('tangent','(x+1)**4*(2-x)**3','1','-16*x+32',486)])
add('Try-Now-5',1,486,'Find tangent to explicit(8−x²)(1+x+x²)atx−2. Originalpoint(−2,12),gradient0,horizontal liney12; this does not ask for stationarypoint classification.',[tangent('tangent','(8-x**2)*(1+x+x**2)','-2','12',645)])
add('Try-Now-5',2,486,'Find tangent to explicit(x+2)(x−1)³atits y-axisintercept. Usex0,ordinate−2 andgradient5; liney5x−2.',[tangent('tangent','(x+2)*(x-1)**3','0','5*x-2',645)])
add('Try-Now-5',3,486,'Find gradient of explicit(1+12√x)(4−x²)atx9. Retainradicalinteriordomainx>0; exactgradient−820.',[point_gradient('gradient','(1+12*sqrt(x))*(4-x**2)','9','-820',645)])
p=deriv('derivative','(2*x**3-1)/(3*x+1)','(12*x**3+6*x**2+3)/(3*x+1)**2',487,quot=True,domain='Originalx≠−1/3; derivative formula keeps that excluded pole.')
r=add('Example',6,487,'Differentiate ORIGINALquotient(2x³−1)/(3x+1). Keep denominatornonzero and quotient-order sign; derivative(12x³+6x²+3)/(3x+1)².',[p])
corrections[-1]['continuation_pdf_pages']=[488]
refs=[(1,483,'Product-rule general panel','d(uv)/dx=u dv/dx+v du/dx; both factors dependonx.',PROD,'table','Example:1'),(2,483,'Product-rule mnemonic','First function times derivativeofsecond PLUS second times derivativeoffirst; do not multiplythe derivatives.',PROD,'table',None),(3,483,'Example1 product-rule working','Original factors7−3x+x² and2x³+1; expanded derivative10x⁴−24x³+42x²+2x−3.',PROD,'table','Example:1'),(4,483,'Example1 alternate expansion working','Originalproductexpands2x⁵−6x⁴+14x³+x²−3x+7;termwise derivative agrees. Expansion is allowed.',POWER,'table','Example:1'),(5,484,'Example2 product-plus-chain working','Retain both derivative terms thenfactor(x−3)(x+2)⁴(7x−11).',PROD,'table','Example:2'),(6,484,'Example3 radical-product working','Inside5x+4 contributeschainfactor5; common denominator2√(5x+4) retainsoriginalinteriordomain.',CHAIN,'table','Example:3'),(7,485,'Example4 factored zero-gradient working','Derivative(x+3)³(x−5)⁶(11x+1)has allthreezeros−3,5,−1/11; divisionwouldloseroots.',STAT,'table','Example:4'),(8,486,'Example5 tangent ordinate step','Sourcex1givesordinate16;this is intermediateworkingfor the requestedline.',TANG,'table','Example:5'),(9,486,'Example5 product-chain derivative working','Negativeinnerderivativeof2−x yieldsgradient−16atx1.',PROD,'table','Example:5'),(10,486,'Example5 tangent equation working','Useoriginalpoint(1,16)andgradient−16;liney−16x+32.',TANG,'table','Example:5'),(11,487,'Quotient-rule general panel','d(u/v)/dx=(v du/dx−u dv/dx)/v²;originalvnonzero.',QUOT,'table','Example:6'),(12,487,'Quotient-rule mnemonic','Denominator times derivativeofnumerator MINUS numerator times derivativeofdenominator,overdenominatorsquared.',QUOT,'table',None),(13,487,'Example6 quotient derivative working','Originaldenominator3x+1;retainsquared denominatorandcorrectsubtraction to get12x³+6x²+3.',QUOT,'table','Example:6')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C11:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C11:'+parent if parent else None);figures[-1]['mathematical_feature_review']['method']='Read each original explicit function,product/quotient sign,chainfactor,radicaldomain and requestedgradient/lineoutput. Independently recompute symbolic derivatives,all zero factors,and tangent incidence ANDslope. These are workedsolutionpanels,not givendiagrams.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=11,page_status='prose only'if page==482 else'items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C11:Try-Now-4:5']if page==486 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='Title/scope/biography482hasno mathematicaltask. AllExamples1–6,Try1–3,Try4Q1–5,Try5Q1–3and13actual product/quotient/solutionpanelsenumerated. Try4Q5continuesontopof486.',scope_screen='ExplicitcurvesdoNOTassessimplicit/parametricgeometry. Rationalpowers,originalradicaldomains,denominatorpolesandaskedoutputsretained.')for page in range(482,488)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C11-opening.json',dict(scope='Complete482–487explicit product/quotient opening.',items=answers)),('census-YM-C11-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=11,source_path=SRC,source_sha256=SHA,scope='Complete482–487page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
