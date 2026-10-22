#!/usr/bin/env python3
"""Original Atomic Structure manuscript, claims and practice for the frozen plan."""
import shutil
from authoring_common_8224 import Topic, WS
from render_chemistry_visuals_8224 import Figure

t=Topic('1.2')
S='OpenStax-Chemistry'

t.objective('1-01',[
    'A proton has relative charge +1 and approximate relative mass 1; a neutron has charge 0 and approximate relative mass 1.',
    'An electron has relative charge −1 and approximate relative mass 1/1836, which is small but not zero.',
    'Protons and neutrons are in the nucleus; electrons occupy the region outside it.',
], [('Three particles, two different comparisons', '''An atom contains a small central nucleus and electrons outside that nucleus. Its protons are positively charged, its neutrons have no electric charge, and its electrons are negatively charged. The proton and neutron each have an approximate relative mass of 1. The electron has an approximate relative mass of 1/1836. These are comparison numbers: a relative mass of 1 does not mean a particle has a mass of one gram. A relative charge of +1 represents one positive elementary charge, whereas −1 represents one negative elementary charge.

| Particle | Location | Approximate relative mass | Relative charge |
|---|---|---:|---:|
| Proton | Nucleus | 1 | +1 |
| Neutron | Nucleus | 1 | 0 |
| Electron | Outside nucleus | 1/1836 | −1 |

Read the headings before using the numbers. The neutron's zero belongs in the charge column; the neutron still contributes mass to the atom. The electron's small mass belongs in the mass column; its negative charge is equal in magnitude to a proton's positive charge. Calling the electron mass zero loses information that matters when comparing how particles respond to forces.

For example, six protons provide a total relative charge of +6. Six electrons provide −6. Their sum is zero, so this combination is electrically neutral even though its mass is not zero. A neutron can be added without changing that charge balance. Conversely, removing an electron changes the charge balance while leaving the number of protons unchanged. This separation of mass counting from charge counting is the starting point for interpreting both isotope symbols and ions. Keep the particle name, its location, its charge and its approximate mass together when checking a completed table.''')],S,'§2.3, printed pp. 78–79, Table 2.2')

t.objective('1-02',[
    'Most atomic mass is concentrated in the nucleus because protons and neutrons are much heavier than electrons.',
    'The nucleus carries the positive charge; negative electron charge is distributed outside it.',
], [('Where the mass and charge are concentrated', '''The nucleus occupies a very small part of the volume of an atom. Most of the atomic volume lies outside the nucleus, in the region occupied by electrons. Most of the mass, however, lies in the nucleus. This follows from the mass comparison: each proton or neutron contributes approximately one relative mass unit, while each electron contributes only about one eighteen-hundredth of that amount. A large occupied region need not contain most of the mass.

Positive charge is concentrated in the nucleus because that is where the protons are. Neutrons add mass there without adding electric charge. Negative charge belongs to the electrons outside the nucleus. In a neutral atom the total positive and negative charges balance; they are not both absent. For example, a neutral atom with 10 protons contains 10 electrons. Its nucleus remains positively charged, even though the atom considered as a whole is neutral.

Consider a model with 10 protons, 10 neutrons and 10 electrons. The approximate relative mass of its nucleus is 20. The electrons contribute about 10/1836, or 0.00545, on that same scale. Almost all of the approximate mass therefore lies in the nucleus. This is a particle-sum estimate for comparing contributions, rather than a precise prediction of an isotope's measured mass.

When describing an atom, avoid placing its electrons inside the nucleus or spreading nuclear mass uniformly throughout its volume. A useful verbal description connects each distribution to a particle: mass to nucleons, positive charge to protons, and negative charge to electrons. This model also explains why an atom can gain or lose electrons in ordinary ion formation without becoming a different element.''')],S,'§2.3, printed pp. 78–79')

t.objective('1-03',[
    'For a monatomic species with proton number Z, mass number A and signed ionic charge q, proton count is Z, neutron count is A−Z and electron count is Z−q.',
    'Positive ions have fewer electrons than protons; negative ions have more electrons than protons.',
    'Particle counts obtained from isotope notation are exact integers, not measured quantities to be rounded.',
], [('A reliable route from symbols to particle counts', '''Use three pieces of information separately. The proton number Z fixes the number of protons. The nucleon number A counts protons plus neutrons, so subtracting Z from A gives the neutrons. Charge compares the proton and electron counts. If q is the signed charge in elementary-charge units, q = protons − electrons; rearranging gives electrons = Z − q. A charge of 2+ means q is +2. A charge of 1− means q is −1.

Take an aluminium ion with A = 27, Z = 13 and charge 3+. Its nucleus contains 13 protons and 27 − 13 = 14 neutrons. The positive ion has lost three electrons, so its electron count is 13 − 3 = 10. Check the charge: 13 − 10 = +3. The mass number remains 27 because removing electrons has not removed any nucleons.

Now take a sulfur ion with A = 34, Z = 16 and charge 2−. It has 16 protons and 34 − 16 = 18 neutrons. The negative charge requires two more electrons than protons, giving 16 + 2 = 18 electrons. In the signed-charge expression this is 16 − (−2) = 18. Writing the verbal reasoning alongside the arithmetic helps prevent a sign error.

For an unknown species containing 15 protons, 16 neutrons and 18 electrons, reverse the process. Z is 15, A is 15 + 16 = 31, and q is 15 − 18 = −3. The species is a phosphorus ion with a 3− charge. These counts are integers describing individual particles. They do not acquire significant-figure limits from the printed number of digits. Check that the neutron count is non-negative and that your electron count reproduces the stated charge before moving to an electron configuration.''')],S,'§2.3, printed pp. 79–83; numerical examples transparently derived from particle-count relations')

t.objective('1-04',[
    'In an electric field between oppositely charged plates, electrons bend towards the positive plate and protons towards the negative plate.',
    'An uncharged neutron has no electric deflection in the idealised uniform field model.',
    'With equal entry speeds in the same field, electrons are deflected more strongly than protons because their masses are much smaller.',
], [('Sketching particle paths in an electric field', '''Begin a particle-path sketch by labelling the plates. In the example below, the top plate is positive and the bottom plate is negative. The particles enter from the left with their initial motion horizontal. An electron is attracted towards the upper positive plate, so its path curves upwards. A proton is attracted towards the lower negative plate, so its path curves downwards. A neutron has no net charge and continues along the initial straight line in this model.

![Original particle paths between electric plates](assets/8224-electric-field.png)

Deflection starts when a charged particle enters the field. Do not draw a long straight segment inside the plates and then suddenly turn the path at the exit. The particle already has a forward velocity, so a transverse force gradually changes its direction; it does not simply stop and move vertically towards a plate.

The proton and electron have opposite charges of equal magnitude. In the same electric field the magnitudes of their electric forces are equal. At equal entry speeds, the much lighter electron changes its motion more strongly, so its trajectory bends more. The picture is schematic and its distances are not a numerical mass comparison. The qualitative comparison requires the stated equal-speed condition: different initial speeds would affect the observed bending as well.

Use three separate checks on your drawing. Plate signs determine which way a charged path bends. Particle mass helps compare the electron and proton deflections under equivalent assumptions. A zero-charge particle stays on the original line. Label each path and add motion arrows so that a reader can identify the particles without guessing from colour. These are electric-field paths; they do not describe the structure of an orbital inside an atom.''')],'SRC-8224-ER-2025','Chemistry Paper 2 Q2(a)–(b), printed p. 75; syllabus §1.2.1, p. 7')

t.objective('2-01',[
    'The proton number is the number of protons in the nucleus and identifies the element.',
    'The nucleon number is the total number of protons and neutrons in a particular nucleus.',
    'A nucleus with proton number Z and nucleon number A contains A−Z neutrons.',
], [('Proton number identifies; nucleon number counts', '''Proton number and nucleon number answer different questions. The proton number Z tells you which element a nucleus belongs to. A nucleus with 8 protons belongs to oxygen. Giving that nucleus a different number of neutrons produces a different oxygen isotope, while changing the number of protons would change the element. The nucleon number A tells you how many nuclear particles are present in total: protons plus neutrons.

A nucleus with 8 protons and 10 neutrons has Z = 8 and A = 18. The two numbers are not alternatives for the same quantity. One records a particular kind of particle; the other records the sum of protons and neutrons. Reversing them would incorrectly suggest 18 protons and would give a negative neutron count when A − Z is evaluated. Always check that A is at least as large as Z.

The word nucleon is useful because it groups the two nuclear particles. Electrons are not included in A. A neutral oxygen-18 atom has 8 electrons, but its nucleon number is still 18, not 26. The oxide ion made from that atom has 10 electrons, yet the same nucleus and the same nucleon number. Ordinary electron gain or loss changes the species' charge, rather than its isotope identity.

Use this reasoning in reverse when a table gives nuclear composition. For a nucleus with 20 protons and 22 neutrons, Z is 20 and A is 42. If the table instead gives Z = 20 and A = 42, subtracting yields 22 neutrons. Both routes describe one nucleus and produce exact particle counts. The decimal relative atomic mass often printed on a periodic table is a different quantity, introduced in Topic 1.1; it is not automatically the nucleon number of an individual atom.''')],S,'§2.3, printed pp. 79–83')

t.objective('2-02',[
    'Isotopes of an element share the same proton number but have different neutron numbers and hence different nucleon numbers.',
    'Neutral isotopes of the same element contain equal electron numbers, while their nuclear particle counts differ.',
    'An isotope distinction concerns the nucleus; an ion distinction concerns electron gain or loss and charge.',
], [('Separating isotope changes from charge changes', '''Isotopes are atoms of one element with different numbers of neutrons. Their proton counts are equal, which preserves the element's identity. Their mass numbers differ because the proton-plus-neutron totals differ. For example, two silicon nuclei can each contain 14 protons while one contains 14 neutrons and another contains 15. Their mass numbers are 28 and 29, so they are silicon-28 and silicon-29.

If both atoms are neutral, each contains 14 electrons. Their electron counts do not differ merely because the nuclear neutron counts differ. In this model their electron arrangements are the same, which is why isotopes have very similar ordinary chemical behaviour. This statement concerns chemistry governed by electron arrangement; it does not claim identical masses or identical nuclear properties.

Contrast that with a magnesium atom and a magnesium 2+ ion made from the same isotope. Both nuclei contain 12 protons and the same number of neutrons. The atom has 12 electrons and the ion has 10. That pair differs in charge, not in isotope identity. A species can therefore be described by both an isotope label and an ionic charge: neither description replaces the other.

To decide whether two listed species are isotopes, compare their proton numbers first. If the proton numbers differ, they are different elements even if their nucleon numbers happen to match. If proton numbers match, compare neutron numbers or A values. Equal proton and neutron numbers indicate the same isotope; an electron-count difference alone indicates different charge states. This order of checking prevents the vague explanation that isotopes merely have different masses. Their nuclear distinction is specifically a difference in neutron number at fixed proton number.''')],S,'§2.3, printed pp. 82–84')

t.objective('2-03',[
    'In isotope notation A is written at the upper left of the element symbol and Z at the lower left; ionic charge is written at the upper right.',
    'A hyphenated isotope name gives the element and its nucleon number, while the element fixes the proton number.',
    'The mass-number label and ionic-charge label refer to different particle counts.',
], [('Reading and writing isotope symbols', '''A compact isotope symbol places the nucleon number A at the upper left and the proton number Z at the lower left of the element symbol X. A charge, when present, appears at the upper right. In plain text we can write [A=37, Z=17]Cl− without losing the positions' meanings. In typeset form the same species is ³⁷₁₇Cl⁻. It is a chloride ion whose nucleus contains 17 protons and 20 neutrons, and whose surrounding electron region contains 18 electrons.

The left-hand numbers describe the nucleus; the right-hand charge describes the proton–electron imbalance. Do not subtract the ionic charge from the neutron count. To interpret ²⁴₁₂Mg²⁺, first identify 12 protons, then calculate 24 − 12 = 12 neutrons. Only then adjust electrons: 12 − 2 = 10. This separates the three pieces of information instead of trying to treat the whole symbol as a single arithmetic expression.

An isotope may also be named using a hyphen, such as chlorine-37. Here 37 is the nucleon number. The element chlorine supplies Z = 17 through its identity. The name by itself does not state an ionic charge. If a task asks for an atom, the electron count equals Z; if an ion is specified, the charge must be supplied separately. A periodic table can supply the proton number but a decimal relative atomic mass must not be substituted for a missing isotope mass number.

For a reverse example, a species has 11 protons, 12 neutrons and 10 electrons. Its symbol uses Na because Z is 11, A is 11 + 12 = 23, and its charge is 11 − 10 = +1. Write ²³₁₁Na⁺. Verify the full symbol by reading it back into the three original counts. This gives a practical check on both number placement and charge placement.''')],S,'§2.3, printed pp. 82–83; isotope examples are original')

t.objective('3-01',[
    'Shell 1 contains an s subshell; shell 2 contains s and p; shell 3 contains s, p and d.',
    'An s subshell contains one orbital, a p subshell three and a d subshell five.',
    'The 4s and 4p subshells belong to shell 4, even though 4s fills before 3d in the introductory ground-state filling sequence.',
], [('Shell, subshell and orbital are different levels of organisation', '''A shell is labelled by its principal quantum number n. Within a shell, electrons can occupy subshells named s, p and d over the range needed here. A subshell contains one or more orbitals. Keep those three terms in that order: shell, then subshell, then orbital. An orbital is a region described by an electron probability distribution, rather than a circular track followed by an electron.

Shell 1 has a 1s subshell containing one orbital. Shell 2 has 2s and 2p subshells, containing one and three orbitals respectively. Shell 3 has 3s, 3p and 3d subshells, containing one, three and five orbitals. Thus shell 3 has nine orbitals across the subshells considered here, not three. The three is the number of subshell types; it is not the number of individual orbitals.

| Shell | Subshells considered | Orbitals in each subshell |
|---|---|---|
| 1 | 1s | 1 |
| 2 | 2s, 2p | 1, 3 |
| 3 | 3s, 3p, 3d | 1, 3, 5 |
| 4, selected subshells | 4s, 4p | 1, 3 |

The leading number is part of the label. Both 2p and 3p contain three p orbitals, but they belong to different shells and differ in energy and spatial extent. Similarly, 4s does not belong to shell 3 simply because it appears near 3d in a filling sequence. Subshell labels tell us the shell and the orbital type; a filling order tells us which available states are occupied first in the model being used.

For a quick check, a statement that 3d has ten orbitals has confused capacity with orbital count. It has five orbitals, each able to hold at most two electrons. Conversely, saying shell 2 contains two orbitals has confused subshell count with orbital count: 2s plus 2p contains four orbitals in total.''')],S,'§§6.3–6.4, printed pp. 302–313')

t.objective('3-02',[
    'An s orbital has a spherical probability distribution about the nucleus.',
    'A p orbital is represented by two lobes on opposite sides of the nucleus.',
    'The three p orbitals in a subshell have mutually perpendicular orientations and equal energy in the isolated-atom model used here.',
], [('Representing s and p orbitals', '''An orbital drawing represents where an electron is likely to be found, using a chosen boundary around a region of relatively high probability. It is not a solid container, a planet-like orbit, or a photograph of an electron's path. A simple s-orbital boundary is spherical, centred on the nucleus. A circle on a flat page is a cross-section or outline of that spherical shape; label it so that the intended three-dimensional form is clear.

A simple p-orbital boundary has two lobes, one on each side of the nucleus. The whole two-lobed shape is one orbital, not two orbitals. This distinction matters when counting capacity: the two lobes do not permit four electrons. The orbital as a whole holds at most two. The three orbitals of a p subshell can be labelled pₓ, pᵧ and p_z to indicate three perpendicular directions in space. Their different orientations do not make them different-energy subshells in this model.

![Original s-orbital and p-orbital outlines](assets/8224-orbitals.png)

When sketching an s orbital, show a round outline centred on a labelled nucleus and state that it represents a sphere. When sketching a p orbital, put two lobes on opposite sides of the same nuclear centre. A sketch of two separated circles with no common centre can mistakenly suggest two separate orbitals or atoms. Avoid that ambiguity with the label and a common central point.

The boundary is schematic. An electron is not confined to a hard outer wall at the drawn line. For the shapes required here, the important information is spherical symmetry for s and a two-lobed shape for p. Detailed mathematical wavefunctions are unnecessary for interpreting the diagram. The distinction becomes useful in Topic 1.3 when orbital overlap is connected to covalent bonding; that bonding discussion should not turn the orbital shape into a literal electron trajectory.''')],S,'§6.3, printed pp. 305–309, orbital shape discussion')

t.objective('3-03',[
    'One atomic orbital accommodates at most two electrons.',
    'When two electrons occupy the same orbital, they are represented with opposite spin arrows in a box diagram.',
], [('What one box represents', '''In an electrons-in-boxes representation, one box stands for one orbital and each arrow stands for one electron. An empty box is an unoccupied orbital. A box containing one arrow is singly occupied. A box containing two opposite arrows is doubly occupied. The two-electron limit belongs to a single orbital, regardless of whether it is an s orbital or one member of a p or d set.

Use [↑↓] to represent a filled orbital. The arrows indicate opposite spins; they are not an assertion that one electron is travelling upwards through the atom while another travels downwards. Two arrows pointing in the same direction in one box do not represent an acceptable paired arrangement. Three arrows in one box exceed the orbital's capacity, even if their directions are varied.

As a small example, the 1s orbital of hydrogen is represented by [↑]. Helium has 1s [↑↓]. Both examples contain one s orbital; the electron occupancy has changed. Removing an electron from a filled orbital leaves a singly occupied orbital rather than splitting the orbital into two new boxes. The boxes are a counting and arrangement representation of the available orbitals.

Keep the orbital limit separate from subshell capacity. A p subshell can contain six electrons because it contains three orbitals, not because a p orbital has room for six. If a diagram shows a single box labelled 2p with six arrows inside it, redraw that subshell as three adjacent boxes and distribute the electrons using the filling rules. Checking the number of boxes before counting arrows prevents capacity and occupancy from being mixed.''')],S,'§6.4, printed pp. 310–315, orbital diagrams and Pauli principle')

t.objective('3-04',[
    'The maximum electron capacities of s, p and d subshells are 2, 6 and 10, from one, three and five orbitals respectively.',
    'Occupied-orbital count and electron count are different quantities; a singly occupied orbital contributes one to both counts.',
], [('Counting orbitals and counting electrons', '''The capacity of a subshell comes from its number of orbitals multiplied by two. An s subshell contains one orbital and can hold two electrons. A p subshell contains three orbitals and can hold six. A d subshell contains five orbitals and can hold ten. The numbers 1, 3 and 5 therefore belong to an orbital-count column, while 2, 6 and 10 belong to a maximum-electron-count column.

Capacity is not the same as present occupancy. A p subshell that currently contains two electrons still has three available orbitals and a capacity of six. Following the ground-state filling rule, its two electrons occupy two different boxes, leaving the third empty. It then has two occupied orbitals and two electrons. A p⁴ subshell has three occupied orbitals, four electrons, and a remaining capacity for two more electrons.

To analyse a box diagram, first count the boxes that contain at least one arrow. That gives the number of occupied orbitals. Then count every arrow. That gives the electron count. For [↑↓] [↑] [↑], there are three occupied orbitals and four electrons. Reporting four occupied orbitals would be impossible because only three orbital boxes are present.

For a complete s²p⁶ set within one shell, add the subshell orbital counts to obtain 1 + 3 = 4 occupied orbitals. Add electron counts separately to obtain 2 + 6 = 8 electrons. The different totals are expected. This method also works for a filled d subshell: five occupied boxes contain ten electrons. Writing the quantity beside each number is a useful safeguard whenever the task switches between orbitals, subshells and electrons.''')],S,'§§6.3–6.4, printed pp. 304–317')

t.objective('3-05',[
    'For a given subshell type, the introductory shell model places higher principal-shell states at higher energies.',
    'Within a given shell of a many-electron atom, the s subshell is lower in energy than p, and p lower than d where present.',
    'Subshells from different principal shells can interleave in the ground-state filling sequence, so shell number alone does not determine that sequence.',
], [('Energy comparisons need the right scope', '''Electrons in an atom occupy allowed energy states rather than a continuous range of arbitrary energies. In the introductory comparisons used here, moving from a lower principal shell to a higher one of the same subshell type increases energy. Thus 1s lies below 2s, which lies below 3s. Within one shell of a many-electron atom, the ordering is s below p below d for the subshells present. For example, within shell 3, write 3s below 3p below 3d.

These are two related comparisons, and their assumptions matter. They do not justify sorting every subshell solely by the first number. In the familiar ground-state building sequence, 4s is occupied before 3d. An energy diagram showing the filling sequence must accommodate that overlap between shells. It must not show every third-shell subshell automatically below every fourth-shell subshell.

A useful way to check an ordering is to compare like with like before considering the complete sequence. For 2s versus 2p, both labels belong to shell 2 and the s state is lower. For 2s versus 3s, the labels share the subshell type and 2s is lower in the model. For 3d versus 4s, use the actual ground-state filling convention instead of either shortcut taken on its own.

Do not transfer the filling diagram unchanged into a claim about electron removal from every ion. The energies depend on the species and its occupation. For the iron examples below, 4s fills before 3d in the introductory construction but its electrons are removed before the 3d electrons when the cations form. Keeping construction and removal as distinct operations avoids an apparent contradiction. The configuration records the electrons remaining in the particular atom or ion, rather than a permanent universal ladder of subshell energies.''')],S,'§6.4, printed pp. 311–318')

t.objective('3-06',[
    'The ground-state building sequence through 4d is 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, subject to known exceptions.',
    'Within an equal-energy subshell set, electrons occupy orbitals singly with parallel spins before pairing.',
    'Iron is [Ar]3d⁶4s², Fe²⁺ is [Ar]3d⁶ and Fe³⁺ is [Ar]3d⁵; the 4s electrons are removed first.',
    'Chromium and copper have the ground-state configurations [Ar]3d⁵4s¹ and [Ar]3d¹⁰4s¹ respectively.',
], [('Building a ground-state arrangement and forming an ion', '''Start an electron configuration by counting the electrons in the species. Then place them in the available orbitals using the ground-state building sequence. Through the range required here, the working sequence is 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d. The sequence indicates where to place the next electrons in this construction; it does not replace the maximum capacities of the subshells.

Within the three p orbitals of a subshell, put one electron in each before pairing. A p³ arrangement is [↑] [↑] [↑], and a p⁴ arrangement can be [↑↓] [↑] [↑]. The location of the paired box may be permuted among the equivalent p orbitals without changing the basic occupancy. The same single-occupancy-before-pairing reasoning applies to the five equal-energy d orbitals. A d⁶ arrangement has one paired box and four singly occupied boxes.

For iron, Z = 26 gives 26 electrons in the neutral atom. An argon core accounts for 18. The remaining eight are distributed as 3d⁶4s². Forming Fe²⁺ removes two electrons, and the 4s electrons are removed first, leaving [Ar]3d⁶. Forming Fe³⁺ removes one further electron from 3d, leaving [Ar]3d⁵. Check the total: 18 + 6 = 24 electrons for Fe²⁺, and 18 + 5 = 23 for Fe³⁺. Both totals reproduce the expected positive charge.

The simple construction has known ground-state exceptions. Chromium, Z = 24, is [Ar]3d⁵4s¹ rather than [Ar]3d⁴4s². Copper, Z = 29, is [Ar]3d¹⁰4s¹ rather than [Ar]3d⁹4s². Use these observed configurations rather than applying the building sequence mechanically. The exceptions do not alter electron conservation: chromium still has 18 + 5 + 1 = 24 electrons and copper has 18 + 10 + 1 = 29.

When checking a proposed diagram, look separately for a capacity error, premature pairing and an incorrect total electron count. An arrangement may have the right total while pairing electrons too early within an equal-energy set. Another may follow the single-occupancy pattern but contain an extra electron. These are different defects and require different corrections. A final count of every occupied subshell is therefore useful even after the diagram looks plausible.''')],S,'§6.4, printed pp. 313–318; chromium also SRC-8224-ER-2025 Paper 2 Q2(c)(i), p. 75')

t.objective('3-07',[
    'The superscript on a subshell label gives its electron count; summing the superscripts gives the species total.',
    'For a monatomic ion, the configuration must account for Z minus its signed charge electrons.',
    'An oxygen atom has 1s²2s²2p⁴, with one paired and two singly occupied orbitals in 2p.',
], [('Moving between configurations and box diagrams', '''The configuration 1s²2s²2p⁴ describes eight electrons: two in 1s, two in 2s and four in 2p. It therefore represents the neutral oxygen atom when Z = 8. In plain text, 1s2 2s2 2p4 conveys the same subshell occupancies, provided the groups are separated clearly. A superscript is the number of electrons occupying the whole subshell, not the number of orbital boxes to draw.

Oxygen's box representation is 1s [↑↓], 2s [↑↓], 2p [↑↓] [↑] [↑]. First the inner s subshells fill. The first three 2p electrons occupy separate boxes, and the fourth pairs in one of them. All three 2p boxes are occupied, but only one is doubly occupied. The atom has two unpaired electrons in this representation.

For O²⁻, count electrons before writing the configuration: 8 + 2 = 10. The arrangement is 1s²2s²2p⁶, with 2p [↑↓] [↑↓] [↑↓]. For Mg²⁺, Z = 12 and the electron count is 12 − 2 = 10, giving the same arrangement. Equal configurations do not make these species the same element: their nuclei still have different proton numbers. Their isotope neutron counts also cannot be read from the electron configuration alone.

For a transition-metal example, Fe³⁺ contains 26 − 3 = 23 electrons. Expand [Ar]3d⁵ as 1s²2s²2p⁶3s²3p⁶3d⁵. The five d electrons occupy five separate boxes in the ground-state representation. No 4s electrons remain. If you are given a configuration and asked for charge, reverse the arithmetic: the difference between Z and the total electron count gives the signed charge.

Finish each configuration problem with three checks. The subshell capacities must be respected. The total electrons must match the nucleus and charge. The box diagram must represent the same distribution as the written configuration, including the arrangement within a partially filled p or d subshell. These checks connect the notation to the particle model rather than treating electron configurations as strings to memorise. Topic 1.3 uses the outer electrons to explain bonding, and Topic 3.1 uses configurations to interpret periodic behaviour.''')],S,'§6.4, printed pp. 313–318; original examples and count checks')

cards={
'001':('Describe the relative masses and charges of a proton, neutron and electron.','Proton: approximate relative mass 1, charge +1. Neutron: approximate relative mass 1, charge 0. Electron: approximate relative mass 1/1836, charge −1.'),
'002':('Explain why an electron contributes little mass to an atom although its charge balances that of one proton.','Its mass is only about 1/1836 of a proton mass, whereas its charge has equal magnitude and the opposite sign. Small mass and small charge are different comparisons.'),
'003':('State where most of the mass of an atom is concentrated.','In its nucleus, where the protons and neutrons are located.'),
'004':('Suggest how a particle model can show a neutral atom with a positively charged central nucleus.','Place equal numbers of protons in the nucleus and electrons outside it. The positive and negative charges balance for the whole atom.'),
'005':('State the relationships for proton, neutron and electron counts when A, Z and signed charge q are known.','Protons = Z; neutrons = A − Z; electrons = Z − q, with q positive for cations and negative for anions.'),
'006':('Determine the proton, neutron and electron counts for a species with A = 31, Z = 15 and charge 3−.','15 protons, 16 neutrons and 18 electrons: 31 − 15 = 16 and 15 + 3 = 18.'),
'007':('Describe the paths of an electron, proton and neutron entering horizontally between oppositely charged electric plates at equal speeds.','Electron towards the positive plate; proton towards the negative plate; neutron straight. The electron is deflected more strongly than the proton under the stated equal-speed assumptions.'),
'008':('Sketch the paths of an electron, proton and neutron entering horizontally between a positive upper plate and a negative lower plate at equal speeds. Label the plates and paths.','![Particle-path sketch](assets/8224-electric-field.png)\nElectron bends upwards more strongly, proton downwards less strongly, neutron straight. Bending starts on entering the field; distances are schematic.'),
'009':('Describe what the proton number and nucleon number tell you about a nucleus.','Z counts its protons and identifies the element. A counts protons plus neutrons. Their difference A − Z gives the neutrons.'),
'010':('Explain why adding a neutron to an oxygen nucleus changes its mass number but not its proton number.','The extra particle adds one nucleon but no proton. The proton count stays 8, so the nucleus remains oxygen, while A increases by one.'),
'011':('Describe the nuclear difference between two isotopes of the same element.','They have equal proton counts but different neutron counts, so their nucleon numbers differ.'),
'012':('Contrast isotope differences with differences between an atom and a monatomic ion made from it.','Isotopes differ in neutron number at fixed proton number. An atom and an ion of the same isotope differ in electron count and charge while the nucleus is unchanged.'),
'013':('State what A, Z and q represent in isotope notation [A,Z]X with charge q.','A is nucleon number; Z is proton number; q is the signed ionic charge. A and Z describe the nucleus, while q relates proton and electron counts.'),
'014':('Suggest the full isotope notation for a sodium species containing 11 protons, 12 neutrons and 10 electrons.','²³₁₁Na⁺, or [A=23,Z=11]Na+. Its charge is +1 because 11 − 10 = 1.'),
'015':('State which s, p and d subshells exist in shells 1, 2 and 3.','Shell 1: 1s. Shell 2: 2s and 2p. Shell 3: 3s, 3p and 3d.'),
'016':('Suggest how to correct a diagram that places 4s inside shell 3 because it fills before 3d.','Place 4s in shell 4 and retain 3d in shell 3. Principal-shell membership comes from the leading number; the filling sequence is a separate ordering.'),
'017':('Identify the shapes of an s orbital and a p orbital.','An s orbital is spherical about the nucleus; a p orbital is represented by two lobes on opposite sides of the nucleus.'),
'018':('Draw an s-orbital outline and a p-orbital outline, showing the nuclear centre.','![Original orbital outlines](assets/8224-orbitals.png)\nThe s outline represents a sphere. Both p lobes belong to one orbital and share a nuclear centre.'),
'019':('State the maximum number of electrons that one orbital can hold.','Two electrons, represented with opposite spin arrows when both occupy the orbital.'),
'020':('Suggest a correction to the orbital box [↑↑].','Change it to [↑↓] to show two electrons with opposite spins in the same orbital.'),
'021':('State the orbital counts and maximum electron counts for s, p and d subshells.','s: 1 orbital, 2 electrons; p: 3 orbitals, 6 electrons; d: 5 orbitals, 10 electrons.'),
'022':('Suggest how many orbitals are occupied in a ground-state p⁴ subshell and how many are doubly occupied.','All three p orbitals are occupied, with one doubly occupied and the other two singly occupied.'),
'023':('State the relative energy order of 3s, 3p and 3d in the many-electron-atom model.','3s below 3p below 3d, comparing subshells within the same principal shell.'),
'024':('Suggest why sorting every subshell solely by shell number gives an incorrect introductory filling sequence.','Subshells from adjacent shells interleave: 4s is occupied before 3d in the introductory ground-state building sequence.'),
'025':('State how electrons occupy the equal-energy orbitals of a p subshell before pairing.','One electron enters each of the three orbitals with parallel spins before a second electron pairs in any of them.'),
'026':('Suggest the subshell electron arrangement of Fe²⁺, given Z(Fe) = 26 and Fe = [Ar]3d⁶4s².','[Ar]3d⁶. The two 4s electrons are removed first, leaving 24 electrons in the ion.'),
'027':('State the electron configuration and 2p box arrangement of a neutral oxygen atom, Z = 8.','1s²2s²2p⁴; 2p [↑↓] [↑] [↑]. Pairing in an equivalent alternative p box represents the same occupation.'),
'028':('Suggest the configuration of an ion with Z = 12 and charge 2+.','It has 12 − 2 = 10 electrons: 1s²2s²2p⁶.'),
'029':('Explain the error in a table giving neutron relative mass 0 and electron relative mass 0.','The neutron mass is approximately 1 and its charge is 0; the electron mass is about 1/1836, not zero. The discriminating check is whether the column asks for mass or charge.'),
'030':('Explain the error in showing equally bent electron and proton paths when they enter the same electric field at equal speeds.','The charges have equal magnitude, but the electron has a far smaller mass and is deflected more strongly towards the opposite plate. Test which particle has the smaller mass for the same charge magnitude.'),
'031':('Explain why [Ar]3d⁴4s² should not be used as the ground-state configuration of chromium, Z = 24.','Chromium is a known exception: its ground state is [Ar]3d⁵4s¹. Both strings total 24 electrons, so counting alone cannot distinguish them; check the known ground-state exception.'),
'032':('Explain the error in saying a full p subshell contains six occupied orbitals.','The error confuses electrons with orbitals. A full p subshell contains six electrons in three occupied orbitals. Test the requested quantity: boxes count orbitals; arrows count electrons.'),
}
for slot in t.wo['item_slots']:
    n=slot['slot'].split('-')[-2];prompt,answer=cards[n]
    subtype='WHY' if n in ('002','010') else None
    if subtype:t.deviations.append({'from':slot['slot']+' subtype MECH with electron movement/intermediate/product rubric','to':'WHY, with reason/because/effect guidance; objective, AOs, Bloom level, command and tariff retained','why':'Particle masses and nucleon counting explain properties rather than a reaction mechanism. A reaction-intermediate rubric would be chemically misleading.'})
    t.item(slot,prompt,answer,subtype=subtype)

mcqs=[
('What is the maximum electron count in one orbital?',['1','2','3','6'],'B','B: one orbital accommodates two electrons. A confuses single occupancy with capacity; C counts p orbitals; D gives p-subshell capacity.'),
('How many orbitals make up a d subshell?',['2','3','5','10'],'C','C: a d subshell has five orbitals. A is one-orbital electron capacity; B counts p orbitals; D is d electron capacity.'),
('Which pair gives the orbital count and electron capacity of a p subshell?',['3 and 6','6 and 3','1 and 2','5 and 10'],'A','A is correct. B reverses the quantities; C describes s; D describes d.'),
('Which box shows an allowed two-electron occupancy of one orbital?',['[↑↑]','[↑↑↓]','[↑]','[↑↓]'],'D','D has two opposite spins. A shows equal spins in one box; B exceeds capacity; C is allowed but contains only one electron.'),
('A p⁴ set is [↑↓] [↑] [↑]. How many orbitals are occupied?',['1','2','3','4'],'C','C: all three boxes contain electrons. A counts paired boxes; B counts singly occupied boxes; D counts electrons.'),
('A filled s subshell and a filled p subshell in one shell contain how many occupied orbitals in total?',['2','4','6','8'],'B','B: 1 + 3 = 4 orbitals. A counts subshells; C is the p electron capacity; D is the combined electron count.'),
('Five d orbitals each contain one electron. How many more electrons can this subshell accommodate?',['0','2','5','10'],'C','C: five further electrons can pair, bringing the total to ten. A treats single occupation as full; B is one-orbital capacity; D forgets the five electrons present.'),
('Which statement about a subshell containing three p electrons follows from the capacity rule?',['Each orbital must hold three electrons','The subshell has six orbitals','The subshell cannot accept another electron','The subshell can accommodate up to three further electrons'],'D','D: capacity six minus occupancy three leaves three spaces. A exceeds orbital capacity; B doubles the orbital count; C confuses present occupancy with full capacity.'),
]
prompt='Identify the correct option in each of these eight questions. Each question has one correct option. [8]\n\n'+'\n\n'.join(f'{n}. {q}\n'+'\n'.join(f'{chr(65+k)}. {a}' for k,a in enumerate(opts)) for n,(q,opts,key,exp) in enumerate(mcqs,1))
answer='Key: '+', '.join(f'{n} {key}' for n,(_,_,key,_) in enumerate(mcqs,1))+'.\n\n'+'\n'.join(f'{n}. {exp}' for n,(_,_,_,exp) in enumerate(mcqs,1))
t.item(t.wo['performance_tasks'][0],prompt,answer,guidance=['Key: one mark for each correct option. Correct option and every distractor error are explained in the canonical answer; a distractor has no partial credit.'])
t.item(t.wo['performance_tasks'][1],
'''A species has A = 34, Z = 16 and charge 2−. Explain your reasoning in the following linked parts.
(a) State its proton, neutron and electron counts. [3]
(b) Explain why most of its mass is in the nucleus. [2]
(c) State its electron configuration and explain the occupancy of its outer p subshell. [3]''',
'''(a) 16 protons, 18 neutrons and 18 electrons. n = 34 − 16; electrons = 16 + 2. (b) Protons and neutrons are in the nucleus and each is much heavier than an electron, so the nuclear particles supply almost all the mass. (c) 1s²2s²2p⁶3s²3p⁶. The outer p subshell has three orbitals; each contains a pair of opposite-spin electrons.''',
guidance=['Part (a): one mark for each correct particle count. Part (b): one mark for nuclear protons/neutrons and one for their much greater mass than electrons. Part (c): one mark for configuration, one for three p orbitals and one for paired opposite spins. Each mark corresponds to a distinct creditworthy point.'])
t.item(t.wo['performance_tasks'][2],
'''Calculate the following quantities for a neutral atom with A = 24 and Z = 12. Use approximate relative masses: proton 1, neutron 1, electron 1/1836.
(a) Calculate its neutron count and electron count. [2]
(b) Calculate the approximate percentage of the particle-sum mass located in its nucleus. [2]
(c) For an electron and proton entering the same uniform electric field at equal speeds, a simple force model gives equal force magnitudes. Calculate their electron-to-proton acceleration ratio, using acceleration = force/mass. [1]''',
'''(a) Neutrons = A − Z = 24 − 12 = 12; electrons = Z = 12. These counts are exact integers. (b) Nucleus relative mass = 12 + 12 = 24. Electron contribution = 12/1836 = 0.00653595. Fraction in nucleus = 24/(24 + 0.00653595) = 0.9997277. Percentage = 99.97277%, or approximately 99.97%. This is an approximate particle-sum model, not a measured isotope mass. (c) a(electron)/a(proton) = m(proton)/m(electron) = 1/(1/1836) = 1836, approximately 1.84 × 10³ to three significant figures. The ratio is dimensionless. The lighter electron bends more strongly; its negative charge determines the opposite direction.''',
guidance=['Equation and working: (a) n=A−Z and electron count, one mark each; (b) particle-sum expression with electron mass included, one mark, and approximately 99.97%, one mark; (c) acceleration ratio 1836, one mark. Answer and unit: counts and ratios have no physical unit, percentage uses %. Significant figures: counts are exact; mass-sum percentage is approximate and the acceleration ratio may be rounded to three significant figures. No unit conversion is needed because all masses are already relative values.'])

assets=t.dir/'assets';assets.mkdir(exist_ok=True)
for ext in ['png','svg','geometry.json']:
    shutil.copy2(WS/'exemplar/visual/assets'/('8224-electric-field.'+ext),assets/('8224-electric-field.'+ext))
f=Figure('s and p orbital outlines','An s orbital is represented as a sphere, here shown by a circular outline around the nucleus. A p orbital is a single two-lobed orbital about one nucleus. Boundary shapes are schematic.')
import math
f.line([(235+85*math.cos(a*math.pi/90),225+85*math.sin(a*math.pi/90)) for a in range(181)],width=3)
f.circle(235,225,5);f.text(165,335,'s: spherical',23)
for side in [-1,1]:
    f.line([(590+side*(5+105*(1+math.cos(a*math.pi/90))/2),225+58*math.sin(a*math.pi/90)) for a in range(181)],width=3)
f.circle(590,225,5);f.text(515,335,'p: two lobes',23);f.text(26,418,'Dots mark nuclei. One two-lobed p shape is one orbital; diagrams are schematic.',17)
f.save('8224-orbitals',out=assets)
t.save()
