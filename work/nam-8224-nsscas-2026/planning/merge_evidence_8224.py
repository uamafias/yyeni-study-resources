#!/usr/bin/env python3
"""Merge the miners' raw evidence files into assessment-evidence/assessment_evidence.json and check them.
Raw miner outputs are kept unchanged in assessment-evidence/raw/ for provenance."""
import json, os, re, glob, collections, jsonschema
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(WS, "..", ".."))
RAW = os.path.join(WS, "assessment-evidence", "raw")
SCHEMA = json.load(open(os.path.join(ROOT, "standard/v0.2.0-draft/schemas/assessment_evidence.schema.json")))
bullets = json.load(open(os.path.join(HERE, "syllabus_bullets.json")))
valid_ids = {b["objective_id"] for b in bullets} | {"OBJ-8224-UNMAPPED"}
recs, p3sum = [], None
for f in ["2021_P12", "2022_P12", "2023_P12", "2024_P12", "P3_2021_2024", "ER2025"]:
    d = json.load(open(os.path.join(RAW, f + ".json")))
    for r in d:
        if "paper3_summary" in r: p3sum = r["paper3_summary"]; continue
        recs.append(r)
problems = []
ids = collections.Counter(r["evidence_id"] for r in recs)
problems += ["duplicate id %s" % k for k, v in ids.items() if v > 1]
for r in recs:
    for o in r["objective_ids"]:
        if o not in valid_ids: problems.append("bad objective %s in %s" % (o, r["evidence_id"]))
    if r["evidence_type"] == "past_paper" and (r["creditworthy_points"] or r["examiner_findings"] or r["common_errors"] or r["strong_response_features"]):
        problems.append("past paper record with invented evidence: %s" % r["evidence_id"])
doc = {"map_id": "EVIDENCE-NAM-8224-NSSCAS-2026", "status": "partial", "records": recs}
for e in jsonschema.Draft202012Validator(SCHEMA).iter_errors(doc):
    problems.append("schema: %s %s" % (list(e.path)[:3], e.message[:100]))
# marks
tot = collections.defaultdict(int); cnt = collections.Counter()
for r in recs:
    if r["evidence_type"] != "past_paper": continue
    tot[(r["year"], r["paper_id"])] += r["mark_tariff"] or 0; cnt[(r["year"], r["paper_id"])] += 1
expect = {"P1": 40, "P2": 60, "P3": 40}
for (y, p), m in sorted(tot.items()):
    ok = m == expect[p]
    print(y, p, "records", cnt[(y, p)], "marks", m, "OK" if ok else "EXPECTED %d" % expect[p])
    if not ok: problems.append("marks %s %s = %s" % (y, p, m))
er = [r for r in recs if r["evidence_type"] == "examiner_report"]
print("2025 report records:", len(er), "| past-paper records:", len(recs) - len(er))
print("UNMAPPED records:", sum(1 for r in recs if r["objective_ids"] == ["OBJ-8224-UNMAPPED"]), "(past-paper:", sum(1 for r in recs if r["objective_ids"] == ["OBJ-8224-UNMAPPED"] and r["evidence_type"] == "past_paper"), ")")
conf = collections.Counter(); graphic = 0
for r in recs:
    n = " ".join(r["notes"])
    m = re.search(r"confidence=(high|medium|low)", n); conf[m.group(1) if m else "none"] += 1
    if re.search(r"needs_graphic: yes", n): graphic += 1
print("confidence:", dict(conf), "| needs_graphic yes:", graphic)
print("PROBLEMS:", len(problems)); [print(" ", p) for p in problems[:25]]
if not problems:
    json.dump(doc, open(os.path.join(WS, "assessment-evidence", "assessment_evidence.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(p3sum, open(os.path.join(WS, "assessment-evidence", "paper3_summary.json"), "w"), indent=1, ensure_ascii=False)
    print("wrote assessment_evidence.json,", len(recs), "records")
