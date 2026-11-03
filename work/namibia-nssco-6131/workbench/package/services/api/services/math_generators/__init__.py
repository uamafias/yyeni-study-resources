"""Registry of vetted math problem generators.

Generators live in this package, in code that is reviewed and tested. A card
refers to one by ``generator_id``; nothing executable is ever read from the
database or from an external caller.

    from services.math_generators import generate_problem
    problem = generate_problem("nssco_factorising_quadratics", seed=42, level=3)
"""

from __future__ import annotations

from typing import Dict, Tuple

from .base import (
    Distractor,
    GeneratedProblem,
    GeneratorError,
    MathGenerator,
    SeededRandom,
    Step,
    UnknownGeneratorError,
)
from .factorising_quadratics import FactorisingQuadraticsGenerator

_REGISTRY: Dict[str, MathGenerator] = {}


def register(generator: MathGenerator) -> None:
    if not generator.generator_id:
        raise GeneratorError("a generator needs a generator_id")
    if generator.generator_id in _REGISTRY:
        raise GeneratorError(f"generator already registered: {generator.generator_id}")
    _REGISTRY[generator.generator_id] = generator


def get_generator(generator_id: str) -> MathGenerator:
    try:
        return _REGISTRY[generator_id]
    except (KeyError, TypeError):
        raise UnknownGeneratorError(f"unknown generator: {generator_id!r}") from None


def registered_generator_ids() -> Tuple[str, ...]:
    return tuple(sorted(_REGISTRY))


def generate_problem(generator_id: str, seed: int, level: int) -> GeneratedProblem:
    return get_generator(generator_id).generate(seed, level)


register(FactorisingQuadraticsGenerator())


def _register_family_modules() -> None:
    """Register runtime recipes; ``family_visual_*`` are offline authoring inputs.

    Visual recipes register through family_prepared_visuals, which reads the
    immutable prepared bank rather than generating diagrams at runtime.
    """
    import importlib
    import pkgutil

    for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
        if info.name.startswith("family_") and not info.name.startswith("family_visual_"):
            module = importlib.import_module(f"{__name__}.{info.name}")
            for generator in module.GENERATORS:
                register(generator)


_register_family_modules()

__all__ = [
    "Distractor",
    "GeneratedProblem",
    "GeneratorError",
    "MathGenerator",
    "SeededRandom",
    "Step",
    "UnknownGeneratorError",
    "generate_problem",
    "get_generator",
    "register",
    "registered_generator_ids",
]
