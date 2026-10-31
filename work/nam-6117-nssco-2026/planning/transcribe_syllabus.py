"""Transcribe NSSCO Chemistry 6117 syllabus facts with page-level evidence."""

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SYLLABUS = ROOT / "Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Chemistry_syllabus.pdf"
OUTPUT = Path(__file__).resolve().parents[1] / "curriculum/syllabus-facts.json"


def pages():
    text = subprocess.check_output(["pdftotext", "-layout", str(SYLLABUS), "-"], text=True)
    return [page.splitlines() for page in text.split("\f")]


def source(pgs, pdf_page, line_number):
    return {
        "pdf_page": pdf_page,
        "printed_page": pdf_page - 3 if pdf_page >= 4 else None,
        "verbatim_line": pgs[pdf_page - 1][line_number].strip(),
    }


def record(pgs, value, pdf_page, line_number):
    return {"value": value, "source": source(pgs, pdf_page, line_number)}


def main():
    pgs = pages()
    facts = {
        "subject": "NSSCO Chemistry",
        "syllabus_code": record(pgs, "6117", 1, 17),
        "edition": record(pgs, 2018, 2, 13),
        "first_examination": record(pgs, 2020, 1, 25),
        "syllabus_file": str(SYLLABUS.relative_to(ROOT)),
        "assessment_objectives": [],
        "papers": [],
        "command_words": [],
        "content_outline": [],
        "stated_limits": [],
        "notes": [
            "The syllabus describes AO weightings as approximate. Its raw-mark row totals "
            "are not the same as the qualification percentage weights because papers are weighted separately.",
            "The 2025 Paper 1 specifies 1 hour; the syllabus specifies 45 minutes.",
        ],
    }

    ao_rows = [
        ("A", "Knowledge with understanding", 50, [25, 50, 0], 41, 9, 43, 18),
        ("B", "Handling information, application and solving problems", 30, [15, 30, 0], 41, 10, 43, 22),
        ("C", "Practical (experimental and investigative) skills and abilities", 20, [0, 0, 40], 41, 11, 43, 27),
    ]
    for code, name, weight, marks, name_page, name_line, grid_page, grid_line in ao_rows:
        criteria = []
        for page_number in (41, 42):
            lines = pgs[page_number - 1]
            for number, line in enumerate(lines):
                match = re.match(rf"^\s*({code}\d+)\s+(.+)$", line)
                if match:
                    entry_lines = [line.strip()]
                    next_number = number + 1
                    while next_number < len(lines) and lines[next_number].strip() and not re.match(r"^\s*[ABC]\d+\s+", lines[next_number]):
                        if len(lines[next_number]) - len(lines[next_number].lstrip()) < 5:
                            break
                        entry_lines.append(lines[next_number].strip())
                        next_number += 1
                    criteria.append({
                        "code": match.group(1),
                        "source": source(pgs, page_number, number),
                        "verbatim_entry": "\n".join(entry_lines),
                    })
        ao = {
            "code": code,
            "name": record(pgs, name, name_page, name_line),
            "qualification_weight_percent": record(pgs, weight, grid_page, grid_line),
            "marks_by_paper": record(pgs, dict(zip(["1", "2", "3"], marks)), grid_page, grid_line),
            "criteria": criteria,
        }
        if code == "A":
            ao["recall_limit_percent"] = record(pgs, 25, 43, 19)
        facts["assessment_objectives"].append(ao)

    paper_rows = [
        ("1", "Theory: Multiple choice questions", 40, 45, 30, "Forty four-choice multiple-choice items; A and B", 17, 6),
        ("2", "Theory: Structured questions", 80, 90, 50, "Compulsory short-answer, structured and free-response questions; A and B", 24, 7),
        ("3", "Alternative to practical", 40, 75, 20, "Written compulsory practical-skills questions; C", 28, 8),
    ]
    for num, name, marks, minutes, weight, description, row_line, weight_line in paper_rows:
        facts["papers"].append({
            "paper": num,
            "name": record(pgs, name, 42, row_line),
            "marks": record(pgs, marks, 42, row_line),
            "duration_minutes": record(pgs, minutes, 42, row_line),
            "qualification_weight_percent": record(pgs, weight, 43, weight_line),
            "description": record(pgs, description, 42, row_line),
        })

    # Glossary entries are captured as full text blocks, preserving the syllabus wording.
    glossary_ranges = [
        ("Define", 45, 1, 2), ("What do you understand by / What is meant by", 45, 3, 7),
        ("State", 45, 8, 9), ("List", 45, 10, 11), ("Explain", 45, 12, 13),
        ("Describe", 45, 14, 23), ("Discuss", 45, 24, 25), ("Outline", 45, 26, 26),
        ("Deduce / predict", 45, 27, 30), ("Comment", 45, 31, 33),
        ("Suggest", 45, 34, 38), ("Find", 45, 39, 40),
        ("Calculate", 46, 0, 1), ("Measure", 46, 3, 5),
        ("Determine", 46, 6, 9), ("Estimate", 46, 10, 13),
        ("Sketch", 46, 14, 20), ("Construct", 46, 21, 23),
        ("Compare", 46, 24, 25), ("Classify", 46, 26, 26),
    ]
    for word, page, first, last in glossary_ranges:
        facts["command_words"].append({
            "word": word,
            "source": source(pgs, page, first),
            "verbatim_entry": "\n".join(line.rstrip() for line in pgs[page - 1][first:last + 1]),
        })

    current_topic = None
    for page in (7, 8):
        for number, line in enumerate(pgs[page - 1]):
            match = re.match(r"^Topic\s+(\d+):\s*(.+)$", line.strip())
            if match:
                current_topic = {
                    "topic": int(match.group(1)),
                    "name": match.group(2),
                    "source": source(pgs, page, number),
                    "subtopics": [],
                }
                facts["content_outline"].append(current_topic)
                continue
            subtopic = re.match(r"^\s*(\d+(?:\.\d+){1,2})\s+(.+)$", line)
            if current_topic and subtopic:
                current_topic["subtopics"].append({
                    "number": subtopic.group(1),
                    "name": subtopic.group(2),
                    "source": source(pgs, page, number),
                })

    limit_pattern = re.compile(r"not required|will not be set|NOT be supplied|limited to aqueous", re.I)
    for page_number, lines in enumerate(pgs, 1):
        if not 9 <= page_number <= 42:
            continue
        for number, line in enumerate(lines):
            if limit_pattern.search(line):
                facts["stated_limits"].append({
                    "source": source(pgs, page_number, number),
                    "context_verbatim": "\n".join(x.rstrip() for x in lines[max(0, number - 2):number + 1]),
                })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(facts, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
