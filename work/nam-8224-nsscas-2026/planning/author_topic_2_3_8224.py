"""Original equilibrium and acid/base manuscript, within the 8224 exclusions."""
from authoring_common_8224 import Topic
t=Topic('2.3')
def add(short,claims,title,text,loc):t.objective(short,claims,[(title,text)],'OpenStax-Chemistry',loc)
add('1-01',[
 'A reversible reaction can proceed in both directions; dynamic equilibrium in a closed system has equal forward and reverse rates and constant concentrations.',
 'Equal forward and reverse rates at equilibrium do not require equal reactant and product concentrations.'
], 'Reversibility and a dynamic steady composition', '''A reversible reaction can proceed from reactants to products and from products back to reactants. The reversible arrow ⇌ represents these two directions. In a closed system, reacting material cannot escape. At a fixed temperature, a reversible mixture can reach dynamic equilibrium: the forward and reverse reactions continue at equal rates, so concentrations remain constant.

Suppose a closed vessel initially contains mainly reactant. Product forms in the forward direction. As product accumulates, the reverse process becomes possible at an increasing rate. Eventually the rates become equal. Material is still changing between forms, but the amount converted each way in a given interval is the same. The mixture shows no net composition change. “Dynamic” refers to continuing reaction at the particle level, not movement of a visible boundary through the vessel.

Equal rates do not mean equal concentrations. A mixture can contain much more product than reactant while the two reaction rates match. A constant colour may provide evidence that the concentration of a coloured species is no longer changing, but it does not establish that the particles have stopped reacting. The model also requires a suitable closed system and sufficient time; a reaction that is very slow may appear unchanged without having reached this state.

For N2O4(g) ⇌ 2NO2(g), the relative amount of brown NO2 affects colour. At fixed temperature a sealed mixture can settle at constant colour with both species present. If temperature changes, the composition may change before a new equilibrium is reached. Keep the rate equality separate from the amounts present. This distinction underlies later concentration calculations and prevents an incorrect starting assumption that both sides of the equation must contain the same number of moles.''',
 '§13.1, printed pp.718–721 (PDF pp.728–731).')
add('1-02',[
 'Le Chatelier’s principle predicts that an equilibrium system responds to an imposed change in concentration, pressure or temperature in a direction that partly opposes that change.',
 'Increasing gas pressure by compression at fixed temperature favours the side with fewer gaseous particles when the gas coefficients differ.',
 'Raising temperature favours the endothermic direction; changing concentration favours net reaction that consumes an added species or replaces a removed species.'
], 'Applying Le Chatelier’s principle to a stated change', '''Le Chatelier's principle states that a system at equilibrium responds to a change in temperature, pressure or concentration in a direction that tends to oppose the imposed change. The response generally partly counters the disturbance; it does not promise to restore the original composition completely. Begin by naming the change, then use the balanced equation to explain the direction of net reaction.

At fixed temperature, adding a reactant increases its concentration. A net forward reaction tends to consume some of that addition. Removing product similarly favours further product formation. The concentrations adjust until the rates match again. Do not say simply that the reaction “moves right” without identifying the species being formed and the imposed concentration change.

For gases, compressing the vessel at constant temperature increases partial pressures. If the equation has different gas totals on its sides, net reaction favours the side with fewer gaseous particles. For N2(g) + 3H2(g) ⇌ 2NH3(g), this means ammonia formation: four gaseous particles become two on the equation basis. For H2(g) + I2(g) ⇌ 2HI(g), the equal gas totals give no predicted composition shift on uniform compression in the ideal-gas model. Adding an inert gas at fixed volume and temperature changes total pressure without changing reacting-gas partial pressures; that is a different disturbance from compression.

For temperature, use the sign of the reaction enthalpy. Heating favours the endothermic direction; cooling favours the exothermic direction. The forward Haber reaction is exothermic, so lowering temperature favours ammonia at equilibrium. Topic 2.1 explains the enthalpy sign. Rate may nevertheless fall at lower temperature, so the favourable final composition can take longer to reach. Pressure, temperature and concentration predictions concern a specific change with other relevant variables held fixed.''',
 '§13.3, printed pp.730–735 (PDF pp.740–745).')
add('1-03',[
 'For a specified reaction equation, the equilibrium constant depends on temperature; changing concentration or pressure at fixed temperature does not change its value.',
 'A catalyst changes the time needed to approach equilibrium at a fixed temperature but not the equilibrium composition or constant.'
], 'A change in composition is not necessarily a change in K', '''For a specified reaction equation, the value of its equilibrium constant changes with temperature. Adding a reactant, removing a product or compressing a gaseous mixture can change composition while the temperature and the constant remain unchanged. The new concentrations or partial pressures satisfy the same constant once the system has adjusted.

This distinction prevents a common error: more product does not automatically imply a larger K. Adding reactant can give more product at the final equilibrium while also leaving larger amounts of some reactants. The full ratio of the relevant concentrations, with their powers, returns to the same value at fixed temperature. Follow the entire expression rather than judging the numerator alone.

A catalyst provides an alternative reaction pathway and accelerates the approach in both directions. At the same temperature it does not change the initial and final thermochemical states, so it does not change K or the final equilibrium composition. A comparison made after a short time may show more product in the catalysed vessel because it has approached its final state faster. That is a rate observation, not evidence that the final composition is different.

For an exothermic forward reaction, raising temperature favours reactants and decreases the constant for the forward equation. Lowering temperature favours products and increases that constant. Reverse the written equation and the interpretation must reverse with it. State which equation the constant describes and the temperature at which it applies. In an experimental comparison, distinguish a change of temperature from simply adding a catalyst at an unchanged temperature. This is why an industrial catalyst helps productivity without making an unfavourable high-temperature equilibrium yield disappear.''',
 '§13.3, printed pp.732–735, temperature dependence and catalyst effects.')
add('1-04',[
 'For aA + bB ⇌ cC + dD, the concentration equilibrium expression is Kc = [C]^c[D]^d/([A]^a[B]^b) at the stated temperature.',
 'A gas-phase Kp expression uses equilibrium partial pressures with stoichiometric powers; pure solids and pure liquids are omitted from these school expressions.'
], 'Writing the concentration and partial-pressure expressions', '''For aA + bB ⇌ cC + dD at a stated temperature, write Kc = [C]^c[D]^d/([A]^a[B]^b). Square brackets denote equilibrium concentrations, commonly in mol dm⁻³. Products go in the numerator and reactants in the denominator. A coefficient becomes a power; it does not become a multiplier placed before the concentration.

For H2(g) + I2(g) ⇌ 2HI(g), Kc = [HI]²/([H2][I2]). For N2(g) + 3H2(g) ⇌ 2NH3(g), Kc = [NH3]²/([N2][H2]³). The direction and coefficients of the written reaction matter. Reversing the equation inverts the expression, so a numerical constant cannot be detached from its defining equation and temperature.

For gaseous species, Kp uses equilibrium partial pressures instead. In 2SO2(g) + O2(g) ⇌ 2SO3(g), Kp = p(SO3)²/(p(SO2)²p(O2)). A partial pressure is a gas component's contribution to total pressure. If its mole fraction is y in an ideal mixture, its partial pressure is y times total pressure. Use a consistent pressure unit throughout the substitution. For example, in an illustrative ideal mixture at total pressure 200 kPa, a gas mole fraction of 0.250 gives partial pressure 0.250 × 200 = 50.0 kPa. Another gas with fraction 0.750 supplies the remaining 150 kPa. The component pressures add to the total, but the total cannot replace a component in Kp. If the composition changes during reaction, use the final mole fractions rather than the original feed fractions. This keeps the pressure calculation tied to the actual mixture being evaluated.

Pure solids and pure liquids do not appear in these expressions. For CaCO3(s) ⇌ CaO(s) + CO2(g), Kp = p(CO2), provided the relevant solid phases are present at the stated temperature. Their absence from the expression does not mean their atoms fail to participate in the balanced reaction. In the school convention, derive units from the concentration or pressure powers: the hydrogen iodide Kc has cancelling units, while the sulphur trioxide Kp has inverse-pressure units. Treat Kc and Kp through their own requested expressions; select the data type that matches the expression rather than substituting a total pressure for one gas's partial pressure.''',
 '§13.2, printed pp.722–730, mass action, partial pressures and heterogeneous expressions; syllabus §2.3.1 governs separate treatment.')
add('1-05',[
 'Equilibrium constants are calculated from equilibrium concentrations or partial pressures, with consistent units and powers from the equation.',
 'A large equilibrium constant indicates product-favoured composition for the stated equation at that temperature, but is not a reaction-rate measure.'
], 'Calculating and interpreting a constant', '''To calculate K, identify the balanced equation, temperature and final concentrations or partial pressures. Write the expression before substituting numbers. Initial quantities cannot be substituted directly unless they have already been shown to be the equilibrium quantities. If amounts are supplied, divide by the vessel volume to obtain concentrations and retain that same volume basis for each species.

For an original illustrative H2(g) + I2(g) ⇌ 2HI(g) mixture at a stated temperature, let [H2] = 0.200, [I2] = 0.200 and [HI] = 0.800 mol dm⁻³. Then Kc = 0.800²/(0.200 × 0.200) = 16.0 to three significant figures. The concentration units cancel. This value describes the stated model mixture; it is not a tabulated claim about a particular temperature.

For an illustrative sulphur trioxide mixture at another stated temperature, take equilibrium partial pressures p(SO3) = 40.0, p(SO2) = 20.0 and p(O2) = 10.0 kPa. The expression gives Kp = 40.0²/(20.0² × 10.0) = 0.400 kPa⁻¹. Convert all pressures consistently if another unit is required; the numerical value in the school pressure-unit convention changes with the chosen unit when the powers do not cancel. The gas coefficients, rather than the total number of atoms, determine those powers.

A relatively large K for the stated equation means products are favoured in its equilibrium ratio. It does not specify that the forward reaction is fast. A small rate can delay access to that composition. Nor does a large K alone give a percentage yield without the starting amounts and equation. Interpret a constant as a composition relationship at a temperature, and use separate rate data to judge how quickly the mixture approaches it.''',
 '§13.2 and §13.4, printed pp.722–730 and 736–741; original numerical examples.')
add('1-06',[
 'Equilibrium amounts follow conservation of matter and stoichiometric changes from initial amounts.',
 'For a model A ⇌ B with a 1:1 amount balance and fixed volume, Kc = [B]/[A] permits a linear calculation of equilibrium quantities.'
], 'Finding the quantities present', '''Use an initial–change–equilibrium account to connect what was added to what is finally present. Work in moles or in concentrations consistently. The coefficient ratio determines the relative changes. For a forward change, reactant amounts fall and product amounts rise. The direction is reversed if products are being consumed.

As a deliberately simple model at fixed temperature, A(aq) ⇌ B(aq) has Kc = 4.00. A and B represent interconvertible forms with a one-to-one amount balance. A 1.00 dm³ vessel initially contains 1.00 mol A and no B. Let x mol form B. The final amounts are 1.00 − x of A and x of B. Thus 4.00 = x/(1.00 − x), giving 4.00 − 4.00x = x, then x = 0.800 mol. A remains at 0.200 mol and B is 0.800 mol. The total of the two forms is still 1.00 mol.

For a reaction with unequal coefficients, use the actual ratios. If 0.100 mol N2 is consumed in N2 + 3H2 ⇌ 2NH3, then 0.300 mol H2 is consumed and 0.200 mol NH3 is formed. Subtract those changes from the supplied initial amounts before dividing by volume for concentrations. If one final concentration is supplied, it can directly determine the other changes.

Check that final amounts are non-negative, conserve the relevant atoms and reproduce the given constant at the stated temperature. Replacing an initial amount by a final one without accounting for reaction breaks the matter balance. If converting a concentration into amount, use n = cV with V in dm³ for mol dm⁻³. Keep unrounded values until the final result. The problems here use directly rearrangeable relationships; choose the stated data rather than adding an unsupported approximation about how little reacts.''',
 '§13.4, printed pp.736–741, stoichiometric changes and equilibrium amount tables; original linear model.')
add('1-07',[
 'For the exothermic Haber and Contact reactions, lower temperature favours equilibrium product yield while higher temperature generally improves rate.',
 'Higher pressure favours ammonia and sulphur trioxide in their stated gas reactions, but industrial pressure choice also depends on benefit, cost and equipment.',
 'A suitable catalyst accelerates industrial reaction at a chosen temperature without increasing the equilibrium yield.'
], 'Why industrial settings are a compromise', '''The Haber process uses N2(g) + 3H2(g) ⇌ 2NH3(g), with an exothermic forward reaction. Low temperature favours ammonia at equilibrium, but a low-temperature uncatalysed reaction is too slow for useful production. A higher operating temperature sacrifices some attainable yield to obtain a useful rate. An iron catalyst helps the system approach equilibrium faster at the chosen temperature. It does not increase the final yield for that temperature and pressure.

High pressure favours ammonia because the gas total decreases from four to two on the equation basis. Compression can also increase collision frequency. However, strong equipment and compression require resources and energy. The chosen pressure therefore balances a yield and rate benefit against equipment demands and cost. Removing ammonia from the output and recycling unreacted gases can improve the overall use of feed even when a single pass has incomplete conversion.

In the Contact process, 2SO2(g) + O2(g) ⇌ 2SO3(g) is also exothermic, and the gas total decreases from three to two. Lower temperature favours sulphur trioxide at equilibrium, while raising temperature generally improves rate. A suitable catalyst permits an effective rate at a moderate temperature. Higher pressure favours product, but a pressure increase is useful only if its extra conversion justifies the extra compression and equipment. A process that already achieves a high conversion may gain little from very high pressure.

Explain a temperature choice through both yield and rate. “Low temperature gives more product” is incomplete as a production decision if it ignores a very long reaction time. “High temperature gives a fast reaction” is likewise incomplete if it ignores reduced attainable conversion in an exothermic system. Topic 2.4 develops the rate explanation; Topic 3.5 applies this reasoning to nitrogen and sulphur chemistry. The optimum cannot be specified from the equilibrium equation alone without operational and economic evidence.''',
 '§13.3 printed pp.733–735, Haber compromise; §18.7 ammonia synthesis; Contact application derived from syllabus §2.3.1 reaction and exothermic gas-balance principles.')
add('1-08',[
 'Industrial equilibrium data must be interpreted alongside rate, pressure, temperature and the stated production criterion.',
 'An improvement in conversion per pass does not by itself establish an improvement in output per unit time or economic performance.'
], 'Reading industrial data instead of memorising a setting', '''Separate what a data table measures from the conclusion being requested. An equilibrium percentage is the attainable conversion at the stated temperature, pressure and feed composition. A time or production-rate measurement concerns kinetics. A pressure or energy-cost column may decide whether an improvement is worthwhile. These columns answer different questions.

For an original model exothermic process at a fixed pressure and feed, suppose a cooler setting gives 80% equilibrium conversion but produces only 2.0 mol product per minute in the available reactor. A warmer setting gives 60% conversion but produces 5.0 mol per minute. If the sole stated goal is output per minute with the same reactor, the warmer setting is favoured by the rate data despite its lower final conversion. If feed use or separation cost matters, the conversion difference also matters and more information may be needed.

Do not label the higher percentage the better process without a criterion. Equally, do not assume the faster rate makes waste or energy costs irrelevant. If a catalyst raises the measured short-time output at an unchanged temperature, distinguish faster approach from a changed equilibrium constant. At constant temperature, the catalyst does not alter the final ratio. A table comparing different temperatures can show both effects, so keep the columns and variables separate.

When explaining data, quote the relevant figures and connect them to the chemistry. For the example, 5.0 is 2.5 times 2.0 mol per minute, while conversion falls by 20 percentage points. A percentage-point change is not the same as a percentage change relative to an initial percentage. Conclude only against the criterion and assumptions supplied. This approach supports a reasoned choice rather than an unsupported statement that a named industrial setting must be ideal for every plant.''',
 '§13.3 printed pp.734–735, industrial rate/yield compromise; data and numerical comparisons original.')

add('2-01',[
 'A Brønsted–Lowry acid donates a proton and a Brønsted–Lowry base accepts a proton.',
 'A conjugate acid–base pair differs by one H+; acid-I becomes base-I and base-II becomes acid-II in a proton-transfer equation.'
], 'Following the transferred proton', '''A Brønsted–Lowry acid is a proton donor and a Brønsted–Lowry base is a proton acceptor. A proton is H+. An acid–base reaction in this model transfers a proton from one species to another. The base need not contain hydroxide before the reaction: ammonia accepts a proton using its lone pair.

Write acid-I + base-II ⇌ base-I + acid-II. Acid-I loses H+ and becomes its conjugate base-I. Base-II gains H+ and becomes its conjugate acid-II. A conjugate pair differs by one proton, so its charge changes by one unit as well. Do not pair species merely because they occur on the same side of the reaction.

For NH3(aq) + H2O(l) ⇌ NH4+(aq) + OH−(aq), water donates a proton and is acid-I; OH− is base-I. Ammonia accepts the proton and is base-II; NH4+ is acid-II. The pairs are H2O/OH− and NH4+/NH3. The aqueous concentrations adjust as proton transfer proceeds in both directions. For HCl reacting with water, HCl donates and H2O accepts, forming Cl− and H3O+. Water's role therefore depends on its reaction partner.

Check a proposed pair by adding or removing one H+ without changing the other atoms. NH4+ loses H+ to give NH3, not NH2−. H2O loses H+ to give OH−, not an oxygen atom. These are proton-transfer changes rather than the electron losses that defined oxidation in Topic 2.2. Stating the transferred particle prevents confusion between acid–base reaction and redox. In aqueous calculations, H+(aq) is the usual shorthand for the hydrated proton represented more explicitly as H3O+. Reversing the ammonia equation reverses the roles: NH4+ donates a proton to OH−, producing NH3 and water. The conjugate pairs stay the same even though the written proton-transfer direction changes. A pair is defined by the one-proton relationship, not by which member was originally added to the vessel. To check charge, removing H+ makes a species one unit more negative, while adding H+ makes it one unit more positive. It does not remove or add an electron in the redox sense.''',
 '§14.1, printed pp.766–768 (PDF pp.776–778).')
add('2-02',[
 'Strong acids dissociate essentially completely in dilute aqueous solution; weak acids dissociate only partly.',
 'At equal analytical concentration for comparable monoprotic acids, the strong acid has higher H+ concentration and lower pH than the weak acid.',
 'Strong soluble bases provide OH− essentially completely, whereas a weak base such as ammonia reacts only partly with water; strength differs from concentration.'
], 'Strength describes extent, concentration describes amount', '''A strong acid dissociates essentially completely in dilute aqueous solution. A weak acid dissociates only partly, leaving a significant proportion as molecules. For two comparable monoprotic acids at the same analytical concentration and temperature, the strong acid therefore produces a higher H+ concentration and has a lower pH. This comparison requires equal concentration: a highly dilute strong acid need not have a lower pH than a concentrated weak acid.

Acid strength and concentration answer different questions. Strength describes the extent of dissociation; concentration describes how much acid has been put into a given solution volume. Diluting a strong acid lowers its H+ concentration without changing its classification to a weak acid. A weak acid is not defined by having a small amount of solute.

For bases, a soluble strong base such as sodium hydroxide provides hydroxide ions essentially completely on dissolving. Ammonia is a weak base: it accepts protons from water only partly, giving NH4+ and OH−. At comparable concentration a strong base provides a higher OH− concentration and a higher pH than a weak base. Do not confuse a poorly soluble solid with a weak dissolved base simply because little solid dissolves.

At 25 °C, acidic aqueous solutions have pH below 7, neutral water has pH 7 and alkaline solutions have pH above 7. The neutral pH depends on temperature, so state the temperature when using that benchmark. These qualitative comparisons concern extent of ion formation and concentration. Numerical work in the next section uses strong acids whose dissociation supplies a stated, directly calculable H+ concentration. A qualitative weak-acid comparison does not justify substituting its initial concentration as though it were fully dissociated.''',
 '§14.3 printed pp.776–777, strength by extent; §14.2 printed pp.770–772, pH and temperature.')
add('2-03',[
 'For the school dilute-solution approximation, pH = −log10[H+] with H+ concentration in mol dm⁻³, and [H+] = 10^(−pH) mol dm⁻³.',
 'For a fully dissociated monoprotic strong acid, H+ concentration is approximately its analytical concentration when water’s own contribution is negligible.',
 'Dilution conserves the amount of acid in the absence of reaction, giving c1V1 = c2V2.'
], 'Strong-acid concentration and pH', '''For the dilute-solution model used here, pH = −log10[H+], with [H+] entered numerically in mol dm⁻³. pH has no unit. The inverse is [H+] = 10^(−pH) mol dm⁻³. Use the base-ten logarithm key rather than the natural logarithm. A smaller pH means a larger H+ concentration, so the negative sign is chemically meaningful.

A fully dissociated monoprotic strong acid supplies one H+ per molecule. A 0.0200 mol dm⁻³ HCl solution therefore has [H+] ≈ 0.0200 mol dm⁻³ and pH = −log10(0.0200) = 1.699, using three decimal places for a concentration given to three significant figures. This approximation neglects water's contribution and is appropriate here because the acid concentration is far greater than that contribution. Extremely dilute cases need more information than this direct substitution.

For dilution without reaction, the acid amount is conserved. If 10.0 cm³ of 0.100 mol dm⁻³ HCl is diluted to 100.0 cm³, c2 = 0.100 × 10.0/100.0 = 0.0100 mol dm⁻³. Thus [H+] ≈ 0.0100 mol dm⁻³ and pH = 2.000. The final volume is the total solution volume, not the volume of water added. Consistent volume units cancel in the dilution ratio; use dm³ if calculating moles explicitly.

As a check, tenfold dilution of a monoprotic strong acid raises pH by about one in this range. From pH 3.00, [H+] = 1.0 × 10⁻³ mol dm⁻³, with two significant figures corresponding to two decimal places. Keep pH precision distinct from ordinary significant-figure rounding. If a question supplies a different hydrogen-ion yield per acid molecule, use its stated dissociation information instead of applying the monoprotic factor blindly.''',
 '§14.2 printed pp.770–775, logarithms and pH precision; §14.3 strong-acid approximation; §3.3 dilution. Original concentrations and examples.')

s=t.wo['item_slots']
qa=[
 ('Describe dynamic equilibrium in a closed reaction system at constant temperature, in terms of continuing reactions, rates and concentrations. [3]','Forward and reverse reactions continue [1] at equal rates [1], so reactant and product concentrations remain constant [1].'),
 ('Explain why constant concentrations in a closed system at fixed temperature do not mean the forward and reverse reactions have stopped at dynamic equilibrium. [2]','The two reactions continue at equal rates [1]; because species are made and consumed at matching rates, there is no net concentration change [1].'),
 ('State Le Chatelier’s principle for a system subjected to a change in temperature, pressure or concentration. [1]','The equilibrium system responds in a direction that tends to oppose the imposed temperature, pressure or concentration change [1].'),
 ('Determine the favoured direction for N2(g) + 3H2(g) ⇌ 2NH3(g) when pressure rises by compression at constant temperature. [1]','Towards ammonia [1], because that side contains fewer gaseous particles.'),
 ('State which of temperature, concentration, pressure or catalyst can change the equilibrium constant for a specified reaction. [1]','Temperature [1]; the other changes do not change K at fixed temperature.'),
 ('Suggest the effect on Kc when a catalyst is added at the same temperature to a reversible mixture. [1]','No change [1]; equilibrium is reached faster but the constant at that temperature is unchanged.'),
 ('State what supplies the powers in a Kc expression written using equilibrium concentrations. [1]','The stoichiometric coefficients in the balanced equation [1].'),
 ('Determine the Kp expression for 2SO2(g) + O2(g) ⇌ 2SO3(g) at a stated temperature. [1]','Kp = p(SO3)²/(p(SO2)²p(O2)) [1], using equilibrium partial pressures.'),
 ('State which concentrations must be used when calculating Kc at a stated temperature. [1]','Equilibrium concentrations [1], rather than unadjusted initial values.'),
 ('Calculate Kc for H2(g) + I2(g) ⇌ 2HI(g) at a stated temperature using equilibrium concentrations [H2] = [I2] = 0.200 and [HI] = 0.800 mol dm⁻³. Give three significant figures. [3]','Relationship Kc = [HI]²/([H2][I2]) [1]. Substitution 0.800²/(0.200 × 0.200) [1]. Answer 16.0, dimensionless in this concentration convention, to three significant figures [1]. Concentration units cancel; no conversion is needed.'),
 ('Determine whether a large Kc by itself shows a fast reaction at the stated temperature. [1]','No [1]: Kc concerns equilibrium concentration ratios, whereas rate requires kinetic information.'),
 ('State the stoichiometric rule for concentration changes in N2 + 3H2 ⇌ 2NH3 at fixed volume. [1]','A decrease of x in nitrogen concentration accompanies a decrease of 3x in hydrogen and an increase of 2x in ammonia [1].'),
 ('Calculate final moles of B for the model A(aq) ⇌ B(aq), Kc = 4.00 at the stated temperature, initially 1.00 mol A and no B in 1.00 dm³. [3]','Let x mol B form: final A = 1.00 − x and B = x [1]. Kc = x/(1.00 − x) = 4.00 gives 5.00x = 4.00 [1]. Answer x = 0.800 mol B to three significant figures [1]. Equal volume factors cancel; no conversion is required.'),
 ('Determine whether a proposed equilibrium calculation giving a negative final reactant concentration can be physically accepted. [1]','No [1]; a final amount or concentration must be non-negative, so the model setup or chosen result needs correction.'),
 ('Describe the temperature, pressure and catalyst reasoning for the exothermic Haber reaction N2 + 3H2 ⇌ 2NH3. [3]','Lower temperature favours equilibrium ammonia but slows rate, requiring a compromise [1]; higher pressure favours the fewer gas particles on the ammonia side but has costs [1]; a suitable catalyst increases rate without changing equilibrium yield at fixed temperature [1].'),
 ('Explain why a catalyst does not replace the temperature compromise in an exothermic industrial equilibrium process. [2]','At a chosen temperature it speeds approach but does not change the equilibrium yield [1]; because higher temperature generally improves rate while lowering the attainable product yield, both effects still matter [1].'),
 ('Explain why “the lowest temperature must be best because it gives most ammonia” is incomplete for the exothermic Haber process. [2]','It considers equilibrium yield but omits rate [1]; low temperature favours ammonia yet slows production, so a practical temperature balances yield and rate [1].'),
 ('State two types of data needed to distinguish equilibrium conversion from productivity at a stated temperature and pressure. [1]','Equilibrium conversion or composition and a rate or output-per-time measurement [1].'),
 ('Determine which setting gives greater output per minute for a model exothermic process: at the same pressure and feed, cooler gives 80% equilibrium conversion and 2.0 mol min⁻¹, warmer gives 60% and 5.0 mol min⁻¹. The sole criterion is output per minute. [1]','The warmer setting [1], because 5.0 mol min⁻¹ exceeds 2.0 mol min⁻¹ despite its lower conversion.'),
 ('Describe a Brønsted–Lowry acid, a base and the relationship between a conjugate pair. [3]','An acid donates H+ [1]; a base accepts H+ [1]; a conjugate acid–base pair differs by one H+ [1].'),
 ('Explain why NH3 acts as a base in NH3(aq) + H2O(l) ⇌ NH4+(aq) + OH−(aq), and name its conjugate acid. [2]','NH3 accepts H+ from water [1], becoming its conjugate acid NH4+ [1].'),
 ('Describe the difference between strong and weak monoprotic acids at the same analytical concentration and temperature. [3]','The strong acid dissociates essentially completely [1], while the weak acid dissociates partly [1]; the strong acid has higher H+ concentration and lower pH [1].'),
 ('Explain why diluting a strong acid does not turn it into a weak acid. [2]','Dilution reduces its concentration, the amount per unit volume [1]; strength concerns extent of dissociation, which remains essentially complete for the stated dilute strong-acid model [1].'),
 ('State the pH relationship using hydrogen-ion concentration for the dilute-solution school model. [1]','pH = −log10[H+] [1], with [H+] entered in mol dm⁻³; pH is dimensionless.'),
 ('Calculate [H+] and pH for 0.0200 mol dm⁻³ HCl, treating it as fully dissociated and neglecting water’s contribution. [3]','[H+] = 0.0200 mol dm⁻³ from the one-H+ monoprotic relationship [1]. pH = −log10(0.0200) [1]. Answer 1.699, dimensionless, to three decimal places for the three-significant-figure concentration [1]. No unit conversion is required.'),
 ('Determine which solution has the greater hydrogen-ion concentration: pH 2.00 or pH 3.00. [1]','The pH 2.00 solution [1]; its H+ concentration is ten times greater.')
]
assert len(qa)==len(s)
for slot,(prompt,answer) in zip(s,qa):
 st='WHY' if slot['subtype']=='MECH' else None
 t.item(slot,prompt,answer,subtype=st)
 if st:t.deviations.append({'from':slot['slot']+' MECH','to':'WHY with original AO/Bloom/command/tariff','why':'The objective asks for equilibrium/rate reasoning, proton transfer or dissociation extent; forcing an electron-movement intermediate/product answer would confuse the chemistry.'})
p=t.wo['performance_tasks']
t.item(p[0],'''Identify one correct option per question for this original model. A(aq) ⇌ B(aq) is exothermic. The total amount of A plus B is conserved. At a cooler temperature Kc = 4.00; initially 1.00 mol A and no B occupy 1.00 dm³. At fixed pressure and feed, cooler operation gives 80% equilibrium conversion and 2.0 mol min⁻¹, while warmer gives 60% and 5.0 mol min⁻¹. [7]
1. If x mol B forms, final A is: A x; B 1.00 + x; C 1.00 − x; D zero by definition.
2. The cooler equation for x is: A 4.00 = x/(1.00 − x); B 4.00 = x + 1.00; C 4.00 = 1.00/x; D 4.00 = 1.00 − x.
3. Cooler final B is: A 0.200 mol; B 4.00 mol; C 1.00 mol; D 0.800 mol.
4. Cooler final A concentration is: A 0.800; B 0.200; C 4.00; D −0.800 mol dm⁻³.
5. If the sole criterion is product per minute, the better setting is: A cooler because conversion is higher; B neither because both are reversible; C warmer because 5.0 exceeds 2.0; D cooler because its temperature is lower.
6. Warmer output divided by cooler output is: A 2.5; B 0.4; C 20; D 60.
7. The conversion difference is: A 20% of the cooler value; B 25 percentage points; C 60 percentage points; D 20 percentage points.''',
 '''Key: 1 C, 2 A, 3 D, 4 B, 5 C, 6 A, 7 D; one mark per correct option.
1. C conserves 1.00 mol. Distractor A uses the product amount for reactant; B adds a consumed quantity; D assumes completion.
2. A uses [B]/[A]. B adds amounts instead of making a ratio; C ignores the remaining A expression; D omits the product numerator.
3. D follows 4.00(1.00 − x) = x. A is the remaining reactant; B exceeds total amount; C assumes complete conversion.
4. B is 0.200 mol divided by 1.00 dm³. A is product concentration; C mistakes Kc for concentration; D is physically negative.
5. C applies the stated output criterion. A substitutes yield for rate; B treats reversibility as zero production; D gives no productivity evidence.
6. A follows 5.0/2.0 = 2.5. B reverses the ratio; C borrows the conversion-point difference; D borrows the warmer percentage.
7. D follows 80 − 60 = 20 percentage points. A confuses a point difference with relative change; B uses the 25% relative decrease but assigns point units; C copies one conversion figure.''')
t.item(p[1],'''Explain the following linked points for an original exothermic industrial model A ⇌ B at fixed pressure. Cooler operation has 80% equilibrium conversion and output 2.0 mol min⁻¹; warmer operation has 60% and 5.0 mol min⁻¹. [8]
(a) Describe dynamic equilibrium using rates and concentrations. [2]
(b) Explain why lower temperature favours B but can reduce production per minute. [2]
(c) Determine the setting favoured if the sole goal is output per minute, quoting data. [1]
(d) State whether increasing the concentration of A changes Kc at fixed temperature. [1]
(e) Explain the effect of a catalyst on the time to equilibrium and on its final composition at fixed temperature. [2]''',
 '''Part (a): forward and reverse rates are equal [1], with concentrations constant while reaction continues [1].
Part (b): cooling favours the exothermic forward direction and B [1], but reduces rate and can reduce product per minute [1].
Part (c): warmer, because 5.0 rather than 2.0 mol min⁻¹ is produced [1].
Part (d): Kc is unchanged at fixed temperature [1].
Part (e): the catalyst reduces the time required to approach equilibrium [1], but does not change final composition at that temperature [1]. Each bracket is a separate creditworthy point.''')
t.item(p[2],'''Calculate the cooler-temperature equilibrium amount of product B in the model A(aq) ⇌ B(aq). Initially 1.00 mol A and no B occupy 2.00 dm³; Kc = 4.00 at this temperature. The total amount of A plus B is conserved. [5]
(a) Calculate equilibrium moles of B and its concentration, to three significant figures. [3]
(b) For the same exothermic process at fixed pressure and feed, cooler operation gives 80% conversion and 2.0 mol min⁻¹ while warmer gives 60% and 5.0 mol min⁻¹. Calculate the warmer/cooler output ratio and identify the setting favoured by an output-per-minute criterion. [2]''',
 '''(a) With x mol B, Kc = (x/2.00)/((1.00 − x)/2.00) = x/(1.00 − x) = 4.00 [1]. Solve x = 0.800 mol B [1]; concentration = 0.800/2.00 = 0.400 mol dm⁻³ [1]. Three significant figures follow the supplied amount, volume and constant; volume is already in dm³, so no conversion is required.
(b) Output ratio = 5.0/2.0 = 2.5, dimensionless, to two significant figures [1]; warmer is favoured for the stated criterion despite lower equilibrium conversion [1].''')
t.deviations.append({'from':'Generic conditions variant register','to':'Use explicit temperature, pressure and concentration settings throughout the industrial discussion','why':'Gas-volume s.t.p./r.t.p. variants do not describe industrial reaction settings. Full relevant variables are taught without imposing those unrelated reference volumes.'})
t.save()
