"""Prepare final review with required planning context supplied in full."""
import hashlib,json
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
OUT=WS/'review'
def read(p):return json.loads(p.read_text())
brief="Conduct the FINAL independent whole-subject review (round 5) of Namibia NSSCO Development Studies 6136, Grades 10–11. Jeremy explicitly authorised this single review. Codex authored the resources and repaired all five round-four findings. Judge the current text independently; no author disposition or earlier verdict is proof, and approval is not presumed.\n\nREVIEW ONLY. Read/Glob/Grep tools; no edits, scripts, web research, subagents, publication, commits or imports. One bounded review, Opus medium, maximum $8 reported API usage. Stop after writing the report; do not launch further reviews.\n\nMandatory supplied context: AGENTS.md, TEAM-PLAYBOOK.md, REVIEWER.md, both complete qualification/subject profiles, current plan and handover, all 18 complete contracts, objective summaries and work-order slot/assessment summaries. Inspect these alongside the learner text for scope, objectives, conditions, commands, tariffs and answer structures. The direct learner packet contains every lesson block and all 543 prompts, answers and marking guides: 18 topics, 101 units, 505 cards, 38 activities, 36,172 rendered-note words. Read every lesson, at least 20 varied cards per topic (all if fewer), all four complete research packages and every changed artefact listed in review/repairs/round4/actions.json. Actual files remain available. Avoid redundant retrieval of supplied documents or broad baseline-tree reads.\n\nApply the reviewer role's six fixed questions. Check prompt, answer and marking guide together; independently recompute meaningful numerical examples and compare adjacent representations. Check teaching depth, top-tariff support, supplied conditions and facts, standalone cards, appropriate quantitative methods and interpretation. Report concrete consequential defects with exact IDs and repairs, not stylistic preferences.\n\nRecheck EACH round-four finding F1–F5, disposition resolved / partial / unresolved with evidence:\nF1: adjacent population-pyramid overview, full age-sex table and construction specifications must agree and handle broad unequal age bands honestly.\nF2: sector practice, systematic/stratified/random sampling, pie/rectangle and map worked examples must teach methods using independent practice datasets rather than supplying assessment answers. Check the related systematic definition and claim revision too.\nF3: 2.2-003 must compare short/long planning horizons, including detail versus direction.\nF4: the 59 revised item-specific criteria and ten duplicate P01 removals must give valid marks aligned to answers, not generic template or full-answer copies. The renewable-resource criterion explicitly includes regrowth. Check related items for recurrence.\nF5: B-only 2.2-P02 must require interpretation of supplied targets/results, with no credit merely for naming pillars; 10.1-P02 must describe collection procedures without giving away the method name in the stem or next question. Verify the spoiled-inside-total clarification remains.\n\nAlso check for regressions in prior repairs, especially restored teaching paragraphs, 4.2 work-status population, 7.3 traditional/modern mapping, SDGs 4/5/13 and climate mechanism, 1.2-006 demand, HPP and NDP5 terminology. Run two learner thought tests from notes alone: a high-tariff sampling-method explanation and a three-mark explanation of climate action's sustainable-development importance. Include a short HPP three-pillar description probe.\n\nSource authority: local official syllabus Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf; curriculum/syllabus-facts.json; assessment-evidence/extracted/, source-manifest.json, GAPS.md; operations/analysis/6136-nssco-development-studies-corpus-analysis.md. Use saved local sources for source checks, no internet. Do not reproduce assessment wording. Distinguish verified source checks from matters not checked.\n\nLocal AUTHOR evidence (not independent approval): all 18 topics zero deterministic failures and what_to_fix exit zero; 543 approved slots/metadata retained; 18 targeted checks, 17 existing numerical checks and two negative cases pass; 65 previously restored teaching paragraphs unchanged and one intentionally renumbered systematic example retains its definition. Copied-wording scan over 40 extracts: zero 12+ word defects, one standard SDG-title 11-word match retained. 78 learner artefacts changed and one claim revision propagated. Evidence and final hashes are in round4/validation.json. Do not repeat the whole mechanical build.\n\nKnown unresolved limitations: 749 claims remain unverified/non-publishable; earlier N-03 source-verification debt, recurring card scenarios and standard graph/schema/runner issues remain visible. C35/C41/C43 not_run are not passes. Distinguish content verdict from release readiness and explain whether these limitations independently block publication. No teacher approval is claimed or required to conduct this review.\n\nOutput about 2,500 words maximum: verdict publish / fix content before publication / fix the plan first; findings with severity, exact IDs, consequence, specific repair and confidence; disposition of every F1–F5; learner tests/probe; explicit coverage of all mandatory profile/plan/contract documents and learner text, including skipped coverage; unresolved source/tool limitations. If required coverage is skipped, label scope INCOMPLETE. Do not mark unchecked matters resolved or author fixes. Stop after the report.\n"
(OUT/'CLAUDE-RESOURCE-REVIEW-BRIEF-5.md').write_text(brief)
parts=[]
manifest={}
topic_dirs=sorted((p for p in (WS/'topics').iterdir() if (p/'contract.json').exists()), key=lambda p:tuple(map(int,p.name.split('.'))))
for td in topic_dirs:
    parts.append(f'\n# TOPIC {td.name}: {read(td/"contract.json")["topic_title"]}\n')
    for p in sorted((td/'content-units').glob('*.json')):
        manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
        u=read(p)
        parts.append(f'\n## UNIT {u["unit_id"]}: {u.get("title", "")}\n')
        for b in u['blocks']:
            parts.append(f'\n### {b["block_id"]}: {b.get("heading", "")}\n{b["text"]}\n')
    for p in sorted((td/'learning-items').glob('topic_*_items.json')):
        manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
        for i in read(p)['items']:
            labels={k:i[k] for k in ['objective_ids','subtype','item_type','assessment_objectives','blooms_level','command_word','mark_tariff'] if k in i}
            parts.append(f'\n### ITEM {i["item_id"]}\n{json.dumps(labels,ensure_ascii=False)}\nPROMPT: {i["prompt"]}\nANSWER: {i["canonical_answer"]}\nGUIDANCE: '+json.dumps(i.get('marking_guidance',[]),ensure_ascii=False)+'\n')
packet=''.join(parts)
(OUT/'LEARNER-TEXT-PACKET-5.md').write_text(packet)
for p in [WS/'qualification-profile.yaml',WS/'subject-profile.yaml',WS/'review/CLAUDE-RESOURCE-REVIEW-2.md',WS/'review/repairs/SECOND-REPAIR-REPORT.md']:
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'claude-resource-review-input-manifest-5.json').write_text(json.dumps(manifest,indent=2)+'\n')
context=[]
mandatory=[REPO/'AGENTS.md',REPO/'TEAM-PLAYBOOK.md',REPO/'standard/v0.2.0-draft/roles/REVIEWER.md',WS/'qualification-profile.yaml',WS/'subject-profile.yaml',WS/'PLAN-6136-nssco-development-studies.md',WS/'HANDOVER-6136-nssco-development-studies.md']
mandatory += [td/'contract.json' for td in topic_dirs]
for p in mandatory:
    context.append('\n## REQUIRED DOCUMENT: '+str(p.relative_to(REPO))+'\n'+p.read_text()+'\n')
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
registry=read(WS/'curriculum/objective_registry.json')
context.append('\n## Objective registry: ID, syllabus wording, commands and demand\n'+json.dumps([{k:o[k] for k in ['objective_id','parent_id','topic_id','syllabus_text','command_words','depth_tier','assessment_objectives'] if k in o} for o in registry['objectives']],ensure_ascii=False)+'\n')
for td in topic_dirs:
    wo=read(td/'work_order.json')
    context.append('\n## WORK ORDER '+td.name+'\n'+json.dumps({k:wo[k] for k in ['item_slots','performance_tasks','assessable_objective_count'] if k in wo},ensure_ascii=False)+'\n')
    manifest[str((td/'work_order.json').relative_to(REPO))]=hashlib.sha256((td/'work_order.json').read_bytes()).hexdigest()
reports=[]
for p in [WS/'review/CLAUDE-RESOURCE-REVIEW-4.md',WS/'review/repairs/round4/REPAIR-REPORT.md',WS/'review/repairs/round4/validation.json']:
    reports.append('\n## PRIOR REVIEW / REPAIR CONTEXT: '+str(p.relative_to(REPO))+'\n'+p.read_text()+'\n')
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'CLAUDE-RESOURCE-REVIEW-INPUT-5.md').write_text(brief+'\nBEGIN MANDATORY GOVERNANCE AND PLANNING CONTEXT\n'+''.join(context)+'\nBEGIN CURRENT LEARNER TEXT PACKET\n'+packet+'\nBEGIN PREVIOUS REVIEW AND REPAIR CONTEXT\n'+''.join(reports))
(OUT/'claude-resource-review-input-manifest-5.json').write_text(json.dumps(manifest,indent=2)+'\n')

print(json.dumps({'topics':len(topic_dirs),'source_files':len(manifest),'packet_words':len(packet.split()),'packet_characters':len(packet)},indent=2))
