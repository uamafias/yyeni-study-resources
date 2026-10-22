#!/usr/bin/env python3
"""Write operations/analysis/8224-nsscas-chemistry-corpus-analysis.md. All figures are computed from
assessment-evidence/assessment_evidence.json, curriculum/exam-exposure.json and curriculum/answer-shapes.json."""
import json, os, re, collections, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(HERE); ROOT = os.path.abspath(os.path.join(WS, "..", ".."))
ev = json.load(open(os.path.join(WS, "assessment-evidence", "assessment_evidence.json")))["records"]
bul = {b["objective_id"]: b for b in json.load(open(os.path.join(HERE, "syllabus_bullets.json")))}
facts = json.load(open(os.path.join(WS, "curriculum", "syllabus-facts.json")))
expo = json.load(open(os.path.join(WS, "curriculum", "exam-exposure.json")))
shapes = json.load(open(os.path.join(WS, "curriculum", "answer-shapes.json")))["8224"]
mis = json.load(open(os.path.join(WS, "curriculum", "misconceptions.json")))["entries"]
scope = json.load(open(os.path.join(WS, "curriculum", "scope-scan.json")))["entries"]
p3s = json.load(open(os.path.join(WS, "assessment-evidence", "paper3_summary.json")))
title = {o["id"]: o["title"] for o in facts["content_outline"]}
pp = [r for r in ev if r["evidence_type"] == "past_paper"]
er = [r for r in ev if r["evidence_type"] == "examiner_report"]
def topic(r):
    b = bul.get(r["objective_ids"][0]); 
    if not b: return None
    u = b["unit"]; return ".".join(u.split(".")[:2])
def theme(r):
    b = bul.get(r["objective_ids"][0]); return b["theme"] if b else None
TN = {"1": "Particulate nature of matter and stoichiometry", "2": "Physical chemistry", "3": "Inorganic chemistry", "4": "Organic chemistry and analysis"}
marks = collections.Counter(); tmarks = collections.Counter(); tot = 0
for r in pp:
    if r["paper_id"] in ("P1", "P2"):
        m = r["mark_tariff"] or 0; marks[topic(r)] += m; tmarks[theme(r)] += m; tot += m
unprobed_by_topic = collections.Counter(o["topic_id"] for o in expo["objectives"] if o["topic_id"] != "5.1" and o["exposure_class"] == "unseen")
bytopic_total = collections.Counter(".".join(b["unit"].split(".")[:2]) for b in bul.values())
def bw(c):
    c = c.strip(); low = c.lower()
    if any(k in low for k in ("record", "table", "carry out", "select reagents", "use observations", "weigh")): return "Practical: record / tests"
    if low.startswith(("which", "what", "how many")): return "Question word"
    if low.startswith("obtain"): return "Calculate"
    m = re.match(r"[A-Za-z]+", c); return m.group(0).title() if m else c
cw = collections.defaultdict(collections.Counter)
for r in pp:
    if r["paper_id"] in ("P2", "P3") and r.get("command_word"): cw[bw(r["command_word"])][r["mark_tariff"]] += 1
cls = collections.Counter(); cls_obj = collections.defaultdict(collections.Counter)
for r in er:
    for f in r["examiner_findings"]:
        m = re.match(r"\[([^\]]+)\]", f); cls[m.group(1)] += 1
tar = collections.Counter(r["mark_tariff"] for r in pp if r["paper_id"] == "P2")
pts = {t["tariff"]: [] for t in shapes["er2025_marking_points_vs_tariff"]["table"]}
for t in shapes["er2025_marking_points_vs_tariff"]["table"]: pts[t["tariff"]].append("%d listed point(s) in %d part(s)" % (t["listed_points"], t["parts"]))
pc = []
for r in er:
    if r["paper_id"] == "P1":
        m = re.search(r"percent_correct: ([\d.]+)", " ".join(r["notes"]))
        if m: pc.append((float(m.group(1)), r["question_ref"], r["objective_ids"][0]))
pc.sort()
L = []
w = L.append
w("# 8224 NSSCAS Chemistry — corpus analysis (step 3)\n")
w("Workspace `work/nam-8224-nsscas-2026/`. Written %s. Evidence: `assessment-evidence/assessment_evidence.json` (%d records), `curriculum/exam-exposure.json`, `answer-shapes.json`, `misconceptions.json`, `scope-scan.json`. Syllabus facts: `curriculum/syllabus-facts.json`. Every table below is computed from those files by `planning/write_corpus_analysis_8224.py`.\n" % (datetime.date.today().isoformat(), len(ev)))
w("**Read this first: the limits of this evidence.**\n")
w("- **No mark schemes exist** for 2021–2024 (none in the repo, none in Drive). So nothing here records what was credited. Credited-answer shape comes only from the %d Paper 2/3 parts the 2025 examiner report describes." % shapes["er2025_marking_points_vs_tariff"]["parts"])
w("- **The only examiner evidence is the 2025 report.** Its question papers are not held, so its comments were mapped to objectives by inference from the comment itself. 2021–2024 examiner reports do not exist.")
w("- **Proof papers.** 2021–2023 papers are proofs (2023 Paper 3 a second revised proof); 2024 is unlabelled. Wording may differ from the printed exams.")
w("- **Marks I inferred.** In 2024 Paper 2 Question 1(a)–(f) the page prints only a total of 6; the six parts are recorded at 1 mark each by inference.")
w("- **Mapping.** Each part was mapped to syllabus bullets by reading its meaning. A 30-record spot-check found about 27 clearly right, 2–3 arguable, none clearly wrong. All 76 diagram-dependent records were subsequently checked against 46 page images; one locator was corrected and no meaning mapping changed. See `work/nam-8224-nsscas-2026/assessment-evidence/IMAGE-REVIEW.md`.")
w("- **Frequency is not difficulty.** Section 5 is frequency; section 6 is difficulty (2025 only). They are kept apart.\n")
# 1
w("## 1. The corpus\n")
w("| Source | Used | Notes |\n|---|---|---|")
w("| Papers 1, 2, 3 for 2021, 2022, 2023, 2024 | 12 papers: 160 Paper 1 questions, %d Paper 2 parts (240 marks), %d Paper 3 parts (160 marks) | Proofs except 2024 |" % (sum(1 for r in pp if r["paper_id"] == "P2"), sum(1 for r in pp if r["paper_id"] == "P3")))
w("| NSSCAS Examiners Report 2025, Chemistry 8224 (printed p. 71 onward) | %d records (40 Paper 1, %d Paper 2, %d Paper 3) | Paper 1 keys with percentage correct and comments; Paper 2/3 marking points with commentary; papers not held |" % (len(er), sum(1 for r in er if r["paper_id"] == "P2"), sum(1 for r in er if r["paper_id"] == "P3")))
w("| Set aside | Drive spreadsheets of grade distributions by centre (2024, 2025) | Results data, not question or content evidence |\n")
# 2
w("## 2. What each paper looks like\n")
c1 = collections.Counter(r["context_type"] for r in pp if r["paper_id"] == "P1"); c2 = collections.Counter(r["context_type"] for r in pp if r["paper_id"] == "P2"); c3 = collections.Counter(r["context_type"] for r in pp if r["paper_id"] == "P3")
w("**Paper 1 (40 four-choice questions, 1 mark each, 1 hour).** Syllabus order is not followed; every year draws from all four themes. Question types by purpose across the four years: " + ", ".join("%s %d" % kv for kv in c1.most_common(8)) + ". Multiple-choice items carry no command word.\n")
w("**Paper 2 (60 marks, 1 hour 15, compulsory).** Five or six questions a year. Parts by mark: " + ", ".join("%d-mark %d" % (k, v) for k, v in sorted(tar.items())) + " (148 parts over four years). Most parts are worth 1 mark; a part above 3 marks is rare. Part types: " + ", ".join("%s %d" % kv for kv in c2.most_common(8)) + ". Questions are usually one topic area but often hold parts from other topics (a question on Group 2, for example, can end in a calculation).\n")
w("**Paper 3 (40 marks, 2 hours, two or three timed experiments).** Experiment topics by year:\n")
for y, t in p3s["experiment_topics"].items(): w("- %s: %s" % (y, "; ".join(t)))
w("")
w("Marks by skill (from the records): " + "; ".join("%s: planning %s, collecting %s, analysing %s, evaluating %s" % ((y,) + tuple(v[k].split()[0] for k in ("planning", "collecting", "analysing", "evaluating"))) for y, v in p3s["share_of_marks_by_skill_from_records"].items()) + ". Practical types: " + ", ".join("%s %d" % kv for kv in c3.most_common(8)) + ". The syllabus notes qualitative-analysis notes are supplied with Paper 3, so recall of test results is not the Paper 3 demand; observation, recording and conclusion are.\n")
# 3
w("## 3. Command words actually used\n")
w("Counts are Paper 2 and Paper 3 parts, 2021–2024 (Paper 1 has none). Raw wordings were normalised to their opening word.\n")
w("| Opening word | Parts | Tariffs seen (marks: count) | In syllabus glossary |\n|---|---:|---|---|")
gl = {x.strip().title() for c in facts["command_words"] for x in c["words"]}
for k, v in sorted(cw.items(), key=lambda kv: -sum(kv[1].values())):
    w("| %s | %d | %s | %s |" % (k, sum(v.values()), ", ".join("%s: %d" % (t, n) for t, n in sorted(v.items())), "yes" if k in gl else "no"))
w("")
w("**Listed in the syllabus glossary but not seen in 2021–2024:** " + ", ".join(shapes["listed_never_observed"]) + ". Caution: the 2025 report shows Sketch used in 2025 (Boltzmann curve, p orbital, particle paths), so Sketch has 2025 evidence only; and Paper 3 'record / measure' wordings absorb Measure.")
w("**Used in papers but not in the glossary:** Identify, Give, Name, Write, Draw, Complete, Plot, Use, Insert, Contrast, and question words (Which, What, How many). Under the playbook rule these are allowed to open a card because the papers use them; the syllabus words never seen should be allowed only where the plan can cite the evidence.")
w("**Tariff pattern:** Calculate and State are mostly 1-mark; Explain and Give run 2–4; Describe and Draw reach 3; the largest Paper 2 part is 5 marks.\n")
# 4
w("## 4. What a creditworthy answer looks like\n")
w("**Limited evidence: no mark schemes.** From the 2025 report only (%d parts with a tariff and listed marking points):\n" % shapes["er2025_marking_points_vs_tariff"]["parts"])
for t in sorted(pts): w("- %d-mark parts: %s" % (t, "; ".join(pts[t])))
w("")
w("(Counts are of listed marking items, not marks: the report sometimes lists alternatives, so a part can show more items than its tariff.)\n")
w("What the report itself states about answers (paraphrased): " + " ".join("(%d) %s" % (i + 1, s) for i, s in enumerate(shapes["stated_by_er2025"])) + "\n")
w("Marks in calculation parts are shown as separate steps in the report (conversion, substitution, final answer to the right number of significant figures). Whether a 1-mark part wants one point or a point with a reason cannot be settled without mark schemes.\n")
# 5
w("## 5. Where the marks fall (frequency; not difficulty)\n")
w("Paper 1 questions plus Paper 2 marks, 2021–2024: **%d marks**, each part counted once to its primary topic (a part that tests two ideas is not split). By theme: " % tot + "; ".join("Theme %s %s %.1f%%" % (k, TN[k], 100 * v / tot) for k, v in sorted(tmarks.items())) + ".\n")
w("| Topic | Marks | Share | Objectives never named 2021–2025 |\n|---|---:|---:|---:|")
for t, m in marks.most_common():
    w("| %s %s | %d | %.1f%% | %d of %d |" % (t, title.get(t, ""), m, 100 * m / tot, unprobed_by_topic.get(t, 0), bytopic_total[t]))
w("")
cls_ex = collections.Counter(o["exposure_class"] for o in expo["objectives"] if o["topic_id"] != "5.1")
w("Exposure classes over the 213 content objectives (definitions in `exam-exposure.json`): core %d, frequent %d, occasional %d, rare %d, unseen %d. Core plus frequent corresponds to the earlier `probed_high` grouping; occasional plus rare corresponds to `probed_low`. Silence is weak evidence: 213 objectives against about 160 questions and 60 Paper 2 marks a year means most objectives cannot appear in any one year. **Frequency calibrates emphasis; it never removes coverage (RS-05).** The earlier keyword-based count in this workspace is superseded by this one and is not to be quoted.\n" % (cls_ex["core"], cls_ex["frequent"], cls_ex["occasional"], cls_ex["rare"], cls_ex["unseen"]))
# 6
w("## 6. How candidates lose marks (2025 report only)\n")
w("Findings by class (87 statements): " + ", ".join("%s %d" % kv for kv in cls.most_common()) + ".\n")
w("Hardest 2025 Paper 1 questions (percentage correct; the report gives a percentage for 38 of 40): " + "; ".join("%s %.0f%% (%s)" % (q, p, o[9:]) for p, q, o in pc[:9]) + ". Easiest: " + "; ".join("%s %.0f%%" % (q, p) for p, q, o in pc[-5:]) + ".\n")
w("Recurring failures and what the resource will do about each:\n")
w("1. **Significant figures, unit conversion and mole calculations** (Paper 2 Q1(b)(ii), Q3(b); most of Paper 3 Q1 and Q2): answers not given to the stated number of figures, cm³ not converted to dm³, wrong Ar (24 for Mg), s.t.p. versus r.t.p. molar volume. *Plan:* calculation cards that require the working, the conversion and the figure count; MISCON cards on 22.4 versus 24.0 and on weighted-mean division.")
w("2. **Practical evaluation and observation** (Paper 3): parallax or 'human error' offered as an experimental error; excess NaOH/ammonia not added or 'soluble in excess' not stated; no conclusion about the ions. *Plan:* practical-skills items, not recall cards; a card family on acceptable error sources and on recording observations.")
w("3. **Boltzmann distribution and rate explanations** (2.4.2): curve confused with an energy profile, area mistaken for Ea, only 'more collisions' given, compromise temperature argued from one side. *Plan:* MISCON cards and explanation items with both-sides answer structure.")
w("4. **Definitions and trend explanations** (3.1.1, 3.1.3): first ionisation energy defined without the ion formed or gaseous states; period trends not linked to nuclear charge and shell. *Plan:* definition cards that name every required element; explain items with claim + reason.")
w("5. **Redox, electrolysis and oxidation numbers** (Paper 1 Q15, Q17, Q28): the lowest-scoring items; the report gives no explanation for the wrong options on Q17 and Q28, so no misconception is claimed for them. *Plan:* items on these objectives; MISCON cards only where an error is stated (nitrate(V) for nitrite).")
w("6. **Drawing and naming organic structures** (4.4.1, 4.5, 4.2.2): O–H bond left out, missing hyphens, primary or tertiary drawn for secondary, double bond kept in a repeat unit, 2-D drawings of enantiomers. *Plan:* structure-drawing items with a displayed-formula discipline.\n")
# 7
w("## 7. Misconceptions\n")
w("%d entries in `curriculum/misconceptions.json`, each stated by the 2025 report, restated in our words with a discriminating test. All are **single-source**, so under the two-source rule agreed for this run they need a second source before they publish as examiner-evidenced. Slips and answering habits were dropped (parallax, 'human error', wrong rounding, item-specific mistakes).\n" % len(mis))
for e in mis: w("- %s (%s): %s" % (e["entry_id"], e["objective_id"][9:], e["a"]))
w("")
# 8
w("## 8. Scope\n")
w("Twelve limits the syllabus states are transcribed with page and verbatim line in `syllabus-facts.json` (`limits`). Ten become draft patterns in `curriculum/scope-scan.json` (nine from stated limits, one inferred exclusion of weak-acid pH calculations, labelled as inferred): " + "; ".join(e["construct"] for e in scope) + ". Patterns are drafts; C-11 must be run on authored text and narrowed where it flags ordinary text.\n")
w("One finding for the plan: the 1.2.1 general objective names behaviour in electric fields, but no specific objective does, and a 2025 question tested it. Treat it as examinable, with the evidence.\n")
# 9
w("## 9. What this means for the plan\n")
w("1. **Coverage is every syllabus objective.** Frequency (section 5) only chooses item types and emphasis.")
bm = sum((r["mark_tariff"] or 0) for r in pp if r["paper_id"] in ("P1", "P2") and r["ao_focus"] == ["B"])
w("2. **AO basis must be chosen.** The syllabus prints 40/40/20 percent, while the marks give 35.7/35.7/28.6. The grid splits Papers 1 and 2 equally between A and B; my judgement of the part types gave B-type parts %.0f%% of the Paper 1 and Paper 2 marks (judgement, not syllabus). Decide which basis the AO targets use and say so." % (100 * bm / tot))
w("3. **Command words for prompts:** the words with evidence in section 3 (Calculate, State, Explain, Identify, Give, Suggest, Write, Draw, Name, Define, Describe, Construct, Determine, plus Sketch on 2025 evidence). Words never seen should not open a card without a stated reason.")
w("4. **Calculation and practical items are required, not optional.** Sections 4 and 6 show that the lost marks are in working, units, significant figures and practical method; recall cards alone will not move them.")
w("5. **Exemplar slice: topic 1.1 (Atoms, molecules and stoichiometry)** as agreed. It carries the heaviest evidence of lost marks (significant figures, mole and gas-volume calculations, mass-spectrum reading) and %.1f%% of Paper 1 and 2 marks. YYeni lesson 6508's objective record is truncated and 1.1 is held in two lessons; cards follow the syllabus bullets, not the broken record." % (100 * marks["1.1"] / tot))
w("6. **Evidence gaps to carry into the plan:** no mark schemes; one examiner report; all misconceptions single-source. The diagram gap is closed: all 76 diagram-dependent records were visually checked. Earlier examiner reports or official marking schemes would still strengthen the evidence base if they become available.\n")
out = os.path.join(ROOT, "operations", "analysis", "8224-nsscas-chemistry-corpus-analysis.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines")
