"""YM64–67 GPbranches and finiteAPsums; fixed source audit, not runtime generation."""
import hashlib,json
import author_YM_C2_opening as base
import author_YM_C2_GP as gp
import author_YM_C2_AP as ap
from author_YM_C2_opening import opening,W,SRC,SHA,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]

def ev(page):
 name='YM-C2-keys-594-source'if 594<=page<=597 else'YM-C1-end-keys-590-source'if 590<=page<=593 else f'YM-C2-{52+4*((page-52)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return{'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
opening.base.ev=ev

def add(kind,n,page,note,parts,direct):
 r=base.add(kind,n,page,note,parts,direct);corrections.extend(base.corrections[-1:]);return r

def asum(label,a,d,n,key,kp):
 return v(label,'summation(('+a+')+(k-1)*('+d+'),(k,1,'+n+'))',key,kp,
 'Independently sum the original term expression '+a+'+(k−1)('+d+') for integerk1through'+n+'. Compare with the separately transcribed key; the number of terms is not the last term’s value. The closedAPformula is an alternative check, not the computation input here.')

def sum_count(label,a,d,total,key,kp):
 expr='Intersection(solveset(x*(2*('+a+')+(x-1)*('+d+'))/2-('+total+'),x,domain=S.Integers),S.Naturals)'
 p=v(label,expr,key,kp,'Form the finiteAPsum from the original first term '+a+', difference '+d+' and target '+total+'. Solve in the integers and retain positive indices. Preserve every admissible positive root; a sum need not be monotone if terms change sign.')
 p['additional_operations']={'all_real_candidates':{'kind':'real-roots','operands':['x*(2*('+a+')+(x-1)*('+d+'))/2-('+total+')']}}
 return p

ps=[v('first-ratio','Tuple((-4)/(1+real_root(108/(-4),3)),real_root(108/(-4),3))','Tuple(2,-3)',593,
 'Originala(1+r)=−4and ar³(1+r)=108. The first sum is nonzero, justifying division to obtainr³−27andrealr−3; thena2. A negative ratio is admissible.')]
add('Try-Now-13',4,64,'Recover a,r from first-two sum−4andfourth-plus-fifth sum108, preserving the shared full-term factor.',ps,[GPTERM])
ps=[v('a-first-three','Tuple(4,4*(-Rational(3,4)),4*(-Rational(3,4))**2)','Tuple(4,-3,Rational(9,4))',593,'Use originala4,r−3/4without dropping alternating signs.'),
 v('b-first-three','Tuple(162/(-3)**3,162/(-3)**2,162/(-3))','Tuple(-6,18,-54)',593,'Work backward fromT4=162withr−3. Nonzero ratio permits division for the earlier terms.'),
 v('c-first-three','Tuple(7*Rational(1,2)**1,7*Rational(1,2)**2,7*Rational(1,2)**3)','Tuple(Rational(7,2),Rational(7,4),Rational(7,8))',593,'The supplied nth formula is7(1/2)^n, so first term usesn1, notn0.'),
 v('d-first-three','Tuple(sqrt(6),sqrt(6)*sqrt(Rational(1,2)),sqrt(6)*Rational(1,2))','Tuple(sqrt(6),sqrt(3),sqrt(6)/2)',593,'The source explicitly forbids decimals. Keep exact positive square roots and simplify their products.')]
add('Try-Now-13',5,64,'Find first three terms under four distinct givens: direct a,r; later term/r; nth formula; and exact-surds/no-decimals.',ps,[GPTERM])
add('Try-Now-13',6,64,'Find the positive integer index of1024in1,2,4,… .',[gp.count('index','1','2','1024','11',593)],[GPTERM])
p=v('a-ratios','solveset(x**4-(Rational(64,3)/108),x,domain=S.Reals)','FiniteSet(Rational(2,3))',593,
 'The originalT3=108andT7=21⅓=64/3give r⁴16/81. BOTH real signs±2/3satisfy the original terms, witha108/r²=243. No positive-ratio restriction is printed; do not discard the negative branch.')
p['difference_disposition']='key incomplete';p['difference_reason']='The even index gap admits both real ratio signs.';p['author_expected_normalised']='FiniteSet(-Rational(2,3),Rational(2,3))'
p2=v('a-first','108/((-Rational(2,3))**2)','243',593,'Both admissible ratio signs have the same square4/9, so both require first terma243.')
p3=v('b-first-three','FiniteSet(Tuple(243,243*Rational(2,3),243*Rational(2,3)**2),Tuple(243,243*(-Rational(2,3)),243*(-Rational(2,3))**2))',
 'FiniteSet(Tuple(243,162,108))',593,'Return both correlated sequences243,162,108and243,−162,108. Each originalthird term is108,andwithits same ratio each seventh term is64/3.')
p3['difference_disposition']='key incomplete';p3['difference_reason']='Negative-ratio first-three-term branch omitted.';p3['author_expected_normalised']='FiniteSet(Tuple(243,162,108),Tuple(243,-162,108))'
add('Try-Now-13',7,64,'Recover both real ratios and first-three-term branches from an even term-index gap. The source key omits the negative-ratio branch.',[p,p2,p3],[GPTERM])
p=v('first-three','Tuple(6-4,6,6+12)','Tuple(2,6,18)',593,'The originalGPconditionp²=(p−4)(p+12) givesp6. Substitute into allthreeoriginal terms; none iszero.')
p['additional_operations']={'parameter':{'kind':'identity','operands':['solve(x**2-(x-4)*(x+12),x)[0]']}};p['additional_operation_expected']={'parameter':'6'}
add('Try-Now-13',8,64,'Determine the GPterms fromp−4,p,p+12andthe consecutive ratio condition.',[p],[GPTERM])
add('Try-Now-13',9,64,'Find T11of16/3,−8/3,4/3,…,preserving the alternating ratio.',[gp.term('T11','Rational(16,3)','-Rational(1,2)','11','Rational(1,192)',593)],[GPTERM])
ps=[v('a-ratio-first','Tuple(real_root((6/256)/(-6/32),3),(-6/32)/(real_root((6/256)/(-6/32),3))**5)','Tuple(-Rational(1,2),6)',593,
 'T9/T6=r³=(6/256)/(−6/32)=−1/8. The real cube root is−1/2; thena6fromthe original6th term.'),
 v('b-first-three','Tuple(6,6*(-Rational(1,2)),6*(-Rational(1,2))**2)','Tuple(6,-3,Rational(3,2))',593,'Use the same recovereda6andr−1/2for allthree terms.')]
add('Try-Now-13',10,64,'Recover ratio,first term andfirst three terms from the6th and9th terms of opposite signs.',ps,[GPTERM])
add('Try-Now-13',11,64,'Find the number of terms when the GPstarts3,6andends768; originalratio2is fixed.',[gp.count('n','3','2','768','9',593)],[GPTERM])
add('Example',14,65,'Sum the first20terms of4+7+10+…using the original arithmetic term rule.',[asum('S20','4','7-4','20','650',65)],[APTERM])
ps=[]
for l,a,d,key in [('a','3','8-3','2265'),('b','12','11-12','-75'),('c','-14','-11-(-14)','885'),('d','9','Rational(11,2)-9','-Rational(2505,2)'),('e','25','14-25','-4035'),('f','2','-Rational(1,2)-2','-Rational(2055,2)')]:ps.append(asum(l,a,d,'30',key,593))
add('Try-Now-14',1,65,'Sum the first30terms of six APseries, with positive/negative and fractional differences. A finite total may be negative.',ps,[APTERM])
add('Try-Now-14',2,65,'Sum23terms of(13x−2y)+(10x)+(7x+2y)+…and retain both symbolic contributions.',[
 asum('S23','13*x-2*y','10*x-(13*x-2*y)','23','-460*x+460*y',593)],[APTERM])
add('Try-Now-14',3,65,'Sum22terms ofx/60+x/30+x/20+x/15+…,recognising the equal coefficient increments.',[
 asum('S22','x/60','x/30-x/60','22','Rational(253,60)*x',593)],[APTERM])
p=asum('sum','Rational(1,2)','1','21','Rational(441,2)',66)
p['additional_operations']={'endpoint_count':{'kind':'identity','operands':['solve(Rational(1,2)+(x-1)-Rational(41,2),x)[0]']}};p['additional_operation_expected']={'endpoint_count':'21'}
add('Example',15,66,'Sum1/2+1½+2½+…+20½. The endpoint gives21terms; source’s S20prose label is a typo,while both S21calculations and220.5are correct.',[p],[APTERM])
ps=[]
for l,a,d,n,lastkey,kp in [('a','4','4','8','144',593),('b','Rational(5,4)','Rational(5,4)','10','Rational(275,4)',593),('c','-7','2','17','153',593),('d','20','-3','22','-253',594)]:
 ps.append(asum(l,a,d,n,lastkey,kp));last={'a':'32','b':'Rational(25,2)','c':'25','d':'-43'}[l]
 ps[-1]['additional_operations']={'endpoint_count':{'kind':'identity','operands':['solve(('+a+')+(x-1)*('+d+')-('+last+'),x)[0]']}};ps[-1]['additional_operation_expected']={'endpoint_count':n}
add('Try-Now',15,66,'Sum four APseries with supplied endpoints. Determine each integer term count before summing; the decreasing final branch has a negative total.',ps,[APTERM])
add('Example',16,66,'Find how many terms of15+20+25+…sumto585; discard the negative algebraic candidate.',[sum_count('n','15','5','585','FiniteSet(13)',66)],[APTERM])
for n,note,a,d,total,key in [
 (1,'Find positive integer term counts for7+10+13+…withsum282.','7','3','282','FiniteSet(12)'),
 (2,'Find ALLpositive term counts for−17−15−13−…withsum−17. One term or17terms are both valid.','-17','2','-17','FiniteSet(1,17)'),
 (3,'Find term counts for100+94+88+…withsum574. A second positive real candidate is nonintegral and invalid.','100','-6','574','FiniteSet(7)')]:
 add('Try-Now-16',n,67,note,[sum_count('n',a,d,total,key,594)],[APTERM])
eqs=['6*a+15*b-Rational(111,2)','12*a+66*b-201']
add('Example',17,67,'Fromfirst-six sum55.5andNEXT-six sum145.5,recover common difference andfirst term. The next-block total is not S12byitself.',[
 ap.system_value('difference-first',eqs,'Tuple(b,a)','Tuple(Rational(5,2),3)',67,'The combinedfirst12sumis201. Form separateS6andS12equations.')],[APTERM])
eqs=['10*a+45*b-210','20*a+190*b-820']
add('Try-Now-17',1,67,'Fromfirst10sum210andNEXT10sum610,recover APconstants andfirst three terms using combinedS20=820.',[
 ap.system_value('a-difference-first',eqs,'Tuple(b,a)','Tuple(4,3)',594,'The second block isS20−S10,notanotherfirst10sum.'),ap.system_value('b-first-three',eqs,'Tuple(a,a+b,a+2*b)','Tuple(3,7,11)',594,'Use the same original block-sum constraints to recover allthree terms.')],[APTERM])
refs=[
 (16,65,'Series and finiteAPsum reference','A series adds terms rather than listing them. Forpositive-integern, S_n=n(a+last)/2=n[2a+(n−1)d]/2. An infinite formal series is not automatically a finite convergent sum.',[APTERM,GPTERM],'table',[('simplify(x*(a+(a+(x-1)*b))/2-x*(2*a+(x-1)*b)/2)','0')],None),
 (17,66,'Example15 two-sum-method comparison','The source correctly finds21terms andS21=220.5byboth formulae, but the preceding prose says findS20. Correct only that subscript; the final sum and worked methods are valid.',[APTERM],'table',[('21*(Rational(1,2)+Rational(41,2))/2','Rational(441,2)')],'Example:15'),
 (18,66,'Positive-integer term-count warning','The inverse-sum quadratic inExample16hasn13or−18. Onlypositive-integern13is a count. Other source tasks may have two admissible positive counts,so do not generalise to retaining only one root.',[APTERM],'table',[('expand((x-13)*(x+18))','x**2+5*x-234')],'Example:16'),
 (19,67,'Consecutive block-sum connection','First6sum55.5plusNEXT6sum145.5equalsFIRST12sum201. General second block total isS(2m)−S(m),notS(m)computedfromthe original first term again.',[APTERM],'table',[('Rational(111,2)+Rational(291,2)','201')],'Example:17')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={64:'Every remainingTry13Q4–11output recorded. Even-gap negative-ratio branch restored; exact surds, nth-formula first-index convention and correlated first terms preserved.',65:'EveryExample14andthreeindependentlynumberedTry14tasksrecorded. AllsixnumericAPsumsandtwosymbolicsumsarechecked;series/formulareferencehasanitem.',66:'EveryExample15/16andallfourTry15outputsrecorded. Endpointcountsprecedesums;S20prose typo separatedfromcorrectS21finalresult;positive-integerwarningretained.',67:'EveryTry16Q1–3,Example17andTry17Q1response recorded. Two admissible counts inTry16Q2 are retained; nonintegral/negative candidates filtered by index semantics. Block-sum relation recorded. FurtherTry17questions begin68andremainpending.'}
pages=[]
for page in range(64,68):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Every GPparameter/term andfiniteAPsumtask onthese pagesrecorded. Negative ratios andmultiplepositiveintegercounts remainvalid when the original permits them; no convergence claim is inferred.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-AP-sums.json',{'scope':'Every64–67response,including all valid negative-ratio/positive-count branches.','items':answers}),('census-YM-C2-AP-sums.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete64–67page census;furtherTry17pending.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
