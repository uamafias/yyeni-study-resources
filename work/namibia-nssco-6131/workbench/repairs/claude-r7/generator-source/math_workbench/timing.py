"""Server-authoritative question and review clocks. Caller holds learner/activity locks."""
from datetime import datetime, timedelta

REVIEW_SECONDS=120


def advance(activity, at):
    activity.position+=1
    activity.question_started_at=at
    activity.deadline_at=at+timedelta(seconds=activity.remaining_seconds or 0)
    activity.timer_paused_at=None
    activity.remaining_seconds=None
    activity.feedback_review_until=None


def expire(activity, at):
    if activity.mode!='test' or activity.status!='active':return
    until=getattr(activity,'feedback_review_until',None)
    if activity.timer_paused_at and until and until<=at:
        if activity.position+1<len(activity.questions):advance(activity,until)
        else:
            activity.deadline_at=until+timedelta(seconds=activity.remaining_seconds or 0)
            activity.timer_paused_at=None
            activity.remaining_seconds=None
            activity.feedback_review_until=None
    if not activity.timer_paused_at and activity.deadline_at and activity.deadline_at<=at:
        activity.status='completed';activity.completed_at=activity.deadline_at


def elapsed(activity, at):
    start=getattr(activity,'question_started_at',None) or activity.started_at
    saved=(getattr(activity,'answers',None) or {}).get(str(activity.position),{})
    submitted=saved.get('submitted_at')
    stop=datetime.fromisoformat(submitted.rstrip('Z')) if submitted else activity.timer_paused_at or at
    return max(0,int((stop-start).total_seconds()))
