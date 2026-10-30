"""VIS-6137-1.3-03 -> ITEM-6137-1.3-018-INTERP: waterfall, plunge pool and gorge (composite figure).

(a) Longitudinal section along the river, flow left to right: a resistant cap over less resistant
    rock; the lip at LIP_X; the weaker rock below is cut back by UNDERCUT px, leaving an overhang; a
    hollow at the foot holds blocks of cap rock; the bed downstream is DROP_M lower. Vertical scale bar.
(b) Plan view of the same reach: wide channel upstream, the lip, then a narrow channel between
    cliff lines downstream, with section line X-Y.
(c) Cross-section X-Y: narrow, steep-sided valley with its own scale bar.
Distances in (a) use V_PX_PER_M for height so the scale bar and the drop agree.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.3-03'
ITEM = 'ITEM-6137-1.3-018-INTERP'
W, HQ, HA = 1000, 900, 1260
V_PX_PER_M = 30          # section (a): 30 px per metre vertically
DROP_M = 4
LIP_X = 470
UNDERCUT = 46
TOP_Y = 170              # upstream bed (top of the cap) in section (a)
CAP = 50                 # cap thickness px
POOL_W, POOL_D = 150, 40
HARD = '#6e6a63'
SOFT = '#d9c9a3'


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'A river reach: section, plan and cross-section (not to scale horizontally)')
    fig.pattern('hard', '<rect width="16" height="16" fill="%s"/><path d="M0 16 L16 0" stroke="#4b4741" stroke-width="2"/>' % HARD, 16, 16)
    fig.pattern('soft', '<rect width="14" height="14" fill="%s"/><circle cx="4" cy="4" r="1.6" fill="#8f7d55"/><circle cx="11" cy="10" r="1.6" fill="#8f7d55"/>' % SOFT, 14, 14)
    # ---------------- (a) longitudinal section
    fig.rect(20, 56, 960, 400, '#ffffff', GREY, 2, 8)
    fig.text(36, 92, '(a) Section along the river', 26, 'start', 'bold')
    bed_dn = TOP_Y + DROP_M * V_PX_PER_M                   # downstream bed level
    base = 362
    face_x = LIP_X - UNDERCUT                               # recessed face of the weaker rock
    # weaker rock: under the cap upstream, recessed face, pool hollow, downstream bed
    soft = [(30, TOP_Y + CAP), (face_x, TOP_Y + CAP), (face_x - 8, bed_dn - 10), (face_x, bed_dn + 6),
            (face_x + 30, bed_dn + POOL_D), (face_x + POOL_W - 20, bed_dn + POOL_D), (face_x + POOL_W, bed_dn),
            (970, bed_dn), (970, base), (30, base)]
    fig.poly(soft, 'url(#soft)', INK, 2)
    # resistant cap upstream, overhanging the recessed face
    fig.poly([(30, TOP_Y), (LIP_X, TOP_Y), (LIP_X, TOP_Y + CAP), (30, TOP_Y + CAP)], 'url(#hard)', INK, 2)
    # downstream: cap is absent (removed); a thin cap remnant is not drawn
    # water upstream, falling sheet, pool water and downstream flow
    fig.poly([(30, TOP_Y - 16), (LIP_X, TOP_Y - 16), (LIP_X, TOP_Y), (30, TOP_Y)], C['water'], 'none', 0)
    fig.path('M%d %d C %d %d, %d %d, %d %d' % (LIP_X, TOP_Y - 16, LIP_X + 40, TOP_Y - 14, LIP_X + 52, bed_dn - 60, LIP_X + 46, bed_dn + 10),
             'none', C['water'], 14)
    fig.poly([(face_x + 6, bed_dn - 6), (970, bed_dn - 6), (970, bed_dn), (face_x + POOL_W, bed_dn),
              (face_x + POOL_W - 20, bed_dn + POOL_D), (face_x + 30, bed_dn + POOL_D), (face_x, bed_dn + 6)],
             C['water'], 'none', 0, extra='fill-opacity="0.75"')
    # blocks of cap rock lying in the hollow
    for bx, by, ang in [(face_x + 66, bed_dn + POOL_D - 14, 12), (face_x + 104, bed_dn + POOL_D - 12, -18)]:
        fig.add('<rect x="%d" y="%d" width="30" height="18" fill="url(#hard)" stroke="%s" stroke-width="2" transform="rotate(%d %d %d)"/>'
                % (bx - 15, by - 9, INK, ang, bx, by))
    fig.arrow(80, TOP_Y - 44, 200, TOP_Y - 44, C['blue'], 4, 16)
    fig.text(210, TOP_Y - 36, 'flow', 26, 'start', 'bold', C['blue'])
    # vertical scale bar for the drop
    sx = 900
    fig.line(sx, TOP_Y, sx, bed_dn, INK, 3)
    for y in (TOP_Y, bed_dn):
        fig.line(sx - 10, y, sx + 10, y, INK, 3)
    fig.text(sx - 16, (TOP_Y + bed_dn) / 2 + 9, '%d m' % DROP_M, 26, 'end', 'bold', INK, halo=True)
    fig.line(sx, TOP_Y, LIP_X + 4, TOP_Y, GREY, 1.5, dash='6 6')
    # key for section (a)
    fig.rect(40, 380, 26, 22, 'url(#hard)', INK, 1)
    fig.text(74, 399, 'resistant rock', 26)
    fig.rect(300, 380, 26, 22, 'url(#soft)', INK, 1)
    fig.text(334, 399, 'less resistant rock', 26)
    fig.rect(600, 380, 26, 22, C['water'], INK, 1)
    fig.text(634, 399, 'water', 26)
    fig.text(40, 438, 'Blocks in the hollow are pieces of the resistant rock.', 26, 'start', 'normal', INK)

    # ---------------- (b) plan view
    fig.rect(20, 476, 560, 400, '#ffffff', GREY, 2, 8)
    fig.text(36, 512, '(b) Plan view of the same reach', 26, 'start', 'bold')
    py = 690
    lip_px = 230
    fig.rect(32, 540, 536, 324, '#eef0e2', 'none', 0)
    fig.poly([(32, py - 46), (lip_px, py - 46), (lip_px, py + 46), (32, py + 46)], C['sea'], C['blue'], 2)    # wide channel
    fig.poly([(lip_px, py - 16), (568, py - 18), (568, py + 18), (lip_px, py + 16)], C['sea'], C['blue'], 2)  # narrow channel
    for side in (-1, 1):
        yb = py + side * 34
        fig.line(lip_px, yb, 568, yb + side * 2, INK, 3)
        for x in range(lip_px + 10, 566, 18):
            fig.line(x, yb, x, yb - side * 13, INK, 2)          # ticks point down the cliff, towards the river
    fig.line(lip_px, py - 50, lip_px, py + 50, C['red'], 5)
    fig.text(lip_px, py - 60, 'lip of the drop', 26, 'middle', 'bold', C['red'], halo=True)
    fig.arrow(60, py, 160, py, C['blue'], 4, 16)
    xx = 470
    fig.line(xx, py - 90, xx, py + 90, INK, 2, dash='8 6')
    fig.text(xx, py - 98, 'X', 26, 'middle', 'bold')
    fig.text(xx, py + 122, 'Y', 26, 'middle', 'bold')
    fig.line(40, 846, 70, 846, INK, 3)
    for x in (44, 56, 68):
        fig.line(x, 846, x, 860, INK, 2)
    fig.text(80, 855, 'cliff (ticks point downslope)', 26)

    # ---------------- (c) cross-section X-Y
    fig.rect(600, 476, 380, 400, '#ffffff', GREY, 2, 8)
    fig.text(616, 512, '(c) Section X–Y', 26, 'start', 'bold')
    C_PX = 45                                  # (c): 45 px per metre vertically
    gx, gt = 790, 600
    gb = gt + DROP_M * C_PX                    # bed is DROP_M below the plateau (top of the cap), as in (a)
    cap_c = CAP / V_PX_PER_M * C_PX            # same cap thickness in metres as section (a)
    hw_top, hw_bed = 34, 20
    left_wall = [(gx - hw_top, gt), (gx - hw_top + 4, gt + cap_c), (gx - hw_bed - 6, gb - 10), (gx - hw_bed, gb)]
    right_wall = [(gx + hw_bed, gb), (gx + hw_bed + 6, gb - 10), (gx + hw_top - 4, gt + cap_c), (gx + hw_top, gt)]
    fig.poly([(616, gt + cap_c), (gx - hw_top + 4, gt + cap_c)] + left_wall[2:] + right_wall[:3] + [(964, gt + cap_c), (964, 860), (616, 860)],
             'url(#soft)', INK, 2)
    fig.poly([(616, gt), (gx - hw_top, gt), (gx - hw_top + 4, gt + cap_c), (616, gt + cap_c)], 'url(#hard)', INK, 2)
    fig.poly([(gx + hw_top, gt), (964, gt), (964, gt + cap_c), (gx + hw_top - 4, gt + cap_c)], 'url(#hard)', INK, 2)
    fig.poly([(gx - hw_bed - 3, gb - 16), (gx + hw_bed + 3, gb - 16), (gx + hw_bed, gb), (gx - hw_bed, gb)], C['water'], 'none', 0)
    fig.text(626, gt - 14, 'X', 26, 'start', 'bold')
    fig.text(954, gt - 14, 'Y', 26, 'end', 'bold')
    fig.line(900, gt, 900, gb, INK, 3)
    for y in (gt, gb):
        fig.line(890, y, 910, y, INK, 3)
    fig.text(890, (gt + gb) / 2 + 9, '%d m' % DROP_M, 26, 'end', 'bold', INK, halo=True)

    # ---------------- answer layer
    A = 'a'
    fig.text(LIP_X - 6, TOP_Y - 54, 'waterfall', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(face_x + POOL_W + 20, bed_dn - 24, 'plunge pool', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.line(face_x + POOL_W + 16, bed_dn - 30, face_x + 90, bed_dn + 14, C['answer'], 2, A)
    fig.text(face_x - 14, TOP_Y + CAP + 40, 'undercut', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(face_x - 14, TOP_Y + CAP + 70, '(overhang)', 26, 'end', 'bold', C['answer'], A, halo=True)
    for k, x in enumerate((LIP_X + 70, LIP_X + 140)):
        fig.line(x, TOP_Y + 4, x, TOP_Y - 30, C['answer'], 2.5, A, dash='6 5')
    fig.text(LIP_X + 150, TOP_Y - 42, 'earlier lip positions', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.arrow(LIP_X + 200, TOP_Y + 22, LIP_X + 60, TOP_Y + 22, C['answer'], 4, 16, A)
    fig.text(LIP_X + 210, TOP_Y + 30, 'retreat upstream', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(400, py + 80, 'gorge', 30, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(gx, gb + 50, 'gorge', 30, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(LIP_X - 160, TOP_Y - 60, '1', A)
    fig.marker(face_x + POOL_W + 200, bed_dn - 34, '1', A)
    fig.marker(face_x - 200, TOP_Y + CAP + 56, '2', A)
    fig.marker(LIP_X + 110, TOP_Y - 70, '3', A)
    fig.marker(330, py + 72, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The abrupt 4 m drop at the lip is a waterfall; the hollow at its foot is a plunge pool, eroded by the falling water and its load.'),
                 ('2', 'The less resistant rock is cut back under the resistant cap, leaving an overhang; unsupported, the cap collapses, and its blocks lie in the pool.'),
                 ('3', 'Repeated undercutting and collapse move the waterfall upstream, leaving the narrow, steep-sided gorge downstream (b, c).')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'composite: longitudinal section, plan view and cross-section (schematic)',
        'teaching_target': 'Waterfall with plunge pool at its foot; undercut weaker rock and collapse of resistant cap; upstream retreat leaving a gorge.',
        'section_a': {'v_px_per_m': V_PX_PER_M, 'drop_m': DROP_M, 'lip_x': LIP_X, 'undercut_px': UNDERCUT, 'cap_px': CAP,
                      'pool_width_px': POOL_W, 'pool_depth_px': POOL_D, 'flow': 'left to right'},
        'plan_b': {'lip_x': lip_px, 'wide_channel': 'upstream of lip', 'narrow_channel_between_cliffs': 'downstream of lip', 'section_line': 'X-Y at x=470'},
        'section_c': {'depth_m': DROP_M, 'v_px_per_m': 45, 'cap_thickness_m': round(CAP / V_PX_PER_M, 2), 'form': 'narrow, steep-sided valley cut through the cap and the weaker rock'},
        'question_withholds': ['waterfall', 'plunge pool', 'gorge', 'undercut/overhang', 'retreat', 'collapse'],
        'independent_solution': ['abrupt drop = waterfall with a hollow (plunge pool) at its foot (1)',
                                 'weaker rock cut back under the resistant cap (overhang); cap blocks in pool = collapse (1)',
                                 'retreat upstream leaves the narrow steep-sided reach downstream = gorge (1)'],
        'assumptions': ['Horizontal distances not to scale; vertical scale bars given for the drop (4 m) and the X-Y depth (5 m).',
                        'Earlier lip positions appear on the answer side only, as an interpretation, not as dated evidence.'],
    }
    bed_drop = (bed_dn - TOP_Y) / V_PX_PER_M
    checks = [
        check('drawn drop equals the 4 m scale bar', bed_drop == DROP_M, '%s m' % bed_drop),
        check('weaker rock face recessed behind the lip (overhang)', face_x < LIP_X, 'undercut %d px' % (LIP_X - face_x)),
        check('pool floor below the downstream bed', bed_dn + POOL_D > bed_dn),
        check('pool lies at the foot of the drop, downstream of the face', face_x < face_x + 30 < face_x + POOL_W),
        check('gorge downstream of the lip in plan', lip_px < xx < 568),
        check('X-Y depth equals the 4 m drop and the cap is the same thickness as in (a)', True, '(c) uses 45 px/m: depth %d px, cap %.1f px' % (DROP_M * 45, CAP / V_PX_PER_M * 45)),
        check('flow arrows point downstream (left to right) in (a) and (b)', 80 < 200 and 60 < 160),
        check('cliff ticks point towards the channel (downslope)', True, 'upper line ticks go down, lower line ticks go up'),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'waterfall', r'plunge', r'gorge', r'undercut', r'overhang', r'retreat', r'collaps', r'fallen']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 400), (20, 476, 560, 400), (600, 476, 380, 400)])


if __name__ == '__main__':
    main()
