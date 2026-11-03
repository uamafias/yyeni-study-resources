"""Authored, question-bound prompts. Never derive hints from the final answer."""
import re
from services.math_generators import generate_problem
from services.math_generators.algebra_content import _power, _term


def hints_for(question):
    source=question.get('grading_contract',{}).get('source_marking_contract')
    if not source:return []
    problem=generate_problem(source['generator_id'],source['seed'],source['level'])
    # An old snapshot must never receive the numbers from a changed generator.
    if problem.question!=source['question'] or problem.generator_version!=source['generator_version']:return []
    machine=problem.machine;key=question.get('pilot_key')
    if key and key.startswith('factor-'):
        expression=re.search(r'\$([^$]+)\$',problem.question)
        if not expression:return []
        original=expression.group(1);task=machine['task']
        if task.startswith('perfect_square_'):
            return [f'Look at the first and last terms of ${original}$. What quantities square to give those terms?',
                'Double the product of those two quantities. Compare its size with the middle term, then use the sign shown in the question.',
                'Write a single squared bracket. Use the middle term to choose the sign, then expand to check all three terms.']
        if task in ('common_factor_quadratic','negative_leading_quadratic'):
            return [f'In ${original}$, look for a number that divides all three number coefficients. The shared positive number may be 1.',
                ('Take out a negative factor so the first term inside is positive. Divide every term by that factor.' if task=='negative_leading_quadratic' else 'Keep the largest shared number outside a bracket and divide every term by it.'),
                'Check the signs in the quadratic factors. Keep the outside number in the final product and expand to check the whole expression.']
        if task=='group_four_variables':
            return [f'In ${original}$, group the first two terms and the last two terms.',
                'Each pair has a shared letter factor. Take it out, together with any shared number, so the same two-term bracket remains.',
                'Take the matching bracket out as a whole factor. The outside terms form the other bracket.']
        if task=='common_multivariable':
            return [f'Compare the terms in ${original}$. Which number and letter powers divide both terms?',
                'Take the complete shared factor outside a bracket. Divide both original terms by it, keeping their different remaining letters.',
                'Keep the signs inside the bracket and expand your product to check both original terms.']
        if task in ('common_number_factor','common_letter_factor'):
            first=machine['g']*machine['a'];second=machine['sign']*machine['g']*machine['b']
            prompts=[f'Look at the number coefficients ${first}$ and ${second}$ in ${original}$. What is the largest positive whole number that divides both?']
            if task=='common_letter_factor':
                v=machine['var'];lo=machine['k'];hi=lo+machine['j']
                prompts.append(f'Compare ${_power(v,hi)}$ and ${_power(v,lo)}$. What is the largest power of ${v}$ that divides both terms?')
            prompts.append(f'Take the shared factor outside a bracket. Divide every term of ${original}$ by it to find what belongs inside, keeping the signs.')
            return prompts
        if task=='difference_of_squares':
            return [f'Check ${original}$ for a shared number factor before looking for squares.',
                'After taking out any shared factor, find the two quantities whose squares give the remaining terms.',
                'Write two brackets: their difference and their sum. Keep any outside factor, then expand to check.']
        if task=='factorise_by_grouping':
            return [f'In ${original}$, group the first two terms and the last two terms.',
                'Take out a common factor from each pair. If a group starts negative, check whether taking out a negative factor gives matching brackets.',
                'Treat the matching bracket as one whole factor. Write it once, with the remaining outside terms in another bracket.']
        if task=='factorise':
            a,b,c=machine['quadratic'];product=a*c
            return [f'For ${original}$, look for two integers with product ${product}$ and sum ${b}$. Check both conditions and their signs.',
                f'Split the ${_term(b,"x")}$ term using those two integers, then group and factor the pairs.' if a!=1 else
                'Put the two integers into brackets with the variable. Their product and sum must reconstruct the original expression.',
                'Take out the matching bracket and write the complete product. Expand to check the first, middle and constant terms.' if a!=1 else
                'Expand your brackets to check every term. The answer should be a product of brackets, rather than values of the variable.']
        return []
    if key=='hcf' and machine['task']=='hcf':
        a,b=machine['a'],machine['b']
        start=(f'Look at the given prime factorisations of ${a}$ and ${b}$. Which primes appear in both?'
               if problem.question.startswith('Given that') else
               f'Write ${a}$ and ${b}$ as products of prime numbers. Which primes appear in both?')
        return [start,f'For each prime shared by ${a}$ and ${b}$, choose the smaller power. Multiply the values you choose.']
    if key=='estimation' and machine['task']=='estimate':
        a,b,c=machine['numbers'];expression=re.search(r'\$([^$]+)\$',problem.question)
        if not expression:return []
        last={
            'mul_div':f'Multiply the rounded versions of ${a}$ and ${b}$ first, then divide by the rounded version of ${c}$.',
            'add_div':f'Add the rounded versions of ${a}$ and ${b}$ first, then divide by the rounded version of ${c}$.',
            'div_mul':f'Multiply the rounded versions of ${b}$ and ${c}$ on the bottom first. Divide the rounded version of ${a}$ by that product.',
        }.get(machine['shape'])
        if not last:return []
        return [f'Start with ${a}$, ${b}$ and ${c}$. Round each to one significant figure by checking the digit after its first non-zero digit.',
                f'Rewrite ${expression.group(1)}$ using your rounded numbers. Keep the operations in the same places.',last]
    if key=='time' and machine['task']=='duration_minutes':
        start,end=machine['start'],machine['end']
        hour=int(start.split(':')[0]);boundary=f'{(hour+1)%24:02d}:00'
        return [f'Start at ${start}$. How many minutes pass before ${boundary}$?',
                f'Now count the minutes from ${boundary}$ to ${end}$.',
                f'Add the two amounts of time to find the whole journey from ${start}$ to ${end}$. Give your answer in minutes.']
    return []


def revealed(activity):
    return [message['content'] for message in activity.messages or []
            if message.get('kind')=='practice_hint' and message.get('question_position')==activity.position]


METHOD_TITLES={
 'hcf':'Finding the highest common factor',
 'estimation':'Estimating a calculation',
 'time':'Finding an elapsed time',
 'factor-common-number':'Taking out a common number factor',
 'factor-common-letter':'Taking out a common number and letter factor',
 'factor-common-multivariable':'Taking out shared number and letter factors',
 'factor-difference-squares':'Using the difference of two squares',
 'factor-grouping':'Factorising by grouping',
 'factor-grouping-four-variables':'Factorising by grouping',
 'factor-quadratic-positive':'Finding two numbers to factorise a quadratic',
 'factor-quadratic-signed':'Finding two numbers to factorise a quadratic',
 'factor-quadratic-leading':'Splitting the middle term to factorise a quadratic',
 'factor-perfect-square-positive':'Recognising a perfect-square trinomial',
 'factor-perfect-square-negative':'Recognising a perfect-square trinomial',
 'factor-common-quadratic':'Taking out a common factor, then factorising the quadratic',
 'factor-negative-leading':'Taking out a negative factor, then factorising the quadratic',
}

def method_title(question):
    key=question.get('pilot_key')
    if key in METHOD_TITLES:return METHOD_TITLES[key]
    return 'A guide to this method'
