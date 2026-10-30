"""VIS-6137-1.5-02 -> ITEM-6137-1.5-020-INTERP: a rocky headland seen from the sea and in plan.

(a) Elevation from the sea: land on the left; the headland ends at HEAD_X. P is a blind opening at
    the cliff foot; Q an opening right through the headland under a surviving rock roof; R an
    isolated pillar offshore; S a low rock whose top lies between low- and high-tide levels.
(b) Plan of the same features at the same x positions: P a dead-end inlet, Q a passage beneath the
    rock (dashed) joining both sides, R a separate rock surrounded by water, S covered at high tide.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.5-02'
ITEM = 'ITEM-6137-1.5-020-INTERP'
W, HQ, HA = 1000, 905, 1250
ROCK = '#a99b86'
HEAD_X = 580
TOP = 160                     # headland top in (a)
HT, LT, BED = 380, 425, 470   # high tide, low tide, sea bed in (a)
P = (170, 250)                # x ranges of each feature
Q = (440, 530)
R = (650, 730)
S = (830, 900)
S_TOP = 405                   # stump top: between high tide (380) and low tide (425)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'A rocky headland: (a) seen from the sea, (b) in plan')
    fig.pattern('rock', '<rect width="18" height="18" fill="%s"/><path d="M0 9 H18 M9 0 V9 M0 18 H18 M4 9 V18 M14 9 V18" '
                'stroke="#8a7d69" stroke-width="1.2"/>' % ROCK, 18, 18)
    # ---- (a) elevation
    fig.rect(20, 56, 960, 470, '#ffffff', GREY, 2, 8)
    fig.text(36, 92, '(a) View from the sea, looking north at the headland', 26, 'start', 'bold')
    fig.rect(22, HT, 956, BED + 40 - HT, C['sea'], 'none', 0)
    fig.rect(22, BED, 956, 50, '#d9cba8', 'none', 0)
    head = [(22, TOP - 20), (300, TOP - 10), (HEAD_X - 40, TOP), (HEAD_X, TOP + 30), (HEAD_X, BED), (22, BED)]
    fig.poly(head, 'url(#rock)', INK, 2.5)
    # P: blind cave (dark interior)
    fig.path('M%d %d L%d %d Q %d %d %d %d L%d %d Z' % (P[0], BED, P[0], BED - 70, (P[0] + P[1]) / 2, BED - 125, P[1], BED - 70, P[1], BED),
             '#3a332b', INK, 2)
    # Q: opening right through, sea and sky visible, roof above
    fig.path('M%d %d L%d %d Q %d %d %d %d L%d %d Z' % (Q[0], BED, Q[0], BED - 110, (Q[0] + Q[1]) / 2, BED - 190, Q[1], BED - 110, Q[1], BED),
             '#eaf5fb', INK, 2)
    fig.rect(Q[0] + 1, HT, Q[1] - Q[0] - 2, BED - HT, C['sea'], 'none', 0)
    # R: pillar
    fig.poly([(R[0], BED), (R[0] + 6, TOP + 60), (R[0] + 30, TOP + 40), (R[1] - 10, TOP + 52), (R[1], BED)], 'url(#rock)', INK, 2.5)
    # S: low rock
    fig.poly([(S[0], BED), (S[0] + 10, S_TOP + 8), (S[0] + 40, S_TOP), (S[1] - 6, S_TOP + 10), (S[1], BED)], 'url(#rock)', INK, 2.5)
    # tide lines drawn over the rock so the stump's relation to them is visible
    fig.line(22, HT, 978, HT, C['blue'], 2.5, dash='12 8')
    fig.line(22, LT, 978, LT, C['blue'], 2.5)
    fig.text(30, HT - 10, 'high tide', 26, 'start', 'bold', C['blue'], halo=True)
    fig.text(30, LT + 30, 'low tide', 26, 'start', 'bold', C['blue'], halo=True)
    for lab, (x1, x2), y in (('P', P, BED - 150), ('Q', Q, BED - 215), ('R', R, TOP + 20), ('S', S, S_TOP - 20)):
        fig.text((x1 + x2) / 2, y, lab, 30, 'middle', 'bold', INK, halo=True)
    fig.text(40, TOP + 30, 'land', 26, 'start', 'bold', INK, halo=True)
    # ---- (b) plan
    fig.rect(20, 540, 960, 300, '#ffffff', GREY, 2, 8)
    fig.text(36, 576, '(b) Plan view (north at top)', 26, 'start', 'bold')
    fig.rect(22, 590, 956, 248, C['sea'], 'none', 0)
    cy = 715
    hw = 62
    land = [(22, 600), (140, 600), (180, cy - hw), (HEAD_X - 30, cy - hw + 6), (HEAD_X, cy - 20), (HEAD_X, cy + 22),
            (HEAD_X - 30, cy + hw - 4), (180, cy + hw), (140, 830), (22, 830)]
    fig.poly(land, 'url(#rock)', INK, 2.5)
    # P: dead-end inlet on the south side
    fig.poly([(P[0], cy + hw), (P[0] + 18, cy + 4), (P[1] - 18, cy + 4), (P[1], cy + hw)], C['sea'], INK, 2)
    # Q: passage beneath the rock joining north and south shores (dashed = beneath rock)
    fig.line(Q[0], cy - hw + 4, Q[0], cy + hw - 2, INK, 2.5, dash='9 6')
    fig.line(Q[1], cy - hw + 6, Q[1], cy + hw - 4, INK, 2.5, dash='9 6')
    # R: separate rock; S: low rock outline dashed (covered at high tide)
    fig.poly([(R[0], cy - 30), (R[0] + 40, cy - 46), (R[1], cy - 20), (R[1] - 6, cy + 30), (R[0] + 10, cy + 36)], 'url(#rock)', INK, 2.5)
    fig.poly([(S[0], cy - 16), (S[0] + 34, cy - 26), (S[1], cy - 6), (S[1] - 10, cy + 22), (S[0] + 6, cy + 20)], ROCK, INK, 2.5,
             extra='stroke-dasharray="7 5"')
    for lab, (x1, x2), y in (('P', P, cy + hw + 34), ('Q', Q, cy - hw - 14), ('R', R, cy - 58), ('S', S, cy - 40)):
        fig.text((x1 + x2) / 2, y, lab, 30, 'middle', 'bold', INK, halo=True)
    fig.arrow(940, 690, 940, 630, INK, 4, 16)
    fig.text(940, 718, 'N', 26, 'middle', 'bold')
    ky = HQ - 30
    fig.line(30, ky - 9, 80, ky - 9, INK, 2.5, dash='9 6')
    fig.text(90, ky, 'passage beneath rock', 26)
    fig.poly([(400, ky - 20), (440, ky - 20), (440, ky + 2), (400, ky + 2)], ROCK, INK, 2, extra='stroke-dasharray="7 5"')
    fig.text(452, ky, 'rock covered at high tide', 26)

    A = 'a'
    for (lab, name, (x1, x2), y) in (('P', 'cave', P, BED - 150), ('Q', 'arch', Q, BED - 215), ('R', 'stack', R, TOP + 20), ('S', 'stump', S, S_TOP - 20)):
        fig.text((x1 + x2) / 2 + 22, y, name, 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(340, BED - 160, '1', A)
    fig.marker(R[0] - 34, TOP + 12, '2', A)
    fig.marker(S[0] - 40, S_TOP - 30, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'P is a cave: erosion has enlarged a weakness into a blind opening. At Q the opening passes right through the headland under a roof: an arch.'),
                 ('2', 'R stands alone with water all round: the roof has collapsed, leaving a stack separated from the headland.'),
                 ('3', 'S is a lower remnant covered at high tide: a stump, the stack reduced further. The letters give the order, not equal times.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'two-view resource: elevation from the sea and plan (schematic)',
        'teaching_target': 'Cave -> arch (breakthrough under a roof) -> stack (roof collapse, separation) -> stump (reduced, covered at high tide).',
        'feature_x_ranges': {'P': P, 'Q': Q, 'R': R, 'S': S}, 'headland_end_x': HEAD_X,
        'elevation_levels_y': {'high_tide': HT, 'low_tide': LT, 'sea_bed': BED, 'stump_top': S_TOP, 'headland_top': TOP},
        'question_withholds': ['cave', 'arch', 'stack', 'stump', 'collapse', 'roof'],
        'independent_solution': ['P blind opening = cave; Q opening through headland under roof = arch (1)', 'R isolated pillar = stack after roof collapse (1)',
                                 'S low remnant covered at high tide = stump (1)'],
        'assumptions': ['Features coexist along one headland; letter order is spatial and developmental, not equal time steps (notes 1.5.06-15).'],
    }
    checks = [
        check('P and Q lie within the headland; R and S beyond it', P[1] < HEAD_X and Q[1] < HEAD_X and R[0] > HEAD_X and S[0] > R[1]),
        check('Q opening is higher than P (passage through, roof above)', True, 'P crown %d, Q crown %d' % (BED - 125, BED - 190)),
        check('stump top between low and high tide', HT < S_TOP < LT),
        check('stack top far above high tide', TOP + 60 < HT),
        check('same x positions used in elevation and plan', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'\bcave', r'\barch', r'\bstack', r'stump', r'collaps', r'\broof']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 470), (20, 540, 960, 300)])


if __name__ == '__main__':
    main()
