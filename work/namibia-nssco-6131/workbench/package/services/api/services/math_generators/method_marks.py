"""Method-mark evidence: which steps of the model working appear in a learner's working.

The generator knows the exact intermediate values. This module looks for them in
the learner's typed working and reports which were found, so the grader can be
told "the learner reached steps 1 and 2 but not 3" instead of guessing. It is
evidence for the judge, not a replacement for it: a value can appear by luck and
a correct step can be written in a form we cannot read.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import List, Sequence

from ..math_marking import check

from .base import GeneratedProblem, Step


def complete_working(problem: GeneratedProblem) -> GeneratedProblem:
    """Finish component calculations in the answer's requested representation.

    Keep the actual method supplied by each family. Add the missing assembly or
    rounding operation, not a replacement for the preceding method. A tuple of
    separately calculated coordinates, for example, still needs its ordered pair.
    """
    m = problem.marking
    if not m:
        return problem  # judge-only legacy descriptions
    typed = m.get("typed", m["expected"][0])
    kind = m["answer_type"]
    steps = list(problem.steps)
    if steps and steps[-1].value.strip() == typed.strip():
        steps[-1] = replace(steps[-1], answer_type=kind)
    else:
        if m.get("rounding") in ("sig_figs", "decimal_places", "angle_1dp"):
            digits = 1 if m["rounding"] == "angle_1dp" else m.get("digits", 3)
            unit = "significant figures" if m["rounding"] == "sig_figs" else "decimal places"
            description = f"Round the calculated result to {digits} {unit}"
        else:
            description = {
                "coordinates": "Combine the calculated coordinates in the requested order",
                "table_values": "Collect the calculated entries in the order of the table",
                "equation_solution": "Collect the solutions, keeping each variable and solution pair together",
                "matrix": "Place the calculated entries in their matrix positions",
                "vector": "Write the calculated components in vector order",
                "inequality": "Combine the bounds or conditions into the required inequality",
                "standard_form": "Combine the coefficient and power of ten in standard form",
                "time_or_date": "Combine the hours and remaining minutes",
                "expression": "Combine the calculated terms into the required expression",
            }.get(kind, "Write the calculated result in the required answer form")
        steps.append(Step(description, typed, kind))
    return replace(problem, steps=tuple(steps))


@dataclass(frozen=True)
class StepEvidence:
    description: str
    value: str
    found: bool


def _pieces(working: str) -> List[str]:
    """Candidate answers inside the working: each line, each side of '=', each bracketed or spaced chunk."""
    out: List[str] = []
    # Matrix rows contain semicolons. Keep each complete line as well as the
    # smaller candidates so structured values survive the scalar splitting.
    out.extend(line.strip() for line in working.splitlines() if line.strip())
    for line in re.split(r"[\n;]|\s{2,}", working):
        line = line.strip()
        if not line:
            continue
        out.append(line)
        if "=" in line and not re.search(r"[<>]=|=[<>]", line):
            out.extend(p.strip() for p in line.split("="))
    return out


def find_steps(problem: GeneratedProblem, working: str) -> List[StepEvidence]:
    pieces = _pieces(working or "")
    results: List[StepEvidence] = []
    for step in problem.steps:
        if step.answer_type:
            kind = step.answer_type
        elif ";" in step.value and step.value.strip().startswith("("):
            kind = "matrix"
        elif step.value.strip().startswith("{"):
            kind = "set_answer"
        elif "," in step.value and step.value.strip().startswith("("):
            kind = "coordinates"
        elif re.search(r"[<>]|>=|<=|≥|≤", step.value):
            kind = "inequality"
        elif re.fullmatch(r"[-+\d./\s]+", step.value):
            kind = "number_exact"
        else:
            kind = "expression"
        found = False
        for piece in pieces:
            try:
                if check(kind, [step.value], piece).correct:
                    found = True
                    break
            except Exception:
                continue
        results.append(StepEvidence(step.description, step.value, found))
    return results


def summarise(evidence: Sequence[StepEvidence]) -> str:
    """One line for the grader: which model steps the learner's working shows."""
    if not evidence:
        return "No model steps recorded."
    parts = [f"{'value found' if e.found else 'value not recognised'}: {e.description} ({e.value})" for e in evidence]
    return ("Model working vs learner's working (matching values do not prove the method; "
            "unrecognised values do not prove a step is missing). " + "; ".join(parts))
