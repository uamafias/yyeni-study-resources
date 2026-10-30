"""VIS-6137-1.2-02 -> ITEM-6137-1.2-021-INTERP: thermal exfoliation as a four-stage sequence.

The same rounded outcrop (cross-section, not to scale) in four panels. Its outer sheet is the band
between two concentric half-ellipses, so the sheet stays distinct from the interior and every crack
drawn between them is parallel to the surface. No water or ice appears anywhere.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.2-02'
ITEM = 'ITEM-6137-1.2-021-INTERP'
W, HQ, HA = 1000, 925, 1300
PW, PH = 470, 395
R, HD, SHEET = 165, 175, 24
HOT, COOL, CORE = '#e08a4f', '#a9cbe6', C['rock']
DETACH = (25, 70)            # degrees (from the right-hand base) of the sheet that detaches in stage 4
STAGES = [
    {'n': 1, 'title': 'Day: sun on the rock', 'sheet': HOT, 'note': 'Outer sheet hotter than interior'},
    {'n': 2, 'title': 'Night', 'sheet': COOL, 'note': 'Outer sheet cooler than interior'},
    {'n': 3, 'title': 'After many day–night cycles', 'sheet': CORE, 'note': 'Cracks along the outer sheet'},
    {'n': 4, 'title': 'Later', 'sheet': CORE, 'note': 'Part of the outer sheet has fallen'},
]


def arc(cx, by, rx, ry, a0, a1, n=40):
    """Points on the upper half-ellipse from angle a0 to a1 (degrees, 0 = right-hand base)."""
    return [(cx + rx * math.cos(math.radians(a)), by - ry * math.sin(math.radians(a)))
            for a in [a0 + (a1 - a0) * k / n for k in range(n + 1)]]


def panel(fig, x0, y0, st):
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, '%d' % st['n'], 30, 'start', 'bold', C['answer'])
    fig.text(x0 + 50, y0 + 38, st['title'], 26, 'start', 'bold')
    cx, by = x0 + PW / 2 - 40, y0 + PH - 62
    fig.rect(x0 + 2, by, PW - 4, 8, '#c9b48a', 'none', 0)                       # ground
    outer = arc(cx, by, R, HD, 0, 180)
    inner = arc(cx, by, R - SHEET, HD - SHEET, 180, 0)
    fig.poly(arc(cx, by, R - SHEET, HD - SHEET, 0, 180), CORE, INK, 1.5)        # interior
    if st['n'] < 4:
        fig.poly(outer + inner, st['sheet'], INK, 2)
    else:
        a0, a1 = DETACH
        fig.poly(arc(cx, by, R, HD, a1, 180) + arc(cx, by, R - SHEET, HD - SHEET, 180, a1), CORE, INK, 2)
        fig.poly(arc(cx, by, R, HD, 0, a0) + arc(cx, by, R - SHEET, HD - SHEET, a0, 0), CORE, INK, 2)
        # the fallen pieces of sheet lie at the foot of the slope
        for k, (dx, ang) in enumerate([(R + 26, -14), (R + 66, 6)]):
            fig.add('<rect x="%.1f" y="%.1f" width="46" height="%d" fill="%s" stroke="%s" stroke-width="2" '
                    'transform="rotate(%d %.1f %.1f)"/>' % (cx + dx - 23, by - SHEET + 2, SHEET - 2, CORE, INK, ang, cx + dx, by - 10))
        fig.poly(arc(cx, by, R - SHEET, HD - SHEET, a0, a1), 'none', INK, 3, closed=False)
    if st['n'] == 3:
        mid = arc(cx, by, R - SHEET / 2, HD - SHEET / 2, 20, 160)
        fig.poly(mid, 'none', INK, 2.5, closed=False, extra='stroke-dasharray="14 7"')
    if st['n'] == 1:
        sx, sy = x0 + PW - 60, y0 + 92
        fig.circle(sx, sy, 20, '#ffd23f', INK, 2)
        for a in range(0, 360, 45):
            fig.line(sx + 26 * math.cos(math.radians(a)), sy + 26 * math.sin(math.radians(a)),
                     sx + 36 * math.cos(math.radians(a)), sy + 36 * math.sin(math.radians(a)), INK, 2)
    if st['n'] == 2:
        sx, sy = x0 + PW - 60, y0 + 92
        fig.circle(sx, sy, 20, '#dfe6f0', INK, 2)
        fig.circle(sx + 10, sy - 6, 18, '#ffffff', 'none', 0)
    fig.text(x0 + 16, y0 + PH - 20, st['note'], 26)
    return cx, by


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Changes in an exposed rock outcrop (cross-sections, not to scale)')
    origins = [(20, 60), (510, 60), (20, 470), (510, 470)]
    cs = [panel(fig, x, y, st) for (x, y), st in zip(origins, STAGES)]
    ky = 910
    for i, (col, lab) in enumerate([(HOT, 'outer sheet, hotter'), (COOL, 'outer sheet, cooler'), (CORE, 'rock')]):
        fig.rect(40 + i * 320, ky - 22, 26, 22, col, INK, 1)
        fig.text(74 + i * 320, ky - 2, lab, 26)
    A = 'a'
    (c1, b1), (c2, b2), (c3, b3), (c4, b4) = cs
    for (cx, by), sign in (((c1, b1), 1), ((c2, b2), -1)):
        for a in (40, 90, 140):
            px, py = cx + (R + 6) * math.cos(math.radians(a)), by - (HD + 6) * math.sin(math.radians(a))
            ox, oy = math.cos(math.radians(a)), -math.sin(math.radians(a))
            if sign > 0:
                fig.arrow(px, py, px + 26 * ox, py + 26 * oy, C['red'], 3, 11, A, halo=False)
            else:
                fig.arrow(px + 28 * ox, py + 28 * oy, px + 2 * ox, py + 2 * oy, C['blue'], 3, 11, A, halo=False)
    fig.marker(c1 - R + 10, b1 - HD + 10, '1', A)
    fig.marker(c2 - R + 10, b2 - HD + 10, '1', A)
    fig.marker(c3 - 30, b3 - HD / 2, '2', A)
    fig.marker(c4 + R + 55, b4 - 62, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'By day the outer sheet warms and expands more than the interior (1); at night it cools and '
                       'contracts (2).'),
                 ('2', 'These repeated stresses help cracks grow parallel to the surface, between the sheet and the interior (3).'),
                 ('3', 'Part of the outer sheet detaches and falls (4): the outcrop peels in sheets. This is exfoliation.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'Heating and cooling is one contributing mechanism. Unloading and other stress changes '
             'can also open surface-parallel cracks.', 26, 920, 32, layer=A)

    spec = {
        'kind': 'four-stage process sequence (cross-sections, not to scale)',
        'teaching_target': 'Thermal exfoliation: outer sheet warms/expands and cools/contracts relative to the interior; repeated stress grows surface-parallel cracks; sheets detach.',
        'outcrop': {'half_width_px': R, 'height_px': HD, 'sheet_thickness_px': SHEET, 'detached_arc_deg': DETACH},
        'stages': [{k: v for k, v in s.items()} for s in STAGES],
        'question_shows': ['day stage: outer sheet hotter than interior (colour + note)', 'night stage: outer sheet cooler than interior',
                           'surface-parallel dashed crack after many cycles', 'detached sheet pieces at the foot'],
        'question_withholds': ['process name', 'the words expand/contract/stress/peel/exfoliation', 'expansion/contraction arrows'],
        'independent_solution': ['outer sheet heats/expands by day and cools/contracts at night relative to interior (1)',
                                 'repeated stress grows cracks parallel to the surface (1)', 'outer sheet detaches = peeling (1)'],
        'assumptions': ['No ice or water drawn.', 'Thermal stress shown as contributing, not the unique cause (unloading noted in the answer).'],
    }
    checks = [
        check('crack is parallel to the surface (concentric half-ellipse midway through the sheet)', True, 'rx=R-SHEET/2, ry=HD-SHEET/2'),
        check('detached arc lies within the sheet band only', 0 < DETACH[0] < DETACH[1] < 180),
        check('no water or ice colours used', all(s['sheet'] != C['water'] for s in STAGES)),
        check('hot and cool sheet fills differ from the interior fill', HOT != CORE and COOL != CORE),
        check('fallen pieces stay inside their panel', PW / 2 - 40 + R + 66 + 23 + 10 < PW, 'rightmost piece edge %d of %d px' % (PW / 2 - 40 + R + 66 + 33, PW)),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'expan', r'contract', r'stress', r'peel', r'exfoliat', r'ice', r'freez']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a'], 'forbidden': [r'\bice\b', r'freez']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 60, PW, PH), (510, 60, PW, PH), (20, 470, PW, PH), (510, 470, PW, PH)])


if __name__ == '__main__':
    main()
