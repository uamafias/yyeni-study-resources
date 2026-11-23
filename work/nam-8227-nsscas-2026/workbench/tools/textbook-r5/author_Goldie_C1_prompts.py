"""Explicit R5 missing/boxed task annotations; human proofs are labelled as such."""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
rows=[]
def evidence(page,key=False):
    name='Goldie-keys-C1'if key else f'Goldie-C1-{15+4*((page-15)//4)}'
    path=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def auto(label,kind,operands,key):
    if isinstance(operands,str):operands=[operands]
    return {'subpart':label,'operation':{'kind':kind,'operands':operands},'printed_key_normalised':key}
def manual(label,status,conclusion,derivation):
    return {'subpart':label,'verification_mode':'manual-derivation','author_comparison_status':status,'author_conclusion':conclusion,'author_derivation':derivation}
def add(kind,n,page,key_page,note,parts,demands,components=None):
    for p in parts:
        p.update(source_evidence=evidence(page),key_evidence=evidence(key_page,True)if key_page>=333 else evidence(key_page),answer_pdf_page=key_page,answer_printed_page=key_page-14)
        p.setdefault('method','Independently derive the stated result from the original prompt; compare the specific printed key entry or explicitly record its absence.')
    row={'item_id':f'8227:TB:Goldie:C1:{kind}:{n}','source_pdf_page':page,'notes':note,
        'assessed_8227_demand_ids':demands,'component_demand_ids':components or[],
        'expected_subpart_labels':[p['subpart']for p in parts],'exam_style':False,'exam_style_basis':'Unnumbered/boxed teaching task,not source-labelled examination material.',
        'value_level_scope_decisions':[{'rule_id':'8227:LIMIT05','status':'not applicable','quoted_value':note,'reason':'No numerical polynomial division is requested; any general remainder property is identified as conceptual evidence.'}],
        'subparts':parts};rows.append(row);return row
F=lambda v:f'8227:2020:M2:T1:{v}'
pair=auto('cube-pairs','cube-pair-list','1729','Tuple(Tuple(1,12),Tuple(9,10))');pair['method']='Enumerate positive cubes up to12³and test each unordered pair for total1729; the two pairs agree with the exact printed key.'
algorithm=manual('finding-method','no key','Tabulate positive cubes up to1729,then for each cube look for its complement to1729; keep unordered pairs once. This finds1³+12³and9³+10³.','Any positive summand cube is at most1729,so its base is at most12. Enumerating that finite list and checking complements is complete. The printed key supplies the pairs but no search algorithm.');algorithm['key_presence']='No separate method answer in the inspected Chapter1 ?Page1key entry; author-derived explanation.'
add('Prompt',1,15,333,'Find two positive-cube decompositions of1729and explain a finite search method; enrichment arithmetic,not an8227assessed demand.',[pair,algorithm],[])
algorithm.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[333])
add('Prompt',2,31,334,'Evaluate g(3),g(-3)forg(x)=|x|,then contrast modulus of a sum/difference with sums of moduli.',[auto('function-values','identity','Tuple(Abs(3),Abs(-3))','Tuple(3,3)'),auto('four-moduli','identity','Tuple(Abs(3+3),Abs(3-3),Abs(3)+Abs(3),Abs(3)+Abs(-3))','Tuple(6,0,6,6)')],[F('O01:D01')])
proof=manual('remainder-degree','matches','The remainder is zero or has degree strictly less than the divisor degree n.','For a reduced polynomial division,if a nonzero remainderRhad degree at leastn,its leading term could be cancelled by subtracting a suitable multiple of the divisor. Adding that multiple to the quotient gives a lower-degree remainder,so the previous expression was not reduced. Constant divisors leave remainder0. Thus degR<nfor nonzeroR; the zero case is allowed. This independently derives the statement in the printed key.');proof['method']='Author algebraic proof using leading-term cancellation and the definition of reduced polynomial division; compared with the actual key sentence. Not mechanically proved.'
add('Prompt',3,27,333,'Given divisor degree n,explain why a reduced remainder is zero or has degree less than n; no particular dividend degree is supplied.',[proof],[F('O03:D03')])
ineq=auto('graph-reason','inequality','Abs(x)<2','Interval.open(-2,2)');ineq['method']='Read the two branches y=xforx>=0andy=-xforx<0. Below y=2,their intervals are[0,2)and(-2,0); their union is(-2,2),as in the printed two-case explanation.'
add('Prompt',4,33,334,'Use the earlier y=|x|graph to justify equivalence between|x|<2and-2<x<2,including both half-line cases.',[ineq],[F('O01:D03')],[F('O02:D02')])
f='x**3+2*x**2-3*x-7'
r=add('Worked-illustration',1,26,26,'Unnumbered remainder-theorem illustration dividesx^3+2x^2-3x-7byx-2and verifies the remainder3also equalsf(2).',[auto('quotient','quotient',[f,'x-2'],'x**2+4*x+5'),auto('remainder','remainder',[f,'x-2'],'3'),auto('substitution-check','identity','(x**3+2*x**2-3*x-7).subs(x,2)','3')],[F('O03:D01'),F('O03:D03'),F('O04:D01')])
r['value_level_scope_decisions'][0].update(status='within',quoted_value='(x^3+2x^2-3x-7) divided by(x-2)',reason='Actual dividend degree3and divisor degree1; nonzero scalar remainder is preserved.')
if __name__=='__main__':
    (W/'tools/textbook-r5/answers-Goldie-C1-prompts.json').write_text(json.dumps({'scope':'AllfourC1boxedprompts plus the newly found unnumbered worked illustration. Two human reasoning outputs are explicitly distinguished from executable arithmetic.','items':rows},ensure_ascii=False,indent=2)+'\n')
    print(len(rows),'prompt/illustration records')
