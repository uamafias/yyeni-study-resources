"""YM420–423: inequality direction, natural-log definitions and positive substitutions."""
import json
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,ev,v,fig,figures,extra,compute,expression,equivalent
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
NAT='8227:2020:M2:T2:O02:D01';EXP=g.EXP;INEQ='8227:2020:M2:T2:O03:D02'
def natural(label,original,key,kp,sf=None,units=None):
 p=v(label,original,key,kp,'Evaluate the ORIGINAL natural exponential/logarithm with basee,retaining any outside sign or factor. Use e^(lnu)=u ONLY foru>0 and ln(e^x)=x for realx. A supplied exponential model is evaluated at the original time;it is not a request to construct a model or solve for an unknown exponent. Round only an explicitly approximate final display.')
 p.update(assessed_8227_demand_ids=[NAT],response_format='numeric')
 if sf:p['operation']={'kind':'rounded','operands':[original],'significant_figures':sf}
 if units:p.update(units=units,printed_key_units=units)
 return p
def solve_exp(label,condition,key,kp,sf=None):
 exact='solve('+condition+',x)[0]';p=v(label,exact,key,kp,'Use the ORIGINAL basee equation and ln/e inverse relation on positive quantities. Retain its actual exponent shifts,outside multipliers and every original domain condition. Solve the resulting linear equation exactly;round only the source numerical display where requested.')
 p.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],response_format='symbolic')
 if sf:p['operation']={'kind':'rounded','operands':[exact],'significant_figures':sf};p['response_format']='numeric'
 p['additional_operations']={'exact-internal-root':{'kind':'identity','operands':[exact]}}
 return p
def inequality(label,condition,key,kp,side,original,sf=None,slope_sign=None):
 exact='solve('+condition+',x)[0]';p=v(label,exact,key,kp,'Take common logs of the ORIGINAL positive-base exponential inequality and retain its strict/inclusive sign. Solve its actual log-linear boundary and determine the sign of its coefficient before division. The separately transcribed source bound is compared after this derivation;rounded display bounds are not treated as exact cutoffs.')
 p.update(assessed_8227_demand_ids=[INEQ],response_format='symbolic',original_inequality=original,solution_relation=side,exact_boundary_expression=exact,required_answer_form='base10logarithms'if not sf else'3sfdisplaywith exact internal boundary')
 if sf:p['operation']={'kind':'rounded','operands':[exact],'significant_figures':sf}
 if slope_sign:extra(p,'actual-log-linear-coefficient-sign','sign(diff('+condition+',x))',slope_sign)
 return p
def add(kind,n,page,note,parts):
 r=g.add(kind,n,page,note,parts)
 r['mapping_rationale']='Explicit e/ln evaluation directly assesses the natural definition objectiveO02. Solving a natural exponential is an EXP demand with that definition as a component. Supplied population/mass models require evaluation,not model construction. Exponential inequalities preserve the sign of the actual log-linear coefficient.'
 return r
ps=[inequality('a','x*log(5)-log(7)','Rational(121,100)',638,'<=','5^x≤7',3,'1'),inequality('b','x*log(Rational(4,5))-log(Rational(3,10))','Rational(27,5)',638,'<=','0.8^x≥0.3',3,'-1'),inequality('c','x*log(Rational(1,3))-log(3)','-1',638,'>','(1/3)^x<3',slope_sign='-1')]
add('Try-Now',16,420,'Three exponential inequalities:positive and reciprocal bases,strict and inclusive signs. Keep exact internal cutoffs separately from source1.21,5.40 and exact−1.',ps)
add('Example',17,420,'Solve7(5/6)^(3−x)≤4,explicitly in base10logs. Two sign reversals in the source algebra yieldx≤3−log(4/7)/log(5/6).',[inequality('solution','log(7)+(3-x)*log(Rational(5,6))-log(4)','3-log(Rational(4,7))/log(Rational(5,6))',420,'<=','7(5/6)^(3−x)≤4',slope_sign='1')])
ps=[inequality('a','(2*x+5)*log(3)-log(20)','log(20)/(2*log(3))-Rational(5,2)',638,'<','3^(2x+5)<20',slope_sign='1'),inequality('b','log(2)+(2*x+1)*log(5)-log(3)','log(Rational(3,2))/(2*log(5))-Rational(1,2)',638,'>=','2·5^(2x+1)≥3',slope_sign='1')]
add('Try-Now-17',1,420,'Solve two shifted-exponent inequalities,expressing bounds in base10logs. Preserve stricta and inclusiveb and the outside factor2.',ps)
p=inequality('show-bound','(2*x-1)*log(3)+(1-3*x)*log(2)-log(5)','log(Rational(15,2))/log(Rational(9,8))',638,'<','3^(2x−1)·2^(1−3x)<5',slope_sign='1');p.update(check_mode='show/prove',response_format='proof/show-that')
add('Try-Now-17',2,420,'Prove the supplied inequality solution by combining the ORIGINAL product exponents. Its effective base9/8 exceeds1;boundlog(15/2)/log(9/8).',[p])
add('Example',18,421,'Evaluate supplied population model P(t)=7e^(0.02t),P measured in MILLIONS andt in years. PresentP0=7million;P6≈7.89million. No model fitting is asked.',[natural('a','7*exp(Rational(1,50)*0)','7',421,units='million people'),natural('b','7*exp(Rational(1,50)*6)','Rational(789,100)',421,3,'million people')])
add('Try-Now',18,422,'Evaluate supplied mass model M(t)=8e^(−0.13t),grams witht inyears. Present8g,after5years4.18g. The negative decay exponent is retained.',[natural('a','8*exp(-Rational(13,100)*0)','8',638,units='g'),natural('b','8*exp(-Rational(13,100)*5)','Rational(209,50)',638,3,'g')])
add('Example',19,422,'Evaluate e^0.6,ln0.8 and lne to3sf where nonexact. A log of a POSITIVE argument below1isnegative and valid.',[natural('a','exp(Rational(3,5))','Rational(91,50)',422,3),natural('b','log(Rational(4,5))','-Rational(223,1000)',422,3),natural('c','log(E)','1',422)])
add('Try-Now',19,422,'Four direct e/ln evaluations: e⁴,e^(−2),ln4,ln1. Exactzero in(d) is not a request to round zero to a fixed significant-figure count.',[natural('a','exp(4)','Rational(273,5)',638,3),natural('b','exp(-2)','Rational(27,200)',638,3),natural('c','log(4)','Rational(139,100)',638,3),natural('d','log(1)','0',638)])
add('Example',20,422,'Without a calculator use the natural inverse relation in e^(ln3),4e^(ln6),and e^(−ln(1/3)). Outside factors/signs remain distinct from the logarithm argument.',[natural('a','exp(log(3))','3',422),natural('b','4*exp(log(6))','24',422),natural('c','exp(-log(Rational(1,3)))','3',422)])
p=natural('a','exp(log(y))','y',638);p.update(response_format='symbolic',original_domain='y>0 from the ORIGINALlny;the simplified y does not broaden that domain.')
add('Try-Now',20,422,'Without a calculator evaluate e^(lny),−2e^(ln5),e^((1/3)ln27). Keepy>0and the OUTSIDE−2;answersy,−10,3.',[p,natural('b','-2*exp(log(5))','-10',638),natural('c','exp(log(27)/3)','3',638)])
add('Example',21,422,'Solve two basee equations explicitly in NATURAL logs: e^x12 ande^(2x+1)5. Keep the original exponent+1beforedivisionby2.',[solve_exp('a','x-log(12)','log(12)',422),solve_exp('b','2*x+1-log(5)','(log(5)-1)/2',422)])
add('Try-Now',21,423,'Solve e^(3x)=10 ande^(x/2−3)=5,in natural logarithms. The second is2ln5+6=ln25+6;no common-log substitution is requested.',[solve_exp('a','3*x-log(10)','log(10)/3',638),solve_exp('b','x/2-3-log(5)','log(25)+6',638)])
add('Example',22,423,'Solve7e^(3x)=320. First isolate the positive exponential320/7,then take ln;source3sf1.27.',[solve_exp('x','3*x-log(Rational(320,7))','Rational(127,100)',423,3)])
add('Try-Now',22,423,'Solve e^(x−1)−5=5 and5e^(2x)=128. Keep outside constants separate from exponent shifts;source displays3.30,1.62.',[solve_exp('a','x-1-log(10)','Rational(33,10)',638,3),solve_exp('b','2*x-log(Rational(128,5))','Rational(81,50)',638,3)])
p=v('possible-e-x','Intersection(solveset(3*x**2-14*x+8,x,domain=S.Reals),Interval.open(0,oo))','FiniteSet(Rational(2,3),4)',423,'Setu=e^x>0 in the ORIGINAL3e^x+8e^(−x)=14. Multiplication by positiveu gives3u²−14u+8=0. Both2/3and4arepositive;retain BOTH possible values ofe^x before recovering x.');p.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],response_format='symbolic')
q=natural('x-negative','log(Rational(2,3))','-Rational(81,200)',423,3);r=natural('x-positive','log(4)','Rational(139,100)',423,3)
for a in[q,r]:a.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],depends_on_source_parts=['possible-e-x'])
add('Example',23,423,'Find BOTH possible values ofe^x,then solve the reciprocal-exponential equation to3sf. A positive substituted value BELOW1produces a valid NEGATIVE x.',[p,q,r])
p=v('a-all-roots','imageset(Lambda(x,log(x)),Intersection(solveset(x**2-5*x+6,x,domain=S.Reals),Interval.open(0,oo)))','FiniteSet(log(2),log(3))',638,'Setu=e^x>0. The quadratic has BOTH positive roots2,3,so recover BOTH exact exponentsln2,ln3.');p.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],response_format='symbolic')
q=v('b-all-roots','imageset(Lambda(x,log(x)),Intersection(solveset(x**2-4*x-21,x,domain=S.Reals),Interval.open(0,oo)))','FiniteSet(log(7))',638,'Originale^x−21e^(−x)=4 givesu²−4u−21=0withu>0. Reject−3andretain7;only exponentln7remains.');q.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],response_format='symbolic')
add('Try-Now-23',1,423,'Two exponential quadratics:one retains TWO positive substituted roots,while the reciprocal form rejects its negative substituted root. Exact answersln2,ln3andln7.',[p,q])
p=v('all-roots','FiniteSet(*[expand_log(log(y),force=True)/log(3) for y in Intersection(solveset(3*x**2-82*x+27,x,domain=S.Reals),Interval.open(0,oo))])','FiniteSet(-1,3)',638,'Setu=e^x>0. The source quadratic has roots1/3and27,bothpositive. Recoverln(1/3)=−ln3andln27=3ln3,in the explicitly requestedkln3form.');p.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[NAT],response_format='symbolic',requested_answer_form='k ln3',normalisation='Complete coefficient set k for x=k ln3; not the raw x-set.',printed_key_display='x=−ln3 or x=3ln3',author_answer_form='x=−ln3 or x=3ln3')
add('Try-Now-23',2,423,'Solve3e^(2x)−82e^x+27=0,giving ALL solutions in the requestedkln3form. Both positive substitution branches survive.',[p])
refs=[(36,420,'Example17 sign reversals and exact log-ratio form','Original affine exponent3−x and log(5/6)<0must both be retained. The final bound is not a log law for logA/logB.',[INEQ],'table','Example:17'),(37,421,'Natural exponential/logarithm inverse definition','e≈2.71828; e^x=y iff x=lny fory>0. This is the natural-definition objective,distinct from earlier arbitrary-base logs.',[NAT],'table',None),(38,421,'Natural inverse-value table','lne1,ln10,ln(e^x)=x ande^(lnx)=x withx>0where required.',[NAT],'table',None),(39,421,'Natural-log product/quotient/power rules','The earlier common-base laws apply with basee and positive original arguments. No arbitrary change-of-base method is added.',[NAT],'table',None),(40,421,'Example18 present-time modelling step','Presenttime means t0 in the SUPPLIED model,not solving for a fitted growth rate. Units are millionpeopleandyears.',[NAT],'table','Example:18'),(41,422,'Example19 calculator natural-key layouts','Calculator keys are procedure context;source mathematics is e^0.6 andln0.8with final3sf displays.',[NAT],'table','Example:19'),(42,422,'Example20 inverse-log reminder','e^(lnx)=xneedsoriginalx>0. An outside sign/coefficient stays outside that inverse relation.',[NAT],'table','Example:20'),(43,422,'Example21 natural-log conversion reminder','Take the ln of an isolated positive exponential,then solve its actual affine exponent.',[EXP],'table','Example:21'),(44,423,'Example22 isolate-before-ln action arrows','Divide by7beforetakingln,andretain exponent coefficient3. Exactx=ln(320/7)/3.',[EXP],'table','Example:22'),(45,423,'Example23 reciprocal substitution/positive-root chain','Multiply by e^x>0toform the quadratic. Both2/3and4areadmissible;afterln the first gives a negative exponent,not an invalid root.',[EXP],'table','Example:23')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read natural-log inverse conditions,model units and original substitution/sign chains. Independently evaluate the original exponentials and solve all admissible substituted branches;keep calculator layouts as procedure context.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry16/Example17/Try17Q1–2andnatural-logExamples18–23/Try18–23questionsplus ten reference panels enumerated. Supplied models are evaluation tasks.',scope_screen='Natural-definition/evaluation versus exponentialsolveclassification remains explicit;originalpositive-substitutionandphysicalunitconditionsretained.')for page in range(420,424)]
def save():
 for name,data in [('answers-YM-C9-natural-opening.json',dict(scope='Complete420–423source responses;natural-definition/equation boundary explicit.',items=answers)),('census-YM-C9-natural-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete420–423page/item/reference census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
