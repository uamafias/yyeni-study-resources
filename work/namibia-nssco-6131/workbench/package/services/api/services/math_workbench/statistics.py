"""Statistics/probability demands with actual data and diagrams."""
from copy import deepcopy
from fractions import Fraction as F
import random
import statistics as stats
import math
from .core import calc, fmt, part, question, step
from .diagrams import asset, cartesian, circle, line, polygon, polyline, rect, spec, text

def partition(total, n, rng):
    cuts = sorted(rng.sample(range(1, total), n - 1))
    points = [0] + cuts + [total]
    return [b - a for a, b in zip(points, points[1:])]

def build_collect_classify_tabulate(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    counts = partition(20, 3, rng)
    responses = ['Walk'] * counts[0] + ['Cycle'] * counts[1] + ['Bus'] * counts[2]
    rng.shuffle(responses)
    q('collect-classify-tabulate', ['12a.1'], 'A travel survey', 'A class records how 20 learners usually travel to school. The responses are:\n\n' + ', '.join(responses) + '.', [part('Write a suitable survey question, including response categories, that could collect these data.', 'How do you usually travel to school: walk, cycle or bus? (Accept an equivalent clear question with the stated categories.)', [step('Identify the recorded variable and its categories', 'A collection question must ask about the usual travel method and allow the recorded responses.', 'Ask the learner’s usual travel method, with Walk/Cycle/Bus options.')]), part('Classify and tabulate the responses in a frequency table.', f'Walk: {counts[0]}; Cycle: {counts[1]}; Bus: {counts[2]}; Total: 20.', [step('Sort responses into the three categories', 'Each learner contributes exactly one observation.', '; '.join((f'{label}: {n}' for label, n in zip(['Walk', 'Cycle', 'Bus'], counts)))), step('Check the table total', 'The category counts must account for every response.', 'Total = 20')], 3, [(1, 'Suitable labelled categories.'), (1, 'Correct category frequencies.'), (1, 'Complete table with total 20.')], checks=[(sum(counts) == len(responses) == 20, 'The frequency table reconciles to all raw observations')])])
    return out

def build_frequency_bar_pie_pictogram(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    counts = [2 * x for x in partition(12, 4, rng)]
    raw = sum(([i] * n for i, n in enumerate(counts)), [])
    rng.shuffle(raw)
    bar, pt = cartesian(0, 5, 0, 24, width=150, height=120, xstep=1, ystep=2)
    bar['commands'] += [text((40, 3), 'Books read'), text((14, 113), 'Number of learners')]
    barsol = deepcopy(bar)
    for i, n in enumerate(counts):
        x, y = pt(i + 0.6, 0)
        x2, _ = pt(i + 1.2, 0)
        _, top = pt(0, n)
        barsol['commands'].append(rect(x, y, x2 - x, top - y, fill='#dddddd'))
        barsol['commands'].append(text((x, 8), i))
    bar['commands'] = [c for c in bar['commands'] if not (c['kind'] == 'text' and c['value'] in ['1', '2', '3', '4', '5'] and (c['p'][1] < 15))]
    barsol['commands'] = [c for c in barsol['commands'] if not (c['kind'] == 'text' and c['value'] in ['0', '1', '2', '3', '4', '5'] and (c['p'][1] < 15))]
    for i in range(4):
        x, _ = pt(i + 0.9, 0)
        bar['commands'].append(text((x - 1, 8), i))
        barsol['commands'].append(text((x - 1, 8), i))
    pie = spec(120, 115, [circle((60, 55), 40)])
    piesol = deepcopy(pie)
    angle = 0
    for i, n in enumerate(counts):
        extent = 360 * n / 24
        points = [(60, 55)] + [(60 + 40 * math.cos(math.radians(angle + extent * j / 60)), 55 + 40 * math.sin(math.radians(angle + extent * j / 60))) for j in range(61)]
        piesol['commands'].append(polygon(points, fill=['#eeeeee', '#cccccc', '#aaaaaa', '#888888'][i]))
        mid = math.radians(angle + extent / 2)
        piesol['commands'].append(text((60 + 26 * math.cos(mid) - 7, 55 + 26 * math.sin(mid)), f'{i} '+('book' if i==1 else 'books'), size=2.8))
        angle += extent
    pic = spec(150, 90, [text((15, 82), 'Key: one circle represents 2 learners')])
    picsol = deepcopy(pic)
    for i, n in enumerate(counts):
        y = 65 - 15 * i
        picsol['commands'].append(text((10, y), f'{i} '+('book' if i==1 else 'books')))
        for j in range(n // 2):
            picsol['commands'].append(circle((40 + 10 * j, y + 1), 3))
    q('frequency-bar-pie-pictogram', ['12a.3'], 'Representing reading data', 'The numbers of books read by 24 learners in one month are:\n\n' + ', '.join(map(str, raw)) + '.', [part('Construct a simple frequency distribution for 0, 1, 2 and 3 books.', '; '.join((f'{i} '+('book' if i==1 else 'books')+f': {n} learners' for i, n in enumerate(counts))), [step('Count each distinct value', 'A frequency distribution records the number of occurrences of every category.', '; '.join((f'{i} '+('book' if i==1 else 'books')+f': {n} learners' for i, n in enumerate(counts))))], 2, [(1, 'Correct categories and labels.'), (1, 'All four frequencies correct.')]), part('Draw a bar chart for these data on the supplied grid.', 'Four separated bars: '+ '; '.join(f'{i} '+('book' if i==1 else 'books')+f': {n} learners' for i,n in enumerate(counts))+'.', [step('Use the supplied scale and categories', 'The vertical scale represents learners and the categories are discrete.', '; '.join(f'{i} '+('book' if i==1 else 'books')+f': {n} learners' for i,n in enumerate(counts))), step('Draw separated bars', 'Bar heights encode frequencies; gaps distinguish the categories.', 'Each bar has the corresponding frequency height.')], 2, [(1, 'Accurate bar heights.'), (1, 'Separated consistently drawn bars.')]), part('Draw a pie chart for these data.', f'Sector angles: {', '.join(str(15*n) for n in counts)} degrees for 0, 1, 2, 3 books respectively.', [step('Convert each frequency to a sector angle', 'A complete circle is 360°, so each of 24 learners accounts for 15°.', ', '.join(str(15*n)+'°' for n in counts)), step('Construct and label the sectors', 'The sectors must account for the full circle.', f'Total angle {sum((15 * n for n in counts))}°.')], 3, [(1, 'Correct sector-angle calculation.'), (1, 'Accurate sector construction.'), (1, 'Complete correctly labelled chart.')]), part('Draw a pictogram using one symbol to represent 2 learners. Include the key.', f'Numbers of symbols: {', '.join(str(n//2) for n in counts)} for 0, 1, 2, 3 books.', [step('Use the key to convert frequencies into symbols', 'Divide each learner count by 2.', ', '.join(str(n//2) for n in counts)), step('Draw labelled rows and the key', 'The reader must know how many learners each symbol represents.', 'One complete symbol represents 2 learners.')], 3, [(1, 'Correct key.'), (1, 'Correct symbol counts.'), (1, 'Consistent symbols and labelled categories.')])], assets=[asset('bar-chart', bar, barsol), asset('pie-chart', pie, piesol), asset('pictogram', pic, picsol)])
    return out

def build_averages_and_their_purposes(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    add = 100 * rng.randint(0, 40)
    data = [4000 + add, 4200 + add, 4200 + add, 4400 + add, rng.randint(16, 28) * 1000 + add]
    mean = sum(data) / 5
    q('averages-and-their-purposes', ['12a.4'], 'Choosing a measure', 'The monthly earnings, in Namibian dollars, of five people are ' + ', '.join(map(str, data)) + '.', [calc('Calculate the mean.', f'N${mean:g}', '(' + '+'.join(map(str, data)) + ') ÷ 5', f'N${mean:g}', reason='The mean is total earnings divided by the number of people.', checks=[(stats.mean(data) == mean, 'Mean independently checked with the statistics library')]), part('Find the median and mode.', f'Median N${data[2]}; mode N${data[2]}.', [step('Locate the centre and most frequent value', 'The ordered list has five values, so the third is the median; the repeated value is the mode.', f'Median = mode = N${data[2]}.')], 2, [(1, 'Correct median.'), (1, 'Correct mode.')]), calc('Calculate the range.', f'N${data[-1] - data[0]}', f'{data[-1]} − {data[0]}', f'N${data[-1] - data[0]}', reason='The range measures spread as the greatest value minus the least.', marks=1), part('Which of the mean or median better represents a typical person’s earnings here? Explain.', 'The median, because the single very high earning pulls the mean upwards.', [step('Consider the effect of the high value', 'The median depends on order and is less affected by a very large outlier.', 'Median is more representative of a typical person in this group.')], 2, [(1, 'Median chosen.'), (1, 'Explanation linked to the high outlier.')]), part('A uniform shop wants to know which shirt size is most often bought. Which measure should it use? Explain.', 'The mode; it identifies the most frequent size.', [step('Match the measure to the decision', 'The shop needs the most common category rather than an average numerical size.', 'Use the mode.')], 2, [(1, 'Mode.'), (1, 'Most frequent category as reason.')])])
    return out

def build_percentiles_and_interpretation(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    frequencies = [4 * x for x in partition(20, 4, rng)]
    cum = [0]
    for f in frequencies:
        cum.append(cum[-1] + f)

    def percentile(rank):
        for i in range(4):
            if rank <= cum[i + 1]:
                return 10 * i + 10 * (rank - cum[i]) / frequencies[i]
        raise AssertionError(rank)
    lower, median, upper, p90 = [percentile(r) for r in [20, 40, 60, 72]]
    graph, pt = cartesian(0, 40, 0, 80, width=150, height=125, xstep=5, ystep=10)
    graph['commands'] += [polyline([pt(10 * i, n) for i, n in enumerate(cum)]), text((40, 3), 'Waiting time (minutes)'), text((14, 117), 'Cumulative frequency')]
    solution=deepcopy(graph)
    for value,rank in ((lower,20),(median,40),(upper,60),(p90,72)):
        solution['commands'] += [line(pt(0,rank),pt(value,rank),dash=True,color='#006633'),line(pt(value,rank),pt(value,0),dash=True,color='#006633')]
    from decimal import Decimal,ROUND_HALF_UP
    rounded=lambda value:str(Decimal(str(value)).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))
    q('percentiles-and-interpretation', ['12a.7'], 'Reading cumulative frequency', 'The cumulative frequency graph shows the waiting times of 80 patients at a clinic. Use the straight-line sections shown for your estimates.', [part('Estimate the median waiting time and explain its meaning.', f'About {rounded(median)} minutes; about half the patients waited no longer than this.', [step('Find half the total frequency', 'The median corresponds to the 40th patient.', f'At cumulative frequency 40, time ≈ {rounded(median)} minutes.'), step('Interpret the percentile', 'A median splits the observations into approximately equal halves.', 'About 50% waited no longer than this time.')], 2, [(1, 'Median within about 1 minute.'), (1, 'Correct interpretation.')]), part('Estimate the lower and upper quartiles.', f'Q1 ≈ {rounded(lower)}; Q3 ≈ {rounded(upper)} minutes.', [step('Find a quarter and three quarters of the total', 'The quartiles correspond to cumulative frequencies 20 and 60.', f'Q1 ≈ {rounded(lower)}; Q3 ≈ {rounded(upper)} minutes.')], 2, [(1, 'Lower quartile within about 1 minute.'), (1, 'Upper quartile within about 1 minute.')]), calc('Estimate the interquartile range.', f'{rounded(upper-lower)} minutes', f'{upper:.6g} − {lower:.6g}', f'{rounded(upper-lower)} minutes', reason='The interquartile range is the upper quartile minus the lower quartile.'), part('Estimate the 90th percentile and explain its meaning.', f'About {rounded(p90)} minutes; about 90% waited no longer than this.', [step('Find 90% of the total frequency', '0.9 × 80 = 72, so read the time at cumulative frequency 72.', f'90th percentile ≈ {rounded(p90)} minutes.'), step('Interpret the percentage', 'The percentile describes the proportion of observations at or below the value.', 'About 90% of patients waited no longer than this time.')], 2, [(1, '90th percentile within about 1 minute.'), (1, 'Correct percentile interpretation.')])], assets=[asset('cumulative-frequency',graph,solution)])
    return out

def build_probability_scale(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    p = rng.choice([F(1, 8), F(1, 4), F(3, 4), F(7, 8)])
    invalid_positive = F(rng.randint(11, 19), 10)
    invalid_negative = -F(rng.randint(1, 9), 10)
    total=rng.randint(4,12);favourable=rng.randint(1,total-1);event=F(favourable,total)
    scale = spec(150, 50, [line((15, 25), (135, 25)), line((15, 22), (15, 28)), line((135, 22), (135, 28)), text((13, 16), '0'), text((133, 16), '1')])
    sol = deepcopy(scale)
    sol['commands'] += [line((15+120*float(event),22),(15+120*float(event),28)),text((12+120*float(event),34),f'{float(event):.3g}'), line((15 + 120 * float(p), 22), (15 + 120 * float(p), 28)), text((12 + 120 * float(p), 12), str(float(p)))]
    q('probability-scale', ['12b.2'], 'The probability scale', 'A probability scale from 0 to 1 is shown.', [part('State which endpoint represents an impossible event and which represents a certain event.', 'Impossible: 0; certain: 1.', [step('Use the endpoint meanings', 'A probability of zero means impossible; one means certain.', '0: impossible; 1: certain.')], 2, [(1, 'Impossible at 0.'), (1, 'Certain at 1.')]), part(f'A bag has {favourable} red counters and {total-favourable} blue counters. One counter is chosen at random. Copy the scale and mark the probability of choosing red.',fmt(event)+', at proportion '+f'{float(event):.3g} of the full interval.',[step('Count equally likely outcomes','Divide the red counters by the total, then place that proportion of the distance from 0 to 1.',rf'P(\text{{red}})=\frac{{{favourable}}}{{{total}}}='+fmt(event))]), part(f'Mark the probability ${fmt(p)}$ on the scale.', f'At proportion {float(p):g} of the distance from 0 to 1.', [step('Place the fraction of the unit interval', 'The scale position is the probability times the full length.', f'{float(p):g} of the full interval from 0.')]), part(f'Explain why neither ${fmt(invalid_negative)}$ nor ${fmt(invalid_positive)}$ is a possible probability.', 'Probabilities cannot be negative or exceed 1.', [step('Apply the probability bounds', 'Every probability lies in the closed interval from 0 to 1.', 'Both given numbers lie outside [0,1].')], 2, [(1, 'Reject the negative value for the correct reason.'), (1, 'Reject the value above 1 for the correct reason.')])], assets=[asset('probability', scale, sol)])
    return out

def build_relative_frequency_experiment(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    N = 10 * rng.randint(5, 20)
    success = rng.randint(N // 5, 4 * N // 5)
    multiple = rng.randint(2, 10)
    future = N * multiple
    q('relative-frequency-experiment', ['12b.5'], 'An experimental probability', f'A spinner is spun {N} times under the same conditions. It lands on red {success} times.', [calc('Use these results to estimate the probability of red. Give your answer as a fraction in simplest form.', fmt(F(success, N)), f'{success} ÷ {N}', fmt(F(success, N)), reason='Relative frequency estimates probability as observed successes divided by the number of trials.'), calc(f'Estimate how many red results would occur in {future} further spins under the same conditions.', multiple * success, f'{future}\\times\\frac{{{success}}}{{{N}}}', multiple * success, reason='Expected frequency is the estimated probability multiplied by the future number of trials.'), part('Explain why the actual number of red results need not equal your estimate.', 'Random outcomes vary; the estimate is an expected count, not a guarantee.', [step('Distinguish expected frequency from certainty', 'Experimental probability estimates a long-run tendency, while a finite new sample can differ.', 'The actual random count can be above or below the expected count.')])])
    return out
BUILDERS = [build_collect_classify_tabulate, build_frequency_bar_pie_pictogram, build_averages_and_their_purposes, build_percentiles_and_interpretation, build_probability_scale, build_relative_frequency_experiment]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
