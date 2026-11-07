"""Render measured tables into the subject's step-3 analysis."""
import json
from pathlib import Path

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
def read(p):return json.loads((WS/p).read_text())
summary=read('planning/corpus-summary.json')
commands=read('assessment-evidence/command-word-counts.json')['commands']
topics=read('assessment-evidence/topic-mark-shares.json')['topics']
exposure=read('curriculum/exam-exposure.json')['objectives']
manifest=read('assessment-evidence/extraction-manifest.json')
rows=[]
for c in sorted(commands,key=lambda x:(-x['count'],x['word'])):
    if not c['count']:continue
    p=c['per_paper']
    rows.append(f"| {c['word']} | {'yes' if c['in_syllabus_table'] else 'no'} | {c['count']} | {c['modal_tariff']} | {', '.join(map(str,c['tariffs']))} | {p.get('P1',0)} / {p.get('P2',0)} |")
command_table='\n'.join(rows)
topic_table='\n'.join(f"| {r['topic_id']} {r['title']} | {r['parts']} | {r['marks']} | {r['share_percent']:.1f}% | {len(r['series'])} |" for r in sorted(topics,key=lambda x:-x['marks']))
source_table='\n'.join(f"| {y} | 2 | absent | {len(next(r for r in manifest if r['kind']=='ER' and r['year']==y)['pdf_pages'])} |" for y in range(2020,2025))
unprobed='\n'.join(f"- `{r['objective_id']}` — {r['syllabus_text']}" for r in exposure if r['exam_exposure'].startswith('unprobed'))
doc=f'''# Corpus analysis — 6145 NSSCO Economics

Step 3 · 7 November 2026 · Owner Jeremy · Codex. The syllabus was read first, and Jeremy confirmed the AO and paper tables match printed pages 13–15. This analysis describes this subject alone. It is evidence for a future plan, not a plan or a publication verdict.

## 1. The corpus

| Year | Question papers | Standalone mark schemes | Economics report pages used |
|---|---:|---|---:|
{source_table}
| 2025 | absent | absent | 16 (supplementary report only) |

The 2018 NIED syllabus is for implementation in 2019 and first examination in 2020; NIED's senior-secondary listing still links the same-named edition. All five held paper years fall after first implementation. The 2021–2023 paper filenames say First Proof: they are usable provisional evidence, not certified final copies. Combined reports were restricted to Economics 6145, ending before the next subject. The six extracted report sections total **102 PDF pages**. The official 2025 report is cached inside this workspace, not added to the shared `sources/` tree.

Question-paper mining yields **{summary['question_parts']} tariff-bearing parts** from ten papers across five annual series. All Paper 1 totals reconcile to 80, with 40 in each section. Every offered Paper 2 question reconciles to 20. Therefore each Paper 2 offers 120 marks but a candidate attempts 80. The entire offered corpus contains **1,000 marks**, whereas five actual two-paper candidate routes contain 800. Optional marks must not be mistaken for compulsory exposure.

Both layout and raw reading orders were extracted. Four layout-specific question-number issues and the shared instruction for the 2021 ownership subparts were accounted for. Every source path, selected PDF page and checksum is in `assessment-evidence/extraction-manifest.json`. Tables, graphs and incomplete shared stems were checked against their layout counterparts. No question text will be reused in learner material.

**Gaps:** no standalone schemes or 2025 QPs, no grade thresholds, and report numbers sometimes conflict with QPs. Suggested answers and guidance inside reports support selected credit structures; missing standalone schemes do not justify inventing the rest. Full limits: `assessment-evidence/GAPS.md`; source conflicts: `assessment-evidence/source-discrepancies.json`.

## 2. What each paper looks like

**Paper 1:** 2 hours 30 minutes, 80 marks, 50% of qualification. Section A is short answer, all compulsory, and the syllabus assigns it AO A. It includes definitions, short reasons, numerical/formula recall and diagram/data selection, sometimes phrased as Explain or Why. Those surface words do not override the syllabus's section-level AO label. Section B is 40 compulsory marks using economic scenarios, data and extended interpretation/evaluation. In 2020 its two questions split 23/17; later held years split 20/20. Do not assume each data question is invariably 20 marks.

Across Paper 1, 120 of 159 parts carry 1–2 marks. The remaining parts range from 3 to 8 marks. Lower tariffs require precision; the extended parts require context, mechanisms and judgement rather than longer definitions.

**Paper 2:** 2 hours, 80 attempted marks, 50% of qualification. Section A is one compulsory 20-mark structured question; Section B offers five 20-mark questions, of which three are answered. All 30 offered main questions in the corpus total 20. Parts range from 1 to 9 marks; **48 of 112 parts carry seven marks**. There are two nine-mark evaluation parts, not a universal eight-mark discussion format. Diagrams and their explanation form a recurring practical demand.

AO targets remain the syllabus's A/B/C splits, with calculated overall weights 39% / 25.5% / 35.5%. The report sometimes prints Kn, Ap, An and Ev labels; Ap and An map into syllabus AO B. Elsewhere part-level AO focus is a labelled semantic judgement, not an official mark-by-mark split. Bloom level is a separate axis: asking learners to devise enquiries about economic costs can require Create while assessment remains AO C.

## 3. Command words actually used

One primary substantive command or interrogative opening is counted per tariff-bearing part. Introductory Use/Using/With wrappers do not replace the task verb they introduce. Shared Comment instructions are inherited by the two 2021 ownership subparts. Compound task verbs are retained on the evidence record. Interrogatives such as What/Why/How remain observable forms, not silently rewritten as Define/Explain. Modal ties choose the smaller tariff.

| Primary word/form | In syllabus command table? | Parts | Modal marks | Tariffs seen | P1 / P2 |
|---|---|---:|---:|---|---|
{command_table}

All **13** syllabus-table words have a primary occurrence. There are **no listed-but-unobserved table entries** in this window. Notably, List, Name, Consider, Comment, Assess, Examine, Illustrate and Write down occur despite not being entries in the 13-word table. Distinguish, Advise, Indicate, Mention and Show also occur. Draw occurs as an embedded instruction, not the primary opening; it must not be counted as an additional tariff-bearing question. Primary counts sum exactly to 271.

Tariffs are source-specific. For example, Explain spans 2, 3, 4, 6 and 7 marks; Describe spans 1, 2, 3, 4, 6 and 7. Discuss has 4, 6, 7 and 8, and Evaluate has 5, 7, 8 and 9. There is no reliable rule that a word alone implies one AO, one tariff or one answer template. Prompt eligibility and tariff selection must preserve the observed combinations, including paper context.

## 4. What a creditable answer looks like

The report guidance supplies structures, which are paraphrased in nine records in `curriculum/answer-shapes.json`. Twelve selected QP parts link directly to those page-cited examples. The rest do not pretend to have individually transcribed marking points.

- **Precise meaning and requested elements:** short definitions can require more than one element. Identify-and-example tasks separately credit the named concept and the matching contextual example. A correct example does not repair a missing definition.
- **Developed explanation:** make a relevant point, show why/how it works, then connect it to the named agent or outcome. The 2021 report criticises lists where fuller explanation was needed (P2 4(c), PDF 141). The 2025 central-bank guidance explicitly uses developed points (PDF 168). Do not stretch a one-mark list into an analytical answer or collapse a seven-mark mechanism into headings.
- **Diagram plus explanation:** the 2020 minimum-wage guidance separates four diagram marks from three explanation marks (PDF 146). The 2024 uranium-cost guidance likewise separates four application from three analysis marks (PDF 177). Correct axes, labels, equilibrium, direction of change and the economic interpretation all matter. A binding price control is drawn relative to fixed curves, not invented by shifting both curves.
- **Evaluation:** develop the relevant opposing arguments in context. For 2023 P2 2(c), the report uses a 1–3 one-sided band, a 4–6 balanced band and a distinct conclusion mark (PDF 185). The nine-mark 2023 fiscal-policy question uses 1–4 versus 5–8, then a separate conclusion (PDF 183). The 2024 current-account question instead shows a 4/3 or 3/4 split across arguments (PDF 178). Keep these distinctions; a generic seven-mark conclusion allocation would misrepresent several sources.
- **Numeracy:** choose the appropriate relationship, substitute accurately and name the result and its unit. For percentage changes use the original denominator. Elasticity divides the percentage changes without multiplying the final ratio by 100 again. The task wording determines whether an answer, workings, interpretation, or all three are needed.
- **RPI:** choose a representative basket, expenditure weights and base period, collect prices and combine the weighted changes. Explain the index process rather than only defining inflation (2024 P2 3(c), PDF 182).

Some report guidance is internally inconsistent, particularly in 2023. QP tariffs win. Claims about precise marking allocations must cite a consistent local example; report errors are not teaching rules.

## 5. Where the marks fall

Each part has one primary objective selected by reading its demand, not by token matching. There was no token-matched first pass to repair. This gives approximate **offered-mark** shares. Broad contextual numeracy and overlapping demands have **28 explicit mapping flags**. A part's additional concepts are not awarded a second copy of its marks.

| Primary topic | Parts | Offered marks | Share of 1,000 | Annual series |
|---|---:|---:|---:|---:|
{topic_table}

The largest primary shares are Market forces (8.9%), Government economic policies (7.9%) and Population (6.3%). The Population heading includes the syllabus's developed/developing-economy outcomes as well as demographic change; interpret that title using its actual bullet content. Financial institutions and Conflicts each carry 5.4%. None of this permits dropping lower-frequency topics.

The measured exposure file retains 96 syllabus-bullet references: **60 probed high** (a six-mark-or-higher demand or at least three annual series), **26 probed low**, and **10 without a primary assignment**. These are the file's explicit definitions and recompute under the standard's C-39 check. They are not estimates of exam probability. The ten zero-primary references are:

{unprobed}

Several appear within broader multi-part tasks or as supporting skills. In particular, no primary assignment to equilibrium or economies-of-scale illustration does **not** mean those ideas were absent. Step 4 must decompose listed members, preserve all syllabus coverage and avoid treating bullet-level counts as member-level counts.

## 6. How candidates lose marks

The retained error-comment set contains **{summary['report_error_comments']} page-verified comments**. It is an extraction/curation, not an exhaustive census of every sentence or every embedded error clause. Of 271 QP parts, 166 have linked common-error records; supplementary 2025 comments are mapped by meaning and excluded from QP frequency counts.

| Repeated failure | Evidence examples (PDF pages) | Resource response |
|---|---|---|
| Listing without development | 2020 general comments 141/146; 2021 P2 4(c), 141; 2024 P2 2(c), 181; 2025 P2 2(b), 162 | Practise point → reason → economic consequence, scaled to the tariff. |
| One-sided evaluation or missing decision | 2023 general comments 173 and P2 2(c), 185; 2024 general comments 171 and P1 24(d), 178; 2025 P2 4(c), 165–166 | Contrast the two arguments and finish with a justified answer to the actual question; preserve each source's mark allocation. |
| Incorrect diagrams, labels or curve changes | 2020 144/146; 2021 137; 2022 164/167; 2023 188; 2024 179–180 | Include construction, interpretation and diagnostic error tasks. Distinguish a movement, a shift and a price control. |
| Generic answers or copying instead of using the case | 2020 P1 23(c)/(d), 144; 2021 P1 25(c), 136; 2022 P2 5(a)/(c), 173/175; 2023 P2 1(a), 181 | Require the named agent, relevant direction and data; rewrite scenarios with invented Namibian entities. |
| Answering a related question | 2020 household versus national debt, 149; 2023 saving versus borrowing/spending, 186; 2025 free trade versus protection, 167 | Identify the requested actor, policy, direction and outcome before explaining. Keep this distinct from a conceptual misconception. |
| Formula, percentage or unit errors | 2020 P1 23(b)(ii), 144; 2023 P1 25(b), 177; 2025 P1 9, 156 | Provide retrieval of formulas, clean workings and interpretation, with percent signs only where appropriate. |
| Teaching from a textbook rather than the syllabus | Teacher recommendations across reports, including 2020 141 and 2024 178 | Make the complete specified outcomes the coverage floor; support real data interpretation without importing a different qualification's scope. |

## 7. Misconceptions

The register contains **{summary['curated_misconceptions']} distinct conceptual confusions**, each with a source finding, objective reference and discriminating test written in our own words. It includes scarcity/resources versus finished goods; employer associations versus trade unions; collective bargaining as process rather than organisation; real versus disposable income; average versus marginal revenue; forward versus backward integration; economies versus diseconomies; demand versus supply shifters; budget versus trade balances; trade versus payments balances; public/private ownership sectors versus production sectors; absolute versus comparative advantage; fiscal versus monetary policy; real income versus income per person; social versus external costs; public versus free goods; economic versus population growth; transfer earnings versus transfer payments; and a public limited company versus a public corporation.

Generic listing, weak development, missing units, missing context and one-sided answers are recorded as answering failures, not padded into the misconception count. A diagnostic must make the learner choose between the confused ideas; restating a definition is insufficient. One provisional capital-intensity entry was dropped because its source supports a missing comparison rather than the specific false belief initially proposed.

## 8. Scope

The syllabus contains no explicit blanket content exclusions. Positive limits still bind: elementary theory/basic data, simple market situations, simple elasticity/RPI calculations, simple applications of trade advantage and simple living-standard measures. They are preserved as manual depth constraints in `curriculum/scope-scan.json`.

Five explicitly labelled planner-judgement regex boundaries catch selected advanced statistical, consumer-choice, trade, macroeconomic and investment-appraisal constructs. Their ten catch/allow examples pass. These are not falsely attributed as verbatim syllabus prohibitions, and regex alone cannot certify depth.

Do **not** blanket-ban comparative advantage, transfer earnings/economic rent or marginal analysis of profit maximisation. The first two are explicit learning content, and the 2021 profit-maximisation suggested answer includes MC=MR (PDF 140). Conversely, glossary entries for income/cross elasticity do not by themselves commission independent units. Concepts such as e-commerce, value added, WTO and formal/informal activity occur as supporting corpus content and require careful placement rather than a new unsourced topic.

Reports must be read critically. Distinguish long-run economies of scale from short-run diminishing returns even where report guidance blurs them. Explain whether a pandemic shock reduces total demand or causes structural mismatch using the specific scenario; do not memorise one unemployment classification for all pandemic questions. New examples must be internally consistent and use invented businesses, N$ and British English.

## 9. What this means for the plan

1. Decompose all 96 specific-objective bullets into the complete registry, including every listed member. Preserve the link to mining IDs and regenerate exposure if IDs change. No count-based removal of content.
2. Plan both precise short retrieval and longer contextual mechanisms, diagram work and evaluation. Knowledge-only flashcards cannot meet the calculated 35.5% overall evaluation share.
3. Use observed command/tariff/paper combinations, not the command table alone. First substantive instruction counts must remain separate from embedded verbs and interrogative forms.
4. Allocate a real discrimination task for each of the 32 curated confusions, alongside answer-development and data-use practice. Do not turn every weak-answer comment into a MISCON slot.
5. Preserve paper-specific answer structures and source-specific evaluation bands. Never add a conclusion mark above the QP total.
6. Build clean, original examples for elasticity, percentage changes, RPI, exchange rates, costs, income per person, opportunity cost and simple comparative advantage. Scenarios and answers must not reproduce the sources.
7. Carry the standalone-scheme and final-copy limitations visibly. Expand direct creditworthy-point mining where the plan depends on more than these selected structures; label all extrapolation as judgement.
8. Keep learner-facing material free of exam-priority claims and examiner wording. These are internal planning findings.

Verification: `planning/corpus-verification.json` reports PASS for reconciliation, independent command counts, source quotations, scope examples and exposure recomputation across all 96 references. The full publication suite has not run because no authored topic exists. **Next checkpoint: Jeremy reads sections 2, 3 and 6 (summarised in chat). Step 4 begins only after that response.**
'''
(ROOT/'operations/analysis/6145-nssco-economics-corpus-analysis.md').write_text(doc)
print('Rendered analysis:',len(doc.split()),'words')
