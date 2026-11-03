"""Evidence-only staff projections. Never include an unsubmitted question."""
from datetime import datetime
import math
from .pilot import PILOT
from .registry import learner_question


def timestamp(value):
    return value.isoformat()+'Z' if value else None


def effective_status(activity):
    if activity.mode=='test' and activity.status=='active' and not getattr(activity,'timer_paused_at',None) and activity.deadline_at and activity.deadline_at<=datetime.utcnow():
        return 'completed'
    return activity.status


def reliable_mark(answer,maximum):
    value=answer.get('mark')
    if answer.get('grading')!='done' or isinstance(value,bool) or not isinstance(value,(float,int)):
        return None
    return float(value) if math.isfinite(value) and 0<=value<=maximum else None


def submitted(activity):
    for index,question in enumerate(activity.questions or []):
        answer=(activity.answers or {}).get(str(index))
        if isinstance(answer,dict) and (str(answer.get('answer','')).strip() or answer.get('photo_ids')):
            yield index,question,answer


def round_summary(activity):
    marks=[reliable_mark(a,q['proposed_total_marks']) for _,q,a in submitted(activity)]
    return {'id':activity.id,'mode':activity.mode,'status':effective_status(activity),
        'started_at':timestamp(activity.started_at),'completed_at':timestamp(activity.completed_at),
        'submitted_count':len(marks),'question_count':len(activity.questions or []),
        'score':sum(mark for mark in marks if mark is not None),
        'max_marks':sum(q['proposed_total_marks'] for q in activity.questions or []) if activity.mode=='test' else sum(q['proposed_total_marks'] for _,q,_ in submitted(activity)),
        'unmarked_count':sum(mark is None for mark in marks),
        'unanswered_count':len(activity.questions or [])-len(marks) if activity.mode=='test' and effective_status(activity)=='completed' else 0}


def history_entry(activity,deck,name,lesson_title):
    from .guidance import saved_solution
    answers=[]
    for index,question,answer in submitted(activity):
        maximum=question['proposed_total_marks']
        answers.append({'position':index,'recipe_key':question.get('pilot_key'),
            'question':learner_question(question),'answer':answer['answer'],
            'mark':reliable_mark(answer,maximum),'max_marks':maximum,
            'grading':answer.get('grading'),'feedback':answer.get('feedback') or '', 'repair_steps':answer.get('repair_steps',[]), 'hint_count':answer.get('hint_count',0),
            'needs_review':bool(answer.get('flag_for_teacher')),**saved_solution(question,answer)})
    return {**round_summary(activity),'deck_id':deck.id,'deck_title':deck.title,
        'learner_id':deck.learner_id,'learner_name':name,'lesson_title':lesson_title,'answers':answers}


def recent_difficulties(rows):
    """Rows are (activity, deck, name). Partial marks are not labelled failures."""
    groups={}
    for activity,deck,name in rows:
        for _,question,answer in submitted(activity):
            key=question.get('pilot_key','unknown');identifier=(deck.learner_id,key,activity.mode)
            group=groups.setdefault(identifier,{'learner_id':deck.learner_id,'learner_name':name,
                'recipe_key':key,'recipe_title':PILOT.get(key,{}).get('title',key),'mode':activity.mode,
                'marked_answers':0,'below_full_marks':0,'unmarked_answers':0,'review_flags':0,
                'marks_earned':0,'marks_available':0,'latest_feedback':''})
            maximum=question['proposed_total_marks'];mark=reliable_mark(answer,maximum)
            group['review_flags']+=bool(answer.get('flag_for_teacher'))
            if mark is None:group['unmarked_answers']+=1;continue
            group['marked_answers']+=1;group['marks_earned']+=mark;group['marks_available']+=maximum
            if mark<maximum:
                group['below_full_marks']+=1
                if not group['latest_feedback']:group['latest_feedback']=answer.get('feedback') or ''
    return sorted((g for g in groups.values() if g['below_full_marks'] or g['unmarked_answers'] or g['review_flags']),
        key=lambda g:(-g['below_full_marks'],-g['unmarked_answers'],g['learner_name'],g['recipe_title']))


def test_progress(activities, recipe_keys):
    """Replay completed tests once per recipe per round; practice never moves boxes."""
    from services.flashcard_grading_service import box_decision_for_mark
    progress={key:{'recipe_key':key,'box':1,'tests':0,'due_date':None,'pending_marking':False} for key in recipe_keys}
    for activity in sorted(activities,key=lambda a:(a.completed_at or a.started_at,a.id)):
        if activity.mode!='test' or effective_status(activity)!='completed':continue
        groups={}
        for index,question in enumerate(activity.questions or []):
            key=question.get('pilot_key')
            if key not in progress:continue
            group=groups.setdefault(key,{'earned':0,'maximum':0,'submitted':False,'pending':False})
            maximum=question['proposed_total_marks'];group['maximum']+=maximum
            answer=(activity.answers or {}).get(str(index))
            if not answer:continue
            group['submitted']=True
            mark=reliable_mark(answer,maximum)
            if mark is None:group['pending']=True
            else:group['earned']+=mark
        for key,group in groups.items():
            state=progress[key]
            if group['pending']:
                state['pending_marking']=True
                continue
            if not group['submitted'] or not group['maximum']:continue
            decision=box_decision_for_mark(group['earned'],state['box'],
                today=(activity.completed_at or activity.started_at).date(),max_mark=group['maximum'],marking_mode='exam')
            state.update(box=decision.new_box,tests=state['tests']+1,due_date=decision.due_date.isoformat())
    return list(progress.values())
