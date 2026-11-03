"""One read-only feedback projection for learner and authorised staff views."""
from copy import deepcopy
from .content_format import display_content

PUBLIC_FIELDS=('answer','photo_ids','grading','submitted_at','mark','max_mark','feedback','grading_breakdown','flag_for_teacher','flag_reason','review_reason','repair_steps','hint_count')

def feedback_payload(answer,maximum=None):
    if answer is None:return None
    result={key:deepcopy(value) for key,value in answer.items() if key in PUBLIC_FIELDS}
    if maximum is not None:result['max_mark']=maximum
    for step in result.get('repair_steps',[]):step['result_content']=display_content(step['result'])
    return result
