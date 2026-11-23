"""YM60–63 GP outputs: signed ratios, unique counts and exact threshold neighbours."""
import json
import author_YM_C2_opening as base
from author_YM_C2_opening import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,GPTERM
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]

def add(kind,n,page,note,parts):
 r=base.add(kind,n,page,note,parts,[GPTERM]);corrections.extend(base.corrections[-1:]);return r

def term(label,a,r,n,key,kp):
 return v(label,'('+a+')*('+r+')**(('+n+')-1)',key,kp,
 'Use the original first term '+a+' and common ratio '+r+'. The index '+n+' is a positive integer; retain the sign of a negative ratio and use n−1multiplications. For symbolic domains, retain original nonzero denominators and the book’s nonzero-ratio convention.')

def count(label,a,r,last,key,kp):
 e='expand_log(log(Abs(('+last+')/('+a+'))),force=True)/expand_log(log(Abs('+r+')),force=True)+1'
 p=v(label,e,key,kp,'Derive n from magnitudes using the exact nonzero first term and ratio with |r|≠1, then verify that n is a positive integer and the SIGNED original term reaches the stated endpoint. Logarithms of a negative ratio are not used in a real computation.')
 p['additional_operations']={'signed_endpoint_residual':{'kind':'identity','operands':['('+a+')*('+r+')**(('+e+')-1)-('+last+')']}};p['additional_operation_expected']={'signed_endpoint_residual':'0'}
 return p

def threshold(label,a,r,bound,key,kp,relation):
 e='floor(log(('+bound+')/('+a+'))/log('+r+')+1)+1'
 p=v(label,e,key,kp,'The original positive GP is monotone with ratio '+r+'. Solve its requested strict '+relation+' threshold, reversing the inequality when dividing by a negative logarithm. Select the least integer usingfloor(threshold)+1, then check the previous term and the selected term exactly.')
 p['additional_operations']={'previous_term':{'kind':'identity','operands':['('+a+')*('+r+')**(('+e+')-2)']},'selected_term':{'kind':'identity','operands':['('+a+')*('+r+')**(('+e+')-1)']}}
 return p

add('Example',9,60,'Find T7 andT10 of12,−4,4/3,… . The stem/working values fix first term12 despite a copied row printing2.',[
 term('T7','12','-4/12','7','Rational(4,243)',60),term('T10','12','-4/12','10','-Rational(4,6561)',60)])
ps=[]
for label,a,r,outs in [('a','9','3/9',[('T6','6','Rational(1,27)'),('T8','8','Rational(1,243)')]),('b','2','-6/2',[('T9','9','13122'),('T13','13','1062882')]),('c','1','Rational(1,3)',[('T5','5','Rational(1,81)'),('T13','13','Rational(1,531441)')])]:
 ps.extend(term(label+'-'+l,a,r,n,k,592)for l,n,k in outs)
add('Try-Now',9,60,'Compute both requested terms in each of three GPs, including alternating signs and small exact reciprocal powers.',ps)
add('Example',10,60,'For1,−1/2,1/4,−1/8,…, find T9 and the nth-term formula, preserving the alternating sign.',[
 term('a','1','-Rational(1,2)','9','Rational(1,256)',60),term('b','1','-Rational(1,2)','x','(-Rational(1,2))**(x-1)',60)])
ps=[term('a-i','1','5','7','15625',593),term('a-ii','1','5','x','5**(x-1)',593),
 term('b-i','5','-Rational(1,2)','7','Rational(5,64)',593),term('b-ii','5','-Rational(1,2)','x','5*(-Rational(1,2))**(x-1)',593),
 term('c-i','a**2/(2*b**3)','(a**4/(2*b))/(a**2/(2*b**3))','7','a**14*b**9/2',593),
 term('c-ii','a**2/(2*b**3)','(a**4/(2*b))/(a**2/(2*b**3))','x','a**2*(a**2*b**2)**(x-1)/(2*b**3)',593)]
r=add('Try-Now',10,61,'Find T7 and nth formulas for three GPs. The symbolic sequence has original b≠0 and nondegenerate ratio conditiona≠0 under this book’s convention.',ps)
r['source_interpretation']='In(c), b≠0 from printed denominators. For the quotient derivation/nonzero-ratio GPconvention usea≠0; ata0 the displayed terms are all0and do not identify a unique common ratio. Record the nondegenerate branch explicitly rather than cancel a zero factor silently.'
p=reasoning('term-count','n5ify≠0andy²≠11. Aty²11the constant sequence does not determine a unique finite length.',
 'The original denominators requirey≠0. First terma=y²/11 andr=11/y²>0. The endpoint1331/y⁶ equalsa r⁴, so n5is a valid position. Inferring n−1=4from equal powers additionally requiresr≠1. Aty=±√11, every displayed value and the final value are1, so arbitrarily many constant terms satisfy the same description. The printed unique answer lacks that exception.',61,'key incomplete')
p['additional_operations']={'fifth_term_identity':{'kind':'identity','operands':['simplify((y**2/11)*(11/y**2)**4-1331/y**6)']},'unit_ratio_branch':{'kind':'identity','operands':['Tuple((sqrt(11)**2)/11,11/(sqrt(11)**2),1331/(sqrt(11)**6))']}}
p['additional_operation_expected']={'fifth_term_identity':'0','unit_ratio_branch':'Tuple(1,1,1)'}
add('Example',11,61,'Determine the term count ofy²/11,1,11/y²,…,1331/y⁶. The endpoint index is unique only when the common ratio is not1.',[p])
ps=[count('a','3','2','192','7',593),count('b','Rational(19,4)','4','19456','7',593),count('c','-Rational(17,3)','-Rational(3,2)','Rational(37179,384)','8',593)]
add('Try-Now-11',1,61,'Find three finite GPterm counts; the negative-ratio case requires checking the endpoint sign after using magnitudes.',ps)
for n,note,a,r,last,key in [(2,'Find the index of458752in7,14,28,… .','7','2','458752','17'),(3,'Find the index of3/4in384,192,96,… .','384','Rational(1,2)','Rational(3,4)','10'),(4,'Find the index of3+13/81in54,36,24,… .','54','Rational(2,3)','3+Rational(13,81)','8')]:
 add('Try-Now-11',n,61,note,[count('index',a,r,last,key,593)])
p=threshold('first-index','128','Rational(1,2)','Rational(1,25)','13',62,'less-than')
p['additional_operation_expected']={'previous_term':'Rational(1,16)','selected_term':'Rational(1,32)'}
add('Example',12,62,'Find the first term below0.04in128,64,32,…; preserve the strict logarithmic inequality and check adjacent exact terms.',[p])
ps=[]
for label,a,r,bound,key,relation in [('a','3','2','1000','10','greater-than'),('b','59049','Rational(1,3)','Rational(1,100)','16','less-than'),('c','Rational(19,4)','4','10000','7','greater-than'),('d','Rational(4,3)','Rational(2,3)','Rational(1,100)','14','less-than')]:
 p=threshold(label,a,r,bound,key,593,relation)
 if label=='d':
  p['additional_operation_expected']={'previous_term':'Rational(16384,1594323)','selected_term':'Rational(32768,4782969)'}
  p['source_reading_clarification']='Printed keyn14is correct. The handwritten13is not publisher evidence: term13≈0.010276exceeds0.01, while term14≈0.006851is below it.'
 ps.append(p)
add('Try-Now',12,62,'Find first strict threshold indices for four increasing/decreasing GPs. The printed14in(d)is confirmed; a handwritten13is rejected.',ps)
ps=[v('a-ratio-first','Tuple(real_root(192/(-24),3),(-24)/(real_root(192/(-24),3))**3)','Tuple(-2,3)',63,
 'T7/T4=r³=192/(−24)=−8; take the real cube root−2, then a=T4/r³=3. The odd index gap fixes the sign uniquely.'),
 v('b-first-three','Tuple(3,3*(-2),3*(-2)**2)','Tuple(3,-6,12)',63,'Use the same independently recovereda3,r−2, preserving alternating signs.')]
add('Example',13,63,'FromT4−24andT7=192, recover ratio/first term and first three terms. An odd term-index gap determines a negative ratio uniquely.',ps)
ps=[v('a-ratio-first','Tuple(real_root(486/18,3),18/real_root(486/18,3)**2)','Tuple(3,2)',593,
 'T6/T3=r³=27 gives realr3; T3=a r²=18 givesa2. Neither term iszero.'),v('b-first-three','Tuple(2,2*3,2*3**2)','Tuple(2,6,18)',593,'Substitutea2,r3into the first three terms and confirm the original third/sixth constraints.')]
add('Try-Now-13',1,63,'Recover the GPfrom6th term486and3rd term18, then list its first three terms.',ps)
p=reasoning('a-ratio-first','Forx≠0,r5xanda=x². Atx0,the terms are allzero and the ratio is not uniquely determined.',
 'OriginalT4=5³x⁵andT7=5⁶x⁸. Fornonzerox,the quotient givesr³=5³x³, hence realr5x; a=T4/r³=x². Atx0both given terms vanish. With the book’s r≠0 convention this forcesa0but leavesr arbitrarynonzero; the printedr0does not represent a unique ratio and violates that convention. The source needs a nonzero parameter condition for its intended branch.',593,'key incomplete')
p['additional_operations']={'nonzero_branch_original_residuals':{'kind':'identity','operands':['Tuple(p**2*(5*p)**3-5**3*p**5,p**2*(5*p)**6-5**6*p**8)']},'zero_given_terms':{'kind':'identity','operands':['Tuple(5**3*0**5,5**6*0**8)']}}
p['additional_operation_expected']={'nonzero_branch_original_residuals':'Tuple(0,0)','zero_given_terms':'Tuple(0,0)'}
p2=v('b-first-three','Tuple(p**2,p**2*(5*p),p**2*(5*p)**2)','Tuple(p**2,5*p**3,25*p**4)',593,
 'On the intended nonzero sourcexbranch, first terms arex²,5x³,25x⁴. Checker p denotes that originalx. Atx0the first term0andany nonzero ratio yield first three terms0,0,0, so these term formulas remain valid even though part(a)’s ratio is not uniquely identified.')
add('Try-Now-13',2,63,'Recover a symbolic GPfromtwo power-valued terms, retaining the missingx≠0condition and distinguishing unique ratio from still-valid zero term formulas.',[p,p2])
# Derive both correlated branches directly from the consecutive-term equation.
original='(x+2)**2-(x-4)*(3*x+1)'
p=v('a-ratios','FiniteSet(*[(q+2)/(q-4) for q in solveset('+original+',x,domain=S.Reals)])','FiniteSet(-Rational(1,3),Rational(5,2))',593,
 'Consecutive termsT4=x−4,T5=x+2,T6=3x+1give(x+2)²=(x−4)(3x+1), withx8or−1/2. Their ratios are5/2and−1/3; neither fourth term iszero.')
p2=v('b-first-terms','FiniteSet(*[(q-4)/(((q+2)/(q-4))**3) for q in solveset('+original+',x,domain=S.Reals)])','FiniteSet(Rational(32,125),Rational(243,2))',593,
 'For each samexbranch, a=T4/r³. x8 gives(r,a)=(5/2,32/125); x−1/2 gives(−1/3,243/2). Keep those pairs rather than independent sign/value choices.')
r=add('Try-Now-13',3,63,'Determine both possible ratios and first terms fromthree consecutive algebraic GPterms. Preserve their correlated branches.',[p,p2]);r['correlated_branch_check']={'required_pairs':[['5/2','32/125'],['-1/3','243/2']],'reason':'Each first term must use the ratio recovered from the same originalxvalue.'}
refs=[
 (10,60,'GPgeneral-term reference','Tn=a r^(n−1), with positive-integern. The source explicitly choosesr≠0. Ratio-by-division also needs nonzero previous terms; a zero sequence does not identify a unique ratio.',[GPTERM],'table',[],None),
 (11,60,'Example9 copied first-term row','The stem says12,−4,4/3andthe derivation usesa12,r−1/3. The copied term row prints2,−4,4/3,which is not the same GP. Both final requested answers are correct from the stem.',[GPTERM],'table',[('Tuple(12*(-Rational(1,3))**6,12*(-Rational(1,3))**9)','Tuple(Rational(4,243),-Rational(4,6561))')],'Example:9'),
 (12,61,'Example11 same-base exponent step','Equating(11/y²)^4with(11/y²)^(n−1) impliesn5only wheny≠0andy²≠11. Unit base1loses index uniqueness, even thoughn5remains one valid position.',[GPTERM],'table',[('simplify((y**2/11)*(11/y**2)**4)','1331/y**6')],'Example:11'),
 (13,62,'Example12 classify-before-index note','The source asks the reader to establish AP/GPstructure before using its term formula. A finite prefix alone does not prove an arbitrary infinite continuation; within the intended pattern,128,64,32has ratio1/2.',[GPTERM],'table',[('Tuple(64/128,32/64)','Tuple(Rational(1,2),Rational(1,2))')],'Example:12'),
 (14,62,'Example12 negative-log sign change','Forr1/2, ln(r)<0. Dividing the logarithmic inequality reverses its direction before selecting the least integer. Keep an exact internal threshold instead of rounding it before comparison.',[GPTERM],'table',[],'Example:12'),
 (15,63,'Example13 quotient of term equations','DivideT7byT4to removera’s shared first-term factor: r³=−8. The supplied nonzeroT4justifies the quotient; the real cube root uniquely fixesr−2.',[GPTERM],'table',[('192/(-24)','-8')],'Example:13')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={60:'Every Example9/10andTry9output recorded, with general-term reference and copied term-row typo. Both negative-ratio final answers are checked from the stem.',61:'Every Try10/11output andExample11recorded. Nonzero symbolic denominator/ratio domains, negative endpoint parity and unit-ratio nonunique count are explicit.',62:'Every Example12/Try12threshold output and both method callouts recorded. Exact adjacent terms confirm printed14in(d),clearing the handwritten13lead.',63:'Every Example13andTry13Q1–3output recorded. Odd-gap ratios, symbolic zero ambiguity and correlated two-branch first terms retained. Remaining Try13questions start on64andare not claimed here.'}
pages=[]
for page in range(60,64):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All GPterm/index/parameter work accounted for. Actual nonzero and unit-ratio exceptions are explicit; no convergence or finite-sum demand is inferred from a term-only task.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-GP.json',{'scope':'Every60–63original response with signed/threshold/zero/unit-ratio conditions.','items':answers}),('census-YM-C2-GP.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete60–63page census;laterTry13questions pending.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
