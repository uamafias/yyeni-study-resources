"""YM569–570: qualitative comparison retained; formal gradient tests extension."""
from author_YM_C13_late_support import *
from author_Goldie_C6_iteration_intro import iterate
reset()
parts=[]
for prefix,F,keys in [('divergent','real_root(7-5*x,3)',['1.25992105','0.888070875','1.367917632','0.543348918','1.624019815']),('convergent','(7-x**3)/5',['1.2','1.0544','1.165552186','1.083316697','1.145729307'])]:
    for step,key in enumerate(keys,1):
        p=iterate(prefix+'-x'+str(step+1),F,'1',step,key,569,dp=len(key.split('.')[1]),prefix=False)
        p['operation']=p['additional_operations']['unrounded_supplied_iterate']
        p['printed_approximation_check']=dict(source_claim='Illustrative ellipsis display; no decimal-place rounding instruction. Some last digits are rounded, others truncated.',required_rounding=None,absolute_error_strictly_below=f'Rational(1,{10**len(key.split(".")[1])})')
        p.update(assessed_8227_demand_ids=[],component_demand_ids=[],given_representation='text',response_format='numeric',evidence_role='supporting teaching calculation; not an extra assigned question',source_precision_note='The finite ellipsis approximation is checked to less than one unit in its last written digit. This is not a requested rounded response; keep full internal recurrence states.')
        parts.append(p)
q=reason('compare-maps','The real-cube-root map spirals outward; (7−x³)/5 converges, with alpha=1.1 to2sf.','Both fixed-point equations recover x³+5x−7=0. Replay both starts at1. The first map repels at the root; the second maps[1,1.2] into itself with derivative magnitude at most.864 there. These derivative arguments are independent author QA only. The provided graphs and traces teach qualitative failure/convergence.',569,[],status='matches')
q['taught_demand_ids']=[CONVERGE,FAIL];parts.append(q)
extra(q,'original-map-equation','expand(5*x-(7-x**3))','x**3+5*x-7')
r=val('root-2sf','0','Rational(11,10)',569,[],'Independently bracket the original increasing cubic between1and1.2; root rounds1.1 to2sf.')
r['operation']=dict(kind='bracketed-source-root',operands=['x**3+5*x-7','1','Rational(6,5)'],rounding=dict(significant_figures=2));parts.append(r)
row=add('Worked-illustration',2,569,'Unnumbered two-map comparison: x³+5x−7=0, both supplied formulas start1; compare qualitative convergence and report successful root2sf1.1. Supporting demonstration, not another assigned question.',parts,fresh=True)
row['evidence_role']='prerequisite/supporting teaching demonstration';row['teaches_8227_demand_ids']=[CONVERGE,FAIL,ITERATE,STOP]

def choice(kind,n,f,bad,good,kp,note,bad_deriv,good_deriv,bad_value,good_value):
    p=reason('nonconvergent-rearrangement',bad,note+' At the specified root, this fixed point is repelling. A large gradient at an arbitrary nearby point alone is not a global theorem.',kp,[FAIL],'matches')
    q=reason('convergent-rearrangement',good,note+' This map is attracting near the selected root; retain the original branch/domain. The source requests inventing rearrangements and uses formal derivative tests; those requirements are extension.',kp,[CONVERGE],'matches')
    extra(p,'independent-displayed-derivative',bad_deriv,bad_value);extra(q,'independent-displayed-derivative',good_deriv,good_value)
    r=add(kind,n,570,note,[p,q])
    r.update(scope_check=dict(status='in-scope-parts-only',basis='Qualitative interpretation of the supplied source comparison is relevant. Unprompted invention of convergent/divergent formulas and the formal derivative test are outside the prescribed provided-rearrangement demand.',excluded_or_qualified_parts=['independently invent two rearrangements','formal |Fprime(alpha)| condition'],limits_considered=['8227:LIMIT08']),
             value_level_scope_decisions=[dict(rule_id='8227:LIMIT08',status='outside',quoted_value=note,reason='Named invention/formal-test parts only: the source asks for a successful and an unsuccessful rearrangement without providing their forms. Retain qualitative comparison as internal support; do not treat the invention/formal test as examination coverage.')])
    return r
choice('Example',6,'exp(x)-3*x-1','(exp(x)-1)/3','log(3*x+1)',570,'Original e^x−3x−1=0; selected root1.5..2, not the additional root0. Compare F=(e^x−1)/3 and F=ln(3x+1), real log domain x>−1/3.',
       'diff((exp(x)-1)/3,x).subs(x,Rational(9,5))','diff(log(3*x+1),x).subs(x,Rational(9,5))','exp(Rational(9,5))/3','Rational(15,32)')
choice('Try-Now-6',1,'x**4-1-x','x**4-1','(x+1)**Rational(1,4)',654,'Quartic x⁴−1−x=0; selected positive root1..2. Source tests at1.5:13.5 versus approximately.13; negative quartic root is not a target of the principal fourth-root map.',
       'diff(x**4-1,x).subs(x,Rational(3,2))','diff((x+1)**Rational(1,4),x).subs(x,Rational(3,2))','Rational(27,2)','Rational(1,4)*Rational(5,2)**(-Rational(3,4))')
choice('Try-Now-6',2,'1/x-log(x)','1/log(x)','exp(1/x)',654,'Equation1/x−ln x=0, real domain x>0; selected root1..2. Source bad map1/ln x also excludes1; good map e^(1/x) excludes0. Tests at1.5 approximately−4.1 and−.9 are explanatory, not required syllabus conditions.',
       'diff(1/log(x),x).subs(x,Rational(3,2))','diff(exp(1/x),x).subs(x,Rational(3,2))','-2/(3*log(Rational(3,2))**2)','-4*exp(Rational(2,3))/9')
refs=[
 (32,569,'Two-map comparison prompt','Both maps have fixed-point equation x³+5x−7=0 and start1; one repels, one attracts.',[RELATE,FAIL], 'table','Worked-illustration:2'),
 (33,569,'Outward spiral graph','Supplied real-cube-root map and y=x; the successive cobweb steps move away from the selected root.',[FAIL],'graph','Worked-illustration:2'),
 (34,569,'Inward spiral graph','Supplied cubic rearrangement and y=x; local path approaches the fixed point.',[CONVERGE],'graph','Worked-illustration:2'),
 (35,569,'Inward spiral enlarged inset','Detail of alternate-side approach, not an additional mathematical task.',[CONVERGE],'diagram','Worked-illustration:2'),
 (36,569,'Divergent full-state table','Six displayed values including given initial1; ellipsis values are rounded at their varying written precisions.',[ITERATE,FAIL],'table','Worked-illustration:2'),
 (37,569,'Convergent full-state table','Six displayed values including1; final root1.1 to2sf.',[ITERATE,STOP],'table','Worked-illustration:2'),
 (38,570,'Formal gradient-test comparison','Source evaluates derivative at1, not at the root; a local observation is not a general necessary-and-sufficient theorem. LIMIT08 excludes formal convergence conditions.',[FAIL,CONVERGE],'table',None),
 (39,570,'Rearrangement warning','Formula choice matters. A conditional fixed-point equality does not prove convergence from every start.',[FAIL],'table',None),
 (40,570,'Example6 exponential-map working','Source compares two rearrangements near1.8; preserve selected nonzero root and log domain.',[FAIL,CONVERGE],'table','Example:6')]
for args in refs:panel(*args)
figures[-3]['scope_check']=dict(status='in-scope-parts-only',basis='Qualitative failure only; formal derivative convergence test extension.',excluded_or_qualified_parts=['formal derivative convergence conditions'])
pages=census(569,570,{569:'Complete unnumbered comparison prompt, both recurrence traces, two main graphs and magnified inset. One supporting worked illustration; no inflated assigned-item coverage.',570:'Formal derivative criterion and worked comparison panel explicitly screened as extension. All Example6 and Try6Q1–2 responses retained with precise scope limits.'})
if __name__=='__main__':save('convergence',pages)
