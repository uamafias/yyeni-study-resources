"""VIS-6137-4.1-01 -> ITEM-6137-4.1-021-PROC (assigned); variants bound to ITEM-6137-4.1-P04 and ITEM-6137-4.1-P05.

Base (notes BL-6137-4.1.04-02, -05 and -09): three panels of one eligible area.
A: twenty numbered eligible sites; five drawn by chance (3, 8, 11, 16, 19).
B: a 100 m transect sampled from a stated start (0 m) at a fixed 10 m interval (11 points).
C: two defined zones (8 and 12 numbered sites); three drawn by chance within each zone.
The question names no method; the answer adds random, systematic and stratified with the procedure.
P04 variant: beach station/record sheet (stations A 0 m, B 50 m, C 100 m on a safe upper-beach route;
pebble lengths 10/12/14, 20/22/24, 30/32/34 mm; falls 40, 50, 25 cm over a 10 m run) with the mean
column blank. Answer: means 12, 22, 32 mm.
P05 variant: respondent form and tally (residents yes 12 / no 8; visitors yes 16 / no 4, respondents 20)
with the resident denominator and both percentages blank. Answer: residents 20, 60%; visitors 80%.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, table, build, check  # noqa: E402

RID = 'VIS-6137-4.1-01'
ITEM = 'ITEM-6137-4.1-021-PROC'
P04, P05 = 'ITEM-6137-4.1-P04', 'ITEM-6137-4.1-P05'
W, HQ, HA = 1000, 700, 1140
V4Y, V4H = 1210, 690
V5Y, V5H = 1970, 680
PY, PW, PH = 70, 300, 450
PX = {'A': 20, 'B': 350, 'C': 680}
RANDOM_DRAW = [3, 8, 11, 16, 19]
INTERVAL, START, LENGTH = 10, 0, 100
ZONES = {'Zone 1': 8, 'Zone 2': 12}
ZONE_DRAW = {'Zone 1': [2, 5, 7], 'Zone 2': [3, 9, 12]}
STATIONS = [('A', 0, (10, 12, 14), 40), ('B', 50, (20, 22, 24), 50), ('C', 100, (30, 32, 34), 25)]
SURVEY = {'Residents': (12, 8), 'Visitors': (16, 4)}


def site(fig, x, y, n, chosen):
    fig.circle(x, y, 22, INK if chosen else '#ffffff', INK, 2.5)
    if n != '':
        fig.text(x, y + 9, str(n), 26, 'middle', 'bold', '#ffffff' if chosen else INK)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Three ways of choosing sample sites in one area')
    fig.extra_h = V5Y + V5H
    for k, x0 in PX.items():
        fig.rect(x0, PY, PW, PH, '#eef4e4', GREY, 2, 6)
        fig.rect(x0, PY, PW, 50, '#ffffff', GREY, 2, 6)
        fig.text(x0 + 16, PY + 37, k, 32, 'start', 'bold')
    # A: numbered frame, chance draw
    x0 = PX['A']
    for n in range(1, 21):
        r, c = divmod(n - 1, 4)
        site(fig, x0 + 45 + c * 70, PY + 95 + r * 80, n, n in RANDOM_DRAW)
    # B: transect, start and fixed interval
    x0 = PX['B']
    tx, ybot, ytop = x0 + 170, PY + PH - 30, PY + 80
    pxm = (ybot - ytop) / LENGTH
    fig.line(tx, ybot, tx, ytop, '#8c8c8c', 8)
    pts = list(range(START, LENGTH + 1, INTERVAL))
    for d in pts:
        fig.circle(tx, ybot - d * pxm, 11, INK, '#ffffff', 2)
    for d in (0, 50, 100):
        fig.text(tx - 26, ybot - d * pxm + 9, '%d m' % d, 26, 'end', 'bold')
    # C: two zones, draw within each
    x0 = PX['C']
    zb = PY + 230
    fig.rect(x0, PY + 50, PW, zb - PY - 50, '#d9ead3', 'none', 0)
    fig.rect(x0, zb, PW, PY + PH - zb, '#f6e7c1', 'none', 0)
    fig.line(x0, zb, x0 + PW, zb, INK, 3, dash='10 6')
    fig.rect(x0, PY, PW, PH, 'none', GREY, 2, 6)
    fig.text(x0 + 12, PY + 80, 'Zone 1', 26, 'start', 'bold', INK, halo=True)
    fig.text(x0 + 12, zb + 32, 'Zone 2', 26, 'start', 'bold', INK, halo=True)
    zpos = {'Zone 1': [(x0 + 45 + c * 70, PY + 120 + r * 72) for r in range(2) for c in range(4)],
            'Zone 2': [(x0 + 45 + c * 70, zb + 64 + r * 62) for r in range(3) for c in range(4)]}
    for z, n in ZONES.items():
        for i, (x, y) in enumerate(zpos[z][:n], 1):
            site(fig, x, y, i, i in ZONE_DRAW[z])
    caps = {'A': ['Chance draw from', 'numbers 1–20:', '3, 8, 11, 16, 19'],
            'B': ['Start at 0 m, then', 'every 10 m along', 'the line'],
            'C': ['Chance draw per zone:', 'Zone 1: 2, 5, 7', 'Zone 2: 3, 9, 12']}
    for k, rows in caps.items():
        fig.lines(PX[k] + PW / 2, PY + PH + 38, rows, 26, 32, anchor='middle')
    site(fig, 60, 668, '', True)
    fig.text(94, 677, 'chosen site', 26)
    site(fig, 300, 668, '', False)
    fig.text(334, 677, 'eligible site, not chosen', 26)
    fig.circle(700, 668, 11, INK, '#ffffff', 2)
    fig.text(724, 677, 'point on the line', 26)

    A = 'a'
    for i, (k, lab) in enumerate((('A', 'random'), ('B', 'systematic'), ('C', 'stratified'))):
        fig.text(PX[k] + 56, PY + 36, lab, 28, 'start', 'bold', C['answer'], A)
        fig.marker(PX[k] + PW - 28, PY + 25, str(i + 1), A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Selection procedures (first define the eligible frame)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Random (A): number every eligible site, then choose by chance, e.g. a random-number table, without replacement. Here sites 3, 8, 11, 16 and 19 were drawn.'),
                 ('2', 'Systematic (B): state the start and the fixed interval, here 0 m and every 10 m, then sample each point the rule gives: 11 points along the line.'),
                 ('3', 'Stratified (C): define the two zones first, then apply a rule within each zone (here a chance draw of three) so both zones are covered. Record the sites chosen, any safe replacements and the limits.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P04 variant: station / record sheet
    V, VQ, VA = 'v-p04', 'v-p04-q', 'v-p04-a'
    y = V4Y
    fig.rect(0, y, W, V4H, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, y + 40, 'Beach survey: stations and record sheet', 28, 'middle', 'bold', layer=V)
    fig.rect(40, y + 70, 920, 120, '#f6e7c1', GREY, 1.5, layer=V)
    fig.rect(40, y + 190, 920, 60, '#9cc3e0', GREY, 1.5, layer=V)
    fig.text(500, y + 229, 'Sea: no entry into the water', 26, 'middle', 'bold', INK, V, halo=True)
    px_m = 8
    fig.line(100, y + 130, 100 + 100 * px_m, y + 130, INK, 3, V, dash='12 8')
    fig.text(500, y + 172, 'safe route along the upper beach', 26, 'middle', 'normal', INK, V, halo=True)
    for s, d, _, _ in STATIONS:
        sx = 100 + d * px_m
        fig.poly([(sx, y + 130), (sx - 14, y + 104), (sx + 14, y + 104)], '#c0392b', INK, 2, layer=V)
        fig.text(sx, y + 96, '%s  %d m' % (s, d), 26, 'middle', 'bold', INK, V, halo=True)
    rows = [['Station', 'Distance (m)', 'Pebble 1', 'Pebble 2', 'Pebble 3', 'Mean', 'Fall (cm)']]
    cl = {}
    for i, (s, d, p, fall) in enumerate(STATIONS, 1):
        rows.append([s, str(d)] + [str(v) for v in p] + [str(round(sum(p) / 3)), str(fall)])
        cl[(i, 5)] = VA
    ty = table(fig, 55, y + 290, [100, 180, 125, 125, 125, 105, 130], 54, rows, layer=V, cell_layers=cl, align=['middle'] * 7)
    fig.lines(55, ty + 40, ['Pebble = longest dimension, in mm; mean in mm.',
                            'Fall = drop in cm over a 10 m horizontal run at each station.'], 26, 34, layer=V)
    fig.text(500, ty + 140, 'A and C completed (j); B is the calculation in (d).', 26, 'middle', 'bold', C['answer'], VA)

    # ---- P05 variant: respondent form and tally
    V5, V5Q, V5A = 'v-p05', 'v-p05-q', 'v-p05-a'
    y = V5Y
    fig.rect(0, y, W, V5H, '#ffffff', 'none', 0, layer=V5)
    fig.text(W / 2, y + 40, 'Tourism survey: respondent form and tally', 28, 'middle', 'bold', layer=V5)
    fig.rect(40, y + 66, 920, 250, '#fbfaf4', INK, 1.5, 6, V5)
    fig.text(60, y + 104, 'Respondent form (one per person; no names recorded)', 26, 'start', 'bold', layer=V5)

    def box(x, yb, lab):
        fig.rect(x, yb - 22, 24, 24, '#ffffff', INK, 2, layer=V5)
        fig.text(x + 34, yb, lab, 26, layer=V5)
    fig.text(60, y + 152, 'Group:', 26, layer=V5)
    box(160, y + 152, 'resident')
    box(330, y + 152, 'visitor')
    fig.text(500, y + 152, '(screening: “Do you live here?”)', 26, 'start', 'normal', GREY, V5)
    fig.text(60, y + 200, 'Agrees to take part voluntarily:', 26, layer=V5)
    box(450, y + 200, 'yes')
    fig.text(560, y + 200, '(if not, record as non-response)', 26, 'start', 'normal', GREY, V5)
    fig.text(60, y + 248, 'Read exactly as written: “Has tourism here brought you', 26, layer=V5)
    fig.text(60, y + 284, 'the benefit named on this card?”', 26, layer=V5)
    box(500, y + 284, 'yes')
    box(620, y + 284, 'no')
    rows5 = [['Group', 'Yes', 'No', 'Respondents', 'Yes (%)']]
    cl5 = {}
    for i, (g, (yes, no)) in enumerate(SURVEY.items(), 1):
        rows5.append([g, str(yes), str(no), str(yes + no), '%d%%' % round(100 * yes / (yes + no))])
        cl5[(i, 4)] = V5A
    cl5[(1, 3)] = V5A
    ty = table(fig, 60, y + 370, [200, 140, 140, 220, 180], 54, rows5, layer=V5, cell_layers=cl5, align=['middle'] * 5)
    fig.text(60, ty + 44, 'Refusals and non-response: record separately, not as “no”.', 26, layer=V5)
    fig.text(500, ty + 100, 'Residents: 12/20 × 100 = 60%; visitors: 16/20 × 100 = 80%.', 26, 'middle', 'bold', C['answer'], V5A)

    means = [sum(p) / 3 for _, _, p, _ in STATIONS]
    grads = ['1:%g' % (1000 / fall) for *_, fall in STATIONS]
    pct = {g: 100 * yes / (yes + no) for g, (yes, no) in SURVEY.items()}
    zone_ok = all(len(set(ZONE_DRAW[z])) == 3 and all(1 <= v <= ZONES[z] for v in ZONE_DRAW[z]) for z in ZONES)
    spec = {
        'kind': 'three-panel sampling diagram with P04 record-sheet and P05 respondent-form variants',
        'notes_match': ['BL-6137-4.1.04-02', 'BL-6137-4.1.04-05', 'BL-6137-4.1.04-09'],
        'panel_A_random': {'frame': list(range(1, 21)), 'drawn': RANDOM_DRAW, 'without_replacement': True},
        'panel_B_systematic': {'start_m': START, 'interval_m': INTERVAL, 'length_m': LENGTH, 'points_m': pts},
        'panel_C_stratified': {'zones': ZONES, 'drawn_within_zone': ZONE_DRAW},
        'question_withholds': ['random', 'systematic', 'stratified', 'procedure wording'],
        'independent_solution_021': ['frame defined; chance selection (A) (1)', 'stated start and interval (B) (1)',
                                     'zones defined then within-zone rule; record chosen sites and limits (C) (1)'],
        'p04': {'bound_item': P04, 'stations': STATIONS, 'means_mm': means, 'gradients': grads,
                'answer': {'A_mean_mm': 12, 'C_mean_mm': 32, 'B_mean_mm_part_d': 22}},
        'p05': {'bound_item': P05, 'responses': SURVEY, 'percent_yes': pct,
                'answer': {'resident_percent': 60, 'resident_denominator': 20, 'visitor_percent_part_d': 80}},
    }
    checks = [
        check('A: five distinct numbers drawn from 1-20', len(set(RANDOM_DRAW)) == 5 and all(1 <= v <= 20 for v in RANDOM_DRAW)),
        check('B: start 0 m, 10 m interval, 11 points to 100 m', pts == list(range(0, 101, 10)) and len(pts) == 11),
        check('C: three distinct sites drawn inside each zone', zone_ok),
        check('P04 means 12, 22, 32 mm; gradients 1:25, 1:20, 1:40', means == [12, 22, 32] and grads == ['1:25', '1:20', '1:40']),
        check('P05 residents 60% of 20; visitors 80% of 20', pct == {'Residents': 60, 'Visitors': 80} and all(a + b == 20 for a, b in SURVEY.values())),
    ]
    c4, c5 = (0, V4Y, W, V4H), (0, V5Y, W, V5H)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'random\b', r'systematic', r'stratif']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p04_question': {'path': 'assets/images/%s-%s-question.png' % (P04, RID), 'layers': [V, VQ], 'clip': c4, 'hide_base': True,
                         'bound_item': P04, 'forbidden': [r'completed']},
        'p04_answer': {'path': 'assets/images/%s-%s-answer.png' % (P04, RID), 'layers': [V, VA], 'clip': c4, 'hide_base': True, 'bound_item': P04},
        'p05_question': {'path': 'assets/images/%s-%s-question.png' % (P05, RID), 'layers': [V5, V5Q], 'clip': c5, 'hide_base': True,
                         'bound_item': P05, 'forbidden': [r'60%', r'80%']},
        'p05_answer': {'path': 'assets/images/%s-%s-answer.png' % (P05, RID), 'layers': [V5, V5A], 'clip': c5, 'hide_base': True, 'bound_item': P05},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
