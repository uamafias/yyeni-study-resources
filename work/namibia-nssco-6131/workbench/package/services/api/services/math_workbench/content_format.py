"""Typed display blocks for trusted recipe content; raw grading values stay intact.

Commands/groups are lexed atomically, so point names cannot turn a formula into
prose. Existing Markdown math spans are explicit. Text outside them stays text.
"""
import re

_MATH=re.compile(r'\(-?\d+(?:\.\d+)?,\s*-?\d+(?:\.\d+)?\)|\\[A-Za-z]+|\b(?:sin|cos|tan|log|ln)\b|[=<>^_]|[≈−×÷±√∠≤≥]|\d(?:[A-Za-z]|\s*\()|(?:\b\d+(?:\.\d+)?|\b[a-z])\s*[+*/-]\s*(?:\d|[a-z]\b)')
_TOKEN=re.compile(r'\\[A-Za-z]+|[A-Za-z]+|[^A-Za-z\\{}]+|\\.')
_TEXT_COMMANDS={'text','textrm','textbf','mathrm','operatorname','begin','end','mathbf','mathbb','mathcal','overrightarrow','overline','underline'}
_WORDS={'and','or','of','to','by','at','in','is','as','on','no','an','if','so','the','for','from','with','each','result','class','units','minutes','hours','learners','all','are','can','has','not','one','two','sum','add','use','end','per','its','any','but','new','odd','arc','ray','run','gap','rise','reflex','north','start'}
_UNITS={'cm','mm','km','kg','ms','ml','m','s','h','g','l'}


def _group(source,start):
    if start>=len(source) or source[start]!='{':return start
    depth=0
    for i in range(start,len(source)):
        if source[i]=='{' and (i==0 or source[i-1]!='\\'):depth+=1
        elif source[i]=='}' and (i==0 or source[i-1]!='\\'):
            depth-=1
            if depth==0:return i+1
    raise ValueError('Unbalanced trusted display group')


def _bare_blocks(source):
    source=source.strip()
    if not source:return []
    if not _MATH.search(source) and not (re.search(r'\d',source) and re.fullmatch(r'[-+\d., ()]+',source)):
        return [{'kind':'text','value':source}]
    # Explicit prose labels before a formula are separate blocks, not maths.
    label=re.match(r'^([^\\=<>^_]*[A-Za-z][^\\=<>^_]*):\s*(.*)$',source,re.S)
    if label and len(label[1])<100:
        return [{'kind':'text','value':label[1].strip()+':'}]+_bare_blocks(label[2])
    blocks=[];kind=None;buffer='';position=0
    def emit(next_kind,value):
        nonlocal kind,buffer
        if next_kind!=kind:
            if buffer.strip():blocks.append({'kind':kind,'value':buffer.strip()})
            kind=next_kind;buffer=''
        buffer+=value
    while position<len(source):
        currency=re.match(r'N\$\d+(?:[,.]\d+)*',source[position:])
        if currency:
            emit('text',currency[0]);position+=len(currency[0]);continue
        if source[position]=='{':
            end=_group(source,position);emit('math',source[position:end]);position=end;continue
        if source[position]=='}':raise ValueError('Unmatched trusted display brace')
        token=_TOKEN.match(source,position)
        if not token:raise ValueError('Unrecognised display token')
        value=token[0];position=token.end()
        if value.startswith('\\'):
            command=value[1:]
            # Preserve command arguments, environment names and text groups.
            if command in _TEXT_COMMANDS and position<len(source) and source[position]=='{':
                end=_group(source,position);value+=source[position:end];position=end
            emit('math',value)
        elif value.isalpha():
            lower=value.lower()
            adjacent=source[:token.start()].rstrip()[-1:]+source[position:].lstrip()[:1]
            algebraic_product=len(value)<=3 and set(value)<=set('abcdfghklmnpqrstuvxyz') and bool(re.search(r'[=+*/^_<>\d−×÷-]',adjacent))
            is_text=lower in _WORDS or (len(value)>1 and not value.isupper() and lower not in {'sin','cos','tan','log','ln'} and not algebraic_product)
            if lower=='a':
                # An article beside prose is not a variable. An algebraic a in
                # a+b or 3a remains mathematical; explicit $a$ is authoritative.
                adjacent=source[:token.start()].rstrip()[-1:]+source[position:].lstrip()[:1]
                is_text=not bool(re.search(r'[=+*/^_<>\d−×÷-]',adjacent)) and not source[position:].startswith(('′','″',"'"))
            if value.isupper() and len(value)==1 and kind=='text':
                rest=source[position:]
                if re.match(r'^[.,;:!?)]*(?:\s|$)',rest):is_text=True
            unit_context=len(value)>1 or source[max(0,token.start()-1):token.start()].isspace() or bool(re.match(r'/s(?:[²³^\s.,;)]|$)',source[position:])) or (source[:token.start()].rstrip().endswith('/') and r'\mathrm' in buffer)
            if value in _UNITS and unit_context and kind=='math' and re.search(r'(?:\d|[}²³])\s*/?\s*$',buffer):emit('math',r'\,\mathrm{'+value+'}')
            else:emit('text' if is_text else 'math',value)
        else:
            # Keep spaces with their current block; punctuation joins formula
            # tokens but is never interpreted as executable markup.
            if ':' in value and ('=' in buffer or '=' in value):
                before,after=value.split(':',1)
                emit('math',before);emit('text',':');emit('math',after)
            else:
                emit('math' if re.search(r'\d|[=<>^_−×÷±√∠≤≥]',value) else kind or 'math',value)
    if buffer.strip():blocks.append({'kind':kind,'value':buffer.strip()})
    cleaned=[]
    for block in blocks:
        if block['kind']=='math':
            if not re.search(r'[A-Za-z0-9\\∠√=<>≤≥±×÷]',block['value']):block['kind']='text'
            suffix=re.search(r'(\)+)([.,;:!?]*)$',block['value'])
            if suffix and block['value'].count(')')>block['value'].count('('):
                excess=min(len(suffix[1]),block['value'].count(')')-block['value'].count('('))
                cut=len(block['value'])-len(suffix[2])-excess
                cleaned.append({**block,'value':block['value'][:cut]})
                cleaned.append({'kind':'text','value':block['value'][cut:]})
                continue
            # An opening parenthesis before prose belongs to that prose, not
            # to the preceding equation (e.g. "x=2 (allow ...)").
            tail=re.search(r'\s+(\(+)$',block['value'])
            if tail:
                block['value']=block['value'][:tail.start()]
                cleaned.append(block);cleaned.append({'kind':'text','value':tail[1]});continue
        if block['value']:cleaned.append(block)
    return cleaned


def _math_value(value):
    # Escape literal currency/percent signs only in display metadata, never in
    # grading evidence. Unicode roots need a complete braced radicand in KaTeX.
    value=value.replace('′',"'").replace('″',"''").replace('²','^{2}').replace('³','^{3}')
    # Explicit spans bypass the bare-token lexer, so normalise their units too.
    value=re.sub(r'(?<=[0-9}])\s+((?:km|cm|mm|kg|ml|m|s|h|g|l)(?:/s(?:\^\{[23]\})?)?)(?![A-Za-z])',lambda m:r'\,\mathrm{'+m[1]+'}',value)
    value=re.sub(r'(?<![A-Za-z\\])(?:sin|cos|tan|log|ln)(?![A-Za-z])',lambda m:'\\'+m[0],value)
    value=re.sub(r'(?<!\\)%',r'\\%',value)
    value=re.sub(r'(?<!\\)\$',r'\\$',value)
    while '√' in value:
        start=value.index('√');end=start+1
        if end<len(value) and value[end]=='(':
            depth=1;end+=1;inner=end
            while end<len(value) and depth:
                if value[end]=='(':depth+=1
                elif value[end]==')':depth-=1
                end+=1
            if depth:raise ValueError('Unbalanced square-root radicand')
            replacement=r'\sqrt{'+value[inner:end-1]+'}'
        else:
            match=re.match(r'[0-9.]+|[A-Za-z]',value[end:])
            if not match:raise ValueError('Missing square-root radicand')
            end+=len(match[0]);replacement=r'\sqrt{'+match[0]+'}'
        value=value[:start]+replacement+value[end:]
    return value


def display_content(value):
    """Convert a trusted source string into an explicit sequence of blocks."""
    source=str(value or '').strip();blocks=[];start=0
    source=re.sub(r'([A-Za-z])_([A-Za-z]{2,})',lambda m:m[1]+r'_{\text{'+m[2]+'}}',source)
    pattern=re.compile(r'\$\$(.*?)\$\$|(?<!\\)\$([^$\n]+?)(?<!\\)\$',re.S)
    # Currency N$ is not a math delimiter.
    masked=re.sub(r'(?<=[A-Za-z0-9])\$(?=\d)','¤',source)
    for match in pattern.finditer(masked):
        blocks.extend(_bare_blocks(masked[start:match.start()].replace('¤','$')))
        value=(match[1] if match[1] is not None else match[2]).strip()
        block={'kind':'text' if value.lower() in _WORDS else 'math','value':value}
        if value in ('a','A'):block['explicit']=True
        blocks.append(block);start=match.end()
    blocks.extend(_bare_blocks(masked[start:].replace('¤','$')))
    for block in blocks:
        if block['kind']=='math':block['value']=_math_value(block['value'])
        else:block['value']=re.sub(r'(?<![\w-])-(?=\d)','−',block['value'])
    return {'format':'text_math_blocks_v1','blocks':blocks}


def validate_content(content):
    assert content['format']=='text_math_blocks_v1'
    for block in content['blocks']:
        assert block['kind'] in ('text','math') and isinstance(block['value'],str) and block['value'].strip()
        if block['kind']=='text':assert not re.search(r'\\[A-Za-z]+',block['value']),block
        else:
            assert re.search(r'[A-Za-z0-9\\∠√=<>≤≥±×÷]',block['value']),('Punctuation-only maths',block)
            assert block['value'] not in ('a','A') or block.get('explicit'),('Article filed as maths',block)
            words=re.sub(r'\\(?:text|mathrm|textrm|operatorname)\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', block['value'])
            assert not any(re.search(r'(?<![A-Za-z\\])'+word+r'(?![A-Za-z])',words,re.I) for word in ('arc','ray','run','gap','reflex')),('Prose filed as maths',block)
    return content


def attach_display_content(question):
    """Derive metadata from raw answers; do not rewrite mathematical evidence."""
    for part in question['parts']:
        part['reference_answer_content']=validate_content(display_content(part['reference_answer']))
        for step in part['worked_steps']:
            step.pop('result_format',None)
            step['result_content']=validate_content(display_content(step['result']))
        for criterion in part.get('criteria',[]):
            criterion['achievement_content']=validate_content(display_content(criterion['achievement']))
    return question
