"""Derive measured paper, named-subtopic and practical-skill exposure."""

import collections
import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
SOURCE = WORK / "assessment-evidence/question_parts.json"
OUTPUT = WORK / "curriculum/exam-exposure.json"


def order(identifier):
    tail = identifier.split(":", 1)[1]
    if tail.startswith("C"):
        return (1, int(tail[1:]))
    return (0, *[int(x) for x in tail.split(".")])


def main():
    records = json.loads(SOURCE.read_text())["records"]
    papers = []
    for paper_id in ("1", "2", "3"):
        subset = [row for row in records if row["paper_id"] == paper_id]
        tariffs = collections.Counter(row["mark_tariff"] for row in subset)
        papers.append({
            "paper_id": paper_id,
            "years": sorted({row["year"] for row in subset}),
            "item_or_part_count": len(subset),
            "raw_marks": sum(row["mark_tariff"] for row in subset),
            "tariff_counts": {str(k): tariffs[k] for k in sorted(tariffs)},
        })
    objective_exposure = []
    for objective_id in sorted({i for row in records for i in row["objective_ids"]}, key=order):
        subset = [row for row in records if objective_id in row["objective_ids"]]
        years = sorted({row["year"] for row in subset})
        words = collections.Counter(row["command_word"] for row in subset if row["command_word"])
        objective_exposure.append({
            "objective_id": objective_id,
            "mapping_level": "named syllabus content subtopic" if not objective_id.startswith("syllabus:C") else "syllabus practical AO C criterion",
            "item_or_part_count": len(subset),
            "raw_marks": sum(row["mark_tariff"] for row in subset),
            "years_seen": years,
            "maximum_tariff": max(row["mark_tariff"] for row in subset),
            "command_word_mix": dict(words.most_common()),
            "exposure_class": "recurs_all_six_years" if len(years) == 6 else "recurs_some_years" if len(years) >= 2 else "seen_once",
        })
    out = {
        "status": "revision_in_progress",
        "basis": "All 691 extracted printed items/marked parts from Chemistry 6117 Papers 1–3, 2020–2025.",
        "measured": {"papers": papers, "total_parts": len(records), "total_raw_marks": sum(row["mark_tariff"] for row in records)},
        "objective_exposure": objective_exposure,
        "content_topic_exposure_file": "curriculum/topic-context-exposure.json",
        "limitation": "Content records are mapped to named syllabus subtopics and Paper 3 records to C1–C5, with specific practical skill types in question_parts.json. This is a primary objective per part; mixed-topic secondary objectives and examiner A/B mark allocation remain distinct questions. Content topic shares exclude Paper 3 to avoid counting a practical mark twice.",
        "principle": "Past-paper frequency calibrates emphasis but does not remove syllabus-mandated coverage.",
    }
    OUTPUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    topic_names = {t["topic"]: t["name"] for t in json.loads((WORK / "curriculum/syllabus-facts.json").read_text())["content_outline"]}
    topic_rows = []
    for topic in range(1, 12):
        subset = [row for row in records if row["paper_id"] in ("1", "2") and row["objective_ids"][0].split(":")[1].split(".")[0] == str(topic)]
        p1 = sum(row["mark_tariff"] for row in subset if row["paper_id"] == "1")
        p2 = sum(row["mark_tariff"] for row in subset if row["paper_id"] == "2")
        topic_rows.append({"topic": topic, "name": topic_names[topic], "paper_1_marks": p1, "paper_2_marks": p2,
                           "raw_marks": p1 + p2, "share_percent": round((p1 + p2) / 720 * 100, 1),
                           "years_seen": sorted({row["year"] for row in subset})})
    assert sum(x["raw_marks"] for x in topic_rows) == 720
    (WORK / "curriculum/topic-context-exposure.json").write_text(json.dumps({
        "status": "derived_from_part_level_subtopic_map",
        "basis": "All 565 Paper 1 and Paper 2 items/parts, 720 raw marks; each assigned one primary named content subtopic by reading the assessed chemistry.",
        "topics": topic_rows,
        "paper_3": {"raw_marks": 240, "primary_assessment": "C1–C5 practical criteria", "years_seen": list(range(2020, 2026))},
        "limitation": "Primary content mapping is not an examiner A/B allocation; mixed parts can contain secondary content. Paper 3 skill exposure is in exam-exposure.json.",
    }, indent=2, ensure_ascii=False) + "\n")
    print("Wrote measured paper/tariff, subtopic and practical-skill exposure")


if __name__ == "__main__":
    main()
