#!/usr/bin/env python3
"""The single source of every published filename.

RS-47's lesson applied to file names: anything the build can derive from data it already
holds is derived, never typed. Before this module existed, `render_notes.py` fell back to
`notes-<number>.md` and each author chose their own name, so one subject shipped
`notes-1.1.md` beside `notes-1.2-business-structure.md` and a human had to look up what
4.3 was. The topic title is in the contract; the name comes from there.

    from naming import topic_stem, notes_filename, flashcards_filename
    topic_stem('4.3', 'Capacity utilisation and outsourcing')
    -> '4.3-capacity-utilisation-and-outsourcing'
"""
import re
import unicodedata


def slug(title):
    """A filename-safe, lowercase, hyphenated form of a human title."""
    t = unicodedata.normalize('NFKD', title or '').encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
    return t or 'untitled'


def topic_stem(topic_id, title):
    """`<number>-<slug>` - the shared stem every file for this topic is named from."""
    return '%s-%s' % (topic_id, slug(title))


def notes_filename(topic_id, title):
    return '%s.md' % topic_stem(topic_id, title)


def flashcards_filename(topic_id, title):
    return '%s-flashcards.json' % topic_stem(topic_id, title)


def topic_label(topic_id, title):
    """`4.3 Capacity utilisation and outsourcing` - for headings and manifests."""
    return ('%s %s' % (topic_id, title or '')).strip()
