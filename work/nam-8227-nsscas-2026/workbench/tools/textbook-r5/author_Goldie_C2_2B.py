"""Fixed source audit: all 20 Exercise2B questions, not renewable recipes."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
P='8227:2020:'
IND=P+'M2:T2:O01:D01';LAW=P+'M2:T2:O01:D02';EQ=P+'M2:T2:O03:D01';INEQ=P+'M2:T2:O03:D02'
SKETCH=P+'M1:T3:O05:D01';GP=P+'M1:T2:O03:D02';MOD_EQ=P+'M2:T1:O01:D02';MOD_INEQ=P+'M2:T1:O01:D03'
FACTOR=P+'M2:T1:O04:D02';COEFF=P+'M2:T1:O04:D03';POLY=P+'M2:T1:O04:D04'
ROM=['i','ii','iii','iv','v','vi','vii','viii','ix','x']
def ev(page):
 name='Goldie-C2-46' if page<=49 else 'Goldie-C2-50' if page<335 else 'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png'
 return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,sketch=False):
 for p in parts:
  kp=p.pop('key_page_override',337 if n>=5 else 336)
  p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:Exercise-2B:{n}','source_pdf_page':page,'notes':note,
  'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Classify the requested output. Definition/equivalent forms, log-law rewriting, logarithmic equation solving, inequality decisions, modulus branches, GP indexing and polynomial scaffolds stay distinct. A component used in a later solve is not automatically directly assessed.',
  'representation':'text','sketch_response_required':sketch,'exam_style':n>=15,
  'exam_style_basis':'The page attributes this question to a specific Cambridge examination.' if n>=15 else 'Ordinary exercise; no examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,
   'reason':'Exact indices or common-log power laws suffice. Internal CAS log ratios evaluate those laws; the learner is not asked to recall a general change-of-base formula.'}],
  'precision_angle_check':{'source':'Questions15–17,19–20 explicitly require3significant figures. Q14requires3decimal places in(i),whole-number percentage in(ii),and nearest whole decibel in(iii). Other keys mix decimal-place and significant-figure displays.',
   'comparison':'Retain exact bounds/roots and original positivity before rounding. Approximate inequality endpoints describe rounded boundaries,not a new exact boundary. Model validity is separate from arithmetic under a supplied formula.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
 answers.append(row);return row
def rounded(label,expr,key,page=337,sf=None,dp=None,method=None):
 p=value(label,expr,key,page,method or 'Derive from the original equation with common logs and positivity restrictions. Retain the exact expression,then compare only at the source display precision.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})};return p
def support(p,checks):
 p['additional_operations']={name:{'kind':'identity','operands':[expr]}for name,expr,target in checks}
 p['additional_operation_expected']={name:target for name,expr,target in checks};return p

# Definition tasks explicitly demand both the equivalent statement and its value.
parts=[]
for label,base,arg,key in zip(ROM,[3,4,2,5,7,16],['9','64','1/4','1/5','1','2'],['2','3','-2','-1','0','1/4']):
 p=value(label,f'log({arg},{base})',key,336,'Rewrite a^x=b as x=log_a(b),recognise a known exact power without a calculator,and verify a^x=b. CAS evaluation is internal QA.')
 p['author_answer_form']=f'x=log_{base}({arg})={key}';support(p,[('inverse',f'{base}**({key})',arg)]);parts.append(p)
add(1,48,'Convert3^x=9,4^x=64,2^x=1/4,5^x=1/5,7^x=1,16^x=2to logarithmic form and find the six exact exponents without a calculator.',parts,[IND])
parts=[]
for label,base,arg,key in zip(ROM,[3,5,2,6,64,5],['9','125','16','1','8','1/25'],['2','3','4','0','1/2','-2']):
 p=value(label,f'log({arg},{base})',key,336,'Rewrite y=log_a(b) as a^y=b; recognise the exact power and check the inverse equality.')
 p['author_answer_form']=f'{base}^y={arg}; y={key}';support(p,[('exponential_statement',f'{base}**({key})',arg)]);parts.append(p)
add(2,48,'Convert y=log3(9),log5(125),log2(16),log6(1),log64(8),log5(1/25)to exponential statements,then evaluate exactly without a calculator.',parts,[IND])
args=['log(10000,10)','log(1/10000,10)','log(sqrt(10),10)','log(1,10)','log(81,3)','log(1/81,3)','log(sqrt(27),3)','log(3**(1/4),3)','log(2,4)','log(1/125,5)']
add(3,48,'Evaluate ten logarithms by exact power recognition:common logs of10000,1/10000,√10,1; base3logs of81,1/81,√27,fourth-root3;log4(2);log5(1/125).',
 [value(label,expr,key,336,'Express the positive argument as a power of its fixed valid base and read off the exact exponent. Only the common-log cases are additionally calculator-checkable as requested.')for label,expr,key in zip(ROM,args,['4','-4','1/2','0','4','-4','3/2','1/4','1/2','-3'])],[IND])
args=['log(5)+log(2)','log(6)-log(3)','2*log(6)','-log(7)','log(9)/2','log(16)/4+log(2)','log(5)+3*log(2)-log(10)','log(12)-2*log(2)-log(9)','log(sqrt(16))/2+2*log(1/2)','2*log(4)+log(9)-log(144)/2']
targets=['10','2','36','1/7','3','4','4','1/3','1/2','12']
parts=[]
for label,arg,target in zip(ROM,args,targets):
 p=value(label,f'exp({arg})',target,336,'Apply product,quotient and power laws to the positive numerical arguments. Return a single logarithm,not a numerical logarithm value. Exponentiating the combined natural-log representation independently checks its argument.')
 p['author_answer_form']=f'log({target}) in the original common base';parts.append(p)
add(4,48,'Combine ten numerical log expressions into one logarithm,including reciprocal,root and product/quotient combinations;the final arguments are10,2,36,1/7,3,4,4,1/3,1/2,12.',parts,[LAW])
parts=[]
for label,expr,key in zip(ROM,['log(x**2)','log(x**5)-2*log(x)','log(sqrt(x))','log(x**(3/2))+log(x**(1/3))','3*log(x)+log(x**3)','log(sqrt(x)**5)'],['2','3','1/2','11/6','6','5/2']):
 p=value(label,f'expand_log({expr},force=True)/log(x)',key,337,'On the required target domain x>0,the power law converts each expression into a multiple of log(x). The coefficient check uses the algebraic identity,with its domain separately explicit;force expansion is not a license to extend to x<0.')
 p['author_answer_form']=f'({key})log(x),x>0';parts.append(p)
row=add(5,48,'Rewrite log(x²),log(x⁵)−2logx,log√x,log(x^(3/2))+log(cuberootx),3logx+log(x³),log((√x)^5)in terms of logx. The requested target restricts realx>0.',parts,[LAW])
row['source_interpretation']={'domain':'Part(i)alone originally admits x≠0,but writing2logx uses x>0. On the larger original domain it is2log|x|. Do not silently assert the positive-target expression on negative inputs.'}
parts=[]
for label,base,shift in [('i',10,0),('ii',2,1),('iii',2,-2)]:
 root=1-shift;pole=-shift
 p=reasoning(label,f'Increasing concave-down logarithm on x>{pole};vertical asymptote x={pole};x-intercept({root},0);unbounded rangeR.',
  'The argument x+shift must be positive. At argument1the logarithm is0. A base greater than1gives positive derivative1/((x+shift)ln(base))and negative second derivative. Approach the vertical asymptote only from its admissible side;do not draw a branch at nonpositive argument.',337,'sketch')
 support(p,[('intercept',f'log(({root})+({shift}),{base})','0'),('pole_argument',f'({pole})+({shift})','0')]);parts.append(p)
add(6,48,'Sketchy=log10x,y=log2(x+1),y=log2(x−2),showing each vertical asymptote and x-axis crossing. Preserve the positive argument domain.',parts,[SKETCH],sketch=True)

# For inequalities record exact open/closed bounds and separately verify each
# printed decimal boundary. Rounded endpoints do not replace exact endpoints.
spec=[('2^x<128','x<7',['7'],['7'],None),('3^x+5≥32','x≥3',['3'],['3'],None),('4^x+6≥70','x≥3',['3'],['3'],None),
 ('0.6^x<0.8','x>log(4/5)/log(3/5)',['log(4/5)/log(3/5)'],['0.437'],3),
 ('0.4^x−0.1≥0.3','x≤1',['1'],['1'],None),('0.5^x+0.2≤1','x≥log(4/5)/log(1/2)',['log(4/5)/log(1/2)'],['0.322'],3),
 ('2≤5^x<8','log(2)/log(5)≤x<log(8)/log(5)',['log(2)/log(5)','log(8)/log(5)'],['0.431','1.29'],3),
 ('1≤7^x<5','0≤x<log(5)/log(7)',['0','log(5)/log(7)'],['0','0.827'],3),
 ('|2^x−4|<2','1<x<log(6)/log(2)',['1','log(6)/log(2)'],['1','2.58'],3),
 ('|5^x−7|<4','log(3)/log(5)<x<log(11)/log(5)',['log(3)/log(5)','log(11)/log(5)'],['0.68','1.49'],None)]
parts=[]
for label,(stem,conclusion,bounds,keys,sf) in zip(ROM,spec):
 p=reasoning(label,conclusion,'Isolate the positive exponential,split a modulus into its strict double inequality when present,and use monotonicity. A base strictly between0and1reverses the inequality. Preserve every strict/non-strict endpoint. Compare the independently derived exact boundary at the printed precision.',337,'matches')
 p['source_inequality']=stem
 p['additional_operations']={};p['additional_operation_expected']={}
 for j,(expr,key)in enumerate(zip(bounds,keys)):
  op={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf and expression(expr)!=0 else{'decimal_places':len(key.split('.')[1])if'.'in key else 0})}
  p['additional_operations'][f'printed_bound_{j}']=op;p['additional_operation_expected'][f'printed_bound_{j}']=key
 parts.append(p)
row=add(7,49,'Solve ten exponential inequalities:2^x<128;3^x+5≥32;4^x+6≥70;0.6^x<0.8;0.4^x−0.1≥0.3;0.5^x+0.2≤1;2≤5^x<8;1≤7^x<5;|2^x−4|<2;|5^x−7|<4.',parts,[INEQ,MOD_INEQ],[LAW])
parts=[value('single-log','exp(2*log(x)-log(7))','x**2/7',337,'On x>0,combine2logx−log7=log(x²/7). Retain this form rather than just evaluating.'),
 value('root','sqrt(7*63)','21',337,'Combining the equation givesx²/7=63. The original logx requiresx>0,so reject−21and keep21.')]
support(parts[1],[('original_substitution','2*log(21)-log(7)-log(63)','0')])
add(8,49,'Combine2log10x−log107as one logarithm,then solve2log10x−log107=log1063with the original positive-x domain.',parts,[LAW],[EQ])
spec=[('2^x=1000000','log(1000000)/log(2)','19.93',2),('2^x=0.001','log(1/1000)/log(2)','-9.97',2),
 ('1.08^x=2','log(2)/log(108/100)','9.01',2),('1.1^x=100','log(100)/log(11/10)','48.3',1),
 ('0.99^x=0.000001','log(1/1000000)/log(99/100)','1375',0),('3^(2x+1)=20','(log(20)/log(3)-1)/2','0.863',3),
 ('2^(5x−2)=30','(log(30)/log(2)+2)/5','1.38',2),('2^(3x)=5^(2x+1)','log(5)/(3*log(2)-2*log(5))','-1.41',2),
 ('7^(x+3)=5^(x+4)','(4*log(5)-3*log(7))/(log(7)-log(5))','1.78',2)]
parts=[rounded(label,expr,key,dp=dp,method='Take common logs of the stated original exponential equation,apply the power law,isolate x and retain its exact expression. Both sides are positive. The compared decimal precision is the key display;the source asks no additional integer rounding.')for label,(stem,expr,key,dp)in zip(ROM,spec)]
for p,s in zip(parts,spec):p['source_equation']=s[0]
add(9,49,'Use common logarithms to solve nine specified equations,from one-base powers with growth/decay to affine exponents and powers of different bases. Preserve real exponents even when a key rounds to an integer.',parts,[EQ],[LAW])
parts=[]
polynomials=['x**2+3*x-18','x**2+x-2','2*x**2-7*x-4','x**2-5*x+6','3*x**2+5*x-2','2*x**2-7*x+3']
printed=[['1.58'],['0'],['1.38'],['0.387','6.13'],['-1'],['-0.356','0.564']]
for label,poly,base,keys in zip(ROM,polynomials,[2,5,3,6,3,7],printed):
 roots=expression(f'solve({poly},x)');positive=[r for r in roots if r.is_positive]
 p=value(label,'0','0',337,'Set y=base^x>0,solve the independently transcribed quadratic completely,discard all nonpositive y-roots,then recover each x by common logs. Compare every surviving root,not just the first one.')
 p['operation']={'kind':'identity','operands':['FiniteSet('+','.join(f'log({str(r)})/log({base})'for r in positive)+')']}
 p.pop('printed_key_normalised');p['printed_key_approximate_values']=keys;p['source_substitution_polynomial']=poly.replace('x','y')
 if label=='iv':
  p['expected_source_key_status']='key wrong';p['author_answer_form']='x=log(2)/log(6)orlog(3)/log(6),approximately0.387or0.613. The source prints6.13for the second root.'
 if label=='iii':
  p['expected_source_key_status']='key wrong';p['author_answer_form']='x=log(4)/log(3)≈1.26to3significant figures. The source key1.38doesnot solve the stated equation.'
 if label=='vi':
  p['expected_source_key_status']='key wrong';p['author_answer_form']='Exact roots−log(2)/log(7)andlog(3)/log(7)≈−0.356207…,0.564575…;nearest3significant figures−0.356and0.565. The source0.564truncates the latter;no rounding precision is explicitly asked inQ10. This is a last-digit display caution,not a lost algebraic branch.'
 parts.append(p)
add(10,49,'Solve2^(2x)+3·2^x−18=0;5^(2x)+5^x−2=0;2·3^(2x)−7·3^x−4=0;6^(2x)−5·6^x+6=0;3^(2x+1)+5·3^x−2=0;2·7^(2x)−7^(x+1)+3=0. Keep every positive-substitution branch.',parts,[EQ],['8227:PRIOR:NSSCO:quadratic',LAW])
p=value('k','1+log(28824005/5)/log(7)','9',337,'The kth GPterm is5·7^(k−1). The exact positive ratio is7^8,so k=9. Confirm the original term,not an off-by-one exponent.')
support(p,[('term','5*7**(9-1)','28824005')]);add(11,49,'Findkwhen a GPwith first term5and ratio7has kthterm28824005;use logs and preserve one-based term indexing.',[p],[GP],[EQ])
parts=[]
for label,a,r,last,key in [('i',-1,-2,-16777216,25),('ii','1/10',3,'43046721/10',17)]:
 expr=f'1+log(Abs(({last})/({a})))/log(Abs({r}))'
 p=value(label,expr,str(key),337,'Use the magnitude equation for the exponent,then check the original signed term. A negative GP ratio requires the final sign/parity check;logarithms of a negative base are not used.')
 support(p,[('signed_endpoint',f'({a})*({r})**({key}-1)',str(last))]);parts.append(p)
add(12,49,'Count terms in−1,2,−4,8,…,−16777216and0.1,0.3,0.9,2.7,…,4304672.1. The negative ratio in(i)requires parity validation after taking magnitudes.',parts,[GP],[EQ])
parts=[rounded('i','log(250000000000/63000)/log(10)','6.6',dp=1),rounded('ii','63000*10**(74/10)','1580000000000',sf=3),rounded('iii','10**(71/10-42/10)','794',sf=3)]
row=add(13,49,'Apply the supplied earthquake formula M=log10(E_J/63000):E=2.5×10^11Jto M;M=7.4to E;compare Efor M7.1and4.2. The named physical model is defective although its printed answers follow the given formula.',parts,[EQ],[LAW])
row['source_interpretation']={'context_model_status':'Source scientific-model defect; arithmetic checked conditionally on the printed model. USGSsource021PDF8–9haslog10(E_J)=1.5M+4.8,not coefficient1.','context_evidence':'analysis/textbook-context-evidence-r5.json','future_use':'Do not reuse this as a verified scientific formula. Supply a verified or explicitly hypothetical model in later authored practice.'}
parts=[rounded('i','10**(1/10)','1.259',dp=3),rounded('ii','100*(10**(1/10)-1)','26',dp=0),rounded('iii','10*log(2)/log(10)','3',dp=0)]
parts[1]['check_mode']='show/prove'
p=reasoning('iv','Percentage change under the supplied model is100(10^3.7−10^3.5)/10^3.5≈58.5%,not100(37−35)/35.',
 'The decibel numbers are logarithmic level readings,not the underlying linear quantity. Convert their difference into a multiplicative ratio before computing percentage change. Calling this quantity perceptual loudness is a physical simplification;only the explicitly supplied mathematical model is certified here.',337,'matches')
support(p,[('percentage','100*(10**(37/10)-10**(35/10))/10**(35/10)','100*(10**(1/5)-1)')]);parts.append(p)
add(14,50,'Using the source’s supplied factor10per10decibels,solve x^10=10to3dp,show35to36dBgives26%increase,find nearest-whole-dBdoubling,and explain Amir’s linear-percentage mistake for35to37dB.',parts,[EQ],[LAW])
p=reasoning('i','4<y<6.','−1<y−5<1gives4<y<6,with both boundaries excluded.',337,'matches')
p2=reasoning('ii','log(4)/log(3)<x<log(6)/log(3),approximately1.26<x<1.63.',
 'Use the part(i)interval withy=3^x>0. Base3is increasing,so taking logs preserves both strict signs. The printed rounded endpoints are3significant-figure approximations to exact bounds.',337,'matches')
support(p2,[('lower','log(4)/log(3)','log(4)/log(3)'),('upper','log(6)/log(3)','log(6)/log(3)')])
p2['additional_operations']['lower_display']={'kind':'rounded','operands':['log(4)/log(3)'],'significant_figures':3};p2['additional_operation_expected']['lower_display']='1.26'
p2['additional_operations']['upper_display']={'kind':'rounded','operands':['log(6)/log(3)'],'significant_figures':3};p2['additional_operation_expected']['upper_display']='1.63'
add(15,50,'Solve|y−5|<1then hence|3^x−5|<1to3significant figures. Cambridge9709Paper2Q3November2007attribution is internal textbook evidence only.',[p,p2],[MOD_INEQ,INEQ],[LAW])
p=value('roots','FiniteSet(log(2)/log(3),-log(3/2)/log(3))','0',337,'Sety=3^x>0. For y≥1,2(y−1)=y givesy=2;for0<y<1,2(1−y)=y givesy=2/3. Both meet their branch conditions. Recover both exponents.')
p.pop('printed_key_normalised');p['printed_key_approximate_values']=['0.631','-0.369']
support(p,[('positive_branch','2*Abs(2-1)-2','0'),('negative_branch','2*Abs(2/3-1)-2/3','0')])
add(16,50,'Solve2|3^x−1|=3^xto3significant figures,keeping both modulus branches and their positive substitution roots. Source attribution9709Paper31Q2November2013.',[p],[MOD_EQ,EQ],[LAW])
p=rounded('root','log(1+sqrt(2))/log(3)','0.802',sf=3,method='Setu=3^x>0;multiplyu=2+1/ubyutogetu²−2u−1=0. Reject1−√2<0and keep1+√2. Recoverxwith common logs and round at the end.')
support(p,[('quadratic_residual','(1+sqrt(2))**2-2*(1+sqrt(2))-1','0')]);add(17,50,'Solve3^x=2+3^(−x)usingu=3^xorotherwise,to3significant figures. Source attribution9709Paper3Q4June2007.',[p],[EQ],[LAW,'8227:PRIOR:NSSCO:quadratic'])
p=value('root','solve(x+9-100*x,x)[0]','1/11',337,'Original logs requirex>0. Subtract logxand combine tolog10((x+9)/x)=2. Thusx+9=100xandx=1/11,which meets the original domain. The rendered equation has no half coefficient on logx.')
support(p,[('original_residual','log(1/11+9)/log(10)-2-log(1/11)/log(10)','0')])
add(18,50,'Solve log10(x+9)=2+log10x withx>0 by the quotient law and original-domain checking. Attribution9709Paper33Q1June2014.',[p],[LAW])
parts=[value('i-coefficients','Tuple(solve([5*(-2)**3+a*(-2)**2+b,5*(-3)**3+a*(-3)**2+b],(a,b))[a],solve([5*(-2)**3+a*(-2)**2+b,5*(-3)**3+a*(-3)**2+b],(a,b))[b])','Tuple(19,-36)',337,'Use the two stated factors to setf(−2)=f(−3)=0,solve the two coefficient equations,and check both original evaluations.'),
 value('ii-factorisation','factor(5*x**3+19*x**2-36)','(x+2)*(x+3)*(5*x-6)',337,'Divide by the two known linear factors and factor completely;expand the proposed product to check every coefficient.'),
 rounded('ii-exponent','log(6/5)/log(5)','0.113',sf=3,method='With a=19,b=−36,setu=5^y>0. Then5^(3y+1)+a5^(2y)+b=5u³+19u²−36. Onlyu=6/5ispositive;discard−2,−3and recover y.')]
add(19,50,'Given factors(x+2),(x+3)of5x³+ax²+b,find a,b;factor fully;hence solve5^(3y+1)+a·5^(2y)+b=0to3significant figures. Attribution9709Paper21Q5November2014.',parts,[COEFF,POLY,EQ],[LAW])
parts=[value('i-zero','(12*x**3+25*x**2-4*x-12).subs(x,-2)','0',337,'Substitute the given candidate−2into the original cubic;zero establishes the linear factor.'),
 value('i-factorisation','factor(12*x**3+25*x**2-4*x-12)','(x+2)*(4*x+3)*(3*x-2)',337,'Divide by x+2then factor the quadratic;expand to check the complete original cubic.'),
 value('ii-power','solve(12*x**3+25*x**2-4*x-12,x)[2]','2/3',337,'Setu=3^y>0in12·27^y+25·9^y−4·3^y−12=0. Factorisation givesu=−2,−3/4,2/3;only2/3ispositive.'),
 rounded('ii-exponent','log(2/3)/log(3)','-0.369',sf=3)]
parts[0]['check_mode']='show/prove';support(parts[2],[('polynomial_at_power','12*(2/3)**3+25*(2/3)**2-4*(2/3)-12','0')])
row=add(20,50,'Showf(−2)=0and factorf(x)=12x³+25x²−4x−12;then state3^yand solve the corresponding27^y/9^y/3^yequation. Attribution9709Paper31Q4June2011.',parts,[FACTOR,POLY,EQ],[LAW])
row['source_interpretation']={'key_locator':'PDF337/printed323,the enlarged answer label is20and matches the exercise. A contact-sized reading of21was cleared;no source numbering defect is claimed.'}

if __name__=='__main__':
 target=W/'tools/textbook-r5/answers-Goldie-C2-2B.json'
 target.write_text(json.dumps({'scope':'Every requested response in all20Exercise2Bquestions;source discrepancies remain explicit.','items':answers},ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation'])
    if 'printed_key_normalised'in p:assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs')
