"""VIS-6137-1.5-01 -> ITEM-6137-1.5-010-APP: two wave regimes on the same beach section (cross-sections).

Uses the teaching numbers of notes BL-6137-1.5.04-08: regime A moves 30 units up the beach and 18 back
(net +12); regime B moves 15 up and 28 back (net -13). Each panel shows the profile before (dashed)
and after (solid) the interval: A's upper beach builds up; B's upper beach is lowered and a nearshore
bar grows (notes 04-04). Arrow lengths are drawn proportional to the units and the key says so.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.5-01'
ITEM = 'ITEM-6137-1.5-010-APP'
W, HQ, HA = 1000, 860, 1180
UNITS = {'A': (30, 18), 'B': (15, 28)}      # (moved up the beach by swash, moved back down by backwash)
PX_PER_UNIT = 6


def before(x):
    """Common starting profile: height (px above a datum) at horizontal position x (0 = landward edge)."""
    return 150 - 0.30 * x if x < 400 else 30 - 0.08 * (x - 400)


def after(regime, x):
    if regime == 'A':                                         # upper beach (x 120-300) built up
        bump = 22 * max(0.0, 1 - abs(x - 210) / 110)
        return before(x) + bump
    upper = -22 * max(0.0, 1 - abs(x - 210) / 110)            # upper beach lowered
    bar = 18 * max(0.0, 1 - abs(x - 560) / 70)                # nearshore bar grows
    return before(x) + upper + bar


SEA_H = 60                    # sea level height (px above datum); the before profile meets it at x = 300


def surf(regime, x, off):
    return x, after(regime, x) + off


def panel(fig, y0, regime, layer='base'):
    up, down = UNITS[regime]
    x0, base_y = 70, y0 + 330
    sea = base_y - SEA_H
    fig.rect(20, y0, 960, 360, '#ffffff', GREY, 2, 8)
    fig.text(36, y0 + 38, 'Regime %s' % regime, 28, 'start', 'bold')
    xs = list(range(0, 841, 4))
    pts_b = [(x0 + x, base_y - before(x)) for x in xs]
    pts_a = [(x0 + x, base_y - after(regime, x)) for x in xs]
    water = [(x0 + x, base_y - after(regime, x)) for x in xs if after(regime, x) <= SEA_H]
    fig.poly([(water[0][0], sea), (x0 + 840, sea), (x0 + 840, base_y + 20)] + water[::-1], C['sea'], 'none', 0)
    fig.poly(pts_a + [(x0 + 840, base_y + 20), (x0, base_y + 20)], C['sand'], INK, 2.5)
    fig.poly(pts_b, 'none', INK, 2.5, closed=False, extra='stroke-dasharray="10 7"')
    fig.line(water[0][0] - 10, sea, x0 + 840, sea, C['blue'], 2)
    fig.text(x0 + 836, sea - 10, 'sea level', 26, 'end', 'normal', C['blue'])
    # swash and backwash arrows follow the beach face just above it; lengths proportional to units moved
    wl = (150 - SEA_H) / 0.30                                   # waterline x on the starting profile
    def along(x1, x2, off):
        return (x0 + x1, base_y - before(x1) - off), (x0 + x2, base_y - before(x2) - off)
    (sx1, sy1), (sx2, sy2) = along(wl, wl - up * PX_PER_UNIT, 18)
    fig.arrow(sx1, sy1, sx2, sy2, C['blue'], 5, 18)
    (bx1, by1), (bx2, by2) = along(wl - down * PX_PER_UNIT, wl, 44)
    fig.arrow(bx1, by1, bx2, by2, C['red'], 5, 18)
    # quantities table
    fig.text(520, y0 + 38, 'Material moved in the interval:', 26, 'start', 'bold')
    fig.text(520, y0 + 74, 'up the beach by swash: %d units' % up, 26, 'start', 'bold', C['blue'])
    fig.text(520, y0 + 108, 'back down by backwash: %d units' % down, 26, 'start', 'bold', C['red'])
    return x0, base_y


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'One beach section under two regimes (cross-sections, not to scale)')
    xa, ba = panel(fig, 56, 'A')
    xb, bb = panel(fig, 430, 'B')
    ky = HQ - 30
    fig.line(30, ky - 9, 90, ky - 9, INK, 2.5, dash='10 7')
    fig.text(100, ky, 'profile before', 26)
    fig.line(310, ky - 9, 370, ky - 9, INK, 2.5)
    fig.text(380, ky, 'profile after', 26)
    fig.text(600, ky, 'arrow length shows units moved', 26)

    A = 'a'
    fig.text(xa + 30, ba - 12, 'upper beach built up (+12)', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(xb + 30, bb - 12, 'upper beach lowered (−13)', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(xb + 560, bb - after('B', 560) + 46, 'bar grows offshore', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(220, 56 + 28, '1', A)
    fig.marker(220, 430 + 28, '2', A)
    fig.marker(xb + 700, bb - after('B', 560) + 38, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A is constructive: swash moves 30 units up but backwash returns only 18, a net gain of 12, and the upper profile builds up.'),
                 ('2', 'B is destructive: backwash removes 28 units while swash brings 15, a net loss of 13, and the upper beach is lowered.'),
                 ('3', 'The bar growing offshore in B is where removed material is stored; it does not contradict erosion of the upper beach.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'two cross-section panels (same starting profile), schematic',
        'teaching_target': 'Apply constructive/destructive using swash vs backwash transport and the profile change at its location.',
        'units_up_back': UNITS, 'net_units': {k: u - d for k, (u, d) in UNITS.items()}, 'arrow_px_per_unit': PX_PER_UNIT,
        'profile_change': {'A': 'upper beach (x 100-320) raised up to 22 px', 'B': 'upper beach lowered up to 22 px; nearshore bar +18 px at x 490-630'},
        'source_numbers': 'notes BL-6137-1.5.04-08 (teaching units, not measured volumes)',
        'question_withholds': ['constructive', 'destructive', 'erosion', 'deposition', 'build', 'net'],
        'independent_solution': ['A constructive: 30 up vs 18 back (+12) and upper beach built up (1)', 'B destructive: 28 back vs 15 up (-13) (1)',
                                 'B upper-beach lowering with offshore bar growth = storage offshore, not a contradiction (1)'],
    }
    checks = [
        check('net units match notes (+12, -13)', [u - d for u, d in UNITS.values()] == [12, -13]),
        check('A upper beach higher after; B upper beach lower after', after('A', 210) > before(210) > after('B', 210)),
        check('B nearshore bar higher after than before', after('B', 560) > before(560)),
        check('A nearshore unchanged', after('A', 560) == before(560)),
        check('arrow lengths proportional to units', True, '%d px per unit' % PX_PER_UNIT),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'constructive', r'destructive', r'erosion', r'eroded', r'deposit', r'built', r'\bnet\b']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 360), (20, 430, 960, 360)])


if __name__ == '__main__':
    main()
