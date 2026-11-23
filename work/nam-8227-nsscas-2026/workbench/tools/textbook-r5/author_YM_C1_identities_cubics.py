"""YM43–46: coefficient identities and cubic reconstruction; preserve factor scaling."""
import json
import author_YM_C1_intervals as base
from author_YM_C1_intervals import opening,W,SRC,SHA,ev,v,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=base.corrections
IDENTITY='8227:2020:M1:T1:O03:D02';DISTINGUISH='8227:2020:M1:T1:O03:D01';CUBIC='8227:2020:M1:T1:O05:D02'

def add(kind,n,page,note,parts,direct,rep='text'):
 r=base.add(kind,n,page,note,parts,direct,rep)
 r['mapping_rationale']='Coefficient matching is directly assessed when constants must make an identity true on its common domain. Cubic reconstruction is assessed from sufficient roots/multiplicities and another point. A definition/comparison table teaches identity versus equation but does not itself supply an assessed classification response.'
 r['precision_angle_check']={'source':'All constants, roots and interpolation points here are exact; no angle quantities.','comparison':'Preserve correlated coefficient alternatives and original rational-identity exclusions. Rescaling a linear factor must be compensated in the global multiplier.'}
 return r

def coeff(label,left,right,names,key,kp,method):
 sol='solve(Poly(expand(('+left+')-('+right+')),x).all_coeffs(),('+','.join(names)+',),dict=True)[0]'
 expr='Tuple('+','.join(sol+'['+n+']'for n in names)+')'
 return v(label,expr,key,kp,method+' Expand both original sides, compare every polynomial coefficient, solve the resulting constant system, and substitute back into all coefficients; do not determine an identity from one convenient x-value alone.')

add('Example',34,43,'Find a,b making2x²+20x+60≡2(x+a)²+b. The source also shows completion of squares as an alternative for the same identity.',[
 coeff('constants','2*x**2+20*x+60','2*(x+a)**2+b',['a','b'],'Tuple(5,10)',43,'The x coefficient gives4a20; then the constant gives2a²+b60.')],[IDENTITY])
rows=[(1,'Use(x−7)²≡x²+mx+n to determine both coefficients.','(x-7)**2','x**2+a*x+b',['a','b'],'Tuple(-14,49)'),
 (2,'Determine a in2x²+20x+50≡2(x+a)².','2*x**2+20*x+50','2*(x+a)**2',['a'],'Tuple(5)'),
 (3,'Determine a,b,c in2x²−4x+5≡a(x+b)²+c.','2*x**2-4*x+5','a*(x+b)**2+c',['a','b','c'],'Tuple(2,-1,3)'),
 (4,'Determine A,B inx²−10x+21≡(x+A)²+B.','x**2-10*x+21','(x+a)**2+b',['a','b'],'Tuple(-5,-4)'),
 (5,'Match a linear factor times a cubic with a supplied quartic; solve all three shared constants.','(x+a)*(x**3-2*x-4)','x**4+b*x**3-2*x**2-6*x+c',['a','b','c'],'Tuple(1,1,-4)')]
for n,note,left,right,names,key in rows:
 add('Try-Now-34',n,43,note,[coeff('constants',left,right,names,key,591,'Checker symbols follow the original constants in the listed order; no source domain restriction is changed.')],[IDENTITY])
ps=[coeff('a','6*x**3+7*x**2-19*x+7','(2*x-1)*(a*x**2+b*x+c)',['a','b','c'],'Tuple(3,5,-7)',591,'Checker a,b,c correspond to source c,d,e respectively.'),
 coeff('b','2*x**3-x**2+6*x','(x-1)**2*(2*x+a)+b*x+c',['a','b','c'],'Tuple(3,10,-3)',591,'Checker a,b,c correspond to source c,d,e respectively; the residual dx+e terms are part of the identity.')]
add('Try-Now-34',6,43,'Determine source c,d,e in each of two cubic identities, including an added linear remainder after a repeated factor.',ps,[IDENTITY])
p=coeff('constants','(a*x+b)*(x+1)+c*(x**2+2)','5*x**2-x',['a','b','c'],'Tuple(3,-4,2)',44,
 'For the original rational identity, x≠−1 and x²+2>0 on the real line. Clear the common denominator only on that domain; the numerator identity then givesA+C5,A+B−1,B+2C0. Checker a,b,c correspond to sourceA,B,C.')
p['original_common_domain']='All realx except−1; x²+2 is never zero for realx.'
add('Example',35,44,'Determine A,B,C in a given rational identity by a common denominator and coefficient comparison. Preserve x≠−1; this is not a newly requested partial-fraction decomposition method.',[p],[IDENTITY])
p=coeff('constants','2*x**4+3*x**3-5*x**2-x+1','(x**2+a*x-1)*(b*x**2-c*x-1)',['a','b','c'],'Tuple(2,2,1)',591,
 'Checker a,b,c correspond to sourcek,m,n. All quartic coefficients must agree, including the constant and linear terms.')
add('Try-Now-35',1,44,'Determine the three constants in a product of two quadratics giving a supplied quartic identity.',[p],[IDENTITY])
p=v('paired-alternatives','FiniteSet(*solve(Poly(expand((x**2+a*x+3)*(x**2+b*x+3)-(x**4+9)),x).all_coeffs(),(a,b)))',
 'FiniteSet(Tuple(-sqrt(6),sqrt(6)),Tuple(sqrt(6),-sqrt(6)))',591,
 'The x³ coefficient givesa+b0; the x² coefficient givesab+60. Both correlated pairs(a,b)=(−√6,√6),(√6,−√6) satisfy every original coefficient. The irrational values are permitted coefficient parameters, not extra complex work.')
r=add('Try-Now-35',2,44,'Find both correlated real coefficient pairs inx⁴+9≡(x²+ax+3)(x²+bx+3), retaining the opposite signs.',[p],[IDENTITY]);r['correlated_branch_check']={'required_pairs':[['-sqrt(6)','sqrt(6)'],['sqrt(6)','-sqrt(6)']],'reason':'Independent sign choices would create invalid coefficient pairs.'}
add('Try-Now-35',3,45,'Use the two given linear factors and a quadratic factor to determine three coefficients in the quartic identity.',[
 coeff('constants','(x+3)*(x-4)*(x**2-b*x-c)','x**4-4*x**3-7*x**2+a*x-24',['a','b','c'],'Tuple(34,3,-2)',591,'The shared x²,x and constant coefficients determine source a,b,c; retain the minus signs in the unknown quadratic.')],[IDENTITY])
add('Try-Now-35',4,45,'Determine a,b in the given quartic product identity with differently scaled leading coefficients.',[
 coeff('constants','2*x**4+5*x**3+4*x**2+7*x+6','(x**2+a*x+2)*(2*x**2+b*x+3)',['a','b'],'Tuple(3,-1)',591,'Both x³ and x coefficients constrain the ordered pair; the remaining coefficients independently confirm it.')],[IDENTITY])
add('Example',36,45,'Reconstruct a cubic crossing at3,1,−2 and passing through(2,−4), with one shared global scale.',[
 v('equation','expand((-4/((2-3)*(2-1)*(2+2)))*(x-3)*(x-1)*(x+2))','x**3-2*x**2-5*x+6',45,
 'The three simple roots giveA(x−3)(x−1)(x+2). The extra point has product−4, so A1. All three roots and the supplied point must be retained; expansion is optional.')],[CUBIC])
add('Try-Now-36',1,46,'Reconstruct a cubic from simple roots−2,0,3 and point(−1,−4). The extra point fixes a negative scale.',[
 v('equation','expand((-4/((-1+2)*(-1)*(-1-3)))*(x+2)*x*(x-3))','-x**3+x**2+6*x',591,
 'The monic factor product at−1 equals4, givingA−1. This fixes both the intercept and end behaviour; no free second scale remains.')],[CUBIC])
ps=[v('a','expand((-8/((0+1)*(0-2)*(0-4)))*(x+1)*(x-2)*(x-4))','-(x+1)*(x-2)*(x-4)',591,
 'Read simple roots−1,2,4 and y-intercept−8 from the first graph. Their monic product at0 is8, soA−1.'),
 v('b','expand((-5/((0+5)*(0+2)*(0-5)))*(x+5)*(x+2)*(x-5))','(x+5)*(x+2)*(x-5)/10',591,
 'Read roots−5,−2,5 and y-intercept−5. The monic product at0 is−50, givingA1/10. The source explicitly allows a fractional scale.')]
add('Try-Now-36',2,46,'Reconstruct both diagram-supplied cubics from their three simple roots and y-intercept. One global scale is fractional.',ps,[CUBIC],rep='graph')
ps=[v('a','expand((6/((0+3)*(0+Rational(1,2))*(0-Rational(1,2))))*(x+3)*(x+Rational(1,2))*(x-Rational(1,2)))','-2*(x+3)*(2*x+1)*(2*x-1)',46,
 'Read roots−3,−1/2,1/2 and intercept6. Monic linear factors give scale−8; replacing the two half-root factors by2x+1,2x−1 multiplies the product by4, so its outer scale is−2. Both forms represent the same cubic.'),
 v('b','expand((-12/((0+4)**2*(0-3)))*(x+4)**2*(x-3))','(x+4)**2*(x-3)/4',46,
 'Touching at−4 means a double root and crossing at3 a simple root. The y-intercept−12 gives−48A−12, hence A1/4. Do not assign independent multiplicities after fitting the scale.')]
add('Example',37,46,'Reconstruct two cubics from graphs: rational simple roots with rescaled factors, and a double touching root plus a simple crossing.',ps,[CUBIC],rep='graph')
ps=[v('a','expand((54/((4-1)**2*(4+2)))*(x-1)**2*(x+2))','(x-1)**2*(x+2)',591,
 'Touching at1 gives a squared factor; crossing at−2 gives a simple factor. At(4,54) the factor product is54, soA1.'),
 v('b','expand((-5/((-1+Rational(2,3))**2*(-1-4)))*(x+Rational(2,3))**2*(x-4))','9*(x+Rational(2,3))**2*(x-4)',591,
 'Touching at−2/3 gives the double factor(x+2/3)²; crossing at4 givesx−4. Atx−1 the monic product is−5/9, soA9. Equivalently(3x+2)²(x−4) has outer scale1.')]
add('Try-Now',37,46,'Reconstruct cubics from specified touching/crossing behaviour and an extra point. The rational double root requires consistent factor scaling.',ps,[CUBIC])
refs=[
 (70,43,'Identity definition and coefficient-comparison guidance','An identity holds throughout its common domain; a conditional equation is solved for the inputs making it true. The source’s advice to simplify sides separately is a teaching method, not a mathematical ban on taking their difference. No separate learner classification question occurs here.',[DISTINGUISH,IDENTITY],'table',[],None),
 (71,43,'Example34 coefficient and square-completion alternatives','Both methods givea5,b10 in2x²+20x+60≡2(x+a)²+b. They are valid alternatives for one identity structure.',[IDENTITY],'table',[('expand(2*(x+5)**2+10)','2*x**2+20*x+60')],'Example:34'),
 (72,44,'Example35 common-denominator coefficient block','On realx≠−1, the common-denominator numerator gives(A+C)x²+(A+B)x+B+2C. Comparing with5x²−x gives the linked systemA+C5,A+B−1,B+2C0.',[IDENTITY],'table',[('expand((3*x-4)*(x+1)+2*(x**2+2))','5*x**2-x')],'Example:35'),
 (73,45,'Equation/inequality/identity comparison table','The three-column table contrasts solving a conditional equality, a relational range and coefficients making two expressions identical. Identities are also equations; the table’s phrase an equation is only true for particular values describes conditional equations, not all possible equations. This supplies teaching support for the previously thin identity-versus-equation distinction.',[DISTINGUISH,IDENTITY],'table',[('expand((x+y)*(x-y))','x**2-y**2')],None),
 (74,45,'Cubic root-factor reconstruction reference','Three roots with multiplicities totalling3 giveA∏(x−root). A further point not at a root fixes nonzeroA. Extra points at roots do not fix the vertical scale.',[CUBIC],'table',[],None),
 (75,46,'Try36 first cubic given graph','The first curve crosses at−1,2,4, passes through(0,−8) and has negative leading coefficient. Those labels jointly fixA−1.',[CUBIC],'graph',[('-(0+1)*(0-2)*(0-4)','-8')],'Try-Now-36:2'),
 (76,46,'Try36 second cubic given graph','The second curve crosses at−5,−2,5 and passes through(0,−5). A1/10 is required; its positive end behaviour agrees with that scale.',[CUBIC],'graph',[('(0+5)*(0+2)*(0-5)/10','-5')],'Try-Now-36:2'),
 (77,46,'Example37 rational-root given graph','Roots−3,−1/2,1/2 and intercept6 fix the polynomial. Both monic half-root factors and doubled integer factors work when the outside scale is adjusted.',[CUBIC],'graph',[('expand(-8*(x+3)*(x+Rational(1,2))*(x-Rational(1,2))+2*(x+3)*(2*x+1)*(2*x-1))','0')],'Example:37'),
 (78,46,'Example37 double-root given graph','The graph touches at−4, crosses at3, and has intercept−12. The double factor is(x+4)², and its shared scale is1/4.',[CUBIC],'graph',[('(0+4)**2*(0-3)/4','-12')],'Example:37'),
 (79,46,'Rational-root factor-scaling callout','The source says root−1/2 is not written as(x+1/2) but as(2x+1). Both are valid factors up to a nonzero scale; multiplying both half-root factors by2 requires dividing the global coefficient by4. The printed final equation is correct; the categorical prohibition is misleading.',[CUBIC],'table',[('expand(4*(x+Rational(1,2))*(x-Rational(1,2)))','(2*x+1)*(2*x-1)')],'Example:37')]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={43:'Identity teaching reference, Example34 and all six independently numbered Try34 tasks recorded, including both Q6 responses. Both worked methods are retained.',44:'Rational identity Example35 and its domain/coefficient block recorded, plus first two Try35 questions. Q2 preserves correlated irrational-coefficient pairs.',45:'Remaining Try35 questions, the full three-way comparison table, cubic reconstruction reference and Example36 recorded. Identity distinction support is teaching evidence, not an invented assessed classification response.',46:'All Try36/37 and Example37 responses recorded, including four given cubic diagrams and the factor-scaling callout. Repeated roots and rational-factor scaling are explicit.'}
pages=[]
for page in range(43,47):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Polynomial coefficient identities and quadratic/cubic graph reconstruction are prescribed. Rational-identity denominators stay explicit; no complex roots or extra partial-fraction instruction is inferred.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-identities-cubics.json',{'scope':'Every43–46original response with correlated constants and multiplicities.','items':answers}),('census-YM-C1-identities-cubics.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete43–46page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
