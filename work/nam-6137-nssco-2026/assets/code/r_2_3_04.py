"""VIS-6137-2.3-04 -> ITEM-6137-2.3-014-INTERP (assigned); variant bound to ITEM-6137-2.3-P07.

Base: one stacked horizontal bar showing an invented tourism enterprise's receipts of N$20,000 (notes
BL-6137-2.3.05-05) divided into N$8,000 paid to local workers and suppliers, N$7,000 paid outside the
area and N$5,000 retained before other unspecified obligations; a N$ scale 0-20,000.
P07 variant: blank before/after axes for litter pieces 0-25 with a key for M (managed) and R
(reference). Answer: M before 20 and after 8 plotted (part k asks for M only).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-2.3-04'
ITEM = 'ITEM-6137-2.3-014-INTERP'
P07 = 'ITEM-6137-2.3-P07'
W, HQ, HA = 1000, 600, 925
VY, VH = 1000, 640
RECEIPTS = 20000
PARTS = [('paid to local workers', 'and suppliers', 8000, '#2e7d4f'), ('paid outside', 'the area', 7000, '#b03a2e'),
         ('retained before other', 'obligations', 5000, '#e0b43c')]
M = (20, 8)


def n(v):
    return 'N$' + '{:,}'.format(v)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Where one tourism enterprise’s receipts went (invented example)')
    fig.extra_h = VY + VH
    x0, x1, y0, h = 60, 940, 170, 110
    sx = (x1 - x0) / RECEIPTS
    fig.text(x0, 140, 'Receipts from visitors: %s' % n(RECEIPTS), 26, 'start', 'bold')
    x = x0
    for a, b, v, col in PARTS:
        w = v * sx
        fig.rect(x, y0, w, h, col, INK, 2)
        fig.text(x + w / 2, y0 + h / 2 + 10, n(v), 28, 'middle', 'bold', '#ffffff' if col != '#e0b43c' else INK)
        fig.text(x + w / 2, y0 + h + 40, a, 26, 'middle')
        fig.text(x + w / 2, y0 + h + 72, b, 26, 'middle')
        x += w
    ay = 420
    fig.line(x0, ay, x1, ay, INK, 2.5)
    for v in range(0, RECEIPTS + 1, 2000):
        fig.line(x0 + v * sx, ay, x0 + v * sx, ay + 10, INK, 2)
        if v % 4000 == 0:
            fig.text(x0 + v * sx, ay + 40, '{:,}'.format(v), 26, 'middle')
    fig.text((x0 + x1) / 2, ay + 80, 'Amount (N$)', 26, 'middle', 'bold')
    fig.text(W / 2, HQ - 30, 'Other obligations from the retained amount are not shown.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.marker(x0 + 4000 * sx, y0 + h + 104, '1', A)
    fig.marker(x0 + 11500 * sx, y0 + h + 104, '2', A)
    fig.marker(x0 + 17500 * sx, y0 + h + 104, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'The chart splits the N$20,000 of receipts into local payments, outward payments and a retained balance.'),
                 ('2', 'N$8,000 goes to local workers and suppliers; N$7,000 leaves the area.'),
                 ('3', 'The N$5,000 retained is before other obligations, so it is not shown to be final profit or an equal benefit to households.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P07 variant
    V, VQ, VA = 'v-p07', 'v-p07-q', 'v-p07-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Litter pieces before and after management', 28, 'middle', 'bold', layer=V)
    ax = Axes(fig, 170, VY + 80, 560, 420, (0, 2), (0, 25), layer=V)
    ax.draw([], range(0, 26, 5), None, 'Litter pieces counted', minor_y=range(1, 25), ylabel_x=70)
    for k, lab in enumerate(('Before', 'After')):
        fig.text(ax.X(k + 0.5), ax.Y(0) + 36, lab, 26, 'middle', 'bold', layer=V)
    fig.rect(780, VY + 200, 190, 120, '#ffffff', INK, 1.5, layer=V)
    fig.text(796, VY + 234, 'Key', 26, 'start', 'bold', layer=V)
    fig.circle(810, VY + 266, 9, C['answer'], '#ffffff', 2, V)
    fig.text(830, VY + 275, 'site M', 26, layer=V)
    fig.poly([(801, VY + 307), (819, VY + 307), (810, VY + 291)], C['blue'], '#ffffff', 2, layer=V)
    fig.text(830, VY + 307, 'site R', 26, layer=V)
    for k, v in enumerate(M):
        fig.circle(ax.X(k + 0.5), ax.Y(v), 10, C['answer'], '#ffffff', 2, VA)
        fig.text(ax.X(k + 0.5) + 18, ax.Y(v) + 9, str(v), 26, 'start', 'bold', C['answer'], VA, halo=True)

    spec = {
        'kind': 'stacked bar of an invented enterprise’s receipts; P07 before/after axes variant',
        'receipts_NAD': RECEIPTS, 'parts_NAD': {a + ' ' + b: v for a, b, v, c in PARTS}, 'scale_px_per_NAD': sx,
        'source': 'notes BL-6137-2.3.05-05 and the card (hypothetical account)',
        'p07': {'bound_item': P07, 'axes': {'x': ['Before', 'After'], 'y': [0, 25, 'pieces']}, 'key': ['site M (circle)', 'site R (triangle)'],
                'answer_points_M': {'before': M[0], 'after': M[1]}},
        'independent_solution_014': ['local, outward and retained flows separated (1)', 'N$8,000 local vs N$7,000 outward (1)',
                                     'N$5,000 retained is not established as final profit or equal household benefit (1)'],
    }
    checks = [
        check('parts sum to receipts', sum(v for a, b, v, c in PARTS) == RECEIPTS),
        check('segment widths proportional to amounts', True, '%.4f px per N$' % sx),
        check('M points within 0-25 axis', all(0 <= v <= 25 for v in M)),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'profit', r'leak']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p07_question': {'path': 'assets/images/%s-%s-question.png' % (P07, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True, 'bound_item': P07},
        'p07_answer': {'path': 'assets/images/%s-%s-answer.png' % (P07, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P07},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
