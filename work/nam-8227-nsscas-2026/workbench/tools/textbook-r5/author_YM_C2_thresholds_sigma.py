"""YM72–75: finite-GP integer thresholds and sigma bounds/expansion.

Fixed source evidence and independent answer checks; no runtime recipes.
"""
import json
import author_YM_C2_blocks_GP_sums as base
import author_YM_C2_AP as ap
from author_YM_C2_AP_sums import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,APTERM,GPTERM
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.base.base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
INTERPRET='8227:2020:M1:T2:O04:D01';EVALUATE='8227:2020:M1:T2:O04:D02'

def add(kind,n,page,note,parts,direct,components=None):
 r=base.base.base.add(kind,n,page,note,parts,direct,components or[])
 corrections.extend(base.base.base.corrections[-1:])
 r['mapping_rationale']='Link the requested progression output or sigma interpretation/evaluation directly. Algebra, logarithm manipulation and AP/GP formulae used only to evaluate sigma are components. Explicit expanded-form responses assess interpretation as well as evaluation; a summation index may start at zero or be negative.'
 r['precision_angle_check']={'source':'Original constants are exact. Some keys label3sf, while others merely display three significant digits; individual response records distinguish those cases.',
 'comparison':'Keep the exact finite sum separately from the source key’s approximate display. No angle units occur. Integer count thresholds use strict/non-strict inequalities and adjacent checks, not rounding to nearest.'}
 return r

def extra(p,label,expr,expected):
 p.setdefault('additional_operations',{})[label]={'kind':'identity','operands':[expr]}
 p.setdefault('additional_operation_expected',{})[label]=expected
 return p

def rounded(label,expr,key,kp,method,explicit=True):
 p=v(label,expr,key,kp,method)
 p['operation']={'kind':'rounded','operands':[expr],'significant_figures':3}
 extra(p,'exact-finite-result',expr,str(compute({'kind':'identity','operands':[expr]})))
 p['precision_interpretation']={'source_key_display':'3 significant figures','explicit_key_3sf_label':explicit,
 'question_precision_requirement':None,'basis':'Compare with the key at its displayed precision, retaining the exact finite result; this does not impose a new precision instruction on the original question.'}
 return p

p=v('n','log(1+315*(2-1)/5)/log(2)','6',594,'From the original5+10+20+…sum, 5(2^n−1)=315 gives2^n64, hence positive integern6.')
extra(p,'original-total','summation(5*2**(k-1),(k,1,6))','315')
add('Try-Now',22,72,'Invert a finite doubling-GPsum315to find its term count.',[p],[GPTERM])
p=v('least-count','floor(log(160)/log(4))+1','4',72,'For the original first2,ratio1/4,target53/20, S_n=(8/3)(1−4^(−n))>53/20 iff4^n>160. The least integer is4. The denominator logarithm in the source is negative, so its inequality reverses when dividing.')
extra(p,'adjacent-original-sums','Tuple(summation(2*Rational(1,4)**(k-1),(k,1,3)),summation(2*Rational(1,4)**(k-1),(k,1,4)))','Tuple(Rational(21,8),Rational(85,32))')
add('Example',23,72,'Find the least number of terms of a decreasing positive GPneeded to exceed2.65; adjacent partial sums certify the integer boundary.',[p],[GPTERM])
p=v('a-Sn','summation(Rational(11,10)**(k-1),(k,1,n))','((Rational(11,10))**n-1)/Rational(1,10)',594,'Sum the original exact decimal GPwithfirst1andratio11/10. For positive integern, S_n=10[(11/10)^n−1].')
p2=v('b-least-count','floor(log(3)/log(Rational(11,10)))+1','12',594,'S_n>20 iff(11/10)^n>3. The least integer count is12; do not round the logarithmic lower bound to nearest.')
extra(p2,'adjacent-threshold-tests','Tuple(10*(Rational(11,10)**11-1)<20,10*(Rational(11,10)**12-1)>20)','Tuple(True,True)')
add('Try-Now-23',1,72,'Derive the finite-sum formula for1+1.1+1.21+…,then find the least count exceeding20.',[p,p2],[GPTERM])
p=v('greatest-count','floor(log(Rational(129,4))/log(Rational(3,2)))','8',594,'Witha2,r3/2, S_n=4[(3/2)^n−1]≤125. Keep the greatest integern≤log_(3/2)(129/4).')
extra(p,'adjacent-threshold-tests','Tuple(4*(Rational(3,2)**8-1)<=125,4*(Rational(3,2)**9-1)>125)','Tuple(True,True)')
add('Try-Now-23',2,72,'Find the greatest finite GPcount whose partialsum does not exceed125; equality is allowed.',[p],[GPTERM])
p=v('a-largest-term-index','ceiling(1+log(50)/log(Rational(6,5)))-1','22',594,'The term100(6/5)^(k−1)<5000 givesk<1+log_(6/5)50. Useceil(upper bound)−1for a strict upper integer boundary; this also handles exact integer bounds correctly.')
extra(p,'adjacent-original-terms','Tuple(100*Rational(6,5)**21<5000,100*Rational(6,5)**22>=5000)','Tuple(True,True)')
p2=rounded('b-Sk','summation(100*Rational(6,5)**(k-1),(k,1,22))','27100',594,'Independently sum the first22original terms. The key expressly labels27100as3sf; the exact finite value remains in the additional check.')
add('Try-Now-23',3,72,'Find the last GPterm below5000,then sum through that same index. Term threshold and partialsum threshold are distinct.',[p,p2],[GPTERM])
for kind,n,coefficient,key,kp in [('Example',24,'Rational(24,25)','Rational(3,5)',73),('Try-Now-24',1,'Rational(10,9)','Rational(2,3)',594)]:
 p=v('positive-ratio','Max(*solveset(x**2+x-('+coefficient+'),x,domain=S.Reals))',key,kp,'For the intended nonzero-first-term GP, dividea(r+r²)=('+coefficient+')a bynonzeroa, then solve the quadratic andretain the positive ratio. The worked example statesa≠0at division, although its stem does not. Under an all-zero multiplicative recurrence interpretation,a0would leave the positive ratio undetermined; preserve this source-convention boundary.')
 extra(p,'all-nondegenerate-roots','solveset(x**2+x-('+coefficient+'),x,domain=S.Reals)','FiniteSet(-Rational(8,5),Rational(3,5))'if kind=='Example'else'FiniteSet(-Rational(5,3),Rational(2,3))')
 r=add(kind,n,73,'Find the positive GPratio from a relation between second/third terms andsymbolic firsta. State the nonzero-first-term condition needed by the intended quotient convention.',[p],[GPTERM])
 r['source_interpretation']='The publisher’s intended ratio answer is correct for the nondegenerate GP convention. The worked example explicitly writesa≠0at cancellation; a zero-sequence recurrence interpretation has no unique ratio. This is a convention/domain caution, not a claim that the intended numeric ratio key is wrong.'
p=v('n','log(1+510*(2-1)/2)/log(2)','8',594,'Usefirst2,ratio2andfinite sum510:2^n=256, son8.')
extra(p,'original-total','summation(2*2**(k-1),(k,1,8))','510')
add('Try-Now-24',2,73,'Find the term count of2+4+8+…withfinite total510.',[p],[GPTERM])
p=v('a-ratio','real_root((-Rational(2,9))/Rational(3,4),3)','-Rational(2,3)',594,'T4=ar³andfirst3/4give r³−8/27; its unique real cube root is−2/3. Preserve the negative sign.')
p2=rounded('b-S10','summation(Rational(3,4)*(-Rational(2,3))**(k-1),(k,1,10))','Rational(442,1000)',594,'Sum10original alternating terms exactly, then compare with the key’s expressly labelled0.442(3sf).')
extra(p2,'exact-independent-form','Rational(9,20)*(1-Rational(1024,59049))','Rational(11605,26244)')
add('Try-Now-24',3,73,'Recover a negative GPratio from first/fourth terms,then sum10terms.',[p,p2],[GPTERM])
p=v('AP-count','Intersection(solveset(x*(2*11+(x-1)*2)/2-summation((-24)*(-2)**(k-1),(k,1,6)),x,domain=S.Integers),S.Naturals)','FiniteSet(18)',594,'First sum the original six-term alternating GPto504. Match it to the APsum n(n+10), obtaining n18or−28; only18is a positive term count.')
extra(p,'GP-target','summation((-24)*(-2)**(k-1),(k,1,6))','504')
add('Try-Now-24',4,73,'Find an APterm count whose sum equals a six-term GPtotal. The target is calculated from a different progression.',[p],[APTERM,GPTERM])
p=v('least-count','floor(log(81)/log(Rational(11,10)))+1','47',594,'Withfirst10,second11, S_n=100[(11/10)^n−1]>8000 requires(11/10)^n>81. Retain the least integer above this logarithmic bound.')
extra(p,'adjacent-threshold-tests','Tuple(100*(Rational(11,10)**46-1)<=8000,100*(Rational(11,10)**47-1)>8000)','Tuple(True,True)')
add('Try-Now-24',5,73,'Find the least GPcount needed for a sum exceeding8000,using the ratio from its first two terms.',[p],[GPTERM])
p=v('a-first','3/(real_root(Rational(648,125)/3,3))','Rational(5,2)',594,'FromT2=3andT5=648/125, divide toobtainr³=216/125,r6/5. Thena=T2/r=5/2. The key also gives the intermediate ratior1.2,but the asked response isfirstterm.')
p2=rounded('b-S15','summation(Rational(5,2)*Rational(6,5)**(k-1),(k,1,15))','180',594,'Independently sum15original terms withrecovered a5/2andr6/5. Compare with the expressly labelled180(3sf).')
add('Try-Now-24',6,73,'Recover the first term from two later GPterms,andfindits first15sum.',[p,p2],[GPTERM])

def expanded(label,expr,lo,hi,expected,kp):
 p=reasoning(label,expected,'Substitute every inclusive integer index from'+str(lo)+'through'+str(hi)+'into the ORIGINAL summand'+expr+'. Preserve order and signs. The answer section lists a numeric total only,so this separately requested expanded-form response is author-derived; no publisher expansion match is claimed.',kp,'no key')
 extra(p,'ordered-term-list','Tuple('+','.join(expr.replace('k','('+str(i)+')')for i in range(lo,hi+1))+')',expected)
 return p

def expansion_task(kind,n,page,terms,kp):
 parts=[]
 for label,expr,lo,hi,termkey,sumkey in terms:
  parts.extend([expanded(label+'-expanded',expr,lo,hi,termkey,kp),v(label+'-sum','summation('+expr+',(k,'+str(lo)+','+str(hi)+'))',sumkey,kp,'Independently evaluate the original inclusive finite sum; compare with the separately transcribed numeric key.')])
 r=add(kind,n,page,'Write each original sigma series in expanded form andthen evaluate it; expanded terms are a required response,not merely hidden solution working.',parts,[INTERPRET,EVALUATE])
 for p in r['subparts']:
  if p['subpart'].endswith('-expanded'):
   # Example25 prints its expansion inline; unlike the TryNow key, it is verified.
   if kind=='Example':
    p['author_comparison_status']='matches'
    p['author_derivation']='The inline worked source prints5+8+11+14; independently substitute indices1,2,3,4to verify the same ordered expansion.'
   else:p.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[kp],key_evidence=ev(kp))
 return r
r=expansion_task('Example',25,74,[('response','3*k+2',1,4,'Tuple(5,8,11,14)','38')],74)
expansion_task('Try-Now-25',1,74,[('a','2*k-1',1,7,'Tuple(1,3,5,7,9,11,13)','49'),('b','3*2**k',2,5,'Tuple(12,24,48,96)','180'),('c','(-1)**k*(2*k)',1,5,'Tuple(-2,4,-6,8,-10)','-6')],594)
parts=[]
for label,expr,lo,hi,key in [('a','k*(k+1)/2',1,6,'56'),('b','2**k',0,5,'63'),('c','(-1)**(k+1)*(k**2+2*k)',1,4,'-14')]:
 parts.append(v(label,'summation('+expr+',(k,'+str(lo)+','+str(hi)+'))',key,594,'Substitute all original inclusive indices then add. The zero lower bound in(b)is valid; a sigma index is not required to start at1. No separate expansion is asked here.'))
add('Try-Now-25',2,74,'Evaluate three sigma sums,including zero-based powers andalternating signed quadratic terms.',parts,[EVALUATE],components=[INTERPRET])
p=v('value','summation(-2*k+10,(k,2,20))','-228',75,'The inclusive range2..20has19terms,withfirst6andlast−30; direct summation gives−228. The worked source’s20−2+1=19is correct,as confirmed on the native render; no text-extraction typo is adopted.')
add('Example',26,75,'Evaluate an APsigma sum withlower bound2; distinguish the number of terms19fromthe upper index20.',[p],[EVALUATE],components=[INTERPRET,APTERM])
parts=[]
for label,expr,lo,hi,key in [('a','8-3*k',1,15,'-240'),('b','2*3**(4-k)',1,20,'81'),('c','4*k-1',-2,15,'450'),('d','-3*k-4',6,16,'-407'),('e','Rational(1,2)**(k-1)',3,20,'Rational(1,2)'),('f','a+(k-1)*b',1,10,'10*a*b+45*b')]:
 expr='summation('+expr+',(k,'+str(lo)+','+str(hi)+'))'
 p=rounded(label,expr,key,594,'Evaluate the original finite sum exactly,then compare at the key’s displayed three significant digits. The stem does not impose that precision; the finite exact answer is retained andis not the infinite-series value.',False)if label in ['b','e']else v(label,expr,key,594,'Sum the original expression over every inclusive index. For(f),checker bmeans the source common difference d. The key’s10ad+45dhas an extraneous factor din the firstterm.')
 if label=='f':p['author_expected_normalised']='10*a+45*b';p['source_symbol_basis']={'b':'source d'}
 parts.append(p)
add('Try-Now',26,75,'Evaluate six finite sigma sums withnonunit,negative andsymbolic index patterns. Two rounded totals need exact-finite retention,andthe symbolic key has an extraneous factor.',parts,[EVALUATE],components=[INTERPRET,APTERM,GPTERM])
parts=[]
for label,expr,lo,hi,expected in [('a','4*k+1',1,8,'Tuple(5,9,13,17,21,25,29,33)'),('b','(-Rational(1,3))**(k-1)',1,6,'Tuple(1,-Rational(1,3),Rational(1,9),-Rational(1,27),Rational(1,81),-Rational(1,243))')]:
 p=reasoning(label,'Sum('+expr+', (k,'+str(lo)+','+str(hi)+'))', 'Derive the summand andinclusive bounds from the ordered original terms,then expand it independently tocheck the entire list. Shifted-index equivalents are valid: (a)Sum(5+4k,k0..7),(b)Sum((−1/3)^k,k0..5). Equality of totals alone is insufficient for this requested representation.',75,'matches')
 extra(p,'ordered-expansion','Tuple('+','.join(expr.replace('k','('+str(i)+')')for i in range(lo,hi+1))+')',expected)
 parts.append(p)
add('Example',27,75,'Write an APand an alternating finite GPin sigma notation; equivalent index shifts are valid when allorderedterms arepreserved.',parts,[INTERPRET])
refs=[
 (26,72,'Example23 logarithmic inequality direction','Dividing bylog(1/4)<0reverses the source inequality. AdjacentS3andS4certify leastcount4. Finite partialsum below8/3approaches its limit frombelow; a target at or above thatlimit would have no finite solution.',[GPTERM],'table',[('Tuple(Rational(21,8)<Rational(53,20),Rational(85,32)>Rational(53,20))','Tuple(True,True)')],'Example:23'),
 (27,73,'Nonzero-first-term cancellation','Example24working explicitly dividesbya(a≠0). Preserve that nondegenerate domain if its intended unique positive ratio is used; the stem alone doesnotstateit. At a0the multiplicative recurrence condition0=0doesnotfixr.',[GPTERM],'table',[('simplify(0*(x+x**2)-Rational(24,25)*0)','0')],'Example:24'),
 (28,74,'Sigma start/end/summand notation','The annotated sigma shows an inclusive start,an end andthe summand. Its index letter must match the formula; the index is not itself an exponent. The unnamed3iillustration expands fori1..5as3,6,9,12,15.',[INTERPRET],'table',[('Tuple(3*1,3*2,3*3,3*4,3*5)','Tuple(3,6,9,12,15)')],None),
 (29,75,'Inclusive sigma term-count note','For integer boundsm≤nwithunit increments,the count is n−m+1. Example26uses2..20,count19. Nonpositive sigma indices are valid when the summand is defined; they are different from positive progression positions.',[INTERPRET],'table',[('20-2+1','19')],'Example:26'),
 (30,75,'APsigma representation derivation','Example27(a)derivesT_n=4n+1andendpointn8for5,9,…,33. A zero-based5+4kform gives the same orderedterms withbounds0..7; no unique index letter/form is required.',[INTERPRET],'table',[('Tuple(4*1+1,4*8+1)','Tuple(5,33)')],'Example:27'),
 (31,75,'Alternating GPsigma representation derivation','Example27(b)usesratio−1/3andterm(−1/3)^(n−1),n1..6. The endpoint sign checks even length6; replacing−1/3by+1/3would lose the alternating demand.',[INTERPRET],'table',[('(-Rational(1,3))**(6-1)','-Rational(1,243)')],'Example:27')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C2:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C2:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={72:'EveryTry22,Example23andTry23Q1–3output recorded. Term andsumthresholds use different inequalities;strict integer bounds andkey3sfdisplayarechecked.',73:'EveryExample24andTry24Q1–6output recorded. IntendednonzeroGPcancellationconditionexplicit;negativecuberoopreserved;AP/GPmixedsumandlater-termrecoverychecked.',74:'Everyannotatedsigmareference,Example25andTry25Q1/2recorded. Explicitexpandedresponsesseparatedfromnumerictotals;theanswerkeyomitsseparateTry25expandedforms,whichareauthor-derived.',75:'EveryExample26,Try26andExample27outputandteachingreference recorded. Negative/zero-basedindexsemantics,finiteexactversusroundedtotals,andthe10adkeydefectareexplicit.'}
pages=[]
for page in range(72,76):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'AllfiniteGPthresholdandsigmabounds/representationtasksonthese4pagesrecorded. Logarithm/AP/GPcomponentmethodsarenotautomaticallyseparateassessedgoals;exactfinitesumsretained.'})
for source_reference in figures:
 source_reference['item_kind']='teaching-figure'
 source_reference['asset_role']='Printed mathematical teaching/solution reference; no additional learner response. A parent link identifies context, not a diagram given in the question.'
if __name__=='__main__':
 for name,data in [('answers-YM-C2-thresholds-sigma.json',{'scope':'Every72–75originalrequestedresponse,includingseparateexpandedforms.','items':answers}),('census-YM-C2-thresholds-sigma.json',{'book':'YM','book_id':'8227-SRC-017','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete72–75pagecensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
