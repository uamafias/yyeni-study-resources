"""VIS-6137-1.5-05 -> ITEM-6137-1.5-046-PROC (assigned); variants bound to ITEM-6137-1.5-P04; reused by P07.

Base figure (question/answer): (a) plan of a transect from a fixed reference post across the beach,
perpendicular to the shoreline, with stations at breaks of slope; (b) side view along the transect
with ranging poles, clinometer sighting between equal marks and a tape; (c) a record-sheet template.
P04 variant region (below the base figure, clipped): blank profile axes (distance 0-30 m, height
0-3 m) and blank field-record headings; the answer variant plots beach A's supplied points
(0,0), (10,0.5), (20,1.5), (30,3) and fills the headings.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.5-05'
ITEM = 'ITEM-6137-1.5-046-PROC'
P04 = 'ITEM-6137-1.5-P04'
W, HQ, HA = 1000, 905, 1275
VY = 1300                  # top of the P04 variant region in the master
VH = 640
A_PROFILE = [(0, 0), (10, 0.5), (20, 1.5), (30, 3)]
STATIONS = [(120, 440), (330, 480), (560, 530), (800, 560)]   # side view: ground points at breaks of slope (x, y)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Measuring a beach profile: equipment and transect')
    fig.extra_h = VY + VH
    # ---- (a) plan
    fig.rect(20, 56, 960, 190, '#ffffff', GREY, 2, 8)
    fig.text(36, 90, '(a) Plan', 26, 'start', 'bold')
    fig.rect(150, 100, 140, 136, C['land'], 'none', 0)
    fig.rect(290, 100, 470, 136, C['sand'], 'none', 0)
    fig.rect(760, 100, 210, 136, C['sea'], 'none', 0)
    fig.line(760, 100, 760, 236, C['blue'], 3)
    fig.text(865, 130, 'sea', 26, 'middle', 'bold', C['blue'])
    fig.text(770, 225, 'shoreline', 26, 'start', 'normal', C['blue'], halo=True)
    fig.rect(214, 158, 16, 16, INK, INK, 1)
    fig.text(222, 148, 'R', 26, 'middle', 'bold', INK, halo=True)
    fig.line(222, 166, 760, 166, C['red'], 3, dash='12 7')
    for i, x in enumerate((222, 380, 560, 740)):
        fig.circle(x, 166, 7, '#ffffff', INK, 2)
        fig.text(x, 205, str(i + 1), 26, 'middle', 'bold', INK, halo=True)
    fig.text(36, 130, 'R = fixed', 26, 'start')
    fig.text(36, 162, 'reference', 26, 'start')
    fig.text(36, 194, 'post', 26, 'start')
    # ---- (b) side view
    fig.rect(20, 260, 960, 380, '#ffffff', GREY, 2, 8)
    fig.text(36, 294, '(b) Side view along the transect (not to scale)', 26, 'start', 'bold')
    ground = [(30, 440)] + STATIONS + [(978, 605)]
    fig.poly(ground + [(978, 632), (30, 632)], C['sand'], INK, 2.5)
    fig.poly([(900, 585), (978, 585), (978, 605)], C['sea'], C['blue'], 1.5)
    fig.text(970, 578, 'sea', 26, 'end', 'bold', C['blue'], halo=True)
    POLE = 110                                     # pole height (px); sighting marks at the same height on each pole
    MARK = 70
    for i, (x, y) in enumerate(STATIONS):
        fig.rect(x - 4, y - POLE, 8, POLE, '#ffffff', INK, 1.5)
        for k in range(0, POLE, 22):
            fig.rect(x - 4, y - POLE + k, 8, 11, C['red'], 'none', 0)
        fig.line(x - 12, y - MARK, x + 12, y - MARK, INK, 3)
        fig.text(x, y + 40, str(i + 1), 26, 'middle', 'bold', INK, halo=True)
    for (x1, y1), (x2, y2) in zip(STATIONS, STATIONS[1:]):
        fig.line(x1, y1 - MARK, x2, y2 - MARK, C['blue'], 2.5, dash='8 6')
        fig.line(x1, y1 + 8, x2, y2 + 8, '#5a3f1c', 3)
    # clinometer drawn at station 1's mark
    cx, cy = STATIONS[0][0] + 30, STATIONS[0][1] - MARK
    fig.path('M%d %d A 26 26 0 0 1 %d %d Z' % (cx - 26, cy, cx + 26, cy), '#ffd23f', INK, 2)
    fig.text(cx + 40, cy - 6, 'clinometer', 26, 'start', 'bold', INK, halo=True)
    fig.text(STATIONS[1][0] + 18, STATIONS[1][1] - POLE - 10, 'ranging poles', 26, 'start', 'bold', INK, halo=True)
    fig.text((STATIONS[1][0] + STATIONS[2][0]) / 2 + 10, (STATIONS[1][1] + STATIONS[2][1]) / 2 + 52, 'tape', 26, 'middle', 'bold', '#5a3f1c', halo=True)
    fig.text(380, 612, 'poles at stations 1\u20134 (breaks of slope)', 26, 'middle', 'normal', INK, halo=True)
    # ---- (c) record sheet template
    fig.rect(20, 654, 960, 236, '#ffffff', GREY, 2, 8)
    fig.text(36, 688, '(c) Record sheet', 26, 'start', 'bold')
    cols = [(36, 'Segment'), (196, 'Distance (m)'), (406, 'Angle (°)'), (586, 'Up (+) or down (−)'), (856, 'Notes')]
    fig.rect(36, 704, 928, 44, '#eef3f7', INK, 1.5)
    for x, lab in cols:
        fig.text(x + 10, 735, lab, 26, 'start', 'bold')
        if x > 36:
            fig.line(x, 704, x, 880, INK, 1.2)
    for r in range(3):
        y = 748 + r * 44
        fig.rect(36, y, 928, 44, '#ffffff', INK, 1.2)
        fig.text(56, y + 31, '%d–%d' % (r + 1, r + 2), 26)
    for x, lab in cols[1:]:
        fig.line(x, 704, x, 880, INK, 1.2)

    A = 'a'
    fig.marker(260, 166, '1', A)
    fig.marker(470, 400, '2', A)
    fig.marker(900, 690, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Start at the fixed reference post R and lay the transect perpendicular to the shoreline, on an approved safe beach, away from breaking waves.'),
                 ('2', 'Place poles at each break of slope; measure each segment with the tape and sight the clinometer between the same marks on both poles.'),
                 ('3', 'Record each segment’s distance (m), angle (°) and whether it rises or falls, so the profile can be plotted on stated scales.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P04 variant region (clipped): blank axes and headings; answer plot
    V, VQ, VA = 'v-p04', 'v-p04-q', 'v-p04-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Beach A profile and field-record headings', 28, 'middle', 'bold', layer=V)
    ax = Axes(fig, 150, VY + 80, 780, 330, (0, 30), (0, 3), layer=V)
    ax.draw(range(0, 31, 5), [0, 0.5, 1, 1.5, 2, 2.5, 3], 'Distance along transect from start (m)', 'Height above start (m)',
            fmt_y=lambda v: ('%g' % v), minor_x=range(1, 30), minor_y=[k / 10 for k in range(1, 30)], ylabel_x=60)
    ty = VY + 530
    fig.text(36, ty - 16, 'Field record for each profile segment', 26, 'start', 'bold', layer=V)
    fig.rect(36, ty, 928, 50, '#eef3f7', INK, 1.5, layer=V)
    fig.line(236, ty, 236, ty + 50, INK, 1.2, layer=V)
    fig.line(600, ty, 600, ty + 50, INK, 1.2, layer=V)
    fig.text(50, ty + 34, 'Segment', 26, 'start', 'bold', layer=V)
    fig.text(250, ty + 34, '______________ ( ____ )', 26, 'start', 'normal', GREY, layer=VQ)
    fig.text(614, ty + 34, '______________ ( ____ )', 26, 'start', 'normal', GREY, layer=VQ)
    fig.text(250, ty + 34, 'Segment distance (m)', 26, 'start', 'bold', C['answer'], layer=VA)
    fig.text(614, ty + 34, 'Slope angle (°)', 26, 'start', 'bold', C['answer'], layer=VA)
    ax.layer = VA
    ax.polyline(A_PROFILE, C['answer'], 4)
    for x, y in A_PROFILE:
        fig.circle(ax.X(x), ax.Y(y), 7, C['answer'], '#ffffff', 2, VA)
        if x == 0:
            fig.text(ax.X(x) + 14, ax.Y(y) - 40, '(0, 0)', 26, 'start', 'bold', C['answer'], VA, halo=True)
        else:                                             # above-left of the point, clear of the rising line
            fig.text(ax.X(x) - 14, ax.Y(y) - 16, '(%g, %g)' % (x, y), 26, 'end', 'bold', C['answer'], VA, halo=True)

    spec = {
        'kind': 'equipment and transect resource (plan, side view, record sheet) with a P04 plotting variant',
        'base_figure': {'plan': 'fixed post R, transect perpendicular to the shoreline, stations 1-4',
                        'side_view': 'ranging poles at breaks of slope, clinometer sighting between equal marks, tape along the ground',
                        'record_sheet_columns': [c[1] for c in cols]},
        'p04_variant': {'bound_item': P04, 'axes': {'x': [0, 30, 'm'], 'y': [0, 3, 'm']}, 'grid': '1 m by 0.1 m minor; 5 m by 0.5 m major',
                        'answer_points': A_PROFILE, 'headings_answer': ['Segment distance (m)', 'Slope angle (degrees)']},
        'reuse': {'ITEM-6137-1.5-P07': 'base question (survey layout) and base answer (procedure)'},
        'question_withholds': ['procedure steps', 'the words perpendicular/consistent/record each'],
        'independent_solution': ['fixed reference post + shore-normal transect (1)', 'segment distance with tape + clinometer between equal pole marks (1)',
                                 'record distance, signed angle per segment for plotting (1)'],
    }
    rise = [(b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(A_PROFILE, A_PROFILE[1:])]
    checks = [
        check('A overall gradient 3 m in 30 m = 1:10 (P04 part d)', A_PROFILE[-1][1] / A_PROFILE[-1][0] == 0.1),
        check('A plotted points lie within the supplied axes', all(0 <= x <= 30 and 0 <= y <= 3 for x, y in A_PROFILE)),
        check('A profile rises in every segment', all(r > 0 for r in rise), str(rise)),
        check('sighting marks at equal height on every pole', True, 'MARK = %d px on all poles' % MARK),
        check('transect perpendicular to the shoreline in plan', True, 'transect horizontal, shoreline vertical'),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'perpendicular', r'procedure', r'consistent']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p04_question': {'path': 'assets/images/%s-%s-question.png' % (P04, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True, 'bound_item': P04,
                         'forbidden': [r'Segment distance', r'Slope angle', r'\(0, 0\)', r'\(30, 3\)']},
        'p04_answer': {'path': 'assets/images/%s-%s-answer.png' % (P04, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P04},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 190), (20, 260, 960, 380), (20, 654, 960, 236)])


if __name__ == '__main__':
    main()
