"""Bounded pilot catalogue. A renewal preserves the actual task and shape."""
import secrets
from fastapi import HTTPException
from .registry import generate_question

PILOT = {
 'hcf': {'topic':'Number properties','title':'Highest common factor','task':'hcf','recipe_id':'wb6131:legacy:nssco_number_classifications_properties:4'},
 'estimation': {'topic':'Estimation','title':'Estimate a calculation','task':'estimate','recipe_id':'wb6131:legacy:nssco_standard_form_estimates_approximations:3'},
 'time': {'topic':'Time','title':'Journey times','task':'duration_minutes','recipe_id':'wb6131:legacy:nssco_time_clocks_timetables:1'},
 'factor-common-number': {'topic':'Factorisation','title':'Common number factors','task':'common_number_factor','recipe_id':'wb6131:legacy:nssco_factorisation_basics:1'},
 'factor-common-letter': {'topic':'Factorisation','title':'Common number and letter factors','task':'common_letter_factor','recipe_id':'wb6131:legacy:nssco_factorisation_basics:2'},
 'factor-difference-squares': {'topic':'Factorisation','title':'Difference of squares','task':'difference_of_squares','recipe_id':'wb6131:legacy:nssco_factorisation_basics:3'},
 'factor-grouping': {'topic':'Factorisation','title':'Factorising by grouping','task':'factorise_by_grouping','recipe_id':'wb6131:legacy:nssco_factorisation_basics:4'},
 'factor-quadratic-positive': {'topic':'Factorisation','title':'Quadratics with positive terms','task':'factorise','recipe_id':'wb6131:legacy:nssco_factorising_quadratics:1'},
 'factor-quadratic-signed': {'topic':'Factorisation','title':'Quadratics with negative terms','task':'factorise','recipe_id':'wb6131:legacy:nssco_factorising_quadratics:2'},
 'factor-quadratic-leading': {'topic':'Factorisation','title':'Quadratics with a leading coefficient','task':'factorise','recipe_id':'wb6131:legacy:nssco_factorising_quadratics:3'},
 'factor-perfect-square-positive': {'topic':'Factorisation','title':'Positive perfect-square trinomials','task':'perfect_square_positive','recipe_id':'wb6131:legacy:nssco_factorisation_extension:1'},
 'factor-perfect-square-negative': {'topic':'Factorisation','title':'Negative-middle perfect-square trinomials','task':'perfect_square_negative','recipe_id':'wb6131:legacy:nssco_factorisation_extension:2'},
 'factor-common-quadratic': {'topic':'Factorisation','title':'Common factor then quadratic factors','task':'common_factor_quadratic','recipe_id':'wb6131:legacy:nssco_factorisation_extension:3'},
 'factor-grouping-four-variables': {'topic':'Factorisation','title':'Grouping with four variables','task':'group_four_variables','recipe_id':'wb6131:legacy:nssco_factorisation_extension:4'},
 'factor-common-multivariable': {'topic':'Factorisation','title':'Shared factors with different letters','task':'common_multivariable','recipe_id':'wb6131:legacy:nssco_factorisation_extension:5'},
 'factor-negative-leading': {'topic':'Factorisation','title':'Negative-leading quadratics','task':'negative_leading_quadratic','recipe_id':'wb6131:legacy:nssco_factorisation_extension:6'},
}


def fresh_question(key, previous=None, seen=()):
    if key not in PILOT:raise HTTPException(422,'Choose one of the available recipe cards.')
    recipe=PILOT[key];fingerprints=set(seen)
    if previous:fingerprints.add(previous['fingerprint'])
    for _ in range(256):
        q=generate_question(recipe['recipe_id'],secrets.randbelow(2**31))
        branch=q.get('source_branch',{})
        if branch.get('task')!=recipe['task']:continue
        if previous and branch!=previous.get('source_branch'):continue
        if q['fingerprint'] in fingerprints:continue
        q['pilot_key']=key
        return q
    raise HTTPException(409,'A new variation is not available right now. Please try again.')
