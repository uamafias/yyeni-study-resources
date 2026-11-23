"""Author-only traces of fixed textbook formulas,with original-equation checks."""
from decimal import Decimal,localcontext,ROUND_HALF_UP
import mpmath as mp
import sympy as sp
from verify_textbook_answers_r5 import expression,compute

def trace(F,start,original,a,b,answer_dp,display_dp):
    x=expression('x');formula=expression(F);residual=expression(original)
    fn=sp.lambdify(x,formula,'mpmath');original_fn=sp.lambdify(x,residual,'mpmath')
    records=[];previous_rounded=None
    with mp.workdps(80),localcontext()as context:
        context.prec=80
        current=mp.mpf(str(sp.N(expression(str(start)),79)))
        lo,hi=[mp.mpf(str(sp.N(expression(str(z)),79)))for z in[a,b]]
        def rounded(z,places):return str(Decimal(str(z)).quantize(Decimal(1).scaleb(-places),rounding=ROUND_HALF_UP))
        for j in range(101):
            records.append({'index_one_based':j+1,'unrounded':str(current),'display':rounded(current,display_dp)})
            answer=rounded(current,answer_dp);center=mp.mpf(answer);half=mp.mpf(10)**(-answer_dp)/2
            left,right=center-half,center+half
            if j>=3 and answer==previous_rounded and lo<=left<right<=hi and original_fn(left)*original_fn(right)<0:
                independent=compute({'kind':'bracketed-source-root','operands':[original,str(a),str(b)],'rounding':{'decimal_places':answer_dp}})
                assert independent==expression(answer)
                return {'formula':F,'start':str(start),'original_equation':original,'original_target_bracket':[str(a),str(b)],'answer_decimal_places':answer_dp,'display_decimal_places':display_dp,
                  'records':records,'answer':answer,'certified_rounding_cell':[str(left),str(right)],
                  'certificate':'At least three actual applications,two consecutive equal requested displays,and an opposite-sign original-equation bracket strictly inside the selected root interval. Source-specific uniqueness is justified separately;stability alone is not the certificate.'}
            previous_rounded=answer;current=fn(current)
            assert isinstance(current,mp.mpf)and mp.isfinite(current),'source iteration left its real finite domain'
    raise AssertionError('source iteration did not obtain a certified requested display')
