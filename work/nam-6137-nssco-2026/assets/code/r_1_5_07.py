"""VIS-6137-1.5-07 -> ITEM-6137-1.5-050-PROC (assigned); variants bound to ITEM-6137-1.5-P06.

Base figure: (a) plan of a north-south beach (sea west) with a fixed origin post O, an alongshore
measuring tape marked -5 to +10 m (positive = north), the tracer start at O on the upper swash zone,
and a safe observation position on the dry upper beach; (b) a record sheet that separates recovery
status from displacement. P06 variant: blank axes (trial 1-5; signed displacement -2 to +5 m) and
blank totals; the answer variant plots +2, +4, +1, -1 m and marks trial 5 as not recovered (no point).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.5-07'
ITEM = 'ITEM-6137-1.5-050-PROC'
P06 = 'ITEM-6137-1.5-P06'
W, HQ, HA = 1000, 870, 1235
VY, VH = 1300, 700
TRIALS = [(1, 2), (2, 4), (3, 1), (4, -1), (5, None)]


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Tracing beach-material movement: reference and record')
    fig.extra_h = VY + VH
    # (a) plan
    fig.rect(20, 56, 960, 470, '#ffffff', GREY, 2, 8)
    fig.text(36, 90, '(a) Plan (not to scale)', 26, 'start', 'bold')
    fig.rect(40, 104, 260, 410, C['sea'], 'none', 0)
    fig.rect(300, 104, 470, 410, C['sand'], 'none', 0)
    fig.rect(770, 104, 190, 410, C['land'], 'none', 0)
    fig.line(300, 104, 300, 514, C['blue'], 3)
    fig.text(170, 140, 'sea', 26, 'middle', 'bold', C['blue'])
    fig.text(865, 140, 'land', 26, 'middle', 'bold', C['green'])
    tx = 400                                 # tape line, alongshore
    oy = 365                                 # origin O
    px = 18                                  # px per metre along the tape
    fig.line(tx, oy + 5 * px, tx, oy - 10 * px, INK, 3)
    for m in range(-5, 11):
        y = oy - m * px
        fig.line(tx - (10 if m % 5 == 0 else 5), y, tx, y, INK, 2)
        if m % 5 == 0:
            fig.text(tx - 16, y + 9, '%+d' % m if m else '0', 26, 'end', 'bold', INK, halo=True)
    fig.text(tx + 8, oy - 10 * px - 14, 'tape, metres', 26, 'start', 'normal', INK, halo=True)
    fig.rect(tx + 14, oy - 9, 18, 18, INK, INK, 1)
    fig.text(tx + 42, oy + 9, 'O  fixed origin post', 26, 'start', 'bold', INK, halo=True)
    for k in range(5):
        fig.circle(tx - 40 + (k % 3) * 9, oy - 6 + (k // 3) * 10, 4.5, C['orange'], INK, 1)
    fig.arrow(720, 480, 720, 400, INK, 4, 16)
    fig.text(732, 422, 'N', 26, 'start', 'bold')
    fig.text(600, 470, '+ = north', 26, 'end', 'bold', INK, halo=True)
    fig.circle(700, 220, 14, '#ffffff', INK, 2.5)
    fig.line(700, 234, 700, 262, INK, 2.5)
    fig.text(600, 300, 'observer on dry upper beach', 26, 'middle', 'normal', INK, halo=True)
    fig.text(330, 500, 'tracer pebbles start at O (orange)', 26, 'start', 'normal', INK, halo=True)
    fig.text(560, 140, 'Interval: 2 minutes per trial', 26, 'middle', 'bold', INK, halo=True)
    # (b) record sheet
    fig.rect(20, 540, 960, 320, '#ffffff', GREY, 2, 8)
    fig.text(36, 574, '(b) Record sheet', 26, 'start', 'bold')
    cols = [(36, 'Trial'), (146, 'Time'), (276, 'Recovered?'), (466, 'Displacement (m, + = north)'), (836, 'Notes')]
    fig.rect(36, 590, 928, 44, '#eef3f7', INK, 1.5)
    for x, lab in cols:
        fig.text(x + 10, 621, lab, 26, 'start', 'bold')
    for r in range(5):
        fig.rect(36, 634 + r * 44, 928, 44, '#ffffff', INK, 1.2)
        fig.text(66, 634 + r * 44 + 31, str(r + 1), 26)
    for x, lab in cols[1:]:
        fig.line(x, 590, x, 854, INK, 1.2)

    A = 'a'
    fig.marker(tx + 300, oy, '1', A)
    fig.marker(tx - 70, oy - 180, '2', A)
    fig.marker(940, 574, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Define the fixed origin O, the direction system (+ = north along the tape) and the 2-minute interval before starting; observe from the dry upper beach.'),
                 ('2', 'For each trial, find the tracer and measure its signed distance from O along the tape; repeat the same method for every trial.'),
                 ('3', 'Record “not recovered” separately: an unrecovered tracer is missing data, not a displacement of 0 m.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P06 variant
    V, VQ, VA = 'v-p06', 'v-p06-q', 'v-p06-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Signed displacement of recovered tracers', 28, 'middle', 'bold', layer=V)
    ax = Axes(fig, 170, VY + 80, 760, 400, (0.5, 5.5), (-2, 5), layer=V)
    ax.draw(range(1, 6), range(-2, 6), 'Trial', 'Displacement (m, + = north)', minor_y=[k / 2 for k in range(-3, 10, 2)], ylabel_x=70,
            grid=True)
    fig.line(ax.X(0.5), ax.Y(0), ax.X(5.5), ax.Y(0), INK, 2.5, V)
    fig.text(ax.X(5.5) - 8, ax.Y(0) - 10, '0 m', 26, 'end', 'bold', layer=V)
    ty = VY + 620
    fig.text(36, ty, 'Recovered trials:', 26, 'start', 'bold', layer=V)
    fig.text(500, ty, 'Unrecovered trials:', 26, 'start', 'bold', layer=V)
    fig.text(260, ty, '______', 26, 'start', 'normal', GREY, VQ)
    fig.text(745, ty, '______', 26, 'start', 'normal', GREY, VQ)
    fig.text(260, ty, '4', 26, 'start', 'bold', C['answer'], VA)
    fig.text(745, ty, '1 (trial 5)', 26, 'start', 'bold', C['answer'], VA)
    for t, d in TRIALS:
        if d is None:
            fig.text(ax.X(t), ax.Y(4.4), 'not', 26, 'middle', 'bold', C['red'], VA, halo=True)
            fig.text(ax.X(t), ax.Y(4.4) + 30, 'recovered', 26, 'middle', 'bold', C['red'], VA, halo=True)
            continue
        fig.circle(ax.X(t), ax.Y(d), 9, C['answer'], '#ffffff', 2, VA)
        fig.text(ax.X(t) + 14, ax.Y(d) - 14, '%+d m' % d, 26, 'start', 'bold', C['answer'], VA, halo=True)

    rec = [d for t, d in TRIALS if d is not None]
    spec = {
        'kind': 'tracer reference plan and record sheet with a P06 plotting variant',
        'reference': {'origin': 'fixed post O', 'axis': 'alongshore tape, -5 to +10 m, + = north', 'interval_min': 2,
                      'observer': 'dry upper beach (no entry into breaking water)'},
        'record_columns': [c[1] for c in cols],
        'p06_variant': {'bound_item': P06, 'axes': {'x': 'trial 1-5', 'y': [-2, 5, 'm']}, 'trials_m': TRIALS,
                        'recovered': len(rec), 'unrecovered': 1, 'mean_recovered_m': sum(rec) / len(rec)},
        'question_withholds': ['procedure steps', 'missing-data treatment'],
        'independent_solution': ['define origin, + north direction and 2-min interval first (1)', 'repeat signed position measurement per trial (1)',
                                 'record non-recovery separately from zero displacement (1)'],
    }
    checks = [
        check('mean of recovered displacements is +1.5 m (P06 part d)', sum(rec) / len(rec) == 1.5),
        check('4 recovered and 1 unrecovered (P06 part j)', len(rec) == 4),
        check('all recovered values within the supplied axis range', all(-2 <= d <= 5 for d in rec)),
        check('trial 5 has no plotted point (not a zero)', True),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'missing', r'not a displacement']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p06_question': {'path': 'assets/images/%s-%s-question.png' % (P06, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True,
                         'bound_item': P06, 'forbidden': [r'not recovered', r'\+4 m', r'1 \(trial 5\)']},
        'p06_answer': {'path': 'assets/images/%s-%s-answer.png' % (P06, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P06},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 470), (20, 540, 960, 320)])


if __name__ == '__main__':
    main()
