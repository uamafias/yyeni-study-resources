"""Two complete investigations and Examples5–8, with explicit scope roles."""
import json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,indefinite,definite,compute,expression,equivalent
from author_Goldie_C5_opening import answers,corrections,fig,figures
from author_Goldie_C5_opening import add as _add
answers.clear();corrections.clear();figures.clear()
TRIGINT='8227:2020:M2:T5:O01:D02';IDENTINT='8227:2020:M2:T5:O02:D01';SQUARED='8227:2020:M2:T5:O02:D02';DEF='8227:2020:M1:T9:O03:D01'
GP='8227:2020:M1:T2:O03:D02';MODEL='8227:2020:M1:T2:O03:D03';ELEMENTARY='8227:2020:M2:T4:O01:D01';POWER='8227:2020:M1:T8:O02:D01'
def ev(page):
 from author_Goldie_C5_opening import ev as base
 if page>=345:return base(page)
 from pathlib import Path
 import hashlib
 p=W/'checks/r5/textbooks/Goldie-C5-142.png'
 return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def add(kind,n,page,note,parts,direct,components=None):
 row=_add(kind,n,page,note,parts,direct,components)
 for p in row['subparts']:p['source_evidence']=ev(page);p['key_evidence']=ev(p['answer_pdf_page'])
 return row
p=value('a0','exp(0)','1',345,'Substitute x=0 into the proposed series. Only its constant term remains.')
p2=reasoning('coefficients','aₙ=1/n! for n≥0; first coefficients are1,1,1/2,1/6,1/24.',
 'After n derivatives, substituting0 gives1=n! aₙ, provided the proposed exponential power series is differentiated term by term. This is a source exploration beyond prescribed8227binomial expansion, not a new syllabus requirement. For the finite first coefficients compute successive derivatives of e^x at0 divided by factorials.',345,'matches')
p2['additional_operations']={'first_coefficients':{'kind':'identity','operands':['Tuple('+','.join(f'diff(exp(x),x,{j}).subs(x,0)/factorial({j})'for j in range(5))+')']}}
p2['additional_operation_expected']={'first_coefficients':'Tuple(1,1,1/2,1/6,1/24)'}
p3=value('e-eight-dp','+'.join(f'1/factorial({j})'for j in range(13)),'2.71828183',345,'Sum through n=12. The remaining positive tail is at most (1/13!)/(1−1/14), since later term ratios do not exceed1/14. Both ends of that rigorous bracket round to2.71828183 at8decimal places.')
p3['operation']={'kind':'rounded','operands':['+'.join(f'1/factorial({j})'for j in range(13))],'decimal_places':8}
p3['additional_operations']={'tail_bracket_upper_rounded':{'kind':'rounded','operands':['+'.join(f'1/factorial({j})'for j in range(13))+'+(1/factorial(13))/(1-1/14)'],'decimal_places':8}}
p3['additional_operation_expected']={'tail_bracket_upper_rounded':'2.71828183'}
row=add('Investigation',1,142,'Derive the coefficients of the proposed infinite series for e^x by repeated differentiation at0, identify the factorial pattern, then use x=1 to approximate e. Maclaurin-series derivation is outside prescribed8227scope; record the complete source response without claiming AS-demand coverage.',[p,p2,p3],[],[])
row['scope_check']={'status':'out-of-scope','basis':'8227 prescribes positive-integer binomial expansions, not Taylor/Maclaurin series. This entire source exploration is retained internally only.','excluded_or_qualified_parts':['whole investigation'],'limits_considered':['8227:QUAL02']}
row['value_level_scope_decisions']=[{'rule_id':'8227:QUAL02','status':'outside','quoted_value':'e^x=Σaₙxⁿ, infinite power series; find aₙ by repeated derivatives.','reason':'Not a positive-integer binomial expansion; it must not enlarge syllabus scope.'}]
row['evidence_role']='excluded source occurrence; complete Maclaurin source QA only; no8227coverage'
parts=[]
for label,expr,key,dp in [('A','2','2',None),('B','(1+1/10)**10','2.594',3),('C','(1+1/20)**20','2.653',3),('1000-instalments','Pow(1001/1000,1000,evaluate=False)','2.717',3),('10000-instalments','Pow(10001/10000,10000,evaluate=False)','2.718',3),('million-instalments','Pow(1000001/1000000,1000000,evaluate=False)','2.71828',5)]:
 p=value(label,expr,key,345,'With n equal payments over the full10years and total nominal interest1, repeated multiplication gives R=(1+1/n)^n. Evaluate independently and compare only at the source written precision. The enlarged answer page states10^6 instalments, not10^5.')
 if dp is not None:p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp}
 parts.append(p)
p=reasoning('scheme-choice','B pays more than A; half-yearly C pays more than B. For a fixed positive nominal total interest, increasingly frequent equal compounding approaches e times the initial amount.',
 'A has ratio2; B is2.5937424601; C≈2.653297705. These finite compound models are geometric-progression applications. The limiting process with changing n is enrichment, not a convergent fixed-ratio GP sum. The printed million-payment result agrees with e to5decimal places.',345,'matches')
p['additional_operations']={'continuous_limit':{'kind':'identity','operands':['limit((1+1/x)**x,x,oo)']},'e_five_dp':{'kind':'rounded','operands':['E'],'decimal_places':5}}
p['additional_operation_expected']={'continuous_limit':'E','e_five_dp':'2.71828'};parts.append(p)
row=add('Investigation',2,142,'Compare100%lump interest after10years with10%annual compounding and20half-yearly5%payments;extend to more equal payments and investigate the limiting ratio. The principal cancels in every ratio. Finite GP models are in scope; the changing-frequency limit is enrichment.',parts,[GP,MODEL])
row['scope_check']={'status':'in-scope-parts-only','basis':'Finite compound-growth/GP calculations prescribed; formal continuous-compounding limit is supporting extension.','excluded_or_qualified_parts':['formal changing-frequency limit is enrichment, not prescribed fixed-ratio GP convergence']}
add('Example',5,143,'Integrate sec²x,sin2x,cos(3x−π) indefinitely. All arguments are radians;retain tangent poles and the linear-argument factors.',[
 indefinite('i','sec(x)**2','tan(x)',143),indefinite('ii','sin(2*x)','-cos(2*x)/2',143),indefinite('iii','cos(3*x-pi)','sin(3*x-pi)/3',143)],[TRIGINT])
add('Example',6,143,'Evaluate the exact proper integral of sin2x−cos4x over[0,π/3]. Retain both linear-argument integration factors and exact special-angle signs.',[
 definite('value','sin(2*x)-cos(4*x)',0,'pi/3','(6+sqrt(3))/8',143)],[TRIGINT,DEF])
p=indefinite('primitive','sin(x)**2','x/2-sin(2*x)/4',144)
p['additional_operations']={'chosen_identity':{'kind':'trig-identity-residual','operands':['sin(x)**2','(1-cos(2*x))/2']}};p['additional_operation_expected']={'chosen_identity':'0'}
add('Example',7,144,'Integrate sin²x by choosing the double-angle power reduction sin²x=(1−cos2x)/2. The identity choice is central to the requested integral.',[p],[IDENTINT,SQUARED],[TRIGINT])
p=indefinite('primitive','cos(x)**4','sin(4*x)/32+sin(2*x)/4+3*x/8',145)
p['additional_operations']={'repeated_reduction':{'kind':'trig-identity-residual','operands':['cos(x)**4','cos(4*x)/8+cos(2*x)/2+3/8']}};p['additional_operation_expected']={'repeated_reduction':'0'}
row=add('Example',8,144,'Integrate cos⁴x by applying the square-reduction identity twice, first to(cos²x)² and then to cos²2x. The solution continues145. The syllabus allows identities to facilitate integration with cos²x as an example, rather than declaring every higher even power excluded.',[p],[IDENTINT,SQUARED],[TRIGINT])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[145]})
# Figure helper belongs to the opening module; override source evidence explicitly.
fig(9,143,'Three linear-argument trig primitive references','For a≠0:∫cos(ax+b)=sin(ax+b)/a+c;∫sin(ax+b)=−cos(ax+b)/a+c;∫sec²(ax+b)=tan(ax+b)/a+c. Radians and original tangent poles are essential.',[TRIGINT],'table',
 [('diff(sin(a*x+b)/a,x)','cos(a*x+b)'),('diff(-cos(a*x+b)/a,x)','sin(a*x+b)'),('diff(tan(a*x+b)/a,x)','sec(a*x+b)**2')])
fig(10,144,'Cosine-square teaching reduction','The unprompted follow-on formula cos²x=(1+cos2x)/2 explains how the sine-square example transfers to cosine. It is teaching support rather than an extra assigned question.',[IDENTINT,SQUARED],'table',[('cos(x)**2-(1+cos(2*x))/2','0')])
for f in figures:f['source_evidence']=ev(f['pdf_page'])
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Both investigations and every Example5–8 subpart/reference enumerated. Example8continues145;that page awaits combined5B census.'}for page in range(142,145)]
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-middle.json',{'scope':'Both investigations completed as source QA, with excluded/enrichment scope explicit; Examples5–8 complete.','items':answers}),('census-Goldie-C5-middle.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete142–144;Example8continuation145awaits5B census.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],str(got)[:300],p['printed_key_normalised'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
