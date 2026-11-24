"""D4 planner text/metadata repair for the two retained calculus recipes.

No domain, tariff, learner item or runtime generation is changed. The common
MR03 policy is coordinated separately by the parent planner.
"""
from pathlib import Path
import json
H=Path(__file__).resolve().parent;P=H.parent;W=P.parent
read=lambda p:json.loads(p.read_text())
write=lambda p,d:p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
owned={'WB8227-implicit-normal','WB8227-stationary-inflexion'}
d=read(P/'calculus-design.json')
for r in d['recipes']:
 if r['recipe_id']not in owned:continue
 r['version']=r['proposed_version']='0.1.4'
 r['status']='D4 proposal; Claude changed-scope confirmation then Vitalis exact-manifest approval pending'
 for b in r['branches']:
  for q in b['part_specs']:
   for key in ['criterion_ids','fully_qualified_criterion_ids','bloom_criterion_ids']:
    if key in q:q[key]=[v.replace('@0.1.3:', '@0.1.4:')for v in q[key]]
   for key in ['criterion_id_rule','bloom_rationale']:
    if key in q:q[key]=q[key].replace('@0.1.3', '@0.1.4')
   for c in q['criteria']:
    c['criterion_id']=c['criterion_id'].replace('@0.1.3:', '@0.1.4:')
    c['status']='adapted D4 proposal; official qualifiers and declared deviations in work order'
    c['qualifiers']=[text.replace(' The fixed supplied proof target is not changed.','')if q['part_id']!='show-derivative'else text for text in c['qualifiers']]
    c['qualifiers']=[text.replace('apply the once-per-datum A/B deduction ledger.', 'apply the proposed MR03 operational ledger, pending exact-manifest approval.')for text in c['qualifiers']]
   q['dependency_basis']='Evaluate dependencies, DM and www against the earned gross evidence before the net MR penalty. A deducted A/B criterion remains earned for those purposes; do not cascade the deduction.'
for case in d['exemplar_cases']:
 if case['recipe_id']in owned:case['recipe_version']='0.1.4'
write(P/'calculus-design.json',d)
for folder in ['work-orders','exemplars']:
 for rid in owned:
  f=W/folder/(rid+'.md');text=f.read_text().replace('0.1.3','0.1.4').replace('planning/d3/','planning/d4/').replace('D3 repairs D2','D4 repairs the D3 delta').replace('D3 marking clarifications','D4 marking clarifications').replace('Current D3 checks','Current D4 checks').replace('## D3 per-part','## D4 per-part').replace('## D3 OD-6','## D4 OD-6').replace("Claude's focused short check", "Claude's D4 changed-scope confirmation").replace("Claude's short check", "Claude's D4 changed-scope confirmation")
  f.write_text('\n'.join(line.rstrip()for line in text.splitlines())+'\n')
f=W/'work-orders/WB8227-implicit-normal.md';text=f.read_text();at=text.index('## D4 per-part misread allocation and fixed proof target')
text=text[:at]+'''## D4 per-part misread application and fixed eligibility

The owner’s OD-6 principle and the proposed MR03 operating rules are separate. The latter await Vitalis’s exact-manifest approval. In criterion order the A/B slots are gradient-only **G2,G3,G5**, proof **S2,S3,S4**, extended gradient **H2**, and normal **N3**. The M/DM slots retain their ordinary evidence rules. Mark all parts on the eligible follow-through data before applying the net deduction. **A deducted G2 or S2 remains earned evidence for G5, S4, DM and www; the deduction does not cascade.** Take the proposed one-per-datum deduction from the first earned A/B anywhere using that datum in question order, including a later part if the first-use part earns none. Only a datum that earns no A/B anywhere has no deduction. Practice feedback names the misread.

**Eligibility is decided once, at first use, for the connected question.** The supplied point must still lie on the misread curve, the gradient must remain finite and nonzero, the chain demand must remain, and a supplied proof target must still represent that curve. These are disclosed planner interpretations of unchanged object/difficulty, not extra owner decisions. Once a datum is ineligible, mark every later use canonically, while retaining the question’s ordinary limited own-working method credit. It cannot become a fresh eligible misread in a later part. For a point misread in the normal part, N2 is judged as usual on their point and perpendicular gradient, conditional on N1; N3 still needs the canonical line.

The proof target remains fixed. S4 requires a complete correct proof of that actual target; it does not endorse a changed target. A proof-target sentence applies only to proof criteria, never to the stationary or gradient-only criteria.

**Settled connected fixtures (calc-D3-02):**

- Canonical $3e^{2x}y+y^2=4$, $P=(0,-4)$: read only $C=4$ as $5$ in part (a), then use the actual displayed derivative in (b)/(c). The point is off the misread curve, so eligibility is false at first use and stays false. Since the constant differentiates to zero, a complete proof still establishes the actual target canonically: **4/4 + 2/2 + 3/3 = 9/9**, with no MR adjustment. This is an ordinary-marking coincidence for an ineligible datum, not an eligible misread excused from its penalty.
- In the same canonical question, read $a=3$ as $4$ in (a) and carry that derivative forward. The curve/point and supplied target are inconsistent, so use canonical marking throughout. The learner derives $y'=-8e^{2x}y/(4e^{2x}+2y)$, gets $m=-8$ and $m_\\perp=1/8$, then $y+4=x/8$. Proof **S1,S3 = 2/4**, gradient **H1 = 1/2**, normal **N1,N2 = 2/3**: **5/9**. H2 and N3 are not revived by reclassifying the datum later. Reading $a$ as $8$ instead makes the denominator zero at P; that singular response is a different ineligible case and does not inherit this finite-gradient fixture.

**Eligible dependency fixture:** gradient-only, read exponent coefficient $k=2$ as $3$, with $a=3,C=4,P=(0,-4)$. The point remains on the curve and the demand is unchanged. Correct working gives $9e^{3x}y+(3e^{3x}+2y)y'=0$ and $m=-36/5$. Gross G1–G5 are all earned. The net penalty is allocated to G2, giving **4/5**, while G2 still satisfies the correct-working dependency of G5. A literal cascade to 3/5 is forbidden by the proposed operating rule.

**Later first-use fixture:** correctly prove the actual displayed derivative (4/4), then read its numerator coefficient $6$ as $8$ only in part (b). Correct substitution gives $m=-32/5$, and normal working gives $m_\\perp=5/32$ and $y+4=(5/32)x$. This fresh datum is first used in (b), with the proof unaffected. Deduct H2 once: **1/2 + 3/3**, total **8/9**. Misreading the learner’s own derived numeral is an ordinary accuracy error, not this printed-data fixture.
'''
f.write_text(text)
f=W/'work-orders/WB8227-stationary-inflexion.md';text=f.read_text().replace('`calculus-domain-audit.json` and `calculus-exemplar-oracle.json`','`calculus-domain-audit.json`, `calculus-exemplar-oracle.json` and `calculus-misread-oracle.json`')
text=text.replace('Deduct once only in the first-use part; later parts using the same datum can earn all their eligible accuracy awards without another deduction.', 'The proposed MR03 operating rule deducts from the first A/B earned on that datum anywhere in question order, carrying to a later using part if needed. No A/B anywhere means no deduction. All dependency and www checks use gross evidence before the net penalty; earned awards remain satisfied after deduction. Practice feedback names the misread.')
text+='''
**D4 deferred-accuracy fixture:** genuinely misread the normal two-extrema constant $+2$ as $+3$, but also make derivative and coordinate slips that leave P1/P3 only in points. Correct own-root classification still earns C1/C2. Gross credit is **2/4 + 2/2 = 4/6**; the first A/B earned on this datum is C2 in nature, so the proposed net penalty gives **2/4 + 1/2 = 3/6**. The first-use part having no accuracy award no longer makes the misread free.

The coefficient-misread eligibility boundary (calc-D3-04) remains an explicitly flagged E/F acceptance fixture: the ordinary object/difficulty test must be resolved for non-constant coefficient edits. These constant-term examples preserve the derivative and branch shape. No new coefficient domain or blanket eligibility permission is introduced in D4.
'''
f.write_text(text)
f=W/'exemplars/WB8227-implicit-normal.md';text=f.read_text().replace('Use the matching work order’s per-part MR policy and deduction ledger; this is Vitalis’s OD-6, supported by NSSCAS report2025 PDF345 item4 plus comparable Cambridge9709/12 March2016 scheme PDF3, not a Namibian one-mark tariff.', 'Use the matching work order’s MR03 application. Vitalis’s OD-6 principle is supported by NSSCAS report2025 PDF345 item4 and comparable Cambridge9709/12 March2016 scheme PDF3, not a Namibian one-mark tariff. The unit, ordering, persistent eligibility and gross/net ledger are proposed operational rules pending approval.')
text=text.replace('No earned A/B means zero MR deduction.', 'Only if no A/B is earned on that datum anywhere is the net deduction zero; otherwise select the first earned A/B in question order. Gross dependencies survive the net penalty.')
text+='''
## D4 connected eligibility and net-penalty examples

For $3e^{2x}y+y^2=4$, $P=(0,-4)$, a first-use C4→5 misread makes the point inconsistent with the curve. It is ineligible once for the whole connected question. A perfect derivative proof is nevertheless unchanged because C differentiates to0; using the true displayed derivative for gradient and normal gives **9/9 canonically**, with no MR adjustment.

A first-use a3→4 misread in that same question is also ineligible and remains canonical in later parts. The learner’s derivative is $-8e^{2x}y/(4e^{2x}+2y)$, its substituted gradient is−8, and their normal is $y+4=x/8$. The ordinary rubric gives S1/S3=2, H1=1, N1/N2=2, hence **5/9**. Correct method follow-through does not convert wrong canonical H2/N3 accuracy into MR accuracy.

For the eligible k2→3 gradient-only misread above, the gross G2 evidence remains correct and earned after the one-mark net deduction is allocated there. G5 therefore remains earned: **4/5, not3/5**. The operating choice is proposed; the one-mark-with-follow-through principle is owner-decided.
''';f.write_text(text)
f=W/'exemplars/WB8227-stationary-inflexion.md';text=f.read_text().replace('Use the matching work order’s own P/C/I criteria and once-per-datum ledger. Source authority is Vitalis OD-6,', 'Use the matching work order’s P/C/I criteria and proposed once-per-datum gross/net ledger, pending exact-manifest approval. Source authority for the misread principle is Vitalis OD-6,')
text=text.replace('Without earned A/B, MR deducts nothing;', 'Only if no A/B is earned anywhere on the datum does MR deduct nothing;')
text+='''
For a constant-term misread plus unrelated derivative/coordinate slips, points may earn only P1/P3 (2/4) while nature earns C1/C2 (2/2). The proposed ledger carries the single deduction to C2, the first earned A/B on that datum: **3/6**, not the old4/6. C1/C2 gross classification evidence is judged before the net adjustment.
''';f.write_text(text)
dev=read(P/'d3/calculus-deviations.json')
for row in dev:
 row['recipe_version']='0.1.4';row['status']=row['status'].replace('D3 confirmation','D4 confirmation')
 row['rationale']=row['rationale'].replace('all27','all 27');row['departure']=row['departure'].replace('Apply3','Apply 3')
write(H/'calculus-deviations.json',dev)
print('D4 owned calculus metadata and text repaired; common policy replacement remains coordinated by parent')
