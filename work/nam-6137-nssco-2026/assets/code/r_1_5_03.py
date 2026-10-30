"""VIS-6137-1.5-03 -> ITEM-6137-1.5-029-INTERP: plan of a north-south beach, sea to the west.

Waves approach from the south-west (crests run NW-SE). A marked grain starts at origin O. Each cycle:
swash carries it north-east up the beach (+STEP east, +STEP north); backwash returns it due west down
the slope (-STEP east). Net per cycle: STEP north. Positions after cycles 1-4 are numbered.
Matches notes BL-6137-1.5.07-02.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.5-03'
ITEM = 'ITEM-6137-1.5-029-INTERP'
W, HQ, HA = 1000, 840, 1150
WATERLINE = 430
BEACH_TOP = 640               # landward edge of the beach
O = (450, 700)
STEP = 120
CYCLES = 4


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Plan of a beach: movement of one marked grain (not to scale)')
    fig.rect(20, 56, 960, 720, '#ffffff', GREY, 2, 8)
    fig.rect(22, 58, WATERLINE - 22, 716, C['sea'], 'none', 0)
    fig.rect(WATERLINE, 58, BEACH_TOP - WATERLINE, 716, C['sand'], 'none', 0)
    fig.rect(BEACH_TOP, 58, 978 - BEACH_TOP, 716, C['land'], 'none', 0)
    fig.line(WATERLINE, 58, WATERLINE, 774, C['blue'], 3)
    fig.text(120, 110, 'SEA', 30, 'middle', 'bold', C['blue'])
    fig.text(540, 110, 'BEACH', 30, 'middle', 'bold', '#8a6a2e')
    fig.text(810, 110, 'LAND', 30, 'middle', 'bold', C['green'])
    # wave crests running NW-SE, waves travelling towards the north-east
    r2 = 0.7071
    for t in range(-4, 8):
        for sgn in range(-4, 5):
            cx, cy = 150 + t * 80 * r2 + sgn * 170 * r2, 560 - t * 80 * r2 + sgn * 170 * r2
            ends = [(cx - 60 * r2, cy - 60 * r2), (cx + 60 * r2, cy + 60 * r2)]
            if all(30 < x < WATERLINE - 14 and 140 < y < 660 for x, y in ends):
                fig.line(*ends[0], *ends[1], C['blue'], 2.5)
    fig.arrow(120, 700, 240, 580, C['blue'], 5, 18)
    fig.text(110, 740, 'waves approach', 26, 'start', 'normal', C['blue'], halo=True)
    # grain path
    x, y = O
    pts = [O]
    for k in range(CYCLES):
        sx, sy = x + STEP, y - STEP
        fig.arrow(x, y, sx, sy, C['blue'], 4, 16, halo=True)
        fig.arrow(sx, sy, x, sy, C['red'], 4, 16, halo=True, dash='10 6')
        x, y = x, sy
        pts.append((x, y))
    fig.circle(O[0], O[1], 12, '#ffffff', INK, 3)
    fig.text(O[0] - 18, O[1] + 10, 'O', 30, 'end', 'bold', INK, halo=True)
    for k, (px, py) in enumerate(pts[1:], 1):
        fig.circle(px, py, 8, INK, '#ffffff', 2)
        fig.text(px - 16, py + 9, str(k), 26, 'end', 'bold', INK, halo=True)
    fig.arrow(910, 300, 910, 190, INK, 4, 16)
    fig.text(910, 330, 'N', 30, 'middle', 'bold')
    ky = HQ - 30
    fig.arrow(40, ky - 9, 110, ky - 9, C['blue'], 4, 14, halo=False)
    fig.text(120, ky, 'swash', 26)
    fig.arrow(250, ky - 9, 320, ky - 9, C['red'], 4, 14, halo=False, dash='10 6')
    fig.text(330, ky, 'backwash', 26)
    fig.circle(500, ky - 9, 8, INK, '#ffffff', 2)
    fig.text(516, ky, 'grain position after cycle 1, 2, 3, 4', 26)

    A = 'a'
    fig.arrow(608, O[1], 608, pts[-1][1] + 10, C['answer'], 7, 26, A)
    fig.text(628, (O[1] + pts[-1][1]) / 2, 'net drift', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(628, (O[1] + pts[-1][1]) / 2 + 32, 'northward', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(O[0] + 60, O[1] - 20, '1', A)
    fig.marker(910 - 50, 230, '2', A)
    fig.marker(650, pts[-1][1] + 30, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Swash carries the grain north-east up the beach; backwash returns it west, straight down the slope: a zigzag.'),
                 ('2', 'Using the north arrow, each cycle leaves the grain farther north: positions 1 to 4 lie north of O.'),
                 ('3', 'So net drift is northward for the observed cycles. A change in wave approach could change it.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'plan view (schematic), north at top',
        'layout': {'sea': 'west (x < %d)' % WATERLINE, 'beach': 'x %d-%d' % (WATERLINE, BEACH_TOP), 'land': 'east'},
        'wave_approach': 'from the south-west (travelling north-east); crests NW-SE',
        'origin': O, 'step_px': STEP, 'cycles': CYCLES, 'positions': pts,
        'per_cycle': {'swash': '+%d east, +%d north' % (STEP, STEP), 'backwash': '-%d east (due west)' % STEP, 'net': '+%d north' % STEP},
        'question_withholds': ['longshore', 'drift', 'net', 'zigzag'],
        'independent_solution': ['zigzag: swash NE up the beach, backwash W downslope (1)', 'north arrow + positions 1-4 north of O (1)',
                                 'net drift northward for the observed interval (1)'],
    }
    checks = [
        check('every position lies due north of the previous one', all(b[0] == a[0] and b[1] < a[1] for a, b in zip(pts, pts[1:]))),
        check('backwash is due west (downslope towards the sea)', True, 'drawn as -%d px in x, 0 in y' % STEP),
        check('swash stays on the beach (between waterline and landward edge)', all(WATERLINE < p[0] + STEP < BEACH_TOP for p in pts[:-1])),
        check('grain path starts in the swash zone near the waterline', WATERLINE < O[0] < WATERLINE + 60),
        check('wave crests run NW-SE (perpendicular to north-east travel) and stay in the sea', True, 'segments along (+1,+1) screen direction, clipped to x < waterline'),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'longshore', r'drift', r'\bnet\b', r'zigzag']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 720)])


if __name__ == '__main__':
    main()
