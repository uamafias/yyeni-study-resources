"""VIS-6137-4.1-03 -> ITEM-6137-4.1-046-INTERP (assigned); variant bound to ITEM-6137-4.1-P07.

Base (notes BL-6137-4.1.07-20, BL-6137-4.1.08-14): paired before/after chart of pollution scores on a
scale where 0 = least and 5 = most pollution (opposite in direction to the 2.3 EQ score). Managed site
M 4 -> 2; reference R 3 -> 4; other influences not fully controlled (stated on the figure). M and R
differ by colour, line style and marker shape. The answer adds the changes (M -2, less pollution;
R +1, more pollution) and the attribution limit.
P07 variant: paired-site sheet (scores and visitor counts 10 -> 40 at both sites) with the change and
condition cells blank, and before/after axes 0-5 with R plotted. Answer: M -2 better, R +1 worse; M
plotted at 4 and 2.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, table, build, check  # noqa: E402

RID = 'VIS-6137-4.1-03'
ITEM = 'ITEM-6137-4.1-046-INTERP'
P07 = 'ITEM-6137-4.1-P07'
W, HQ, HA = 1000, 690, 1010
V7Y, V7H = 1080, 930
SCORES = {'M': (4, 2), 'R': (3, 4)}
VISITORS = {'M': (10, 40), 'R': (10, 40)}
STYLE = {'M': ('#1b7f5b', None, 'circle', 'M managed site'), 'R': ('#a33b2b', '12 8', 'square', 'R reference site')}


def mark(fig, kind, x, y, col, layer):
    if kind == 'circle':
        fig.circle(x, y, 11, col, '#ffffff', 2.5, layer)
    else:
        fig.rect(x - 11, y - 11, 22, 22, col, '#ffffff', 2.5, layer=layer)


def series(fig, ax, k, layer, labels=True):
    col, dash, kind, _ = STYLE[k]
    b, a = SCORES[k]
    ax.polyline([(0.5, b), (1.5, a)], col, 5, layer, dash=dash)
    for x, v in ((0.5, b), (1.5, a)):
        mark(fig, kind, ax.X(x), ax.Y(v), col, layer)
    if labels:
        fig.text(ax.X(0.5) - 22, ax.Y(b) + 9, '%s %d' % (k, b), 26, 'end', 'bold', col, layer, halo=True)
        fig.text(ax.X(1.5) - 10, ax.Y(a) + (44 if a < b else -22), '%s %d' % (k, a), 26, 'end', 'bold', col, layer, halo=True)


def key(fig, x, y, layer, keys='MR'):
    for i, k in enumerate(keys):
        col, dash, kind, lab = STYLE[k]
        xx = x + i * 340
        fig.line(xx, y, xx + 60, y, col, 5, layer, dash=dash)
        mark(fig, kind, xx + 30, y, col, layer)
        fig.text(xx + 76, y + 9, lab, 26, layer=layer)


def scale_box(fig, y, layer):
    fig.rect(40, y, 920, 50, '#fff6d6', INK, 1.5, layer=layer)
    fig.text(500, y + 34, 'Pollution score: 0 = least pollution, 5 = most pollution', 26, 'middle', 'bold', layer=layer)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Pollution scores before and after: managed and reference sites')
    fig.extra_h = V7Y + V7H
    scale_box(fig, 64, 'base')
    ax = Axes(fig, 220, 150, 520, 360, (0, 2), (0, 5))
    ax.draw([], range(0, 6), None, 'Pollution score', ylabel_x=120)
    for x, lab in ((0.5, 'Before'), (1.5, 'After')):
        fig.text(ax.X(x), ax.Y(0) + 36, lab, 26, 'middle', 'bold')
    for k in 'MR':
        series(fig, ax, k, 'base')
    key(fig, 120, 594, 'base')
    fig.text(500, 650, 'Weather, cleaning times and other users were not fully controlled.', 26, 'middle', 'normal', GREY)

    A = 'a'
    for k, txt in (('M', 'M: −2 (less pollution)'), ('R', 'R: +1 (more pollution)')):
        col = STYLE[k][0]
        fig.text(ax.X(1.5) + 26, ax.Y(SCORES[k][1]) + 9, txt, 26, 'start', 'bold', col, A, halo=True)
    fig.marker(ax.X(1.5) + 40, ax.Y(2) + 44, '1', A)
    fig.marker(ax.X(1.5) + 40, ax.Y(4) - 40, '2', A)
    fig.marker(950, 640, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation (lower score = less pollution)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Recorded pollution improves at the managed site: 4 → 2, a fall of 2 points.'),
                 ('2', 'It worsens at the reference site: 3 → 4, a rise of 1 point. The paired changes differ.'),
                 ('3', 'Other influences were not fully controlled, so the chart does not isolate the management change as the cause.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P07 variant: paired sheet and axes
    V, VQ, VA = 'v-p07', 'v-p07-q', 'v-p07-a'
    y = V7Y
    fig.rect(0, y, W, V7H, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, y + 40, 'Paired-site record sheet and plotting axes', 28, 'middle', 'bold', layer=V)
    scale_box(fig, y + 64, V)
    rows = [['Site', 'Before', 'After', 'Change (points)', 'Condition']]
    cl = {}
    for i, (k, (b, a)) in enumerate(SCORES.items(), 1):
        rows.append([k, str(b), str(a), ('%+d' % (a - b)).replace('-', '−'), 'better' if a < b else 'worse'])
        cl[(i, 3)] = VA
        cl[(i, 4)] = VA
    ty = table(fig, 70, y + 140, [130, 130, 130, 240, 230], 54, rows, layer=V, cell_layers=cl, align=['middle'] * 5)
    fig.text(70, ty + 40, 'Visitors counted in the same matched periods:', 26, 'start', 'bold', layer=V)
    ty = table(fig, 70, ty + 58, [130, 130, 130], 50, [['Site', 'Before', 'After']] + [[k, str(b), str(a)] for k, (b, a) in VISITORS.items()],
               layer=V, align=['middle'] * 3)
    a7 = Axes(fig, 220, ty + 50, 480, 300, (0, 2), (0, 5), layer=V)
    a7.draw([], range(0, 6), None, 'Pollution score', ylabel_x=120)
    for x, lab in ((0.5, 'Before'), (1.5, 'After')):
        fig.text(a7.X(x), a7.Y(0) + 36, lab, 26, 'middle', 'bold', layer=V)
    series(fig, a7, 'R', V, labels=False)
    series(fig, a7, 'M', VA, labels=False)
    for k in 'MR':
        col, dash, kind, lab = STYLE[k]
        yk = ty + 120 + (0 if k == 'M' else 60)
        fig.line(740, yk, 800, yk, col, 5, V, dash=dash)
        mark(fig, kind, 770, yk, col, V)
        fig.text(812, yk + 9, k + (' managed' if k == 'M' else ' reference'), 26, layer=V)
    y_end = a7.Y(0) + 60

    ch = {k: a - b for k, (b, a) in SCORES.items()}
    spec = {
        'kind': 'paired before/after pollution-score chart with P07 sheet-and-axes variant',
        'scale': {'min': 0, 'max': 5, 'direction': '0 = least pollution, 5 = most pollution (lower is better)'},
        'scores': SCORES, 'visitors': VISITORS, 'changes': ch,
        'context_on_figure': 'other influences not fully controlled',
        'notes_match': ['BL-6137-4.1.07-20', 'BL-6137-4.1.08-14', 'BL-6137-4.1.08-03'],
        'encoding': 'M solid green line with circles; R dashed red line with squares (distinct in greyscale)',
        'question_withholds': ['changes and their direction', 'attribution limit wording'],
        'independent_solution_046': ['M improves 4 -> 2 (1)', 'R worsens 3 -> 4; changes differ (1)', 'intervention not isolated from other influences (1)'],
        'p07': {'bound_item': P07, 'question_plots': ['R'], 'answer_plots': {'M': SCORES['M']},
                'answer_sheet': {'M': {'change': -2, 'condition': 'better'}, 'R': {'change': 1, 'condition': 'worse'}}},
    }
    checks = [
        check('M change −2 (improvement) and R change +1 (worse) under 0 = least pollution', ch == {'M': -2, 'R': 1}),
        check('all scores within the 0-5 scale', all(0 <= v <= 5 for p in SCORES.values() for v in p)),
        check('visitor counts rise 10 -> 40 at both sites', all(v == (10, 40) for v in VISITORS.values())),
        check('P07 axes region fits its clip', y_end <= V7Y + V7H, 'axes end %d, clip end %d' % (y_end, V7Y + V7H)),
    ]
    c7 = (0, V7Y, W, V7H)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'less pollution\)', r'cause']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p07_question': {'path': 'assets/images/%s-%s-question.png' % (P07, RID), 'layers': [V, VQ], 'clip': c7, 'hide_base': True,
                         'bound_item': P07, 'forbidden': [r'better', r'worse']},
        'p07_answer': {'path': 'assets/images/%s-%s-answer.png' % (P07, RID), 'layers': [V, VA], 'clip': c7, 'hide_base': True, 'bound_item': P07},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
