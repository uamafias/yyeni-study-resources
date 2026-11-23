"""All four C6reference blocks and outcome-only chapter boundary,PDF175."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,compute,expression,equivalent
from author_Goldie_C5_opening import fig,figures
figures.clear()
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';RELATE='8227:2020:M2:T6:O03:D01';ITERATE='8227:2020:M2:T6:O04:D01';FAIL='8227:2020:M2:T6:O02:D02'
p=W/'checks/r5/textbooks/Goldie-C6-174.png';evidence={'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for n,label,note,teaches,checks in [
 (20,'Key points1 sign-change existence','A continuous function with opposite signs at finite interval endpoints has at least one root inside. Neither continuity nor the wordsatleastonemay be dropped;the result does not certify uniqueness.',[BRACKET],[]),
 (21,'Key points2 interval reduction','A valid root-containing interval may be narrowed systematically by decimal search or bisection. These are supporting algorithms;the syllabus’s locating-by-sign-change demand does not make both specific implementations mandatory.',[BRACKET],[]),
 (22,'Key points3 fixed-point procedure','Rearrangingf(x)=0asx=F(x)provides an iterationxₙ₊₁=F(xₙ). Check equivalence domains and understand that not every rearrangement/start converges to the intended root.',[RELATE,ITERATE],[]),
 (23,'Key points4 qualitative convergence wording caution','The summary says failure may occur when the gradient isnotverysteep,contrasting with the preceding explanatory text’snottoosteepconvergence advice. Treat this as a misleading qualitative wording conflict,not a formal if-and-only-if theorem. Required8227knowledge is that iteration may fail;formal derivative conditions are excluded.',[FAIL],
  [('Tuple((x/2).subs(x,1),(2*x).subs(x,1),(-2*x).subs(x,1))','Tuple(1/2,2,-2)')])]:
 fig(n,175,label,note,teaches,'table',checks)
for row in figures:
 row['item_id']=row['item_id'].replace(':C5:',':C6:');row['source_evidence']=evidence
 if row['item_number']=='23':row['source_wording_caution']='Do not turn the qualitative wording into a guaranteed convergence/failure condition. Compare the contraction/expansion examples and retain formal-theorem exclusion.'
pages=[{'pdf_page':175,'printed_page':161,'chapter':6,'page_status':'items enumerated','item_ids':[r['item_id']for r in figures],'continuation_item_ids':[],
 'source_evidence':evidence,'reader':'Codex author','date':'2026-11-18','non_item_content':'All four key-point reference blocks enumerated. Learning outcomes are a checklist,not another task;chapter7begins176and was separately scope-screened.'}]
if __name__=='__main__':
 (W/'tools/textbook-r5/census-Goldie-C6-closing.json').write_text(json.dumps({'book':'Goldie','book_id':'8227-SRC-015','chapter':6,'source_path':SRC,'source_sha256':SHA,
  'scope':'Complete175reference blocks and outcomes boundary.','new_items':figures,'corrections':[],'pages':pages},ensure_ascii=False,indent=2)+'\n')
 print('Four reference blocks;convergence-wording conflict explicit;chapter boundary read')
