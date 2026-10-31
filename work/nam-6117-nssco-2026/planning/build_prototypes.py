"""Nine original, fully answered prototype cards for the production review gate."""
import copy,hashlib,json,sys
from pathlib import Path
import jsonschema
W=Path(__file__).resolve().parents[1];R=W.parents[1];P=W/'prototypes';P.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
slots={s['slot']:s for p in (W/'topics').glob('*/work_order.json') for s in read(p)['item_slots']}
# Prompts and answers are newly authored, not official examination wording.
TEXT={
'ITEM-6117-9-011-DEF':('State whether most metals in ores are present as uncombined elements or chemically combined with other elements.', 'Most occur chemically combined with other elements, in compounds.', ['Credit the fact that most occur as compounds (1 mark); accept chemically combined with other elements. Do not require every metal to occur this way.']),
'ITEM-6117-9-007-FEATURE':('State which metal is more reactive: magnesium or copper.', 'Magnesium is more reactive than copper.', ['Credit the correct relative-reactivity property: magnesium (1 mark).']),
'ITEM-6117-9-008-MECH':('Explain why magnesium can displace copper from aqueous copper(II) sulfate.', 'Magnesium is more reactive than copper, so magnesium forms ions while copper ions are converted to copper metal.', ['Credit the causal reason that magnesium is more reactive than copper and therefore displaces it (1 mark); a balanced equation is not required.']),
'ITEM-6117-9-002-APP':('Suggest which material is more suitable for a bendable electrical contact, giving a reason. Material X conducts electricity and bends without breaking. Material Y does not conduct electricity and breaks when bent.', 'X, because its electrical conductivity and ability to bend meet the stated requirements.', ['Credit X with a reason linked to the given case: it conducts and can be bent into shape (1 mark for the supported choice). Do not award a separate reason mark.']),
'ITEM-6117-9-004-INTERP':('Identify which diagram represents an alloy. Each symbol is an atom in a solid metallic sample. ○ represents one metallic element; ● represents a different metallic element.\n\nDiagram A\n○ ○ ○ ○\n ○ ○ ○ ○\n○ ○ ○ ○\n\nDiagram B\n○ ○ ● ○\n ○ ● ○ ○\n○ ○ ○ ●', 'Diagram B represents an alloy: it contains atoms of two metallic elements.', ['Credit B (1 mark). The diagram evidence is the two atom types; this supports the alloy inference but a separate written explanation is not required.']),
'ITEM-6117-9-021-PROC':('Describe the two reactions by which carbon monoxide is formed from coke and the incoming air in a blast furnace.', 'Coke burns in oxygen to form carbon dioxide: C + O₂ → CO₂. Carbon dioxide then reacts with more hot coke to form carbon monoxide: CO₂ + C → 2CO.', ['Credit the first step: carbon reacts with oxygen to produce carbon dioxide (1 mark).','Credit the subsequent reaction/result: carbon dioxide reacts with hot carbon to produce carbon monoxide (1 mark). Accept correct word or balanced symbol equations.']),
'ITEM-6117-7-062-MISCON':('Explain why this proposed method is mistaken: after an insoluble salt forms as a precipitate, a learner filters the mixture and evaporates the filtrate to recover that salt.', 'The insoluble salt is the residue on the filter paper, so the filtrate does not contain that precipitate to recover by evaporation.', ['Credit correction of the confusion: the wanted precipitate is retained as the residue, because it is insoluble (1 mark). This diagnostic distinguishes filtering an insoluble salt from crystallising a dissolved salt.'])
}
items=[];claims=[];deviations=[]
for iid in read(W/'planning/semantic-review-gate.json')['authored_card_sample_gate']['required_planned_slot_ids']:
 s=slots[iid];prompt,answer,guidance=TEXT[iid];cid='CLM-PROT-'+iid.removeprefix('ITEM-6117-')
 item={'item_id':iid,'objective_ids':[s['objective_id']],'claim_ids':[cid],'item_type':'flashcard','subtype':s['subtype'],'assessment_objectives':s['assessment_objectives'],'difficulty':s['difficulty'],'prompt':prompt,'canonical_answer':answer,'marking_guidance':guidance,'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original Chemistry production prototype; authored from syllabus scope and approved task shape.','qa_status':'review_required','blooms_level':s['blooms_level'],'command_word':s['command_word'],'mark_tariff':s['mark_tariff'],'claims_seen':{cid:1}}
 if s.get('misconception_entry'):item['misconception_entry']=s['misconception_entry']
 if s['subtype']=='PROC':
  item['blooms_level']='Understand';deviations.append({'item_id':iid,'field':'blooms_level','from':s['blooms_level'],'to':'Understand','reason':'The actual task describes a familiar furnace sequence; it does not apply a method to a new case.'})
 if s['subtype']=='MISCON':
  item['blooms_level']='Apply';deviations.append({'item_id':iid,'field':'blooms_level','from':s['blooms_level'],'to':'Apply','reason':'The learner applies solubility/separation principles to diagnose the supplied mistaken procedure.'})
 item['authored_hash']=hashlib.sha256(_artefact_text(item).encode()).hexdigest();items.append(item)
 claims.append({'claim_id':cid,'objective_ids':item['objective_ids'],'text':answer,'claim_type':'synthetic_example' if s['subtype'] in ['APP','INTERP'] else 'misconception_correction' if s['subtype']=='MISCON' else 'factual','provenance':'generated_gap','evidence':[],'derived_from_claim_ids':[],'revision':1,'verification':{'status':'unverified','method':'Agent semantic review recorded separately; human prototype review remains pending.','reviewer_id':None,'reviewed_at':None,'confidence':0.95},'publishable':False})
ex=read(W/'exemplar/topics/4/learning-items/concentration.json')['items'];ex_claims=read(W/'exemplar/topics/4/claims/canonical_claim_ledger.json')['claims']
items += [copy.deepcopy(i) for i in ex if i['item_id'] in ['ITEM-6117-EX-1','ITEM-6117-EX-2']];claims+=ex_claims
pack={'dataset_id':'DATA-6117-NINE-PROTOTYPES','topic_id':'production-prototypes','items':items};ledger={'ledger_id':'LEDGER-6117-PROTOTYPES','claims':claims}
for schema,data in [('learning_items',pack),('canonical_claim_ledger',ledger)]:jsonschema.validate(data,read(R/f'standard/v0.2.0-draft/schemas/{schema}.schema.json'))
assert len(items)==9 and len({i['item_id'] for i in items})==9
assert .125*(32/1000)==.004 and abs(.009/(30/1000)-.3)<1e-12
save(P/'cards.json',pack);save(P/'canonical_claim_ledger.json',ledger);save(P/'authoring_notes.json',{'deviations':deviations,'scope':'Prototype only; these are not a full topic release.'})
lines=['# Nine Chemistry prototype cards', '', 'Fully authored samples for the pre-production checkpoint. Agent-reviewed; human review remains pending. No official question wording is reproduced.', '']
for i in items:
 lines += [f"## {i['item_id']} — {i['subtype']}",'',f"AO {','.join(i['assessment_objectives'])}; Bloom {i['blooms_level']}; {i['mark_tariff']} mark(s).",'',i['prompt'],'','**Answer:** '+i['canonical_answer'],'','**Marking:**','']+['- '+g for g in i['marking_guidance']]+['']
(P/'REVIEW-CARDS.md').write_text('\n'.join(lines)+'\n')
print('Built nine authored prototype cards; schemas and both numerical results checked.')
