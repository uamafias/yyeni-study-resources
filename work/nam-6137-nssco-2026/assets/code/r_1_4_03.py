"""VIS-6137-1.4-03 -> ITEM-6137-1.4-017-INTERP: plan views of two dunes at one scale, with long-term winds.

Dune A: four crests radiating from a central peak (star form). Dune B: a single long, narrow crest
800 m long and 40 m wide (20:1, as in notes BL-6137-1.4.04-09). Both panels share one scale
(PX_PER_M) and carry a scale bar and north arrow. Each has a long-term sand-moving wind rose (percent
of time from each direction): A from many directions; B dominated by south-west and south-east winds
whose combined drift is towards the north, along the ridge. No single present-day wind arrow is drawn.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.4-03'
ITEM = 'ITEM-6137-1.4-017-INTERP'
W, HQ, HA = 1000, 920, 1295
PX_PER_M = 0.4
SAND, SAND_DARK, CREST = '#ecd9a0', '#c8a85e', '#6b4f2a'
DIRS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
ROSE_A = [22, 8, 18, 6, 10, 22, 9, 5]
ROSE_B = [3, 2, 4, 28, 20, 33, 6, 4]
ARMS_A = [(15, 300), (110, 270), (200, 310), (290, 280)]      # bearing (deg) and length (m) of each arm crest
B_LEN, B_WID = 800, 40


def resultant(rose):
    """Net direction of sand drift (degrees, towards) from a 'wind from' rose, weighting by percent."""
    x = sum(p * math.sin(math.radians(i * 45 + 180)) for i, p in enumerate(rose))
    y = sum(p * math.cos(math.radians(i * 45 + 180)) for i, p in enumerate(rose))
    return (math.degrees(math.atan2(x, y)) + 360) % 360, math.hypot(x, y)


def rose(fig, cx, cy, data, scale=2.0):
    fig.circle(cx, cy, 32, 'none', '#bbbbbb', 1)
    for i, p in enumerate(data):
        a = math.radians(i * 45)
        L = 12 + p * scale
        fig.line(cx, cy, cx + L * math.sin(a), cy - L * math.cos(a), C['blue'], 9)
        lx, ly = cx + (L + 22) * math.sin(a), cy - (L + 22) * math.cos(a)
        fig.text(lx, ly + 9, '%d' % p, 26, 'middle', 'normal', INK, halo=True)
    fig.circle(cx, cy, 6, '#ffffff', INK, 1.5)


def panel(fig, x0, y0, w, h, title):
    fig.rect(x0, y0, w, h, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, title, 28, 'start', 'bold')


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Two dunes in plan view (same scale) and their long-term winds')
    # ---- dune A (star)
    panel(fig, 20, 56, 470, 560, 'Dune A')
    ax, ay = 255, 330
    pts = []
    for k in range(361):
        b = math.radians(k)
        r = 50
        for brg, L in ARMS_A:
            d = math.radians(((k - brg + 180) % 360) - 180)
            r += (L * PX_PER_M + 6) * math.exp(-(d / 0.30) ** 2)
        pts.append((ax + r * math.sin(b), ay - r * math.cos(b)))
    fig.poly(pts, SAND, INK, 2)
    for brg, L in ARMS_A:
        a = math.radians(brg)
        ex, ey = ax + L * PX_PER_M * math.sin(a), ay - L * PX_PER_M * math.cos(a)
        # slip-face shading on one side of each crest
        fig.poly([(ax, ay), (ex, ey), (ax + (L * PX_PER_M) * 0.55 * math.sin(a + 0.25), ay - (L * PX_PER_M) * 0.55 * math.cos(a + 0.25))],
                 SAND_DARK, 'none', 0)
        mx, my = ax + L * PX_PER_M * 0.5 * math.sin(a - 0.12), ay - L * PX_PER_M * 0.5 * math.cos(a - 0.12)
        fig.path('M%.1f %.1f Q %.1f %.1f %.1f %.1f' % (ax, ay, mx, my, ex, ey), 'none', CREST, 4)
    fig.poly([(ax, ay - 12), (ax - 10, ay + 7), (ax + 10, ay + 7)], CREST, INK, 1)
    # ---- dune B (linear), long axis north-south
    panel(fig, 510, 56, 470, 560, 'Dune B')
    bx, by = 745, 335
    hl, hw = B_LEN * PX_PER_M / 2, B_WID * PX_PER_M / 2
    outline = []
    for k in range(0, 181):
        t = math.radians(k)
        outline.append((bx + hw * math.sin(t) * (1.0), by - hl * math.cos(t)))
    outline += [(bx - hw * math.sin(math.radians(k)), by - hl * math.cos(math.radians(k))) for k in range(180, -1, -1)]
    fig.poly(outline, SAND, INK, 2)
    fig.poly([(bx, by - hl)] + [(bx + hw * 0.9 * math.sin(math.radians(k)), by - hl * math.cos(math.radians(k))) for k in range(0, 181, 5)],
             SAND_DARK, 'none', 0)
    fig.path('M%.1f %.1f ' % (bx, by - hl + 4) + ' '.join('L%.1f %.1f' % (bx + 2.5 * math.sin(k / 6), by - hl + 4 + k * (2 * hl - 8) / 60)
                                                            for k in range(61)), 'none', CREST, 3.5)
    # shared scale bar and north arrows
    for x0 in (20, 510):
        sx, sy = x0 + 30, 590
        L = 500 * PX_PER_M
        fig.rect(sx, sy - 10, L / 2, 10, INK, INK, 1)
        fig.rect(sx + L / 2, sy - 10, L / 2, 10, '#ffffff', INK, 1.5)
        fig.text(sx, sy - 18, '0', 26, 'middle')
        fig.text(sx + L, sy - 18, '500 m', 26, 'middle')
        fig.arrow(x0 + 430, 150, x0 + 430, 90, INK, 4, 16)
        fig.text(x0 + 430, 178, 'N', 28, 'middle', 'bold')
    # ---- wind roses
    fig.rect(20, 632, 960, 278, '#ffffff', GREY, 2, 8)
    fig.text(36, 668, 'Long-term sand-moving winds: % of time from each direction', 26, 'start', 'bold')
    fig.text(36, 700, '(bars point to where the wind comes from)', 26, 'start', 'normal')
    rose(fig, 255, 805, ROSE_A)
    rose(fig, 745, 805, ROSE_B)
    fig.text(110, 814, 'Dune A', 26, 'middle', 'bold')
    fig.text(600, 814, 'Dune B', 26, 'middle', 'bold')

    # ---- answer layer
    A = 'a'
    fig.text(40, 140, 'arms radiate from a', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(40, 172, 'central peak: star dune', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(bx - 30, by - 60, 'one long,', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(bx - 30, by - 28, 'narrow crest:', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(bx - 30, by + 4, 'linear dune', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(bx + 30, by + 90, '800 m × 40 m', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(bx + 30, by + 122, '= 20 : 1', 26, 'start', 'bold', C['answer'], A, halo=True)
    rb, rm = resultant(ROSE_B)
    fig.arrow(905, 850, 905 + 70 * math.sin(math.radians(rb)), 850 - 70 * math.cos(math.radians(rb)), C['answer'], 5, 18, A)
    fig.text(905, 880, 'net drift', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(190, 85, '1', A)
    fig.marker(680, 85, '2', A)
    fig.marker(bx + 160, by + 150, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A: four arms radiate from a central peak, each about 300 m long: a star dune, consistent with winds from many directions.'),
                 ('2', 'B: one long, narrow crest: a linear (seif-type) dune. South-west and south-east winds give a net drift towards the north, along the ridge.'),
                 ('3', 'Scale: B is about 800 m long but only 40 m wide (20:1); A is about 600 m across in several directions. Shape and proportion classify them, not colour or a place name.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    ra, ma = resultant(ROSE_A)
    spec = {
        'kind': 'two plan-view panels at one scale with wind roses (schematic)',
        'scale_px_per_m': PX_PER_M, 'scale_bar_m': 500,
        'dune_A': {'arms_bearing_deg_length_m': ARMS_A, 'form': 'star'},
        'dune_B': {'length_m': B_LEN, 'width_m': B_WID, 'ratio': B_LEN / B_WID, 'long_axis': 'north-south', 'form': 'linear'},
        'wind_roses_percent_from': {'directions': DIRS, 'A': ROSE_A, 'B': ROSE_B},
        'resultant_drift_towards_deg': {'A': round(ra, 1), 'B': round(rb, 1)}, 'resultant_magnitude': {'A': round(ma, 1), 'B': round(rb and rm, 1)},
        'question_withholds': ['star', 'linear', 'seif', 'crest', 'radiat'],
        'independent_solution': ['A arms radiating around a central peak -> star (1)', 'B long narrow crest -> linear (1)',
                                 'scale: B 800 m x 40 m (20:1) vs A ~600 m across in several directions (1)'],
        'assumptions': ['Schematic forms; not a measured Namibian dune.', 'Roses are long-term illustrative data, not observations.'],
    }
    checks = [
        check('both roses total 100%', sum(ROSE_A) == 100 and sum(ROSE_B) == 100),
        check('B: long axis 800 m and width 40 m at the shared scale', abs(2 * hl / PX_PER_M - 800) < 1e-9 and abs(2 * hw / PX_PER_M - 40) < 1e-9),
        check('B: net drift is along the ridge (within 15 deg of north)', min(rb, 360 - rb) < 15, 'resultant towards %.1f deg' % rb),
        check('A: winds from many directions (no direction above 25%) and weak net drift', max(ROSE_A) <= 25 and ma < 0.5 * rm,
              'A resultant %.1f vs B %.1f' % (ma, rm)),
        check('A: four arms, 270-310 m long, spread round the compass', len(ARMS_A) == 4 and all(270 <= L <= 310 for b, L in ARMS_A)),
        check('scale bar 500 m = %d px' % (500 * PX_PER_M), 500 * PX_PER_M == 200),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'star', r'linear', r'seif', r'crest', r'radiat', r'drift']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 470, 560), (510, 56, 470, 560), (20, 632, 960, 278)])


if __name__ == '__main__':
    main()
