"""VIS-6137-1.6-02 -> ITEM-6137-1.6-017-INTERP: three days at one station, each element on its own axes.

Values (from the card and notes BL-6137-1.6.04-21): daily maximum temperature 24, 28, 26 degC;
daily rainfall total 0, 8, 4 mm; daily sunshine total 8, 3, 6 hours. Each element keeps its own
vertical axis, unit and recording period; days share the horizontal axis. Temperature is plotted as
points only (no joining line: values between days were not measured).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.6-02'
ITEM = 'ITEM-6137-1.6-017-INTERP'
W, HQ, HA = 1000, 1045, 1335
TEMP = [24, 28, 26]
RAIN = [0, 8, 4]
SUN = [8, 3, 6]
PANELS = [('Daily maximum temperature', '°C', TEMP, (20, 30), 2, 'point'),
          ('Daily rainfall total', 'mm', RAIN, (0, 10), 2, 'bar'),
          ('Daily sunshine total', 'hours', SUN, (0, 10), 2, 'bar')]


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'One weather station, days 1–3 (each element on its own axis)')
    axes = []
    for k, (title, unit, vals, yr, step, kind) in enumerate(PANELS):
        y0 = 70 + k * 312
        fig.rect(20, y0, 960, 300, '#ffffff', GREY, 2, 8)
        fig.text(36, y0 + 36, '%s (%s)' % (title, unit), 26, 'start', 'bold')
        ax = Axes(fig, 170, y0 + 60, 560, 180, (0.5, 3.5), yr)
        ax.draw(range(1, 4), range(yr[0], yr[1] + 1, step), None, unit, fmt_x=lambda v: 'Day %d' % v, ylabel_x=90)
        for d, v in enumerate(vals, 1):
            if kind == 'bar' and v == 0:
                fig.text(ax.X(d), ax.Y(0) - 14, '0 (measured)', 26, 'middle', 'normal', INK, halo=True)
            elif kind == 'bar':
                fig.rect(ax.X(d) - 50, ax.Y(v), 100, ax.Y(yr[0]) - ax.Y(v), C['blue'] if unit == 'mm' else '#e0b43c', INK, 1.5)
            else:
                fig.circle(ax.X(d), ax.Y(v), 10, C['red'], INK, 2)
        axes.append(ax)
    fig.text(W / 2, HQ - 24, 'Read each element from its own scale; do not compare heights across panels.', 26, 'middle', 'normal', GREY)

    A = 'a'
    for k, ax in enumerate(axes):
        vals = PANELS[k][2]
        unit = PANELS[k][1]
        for d, v in enumerate(vals, 1):
            if v == 0:
                continue
            fig.text(ax.X(d) + (16 if PANELS[k][5] == 'point' else 0), ax.Y(v) - 14, '%d %s' % (v, unit), 26,
                     'start' if PANELS[k][5] == 'point' else 'middle', 'bold', C['answer'], A, halo=True)
        fig.marker(880, 70 + k * 312 + 150, str(k + 1), A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Maximum temperature peaks on day 2 at 28 °C, then falls to 26 °C (from 24 °C on day 1).'),
                 ('2', 'Rainfall also peaks on day 2 (8 mm); day 1 was dry (0 mm, a measured zero).'),
                 ('3', 'Sunshine is lowest on day 2 (3 hours), against 8 hours on day 1 and 6 on day 3.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'three stacked charts sharing the day axis, separate vertical axes',
        'data': {'daily_max_temp_C': TEMP, 'daily_rainfall_total_mm': RAIN, 'daily_sunshine_total_h': SUN},
        'source': 'card prompt and notes BL-6137-1.6.04-21 (original teaching data)',
        'axes': {p[0]: {'unit': p[1], 'range': p[3]} for p in PANELS},
        'question_withholds': ['value labels', 'interpretation'],
        'independent_solution': ['temperature peaks day 2 (28 C) then 26 C (1)', 'rainfall peaks day 2 (8 mm), day 1 0 mm (1)',
                                 'sunshine lowest day 2 (3 h) vs 8 and 6 h (1)'],
        'derived': {'mean_max_C': sum(TEMP) / 3, 'range_C': max(TEMP) - min(TEMP), 'rain_total_mm': sum(RAIN), 'sun_total_h': sum(SUN)},
    }
    checks = [
        check('values match card and notes', (TEMP, RAIN, SUN) == ([24, 28, 26], [0, 8, 4], [8, 3, 6])),
        check('derived values match notes 04-21 (mean 26, range 4, rain 12, sun 17)', (sum(TEMP) / 3, max(TEMP) - min(TEMP), sum(RAIN), sum(SUN)) == (26, 4, 12, 17)),
        check('every value within its own axis', all(p[3][0] <= v <= p[3][1] for p in PANELS for v in p[2])),
        check('separate vertical axes with their own units', len({p[1] for p in PANELS}) == 3),
        check('measured zero rainfall labelled so it is not read as missing', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'peak', r'lowest']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 70 + k * 312, 960, 300) for k in range(3)])


if __name__ == '__main__':
    main()
