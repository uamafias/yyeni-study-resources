"""UNWIRED YM564–565: source initial-value policies, rearrangements and exact fixed points."""
import json
import author_YM_C13_opening as a
from author_YM_C13_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent,BRACKET
from author_Goldie_C6_iteration_intro import iterate
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
RELATE='8227:2020:M2:T6:O03:D01';REARRANGE='8227:2020:M2:T6:O03:D02';ITERATE='8227:2020:M2:T6:O04:D01';STOP='8227:2020:M2:T6:O04:D02'
def val(l,e,k,kp,ds,method):return a.a.val(l,e,k,kp,method,ds)

def sequence_parts(prefix,F,start,keys,display_dp,kp,equation,bracket,final,final_dp,start_policy,root_printed=True,equation_origin='given source equation'):
 parts=[]
 for step,key in enumerate(keys,1):
  p=iterate(prefix+'-x'+str(step+1),F,start,step,key,kp,dp=display_dp)
  p.update(assessed_8227_demand_ids=[ITERATE],component_demand_ids=[],given_representation='text',response_format='numeric',source_index_one_based=step+1,initial_value_policy=start_policy,author_reference_start=str(start),display_precision=str(display_dp)+'decimalplaces',original_iteration_formula=F)
  parts.append(p)
 p=val(prefix+'-root','0',final,kp,[ITERATE,STOP],'Independentlysolve the continuous verification equation in its admissible sign bracket,then round to the source requested accuracy. Separately test BOTH final iteration states at that accuracy;use unrounded states throughout. A stipulated start is binding;an author benchmark start is only one valid permitted trace.')
 p.update(operation=dict(kind='bracketed-source-root',operands=[equation,*map(str,bracket)],rounding=dict(decimal_places=final_dp)),verification_equation=equation,equation_origin=equation_origin,verification_bracket_origin='source-stated sign bracket'if equation_origin=='given source equation'else'author QA bracket for the derived fixed-point equation',requested_precision=str(final_dp)+' decimal places',initial_value_policy=start_policy,author_reference_start=str(start),depends_on_source_parts=[q['subpart']for q in parts])
 for name,count in [('last-state-target-precision',len(keys)),('previous-state-target-precision',len(keys)-1)]:
  p.setdefault('additional_operations',{})[name]=dict(kind='supplied-source-iteration',operands=[F,str(start)],steps=count,rounding=dict(decimal_places=final_dp));p.setdefault('additional_operation_expected',{})[name]=final
 if not root_printed:
  p.pop('printed_key_normalised');p.update(author_check_target_normalised=final,author_expected_normalised=final,check_mode='no key',key_presence='No separate final rounded root is printed;source table Yes and its states imply the author-formatted value.',source_key_limitation='Author-derived final rounding is corroborated by source states;do not quote it as a separately printed answer.')
 parts.append(p);return parts

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(mapping_rationale='Given original equation to provided rearrangement,provided iteration to original equation,and executing the prescribed map are distinct directions. Every calculated state is retained where requested;initial given state is not invented as another assessed output. A benchmark start chosen inside a source bracket is not mandatory when the stem leaves the start open. Rootaccuracyischeckedagainsttheverificationequation,notjustthemap.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT08',status='within',quoted_value=note,reason='Usegivenformula/rearrangementandunderstandconvergencequalitatively. Noformalderivativeconvergenceconditionisrequired.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT08']),precision_angle_check=dict(source='Example3/Try3/Example4root2dp;eachcalculatedstate4dp. Sourceformulaandinitial-valuepolicyretained.',comparison='Useunrounded80-digitstatesfornextapplicationandroundonlydisplay. Independentlybisection-checktheroot,andlasttwostatesattherequestedrootprecision. Nonzeroscalarmultiplesofaderivedequationarevalidunlessaformisexplicitlyfixed.'))
 return r
original='x**3-2*x**2+5*x-3'
p=a.bracket('a-sign-bracket',original,'Rational(7,10)','Rational(4,5)','-Rational(137,1000)','Rational(29,125)',564,'Originalcontinuouscubicvaluesf.7−.137,f.8+.232. Thislocatesthepositiveintervalusedforastart;derivative3x²−4x+5>0alsoconfirmsuniqueglobalrootasanindependentauthorcheck.')
q=val('b-coefficients','Tuple(-Poly('+original+',x).coeff_monomial(x**2),Poly('+original+',x).coeff_monomial(x))','Tuple(2,5)',564,[REARRANGE,RELATE],'MatchtheORIGINALmoniccubicto x(x²+b)−(a x²+3). Coefficientsgivea2,b5. Rearrangedrootformula x=(2x²+3)/(x²+5);denominatoralwayspositive. Sourceworkingdivisionbyxisvalidforthisbracketedroot;directcollectionavoidsunnecessarydivision.')
extra(q,'original-reconstruction','expand(x*(x**2+5)-(2*x**2+3))',original)
parts=[p,q]+sequence_parts('c','(2*x**2+3)/(x**2+5)','Rational(3,4)',['0.7416','0.7387'],4,564,original,['Rational(7,10)','Rational(4,5)'],'0.74',2,'No start stipulated;source note accepts any start between0.7and0.8. Benchmark0.75isonevalidreference.',root_printed=False)
for part in parts[2:]:part.setdefault('depends_on_source_parts',[]).append('b-coefficients')
add('Example',3,564,'(a)Verifycubicbracket.7..8;(b)finda2,b5inprovidedrationalrearrangement;(c)executeformula,each4dp,root2dp. Startnotstipulated;sourceworkinguses.75. Final.74isimpliedbytable,notseparatelyprinted.',parts)
original='6/x**2-x-1'
p=a.bracket('a-sign-bracket',original,'Rational(7,5)','Rational(8,5)','Rational(162,245)','-Rational(41,160)',653,'Originalcontinuousrationaldifferencebetween1.4and1.6hasvalues+.661224...and−.25625;pole0isoutsideinterval.')
q=a.a.reasoning('b-rearrangement','x=sqrt(6/(x+1)) for the indicated positive point P.','FromORIGINAL6/x²=x+1,multiplybynonzerox²toobtainx²=6/(x+1). Part(a)locatesPpositive,sotakethePOSITIVEroot;theprovidedformulaonlymakesrealvalueswhenx>−1,andthetargetdoesnotlieatx0. Anegativerootbranchisnotintroduced.',653,'show/prove');q.update(assessed_8227_demand_ids=[REARRANGE,RELATE],component_demand_ids=[],given_representation='text',response_format='proof/show-that',depends_on_source_parts=['a-sign-bracket']);extra(q,'cross-multiplied-original','expand((6/x**2-x-1)*x**2)','6-x**3-x**2')
parts=[p,q]+sequence_parts('c','sqrt(6/(x+1))','Rational(3,2)',['1.5492','1.5342','1.5387','1.5373'],4,653,original,['Rational(7,5)','Rational(8,5)'],'1.54',2,'Initialx1=1.5explicitlygiven;keepit,andkeeppositivesquare-rootbranch.')
for part in parts[2:]:part.setdefault('depends_on_source_parts',[]).append('b-rearrangement')
add('Try-Now',3,565,'Curve6/x²intersectsx+1atP:(a)verify1.4..1.6bracket;(b)showprovidedpositive-square-rootrearrangement;(c)GIVENstart1.5,each4dp,final2dp1.54. Originalrationaldomainretained.',parts)
F='2*x/3+4/x**2'
parts=sequence_parts('a',F,'2',['2.3333','2.2902','2.2894'],4,565,'x**3-12',['2','Rational(7,3)'],'2.29',2,'Initialx1=2explicitlygiven;Fundefinedat0.',equation_origin='Derived independently from supplied fixed-point equation,as asked in part(b).')
p=val('b-fixed-equation','expand(3*x**2*(x-(2*x/3+4/x**2)))','x**3-12',565,[RELATE,REARRANGE],'Limitαsatisfiesα=2α/3+4/α²withα≠0. Multiplyby3α²toobtainα³−12=0. Aconvergedvaluealonewouldnotjustifyignoringtheoriginalmapdomain.')
q=val('b-exact-alpha','Tuple(*solveset(x**3-12,x,domain=S.Reals))[0]','real_root(12,3)',565,[RELATE],'Thederivedequationhasuniquerealrootcuberoot12,positiveandnonzero. SubstituteitintotheORIGINALfixed-pointmap;realoddroot,notprincipalcomplexbranches.');extra(q,'original-fixed-point-residual','simplify((x-(2*x/3+4/x**2)).subs(x,real_root(12,3)))','0');q['depends_on_source_parts']=['b-fixed-equation']
parts.extend([p,q]);add('Example',4,565,'GIVENF2x/3+4/x²,start2:(a)iterationeach4dp,final2dp2.29;(b)derivefixed-pointequationandexactα=cuberoot12. Originalpolynomialisnotagivenbutarequiredlaterderivation.',parts)
refs=[(18,564,'Example3 original sign-change working','Exactsourcevalues−.137and+.232at.7,.8.',[BRACKET],'Example:3'),(19,564,'Example3 supplied-form coefficient derivation','Originalx³−2x²+5x−3rewritestox(x²+5)=2x²+3;a2,b5.',[REARRANGE],'Example:3'),(20,564,'Example3 initial-value and iteration table','Workingstart.75isoneacceptedchoice,notastemrequirement. Display.7416,.7387andtableYesat2dpimply.74.',[ITERATE,STOP],'Example:3'),(21,564,'Example3 calculator recurrence reminder','UsefullAnsvaluewhenapplyingthenextstep;donotfeedroundedfour-decimaldisplaybackintomap.',[ITERATE],'Example:3'),(22,565,'Example4 calculator recurrence instruction','Sourcegivenstart2andmap2Ans/3+4/Ans²;keybuttoninstructionisprocedurecontext,notanotherassessedtask.',[ITERATE],'Example:4'),(23,565,'Example4 supplied-map iteration table','2,2.3333,2.2902,2.2894;lasttwoboth2.29at2dp.',[ITERATE,STOP],'Example:4'),(24,565,'Example4 derived-equation exact root working','Nonzerofixedpointimpliesx³12,uniquerealpositivecuberoot12.',[RELATE,REARRANGE],'Example:4')]
for n,page,label,note,ds,parent in refs:
 fig(n,page,label,note,ds,'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C13:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C13:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readinitial-valuepolicy,displayprecision,sourceformulaandsignvalues. Independentlyreplayfull-precisionstatesandsolvetheverificationequation. Equationdirectionandnonzerodenominator/positive-rootbranchesareexplicit;formalconvergencetheoremnotmandated.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=13,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample3/Try3,Example4andactualworkedderivation/iteration/calculatorreminderpanelsenumerated. Sourceinitial-valuechoiceandgivenstartsdistinguished;calculatedstatesrequestedexplicitlyretained.',scope_screen='Givenrearrangements,suppliediterationandfixed-pointequationderivation. Positive/even-rootandnonzero-mapdomainsretained;formalconvergenceconditionexcluded.')for page in range(564,566)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    expected=p.get('author_expected_normalised',p.get('printed_key_normalised',p.get('author_check_target_normalised')))
    assert equivalent(compute(p['operation']),expression(expected)),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C13-iteration-examples.json',dict(scope='Complete564–565bracket/rearrangement/iterationresponses.',items=answers)),('census-YM-C13-iteration-examples.json',dict(book='YM',book_id='8227-SRC-017',chapter=13,source_path=SRC,source_sha256=SHA,scope='Complete564–565page/item/teachingpanelcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
