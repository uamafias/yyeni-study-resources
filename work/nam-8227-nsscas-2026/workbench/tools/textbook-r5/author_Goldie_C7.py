"""R5 rendered-page annotations of the relevant material inside Goldie chapter7.
This is a source analysis/answer audit,not a renewable question generator.
"""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SOURCE='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
items=[];answers=[]
def ev(page,key=False):
    name='Goldie-keys-C7'if key else f'Goldie-scope-{176+4*((page-176)//4)}'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def add(kind,n,page,note,parts,demands=None,components=None,excluded=None):
    iid=f'8227:TB:Goldie:C7:{kind}:{n}'
    key_page=parts[0]['answer_pdf_page']if parts else None
    row={'item_id':iid,'item_kind':'exercise'if kind.startswith('Exercise')else'boxed-prompt'if kind=='Prompt'else'worked-illustration',
      'exercise':kind.replace('-',' '),'item_number':str(n),'pdf_page':page,'printed_page':page-14,'notes':note,
      'assessed_8227_demand_ids':demands or[],'component_demand_ids':components or[],'representation':'text','source_evidence':ev(page),
      'evidence_role':'directly related assessed practice'if demands else'prerequisite/supporting practice; no direct AS-demand coverage claimed',
      'answer_key':{'available':True,'pdf_pages':[key_page],'printed_pages':[key_page-14],
        'locator':f'{kind} {n}; '+('inline worked solution'if key_page<333 else'Answers section'),
        'source_path':SOURCE,'source_sha256':SHA}}
    if excluded:row['scope_check']={'status':'in-scope-parts-only','basis':note,'excluded_or_qualified_parts':excluded,'qualifier_screen':[],'limits_considered':[]}
    items.append(row)
    for p in parts:
        p.update(source_evidence=ev(page),key_evidence=ev(p['answer_pdf_page'],p['answer_pdf_page']>=333),answer_printed_page=p['answer_pdf_page']-14)
        p.setdefault('method','Form the exact rational expression from the rendered question,combine denominators and cancel common factors; compare with the independently transcribed printed result. Retain original denominator and divisor exclusions even when factors cancel.')
    answers.append({'item_id':iid,'source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':demands or[],'component_demand_ids':components or[],
      'mapping_rationale':'The explicit result is classified; ordinary fraction manipulation is prerequisite algebra,not a new AS demand. A supplied identity/equation distinction or positive-integer binomial expansion has its own direct objective.',
      'exam_style':False,'exam_style_basis':'No examination attribution or exam-style label on this task.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT05','status':'not applicable','quoted_value':note,'reason':'This item does not ask polynomial long division; rational fraction simplification alone does not invoke the polynomial dividend-degree limit.'}],
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts})
    return row,answers[-1]
def calc(label,expression,key,page,**extra):
    return {'subpart':label,'operation':{'kind':'identity','operands':[expression]},'printed_key_normalised':key,'answer_pdf_page':page,**extra}

# Every displayed unnumbered worked illustration in section7.2,including the
# numeric lead-ins. These are supporting algebra; no fabricated AS scope claim.
illustrations=[
 (186,'15/20','3/4','Reduce 15/20 to3/4; numeric common-factor cancellation.'),
 (186,'6*a/(9*a**2)','2/(3*a)','Cancel 6a/(9a²),with a≠0 retained; coefficient and variable factors both cancel.'),
 (186,'(2*a+4)/(a**2-4)','2/(a-2)','Factor (2a+4)/(a²−4) before cancelling a+2; preserve a≠−2,2.'),
 (186,'(10*a/(3*b**2))*(9*a*b/25)','6*a**2/(5*b)','Multiply 10a/(3b²) by9ab/25; b≠0; cancel numeric factors and one b.'),
 (186,'((a**2+3*a+2)/9)*(12/(a+1))','4*(a+2)/3','Factor the quadratic in (a²+3a+2)/9 times12/(a+1); a≠−1.'),
 (186,'(12/(x**2-1))/(4/(x+1))','3/(x-1)','Divide12/(x²−1) by4/(x+1); invert the divisor and preserve x≠−1,1.'),
 (187,'2/3+1/4','11/12','Use common denominator12 to add2/3and1/4.'),
 (187,'2*x/3+x/4','11*x/12','Combine2x/3andx/4 over denominator12; the common numerator variable remains.'),
 (187,'2/(3*x)+1/(4*x)','11/(12*x)','Combine2/(3x)and1/(4x); preserve x≠0.'),
 (187,'(4*x-3)/6-(2*x+1)/4','(2*x-9)/12','Subtract (2x+1)/4 from(4x−3)/6; distribute the subtraction to both numerator terms.'),
 (187,'2/(x+3)+3/(x-2)','5*(x+1)/((x+3)*(x-2))','Add2/(y+3)and3/(y−2) using both linear denominator factors; y≠−3,2. Computation renames y to x only.'),
 (187,'2*b/(a**2-b**2)-3/(a+b)','(5*b-3*a)/((a+b)*(a-b))','Subtract3/(a+b)from2b/(a²−b²); use the difference-of-squares denominator and retain a≠±b.')]
for n,(page,expression,key,note)in enumerate(illustrations,1):
    add('Worked-illustration',n,page,note,[calc('simplified',expression,key,page)])

# Questions1–24 on the one Exercise7B page; keys1–20arePDF349,21–24PDF350.
fractions=[
 ('(6*a/b)*(a/(9*b**2))','2*a**2/(3*b**3)','Multiply6a/bby a/(9b²),b≠0.'),
 ('(5*x*Symbol("y")/3)/(15*x*Symbol("y")**2)','1/(9*Symbol("y"))','Divide5xy/3by15xy²; original x≠0,y≠0.'),
 ('(x**2-9)/(x**2-9*x+18)','(x+3)/(x-6)','Factor the numerator difference of squares and denominator quadratic; x≠3,6.'),
 ('((5*x-1)/(x+3))*((x**2+6*x+9)/(5*x**2+4*x-1))','(x+3)/(x+1)','Factor all three quadratics/linear factors before multiplying; x≠−3,−1,1/5.'),
 ('(4*x**2-25)/(4*x**2+20*x+25)','(2*x-5)/(2*x+5)','Cancel one2x+5factor from a difference of squares over a perfect square; x≠−5/2.'),
 ('((a**2+a-12)/5)*(3/(4*a-12))','3*(a+4)/20','Factor a²+a−12 and4a−12,then multiply; a≠3.'),
 ('((4*x**2-9)/(x**2+2*x+1))/((2*x-3)/(x**2+x))','x*(2*x+3)/(x+1)','Divide the two factored rational expressions; retain x≠−1,0,3/2 from the original expression and nonzero divisor.'),
 ('((2*p+4)/5)/(p**2-4)','2/(5*(p-2))','Divide (2p+4)/5 byp²−4; p≠−2,2 even after cancelling p+2.'),
 ('(a**2-b**2)/(2*a**2+a*b-b**2)','(a-b)/(2*a-b)','Factor a two-variable quadratic denominator; a+b≠0 and2a−b≠0.'),
 ('((x**2+8*x+16)/(x**2+6*x+9))*((x**2+2*x-3)/(x**2+4*x))','(x+4)*(x-1)/(x*(x+3))','Multiply two rational expressions with square and mixed-product factors; x≠−3,−4,0.'),
 ('1/(4*x)+1/(5*x)','9/(20*x)','Add reciprocal monomials with numerical denominators4and5; x≠0.'),
 ('x/3-(x+1)/4','(x-3)/12','Subtract the whole numerator x+1 after using common denominator12.'),
 ('a/(a+1)+1/(a-1)','(a**2+1)/(a**2-1)','Add a/(a+1)to1/(a−1); a≠−1,1.'),
 ('2/(x-3)+3/(x-2)','(5*x-13)/((x-3)*(x-2))','Add2/(x−3)and3/(x−2); x≠2,3. High-resolution source check confirms the plus sign.'),
 ('x/(x**2-4)-1/(x+2)','2/((x+2)*(x-2))','Subtract1/(x+2)fromx/(x²−4) using the shared factor; x≠−2,2.'),
 ('p**2/(p**2-1)-p**2/(p**2+1)','2*p**2/((p**2-1)*(p**2+1))','Subtract two p²numerator fractions with denominators p²−1andp²+1; real p≠±1.'),
 ('2/(a+1)-a/(a**2+1)','(a**2-a+2)/((a+1)*(a**2+1))','Combine2/(a+1)minus a/(a²+1); real a≠−1.'),
 ('2*x/(x+2)**2-4/(x+4)','-2*(x**2+4*x+8)/((x+2)**2*(x+4))','Subtract4/(y+4)from2y/(y+2)²; y≠−2,−4. Computation renames y to x only.'),
 ('x+1/(x+1)','(x**2+x+1)/(x+1)','Write the sum of polynomial x and1/(x+1)as one fraction; x≠−1.'),
 ('2/(b**2+2*b+1)-3/(b+1)','-(3*b+1)/(b+1)**2','Use the perfect-square denominator to combine2/(b²+2b+1)minus3/(b+1); b≠−1.'),
 ('2/(3*(x-1))+3/(2*(x+1))','(13*x-5)/(6*(x-1)*(x+1))','Add2/[3(x−1)]and3/[2(x+1)]; use coefficient LCM6and both linear factors; x≠±1.'),
 ('6/(5*(x+2))+2*x/(x+2)**2','4*(3-x)/(5*(x+2)**2)','Add6/[5(x+2)]and2x/(x+2)²; x≠−2. The printed key has a negative x contribution despite the source plus sign.'),
 ('2/(a+2)-(a-2)/(2*a**2+a-6)','(3*a-4)/((a+2)*(2*a-3))','Subtract(a−2)/(2a²+a−6)from2/(a+2); denominator factors(a+2)(2a−3),a≠−2,3/2.'),
 ('1/(x-2)+1/x+1/(x+2)','(3*x**2-4)/(x*(x-2)*(x+2))','Combine three reciprocal linear terms; x≠−2,0,2; numerator becomes3x²−4.')]
for n,(expression,key,note)in enumerate(fractions,1):
    part=calc('simplified',expression,key,349 if n<=20 else 350)
    if n==22:part['source_defect_id']='TB-Goldie-C7-7B22-NUMERATOR-SIGN'
    add('Exercise-7B',n,188,note,[part])

row,answer=add('Exercise-7A',5,184,'Only(i): expand(1−x)^3with positive integer exponent3. Parts(ii)and(iii)require negative-exponent series and stay outside8227.',
 [calc('i','(1-x)**3','1-3*x+3*x**2-x**3',349)],['8227:2020:M1:T2:O01:D01'],excluded=['ii: (1−x)^−4 series','iii: coefficients determined from the nonpositive-power series'])
answer['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'within','parts':['i'],'quoted_value':'(i)(1−x)^3','reason':'The exponent3is a positive integer.'},{'rule_id':'8227:QUAL02','status':'outside','parts':['ii','iii'],'quoted_value':'(ii)(1−x)^−4','reason':'Exponent−4in(ii),and its connected coefficient comparison(iii),are outside. No entire-question scope claim.'}]

show=calc('i','(4+x)**(-S(1)/2)-(1+x/4)**(-S(1)/2)/2','0',185,check_mode='show/prove')
show['method']='For real x>−4,factor4+x=4(1+x/4); the positive square root of4is2. Simplify both expressions under that domain; no infinite series is used.'
row,answer=add('Exercise-7A',6,185,'Only(i): rewrite1/√(4+x)as(1/2)(1+x/4)^−1/2 for x>−4; an indices prerequisite. The requested infinite series and approximation in(ii),(iii)are outside8227.',[show],excluded=['ii: rational-power infinite binomial series','iii: approximation from that outside-scope series'])
answer['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'not applicable','parts':['i'],'quoted_value':'1/√(4+x)=(1/2)(1+x/4)^−1/2','reason':'The exact identity in(i)is supporting algebra only,not a binomial expansion.'},{'rule_id':'8227:QUAL02','status':'outside','parts':['ii','iii'],'quoted_value':'(1+x/4)^−1/2','reason':'The exponent−1/2makes the infinite series requested in(ii),(iii)outside scope.'}]

part={'subpart':'identity-versus-equation','verification_mode':'manual-derivation','author_comparison_status':'matches',
 'author_conclusion':'The identity holds for every allowed x. Substituting a particular x gives an equation in the unknown constants A and B; equating coefficients likewise yields equations in those constants.',
 'author_derivation':'Start with4+x≡A(2−x)+B(1+x). An identity requires the same A,B for every x. At x=2,it yields6=3B; at x=−1,it yields3=3A. These are equations in A or B at a fixed x,not identities in x. They determine A=1,B=2; substituting these back restores an identity. The printed key states the all-values versus particular-value distinction and notes equating constant terms corresponds to x=0.',
 'method':'Author logical derivation from the actual identity and its fixed-x substitutions; compared with the rendered printed answer,not a mechanically certified proof.','answer_pdf_page':350}
add('Prompt',1,190,'Explain why≡was replaced by=when particular x values or coefficient comparisons were used in4+x≡A(2−x)+B(1+x). The surrounding partial-fractions task is outside scope; this explicit distinction prompt is in scope.',[part],['8227:2020:M1:T1:O03:D01'])

# The positive-integer recap is teaching evidence rather than an assessed item.
figure={'item_id':'8227:TB:Goldie:C7:Teaching-figure:1','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':'1','pdf_page':178,'printed_page':164,
 'notes':'Pascal triangle beside the finite expansions for powers0through4; positive-integer rows support binomial calculation. The zero row is notation support,not expansion with a prescribed positive exponent.',
 'what_it_shows':'Rows1;1,1;1,2,1;1,3,3,1;1,4,6,4,1and the corresponding finite expansions.',
 'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':['8227:2020:M1:T2:O01:D01'],
 'representation':'table','source_evidence':ev(178),'learner_display':False,
 'exam_representation_check':{'status':'teaching aid; no NSSCAS Pascal-triangle response task claimed','examination_part_ids':[],
 'relation':'The inspected NSSCAS corpus assesses finite binomial coefficients/terms; a displayed Pascal triangle is not evidence that coefficient properties are assessed.'},
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL02','status':'within','quoted_value':'n=1,2,3,4 finite expansions','reason':'These rows have positive integer exponents; the nearby n=−3 and n=1/2 infinite-series exposition is excluded.'},
 {'rule_id':'8227:LIMIT01','status':'not applicable','quoted_value':'Pascal triangle rows through1,4,6,4,1','reason':'Figure is an optional calculation aid; no greatest-term or coefficient-property assessment is introduced.'}],
 'value_level_scope_review_status_r5':'author actual-value scope checked; independent review pending',
 'mathematical_feature_review':{'status':'author verified exact entries and finite expansions; independent review pending','method':'Each displayed row equals C(n,r)forr=0..n,n=0..4; direct binomial expansion confirms the coefficients. No graph response or separate key.'}}
items.append(figure)

page_notes={
176:'Chapter7 opener asks approximate√101without calculator; intended general rational binomial method outsideQUAL02.',
177:'Squareroots investigation approximates√(1+x)using exponent1/2,outsideQUAL02. Positive-integer recap at foot is relevant exposition; no separate task.',
178:'Finite positive-integer binomial recap and Pascal triangle retained; negative−3and half-power infinite expansions and boxed x=8 convergence prompt excluded byQUAL02.',
179:'Figure7.1andActivity7.1compare√(1+x)with truncated rational-power series; outsideQUAL02,not prescribed graph practice.',
180:'Activity7.2ties GP to exponent−1binomial series; Example7.1uses(1−x)^−2; both outsideQUAL02.',
181:'Example7.2uses exponent−1/2; negative-integer coefficient investigation outsideQUAL02/LIMIT01.',
182:'Example7.3uses exponent−3; repeated√101approximation uses exponent1/2; Example7.4introduces reciprocal-series expansion. OutsideQUAL02.',
183:'Examples7.4and7.5continue rational/negative-power series; outsideQUAL02.',
184:'Exercise7A1–4outsideQUAL02;5(i)finite cube retained,5(ii),(iii)negative-power series excluded.',
185:'Exercise7A6(i)exact-index rewrite retained as supporting;6(ii),(iii),7–13require negative or fractional binomial series.7.2starts next page.',
186:'All six unnumbered worked fraction illustrations recorded individually; this review of algebraic fractions is not partial-fractions decomposition.',
187:'All six unnumbered addition/subtraction illustrations recorded individually.',
188:'Exercise7B1–24all recorded. Section7.3opening1/[(1+2x)(1+x)]decomposition is outside prescribed scope.',
189:'Partial-fractions model-selection exposition andExample7.6outside8227; identity context continues to explicit relevant prompt onPDF190.',
190:'Example7.6continuation andExample7.7partial-fractions decomposition excluded; the explicit boxed identity/equation prompt retained independently.',
191:'Examples7.7and7.8partial-fractions decomposition excluded; extracting a quotient is incidental to the requested decomposition,not standalone assessed polynomial division.',
192:'Exercise7C1–15andExample7.9require partial-fractions decomposition,not prescribed8227scope.',
193:'Repeated-factor partial-fractions model andExample7.10outside scope.',
194:'Example7.11partial fractions andExample7.12partial fractions plus nonpositive binomial series outside scope.',
195:'Example7.12continuation,Activity7.3andExercise7D1outside partial-fractions/nonpositive-series scope.',
196:'Exercise7D2–9requires nonpositive-series/partial-fractions methods; no independently stated within-scope part.',
197:'Key-points/learning-outcomes prose only. Finite expansion reminder and algebraic-fraction simplification are relevant; wider rational-power and partial-fractions outcomes do not extend8227scope.'}
pages=[]
for page in range(176,198):
    own=[i['item_id']for i in items if i['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':7,
      'page_status':'items enumerated'if own else'prose only'if page==197 else'scope-screened; no in-scope item starts',
      'item_ids':own,'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':page_notes[page],
      'scope_screen':'Rendered entire page inspected,including excluded tasks; exclusions are stated here rather than silently treating this chapter as wholly irrelevant.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    census={'book':'Goldie','book_id':'8227-SRC-015','chapter':7,'source_path':SOURCE,'source_sha256':SHA,
      'scope':'Full rendered chapter7 boundary pass. Retains all section7.2supporting items,the finite-power7A5(i),exact-index7A6(i),and explicit identity/equation prompt. All other exclusions have page-specific reasons. Independent acceptance pending.',
      'pages':pages,'new_items':items,'corrections':[]}
    (W/'tools/textbook-r5/census-Goldie-C7.json').write_text(json.dumps(census,ensure_ascii=False,indent=2)+'\n')
    (W/'tools/textbook-r5/answers-Goldie-C7.json').write_text(json.dumps({'scope':'Every retained assessed/supporting task in chapter7; excluded parts remain explicitly outside. No rights to learner textbook reproduction.','items':answers},ensure_ascii=False,indent=2)+'\n')
    print(len(items),'chapter7records;',len(answers),'answer-checked items')
