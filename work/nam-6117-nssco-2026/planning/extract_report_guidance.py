"""Index report answer tables by main question, preserving source text internally.

This is source evidence for a human to paraphrase, not learner-facing content.
It never treats an absent answer table as a zero-mark answer.
"""

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parents[1]
RANGES = {2020: (85, 100), 2021: (81, 90), 2022: (91, 102), 2023: (95, 108), 2024: (105, 118), 2025: (89, 104)}


def report_path(year):
    if year < 2024:
        return next((ROOT / f"Question Banks/Namibian Curricula/NSSCO (New)/Chemistry (6117)/{year}").glob("*Report*.pdf"))
    return next((ROOT / f"Question Banks/Namibian Examiner Reports/NSSCO (New) /{year}").glob("*.pdf"))


def pdf_lines(year):
    start, end = RANGES[year]
    path = report_path(year)
    raw = subprocess.check_output(["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(path), "-"], text=True)
    lines = []
    for offset, page in enumerate(raw.split("\f")):
        for line in page.splitlines():
            lines.append((start + offset, line))
    return lines


def paper_windows(lines):
    headings = []
    for index, (_, line) in enumerate(lines):
        found = re.match(r"^\s*Paper\s+([123])\s*$", line, re.I)
        if found:
            headings.append((index, int(found.group(1))))
    windows = {}
    for pos, (index, paper) in enumerate(headings):
        windows[paper] = (index, headings[pos + 1][0] if pos + 1 < len(headings) else len(lines))
    return windows


def table_start(lines, lo, hi, question):
    pattern = re.compile(rf"^\s*{question}\s*\.?\s*(?:\([a-h]\)|[a-h]\.)")
    candidates = []
    for i in range(lo, hi):
        if not pattern.match(lines[i][1]):
            continue
        nearby = " ".join(line for _, line in lines[i:i + 5])
        score = nearby.count("") + nearby.count("") + nearby.count("")
        candidates.append((score, i))
    if not candidates:
        return None
    scored = [item for item in candidates if item[0] > 0]
    return min(scored or candidates, key=lambda item: item[1])[1]


ROW = re.compile(r"^\s*(?:(?:\d+\s*)?\([a-h]\)(?:\s*\([ivx]+\))?|\([ivx]+\)|(?:\d+\.?\s*)?[a-h]\.(?:\s*[ivx]+\.)?|(?:i|ii|iii|iv|v)\.)\s+")


def table_rows(lines, start, stop):
    positions = [i for i in range(start, stop) if ROW.match(lines[i][1])]
    return [
        {"label_line": lines[pos][1].strip(), "source_page": lines[pos][0],
         "source_text": "\n".join(line.rstrip() for _, line in lines[pos:positions[j + 1] if j + 1 < len(positions) else stop]).strip()}
        for j, pos in enumerate(positions)
    ]


def main():
    qp = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    out = []
    for year in range(2020, 2026):
        lines = pdf_lines(year)
        windows = paper_windows(lines)
        for paper in (2, 3):
            lo, hi = windows[paper]
            qnums = sorted({int(re.search(r"Q(\d+)", x["question_ref"]).group(1)) for x in qp if x["year"] == year and x["paper_id"] == str(paper)})
            for q in qnums:
                expected = [x for x in qp if x["year"] == year and x["paper_id"] == str(paper) and x["question_ref"].startswith(f"Q{q},")]
                start = table_start(lines, lo, hi, q)
                if start is None:
                    out.append({"year": year, "paper": paper, "question": q, "expected_parts": len(expected), "status": "no_text_answer_table_detected", "rows": []})
                    continue
                candidates = []
                for i in range(start + 1, min(start + 180, hi)):
                    line = lines[i][1]
                    if re.search(r"\[\d+\]\s*$", line) or re.match(rf"^\s*Question\s+{q+1}\s*$", line, re.I):
                        candidates.append(i)
                following = table_start(lines, start + 1, hi, q + 1)
                if following is not None:
                    candidates.append(following)
                stop = min(candidates) if candidates else min(start + 120, hi)
                rows = table_rows(lines, start, stop)
                out.append({"year": year, "paper": paper, "question": q, "expected_parts": len(expected),
                            "status": "answer_table_rows_detected" if rows else "no_text_answer_table_detected",
                            "source_locator": f"{report_path(year).relative_to(ROOT)}, PDF viewer p. {lines[start][0]}",
                            "rows": rows})
    path = WORK / "assessment-evidence/report-answer-tables.json"
    path.write_text(json.dumps({"status": "raw_internal_extraction_for_alignment", "purpose": "Source answer rows for evidence mining; never learner-facing", "questions": out}, indent=2, ensure_ascii=False) + "\n")
    for y in range(2020, 2026):
        print(y,[(f"P{x['paper']}Q{x['question']}",x['expected_parts'],len(x['rows'])) for x in out if x['year']==y])


if __name__ == "__main__":
    main()
