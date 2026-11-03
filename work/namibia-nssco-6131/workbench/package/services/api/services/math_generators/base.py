"""Core types for generated math flashcards.

A generated card is a *recipe*: given a seed and a difficulty level it produces
one concrete problem (question text, correct answer, and the answers a learner
would get from known mistakes). Everything here is deterministic and uses only
the standard library, so a seed gives the same problem on every machine and
Python version.

Rules every generator follows:

* Answers come from construction (pick the answer, build the question around
  it), never from a model. The generator also re-checks its own arithmetic
  with exact integer/fraction algebra before returning a problem.
* Question and answer text follow the LaTeX contract: math in ``$...$``,
  never wrapped in Markdown emphasis.
* No randomness outside ``SeededRandom``.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field, replace
from typing import Any, Dict, Mapping, Sequence, Tuple

MAX_SEED = 2**63 - 1


def question_identity_text(question, question_image=None):
    normalised = ' '.join((question or '').split())
    # Only the new bank changes identity semantics. Existing text cards and the
    # original gradient pilot keep their historical fingerprints exactly.
    if isinstance(question_image, str) and question_image.startswith('yyeni-diagram:'):
        normalised += '\0' + question_image
    return normalised


def visible_question_fingerprint(question, question_image=None):
    return hashlib.sha256(question_identity_text(question,question_image).encode('utf-8')).hexdigest()


class GeneratorError(ValueError):
    """A generator was asked for something invalid, or failed its own check."""


class UnknownGeneratorError(GeneratorError):
    """No generator is registered under the requested id."""


def validate_seed(seed: Any) -> int:
    """Seeds are non-negative integers below 2**63 (bool is not accepted)."""
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise GeneratorError("seed must be an integer")
    if seed < 0 or seed > MAX_SEED:
        raise GeneratorError("seed must be between 0 and 2**63 - 1")
    return seed


def validate_level(level: Any, levels: Sequence[int]) -> int:
    if isinstance(level, bool) or not isinstance(level, int):
        raise GeneratorError("level must be an integer")
    if level not in levels:
        raise GeneratorError(f"level must be one of {tuple(levels)}")
    return level


class SeededRandom:
    """A small deterministic random stream.

    Built on SHA-256 so results never depend on the interpreter's ``random``
    implementation (which the standard library does not promise to keep
    stable between versions). ``randbelow`` uses rejection sampling, so every
    value is exactly equally likely.
    """

    def __init__(self, seed: int, salt: str = "") -> None:
        self._seed = validate_seed(seed)
        self._salt = salt
        self._counter = 0
        self._buffer = b""

    def _take(self, count: int) -> bytes:
        while len(self._buffer) < count:
            block = f"{self._seed}:{self._salt}:{self._counter}".encode("utf-8")
            self._buffer += hashlib.sha256(block).digest()
            self._counter += 1
        taken, self._buffer = self._buffer[:count], self._buffer[count:]
        return taken

    def randbelow(self, n: int) -> int:
        """Uniform integer in ``[0, n)``."""
        if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
            raise GeneratorError("randbelow needs a positive integer")
        if n == 1:
            return 0
        width = ((n - 1).bit_length() + 7) // 8
        span = 256**width
        limit = span - (span % n)
        while True:
            value = int.from_bytes(self._take(width), "big")
            if value < limit:
                return value % n

    def randint(self, low: int, high: int) -> int:
        """Uniform integer in ``[low, high]`` inclusive."""
        if high < low:
            raise GeneratorError("randint needs low <= high")
        return low + self.randbelow(high - low + 1)

    def choice(self, options: Sequence[Any]) -> Any:
        if not options:
            raise GeneratorError("choice needs a non-empty sequence")
        return options[self.randbelow(len(options))]

    def chance(self, numerator: int, denominator: int) -> bool:
        """True with probability ``numerator / denominator``."""
        return self.randbelow(denominator) < numerator


@dataclass(frozen=True)
class Distractor:
    """The answer a learner would give after one specific, known mistake.

    ``description`` is plain language for the grader (and, after review, for
    feedback): what the learner did wrong, not how to fix it.
    """

    answer: str
    error_code: str
    description: str
    # What a learner would TYPE for this wrong answer (plain text, no LaTeX).
    # Used to prove the marker rejects it; optional.
    typed: str = ""


@dataclass(frozen=True)
class Step:
    """One line of the model working: what is done, and the value it produces.

    The values are what the method-mark layer looks for in a learner's working.
    """

    description: str
    value: str
    answer_type: str = ""  # explicit for structured values; empty keeps legacy inference

    def to_dict(self) -> Dict[str, str]:
        out = {"description": self.description, "value": self.value}
        if self.answer_type:
            out["answer_type"] = self.answer_type
        return out


@dataclass(frozen=True)
class GeneratedProblem:
    generator_id: str
    generator_version: int
    seed: int
    level: int
    skill: str
    question: str
    answer: str
    distractors: Tuple[Distractor, ...] = ()
    # Structured form of the problem, for verification and for later
    # equivalence checks. Not shown to learners.
    machine: Mapping[str, Any] = field(default_factory=dict)
    # One valid worked route, in order. This is reference evidence, not a mark
    # allocation: exam criteria and alternative routes come from the grading contract.
    steps: Tuple[Step, ...] = ()
    # How the final answer is marked by program (see services.math_marking.check):
    # {"answer_type", "expected": [plain-text answers], "rounding", "digits", "form", "typed"}
    marking: Mapping[str, Any] = field(default_factory=dict)

    @property
    def fingerprint(self) -> str:
        """Identity of the problem as the learner sees it.

        Different seeds can produce the same question, so "have they seen
        this" is tracked on this value, not on the seed.
        """
        return visible_question_fingerprint(self.question, self.machine.get('reference_images', {}).get('question'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "generator_id": self.generator_id,
            "generator_version": self.generator_version,
            "seed": self.seed,
            "level": self.level,
            "skill": self.skill,
            "question": self.question,
            "answer": self.answer,
            "fingerprint": self.fingerprint,
            "distractors": [
                {
                    "answer": d.answer,
                    "error_code": d.error_code,
                    "description": d.description,
                    "typed": d.typed,
                }
                for d in self.distractors
            ],
            "machine": dict(self.machine),
            "steps": [st.to_dict() for st in self.steps],
            "marking": dict(self.marking),
        }


def _drop_accepted_distractors(problem: "GeneratedProblem") -> Tuple["Distractor", ...]:
    """A listed wrong answer that the marker would accept as correct (it rounds to the right value, or is an
    equivalent form) is not a wrong answer: drop it, whatever the generator believed."""
    marking = problem.marking
    if not marking or not marking.get("expected"):
        return problem.distractors
    from services.math_marking import check

    kwargs = {k: marking[k] for k in ("rounding", "digits", "form") if k in marking}
    kept = []
    for d in problem.distractors:
        if d.typed:
            try:
                if check(marking["answer_type"], marking["expected"], d.typed, **kwargs).correct:
                    continue
            except Exception:
                pass
        kept.append(d)
    return tuple(kept)


class MathGenerator:
    """Base class. Subclasses set the class attributes and implement
    :meth:`_build`."""

    generator_id: str = ""
    version: int = 1
    levels: Tuple[int, ...] = ()
    # skill code -> {error code -> plain-language description}
    error_notes: Mapping[str, Mapping[str, str]] = {}
    # level -> skill codes that can appear at that level
    level_skills: Mapping[int, Tuple[str, ...]] = {}

    def generate(self, seed: int, level: int) -> GeneratedProblem:
        seed = validate_seed(seed)
        level = validate_level(level, self.levels)
        rng = SeededRandom(seed, salt=f"{self.generator_id}:{self.version}:{level}")
        problem = self._build(rng, seed, level)
        from .formatting import localise_money
        from .method_marks import complete_working

        problem = complete_working(problem)

        return replace(
            problem,
            question=localise_money(problem.question),
            answer=localise_money(problem.answer),
            distractors=_drop_accepted_distractors(problem),
        )

    def notes_for_level(self, level: int) -> Dict[str, str]:
        """Common-error notes for every skill that can appear at ``level``."""
        level = validate_level(level, self.levels)
        notes: Dict[str, str] = {}
        for skill in self.level_skills.get(level, ()):
            for code, description in self.error_notes.get(skill, {}).items():
                notes[f"{skill}.{code}"] = description
        return notes

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        raise NotImplementedError
