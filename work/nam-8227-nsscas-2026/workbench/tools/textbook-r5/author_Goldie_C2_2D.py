"""All Exercise2D responses and its four given graphs; fixed-source author QA."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
NAT='8227:2020:M2:T2:O02:D01';INV='8227:2020:M2:T2:O02:D02';LAW='8227:2020:M2:T2:O01:D02';EQ='8227:2020:M2:T2:O03:D01';LIN='8227:2020:M2:T2:O04:D01';PARAM='8227:2020:M2:T2:O04:D02'
def ev(page):
 name='Goldie-C2-66'if page<335 else'Goldie-key-C2-335'if page<=338 else'Goldie-key-C2-339'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,rep='text',continuation=None):
 for p in parts:
  kp=p.pop('key_page_override',338 if n<=6 else 339);pp=p.pop('source_page_override',page)
  p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:Exercise-2D:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Classify the actual rearrangement,graph,exponential equation or transformed-graph parameter decision. A supplied log-plot does not automatically assess construction of that plot;data reading and deriving the transformation are separate outputs.',
  'representation':rep,'sketch_response_required':any(p.get('author_comparison_status')=='sketch'for p in parts),'exam_style':n>=8,'exam_style_basis':'Specific Cambridge examination attribution.'if n>=8 else'Ordinary exercise without examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Natural logarithms,common-log power laws and their inverse definitions;no memorised change-of-base formula is asked.'}],
  'precision_angle_check':{'source':'Q11/12/13ask2decimal places;Q14asks2significant figures;Q9/10ask3significant figures. Population/height keys use mixed contextual approximations.',
   'comparison':'Read the plotted ordinate ln(y),not y. Recover coefficients by exponentiating intercepts. Preserve source time units and continuous threshold times;do not silently replace them with first whole-number observation times.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
 if continuation:row['continuation_pdf_pages']=continuation
 answers.append(row);return row
def rounded(label,expr,key,page=None,sf=None,dp=None,method=None):
 p=value(label,expr,key,page,method or'Derive the exact result from the original source equation,retain admissibility and units,and round only at the requested final precision.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})};return p
def support(p,checks):
 p['additional_operations']={name:{'kind':'identity','operands':[expr]}for name,expr,target in checks}
 p['additional_operation_expected']={name:target for name,expr,target in checks};return p
p=value('x','exp(log(a)+k*t)','a*exp(k*t)',338,'Normalize x0as a for internal algebra. Original ln x and ln x0require x>0,x0>0. Add ln x0then exponentiate to obtainx=x0e^(kt),which preserves positive x for realk,t.');p['author_answer_form']='x=x0e^(kt),x0>0.'
add(1,66,'Make x the subject of ln x−ln x0=kt;keep x0>0and the resulting positive x.',[p],[LAW,NAT])
p=value('t','-log(b/a)/k','log(a/b)/k',338,'Normalize s0=a,s=b. For s/s0>0andk≠0,t=−ln(s/s0)/k. The log quotient is equivalent to ln(s0/s)/k on that positive ratio domain. If k=0,the original equation instead says s=s0and does not determine unique t.')
# The quotient rewrite uses its real positive-ratio domain explicitly. CAS
# expands log ratios only for this qualified symbolic comparison.
p['operation']={'kind':'identity','operands':['expand_log(-log(b/a)/k,force=True)']};p['printed_key_normalised']='(log(a)-log(b))/k';p['author_answer_form']='t=ln(s0/s)/k, k≠0and s/s0>0; k=0is a separate nonunique/inconsistent case.'
add(2,66,'Make t the subject of s=s0e^(−kt),with k≠0and a positive ratio;record the k=0degeneracy rather than dividing by zero.',[p],[NAT,EQ],[LAW])
p=value('p','exp(-t/50)','25*exp(-t/50)',338,'Exponentiate the stated ln p=−0.02t directly. The correct p=e^(−0.02t)has initial value1at t=0. The printed25factor has no basis in the question and adds ln25to the original left side.')
p['expected_source_key_status']='key wrong';p['author_answer_form']='p=e^(−0.02t),p>0.'
support(p,[('initial_value_correct','exp(0)','1'),('printed_initial_value','25*exp(0)','25')])
add(3,66,'Make p the subject of ln p=−0.02t. The enlarged answer key incorrectly includes a factor25;the original equation has no ln25constant.',[p],[NAT])
p=value('x','log(solve((y-5)-(a-5)*x,x)[0])','log((y-5)/(a-5))',338,'Normalize y0as a. Dividing the original equation by y0−5requires y0≠5. The resulting ratio must be positive to take its real logarithm. If y0=5,the original requires y=5and does not uniquely determine x.')
p['author_answer_form']='x=ln((y−5)/(y0−5)),provided y0≠5and (y−5)/(y0−5)>0;otherwise use the original equation’s degenerate/no-real-solution cases.'
support(p,[('inverse_equation','(a-5)*exp(log((y-5)/(a-5)))-(y-5)','0')])
add(4,66,'Make x the subject of y−5=(y0−5)e^x;retain a nonzero y0−5and the positive logarithm ratio,plus the degenerate original case.',[p],[NAT,EQ])
spec=[('i','3/(1+exp(4))','0.0540',4,'ln(3−x)=4+lnx;original0<x<3.'),('ii','5/(exp(5)-1)','0.0339',4,'ln(x+5)=5+lnx;originalx>0.'),
 ('iii','2/(1+exp(2))','0.238',3,'ln(2−x)=2+lnx;original0<x<2.'),('iv','log(2)','0.693',3,'e^x=4/e^x;positive e^xgives e^(2x)=4.'),
 ('v','log(4)','1.386',3,'e^(2x)−8e^x+16=0;the substituted quadratic is a repeated positive root4.'),('vi','log(3)','1.099',3,'e^(2x)+e^x=12;substitution roots3,−4and only3ispositive.')]
parts=[]
for label,expr,key,dp,method in spec:
 p=rounded(label,expr,key,338,dp=dp,method=method+' Rearrange exactly,verify the original argument/positive-power domain,then compare at the key’s written precision.');parts.append(p)
add(5,66,'Solve six ln/e equations:three shifted-log domain cases,e^x=4e^(−x),a repeated quadratic in e^x,and e^(2x)+e^x=12. The key displays4dp,4dp,3dp,3dp,3dp,3dp respectively.',parts,[LAW,NAT,EQ],['8227:PRIOR:NSSCO:quadratic'])
p=reasoning('i','Sketch P=100e^(0.05t)for t≥0as an increasing convex curve starting at(0,100).','Positive first/second derivatives give the shape;the physical initial time truncates the full-real exponential. Source key sketch agrees.',338,'sketch')
p2=value('ii','100*exp(0)','100',338,'Set t=0in the original population model.')
p3=rounded('iii','100*exp(50/20)','1218',338,dp=0);p3['source_page_override']=67
p4=reasoning('iv','The continuous time is20ln10000≈184.207years;the key’s approximate184years is a rounded duration.','Set10^6=100e^(t/20),divide by100and take natural logarithms. It is not a first-whole-year question:rounding up to185would impose a different requirement.',338,'matches');p4['source_page_override']=67
support(p4,[('threshold','100*exp((20*log(10000))/20)','1000000')])
add(6,66,'For colony population P=100e^(0.05t),t years,sketch,find initial and50-year populations,and solve the continuous time to1million. Parts(iii)/(iv)continue on67.',[p,p2,p3,p4],[INV,EQ],continuation=[67])
parts=[value('i','20-19*(9/10)**0','1',339,'Substitute planting time0;the model does not start at height0.'),
 value('ii-height','20-19*(9/10)**2','4.61',339,'Use the original supplied decay factor for2years;output is metres.'),
 rounded('ii-time','log(10/19)/log(9/10)','6.09',339,dp=2,method='Set20−19·0.9^t=10;0.9^t=10/19. The base is below1,but the solved time is positive. Compare the key’s2decimal places.'),
 rounded('iii-a','exp(-2)','0.135',339,dp=3,method='The given ln y against ln hgraph has ordinate intercept−2=ln a. Recover a=e^(−2),not−2. The source also preserves the exact a=e^(−2).'),
 value('iii-b','(0-(-2))/(4/5-0)','2.5',339,'From the labelled grid,the line passes(0,−2)and(0.8,0). Its gradient isb=2/0.8=2.5.'),
 rounded('iv-time','log((20-(100*exp(2))**(2/5))/19)/log(9/10)','11',339,dp=0,method='First use100=e^(−2)h^(5/2)to find the positive target height,which lies below the20m asymptote. Substitute that height into the original time model and solve. The approximate key11years is a rounded continuous duration,not an imposed integer stopping rule.')]
add(7,67,'Use h=20−19·0.9^tmetres after t years;find initial/two-year heights and10m time. Read ln y=−2+2.5ln hfrom the given timber-value plot,then calculate time for y=$100using the same height model.',parts,[EQ,PARAM],[LAW],rep='graph')
p=value('y','solve((y+5)/y-x**2,y)[0]','5/(x**2-1)',339,'Original logs require y>0and x>0. Combining ln(y+5)−ln y=2lnxgives(y+5)/y=x²;solve and retain y>0,which forcesx>1. x=1isnot allowed and0<x<1would give the wrong ysign.')
add(8,67,'Express y in terms of xwithout logs given ln(y+5)−ln y=2lnx. Preserve original x>0,y>0and resultingx>1. Attribution9709Paper22Q2November2009.',[p],[LAW,NAT])
p=rounded('ratio','log(5/2)/log(5/4)','4.11',339,sf=3,method='Take logs of(1.25)^x=(2.5)^yto getxln1.25=yln2.5. Divide by nonzero yandln1.25. The special x=y=0satisfies the original equation but leaves the requested ratio undefined.')
add(9,67,'Given(1.25)^x=(2.5)^y,find x/yto3significant figures,assuming its denominator is nonzero. Attribution9709Paper2Q1June2009.',[p],[EQ],[LAW])
p=rounded('root','log((1+sqrt(5))/2)','0.481',339,sf=3,method='Putu=e^x>0. Originalu+u²=u³allows division byu,butu=0isnot an admissible exponential. Solveu²−u−1=0,discard the negative root,and returnln((1+√5)/2).')
support(p,[('original_polynomial','((1+sqrt(5))/2)+((1+sqrt(5))/2)**2-((1+sqrt(5))/2)**3','0')])
add(10,67,'Solve e^x+e^(2x)=e^(3x)to3significant figures;filter the exponential zero and negative quadratic root. Attribution9709Paper3Q2June2008.',[p],[EQ],['8227:PRIOR:NSSCO:quadratic',NAT])
parts=[rounded('A','exp(13/10)','3.67',339,dp=2,method='In ln y=ln A−xln b,the supplied point(0,1.3)gives ln A=1.3. Exponentiate before rounding.'),
 rounded('b','exp(-((9/10-13/10)/(16/10)))','1.28',339,dp=2,method='The line gradient is(0.9−1.3)/1.6=−0.25=−ln b. Therefore b=e^0.25,not e^(−0.25).')]
add(11,68,'For y=A b^(−x),read supplied ln yversusxpoints(0,1.3),(1.6,0.9)and recover A,bto2decimal places. Attribution9709Paper2Q3November2008.',parts,[PARAM],[LAW],rep='graph')
p=rounded('x','-log(exp(2)-2)','-1.68',339,dp=2,method='ln(2+e^(−x))=2impliese^(−x)=e²−2>0. Take ln and preserve the negative sign on x;the original log argument is positive for every real x.')
add(12,68,'Solve ln(2+e^(−x))=2to2decimal places. Attribution9709Paper3Q1June2009.',[p],[NAT,EQ])
parts=[rounded('K','exp(2)','7.39',339,dp=2,method='ln y=ln K+m ln xhas supplied ordinate intercept2,soK=e².'),
 rounded('m','(102/10-2)/6','1.37',339,dp=2,method='The supplied transformed points(0,2),(6,10.2)give gradient8.2/6=m. Do not use original yvalues or reverse axes.')]
add(13,68,'For y=Kx^m,read ln yagainstln xpoints(0,2),(6,10.2),then recover K,mto2decimal places. Attribution9709Paper21Q3June2011.',parts,[PARAM],[LAW],rep='graph')
parts=[rounded('p','(292/100-160/100)/(5-2)','0.44',339,sf=2,method='ln y=ln A+p(x−1)=px+(ln A−p). The supplied line gradient is(2.92−1.60)/(5−2)=0.44=p.'),
 rounded('A','exp(160/100-((292/100-160/100)/(5-2))*(2-1))','3.2',339,sf=2,method='Use point(2,1.60)in ln y=ln A+p(x−1):ln A=1.60−0.44=1.16. The ordinate intercept0.72isln A−p,notln A. Exponentiate1.16and round to2significant figures.')]
for p in parts:p['source_page_override']=69
add(14,68,'For y=Ae^(p(x−1)),use ln yagainst xthrough(2,1.60),(5,2.92),continued on69,to find A,pboth to2significant figures. Attribution9709Paper21Q2June2015.',parts,[PARAM],[LAW],rep='graph',continuation=[69])
figures.clear()
for n,page,label,note,teaches,parent in [
 (60,67,'Exercise2D7 timber-value log plot','The plotted axes areln yandln h. The line has ordinate intercept−2and slope2.5,so y=e^(−2)h^(5/2). The red plot is a straight line in transformed coordinates,not a physical timber-height curve.',[PARAM],'Exercise-2D:7'),
 (61,68,'Exercise2D11 decreasing log plot','ln yagainstxhas givenpoints(0,1.3),(1.6,0.9),slope−0.25and positive ordinate intercept. For y=A b^(−x),the negative gradient is−ln b;it does not mean b<1.',[PARAM],'Exercise-2D:11'),
 (62,68,'Exercise2D13 power-law log plot','ln yagainstln xpasses(0,2),(6,10.2). They are transformed coordinates;the original xat the first point is1,not0.',[PARAM],'Exercise-2D:13'),
 (63,68,'Exercise2D14 shifted-exponent log plot','ln yagainstxpasses(2,1.60),(5,2.92). For y=Ae^(p(x−1)),the ordinate intercept equalsln A−p. The exponent shift changes recovery ofAwhile leaving gradientp.',[PARAM],'Exercise-2D:14')]:fig(n,page,label,note,teaches,'graph',[],parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:');f['source_evidence']=ev(f['pdf_page'])
# The chapter summary is one consolidated teaching reference,not8extra tasks.
fig(64,69,'Chapter2 key-points reference','The summary collects exponential definition,log/indices equivalence,positive-argument log laws,power/exponential linearisation,e/lninverse meanings,and∫1/x dx=ln|x|+Cfor x≠0. The listed eapproximation is2.7182818284…;it is a prefix,not a nearest-rounded10dpclaim.',[NAT,INV,LAW,LIN,PARAM],'table',[('diff(log(-x),x)','1/x')])
f=figures[-1];f['item_id']=f['item_id'].replace(':C5:',':C2:');f['source_evidence']=ev(69)
pages=[]
for page in range(66,70):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==66:ids+=['8227:TB:Goldie:C2:Example:12']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':ids,
  'continuation_item_ids':['8227:TB:Goldie:C2:Exercise-2D:6']if page==67 else['8227:TB:Goldie:C2:Exercise-2D:14']if page==69 else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every Exercise2Dquestion and given graph,Example12and consolidated key-points block enumerated. Connected-part continuations retain their original item identifiers.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-2D.json',{'scope':'All14Exercise2Dquestions and every requested subpart.','items':answers}),('census-Goldie-C2-2D.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete66–69including Example12and chapter summary.','new_items':figures,'corrections':[{'item_id':r['item_id'],'continuation_pdf_pages':r['continuation_pdf_pages']}for r in answers if r.get('continuation_pdf_pages')],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    same=equivalent(compute(p['operation']),expression(p['printed_key_normalised']))
    assert(not same)if p.get('expected_source_key_status')=='key wrong'else same,(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
