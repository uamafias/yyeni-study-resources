"""Additional independent Ridder references for fixed-source root QA."""
import json
import mpmath as mp
import sympy as sp
from analysis_sources import WB,write
from verify_textbook_answers_r5 import compute,expression,x

def main():
    checked=[];seen=set();iteration_checks=[];trace_checks=[]
    with mp.workdps(75):
        for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
            for item in json.loads(path.read_text())['items']:
                for part in item['subparts']:
                    if part.get('iteration_trace'):
                        t=part['iteration_trace'];formula=expression(t['formula']);current=sp.N(expression(t['start']),75)
                        for j,record in enumerate(t['records']):
                            assert record['index_one_based']==j+1
                            difference=abs(sp.N(current-expression(record['unrounded']),65))
                            assert difference<sp.Float('1e-58')*(1+abs(current)),(item['item_id'],part['subpart'],j,'trace value')
                            displayed=compute({'kind':'rounded','operands':[str(current)],'decimal_places':t['display_decimal_places']})
                            assert displayed==expression(record['display']),(item['item_id'],part['subpart'],j,'trace display')
                            current=sp.N(formula.subs(x,current),75)
                        left,right=map(expression,t['certified_rounding_cell']);a,b=map(expression,t['original_target_bracket']);f=expression(t['original_equation'])
                        assert a<=left<right<=b
                        signs=[sp.sign(sp.N(f.subs(x,z),60))for z in[left,right]]
                        assert signs[0]*signs[1]==-1
                        trace_checks.append({'item_id':item['item_id'],'subpart':part['subpart'],'states_checked':len(t['records']),'independent_CAS_replay':True,'rounding_cell_signs':list(map(str,signs)),'answer':t['answer']})
                    for op in [part.get('operation',{}),*part.get('additional_operations',{}).values()]:
                        if op.get('kind')=='supplied-source-iteration':
                            clean={k:v for k,v in op.items()if k!='rounding'}
                            marker=(item['item_id'],part['subpart'],json.dumps(clean,sort_keys=True))
                            if marker in seen:continue
                            seen.add(marker)
                            formula=expression(op['operands'][0]);current=sp.N(expression(op['operands'][1]),75);values=[current]
                            for unused in range(op['steps']):
                                current=sp.N(formula.subs(x,current),75);values.append(current)
                            got=compute(clean);expected=sp.Tuple(*values)if op.get('return_sequence')else current
                            pairs=list(zip(got,expected))if isinstance(expected,sp.Tuple)else[(got,expected)]
                            for actual,wanted in pairs:
                                assert abs(sp.N(actual-wanted,65))<sp.Float('1e-58')*(1+abs(wanted)),(item['item_id'],part['subpart'],'independent iteration')
                            iteration_checks.append({'item_id':item['item_id'],'subpart':part['subpart'],'steps':op['steps'],'independent_CAS_replay':True})
                            continue
                        if op.get('kind')!='bracketed-source-root':continue
                        clean={k:v for k,v in op.items()if k!='rounding'}
                        key=(item['item_id'],part['subpart'],json.dumps(clean,sort_keys=True))
                        if key in seen:continue
                        seen.add(key)
                        f,a,b=map(expression,op['operands']);fn=sp.lambdify(x,f,'mpmath')
                        lo,hi=[mp.mpf(str(sp.N(z,74)))for z in[a,b]]
                        reference=mp.findroot(fn,(lo,hi),solver='ridder',tol=mp.mpf('1e-65'),maxsteps=150)
                        computed=mp.mpf(str(compute(clean)))
                        assert lo<=reference<=hi and abs(reference-computed)<mp.mpf('1e-58'),(item['item_id'],part['subpart'])
                        checked.append({'item_id':item['item_id'],'subpart':part['subpart'],'original_equation_residual':str(f),'bracket':[str(a),str(b)],'independent_Ridder_root':str(reference),'bisection_root':str(computed),'difference':str(abs(reference-computed))})
    rejected=[]
    for op,reason in [({'kind':'bracketed-source-root','operands':['x**2+1','-1','1']},'sign bracket'),({'kind':'bracketed-source-root','operands':['1/x','-1','1']},'original discontinuity')]:
        try:compute(op)
        except AssertionError as e:assert reason in str(e);rejected.append(str(e))
        else:raise AssertionError('invalid root bracket accepted')
    write(WB/'checks/r5/numerical-root-independent-checks.json',{'status':'author independent numerical method checks;cross-vendor acceptance pending','root_checks':checked,'supplied_iteration_checks':iteration_checks,'certified_trace_checks':trace_checks,'invalid_brackets_rejected':rejected,'limits':'Bisection and Ridder agree inside the listed continuous sign brackets. This is not a proof that all roots were found;the source-specific graph/monotonicity arguments must establish completeness separately.'})
    print(len(checked),'Ridder root checks;',len(iteration_checks),'supplied-sequence checks;',len(trace_checks),'iteration traces/',sum(r['states_checked']for r in trace_checks),'states replayed;invalid sign/pole brackets rejected')
if __name__=='__main__':main()
