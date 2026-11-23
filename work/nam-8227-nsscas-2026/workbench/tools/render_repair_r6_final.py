"""Generate the completed author handback only from the saved full R6 proof."""
import collections,json,re
from analysis_sources import A,WB,ROOT,write,digest
from apply_textbook_family_prose_parallel_r6 import validate as family_validate
from apply_textbook_figures_r6 import validate as figure_validate
from check_textbook_answer_pages_r6 import check as page_check

def readable(text):
 text=re.sub(r'([a-z])((?:R|P|Q)\d+)\b',r'\1 \2',text)
 text=re.sub(r'([a-z])([A-Z])',r'\1 \2',text)
 text=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',text)
 text=re.sub(r'\b([A-Za-z]{3,})(?=\d)',r'\1 ',text)
 text=re.sub(r'(?<!\d)([.;:])(?=\d)',r'\1 ',text)
 text=re.sub(r',(?=[A-Za-z0-9])',', ',text)
 text=re.sub(r'(?<=\))(?=[A-Za-z])',' ',text)
 text=re.sub(r'\b(no|on|of)(?=\d)',r'\1 ',text)
 text=re.sub(r';(?=\S)','; ',text)
 text=text.replace('reviewer’s634','reviewer’s 634').replace('YMsolution','YM solution').replace('YMleads','YM leads')
 for old,new in [('verifiedduplicate','verified duplicate'),('templatelead','template lead'),('summarylabels','summary labels'),('Twofresh','Two fresh'),('not60','not 60'),('A–Dscope','A–D scope')]:text=text.replace(old,new)
 return text

def main():
 proof=json.loads((WB/'checks/fresh-copy-verification-r6.json').read_text())
 assert proof['status']=='pass'and proof['double_rebuild']and proof['matches_author_checkout']
 manifest=json.loads((A/'history/rebuild-verification-r6-final-fresh-copy.json').read_text())
 for path,sha in manifest['output_hashes'].items():assert digest(ROOT/path)==sha,('proof stale',path)
 f=json.loads((A/'textbook-families.json').read_text());items=json.loads((A/'textbook-inventory.json').read_text())['items']
 family=family_validate(f,wb=WB);figures=figure_validate(items,json.loads((A/'textbook-figure-comparisons-r6.json').read_text()));pages=page_check()
 comparison=json.loads((WB/'checks/r6/comparison-progress.json').read_text())['counts'];problem_map=json.loads((A/'objective-problem-map.json').read_text())
 notes=[r for name in ['textbook-note-spacing-r6.json','textbook-note-spacing-parallel-r6.json','textbook-note-spacing-root-r6.json']for r in json.loads((WB/'tools'/name).read_text())['entries']]
 assert len({r['item_id']for r in notes})==len(notes)
 total=proof.get('total_seeded_errors_rejected',proof['previous_seeded_errors_rejected']+proof['r6_seeded_errors_rejected'])
 lines=['# Repair round 6 — author handback, NSSCAS Mathematics 8227','',
 '**Author repair complete; focused Claude cross-vendor acceptance pending. Step 3 still waits.** Owner: Vitalis. Author: Codex with three parallel author assistants, authorised22November2026. No commit or push.','',
 '| Finding | What changed | Evidence and author check |','|---|---|---|',
 '| R5-01 | All uncapped family–part candidates decided; actual positive source reads; named response exceptions;60-objective/138-demand map; all58 insight comparisons and affected proposals rebuilt. | `textbook-exam-relations-r6.json`, `textbook-families.json`, `objective-problem-map.json`, `textbook-insights.md`; `check_repair_r6.py --final`. |',
 '| R5-02 | Repaired membership/part selection and split topic-led groups; all original5744source-response pairs retained.500nearest-sibling comparisons,147singletons/353ordered multi-member progressions, family-specific precision and2385selected-response membership reasons. | `textbook_family_repairs_r6.py`, `textbook-family-prose-parallel-r6.json`; `check_textbook_family_prose_parallel_r6.py`. Source-input hash refresh requires identical selected method, answer and operands. |',
 '| R5-03 | All3940accepted assessed/component/objective/display link projections preserved. Per-objective map retains the accepted item union separately from family matching. | `history/r6-accepted-item-links-r5.json`; preservation and finalR6checks. Registry overlaps remain a step3decision; no retagging. |',
 '| R5-04 | All1758figures classified, stale status text retired, explicit not-checked content boundary retained; known9source-figure errors and11-entry correction register preserved. Native role/layout ambiguities checked separately. | `textbook-figure-repairs-r6.json`, `textbook-figure-comparisons-r6.json`; `check_textbook_figures_r6.py`. Medium+demand is representation evidence, not exact geometry or same-type equivalence. |',
 f'| R5-05 | {len(notes)}notes repaired;103end-key page boundary regions inspected;15leaf locators corrected or confirmed through canonical, flat, nested and parent records; two source slips preserved. | Three named note inputs; `textbook-answer-page-audit-r6.json`; `check_textbook_answer_pages_r6.py`. Four transparent author-prose typo changes explicitly recorded; other note repairs preserve every non-whitespace character. |',
 '| R5-06 | Added2023P2Q4(b)←Cambridge2020May/JunePaper22Q1, verifiedduplicate23, weaker2017templatelead;hidden label;Q4(a)stays027. Pair021unchanged tariff removed. Screen recall16/32, with baseline16/31. | `nsscas-cambridge-provenance.json`, `provenance-reading-r5.json`, `provenance-full-screen-r5.json`; foundation check and preserved source/render evidence. |','',
 '## Counts before and after','',
 '| Measure | R5 | R6 |','|---|---:|---:|',
 '| Analysis families, not recipe counts |380|500|',
 '| Main family–part decisions |0|2675|',
 '| Main same-type / ordered branch / rejected decisions |0 /219summarylabels /0|100 /619 /1956|',
 '| Member exception rows |0|126|',
 '| Unique same-type family/part pairs including named exceptions |0|183|',
 '| Family summaries: same-type / branch / textbook-only |0 /219 /161|102 /181 /217|',
 '| Incorrect no-exam insight sections |6|0|',
 '| Genuine no-exam insight sections |2|2|',
 '| Original source-response pairs retained |5744|5744|',
 '| Accepted item-link projections retained |3940|3940|',
 '| Figures: graphic / text callout |not separated|987 /771|',
 '| Stale actual-value / representation-pending figures |1444 /1733|0 /0|',
 '| Figure content explicitly not checked |not consistently explicit|1758|','',
 'Two ordered comparisons with the held2023P1Q1(b)stay internal only. They are excluded from usable family anchor lists and active insight proposals; the new held-anchor negative enforces this boundary. All other holds remain binding.','',
 'The earlier2080candidate count was computed on380families. Explicit demand/decision splits produce500families and2675uncapped candidates; this is not an increase in approved recipes.208provisional nonordered comparisons were withdrawn as positive branch claims and retained as rejected/related teaching connections. Branch labels require a warranted easier/harder direction.','',
 '## Per-objective problem map','', '```json',json.dumps(problem_map['counts'],indent=2),'```','',
 'Eleven demands have no NSSCAS part. Held parts stay visible and do not become usable learner anchors. Interpreting a radian has teaching support but no indexed posed practice item. A supporting drill or topic match is not full examination coverage.','',
 '## Narrow repair coverage and limits','',
 f'Family prose checks: {family["families"]}families/{family["memberships"]}memberships. Figure taxonomy uses accepted individual census descriptions, with23new native layout/role page reads; no1758figure content audit is claimed. {figures["by_type"]}. The512positive figure comparisons establish an observed medium on a linked demand only;475graphics have no such usable recorded part. Text callouts are separated.42agent role repairs plus the2earlierYMsolution-panel corrections are retained.','',
 f'Notes: {len(notes)}unique source records were repaired using the original100patches plus200parallel and734root-read proposals. The reviewer’s634count had no supplied detection predicate; this broader repair count is not presented as the same denominator. Original discovery proposals remain discovery; the applied, dated author inputs are authoritative. Four transparent prose typos were corrected with explicit before/after guards. Note repair is not a new mathematical content audit.','',
 'The103key-page inspections cover referenced end-key page tops and column starts (32Goldie,71YM). Inline worked solutions retain prior accepted locators; no new whole-body answer-page audit is claimed. Eight additional question-level locator repairs and two preserved prior repairs account for15leaf checks. Two laterYMleads were rejected after native label verification and were not edited.','',
 'The32confirmed provenance pairs cover29NSSCAS questions. The matching screen finds16of32confirmed pairs; no missing match proves original authorship. Textbook originals remain internal and learner_display:false.','',
 '## Validation','',
 f'Two complete builds in independent fresh directories: {proof["commands_per_run"]}commands each, {proof["outputs_compared"]}byte-identical outputs, matching the author checkout. {total}seeded corruption checks rejected:38prior,{proof["r6_seeded_errors_rejected"]}coreR6,5family-prose and5figure checks. These counts include separately exercised overlapping protections; they are not{total}different educational demands.','',
 '`checks/fresh-copy-verification-r6.json` and `analysis/history/rebuild-verification-r6-final-fresh-copy.json` hold the proof.436original source hashes and23baseline review-file hashes were checked; the single owner-revised prompt hash is the recorded authorised difference. The originalR5snapshot is preserved.','',
 'The declared pipeline reproduces assembly from independently copied workspaces that include retained generated records. Byte agreement does not assert that every compared file was regenerated from an empty directory. The recorded tool/input manifest enforces byte equality of the pipeline code and author records; a late dependency correction was staged identically before its dependent family/check stages and is recorded in checks/r6/proof-held-anchor-repair.json.','',
 'Passing author checks does not establish educational correctness, cross-vendor acceptance, runtime marking, learner UI, resource installation or production readiness. No PLAN, recipe contract, recipes, runtime generators, work orders, imports, assignments, commit or push were produced.','',
 '## Next step','',
 'Claude performs the focused cross-vendor check of this frozen repair. Vitalis’s ruling still holds: step3starts only after source-analysis acceptance. See `analysis/REVIEW-START-HERE.md`.','']
 (WB/'checks/repair-r6-report.md').write_text(readable('\n'.join(lines))+'\n')
 facts=(f'R6 author repair complete; focused independent Claude check pending. All2675uncapped candidate decisions saved,500families,2385memberships,60objectives/138demands. {len(notes)}notes repaired;1758figure records classified;103end-key page regions inspected. Twofresh complete builds agree across{proof["outputs_compared"]}outputs;{total}seeded checks rejected. No owner or independent acceptance is inferred. Step3waits. No commit/push.\n')
 facts=readable(facts)
 (WB/'STATUS.md').write_text('# STATUS — NSSCAS Mathematics 8227 Workbench\n\n'+facts+'\nSee checks/repair-r6-report.md, checks/fresh-copy-verification-r6.json and analysis/REVIEW-START-HERE.md.\n')
 h=WB/'HANDOVER.md';old=h.read_text();old=old.split('\n## Final R6 author handback',1)[0];a=old.index('## Current saved checkpoint');b=old.index('## Latest content work',a);old=old[:a]+'## Current saved checkpoint\n\n'+facts+'\n'+old[b:];old+='\n## Final R6 author handback —22November2026\n\n'+facts+'\nThe prior working entries are historical. Read the generated repair report and frozen snapshot before continuing. Claude independently checks the repair; no step3work is authorised by an author pass alone.\n';h.write_text(old)
 for name in ['STATUS.md','README.md']:
  p=WB.parent/name;text=p.read_text();banner='<!-- R6-ACTIVE-CHECKPOINT -->\n'+facts+'<!-- /R6-ACTIVE-CHECKPOINT -->';text=re.sub(r'<!-- R6-ACTIVE-CHECKPOINT -->.*?<!-- /R6-ACTIVE-CHECKPOINT -->',lambda _:banner,text,count=1,flags=re.S);p.write_text(text)
 request='# Focused review request —8227repair round6\n\nRead `analysis/REVIEW-START-HERE.md`, the revised owner prompt in `review/opus-5-5-repair-r5/REPAIR-PROMPT.md`, `checks/repair-r6-report.md` and the current frozen `analysis/analysis-snapshot.json`. Independently check the repaired A–Dscope against the named sources, re-run the author checks and select your own semantic spotchecks. Check same-type decisions and response exceptions, nearest-sibling/progression/precision claims, representation-medium limits, spaced notes and key-page boundaries, provenance037and measured recall. Do not infer acceptance from counts or hashes. Return accept named scope or repair with concrete locators. Do not edit author sources or start step3.\n'
 request=request.replace('Read `analysis/REVIEW-START-HERE.md`','You are REVIEWER; workspace `work/nam-8227-nsscas-2026/`. Read AGENTS.md, TEAM-PLAYBOOK.md and only `standard/v0.2.0-draft/roles/REVIEWER.md`, then the Workbench playbook and `analysis/REVIEW-START-HERE.md`')
 request=request.replace('Read AGENTS.md','Workbench path: `work/nam-8227-nsscas-2026/workbench/`; analysis, checks and review paths below are relative to it. Read AGENTS.md')
 (WB/'checks/repair-r6-review-request.md').write_text(readable(request))
 print(json.dumps(dict(status='author handback generated; independent acceptance pending',notes=len(notes),families=500,total_seeded_checks=total),indent=2))
if __name__=='__main__':main()
