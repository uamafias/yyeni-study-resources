"""Original exam-style number, finance, set and measure questions."""
from fractions import Fraction as F
import math
import random
from .core import calc, fmt, part, question, step, significant

def build_classify_real_numbers(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    natural, negative, numerator = (rng.randint(2, 90), -rng.randint(1, 90), rng.choice([1, 3, 7, 9]))
    rows = [('0', 'whole, integer, rational, real'), (str(natural), 'natural, whole, integer, rational, real'), (str(negative), 'integer, rational, real'), (f'\\frac{{{numerator}}}{{10}}', 'rational, real'), (f'\\sqrt{{{rng.choice([2, 3, 5, 7, 11, 13])}}}', 'irrational, real'), ('\\pi', 'irrational, real')]
    q('classify-real-numbers', ['1a.1'], 'The real number system', 'Natural numbers in this question are the positive integers. For each number, write all the categories to which it belongs: natural, whole, integer, rational, irrational, real.', [part(f'Classify ${n}$.', a, [step('Identify the number and all containing sets', 'The categories overlap; an integer is also rational and real, while an irrational number is real but not rational.', a)]) for n, a in rows])
    return out

def build_number_properties(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    q('number-properties', ['1a.2'], 'Number properties', f'The numbers ${12 * t}$ and ${18 * t}$ are used in the calculations below.', [calc('Find their highest common factor.', 6 * t, f'\\gcd({12 * t},{18 * t})={6 * t}', 6 * t, checks=[(math.gcd(12 * t, 18 * t) == 6 * t, 'HCF independently checked with gcd')]), calc('Find their lowest common multiple.', 36 * t, f'\\frac{{{12 * t}\\times {18 * t}}}{{{6 * t}}}', 36 * t, checks=[(math.lcm(12 * t, 18 * t) == 36 * t, 'LCM independently checked with lcm')]), part('Write down a prime number between 10 and 20.', '11, 13, 17 or 19', [step('Test divisors below the square root', 'A prime has exactly two positive factors.', '11, 13, 17 or 19')]), part(f'Which of ${t * t}, {t * t + 1}, {t ** 3}$ is a square number? Give one answer.', t * t, [step('Identify an integer square', 'A square is the product of an integer with itself.', f'{t * t}={t}^2')]), part(f'Which of ${t ** 3}, {t ** 3 + 2}, {t ** 3 + 3}$ is a cube number?', t ** 3, [step('Identify an integer cube', 'A cube is the product of three equal integer factors.', f'{t ** 3}={t}^3')])])
    return out

def build_squares_cubes_roots(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    q('squares-cubes-roots', ['1b.1'], 'Powers and roots', 'Work out the following.', [calc(f'${t + 1}^2$', (t + 1) ** 2, f'{t + 1} × {t + 1}', (t + 1) ** 2, marks=1), calc(f'${t}^3$', t ** 3, f'{t} × {t} × {t}', t ** 3, marks=1), calc(f'$\\sqrt{{{(t + 3) ** 2}}}$', t + 3, f'({t + 3})^2={(t + 3) ** 2}', t + 3, marks=1), calc(f'$\\sqrt[3]{{{-t ** 3}}}$', -t, f'({-t})^3={-t ** 3}', -t, marks=1)])
    return out

def build_fraction_quantity_context(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    q('fraction-quantity-context', ['1d.1'], 'Water in a container', f'A container holds ${4 * t}$ litres of water. A learner uses $\\frac{{3}}{{8}}$ of the water.', [calc('Calculate the amount used, in litres.', fmt(F(3 * t, 2)), f'\\frac{{3}}{{8}}\\times {4 * t}', fmt(F(3 * t, 2))), calc('Calculate the amount left, in litres.', fmt(F(5 * t, 2)), f'{4 * t}-{fmt(F(3 * t, 2))}', fmt(F(5 * t, 2))), part('Express the fraction used as a decimal and as a percentage.', '0.375; 37.5%', [step('Convert the fraction', 'Division gives the decimal; multiplying by 100 expresses the same proportion as a percentage.', '3\\div8=0.375=37.5\\%')], 2, [(1, 'Correct decimal.'), (1, 'Correct percentage.')], objectives=['1d.2'])])
    return out

def build_six_way_conversions(seed,rng,requested_key=None):
    denominators=[2,4,5,8,10,16,20,25,40,50,100]
    values=rng.sample(sorted({F(n,d) for d in denominators for n in range(1,d)}),6)
    a,b,c,d,e,f=values
    decimal=lambda x:format(float(x),'.8f').rstrip('0').rstrip('.')
    return [question('six-way-conversions',['1d.2'],'Converting numbers',
        'Give fractions in their simplest form.',[
        calc(f'Write {decimal(a)} as a fraction.',fmt(a),f'{decimal(a)} as equal place-value parts',fmt(a),marks=1),
        calc(f'Write ${fmt(b)}$ as a decimal.',decimal(b),f'{b.numerator} ÷ {b.denominator}',decimal(b),marks=1),
        calc(f'Write ${fmt(c)}$ as a percentage.',decimal(100*c)+'%',f'{fmt(c)} × 100%',decimal(100*c)+'%',marks=1),
        calc(f'Write {decimal(100*d)}% as a fraction.',fmt(d),f'{decimal(100*d)}/100',fmt(d),marks=1),
        calc(f'Write {decimal(100*e)}% as a decimal.',decimal(e),f'{decimal(100*e)} ÷ 100',decimal(e),marks=1),
        calc(f'Write {decimal(f)} as a percentage.',decimal(100*f)+'%',f'{decimal(f)} × 100%',decimal(100*f)+'%',marks=1)],variant=seed)]


def build_ordering_and_relations(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    q('ordering-and-relations', ['1e.1'], 'Ordering numbers', f'The numbers are $-{t},\\ -{t}.5,\\ \\frac{{1}}{{2}},\\ 0.05,\\ 0$.', [part('Write the numbers in ascending order, using < signs.', f'-{t}.5<-{t}<0<0.05<\\frac{{1}}{{2}}', [step('Compare signs and magnitudes', 'More negative numbers are smaller; compare the positive numbers in decimal form.', f'-{t}.5<-{t}<0<0.05<0.5')], 2, [(1, 'Both negative numbers in the correct order.'), (1, 'Complete increasing chain.')]), part('Write the numbers in descending order.', f'\\frac{{1}}{{2}},0.05,0,-{t},-{t}.5', [step('Reverse the increasing order', 'Descending order runs from greatest to least.', f'\\frac{{1}}{{2}},0.05,0,-{t},-{t}.5')]), part(f'Use inequality signs to state that an integer $n$ is at least ${t}$ and at most ${t + 5}$.', f'{t}\\le n\\le {t + 5}', [step('Translate both inclusive bounds', 'At least and at most include the boundary values.', f'{t}\\le n\\le {t + 5}')]), part('Write = or $\\ne$ in each space: $0.5\\ \\square\\ \\frac12$; $0.05\\ \\square\\ \\frac12$.', '=; \\ne', [step('Express each fraction as a decimal', 'Equality requires the same value.', '0.5=\\frac12;\\quad0.05\\ne\\frac12')], 2, [(1, 'Correct equality.'), (1, 'Correct non-equality.')])])
    return out

def build_standard_form_four_operations(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b = (rng.randint(2, 4), rng.randint(2, 9))
    q('standard-form-four-operations', ['1f.2'], 'Calculations in standard form', 'Give each answer in standard form.', [calc(f'$( {a}\\times10^5)+( {b}\\times10^4)$', f'{a + b / 10:g}\\times10^5', f'({a}+{b / 10:g})\\times10^5', f'{a + b / 10:g}\\times10^5'), calc(f'$( {b}\\times10^5)-( {a}\\times10^4)$', f'{b - a / 10:g}\\times10^5', f'({b}-{a / 10:g})\\times10^5', f'{b - a / 10:g}\\times10^5'), calc(f'$( {a}\\times10^3)( 2\\times10^{{-5}})$', f'{2 * a / 10:g}\\times10^{{-1}}' if 2 * a >= 10 else f'{2 * a}\\times10^{{-2}}', f'{2 * a}\\times10^{{-2}}', fmt(2 * a * 0.01)), calc(f'$( {2 * a}\\times10^6)\\div(2\\times10^2)$', f'{a}\\times10^4', f'({2 * a}\\div2)\\times10^{{6-2}}', f'{a}\\times10^4')])
    return out

def build_mixed_arithmetic(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    q('mixed-arithmetic', ['1g.1'], 'Calculations with numbers', 'Work out the following. Give fraction answers in their simplest form.', [calc(f'$-{t}+3\\times({t}-5)$', -t + 3 * (t - 5), f'-{t}+3({t - 5})', -t + 3 * (t - 5)), calc(f'${t}.4+2.75-1.6$', f'{t + 1.55:g}', f'{t + 0.4:g}+2.75-1.6', f'{t + 1.55:g}'), calc(f'$({t}.5\\times0.4)\\div0.2$', 2 * t + 1, f'{t + 0.5:g}\\times2', 2 * t + 1), calc(f'${t}\\frac12+\\frac23-\\frac34$', fmt(F(t) + F(1, 2) + F(2, 3) - F(3, 4)), f'{t}+\\frac{{6+8-9}}{{12}}', fmt(F(t) + F(5, 12))), calc(f'${t}\\frac12\\div\\frac34$', fmt(F(2 * t + 1, 2) / F(3, 4)), f'\\frac{{{2 * t + 1}}}{{2}}\\times\\frac43', fmt(F(4 * t + 2, 3)))])
    return out

def build_rounding_in_context(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    length = rng.randint(111, 999) / 10
    length_exact = F(str(length))
    count = math.ceil(length_exact / F(3, 5))
    q('rounding-in-context', ['1h.3'], 'Buying fence panels', f'A straight fence must cover at least ${length:g}$ m. Each panel covers $0.6$ m. Panels can only be bought whole.', [calc('Find the least number of panels required.', count, f'{length:g}\\div0.6={length / 0.6:.6g}', f'{count} panels', reason='Round up, since rounding down would leave part of the fence uncovered.', checks=[(count * F(3, 5) >= length_exact and (count - 1) * F(3, 5) < length_exact, 'Purchased panels cover the length and one fewer does not')]), part('Explain why rounding the division to the nearest whole number may not give a suitable answer.', 'A rounded-down count can leave a gap; the count must be rounded upwards.', [step('Relate rounding to the requirement', 'The fence must cover at least the stated length.', 'Use the smallest whole count whose total length is sufficient.')])])
    return out

def build_increase_decrease_ratio(seed, rng, requested_key=None):
    denominator = rng.randint(3, 9)
    up = denominator + rng.randint(1, 5)
    down = rng.randint(1, denominator - 1)
    original = denominator * 20 * rng.randint(3, 20)
    return [question('increase-decrease-ratio', ['1j.3'], 'Changing by a ratio', f'A school club has N${original}.', [calc(f'Increase this amount in the ratio {up} : {denominator}.', f'N${original * up // denominator}', f'{original}\\times\\frac{{{up}}}{{{denominator}}}', f'N${original * up // denominator}', reason='The new-to-original ratio multiplies the original by its first term divided by its second.'), calc(f'Starting with the original amount, decrease it in the ratio {down} : {denominator}.', f'N${original * down // denominator}', f'{original}\\times\\frac{{{down}}}{{{denominator}}}', f'N${original * down // denominator}', reason='The new amount is the original multiplied by the stated fraction, which is smaller than one.')], variant=seed)]

def build_calculator_brackets(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = seed
    base_v = v % 6
    v = base_v
    x, y = (rng.randint(160, 300) / 10, rng.randint(20, 90) / 10)
    value = (x * x - y * y) / math.sqrt(9.7 + v)
    q('calculator-brackets', ['1k.1'], 'Using a calculator', 'Use a calculator.', [calc(f'Calculate $(({x:g})^2-({y:g})^2)\\div\\sqrt{{{9.7 + v:g}}}$ to 3 significant figures.', significant(value), f'(({x:g})^2-({y:g})^2)\\div\\sqrt{{{9.7 + v:g}}}', significant(value), reason='Bracket the numerator and keep the full calculator value until the final rounding.')])
    return out

def build_check_calculator_answer(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = rng.randint(0, 50)
    actual = (9.8 + v) * 51.3
    q('check-calculator-answer', ['1k.2'], 'Checking a result', f'A learner says that $({9.8 + v:g})\\times51.3={actual * 10:g}$.', [calc('Estimate the product using each number to 1 significant figure.', round(9.8 + v, -1) * 50, f'{round(9.8 + v, -1):g} × 50', round(9.8 + v, -1) * 50, objectives=['1h.1', '1k.2']), part('Use the estimate to explain whether the stated answer is reasonable.', 'No; the stated answer is about ten times the estimate.', [step('Compare the sizes', 'An estimate checks the order of magnitude without repeating the exact calculation.', f'The product is about {round(9.8 + v, -1) * 50:g}, not {actual * 10:g}.')]), calc('Calculate the correct product.', f'{actual:.2f}', f'{9.8 + v:g} × 51.3', f'{actual:.2f}')])
    return out

def build_household_finance(seed, rng, requested_key=None):
    cost = 20 * rng.randint(10, 70)
    profit, loss, discount = [rng.randint(5, 35) for _ in range(3)]
    principal = 500 * rng.randint(2, 30)
    rate = rng.randint(2, 12)
    years = rng.randint(2, 5)
    sale = cost * (1 + profit / 100)
    low = cost * (1 - loss / 100)
    return [question('household-finance', ['1l.2'], 'Savings and purchases', 'All rates below are supplied for this exercise.', [calc(f'A shop buys a desk for N${cost:.2f} and sells it for N${sale:.2f}. Calculate the percentage profit.', f'{profit}%', f'({sale:.2f} − {cost}) ÷ {cost} × 100%', f'{profit}%'), calc(f'A desk costing N${cost:.2f} is sold for N${low:.2f}. Calculate the percentage loss.', f'{loss}%', f'({cost} − {low:.2f}) ÷ {cost} × 100%', f'{loss}%'), calc(f'Find the price after a {discount}% discount on N${cost:.2f}.', f'N${cost * (1 - discount / 100):.2f}', f'{cost} × (1 − {discount}/100)', f'N${cost * (1 - discount / 100):.2f}', reason='A discount removes the stated percentage of the original price, leaving the complementary proportion.'), calc(f'N${principal} earns simple interest at {rate}% per year for {years} years. Calculate the interest.', f'N${principal * rate * years / 100:.2f}', f'{principal} × {rate}/100 × {years}', f'N${principal * rate * years / 100:.2f}'), calc(f'N${principal} is invested at {rate}% compound interest per year for {years} years. Calculate its final value to the nearest cent.', f'N${principal * (1 + rate / 100) ** years:.2f}', f'{principal} × (1+{rate}/100)^{years}', f'N${principal * (1 + rate / 100) ** years:.2f}')], variant=seed)]

def build_types_of_earnings(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = rng.randint(0, 40)
    base = 3000 + 200 * v
    pieces = 120 + 10 * v
    q('types-of-earnings', ['1l.4'], 'Earnings', 'The following workers are paid under different arrangements.', [calc(f'Anna earns a monthly salary of N${base}. Calculate her annual salary.', f'N${12 * base}', f'12 × {base}', f'N${12 * base}'), calc(f'Tangeni makes {pieces} items at N$3.50 per item. Calculate his piece-work pay.', f'N${pieces * 3.5:.2f}', f'{pieces} × 3.50', f'N${pieces * 3.5:.2f}'), calc(f'Selma earns N$40 per hour for 35 hours and 4% commission on sales of N${5000 + 500 * v}. Calculate her total earnings.', f'N${1600 + 20 * v}', f'35\\times40+0.04\\times{5000 + 500 * v}', f'N${1600 + 20 * v}')])
    return out

def build_water_bill_table(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = rng.randint(0, 15)
    old = 400 + 20 * v
    new = old + 24 + v
    usage = new - old
    bill = 35 + usage * 8
    q('water-bill-table', ['1l.5', '1l.3'], 'Reading a household bill', f'A household receives the following water bill. The tariff is supplied for this exercise.\n\n| Item | Value |\n|---|---:|\n| Previous meter reading | {old} m³ |\n| Current meter reading | {new} m³ |\n| Charge per m³ used | N$8.00 |\n| Monthly fixed charge | N$35.00 |\n| Credit already paid | N$50.00 |', [calc('Calculate the volume of water used.', f'{usage} m³', f'{new} − {old}', f'{usage} m³'), calc('Calculate the total charge before the credit.', f'N${bill:.2f}', f'{usage} × 8 + 35', f'N${bill:.2f}'), calc('Find the balance still payable.', f'N${bill - 50:.2f}', f'{bill} − 50', f'N${bill - 50:.2f}')])
    return out

def build_income_tax_table(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = rng.randint(0, 24)
    income = 120000 + 1200 * v
    tax = 7500 + 0.25 * (income - 100000)
    q('income-tax-table', ['1l.6', '1l.3'], 'Income tax', 'Use this fictional annual income-tax table for this exercise only.\n\n| Annual income (N$) | Annual tax |\n|---|---|\n| 0 to 50 000 | 0 |\n| Over 50 000 to 100 000 | 15% of income above 50 000 |\n| Over 100 000 to 150 000 | N$7 500 + 25% of income above 100 000 |\n| Over 150 000 | N$20 000 + 30% of income above 150 000 |', [calc(f'Petrus earns N${income} in one year. Calculate his annual tax.', f'N${tax:.2f}', f'7500 + 0.25({income} − 100000)', f'N${tax:.2f}'), calc('Calculate his average monthly income after this tax.', f'N${(income - tax) / 12:.2f}', f'({income} − {tax:g}) ÷ 12', f'N${(income - tax) / 12:.2f}'), part(f'Anna earns N${42000 + 100 * v} in one year. State her tax.', 'N$0', [step('Choose the matching income band', 'This income does not exceed N$50 000.', 'No tax is payable under the supplied table.')])])
    return out

def build_defining_sets_all_forms(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    v = rng.randint(0, 15)
    limit = 20 + 2 * v
    multiples = list(range(4, limit + 1, 4))
    q('defining-sets-all-forms', ['2main.1'], 'Defining sets', f'The universal set is the positive integers not exceeding {limit}.', [part('List the set A of multiples of 4 in this universal set.', '{' + ', '.join(map(str, multiples)) + '}', [step('List multiples inside the universal set', 'Only positive multiples not exceeding the stated limit belong.', '{' + ', '.join(map(str,multiples)) + '}')]), part('Write A in set-builder notation.', f'A=\\{{x:x=4n,\\ n\\in\\mathbb{{N}},\\ 1\\le n\\le {limit // 4}\\}}', [step('State a property that generates exactly A', 'Every element is four times a positive integer within the finite bound.', f'x=4n,\\quad1\\le n\\le{limit // 4}')], criteria=[(1, 'Any equivalent set-builder description that generates exactly A, with integer domain and finite bound.')]), part(f'Describe the set $B=\\{{2,4,6,\\ldots,{limit}\\}}$ in words.', f'The even positive integers not exceeding {limit}.', [step('Identify the common property and bound', 'A description must include both which numbers and the finite limit.', f'Even positive integers from 2 to {limit}.')])])
    return out

def build_set_operations_notation(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    start = rng.randint(1, 100)
    U, A, B, C = [list(range(start, start + n)) for n in (6, 3, 3, 5)]
    B, C = ([start + 1, start + 2], [start + 3, start + 4])
    sets = lambda xs: '\\{' + ','.join(map(str, xs)) + '\\}'
    common = f'Let $U={sets(U)}$, $A={sets(A)}$, $B={sets(B)}$ and $C={sets(C)}$.'
    q('set-operations-notation', ['2main.2'], 'Set notation', common, [part('Find $A\\cup C$.', sets(sorted(set(A) | set(C))), [step('Collect elements in either set', 'Union includes membership in at least one set.', sets(sorted(set(A) | set(C))))]), part('Find $A\\cap B$ and $A\\cap C$.', sets(B) + ';\\ \\varnothing', [step('Find common elements', 'Intersection includes only elements in both sets.', f'$A\\cap B={sets(B)}$; $A\\cap C=\\varnothing$')], 2, [(1, 'First intersection.'), (1, 'Empty second intersection.')]), part('Find $A\\prime$ and $n(A)$.', sets(U[3:]) + ';\\ 3', [step('Use the universal set', 'The complement contains elements of U outside A, and n(A) counts A.', f'$A\\prime={sets(U[3:])}$; $n(A)=3$')], 2, [(1, 'Complement relative to U.'), (1, 'Cardinality.')]), part(f'Complete using $\\in$ or $\\notin$: ${start + 1}\\ \\square\\ A$; ${start + 4}\\ \\square\\ A$.', '\\in;\\ \\notin', [step('Check membership', 'An element belongs exactly when it appears in the set.', f'{start + 1}\\in A;\\quad{start + 4}\\notin A')], 2, [(1, 'Correct membership.'), (1, 'Correct non-membership.')])])
    return out

def build_proper_subsets(seed,rng,requested_key=None):
    start=rng.randint(1,100)
    pool=list(range(start,start+7))
    A=set(rng.sample(pool,rng.randint(2,5)))
    cases=[set(A),set(rng.sample(sorted(A),len(A)-1)),set(pool)-A,
           set(A)|{next(x for x in pool if x not in A)},set()]
    B=rng.choice(cases)
    display=lambda values:r'\{'+','.join(map(str,sorted(values)))+r'\}'
    statements=[('B',B,'A',A,'subseteq'),('B',B,'A',A,'subset'),
                ('A',A,'B',B,'subseteq'),('A',A,'B',B,'subset'),('B',B,'A',A,'nsubseteq')]
    rng.shuffle(statements)
    parts=[]
    for lname,left,rname,right,relation in statements:
        inclusion=left<=right
        truth=left<right if relation=='subset' else not inclusion if relation=='nsubseteq' else inclusion
        positive='subseteq' if inclusion else 'nsubseteq'
        correction=lname+'\\'+positive+' '+rname
        answer='True' if truth else 'False; '+correction+(' (the sets are equal, so the inclusion is not proper)' if left==right else '')
        label=' (proper subset)' if relation=='subset' else ''
        parts.append(part('$'+lname+'\\'+relation+' '+rname+'$'+label,answer,
            [step('Check membership and, for proper inclusion, inequality',
                'A subset contains no element outside the containing set; a proper subset must also differ from it. A negated inclusion is true only when inclusion fails.',answer)]))
    return [question('proper-subsets',['2main.2'],'Subsets',
        f'Let $A={display(A)}$ and $B={display(B)}$. State whether each statement is true or false, and correct each false statement.',parts,variant=seed)]


def build_metric_quantities(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    t = rng.choice([n for n in range(2, 51) if math.isqrt(n) ** 2 != n])
    v = rng.randint(0, 15)
    q('metric-quantities', ['3main.1', '3main.2'], 'Metric quantities', 'A school is preparing its garden.', [calc(f'A path is ${2.4 + 0.1 * v:g}$ km long. Express this in metres.', f'{2400 + 100 * v} m', f'{2.4 + 0.1 * v:g} × 1000', f'{2400 + 100 * v} m', marks=1), calc(f'A bag of soil has mass ${12 + t}$ kg. Express this in grams.', f'{(12 + t) * 1000} g', f'{12 + t} × 1000', f'{(12 + t) * 1000} g', marks=1), calc(f'A board has area ${t}$ m². Express this in cm².', f'{t * 10000} cm²', f'{t} × 100²', f'{t * 10000} cm²'), calc(f'A container holds ${t}$ litres. Express this in cm³.', f'{t * 1000} cm³', f'{t} × 1000', f'{t * 1000} cm³', marks=1), calc(f'A storage box has volume ${t * 1000000}$ cm³. Express this in m³.', f'{t} m³', f'{t * 1000000} ÷ 100³', f'{t} m³')])
    return out

def build_bus_timetable(seed, rng, requested_key=None):
    depart = 60 * rng.randint(7, 15) + rng.randint(0, 59)
    first, wait, last = (rng.randint(8, 45), rng.randint(3, 18), rng.randint(15, 70))
    arrival = depart + first
    leave = arrival + wait
    finish = leave + last
    clock = lambda n: f'{n // 60:02d}:{n % 60:02d}'
    return [question('bus-timetable', ['3main.4', '3main.3'], 'Reading a timetable', f'The service runs on the same day.\n\n| Stop | Arrival | Departure |\n|---|---|---|\n| School | — | {clock(depart)} |\n| Library | {clock(arrival)} | {clock(leave)} |\n| Sports ground | {clock(finish)} | — |', [part('Write the departure time from the library.', clock(leave), [step('Read the library departure entry', 'The departure column records when the bus leaves, rather than when it arrives.', clock(leave))]), calc('Find the time spent at the library.', f'{wait} minutes', f'{clock(leave)} − {clock(arrival)}', f'{wait} minutes', marks=1), calc('Find the total time from leaving school to reaching the sports ground.', f'{first + wait + last} minutes', f'{first} + {wait} + {last}', f'{first + wait + last} minutes', marks=1), part('Write the arrival time at the sports ground using the 12-hour clock, including am or pm.', f'{finish // 60 % 12 or 12}:{finish % 60:02d} ' + ('am' if finish // 60 < 12 else 'pm'), [step('Convert the hour while preserving minutes', 'Midnight and noon use 12; hours after noon subtract 12 and use pm.', f'{finish // 60 % 12 or 12}:{finish % 60:02d} ' + ('am' if finish // 60 < 12 else 'pm'))])], variant=seed)]
BUILDERS = [build_classify_real_numbers, build_number_properties, build_squares_cubes_roots, build_fraction_quantity_context, build_six_way_conversions, build_ordering_and_relations, build_standard_form_four_operations, build_mixed_arithmetic, build_rounding_in_context, build_increase_decrease_ratio, build_calculator_brackets, build_check_calculator_answer, build_household_finance, build_types_of_earnings, build_water_bill_table, build_income_tax_table, build_defining_sets_all_forms, build_set_operations_notation, build_proper_subsets, build_metric_quantities, build_bus_timetable]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
