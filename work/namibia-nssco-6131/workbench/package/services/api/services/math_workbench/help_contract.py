"""Answer-free, question-bound help for every authored Workbench recipe.

Only operation names are reused from authored working. Evaluated results,
reference answers, grading achievements and AI feedback are never inputs to
this projection. Generic calculator steps use separately authored principles.
"""
import hashlib,json,re
from .core import CALC_REASONS

VERSION=2
TITLE_PLANS={
 'number-properties':['Prime factors and the highest common factor','Prime factors and the lowest common multiple','Testing prime divisors','Recognising square numbers','Recognising cube numbers'],
 'squares-cubes-roots':['Squaring a number','Cubing a number','Finding a square root','Finding a cube root'],
 'fraction-quantity-context':['Finding a fraction of a quantity','Finding the amount left','Converting a fraction'],
 'six-way-conversions':['Converting a decimal to a fraction','Converting a fraction to a decimal','Converting a fraction to a percentage','Converting a percentage to a fraction','Converting a percentage to a decimal','Converting a decimal to a percentage'],
 'standard-form-four-operations':['Adding in standard form','Subtracting in standard form','Multiplying in standard form','Dividing in standard form'],
 'mixed-arithmetic':['Order of operations','Decimal place values','Multiplication and division','Adding and subtracting fractions','Dividing by a fraction'],
 'rounding-in-context':['Dividing then rounding up','Choosing a sensible rounding direction'],
 'increase-decrease-ratio':['Increasing in a ratio','Decreasing in a ratio'],
 'calculator-brackets':['Using brackets on a calculator'],
 'check-calculator-answer':['Estimating a product','Checking the size of a result','Checking with the original values'],
 'household-finance':['Percentage profit','Percentage loss','Percentage discount','Simple interest','Compound interest'],
 'types-of-earnings':['Converting monthly pay to yearly pay','Calculating piece-work pay','Combining wages and commission'],
 'water-bill-table':['Finding metered usage','Applying a tariff and fixed charge','Subtracting credit already paid'],
 'income-tax-table':['Applying the correct tax band','Finding monthly pay after tax','Reading a tax band'],
 'metric-quantities':['Converting length units','Converting mass units','Converting area units','Converting capacity and volume','Converting volume units'],
 'bus-timetable':['Reading a timetable','Finding a waiting time','Finding a whole journey time','Converting to a twelve-hour clock'],
 'cube-and-prism-measures':['Cross-sectional area times length','Adding the areas of exposed faces','Cube surface area and volume'],
 'sphere-cone-pyramid-measures':['Sphere surface area and volume','Cone slant height and surface area','Pyramid volume','Regular pyramid surface area'],
 'symmetry-properties':['Using equal chord halves','Using equal sides and equal base angles','Using the symmetry of a rhombus'],
 'line-plane-angle':['Using the base right triangle','Using a vertical right triangle','Using the line’s projection onto the plane'],
 'factorising-required-forms':['Taking out a common factor','Factorising by grouping','Using the difference of two squares','Recognising a perfect-square trinomial','Factorising a quadratic'],
 'polynomial-operations':['Adding like powers','Subtracting every term','Expanding and collecting like powers'],
 'all-index-types':['Using a zero index','Using a negative index','Using a fractional index','Combining equal bases'],
 'geometric-nth-term-and-sum':['Finding a geometric term','Using a finite geometric sum','Evaluating a finite geometric sum'],
 'household-spending-chart':['Reading the correct bar','Adding the category amounts','Expressing one amount as a fraction of the total'],
 'averages-and-their-purposes':['Finding the mean','Finding the median and mode','Finding the range','Choosing an average with an extreme value','Choosing an average for a purpose'],
 'percentiles-and-interpretation':['Finding and interpreting the median','Finding the quartiles','Finding the interquartile range','Finding and interpreting a percentile'],
 'relative-frequency-experiment':['Finding relative frequency','Estimating an expected count','Interpreting an experimental estimate'],
}
EXTRA_PRINCIPLES={
 'sphere-cone-pyramid-measures':{3:'Find a triangular face’s slant height using the vertical height and half a base side. Add the four triangular faces to the square base.'},
 'rounding-in-context':{0:'Divide the required total length by the length of one panel. Choose a whole number of panels that covers the entire length.'},
 'calculator-brackets':{0:'Keep each numerator and denominator together with brackets. Evaluate the complete expression before rounding.'},
 'household-spending-chart':{1:'Add the requested categories using the chart scale.',2:'Write the requested category amount over the whole budget and simplify.'},
 'averages-and-their-purposes':{0:'Add all the observations and divide by the number of observations.',2:'Subtract the smallest observation from the largest.'},
 'percentiles-and-interpretation':{2:'Subtract the lower quartile from the upper quartile. Keep the time units.'},
 'relative-frequency-experiment':{0:'Divide the number of successes by the number of trials.',1:'Multiply the estimated probability by the new number of trials.'},
 'line-plane-angle':{2:'Find the projection of the sloping line onto the base. Use the vertical right triangle to choose a trigonometric ratio.'},
}
ACRONYMS={'HCF':'highest common factor','LCM':'lowest common multiple','IQR':'interquartile range',
 'SSS':'three corresponding equal sides','SAS':'two corresponding equal sides and the included angle','ASA':'two corresponding equal angles and a side','AA':'two corresponding equal angles'}

def plain(value):
    for short,long in ACRONYMS.items():value=re.sub(r'\b'+short+r'\b',long,value)
    return value.strip().rstrip('.')+'.'


def principles(key,index):
    extra=EXTRA_PRINCIPLES.get(key,{})
    if index in extra:return extra[index]
    entries=CALC_REASONS.get(key,[])
    return entries.get(index) if isinstance(entries,dict) else entries[index] if index<len(entries) else None


def build_help(question,special_prompts=None,special_title=None):
    """Keep hints bound to the exact displayed prompt, including old snapshots."""
    key=question['recipe_id'].removeprefix('wb6131:');parts=[]
    for index,part in enumerate(question['parts']):
        operations=[]
        for step in part['worked_steps']:
            action=step['action']
            if action=='Calculate the requested quantity':
                action=principles(key,index)
                if not action:raise ValueError(f'No answer-free calculation guide: {key} part {index}')
            # Only high-level authored operations enter the help. Result fields
            # are not read, even if a caller supplies an alternative solution.
            prompt=plain(action)
            if prompt not in operations:operations.append(prompt)
        titles=TITLE_PLANS.get(key,[])
        method=special_title if special_title and len(question['parts'])==1 else titles[index] if index<len(titles) else plain(part['worked_steps'][0]['action']).rstrip('.')
        method=plain(method).rstrip('.')
        if special_prompts and len(question['parts'])==1:operations=list(special_prompts)
        # Instance context is copied solely from the displayed question. It can
        # contain given or requested values, never a computed solution field.
        context=' '.join(filter(None,(question.get('stem',''),part['prompt'])))
        # Currency signs must never be paired as Markdown math delimiters.
        maths_source=re.sub(r'(?<=[A-Za-z0-9])\$(?=\d)','¤',context)
        maths=re.findall(r'(?<!\\)\$([^$\n]+)(?<!\\)\$',maths_source)
        numeric=bool(re.search(r'\d',context))
        if not special_prompts and operations:
            if maths:operations[0]='For '+', '.join('$'+m+'$' for m in maths[:2])+':\n\n'+operations[0]
            elif numeric:
                # Keep amounts, times and units bound to the displayed part;
                # given values may live in its shared stem or table.
                values=re.findall(r'(?<![A-Za-z])(?:N\$)?-?\d+(?:[.,:]\d+)*(?:%|°)?',context)
                operations[0]='Use the given values: '+', '.join(dict.fromkeys(values))+'.\n\n'+operations[0]
        parts.append({'part_id':chr(97+index),'method':method,'prompts':operations})
    prompts=[]
    for part in parts:
        for index,prompt in enumerate(part['prompts']):
            label=f"**Part ({part['part_id']}): {part['method']}**\n\n" if len(parts)>1 and index==0 else ''
            prompts.append(label+prompt)
    bound={'recipe_id':question['recipe_id'],'stem':question.get('stem',''),'parts':[p['prompt'] for p in question['parts']]}
    return {'version':VERSION,'question_fingerprint':hashlib.sha256(json.dumps(bound,sort_keys=True).encode()).hexdigest(),
        'title':special_title or (parts[0]['method'] if len(parts)==1 else 'Methods for this question'),
        'parts':parts,'prompts':prompts,'source':'authored_operations_and_displayed_inputs; no solution results'}
