"""Original Codex manuscript: the syllabus's five Vision 2030 areas."""
import sys
from pathlib import Path
TD=Path(__file__).resolve().parent
sys.path.insert(0,str(TD.parent))
from authoring_support import assemble
C={'01-00':[
 ('factual','The syllabus treats education, science and technology; health and development; sustainable agriculture; peace and social justice; and gender equality as five areas contributing towards Vision 2030.'),
 ('causal','Education and appropriate technology can develop productive capabilities, while health supports participation in learning, work and community life.'),
 ('causal','Sustainable agriculture protects future productive resources; peaceful cooperation, fair access and gender equality can widen opportunities to contribute to and benefit from development.')]
}
B={'01':[
 ('plain_explanation','Five connected areas',"Vision 2030 provides the long-term development context for this lesson. Study the five areas named here without assuming that a stated ambition has already been achieved. Education, science and technology can build knowledge and usable skills. Health and development connect people's well-being with their ability to learn, work and participate. Sustainable agriculture maintains farming while protecting soil, water and future production. Peace and social justice concern cooperation, fair treatment and access to opportunities. Gender equality means equal rights, opportunities and treatment regardless of gender; formal equality does not by itself establish equal lived outcomes.",['01-00']),
 ('worked_application','Make the connection explicit',"In an invented community, a training centre has equipment but some learners cannot attend because sessions clash with caring duties. Offering workable session times and fair access could connect education and gender equality: more people could gain usable skills. This proposal addresses the identified barrier rather than assuming that equal admission rules have removed it. In a separate fictional comparison, Centre A has 40% course completion and 35% participation among eligible women; Centre B has 75% completion and 70% participation. B combines higher completion with wider participation. That relationship helps identify an access issue to investigate; the figures do not prove which policy caused it.",['01-00']),
 ('cross_link','Use the areas together',"These areas reinforce one another when practical conditions allow it. Healthy learners can benefit from accessible education; usable skills and sustainable farming can support livelihoods. Topic 1.2 explains sustainability, Topic 7.2 health, Topic 7.3 education and Topic 6.2 gender. Here, describe each area's contribution and show a connection using the facts of a case. A programme's title is not evidence that its intended outcome occurred; look for participation, service and living-condition changes.",['01-00'])]}
Q={
 1:('Describe how two of the five syllabus areas can contribute towards Vision 2030.',
    'Education, science and technology can develop usable knowledge and productive skills. Sustainable agriculture can maintain farming while protecting soil and water for future production.',
    ['Feature: describe a contribution from each of two distinct areas. Accept health and participation, peace and fair opportunity, or gender equality with a clear contribution.']),
 2:('Suggest an improvement linking education and gender equality for an invented training centre whose sessions clash with caring duties and prevent some otherwise eligible learners attending.',
    'Offer workable alternative session times and fair access to the same training. Reducing the stated timetable barrier could widen participation and the opportunity to gain usable skills.',
    ['Context: respond to the timetable/caring barrier.','Reason: connect the proposal to equal opportunity and access to skills; admission rules alone do not remove the stated constraint.'])}
P={
 'P01':(['01-00'],
 'State (a) two syllabus Vision 2030 areas connected to this invented case [2]. Explain (b) how the two supplied facts interact to constrain development [4]. A community training programme has working equipment and relevant instruction, but repeated illness causes many learners to miss the sessions.',
 '(a) Education, science and technology; health and development. (b) Although equipment and instruction provide a learning opportunity, illness prevents learners using it consistently. Missed training can restrict skill acquisition, reducing the gain expected from the educational investment. Health and education are therefore linked in this case rather than independent lists of activities.',
 ['Point (a), 2 marks: the two relevant areas.','Development (b), up to 4 marks: combine available training and illness-related absence to explain the barrier to skills and expected benefits. Do not credit an invented diagnosis or claim that equipment is missing.']),
 'P02':(['01-00'],
 'Describe (a) the relationship in this original fictional comparison: Centre A has course completion 40% and participation among eligible women 35%; Centre B has 75% and 70% respectively [3]. Suggest (b) a justified first action if the aim is to widen fair access and completion. A reports that session times clash with caring duties; both centres have available places [3].',
 '(a) B combines higher completion and wider participation: both measures are 35 percentage points higher than A. (b) Centre A should trial workable alternative session times and monitor participation and completion. The stated caring-duty clash is an actionable barrier and available places mean capacity is not the immediate constraint. The comparison alone does not prove the timetable explains the whole difference.',
 ['Evidence (a), up to 3 marks: use both participation and completion to describe the association accurately.','Meaning (b), up to 3 marks: target the supplied barrier, connect it to the fair-access/completion aim, and justify using the available-place condition.'])}
if __name__=='__main__':assemble(TD,C,B,Q,P)
