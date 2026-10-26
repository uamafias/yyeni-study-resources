"""Count visible command openings in 6117 Papers 2 and 3.

This is a reproducible line-level count, not a full question-part map. A tariff is
recorded only where the next printed bracket can be found before another
command opening. The corpus analysis states this limitation.
"""

import collections
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BANK = ROOT / "Question Banks/Namibian Curricula/NSSCO (New)/Chemistry (6117)"
OUTPUT = Path(__file__).resolve().parents[1] / "assessment-evidence/command-openings.json"
WORDS = [
    "define", "name", "list", "indicate", "give", "state", "describe", "compare",
    "explain", "distinguish", "outline", "discuss", "deduce", "find", "estimate",
    "interpret", "evaluate", "sketch", "predict", "identify", "relate", "suggest",
    "calculate", "determine", "measure", "construct", "classify", "comment",
    "draw", "write", "complete", "plot", "label", "record",
]
OPENING = re.compile(
    r"^\s*(?:(?:\d{1,2}|\([a-zivx]+\))\s+)?(" + "|".join(WORDS) + r")\b", re.I
)
MARK = re.compile(r"\[(\d+)\]")


def main():
    entries = []
    for year in range(2020, 2026):
        for paper in (2, 3):
            files = [
                f for f in (BANK / str(year)).glob("*.pdf")
                if re.search(fr"6117[-_/]{paper}|Paper {paper}", f.name, re.I)
            ]
            assert len(files) == 1, (year, paper, files)
            lines = subprocess.check_output(
                ["pdftotext", "-raw", str(files[0]), "-"], text=True
            ).splitlines()
            for i, line in enumerate(lines):
                stripped = line.strip()
                match = OPENING.match(stripped)
                if not match or stripped.count(".") > 20:
                    continue
                word = match.group(1).lower()
                next_opening = next(
                    (j for j in range(i + 1, min(i + 20, len(lines)))
                     if OPENING.match(lines[j].strip()) and lines[j].strip().count(".") <= 20),
                    min(i + 20, len(lines)),
                )
                candidate = " ".join(lines[i:next_opening])
                mark = MARK.search(candidate)
                entries.append({
                    "year": year,
                    "paper": paper,
                    "word": word,
                    "nearest_bracket": int(mark.group(1)) if mark else None,
                    "source_file": str(files[0].relative_to(ROOT)),
                    "opening": stripped,
                })
    grouped = []
    for paper in (2, 3):
        for word in WORDS:
            subset = [e for e in entries if e["paper"] == paper and e["word"] == word]
            if not subset:
                continue
            tariff = collections.Counter(e["nearest_bracket"] for e in subset if e["nearest_bracket"] is not None)
            grouped.append({
                "paper": paper,
                "word": word,
                "opening_lines": len(subset),
                "nearest_bracket_distribution": dict(sorted(tariff.items())),
            })
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "method": "Line-level command openings in pdftotext -raw; nearest bracket is a provisional tariff, not a validated part-level tariff.",
        "corpus": "NSSCO Chemistry 6117 Papers 2 and 3, 2020–2025",
        "groups": grouped,
        "entries": entries,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(entries)} command-opening lines; wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
