"""Prepare a concise lossless learner-text packet and run a fresh read-only review."""
import hashlib
import json
import subprocess
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
REPO = WS.parents[1]
OUT = WS / 'review'

def read(p):
    return json.loads(p.read_text())

brief = '''Conduct the THIRD independent whole-subject review of Namibia NSSCO Development Studies 6136, Grades 10–11. Jeremy explicitly authorised this review. You are a fresh Claude Code session: Codex authored the subject and applied two sets of review repairs. You assess it independently; author repair claims and automated decisions are evidence to inspect, not proof of quality.

Read AGENTS.md, TEAM-PLAYBOOK.md Step 6, and standard/v0.2.0-draft/roles/REVIEWER.md. Jeremy overrides any repair instruction: REVIEW ONLY. Your available tools are Read, Glob and Grep. No edits, scripts, web, subagents, publication, commits or imports. Stay within this subject and its named local sources. This is one finite review round under the reviewer's six questions, not an open-ended hunt. Output a report and stop.

The learner packet below is extracted directly from current structured units/items, retaining every block's text and every item's prompt, canonical answer, marking guidance, IDs and assessment labels. It contains all 18 lessons and all 543 items (505 cards, 38 activities), without redundant JSON metadata. Its manifest records underlying file hashes. Use the packet as your principal reading; inspect actual rendered notes, claims and source files for specific checks as needed. Avoid rereading whole baseline trees or repair scripts without a concrete reason. Read the two profiles and current PLAN/HANDOVER as well: qualification-profile.yaml, subject-profile.yaml, PLAN-6136-nssco-development-studies.md and HANDOVER-6136-nssco-development-studies.md, all under work/nam-6136-nssco-2026/. Inspect curriculum/objective_registry.json and relevant work-order/contract portions for scope and command/tariff checks. Never read another subject workspace.

Syllabus authority: Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf; its saved transcription curriculum/syllabus-facts.json. Assessment evidence: this workspace's assessment-evidence/extracted/, source-manifest.json and GAPS.md, plus operations/analysis/6136-nssco-development-studies-corpus-analysis.md. No external research. Use these to test accuracy and assessment demand; do not reproduce exam wording.

Coverage: read all 18 lessons; at least 20 cards per topic (all if fewer), prioritising repaired cards and a varied sample across subtypes; all four research packages, including stimuli, answers, tariffs and Section B scaffolds. All learner text is available in the packet, but state exactly what you actually reviewed. Check the reviewer's six fixed questions: causal validity; facts supplied by prompts; conditions; syllabus scope/missing teaching; numerical methods and interpretations; and two demanding learner tests from the notes alone. One learner test MUST cover defining and describing random, stratified and systematic sampling; another should cover an applied high-tariff objective. Check notes-to-card support, questions' actual demand vs tariff, and that fictional examples never become a learner's personal research record.

First form your own assessment of the learner text. Then read review/CLAUDE-RESOURCE-REVIEW-2.md and review/repairs/SECOND-REPAIR-REPORT.md. Recheck N-01–N-08, R6136-004 and R6136-015, with particular attention to restoration of 66 teaching paragraphs, source-to-claim attribution, the new SDG material (including learner-facing references to exam provenance), the 1.2-006 answer's prompt-supplied facts and three-mark demand, HPP/NDP5 cards, and 7.3-006. Do not treat a repair disposition as resolved without checking its actual text. The previous whole-subject review is not blind context; your verdict must still be independent.

Latest Codex audit: 18 topics, 749 unverified/non-publishable claims, 101 units, 543 items and 36,241 rendered-note words; zero deterministic failures, 16 local numerical checks, no exact 8+ word matches against 40 saved assessment extracts. Attribute these as Codex runs. Do not execute or repeat mechanical checks. Focus on methods/interpretations and not_run gaps; C35/C41/C43 are not_run, not PASS. Standard profile-schema/runner/command-word limitations remain outside your editing scope. Review cannot confer teacher verification or publication authorisation.

Cost discipline: one model at medium effort, no subagents or research. This invocation has an $8 reported API-cost ceiling. Keep tool retrieval selective; the full learner packet is already supplied. Final report at most roughly 2,500 words: verdict (publish / fix content before publication / fix the plan first), concrete findings with severity, exact IDs/locators, learner consequence, repair and confidence; a compact disposition table for N-01–N-08/R6136-004/R6136-015; actual coverage by topic; two learner tests; and explicit limitations. Do not restate entire old reports or mark unchecked findings resolved. If budget prevents full coverage, label the review INCOMPLETE and state missing scope. You make no edits. Stop after the report.
'''
(OUT / 'CLAUDE-RESOURCE-REVIEW-BRIEF-3.md').write_text(brief)
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
(OUT/'LEARNER-TEXT-PACKET-3.md').write_text(packet)
for p in [WS/'qualification-profile.yaml',WS/'subject-profile.yaml',WS/'review/CLAUDE-RESOURCE-REVIEW-2.md',WS/'review/repairs/SECOND-REPAIR-REPORT.md']:
    manifest[str(p.relative_to(REPO))]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'claude-resource-review-input-manifest-3.json').write_text(json.dumps(manifest,indent=2)+'\n')
(OUT/'CLAUDE-RESOURCE-REVIEW-INPUT-3.md').write_text(brief+'\n\nBEGIN CURRENT LEARNER TEXT PACKET\n'+packet)
print(json.dumps({'topics':len(topic_dirs),'source_files':len(manifest),'packet_words':len(packet.split()),'packet_characters':len(packet)},indent=2))
