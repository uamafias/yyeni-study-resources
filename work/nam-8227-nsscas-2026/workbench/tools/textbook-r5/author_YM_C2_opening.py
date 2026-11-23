"""YM52–55: exact AP/GP recognition, parameter pairs and first general terms."""
import hashlib,json
import author_YM_C1_opening as opening
from author_YM_C1_opening import W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
AP='8227:2020:M1:T2:O02:D01';GP='8227:2020:M1:T2:O02:D02';APTERM='8227:2020:M1:T2:O03:D01';GPTERM='8227:2020:M1:T2:O03:D02'

def ev(page):
 name='YM-C1-end-keys-590-source'if 590<=page<=593 else f'YM-C2-{52+4*((page-52)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
opening.base.ev=ev

def add(kind,n,page,note,parts,direct,components=None):
 r=opening.add(kind,n,page,note,parts,direct,components=components or[])
 r['item_id']=r['item_id'].replace(':YM:C1:',':YM:C2:');prior=new.pop();prior['item_id']=r['item_id']
 corrections.append({k:prior[k]for k in ['item_id','pdf_page','printed_page','continuation_pdf_pages']})
 r['mapping_rationale']='Recognising a fixed difference/ratio is assessed when explicitly requested; using that definition to find a parameter or term assesses the corresponding progression output. Quadratic parameter solving and logarithm laws are components, not invented independent assessed goals. A finite displayed prefix alone does not prove a unique continuation rule.'
 r['precision_angle_check']={'source':'Exact integers,rational decimals and symbolic parameters; no angle units.','comparison':'Treat source decimals exactly. Sequence indices are positive integers; ratio-by-division requires a nonzero previous term, while a zero sequence can still satisfy a multiplicative recurrence.'}
 return r

def classify(label,conclusion,method,kp,expr,key):
 p=reasoning(label,conclusion,method,kp,'matches')
 p['additional_operations']={'consecutive_test':{'kind':'identity','operands':[expr]}};p['additional_operation_expected']={'consecutive_test':key}
 return p

ps=[classify('a','AP with common difference9.','The consecutive differences21−12,30−21,39−30 all equal9. The displayed intended arithmetic pattern is consistent; finite data alone does not fix every future term without the stated pattern context.',54,'Tuple(21-12,30-21,39-30)','Tuple(9,9,9)'),
 classify('b','GP with common ratio1/5=0.2.','The exact successive ratios2/10,0.4/2,0.08/0.4 all equal1/5; every denominator is nonzero. Differences are not constant.',54,'Tuple(2/10,Rational(4,10)/2,Rational(8,100)/Rational(4,10))','Tuple(Rational(1,5),Rational(1,5),Rational(1,5))')]
add('Example',1,54,'Classify the two supplied numeric sequences and determine their common difference or ratio, using exact values.',ps,[AP,GP])
ps=[]
for l,kind,terms,result in [('a','GP',['4','6','9','Rational(27,2)'],'Rational(3,2)'),('b','AP',['250','244','238','232'],'-6'),('c','AP',['Rational(17,100)','Rational(49,100)','Rational(81,100)','Rational(113,100)'],'Rational(8,25)'),('d','AP',['5','-2','-9','-16'],'-7')]:
 tests=[f'({terms[i+1]})/({terms[i]})'if kind=='GP'else f'({terms[i+1]})-({terms[i]})'for i in range(3)]
 ps.append(classify(l,kind+' with '+('ratio 'if kind=='GP'else'difference ')+result+'.',
  'Check every displayed consecutive '+('ratio with nonzero denominator'if kind=='GP'else'difference')+'. The source asks both classification and the common value. Exact decimal arithmetic avoids a false rounding discrepancy.',592,'Tuple('+','.join(tests)+')','Tuple('+','.join([result]*3)+')'))
add('Try-Now',1,54,'Classify all four numeric sequences, including decimal common difference0.32 and a sign-changing arithmetic progression.',ps,[AP,GP])
ps=[v('y','solve((4*x-(x+2))-((6*x+4)-4*x),x)[0]','6',54,'Set the two AP differences equal:3y−2=2y+4, hencey6.'),
 v('first-three-terms','Tuple(6+2,4*6,6*6+4)','Tuple(8,24,40)',54,'Substitute the independently derivedy6 into each original term, in order. Consecutive differences are both16; do not confuse that difference with the parameter6.')]
add('Example',2,54,'Determine y so y+2,4y,6y+4 form an AP, then report the first three terms.',ps,[APTERM])
p=v('parameter-values','solveset((2*x+2)**2-(7*x+1)*(x-1),x,domain=S.Reals)','FiniteSet(-Rational(1,3),5)',592,
 'The GP condition is(2a+2)²=(7a+1)(a−1). Expanding gives3a²−14a−5=0, witha−1/3 or5. Neither first term vanishes, so the original ratio test is legitimate. At−1/3 the terms alternate−4/3,4/3,−4/3 withr−1; at5 they are36,12,4 withr1/3.')
p['additional_operations']={'first-branch-terms':{'kind':'identity','operands':['Tuple(7*(-Rational(1,3))+1,2*(-Rational(1,3))+2,-Rational(1,3)-1)']},'second-branch-terms':{'kind':'identity','operands':['Tuple(7*5+1,2*5+2,5-1)']}}
p['additional_operation_expected']={'first-branch-terms':'Tuple(-Rational(4,3),Rational(4,3),-Rational(4,3))','second-branch-terms':'Tuple(36,12,4)'}
add('Try-Now-2',1,54,'Find both a-values making7a+1,2a+2,a−1 a GP. Retain the negative-ratio branch and verify its original terms.',[p],[GPTERM],components=[opening.QUAD])
p=v('correlated-pairs','FiniteSet(*solve([2*x-y-2,y**2-9*x],(x,y)))','FiniteSet(Tuple(Rational(1,4),-Rational(3,2)),Tuple(4,6))',592,
 'For2,a,b,9, the first three AP terms requireb=2a−2; the last three GP terms requireb²=9a. Solve jointly, retaining(a,b)=(1/4,−3/2),(4,6). Botha-values are nonzero; ratios are−6 and3/2 respectively. Never chooseaandb independently from their separate two-element lists.')
r=add('Try-Now-2',2,54,'Determine the correlated a,b pairs where the first three of2,a,b,9 form an AP and the last three form a GP.',[p],[APTERM,GPTERM],components=[opening.QUAD]);r['correlated_branch_check']={'required_pairs':[['1/4','-3/2'],['4','6']],'reason':'The AP and GP conditions hold jointly for the same ordered parameter pair.'}
ps=[classify('a','GP, with a valid multiplicative ratio1/2. Atx0 the all-zero sequence is also an AP; quotient testing is then undefined.',
 'The original termsx/2,x/4,x/8,x/16 satisfy next=(1/2)previous identically, includingx0. Forx≠0 all ratios equal1/2. The key’s GP classification is valid, but it should not imply division by zero or exclusive classification in the zero case.',592,'Tuple(x/4-x/2/2,x/8-x/4/2,x/16-x/8/2)','Tuple(0,0,0)'),
 classify('b','AP with common difference−4b.',
 'For a+5b,a+b,a−3b, both consecutive differences are−4b. This remains an AP whenb0, although a constant sequence may also be geometric. The key does not require an exclusive classification.',592,'Tuple((a+b)-(a+5*b),(a-3*b)-(a+b))','Tuple(-4*b,-4*b)'),
 classify('c','GP with ratio−1/x; originalx≠0.',
 'The fourth term−1/x excludesx0. The ratios ofx²,−x,1,−1/x are all−1/x. At special parameters the sequence may also be constant/AP, without invalidating the GP classification.',592,'Tuple((-x)/(x**2),1/(-x),(-1/x)/1)','Tuple(-1/x,-1/x,-1/x)'),
 classify('d','GP with ratio2; originaly≠0.',
 'The four terms2/y,4/y,8/y,16/y all requirey≠0; each nonzero consecutive ratio is2. Keep that source-domain condition.',592,'Tuple((4/y)/(2/y),(8/y)/(4/y),(16/y)/(8/y))','Tuple(2,2,2)')]
add('Try-Now-2',3,55,'Classify four symbolic sequences, preserving denominator restrictions and the zero/constant cases where classification need not be exclusive.',ps,[AP,GP])
ps=[v('a-AP-p','solve((2*log(2)-log(2))-(x*log(2)-2*log(2)),x)[0]','3',592,
 'Forlog2,log(2²),log(2^p), writeL=log2≠0. TermsL,2L,pL have equal differences only ifp3. The positive-base logarithm law is a component, not a separate requested log-equation goal.'),
 v('b-GP-p','solve((2*log(2))**2-log(2)*(x*log(2)),x)[0]','4',592,
 'With the same nonzeroL, the GP condition(2L)²=L(pL) givesp4. The resulting termsL,2L,4L have ratio2.')]
add('Try-Now-2',4,55,'Find p separately for AP and GP structure in the three supplied powers-of2 logarithms. The two structural requirements give different parameters.',ps,[APTERM,GPTERM])
ps=[v('sixth','3+(6-1)*5','28',55,'Read first term3 and common difference5; index6 requires five increments, not six.'),v('thirteenth','3+(13-1)*5','63',55,'Use the same AP and12increments to reach index13; the source’s original terms3,8,13,18 agree.')]
add('Example',3,55,'Find the6th and13th terms of3,8,13,18,… using the positive-integer index convention.',ps,[APTERM])
refs=[
 (1,53,'Even-number term arrows','The displayed2,4,6,8 are labelledn1,2,3,4, with+2arrows. An infinite intended rule is distinct from a finite prefix or a bounded list ending at20.',[AP],'diagram',[('Tuple(4-2,6-4,8-6)','Tuple(2,2,2)')],None),
 (2,53,'Common-difference reference','APd=Tn−T(n−1), with examples2,5,8,11(d3) and3,−1,−5,−9(d−4). The previous term exists only forn≥2; index1is the first term.',[AP],'table',[('Tuple(5-2,8-5,-1-3,-5-(-1))','Tuple(3,3,-4,-4)')],None),
 (3,53,'Common-ratio reference','For nonzero previous terms, GPr=Tn/T(n−1). The examples1,2,4,8and81,27,9,3have ratios2and1/3. Multiplicative recurrence also covers a zero sequence, where division is unavailable.',[GP],'table',[('Tuple(2/1,4/2,27/81,9/27)','Tuple(2,2,Rational(1,3),Rational(1,3))')],None),
 (4,55,'Term-index weight illustration','The three figures carry values10,15,20 and labelsfirst/second/thirdterm,n1,2,3. They illustratea10,d5; no mass unit is specified, so no invented physical unit or measurement is asserted.',[APTERM],'diagram',[('Tuple(15-10,20-15)','Tuple(5,5)')],None),
 (5,55,'AP general-term formula','Tn=a+d(n−1) uses positive-integern. The first term has zero increments. This is a term formula, not a finite-sum formula.',[APTERM],'table',[('simplify(a+b*(1-1))','a')],None)]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={52:'Chapter title, scope list and biographical portrait only; no exercise, worked mathematical example, boxed learner prompt or mathematical teaching diagram. The portrait is not a quantitative problem asset.',53:'Introduction, finite/infinite sequence discussion, term-index arrows and AP/GP definitions/examples all accounted for. Three mathematical reference figures recorded; no learner response starts here.',54:'Every Example1/Try1 and Example2 response, plus first two independently numbered Try2 questions recorded. Both GP parameter branches and correlated AP/GP pairs retained.',55:'Both remaining Try2 questions, term-index illustration, APterm formula and Example3 recorded. Source algebraic domains and positive-integer indexing are explicit.'}
pages=[]
for page in range(52,56):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated'if ids else'prose only','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All opening AP/GP definitions, tasks and mathematical illustrations recorded. Common-base logarithm manipulation and quadratic parameter algebra are components; no convergence or finite-sum demand is invented here.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-opening.json',{'scope':'Every52–55original learner response, including symbolic/zero-domain cases.','items':answers}),('census-YM-C2-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete52–55source census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
