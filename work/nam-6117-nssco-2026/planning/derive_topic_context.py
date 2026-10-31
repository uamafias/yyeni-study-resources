"""Derive an auditable primary-topic context table from paper items.

Paper 1 items were read individually. Paper 2 main questions were read in
context; mixed questions have marked-part overrides below. Paper 3 is analysed
separately as practical assessment and is not forced into content mark shares.
These are contextual topics, not a claim about the examiner's AO allocation.
"""

import collections
import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

P1_RUNS = {
    2020: [(6, 2), (7, 9), (11, 2), (14, 3), (19, 4), (21, 5), (27, 6), (29, 7), (30, 8), (33, 9), (37, 10), (40, 11)],
    2021: [(3, 1), (13, 2), (17, 3), (18, 4), (21, 5), (24, 6), (27, 7), (28, 8), (29, 9), (34, 10), (40, 11)],
    2022: [(1, 2), (2, 1), (12, 2), (14, 3), (15, 4), (16, 5), (19, 6), (20, 2), (21, 6), (22, 9), (25, 7), (27, 9), (32, 10), (40, 11)],
    2023: [(3, 1), (14, 2), (17, 3), (18, 7), (20, 4), (21, 5), (22, 9), (24, 6), (26, 7), (27, 8), (29, 9), (34, 10), (40, 11)],
    2024: [(3, 1), (11, 2), (12, 3), (15, 4), (17, 5), (23, 6), (25, 7), (27, 8), (29, 9), (35, 10), (40, 11)],
    2025: [(3, 1), (11, 2), (12, 3), (14, 4), (15, 5), (21, 6), (24, 7), (26, 8), (30, 9), (37, 10), (40, 11)],
}

P2_MAIN = {
    2020: [2, 2, 4, 5, 7, 9, 10, 11],
    2021: [2, 2, 7, 6, 2, 9, 10, 11],
    2022: [2, 5, 7, 4, 6, 9, 10, 11],
    2023: [2, 2, 5, 6, 6, 9, 10, 11],
    2024: [2, 2, 6, 7, 9, 10, 11],
    2025: [2, 7, 6, 5, 9, 3, 10, 11],
}

P3_CONTEXT = {
    2020: [1, 7, 8, 6],
    2021: [1, 6, 8, 6],
    2022: [7, 6, 7, 1],
    2023: [8, 6, 8, 6],
    2024: [1, 1, 6, 8, 6],
    2025: [1, 6, 8, 9],
}

# Overrides are (year, main question, marked part): primary topic. These are
# chemistry judgements on parts within mixed main questions, not token matches.
OVERRIDE = {
    (2020, 1, 3): 8, (2020, 1, 5): 3, (2020, 1, 6): 3,
    (2020, 1, 8): 3, (2020, 1, 9): 3, (2020, 1, 10): 3,
    (2020, 4, 3): 6, (2020, 4, 4): 6, (2020, 4, 5): 6,
    (2020, 5, 6): 4, (2020, 5, 7): 8,
    (2020, 6, 1): 9, (2020, 6, 2): 9, (2020, 6, 4): 9,
    (2020, 6, 5): 9, (2020, 6, 6): 9,
    (2021, 1, 1): 5, (2021, 3, 1): 7,
    (2021, 3, 2): 7, (2021, 3, 3): 4,
    (2022, 4, 1): 7,
    (2023, 4, 1): 1,
    (2024, 2, 4): 5, (2024, 2, 5): 5, (2024, 2, 6): 5,
    (2024, 3, 1): 2, (2024, 3, 3): 6, (2024, 3, 7): 11,
    (2024, 3, 8): 4, (2024, 3, 9): 11,
    (2024, 4, 1): 7, (2024, 4, 2): 7,
    (2024, 5, 11): 6,
    (2024, 7, 2): 1,
    (2025, 1, 8): 2,
    (2025, 2, 6): 7, (2025, 2, 7): 4, (2025, 2, 8): 4, (2025, 2, 9): 4,
    (2025, 3, 5): 6, (2025, 3, 6): 6, (2025, 3, 7): 11,
    (2025, 4, 1): 2, (2025, 4, 6): 2, (2025, 4, 7): 2, (2025, 4, 8): 2,
    (2025, 5, 4): 6,
}


def topic_for(row):
    year = row["year"]
    paper = row["paper_id"]
    q = int(re.search(r"Q(\d+)", row["question_ref"]).group(1))
    if paper == "1":
        return next(topic for end, topic in P1_RUNS[year] if q <= end)
    if paper == "2":
        part = int(re.search(r"marked part (\d+)", row["question_ref"]).group(1))
        return OVERRIDE.get((year, q, part), P2_MAIN[year][q - 1])
    return P3_CONTEXT[year][q - 1]


def main():
    rows = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    topics = json.loads((WORK / "curriculum/syllabus-facts.json").read_text())["content_outline"]
    names = {t["topic"]: t["name"] for t in topics}
    tally = collections.Counter()
    appearances = collections.defaultdict(set)
    by_paper = collections.defaultdict(lambda: collections.Counter())
    for row in rows:
        topic = topic_for(row)
        row["context_topic_id"] = f"syllabus:{topic}"
        row["notes"] = [note for note in row["notes"] if "await" not in note.lower() and "Do not infer objective IDs" not in note]
        if row["paper_id"] == "3":
            row["objective_ids"] = ["syllabus:1.2"]
            row["context_type"] = "practical assessment with chemistry topic context"
            row["mapping_method"] = "Read practical task and chemistry context; procedural objective 1.2 is primary. Context topic is recorded separately."
            row["mapping_confidence"] = "medium"
            continue
        row["objective_ids"] = [f"syllabus:{topic}"]
        row["context_type"] = "four-option multiple choice" if row["paper_id"] == "1" else "structured or free-response marked part"
        row["mapping_method"] = "Read Paper 1 item" if row["paper_id"] == "1" else "Read main question and marked part in chemistry context; see explicit mixed-question overrides"
        row["mapping_confidence"] = "high" if row["paper_id"] == "1" else "medium"
        key = (row["year"], topic)
        tally[topic] += row["mark_tariff"]
        appearances[topic].add(row["year"])
        by_paper[row["paper_id"]][topic] += row["mark_tariff"]
    assert sum(tally.values()) == 720
    assert sum(by_paper["1"].values()) == 240
    assert sum(by_paper["2"].values()) == 480
    source = WORK / "assessment-evidence/question_parts.json"
    source.write_text(json.dumps({
        "status": "mapped_to_primary_syllabus_topic_for_step_3_review",
        "method": "All paper marks reconcile. Content mapping is a reviewed primary topic context, not a claim of exact leaf-objective or examiner AO allocation.",
        "records": rows,
    }, indent=2, ensure_ascii=False) + "\n")
    out = {
        "status": "complete_for_primary_topic_context",
        "basis": "All 240 Paper 1 items and 325 Paper 2 marked parts from 2020–2025; 720 raw marks. Paper 3 is measured separately as practical skills.",
        "method": "Manual chemistry reading of individual Paper 1 items and Paper 2 main questions, with explicit overrides for mixed questions. Each mark is assigned once to its primary content context. These are contextual estimates, not an examiner AO split or exact objective exposure.",
        "topics": [
            {"topic": n, "name": names[n], "raw_marks": tally[n],
             "share_percent": round(tally[n] / 720 * 100, 1),
             "paper_1_marks": by_paper["1"][n], "paper_2_marks": by_paper["2"][n],
             "years_seen": sorted(appearances[n])}
            for n in range(1, 12)
        ],
        "paper_3": {"raw_marks": 240, "primary_assessment": "AO C practical (experimental and investigative) skills and abilities", "years_seen": list(range(2020, 2026))},
        "limitation": "Mixed-topic parts, diagrams and context may warrant a secondary topic. This table assigns one primary context per mark. The specific learning-objective map and item-level A/B split are Step 4 planning work.",
    }
    path = WORK / "curriculum/topic-context-exposure.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print("Wrote", path, "720 content marks + 240 practical marks")


if __name__ == "__main__":
    main()
