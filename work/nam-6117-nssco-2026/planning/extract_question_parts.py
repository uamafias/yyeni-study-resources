"""Extract every printed mark-bearing part from held Chemistry 6117 papers.

Objective mapping remains deliberately unset until a human reads each part in
context. This script distinguishes question-total brackets from part marks and
checks each paper against the cover's total marks.
"""

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parents[1]
BANK = ROOT / "Question Banks/Namibian Curricula/NSSCO (New)/Chemistry (6117)"
MARK = re.compile(r"\[(\d+)\]")
COMMAND = re.compile(
    r"\b(Define|Name|List|Indicate|Give|State|Describe|Compare|Explain|Distinguish|"
    r"Outline|Discuss|Deduce|Find|Estimate|Interpret|Evaluate|Sketch|Predict|"
    r"Identify|Relate|Suggest|Calculate|Determine|Measure|Construct|Classify|"
    r"Comment|Draw|Write|Complete|Plot|Label|Record|Plan|Use|Choose|Circle|"
    r"Arrange|Balance|Show|Match)\b", re.I
)
PART_LABEL = re.compile(r"\(([a-z]|[ivx]+)\)")
PARENT_COMMAND = {
    (2020, 2, 1): "state", (2020, 2, 3): "match", (2020, 2, 6): "state",
    (2020, 3, 1): "choose", (2021, 2, 1): "which",
    (2021, 3, 3): "complete", (2022, 2, 1): "state",
    (2022, 3, 2): "record", (2024, 2, 1): "choose",
    (2025, 2, 1): "give", (2025, 2, 3): "state",
    (2025, 3, 3): "complete", (2024, 2, 5): "identify",
}
COMMAND_OVERRIDE = {
    (2020, 2, 4, 4): "calculate",
    (2020, 2, 8, 5): "state",
    (2020, 3, 2, 2): "plot",
    (2020, 3, 2, 10): "use",
    (2020, 3, 3, 1): "suggest",
    (2021, 3, 4, 1): "plan",
    (2021, 2, 5, 2): "name",
    (2022, 2, 4, 1): "explain",
    (2023, 2, 5, 2): "calculate",
    (2023, 3, 2, 2): "plot",
    (2023, 3, 3, 1): "explain",
    (2024, 2, 7, 1): "give",
    (2024, 3, 5, 1): "plan",
    (2025, 2, 3, 7): "show",
    (2025, 2, 4, 1): "deduce",
    (2025, 3, 4, 1): "describe",
}


def command_for(segment, inherited):
    # A mark bracket closes one printed task. Cross-references such as (b)(i)
    # and chemical-state symbols such as (s) can occur after its opening verb,
    # so the LAST parenthesis is not a reliable part boundary.
    segment = re.sub(r"For\s+Examiner[’']s\s+Use", "", segment, flags=re.I)
    labels = list(PART_LABEL.finditer(segment))

    def directives(text):
        found = []
        for match in COMMAND.finditer(text):
            prefix = text[:match.start()]
            # Lowercase command words follow an instruction lead-in such as
            # “On the grid, sketch ...”. Elsewhere they can be ordinary nouns
            # or infinitives: “liquid state”, “used to measure”.
            if match.group()[0].isupper() or not prefix.strip() or re.search(r"[,.;:]\s*$", prefix):
                found.append(match)
        return found

    if labels:
        text = segment[labels[0].end():]
        interrogative = re.match(r"\s*(What|Which|How)\b", text, re.I)
        if interrogative:
            return interrogative.group(1).lower(), "explicit_interrogative"
        matches = directives(text)
        if matches:
            selected = matches[0]
            # Introductory “Use the table/list...” or “Choose from...” may be
            # followed by the operative State/Identify/Choose instruction.
            if selected.group(1).lower() in {"use", "choose"} and len(matches) > 1:
                second = matches[1]
                if len(labels) == 1 or second.start() < labels[1].start() - labels[0].end():
                    selected = second
            return selected.group(1).lower(), "explicit"
        prefix = segment[:labels[0].start()]
        prefix_hits = directives(prefix)
        prefix_question = list(re.finditer(r"\b(What|Which|How)\b", prefix, re.I))
        if prefix_question and (not prefix_hits or prefix_question[-1].start() > prefix_hits[-1].start()):
            return prefix_question[-1].group(1).lower(), "inherited_from_printed_parent_instruction"
        if prefix_hits:
            return prefix_hits[-1].group(1).lower(), "inherited_from_printed_parent_instruction"
    if not labels:
        matches = directives(segment)
        if matches:
            return matches[0].group(1).lower(), "explicit"
    return (inherited, "inherited") if inherited else (None, "unresolved")


def source_file(year, paper):
    files = [
        f for f in (BANK / str(year)).glob("*.pdf")
        if re.search(fr"6117[-_/]{paper}|Paper {paper}", f.name, re.I)
    ]
    assert len(files) == 1, (year, paper, files)
    return files[0]


def line_bounds(text, match):
    start = max(text.rfind("\n", 0, match.start()), text.rfind("\f", 0, match.start())) + 1
    ends = [x for x in (text.find("\n", match.end()), text.find("\f", match.end())) if x >= 0]
    end = min(ends) if ends else len(text)
    return text[start:end]


def clean_excerpt(text):
    text = re.sub(r"\.{6,}", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[-550:]


def paper_records(year, paper):
    file = source_file(year, paper)
    text = subprocess.check_output(["pdftotext", "-raw", str(file), "-"], text=True)
    results = []
    q = part = 1
    run = 0
    last_end = 0
    totals = []
    inherited_command = None
    for match in MARK.finditer(text):
        marks = int(match.group(1))
        line = line_bounds(text, match)
        standalone = not line[:line.find("[")].strip() and not line[line.find("]") + 1:].strip()
        if standalone and marks >= 5 and marks == run:
            totals.append(marks)
            run = 0
            q += 1
            part = 1
            inherited_command = None
            last_end = match.end()
            continue
        segment = text[last_end:match.start()]
        word, command_origin = command_for(segment, inherited_command)
        if command_origin in {"explicit", "inherited_from_printed_parent_instruction"}:
            inherited_command = word
        page = text.count("\f", 0, match.start()) + 1
        results.append({
            "evidence_id": f"QP-6117-{year}-{paper}-Q{q:02d}-P{part:02d}",
            "source_id": f"QP-6117-{year}-{paper}",
            "evidence_type": "past_paper",
            "exam_series": "Oct/Nov",
            "year": year,
            "paper_id": str(paper),
            "variant": None,
            "question_ref": f"Q{q}, marked part {part}",
            "mark_tariff": marks,
            "objective_ids": ["syllabus:unmapped"],
            "command_word": word,
            "command_origin": command_origin,
            "ao_focus": ["C"] if paper == 3 else ["A", "B"],
            "context_type": "question part awaiting semantic objective mapping",
            "context_summary": clean_excerpt(segment),
            "creditworthy_points": [],
            "examiner_findings": [],
            "common_errors": [],
            "strong_response_features": [],
            "source_locator": f"{file.relative_to(ROOT)}, PDF viewer p. {page}, Q{q} marked part {part}",
            "notes": ["Part number is sequential within the main question; check the PDF for the printed letter/roman numeral.", "Do not infer objective IDs or credit rules from a text match."],
        })
        run += marks
        part += 1
        last_end = match.end()
    expected = 80 if paper == 2 else 40
    assert sum(x["mark_tariff"] for x in results) == expected, (year, paper, totals, run)
    expected_q = 7 if year == 2024 and paper == 2 else 5 if year == 2024 and paper == 3 else 8 if paper == 2 else 4
    assert len(totals) + (1 if run else 0) == expected_q, (year, paper, totals, run)
    for row in results:
        number = int(re.search(r"Q(\d+)", row["question_ref"]).group(1))
        part_number = int(re.search(r"marked part (\d+)", row["question_ref"]).group(1))
        if (year, paper, number) == (2021, 2, 1):
            row["command_word"] = "which"
            row["command_origin"] = "inherited_from_printed_parent_instruction"
            continue
        override = COMMAND_OVERRIDE.get((year, paper, number, part_number))
        if override:
            row["command_word"] = override
            row["command_origin"] = "verified_compound_or_ocr_instruction"
            continue
        if row["command_word"] is None:
            parent = PARENT_COMMAND.get((year, paper, number))
            if parent:
                row["command_word"] = parent
                row["command_origin"] = "inherited_from_printed_parent_instruction"
    return results


def paper_one_records(year):
    file = source_file(year, 1)
    text = subprocess.check_output(["pdftotext", "-raw", str(file), "-"], text=True)
    position = text.find("\f") + 1
    matches = []
    for question in range(1, 41):
        pattern = re.compile(fr"(?m)^{question}\s+((?:[A-Z](?:[a-z]+)?|[0-9]+)[^\n]*)$")
        match = pattern.search(text, position)
        assert match is not None, (year, question)
        matches.append(match)
        position = match.end()
    records = []
    for question, match in enumerate(matches, 1):
        stop = matches[question].start() if question < 40 else text.find("DATA SHEET", match.end())
        if stop < 0:
            stop = len(text)
        excerpt = re.sub(r"\s+", " ", text[match.start():stop]).strip()[:500]
        page = text.count("\f", 0, match.start()) + 1
        records.append({
        "evidence_id": f"QP-6117-{year}-1-Q{question:02d}",
        "source_id": f"QP-6117-{year}-1",
        "evidence_type": "past_paper",
        "exam_series": "Oct/Nov",
        "year": year,
        "paper_id": "1",
        "variant": None,
        "question_ref": f"Q{question}",
        "mark_tariff": 1,
        "objective_ids": ["syllabus:unmapped"],
        "command_word": None,
        "command_origin": "multiple_choice_item",
        "ao_focus": ["A", "B"],
        "context_type": "four-option multiple choice awaiting semantic objective mapping",
        "context_summary": excerpt,
        "creditworthy_points": [],
        "examiner_findings": [],
        "common_errors": [],
        "strong_response_features": [],
        "source_locator": f"{file.relative_to(ROOT)}, PDF viewer p. {page}, Q{question}",
        "notes": ["Forty one-mark items stated on the paper cover and in the syllabus; objective and AO split await item-level reading."],
        })
    return records


def main():
    records = []
    for year in range(2020, 2026):
        records.extend(paper_one_records(year))
        records.extend(paper_records(year, 2))
        records.extend(paper_records(year, 3))
    path = WORK / "assessment-evidence/question_parts.json"
    path.write_text(json.dumps({
        "status": "extracted_unmapped",
        "method": "Printed mark brackets, excluding main-question total brackets; every paper reconciles to 40/80/40 marks.",
        "records": records,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(records)} item/part records; {sum(x['mark_tariff'] for x in records)} total raw marks")


if __name__ == "__main__":
    main()
