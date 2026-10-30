"""VIS-6137-1.5-08 -> ITEM-6137-1.5-P03 (assigned, 5-mark judgement); variant bound to ITEM-6137-1.5-P07.

Hypothetical coastal-management plan, north at top, sea west. A groyne crosses the beach; net drift is
northward. U lies immediately south of the groyne (updrift), D north of it (downdrift), and C is a
reference reach south of a headland. Beach width is drawn to scale (PX_PER_M) from the fixed back-beach
line: dashed = before, solid shoreline = after. Mean widths before -> after: U 20 -> 30, D 18 -> 10,
C 20 -> 19 m (as stated in P03 and P07). The P07 variant gives blank paired before/after axes
(reach U, D, C; width 0-35 m); its answer variant draws the paired bars.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.5-08'
ITEM = 'ITEM-6137-1.5-P03'
P07 = 'ITEM-6137-1.5-P07'
W, HQ, HA = 1000, 860, 1180
VY, VH = 1300, 620
WIDTHS = {'U': (20, 30), 'D': (18, 10), 'C': (20, 19)}
PX_PER_M = 4
BACK = 560                                   # back-beach line x (fixed)
REACH_Y = {'D': (90, 300), 'U': (330, 500), 'C': (590, 760)}
GROYNE_Y = 315
HEADLAND = (520, 570)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Hypothetical groyne scheme: plan with beach widths (widths to scale)')
    fig.extra_h = VY + VH
    fig.rect(20, 56, 960, 720, C['sea'], GREY, 2, 8)
    fig.rect(BACK, 58, 418, 716, C['land'], 'none', 0)
    for key, (y1, y2) in REACH_Y.items():
        b, a = WIDTHS[key]
        fig.rect(BACK - a * PX_PER_M, y1, a * PX_PER_M, y2 - y1, C['sand'], INK, 1.5)
        fig.line(BACK - b * PX_PER_M, y1, BACK - b * PX_PER_M, y2, INK, 2.5, dash='10 7')
        fig.text(BACK + 30, (y1 + y2) / 2 + 12, key, 40, 'start', 'bold', INK, halo=True)
    # gaps between reaches drawn as plain beach of the before width
    fig.rect(BACK - 20 * PX_PER_M, 300, 20 * PX_PER_M, 30, C['sand'], 'none', 0)
    fig.rect(BACK - 20 * PX_PER_M, 500, 20 * PX_PER_M, 90, C['sand'], 'none', 0)
    # headland separating C from U
    fig.poly([(BACK, HEADLAND[0]), (300, HEADLAND[0] + 15), (280, (HEADLAND[0] + HEADLAND[1]) / 2 + 10), (310, HEADLAND[1] + 10),
              (BACK, HEADLAND[1] + 10)], '#a99b86', INK, 2)
    fig.text(360, HEADLAND[0] + 42, 'headland', 26, 'start', 'bold', INK, halo=True)
    # groyne
    fig.rect(BACK - 170, GROYNE_Y - 7, 175, 14, '#5a4126', INK, 1.5)
    fig.text(BACK - 180, GROYNE_Y + 9, 'groyne', 26, 'end', 'bold', INK, halo=True)
    fig.line(BACK, 58, BACK, 774, INK, 2.5)
    fig.text(BACK + 14, 90, 'back of beach', 26, 'start', 'normal', INK, halo=True)
    fig.arrow(130, 700, 130, 160, C['blue'], 7, 26)
    fig.text(150, 430, 'net drift', 26, 'start', 'bold', C['blue'], halo=True)
    fig.text(150, 462, 'northward', 26, 'start', 'bold', C['blue'], halo=True)
    fig.text(220, 130, 'SEA', 30, 'middle', 'bold', C['blue'])
    fig.arrow(930, 200, 930, 110, INK, 4, 16)
    fig.text(930, 230, 'N', 28, 'middle', 'bold')
    # data table
    tx, ty = 650, 300
    fig.rect(tx, ty, 310, 210, '#ffffff', INK, 1.5)
    fig.text(tx + 12, ty + 34, 'Mean width (m)', 26, 'start', 'bold')
    fig.text(tx + 12, ty + 70, 'Reach  Before  After', 26, 'start', 'bold')
    for i, k in enumerate(('U', 'D', 'C')):
        b, a = WIDTHS[k]
        fig.text(tx + 30, ty + 106 + i * 34, k, 26, 'start', 'bold')
        fig.text(tx + 140, ty + 106 + i * 34, str(b), 26, 'middle')
        fig.text(tx + 250, ty + 106 + i * 34, str(a), 26, 'middle')
    ky = HQ - 50
    fig.line(30, ky - 9, 80, ky - 9, INK, 2.5, dash='10 7')
    fig.text(90, ky, 'shoreline before', 26)
    fig.rect(330, ky - 22, 30, 24, C['sand'], INK, 1.5)
    fig.text(370, ky, 'beach after', 26)
    fig.text(560, ky, 'C = reference reach', 26)
    fig.text(30, ky + 38, 'Aims: keep the recreational beach at U; do not reduce supply to D.', 26)

    A = 'a'
    fig.text(BACK - 140, 420, '+10 m', 30, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(BACK - 50, 200, '−8 m', 30, 'middle', 'bold', C['red'], A, halo=True)
    fig.text(BACK - 100, 680, '−1 m', 30, 'middle', 'bold', GREY, A, halo=True)
    fig.marker(BACK - 210, 400, '1', A)
    fig.marker(BACK - 120, 150, '2', A)
    fig.marker(BACK - 180, 680, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Judgement: only partly successful', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'U, just updrift of the groyne, gains 10 m: consistent with the groyne trapping northward drift, so aim 1 is met.'),
                 ('2', 'D, downdrift, loses 8 m, far more than the 1 m lost at reference C: reduced supply is a plausible cause, but aim 2 is not demonstrated.'),
                 ('3', 'C shows the wider change is small, but other site differences could still contribute: overall success remains unproven.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P07 variant: paired before/after axes
    V, VQ, VA = 'v-p07', 'v-p07-q', 'v-p07-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Mean beach width before and after the groyne', 28, 'middle', 'bold', layer=V)
    ax = Axes(fig, 170, VY + 80, 760, 400, (0, 3), (0, 35), layer=V)
    ax.draw([], range(0, 36, 5), '', 'Mean width (m)', minor_y=range(1, 35), ylabel_x=70)
    for i, k in enumerate(('U', 'D', 'C')):
        fig.text(ax.X(i + 0.5), ax.Y(0) + 36, 'Reach %s' % k, 26, 'middle', 'bold', layer=V)
    fig.rect(200, VY + 560, 30, 24, '#ffffff', INK, 2, layer=V)
    fig.text(240, VY + 580, 'before', 26, layer=V)
    fig.rect(400, VY + 560, 30, 24, C['answer'], INK, 2, layer=V)
    fig.text(440, VY + 580, 'after', 26, layer=V)
    for i, k in enumerate(('U', 'D', 'C')):
        b, a = WIDTHS[k]
        for j, (v, fill) in enumerate(((b, '#ffffff'), (a, C['answer']))):
            x0 = ax.X(i + 0.18 + j * 0.32)
            x1 = ax.X(i + 0.18 + j * 0.32 + 0.28)
            fig.rect(x0, ax.Y(v), x1 - x0, ax.Y(0) - ax.Y(v), fill, INK, 2, layer=VA)
            fig.text((x0 + x1) / 2, ax.Y(v) - 10, str(v), 26, 'middle', 'bold', INK, VA, halo=True)

    spec = {
        'kind': 'hypothetical management plan with widths to scale; P07 paired-bar variant',
        'widths_m_before_after': WIDTHS, 'px_per_m': PX_PER_M, 'drift': 'northward', 'groyne_y': GROYNE_Y,
        'reaches': {'U': 'immediately south (updrift) of the groyne', 'D': 'north (downdrift) of the groyne', 'C': 'reference reach south of a headland'},
        'aims': ['maintain the recreational beach at U', 'do not reduce sediment supply to D'],
        'p07_variant': {'bound_item': P07, 'axes': {'x': 'reach U, D, C', 'y': [0, 35, 'm']}},
        'question_withholds': ['judgement', 'change values (+10, -8, -1)', 'trapping/supply wording'],
        'independent_solution': ['U +10 m vs C -1 m: local widening updrift (aim 1 met)', 'D -8 m vs C -1 m: downdrift narrowing, plausibly reduced supply (aim 2 not demonstrated)',
                                 'reference limits confounding but cannot prove unique cause; overall partial success'],
    }
    ch = {k: a - b for k, (b, a) in WIDTHS.items()}
    checks = [
        check('changes U +10, D -8, C -1', ch == {'U': 10, 'D': -8, 'C': -1}),
        check('U percentage increase 50% (P07 part d)', (30 - 20) / 20 * 100 == 50),
        check('mean of U after readings 29, 30, 31 = 30 m (P07 part j)', (29 + 30 + 31) / 3 == 30),
        check('U lies south (updrift) and D north (downdrift) of the groyne for northward drift',
              REACH_Y['U'][0] > GROYNE_Y > REACH_Y['D'][1]),
        check('drawn widths to scale', True, '%d px per metre from the back-beach line' % PX_PER_M),
        check('all widths within the 0-35 m axis', all(0 <= v <= 35 for p in WIDTHS.values() for v in p)),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'partly', r'trap', r'\+10', r'−8', r'judgement']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p07_question': {'path': 'assets/images/%s-%s-question.png' % (P07, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True, 'bound_item': P07},
        'p07_answer': {'path': 'assets/images/%s-%s-answer.png' % (P07, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P07},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
