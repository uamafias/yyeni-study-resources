"""YM244–247: displacement, geometric division and collinearity proofs."""
import json
import author_YM_C5_magnitude_units as h
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,NOTATION,GEOM,SCALE
h.prior.answers.clear();h.prior.new.clear();figures.clear();h.prior.corrections.clear()
answers=h.prior.answers;new=h.prior.new;corrections=h.prior.corrections
ADD='8227:2020:M1:T7:O02:D01';DISP='8227:2020:M1:T7:O03:D02';POS='8227:2020:M1:T7:O03:D03';MAG=h.MAG
extra=h.extra
def add(kind,n,page,note,parts,direct,rep='text',continuation=None,new_item=False):
 r=h.prior.add(kind,n,page,note,parts,direct,new_item=new_item);r.update(representation=rep,component_demand_ids=[],mapping_rationale='The asked displacement,vector expression,norm or geometric proof is direct. In symbolic geometry,checker tuples are COEFFICIENTS of the explicitly recorded source vector basis,not point coordinates or scalar replacements for vectors. A proportionality proof needs a shared origin/incidence and a nonzero direction to establish a unique line.',value_level_scope_decisions=[])
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],'qualifier_applicability_note':'Prescribed elementary vector geometry. Original triangles/parallelograms are nondegenerate; division ratios are internal positive ratios. No formal3Dvector-line or other excluded technique is required.'}
 r['precision_angle_check']={'source':'Exact signed components and rational coefficients; norms kept as exact radicals. No rounding or angle units requested.','comparison':'Displacement is HEAD minus TAIL,not a sum of position vectors. Preserve endpoint order,internal segment-ratio orientation and a common point for collinearity. Merely parallel free vectors need not share one line.'}
 if continuation:r['continuation_pdf_pages']=continuation;corrections[-1]['continuation_pdf_pages']=continuation
 r['assessed_8227_demand_ids']=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 r['component_demand_ids']=sorted({d for p in parts for d in p.get('component_demand_ids',[])})
 if any(p.get('author_comparison_status')=='show/prove' for p in parts):r['component_demand_ids']=sorted(set(r['component_demand_ids'])|{POS,DISP,ADD,SCALE})
 r['component_demand_ids']=sorted(set(r['component_demand_ids'])-set(r['assessed_8227_demand_ids']))
 for p in parts:p.setdefault('given_representation',rep);p.setdefault('response_format','symbolic')
 if new_item:new[-1].update(item_kind='exercise',scope_check=r['scope_check'],component_demand_ids=r['component_demand_ids'],assessed_8227_demand_ids=r['assessed_8227_demand_ids'],mapping_rationale=r['mapping_rationale'],representation=rep)
 return r
def displacement(label,tail,head,key,kp):
 expr='Tuple('+','.join(f'({b})-({a})'for a,b in zip(tail,head))+')'
 p=v(label,expr,key,kp,'Read ORIGINAL endpoint coordinates and compute head minus tail in every component. Preserve the requested i,j,k basis form; a reversed arrow changes all signs.');p.update(source_arrow_tail=tail,source_arrow_head=head,assessed_8227_demand_ids=[DISP,NOTATION]);return p
def pair(label,expr,key,kp,method,basis=('a','b')):
 p=v(label,expr,key,kp,method+' Checker pairs are the two coefficients in the source vector basis,not scalarising the vectors.');p.update(source_vector_basis={'first':'source vector '+basis[0],'second':'source vector '+basis[1]},assessed_8227_demand_ids=[DISP,GEOM],component_demand_ids=[ADD,SCALE]);return p
def prove(label,answer,method,kp,checks):
 p=reasoning(label,answer,method+' The source gives this textbook result/argument; no official criterion-level award table is claimed.',kp,'show/prove');p.update(response_format='proof/show-that',assessed_8227_demand_ids=[GEOM])
 for name,expr,key in checks:extra(p,name,expr,key)
 return p

ps=[displacement('a',[-1,3,0],[-3,0,7],'Tuple(-2,-3,7)',244),h.norm('b',['-2','-3','7'],'sqrt(62)',244)]
add('Example',7,244,'For D(−1,3,0),E(−3,0,7),find DE in i,j,k form and its exact length sqrt62.',ps,[DISP,NOTATION,MAG])
ps=[displacement('a',[2,-1,4],[-1,6,2],'Tuple(-3,7,-2)',616),h.norm('b',['-3','7','-2'],'sqrt(62)',616)]
add('Try-Now-7',1,245,'A(2,−1,4),B(−1,6,2): write AB=−3i+7j−2k and find its exact length sqrt62.',ps,[DISP,NOTATION,MAG])
ps=[displacement('a',[0,0,2],[-1,3,2],'Tuple(-1,3,0)',616),displacement('b',[0,0,2],[1,0,4],'Tuple(1,0,2)',616),displacement('c',[1,0,4],[-1,3,2],'Tuple(-2,3,-2)',616)]
add('Try-Now-7',2,245,'Triangle A(0,0,2),B(−1,3,2),C(1,0,4): write AB,AC,and specifically CB,not BC.',ps,[DISP,NOTATION])
ps=[]
for label,expr,key in[
 ('a','Tuple(2+1,3+1,-1+1)','Tuple(3,4,0)'),
 ('b','Tuple(2-(-2),3-2,-1-(-1))','Tuple(4,1,0)'),
 ('c','Tuple(2+1+(-2),3+1+2,-1+1+(-1))','Tuple(1,6,-1)'),
 ('d','Tuple(2-3*1+2*(-2),3-3*1+2*2,-1-3*1+2*(-1))','Tuple(-5,4,-6)')]:
 p=v(label,expr,key,616,'Use ORIGINAL a=(2,3,−1),b=(1,1,1),c=(−2,2,−1). Apply the requested signed linear combination component by component; do not lose a zero component in a column representation.');p['assessed_8227_demand_ids']=[ADD,SCALE]if label=='d'else[ADD];ps.append(p)
add('Try-Now-7',3,245,'Compute a+b,a−c,a+b+c,and a−3b+2c for three explicit3Dvectors,retaining signed coefficients.',ps,[ADD,SCALE])
p=h.norm('magnitude',['-5','-2','4'],'3*sqrt(5)',616);p['method']='First derive a−b from ORIGINAL a=(−5,−1,2),b=(0,1,−2),giving(−5,−2,4). Then square all signed components and take the positive square root; the result is3sqrt5.';p['component_demand_ids']=[ADD];extra(p,'original-difference','Tuple(-5-0,-1-1,2-(-2))','Tuple(-5,-2,4)')
add('Try-Now-7',4,245,'Find |a−b| for a=−5i−j+2k and b=j−2k; first form the difference,then its norm3sqrt5.',[p],[MAG])
ps=[pair('a','Tuple(Rational(2,3)*(0-1),Rational(2,3)*(1-0))','Tuple(-Rational(2,3),Rational(2,3))',245,'Original DE=a,DF=b,so EF=b−a. Internal EG:GF=2:1 gives EG=(2/3)EF.'),pair('b','Tuple(1+Rational(2,3)*(0-1),0+Rational(2,3)*(1-0))','Tuple(Rational(1,3),Rational(2,3))',245,'Use DG=DE+EG,with both displacements properly chained. Alternative DF+FG gives the same result because FG=−(1/3)EF.')]
add('Example',8,245,'Triangle DEF with DE=a,DF=b,and G dividing EF in ratioEG:GF2:1: find EG and DG in the source vector basis.',ps,[DISP,ADD,GEOM],rep='diagram')
ps=[pair('a','Tuple((0-1)/6,(1-0)/6)','Tuple(-Rational(1,6),Rational(1,6))',616,'From ORIGINAL AB=b,AC=a,CB=b−a. Diagram ratioCD:DB=1:5 gives CD=(1/6)CB.'),pair('b','Tuple(1+(0-1)/6,0+(1-0)/6)','Tuple(Rational(5,6),Rational(1,6))',616,'Follow AD=AC+CD. The ratio starts from C,not B,so the coefficient5/6belongs to a.')]
add('Try-Now-8',1,245,'AB=b,AC=a,and D divides CB with CD:DB1:5: express CD and AD,using actual endpoint order.',ps,[DISP,ADD,GEOM],rep='diagram')
ps=[pair('a','Tuple((1+0)/2,(0+1)/2)','Tuple(Rational(1,2),Rational(1,2))',616,'B is the midpoint of PQ,with OP=p,OQ=q,so OB=(p+q)/2.',('p','q')),pair('b','Tuple(Rational(2,3),0)','Tuple(Rational(2,3),0)',616,'A divides OP with OA:AP=2:1,so OA=(2/3)p.',('p','q')),pair('c','Tuple(0,Rational(1,4))','Tuple(0,Rational(1,4))',616,'C divides OQ with OC:CQ=1:3,so OC=q/4.',('p','q')),pair('d','Tuple(0-Rational(2,3),Rational(1,4)-0)','Tuple(-Rational(2,3),Rational(1,4))',616,'Use AC=OC−OA with the same selected originO.',('p','q'))]
for p in ps[:3]:p['assessed_8227_demand_ids']=[POS,GEOM]
add('Try-Now-8',2,246,'B midpointPQ,A dividesOP2:1,C dividesOQ1:3,with OP=p,OQ=q: find OB,OA,OC and AC.',ps,[POS,DISP,ADD,GEOM],rep='diagram',new_item=True)
p=prove('a','A,B,C are collinear because AC=2AB with common starting pointA and AB=(1,−1)!=0.','Original positions A(2,3),B(3,2),C(4,1)give AB=(1,−1),AC=(2,−2). Establish both the positive scalar relation and shared point; equal direction alone for unrelated free vectors would not locate all three points on one line.',246,[('AB-AC','Tuple(3-2,2-3,4-2,1-3)','Tuple(1,-1,2,-2)'),('proportional-residual','Tuple((4-2)-2*(3-2),(1-3)-2*(2-3))','Tuple(0,0)')])
p2=reasoning('b','B is the midpoint of AC; AB:BC=1:1.','The ORIGINAL coordinate midpoint of A(2,3)andC(4,1)is(3,2),exactlyB. The already established common-origin relation AC=2AB also proves it.',246,'matches');p2['assessed_8227_demand_ids']=[GEOM];extra(p2,'midpoint','Tuple((2+4)/2,(3+1)/2)','Tuple(3,2)')
add('Example',9,246,'OA=2i+3j,OB=3i+2j,OC=4i+j: show A,B,C collinear and state how B divides AC.',[p,p2],[GEOM],rep='diagram')
ps=[pair('a-OK','Tuple(2,0)','Tuple(2,0)',616,'Original OK=2OA and OA=a,so OK=2a.'),pair('a-OL','Tuple(0,3)','Tuple(0,3)',616,'Original OL=3OB and OB=b,so OL=3b.'),pair('b','Tuple(1-0,0-1)','Tuple(1,-1)',616,'Displacement BA=OA−OB=a−b.'),pair('c','Tuple(2-0,0-3)','Tuple(2,-3)',616,'Displacement LK=OK−OL=2a−3b.'),pair('d','Tuple(0+4*(1-0),1+4*(0-1))','Tuple(4,-3)',616,'Given BC=4BA,follow OC=OB+BC=b+4(a−b).'),pair('e','Tuple(4-0,-3-3)','Tuple(4,-6)',616,'Displacement LC=OC−OL=4a−6b.')]
p=prove('f','L,K,C are collinear because LC=2LK and both start atL.','Use specifically the previously derived LK=(2,−3)andLC=(4,−6)in the source basis. The geometric configuration is nondegenerate,so LK is nonzero. A common point and scalar multiple establish the claimed straight line; the relation also places K midway fromLtoC.',616,[('coefficient-residual','Tuple(4-2*2,-6-2*(-3))','Tuple(0,0)')]);p['source_dependency']={'type':'cue','from':['c','e'],'verbatim':'Use the vectors for LK and LC'};ps.append(p)
for p in ps[:2]:p['assessed_8227_demand_ids']=[POS,SCALE]
ps[4]['assessed_8227_demand_ids']=[POS,GEOM]
add('Try-Now-9',1,247,'OK=2OA,OL=3OB,OA=a,OB=b,and BC=4BA: express six named vectors,then use LK and LC to prove L,K,C collinear.',ps,[POS,DISP,ADD,GEOM],rep='diagram')
ps=[pair('a-AB','Tuple(0-1,1-0)','Tuple(-1,1)',616,'Use AB=OB−OA=b−a.'),pair('a-AT','Tuple(Rational(2,3)*(0-1),Rational(2,3)*(1-0))','Tuple(-Rational(2,3),Rational(2,3))',616,'Original AT=(2/3)AB,so retain the signed coefficients in that direction.'),pair('b-MA','Tuple(1-Rational(1,2),0)','Tuple(Rational(1,2),0)',616,'M is midpointOA,so MA=OA−OM=a/2.'),pair('b-MT','Tuple(1+Rational(2,3)*(0-1)-Rational(1,2),Rational(2,3)*(1-0))','Tuple(-Rational(1,6),Rational(2,3))',616,'OT=OA+AT=a/3+2b/3. Subtract OM=a/2 to obtain MT.'),pair('c','Tuple(0-Rational(1,2),2-0)','Tuple(-Rational(1,2),2)',616,'Y lies on OB produced with OB=BY,so OY=2b. Then MY=OY−OM.')]
p=prove('d','M,T,Y are collinear because MT=(1/3)MY and both start atM.','Compare MT=−a/6+2b/3 with MY=−a/2+2b. Source geometry gives a nonzero direction,so the positive ratio1/3establishes the straight line with T betweenM andY.',616,[('coefficient-residual','Tuple(-Rational(1,6)-Rational(1,3)*(-Rational(1,2)),Rational(2,3)-Rational(1,3)*2)','Tuple(0,0)')]);ps.append(p)
ps[1]['assessed_8227_demand_ids']=[DISP,SCALE]
add('Try-Now-9',2,247,'M midpointOA,T onAB with AT=(2/3)AB,and Y onOB produced with OB=BY: express AB,AT,MA,MT,MY and prove M,T,Y collinear.',ps,[POS,DISP,ADD,GEOM],rep='diagram')
p=prove('proof','OB=3RS,so they are parallel in the same direction and |OB|=3|RS|.','In source basis(a,c),parallelogram OB=a+c. Internal OR:RC=1:2 gives OR=c/3; AS:SC=2:1 gives OS=a+(2/3)(c−a)=a/3+2c/3. Thus RS=OS−OR=(a+c)/3. Nondegenerate parallelogram guarantees nonzero diagonalOB. Positive factor3proves both requested direction and length relation.',616,[('RS-coefficients','Tuple(1+Rational(2,3)*(0-1)-0,Rational(2,3)-Rational(1,3))','Tuple(Rational(1,3),Rational(1,3))'),('three-times-RS','Tuple(3*Rational(1,3),3*Rational(1,3))','Tuple(1,1)')]);p['source_vector_basis']={'first':'source vector a=OA','second':'source vector c=OC'}
p['assessed_8227_demand_ids']=[GEOM,SCALE]
add('Try-Now-9',3,247,'Parallelogram OABC with OA=a,OC=c,R onOC with OR:RC1:2 and S onAC with AS:SC2:1: prove OB parallel and three times as long asRS.',[p],[GEOM,SCALE])

refs=[
 (34,244,'Position vectors from one chosen origin','The grid arrows fromOtoA(3,4),B(−2,3),C(−1,−4),D(4,−3)are position vectors. Their signed components read the same coordinate frame; a free arrow not starting atOis not itself a position vector fromO.',[POS,NOTATION],'graph',None,'teaching-figure'),
 (35,244,'Displacement as difference of positions','The grid/path explanation gives AB=AO+OB=−OA+OB. Source points A(3,4),B(−2,3)give AB=(−5,−1). Preserve head-minus-tail and the shared origin.',[DISP,ADD,POS],'graph',None,'teaching-figure'),
 (36,245,'Example8 given divided triangle','D,E,F form a nondegenerate triangle,DE=a,DF=b,and G lies onEF with EG:GF2:1. The2:1labels refer to segment order fromE,not coordinate distances measured off the page.',[DISP,GEOM],'diagram','Example:8','given-figure'),
 (37,245,'Try8Q1 given internal division','AB=b,AC=a; D is betweenC andB with CD:DB1:5. The short marked segment isCD. Reversing the ratio would change both requested coefficient pairs.',[DISP,GEOM],'diagram','Try-Now-8:1','given-figure'),
 (38,246,'Try8Q2 midpoint and side divisions','In triangleOPQ,B is midpointPQ,OA:AP2:1,OC:CQ1:3. Source basis vectorsp=OP,q=OQshareO. The diagram supplies incidence and ratios,not extra lengths.',[POS,DISP,GEOM],'diagram','Try-Now-8:2','given-figure'),
 (39,246,'Equal displacement with common start reminder','AD=AE implies D=E because both have initial pointA. Equal free vectors at different starting points would not imply equal terminal points.',[GEOM],'table',None,'teaching-figure'),
 (40,246,'Double-length parallel arrows reminder','For nonzero source PQ,the relation XY=2PQ gives the same direction and twice the length,even when the arrows occupy different lines. It does not alone establish collinearity of all four endpoints.',[SCALE,GEOM],'diagram',None,'teaching-figure'),
 (41,246,'Common-start collinearity and midpoint reminder','RS=2RT with commonR and nonzero direction puts R,T,S on one line andT at the midpoint. The nonzero condition gives a unique line; the midpoint equality itself also has a degenerate limiting case.',[GEOM],'diagram',None,'teaching-figure'),
 (42,246,'Example9 given position-arrow sketch','The illustrative rays fromOtoA,B,Ccorrespond to numeric position vectors(2,3),(3,2),(4,1). Exact collinearity and midpoint are established algebraically; the sketch is not a required learner construction.',[POS,GEOM],'diagram','Example:9','given-figure'),
 (43,247,'Try9Q1 common-origin geometry','A/K lie on the same ray fromO,with OK=2OA;B/Lonanother with OL=3OB. Given BC=4BA fixesC. Later collinearity uses LK andLCwith commonL,not a visual alignment alone.',[POS,DISP,GEOM],'diagram','Try-Now-9:1','given-figure'),
 (44,247,'Try9Q2 midpoint/produced-line construction','MmidpointOA,TdividesABat2/3fromA,andYliesonOBproduced with BY=OB. Retain the produced ray direction and sharedMwhen comparingMT/MY.',[POS,DISP,GEOM],'diagram','Try-Now-9:2','given-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C5:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C5:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
 f['mathematical_feature_review']['method']='Inspect original arrowheads,common starting points,endpoint order and internal segment ratios. Recompute source-coordinate displacements or formal vector-basis coefficients; visual alignment alone does not prove collinearity.'
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'Every Example7–9,Try7Q1–4,Try8Q1/2,Try9Q1–3 output and every position/displacement/division/collinearity teaching or given panel is recorded across244–247. No learner sketch is asked. Formal vector-basis coefficient checks retain nondegenerate geometry and common-origin proof conditions.','scope_screen':'Elementary vector displacement,scaling and geometry are prescribed. No formal3Dline equation,skew-line or other excluded method is needed. Numeric and symbolic vector representations remain distinct.'}for page in range(244,248)]

if __name__=='__main__':
 for name,data in [('answers-YM-C5-displacement-geometry.json',{'scope':'Every244–247 explicit requested vector output and proof.','items':answers}),('census-YM-C5-displacement-geometry.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete244–247 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
