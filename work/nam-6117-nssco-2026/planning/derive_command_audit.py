"""Count commands and exact printed part tariffs after instruction review."""

import collections
import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]


def main():
    rows = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    written = [row for row in rows if row["paper_id"] != "1"]
    assert len(written) == 451
    groups = []
    for paper, word in sorted({(row["paper_id"], row["command_word"]) for row in written}):
        subset = [row for row in written if row["paper_id"] == paper and row["command_word"] == word]
        tariffs = collections.Counter(row["mark_tariff"] for row in subset)
        origins = collections.Counter(row["command_origin"] for row in subset)
        groups.append({
            "paper": paper,
            "word": word,
            "parts": len(subset),
            "tariff_counts": {str(k): tariffs[k] for k in sorted(tariffs)},
            "modal_tariff": min(k for k, v in tariffs.items() if v == max(tariffs.values())),
            "command_origins": dict(origins),
        })
    counts = collections.Counter(row["command_word"].lower() for row in written)
    glossary = json.loads((WORK / "curriculum/syllabus-facts.json").read_text())["command_words"]
    glossary_forms = set()
    glossary_usage = []
    for entry in glossary:
        label = entry["word"]
        forms = ["deduce", "predict"] if label.lower() == "deduce / predict" else [label.lower()]
        glossary_forms.update(forms)
        glossary_usage.append({"glossary_entry": label, "parts": sum(counts[form] for form in forms)})
    out = {
        "status": "part_aligned_command_review",
        "basis": "451 actual printed marked parts in Papers 2 and 3, 2020–2025. Counts use the resolved opening command, including inherited opening instructions, rather than every verb occurring in a question. Tariffs come from printed part brackets and reconcile to each paper total.",
        "method": "Instruction parsed case-insensitively from each printed part, excluding noun/header matches; inherited parent wording and explicit OCR or compound-instruction corrections retain their provenance. A command is recorded for every part.",
        "groups": groups,
        "glossary_comparison": {
            "basis": "Resolved opening/main command for each written marked part; not every verb occurring inside an instruction. Bare What questions do not count as the glossary's longer definition phrase.",
            "unused_glossary_entries": [x["glossary_entry"] for x in glossary_usage if x["parts"] == 0],
            "rare_glossary_entries": [x for x in glossary_usage if 0 < x["parts"] <= 3],
            "observed_forms_outside_glossary": [{"word": word, "parts": count} for word, count in counts.most_common() if word not in glossary_forms],
            "prompt_policy": "An observed paper command may be eligible even when absent from the glossary. Unobserved glossary entries do not become prompt openings merely because the glossary lists them. Match task type and observed tariff; separately review generic Use/Which/What and compound instructions.",
        },
        "unresolved": [row["evidence_id"] for row in written if row["command_word"] is None],
        "limitation": "A part may contain multiple verbs. The table uses its main action for counts; original evidence excerpts and command origins must be inspected before prompt wording is approved.",
    }
    path = WORK / "assessment-evidence/command-part-audit.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print("wrote", len(groups), "paper/command groups; unresolved", len(out["unresolved"]))


if __name__ == "__main__":
    main()
