"""YM417–419: original exponential equations, positive substitutions and inequalities."""
import json
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,ev,v,fig,figures,extra,compute,expression,equivalent
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
EXP=g.EXP;INEQ='8227:2020:M2:T2:O03:D02';LAW='8227:2020:M2:T2:O01:D02'
def root(label,linear_log_condition,key,kp,original):
 exact='solve('+linear_log_condition+',x)[0]'
 p=v(label,exact,key,kp,'Take a COMMON valid logarithm of the ORIGINAL positive-base exponential relation. Apply the power/product laws to the actual original exponents,solve the resulting linear equation independently,and round only the final result to the written3sf display. The exact value is kept. This is not a memorised change-of-base method.')
 p.update(operation={'kind':'rounded','operands':[exact],'significant_figures':3},original_equation=original,original_domain='All real x; original fixed exponential bases are positive and not1.',assessed_8227_demand_ids=[EXP],component_demand_ids=[LAW],response_format='numeric',display_precision='Source/answer key displays3significant figures;exact internal value retained.')
 p['additional_operations']={'exact-root':{'kind':'identity','operands':[exact]}}
 return p
def substitution_root(label,poly,base,key,kp,original):
 # The independently derived exact roots of the source quadratic are filtered
 # before recovering the exponent. No source key enters this computation.
 exact='log(Max(*Intersection(solveset('+poly+',x,domain=S.Reals),Interval.open(0,oo))))/log('+base+')'
 p=v(label,exact,key,kp,'Setu equal to the ORIGINAL positive exponential base^x. Solve the actual source quadratic in u and retain ONLYu>0;the single admissible root determines the unique real exponent. Recover x using common logarithms,retain its exact value,and round the final display once.')
 p.update(operation={'kind':'rounded','operands':[exact],'significant_figures':3},original_equation=original,positive_substitution='u='+base+'^x>0',substitution_polynomial=poly,assessed_8227_demand_ids=[EXP],component_demand_ids=[LAW],response_format='numeric')
 extra(p,'positive-substitution-root-count','len(Intersection(solveset('+poly+',x,domain=S.Reals),Interval.open(0,oo)))','1')
 p['additional_operations']['exact-exponent']={'kind':'identity','operands':[exact]}
 return p
def proof(label,original,rewritten,kp,method):
 p=v(label,'simplify(('+original+')-('+rewritten+'))','0',kp,method)
 p.update(original_zero_form=original,rewritten_zero_form=rewritten,assessed_8227_demand_ids=[EXP],check_mode='show/prove',response_format='proof/show-that')
 return p
def add(kind,n,page,note,parts):
 r=g.add(kind,n,page,note,parts)
 r['mapping_rationale']='Distinguish a single exponential term,a product of exponentials,different bases,a positive exponential substitution,and an inequality whose log multiplier can be negative. Numerical changes within those same decisions are variations,not automatically new families.'
 return r
add('Example',12,417,'Solve5^(x+2)=7 by common logs; exactxlog7/log5−2,source−0.791to3sf.',[root('x','(x+2)*log(5)-log(7)','-Rational(791,1000)',417,'5^(x+2)=7')])
add('Try-Now',12,417,'Three single-base exponentials,including17^x5.23 and an affine exponent2x−5. Retain decimal input5.23 exactly before rounding.',[root('a','x*log(4)-log(3)','Rational(99,125)',638,'4^x=3'),root('b','x*log(17)-log(Rational(523,100))','Rational(73,125)',638,'17^x=5.23'),root('c','(2*x-5)*log(3)-log(20)','Rational(193,50)',638,'3^(2x−5)=20')])
add('Example',13,417,'Solve4^(1−3y)=3^(y−2). Keep BOTH original affine exponents when collecting y;source0.682.',[root('y','(1-3*x)*log(4)-(x-2)*log(3)','Rational(341,500)',417,'4^(1−3y)=3^(y−2)')])
add('Try-Now',13,418,'Three different-base exponential equations:5^(y+3)=7^(4−3y),3^(2y)=4^(y+5),and2^(2y+1)=3^(y+2). Unknown source y is checker x.',[root('a','(x+3)*log(5)-(4-3*x)*log(7)','Rational(397,1000)',638,'5^(y+3)=7^(4−3y)'),root('b','2*x*log(3)-(x+5)*log(4)','Rational(171,20)',638,'3^(2y)=4^(y+5)'),root('c','(2*x+1)*log(2)-(x+2)*log(3)','Rational(523,100)',638,'2^(2y+1)=3^(y+2)')])
add('Example',14,418,'Solve product5^x·7^(x+1)=582. The extra factor7 is retained;it is not35^x582.',[root('x','x*log(5)+(x+1)*log(7)-log(582)','Rational(31,25)',418,'5^x·7^(x+1)=582')])
add('Try-Now',14,418,'Three product/ratio exponential structures retain outside factor0.6,shift−1,and doubled exponent2x. Common-log linearisation gives1.20,2.31,1.70.',[root('a','(x-1)*log(5)-log(Rational(3,5))-x*log(2)','Rational(6,5)',638,'5^(x−1)=0.6·2^x'),root('b','(x-1)*log(3)+x*log(2)-log(21)','Rational(231,100)',638,'3^(x−1)·2^x=21'),root('c','x*log(2)+2*x*log(3)-log(5)-x*log(7)','Rational(17,10)',638,'2^x·3^(2x)=5·7^x')])
add('Example',15,418,'Solve4^x−2^(x+2)=5 viau2^x>0. Quadraticu²−4u−5 has admissible5and inadmissible−1;exactxlog5/log2.',[substitution_root('x','x**2-4*x-5','2','Rational(58,25)',418,'4^x−2^(x+2)=5')])
add('Try-Now-15',1,418,'Solve2·3^(2x)+7·3^x−15=0 viau3^x>0. Keepu3/2,rejectu−5.',[substitution_root('x','2*x**2+7*x-15','3','Rational(369,1000)',638,'2·3^(2x)+7·3^x−15=0')])
p=proof('a-rewrite','2**(x+1)+6*2**(x-1)-12','2*2**x+3*2**x-12',638,'Use the ORIGINAL exponent laws2^(x+1)=2·2^x and6·2^(x−1)=3·2^x. Their difference is exactlyzero for all real x.')
q=root('b-x','x*log(2)-log(Rational(12,5))','Rational(63,50)',638,'2^(x+1)+6·2^(x−1)−12=0');q['depends_on_source_parts']=['a-rewrite']
add('Try-Now-15',2,418,'First show the specified rewrite,then hence solve. This reduces to a LINEAR equation in2^x,not a forced quadratic substitution.',[p,q])
add('Try-Now-15',3,418,'Solve9^x−3^(x+1)=4 viau3^x>0. Quadraticu²−3u−4keeps4andrejects−1.',[substitution_root('x','x**2-3*x-4','3','Rational(63,50)',638,'9^x−3^(x+1)=4')])
p=proof('a-quadratic','y+3/y-4','(y**2-4*y+3)/y',638,'Sety=2^x>0. The ORIGINAL equation becomesy+3/y4; multiplying by nonzero y gives the stated quadratic. Keepy>0 so multiplication is reversible.')
p['positive_substitution']='y=2^x>0'
q=v('b-x-zero','log(1)/log(2)','0',638,'Both quadratic roots1,3arepositive. Rootu1recovers exactx0;do not discard the zero exponent as a zero substituted variable.');q.update(assessed_8227_demand_ids=[EXP],response_format='numeric',depends_on_source_parts=['a-quadratic'])
r=root('b-x-nonzero','x*log(2)-log(3)','Rational(79,50)',638,'2^x+3·2^(−x)=4,positive substituted root3');r['depends_on_source_parts']=['a-quadratic']
extra(q,'complete-positive-substituted-roots','solveset(x**2-4*x+3,x,domain=S.Reals)','FiniteSet(1,3)')
add('Try-Now-15',4,419,'Connected reciprocal-exponential rewrite and solve. Both positive substituted roots1,3survive,givingx0andexactlog3/log2(display1.58).',[p,q,r])
ps=[]
for label,base,target,relation,key in [('a','2','5','<','Rational(58,25)'),('b','Rational(4,5)','Rational(1,2)','>','Rational(311,100)')]:
 p=root(label,'x*log('+base+')-log('+target+')',key,419,base+'^x<'+target)
 p['assessed_8227_demand_ids']=[INEQ];p['source_answer_form']='x'+relation+('2.32'if label=='a'else'3.11')
 p['exact_solution_set']=('Interval.open(-oo,log(5)/log(2))'if label=='a'else'Interval.open(log(Rational(1,2))/log(Rational(4,5)),oo)')
 p['inequality_reason']='The common log multiplier is positive,so preserve <.'if label=='a'else'The common log multiplierlog(0.8)is NEGATIVE,so dividing reverses < to >.'
 p['boundary_display_note']='Printed3sf cutoff is a rounded representation of the exact boundary,not a changed exact real solution set.'
 extra(p,'original-log-multiplier-sign','sign(log('+base+'))','1'if label=='a'else'-1');ps.append(p)
add('Example',16,419,'Solve2^x<5 and0.8^x<0.5. Store the EXACT half-lines and strict boundaries separately from rounded source cutoffs2.32,3.11; the second inequality reverses direction.',ps)
refs=[(26,417,'Taking a common log of equal positive quantities','Forpositive m,n, equal quantities have equal common-base logarithms. Power-law linearisation uses the actual original exponents.',[LAW],'table',None),(27,417,'Example12 common-log action arrows','Take logs,bring downx+2,divide by the nonzero log5,and retain the exponent shift−2.',[EXP],'table','Example:12'),(28,417,'Example13 two-base linear equation','Both affine exponents contribute to the coefficient ofy. The final denominatorlog3+3log4isnonzero.',[EXP],'table','Example:13'),(29,418,'Example14 product-log arrows','A product of exponentials becomes a sum of logs;the+1exponent produces an extra log7term.',[EXP],'table','Example:14'),(30,418,'Example15 positive-exponential substitution callout','2^xispositive for all real x. Reject the negative quadratic root−1;this does not reject negative exponent values in general.',[EXP],'table','Example:15'),(31,418,'Example15 index-factor rewrite','4^x=(2^x)² and2^(x+2)=4·2^x; these give the actual substitution polynomial.',[EXP],'table','Example:15'),(32,419,'Exponential inequality sign rule','Forbase>1the relevant logarithm is positive;for0<base<1it is negative. Division by a negative multiplier reverses the comparison.',[INEQ],'table',None),(33,419,'Increasing-base logarithm comparison graph','Forbase3,log_3x<log_3(12)means0<x<12. The logarithm original domainx>0is retained.',[INEQ],'graph',None),(34,419,'Reciprocal-base logarithm comparison graph','Forbase1/3,the same log-value comparison reverses to x>12 onx>0. Positive arguments and decreasing orientation are essential.',[INEQ],'graph',None),(35,419,'Example16 negative-log warning','For0.8,the common log is negative;the strict inequality reverses on division. Rounding the final cutoffdoesnotchangeits exact internal value.',[INEQ],'table','Example:16')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read actual exponent shifts,products,substitution roots and increasing/decreasing graph arrows. Independently solve source log-linear conditions and quadratic substitutions;compare source final3sf displays after exact recovery.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='EveryExample12–16/Try12–14/Try15Q1–4 and ten method/graph panels enumerated. Q4starts419as an independently numbered task,not a continuation ofQ3.',scope_screen='Common-log solving and positive substitutions;preserve reciprocal-base inequality direction and exact internal cutoffs.')for page in range(417,420)]
def save():
 for name,data in [('answers-YM-C9-exponential-opening.json',dict(scope='Complete417–419source responses and strict inequality semantics.',items=answers)),('census-YM-C9-exponential-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete417–419page/item/reference census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    got=compute(op)
    if name in p.get('additional_operation_expected',{}):assert equivalent(got,expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
