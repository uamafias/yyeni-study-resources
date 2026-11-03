"""Program-side marking of final answers to maths questions.

``check(answer_type, expected, given, ...)`` says whether a learner's typed
answer is equivalent to the right one. It never guesses: when it cannot read an
answer, or the answer type needs a written reason, it says so and a judge (an AI
or a phrase list) decides instead.
"""

from .check import Verdict, check
from .parse import official_alternatives

__all__ = ["Verdict", "check", "official_alternatives"]
