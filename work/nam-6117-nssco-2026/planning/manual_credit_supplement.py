"""Part-aligned, paraphrased report guidance where automatic row splitting failed.

Question order is the printed mark order. Report page numbers are PDF viewer pages.
"""
import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
POINTS = {
 (2021,2,7,86): [
  "Name propanol.", "Give the alkene general formula CnH2n.",
  "Identify the carbon–carbon double bond and explain addition of simple molecules across it; two points.",
  "Choose both isomer letters C and E; both are required for the two marks.",
  "Divide each mass percentage by relative atomic mass, divide by the smallest mole amount, then scale the ratio to whole numbers; the report separates four method/result marks.",
 ],
 (2022,2,4,94): [
  "Define a strong acid as one that ionises completely in aqueous solution.",
  "Name the Contact process.", "Place coefficient 2 before water to balance the equation.",
  "Convert 600 cm³ to 0.600 dm³ and multiply by 1.5 mol/dm³ to obtain 0.9 mol; two marks include method.",
  "Calculate relative formula mass of magnesium sulfate as 120.",
  "Multiply 0.9 mol by 120 to obtain 108 g; method and answer credit, with follow-through from earlier parts.",
  "Apply the equation's water-to-acid ratio of two to one, then multiply 1.8 mol by Avogadro's constant to obtain about 1.08 × 10²⁴ molecules; two marks with follow-through.",
  "Divide C, H and O percentages by relative atomic masses; divide by the smallest result; multiply the fractional ratio by three to obtain C3H4O3. Three staged marks.",
  "Divide molecular Mr 176 by empirical Mr 88, then double the empirical subscripts to obtain C6H8O6; two staged marks.",
 ],
 (2022,3,1,99): [
  "Name the pipette.", "State the indicator's pink-to-colourless change; one mark for each endpoint colour.",
  "Explain that universal indicator lacks a sharp titration endpoint.",
  "Record both burette readings, 23.20 and 2.50 cm³, correctly.",
  "Subtract the initial from final burette reading to obtain 20.70 cm³.",
  "Use titre and known concentration to calculate acid moles; use the mole ratio and alkali volume to calculate barium hydroxide concentration; two stages.",
  "Repeat the titration and compare results until concordant, checking for anomalies; two connected points.",
 ],
 (2022,3,2,100): [
  "Complete the missing table masses as 4.00 g and 2.70 g; one mark each.",
  "Plot 8–14 points accurately for partial credit, all 15 for the second plotting mark, and a smooth balanced curve for the third.",
  "Use the starting mass minus 1 g, read the corresponding time from the graph, and show the horizontal read-off construction; three stages.",
  "Predict 2.48 g and explain that reaction ends when a reactant is used up or gas production stops; two points.",
  "Subtract masses at 1 and 9 minutes to obtain 0.94 g.",
  "Divide mass change by 8 minutes to obtain 0.1175 g/min; value and unit each earn credit.",
  "State two controls such as the starting carbonate mass, acid concentration or acid volume; one mark per distinct variable.",
 ],
 (2023,2,5,101): [
  "Define endothermic as absorbing energy from surroundings.",
  "Sum energies of bonds broken and bonds formed, then subtract formation from breaking; the report allows intermediate-value credit and three marks overall.",
  "Define dynamic equilibrium by equal forward and reverse reaction rates.",
  "Draw reactants higher than products, a correctly directed negative enthalpy arrow, and activation energy from the reactant level to peak; three features.",
  "For an exothermic equilibrium, increased temperature shifts equilibrium towards reactants.",
  "Higher pressure shifts equilibrium to the side with fewer gas molecules, towards products.",
 ],
 (2023,3,1,104): [
  "Use damp red litmus paper and state its change to blue in ammonia; separate test and result marks.",
  "Name Bunsen burner, round-bottom flask and Liebig condenser; one mark each.",
  "Filter or decant, wash the solid residue, then dry it; three sequence marks.",
 ],
 (2023,3,2,105): [
  "Read all nine measuring-cylinder values; the report gives one mark for four or five, two for six to eight, and three for all nine correct.",
  "Plot all nine points within about 1 mm for two marks; draw a smooth, balanced best-fit curve for another.",
  "Read graph volume at 100 s, divide by elapsed time, and include the requested rate unit; three stages.",
  "State that a reactant is exhausted, so gas production has ended.",
  "Predict faster reaction with powder and explain its greater surface area; two linked points.",
  "Agree that a gas syringe improves accuracy and justify it by better precision or avoiding CO2 dissolution in water; statement and reason.",
 ],
}
PLANS = {
 (2021,3,4,90): ["Six one-mark points: measure acid volume; initial acid temperature; a metal mass; final temperature or regular temperature readings; repeat using the same metal mass and acid volume; infer the greater energy change from the larger temperature rise."],
 (2022,3,4,101): ["Six marks from seven points: crush petals; mix crushed petals with ethanol; filter; draw pencil baseline or centre mark on chromatography paper; spot the pigment; put paper into solvent with spot above solvent (or add solvent centrally); allow solvent to separate colours."],
 (2023,3,4,107): ["Eight one-mark stages: put thiosulfate in flask; place flask over the marked cross; add measured acid volume; measure that acid volume; time cross disappearance; repeat with a different thiosulfate concentration; keep acid volume fixed; compare disappearance times across concentrations."],
 (2024,3,5,117): ["Award any seven of eight points: take equal product volumes; measure volumes with suitable apparatus; add a suitable indicator; add acid dropwise; deliver it from a burette; continue to colour change; record or calculate acid volume used for each; infer that the product consuming more acid is more concentrated."],
}
COMMENTARY_ONLY = {
 (2022,2,3,93): [
  "Name a suitable lead compound that reacts with zinc sulfate to form insoluble lead sulfate; the report does not print the accepted-answer table for this part.",
  "Identify precipitation or a double-displacement reaction; exact accepted wording and mark allocation are not printed in the report.",
  "Separate the lead-sulfate precipitate from the mixture and wash it before drying; the commentary rejects evaporation and crystallisation, but no part-level mark table is printed.",
  "Complete the neutralisation equation with hydrochloric acid and water; the commentary names these products/reactants without a part-level allocation.",
  "Describe passing gas into limewater and the cloudy observation; the report says this test was frequently incomplete but prints no accepted-answer row.",
 ],
}
SPECIAL = {
 'QP-6117-2024-2-Q04-P01': (110, 'paraphrased_shared_answer_row', 'Test tube X: universal indicator turns red; one mark for this observation.'),
 'QP-6117-2024-2-Q04-P02': (110, 'paraphrased_shared_answer_row', 'Test tube Y: magnesium dissolves or bubbles/effervescence appear; one mark for a valid observation.'),
 'QP-6117-2023-2-Q07-P09': (103, 'paraphrased_image_answer', 'Draw the ester linkage as a carbonyl carbon bonded to an oxygen atom, –C(=O)–O–; one mark for the correct connectivity.'),
 'QP-6117-2025-2-Q03-P07': (95, 'paraphrased_image_answer', 'Calculate nitrogen mass percentages separately: ammonium nitrate, 28/80 × 100 = 35%; ammonium sulfate, 28/132 × 100 ≈ 21%. One mark for each supported comparison value.'),
}

def main():
    rows=json.loads((WORK/'assessment-evidence/question_parts.json').read_text())['records']
    out={}
    for (year,paper,q,page),points in POINTS.items():
        subset=[r for r in rows if r['year']==year and r['paper_id']==str(paper) and r['question_ref'].startswith(f'Q{q},')]
        assert len(subset)==len(points),(year,paper,q,len(subset),len(points))
        for row,point in zip(subset,points):out[row['evidence_id']]={'creditworthy_points':[point],'report_pdf_page':page,'status':'paraphrased_answer_table'}
    for (year,paper,q,page),points in PLANS.items():
        subset=[r for r in rows if r['year']==year and r['paper_id']==str(paper) and r['question_ref'].startswith(f'Q{q},')]
        assert len(subset)==1,(year,paper,q,len(subset))
        out[subset[0]['evidence_id']]={'creditworthy_points':points,'report_pdf_page':page,'status':'paraphrased_plan_marking'}
    for (year,paper,q,page),points in COMMENTARY_ONLY.items():
        subset=[r for r in rows if r['year']==year and r['paper_id']==str(paper) and r['question_ref'].startswith(f'Q{q},')]
        assert len(subset)==len(points),(year,paper,q,len(subset),len(points))
        for row,point in zip(subset,points):out[row['evidence_id']]={'creditworthy_points':[point],'report_pdf_page':page,'status':'commentary_only_no_allocated_answer'}
    for eid,(page,status,point) in SPECIAL.items():
        assert any(r['evidence_id']==eid for r in rows),eid
        out[eid]={'creditworthy_points':[point],'report_pdf_page':page,'status':status}
    path=WORK/'assessment-evidence/manual-credit-supplement.json'
    path.write_text(json.dumps({'status':'curated','records':out},indent=2,ensure_ascii=False)+'\n')
    print('Wrote',len(out),'supplemental guidance entries')

if __name__=='__main__':main()
