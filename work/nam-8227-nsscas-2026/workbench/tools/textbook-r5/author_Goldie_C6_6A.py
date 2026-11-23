"""All fixed-source6Aparts;actual decimal/bisection traces use original signs."""
import json,hashlib
from fractions import Fraction
from decimal import Decimal,localcontext,ROUND_HALF_UP
import sympy as sp
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';STOP='8227:2020:M2:T6:O04:D02';STATIONARY='8227:2020:M1:T8:O04:D01';SKETCH='8227:2020:M1:T3:O05:D01'
ELEMENTARY='8227:2020:M2:T4:O01:D01';POWER='8227:2020:M1:T8:O02:D01'
def ev(page):
 name='Goldie-C6-162'if page<347 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def fraction_round(z,dp):
 with localcontext()as context:
  context.prec=80
  return str((Decimal(z.numerator)/Decimal(z.denominator)).quantize(Decimal(1).scaleb(-dp),rounding=ROUND_HALF_UP))

def localise(source,lower,upper,dp,method):
 F=expression(source);x=expression('x');lo,hi=Fraction(lower),Fraction(upper);trials=[];levels=0
 def sign(z):
  q=sp.simplify(F.subs(x,sp.Rational(z.numerator,z.denominator)))
  if q==0:return 0
  number=sp.N(q,65);assert number.is_real
  return 1 if number>0 else -1
 fa,fb=sign(lo),sign(hi);assert fa*fb<0
 while fraction_round(lo,dp)!=fraction_round(hi,dp):
  levels+=1;assert levels<200
  if method=='bisection':
   mid=(lo+hi)/2;fm=sign(mid);trials.append({'point':str(mid),'sign':fm})
   if fm==0:lo=hi=mid;break
   if fa*fm<0:hi=mid;fb=fm
   else:lo=mid;fa=fm
  else:
   assert method=='decimal';step=(hi-lo)/10;previous=lo;previous_sign=fa
   for j in range(1,11):
    q=lo+j*step;fq=sign(q);trials.append({'point':str(q),'sign':fq})
    if fq==0:lo=hi=q;break
    if previous_sign*fq<0:lo,hi=previous,q;fa,fb=previous_sign,fq;break
    previous,previous_sign=q,fq
   else:raise AssertionError('decimal sign bracket lost')
  if lo==hi:break
 return {'method':method,'original_equation':source,'initial_interval':[str(lower),str(upper)],'trials':trials,'levels':levels,
  'final_interval':[str(lo),str(hi)],'midpoint':str((lo+hi)/2),'half_width':str((hi-lo)/2),'rounded_result':fraction_round((lo+hi)/2,dp),
  'stopping_basis':'Both unrounded rational endpoints round to the same requested decimal value,or the exact root was hit. No internal rounded sign decisions.'}
answers=[]
def add(n,page,note,parts,direct,components=None,sketch=False):
 for p in parts:
  kp=p.pop('key_page_override',347);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 347),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[347,348])
 row={'item_id':f'8227:TB:Goldie:C6:Exercise-6A:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Map the requested graph/root count,sign bracket or explicit stationary-point argument. Decimal/bisection procedures requested by this book are supporting algorithm branches;they do not invent a new prescribed8227method. A pole cannot serve as a root.',
  'representation':'graph'if n==7 else'text','sketch_response_required':sketch,'exam_style':False,'exam_style_basis':'Ordinary Exercise6Awithout examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT08','status':'not applicable','quoted_value':note,'reason':'Sign-search localisation,not a formal fixed-point derivative convergence condition.'}],
  'precision_angle_check':{'source':'Q1/3/7ask3decimal places;Q2/4/5/6ask2decimal places. Q6(iv)asks an explicit error-interval form. No trig angles.',
   'comparison':'Independent reference roots come from the original continuous equation;where a particular algorithm is requested,its actual trial trace is also retained. No finite search proves root completeness without the separate graph/monotonicity argument.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row

def root(label,f,a,b,key,dp=2,kp=347,method=None):
 p=value(label,'0',key,kp,'Independently localise the original continuous equation in the stated sign bracket;round only the reference result. The key is not a computation input. Use the source-specific graph argument for completeness.')
 p['operation']={'kind':'bracketed-source-root','operands':[f,str(a),str(b)],'rounding':{'decimal_places':dp}}
 if method:
  trace=localise(f,a,b,dp,method);assert sp.Rational(trace['rounded_result'])==expression(key)
  p['requested_method_trace']=trace
 return p
p=reasoning('i','There are no stationary points because f′=3x²+3>0for all real x.',
 'Differentiate the original cubic. Sincex²≥0,the derivative is at least3and cannot vanish. This proves strict increase and excludes turning points.',347,'show/prove')
p['additional_operations']={'derivative':{'kind':'identity','operands':['diff(x**3+3*x-5,x)']}};p['additional_operation_expected']={'derivative':'3*x**2+3'}
p2=reasoning('ii','Sketch an increasing cubic through(0,−5),with one positive crossing and opposite infinite tails.',
 'Strict increase proves at most one root;the cubic tails prove at least one. Sincef(0)=−5andf(2)=9,the crossing is positive. The source graph agrees;no extra stationary shape should be drawn.',347,'sketch')
add(1,164,'Forx³+3x−5=0:show no stationary points,use a sketch to justify exactly one positive root,and calculate it to3dp.',[p,p2,root('iii','x**3+3*x-5',1,2,'1.154',3)],[STATIONARY,ROOTG,BRACKET],[POWER],True)
p=reasoning('i','There are two real roots.',
 'Forf=e^x−3x,the derivative e^x−3vanishes onlyatln3. The strictly convex function has positive tails and minimum3−3ln3<0,so it crosses twice. It is positive forx≤0,so both roots are positive.',347,'matches')
p2=value('ii','Tuple(Tuple(0,1),Tuple(1,2))','Tuple(Tuple(0,1),Tuple(1,2))',347,'The original endpoint signs arepositive,negative,positive at0,1,2. Continuity gives one root in each interval;the separate count argument shows there are no additional roots.')
p2['assertions']=[{'expression':'Tuple(sign(exp(0)-3*0),sign(exp(1)-3),sign(exp(2)-6))','expected':'Tuple(1,-1,1)'}]
add(2,164,'Fore^x−3x=0,determine the root count,find unit sign brackets,and compute both roots to2dp.',[p,p2,root('iii-lower','exp(x)-3*x',0,1,'0.62'),root('iii-upper','exp(x)-3*x',1,2,'1.51')],[ROOTG,BRACKET],[ELEMENTARY])
p=reasoning('i','Sketch increasing convexy=2^xandliney=x+2on shared axes,showing two intersections,one negative and the exact positive one(2,4).',
 'The line crosses thex-axis at−2and the exponential is always positive. The continuous difference is positive at−2,negative at−1,and zero at2. Convexity and a unique derivative-zero point bound the root count by two.',347,'sketch')
p2=reasoning('ii','The equation has two real roots.',
 'For2^x−x−2,the derivative ln2·2^x−1is strictly increasing and has one zero. Both tails are positive whilef(0)=−1. Therefore two and only two crossings occur;the graph and sign intervals agree.',347,'matches')
add(3,164,'Sketchy=2^xandy=x+2,deduce the two-root count,and find both roots to3dpwhere appropriate. The positive root2is exact.',[p,p2,root('iii-negative','2**x-x-2',-2,-1,'-1.690',3),root('iii-positive','2**x-x-2',1,2,'2',3)],[ROOTG,BRACKET],sketch=True)
parts=[root(label,'x**3-3*x+1',a,b,key)for label,a,b,key in [('negative',-2,-1,'-1.88'),('middle',0,1,'0.35'),('positive',1,2,'1.53')]]
for p in parts:p['completeness_argument']='A cubic has at most3real roots;the three disjoint sign brackets give3distinct roots. No extra real root can occur.'
add(4,164,'Find every real root ofx³−3x+1to2dp. Three disjoint continuous sign brackets establish the full real set.',parts,[BRACKET])
parts=[]
for method in ['decimal','bisection']:
 for label,a,b,key in [('negative',-2,-1,'-1.62'),('positive',1,2,'1.28')]:parts.append(root(f'i-{method}-{label}','x**5-5*x+3',a,b,key,method=method))
p=reasoning('ii','Both methods work;their trial cost and convenience differ. Bisection steadily halves a valid interval,while decimal search aligns trials with requested digits.',
 'The explicit traces count actual function evaluations for both outer roots under a declared stopping criterion. Neither rounded display digits nor a generic statement that one method is always best establishes accuracy. Keep source-specific ease/efficiency as discussion rather than an additional numeric answer key.',None,'no key')
p['comparison_counts']=[{'label':q['subpart'],'evaluations':len(q['requested_method_trace']['trials'])}for q in parts];parts.append(p)
add(5,165,'Find the two outer quintic roots on[−2,−1]and[1,2]to2dpby both decimal search and interval bisection;comment on ease/efficiency. Actual method traces are preserved,not inferred from final roots.',parts,[BRACKET])
f='x**3-4*x**2-3*x+8'
p=reasoning('i','The unit intervals are[−2,−1],[1,2],[4,5].',
 'Starting at−2,the original integer-node values through5are−10,6,8,2,−6,−10,−4,18. These give three disjoint sign changes. A cubic has at most three roots,so the set is complete.',347,'matches')
p['additional_operations']={'systematic_values':{'kind':'identity','operands':['Tuple('+','.join(f'({f}).subs(x,{j})'for j in range(-2,6))+')']}}
p['additional_operation_expected']={'systematic_values':'Tuple(-10,6,8,2,-6,-10,-4,18)'}
p2=reasoning('ii','Sketch cubic through(0,8),with local maximum(−1/3,230/27),local minimum(3,−10),three crossings in the identified intervals and cubic tails.',
 'f′=3x²−8x−3=(3x+1)(x−3). Its sign changes positive/negative/positive,so the two labelled extrema and three crossings follow. The source graph supplies the same qualitative shape.',347,'sketch')
p2['additional_operations']={'extremal_values':{'kind':'identity','operands':['Tuple((x**3-4*x**2-3*x+8).subs(x,-1/3),(x**3-4*x**2-3*x+8).subs(x,3))']}}
p2['additional_operation_expected']={'extremal_values':'Tuple(230/27,-10)'}
parts=[p,p2]+[root(label,f,a,b,key,method='bisection')for label,a,b,key in [('iii-negative',-2,-1,'-1.51'),('iii-middle',1,2,'1.24'),('iii-positive',4,5,'4.26')]]
p=reasoning('iv','For each saved final bisection interval,report its exact midpointaandhalf-width(½)^n. Different valid stopping intervals can give differenta,n.',
 'From an initial unit interval,afterkhalvings the midpoint error is at most2^(−k−1),so n=k+1. The source listed midpoint/exponent pairs are examples,not unique outputs:their exact midpoint values are−1.51171875,1.244384765625,4.2626953125with n8,12,10;printed later midpoint digits are rounded. Independently test the original polynomial signs at both endpoints rather than comparing another valid trace’snwith these fixed examples.',347,'matches')
p['own_trace_error_forms']=[{'subpart':q['subpart'],'a':q['requested_method_trace']['midpoint'],'half_width':q['requested_method_trace']['half_width'],'n':Fraction(q['requested_method_trace']['half_width']).denominator.bit_length()-1}for q in parts[2:]]
p['additional_operations']={}
p['additional_operation_expected']={}
for label,a,n in [('negative','-1.51171875',8),('middle','1.244384765625',12),('positive','4.2626953125',10)]:
 op={'kind':'identity','operands':[f'Tuple(sign(({f}).subs(x,({a})-2**(-{n}))),sign(({f}).subs(x,({a})+2**(-{n}))))']}
 p['additional_operations']['source_bracket_'+label]=op
 p['additional_operation_expected']['source_bracket_'+label]='Tuple(-1,1)'if label!='middle'else'Tuple(1,-1)'
parts.append(p)
add(6,165,'Systematically search integer nodes from−2for the three cubic roots,sketch,find each to2dpby bisection,and express the saved intervals as a±(½)^n. Midpoints are approximations,not the true roots.',parts,[ROOTG,BRACKET],sketch=True)
p=reasoning('i','There are unit sign brackets[1,2]and[4,5].',
 'Forx≤0,e^x−x³>0. Forx>0,the equivalent equation isx−3lnx=0;its unique minimum at3is negative and both tails are positive,so there are exactly two roots. Original values change sign across1/2and4/5.',347,'matches')
p['additional_operations']={'integer_signs':{'kind':'identity','operands':['Tuple(sign(exp(1)-1),sign(exp(2)-8),sign(exp(4)-64),sign(exp(5)-125))']}}
p['additional_operation_expected']={'integer_signs':'Tuple(1,-1,-1,1)'}
add(7,165,'Use the given unscaled graph ofe^x−x³to locate unit sign brackets for each root,then calculate both to3dp. Despite its two extrema and left-tail wiggle,the graph has only two real crossings.',[p,root('ii-lower','exp(x)-x**3',1,2,'1.857',3),root('ii-upper','exp(x)-x**3',4,5,'4.536',3)],[ROOTG,BRACKET])
# Every requested graph/root/failure subpart of8is explicit.
parts=[]
for label,formula,features,roots_text,behaviour,kp in [
 ('i','1/x','Two reciprocal branches,vertical asymptote0,horizontal asymptote0,no x-intercept.','No roots.','The initial interval[−0.3,0.7]crosses the pole0. Opposite signs do not imply a root;blind search may approach the pole.',347),
 ('ii','x/(x**2+1)','Odd continuous curve crossingO,extrema(−1,−½),(1,½),horizontal asymptote0.','Only x=0.','The function is continuous on the initial interval and changes sign. A valid search locates the actual root0.',348),
 ('iii','x**2/(x**2+1)','Even nonnegative curve touchingO,minimum0,horizontal asymptote1frombelow.','Only x=0.','The root is a touch with positive values at both initial endpoints. A sign-change-only search has no bracket and can miss it.',348)]:
 p=reasoning(label+'-a-sketch',features,'Derive the original domain,zeros and asymptotes before interpreting the graph. Match the key shape without inventing an equation from a drawing;here the equation is explicitly supplied.',kp,'sketch');parts.append(p)
 p=reasoning(label+'-b-roots',roots_text,'An original reciprocal has no zero numerator;the two rational functions have denominatorx²+1>0and numeratorzero onlyat0.',kp,'matches');parts.append(p)
 p=reasoning(label+'-c-search',behaviour,'Test original continuity and endpoint signs before applying any search. For a touching root,no sign change is a failure of that detector,not evidence that no root exists.',kp,'matches')
 p['additional_operations']={'endpoint_signs':{'kind':'identity','operands':[f'Tuple(sign(({formula}).subs(x,-3/10)),sign(({formula}).subs(x,7/10)))']}}
 p['additional_operation_expected']={'endpoint_signs':'Tuple(1,1)'if label=='iii'else'Tuple(-1,1)'};parts.append(p)
add(8,165,'For1/x,x/(x²+1),x²/(x²+1):sketch each,write down its roots,and investigate sign-search behaviour on[−0.3,0.7]. Separate a pole,an ordinary crossing and an even/touching zero.',parts,[ROOTG,BRACKET,SKETCH],sketch=True)
from author_Goldie_C5_opening import fig,figures
figures.clear()
fig(17,165,'Exercise6A7 given unscaled exponential-minus-cubic graph','The originale^x−x³curve remains positive for nonpositivex,crosses twice on positivex,and has an unscaled local maximum/minimum. Do not infer three crossings merely from an undulating curve.',[ROOTG,BRACKET],'graph',parent='Exercise-6A:7')
for row in figures:row['item_id']=row['item_id'].replace(':C5:',':C6:');row['parent_item_id']=row['parent_item_id'].replace(':C5:',':C6:');row['source_evidence']=ev(165)
pages=[]
for page in[164,165]:
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==164:ids+=['8227:TB:Goldie:C6:Teaching-figure:9']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':6,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:Goldie:C6:Worked-illustration:3']if page==164 else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'All6Aquestions,connected algorithm requests and the given6A7graph recorded. The pole-warning continuation on164is linked. Section6.2opens with introductory prose on165;the investigation starts166.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C6-6A.json',{'scope':'All8questions and every connected graph/root/algorithm/interval response.','items':answers}),('census-Goldie-C6-6A.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':6,'source_path':SRC,'source_sha256':SHA,'scope':'Complete164–165including warning continuation and6A7given graph.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;one given graph;method traces verified')
