"""VIS-6137-2.4-01 -> ITEM-6137-2.4-012-INTERP: three-month stacked bar chart of solar and hydro output.

Values (card and notes BL-6137-2.4.03-26): solar 2, 4, 6 and hydro 6, 4, 2 energy units in months 1-3.
Stacked bars make each month's combined output (8) visible without printing it. Demand is not shown,
and the chart covers three months only (both stated on the figure).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-2.4-01'
ITEM = 'ITEM-6137-2.4-012-INTERP'
W, HQ, HA = 1000, 720, 1040
SOLAR = [2, 4, 6]
HYDRO = [6, 4, 2]
SC, HC = '#e0b43c', '#2f6fae'


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Renewable electricity output, months 1–3')
    ax = Axes(fig, 170, 90, 600, 460, (0, 3), (0, 10))
    ax.draw([], range(0, 11, 2), None, 'Output (energy units)', minor_y=range(1, 10, 2), ylabel_x=80)
    for m in range(3):
        x0, x1 = ax.X(m + 0.2), ax.X(m + 0.8)
        fig.rect(x0, ax.Y(SOLAR[m]), x1 - x0, ax.Y(0) - ax.Y(SOLAR[m]), SC, INK, 2)
        fig.rect(x0, ax.Y(SOLAR[m] + HYDRO[m]), x1 - x0, ax.Y(SOLAR[m]) - ax.Y(SOLAR[m] + HYDRO[m]), HC, INK, 2)
        fig.text((x0 + x1) / 2, ax.Y(SOLAR[m] / 2) + 10, str(SOLAR[m]), 28, 'middle', 'bold', INK)
        fig.text((x0 + x1) / 2, ax.Y(SOLAR[m] + HYDRO[m] / 2) + 10, str(HYDRO[m]), 28, 'middle', 'bold', '#ffffff')
        fig.text((x0 + x1) / 2, ax.Y(0) + 36, 'Month %d' % (m + 1), 26, 'middle', 'bold')
    fig.rect(800, 200, 30, 30, HC, INK, 1.5)
    fig.text(840, 224, 'hydro', 26)
    fig.rect(800, 250, 30, 30, SC, INK, 1.5)
    fig.text(840, 274, 'solar', 26)
    fig.text(W / 2, HQ - 60, 'Demand is not shown. Months outside 1–3 are not shown.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.line(ax.X(0.1), ax.Y(8), ax.X(2.9), ax.Y(8), C['answer'], 3, A, dash='10 7')
    fig.text(ax.X(3) + 20, ax.Y(8) - 20, 'total 8', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(ax.X(3) + 20, ax.Y(8) + 12, 'each month', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(ax.X(1.5), ax.Y(9.3), '1', A)
    fig.marker(ax.X(3) + 40, ax.Y(8) - 70, '2', A)
    fig.marker(W / 2 - 360, HQ - 70, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Solar output rises (2, 4, 6) while hydro output falls (6, 4, 2).'),
                 ('2', 'Their combined output stays at 8 units in every month: the opposite trends offset each other.'),
                 ('3', 'The chart cannot show whether 8 units meets demand, or what happens in the rest of the year.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {'kind': 'stacked bar chart, 3 months', 'solar': SOLAR, 'hydro': HYDRO, 'unit': 'energy units per month',
            'totals': [s + h for s, h in zip(SOLAR, HYDRO)], 'stated_limits': ['demand not shown', 'only months 1-3'],
            'question_withholds': ['total', 'constant'],
            'independent_solution': ['solar rises, hydro falls (1)', 'combined 8 each month (1)', 'no demand or rest-of-year evidence (1)']}
    checks = [check('totals are 8 every month', all(s + h == 8 for s, h in zip(SOLAR, HYDRO))),
              check('values match card and notes', (SOLAR, HYDRO) == ([2, 4, 6], [6, 4, 2])),
              check('bars within 0-10 axis', all(s + h <= 10 for s, h in zip(SOLAR, HYDRO)))]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'total', r'constant']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
