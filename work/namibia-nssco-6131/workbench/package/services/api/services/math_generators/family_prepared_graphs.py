"""One bounded graph-reading recipe backed by immutable prepared PNG pairs."""
from fractions import Fraction
from .base import GeneratedProblem, MathGenerator, Step
from .formatting import number_latex
from .graph_bank import GENERATOR_ID, entries, references


class PreparedLineGraphsGenerator(MathGenerator):
    generator_id = GENERATOR_ID
    version = 1
    levels = (2,)
    level_skills = {2: ('gradient_from_graph',)}
    error_notes = {'gradient_from_graph': {'inverted': 'Divided horizontal change by vertical change.'}}

    def _build(self, rng, seed, level):
        bank = entries()
        entry = bank[rng.randbelow(len(bank))]
        xp, xq = entry['xp'], entry['xq']
        m = Fraction(entry['numerator'], entry['denominator'])
        yp, yq = m*xp+entry['intercept'], m*xq+entry['intercept']
        n = number_latex
        question = (f'The graph shows a straight line through $P$ and $Q$. '
                    f'$P$ has $x$-coordinate ${xp}$ and $Q$ has $x$-coordinate ${xq}$. '
                    'Read their $y$-coordinates from the graph and find the gradient of $PQ$. Show your working.')
        answer = (f'$P=({xp},{n(yp)})$, $Q=({xq},{n(yq)})$.\n\n'
                  f'$m=\\dfrac{{y_Q-y_P}}{{x_Q-x_P}}'
                  f'=\\dfrac{{{n(yq)}-({n(yp)})}}{{{xq}-({xp})}}'
                  f'=\\dfrac{{{n(yq-yp)}}}{{{xq-xp}}}={n(m)}$.')
        explanation = (f'$x_P={xp}$ and $x_Q={xq}$ are the horizontal coordinates. '
                       f'Reading the graph gives $y_P={n(yp)}$ and $y_Q={n(yq)}$. '
                       f'Here $m$ names the gradient: vertical change ${n(yq-yp)}$ divided by '
                       f'horizontal change ${xq-xp}$. Each minor square represents half a unit on both axes. '
                       'Keep the order of the two points the same in numerator and denominator. '
                       'A line falling from left to right has a negative gradient.')
        return GeneratedProblem(self.generator_id, self.version, seed, level, 'gradient_from_graph',
            question, answer, machine={'task':'gradient_from_graph','reference_images':references(entry),
                'gradient':[m.numerator,m.denominator], 'explanation':explanation},
            steps=(Step('Read coordinates and divide vertical change by horizontal change',str(m),'number_exact'),),
            marking={'answer_type':'number_exact','expected':[str(m)],'typed':str(m)})


GENERATORS = [PreparedLineGraphsGenerator()]
