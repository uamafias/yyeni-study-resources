"""VIS-6137-1.3-02 -> ITEM-6137-1.3-007-INTERP: longitudinal profile with height and distance scales.

The profile passes exactly through the values used in notes block BL-6137-1.3.02-06 (900 m at 0 km,
500 m at 10 km, 200 m at 30 km, 100 m at 50 km) and adds one local exception: an abrupt 40 m step
between 19.7 and 20.0 km. A monotone cubic (PCHIP) joins the anchor points, so the line never rises.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, pchip, build, check  # noqa: E402

RID = 'VIS-6137-1.3-02'
ITEM = 'ITEM-6137-1.3-007-INTERP'
W, HQ, HA = 1000, 760, 1120
ANCHORS = [(0, 900), (3, 740), (10, 500), (15, 420), (19.7, 358), (20.0, 318), (25, 255), (30, 200), (40, 140), (50, 100)]


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Longitudinal profile of a river (vertical scale exaggerated)')
    ax = Axes(fig, 160, 90, 780, 520, (0, 50), (0, 1000))
    ax.draw(range(0, 51, 10), range(0, 1001, 200), 'Distance downstream from source (km)', 'Height above sea level (m)',
            minor_y=range(100, 1000, 200), minor_x=range(5, 50, 10))
    fn = pchip([a for a, b in ANCHORS], [b for a, b in ANCHORS])
    xs = [i / 20 for i in range(0, 1001)]
    pts = [(x, fn(x)) for x in xs]
    ax.polyline(pts, C['blue'], 5)
    fig.circle(ax.X(0), ax.Y(900), 7, C['blue'], INK, 2)
    fig.text(ax.X(0) + 16, ax.Y(900) - 14, 'Source', 26, 'start', 'bold', INK, halo=True)
    fig.circle(ax.X(50), ax.Y(100), 7, C['blue'], INK, 2)
    fig.text(ax.X(50) - 6, ax.Y(100) - 62, 'Downstream end', 26, 'end', 'bold', INK, halo=True)

    A = 'a'
    for (xa, xb), lab, yoff in [((0, 10), '400 m drop in 10 km = 1:25', -60), ((10, 30), '300 m in 20 km ≈ 1:67', -50),
                                ((30, 50), '100 m in 20 km = 1:200', -46)]:
        ya, yb = fn(xa), fn(xb)
        fig.line(ax.X(xa), ax.Y(ya), ax.X(xb), ax.Y(yb), C['answer'], 3, A, dash='8 6')
    fig.text(ax.X(4) + 30, ax.Y(560), '0–10 km: 1:25', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(ax.X(16), ax.Y(470), '10–30 km: ≈ 1:67', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(ax.X(31), ax.Y(70), '30–50 km: 1:200', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.circle(ax.X(19.85), ax.Y(338), 26, 'none', C['red'], 3, A)
    fig.text(ax.X(21.5), ax.Y(340) + 8, 'step: about 40 m', 26, 'start', 'bold', C['red'], A, halo=True)
    fig.marker(ax.X(46), ax.Y(330), '1', A)
    fig.marker(ax.X(2.5), ax.Y(560), '2', A)
    fig.marker(ax.X(17.5), ax.Y(300), '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The river falls from 900 m at the source to 100 m at 50 km.'),
                 ('2', 'It is steeper upstream and gentler downstream: 400 m in the first 10 km (1:25) but only 100 m in the last 20 km (1:200).'),
                 ('3', 'Local exception: an abrupt step of about 40 m at about 20 km, so the fall is not smooth everywhere.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'A profile gives height and distance only: it does not show how fast the water flows.', 26, 920, 32, layer=A)

    spec = {
        'kind': 'line graph: longitudinal profile (height vs distance downstream)',
        'axes': {'x': {'label': 'Distance downstream from source (km)', 'range': [0, 50], 'major': 10, 'minor': 5},
                 'y': {'label': 'Height above sea level (m)', 'range': [0, 1000], 'major': 200, 'minor': 100}},
        'anchor_points_km_m': ANCHORS, 'interpolation': 'monotone cubic (PCHIP) through anchors; sampled every 0.05 km',
        'notes_values_matched': {'0': 900, '10': 500, '30': 200, '50': 100},
        'local_step': {'from_km': 19.7, 'to_km': 20.0, 'drop_m': 40},
        'derived': {'0-10 km': {'drop_m': 400, 'gradient': '1:25'}, '10-30 km': {'drop_m': 300, 'gradient': '1:66.7'},
                    '30-50 km': {'drop_m': 100, 'gradient': '1:200'}},
        'question_withholds': ['gradient values', 'step annotation', 'the words steep/gentle/waterfall/knickpoint'],
        'independent_solution': ['falls 900 -> 100 m (1)', 'steeper upstream (400 m in first 10 km) than downstream (100 m in last 20 km) (1)',
                                 'local abrupt step ~40 m at ~20 km (1)'],
    }
    seg = lambda a, b: (fn(a) - fn(b)) / (b - a)
    reach = [seg(0, 10), seg(10, 30), seg(30, 50)]
    checks = [
        check('profile passes through the notes values', all(abs(fn(k) - v) < 1e-9 for k, v in [(0, 900), (10, 500), (30, 200), (50, 100)])),
        check('profile never rises downstream', all(pts[i + 1][1] <= pts[i][1] + 1e-9 for i in range(len(pts) - 1))),
        check('reach gradients decrease downstream', reach[0] > reach[1] > reach[2], 'm/km: %s' % [round(r, 1) for r in reach]),
        check('gradient ratios', (round(10000 / 400), round(20000 / 300, 1), round(20000 / 100)) == (25, 66.7, 200)),
        check('local step steeper than any reach before it', seg(19.7, 20.0) > seg(0, 3), 'step %.0f m/km vs first 3 km %.0f m/km' % (seg(19.7, 20.0), seg(0, 3))),
        check('step drop 40 m', abs((fn(19.7) - fn(20.0)) - 40) < 1e-9),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'1:', r'steep', r'gentle', r'waterfall', r'knick', r'step']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
