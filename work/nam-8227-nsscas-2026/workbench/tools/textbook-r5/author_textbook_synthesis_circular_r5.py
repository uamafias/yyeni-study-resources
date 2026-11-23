"""Explicit circular-measure source decisions; no automatic topic clustering."""
from synthesis_authoring_support_r5 import D,members,family,insight,emit
def Y(k,ns,parts='*'):return members('YM',4,k,ns,parts)
def C(o,n):return D(f'M1:T5:O0{o}:D0{n}')
families=[]
def F(*a):families.append(family(*a))
F('angle-unit-conversion','Convert degrees and radians, including a geometric unit illustration',
  'Use a complete turn to convert the actual angle and distinguish exact multiples of pi from decimal approximations.',
  'Degree/radian measures; unknown equivalent measure.',
  'Retain signed measure and unit. A conversion task does not itself ask the learner to explain the definition of a radian.',
  'Angle notation to exact/rounded measure.', 'Independent conversions retain their source subparts.',
  'Use 180 degrees = pi radians; a full-turn proportion is equivalent.',
  'Exact pi expression or requested decimal with angular unit.',
  'YM examples begin with exact rational degrees, then non-special decimal radians; Exercise4.1 mixes exact and 1dp outputs.',
  'Unit conversion differs from interpreting the geometric arc/radius definition.',[C(1,2)],
  Y('Example',[1,2])+Y('Try-Now',[1,2])+Y('Exercise-4.1',[1,2])+Y('Worked-illustration',[1]))
F('circle-arc-major-minor','Select the minor or major arc before calculating its length',
  'Identify the requested arc and complement the given minor angle when the major arc is asked.',
  'Radius and minor central angle; unknown named arc lengths.',
  'Positive radius; minor angle and complementary full turn must describe the actual diagram.',
  'Labelled circle to lengths.', 'Minor and major outputs share one original circle.',
  's=r theta with radians; a full-circumference subtraction is equivalent.',
  'Length in the original units.', 'YM3/Try3 ask both arcs rather than only a direct substitution.',
  'The region selection is additional to ordinary numeric replacement.',[C(2,1)],Y('Example',[3])+Y('Try-Now',[3]))
F('circle-major-sector','Select a major sector and compute its area',
  'Recover the reflex sector angle from the minor marked angle and use the correct sector.',
  'Circle radius and minor angle; unknown major-sector area.', 'r>0; 0<minor angle<2pi; squared length units.',
  'Circle diagram to positive area.', 'No invented perimeter response.',
  'Half r squared theta or whole-circle area minus minor sector.', 'Exact or requested rounded area.',
  'YM4/Try4 hold the same region decision with different original values.',
  'Major-sector selection differs from segment subtraction or perimeter inference.',[C(2,2)],Y('Example',[4])+Y('Try-Now',[4]))
F('sector-perimeter-inverse','Infer sector angle/radius from area or boundary information',
  'Separate curved length from the two radii, infer missing values and use the second sector relation.',
  'Perimeter/area/radius or two entries in a sector table; unknown arc, angle, radius and area.',
  'All length units consistent; perimeter includes both radii; reject nonpositive inferred radius/arc.',
  'Prose/sector table to linked measures.', 'Retain each row and its two unknowns rather than inventing an extra question.',
  'Solve s=r theta and A=rs/2; equivalent exact algebra.', 'All requested measures with correct units.',
  'YM5 starts from perimeter;6 starts from area; Exercise4.1Q3 has two simultaneous unknowns per row.',
  'Inverse use of a boundary/area relation changes the learner decision.',[C(2,1),C(2,2)],
  Y('Example',[5,6])+Y('Try-Now',[5,6])+Y('Exercise-4.1',[3]))
F('annular-sector-model','Read an annular sector and identify all exposed boundaries',
  'Infer the outer radius from radial width, recover the common angle and subtract sectors for area.',
  'Inner radius8, width12, inner-sector area80; unknown angle, perimeter, shaded area.',
  'Outer radius20, not12; same central angle; boundary includes inner and outer arcs plus two radial widths.',
  'Given annular diagram to angle/length/area.', 'Angle precedes perimeter and area.',
  'Difference of sectors or half difference of radius squares times angle.', 'All three linked outputs.',
  'Unknown angle and an inner arc make this more than one simple-sector evaluation.',
  'An annular hole changes both the boundary and area model.',[C(2,1),C(2,2)],Y('Exercise-4.1',[4]))
F('overlapping-sector-area','Combine sectors and triangles for curved overlaps or gaps',
  'Read distinct centres/radii and identify which sectors and triangles form the actual shaded region.',
  'Right triangles, rectangle or touching circles with named arcs; unknown angles and overlap/gap areas.',
  'Each arc uses its own centre/radius. Keep exact angles/lengths until final rounding. Exercise4.1Q5 includes the remaining sector and two triangles.',
  'Given multi-centre diagram to shown angle/area.', 'A shown angle may scaffold the later region calculation.',
  'Geometric inclusion/subtraction with valid sine/cosine triangle areas.', 'Positive shaded area and requested angle/sector values.',
  'YM7 has two-sector overlap;57 rectangle overlap; revisionQ4 three touching circles form a curvilinear gap. These remain explicit structural branches, not equivalent diagrams.',
  'The active region and arc centres change the modelling beyond the sector formula.',[C(2,2)],
  Y('Example',[7,57])+Y('Try-Now-7',[1])+Y('Exercise-4.1',[5])+Y('Revision-Exercise-4',[4]))
F('curvilinear-perimeter','Find a curvilinear boundary before combining its area components',
  'Use the actual right-triangle/tangent geometry to recover missing lengths, then trace only the external boundary.',
  'Right-triangle sector plate, tangent wedge, or two-centre semicircle; unknown length/perimeter/area ratio.',
  'Keep tangent perpendicular to radius; 0<alpha<pi/2 in the symbolic tangent wedge. Internal seams are not perimeter.',
  'Labelled diagram to symbolic/numeric boundary and region measures.', 'Earlier length/arc results feed later area or ratio.',
  'Triangle trigonometry then arc/sector relations; independently trace the same boundary.',
  'Requested perimeter, area or ratio.', 'Try7Q2 has three connected outputs; Try57 switches arc centre and asks ratio; Exercise4.1Q6 asks a symbolic perimeter.',
  'External boundary tracing and symbolic geometry differ from a simple sector table.',[C(2,1)],
  Y('Try-Now-7',[2])+Y('Try-Now',[57])+Y('Exercise-4.1',[6]))
F('segment-and-chord','Separate a segment from its sector and triangle',
  'Find the chord/sector first, then subtract the correct triangle for the named segment.',
  'Radius and obtuse central angle; unknown arc, perimeter, sector area, segment area and chord.',
  'Use the actual minor/major region and angle. The Try8Q1 undefined B label remains a source defect.',
  'Sector diagram to exact linked quantities.', 'Arc/sector, segment and chord are distinct requested parts.',
  'Cosine rule or half-angle chord relation; Asegment=Asector-Atriangle.',
  'Exact lengths and areas with units.', 'YM8 and Try8Q1 ask several exact outputs; same decision with changed radius/angle.',
  'The triangle removed from a sector is essential evidence.',[C(2,1),C(2,2),C(2,3)],Y('Example',[8])+Y('Try-Now-8',[1]))
F('segment-composite-plate','Build a plate from a segment and a semicircle on its chord',
  'Recover the new semicircle radius from a chord and combine only the correct named regions/boundaries.',
  'Original circle plus external semicircle on chord; unknown radius, perimeter or crescent area.',
  'Do not reuse the original circle radius as the semicircle radius; retain the source half-angle range.',
  'Composite circle diagram to positive area/length.', 'Derived chord is a dependency for later semicircle quantities.',
  'Chord geometry and sector-minus-triangle model.', 'Requested composite perimeter/area.',
  'Try8Q2 combines a major segment with a semicircle; Try9 subtracts a minor segment to form a crescent.',
  'A new circle built on the chord changes the geometric model.',[C(2,2),C(2,3)],Y('Try-Now-8',[2])+Y('Try-Now',[9]))
F('sector-segment-equality','Derive an angle relation from equal triangle and segment areas',
  'Write both areas in the same variables and cancel only justified nonzero factors.',
  'Radius r and angle theta with equal triangle/segment areas; unknown p in theta=p sin(theta).',
  'r>0 and 0<theta<pi ensure the required divisions are valid.',
  'Symbolic labelled circle to a shown relation/coefficient.', 'The area models establish the equation, not a numerical root task.',
  'Sector-minus-triangle relation and exact algebra.', 'p=2 with assumptions retained.',
  'YM9 asks an equation from a geometric equality rather than an area value.',
  'Equal-region reasoning changes what must be demonstrated.',[C(2,2),C(2,3)],Y('Example',[9]))

def S(k,n):return f'8227:TB:YM:C4:{k}:{n}'
insights=[
 insight('radian-definition-and-conversion','Geometric radian meaning and conversion',[C(1,1),C(1,2)],
  'YM PDF154 explicitly shows an arc equal to its radius and six unit-radian arcs plus a remainder. Its unnumbered conversion then uses a complete turn. Goldie retained advanced-trigonometry pages assume this unit; no corresponding retained basic-radian exercise was found. YM teaching figures provide explanation, not a posed definition exercise.',
  'A degree/radian conversion is not evidence that a learner can explain the radian definition. Keep the independent examination coverage matrix authoritative; a topic label or calculator conversion does not close the definition demand.',
  'Start with arc/radius meaning before conversion; harder decimals test precision, not a higher cognitive level. Scope is the ordinary geometric unit, not arbitrary analytic angle conventions.',
  'Confusing radians with a length or entering degrees into s=r theta changes the answer. These are concept-based author feedback leads; this statement does not assert an examiner-reported frequency.',
  'The definition has teaching support in YM but no separately posed definition response in the retained population. This is an honest practice gap even though the source census contains the relevant diagram.',
  'Propose a purpose-built arc/radius interpretation response and exact/decimal conversion branches; derive the arc and angle from the same values. Keep teaching evidence separate from assessed-item counts.',
  [S('Teaching-figure',1),S('Teaching-figure',2),S('Worked-illustration',1),S('Exercise-4.1',1),S('Exercise-4.1',2)]),
 insight('arcs-sectors-and-boundaries','Arc length, sector area and geometric inverse problems',[C(2,1),C(2,2)],
  'YM proceeds through direct minor/major arcs, major-sector area, perimeter/area inverse problems, then overlapping circles and composite plates. Goldie advanced chapters use geometry in applications but do not replace this explicit circular-measure progression. Worked diagrams and source-given diagrams retain distinct roles.',
  'The 8227 source pattern registry records examination region demands; textbook numerical drills alone do not demonstrate all observed boundary/unknown decisions. Multi-centre overlap and area-ratio questions are candidate structural variety, not additional exam frequency.',
  'The accessible end uses one formula with a stated radius/angle; harder sources require reconstructing a radius, converting an inverse-trig angle and selecting several regions. Grade descriptors bound later parameters; present groupings do not certify grade levels.',
  'Major/minor substitution, internal seam perimeter and mixing two arc centres are source-specific hazards. Rounding a derived length before using it in the area can spoil the final required precision.',
  'YM provides the principal explicit practice. Goldie absence here is not a syllabus omission. The tangent wedge, annular sector and two-centre overlaps change the geometry and must not be flattened into number substitutions.',
  'Propose separate given/unknown and region branches, correlated centres/radii, explicit outer-boundary lists and independent geometry recomputation. Preserve the literal units and any source ambiguity.',
  [S('Example',3),S('Example',5),S('Example',7),S('Example',57),S('Exercise-4.1',4),S('Exercise-4.1',6),S('Try-Now',57)]),
 insight('circular-segments','Segments, chords and new circles on a chord',[C(2,3)],
  'YM first derives exact sector/triangle/chord quantities in Example8, then combines a major segment and new semicircle in Try8Q2, and poses a symbolic equal-area relation in Example9. Goldie retained scope does not offer an equivalent basic segment sequence.',
  'A sector formula supporting drill does not cover a full segment or composite-region demand. Compare future branches to actual examination part/criterion links before labelling same-type; these source groups remain textbook-derived.',
  'Direct segment subtraction is the entry branch. Symbolic area equality, major-segment selection and the new semicircle radius introduce additional decisions; none requires expanding beyond syllabus circular geometry.',
  'Try8Q1 names an undefined B where the diagram uses Y. Keep the correction as a source defect, not a wrong learner inference. A semicircle built on a chord generally has a different radius from the original circle.',
  'YM contains useful original-diagram templates and symbolic variety; source originals remain internal. A fixed image cannot be paired with unrelated generated radii/angles.',
  'Propose distinct segment, chord-built semicircle and equal-area branches. Generate chord, centres, shaded region and labels from a single geometry model and test both exact and rounded boundary instances.',
  [S('Example',8),S('Try-Now-8',1),S('Try-Now-8',2),S('Example',9),S('Try-Now',9)])]

if __name__=='__main__':
 for row in insights:
  row['grade_descriptor_ids']=['8227:GRADE:E:05','8227:GRADE:C:05','8227:GRADE:A:05']
  row['difficulty_and_grade_bounds']+=' E05 explicitly bounds radian interpretation/conversion; C05/A05 bound arc, sector and segment applications. These statements set limits, not a grade label for every source occurrence.'
 insights[1]['examination_part_ids']=['8227:EXAM:2021:P1:Q7:a','8227:EXAM:2021:P1:Q7:b','8227:EXAM:2022:P1:Q8:a']
 insights[1]['examination_comparison']+=' Specifically,2021P1Q7(a)(b)and2022P1Q8(a) link arc/perimeter modelling to area; source groups that isolate one formula are supporting branches.'
 emit('circular','Complete YM circular-measure response families and three insights covering the five M1T5 demands; Goldie comparison limitations explicit.',families,insights)
