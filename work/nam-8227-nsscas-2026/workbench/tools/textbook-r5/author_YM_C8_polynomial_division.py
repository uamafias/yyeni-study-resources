"""YM390–393: actual linear/quadratic divisions and remainder-theorem requests."""
import hashlib
import author_YM_C8_opening as h
from author_YM_C8_opening import W,pp,v,fig,figures,extra,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers
LIN='8227:2020:M2:T1:O03:D01';QUAD='8227:2020:M2:T1:O03:D02';QR='8227:2020:M2:T1:O03:D03';REM='8227:2020:M2:T1:O04:D01'
def ev(page):
 name='YM-C8-key-634'if page>=634 else f'YM-C8-{376+4*((page-376)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png'
 return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev
def division(label,f,d,key,kp,which,source_variable='x',no_key=False):
 expr=('quo'if which=='quotient'else'rem')+'('+f+','+d+',x)'
 p=v(label,expr,key,kp,'Divide the ORIGINAL polynomials with every missing power retained as a zero coefficient. Independently reconstruct dividend=divisor×quotient+remainder and verify that the remainder degree is less than the divisor degree. The separately transcribed source key is not used to calculate the quotient or remainder.')
 p.update(original_dividend=f,original_divisor=d,source_variable=source_variable,checker_variable='x',assessed_8227_demand_ids=[QR],component_demand_ids=[LIN if expression(d).as_poly(h.expression('x')).degree()==1 else QUAD],response_format='symbolic')
 extra(p,'full-original-reconstruction','expand(('+d+')*quo('+f+','+d+',x)+rem('+f+','+d+',x)-('+f+'))','0')
 extra(p,'actual-degrees','Tuple(degree('+f+',x),degree('+d+',x))','Tuple('+str(expression(f).as_poly(h.expression('x')).degree())+','+str(expression(d).as_poly(h.expression('x')).degree())+')')
 if no_key:
  p.pop('printed_key_normalised');p.update(author_check_target_normalised=key,author_expected_normalised=key,check_mode='no key',key_presence='no separately readable quotient key',source_key_limitation='Author-derived quotient; the key gives only the remainder, or its quotient is obscured as specifically recorded. Do not describe this as a transcribed printed quotient.')
 return p
def pair(label,f,d,q,r,kp,var='x',obscured=False):
 return [division(label+'-quotient',f,d,q,kp,'quotient',var,obscured),division(label+'-remainder',f,d,r,kp,'remainder',var)]
def remainder(label,f,c,key,kp):
 p=v(label,'('+f+').subs(x,'+c+')',key,kp,'Set the ORIGINAL linear divisor to zero, then evaluate the original polynomial at that exact root. This explicitly requested remainder theorem method avoids doing the full long division. Compare the independently transcribed remainder.')
 p.update(original_polynomial=f,divisor_root=c,assessed_8227_demand_ids=[REM],response_format='symbolic')
 return p
def add(kind,n,page,note,parts,theorem=False):
 r=h.add(kind,n,page,note,parts)
 direct=set(r['assessed_8227_demand_ids']);r['component_demand_ids']=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-direct)
 r.update(mapping_rationale='Identify the explicit quotient/remainder output separately from the linear/quadratic division method used to obtain it. A stated without-division/remainder-theorem request directly assesses the theorem. Supporting division reconstruction does not invent an extra requested quotient.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT05',status='not applicable'if theorem else'within',quoted_value=note,reason='The request explicitly uses the remainder theorem without division.'if theorem else'Every actual dividend here has degree at most4 and every divisor has degree1 or2; source variable names do not change those degrees.')])
 r['scope_check'].update(limits_considered=['8227:LIMIT05'],qualifier_applicability_note='Polynomial division degree restriction is checked on actual operands; it is not automatically imposed on a theorem evaluation without division.')
 return r
r=add('Example',14,390,'Divide 2x³+6x²−4x+3 by x−2: quotient2x²+10x+16, remainder35. The next-page displayed identity mistakenly changes the dividend constant to16.',pair('answer','2*x**3+6*x**2-4*x+3','x-2','2*x**2+10*x+16','35',390))
r['continuation_pdf_pages']=[391]
h.corrections[-1]['continuation_pdf_pages']=[391]
data=[('a','x**2+2*x-3','x+2','x','-3'),('b','x**2+3*x+4','x+1','x+2','2'),('c','x**2+4*x-11','x+3','x+1','-14'),('d','2*x**2-7*x+2','x-2','2*x-3','-4'),('e','x**3-x**2-3*x-5','x-3','x**2+2*x+3','4'),('f','2*x**4-x**3-2*x**2+8*x+4','2*x+3','x**3-2*x**2+2*x+1','1')]
add('Try-Now',14,391,'Find quotient AND remainder for six original linear-divisor tasks of dividend degrees2–4. Part(f) uses the nonmonic divisor2x+3; a monic-only shortcut must not silently change it.',[p for l,f,d,q,r in data for p in pair(l,f,d,q,r,634)])
p=division('remainder','2*x**3-x','x+4','-124',391,'remainder')
add('Example',15,391,'Find only the remainder when2x³−x is divided byx+4. Long and synthetic division are shown as alternatives; the quotient is worked support, not an additional requested output.',[p])
ps=[]
for l,f,d,q,r in [('a','3*x**3+4*x-5','x+1','3*x**2-3*x+7','-12'),('b','x**4+2*x**2-1','x+3','x**3-3*x**2+11*x-33','98')]:
 ps.extend([division(l+'-quotient',f,d,q,634,'quotient',no_key=True),division(l+'-remainder',f,d,r,634,'remainder')])
add('Try-Now',15,392,'Simplify two polynomial fractions and find their remainders. The answer key supplies only remainders−12,98; both requested quotients are independently derived and labelled no-key.',ps)
add('Example',16,392,'Arrange4x⁴−2x³+2x+1 and quadratic2x²−3x+4 in descending powers, inserting the missing x² coefficient. Quotient2x²+2x−1 and remainder−9x+5 reconstruct the original.',pair('answer','4*x**4-2*x**3+2*x+1','2*x**2-3*x+4','2*x**2+2*x-1','-9*x+5',392))
data=[('a','x**3+2*x**2+x-3','x**2+x+1','x+1','-x-4','x',False),('b','2*x**3-6*x**2-4*x+5','x**2-3*x-2','2*x','5','t',True),('c','12*x**4+x**3+7*x**2+7*x-2','3*x**2-2*x+1','4*x**2+3*x+3','10*x-5','x',False),('d','16*x**4-38*x**2-13*x-9','2*x**2-x-5','8*x**2+4*x+3','10*x+6','y',False),('e','x**2-x+1','x**2+x+1','1','-2*x','x',False),('f','x**4-2*x**3+x+5','(x-1)*(x+1)','x**2-2*x+1','-x+6','x',False)]
add('Try-Now-16',1,392,'Six quotient/remainder tasks with quadratic divisors, including equal degrees, sparse terms, nonmonic divisors and variables t,y. In(b), the quotient glyph is annotated/obscured; correct2t is author-derived, while remainder5 is readable.',[p for l,f,d,q,r,var,obscured in data for p in pair(l,f,d,q,r,634,var,obscured)])
data=[('a','x**3','x**2+1','x','-x'),('b','x**4','(x+1)**2','x**2-2*x+3','-4*x-3'),('c','x**3','x+1','x**2-x+1','-1')]
add('Try-Now-16',2,392,'Carry out three divisions, retaining all quotient and remainder terms. Parts(a),(b) have quadratic divisors; part(c) has linear x+1 despite its surrounding quadratic-division section.',[p for l,f,d,q,r in data for p in pair(l,f,d,q,r,634)])
add('Example',17,393,'Use the remainder theorem explicitly for x³−2x²−6x−5 divided byx−1. Evaluate at1 to obtain−12 without long division.',[remainder('remainder','x**3-2*x**2-6*x-5','1','-12',393)],True)
data=[('a','2*x**3-3*x**2+2*x+1','3','34'),('b','2*x**3-8*x+11','-3','-19'),('c','x**4-2*x**2+3*x-1','-2','1')]
add('Try-Now',17,393,'Without doing division, evaluate the original cubic/cubic/quartic at divisor roots3,−3,−2. The signs of the divisor constants determine the substitution inputs.',[remainder(l,f,c,k,634)for l,f,c,k in data],True)
refs=[(34,390,'Polynomial definition and non-polynomial contrast','Nonnegative integer exponents and nonzero leading coefficient define the degree; variable denominators/fractional exponents are excluded. Generic exposition is not a separate learner exercise.',[],'table',None),(35,390,'Example14 long-division layout','Divisorx−2, original constant3, quotient2x²+10x+16, remainder35. Align powers and repeat divide/multiply/subtract.',[QR],'table','Example:14'),(36,391,'Example14 incorrect dividend identity','The displayed top identity prints constant16 rather than original3. Its right side actually expands to the original constant3. This is a source display defect, not a wrong quotient.',[QR],'table','Example:14'),(37,391,'Polynomial division algorithm','P=DQ+R with degreeR<degreeD (orR=0). Rational form requires D≠0, while the polynomial identity is valid everywhere.',[QR],'table',None),(38,391,'Example15 long and synthetic division alternatives','Both calculate remainder−124 for (2x³−x)/(x+4). Synthetic root−4 must not be read as divisor+4.',[QR],'table','Example:15'),(39,391,'Synthetic-division method boundary note','The source recommends monic linear divisors. General coefficient methods can accommodate nonmonic divisors; a quadratic divisor does not fit this elementary one-root synthetic layout.',[QR],'table',None),(40,392,'Example16 quadratic long-division layout','Reorder both original polynomials and insert zero x² coefficient. Stop at remainder−9x+5, whose degree1 is below divisor degree2.',[QR],'table','Example:16'),(41,393,'Remainder theorem derivation and nonmonic root','P(x)=(x−c)Q(x)+R givesP(c)=R. For divisorax−b usec=b/a witha≠0; do not substitute the unnormalised constantb.',[REM],'table',None)]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C8:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C8:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Read each coefficient, missing-power column and divisor sign from the rendered source; independently reconstruct the actual division identity and compare the remainder degree. Separate source method advice from a mathematical impossibility claim.'
h.pages=[dict(pdf_page=page,printed_page=pp(page),chapter=8,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=['8227:TB:YM:C8:Example:14']if page==391 else[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExamples14–17,Try14–17 with both Try16 questions and eight teaching panels enumerated. Original variable names retained separately from the checker x.',scope_screen='Every actual division has dividend degree≤4 and linear/quadratic divisor. Remainder-theorem evaluations without division are distinguished.')for page in range(390,394)]
if __name__=='__main__':h.save('polynomial-division','Complete390–393 polynomial-division and remainder-theorem source census, including every asked quotient and remainder.')
