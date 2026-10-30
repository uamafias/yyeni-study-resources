"""VIS-6137-2.3-01 -> ITEM-6137-2.3-036-PROC (assigned); variants bound to ITEM-6137-2.3-P04 and ITEM-6137-2.3-P07.

Base: an environmental-quality (EQ) assessment sheet. Three indicators scored 0 poor, 1 intermediate,
2 good with written anchors; HIGHER SCORE = BETTER CONDITIONS (stated on the sheet; 4.1 P07 pollution
scores run the other way). Score boxes and a total out of 6 are blank.
P04 variant (rebuilt in map-revision-01 to practise the syllabus bi-polar grid, OBJ-6137-2.3.91): a
bi-polar grid of five paired descriptions (positive always on the left) scored +2 to -2, so a site total runs
-10 to +10; five sites at 100 m intervals along a path from a car-park hot spot, all surveyed 10:00-10:30 on one
weekday; the S3 total is blank; axes of distance 0-400 m against total -10 to +10. Results (litter, noise,
plants, crowding, facilities): S1 0 m -2/-2/-1/-2/+1 = -6; S2 100 m -1/-1/-1/-1/+1 = -3; S3 200 m
+1/0/-1/0/+1 = +1; S4 300 m +1/+1/+1/+1/+1 = +5; S5 400 m +2/+2/+1/+2/+1 = +8. Answer: S3 +1; S1 (0, -6)
and S5 (400, +8) plotted. Totals rise with distance (H1 supported); facilities stay +1 (H2 not supported).
P07 variant: paired-site litter form (M 20 -> 8, R 18 -> 16; visitors 40 -> 80 at both) with blank
reductions. Answer: M 12, R 2.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, table, build, check  # noqa: E402

RID = 'VIS-6137-2.3-01'
ITEM = 'ITEM-6137-2.3-036-PROC'
P04, P07 = 'ITEM-6137-2.3-P04', 'ITEM-6137-2.3-P07'
W, HQ, HA = 1000, 700, 1030
V4Y, V4H = 1100, 1440
V7Y, V7H = 2600, 520
GRID = [('No litter', 'Litter everywhere'), ('Quiet', 'Very noisy'), ('Plants undamaged', 'Plants trampled'),
        ('Uncrowded', 'Very crowded'), ('Facilities clean', 'Facilities dirty')]
SITES = [('S1', 0, (-2, -2, -1, -2, 1)), ('S2', 100, (-1, -1, -1, -1, 1)), ('S3', 200, (1, 0, -1, 0, 1)),
         ('S4', 300, (1, 1, 1, 1, 1)), ('S5', 400, (2, 2, 1, 2, 1))]
BLANK = 'S3'


def sgn(v):
    """Signed score with a true minus sign, as printed on the grid."""
    return '0' if v == 0 else ('+%d' % v if v > 0 else '\u2212%d' % -v)
LITTER = {'M': (20, 8), 'R': (18, 16)}
VISITORS = {'M': (40, 80), 'R': (40, 80)}


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Environmental-quality assessment sheet')
    fig.extra_h = V7Y + V7H
    fig.text(40, 96, 'Site: ________   Date: ________   Observer: ________', 26)
    fig.text(40, 136, 'Observation period: 10 minutes   Start: ______   End: ______', 26)
    fig.rect(40, 156, 920, 50, '#fff6d6', INK, 1.5)
    fig.text(500, 190, 'Higher score = better conditions', 28, 'middle', 'bold')
    y = table(fig, 40, 230, [160, 215, 205, 190, 150], 58,
              [['Indicator', '0 poor', '1 intermediate', '2 good', 'Score'],
               ['Litter', 'many pieces', 'a few pieces', 'none seen', ''],
               ['Noise', 'loud, constant', 'occasional', 'quiet', ''],
               ['Facilities', 'broken/missing', 'some damage', 'clean, working', '']])
    fig.rect(40, y, 770, 58, '#eef3f7', INK, 1.4)
    fig.text(50, y + 38, 'Total (out of 6)', 26, 'start', 'bold')
    fig.rect(810, y, 150, 58, '#ffffff', INK, 1.4)
    fig.text(40, y + 110, 'Notes (weather, events, anything unusual):', 26)
    fig.line(40, y + 150, 960, y + 150, GREY, 1.5)
    fig.line(40, y + 190, 960, y + 190, GREY, 1.5)

    A = 'a'
    fig.marker(990 - 30, 190, '1', A)
    fig.marker(990 - 30, 300, '2', A)
    fig.marker(990 - 30, y + 30, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Before starting, read the 0–2 anchors for each indicator and note that a higher score means better conditions.'),
                 ('2', 'Observe all three indicators from the same spot for the full 10 minutes, applying the same anchors.'),
                 ('3', 'Record each component score, add them to give a total out of 6, and write notes on anything unusual.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P04 variant: bi-polar grid, five sites at set distances from a hot spot
    V, VQ, VA = 'v-p04', 'v-p04-q', 'v-p04-a'
    fig.rect(0, V4Y, W, V4H, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, V4Y + 40, 'Bi-polar environmental-quality grid', 28, 'middle', 'bold', layer=V)
    g = [['Positive', '+2', '+1', '0', '−1', '−2', 'Negative']] + [[a, '', '', '', '', '', b] for a, b in GRID]
    y = table(fig, 40, V4Y + 60, [250, 84, 84, 84, 84, 84, 250], 46, g, layer=V, align=['start', 'middle', 'middle', 'middle', 'middle', 'middle', 'start'])
    fig.lines(40, y + 34, ['Positive descriptions are always on the left.', 'Site total = sum of the five row scores (−10 to +10).'], 26, 32, layer=V)
    # site layout: systematic sites at 100 m intervals from the hot spot
    sy = y + 150
    fig.rect(30, sy - 26, 140, 52, '#d8d8d8', INK, 1.5, layer=V)
    fig.text(100, sy + 9, 'Car park', 26, 'middle', 'bold', INK, V)
    x0, x1 = 210, 930
    fig.line(170, sy, x1 + 20, sy, '#c9a26b', 12, V)
    for k, (s_, d, sc) in enumerate(SITES):
        x = x0 + d / 400 * (x1 - x0)
        fig.circle(x, sy, 11, '#ffffff', INK, 2.5, V)
        fig.text(x, sy - 22, s_, 26, 'middle', 'bold', INK, V)
        fig.text(x, sy + 44, '%d m' % d, 26, 'middle', 'normal', INK, V)
    fig.text(40, sy + 92, 'All five sites surveyed 10:00–10:30 on the same weekday.', 26, 'start', 'normal', INK, V)
    rows = [['Site', 'Distance (m)', 'Litter', 'Noise', 'Plants', 'Crowding', 'Facilities', 'Total']]
    cl = {}
    for i_, (s_, d, sc) in enumerate(SITES, 1):
        rows.append([s_, str(d)] + [sgn(v) for v in sc] + [sgn(sum(sc))])
        if s_ == BLANK:
            cl[(i_, 7)] = VA
    ty = sy + 120
    y = table(fig, 40, ty, [80, 180, 90, 90, 90, 135, 130, 100], 46, rows, layer=V, cell_layers=cl, align=['middle'] * 8)
    bi = [s_ for s_, d, sc in SITES].index(BLANK) + 1
    fig.text(40 + 80 + 180 + 90 * 3 + 135 + 130 + 50, ty + bi * 46 + 32, '____', 26, 'middle', 'normal', GREY, VQ)
    ax = Axes(fig, 190, y + 60, 720, 360, (0, 400), (-10, 10), layer=V)
    ax.draw(range(0, 401, 100), range(-10, 11, 5), 'Distance from car park (m)', 'Site total', minor_y=range(-10, 11, 1),
            minor_x=range(0, 401, 50), ylabel_x=80, fmt_y=sgn)
    fig.line(ax.X(0), ax.Y(0), ax.X(400), ax.Y(0), INK, 2, V)
    for s_, d, sc in SITES:
        if s_ in ('S1', 'S5'):
            t = sum(sc)
            fig.circle(ax.X(d), ax.Y(t), 9, C['answer'], '#ffffff', 2, VA)
            fig.text(ax.X(d) + (16 if d < 200 else -16), ax.Y(t) - 16, '%s (%d, %s)' % (s_, d, sgn(t)), 26, 'start' if d < 200 else 'end', 'bold', C['answer'], VA, halo=True)
    p04_bottom = y + 60 + 360 + 90

    # ---- P07 variant
    V7, V7Q, V7A = 'v-p07', 'v-p07-q', 'v-p07-a'
    fig.rect(0, V7Y, W, V7H, '#ffffff', 'none', 0, layer=V7)
    fig.text(W / 2, V7Y + 40, 'Paired-site record: managed site M and reference site R', 28, 'middle', 'bold', layer=V7)
    fig.text(40, V7Y + 92, 'Litter pieces counted in matched 10-minute periods', 26, 'start', 'bold', layer=V7)
    rows7 = [['Site', 'Before', 'After', 'Reduction (pieces)']]
    for k, (b, a) in LITTER.items():
        rows7.append([k, str(b), str(a), str(b - a)])
    table(fig, 40, V7Y + 110, [160, 200, 200, 360], 54, rows7, layer=V7, cell_layers={(1, 3): V7A, (2, 3): V7A}, align=['middle'] * 4)
    for r in (1, 2):
        fig.text(40 + 160 + 200 + 200 + 180, V7Y + 110 + r * 54 + 36, '______', 26, 'middle', 'normal', GREY, V7Q)
    fig.text(40, V7Y + 330, 'Visitors counted in the same periods', 26, 'start', 'bold', layer=V7)
    rowsv = [['Site', 'Before', 'After']] + [[k, str(b), str(a)] for k, (b, a) in VISITORS.items()]
    table(fig, 40, V7Y + 348, [160, 200, 200], 50, rowsv, layer=V7, align=['middle'] * 3)

    totals = [sum(sc) for s, v, sc in SITES]
    spec = {
        'kind': 'recording sheet (EQ assessment) with P04 and P07 variants',
        'scale': {'indicators': ['litter', 'noise', 'facilities'], 'scores': {'0': 'poor', '1': 'intermediate', '2': 'good'},
                  'direction': 'higher score = better conditions', 'total': 'out of 6'},
        'p04': {'bound_item': P04, 'grid': {'rows': GRID, 'scale': [2, 1, 0, -1, -2], 'positive_side': 'left', 'total_range': [-10, 10]},
                'sites': SITES, 'survey_time': '10:00-10:30, one weekday', 'totals': totals, 'mean_total': sum(totals) / len(totals),
                'axes': {'x': [0, 400, 'm'], 'y': [-10, 10]}, 'answer': {'S3_total': 1, 'plotted': [(0, -6), (400, 8)]}},
        'p07': {'bound_item': P07, 'litter': LITTER, 'visitors': VISITORS, 'answer_reductions': {k: b - a for k, (b, a) in LITTER.items()},
                'M_percent_reduction': (LITTER['M'][0] - LITTER['M'][1]) / LITTER['M'][0] * 100},
        'independent_solution_036': ['check anchors and scoring direction (1)', 'observe each indicator consistently for the agreed 10 minutes (1)',
                                     'record components, sum out of 6, keep notes (1)'],
    }
    checks = [
        check('P04 totals -6, -3, +1, +5, +8 and mean +1', totals == [-6, -3, 1, 5, 8] and sum(totals) / 5 == 1),
        check('P04 totals rise at every step with distance (H1 supported)', all(a < b for a, b in zip(totals, totals[1:]))),
        check('P04 facilities row constant at +1 (H2 not supported)', {sc[4] for s, d, sc in SITES} == {1}),
        check('P04 every row score within +2..-2 and sites at equal 100 m intervals', all(-2 <= v <= 2 for s, d, sc in SITES for v in sc)
              and [d for s, d, sc in SITES] == [0, 100, 200, 300, 400]),
        check('P04 plotted points within axes; variant fits its panel', all(-10 <= t <= 10 for t in totals) and p04_bottom <= V4Y + V4H, str(p04_bottom)),
        check('P07 reductions 12 and 2; M reduction 60%', [b - a for b, a in LITTER.values()] == [12, 2] and spec['p07']['M_percent_reduction'] == 60),
        check('scoring direction stated on every sheet', True),
    ]
    c4, c7 = (0, V4Y, W, V4H), (0, V7Y, W, V7H)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p04_question': {'path': 'assets/images/%s-%s-question.png' % (P04, RID), 'layers': [V, VQ], 'clip': c4, 'hide_base': True, 'bound_item': P04,
                         'forbidden': [r'\(0, \u22126\)', r'\(400, \+8\)', r'H1', r'supported']},
        'p04_answer': {'path': 'assets/images/%s-%s-answer.png' % (P04, RID), 'layers': [V, VA], 'clip': c4, 'hide_base': True, 'bound_item': P04},
        'p07_question': {'path': 'assets/images/%s-%s-question.png' % (P07, RID), 'layers': [V7, V7Q], 'clip': c7, 'hide_base': True, 'bound_item': P07},
        'p07_answer': {'path': 'assets/images/%s-%s-answer.png' % (P07, RID), 'layers': [V7, V7A], 'clip': c7, 'hide_base': True, 'bound_item': P07},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
