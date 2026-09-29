"""C-43 / RS-48: a task answered from a practice text names it, and the text exists, declares itself
original and sits inside its stated length. Added with CR-004 (2026-09-29)."""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'checks'))
import yyeni_checks as Y  # noqa: E402


def _build(tmp_path, body_words=520, original=True, cite=True, declared=True):
    td = tmp_path / 'topics' / '1.3'
    (td / 'texts').mkdir(parents=True)
    fm = 'text_id: TXT-X\n' + ('original: true\n' if original else '') + ('words_min: 500\nwords_max: 650\n' if declared else '')
    (td / 'texts' / 'TXT-X.md').write_text('---\n' + fm + '---\n' + ' '.join(['word'] * body_words))
    item = {'item_id': 'I1', 'context': {'text_id': 'TXT-X'} if cite else {}}
    return types.SimpleNamespace(topic_dir=str(td), topic_id='1.3', items=[item])


def test_passes_when_declared_original_and_in_length(tmp_path):
    assert Y.c43(_build(tmp_path))[0] == 'pass'


def test_fails_when_too_short(tmp_path):
    assert Y.c43(_build(tmp_path, body_words=300))[0] == 'fail'


def test_fails_when_not_declared_original(tmp_path):
    assert Y.c43(_build(tmp_path, original=False))[0] == 'fail'


def test_fails_when_length_undeclared(tmp_path):
    assert Y.c43(_build(tmp_path, declared=False))[0] == 'fail'


def test_warns_on_an_orphan_text(tmp_path):
    assert Y.c43(_build(tmp_path, cite=False))[0] == 'warn'


def test_fails_when_cited_text_is_missing(tmp_path):
    b = _build(tmp_path)
    os.remove(os.path.join(b.topic_dir, 'texts', 'TXT-X.md'))
    assert Y.c43(b)[0] == 'fail'


def test_not_run_without_texts(tmp_path):
    b = types.SimpleNamespace(topic_dir=str(tmp_path), topic_id='1.1', items=[{'item_id': 'I1', 'context': {}}])
    assert Y.c43(b)[0] == 'not_run'
