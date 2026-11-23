"""YM575–578: golden-ratio support and coupled circle/curve-area problems."""
from author_YM_C13_late_support import *
from author_Goldie_C6_iteration_intro import iterate
reset()
SEG='8227:2020:M1:T5:O02:D03';SECTOR='8227:2020:M1:T5:O02:D02';AREA='8227:2020:M1:T9:O04:D01';DEF='8227:2020:M1:T9:O03:D01';TRIGINT='8227:2020:M2:T5:O01:D02'
keys=['2','1.5','1.6666','1.6','1.625','1.615384615','1.619047619','1.617647059','1.618181818']
parts=[]
for step,key in enumerate(keys,1):
    p=iterate('phi'+str(step+1),'1+1/x','1',step,key,576)
    p['operation']=p['additional_operations']['unrounded_supplied_iterate']
    if key in ['2','1.5','1.6','1.625']:
        pass
    else:p['printed_approximation_check']=dict(source_claim='Illustrative ellipsis values with no per-state rounding instruction.',required_rounding=None,absolute_error_strictly_below=f'Rational(1,{10**len(key.split(".")[1])})')
    p.update(assessed_8227_demand_ids=[],component_demand_ids=[],given_representation='text',response_format='numeric',evidence_role='supporting golden-ratio demonstration')
    parts.append(p)
p=val('phi-root','(1+sqrt(5))/2','Rational(809,500)',576,[],'Positive fixed point satisfies phi²−phi−1=0; choose positive (1+sqrt5)/2. Round independently to3dp1.618. Source table header5sf is wrong: its last two states agree at3dp, not5sf.')
p['operation']=dict(kind='rounded',operands=['(1+sqrt(5))/2'],decimal_places=3);parts.append(p)
row=add('Worked-illustration',3,576,'Golden-ratio calculation with supplied map1+1/phi and start1; nine calculated states, final3dp1.618. Source header5sf conflicts with intended3dp stopping. Supporting illustration, no additional assigned-question coverage.',parts,fresh=True)
row['evidence_role']='prerequisite/supporting worked illustration';row['teaches_8227_demand_ids']=[RELATE,ITERATE,STOP]
f='pi/3+sin(x)-x'
p=reason('a-segment-equation','alpha=pi/3+sin alpha, 0<alpha<pi.','Minor segment area r²(alpha−sin alpha)/2 equals pi r²/6. Cancel positive r²/2 and rearrange. Keepr>0 and the minor central-angle domain; the radius cancels because this is an area fraction.',577,[SEG,REARRANGE],rep='diagram');p['component_demand_ids']=[SECTOR];extra(p,'area-reconstruction','simplify((x-sin(x))/2-pi/6-(x-sin(x)-pi/3)/2)','0')
q=a.bracket('b-sign-bracket',f,'pi/2','2*pi/3','1-pi/6','sqrt(3)/2-pi/3',577,'At pi/2 residual positive, at2pi/3 negative, in radians.');q['depends_on_source_parts']=['a-segment-equation']
parts=[p,q]+b.sequence_parts('c','pi/3+sin(x)','2',['1.9565','1.9737','1.9671'],4,577,f,['pi/2','2*pi/3'],'1.97',2,'Stem stipulates2; radians; each4dp and final2dp.')
add('Example',9,577,'GIVEN circle, central angle0<alpha<pi, minor segment one sixth ofcircle. Derive supplied relation, verify pi/2..2pi/3 bracket, execute map from2; each4dp, final2dp1.97.',parts,'diagram')
f='2*sin(x)-x'
p=reason('a-equal-areas-relation','alpha=2sin alpha.','Equal minor segment and triangle means r²(alpha−sin alpha)/2=r²sin alpha/2. For actual nondegenerate logo r>0, cancel and obtainalpha=2sin alpha. The zero-angle algebraic solution is excluded by the GIVEN two-distinct-endpoints shape.',655,[SEG,REARRANGE],rep='diagram');p['component_demand_ids']=[SECTOR];extra(p,'area-relation','expand((x-sin(x))-sin(x))','x-2*sin(x)')
parts=[p]+b.sequence_parts('b','2*sin(x)','Rational(37,20)',['1.9226','1.8775','1.9066','1.8883','1.9001','1.8926','1.8974','1.8943','1.8963','1.8950'],4,655,f,['Rational(9,5)','2'],'1.90',2,'Stem stipulates1.85; source final is3 significant figures1.90 (numerically same as2dp here). No per-state precision stipulated; key uses4dp.')
parts[-1]['requested_precision']='3 significant figures'
p=val('c-chord-cm','0','13',655,[],'With radius8cm, chord=16sin(alpha/2), equivalently cosine rule. Independently solve nonzero angle from2sin alpha−alpha=0, not from a rounded key. Exact internal alpha≈1.895494... gives 12.99364779768388; final matches the key13.0cm at3sf.')
# This output is evaluated from the original geometric equation at80digits.
p['operation']=dict(kind='identity',operands=['16*sin(nsolve(2*sin(x)-x,Rational(19,10),prec=80)/2)'])
p['printed_approximation_check']=dict(source_claim='Key13.0cm with no stem precision; compare its3sf accuracy.',required_rounding=None,absolute_error_strictly_below='Rational(1,20)')
p['units']='cm';p['depends_on_source_parts']=['b-root'];p['prerequisite_knowledge']=[dict(skill='Cosine rule or isosceles-triangle chord formula',role='Directly asked prerequisite extension in partc; no matching8227demand is invented. The preceding angle is the assessed8227numerical/circular-area result.')];parts.append(p)
add('Try-Now-9',1,578,'GIVEN circle-logo minor segment equals triangle. Derivealpha=2sin alpha, nondegenerate positive angle; start1.85 and final3sf1.90; then chord XY forradius8cm, key13.0cm.',parts,'diagram')
p=val('a-area-R','integrate(cos(x),(x,a,pi/2))','1-sin(a)',655,[AREA,TRIGINT,DEF],'Read shaded area to the RIGHT ofx=theta, belowcosx and aboveaxis. Integrate fromtheta topi/2, giving1−sin theta; theta is represented bya in CAS.');p.update(original_integrand='cos(x)',original_bounds=['a','pi/2'],source_parameter='theta represented by a')
q=reason('b-equal-area-recurrence','theta=(1−sin theta)/cos theta.','Rectangle OABC has widththeta and heightcos theta; equal shaded area gives theta cos theta=1−sin theta. For the nondegenerate interior point0<theta<pi/2, cos theta>0, so division is valid. Endpointpi/2 would be a degenerate0=0 equality, not a valid rectangle.',655,[AREA,REARRANGE],rep='graph');extra(q,'equal-area-equation','expand(x*cos(x)-(1-sin(x)))','x*cos(x)+sin(x)-1');q['depends_on_source_parts']=['a-area-R']
parts=[p,q]+b.sequence_parts('c','(1-sin(x))/cos(x)','Rational(1,2)',['0.5932','0.5319','0.5719','0.5456','0.5628','0.5515','0.5589','0.5541','0.5572','0.5552'],4,655,'x*cos(x)+sin(x)-1',['Rational(1,2)','Rational(3,5)'],'0.56',2,'Given theta1=.5; radians. QA bracket.5..6 is author-derived for the interior nondegenerate root.')
parts[-1]['verification_bracket_origin']='Author QA bracket for nondegenerate interior root; not a source-stated bracket.'
add('Try-Now-9',2,578,'GIVEN cosine curve, rectangle OABC and right-hand shaded R, interior0<theta<pi/2. Find area, derive provided equal-area map, then start.5; each4dp, final2dp.56. Degenerate endpoint excluded.',parts,'graph')
refs=[
 (55,575,'Golden-ratio partition diagram','Longa,shortb,wholea+b; positive equal ratios imply phi²−phi−1=0. Displayed decimal partitions are approximate.',[RELATE],'diagram',None,False),
 (56,575,'Approximate100-unit golden partition','61.8and38.2sum100; ratios displayed1.618 are approximations, not exact equalities.',[RELATE],'diagram',None,False),
 (57,575,'Golden-ratio exact relation and numeric expansion','Positive root (1+sqrt5)/2; native long decimal1.61803398874989484820 is correct. Adjacent algebra incorrectly labels b/a=phi; it must be1/phi. Final fixed-point relation is correct.',[RELATE],'table',None,False),
 (58,576,'Golden-ratio recurrence table','Start1; approximate ellipsis displays; final1.618to3dp. Native5sfheaderwrong.',[ITERATE,STOP],'table','Worked-illustration:3',False),
 (59,576,'Fibonacci consecutive-ratio table','3/2=1.5,5/3≈1.6667,233/144≈1.61806,377/233≈1.61803; finite ratios are approximations, not exactlyphi.',[RELATE],'table',None,False),
 (60,576,'Fibonacci-square spiral teaching diagram','Square side labels1,2,3,5,8,13 support a quarter-circle approximation to a logarithmic golden spiral; not exact identity of the two curves.',[],'diagram',None,False),
 (61,577,'Example9 GIVEN minor circular segment','ChordAB,centreO,radii r,centralalpha0..pi, shaded minor segment area pi r²/6; rpositive and cancels.',[SEG],'diagram','Example:9',True),
 (62,577,'Example9 area derivation','Sector minus isosceles triangle, then fraction ofwholecircle; retain radians.',[SEG,REARRANGE],'table','Example:9',False),
 (63,577,'Example9 sign-bracket working','Residualpi/3+sinx−x: positive atpi/2, negative at2pi/3.',[BRACKET],'table','Example:9',False),
 (64,577,'Example9 recurrence and rounding-cell check','Given2; table1.9565,1.9737,1.9671. Signs at1.965and1.975 independently certify1.97to2dp.',[ITERATE,STOP],'table','Example:9',False),
 (65,578,'Try9Q1 GIVEN equal-area logo','Unshaded minor segment equals shaded triangle; X,Y distinct; angle inradians, radius8cm introduced only inc.',[SEG],'diagram','Try-Now-9:1',True),
 (66,578,'Try9Q2 GIVEN cosine rectangle and shaded region','B(theta,cos theta),A(theta,0),C(0,cos theta); R undercosx fromtheta topi/2. Theta interior, not endpoint.',[AREA],'graph','Try-Now-9:2',True)]
for args in refs:panel(*args)
pages=census(575,578,{575:'All partition diagrams and exact-relation/number panels. Cultural/visual context does not create new prescribed golden-ratio or spiral scope.',576:'Complete golden-ratio worked calculation, Fibonacci ratio table and square/spiral teaching figure. New supporting worked illustration recovered; no extra assigned practice coverage.',577:'All Example9 parts, GIVEN segment, area derivation, bracket working and recurrence/rounding-cell panel.',578:'Both Try9 problems, both GIVEN diagrams, and every area/relation/iteration/chord response. Retain interior-angle and nondegenerate-area constraints.'})
if __name__=='__main__':save('geometry',pages)
