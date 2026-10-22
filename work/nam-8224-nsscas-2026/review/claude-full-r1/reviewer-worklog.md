# Claude reviewer worklog (scratch; consolidated into REVIEW.md / findings.json / coverage.json)

## Global
- preflight: 21/21 decision publish; 0 fail; 21 C-18 warn; 63 not_run (C-35, C-41, C-43 in every topic). C-41 says "no item shows a generated depiction" although 30 figures exist -> checker blind to these PNG/SVG; C-35 "no graphical task" even in 5.1.
- metadata-completeness: 631 items, 0 metadata mismatches; 51 subtype changes, all MECH->WHY (1.2:2, 1.3:7, 1.4:1, 2.1:3, 2.2:1, 2.3:4, 2.4:8, 3.1:9, 3.2:1, 3.3:1, 3.4:3, 3.5:4, 4.2:3, 4.3:1, 4.4:1, 4.5:1, 4.7:1).
- copied wording: 10 runs 8-10 words, 0 >=12.

## 1.1 (read all 5 CUs / 34 blocks, 27 claims, 20 sampled items, authoring_notes)
Sampled: 026-MISCON, 008-CALC, 027-MISCON, 011-CALC, 016-CALC, 019-EQUATION, 021-CALC, 022-CALC, 023-CALC, 025-MISCON, P01, P02, P03, 001-DEF, 002-APP, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE
Arithmetic checked: CO2 44.0; MgO 40.3; 0.250*NA=1.505e23; 4.50/18=0.250; Na2CO3 0.200 mol Na+ =1.204e23; Ar 24.32; 827/13=63.615; NH4NO3 35.0%; CaCO3 O 47.95%; Cl 35.5 both ways; Al2(SO4)3 342.3 & 15.8%; CH2O ratios; C6H12O6; combustion 2:5; O by difference; CaO 14.0 g; O2 16.8/15.68 dm3; n=cV 0.00375; c 0.150; limiting NH3 0.600; Cu 63.6; CaO 5.60 g; O2 12.0 dm3; 4.20e-3; P02 C4H8; P03 2.25 g H2 limiting. All correct.
Minor: 15.68 dm3 (1.1.5-b5) and 1.204e23 (1.1.2-b5, 004-APP) shown at 4 s.f. from 3 s.f. data while notes stress sf -> low.
Mole definition = Avogadro-constant number of specified entities (post-2019 consistent). OK.

## 1.2 (rendered notes read in full = 14 blocks in 3 CUs; 40 claims; 20 sampled; 2 deviations)
Sampled: 029-MISCON, 030-MISCON, 008-DIAGRAM, 018-DIAGRAM, 032-MISCON, 031-MISCON, P01, P02, P03, 001-FEATURE, 002-MECH(WHY), 003-FEATURE, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 009-FEATURE, 010-MECH(WHY), 011-FEATURE, 012-DIST
Images: 8224-electric-field.png (correct: field arrow + to -, electron up stronger, proton down weaker, neutron straight, bending from entry); 8224-orbitals.png (s circle w/ nucleus; p two touching circles with nucleus at contact — schematic, acceptable; lobes would ideally be tear-drop; low).
Arithmetic: 10/1836=0.00545; Al3+ 13/14/10; S2- 16/18/18; P3- ; Fe2+/Fe3+ counts; Cr/Cu totals; P03 99.97%, ratio 1836. Correct.
Deviation MECH->WHY (002, 010): justified (property explanations, not reaction mechanisms) -> plan defect (planner assigned MECH to non-mechanism objectives).
No content issues found.

## 1.3 (rendered notes read in full: 6 CUs; 60 claims; 20 sampled; 8 deviations/clarifications)
Sampled: 012-DIAGRAM, 014-DIAGRAM, 051-MISCON, 052-MISCON, 042-DIAGRAM, 044-DIAGRAM, 046-DIAGRAM, 048-DIAGRAM, 050-DIAGRAM, P01, P02, P03, 001-FEATURE, 002-APP, 003-FEATURE, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 008-MECH(WHY)
Images: water-shape (bent, 2 LP, 104.5 OK); ionic-lattice (alternating +/- slice OK); metallic (+ centres, e- between, arrow; OK); molecular-separation ("I" glyph reads like a bar - low legibility only; caption clarifies).
Arithmetic: CaF2 1.50/78.1=0.0192; F- 0.0384; total ions 0.0576. OK.
Chemistry: shapes/angles correct (CO2 180, BF3 120, CH4 109.5, NH3 107, H2O 104.5, PF5, SF6); NH4+ tetrahedral; H3O+ pyramidal; Al2Cl6 two bridging Cl donating to Al (standard AS model; no exact local locator per author note -> source gap, not error); CO dative; H-bond donor/acceptor N,O,F; ice less dense; CHCl3 liquid/HCl gas.
C60/nanotube clarification: correct chemistry; registry grouping is a plan wording issue (record as plan problem, low).
MECH->WHY x7 justified.
FINDING (medium, curriculum): syllabus 1.3.6 (syllabus-layout.txt l.458-465) lists "simple molecular, including iodine and the fullerene allotropes of carbon (C60 and nanotubes only)". Notes (CU 1.3.6 'Reading the structural unit in a crystal' and 'Choosing the carrier...') present nanotubes as an "extended" framework contrasted with molecular and never tell learner the syllabus classifies them as fullerene/simple molecular. Learner asked to classify nanotube structure could contradict syllabus. Repair: add sentence stating syllabus grouping & reconciling (each tube is one very long covalent molecule; tubes attract one another by intermolecular forces). Author's clarification hides the syllabus classification -> plan defect (registry correct to syllabus; authoring deviation partially wrong).

## 1.4 (notes read in full, 1 CU 3 blocks; 9 claims; all 10 items)
Sampled: 006-CALC, P01, P02, P03, 001-FEATURE, 002-APP, 003-FEATURE, 004-MECH(WHY), 005-FEATURE, 007-INTERP
Arithmetic: n=0.0902527 -> 0.0903; M=43.877; P01 V=0.004986 m3=4.99 dm3; P02 p=132960 Pa; P03 n=0.0501404, M=49.86. All correct.
Source: syllabus l.341-344 Vm 22.4 s.t.p./24.0 r.t.p. (101 kPa & 273 K / 298 K); R=8.31 l.480. Notes consistent. 273.15 vs 273 accommodated.
No issues.

## 2.1 (notes read in full, 2 CUs ~12 blocks; 26 claims; 20 sampled; 5 deviations/clarifications)
Sampled: 006-CALC, 011-CALC, 014-CALC, 017-CALC, 020-CALC, P01, P02, P03, 001-FEATURE, 002-MECH(WHY), 003-FEATURE, 004-MECH(WHY), 005-FEATURE, 007-INTERP, 008-FEATURE, 009-MECH(WHY), 010-FEATURE, 012-INTERP, 013-FEATURE, 015-INTERP
Images: hess-cycle (A->C -120, A->B -45, B->C unknown; arrows correct); enthalpy-pathway (Ea arrow from reactant level to max, dH arrow reactants->products; scale consistent 3.5px/unit; "Enthalpy" label overlaps y-axis arrowhead - cosmetic).
Arithmetic: 1254 J -> -50.2; -185; 6.86%->6.9%; -75; -76; P01 400 J, -60; P02 -836 J; P03 -41.8 & x=-49.8; pathway Ea rev 120, endo 70. Correct.
Source: syllabus 2.1 (l.495-515) does not state standard pressure; notes use 100 kPa (IUPAC), syllabus elsewhere uses 101 kPa for s.t.p./r.t.p. -> low source-gap note (open, no repair).
Deviation 023-INTERP added unmarked construction practice: acceptable within slot (no metadata change).

## 2.2 (notes read in full, 2 CUs ~11 blocks; 28 claims; 20 sampled; 2 deviations)
Sampled: 002-CALC, 007-EQUATION, 022-MISCON, 019-EQUATION, P01, P02, P03, 001-FEATURE, 003-INTERP, 004-FEATURE, 005-MECH(WHY), 006-FEATURE, 008-FEATURE, 009-APP, 010-DEF, 011-APP, 012-FEATURE, 013-APP, 014-FEATURE, 015-APP
No images.
Arithmetic/equations: S +6; Cr +6; MnO4-/Fe2+ charge +17 both sides; nitrate(III)/(V), chlorate(I)/(V); half-equations (H+, H2O, Cl-, OH-, acid water oxidation) balanced; water 2:1; P02 0.0200 mol; P03 3.60e-4 -> 1.80e-3 mol. Correct.
Syllabus 2.2.2 (l.536-550) cathode list Ag, Cu, (H), Fe, Zn, Na; notes match school model and qualify Mn engineered recovery. OK. Manganese specifics: no plant recipe asserted -> source focus fine.
LOW tidiness: "sulphur/sulphate/sulphuric" spelling (39 occurrences in 7 rendered notes: 2.2,2.3,3.1,3.2,3.3,3.4,3.5) vs syllabus "sulfur/sulfuric" and the topic title "Nitrogen and sulfur"; inconsistent. Not repaired (cosmetic, broad).

## 2.3 (notes read in full, 2 CUs ~11 blocks; 26 claims; 20 sampled; 5 deviations)
Sampled: 010-CALC, 013-CALC, 026-MISCON, 024-CALC, P01, P02, P03, 001-FEATURE, 002-MECH(WHY), 003-FEATURE, 004-INTERP, 005-FEATURE, 006-APP, 007-FEATURE, 008-INTERP, 009-FEATURE, 011-INTERP, 012-FEATURE, 014-INTERP, 015-FEATURE
No images.
Arithmetic: Kc 16.0; Kp 0.400 kPa-1; partial pressures 50/150 kPa; x=0.800; P03 0.400 mol dm-3; ratio 2.5; 20 points vs 25%; pH 1.699; dilution pH 2.000; pH3 -> 1.0e-3. Correct.
Chemistry: K changes only with T; catalyst no change; Le Chatelier; Haber/Contact compromise; B-L acid-I/base-II labels correct. Contact catalyst not named here (check 3.5). Excluded Ka/buffers absent.
No issues.

## 2.4 (notes read in full, 3 CUs ~11 blocks; 26 claims; 20 sampled; 9 deviations/clarifications)
Sampled: 020-MISCON, 021-MISCON, 022-MISCON, 015-DIAGRAM, P01, P02, P03, 001-FEATURE, 002-MECH(WHY), 003-FEATURE, 004-MECH(WHY), 005-FEATURE, 006-MECH(WHY), 007-FEATURE, 008-MECH(WHY), 009-FEATURE, 010-MECH(WHY), 011-FEATURE, 012-MECH(WHY), 013-FEATURE
Images: boltzmann-temperature (origin start, higher-T lower/broader/right-shifted peak, curves cross, fixed Ea, shaded higher-T tail: correct; 'Lower T' label overlaps curve - cosmetic); boltzmann-catalyst (one curve, Ea cat left of Ea uncat, shaded extra interval: correct).
Arithmetic: 1.20 cm3/s; P02 0.00200 mol dm-3 s-1; P03 1.20, 1.80, ratio 1.50. Correct.
Misconceptions MC-11/12/13 discriminate by axes/area/fraction. OK. Enzyme range clarification appropriate.
No issues.

## 3.1 (notes read in full, 4 CUs ~17 blocks; 40 claims; 20 sampled; 10 deviations/clarifications)
Sampled: 016-EQUATION, 017-EQUATION, 037-MISCON, 022-EQUATION, 027-EQUATION, P01, P02, P03, 001-FEATURE, 002..012 (002,004,006,008,010,012 WHY; 003,005,007,009,011 FEATURE)
No images.
Arithmetic/equations: 600x0.0200=12.0 kJ; 738x0.0200=14.76->14.8 kJ; Na2O/MgO/Al2O3/P4O10/SO2/SO3; chlorides incl. Al2Cl6, P4+10Cl2->4PCl5; Na/water; Mg/steam; P4O10+6H2O; Al2O3 + 2OH- + 3H2O -> 2[Al(OH)4]- (balanced); P4O10+12NaOH; SiCl4+2H2O; PCl5+4H2O. All balanced/correct.
Chemistry: radius/IE/EN trends with shielding; isoelectronic ions; oxidation numbers max +1..+6 (Na-S) and chlorides +1..+5 matches syllabus l.655-657; MgCl2 weakly acidic; Al hydrolysis eqn. Paired-electron IE exclusion respected.
No issues.

## 3.2 (notes read in full, 2 CUs ~9 blocks; 23 claims; 20 of 21 sampled; 3 deviations/focus)
Sampled: 004-EQUATION, 005-EQUATION, P01, P02, P03, 001-FEATURE, 002-CHAIN, 003-FEATURE, 006-APP, 007-FEATURE, 008-APP, 009-FEATURE, 010-APP, 011-FEATURE, 012-INTERP, 013-FEATURE, 014-CHAIN, 015-FEATURE, 016-APP, 017-FEATURE
No images.
Arithmetic: 0.0250 mol CaCO3 -> 0.0500 H+; 10.0 g CaCO3 -> 5.60 g CaO, loss 4.40 g; 5.60 g CaO -> 7.40 g Ca(OH)2; P03 0.200 mol H+, 0.100 mol H2; Mg 650 / Ca 842 C (correct literature values). Nitrate equation O-balance correct.
(see 3.3 below)
Source focus check: nitrate pattern 2M(NO3)2->2MO+4NO2+O2 standard; hydroxide/sulfate solubility directions correct; Mg/Ca melting irregularity correct; cement stage description (CaO + silica/alumina at high T; hydration) generic and correct. No local locator -> verification remains author/human gate, no error found.
No issues.

## 3.3 (notes read in full, 2 CUs ~13 blocks; 32 claims; 20 of 25 sampled; 4 deviations/focus)
Sampled: P01, P02, P03, 001-FEATURE, 002-MECH(WHY), 003-FEATURE, 004-WHY, 005-FEATURE, 006-APP, 007-FEATURE, 008-DIST, 009-FEATURE, 010-APP, 011-FEATURE, 012-APP, 013-FEATURE, 014-APP, 015-FEATURE, 016-APP, 017-FEATURE
No images.
Arithmetic/equations: density 7.90, ratio 5.10; 2CuO+C; CuO+CO; Fe2O3+3C->2Fe+3CO; MnO+C; CuO+H2SO4; U4+/Mg 2:1; recycling 80.0%. Correct.
Chemistry: definition per syllabus l.703-704; Cu2+ 3d9 qualifies, Zn2+ 3d10 not; uranium actinide; Mg reduction of prepared compound (syllabus says "reduction of uranium ions using magnesium" l.719-720; notes reconcile). Recycling objective in syllabus l.726. OK.
No issues.

## 3.4 (notes read in full, 5 CUs ~15 blocks; 36 claims; 20 of 33 sampled; 4 deviations/focus)
Sampled: 010-EQUATION, 017-EQUATION, 018-EQUATION, 023-EQUATION, P01, P02, P03, 001-FEATURE, 002-APP, 003-FEATURE, 004-CHAIN, 005-FEATURE, 006-INTERP, 007-FEATURE, 008-APP, 009-FEATURE, 011-APP, 012-FEATURE, 013-MECH(WHY), 014-FEATURE (+ unsampled 015-INTERP read for repair)
No images.
Equations: displacements; H2+X2; Ag+ + Cl-; NaCl+H2SO4; 2HBr+H2SO4; 8HI+H2SO4->4I2+H2S+4H2O; cold/hot disproportionation; Cl2+H2O; ClO-+Cl-+2H+ — all balanced. 0.200 g/10 min=0.0200; 0.200/254=7.87e-4.
FINDING (medium, quantitative/curriculum): CU-8224-3.4.2 block "Interpreting bond-energy evidence" quotes H-Cl 432, H-Br 370, H-I 295 kJ/mol "in the local textbook table" (OpenStax Table 7.2 — verified at OpenStax-Chemistry.txt l.16400-16404) and derives 137 kJ/mol and 2.95 kJ. Official NSSCAS Data Booklet (syllabus-layout.txt l.2204-2209, printed p59) gives H-Cl 431, H-Br 366, H-I 299. Learners use the Data Booklet in the exam -> inconsistent values. ITEM-8224-3.4-015-INTERP also supplies 432/370/295. Repair to 431/366/299, 132 kJ/mol, 2.99 kJ.
LOW: 2.1 worked example and items 2.1-011-CALC, 2.1-P02 use "supplied" H-H 436, Cl-Cl 243, H-Cl 432 (OpenStax) vs Data Booklet Cl-Cl 242, H-Cl 431 (-> -184 vs -185). Values explicitly supplied, method correct; not repaired; recommend aligning to Data Booklet.
Chemistry: colours/state; AgX + NH3 solubility; conc H2SO4 behaviour; disproportionation; HOCl/ClO- pH; disinfection; CFCs. Correct.

## 3.5 (notes read in full, 2 CUs ~10 blocks; 29 claims; 20 of 23 sampled; 8 deviations/focus)
Sampled: 002-DIAGRAM, P01, P02, P03, 001-FEATURE, 003-FEATURE, 004-WHY, 005-FEATURE, 006-MECH(WHY), 007-FEATURE, 008-MECH(WHY), 009-FEATURE, 010-APP, 011-FEATURE, 012-MECH(WHY), 013-FEATURE, 014-MECH(WHY), 015-FEATURE, 016-APP, 017-FEATURE
Image: ammonium-tetrahedral (brackets, +, 2 in-plane, wedge narrow at N, hashed away; no LP; 109.5): correct.
Arithmetic: (NH4)2SO4 132, 21.2% N; 25.0 mol; 32.0 g S -> 64.0 g SO2; fuel 10.0/2.00 kg S -> 20.0/4.00 kg SO2; P03 0.0500 -> 0.100 mol NH3; 0.0200 mol. Correct.
Equations: NH3+H2O; NH4+ + OH-; NH4Cl+NaOH; 2NH3+H2SO4; NH3+HNO3; S+O2; 2SO2+O2+2H2O->2H2SO4; CaCO3+2H+. Balanced.
Oxidation numbers per syllabus l.780-781 (NH3 -3, N2 0, N2O +1, NO3- +5). WHO distinction appropriate; WHO URL is an external link in learner notes (noted, low).
FINDING (medium, curriculum gap) relates to 2.3: no topic names the Contact-process catalyst vanadium(V) oxide (0 occurrences of 'vanadium'/'V2O5' in topics/). Syllabus 2.3.1 (l.576-578) requires explaining choice of catalyst for Haber AND Contact; corpus 2023 P12 has an item on V2O5 catalyst effect (assessment_evidence.json l.5260). Haber iron catalyst is named. Local support: OpenStax-Chemistry.txt l.47400 "Vanadium oxide is used to produce ... sulfuric acid". Repair in 2.3 Contact block.

## 4.1 (notes read in full, 3 CUs ~7 blocks; 15 claims; all 14 items; 2 clarifications)
Sampled: 003-DIAGRAM, 007-DIAGRAM, 009-DIAGRAM, P01, P02, P03, 001-FEATURE, 002-MECH (genuine), 004-DEF, 005-APP, 006-FEATURE, 008-FEATURE, 010-FEATURE, 011-INTERP
Images: ethane-centre (tetrahedral wedge/hash, R=CH3; OK); tetrahedral-carbon.png is byte-identical-looking duplicate of ethane-centre and is not referenced in notes (low, unused asset); ethene-planar OK; bond-fission (fishhooks for homolysis, full head for heterolysis, arrows from bond; OK); ir-carbonyl (axis linear, 1720 dip at correct x; also 2900 and ~1100 bands; caption avoids unique structure; 'cm^-1' caret glyph cosmetic).
IR table in notes matches Data Booklet (syllabus-layout.txt l.2341-2356) exactly.
Arithmetic: P03 0.0500 mol, 5.45 g (C2H5Br 109). Correct. Names: propan-2-ol, 1-chlorobutane, 1,2-dichloropropane, ethyl ethanoate. Correct.
No issues.

## 4.2 (notes read in full, 3 CUs ~25 blocks; 53 claims; 20 of 60 sampled; 6 deviations/focus)
Sampled: 002-DIAGRAM, 010-EQUATION, 011-EQUATION, 015-DIAGRAM, 021-DIAGRAM, 027-EQUATION, 028-EQUATION, 034-DIAGRAM, 037-DIAGRAM, 057-MISCON, 051-EQUATION, P01, P02, P03, 001-FEATURE, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE
Images: alkane-representations (displayed ethane 6 H, skeletal butane 4 positions, C4H10: OK); propene-hbr-mechanism (pi->H, H-Br->Br, secondary C+, Br- lone pair -> C+: OK); pvc-repeat-unit (brackets crossed, n, Cl on one C: OK).
Arithmetic/equations: C5H12, C8H18, C4H9; 2C2H6+7O2; 2C2H6+5O2->4CO+6H2O; C10H22 cracking (Mr 142/86/56); diol [O]; but-2-ene+4[O]->2CH3COOH; propene+5[O]->CH3COOH+CO2+H2O; C3H8+5O2; 480/800=60.0%; 2CO+O2; 2NO+2CO->N2+2CO2; P03 C6H14 Mr 86.0, 2,2-dimethylbutane. All correct.
Mechanisms: radical chain with ethyl radical; Markovnikov via secondary cation & inductive effect; Br2/ethene taught via bridged bromonium (chemically supported). LOW/open assessment-alignment note: no mark schemes held; notes call open-carbocation "unsupported" — teacher check advisable; not an error.
LOW tidiness: ITEM-8224-4.2-P01 distractor feedback repeats filler "Each distractor identifies the stated naming error." x12 and missing spaces "carbons3 and4", "at2 and3"; ITEM-8224-4.2-P02 "total8 marks". Not repaired (cosmetic).
Cold dilute acidified MnO4- -> diol matches syllabus l.874 wording exactly.

## (resumed session after 429 quota stop)
## 4.3 (notes read in full, 2 CUs ~9 blocks; 20 claims; 20 of 22 sampled; 3 deviations/focus)
Sampled: 002-DIAGRAM, 009-DIAGRAM, P01, P02, P03, 001-FEATURE, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 008-MECH (genuine), 010-FEATURE, 011-INTERP, 012-FEATURE, 013-MECH(WHY), 014-FEATURE, 015-APP, 016-FEATURE, 017-APP
Images: bromoethane-displayed (5 H + Br, C2H5Br: OK); bromoethane-hydroxide (O lone pair -> C, C-Br -> Br, one step, no carbocation: OK).
Arithmetic: P03 Mr 108.9, n 0.0500459, ethanol 2.30 g. Correct. Names 1-bromo-3-chloropropane, 2-bromo-1-chloropropane, 1,2-dibromoethane, 2-bromobutane correct. C-Cl 340 / C-I 240 example consistent with Data Booklet (l.2235-2237).
Equations: OH-/CN-/2NH3 substitutions; 2-bromopropane elimination; Cl./O3 cycle -> O3+O->2O2. Correct; conditions (aqueous vs ethanolic, heat) carried.
LOW tidiness: P01/P02 filler "Each distractor reflects the specified error." and "total8 marks". No other issues.

## 4.4 (notes read in full, 1 CU 8 blocks; 17 claims; 20 of 24 sampled; 2 deviations/focus)
Sampled: 002-DIAGRAM, 008-EQUATION, 009-EQUATION, 019-MISCON, 020-MISCON, 021-MISCON, P01, P02, P03, 001-FEATURE, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 010-APP, 011-FEATURE, 012-WHY, 013-FEATURE, 014-DIST
Image: ethanol-displayed (5 C-H, C-O, O-H; OK).
Arithmetic/equations: combustion C2H5OH+3O2; HBr substitution; 2EtOH+2Na; [O] and 2[O]; dehydration; esterification; 0.200->0.100 mol H2; P03 4.60/46.0=0.100 -> 0.0500 mol H2. Correct.
Chemistry: classification by OH-carbon neighbours; tertiary resists mild oxidation; orange->green dichromate; iodoform CH3CH(OH)R incl. ethanol; pentan-3-ol negative; conc H2SO4 ~170 C / Al2O3; solvent explanation with qualified coal sulfur extraction (syllabus l.958-959). Correct.
Misconceptions MC-16 (dilute vs concentrated acid), MC-17 (yellow solution vs precipitate), MC-18 (CHI3 not iodobutane): each discriminates the wrong idea and is answerable from notes (blocks 'Ethanol as a reaction hub', 'The alkaline iodine test...').
No issues.

## 4.5 (notes read in full, 1 CU 7 blocks; 12 claims; all 15 items; 2 deviations)
Sampled: 002-DIAGRAM, 006-DIAGRAM, 010-DIAGRAM, P01, P02, P03, 001-FEATURE, 003-FEATURE, 004-APP, 005-FEATURE, 007-FEATURE, 008-MECH(WHY), 009-FEATURE, 011-FEATURE, 012-APP
Images: cis-trans-butene (correct same/opposite methyls); optical-mirror-pair (true reflection, wedge/hash consistent, C* marked: correct).
Counts: C4H10 2; open-chain C4H8 alkenes 3 connectivities / 4 forms (1+2+1). Correct. Excluded E/Z, diastereoisomers, meso not taught (only the syllabus NB about multiple centres). Calculation-slot deviation (exact counts) acceptable; it is a plan defect that a CALC task was assigned to an objective with no measured quantity.
No issues.

## 4.6 (notes read in full, 1 CU 4 blocks; 8 claims; all 11 items; no deviations)
Sampled: 002-DIAGRAM, P01, P02, P03, 001-FEATURE, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 008-APP
Image: carbonyl-connections (ethanal with C-H, propanone two CH3; OK).
Scope matches syllabus 4.6.1 (l.993-1000): no Tollens/Fehling/DNPH taught (correctly). Arithmetic: 0.100 mol -> 5.80 g propanone; P03 3.00/60.0 -> 2.90 g; C4H8O, C5H10O. Correct.
No issues.

## 4.7 (notes read in full, 2 CUs 10 blocks; 20 claims; 20 of 24 sampled; 1 deviation)
Sampled: 002-DIAGRAM, 010-EQUATION, 013-DIAGRAM, 017-DIAGRAM, 019-DIAGRAM, P01, P02, P03, 001-FEATURE, 003-DEF, 004-APP, 005-FEATURE, 006-INTERP, 007-FEATURE, 008-APP, 009-FEATURE, 011-APP, 012-FEATURE, 014-DEF, 015-APP
Image: acid-ester-amine (ethanoic acid, methyl ethanoate, ethanamine: OK).
Equations/arithmetic: 2[O] oxidation; aldehyde+[O]; Mg, NaOH, Na2CO3 salts; esterification; acid/base hydrolysis (base gives salt before acidification); 0.0500 mol -> 3.00 g; C3H6O2, C4H8O2, C2H7N, C4H11N; CnH2n+3N. Correct. Scope matches syllabus 4.7 (l.1003-1032).
No issues.

## 5.1 (notes read in full, 4 CUs ~37 blocks; 78 claims; 20 of 84 sampled incl. all 6 practical tasks; 3 deviations)
Sampled: 024-CALC, 026-CALC, 028-CALC, 030-CALC, 032-CALC, 034-CALC, 036-CALC, P01, P02, P03, P04, P05, P06, 001-PROC, 002-APP, 003-PROC, 004-APP, 005-PROC, 006-APP, 007-PROC
Images: practical-sequence (fresh portion -> dropwise -> excess: OK); practical-calibration (points lie on S=20.0c+0.10; 0.70 -> 0.030 correct; construction shows only horizontal line, no vertical drop to concentration axis - low); practical-linear-rate (5 points on 1/t=0.0500c through origin: OK); practical-tangent (V=60(1-e^-t/40), tangent through (0,15.9) and (80,60.0) touching at (40,37.9): OK; "at40s" missing space cosmetic). Axis "^-1/^-3" caret glyphs cosmetic.
Arithmetic (all recomputed): titres 24.65/24.70, mean 24.675; 0.0987 mol dm-3; mass loss 0.44, 0.45 g; 1/t; P02 titres 19.90/19.95 mean 19.925, n MnO4- 3.985e-4, Fe2+ 1.9925e-3, 0.0797; P03 q=2717 J, -54.3 -> ~-54 kJ/mol, 15% uncertainty; P04 reciprocals, slope 0.0500, 40 s, 2.5%; P06 0.500 cm3/s, 1.25%; V(40)=37.9, dV/dt=0.552, V(80)=51.9; gradient 0.400 & intercept 4; calibration 0.0300; 0.400% burette; 15%/50%. All correct.
Source alignment: burette 0.05 cm3, thermometer 0.5 C (syllabus l.1436-1437); concordant within 0.10 (l.1924); sf rule (l.1527-1531); Annexe D qualitative notes (l.2008-2067): Al/Zn NaOH & NH3, sulfate/sulfite, gas tests all match notes and P05.
FINDING (medium, curriculum alignment) in 3.4 (found via Annexe D): Annexe D l.2013-2018 says AgCl soluble in dilute NH3, AgBr "partially soluble in dilute ammonia", AgI insoluble in dilute NH3. 3.4 notes (CU 3.4.3 'Two distinct halide comparisons') say AgBr "dissolves appreciably in concentrated ammonia" and never give the board's dilute-ammonia description that learners see in Paper 3 notes.
LOW tidiness: many 5.1 item strings lack spaces before numbers ("readings0.20/24.85", "Total20 marks", "to3 significant figures") — likely stripped thin spaces; affects readability across 4.x/5.1 tasks.
