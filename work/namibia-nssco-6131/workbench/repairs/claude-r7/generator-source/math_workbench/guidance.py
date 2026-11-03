"""Question-bound tutor evidence and canonical worked-example presentation."""
from services.math_workbench.registry import learner_question
import re


def question_evidence(question, answer=None):
    answer=answer or {}
    return {'question':learner_question(question),
            'submitted_work':answer.get('answer'),'photo_count':len(answer.get('photo_ids',[])),
            'marking':{key:answer[key] for key in ('grading','mark','max_mark','feedback','grading_breakdown','repair_steps','hint_count','flag_for_teacher','flag_reason','review_reason') if key in answer},
            'reference':question['parts']}


def conversation_for_question(messages, position, question_count):
    # Old untagged messages are attributable only before the first renewal.
    result=[]
    for message in messages:
        prior=message.get('question_position')
        if prior is not None and prior>position:continue
        if prior is None and question_count>1:continue
        result.append({**message,'content':(f'Earlier practice question {prior+1}, not the current question: ' if prior is not None and prior<position else '')+message['content']})
    return result[-12:]


def equation(value):
    from services.math_generators.prose_formatting import markdown_result
    source=str(value)
    rows=re.split(r'\\{2,}(?=\s|$)',source) if r'\begin{' not in source else [source]
    return '\n\n'.join(markdown_result(row) for row in rows if row.strip())


def example_snapshot(question):
    from .content_format import display_content
    from copy import deepcopy
    parts=deepcopy(question['parts'])
    for part in parts:
        part['reference_answer_content']=part.get('reference_answer_content') or display_content(part['reference_answer'])
        for step in part['worked_steps']:step['result_content']=step.get('result_content') or display_content(step['result'])
    return {'stem':question['stem'],'parts':[{key:part[key] for key in ('prompt','worked_steps','reference_answer','reference_answer_content')} for part in parts]}


def readable_example_message(message):
    if message.get('kind')!='worked_example':return message
    result={key:value for key,value in message.items() if key!='example'}
    if message.get('example'):
        result['content']=worked_example_text(message['example'])
        result['example_snapshot']=message['example']
    else:
        # Repair the old saved examples at presentation time; retain original evidence.
        result['content']=re.sub(r'\\\((.*?)\\\)',lambda match:'\n\n'+equation(match[1])+'\n\n',message['content'],flags=re.S)
    return result


def worked_example_text(question):
    lines=[question['stem']]
    for part in question['parts']:
        lines.append(part['prompt'])
        for index,step in enumerate(part['worked_steps'],1):
            maths=equation(step['result']).replace('\n','\n   ')
            lines.append(f"{index}. **{step['action']}**\n\n   {step['reason']}\n\n   {maths}")
        # The final worked row already states the answer on authored programs.
        last=part['worked_steps'][-1]['result'] if part['worked_steps'] else ''
        def comparable(value):return re.sub(r'\s+','',equation(value)).strip('$')
        if comparable(last)!=comparable(part['reference_answer']):
            lines.append(f"Answer: {equation(part['reference_answer'])}")
    return '\n\n'.join(lines)


def displayed_example_evidence(activity, context):
    """Resolve learner-selected example pointers against server snapshots only."""
    context=context or {}
    position=activity.position
    if context.get('kind')=='requested':
        example=next((m.get('example') for m in reversed(activity.messages) if m.get('kind')=='worked_example' and m.get('question_position')==position),None)
    else:
        example=activity.questions[0].get('practice_example')
    if not example:return None
    snapshot=example_snapshot(example)
    steps=[step for part in snapshot['parts'] for step in part.get('worked_steps',[])]
    index=context.get('step',0)
    if not isinstance(index,int) or index<0 or index>len(steps):return None
    return {'example':snapshot,'display':'exam-style answer' if index==len(steps) else f'Step {index+1}',
            'current_step':steps[index] if index<len(steps) else None}


def saved_solution(question, answer):
    """Only frozen generated solution data; never infer a final answer from AI repairs."""
    if not answer or answer.get('grading')!='done':return {}
    from copy import deepcopy
    from .review_policy import question_notice
    from .content_format import display_content
    parts=[]
    for part in question['parts']:
        saved={key:deepcopy(part[key]) for key in ('part_id','prompt','reference_answer','worked_steps') if key in part}
        saved['reference_answer_content']=deepcopy(part.get('reference_answer_content') or display_content(part['reference_answer']))
        for step in saved['worked_steps']:
            step['result_content']=step.get('result_content') or display_content(step['result'])
        parts.append(saved)
    return {'solution_review_note':question_notice(question),'solution_parts':parts}
