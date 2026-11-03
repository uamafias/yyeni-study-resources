"""Workbench-specific explanation standard; exam marks keep their frozen criteria."""

def system_prompt(base):
    # Recall's stricter practice conventions are not examination-board rules.
    start=base.index('RECALL-ONLY PRACTICE POLICY')
    end=base.index('Explain each deduction',start)
    base=base[:start]+base[end:]
    base=base.replace('A separate prepared full solution is displayed below; do not duplicate it in feedback, reasoning and every justification.',
        'The learner sees your summary and repair_steps; do not assume a full solution is already displayed.')
    return base+('\nEXAM POLICY: Require a particular solving method only where the question explicitly requests it. '
        'Otherwise accept mathematically valid alternative methods. Withhold only awards requiring the specified method; '
        'retain independent accuracy credit where the frozen memo authorises it. Do not invent a universal no-working penalty. '
        '\nWORKBENCH FEEDBACK STANDARD: feedback recognises valid progress and identifies the first consequential error supported by the submitted evidence. '
        'Keep feedback to a brief recognition of valid progress and the first error; do not duplicate calculations or the full solution already in repair_steps. Never invent praise or use filler such as you gave an answer. '
        'For a reliably marked answer below full credit, also provide repair_steps: an ordered array of objects with action, reason and result. '
        'Each meaningful step makes one consequential mathematical action or decision explicit, explains why it follows, and shows the result using the actual question values. '
        'Group routine calculations; separate changes of method, principle or representation. Use as many steps as the demand needs; step count is not mark count. '
        'Start from the first evidenced error or missing required achievement and carry the repair to the requested result. Accept valid alternative methods. '
        'Do not invent an error from the score alone or repeat generic advice as steps. For full credit use an empty repair_steps array. '
        'For genuinely unresolved evidence, request clarification in feedback, flag review and leave repair_steps empty rather than guessing. '
        'Write plain learner-facing language. Put no step numbers in action/reason/result: the interface labels them. Return repair_steps in the same JSON as the mark.')


def extend_schema(schema):
    schema['properties']['repair_steps']={'type':'array','items':{'type':'object','properties':{key:{'type':'string'} for key in ('action','reason','result')},'required':['action','reason','result']}}
    schema['required'].append('repair_steps')
    return schema


def validate_steps(payload, validated, clean):
    steps=payload.get('repair_steps')
    if not isinstance(steps,list):raise ValueError('Missing ordered repair steps')
    full=validated['marks_awarded']==float(payload['max_marks'])
    unresolved=validated['needs_human_review']
    if full and steps:raise ValueError('Correct work must not receive correction steps')
    if not full and not unresolved and not steps:raise ValueError('Incomplete answer requires meaningful repair steps')
    result=[]
    for step in steps:
        if not isinstance(step,dict):raise ValueError('Invalid repair step')
        item={}
        for key in ('action','reason','result'):
            value=step.get(key)
            if not isinstance(value,str) or not value.strip():raise ValueError('Repair step requires action, reason and result')
            text,invalid=clean(value,key)
            if invalid or not text:raise ValueError('Unreadable repair step')
            item[key]=text
        result.append(item)
    return result
