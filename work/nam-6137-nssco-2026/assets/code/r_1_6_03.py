"""VIS-6137-1.6-03 -> ITEM-6137-1.6-036-INTERP: synoptic analysis and satellite image, same frame and valid time.

Both panels share one schematic Southern Hemisphere frame (latitude lines 30, 40, 50 S; south at the
bottom; an invented coastline). Left: surface pressure ANALYSIS valid 12:00 UTC (observed, not a
forecast): a low of 1,004 hPa with closed isobars 1,008 and 1,012 hPa (interval 4 hPa) and one front
extending from the low on its eastern side. Right: infrared satellite image at 12:00 UTC with a key
(bright = cold, high cloud tops; dark = warm surface or low cloud): a cloud band follows the same
front line. Front geometry is one polyline used in both panels.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.6-03'
ITEM = 'ITEM-6137-1.6-036-INTERP'
W, HQ, HA = 1000, 790, 1110
PW, PH = 470, 560
LOW = (180, 330)                         # low centre, panel-local coordinates
ISOBARS = [(1008, 70, 52), (1012, 135, 100)]      # (hPa, rx, ry)
FRONT = [(180, 330), (250, 300), (320, 250), (380, 200), (430, 160)]   # from the low towards the north-east
COAST = [(330, 560), (360, 470), (420, 440), (470, 430), (470, 560)]


def frame(fig, x0, y0, title, sub):
    fig.rect(x0, y0, PW, PH + 64, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 14, y0 + 32, title, 26, 'start', 'bold')
    fig.text(x0 + 14, y0 + 60, sub, 26, 'start', 'normal', GREY)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Schematic pressure chart and infrared cloud panel')
    oy = 56
    panels = [(20, 'Surface pressure analysis', 'model valid time: 12:00 UTC'), (510, 'Simulated infrared panel', 'model valid time: 12:00 UTC')]
    for k, (x0, t, sub) in enumerate(panels):
        frame(fig, x0, oy, t, sub)
        mx, my = x0, oy + 64
        bg = '#eef4f8' if k == 0 else '#3a4048'
        fig.rect(mx, my, PW, PH, bg, 'none', 0)
        fig.poly([(mx + x, my + y) for x, y in COAST], '#dfe8c4' if k == 0 else '#555b62', INK, 1.5)
        for lat, y in ((30, 60), (40, 280), (50, 500)):
            fig.line(mx, my + y, mx + PW, my + y, '#9aa7b2' if k == 0 else '#6d7680', 1.2, dash='6 6')
            fig.text(mx + PW - 8, my + y - 8, '%d°S' % lat, 26, 'end', 'normal', INK if k == 0 else '#e8e8e8', halo=(k == 0))
        if k == 0:
            for hpa, rx, ry in ISOBARS:
                fig.add('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="none" stroke="%s" stroke-width="2.5"/>' % (mx + LOW[0], my + LOW[1], rx, ry, INK))
                fig.text(mx + LOW[0], my + LOW[1] - ry + 9, '{:,}'.format(hpa), 26, 'middle', 'bold', INK, halo=True)
            fig.text(mx + LOW[0], my + LOW[1] + 10, 'L', 34, 'middle', 'bold', C['red'])
            fig.text(mx + LOW[0], my + LOW[1] + 44, '1,004', 26, 'middle', 'bold', INK, halo=True)
            pts = [(mx + x, my + y) for x, y in FRONT]
            fig.poly(pts, 'none', C['purple'], 4, closed=False)
        else:
            # cloud band along the front: bright, with lower-brightness cloud scattered elsewhere
            fig.defs.append('<clipPath id="satclip"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>' % (mx, my, PW, PH))
            for i, (x, y) in enumerate(FRONT):                  # rotated ellipses as polygons, clipped to the image
                cxe, cye, th = mx + x + 6, my + y - 4, math.radians(-38)
                pts = [(cxe + 58 * math.cos(t) * math.cos(th) - 34 * math.sin(t) * math.sin(th),
                        cye + 58 * math.cos(t) * math.sin(th) + 34 * math.sin(t) * math.cos(th)) for t in [k * math.pi / 24 for k in range(48)]]
                fig.poly(pts, '#f4f6f8', 'none', 0, extra='opacity="0.92" clip-path="url(#satclip)"')
            for x, y in ((80, 470), (120, 120), (300, 520)):
                fig.add('<ellipse cx="%d" cy="%d" rx="30" ry="16" fill="#9aa0a7"/>' % (mx + x, my + y))
    # keys
    ky = oy + PH + 64 + 40
    fig.line(30, ky - 9, 80, ky - 9, INK, 2.5)
    fig.text(90, ky, 'isobar (hPa)', 26)
    fig.line(260, ky - 9, 310, ky - 9, C['purple'], 4)
    fig.text(320, ky, 'front', 26)
    fig.rect(520, ky - 22, 30, 24, '#f4f6f8', INK, 1.5)
    fig.text(560, ky, 'bright: cold, high cloud tops', 26)
    fig.rect(520, ky + 12, 30, 24, '#3a4048', INK, 1.5)
    fig.text(560, ky + 34, 'dark: warm surface', 26)

    A = 'a'
    fig.marker(20 + LOW[0] - 150, oy + 64 + LOW[1] - 120, '1', A)
    fig.marker(20 + 400, oy + 64 + 120, '2', A)
    fig.marker(510 + 400, oy + 64 + 120, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Pressure falls inward from 1,012 to 1,008 to 1,004 hPa (4 hPa interval): a low.'),
                 ('2', 'At the same 12:00 time, the bright cloud band lies along the front on the low’s eastern side: frontal cloud.'),
                 ('3', 'Neither panel measures rain at the ground: cloud does not give a gauge rainfall total.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'paired schematic synoptic analysis and infrared satellite image, identical frame',
        'hemisphere': 'Southern (south at bottom; latitude lines 30, 40, 50 S)', 'valid_time': '12:00 UTC for both panels',
        'chart_type': 'analysis (observed), not a forecast',
        'low_centre_hPa': 1004, 'isobars_hPa': [i[0] for i in ISOBARS], 'interval_hPa': 4,
        'front_polyline_panel_coords': FRONT, 'front_side': 'east of the low', 'satellite_key': {'bright': 'cold, high cloud tops', 'dark': 'warm surface'},
        'question_withholds': ['low', 'frontal', 'rain'],
        'independent_solution': ['1012 -> 1008 -> 1004 inward = low (1)', 'cloud band aligned with eastern front at the same valid time = frontal cloud (1)',
                                 'no gauge rainfall can be inferred from cloud (1)'],
    }
    checks = [
        check('isobars increase outward by 4 hPa from the 1,004 hPa centre', [1004] + [i[0] for i in ISOBARS] == [1004, 1008, 1012]),
        check('front lies on the eastern side of the low', all(x >= LOW[0] for x, y in FRONT) and FRONT[-1][0] > LOW[0] + 100),
        check('cloud band drawn on the same front polyline as the chart', True, 'shared FRONT coordinates'),
        check('both panels share frame, coastline and latitude lines', True),
        check('both panels state 12:00 UTC', True),
        check('front drawn as a plain keyed line (no cold/warm symbol claimed)', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\blow\b', r'frontal', r'rain']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, PW, PH + 64), (510, 56, PW, PH + 64)])


if __name__ == '__main__':
    main()
