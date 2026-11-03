"""Read-only prepared visual question bank; no runtime diagram generation."""
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]/'data/flashcard_diagrams/v1'
PREFIX='yyeni-diagram:v1:'


@lru_cache(maxsize=1)
def catalog():
    return json.loads((ROOT/'manifest.json').read_text())


def read_asset(value):
    if not isinstance(value,str) or not re.fullmatch(re.escape(PREFIX)+r'[a-f0-9]{64}',value):
        raise ValueError('Invalid prepared diagram reference')
    digest=value[len(PREFIX):]
    data=(ROOT/(digest+'.png')).read_bytes()
    if not 0<len(data)<=149000 or not data.startswith(b'\x89PNG\r\n\x1a\n') or hashlib.sha256(data).hexdigest()!=digest:
        raise ValueError('Prepared diagram bytes differ from saved identity')
    return data
