"""Small cached metadata lookup for the Workbench video preview."""
import re
import time
from threading import Lock
import requests
import isodate
from settings import get_youtube_api_key

_cache = {}
_lock = Lock()


def video_details(identifier):
    if not isinstance(identifier,str) or not re.fullmatch(r'[A-Za-z0-9_-]{11}',identifier):
        return {}
    with _lock:
        cached=_cache.get(identifier)
        if cached and cached[0]>time.monotonic():return dict(cached[1])
    key=get_youtube_api_key(required=False)
    if not key:return {}
    details={}
    try:
        response=requests.get('https://www.googleapis.com/youtube/v3/videos',
            params={'part':'snippet,contentDetails','id':identifier,'key':key},timeout=10)
        response.raise_for_status()
        items=response.json().get('items',[])
        if items:
            item=items[0]
            duration=item.get('contentDetails',{}).get('duration')
            seconds=int(isodate.parse_duration(duration).total_seconds()) if duration else 0
            if seconds>0:details['duration_seconds']=seconds
            image=item.get('snippet',{}).get('thumbnails',{}).get('high',{}).get('url','')
            if image.startswith('https://i.ytimg.com/'):
                details['thumbnail_url']=image
    except (requests.RequestException,ValueError,TypeError,AttributeError,OverflowError,isodate.ISO8601Error):
        # Never log request URLs: YouTube credentials are query parameters.
        pass
    with _lock:
        if len(_cache)>=256:
            oldest=min(_cache,key=lambda key:_cache[key][0]);_cache.pop(oldest,None)
        _cache[identifier]=(time.monotonic()+(3600 if details else 60),dict(details))
    return details


def preview(result):
    video=result.get('video')
    if not video:return result
    return {**result,'video':{**video,**video_details(video.get('id'))}}
