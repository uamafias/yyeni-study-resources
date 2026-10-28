"""Render the mining report, with all counts/tables from the mined evidence."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
load = lambda p: json.loads(p.read_text())
e = WS / 'assessment-evidence'
v = load(e / 'verification.json')
ex = load(WS / 'curriculum/exam-exposure.json')
cw = load(e / 'command-word-analysis.json')
sources = load(e / 'sources.json')['sources']
rows = load(e / 'assessment_evidence.json')['records']
out = ['# Corpus analysis — 6145 NSSCO Economics', '',
       '28 October 2026. Owner: Vitalis P Haupindi. Miner: Codex. This is step 3 evidence for the 2026 learner resources; it is not an authoring plan or learner-facing text.', '',
       '## 1. The corpus', '',
       'The 2018 NIED syllabus was read first and its assessment tables were confirmed by Vitalis before this analysis. All held Economics question papers and Economics sections of the five annual reports were then read in plain and layout extraction. Poppler/pdftotext is unavailable on PATH, so pypdf supplied both views; selected diagrams and tables were rendered with PDFium. No other subject was mined.', '',
       '| Year | QP parts, Paper 1 | QP parts, Paper 2 | Report PDF pages (one-based) |',
       '|---|---:|---:|---|']
for y in range(2020, 2025):
    r = next(s for s in sources if s['source_id'] == f'{y}-ER')
    out.append(f"| {y} | {sum(q['year']==y and q['paper_id']=='1' for q in rows)} | {sum(q['year']==y and q['paper_id']=='2' for q in rows)} | {r['pdf_pages'][0]}–{r['pdf_pages'][1]} |")
out += ['', f"**{v['question_parts']} independently tariffed parts; {v['marks_offered']:,} marks offered; {v['candidate_marks']} candidate marks across five annual series.** Every Paper 1 reconciles to 40 + 40 = 80. Every Paper 2 reconciles to six offered questions of 20 = 120; the candidate answers compulsory Q1 plus three of Q2–Q6 = 80. The latter distinction is preserved in all exposure figures.", '',
        f"The reports contain answers and marking guidance; they are **not standalone mark schemes**. {v['parts_with_credit_shape']} parts have a report-supported credit-shape record; 12 parts in 2020 Paper 1 Section B have performance comments without complete per-part answer grids. {v['report_performance_comments']} question-specific performance-comment records are retained (including positive observations); {v['report_statement_spans']} sentence spans are indexed, not claimed as independent mistakes. {v['parts_with_common_errors']} question parts link to a recorded weakness. One report paragraph covers both 2021 Q11 parts, and displaced 2021 comments are remapped semantically with the original reference preserved.", '',
        'No 2025 papers/reports, standalone mark schemes or grade-threshold tables were found. Covers state the year, not an examination month; series are not labelled October/November without evidence. Six QP filenames from 2021–2023 say First Proof and cannot be certified final from filenames. Exact paths and hashes are in assessment-evidence/sources.json; limitations are in assessment-evidence/GAPS.md.', '',
        '## 2. What each paper looks like', '',
        '- **Paper 1, 2 h 30 min, 80 marks:** Section A is compulsory short response, 40 marks, using 1–3-mark parts. Definitions, precise distinctions, classifications, formula recall, simple calculations and diagram reading appear. Section B is compulsory applied/data-response work, 40 marks, normally two cases. Context interpretation, economic mechanisms, diagrams and extended judgements are required. The split between the two cases varies: 23/17 in 2020, 20/20 in the later held papers.',
        '- **Paper 2, 2 h, 80 candidate marks:** Q1 is a compulsory 20-mark case; the remaining five 20-mark questions are optional, of which three are answered. Structured essays combine short knowledge elements with longer analysis/evaluation. Seven-mark parts recur; compulsory tasks can reach nine marks. Draw-and-explain tasks recur on demand/supply and government intervention. Students need to follow the choice instructions as well as the economics.', '',
        '| Paper/section | Independently tariffed parts | Tariffs seen, with counts |',
        '|---|---:|---|']
for paper, sec in [('1','A'),('1','B'),('2','A'),('2','B')]:
    rs = [q for q in rows if q['paper_id'] == paper and q['section'] == sec]
    counts = collections.Counter(q['mark_tariff'] for q in rs)
    out.append(f"| Paper {paper}, {sec} | {len(rs)} | " + '; '.join(f'{k}m × {n}' for k,n in sorted(counts.items())) + ' |')
out += ['', 'These are counts of tasks offered, not how many a learner attempts. Source: all ten question papers, checked against every printed tariff token.', '',
        '## 3. Command words actually used', '',
        'Counts below use one primary opening per tariffed part. Context or “Except…” prefaces are ignored, Using is normalised to Use, and “To what…” is classified with What. **Use-prefaced compound instructions retain their embedded verbs separately**, so Calculate at 2 marks, for example, is evidenced within such instructions even though the primary-opening Calculate row below has 1 and 5. All embedded verbs, tariffs and evidence IDs are in assessment-evidence/command-word-analysis.json. Interrogative frames are listed separately; their presence does not create a missing official definition.', '',
        '| Syllabus-table word | Primary count | Modal tariff(s) | Primary-opening tariffs and counts |',
        '|---|---:|---|---|']
for c in sorted([c for c in cw['commands'] if c['in_syllabus_table']],key=lambda c:-c['count']):
    out.append(f"| {c['word'].title()} | {c['count']} | {', '.join(map(str,c['modal_tariffs']))} | " + '; '.join(f'{k}m × {n}' for k,n in c['tariffs'].items()) + ' |')
out += ['', '**All 13 words from section 10 are observed. None is listed-but-unobserved in this corpus.**', '',
        '| Other observed directive | Primary count | Modal tariff(s) | Tariffs seen |',
        '|---|---:|---|---|']
for c in sorted([c for c in cw['commands'] if not c['in_syllabus_table'] and not c['note']],key=lambda c:-c['count']):
    out.append(f"| {c['word'].title()} | {c['count']} | {', '.join(map(str,c['modal_tariffs']))} | {', '.join(c['tariffs'])} |")
frames = [c for c in cw['commands'] if c['note']]
out += ['', 'Interrogative openings: ' + '; '.join(f"{c['word']} ({c['count']})" for c in frames) + '.', '',
        'Draw is observed as an embedded instruction, notably 2022 Paper 2 Q4(b); it must not be presented as an observed primary opening in these counts. Before slot generation, the framework must preserve the distinction between a complete compound instruction and an isolated verb/tariff. A word from another qualification is not evidence for this one.', '',
        '## 4. What a creditable answer looks like', '',
        'The following architectures are paraphrased from the reports’ answer/guidance columns and performance comments; exact wording is not supplied for reuse.', '',
        '- **Short definitions:** include the features that distinguish the term. The 2024 report distinguishes total income from income per head (P1 Q19, PDF p.175), and requires active willingness/ability to find work in unemployment (P2 Q5(a), p.184). Do not assume an example earns full definition credit.',
        '- **Lists versus developed descriptions:** six marks can ask for six items or three developed features. 2021 P2 Q2(a), report p.138, caps bare feature names at three of six marks. Conversely 2022 P2 Q3(a), p.170, asks for six growth motives. Tariff alone does not decide the structure.',
        '- **Calculations:** give the requested method, substitution, magnitude and unit. Elasticity is not a percentage; a percentage change is. The 2021 P1 Q25(a) report (p.135) explicitly records loss of marks for a percent sign on the final elasticity. The 2023 population calculation needs a consistent persons/millions unit (P2 Q1(c), p.181). Source arithmetic anomalies are quarantined.',
        '- **Diagram with analysis:** multiple tasks use a 4-mark diagram plus a 3-mark explanation, e.g. 2020 P2 Q1(b), report p.146, and 2024 P2 Q1(c), pp.179–180. Label axes, curves, original and changed positions; use the correct curve/control and connect the written mechanism to the diagram. A binding minimum wage/maximum price does not itself shift the curves.',
        '- **Diagram-only and mixed tasks:** 2022 P1 Q26(b), report p.164, awards four marks for the diagram and no unrequested explanation. 2022 P2 Q4(b), p.172, combines a quota definition and a diagram within seven marks. Do not impose a 4+3 model on these.',
        '- **Analysis:** show the relevant change and causal links to the specified actor/outcome. 2023 P2 Q3(b), report p.186, concerns saving, not a generic discussion of cheaper borrowing. 2024 P2 Q6(b), p.186, requires two developed causes and penalises a static statement where a change is asked for.',
        '- **Evaluation and decisions:** two-sided “whether/always” tasks need developed opposing considerations; recent report guidance often reserves a distinct conclusion/decision. 2023 P2 Q2(c), p.185, and Q5(c), p.190, state this. In 2024 P2 Q2(d), p.181, a one-sided answer is capped at four of seven. However 2021 P2 Q1(c), p.138, is a focused five-mark evaluation of employment consequences; 2024 P2 Q1(d), p.180, is a five-mark subsidy justification. Do not add a compulsory counterargument/conclusion mark where the source does not require one.',
        '- **Multiple components/enquiry:** 2021 P1 Q24(c), report p.134, requires stock-exchange functions and economic effects, rather than a generic pros/cons debate. 2023 P1 Q25(d), p.178, requires questions to investigate economic costs, not statements about accidents. 2023 P2 Q2(a), p.184, requires the link between productivity and profit as well as the definitions.', '',
        'The generated curriculum/answer-shapes.json records 13 families and task-specific allocations. They are planning guidance, not a universal mark scheme. Assessment AO labels on individual evidence records are explicitly judgement unless the source states them; component percentages remain the syllabus values.', '',
        '## 5. Where the marks fall', '',
        'Every part was mapped by reading its actual assessed meaning and the case context. No token-matching first pass was used, so there is no fabricated count of mappings corrected from such a pass. A cross-topic part has one primary owner for mark-share arithmetic; secondary links count for exposure without double-counting marks. This is an analytic allocation convention, not an official topic weighting.', '',
        '| Syllabus topic | Primary marks offered | Share of 1,000 offered marks | Annual series represented |',
        '|---|---:|---:|---|']
for t in sorted(ex['topics'], key=lambda t:-t['primary_marks_offered']):
    out.append(f"| {t['topic_id']} {t['title']} | {t['primary_marks_offered']} | {t['share_of_offered_marks_percent']}% | {len(t['series'])} |")
out += ['', 'At the 96 syllabus-bullet anchors, exposure classes are: ' + '; '.join(f'{k}: {n}' for k,n in v['exposure_classes'].items()) + '. Here core means 4–5 annual series; frequent 3; occasional 2; rare 1; unseen 0. These thresholds are explicitly calibrated to five years.', '',
        'Eleven bullet anchors have no observation in this held corpus; they remain mandatory coverage. There is one low-confidence mapping (2021 P1 Q8, e-commerce, not explicitly named in the content outline) and eleven supporting/cross-cutting mappings. Value added, formal/informal firms, WTO and occupational mobility are retained as visibly supporting mappings, not silently promoted into explicit syllabus wording. The planner must decompose listed members and preserve an ID crosswalk from assessment-evidence/syllabus-objective-index.json.', '',
        '## 6. How candidates lose marks', '',
        '| Recurring failure | Evidence examples (report PDF pages) | Resource response |',
        '|---|---|---|',
        '| Giving definitions where reasons, applications or methods were asked for | 2020 P1 Q18 p.143; 2023 P1 Q26(b) p.178; 2024 P1 Q10 p.173 | Use contrast tasks: identify the requested operation, then perform it in the new case. |',
        '| Listing without developing the mechanism | 2021 P2 Q4(c) p.141; 2022 P2 Q2(c) p.169; 2024 P2 Q2(c) p.181 | Worked point → reason → economic effect chains, followed by independent short practice. |',
        '| One-sided evaluation, no distinct decision, or mirrored repetitions | 2020 P2 Q1(c) pp.146–147; 2023 P1 Q26(c) p.179; 2024 P1 Q24(d) p.178 and P2 Q4(d) p.184 | Balanced case reasoning where demanded; decisions must add a condition or priority, not repeat a credited point. |',
        '| Missing labels, wrong curve or price-control diagram | 2020 P1 Q23(a)(ii) p.144; 2021 P2 Q1(b) p.137; 2022 P2 Q1(b) p.167; 2024 P2 Q1(c) pp.179–180 | Label-and-complete tasks; discriminate a curve shift from a price ceiling/floor on unchanged curves. |',
        '| Wrong direction or a static factor instead of a change | 2022 P2 Q5(a)/(c) pp.173–175; 2023 P2 Q6(b) p.190; 2024 P2 Q1(a) p.179 and Q6(b) p.186 | State increase/decrease explicitly and trace it to the requested price, quantity or income effect. |',
        '| Wrong actor, level or case; copying an excluded factor | 2020 P2 Q3(b)/(c) p.149; 2021 P1 Q25(c) p.136; 2023 P2 Q6(d) p.192; 2024 P2 Q1(a) p.179 | Case-linked explanations, actor checks, national versus individual specialisation, and “other than” drills. |',
        '| Incomplete definitions or confused neighbouring concepts | 2021 P1 Q17–20 p.133; 2022 P1 Q19–24 pp.160–161; 2024 P1 Q12 p.173 and Q22 p.175 | Discrimination cards and short examples that expose the boundary rather than repeating the definition. |',
        '| Missing formula elements, percent signs or magnitude/units | 2021 P1 Q25(a)(i) p.135; 2023 P2 Q6(a) p.190; 2024 P1 Q17 p.174 | Calculation cards with independent checking of ratio, percentage, currency and persons/millions. |', '',
        'The individual source comments remain attached to question evidence. Performance-only comments are not counted as misconceptions. Source defects are not treated as learner beliefs.', '',
        '## 7. Misconceptions', '',
        f"**{v['curated_misconceptions']} curated concept confusions** are saved in curriculum/misconceptions.json, each with syllabus anchors, source evidence and an original discrimination test. They cover, for example, real/disposable income; average/marginal revenue; social/external cost; absolute/comparative advantage; budget/trade balance; production/productivity; natural/total population change; fiscal/monetary policy; transfer earnings/economic rent; public/free goods; and economic/population growth.", '',
        'Unemployment classification is conditional on the stated mechanism. The 2022 tourism case asks for structural rather than seasonal unemployment, while the 2023 economy-wide downturn case is marked cyclical. A resource must not teach “pandemic = one universal type”. Neither listing nor omitting units is promoted into a concept-confusion entry.', '',
        '## 8. Scope and source reliability', '',
        'The syllabus has no explicit subject-content prohibition of the kind found in some other qualifications. Its positive depth limits require simple market situations/calculations/applications. All seven constraints transcribed at step 2 have corresponding reviewed scan entries and 30 must-catch/must-allow controls in curriculum/scope-scan.json. Patterns catch explicit incompatible instructions only; depth still needs semantic review. No bare marginal-cost, comparative-advantage or economic-rent term is banned: this syllabus/report corpus explicitly supports them.', '',
        'Fourteen source-anomaly records are saved in assessment-evidence/source-anomalies.json. Material issues include the displaced 2021 P1 performance comments; 2022 public-good and multinational assertions; the reversed 2022 depreciation/imported-inflation mechanism; inconsistent debt/expected-price statements; tariff/band typos; the malformed 2023 population calculation; and 2023 scale/diminishing-returns conflation. The held QP supplies the printed tariff; inconsistent report suballocations are not invented into a clean grid. The syllabus overrides wrong report content. The 2023 supply diagram and the 2022 currency row were visually checked.', '',
        '## 9. What this means for the plan', '',
        '1. Cover all 28 topics and every decomposed outcome; reserve additional applied practice for market forces, government policy, financial institutions, population/development, employment and costs/conflicts, without using exposure as a content filter.',
        '2. Preserve the syllabus’s A/B/C labels and its per-paper target percentages. Calculated overall targets are A 39%, B 25.5%, C 35.5%; these are derived from the 50/50 paper weights, not a separate printed qualification table.',
        '3. Include short exact retrieval, discrimination, calculations, diagram construction/reading, data analysis, applied causal chains and task-specific extended judgement. Map Bloom separately from the credited AO.',
        '4. Use observed complete command/tariff forms, including prefaced/compound instructions, and original invented Namibian cases. All thirteen syllabus-table verbs occur; additional examined verbs are retained with evidence rather than guessed.',
        '5. Build genuine misconception slots from the curated register. Put command interpretation, exclusions, units and development practice into the appropriate skill tasks instead of labelling every answering fault a misconception.',
        '6. Keep legal/current institutional statements modest and source-specific; do not turn dated report statements into universal law or live facts. Exact numerical examples and diagrams must be newly worked, checked and internally consistent.',
        '7. Carry the missing standalone schemes, 2020 credit-grid gaps, First Proof status, supporting mappings and source anomalies into the plan/handover. No grade prediction or certainty about the next paper is warranted by this corpus.', '',
        'Verification: all 15 source hashes reopened; all ten printed tariff sequences independently reconciled; all 269 extracted performance quotes rechecked on their cited report pages; all 96 exposure rows recomputed; all 30 scope controls passed. See assessment-evidence/source-verification.json. This verifies the mining, not later learner content.', '',
        '**Next YOU checkpoint:** Vitalis reads the paper/command/error summary and confirms that it fits the examination the learners are preparing for. Planning has not started.', '']
(ROOT / 'operations/analysis/6145-nssco-economics-corpus-analysis.md').write_text('\n'.join(out))
print('Corpus analysis written from current evidence.')
