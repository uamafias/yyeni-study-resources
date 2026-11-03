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
            from services.math_workbench.selection import slot_allowed
            if not slot_allowed(generator_id, {'level': level, 'slot': slot}):
                continue
        seed = level * 1000 + slot
        for _ in range(500):
            problem = generator.generate(seed, level)
            if enforce_workbench_policy:
                from services.math_workbench.legacy import rejection_reasons
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


def create_recipe_cards(
    db,
    *,
    generator_id: str,
    classroom_id: int,
    topic_bucket_id: int,
    created_by_user_id: int,
    levels: Sequence[int],
    slots_per_level: int = SLOTS_PER_LEVEL,
    apply: bool = False,
) -> RecipeReport:
    """Plan (and, with ``apply=True``, create) the recipe cards for ``levels``."""
    from models import Classroom, Flashcard, Section, TopicBucket, User

    generator = get_generator(generator_id)
    if not isinstance(levels, (list, tuple, range)) or len(levels) == 0:
        raise GeneratorError("levels must be a non-empty list of integers")
    if any(isinstance(level, bool) or not isinstance(level, int) for level in levels):
        raise GeneratorError("levels must be a non-empty list of integers")
    # A level listed twice (e.g. `--levels 1 1`) is one level: without this both
    # passes would see every slot as missing and create each card twice.
    levels = list(dict.fromkeys(levels))
    for level in levels:
        if level not in generator.levels:
            raise GeneratorError(f"level {level} is not a level of {generator_id}")
    if isinstance(slots_per_level, bool) or not isinstance(slots_per_level, int):
        raise GeneratorError("slots_per_level must be a whole number")
    if slots_per_level < 1:
        raise GeneratorError("slots_per_level must be at least 1")
    if slots_per_level > MAX_SLOTS_PER_LEVEL:
        raise GeneratorError(f"slots_per_level must be at most {MAX_SLOTS_PER_LEVEL}")

    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if classroom is None:
        raise GeneratorError(f"classroom {classroom_id} not found")
    lesson = db.query(TopicBucket).filter(TopicBucket.id == topic_bucket_id).first()
    if lesson is None:
        raise GeneratorError(f"lesson {topic_bucket_id} not found")
    section = db.query(Section).filter(Section.id == lesson.section_id).first()
    if section is None or section.classroom_id != classroom.id:
        raise GeneratorError(f"lesson {topic_bucket_id} does not belong to classroom {classroom_id}")
    if db.query(User).filter(User.id == created_by_user_id).first() is None:
        raise GeneratorError(f"user {created_by_user_id} not found")

    existing_cards = (
        db.query(Flashcard)
        .filter(Flashcard.classroom_id == classroom.id, Flashcard.topic_bucket_id == lesson.id)
        .all()
    )
    existing_slots = {
        (card.generator_params.get("level"), card.generator_params.get("slot"))
        for card in existing_cards
        if card.generator_id == generator_id and isinstance(card.generator_params, dict)
    }
    taken = {question_identity_text(card.question, card.question_image_url) for card in existing_cards}

    report = RecipeReport(applied=apply)
    from services.math_workbench.selection import slot_allowed, retirement_plan
    retire, edited = retirement_plan([c for c in existing_cards if c.generator_id == generator_id])
    report.cards_to_deactivate = len(retire)
    report.edited_excluded_card_ids = edited
    for level in levels:
        wanted = [slot for slot in range(1, slots_per_level + 1) if (level, slot) not in existing_slots]
        report.skipped_existing.extend(
            (level, slot) for slot in range(1, slots_per_level + 1) if (level, slot) in existing_slots
        )
        if not wanted:
            continue
        report.skipped_excluded.extend((level, slot) for slot in wanted
            if not slot_allowed(generator_id, {'level': level, 'slot': slot}))
        planned = plan_level_cards(generator_id, level, wanted, taken_questions=taken,
                                   enforce_workbench_policy=True)
        taken |= {question_identity_text(p.question, p.question_image_url) for p in planned}
        report.planned.extend(planned)

    if apply:
        for row in retire:
            row.is_active = False
        for card in report.planned:
            row = Flashcard(
                card_uuid=str(uuid.uuid4()),
                classroom_id=classroom.id,
                topic_bucket_id=lesson.id,
                question=card.question,
                answer=card.answer,
                explanation=card.explanation,
                question_image_url=card.question_image_url,
                answer_image_url=card.answer_image_url,
                source="teacher",
                created_by_user_id=created_by_user_id,
                is_active=True,
                generator_id=generator_id,
                generator_params={"level": card.level, "slot": card.slot, "canonical_seed": card.seed},
            )
            db.add(row)
            db.flush()
            report.created_card_ids.append(row.id)
        db.commit()
    return report
