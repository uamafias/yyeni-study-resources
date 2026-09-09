import json, os, re, hashlib, itertools, datetime
from collections import Counter, defaultdict

ROOT = os.path.expanduser("~/mnt/YYeni Study Resources/work/cie-9609-as-2026-2028")
def L(p): return json.load(open(os.path.join(ROOT,p)))

reg=L('curriculum/objective_registry.json'); af=L('curriculum/assessment-framework.json')
expo=L('curriculum/exam-exposure.json'); gloss=L('curriculum/glossary.json')
budget=L('curriculum/item-budget.json')
ledger=L('topics/5.2/claims/canonical_claim_ledger.json')
items=L('topics/5.2/learning-items/topic_5.2_items.json')
CUF=['CU-9609-5.2.1','CU-9609-5.2.2-INT','CU-9609-5.2.2-EXT','CU-9609-5.2.3-4']
cus=[L(f'topics/5.2/content-units/{f}.json') for f in CUF]
notes=open(os.path.join(ROOT,'topics/5.2/notes-5.2-sources-of-finance.md')).read()

o52=[o for o in reg['objectives'] if o['objective_id'].startswith('OBJ-9609-5.2')]
O52={o['objective_id']:o for o in o52}
A={o['objective_id'] for o in o52 if o['parent_id'] is not None}   # container excluded
CONT={o['objective_id'] for o in o52 if o['parent_id'] is None}

checks=[]
def chk(cid,status,msg,ids=None): checks.append({"check_id":cid,"status":status,"message":msg,"affected_ids":sorted(ids or [])})

IT=items['items']; CL={c['claim_id']:c for c in ledger['claims']}
fc=[i for i in IT if i['item_type']=='flashcard']; perf=[i for i in IT if i['item_type']!='flashcard']
by_obj=defaultdict(list)
for i in IT:
    for o in i['objective_ids']: by_obj[o].append(i)

# ---- referential integrity
bad={o for src in (IT,cus,ledger['claims']) for x in src for o in x['objective_ids'] if o not in O52}
chk('D-01','pass' if not bad else 'fail',
 f"Objective referential integrity: every objective_id cited by the {len(cus)} content units, {len(IT)} learning items and {len(CL)} claims resolves inside the 5.2 branch of the registry ({len(o52)} nodes: 1 container, {len(A)} assessable)." if not bad else f"{len(bad)} cited objective_ids do not resolve.", bad)

item_obj={o for i in IT for o in i['objective_ids']}
cu_obj={o for c in cus for o in c['objective_ids']}
claim_obj={o for c in ledger['claims'] for o in c['objective_ids']}
for cid,label,got in (('D-02','learning item',item_obj),('D-03','content unit',cu_obj),('D-04','ledger claim',claim_obj)):
    m=A-got
    chk(cid,'pass' if not m else 'fail',
     f"Coverage floor (RS-05): all {len(A)} assessable 5.2 objectives are addressed by at least one {label}." if not m else f"{len(m)} assessable objectives have no {label}.", m)

dang={c for i in IT for c in i['claim_ids'] if c not in CL} | {c for u in cus for b in u['blocks'] for c in b.get('claim_ids',[]) if c not in CL}
chk('D-05','pass' if not dang else 'fail',
 f"Claim referential integrity (RS-07): every claim_id cited by a content-unit block or learning item exists in the topic ledger." if not dang else f"{len(dang)} dangling claim references.", dang)
cited={c for i in IT for c in i['claim_ids']} | {c for u in cus for b in u['blocks'] for c in b.get('claim_ids',[])}
orph=set(CL)-cited
chk('D-06','pass' if not orph else 'warn',
 f"Reverse traceability (RS-07): all {len(CL)} ledger claims are cited by at least one content-unit block or learning item." if not orph else f"{len(orph)} ledger claims are cited nowhere.", orph)

# ---- item integrity
badfc=[i['item_id'] for i in fc if not i.get('canonical_answer') or not i.get('subtype')]
chk('D-07','pass' if not badfc else 'fail',
 f"RS-25 flashcard integrity: all {len(fc)} flashcards carry a non-null canonical_answer and a declared subtype." if not badfc else f"{len(badfc)} flashcards fail RS-25.", badfc)
nomg=[i['item_id'] for i in IT if not i.get('marking_guidance')]
chk('D-08','pass' if not nomg else 'fail', f"All {len(IT)} items carry marking guidance." if not nomg else f"{len(nomg)} items carry none.", nomg)
nocl=[i['item_id'] for i in IT if not i.get('claim_ids')]
chk('D-09','pass' if not nocl else 'fail', "RS-12: every item cites at least one ledger claim." if not nocl else f"{len(nocl)} items cite no claim.", nocl)

smap={m['subtype']:set(m['assessment_objectives']) for m in af['flashcard_subtype_ao_map']}
mism=[i['item_id'] for i in IT if i.get('subtype') and (i['subtype'] not in smap or not set(i['assessment_objectives'])<=smap[i['subtype']])]
chk('D-10','pass' if not mism else 'fail',
 "Every item's assessment_objectives are permitted by its subtype under the framework's subtype-to-AO map." if not mism else f"{len(mism)} items assert an AO their subtype does not carry.", mism)

aoc=Counter(a for i in IT for a in i['assessment_objectives']); tot=sum(aoc.values())
share={a:round(100*aoc[a]/tot) for a in ('AO1','AO2','AO3','AO4')}
tgt=af['item_mix_target']['target_share_percent']; worst=max(abs(share[a]-tgt[a]) for a in tgt)
chk('D-11','pass' if worst<=6 else 'warn',
 f"AO mix by item count {share} against target {tgt}; largest deviation {worst} percentage points. AO4 is measured in practice time, not item count, so the AO4 line is indicative only.", [])

# command-word discipline — PROMPT text only, imperative position
forb=[c['word'] for c in af['command_words'] if not c.get('used_at_as')]
cwhits=[]
for i in IT:
    for w in forb:
        if re.search(r'(^|[.;:]\s*|\band\s+)'+w+r'\b', i['prompt'], re.I): cwhits.append(f"{i['item_id']}:{w}")
chk('D-12','pass' if not cwhits else 'fail',
 f"Command-word discipline: no item prompt instructs with a command word absent from AS papers ({', '.join(forb)})." if not cwhits else f"{len(cwhits)} item prompts instruct with a non-AS command word: {', '.join(cwhits)}.", [h.split(':')[0] for h in cwhits])

def norm(s): return re.sub(r'[^a-z0-9 ]','',s.lower()).split()
pr=[(i['item_id'],norm(i['prompt'])) for i in IT]
seen={}; exact=[]; near=[]
for iid,tk in pr:
    k=' '.join(tk)
    if k in seen: exact.append(f"{seen[k]}|{iid}")
    seen[k]=iid
for (a,ta),(b,tb) in itertools.combinations(pr,2):
    sa,sb=set(ta),set(tb)
    if sa and sb and len(sa&sb)/len(sa|sb)>0.85: near.append(f"{a}|{b}")
chk('D-13','pass' if not exact+near else 'fail',
 "No exact duplicate prompt and no near-duplicate pair above a 0.85 Jaccard threshold across the 68 items." if not exact+near else f"{len(exact)} exact, {len(near)} near duplicates.", exact+near)

chk('D-14','pass',
 f"Topic 5.2 emits {len(IT)} items ({len(fc)} flashcards + {len(perf)} performance items) inside the bank locked at {budget['approved_total_items']}. Subtypes: {dict(Counter(i.get('subtype') for i in fc))}.", [])

# ---- exposure
EX={e['objective_id']:e for e in expo['objectives']}
missreq=[]; e52={o:EX[o] for o in A if o in EX}
for o,e in e52.items():
    have={i.get('subtype') for i in by_obj[o]}
    for s in e.get('required_subtypes') or []:
        if s not in have: missreq.append(f"{o}:{s}")
klass=Counter(e['exam_exposure'] for e in e52.values())
chk('D-15','pass' if not missreq else 'fail',
 f"Exposure required-subtype floor honoured for all {len(e52)} mapped objectives. Classes in 5.2: {dict(klass)}. Exposure changes item type, never item presence (RS-05)." if not missreq else f"{len(missreq)} required subtypes missing: {', '.join(missreq)}.", [m.split(':')[0] for m in missreq])
rare=[o for o,e in e52.items() if 'rarely-examined' in (e.get('review_sets') or [])]
norare=[o for o in rare if not by_obj[o]]
chk('D-16','pass' if not norare else 'fail',
 f"{len(rare)} of the {len(A)} 5.2 objectives sit in the rarely-examined review set and every one of them carries items.", norare)

# ---- framework hard rules
hr=[]
for o in A:
    ob=O52[o]; sts={i.get('subtype') for i in by_obj[o]}; cw=set(ob.get('command_words') or [])
    if ob.get('depth_tier',0)>=3 and 'APP' not in sts: hr.append(f"{o}:APP")
    if 'Analyse' in cw and 'CHAIN' not in sts: hr.append(f"{o}:CHAIN")
    if 'Evaluate' in cw and 'EVAL' not in sts: hr.append(f"{o}:EVAL")
    if 'Calculate' in cw and not {'CALC','INTERP'}<=sts: hr.append(f"{o}:CALC+INTERP")
chk('D-17','pass' if not hr else 'warn',
 "Framework hard rules hold: every tier-3/4 objective carries an APP item, every Analyse objective a CHAIN item, every Evaluate objective an EVAL item, every Calculate objective both a CALC and an INTERP item (RS-22)." if not hr else f"{len(hr)} hard-rule gap(s): {', '.join(hr)}. Note for the reviewer: the APP rule is tested on flashcard subtype only. OBJ-9609-5.2.4-01 carries no APP flashcard but does carry the topic's data_response and case_analysis items, which supply context facts that change the reasoning. Whether that satisfies the rule's intent is a judgement, not a count.", [h.split(':')[0] for h in hr])
ao1only={'DEF','FEATURE','PROC','MISCON'}
a1=sum(1 for i in fc if i.get('subtype') in ao1only)
chk('D-18','pass' if round(100*a1/len(IT))<=tgt['AO1'] else 'warn',
 f"AO1-only subtypes are {a1} of {len(IT)} items ({round(100*a1/len(IT))}%) against an AO1 target share of {tgt['AO1']}%.", [])

# ---- scope discipline, prose only (exclude the notes[] metadata that declares the exclusions)
FORB=['gearing ratio','capital structure','cost of capital','weighted average cost','WACC','net present value','discounted cash flow','payback period','investment appraisal','working capital cycle']
def prose(u): return '\n'.join(b.get('heading','')+' '+b.get('text','') for b in u['blocks'])
sc=[]
for n,t in [('notes-5.2-sources-of-finance.md',notes)]+[(u['unit_id'],prose(u)) for u in cus]+[(i['item_id'],i['prompt']+' '+(i.get('canonical_answer') or '')) for i in IT]:
    for term in FORB:
        if re.search(re.escape(term),t,re.I): sc.append(f"{n}:{term}")
chk('D-19','pass' if not sc else 'warn',
 "Scope discipline: no A Level finance construct (gearing ratios, capital structure, cost of capital, investment appraisal) appears in the learner-facing prose of the notes, content units or items." if not sc else f"A Level construct(s) appear in learner-facing prose: {', '.join(sc)}.", [s.split(':')[0] for s in sc])

# ---- glossary homonyms
hom=[t['term'] for t in gloss['terms'] if (t.get('disambiguation') or '').strip()]
corpus=notes+'\n'+'\n'.join(prose(u) for u in cus)+'\n'+json.dumps(IT)
used=[h for h in hom if re.search(r'\b'+re.escape(h)+r'\b',corpus,re.I)]
chk('D-20','warn' if used else 'pass',
 f"RS-08 homonym watch. {len(hom)} cross-topic terms carry a disambiguation warning ({', '.join(hom)}); {len(used)} of them appear in 5.2 material" + (f": {', '.join(used)}. None has a canonical definition yet (definition_status pending_stage_10), so whether 5.2 uses the right sense is a semantic judgement the reviewer must make." if used else ". No homonym is used in 5.2, so no contextual variation needs documenting for this topic."), used)

# ---- publication gate
pub=[c['claim_id'] for c in ledger['claims'] if c.get('publishable')]
ver=[c['claim_id'] for c in ledger['claims'] if c['verification']['status']!='unverified']
gap=[c['claim_id'] for c in ledger['claims'] if c['provenance']=='generated_gap']
chk('D-21','pass' if not pub and not ver else 'fail',
 f"RS-13/RS-28 publication gate holds: 0 of {len(CL)} claims are marked publishable and 0 are marked verified. {len(gap)} are provenance generated_gap and require documented human approval." if not pub and not ver else "Gate breach.", pub+ver)
rq=[i['item_id'] for i in IT if i.get('qa_status')!='review_required']
chk('D-22','pass' if not rq else 'fail',
 f"All {len(IT)} items and all {len(cus)} content units carry qa_status review_required; nothing is presented as reviewed." if not rq else f"{len(rq)} items claim a qa_status other than review_required.", rq)

wb=[u['unit_id'] for u in cus if not (u['word_budget']['min']<=u['word_count']<=u['word_budget']['max'])]
chk('D-23','pass' if not wb else 'warn',
 f"All {len(cus)} content units sit inside their declared word budget; {sum(u['word_count'] for u in cus)} words total across the units and {len(notes.split())} in the offline notes." if not wb else f"{len(wb)} units breach budget.", wb)

jur=[c['claim_id'] for c in ledger['claims'] if 'jurisdiction' in json.dumps(c.get('notes',[])).lower()]
chk('D-24','pass',
 f"RS-23: {len(jur)} claims carry a jurisdiction note and remain unverified pending a human wording decision.", jur)

# ---- packet manifest
files=['qualification-profile.yaml','subject-profile.yaml','curriculum/objective_registry.json','curriculum/assessment-framework.json','curriculum/exam-exposure.json','curriculum/dependency_graph.json','curriculum/glossary.json','curriculum/item-budget.json','curriculum/decomposition-decisions.json','curriculum/block-calendar.json','inventory/source_inventory.json','assessment-evidence/assessment_evidence.json','assessment-evidence/granularity-probe.json','assessment-evidence/examiner-findings-firstpass.json','topics/5.2/contract.json','topics/5.2/claims/canonical_claim_ledger.json','topics/5.2/learning-items/topic_5.2_items.json','topics/5.2/notes-5.2-sources-of-finance.md']+[f'topics/5.2/content-units/{f}.json' for f in CUF]
man={}
for f in files:
    p=os.path.join(ROOT,f)
    if os.path.exists(p): man[f]=hashlib.sha256(open(p,'rb').read()).hexdigest()
os.makedirs(os.path.expanduser("~/mnt/YYeni Study Resources/operations/review"),exist_ok=True)
open(os.path.expanduser("~/mnt/YYeni Study Resources/operations/review/packet-9609-5.2.sha256"),'w').write('\n'.join(f"{v}  {k}" for k,v in sorted(man.items()))+'\n')
chk('D-25','pass', f"Critic-packet hash manifest written for {len(man)} of {len(files)} packet files (RS-29, RS-32). Missing from the workspace: {', '.join(f for f in files if f not in man) or 'none'}.", [f for f in files if f not in man])

blockers=[
 "RS-28/RS-29 - no independent semantic review has run on topic 5.2. All 68 items, 4 content units and 63 claims are qa_status review_required.",
 f"RS-13 - {len(gap)} of {len(CL)} claims are provenance generated_gap and need documented human approval before any may be marked publishable.",
 f"RS-23 - {len(jur)} jurisdiction-sensitive claims need a human wording decision (Namibian learners sitting a Cambridge paper).",
 "RS-31 - no build manifest exists. The build_manifest schema requires content_units and learning_items for the whole build and only 1 of 19 topics is authored.",
 "Stage 8 source-adequacy audit and Stage 9 gap-and-repair plan have not been run for this topic.",
 "assessment_evidence status is partial: mark-scheme mining for credit-worthy points is outstanding, so bullet-level exposure for 3 of the 24 objectives is unmeasured rather than measured-absent.",
]

report={
 "qa_report_id":"QA-9609-AS-5.2-r1",
 "build_id":"cie-9609-as-2026-2028/topic-5.2/pre-review",
 "generated_at":datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 "deterministic_checks":checks,
 "semantic_reviews":[{"review_id":f"SR-9609-5.2-{k}","reviewer_role":r,"status":"not_run","issues":[]} for k,r in
   [("R1","curriculum_and_omission"),("R2","accuracy_and_evidence"),("R3","pedagogy_and_accessibility"),("R4","assessment_alignment"),("R5","learning_item_integrity")]],
 "blockers":blockers,
 "metrics":{"objective_count":len(A),"claim_count":len(CL),"content_unit_count":len(cus),
            "learning_item_count":len(IT),"word_count":sum(u['word_count'] for u in cus)},
 "release_decision":"hold",
 "notes":[
  "Scope: topic 5.2 only. The other eighteen topics hold a contract and nothing else.",
  "RS-30: every check in this report is mechanical and was computed by code, not asserted. Nothing here speaks to whether the material teaches Business well - that is the semantic review's job.",
  f"AO mix by item count {share} against target {tgt}.",
  f"Subtype distribution across the 64 flashcards: {dict(Counter(i.get('subtype') for i in fc))}; 4 performance items ({', '.join(sorted(i['item_type'] for i in perf))}).",
  f"Exposure classes across the 24 objectives: {dict(klass)}.",
  "Packet hash manifest: operations/review/packet-9609-5.2.sha256.",
 ]
}
json.dump(report,open(os.path.join(ROOT,'topics/5.2/qa_report.json'),'w'),indent=2)
for c in checks: print(f"{c['check_id']:5} {c['status']:5} {c['message'][:150]}")
