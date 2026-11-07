"""Display numeric sequences in authored prose without Python representation.

This only parses numeric literal lists already in the trusted content package;
no executable expression, string element or object is accepted.
"""
import ast
import re
from .formatting import number_latex

_SEQUENCE=re.compile(r'\[(?:\s*(?:\([^()\[\]]*\)|\[[^\[\]]*\]|-?\d+(?:\.\d+)?)\s*,?)+\]')


def authored_prose(text):
    def render(match):
        try:values=ast.literal_eval(match[0])
        except (ValueError,SyntaxError):return match[0]
        number=lambda v:type(v) in (int,float)
        if not isinstance(values,list) or not values:return match[0]
        if all(number(x) for x in values):
            body=', '.join(number_latex(x) for x in values)
            context=text[max(0,match.start()-60):match.start()].lower()
            if any(w in context for w in ('outside','inside','interval','within','between','lie in','lies in')):
                return match[0]
            if len(values)==2 and any(w in context for w in ('centre','endpoint','vector')):
                return '('+body+')'
            if any(w in context for w in ('values','evaluations','angles','calculations','widths','densities','frequencies','counts','symbols','observations')):
                return body
            # A bare numeric bracket pair can be a genuine closed interval.
            # Never change it merely because Python can parse it as a list.
            return match[0]
        if all(isinstance(row,(list,tuple)) and len(row)==2 and all(number(x) for x in row) for row in values):
            return '; '.join('('+', '.join(number_latex(x) for x in row)+')' for row in values)
        return match[0]
    return _SEQUENCE.sub(render,text)


def normalise_notation(text):
    """Remove redundant numeric signs/coefficient notation, preserving grouping."""
    text=authored_prose(str(text))
    text=re.sub(r'\ba enlargement\b','an enlargement',text)
    text=re.sub(r'\\frac\{(-?\d+)\}\{1\}',r'\1',text)
    text=re.sub(r'\b([xyz])-\(0\)(?!\s*(?:\^|[²³!]))',r'\1',text)
    text=re.sub(r'\b([xyz])-\((\d+(?:\.\d+)?)\)(?!\s*(?:\^|[²³!]))',r'\1-\2',text)
    text=re.sub(r'(?<![A-Za-z}])\(([xyz])\)',r'\1',text)
    text=re.sub(r'(?<![\w.\\])(-?)1(?=\()',r'\1',text)
    text=re.sub(r'\+\s+\((-?\d+(?:\.\d+)?)\)(?=\s*(?:[+\-=,;:.$)]|$))',lambda m:m[1] if m[1].startswith('-') else '+'+m[1],text)
    # Do not remove grouping: a following power, factorial or product changes
    # the meaning of +(-a) and -(-a). Retaining brackets is always sound.
    # A signed numeric operand immediately before +, -, = or the end has no
    # exponent/product binding to preserve. Leave every other bracket intact.
    text=re.sub(r'-\((-(?:\d+(?:\.\d+)?))\)(?=\s*(?:[+\-=,;:.$)]|$))',lambda m:'+'+m[1][1:],text)
    text=re.sub(r'\+\((\d+(?:\.\d+)?)\)(?=\s*(?:[+\-=,;:.$)]|$))',r'+\1',text)
    text=re.sub(r'\+\((-\d+(?:\.\d+)?)\)(?=\s*(?:[+\-=,;:.$)]|$))',r'\1',text)
    text=re.sub(r'([+-])\((-?\d+(?:\.\d+)?)\)(?=[a-zA-Z])',lambda m: ('-' if (m[1]=='-') != m[2].startswith('-') else '+')+m[2].lstrip('-'),text)
    text=re.sub(r'(^|[=$,(;])\((-?\d+(?:\.\d+)?)\)(?=[a-zA-Z])',r'\1\2',text)
    text=re.sub(r'(?<![\d._a-zA-Z\\])1([a-zA-Z])(?=[\s\\^²³{}$),;=+\-]|$)',r'\1',text)
    text=re.sub(r'([a-zA-Z])\^\{1\}',r'\1',text)
    text=re.sub(r'(^|[=$,(;+])\\frac\{-(\d+)\}\{(\d+)\}',r'\1-\\frac{\2}{\3}',text)
    text=re.sub(r'\\frac\{-(\d+)\}\{-(\d+)\}',r'\\frac{\1}{\2}',text)
    text=re.sub(r'(?<=[\d)])\s*\*\s*(?=[\d(])',r'\\times ',text)
    text=re.sub(r'(^|[=$,(;+])1(?=\()', r'\1', text)
    return text


def notation_faults(text):
    """Find defects without rejecting valid grouped terms or interval notation."""
    patterns={
        'placeholder':r'REPLACE|AUTHOR_REASON_REQUIRED|TODO_ANSWER',
        'python_sequence':r'\[\s*[\[(]',
        'bracketed_coefficient':r'(^|[=$,(;])\(-?\d+(?:\.\d+)?\)[a-zA-Z]',
        'coefficient_one':r'(?<![\d._a-zA-Z\\])1[a-zA-Z](?=[\s\\^²³{}$),;=+\-]|$)',
        'power_one':r'[a-zA-Z]\^\{1\}',
        'calculator_multiplication':r'(?<=[\d)])\s*\*\s*(?=[\d(])',
        'double_minus':r'(?<!-)-\s*-(?=[0-9A-Za-z\\(])',
        'literal_pi':r'\b\d+(?:\.\d+)?pi\b',
    }
    faults=[name for name,pattern in patterns.items() if re.search(pattern,text)]
    # Matrix columns are structural, not expendable alignment characters.
    for match in re.finditer(r'\\begin\{(p?matrix|bmatrix|vmatrix)\}(.*?)\\end\{\1\}',text,re.S):
        rows=re.split(r'\\\\',match[2])
        widths=[len(row.split('&')) for row in rows if row.strip()]
        if len(set(widths))>1:faults.append('matrix_columns')
    # Reject delimiters damaged by rewriting signed powers, without guessing
    # which signs a valid arithmetic expression was meant to contain.
    for match in re.finditer(r'\\sqrt\{([^{}]*)\}',text):
        body=match[1]
        if body.count('(')!=body.count(')'):faults.append('signed_power_grouping')
    return faults


def markdown_result(value):
    """Compatibility export: new consumers use typed blocks instead."""
    from ..math_workbench.content_format import display_content
    return '\n\n'.join(('$$\n'+b['value']+'\n$$') if b['kind']=='math' else b['value'] for b in display_content(value)['blocks'])
