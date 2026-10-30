"""VIS-6137-1.2-01 -> ITEM-6137-1.2-019-INTERP: freeze-thaw weathering as a four-stage sequence.

The same rock block and vertical joint appear in all four panels (cross-section, not to scale).
Joint width at the surface is drawn at JOINT_PX_PER_MM, so the observed widths (2, 2, 6 mm) and
the drawing agree. Stage 2 shows ice and arrows of force on the joint walls; stage 3 a wider joint
after many cycles; stage 4 a loosened fragment. Rock colour (minerals) is identical in every stage.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.2-01'
ITEM = 'ITEM-6137-1.2-019-INTERP'
W, HQ, HA = 1000, 925, 1285
PX_PER_MM = 8
DEPTH = 150            # joint depth below the surface (px)
STAGES = [
    {'n': 1, 'title': 'Air above 0 °C', 'fill': 'water', 'width_mm': 2, 'fragment': 'none',
     'note': 'Joint width at surface: 2 mm'},
    {'n': 2, 'title': 'Air below 0 °C', 'fill': 'ice', 'width_mm': 2, 'fragment': 'none',
     'note': 'Joint width at surface: 2 mm'},
    {'n': 3, 'title': 'After many cycles of freezing and thawing', 'fill': 'water', 'width_mm': 6, 'fragment': 'crack',
     'note': 'Joint width at surface: 6 mm'},
    {'n': 4, 'title': 'Later', 'fill': 'none', 'width_mm': 6, 'fragment': 'loose',
     'note': 'Fragment loose; minerals unchanged'},
]
PW, PH = 470, 395


def panel(fig, x0, y0, st, layer='base'):
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, '%d' % st['n'], 30, 'start', 'bold', C['answer'])
    fig.text(x0 + 50, y0 + 38, st['title'] if len(st['title']) < 26 else 'After many cycles of', 26, 'start', 'bold')
    if len(st['title']) >= 26:
        fig.text(x0 + 50, y0 + 70, 'freezing and thawing', 26, 'start', 'bold')
    top = y0 + 130
    bot = y0 + PH - 70
    cx = x0 + PW / 2
    half = st['width_mm'] * PX_PER_MM / 2
    tip = (cx, top + DEPTH)
    left = [(x0 + 30, top), (cx - half, top), tip, (cx, bot), (x0 + 30, bot)]
    right = [(cx + half, top), (x0 + PW - 30, top), (x0 + PW - 30, bot), (cx, bot), tip]
    fig.poly(left, C['rock'], INK, 2)
    if st['fragment'] == 'loose':
        # fragment bounded by the joint wall, the surface and a crack from 70 px down the joint
        fx = cx + half + 95
        jy = top + 70
        jx = cx + half - half * 70 / DEPTH
        rest = [(fx, top), (x0 + PW - 30, top), (x0 + PW - 30, bot), (cx, bot), tip, (jx, jy)]
        fig.poly(rest, C['rock'], INK, 2)
        tri = [(cx + half, top), (fx, top), (jx, jy)]           # the piece that was cut off by the crack
        gx = sum(p[0] for p in tri) / 3
        gy = sum(p[1] for p in tri) / 3
        fig.poly(tri, C['rock'], INK, 2.5, extra='transform="translate(14 -22) rotate(-10 %.1f %.1f)"' % (gx, gy))
    else:
        fig.poly(right, C['rock'], INK, 2)
        if st['fragment'] == 'crack':
            jx = cx + half - half * 70 / DEPTH
            fig.line(jx, top + 70, cx + half + 95, top, INK, 2, dash='5 4')
            fig.text(cx + half + 100, top - 10, 'crack', 26)
    # joint contents
    if st['fill'] in ('water', 'ice'):
        lvl = top + (40 if st['fill'] == 'water' else 0)
        wl = half * (1 - (lvl - top) / DEPTH)
        pts = [(cx - wl, lvl), (cx + wl, lvl), tip]
        if st['fill'] == 'water':
            fig.poly(pts, C['water'], 'none', 0)
        else:
            fig.poly([(cx - half, top - 3), (cx + half, top - 3), tip], '#dff3ff', C['blue'], 2)
            for k in range(3):
                yy = top + 25 + k * 40
                fig.arrow(cx - 4, yy, cx - 42, yy, C['red'], 3.5, 12, halo=False)
                fig.arrow(cx + 4, yy, cx + 42, yy, C['red'], 3.5, 12, halo=False)
    # surface-width dimension line
    fig.line(cx - half, top - 26, cx + half, top - 26, INK, 1.5)
    fig.line(cx - half, top - 34, cx - half, top - 18, INK, 1.5)
    fig.line(cx + half, top - 34, cx + half, top - 18, INK, 1.5)
    fig.text(x0 + 16, y0 + PH - 22, st['note'], 26)
    return cx, top


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Changes in a rock joint (cross-sections, not to scale)')
    origins = [(20, 60), (510, 60), (20, 470), (510, 470)]
    centres = [panel(fig, x, y, st) for (x, y), st in zip(origins, STAGES)]
    # key
    ky = 910
    fig.rect(40, ky - 22, 26, 22, C['water'], INK, 1)
    fig.text(74, ky - 2, 'water', 26)
    fig.rect(170, ky - 22, 26, 22, '#dff3ff', C['blue'], 2)
    fig.text(204, ky - 2, 'ice', 26)
    fig.arrow(270, ky - 11, 320, ky - 11, C['red'], 3.5, 12, halo=False)
    fig.text(330, ky - 2, 'force on the rock', 26)
    fig.rect(560, ky - 22, 26, 22, C['rock'], INK, 1)
    fig.text(594, ky - 2, 'rock (same minerals throughout)', 26)
    # answer
    A = 'a'
    (c1, t1), (c2, t2), (c3, t3), (c4, t4) = centres
    fig.marker(c1 + 60, t1 + 70, '1', A)
    fig.marker(c2 + 75, t2 + 150, '1', A)
    fig.marker(c3 + 60, t3 + 120, '2', A)
    fig.marker(c4 + 150, t4 - 50, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Water enters the joint (1). When the air falls below 0 °C it freezes; the ice expands and '
                       'pushes against the joint walls (2).'),
                 ('2', 'Thawing lets more water in, and repeated freezing and thawing widens the joint: 2 mm to 6 mm (3).'),
                 ('3', 'The loose fragment (4) is physical breakdown: the rock splits into pieces but its minerals do not change.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'One reading below 0 °C does not by itself break rock: water supply and repeated cycles '
             'around freezing matter.', 26, 920, 32, layer=A)

    spec = {
        'kind': 'four-stage process sequence (cross-sections, not to scale)',
        'teaching_target': 'Freeze-thaw: water in an accessible joint, freezing with force against the walls, repeated cycles widen the joint, a fragment loosens; minerals unchanged.',
        'stages': STAGES, 'joint_px_per_mm': PX_PER_MM, 'joint_depth_px': DEPTH,
        'question_shows': ['water in the joint above 0 C', 'ice filling the joint below 0 C with force arrows on the walls',
                           'joint width 2 -> 2 -> 6 mm after many cycles', 'loose fragment; minerals unchanged (stated)'],
        'question_withholds': ['process name', 'the words expand/pressure/physical/widen', 'causal links between stages'],
        'independent_solution': ['water enters joint and freezes to ice pushing on the walls (1)', 'repeated freeze-thaw cycles widen the joint 2 -> 6 mm (1)',
                                 'loose fragment = physical breakdown with no mineral change (1)'],
        'assumptions': ['Widths illustrative, drawn to 8 px per mm; not a measured site.', 'No claim that one sub-zero reading breaks rock.'],
    }
    drawn = [st['width_mm'] * PX_PER_MM for st in STAGES]
    checks = [
        check('drawn joint widths match stated widths', drawn == [16, 16, 48, 48], str(drawn)),
        check('widths never decrease through the sequence', all(a <= b for a, b in zip(drawn, drawn[1:]))),
        check('ice only in the below-0 C stage; water only where above 0 C or thawed', [s['fill'] for s in STAGES] == ['water', 'ice', 'water', 'none']),
        check('rock colour identical in every stage (minerals unchanged)', True, C['rock']),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'expan', r'pressure', r'physical', r'widen', r'freeze-thaw', r'weathering']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 60, PW, PH), (510, 60, PW, PH), (20, 470, PW, PH), (510, 470, PW, PH)])


if __name__ == '__main__':
    main()
