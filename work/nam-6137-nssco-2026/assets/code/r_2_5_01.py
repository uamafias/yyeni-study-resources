"""VIS-6137-2.5-01 -> ITEM-6137-2.5-014-INTERP: reservoir water-balance diagram for one interval.

Values (card and notes BL-6137-2.5.04-09): opening stock 100 units; inflow 20 in; abstraction 30 out;
evaporation 10 out; no other changes. Arrow widths are proportional to the flows (WPU px per unit).
The question leaves the closing stock blank; the answer gives 100 + 20 - 30 - 10 = 80.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-2.5-01'
ITEM = 'ITEM-6137-2.5-014-INTERP'
W, HQ, HA = 1000, 700, 1020
OPEN, INFLOW, ABSTRACT, EVAP = 100, 20, 30, 10
WPU = 1.6


def band(fig, x1, y1, x2, y2, units, col, label, lx, ly, anchor='middle'):
    fig.line(x1, y1, x2, y2, col, units * WPU)
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hw = units * WPU * 0.9 + 6
    tip = (x2 + 20 * math.cos(a), y2 + 20 * math.sin(a))
    fig.poly([tip, (x2 - hw * math.sin(a), y2 + hw * math.cos(a)), (x2 + hw * math.sin(a), y2 - hw * math.cos(a))], col, 'none', 0)
    fig.text(lx, ly, label, 26, anchor, 'bold', INK, halo=True)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Water balance of a reservoir for one interval (units of water)')
    fig.rect(330, 250, 340, 220, '#cfe6f5', INK, 3, 14)
    fig.text(500, 330, 'Reservoir store', 28, 'middle', 'bold')
    fig.text(500, 372, 'Opening stock: %d' % OPEN, 26, 'middle')
    fig.text(500, 412, 'Closing stock: ______', 26, 'middle', 'normal', INK, 'q')
    fig.text(500, 412, 'Closing stock: %d' % (OPEN + INFLOW - ABSTRACT - EVAP), 26, 'middle', 'bold', C['answer'], 'a')
    band(fig, 80, 360, 300, 360, INFLOW, C['blue'], 'inflow from river: %d' % INFLOW, 170, 320)
    band(fig, 680, 400, 900, 400, ABSTRACT, C['red'], 'abstraction', 790, 360)
    fig.text(790, 470, 'to town supply: %d' % ABSTRACT, 26, 'middle', 'bold', INK, halo=True)
    band(fig, 500, 240, 500, 120, EVAP, C['orange'], 'evaporation: %d' % EVAP, 520, 100, 'start')
    fig.text(W / 2, 560, 'Arrow widths are proportional to the amounts. Other changes are absent.', 26, 'middle', 'normal', GREY)
    fig.text(W / 2, 600, 'No rainfall record is shown.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.marker(40, 410, '1', A)
    fig.marker(690, 300, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Inflow (20) adds water; abstraction (30) and evaporation (10) remove it.'),
                 ('2', 'Closing stock = 100 + 20 − 30 − 10 = 80 units: a 20-unit decline.'),
                 ('3', 'This shows the balance only; without a rainfall baseline it does not prove a meteorological drought.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    close = OPEN + INFLOW - ABSTRACT - EVAP
    spec = {'kind': 'store-and-flow diagram (one interval)', 'opening': OPEN, 'inflow': INFLOW, 'abstraction': ABSTRACT, 'evaporation': EVAP,
            'closing': close, 'arrow_px_per_unit': WPU, 'stated_limits': ['other changes absent', 'no rainfall record'],
            'question_withholds': ['closing stock value', 'drought'],
            'independent_solution': ['inflow adds; abstraction and evaporation remove (1)', 'closing 80, decline 20 (1)', 'no drought proof without rainfall baseline (1)']}
    checks = [check('closing stock 80', close == 80), check('decline 20', OPEN - close == 20),
              check('arrow widths proportional', True, '%.1f px per unit' % WPU)]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\b80\b', r'drought']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
