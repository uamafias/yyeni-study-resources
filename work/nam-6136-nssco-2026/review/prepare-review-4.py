"""Prepare final review with required planning context supplied in full."""
import hashlib,json
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
OUT=WS/'review'
def read(p):return json.loads(p.read_text())
brief='Conduct the FINAL independent review (round 4) of Namibia NSSCO Development Studies 6136, Grades 10–11. Jeremy authorised this single review on 2026-10-21. Fresh Claude session; Codex authored the subject and repaired R3-01–R3-10. Form your own judgement from the current material. Earlier verdicts and author dispositions are not proof.\n\nREVIEW ONLY: Read/Glob/Grep tools, no edits, scripts, web research, subagents, publication, commits or imports. One finite round using the reviewer’s six fixed questions. The supplied context contains AGENTS.md, TEAM-PLAYBOOK.md, REVIEWER.md, BOTH COMPLETE profiles, current PLAN and HANDOVER, objective register summary, ALL 18 COMPLETE contracts, and work-order slot/assessment summaries. These are mandatory review scope, not optional background. Round 3 skipped profiles/plan/contracts: this final review must inspect them and report any content/plan incompatibilities. They are supplied directly so you need not fetch them again. Check scope exclusions, answer structures, conditioned mechanisms, objective alignment, command words, tariffs and qualifications against learner material. Do not claim full review if you skip any required section.\n\nThe learner packet contains every current lesson block and all 543 prompts, canonical answers and marking guides, with exact IDs and labels: 18 topics, 749 unverified/non-publishable claims, 101 units, 505 cards, 38 activities, 36,079 rendered-note words. Read every lesson, at least 20 varied cards/topic (all when fewer), every changed artefact in round3/actions.json, and all four research packages including stimuli, answer/guidance and own-enquiry scaffolds. The packet is a direct text extraction, not an author summary; actual files and hash manifest remain available for selective checks. Avoid reading whole baseline trees or old repair scripts without a specific concern.\n\nSource authority is the official syllabus and saved assessment corpus: Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf; work/nam-6136-nssco-2026/curriculum/syllabus-facts.json; this workspace’s assessment-evidence/extracted/, source-manifest.json and GAPS.md; operations/analysis/6136-nssco-development-studies-corpus-analysis.md. Use local evidence to check syllabus demand and facts. No new internet research. Do not reproduce official assessment wording.\n\nAssess the six reviewer questions: causal validity; facts/conditions supplied by prompts; scope and missing teaching; appropriate quantitative methods and interpretation; and whether notes support top-tariff answers. Check prompt/answer/marking-guide agreement as one unit, not separately. Recheck all R3-01–R3-10 against actual files, especially four-mark explanation depth, distinct worked-note examples, 4.2 work-status population, 10.1-P02 spoiled-inside-total fact, 7.3 traditional/modern mapping, SDG 4/5/13 and climate mechanism, 1.2-006 three-mark demand, HPP three-pillar description, NDP5 terminology and internal-reference removal. Existing 2.2-P02(a) provides three-mark applied description of HPP pillars; 1.2-P01(a) provides two-mark pillar retrieval, with unchanged slot labels. Judge whether these substitutions genuinely meet their objectives and AO demands. Record new defects only when concrete and consequential, not stylistic preferences.\n\nTwo learner tests: (1) high-tariff sampling-method explanation from notes alone; (2) a three-mark explanation of climate action’s sustainable-development importance. Add a short probe of HPP three-pillar description. Report whether the notes actually teach sufficient distinct content and conditions.\n\nKnown limitations are not hidden: external fact/claim verification debt N-03, some recurring card scenarios, and standard-owner graph/schema/runner limits remain; no teacher approval is claimed or required to conduct this review. Distinguish these from newly defective learner text. Latest LOCAL Codex evidence: 18 topics with zero deterministic failures, 12 targeted regression checks, 17 numerical checks plus one negative case, preservation of 66 restored teaching paragraphs, zero full card prompts pasted into notes. Copied-wording scan: one 11-word run made solely of official SDG 8/12 titles/numbers (retained terminology), zero 12+ defects against 40 extracts. Attribute these as Codex runs. Do not repeat mechanical checks; inspect meaning, conditions, methods and not_run gaps. C35/C41/C43 remain not_run, not passes.\n\nBudget: Opus medium, $8 maximum reported API usage, no subagents/research. Input context is supplied once to avoid repeated retrieval. Output roughly 2,500 words maximum: verdict publish / fix content before publication / fix the plan first; consequential findings with severity, exact IDs, consequence, concrete repair and confidence; disposition of every R3 finding; two learner tests plus HPP probe; explicit coverage of learner text AND each mandatory profile/plan/contract document; unresolved limitations. If required coverage is skipped, label overall scope INCOMPLETE, even when learner content was fully read. Do not mark unchecked matters resolved. Do not author fixes or request another round. Stop after the report.\n'
(OUT/'CLAUDE-RESOURCE-REVIEW-BRIEF-4.md').write_text(brief)
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
(OUT/'LEARNER-TEXT-PACKET-4.md').write_text(packet)
for p in [WS/'qualification-profile.yaml',WS/'subject-profile.yaml',WS/'review/CLAUDE-RESOURCE-REVIEW-2.md',WS/'review/repairs/SECOND-REPAIR-REPORT.md']:
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'claude-resource-review-input-manifest-4.json').write_text(json.dumps(manifest,indent=2)+'\n')
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
for p in [WS/'review/CLAUDE-RESOURCE-REVIEW-3.md',WS/'review/repairs/round3/REPAIR-REPORT.md',WS/'review/repairs/round3/validation.json']:
    reports.append('\n## PRIOR REVIEW / REPAIR CONTEXT: '+str(p.relative_to(REPO))+'\n'+p.read_text()+'\n')
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'CLAUDE-RESOURCE-REVIEW-INPUT-4.md').write_text(brief+'\nBEGIN MANDATORY GOVERNANCE AND PLANNING CONTEXT\n'+''.join(context)+'\nBEGIN CURRENT LEARNER TEXT PACKET\n'+packet+'\nBEGIN PREVIOUS REVIEW AND REPAIR CONTEXT\n'+''.join(reports))
(OUT/'claude-resource-review-input-manifest-4.json').write_text(json.dumps(manifest,indent=2)+'\n')

print(json.dumps({'topics':len(topic_dirs),'source_files':len(manifest),'packet_words':len(packet.split()),'packet_characters':len(packet)},indent=2))
