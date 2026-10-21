"""Save local repair evidence and status. No model, network or release calls."""
from pathlib import Path
import ast
import hashlib
import json
import jsonschema

WS=Path(__file__).resolve().parents[2]; REPO=WS.parents[1]; OUT=Path(__file__).parent
def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')

audit=read(WS/'authoring-progress.json')
assert len(audit['topics'])==18 and all(not t['failures'] and t['what_to_fix_exit_code']==0 for t in audit['topics'])
registry=read(WS/'curriculum/objective_registry.json')
jsonschema.validate(registry,read(REPO/'standard/v0.2.0-draft/schemas/objective_registry.schema.json'))
for td in (WS/'topics').iterdir():
    if not (td/'work_order.json').exists():continue
    wo=read(td/'work_order.json');items=read(next((td/'learning-items').glob('*.json')))['items']
    assert len(items)==len(wo['item_slots'])+len(wo['performance_tasks'])
    for i in items:
        assert not any(s in i['prompt'].lower() for s in ['two relevant aspects','one reason or limitation relevant to','relevant to choose methods'])
        if td.name=='10.1' and i['item_type']!='flashcard':
            bs=[s for s in i['canonical_answer'].splitlines() if s.startswith('B(')]
            assert bs and all('Own-enquiry scaffold:' in s for s in bs)
            assert all('Fictional model:' not in s for s in bs)
tree=ast.parse((OUT/'repair_resources.py').read_text())
datasets={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['REWRITES','EVALUATIONS']}
rewrites=sum(len(v) for v in datasets['REWRITES'].values());evals=len(datasets['EVALUATIONS'])
assert rewrites==72
counts=audit['totals'];word=f"{counts['rendered_words']:,}"
rows=[
('001','Vision 2030 definition and 2004–2030 horizon; assessed description','2.1 unit 01 and 001'),
('002','HPP year, president, pillars and purpose; NDP5 goal-based evaluation','2.2 unit 02 and 003/004/P01'),
('003','Syllabus term restored; definition, GBV types, factors, effects and responses','6.2 units 05–06, revision history and rewritten cards'),
('004','Distinct teaching sets for breadth gaps, including trade, aid and decentralisation','1.1/1.2, 3.1, 4.1, 5.1, 6.2, 7.1–7.3, 8.1, 9.1–9.3, 10.1'),
('005','Worked percentage change, percentage points, natural increase and per-thousand conversion','7.2 unit 01; 7.1 unit 03'),
('006','All 72 flagged templates individually rewritten with responsive answers','REWRITES in repair_resources.py; IDs in content-actions.json'),
('007','Three work categories reconciled; employed and unmet-need totals distinguished','4.2-022 and notes example'),
('008',f'{evals} evaluations rewritten with real merits/costs and developed conditional answers','EVALUATIONS in repair_resources.py; 7.3-006 describes both routes before judging'),
('009','Named Namibian/regional examples and historical mechanisms added; original industry names retained','4.1, 5.1, 6.1, 6.2 and 9.3'),
('010','Disease-route distinctions, immunisation purpose and delivery conditions taught','7.2 unit 01; no clinical schedule'),
('011','All four Section B answer sets become own-enquiry scaffolds; personal-record template added','10.1 P01–P04 and unit 12; old fictional answers retained only as audit history'),
('012','Sampling quantities supplied inline and exact package IDs given','10.1 units 10–11'),
('013','P02 whole defined as production cost and inference limit clarified; P03 journeys linked to schools','10.1-P02 A2(3–4) and P03 stimulus'),
('014','Area examples use average income; unsafe-water wording corrected','1.1 unit 04 and 017/P02'),
('015','Repeated unit-end filler removed; woodland, irrigation and regional cases varied','5.1-034/038, revised 4.1/9.3 cases and cross-link removal log'),
('016','Three misconception cards require applied separating tests','9.1-031; 9.2-017/018'),
('017','Existing dated official-source locators attached to relevant claim ledgers','Source blocks and ledger evidence; still unverified')]
report='''# Codex repairs after Claude’s whole-subject review

Jeremy authorised repairs after Claude’s **FIX CONTENT BEFORE PUBLICATION** verdict. Codex applied them across the completed subject. No further Claude call, web research, publication, commit, push or platform import was made.

The original [Claude report](../CLAUDE-RESOURCE-REVIEW.md) remains unchanged. These dispositions are **Codex repair judgements**, not new independent approval. Claims remain unverified/non-publishable; resources remain review_required.

## Content findings

| Finding | Repair applied | Where |
|---|---|---|
'''
for number,action,where in rows:report+=f'| R6136-{number} | {action} | {where} |\n'
report+='''
## Plan repairs

PL-1–PL-5 are addressed in `curriculum/post-resource-review-amendments.json` and the plan/handover. Eighty-two generic member titles were made specific, with two additional same-word targets kept distinct for their different contexts. Work-order displays were regenerated with the standard Markdown function. EVAL requirements now demand genuine trade-offs while retaining multi-point knowledge teaching. CALC requirements include prerequisite methods. Named examined examples remain required.

The compound command on 7.3-006 retains its metadata, describes both alternatives, then requires reasoned judgement. Its C14 incompatibility remains an owner issue. No silent metadata change was made.

All 356 targets, 543 slots, IDs, subtypes, AOs, Bloom labels, command metadata, tariffs and unit ceilings remain. Research P02 is correctly A1=20/A2=15; the others are A1=25/A2=10. Every package has A=35 and B=15. The review brief’s universal 25/10 assumption was wrong; P02’s authored total was correct.

## Learner tests repeated by Codex

**GBV/baby dumping (6.2.05–06):** the notes now supply the definition with lack of appropriate care and risk of harm, two or more GBV types, distinct contributing factors, personal/development effects and matched responses. The prior term-recognition and knowledge gaps are addressed. Cards 020/021/024/025 ask specific questions. This is a teaching-coverage judgement, not a promised examination score.

**Rural schemes (5.1.04):** the notes give at least six distinct cooperative benefits, named regional schemes and separate implementation barriers. Namibian land reform/resettlement and conservancies provide local context. Revised 024–030 evaluations give both options merits and costs. The production-versus-marketing distinction remains explicit.

**Calculation prerequisites:** 7.1 teaches birth-minus-death rates and 20 per thousand = 2%; 7.2 teaches change divided by the original value, works 80→100 and 100→80 separately, and distinguishes percentage points. Learners now have the methods required by 7.1-011 and 7.2-003/014.

## Verification

'''
report+=f'''- All **18/18** check reports say `publish`, with **zero deterministic failures** and `what_to_fix` exit 0. This is a tool result, not learner-release approval.
- **{counts['claims']} claims, {counts['units']} units, {counts['flashcards']} flashcards and {counts['activities']} activities; {word} rendered-note words.** No upper ceiling exceeded.
- Exact slot/metadata audit: no missing, extra or mismatched items. Registry schema validates. The pre-existing subject-profile schema incompatibility remains open.
- **16 checks parse actual authored research inputs, answers and question tariffs**, including age-sex totals. Fixed-literal checks were removed. Three corrupted in-memory cases (output, pie angle, tariff) were correctly rejected; files were not mutated.
- Copied wording against 40 saved paper/report extracts: **zero 8+ and zero 12+ matches**; syllabus excluded. Exact matching does not prove semantic originality.
- Changed claim text has revision/history records, updated claims_seen and unchanged-text reviews where applicable. Previous artefact hashes are retained. Standard restamping and rendering completed.

'''
report+='''## Standard/tool findings

| Finding | Disposition |
|---|---|
| T-1 | Open with standard owner. C35/C41/C43 are not_run. The stock no-graph explanation is incorrect for 7.1 and 10.1. Specifications are checked; no rendered-figure PASS claimed. |
| T-2 | Fixed locally: audit_research.py parses actual stimuli, answers and tariffs; audit_build.py consumes it. See authored-numerical-audit.json and numerical-audit-negative-checks.json. |
| T-3 | Open with standard owner: runner exit/JSON mismatch and stale subject-profile schema. standard/ is unchanged. |
| T-4 | AO allocations remain explicit planning judgements. The documented D relative shortfall remains; metadata cannot establish real demand. |
| T-5 | Claude found no causal error. The pronatalist comparison was nevertheless strengthened with two real support alternatives and fuller reasoning. |
| T-6 | Advisory minima remain advisory. Missing substance was added; word counts were not padded. |
| T-7 | Exact copied-wording tool limits remain visible; the rerun is not semantic-originality certification. |

## Reproduction and next state

The original author_topic.py files are pre-review manuscripts. Do not run them alone as current build sources. Run `review/repairs/repair_resources.py` to replay explicit repairs from the preserved pre-repair JSON baseline, then `planning/repair_review_demands.py`, standard restamping/rendering, `topics/audit_build.py` and the copied-wording scan. Repair scripts make no model or network calls.

Repairs have not been independently re-reviewed. Another Claude review is not authorised. Standard-owner fixes, publication, commit/push, pilot completion and YYeni replacement/import remain pending.
'''
(OUT/'REPAIR-REPORT.md').write_text(report)
validation=dict(result='PASS for local repair checks; not independent approval',totals=counts,
    topic_failures={t['topic_id']:len(t['failures']) for t in audit['topics']},registry_schema='PASS',
    numeric_checks=16,template_rewrites=rewrites,evaluation_rewrites=evals,claude_contacted_for_repairs=False,
    web_research_during_repairs=False,release_approved=False)
dump(OUT/'repair-validation.json',validation)
p=WS/'STATUS.md';s=p.read_text();anchor='## Current checkpoint\n'
if '**Codex repairs complete' not in s:
    s=s.replace(anchor,anchor+'\n**Codex repairs complete — R6136-001–017 and PL-1–PL-5 addressed locally (2026-10-20).** All 18 topics rerendered and checked with zero deterministic failures; 543 slots retained. See `review/repairs/REPAIR-REPORT.md`. Claude’s original verdict remains the independent record; no follow-up review or learner release is claimed. Standard-owner limitations remain open.\n',1)
s=s.replace('- [ ] 6 Claude Code independently reviews Codex-authored resources; fixes or routes findings back.','- [x] 6 Initial Claude whole-subject review returned; findings repaired by Codex at Jeremy’s instruction. Follow-up review is not authorised.')
start=s.index('## Next session\n');end=s.index('\n## ',start+len('## Next session\n'))
s=s[:start]+'''## Next session

Read `review/repairs/REPAIR-REPORT.md` and the preserved Claude report. Content repairs and local checks are complete. The repair manuscript supersedes the pre-review drafts; do not execute old author_topic.py files alone. Do not send another Claude review without Jeremy’s explicit approval. Standard-owner issues, publication and human commit/push/import steps remain pending.
'''+s[end:]
s=s.replace('The final resources will be authored by Claude and independently reviewed by Codex;', 'The whole-subject resources were authored by Codex and reviewed by Claude at Jeremy’s direction;')
p.write_text(s)
p=REPO/'operations/SUBJECT-TRACKER.md';s=p.read_text()
s=s.replace('| Codex | review returned — content fixes required |','| Codex | Codex repairs complete; not re-reviewed |').replace('33,417 rendered-note words',word+' rendered-note words')
s=s.replace('read-only Claude Code review completed: FIX CONTENT BEFORE PUBLICATION; report in workspace review/CLAUDE-RESOURCE-REVIEW.md.', 'read-only Claude review returned FIX CONTENT BEFORE PUBLICATION; Codex repaired R6136-001–017 and PL-1–5, reran all checks with zero failures and saved review/repairs/REPAIR-REPORT.md. No follow-up review authorised.')
p.write_text(s)
manifest={str(p.relative_to(WS)):hashlib.sha256(p.read_bytes()).hexdigest() for p in WS.rglob('*') if p.is_file() and not any(x in p.parts for x in ['baseline','__pycache__']) and p.suffix in ['.json','.yaml','.md','.py'] and p.name!='post-repair-manifest.json'}
dump(OUT/'post-repair-manifest.json',manifest)
print(json.dumps(validation))
