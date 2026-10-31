"""Individual chemistry reading of the 240 multiple-choice item contexts."""

import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

MAP = {
  2020: "2.1.1 2.1.2 2.1.2 2.1 2.1 2.4.2 9.4 2.4.3 2.4.4 2.4.1 2.4.6 3.1 3.2 3.4 4.2 4.2 4.2 4.2 4.2 5.1 5.1 6.3 6.2 6.4 6.4 6.6 6.5 7.1 7.1 8.1 9.2 9.3 9.4 10.2 10.2.2 10.6 10.8.1 11.1 11.1.2 11.4",
  2021: "1.5 1.5 1.5 2.1.2 2.1.2 2.1.2 2.3.3 2.1 2.4.2 2.1 2.4.3 2.2 2.4.1 3.1 3.2 3.3 3.4 4.2 5.1 5.1 5.1 6.2 6.4 6.5 7.1 7.2 7.4 8.1 9.1 10.2 10.3 10.5 10.8.1 10.8.2 11.1.1 11.1 11.1 11.4 11.4 11.5",
  2022: "2.1.1 1.5 2.1 2.2 2.3.1 2.4.2 2.4.3 2.4.3 2.4.4 2.4.5 2.4.1 2.4.6 3.2 3.1 4.2 5.1 6.1 6.2 6.3 2.3.2 6.5 9.3 7.1 7.2 7.1 9.3 9.2 10.2.2 10.3 10.5 10.5 10.8.1 11.1.1 11.1 11.1 11.3 11.4 11.5 11.5 11.5",
  2023: "2.1.1 1.5 2.1.1 2.1.2 2.3.1 2.3.3 2.3.3 9.1 2.4 2.4.2 2.4.4 2.4.5 2.4.5 2.4.6 3.1 3.2 3.3 7.2 4.2 4.2 5.1 2.3.3 6.4 6.6 7.1 7.4 8.1 9.3 9.2 10.3 10.2.2 10.4 10.7 10.8 10.8.1 11.1 11.3 11.4 11.5 11.5",
  2024: "1.5 1.5 1.5 2.1.1 2.1.2 2.2 2.3.3 2.4.3 2.4.4 2.1 2.4 3.3 4.1 4.2 4.2 5.1 5.1 6.2 6.3 6.4 6.4 6.5 6.6 7.1 7.4 8.1 8.2 9.3 9.3 10.2.1 10.3 10.4 10.2.1 10.6 10.8.1 11.1 11.1.2 11.5 11.5 11.5",
  2025: "1.5 1.5 1.5 2.1.2 2.3.2 2.3.3 2.3.3 2.3.3 2.4.3 2.4.4 2.4.6 3.2 4.2 4.2 5.1 6.2 6.4 6.5 6.5 6.6 6.6 7.1 7.4 7.4 8.1 8.1 9.1 9.2 9.3 9.4 10.2 10.3 10.4 10.5 10.5 10.8.2 10.8.1 11.3 11.4 11.5",
}


def main():
    path = WORK / "assessment-evidence/question_parts.json"
    data = json.loads(path.read_text())
    valid = {s["number"] for t in json.loads((WORK / "curriculum/syllabus-facts.json").read_text())["content_outline"] for s in t["subtopics"]}
    for year, line in MAP.items():
        ids = line.split()
        assert len(ids) == 40, (year, len(ids))
        assert all(i in valid for i in ids), (year, [i for i in ids if i not in valid])
        subset = [row for row in data["records"] if row["year"] == year and row["paper_id"] == "1"]
        assert len(subset) == 40
        for row, subtopic in zip(subset, ids):
            row["objective_ids"] = [f"syllabus:{subtopic}"]
            row["context_topic_id"] = f"syllabus:{subtopic.split('.')[0]}"
            row["mapping_method"] = "Individually read multiple-choice stem/options and matched assessed chemistry concept to the named syllabus subtopic."
            row["mapping_confidence"] = "high"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("Mapped 240 Paper 1 items to named syllabus subtopics")


if __name__ == "__main__":
    main()
