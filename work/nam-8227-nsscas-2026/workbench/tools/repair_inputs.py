"""Round-2 human annotations, independent of family membership (8227 only).

Short demand notation is theme.topic.objective.demand. '+' joins direct demands.
NSSCO.* and MODEL are separately registered assessed prior/cross-cutting demands;
they never add coverage to the 138 specific-objective demands. These are author
judgements to be independently re-reviewed, not automated content certification.
"""

PART_DEMANDS = '''
2021-1-Q1|a=1.2.1.1;b=1.2.1.2+1.2.1.3
2021-1-Q2|answer=1.1.5.1
2021-1-Q3|a=1.1.4.1+1.1.4.2+1.1.4.3;b=1.1.4.1+1.1.4.2+1.1.4.3
2021-1-Q4|a=1.9.1.1+1.9.1.2+1.9.2.1+1.9.4.3;b=1.9.1.2+1.9.4.3+1.9.3.1
2021-1-Q5|a=1.6.6.1+1.6.6.2;b=1.6.5.1
2021-1-Q6|a=1.7.2.1+1.7.2.2+1.7.2.3+1.7.3.2+1.7.3.3;b=1.7.4.2+1.7.5.2
2021-1-Q7|a=1.5.2.1+MODEL;b=1.5.2.2
2021-1-Q8|a=1.2.2.2+1.2.3.2+1.2.3.3;b=1.2.2.1+1.2.3.1+1.2.3.3
2021-1-Q9|a=1.9.1.2+1.9.3.1+1.9.4.1;b=1.9.3.1+1.9.4.2
2021-1-Q10|a=1.1.2.1+1.1.2.2+1.1.2.3+1.1.6.1+1.1.6.2+1.4.2.1;b=1.1.2.1+1.1.2.2
2021-1-Q11|a=1.8.2.1+1.8.4.1;b=1.8.2.1+1.8.3.1
2021-1-Q12|a=1.3.2.1+1.3.1.2;b=1.3.3.2+1.3.2.1+1.3.1.2;c=1.3.5.1+1.3.5.2;d=1.8.2.2
2021-2-Q1|a=2.1.4.1+2.1.4.3;b=2.1.4.2+2.1.4.4
2021-2-Q2|answer=2.5.1.1+1.9.3.1+2.2.1.2
2021-2-Q3|answer=2.1.1.3+1.1.6.1+1.1.6.2
2021-2-Q4|a=2.2.2.2;b=2.2.3.1+2.2.3.2
2021-2-Q5|a=2.4.2.1+2.4.1.1;b=2.5.1.3+1.9.3.1
2021-2-Q6|a=2.3.2.2+2.3.2.5;b=1.6.6.1+2.3.2.5+1.6.3.1
2021-2-Q7|answer=2.4.3.2+2.4.3.3+1.8.3.1
2021-2-Q8|a=2.6.1.2;b=2.6.3.1+2.6.3.2;c.i=2.6.4.1;c.ii=2.6.4.1+2.6.4.2+2.6.2.1
2021-2-Q9|a=2.5.1.1;b=2.5.2.1+2.5.2.2+2.5.1.2
2021-2-Q10|a=2.4.3.1;b=2.4.3.3+1.8.3.1
2021-2-Q11|a=2.2.1.1+2.2.1.2;b=1.1.4.1+1.1.4.2+1.1.4.3+2.2.3.1
2021-2-Q12|a.i=2.3.2.4;a.ii=2.3.2.5+1.6.6.1+1.6.6.2;b=2.3.2.3+2.3.2.5+1.6.6.1+1.6.6.2
2022-1-Q1|a=1.1.1.1;b=1.1.1.2
2022-1-Q2|a=NSSCO.quadratic;b=1.1.4.1+1.1.4.2+1.1.4.3
2022-1-Q3|answer=1.2.1.2+1.2.1.3
2022-1-Q4|answer=1.1.2.1+1.1.2.2+1.1.2.3+1.1.6.1+1.1.6.2
2022-1-Q5|a=1.2.3.1;b=1.2.4.1+1.2.4.2+1.2.5.2
2022-1-Q6|a=1.3.2.1+1.3.1.2;b=1.3.3.2+2.2.2.2+2.2.2.1;c=1.3.5.1+1.3.5.2+2.2.2.2
2022-1-Q7|answer=1.8.2.1+1.8.3.1+1.4.1.1
2022-1-Q8|a=1.5.2.1+1.5.2.2+MODEL;b=1.8.4.1+1.8.4.2+1.8.2.1
2022-1-Q9|a=1.6.5.2;b=1.6.6.1+1.6.6.2+1.6.3.1
2022-1-Q10|a=1.6.2.1+1.6.2.2;b=1.6.2.1;c=1.6.2.2
2022-1-Q11|a=1.7.2.1+1.7.2.2+1.7.2.3+1.7.3.3;b=1.7.4.1+1.7.4.2+1.7.5.1
2022-1-Q12|a=MODEL+NSSCO.similar-triangles+NSSCO.mensuration;b=1.8.3.3+1.8.2.1
2022-1-Q13|answer=1.9.1.2+1.9.2.1+1.9.2.2
2022-1-Q14|a=1.4.1.1;b=1.9.4.2+1.9.1.2+1.9.3.1
2022-2-Q1|a=2.1.1.1+2.1.1.2;b=2.1.1.2+2.2.3.1
2022-2-Q2|answer=1.1.4.1+1.1.4.2+1.1.4.3+2.2.3.1
2022-2-Q3|a=1.6.6.1+1.6.6.2+1.6.3.1;b=2.4.1.1+2.4.1.2+1.8.1.1+1.6.3.1;c=2.5.2.1+2.5.2.2+1.9.4.1+1.9.3.1
2022-2-Q4|a=2.1.4.1+2.1.4.2+2.1.4.3;b=1.1.1.1+1.1.1.2
2022-2-Q5|a=2.4.2.1+2.4.1.2+1.8.1.1+2.6.3.1+2.6.3.2;b=2.6.1.2;c=2.6.4.1+2.6.4.2+2.6.2.1
2022-2-Q6|a=2.3.2.4;b.i=2.3.2.5+1.6.6.1+1.6.6.2;b.ii=2.3.2.4+2.3.2.5
2022-2-Q7|a=2.3.1.1+2.3.2.1+2.3.2.3+2.3.2.5;b=2.5.2.1+2.5.1.2
2022-2-Q8|answer=2.5.1.1+1.9.3.1+2.2.1.2
2022-2-Q9|a=1.3.2.1+1.3.1.2;b.i=1.3.3.2+2.2.1.1;b.ii=1.3.2.2+1.3.1.2;c.i=1.3.4.1+1.3.1.1;c.ii=1.3.4.2+1.3.2.1+1.3.1.2
2022-2-Q10|a=2.4.3.2+2.4.3.3;b=2.4.3.2+2.4.3.3+2.3.2.3
2023-1-Q1|a=1.1.6.1+1.1.6.2;b=1.1.2.1+1.1.2.2
2023-1-Q2|a=1.3.3.2;b=1.3.2.1+1.3.1.2;c.i=1.3.4.1;c.ii=1.3.4.1
2023-1-Q3|answer=1.1.3.2
2023-1-Q4|a=1.2.1.1;b=1.2.1.2+1.2.1.3
2023-1-Q5|a=1.2.2.2;b=1.2.5.1;c=1.2.5.2+1.2.5.1
2023-1-Q6|a=MODEL+NSSCO.right-triangle-trig;b=1.5.2.2
2023-1-Q7|a.i=1.7.2.1+1.7.3.2;a.ii=1.7.2.1+1.7.2.3+1.7.3.3;b.i=1.7.4.1;b.ii=1.7.4.2+1.7.5.1
2023-1-Q8|a=1.6.5.1;b=1.6.5.2+1.6.6.1+1.6.6.2
2023-1-Q9|answer=1.6.4.1
2023-1-Q10|a=1.8.4.1+1.8.3.4+1.8.2.1;b=1.8.4.1
2023-1-Q11|answer=1.8.2.2+1.8.1.2
2023-1-Q12|answer=1.9.1.2+1.9.3.1+1.9.3.2+1.9.4.1
2023-1-Q13|a=MODEL+NSSCO.mensuration;b=1.8.4.1+1.8.2.1
2023-2-Q1|a=2.1.3.1+2.1.3.3;b=2.1.4.2;c=2.1.4.4
2023-2-Q2|answer=2.1.2.2
2023-2-Q3|a=2.3.2.2+2.3.2.5+1.6.6.1+1.6.3.1;b.i=2.3.1.1+2.3.2.1+2.3.2.3+2.3.2.5;b.ii=2.3.2.5+1.6.3.1;b.iii=2.5.2.1+2.5.1.2
2023-2-Q4|a=2.2.4.1+2.2.4.2;b=2.2.1.2+2.2.3.1;c=2.2.1.2+2.2.3.1
2023-2-Q5|a=2.4.2.2+2.4.1.1+1.8.4.1;b=2.5.2.1+2.5.2.2+2.5.1.2+1.9.3.1
2023-2-Q6|a=2.5.3.1+2.5.3.2;b=2.5.3.2+2.2.1.2;c=2.2.2.2+2.5.4.1;d=2.5.4.2
2023-2-Q7|a=1.9.1.2+2.5.1.2+1.9.3.1+2.6.3.1+2.6.3.2;b=2.6.1.2;c=2.6.4.1+2.6.4.2+2.6.2.1
2023-2-Q8|a=2.4.3.1+2.4.2.1;b=2.4.3.3+1.8.1.1
2023-2-Q9|a=2.4.1.1+2.4.1.2+1.8.3.4;b=2.5.1.1+1.9.4.3+1.9.3.1
2024-1-Q1|answer=1.1.4.1+1.1.4.2+1.1.4.3+2.2.3.1
2024-1-Q2|answer=1.1.3.2
2024-1-Q3|answer=1.2.1.2
2024-1-Q4|a=1.2.3.2+1.2.3.3;b=1.2.3.2+1.2.3.3+2.2.3.2;c=1.2.5.2
2024-1-Q5|a=1.1.2.1+1.1.2.2+1.1.2.3+1.1.6.1+1.1.6.2;b=1.1.2.1+1.1.2.2
2024-1-Q6|a=1.1.1.1;b=1.3.2.2+1.3.1.2;c=1.3.3.2
2024-1-Q7|a=MODEL+NSSCO.right-triangle-trig;b=1.5.2.2
2024-1-Q8|answer=1.4.1.1+NSSCO.coordinate-geometry
2024-1-Q9|a=1.6.2.1+1.6.2.2;b=1.6.2.1;c=1.6.2.2+1.6.1.1
2024-1-Q10|a=1.7.1.1+1.7.1.2+1.7.2.1+1.7.2.2+1.7.3.2;b=1.7.1.1+1.7.2.1+1.7.3.2;c=1.7.4.1+1.7.4.2+1.7.5.1
2024-1-Q11|a=MODEL+NSSCO.mensuration;b=MODEL+NSSCO.mensuration;c=1.8.4.1+1.8.2.1
2024-1-Q12|a=1.6.5.2+2.3.1.1;b=1.6.6.1+1.6.6.2+1.6.3.1
2024-1-Q13|a=1.8.1.1+1.8.3.1;b=1.9.1.2+1.9.2.1+1.9.2.2
2024-1-Q14|answer=1.9.1.2+1.9.3.1+1.9.4.1
2024-2-Q1|answer=2.4.2.2+1.8.1.1
2024-2-Q2|answer=2.3.2.2+2.3.1.1+2.3.2.5+1.6.6.1+1.6.6.2+1.6.3.1
2024-2-Q3|answer=2.2.1.2+1.1.6.1+1.1.6.2
2024-2-Q4|a=2.4.1.2;b=2.5.1.3
2024-2-Q5|a=2.1.3.1+2.1.3.3;b=2.5.1.1+1.9.1.2;c=2.1.4.2+2.1.4.4+2.3.1.1+1.6.6.1+1.6.6.2
2024-2-Q6|a=2.5.2.1+2.5.2.2+2.5.1.2+1.9.3.1;b=1.9.4.2+2.5.2.1+2.5.1.2+1.9.3.1
2024-2-Q7|a=2.6.3.1+2.6.3.2;b=2.6.4.1+2.6.4.2+2.6.2.1;c=2.4.3.2+2.4.2.1+2.4.1.2+2.4.3.3
2024-2-Q8|a=2.2.2.2;b=2.2.3.1+1.4.2.1
2024-2-Q9|a=2.3.1.1+2.3.2.1+2.3.2.5;b=2.3.2.2+2.3.2.5+1.6.3.1
2024-2-Q10|a=2.4.1.1+2.4.1.2+1.8.4.1;b=1.8.4.2
2024-2-Q11|a=2.1.2.1+1.4.1.1;b=2.1.1.2+1.4.2.1;c=2.1.1.3+2.1.2.2
2025-1-Q1|a=1.1.2.1+1.1.2.2;b=1.1.6.1+1.1.6.2
2025-1-Q2|answer=1.2.1.2+1.2.1.3
2025-1-Q3|a=1.7.2.1+1.7.2.2+1.7.4.2+1.7.5.2;b=1.7.4.1+1.7.4.2+1.7.5.1
2025-1-Q4|a=1.6.2.3+1.6.1.1;b=1.4.1.1;c=1.4.2.1
2025-1-Q5|a=1.2.5.2+1.2.3.1;b=1.2.3.1
2025-1-Q6|a=1.6.5.1;b=1.6.5.2+1.6.6.1+1.6.6.2
2025-1-Q7|a=1.1.1.1;b=1.3.3.1+1.3.3.2+1.3.1.3;c=1.3.2.2+1.3.1.2;d=1.3.3.2+1.3.2.1+1.3.1.2
2025-1-Q8|a=1.8.1.1;b=1.9.1.2+1.9.2.1+1.9.2.2
2025-1-Q9|a=MODEL+NSSCO.mensuration+NSSCO.right-triangle-trig;b=1.8.2.1+1.8.4.1;c=1.8.4.2
2025-1-Q10|a=MODEL+NSSCO.right-triangle-trig;b=1.5.2.2
2025-1-Q11|a=1.4.2.1;b=1.1.4.1+1.1.4.2+1.1.4.3;c=1.9.1.2+1.9.3.1+1.9.4.1
2025-1-Q12|a=1.4.1.1+NSSCO.coordinate-geometry;b=1.4.1.1+NSSCO.coordinate-geometry
2025-2-Q1|answer=2.1.4.1+2.1.4.2+2.1.4.3
2025-2-Q2|answer=2.1.1.1+2.1.1.2+2.2.1.1
2025-2-Q3|answer=2.3.1.1+2.3.2.2+2.3.2.5+1.6.3.1
2025-2-Q4|a=2.5.3.1+2.5.3.2+2.3.1.1;b=2.5.4.1+2.5.4.2+2.3.1.2
2025-2-Q5|answer=2.4.3.1+2.4.2.1+2.4.1.2+2.4.3.3
2025-2-Q6|a=2.2.4.1+2.2.4.2;b=2.2.3.1
2025-2-Q7|a=2.3.2.3+2.3.2.5+2.3.2.1;b=2.3.2.5
2025-2-Q8|answer=1.8.3.4+1.8.2.1+1.8.2.2
2025-2-Q9|a=2.3.2.4;b=2.3.1.1+2.3.2.5+1.6.6.1+1.6.6.2
2025-2-Q10|a=2.4.1.1+2.4.1.2+2.3.2.1;b=2.5.1.3+2.5.2.1+2.5.1.2+1.9.3.1
2025-2-Q11|a=2.2.2.2;b=2.2.3.1;c=2.4.1.1+2.4.1.2+1.8.3.3
2025-2-Q12|a=2.6.1.1+2.1.2.1+2.2.2.2;b=2.6.3.1+2.6.3.2;c=2.6.1.2;d=2.6.4.1+2.6.4.2+2.6.2.1
'''

# Implicit shared-given dependencies are not an official F.T. award. Manual
# choices record the actual reused result; wording cues are scanned separately.
DEPENDENCY_OVERRIDES = {
 '2022-2-Q6': [('a','b.ii','Hence applies to both subparts of (b); reuse R for extrema')],
 '2021-1-Q1': [('a','b','Expansion coefficients reused')],
 '2021-1-Q4': [('a','b','Integrate the recovered velocity')],
 '2021-1-Q6': [('a','b','Use AP and coordinates constructed in (a)')],
 '2021-1-Q8': [('a','b','Equal donation totals')],
 '2021-1-Q12': [('a','b','Least domain bound'),('a','c','Specified domain bound'),('b','c','Inverse expression')],
 '2022-2-Q9': [('a','b.i','Chosen domain'),('b.i','b.ii','Range of inverse'),('b.i','c.i','Evaluate inverse before composition'),('a','c.ii','Check log domain')],
 '2023-1-Q4': [('a','b','Reuse binomial expansion')],
 '2023-1-Q5': [('a','b','Common ratio'),('b','c','Admissibility of infinite-sum solutions')],
 '2023-1-Q6': [('a','b','Inner radius before area')],
 '2023-1-Q7': [('a.i','a.ii','AB reused to construct OC'),('b.i','b.ii','Magnitudes in angle denominator')],
 '2024-1-Q4': [('a','b','Common ratio'),('a','c','Common ratio')],
 '2024-1-Q6': [('a','b','Vertex and endpoint comparison'),('a','c','Square form and inverse sign')],
 '2024-1-Q7': [('a','b','Unrounded common-tangent angle')],
 '2024-1-Q10': [('a','c','AN'),('b','c','AC')],
 '2024-1-Q11': [('a','b','Eliminate height'),('b','c','Optimise area model')],
 '2024-1-Q13': [('a','b','Recovered derivative coefficient')],
 '2025-1-Q7': [('a','b','Vertex bounds one-to-one branch'),('b','c','Domain bound'),('b','d','One-to-one restriction')],
 '2025-1-Q8': [('a','b','Recovered k')],
 '2025-1-Q9': [('a','b','Surface-area model'),('b','c','Stationary location')],
 '2025-1-Q10': [('a','b','R=3r')],
 '2025-1-Q11': [('a','b','Quartic intersection equation'),('b','c','Integration bounds')],
}

SKETCH_PARTS = {'2021-1-Q12:c','2021-2-Q4:a','2022-1-Q6:c','2023-2-Q6:c',
 '2024-2-Q8:a','2024-2-Q11:a','2025-1-Q4:a','2025-1-Q4:b',
 '2025-2-Q4:b','2025-2-Q11:a','2025-2-Q12:a'}
SKETCH_DEPENDENT = {'2023-2-Q6:d','2025-1-Q4:c'}

HOLD_QUESTIONS = {
 '2022-1-Q13':'SRC-8227-DOMAIN-2022-P1-Q13',
 '2023-1-Q9':'SRC-8227-PRINCIPAL-2023-P1-Q9',
}
HOLD_PARTS = {'2023-1-Q1:b':'SRC-8227-DEGENERATE-2023-P1-Q1B'}

# Minor repairs to legacy family tags are separate from the demand annotation.
PATTERN_OVERRIDES = {
 '2021-2-Q9:b':['55','54'], '2021-2-Q11:a':['42'],
 '2022-1-Q2:a':[], '2025-1-Q8:a':[], '2023-1-Q10:a':['29'],
 '2022-2-Q8:answer':['54','33','42'], '2025-1-Q4:c':['18'],
 '2022-1-Q8:a':['19'], '2022-1-Q12:a':[], '2023-1-Q13:a':[],
 '2024-1-Q11:a':[], '2024-1-Q11:b':[], '2025-1-Q9:a':[],
 '2023-1-Q9:answer':[],
}

MAPPING_NOTES = {
 '2021-2-Q9:b':'Indefinite integral: integration constant is assessed (2021 report PDF 241); no definite-integral demand.',
 '2022-1-Q2:a':'Ordinary NSSCO quadratic solved; no substituted-variable demand until part (b).',
 '2021-2-Q11:a':'Log laws establish a quoted ordinary quadratic; no disguised-variable recovery in this part.',
 '2025-1-Q8:a':'Substitute the point gradient into the supplied derivative; no differentiation performed.',
 '2025-2-Q8:answer':'Rewrite rational velocity as powers; quotient rule is an alternative, not a required directly assessed demand.',
 '2022-1-Q7:answer':'Quartic tangency uses derivative, not a repeated-root discriminant test on a quadratic.',
 '2022-2-Q8:answer':'Logarithms equated to solve for an integral bound; not an exponential equation a^x=b.',
 '2023-1-Q6:a':'Radius derived by right-triangle geometry; no sector calculation or differentiation yet.',
 '2024-1-Q7:a':'Angle established by common-tangent right-triangle geometry; no sector calculation yet.',
 '2025-1-Q10:a':'Circle contact establishes radius relation by right-triangle geometry.',
 '2023-1-Q9:answer':'Defective principal-value equation; retained as held source evidence, never counted as a usable examination exemplar.',
}


def demand_id(short):
    if short == 'MODEL':
        return '8227:2020:ABILITY:08:MODEL'
    if short.startswith('NSSCO.'):
        return '8227:PRIOR:' + short.replace('.', ':')
    theme, topic, obj, demand = map(int, short.split('.'))
    return f'8227:2020:M{theme}:T{topic}:O{obj:02d}:D{demand:02d}'


def part_annotations():
    result = {}
    for line in PART_DEMANDS.strip().splitlines():
        q, parts = line.split('|')
        for part in parts.split(';'):
            label, codes = part.split('=')
            key = q + ':' + label
            assert key not in result
            result[key] = [demand_id(x) for x in codes.split('+')]
    assert len(result) == 250
    return result


# Response evidence, authored from the requested output rather than inferred
# from a family or words in the shared stem. Entries follow printed part order.
# n numeric; s symbolic; p proof/show-that; g sketch; e explanation.
RESPONSE_FORMATS='''
2021-1-Q1|s,n
2021-1-Q2|s
2021-1-Q3|n,n
2021-1-Q4|s,n
2021-1-Q5|n,p
2021-1-Q6|n,p
2021-1-Q7|s,n
2021-1-Q8|n,n
2021-1-Q9|n,s
2021-1-Q10|s,e
2021-1-Q11|n,s
2021-1-Q12|n,s,g,n
2021-2-Q1|n,n
2021-2-Q2|p
2021-2-Q3|s
2021-2-Q4|g,n
2021-2-Q5|s,n
2021-2-Q6|p,n
2021-2-Q7|s
2021-2-Q8|p,p,n,n
2021-2-Q9|s,s
2021-2-Q10|p,s
2021-2-Q11|p,n
2021-2-Q12|s,n,n
2022-1-Q1|s,n
2022-1-Q2|n,n
2022-1-Q3|n
2022-1-Q4|s
2022-1-Q5|n,n
2022-1-Q6|n,s,g
2022-1-Q7|s
2022-1-Q8|p,e
2022-1-Q9|p,n
2022-1-Q10|n,n,s
2022-1-Q11|p,n
2022-1-Q12|p,s
2022-1-Q13|s
2022-1-Q14|n,s
2022-2-Q1|n,n
2022-2-Q2|s
2022-2-Q3|s,s,n
2022-2-Q4|n,n
2022-2-Q5|p,p,n
2022-2-Q6|s,n,n
2022-2-Q7|p,s
2022-2-Q8|n
2022-2-Q9|n,s,s,n,e
2022-2-Q10|n,s
2023-1-Q1|s,p
2023-1-Q2|s,s,s,n
2023-1-Q3|n
2023-1-Q4|s,n
2023-1-Q5|p,s,n
2023-1-Q6|p,n
2023-1-Q7|s,s,n,n
2023-1-Q8|p,n
2023-1-Q9|n
2023-1-Q10|n,n
2023-1-Q11|s
2023-1-Q12|p
2023-1-Q13|p,n
2023-2-Q1|p,s,n
2023-2-Q2|n
2023-2-Q3|n,p,s,s
2023-2-Q4|n,p,n
2023-2-Q5|s,p
2023-2-Q6|n,n,g,e
2023-2-Q7|p,p,n
2023-2-Q8|p,n
2023-2-Q9|s,n
2024-1-Q1|n
2024-1-Q2|n
2024-1-Q3|s
2024-1-Q4|n,n,n
2024-1-Q5|s,n
2024-1-Q6|s,s,s
2024-1-Q7|p,n
2024-1-Q8|n
2024-1-Q9|n,n,s
2024-1-Q10|p,s,n
2024-1-Q11|s,p,s
2024-1-Q12|p,n
2024-1-Q13|n,s
2024-1-Q14|n
2024-2-Q1|n
2024-2-Q2|n
2024-2-Q3|s
2024-2-Q4|s,s
2024-2-Q5|p,s,n
2024-2-Q6|p,s
2024-2-Q7|p,n,n
2024-2-Q8|g,s
2024-2-Q9|n,s
2024-2-Q10|n,e
2024-2-Q11|g,s,s
2025-1-Q1|p,s
2025-1-Q2|n
2025-1-Q3|n,n
2025-1-Q4|g,g,n
2025-1-Q5|n,n
2025-1-Q6|p,n
2025-1-Q7|s,n,s,s
2025-1-Q8|n,s
2025-1-Q9|p,n,e
2025-1-Q10|p,n
2025-1-Q11|p,n,n
2025-1-Q12|s,n
2025-2-Q1|n
2025-2-Q2|n
2025-2-Q3|s
2025-2-Q4|n,g
2025-2-Q5|n
2025-2-Q6|s,n
2025-2-Q7|p,n
2025-2-Q8|n
2025-2-Q9|s,n
2025-2-Q10|p,s
2025-2-Q11|g,n,n
2025-2-Q12|g,p,p,n
'''


def response_annotations():
    labels={line.split('|')[0]:[v.split('=')[0] for v in line.split('|')[1].split(';')]
            for line in PART_DEMANDS.strip().splitlines()}
    names={'n':'numeric','s':'symbolic','p':'proof/show-that','g':'sketch','e':'explanation'}
    result={}
    for line in RESPONSE_FORMATS.strip().splitlines():
        key,formats=line.split('|');codes=formats.split(',')
        assert len(labels[key])==len(codes),key
        for label,code in zip(labels[key],codes):result[key+':'+label]=names[code]
    assert set(result)==set(part_annotations())
    return result

# Source-checked conceptual interpretations; broad objective links do not create standalone recipe types.
MAPPING_NOTES.update({'2021-1-Q12:a': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2021-1-Q12:b': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2022-1-Q6:a': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2022-1-Q6:b': 'Inverting ln(x-2) explicitly uses the defining inverse relationship between ln and exp; it is not merely a graph-shape prerequisite.', '2022-2-Q9:a': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2022-2-Q9:b.ii': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2022-2-Q9:c.ii': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2023-1-Q2:b': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2024-1-Q6:b': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2025-1-Q7:b': 'The explicitly credited one-to-one/inverse-existence condition also assesses interpretation of that concept.', '2025-1-Q7:c': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.', '2025-1-Q7:d': 'The required domain/range answer directly demonstrates interpretation of the domain/image-set terms, as well as the more specific determination objective.'})

# Round-3 source-confirmed dependencies, supplementary to scanned cues.
DEPENDENCY_OVERRIDES.setdefault("2024-2-Q11", []).append(("a","c","Deduce uses the two sketches as well as the intersection from part (b)."))
MAPPING_NOTES["2021-1-Q4:b"]="Distance after 3 seconds is the definite integral of positive v=3t^2+t+2 from 0 to 3 (37.5 m); first-order curve recovery is not the only acceptable method."
