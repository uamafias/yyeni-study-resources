"""Part-by-part reading of Paper 2 content against named syllabus subtopics."""

import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

# Each list follows the printed marked-part sequence of the main question.
MAP = {
  2020: {
    1: "2.1 2.4.3 8.2 2.4.3 2.4.4 3.4 2.4.4 3.3 3.3 3.3",
    2: "2.3.3 2.3.1 2.3.2 2.3.3 2.3.3",
    3: "4.1 4.2 4.2 4.2 4.2 4.2",
    4: "5.1 5.1 6.3 6.2 6.2",
    5: "7.1 7.1 7.1 7.3 7.3 4.2 8.2",
    6: "9.3 9.3 5.1 9.1 9.4 9.3",
    7: "10.2.2 10.5 10.4 10.3 10.3 10.8.1 10.8.1 10.8.1",
    8: "11.5 11.5 11.5 11.5 11.5 11.5 11.5",
  },
  2021: {
    1: "5.1 6.1 2.4.4 11.1.2 11.2 2.4.3",
    2: "2.1.2 2.4.5 2.4.5 2.4.2 2.4.2 2.4.2",
    3: "7.1 7.1 4.2 4.2 4.2 7.4 4.2 4.2",
    4: "6.4 6.4 6.4 6.6 6.6",
    5: "2.4.1 2.1.1 2.1.1 8.2",
    6: "9.3 9.3 9.3 9.3 9.4 9.2",
    7: "10.1 10.4 10.4 10.2.2 4.2",
    8: "11.5 11.5 11.5 11.5 11.5 11.4 11.4",
  },
  2022: {
    1: "2.3.3 2.3.3 2.3.3 2.3.3 2.3.3 2.1.2 2.4.2 2.4.2 2.4.1",
    2: "5.1 5.1 5.1 5.1 5.1 9.4",
    3: "7.4 7.4 7.4 7.3 8.2",
    4: "7.1 11.5 2.4.6 4.2 4.2 4.2 4.2 4.2 4.2",
    5: "9.2 6.4 6.4 6.6 6.2 6.2 9.3",
    6: "9.2 9.2 9.2 9.2 11.1 11.1",
    7: "10.8.2 10.5 10.6 10.7 10.7 10.8.1 10.8.1",
    8: "11.2 11.1.2 11.1.2 11.1.2 11.1",
  },
  2023: {
    1: "2.2 2.2 2.2 6.3 2.2",
    2: "2.3.2 9.1 2.1.2 9.2 8.1 7.1 7.1 7.3 7.2 2.4.4 2.4.4 2.4.1 2.4.3 11.1.2 8.2 2.3.3",
    3: "5.1 5.1 5.1 5.1",
    4: "1.5 4.2 6.4 6.4 6.4",
    5: "6.2 6.2 6.5 6.2 6.5 6.5",
    6: "9.2 9.2 9.3 9.3 9.3 9.4",
    7: "10.2 10.2.1 10.2.1 10.2.1 10.2.1 10.5 10.5 10.8.1 10.8.1 10.8.2",
    8: "11.5 11.5 11.1",
  },
  2024: {
    1: "2.3.1 2.3.3 7.2 2.3.3 2.3.3 2.3.3",
    2: "2.1.2 2.1.2 2.4.2 5.1 5.1 5.1 2.4 2.4.4 2.4.4",
    3: "2.4.6 6.4 6.2 6.5 2.4.3 7.1 4.2 4.2 11.5",
    4: "7.1 7.1 7.1 11.1.1 7.3 7.4 7.4",
    5: "8.1 9.2 9.1 9.3 9.2 9.1 9.2 9.3 9.2 9.2 6.6",
    6: "10.2.2 10.5 10.5 10.5 10.5 10.5 10.8.2 10.8.2 10.8.2",
    7: "11.2 11.3 11.3 11.4 11.5 11.4",
  },
  2025: {
    1: "2.3.1 2.3.1 2.3.3 2.3.3 2.3.1 2.1.2 2.1.2 2.2",
    2: "7.1 7.3 7.4 7.4 7.4 7.1 4.2 4.2 4.2",
    3: "11.5 11.5 11.5 6.5 6.4 6.4 4.2",
    4: "2.4.2 5.1 5.1 5.1 5.1 2.3.3 2.3.3 2.3.3",
    5: "9.3 9.3 9.3 6.6 9.3 9.1 9.1 9.3 9.3 9.4",
    6: "10.8.3 10.8.3 3.4 3.2",
    7: "10.5 10.6 10.4 10.7 10.8.2 10.8.2",
    8: "11.5 11.5 11.5 11.4 11.4 11.4",
  },
}


def main():
    path = WORK / "assessment-evidence/question_parts.json"
    data = json.loads(path.read_text())
    valid = {s["number"] for t in json.loads((WORK / "curriculum/syllabus-facts.json").read_text())["content_outline"] for s in t["subtopics"]}
    count = 0
    for year, questions in MAP.items():
        for q, line in questions.items():
            ids = line.split()
            assert all(i in valid for i in ids), (year, q, [i for i in ids if i not in valid])
            subset = [row for row in data["records"] if row["year"] == year and row["paper_id"] == "2" and row["question_ref"].startswith(f"Q{q},")]
            assert len(ids) == len(subset), (year, q, len(ids), len(subset))
            for row, subtopic in zip(subset, ids):
                row["objective_ids"] = [f"syllabus:{subtopic}"]
                row["context_topic_id"] = f"syllabus:{subtopic.split('.')[0]}"
                row["mapping_method"] = "Read the marked part in its main-question context and matched its assessed chemistry meaning to a named syllabus subtopic."
                row["mapping_confidence"] = "high"
                count += 1
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("Mapped", count, "Paper 2 parts to named syllabus subtopics")


if __name__ == "__main__":
    main()
