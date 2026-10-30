"""VIS-6137-3.1-01 -> ITEM-6137-3.1-033-INTERP (assigned: pyramid A); reused by ITEM-6137-3.1-035-INTERP (paired A and B).

Five-year age-sex pyramids with equal 5-year bands 0-4 ... 75-79 and a separately labelled open-ended
80+ band (handover requirement). Counts from notes BL-6137-3.1.07-05 (A) and 3.1.08-05 (B):
A: 50/50 in each of 0-4, 5-9, 10-14; 28/32 in each band 15-19 to 60-64; 10/15 in each of 65-69 to 80+.
B: 33/33, 33/33, 34/34 young; 28/32 working; 20/30 older. Totals A 300/600/100, B 200/600/200.
Both panels use the same horizontal scale (PX_PER_PERSON) and bar height, so bars are proportional.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, table, build, check  # noqa: E402

RID = 'VIS-6137-3.1-01'
ITEM = 'ITEM-6137-3.1-033-INTERP'
R035 = 'ITEM-6137-3.1-035-INTERP'
BANDS = ['0–4', '5–9', '10–14', '15–19', '20–24', '25–29', '30–34', '35–39', '40–44', '45–49',
         '50–54', '55–59', '60–64', '65–69', '70–74', '75–79', '80+']
A_COUNTS = [(50, 50)] * 3 + [(28, 32)] * 10 + [(10, 15)] * 4
B_COUNTS = [(33, 33), (33, 33), (34, 34)] + [(28, 32)] * 10 + [(20, 30)] * 4
MALE, FEMALE = '#3d6fa8', '#c0617a'
W, HQ, HA = 1000, 860, 1160
VY, VH = 1220, 960
PX_PER_PERSON = 5.1
BAR_H = 34


def group(counts):
    tot = [m + f for m, f in counts]
    return sum(tot[:3]), sum(tot[3:13]), sum(tot[13:])


GAP = 48     # half-width of the central band-label column


def pyramid(fig, cx, top, counts, layer, label_bands=True, title=None, px=PX_PER_PERSON, bh=BAR_H):
    if title:
        fig.text(cx, top - 18, title, 28, 'middle', 'bold', layer=layer)
    n = len(BANDS)
    for i, (band, (m, f)) in enumerate(zip(BANDS, counts)):
        y = top + (n - 1 - i) * bh
        fig.rect(cx - GAP - m * px, y + 2, m * px, bh - 4, MALE, INK, 1, layer=layer)
        fig.rect(cx + GAP, y + 2, f * px, bh - 4, FEMALE, INK, 1, layer=layer)
        if label_bands:
            fig.text(cx, y + bh / 2 + 9, band, 26 if bh >= 30 else 26, 'middle', 'normal', INK, layer)
    base = top + n * bh
    for side in (-1, 1):
        for v in range(0, 61, 20):
            x = cx + side * (GAP + v * px)
            fig.line(x, base, x, base + 8, INK, 2, layer)
            fig.text(x, base + 36, str(v), 26, 'middle', layer=layer)
    fig.line(cx - GAP - 60 * px, base, cx + GAP + 60 * px, base, INK, 2, layer)
    return base


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Population A by age and sex (five-year bands; 80+ open-ended)')
    fig.extra_h = VY + VH
    cx, top = 500, 110
    base = pyramid(fig, cx, top, A_COUNTS, 'base')
    fig.text(cx - GAP - 30 * PX_PER_PERSON, top - 22, 'Males', 26, 'middle', 'bold', MALE)
    fig.text(cx + GAP + 30 * PX_PER_PERSON, top - 22, 'Females', 26, 'middle', 'bold', FEMALE)
    fig.text(cx, base + 76, 'Number of people in each band', 26, 'middle', 'bold')
    fig.text(cx, base + 112, 'Ages in years; 80+ includes everyone aged 80 and over.', 26, 'middle', 'normal', GREY)

    A = 'a'
    y_young = top + 14 * BAR_H
    y_work = top + 4 * BAR_H
    for (y0, y1, lab) in ((top + 14 * BAR_H, top + 17 * BAR_H, 'young (0–14): 300'), (top + 4 * BAR_H, top + 14 * BAR_H, 'working age (15–64): 600'),
                          (top, top + 4 * BAR_H, 'older (65+): 100')):
        fig.line(cx + GAP + 52 * PX_PER_PERSON, y0 + 4, cx + GAP + 52 * PX_PER_PERSON, y1 - 4, C['answer'], 3, A)
        fig.text(cx + GAP + 54 * PX_PER_PERSON, (y0 + y1) / 2 + 9, lab.split(': ')[1], 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(70, top + 9 * BAR_H, '1', A)
    fig.marker(70, top + 2 * BAR_H, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'Working ages (15–64) are the largest group at 600; young ages (0–14) total 300 and older ages (65+) 100.'),
                 ('2', 'Females outnumber males in the working (32 v 28 per band) and older (15 v 10) groups; young counts are equal (50 v 50).'),
                 ('3', 'The shape alone cannot separate the effects of births, survival and migration.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- card 035 variant: paired panels on the same scale, aggregate table
    V, VA = 'v-035', 'v-035-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Populations A and B (same scale; five-year bands; 80+ open-ended)', 28, 'middle', 'bold', layer=V)
    px2, bh2 = 2.9, 30
    for cx2, counts, t in ((250, A_COUNTS, 'A'), (750, B_COUNTS, 'B')):
        b2 = pyramid(fig, cx2, VY + 120, counts, V, label_bands=True, title=t, px=px2, bh=bh2)
    for cx2 in (250, 750):
        fig.text(cx2 - GAP - 35 * px2, VY + 102, 'Males', 26, 'middle', 'bold', MALE, V)
        fig.text(cx2 + GAP + 35 * px2, VY + 102, 'Females', 26, 'middle', 'bold', FEMALE, V)
    fig.text(W / 2, b2 + 72, 'Number of people in each band (both panels)', 26, 'middle', 'bold', layer=V)
    ty = b2 + 100
    gA, gB = group(A_COUNTS), group(B_COUNTS)
    table(fig, 60, ty, [160, 200, 240, 180, 100], 50,
          [['Panel', 'Young 0–14', 'Working 15–64', 'Older 65+', 'Total'],
           ['A', str(gA[0]), str(gA[1]), str(gA[2]), str(sum(gA))], ['B', str(gB[0]), str(gB[1]), str(gB[2]), str(sum(gB))]],
          layer=V, align=['middle'] * 5)
    fig.text(500, ty + 190, 'dependants 400 in both', 26, 'middle', 'bold', C['answer'], VA, halo=True)

    spec = {
        'kind': 'age-sex pyramid(s), equal five-year bands plus labelled open-ended 80+',
        'bands': BANDS, 'counts_male_female': {'A': A_COUNTS, 'B': B_COUNTS},
        'groups_young_working_older': {'A': gA, 'B': gB}, 'scale_px_per_person': {'main': PX_PER_PERSON, 'paired_variant': px2},
        'same_scale_in_paired_panels': True, 'source': 'notes BL-6137-3.1.07-05 and BL-6137-3.1.08-05 (original teaching data)',
        'reuse': {'bound_item': R035, 'images': 'paired A/B panels and aggregate table'},
        'independent_solution_033': ['working 600 largest; young 300; older 100 (1)', 'females exceed males in working and older; young equal (1)',
                                     'shape alone does not isolate fertility, survival or migration (1)'],
    }
    checks = [
        check('17 bands: sixteen equal five-year bands then 80+', len(BANDS) == 17 and BANDS[-1] == '80+'),
        check('A groups 300/600/100', gA == (300, 600, 100)),
        check('B groups 200/600/200', gB == (200, 600, 200)),
        check('dependants equal (400) in A and B', gA[0] + gA[2] == gB[0] + gB[2] == 400),
        check('all bars within the 0-60 scale', all(max(m, f) <= 60 for m, f in A_COUNTS + B_COUNTS)),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\b600\b', r'\b300\b']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'r035_question': {'path': 'assets/images/%s-%s-question.png' % (R035, RID), 'layers': [V], 'clip': clip, 'hide_base': True, 'bound_item': R035,
                          'forbidden': [r'dependants']},
        'r035_answer': {'path': 'assets/images/%s-%s-answer.png' % (R035, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': R035},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
