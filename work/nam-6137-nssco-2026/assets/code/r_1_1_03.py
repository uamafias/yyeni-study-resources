"""VIS-6137-1.1-03 -> ITEM-6137-1.1-014-INTERP: conservative (transform) margin in PLAN view.

Looking straight down. A straight north-south fault separates plate M (west) and plate K (east).
Opposed arrows run parallel to the fault: M moves south, K moves north. A stream flowing east
crosses the fault; its eastern reach is displaced north by OFFSET, the same sense as N's arrow.
No trench, ridge or slab is drawn.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.1-03'
ITEM = 'ITEM-6137-1.1-014-INTERP'
W, HQ, HA = 1000, 720, 1110
FX = 500                 # fault line x
TOP, BOT = 90, 660       # map frame
Y_WEST = 470             # where the stream meets the fault from the west
OFFSET = 150             # northward displacement of the eastern reach (px)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Plan view of a plate margin (looking down from above; not to scale)')
    fig.rect(40, TOP, 920, BOT - TOP, '#e9f0d6', INK, 2)
    # a few field boundaries / vegetation dots for texture, mirrored so they do not imply an offset
    for x in range(80, 940, 70):
        for y in range(130, 640, 70):
            if abs(x - FX) > 30:
                fig.circle(x, y, 3, C['veg'], 'none', 0)
    # stream: west reach -> along the fault -> east reach (displaced north)
    ye = Y_WEST - OFFSET
    west = 'M40 %d C 150 %d, 260 %d, 360 %d S 470 %d, %d %d' % (Y_WEST + 60, Y_WEST + 90, Y_WEST + 20, Y_WEST + 10, Y_WEST, FX, Y_WEST)
    along = 'M%d %d L%d %d' % (FX, Y_WEST, FX, ye)
    east = 'M%d %d C 560 %d, 640 %d, 720 %d S 880 %d, 960 %d' % (FX, ye, ye, ye - 30, ye - 20, ye + 40, ye + 20)
    for d in (west, along, east):
        fig.path(d, 'none', C['water'], 9)
    # fault line on top
    fig.line(FX, TOP, FX, BOT, C['red'], 5, dash='22 10')
    fig.text(FX + 14, TOP + 34, 'Fault (plate margin)', 26, 'start', 'bold', C['red'], halo=True)
    # plate labels and opposed arrows parallel to the fault
    fig.text(250, 170, 'Plate M', 30, 'middle', 'bold', INK, halo=True)
    fig.text(750, 620, 'Plate K', 30, 'middle', 'bold', INK, halo=True)
    fig.arrow(320, 220, 320, 420, INK, 7, 26)          # M moves south
    fig.arrow(680, 600, 680, 400, INK, 7, 26)          # K moves north
    fig.text(210, Y_WEST + 128, 'Stream', 26, 'middle', 'bold', C['blue'], halo=True)
    # north arrow
    fig.arrow(905, 230, 905, 140, INK, 4, 18)
    fig.text(905, 262, 'N', 30, 'middle', 'bold')
    # key
    ky = HQ - 34
    fig.arrow(60, ky - 9, 130, ky - 9, INK, 5, 18)
    fig.text(142, ky, 'plate movement', 26)
    fig.line(380, ky - 9, 440, ky - 9, C['red'], 5, dash='14 8')
    fig.text(452, ky, 'fault', 26)
    fig.line(560, ky - 9, 620, ky - 9, C['water'], 9)
    fig.text(632, ky, 'stream (flows east)', 26)

    A = 'a'
    # bracket showing the offset along the fault
    fig.line(FX - 40, Y_WEST, FX - 40, ye, C['answer'], 3, A)
    fig.line(FX - 52, Y_WEST, FX - 28, Y_WEST, C['answer'], 3, A)
    fig.line(FX - 52, ye, FX - 28, ye, C['answer'], 3, A)
    fig.text(FX - 60, (Y_WEST + ye) / 2 + 9, 'offset', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.marker(275, 320, '1')
    fig.marker(725, 500, '1')
    fig.marker(FX + 34, 150, '2')
    fig.marker(FX + 40, (Y_WEST + ye) / 2, '3')
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The arrows are parallel to the fault and point in opposite directions: M moves south and K moves north.'),
                 ('2', 'So the plates slide horizontally past one another along the margin; no crust is created or destroyed.'),
                 ('3', 'The stream’s eastern part is displaced north along the fault, the same sense as K’s movement: '
                       'consistent with sideways displacement on the fault.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 4, 'The offset records past displacement; on its own it does not show when the fault moved.',
             26, 920, 32, layer=A)

    spec = {
        'kind': 'plan view (map-like), schematic, not to scale',
        'viewing_direction': 'vertical, looking down; north at top (north arrow)',
        'teaching_target': 'Conservative margin: opposed arrows parallel to the fault, horizontal sliding, a stream offset in the same sense as the relative movement.',
        'geometry': {'fault_x': FX, 'fault_strike': 'north-south', 'plate_M_motion': 'south (west side)', 'plate_K_motion': 'north (east side)',
                     'stream_meets_fault_from_west_y': Y_WEST, 'stream_leaves_fault_eastward_y': ye, 'offset_px': OFFSET,
                     'sense': 'east side displaced north relative to west side (left-lateral)'},
        'question_shows': ['fault (plate margin) line', 'opposed arrows parallel to the fault', 'stream crossing with an offset', 'north arrow', 'key'],
        'question_withholds': ['margin type name', 'the words slide/transform/conservative/offset/displaced', 'offset bracket'],
        'independent_solution': ['plates slide past each other horizontally, parallel to the margin (1)', 'arrows parallel to the fault and opposed (1)',
                                 'stream displaced sideways along the fault in the same sense as relative movement (1)'],
        'assumptions': ['Offset is past cumulative displacement; no dated evidence of movement during any observation period.'],
    }
    checks = [
        check('arrows parallel to the fault (both vertical)', True, 'M: (320,220)->(320,420); K: (680,600)->(680,400)'),
        check('arrows opposed and on opposite sides of the fault', 320 < FX < 680 and (420 - 220) * (400 - 600) < 0),
        check('stream offset sense matches relative motion (east side moved north)', ye < Y_WEST and (400 - 600) < 0),
        check('no subduction/ridge elements drawn', True, 'only fault, arrows, stream, north arrow, key'),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'conservative', r'transform', r'slide', r'offset', r'displac', r'lateral']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
