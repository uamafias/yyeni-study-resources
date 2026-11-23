"""YM68–71: block sums, sign-selected terms and finite geometric sums."""
import json
import author_YM_C2_AP_sums as base
import author_YM_C2_AP as ap
import author_YM_C2_GP as gp
from author_YM_C2_AP_sums import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]

def add(kind,n,page,note,parts,direct):
 r=base.base.add(kind,n,page,note,parts,direct);corrections.extend(base.base.corrections[-1:]);return r

def gsum(label,a,r,n,key,kp):
 return v(label,'summation(('+a+')*('+r+')**(k-1),(k,1,'+n+'))',key,kp,
 'Independently sum the original geometric term expression over integer positions1through'+n+'. Retain the sign of ratio '+r+' and compare with the separately transcribed finite total. Both closed forms are equivalent whenr≠1; a unit ratio instead usesna.')

p=reasoning('next-fifteen-sum','Under the author readingS15=375,the requested NEXT15sum is1050; the key gives only intermediatesa4,d3.',
 'The originalT5+T7=38gives2a+10d=38. Reading the printed digit string as375gives15a+105d=375, hencea4,d3. The requested sum isS30−S15=1050, absent from the key. A small mark appears below the7in the scan; if a future native review instead establishes37.5,the same independent equations givea241/4,d−33/4andnext-block sum−7275/4. Preserve the scan limitation and both conditional results rather than using the incomplete key to certify that glyph.',594,'key incomplete')
p['additional_operations']={'primary_reading_constants':{'kind':'identity','operands':['Tuple(solve([2*a+10*b-38,15*a+105*b-375],(a,b))[a],solve([2*a+10*b-38,15*a+105*b-375],(a,b))[b])']},'primary_next_block':{'kind':'identity','operands':['summation(4+(k-1)*3,(k,16,30))']},'alternate_decimal_next_block':{'kind':'identity','operands':['summation(Rational(241,4)+(k-1)*(-Rational(33,4)),(k,16,30))']}}
p['additional_operation_expected']={'primary_reading_constants':'Tuple(4,3)','primary_next_block':'1050','alternate_decimal_next_block':'-Rational(7275,4)'}
r=add('Try-Now-17',2,68,'From a two-term sum andfirst15sum, determine the NEXT15sum. The key stops at intermediate constants; a small scan mark near375is explicitly dispositioned.',[p],[APTERM]);r['source_interpretation']='Author reads375, with a below-baseline scan mark. Preserve the native crop and alternate37.5conditional computation for independent review. The requested block total is missing from the key under either reading; no learner-display reuse is authorised.'
add('Try-Now-17',3,68,'Given APfirst−24,last72andtotal600, find its positive integer length and difference.',[
 v('a-n','2*600/(-24+72)','25',594,'S_n=n(first+last)/2andthe nonzero endpoint sum48give n25. Confirm a positive integer.'),
 v('b-d','(72-(-24))/(25-1)','4',594,'Twenty-four increments span96units, givingd4.')],[APTERM])
p=v('a-d','solve(5*(12+(12+x)+(12+2*x))-((12+20*x)+(12+21*x)+(12+22*x)),x)[0]','3',68,
 'The APhas23terms, so its lastthree arepositions21,22,23. Apply the given five-times relation to the complete first/last blocks, yieldingd3.')
p2=base.asum('b-S17','12','3','17','612',68)
add('Example',18,68,'Given a23term APwith first12andlast-three sum5timesfirst-three sum, finddandS17. One printed substitution uses3instead12but final612is correct.',[p,p2],[APTERM])
p=v('a-show-last-five','summation(a+(k-1)*b,(k,15,19))','5*a+80*b',594,
 'In a19term AP,the lastfive positions are15through19. Sum those original terms directly to establish5a+80d; do not use first-five offsets0through4.')
p['check_mode']='show/prove'
p2=ap.system_value('b-d-first',['a+18*b-52','(5*a+10*b)+(5*a+80*b)-310'],'Tuple(b,a)','Tuple(Rational(7,3),10)',594,
 'The lastterm is52andthe combinedfirst/lastfive total310. Use both original constraints, with separate offsets for the two blocks.')
add('Try-Now-18',1,68,'Establish the symbolic last-five sum, then determine APconstants from its endpoint and two edge-block sums.',[p,p2],[APTERM])
eqs=['8+98*b+8+99*b+8+100*b-3*(8+8+b+8+2*b)','a-8']
p=ap.system_value('a-d',eqs,'b','Rational(1,6)',594,'The101term APhas lastthree offsets98,99,100; preserve the given factor3on the FIRSTthree sum.')
p2=ap.system_value('b-last-forty-eight',eqs,'summation(a+(k-1)*b,(k,54,101))','996',594,
 'The last48positions are54through101; equivalentlyS101−S53. The key’s numeric996is correct, but calling thisS48conflicts with its definition as the FIRST48sum.')
r=add('Try-Now-18',2,68,'Determine d from first/last-three sums of a101term AP, then sum its LAST48terms. Preserve starting position54.',[p,p2],[APTERM]);r['source_label_warning']='The key labels the correct block total996asS48=S101−S53. Under the book’s first-n notation, S48is572; use last48sum orS101−S53 for996.'
p=v('a-total-count','4*floor((91/6)+1)','64',69,
 'Forfirst−91,d6,the nth term is6n−97. Negative positions satisfy n<97/6, giving16negative terms; none iszero because97/6isnotaninteger. Three times asmanypositive terms means48positive terms and64total. A generated branch with azero term would need to count it separately.')
p2=v('b-positive-sum','summation(-91+(k-1)*6,(k,17,64))','7008',69,
 'Sum the actual positive positions17through64, not the first48terms. Their endpoint values5and287 give48(5+287)/2=7008 as a separate endpoint check.')
add('Example',19,69,'From a fixed APwith three times asmanypositive asnegative terms, determine finite length andpositive-term sum. This instance has no zero term.',[p,p2],[APTERM])
p=v('smallest-index','floor(Rational(97,5))+1','20',594,
 'Forfirst−23,d5/2,the PARTIALSUM is n(5n−97)/4. For positiveintegern,it becomes positive only forn>97/5, so20isfirst. This is distinct from the first positive individual term.')
p['additional_operations']={'adjacent_partial_sums':{'kind':'identity','operands':['Tuple(summation(-23+(k-1)*Rational(5,2),(k,1,19)),summation(-23+(k-1)*Rational(5,2),(k,1,20)))']}};p['additional_operation_expected']={'adjacent_partial_sums':'Tuple(-Rational(19,2),15)'}
add('Try-Now-19',1,69,'Find the least index giving apositive partialsum for an APthat starts with negative terms.',[p],[APTERM])
p=v('greatest-count','floor((23+sqrt(23**2+4*3*1800))/(2*3))','28',594,
 'The original APsum is n(3n−23)/4. S_n≤450gives3n²−23n−1800≤0. The positive upperroot is between28and29; retain the greatest integer28, not nearest rounding.')
p['additional_operations']={'adjacent_sums':{'kind':'identity','operands':['Tuple(summation(-5+(k-1)*Rational(3,2),(k,1,28)),summation(-5+(k-1)*Rational(3,2),(k,1,29)))']}};p['additional_operation_expected']={'adjacent_sums':'Tuple(427,464)'}
add('Try-Now-19',2,69,'Find the greatest APterm count whose sum does not exceed450, including the equality convention and integer boundary.',[p],[APTERM])
add('Try-Now-19',3,69,'Find the sum of20APterms with first50andlast10; no common difference is needed.',[
 v('sum','20*(50+10)/2','600',594,'The average of first/last terms is30andthereare20terms; use the endpoint-sum form.')],[APTERM])
add('Try-Now-19',4,69,'Recover APfirst term anddifference fromT3=11andfirst-six sum60.',[
 ap.system_value('first-difference',['a+2*b-11','6*a+15*b-60'],'Tuple(a,b)','Tuple(15,-2)',594,'Use the single-term equation andfinite-sum equation together.')],[APTERM])
add('Try-Now-19',5,69,'Sum the SECONDten terms of4+7+10+…,meaningpositions11through20.',[
 v('block-sum','summation(4+(k-1)*3,(k,11,20))','475',594,'Compute the requested positions directly; equivalentlyS20−S10. Summing positions1through10would answer a different question.')],[APTERM])
eqs=['a+14*b-7','9*a+36*b-18']
add('Try-Now-19',6,70,'UseT15=7andfirst-nine sum18tofindfirst term,difference andT20.',[
 ap.system_value('constants-and-T20',eqs,'Tuple(a,b,a+19*b)','Tuple(0,Rational(1,2),Rational(19,2))',594,'The inferred first term0is valid; do not exclude a zero APfirst term.')],[APTERM])
eqs=['a-2','8*a+28*b-58']
p=ap.system_value('a-d',eqs,'b','Rational(3,2)',594,'First terma2andS8=58fix the difference.')
p2=v('b-count','Intersection(solveset(x*(2*2+(x-1)*Rational(3,2))/2-325,x,domain=S.Integers),S.Naturals)','FiniteSet(20)',594,
 'With the recovered constants, solveS_n325in positive integers. The other real candidate−65/3is not a term count.')
p3=v('c-last-term','2+(20-1)*Rational(3,2)','Rational(61,2)',594,'Use19increments for the20th/last term; it is30.5, not the term count20.')
add('Try-Now-19',7,70,'Recover common difference,whole-series length andlast term fromfirst2,S8=58andtotal325.',[p,p2,p3],[APTERM])
add('Example',20,70,'Sum10terms of8−4+2−1+…with both equivalent GPsum forms. S15labels in the working are typos; the10term value is correct.',[
 gsum('S10','8','-Rational(1,2)','10','Rational(341,64)',70)],[GPTERM])
ps=[gsum('a','2','2','10','2046',594),gsum('b','3','-3','15','10761681',594),gsum('c','6','Rational(1,3)','8','8+Rational(80,81)',594)]
ps[-1]['author_expected_normalised']='Rational(6560,729)'
ps[-1]['additional_operations']={'six-term-total':{'kind':'identity','operands':['summation(6*Rational(1,3)**(k-1),(k,1,6))']}};ps[-1]['additional_operation_expected']={'six-term-total':'8+Rational(80,81)'}
add('Try-Now-20',1,70,'Compute three finite GPsums with positive,negative andfractional ratios. The key’s third total corresponds to6terms, not the requested8.',ps,[GPTERM])
ps=[gsum('S5','18','-Rational(1,2)','5','Rational(99,8)',594),gsum('S6','18','-Rational(1,2)','6','Rational(189,16)',594),
 v('T6','summation(18*(-Rational(1,2))**(k-1),(k,1,6))-summation(18*(-Rational(1,2))**(k-1),(k,1,5))','-Rational(9,16)',594,
 'The sixth term is the difference of consecutive partialsums, S6−S5, not their ratio; independently18(−1/2)^5gives−9/16.')]
add('Try-Now-20',2,71,'Compute S5andS6for18−9+4½−…,then hence recoverT6fromtheir difference.',ps,[GPTERM])
p=gsum('finite-sum','16','Rational(1,2)','10','Rational(1023,32)',71)
p['additional_operations']={'endpoint-index':{'kind':'identity','operands':['log(Rational(1,32)/16)/log(Rational(1,2))+1']}};p['additional_operation_expected']={'endpoint-index':'10'}
add('Example',21,71,'Sum16+8+4+…+1/32after determining the exact positive integer endpoint index10.',[p],[GPTERM])
ps=[]
for label,a,r,n,key in [('a','Rational(1,27)','3','8','Rational(3280,27)'),('b','-9','-Rational(2,3)','6','-Rational(133,27)'),('c','6','2','9','3066'),('d','Rational(1,16)','-2','12','-Rational(1365,16)')]:
 p=gsum(label,a,r,n,key,594);last={'a':'81','b':'1+Rational(5,27)','c':'1536','d':'-128'}[label]
 p['additional_operations']={'endpoint-residual':{'kind':'identity','operands':['('+a+')*('+r+')**(('+n+')-1)-('+last+')']}};p['additional_operation_expected']={'endpoint-residual':'0'}
 ps.append(p)
add('Try-Now',21,71,'Sum four finite GPseries with given endpoints. Determine integer length andverify signed endpoint parity before summing.',ps,[GPTERM])
p=v('n','log(1+605*(3-1)/5)/log(3)','5',71,
 'The source5+15+45+…hasfirst5,ratio3. Itsfinite sum605requires3^n=1+605(3−1)/5=243, hencen5, apositive integer. No convergence condition is relevant to thisfinite sum.')
p['additional_operations']={'original-finite-total':{'kind':'identity','operands':['summation(5*3**(k-1),(k,1,5))']}};p['additional_operation_expected']={'original-finite-total':'605'}
add('Example',22,71,'Invert a finite increasing GPsum of605tofind its term count; distinguish finite sum fromsum-to-infinity.',[p],[GPTERM])
refs=[
 (20,68,'Example18 substitution typo','The source correctly findsd3froma12andlast/first-three relation. Its S17line wrongly substitutes2(3)instead2(12),while annotationa12andfinal612are correct.',[APTERM],'table',[('summation(12+(k-1)*3,(k,1,17))','612')],'Example:18'),
 (21,69,'Example19 sign-selected term block','The AP6n−97has16negative terms,nozero term,and48positive terms bythe given3:1count ratio. Positive sum ispositions17through64. A zero term would require an extra counting case in a variation.',[APTERM],'table',[('Tuple(6*16-97,6*17-97)','Tuple(-1,5)')],'Example:19'),
 (22,70,'FiniteGPsum reference','Forr≠1,both a(1−r^n)/(1−r)and a(r^n−1)/(r−1)are equivalent forfinite positiveintegern,including negative ratios. At r1the author-derived extension isna; the displayed quotient formulae are undefined there. No infinite-convergence claim is implied.',[GPTERM],'table',[('simplify(a*(1-b**x)/(1-b)-a*(b**x-1)/(b-1))','0')],None),
 (23,70,'Example20 formula comparison and labels','Both worked formulae use exponent10andgive341/64,but each substituted line is labelledS15. Correct those labels toS10; the two formulae are valid alternatives for the same task.',[GPTERM],'table',[('8*(1-(-Rational(1,2))**10)/(1+Rational(1,2))','Rational(341,64)')],'Example:20'),
 (24,71,'Example21 endpoint exponent step','16(1/2)^(n−1)=1/32gives(1/2)^(n−1)=1/512=(1/2)^9,hencen10. The nonunit positive base permits unique exponent comparison.',[GPTERM],'table',[('16*Rational(1,2)**9','Rational(1,32)')],'Example:21'),
 (25,71,'Example22 inverse finite-sum step','S_n605witha5,r3gives3^n243,hencen5. Verify the original finite sum; never apply |r|<1to a finite-sum task.',[GPTERM],'table',[('5*(3**5-1)/(3-1)','605')],'Example:22')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={68:'EveryTry17Q2/3,Example18andTry18Q1/2output recorded. Native scan limitation near375is explicit; key omissions/labels andcorrect-final substitutiontypo are distinguished from numerical errors.',69:'EveryExample19andTry19Q1–5output recorded. Positive terms versuspositive partialsums,zero-term counting andsuccessive-block sums remain distinct.',70:'EveryTry19Q6/7,Example20andTry20Q1output recorded. FiniteGPformula scope andlabeltypos retained; wrong8term fractional-GPkey independently recomputed.',71:'EveryTry20Q2,Example21,Try21andExample22output recorded. Endpointparity,consecutivepartialsums andfinite-sum inverseindex are explicit.'}
pages=[]
for page in range(68,72):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Every APblock/sign-selected andfiniteGPsumtask recorded. Integerindex,originalratio andfinite-versus-infinite distinctions preserved; source-scan ambiguity remains explicit for independent review.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-blocks-GP-sums.json',{'scope':'Every68–71original requested result, with source omissions/scan limitation explicit.','items':answers}),('census-YM-C2-blocks-GP-sums.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete68–71page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
