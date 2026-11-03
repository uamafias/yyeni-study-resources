"""Authored visual-task helpers; geometry is data, never executable content."""
from .base import GeneratedProblem,MathGenerator,Step
from .figures import figure,line,text,point,circle,arc,spec,grid

PHOTO_NOTE=(' Draw on paper and upload a clear photo of the complete drawing. '
            'Keep axis labels, scales and any construction arcs visible. '
            'For centimetre measurements, include a ruler in the photo; do not measure the screen.')


def make(g,seed,level,task,question,answer,question_figure,answer_figure,explanation,awards,sources,data=None,draw=True):
    question=question+(PHOTO_NOTE if draw else '')
    machine=dict(data or {},task=task,response_mode='draw' if draw else 'read',
                 question_figure=question_figure,reference_figure=answer_figure,
                 explanation=explanation,awards=[{'marks':m,'achievement':s} for m,s in awards],sources=list(sources))
    kind='draw_or_construct' if draw else 'text_description'
    return GeneratedProblem(g.generator_id,g.version,seed,level,g.level_skills[level][0],question,answer,
        machine=machine,steps=(Step('Set out the required drawing or diagram reading',answer,kind),),
        marking={'answer_type':kind,'expected':[answer],'typed':answer})


class VisualGenerator(MathGenerator):
    version=1
    def __init__(self,slug,lesson_id,title,builders,labels):
        self.generator_id='nssco_visual_'+slug;self.lesson_id=lesson_id;self.title=title
        self._builders=builders;self.levels=tuple(builders);self.labels=labels
        self.level_skills={l:(f'{slug}_{l}',) for l in self.levels}
        self.error_notes={s:{'diagram_misread':'Misread the diagram, ignored its scale or did not complete the required drawing.'} for v in self.level_skills.values() for s in v}
    def _build(self,rng,seed,level):return self._builders[level](self,rng,seed,level)


def closed(points,color='ink',fill=False):return line([*points,points[0]],color,fill=fill)
def shifted(points,dx,dy):return [[x+dx,y+dy] for x,y in points]
def polygon_with_labels(points,names='ABC',color='ink'):
    return [closed(points,color)]+[text(x+0.25,y+0.35,name,color) for (x,y),name in zip(points,names)]
def points_table(xs,ys):return '| $x$ | '+' | '.join(f'${x}$' for x in xs)+' |\n|---|'+'---|'*len(xs)+'\n| $y$ | '+' | '.join(f'${y}$' for y in ys)+' |'
def tick_step(span):return max(1,round(span/10))


def teaching(problem):
    if not problem.generator_id.startswith('nssco_visual_'):return None
    return problem.answer,problem.machine['explanation']


def guidance(problem):
    m=problem.machine
    awards=m['awards']
    if not awards or any(type(a['marks']) is not int or a['marks']<1 for a in awards) or sum(a['marks'] for a in awards)>6:
        raise ValueError('Invalid authored visual tariff')
    note=('The attached question and solution images are trusted reference diagrams, not learner evidence. '
          'For a required drawing, award its drawing achievements only from visible learner-uploaded drawing evidence; '
          'typed coordinates, an equation or a claim that a drawing was made do not establish that drawing. '
          'A separate requested calculation/table/description can earn its own explicitly allocated marks from text. '
          'Check labelled coordinates, shape, scales, joins, labels and construction arcs as specified. '
          'Accept an equivalent valid construction or layout unless a method is explicitly required. '
          'Do not infer centimetres from screen pixels or an uncalibrated photo; a metric measurement needs a visible ruler/scale. '
          'If the photo cannot establish an achievement reliably, request review rather than inventing a measurement. '
          'Do not invent pixel tolerances, extra shape/label marks, or universal follow-through.')
    return awards,list(m['sources']),note
