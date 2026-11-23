"""YM56–59 AP outputs: exact indices, strict thresholds and zero-parameter cases."""
import json
import author_YM_C2_opening as base
from author_YM_C2_opening import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=base.corrections

def add(kind,n,page,note,parts):
 return base.add(kind,n,page,note,parts,[APTERM])

def term(label,a,d,n,key,kp):
 return v(label,'('+a+')+(('+n+')-1)*('+d+')',key,kp,
 'Use the original first term '+a+' and consecutive difference '+d+'. The requested index '+n+' counts one fewer increments. Evaluate exactly; n is a positive integer for an actual sequence position. A symbolic nth-term formula is not a sum formula.')

def count(label,a,d,last,key,kp):
 p=v(label,'solve(('+a+')+(x-1)*('+d+')-('+last+'),x)[0]',key,kp,
 'Solve the endpoint equation from original first term '+a+', difference '+d+' and last term '+last+'. Verify that the resulting n is a positive integer; a noninteger algebraic solution would not define a term count.')
 return p

def ap_solution(eqs):return 'solve(['+','.join(eqs)+'],(a,b),dict=True)[0]'
def system_value(label,eqs,output,key,kp,method):
 return v(label,'('+output+').subs('+ap_solution(eqs)+')',key,kp,
 method+' Checker a is the first term and b the common difference. Form the equations directly from the source term constraints, solve them together, then substitute the same pair into the requested output; the printed key is not used to form that system.')

for n,note,a,d,outputs in [
 (1,'Find T25 of21,18,15,12,…; the progression is decreasing.','21','18-21',[('T25','25','-51')]),
 (2,'Find T8 and T14 of−12,−8,−4,…; the first term is negative but the difference positive.','-12','-8-(-12)',[('T8','8','16'),('T14','14','40')]),
 (3,'Find T5 and T12 of2,8,14,20,… from its common difference6.','2','8-2',[('T5','5','26'),('T12','12','68')])]:
 add('Try-Now-3',n,56,note,[term(l,a,d,i,k,592)for l,i,k in outputs])
add('Example',4,56,'For2,−1/2,−3,…, determine T10 and the nth-term expression with exact half-integer difference.',[
 term('a','2','-Rational(1,2)-2','10','-Rational(41,2)',56),term('b','2','-Rational(1,2)-2','x','Rational(9,2)-Rational(5,2)*x',56)])
ps=[]
for l,a,d,k19,kn in [('a','11','17-11','119','6*x+5'),('b','-4','1-(-4)','86','5*x-9'),('c','-33','-29-(-33)','39','4*x-37'),('d','-8','-15-(-8)','-134','-7*x-1'),('e','Rational(1,5)','Rational(3,10)-Rational(1,5)','2','x/10+Rational(1,10)'),('f','16','Rational(31,2)-16','7','-x/2+Rational(33,2)')]:
 ps.extend([term(l+'-i',a,d,'19',k19,592),term(l+'-ii',a,d,'x',kn,592)])
add('Try-Now',4,56,'For all six given APs, determine T19 and the nth-term formula. Increasing/decreasing, decimal and half-integer differences are retained.',ps)
add('Example',5,56,'Count the terms of6,13,20,…,76 by the exact endpoint equation.',[count('n','6','13-6','76','11',56)])
ps=[count('a','104','101-104','-256','121',592),count('b','-4','1-(-4)','56','13',592),count('c','Rational(13,2)','Rational(7,2)-Rational(13,2)','-Rational(53,2)','12',592)]
p=reasoning('d','For a≠0 there are10terms. At a0 the given all-zero terms do not determine a unique length.',
 'The original−5a,−8a,−11a,…,−32a has differenced−3a. Endpoint equation−5a+(n−1)(−3a)=−32a reduces to3a(n−10)=0. Only whena≠0 may it be divided bya to getn10. Ata0 every displayed value is0, and arbitrarily many zero terms fit the same givens. The source/key omit that condition.',592,'key incomplete')
p['additional_operations']={'endpoint_identity':{'kind':'identity','operands':['expand((-5*a+(x-1)*(-3*a))-(-32*a))']},'zero_parameter_endpoint':{'kind':'identity','operands':['(-5*a+(x-1)*(-3*a)+32*a).subs(a,0)']}}
p['additional_operation_expected']={'endpoint_identity':'-3*a*(x-10)','zero_parameter_endpoint':'0'};ps.append(p)
add('Try-Now',5,56,'Count terms in four finite APs, including a symbolic endpoint whose unique count requires a≠0. Do not cancel a possible zero parameter silently.',ps)
p=v('first-index','floor((600-3)/7+1)+1','87',57,
 'For3,10,17,…, solve3+7(n−1)>600, givingn>604/7. The least integer isfloor(604/7)+1=87. This is strict-threshold selection, not rounding to nearest; at an integral threshold plain ceiling would be insufficient.')
p['additional_operations']={'adjacent_terms':{'kind':'identity','operands':['Tuple(3+7*(86-1),3+7*(87-1))']}};p['additional_operation_expected']={'adjacent_terms':'Tuple(598,605)'}
add('Example',6,57,'Find the first APterm greater than600, testing both the chosen term and its predecessor.',[p])
for n,note,a,d,bound,index,pair,relation in [
 (1,'First term greater than80 in5,10,15,… includes the exact-equality predecessor.','5','5','80','17','Tuple(80,85)','greater'),
 (2,'First term exceeding700 in5,14,23,… needs an integer index above a nonintegral bound.','5','9','700','79','Tuple(698,707)','greater'),
 (3,'First term below−200 in−1¾,−3,−4¼,… is in a decreasing fractional AP.','-Rational(7,4)','-Rational(5,4)','-200','160','Tuple(-Rational(797,4),-Rational(401,2))','less')]:
 p=v('first-index','floor((('+bound+')-('+a+'))/('+d+')+1)+1',index,592,
  'Write the original term as '+a+'+(n−1)('+d+'). Apply the requested strict '+relation+' condition, reversing the inequality when dividing by a negative difference. Then select the least admissible positive integer. Check its predecessor to establish that it is the first qualifying term.')
 p['additional_operations']={'adjacent_terms':{'kind':'identity','operands':['Tuple(('+a+')+(('+index+')-2)*('+d+'),('+a+')+(('+index+')-1)*('+d+'))']}};p['additional_operation_expected']={'adjacent_terms':pair}
 add('Try-Now-6',n,57,note,[p])
eqs=['a+7*b+8','a+15*b+32']
add('Example',7,57,'Given T8−8 and T16−32, determine difference and first term, then the first three terms.',[
 system_value('a-difference-first',eqs,'Tuple(b,a)','Tuple(-3,13)',57,'Eight index increments change the value by−24.'),
 system_value('b-first-three',eqs,'Tuple(a,a+b,a+2*b)','Tuple(13,10,7)',57,'Recover the ordered first three terms from the shared AP constants.')])
for n,note,eqs,parts in [
 (1,'Given T19=20.8 andT4=17.8, determine the APconstants and first three terms.',['a+18*b-Rational(104,5)','a+3*b-Rational(89,5)'],[('a','Tuple(b,a)','Tuple(Rational(1,5),Rational(86,5))'),('b','Tuple(a,a+b,a+2*b)','Tuple(Rational(86,5),Rational(87,5),Rational(88,5))')]),
 (2,'Given T4=55 andT10=45, determine the negative difference and first three terms.',['a+3*b-55','a+9*b-45'],[('a','Tuple(b,a)','Tuple(-Rational(5,3),60)'),('b','Tuple(a,a+b,a+2*b)','Tuple(60,Rational(175,3),Rational(170,3))')]),
 (3,'Given T8=31,T16=63 andlast term79, determine the finite term count.',['a+7*b-31','a+15*b-63'],[('n','(79-a)/b+1','20')])]:
 add('Try-Now-7',n,58,note,[system_value(l,eqs,expr,key,592,'Use both original index/value constraints; intermediate a,d values are retained in the derivation.')for l,expr,key in parts])
eqs=['a+4*b-3*(a+b)','a+2*b-10']
add('Example',8,58,'Given T5=3T2 andT3=10, determine first term,difference andT15. The multiplicative relation links full terms, not just differences.',[
 system_value('a',eqs,'a','2',58,'Preserve the entire relationa+4d=3(a+d).'),system_value('b',eqs,'b','4',58,'Use the same simultaneous system.'),system_value('c-T15',eqs,'a+14*b','58',58,'Recover T15 only after fixing both constants.')])
eqs=['a+b-7*(a+2*b)','a+4*b+Rational(11,2)']
add('Try-Now-8',1,58,'Native source says T2 is SEVEN timesT3, withT5−5.5. Determine first term,difference andT10.',[
 system_value('a',eqs,'a','Rational(13,2)',592,'The ratio is seven, not six; the source enlargement confirms the word.'),system_value('b',eqs,'b','-3',592,'Retain both original conditions.'),system_value('c-T10',eqs,'a+9*b','-Rational(41,2)',592,'Use nine increments to reach the10th term.')])
eqs=['a+5*b-19',( 'a+14*b-(a+9*b)-20')]
add('Try-Now-8',2,59,'Given T6=19 andT15 exceedsT10 by20, determine difference,first term and first three terms.',[
 system_value('a',eqs,'b','4',592,'Five common differences account for the20-unit excess.'),system_value('b',eqs,'a','-1',592,'Recover the first term using T6.'),system_value('c',eqs,'Tuple(a,a+b,a+2*b)','Tuple(-1,3,7)',592,'The first three terms use the same solved constants.')])
eqs=['(a+3*b)+(a+7*b)-10','(a+5*b)+(a+11*b)-22']
add('Try-Now-8',3,59,'Use T4+T8=10 andT6+T12=22 to find the first three terms; each equation contains two first terms.',[
 system_value('first-three',eqs,'Tuple(a,a+b,a+2*b)','Tuple(-5,-3,-1)',593,'The two equations are2a+10d10 and2a+16d22; do not lose the factor2on the first term.')])
add('Try-Now-8',4,59,'Determine symbolic nth terms for3,4½,6,… and for(a+b),(a+3b),(a+5b),….',[
 term('a','3','Rational(9,2)-3','x','3*x/2+Rational(3,2)',593),term('b','a+b','(a+3*b)-(a+b)','x','a+b*(2*x-1)',593)])
p=reasoning('b-membership','124is not a term: its algebraic index is31.5, not a positive integer.',
 'For2,6,10,…, Tn=4n−2. Solving4n−2=124 givesn31.5. Sequence positions are positive integers, so no term equals124. The key correctly distinguishes this from the21st term equalling82.',593,'matches')
p['additional_operations']={'algebraic_index':{'kind':'identity','operands':['solve(2+(x-1)*4-124,x)[0]']}};p['additional_operation_expected']={'algebraic_index':'Rational(63,2)'}
add('Try-Now-8',5,59,'Find which term of2,6,10,… equals82 and decide whether124 occurs, enforcing integer membership.',[count('a-index','2','4','82','21',593),p])
p=reasoning('a-positive-count','Only the first5terms are positive.',
 'For14,11,8,…, Tn=17−3n. Strict positivity requiresn<17/3. The positive integer positions are1through5; T5=2 andT6=−1 confirm the boundary. Do not round the fractional threshold to6.',593,'matches')
p['additional_operations']={'boundary_terms':{'kind':'identity','operands':['Tuple(14+(5-1)*(-3),14+(6-1)*(-3))']}};p['additional_operation_expected']={'boundary_terms':'Tuple(2,-1)'}
add('Try-Now-8',6,59,'Count positive terms of14,11,8,…, and determine membership of−310 using an integer index.',[p,count('b-index','14','-3','-310','109',593)])
add('Try-Now-8',7,59,'Given first term3 andT21=103, determine common difference and the nth term.',[
 v('a-difference','(103-3)/(21-1)','5',593,'Twenty increments separate the first and21st terms; divide the100-unit increase by20.'),term('b-nth','3','(103-3)/(21-1)','x','5*x-2',593)])
add('Try-Now-8',8,59,'Count the terms of3,7,11,…,399 and301,298,295,…,−29, preserving the decreasing branch sign.',[
 count('a','3','7-3','399','100',593),count('b','301','298-301','-29','111',593)])
p=v('x-values','solveset(x+14*(3*x-x)-x**2,x,domain=S.Reals)','FiniteSet(29)',593,
 'The original AP startsx,3x, so its common difference is2x andT15=29x. Equating to the statedx² givesx(x−29)=0. Bothx0 and29are valid: x0 is the all-zero AP withT15=x²0. No nonzero or nonconstant restriction is printed. The key omits0.')
p['difference_disposition']='key incomplete';p['difference_reason']='Valid zero/constant AP branch omitted.';p['author_expected_normalised']='FiniteSet(0,29)'
add('Try-Now-8',9,59,'Find all x for the APx,3x,… whose15th term isx². The zero-progression branch is valid and missing from the key.',[p])
p=v('common-difference','24/(13-1)','12',593,
 'Native source says the13th term isy+24, with first termy. Therefore12d24, so d2. The printed key gives12, confusing the index gap with the difference. Direct substitution with d12 would makeT13=y144, contradicting the giveny24.')
p['author_expected_normalised']='2'
add('Try-Now-8',10,59,'Determine d from first termy and13th termy+24; source/key native readings confirm a wrong printed difference.',[p])
add('Try-Now-8',11,59,'Given differenced2 andT48=99, recover the first term using47increments.',[v('first-term','99-(48-1)*2','5',593,'T48=a+47d, so a99−94=5. Check the original48th term.')])
eqs=['a+7*b-150','a+52*b+30']
add('Try-Now-8',12,59,'Given T8=150 andT53−30, determine first term and common difference from45increments.',[
 system_value('first-and-difference',eqs,'Tuple(a,b)','Tuple(178,-4)',593,'The−180change over45increments givesd−4; thena178.')])
refs=[
 (6,56,'Fractional AP index formula','For2,−1/2,−3,…, a2,d−5/2,Tn9/2−5n/2. The source compares numericT10 with symbolic nth form; these are different outputs from the same sequence.',[APTERM],'table',[('2+(x-1)*(-Rational(5,2))','Rational(9,2)-5*x/2')],'Example:4'),
 (7,57,'Strict threshold round-up callout','The source usesn>604/7 and87as the first term index. In general forstrictn>t usefloor(t)+1; ceiling alone fails when t is already an integer. The source’s particular noninteger example is correct.',[APTERM],'table',[('floor(Rational(604,7))+1','87')],'Example:6'),
 (8,57,'Two-term AP simultaneous-equation layout','T8−8,T16−32 givea+7d−8,a+15d−32. Subtracting removes the shared first term and yields8d−24.',[APTERM],'table',[('expand((a+15*b)-(a+7*b))','8*b')],'Example:7'),
 (9,58,'Whole-term multiplier equation layout','T5=3T2 meansa+4d=3(a+d), not3a+d. Combined withT3=10 this givesa2,d4.',[APTERM],'table',[('expand((a+4*b)-3*(a+b))','-2*a+b')],'Example:8')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={56:'Every Try3/4/5 output and Examples4/5 recorded, including all six nth-term pairs and the symbolic zero-parameter endpoint ambiguity. Fractional APformula reference retained.',57:'Every Example6/7 and three independent Try6 questions recorded. Strict-threshold predecessor checks, noninteger-index selection and two-term system layout retained.',58:'Every Try7 task, Example8 and Try8Q1 recorded. Native reading confirms SEVEN timesT3, clearing a six-times transcription lead. The whole-term multiplier layout is retained.',59:'Every Try8Q2–12output recorded, with exact key-page592/593 split. Membership, zero progression, wrong keyd12and index positivity are explicit.'}
pages=[]
for page in range(56,60):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All APterm/index/parameter tasks and source method callouts recorded. Actual indices are positive integers; symbolic coefficient cancellation and zero progressions have explicit domain dispositions.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-AP.json',{'scope':'Every56–59original output, with integer/strict/zero boundaries.','items':answers}),('census-YM-C2-AP.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete56–59page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
