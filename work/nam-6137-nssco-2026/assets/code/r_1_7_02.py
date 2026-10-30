"""VIS-6137-1.7-02 -> ITEM-6137-1.7-017-INTERP: three climate graphs with twelve months each.

Rainfall bars (left axis, mm, 0-200) and monthly mean temperature line (right axis, degC, 0-35) on the
same scales in all three graphs. Series A and B rainfall are the notes' values (BL-6137-1.7.04-02/03);
A, B and C temperatures and C rainfall are original teaching values chosen to give the stated totals
and ranges: A 2,000 mm and 26-27 C; B 500 mm and 18-27 C (Southern Hemisphere summer-wet); C 20 mm
and 17-30 C. Invented data, not measured climates of real places.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.7-02'
ITEM = 'ITEM-6137-1.7-017-INTERP'
W, HQ, HA = 1000, 1100, 1440
MONTHS = 'JFMAMJJASOND'
SERIES = {
    'A': ([180, 160, 190, 180, 170, 160, 140, 130, 150, 170, 180, 190], [27, 27, 27, 26.5, 26.5, 26, 26, 26, 26.5, 27, 27, 27]),
    'B': ([100, 90, 80, 40, 10, 0, 0, 0, 5, 25, 60, 90], [27, 26, 25, 23, 20, 18, 18, 20, 23, 25, 26, 27]),
    'C': ([4, 5, 3, 1, 0, 0, 0, 0, 0, 1, 2, 4], [30, 29, 27, 24, 20, 17, 17, 19, 23, 26, 28, 30]),
}


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Climate graphs A, B and C (same scales; invented data)')
    axes = {}
    for k, key in enumerate('ABC'):
        y0 = 62 + k * 328
        fig.rect(20, y0, 960, 316, '#ffffff', GREY, 2, 8)
        fig.text(36, y0 + 36, key, 32, 'start', 'bold')
        ax = Axes(fig, 170, y0 + 54, 640, 200, (0, 12), (0, 200))
        ax.draw([], range(0, 201, 50), None, 'Rainfall (mm)', ylabel_x=96)
        rain, temp = SERIES[key]
        for m, v in enumerate(rain):
            fig.rect(ax.X(m + 0.12), ax.Y(v), ax.X(0.76) - ax.X(0), ax.Y(0) - ax.Y(v), C['blue'], 'none', 0)
            fig.text(ax.X(m + 0.5), ax.Y(0) + 32, MONTHS[m], 26, 'middle')
        tY = lambda t: ax.Y(t / 35 * 200)
        fig.line(ax.X(12), ax.Y(0), ax.X(12), ax.Y(200), INK, 2.5)
        for t in range(0, 36, 5):
            fig.line(ax.X(12), tY(t), ax.X(12) + 8, tY(t), INK, 2)
            fig.text(ax.X(12) + 14, tY(t) + 9, str(t), 26, 'start')
        fig.text(ax.X(12) + 100, y0 + 156, 'Temperature (°C)', 26, 'middle', 'bold', rotate=90)
        fig.path('M' + ' L'.join('%.1f %.1f' % (ax.X(m + 0.5), tY(t)) for m, t in enumerate(temp)), 'none', C['red'], 4)
        for m, t in enumerate(temp):
            fig.circle(ax.X(m + 0.5), tY(t), 5, C['red'], 'none', 0)
        axes[key] = (ax, y0)
    ky = HQ - 26
    fig.rect(40, ky - 22, 30, 24, C['blue'], 'none', 0)
    fig.text(80, ky, 'monthly rainfall total (left axis)', 26)
    fig.line(520, ky - 9, 570, ky - 9, C['red'], 4)
    fig.text(580, ky, 'monthly mean temperature (right)', 26)

    A = 'a'
    notes = {'A': 'total 2,000 mm; every month wet; range 1 °C', 'B': 'total 500 mm; wettest Dec–Mar, dry Jun–Aug; range 9 °C',
             'C': 'total 20 mm; range 13 °C'}
    for k, key in enumerate('ABC'):
        ax, y0 = axes[key]
        fig.text(132, y0 + 36, notes[key], 26, 'start', 'bold', C['answer'], A, halo=True)
        fig.marker(100, y0 + 27, str(k + 1), A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A: high rainfall in every month (2,000 mm a year) and a very small temperature range (1 °C): consistent with rainforest.'),
                 ('2', 'B: a marked wet season (wettest December to March) and dry months (June to August), 500 mm a year, with a larger range (9 °C): consistent with savannah.'),
                 ('3', 'C: very little rain (20 mm a year) and the largest range of the three (13 °C): consistent with an inland tropical desert.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    stats = {k: {'total_mm': sum(r), 'range_C': max(t) - min(t), 'min_C': min(t), 'max_C': max(t)} for k, (r, t) in SERIES.items()}
    spec = {
        'kind': 'three climate graphs, 12 months each; rainfall bars (left, 0-200 mm) and temperature line (right, 0-35 C); identical scales',
        'series': SERIES, 'derived': stats,
        'source': 'A and B rainfall from notes BL-6137-1.7.04-02/03; other monthly values original, constrained to the stated totals and ranges',
        'question_withholds': ['totals', 'ranges', 'vegetation names'],
        'independent_solution': ['A: year-round high rain, small range (1)', 'B: seasonal rain with dry months, larger range (1)',
                                 'C: very low rain, largest range -> desert (1)'],
    }
    checks = [
        check('twelve months in every series', all(len(r) == 12 == len(t) for r, t in SERIES.values())),
        check('totals 2,000 / 500 / 20 mm', [stats[k]['total_mm'] for k in 'ABC'] == [2000, 500, 20]),
        check('temperature ranges 26-27, 18-27, 17-30 C', [(stats[k]['min_C'], stats[k]['max_C']) for k in 'ABC'] == [(26, 27), (18, 27), (17, 30)]),
        check('C has the largest range of the three', stats['C']['range_C'] > stats['B']['range_C'] > stats['A']['range_C']),
        check('B wettest in the Southern Hemisphere summer months', SERIES['B'][0][0] == max(SERIES['B'][0]) and SERIES['B'][0][6] == 0),
        check('all values within the shared axes', all(0 <= v <= 200 for r, t in SERIES.values() for v in r) and all(0 <= v <= 35 for r, t in SERIES.values() for v in t)),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'rainforest', r'savannah', r'desert', r'2,000', r'500 mm', r'20 mm']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 62 + k * 328, 960, 316) for k in range(3)])


if __name__ == '__main__':
    main()
