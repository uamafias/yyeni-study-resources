"""Runtime recipe adapters for the prepared visual families."""
from copy import deepcopy
from .base import GeneratedProblem, MathGenerator, Step
from .prepared_visual_bank import catalog, ROOT


class PreparedVisualGenerator(MathGenerator):
    version=1
    def __init__(self,gid,group):
        self.version=2 if gid=='nssco_visual_linear_programming' else 1
        self.generator_id=gid;self.title=group['title'];self.lesson_id=group['lesson_id']
        self.labels={int(k):v for k,v in group['labels'].items()}
        self._rows={int(k):v for k,v in group['levels'].items()}
        self.levels=tuple(sorted(self._rows))
        self.bank_sizes={level:len(rows) for level,rows in self._rows.items()}
        # Some levels mix reading and drawing examples. Assignment must use
        # the whole bank, since a later Recall round may draw any row.
        self.drawing_levels=frozenset(
            level for level,rows in self._rows.items()
            if any(row['machine'].get('response_mode') == 'draw' for row in rows)
        )
        self.level_skills={level:tuple(dict.fromkeys(row['skill'] for row in rows)) for level,rows in self._rows.items()}
        self.error_notes={skill:{'diagram_misread':'Misread the diagram or did not complete the requested drawing.'}
                          for skills in self.level_skills.values() for skill in skills}

    def _build(self,rng,seed,level):
        rows=self._rows[level];row=deepcopy(rows[seed%len(rows)])
        if self.generator_id=='nssco_visual_linear_programming' and not row['machine'].get('strict',True):
            if row['machine']['task']=='shade_lp':
                old=row['answer'];row['answer']='The triangular intersection R is left unshaded. All three boundaries are solid because equality is allowed.'
                row['steps']=[{**s,'value':row['answer'] if s['value']==old else s['value']} for s in row['steps']]
                row['marking']={**row['marking'],'expected':[row['answer']],'typed':row['answer']}
            row['machine']['explanation']=row['machine']['explanation'].replace('The broken horizontal boundary is strict; solid boundaries permit equality.', 'All three solid boundaries permit equality.')
        return GeneratedProblem(self.generator_id,self.version,seed,level,row['skill'],row['question'],row['answer'],
            machine=row['machine'],steps=tuple(Step(**s) for s in row['steps']),marking=row['marking'])


# The API release must include the immutable manifest and all referenced PNGs.
GENERATORS=[PreparedVisualGenerator(gid,group) for gid,group in catalog().items()]
