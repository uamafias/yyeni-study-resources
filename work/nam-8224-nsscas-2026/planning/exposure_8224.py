#!/usr/bin/env python3
"""Compute curriculum/exam-exposure.json from assessment-evidence/assessment_evidence.json (derived, never typed)."""
import json, os, collections, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(HERE)
ev = json.load(open(os.path.join(WS, "assessment-evidence", "assessment_evidence.json")))["records"]
bullets = json.load(open(os.path.join(HERE, "syllabus_bullets.json")))
agg = {}
for r in ev:
    for oid in r["objective_ids"]:
        a = agg.setdefault(oid, {"parts": 0, "series": set(), "max": 0, "cw": collections.Counter(), "src": collections.Counter()})
        a["parts"] += 1; a["series"].add(r.get("exam_series")); a["max"] = max(a["max"], r.get("mark_tariff") or 0)
        if r.get("command_word"): a["cw"][r["command_word"]] += 1
        a["src"]["%s%s" % ("ER-" if r["evidence_type"] == "examiner_report" else "", r["paper_id"])] += 1
HI_MARKS, HI_SERIES, LO_MARKS = 4, 3, 3
objs = []
for b in bullets:
    a = agg.get(b["objective_id"])
    if not a:
        klass = "unprobed_2020_2025"; e = {"question_parts_naming_it": 0, "distinct_series": 0, "max_mark_tariff": 0, "command_words_observed": {}, "by_source": {}}
    else:
        if a["max"] >= HI_MARKS or len(a["series"]) >= HI_SERIES: klass = "probed_high"
        else: klass = "probed_low"
        e = {"question_parts_naming_it": a["parts"], "distinct_series": len(a["series"]), "max_mark_tariff": a["max"],
             "command_words_observed": dict(a["cw"]), "by_source": dict(a["src"]), "series": sorted(s for s in a["series"] if s)}
    objs.append({"objective_id": b["objective_id"], "learner_objective": b["text"], "parent_bullet": b["unit"], "exam_exposure": klass,
                 "evidence": e, "item_allocation": None, "required_subtypes": [], "review_sets": []})
out = {
    "exposure_id": "EXPOSURE-NAM-8224-NSSCAS-2026",
    "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "evidence_window": "12 question papers (Papers 1, 2 and 3) 2021-2024 and the 2025 examiner report: %d evidence records. 2021-2023 papers are proofs. No mark schemes exist; 2021-2024 examiner reports do not exist." % len(ev),
    "principle": "RS-05: past-paper frequency may calibrate emphasis but MUST NOT remove or weaken syllabus-mandated coverage. Exposure is evidence metadata, never a priority ranking.",
    "why_silence_is_weak_evidence": "213 syllabus objectives against about 160 Paper 1 questions and about 60 Paper 2 marks a year: most objectives cannot appear in any year. Four years of silence is the default state, not a signal.",
    "method": "Each question part was mapped to syllabus objectives by reading its meaning (not by word matching) in step 3; the 2025 report records are mapped by inference from examiner comments because the 2025 papers are not held. Figures are computed from the evidence records by planning/exposure_8224.py. Roughly 90 percent of a 30-record spot-check was clearly right, 2-3 arguable, none clearly wrong. 76 of 475 records depend on a diagram the miner did not always view.",
    "classes": {
        "probed_high": "Named in an evidence record and either reaching %d marks or more or named in %d or more distinct series." % (HI_MARKS, HI_SERIES),
        "probed_low": "Named in an evidence record, capped at %d marks or fewer, and named in fewer than %d distinct series." % (LO_MARKS, HI_SERIES),
        "unprobed_2020_2025": "Not named by any evidence record in the 2021-2025 window (the key keeps the standard's name; the NSSCAS window starts in 2021). Coverage floor applies; never down-weighted below it.",
        "class_note": "Series are the four paper years 2021-2024 plus the 2025 examiner report as a fifth. A 2025 report record counts as a series because it is the only examiner evidence held."
    },
    "unmatched_parts": sum(1 for r in ev if r["objective_ids"] == ["OBJ-8224-UNMAPPED"]),
    "status": "measured",
    "objectives": objs,
}
json.dump(out, open(os.path.join(WS, "curriculum", "exam-exposure.json"), "w"), indent=1, ensure_ascii=False)
c = collections.Counter(o["exam_exposure"] for o in objs)
print("objectives", len(objs), dict(c), "| unmatched records", out["unmatched_parts"])
# command words used in past papers
cw = collections.defaultdict(lambda: collections.Counter())
for r in ev:
    if r["evidence_type"] == "past_paper" and r["paper_id"] in ("P2", "P3") and r.get("command_word"):
        cw[r["command_word"]][r["mark_tariff"]] += 1
print("\nPAST-PAPER P2/P3 command words (count | tariffs):")
for w, t in sorted(cw.items(), key=lambda x: -sum(x[1].values())):
    print(f"  {w:18} {sum(t.values()):3} | {dict(sorted(t.items()))}")
