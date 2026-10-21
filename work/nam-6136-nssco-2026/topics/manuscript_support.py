"""Assemble explicit original lesson paragraphs and item-specific manuscripts.

This supplies no subject matter or question wording. Guidance is supplied per
item; required labels and parts are validated against the unchanged work order.
"""
from authoring_support import assemble, read

def build(td, entries, questions, performances, links, examples):
    claims={};blocks={}
    for suffix,title,meaning,explanation in entries:
        claims[suffix]=[('factual',meaning),('causal',explanation)]
        blocks.setdefault(suffix[:2],[]).append(('plain_explanation',title,meaning+' '+explanation,[suffix]))
    for unit,heading,text,suffixes in examples:
        blocks[unit].append(('worked_application',heading,text,suffixes))
    for unit,text in links.items():
        blocks[unit].append(('cross_link','Connect the ideas',text,[s for s in claims if s.startswith(unit+'-')]))
    assemble(td,claims,blocks,questions,performances,[{'from':'Generated lower word allocations for related parent and member targets',
        'to':'Integrated concise explanations and original worked examples; all allocated targets and items retained.',
        'why':'The approved subject handover makes minima advisory. Explanations are written to teach distinct concepts and mechanisms without padding.'}])
