"""Create the recipe cards for a generated lesson.

A level's deck is about ten ordinary ``Flashcard`` rows that each carry a recipe
(``generator_id`` + ``generator_params = {"level": n, "slot": k}``) and one
canonical example as their visible question/answer. This module plans and
creates them. It only ever *adds* cards, is idempotent (a level/slot that
already exists is skipped) and defaults to a dry run.

Not imported by ``services.math_generators``; it needs the database models.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Sequence, Set, Tuple

from . import get_generator
from .base import GeneratorError, question_identity_text
from .presentation import worked_example
from .graph_bank import problem_references

SLOTS_PER_LEVEL = 10
MAX_SLOTS_PER_LEVEL = 100  # a guard against a typo, not a design limit
_SEED_STEP = 7919  # a prime, so successive tries never revisit a seed


@dataclass(frozen=True)
class PlannedCard:
    level: int
    slot: int
    seed: int
    question: str
    answer: str
    explanation: Optional[str] = None
    question_image_url: Optional[str] = None
    answer_image_url: Optional[str] = None


@dataclass
class RecipeReport:
    applied: bool
    planned: List[PlannedCard] = field(default_factory=list)
    skipped_existing: List[Tuple[int, int]] = field(default_factory=list)
    skipped_excluded: List[Tuple[int, int]] = field(default_factory=list)
    cards_to_deactivate: int = 0
    edited_excluded_card_ids: List[int] = field(default_factory=list)
    created_card_ids: List[int] = field(default_factory=list)


def _normalise(text: Optional[str]) -> str:
    return " ".join((text or "").split())


def plan_level_cards(
    generator_id: str,
    level: int,
    slots: Iterable[int],
    *,
    taken_questions: Set[str],
    enforce_workbench_policy: bool = False,
) -> List[PlannedCard]:
    """One canonical example per requested slot, all distinct from each other
    and from ``taken_questions`` (normalised question text already in the lesson).

    The seeds are a fixed function of (level, slot), so planning twice gives the
    same examples.
    """
    generator = get_generator(generator_id)
    used = {_normalise(q) for q in taken_questions}
    planned: List[PlannedCard] = []
    for slot in slots:
        if enforce_workbench_policy:
            from ..math_workbench.selection import slot_allowed
            if not slot_allowed(generator_id, {'level': level, 'slot': slot}):
                continue
        seed = level * 1000 + slot
        for _ in range(500):
            problem = generator.generate(seed, level)
            if enforce_workbench_policy:
                from ..math_workbench.legacy import rejection_reasons
                if rejection_reasons(problem):
                    seed += _SEED_STEP
                    continue
            key = question_identity_text(problem.question, problem.machine.get('reference_images', {}).get('question'))
            if key not in used:
                used.add(key)
                images = problem_references(problem)
                planned.append(PlannedCard(level, slot, seed, problem.question, problem.answer,
                                           worked_example(problem),
                                           images.get('question'),
                                           images.get('answer')))
                break
            seed += _SEED_STEP
        else:
            raise GeneratorError(
                f"could not find {len(list(slots))} distinct examples at level {level}"
            )
    return planned


