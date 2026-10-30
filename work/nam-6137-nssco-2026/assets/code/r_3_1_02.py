"""VIS-6137-3.1-02 -> ITEM-6137-3.1-027-INTERP: birth and death rates in four model stages.

Paired bars per stage (rates per 1,000 per year), values from notes BL-6137-3.1.06-06: births 40, 40,
25, 11; deaths 38, 15, 10, 10. Rates only: no population totals are drawn (handover requirement).
The answer side adds the natural-change gaps 2, 25, 15, 1 per 1,000.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-3.1-02'
ITEM = 'ITEM-6137-3.1-027-INTERP'
W, HQ, HA = 1000, 720, 1060
BIRTHS = [40, 40, 25, 11]
DEATHS = [38, 15, 10, 10]
BC, DC = '#2f6fae', '#9a9a9a'


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Birth and death rates in four model stages (illustrative)')
    ax = Axes(fig, 160, 90, 640, 460, (0, 4), (0, 50))
    ax.draw([], range(0, 51, 10), None, 'Rate per 1,000 people per year', minor_y=range(5, 50, 10), ylabel_x=80)
    for s in range(4):
        for k, (vals, col) in enumerate(((BIRTHS, BC), (DEATHS, DC))):
            x0 = ax.X(s + 0.15 + k * 0.36)
            x1 = ax.X(s + 0.15 + k * 0.36 + 0.32)
            fig.rect(x0, ax.Y(vals[s]), x1 - x0, ax.Y(0) - ax.Y(vals[s]), col, INK, 1.5)
            fig.text((x0 + x1) / 2, ax.Y(vals[s]) - 10, str(vals[s]), 26, 'middle', 'bold')
        fig.text(ax.X(s + 0.5), ax.Y(0) + 36, 'Stage %d' % (s + 1), 26, 'middle', 'bold')
    fig.rect(820, 200, 30, 30, BC, INK, 1.5)
    fig.text(860, 224, 'births', 26)
    fig.rect(820, 250, 30, 30, DC, INK, 1.5)
    fig.text(860, 274, 'deaths', 26)
    fig.text(W / 2, HQ - 40, 'Rates are illustrative model values, not data for real countries.', 26, 'middle', 'normal', GREY)

    A = 'a'
    for s in range(4):
        xg = ax.X(s + 0.83)
        fig.line(xg, ax.Y(BIRTHS[s]), xg, ax.Y(DEATHS[s]), C['answer'], 4, A)
        fig.text(xg + 6, (ax.Y(BIRTHS[s]) + ax.Y(DEATHS[s])) / 2 + 9 - (14 if s in (0, 3) else 0), str(BIRTHS[s] - DEATHS[s]), 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(ax.X(1.5), ax.Y(47), '1', A)
    fig.marker(ax.X(3.5), ax.Y(30), '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation (gap = births − deaths)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'Natural-change gaps are 2, 25, 15 and 1 per 1,000: the gap widens as deaths fall (stage 2), then narrows as births fall.'),
                 ('2', 'The largest gap is in stage 2 (40 − 15 = 25 per 1,000).'),
                 ('3', 'These are rates; a population total is a different, accumulated measure not shown here.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    gaps = [b - d for b, d in zip(BIRTHS, DEATHS)]
    spec = {'kind': 'paired bar chart of model rates (per 1,000 per year)', 'births': BIRTHS, 'deaths': DEATHS, 'gaps': gaps,
            'source': 'notes BL-6137-3.1.06-06 (illustrative model values)', 'no_population_totals': True,
            'question_withholds': ['gap values', 'natural increase'],
            'independent_solution': ['gaps 2, 25, 15, 1: widen then narrow (1)', 'component rates from the chart (1)', 'rates are not totals (1)']}
    checks = [check('gaps 2, 25, 15, 1', gaps == [2, 25, 15, 1]), check('largest gap in stage 2', gaps.index(max(gaps)) == 1),
              check('no population-total series drawn', True), check('all values within 0-50', all(0 <= v <= 50 for v in BIRTHS + DEATHS))]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'gap', r'natural']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
