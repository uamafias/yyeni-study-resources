"""Align extracted internal answer rows to printed parts where defensible."""

import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

# Row indices are zero-based; groups preserve one marked part that the report
# prints on multiple answer lines. Shared rows cover a report answer printed
# once for two separately bracketed paper parts.
GROUPS = {
    (2021, 2, 2): [[0, 1, 2], [3], [4], [5], [6], [7]],
    (2022, 2, 1): [[0], [1], [2], [3], [4], [5, 6], [7], [8], [9]],
    (2024, 2, 4): [[0], [0], [1], [2], [3], [4], [5]],
    (2025, 2, 5): [[0], [1], [2], [3], [4, 5], [6], [7], [8], [9], [10]],
}


def main():
    tables = json.loads((WORK / "assessment-evidence/report-answer-tables.json").read_text())["questions"]
    parts = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    aligned = {}
    coverage = []
    for table in tables:
        key = (table["year"], table["paper"], table["question"])
        subset = [row for row in parts if row["year"] == key[0] and row["paper_id"] == str(key[1]) and row["question_ref"].startswith(f"Q{key[2]},")]
        rows = table["rows"]
        # The 2020 Paper 3 Question 3 text match is commentary, not an
        # answer table. The actual scheme is an image on the next page.
        if key == (2020, 3, 3):
            rows = []
        groups = GROUPS.get(key)
        if groups is None and len(rows) == len(subset) and rows:
            groups = [[i] for i in range(len(subset))]
        status = "candidate_answer_row_links_pending_audit" if groups else (
            "answer_table_needs_manual_alignment" if rows else
            "report_commentary_or_image_only")
        if groups:
            assert len(groups) == len(subset)
            for part, indices in zip(subset, groups):
                assert all(i < len(rows) for i in indices), (key, indices, len(rows))
                selected_rows = [rows[i] for i in indices]
                pages = sorted({row['source_page'] for row in selected_rows})
                source_file = table['source_locator'].split(', PDF viewer')[0]
                page_reference = f'p. {pages[0]}' if len(pages) == 1 else f'pp. {pages[0]}–{pages[-1]}'
                aligned[part["evidence_id"]] = {
                    "source_locator": f'{source_file}, PDF viewer {page_reference}',
                    "source_rows": selected_rows,
                    "alignment": "shared_row_candidate" if len(indices) == 1 and sum(indices[0] in g for g in groups) > 1 else "grouped_row_candidate" if len(indices) > 1 else "positional_candidate",
                }
        coverage.append({"year": key[0], "paper": key[1], "question": key[2], "parts": len(subset), "status": status,
                         "aligned_parts": len(subset) if groups else 0,
                         "source_locator": table.get("source_locator")})
    out = {
        "status": "candidate_links_pending_label_and_meaning_audit",
        "aligned_parts": aligned,
        "question_coverage": coverage,
        "unsupported_parts": [row["evidence_id"] for row in parts if row["paper_id"] != "1" and row["evidence_id"] not in aligned],
        "note": "These are candidate links from report row order and explicit grouped-row exceptions. Verify printed labels and answer meaning with report-alignment-audit.json before using a link. Unsupported here means no candidate text-row link; scanned image tables and commentary may still give guidance.",
    }
    path = WORK / "assessment-evidence/report-guidance-alignment.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print("Candidate links", len(aligned), "of 451 written parts;", len(out["unsupported_parts"]), "without candidate text rows")


if __name__ == "__main__":
    main()
