"""Original, explicitly authored nutrition teaching and tasks for the approved 3B slots."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from authoring_support import Author
A=Author(3,group='3B')
OS='SRC-OSB2E'
def E(o,h,c,p='',r=None):
    A.entry(o,h,c,p,source=(OS,r,'corroboration') if r else None)
GUIDE={
'3.6-01|DIST':["1 mark: autotrophic nutrition makes organic nutrients from inorganic materials, using an energy source such as light.","1 mark: whereas heterotrophic nutrition obtains ready-made organic nutrients from other organisms or their products."],
'3.6.1.1-01|FEATURE':["1 mark: names the elongated, tightly packed layer below the upper epidermis as palisade mesophyll.","1 mark: names the loose tissue with air spaces below it as spongy mesophyll."],
'3.6.1.1-02|FEATURE':["1 mark: the chloroplasts absorb a large amount of light energy for photosynthesis. This point must link the chloroplasts to absorbing light."],
'3.6.1.1-03|FEATURE':["1 mark: carbon dioxide diffuses in through the open pores, along the air spaces and on to the mesophyll cells. Saying only that the stomata open earns no point."],
'3.6.1.1-04|FEATURE':["1 mark: names water as the substance that xylem carries into the leaf. Mineral ions are also accepted. Sugars earn no mark because phloem carries them."],
'3.6.1.1-05|PROC':["1 mark: one feature with its function, for example chloroplast-rich palisade cells absorb light, so more photosynthesis can take place.","1 mark: a second, different feature with its function, for example air spaces let carbon dioxide diffuse to the mesophyll cells. The two features may come in either order; a feature named without its function earns nothing."],
'3.6.1.1-05|APP':["1 mark: carbon dioxide reaches the mesophyll cells of this leaf more slowly, because it diffuses more slowly through water than through air.","1 mark: less carbon dioxide reaches the chloroplasts, so carbon dioxide becomes the limiting factor and the rate of photosynthesis falls."],
'3.6.1.1-06|PROC':["1 mark: a workable way to make the impressions: thin varnish painted on each surface, left to dry, then lifted with clear tape onto a labelled slide.","1 mark: stomata are counted in several equal-sized fields on each surface and the mean counts compared, so the surface with more stomata per field is found."],
'3.6.1.1-06|WHY':["1 mark: stomata are not spread evenly, so one chosen field may not be typical of the whole surface.","1 mark: the mean of several equal-sized fields is more reliable, because chance differences between fields average out."],
'3.6.1.1-07|APP':["1 mark: the drawing is large, with clear, continuous pencil outlines and no shading.","1 mark: upper and lower epidermis enclose palisade mesophyll above spongy mesophyll, in the order seen in this section.","1 mark: the vein is drawn in the position and relative size it has in the figure, so the drawing records the specimen.","1 mark: label lines are ruled, do not cross, and end on the correct tissues."],
'3.6.1.1-07|WHY':["1 mark: real sections vary between species and with the angle of the cut, so they do not always match a memorised diagram.","1 mark: drawing what is visible records real evidence, because no feature is added just because it was expected."],
'3.6.1.2-01|FEATURE':["1 mark: iron is needed to make chlorophyll. The point that iron is part of the chlorophyll molecule earns nothing, because that is magnesium."],
'3.6.1.2-02|FEATURE':["1 mark: magnesium is part of the chlorophyll molecule. The point that it is needed to make chlorophyll is also accepted."],
'3.6.1.2-03|FEATURE':["1 mark: names one use: making DNA, or making ATP, the energy-transfer molecule."],
'3.6.1.2-04|FEATURE':["1 mark: nitrate supplies the nitrogen needed to make amino acids and so proteins. This point needs nitrogen, amino acids or proteins."],
'3.6.1.2-05|CHAIN':["1 mark: when iron is short, less chlorophyll is made, so less light is absorbed.","1 mark: photosynthesis slows, so the plant makes less carbohydrate for growth."],
'3.6.1.2-05|APP':["1 mark: the seedlings given iron turned green while the matched untreated ones stayed pale, so lack of iron caused the paleness.","1 mark: iron is needed to make chlorophyll, which the treated seedlings could then make because they now had iron."],
'3.6.1.2-06|CHAIN':["1 mark: when magnesium is short, less chlorophyll is made, so less light is absorbed.","1 mark: photosynthesis slows, so the plant has less carbohydrate for growth."],
'3.6.1.2-06|APP':["1 mark: the shaded seedling is limited by light, so in bright light this seedling photosynthesises faster.","1 mark: the deficient seedling cannot make enough chlorophyll because magnesium is missing, and extra light does not supply magnesium."],
'3.6.1.2-07|CHAIN':["1 mark: if phosphate is short, less DNA and ATP can be made.","1 mark: fewer new cells can be made, or less energy is available for growth, so the plant grows less."],
'3.6.1.2-07|APP':["1 mark: quotes the difference: roots are 4.8 cm shorter on average without phosphate (8.2 cm compared with 3.4 cm).","1 mark: lack of phosphate reduced root growth in this investigation, because phosphate is needed for the DNA and ATP used to make new cells."],
'3.6.1.2-08|CHAIN':["1 mark: when nitrate is short, less nitrogen is available for making amino acids.","1 mark: fewer proteins are made, so the cells grow and divide more slowly and the plant is stunted."],
'3.6.1.2-08|APP':["1 mark: extra light cannot supply nitrogen, so the lack of nitrate in this solution still limits growth.","1 mark: without nitrate the seedlings cannot make enough amino acids and proteins, because carbohydrate contains no nitrogen."],
'3.6.1.2-09|SYNTH':["1 mark: the independent variable is changed: a complete solution is compared with one lacking only nitrate.","1 mark: the dependent variable is measured, for example shoot height or dry mass after a set time.","1 mark: at least two of species, starting size, light and temperature are kept the same.","1 mark: a workable method, such as equal volumes of solution in labelled containers with the seedlings supported in them.","1 mark: several seedlings in each treatment (repeats), with the mean growth compared."],
'3.6.1.2-09|LIM':["1 mark: the limitation is that light differs between the groups as well as nitrate, so a difference in growth could be caused by the light.","1 mark: an improvement: put all the seedlings under the same lighting, or rotate their positions."],
'3.6.1.2-09|APP':["1 mark: quotes the difference in mean shoot growth, 4.1 cm (6.1 cm compared with 2.0 cm).","1 mark: lack of nitrate reduced growth in this investigation, because the other conditions were controlled."],
'3.6.1.3-01|FEATURE':["1 mark: names all four substances in the right places, carbon dioxide and water on the left and glucose and oxygen on the right. Light and chlorophyll are not needed for the mark."],
'3.6.1.3-02|FEATURE':["1 mark: the balanced equation with correct formulae and numbers. This is one point only, so an unbalanced equation earns nothing. Light and chlorophyll above the arrow are not needed."],
'3.6.1.3-03|SYNTH':["1 mark: the independent variable is changed: an opaque cover stops light reaching one part of a destarched leaf.","1 mark: the dependent variable is measured: the presence of starch, tested with iodine after the exposure.","1 mark: at least two of the same leaf, the same time in light and the same temperature are kept for both parts.","1 mark: a workable starch test: boil the leaf, decolourise it in ethanol warmed in a water bath (no flame), rinse it, then add iodine.","1 mark: repeats with several leaves, comparing covered with uncovered regions."],
'3.6.1.3-03|LIM':["1 mark: starch made before the investigation could give the blue-black result, so the error is that starch cannot be linked to the light treatment.","1 mark: an improvement: keep the plant in darkness for about two days first and test one leaf to check that it has no starch."],
'3.6.1.3-03|APP':["1 mark: starch formed only in the green areas of this leaf, where chlorophyll is present.","1 mark: so chlorophyll is needed for photosynthesis, because the leaf was destarched and all parts had the same light."],
'3.6.1.3-04|FEATURE':["1 mark: the rate rises as light intensity increases, while light is the limiting factor.","1 mark: the rate then levels off because another factor, such as carbon dioxide or temperature, now limits it. Saying the rate falls does not earn this point."],
'3.6.1.3-04|WHY':["1 mark: light is no longer the limiting factor at high intensity.","1 mark: extra light has no effect because another factor, such as carbon dioxide supply or temperature, now limits the rate."],
'3.6.1.3-05|FEATURE':["1 mark: the rate rises as carbon dioxide concentration increases, while carbon dioxide is the limiting factor.","1 mark: the rate then levels off because another factor, such as light or temperature, now limits it. Saying the rate falls does not earn this point."],
'3.6.1.3-05|WHY':["1 mark: in the well-lit greenhouse carbon dioxide is the limiting factor, so adding more raises the rate.","1 mark: in very dim light, light is the limiting factor because there is too little light energy, so extra carbon dioxide has little effect."],
'3.6.1.3-06|FEATURE':["1 mark: the rate rises as temperature increases up to an optimum, because enzyme-controlled reactions speed up.","1 mark: above the optimum the rate falls, because the enzymes are denatured. This point needs a fall, not just a levelling off."],
'3.6.1.3-06|WHY':["1 mark: high temperature changes the shape of the enzymes' active sites (denaturation).","1 mark: because the substrate no longer fits, fewer enzyme-substrate complexes form and the reactions slow."],
'3.6.1.3-07|PROC':["1 mark: photosynthesis first makes glucose.","1 mark: then many glucose units are joined together, so starch or cellulose is formed."],
'3.6.1.3-08|FEATURE':["1 mark: names one correct use, for example respiration to release energy.","1 mark: names a second, different use. Any two of respiration, cellulose for cell walls, sucrose for transport, starch for storage, and conversion to fats or amino acids are accepted."],
'3.6.1.3-08|WHY':["1 mark: because starch is insoluble, it does not affect the movement of water into and out of the cell by osmosis.","1 mark: starch can be broken down to glucose when the plant needs it, so it works as a store."],
'3.6.1.3-09|DEF':["1 mark: the definition names something in the environment that is in short supply.","1 mark: it restricts a life process, such as the rate of photosynthesis. Restricts or limits are accepted key words."],
'3.6.1.3-10|APP':["1 mark: at the same light intensity the second curve rises above the plateau of the first, so raising carbon dioxide increased the rate.","1 mark: in this graph the first curve is flat at high light, so extra light did not raise the rate and light was not limiting; raising carbon dioxide alone did raise it, so carbon dioxide was the limiting factor."],
'3.6.1.3-11|SYNTH':["1 mark: the independent variable, light intensity, is changed, for example by placing a lamp at measured distances.","1 mark: the dependent variable is measured: the volume of oxygen collected in a fixed time.","1 mark: at least two of temperature, shoot size and carbon dioxide supply are kept the same, for example with a water bath and the same hydrogencarbonate solution.","1 mark: a workable method: a shoot under water with the gas collected in a graduated tube, left to adjust for a few minutes at each light level.","1 mark: repeats at each light level, with the mean volume per minute calculated."],
'3.6.1.3-11|LIM':["1 mark: bubbles vary in size, so counting them is an inaccurate measure of the oxygen produced.","1 mark: an improvement: collect the gas and measure its volume in a graduated tube over the same time instead."],
'3.6.1.3-11|APP':["1 mark: quotes the rise in mean oxygen output from 0.8 to 1.4 cm³/min when the lamp moved from 20 cm to 10 cm.","1 mark: light intensity was limiting the rate at 20 cm, because temperature and carbon dioxide were controlled in this experiment."],
'3.6.1.3-12|FEATURE':["1 mark: names one way, for example adding carbon dioxide so that it does not limit the rate.","1 mark: names a second, different way. Any two of carbon dioxide enrichment, keeping the temperature near the optimum for the enzymes, and extra lighting are accepted."],
'3.6.1.3-12|WHY':["1 mark: several factors can limit the rate, so raising one leaves another factor limiting.","1 mark: too high a temperature can denature enzymes, so maximising one input can lower productivity. Wasted fuel or cost because the extra input gives no gain is also accepted."],
'3.6.1.3-13|SYNTH':["1 mark: the independent variable is changed: sealed tubes are kept in light or wrapped in opaque material for darkness.","1 mark: the dependent variable is measured: the colour of the indicator after a fixed time.","1 mark: at least two of plant mass, indicator volume, starting colour and temperature are kept the same.","1 mark: tubes with no plant, in light and in darkness, are included as controls.","1 mark: repeats of each treatment so that the results are reliable."],
'3.6.1.3-13|LIM':["1 mark: the lamp warms the lit tubes, so temperature differs as well as light; this error means the effect of light alone is uncertain.","1 mark: an improvement: use a cool light source such as an LED, or stand the tubes in a water bath."],
'3.6.1.3-13|APP':["1 mark: purple in light shows low carbon dioxide, so this plant took up more carbon dioxide in photosynthesis than it released in respiration.","1 mark: yellow in darkness shows high carbon dioxide, because respiration released carbon dioxide and no photosynthesis took place."],
'3.6.2.1-01|FEATURE':["1 mark: names a diet short of vitamin A-rich foods, such as liver, eggs or orange vegetables, as the cause.","1 mark: names poor vision in dim light (night blindness) as an effect."],
'3.6.2.1-01|WHY':["1 mark: vitamin A is needed for the light-sensitive cells of the retina to work normally.","1 mark: because these cells work poorly when vitamin A is short, seeing in dim light at dusk is difficult."],
'3.6.2.1-02|FEATURE':["1 mark: names a cause: too little vitamin D in the diet, or too little sunlight on the skin. Either is accepted.","1 mark: names the effect on bones: rickets, with soft bones that bend."],
'3.6.2.1-02|WHY':["1 mark: vitamin D is needed to absorb calcium from the gut, so less calcium reaches the growing bones.","1 mark: the bones harden poorly and bend under the body's weight, which is why the legs bow."],
'3.6.2.1-03|FEATURE':["1 mark: names the cause: a long-term diet lacking vitamin C from fresh fruit and vegetables.","1 mark: names one effect of scurvy: bleeding gums or poor wound healing."],
'3.6.2.1-03|WHY':["1 mark: vitamin C is needed to make and repair connective tissue.","1 mark: because too little vitamin C is available, new tissue in a wound is weak and healing is slow."],
'3.6.2.1-04|FEATURE':["1 mark: names the cause: too little iodine in the diet.","1 mark: names the effect: the thyroid gland enlarges to form a goitre."],
'3.6.2.1-04|WHY':["1 mark: iodine is used to make thyroid hormones.","1 mark: these hormones help control the body's metabolic rate, which is the reason iodine is needed in the diet."],
'3.6.2.1-04|MISCON':["1 mark: the error is the mineral: iron, not iodine, is needed for haemoglobin, so iron shortage causes anaemia.","1 mark: iodine shortage instead affects the thyroid gland and can cause goitre."],
'3.6.2.1-05|FEATURE':["1 mark: names a cause: too little iron in the diet, or iron lost in blood faster than it is replaced.","1 mark: names the effect on the blood: less haemoglobin is made, causing anaemia."],
'3.6.2.1-05|WHY':["1 mark: less haemoglobin means the blood carries less oxygen.","1 mark: because less oxygen reaches the muscles, aerobic respiration cannot release energy fast enough during activity, so the person tires."],
'3.6.2.1-06|FEATURE':["1 mark: names one requirement with its use, for example protein to make new tissue as the child grows.","1 mark: names a second, different requirement, for example calcium with vitamin D for bones and teeth. Iron for haemoglobin, or enough energy for growth and activity, is also accepted."],
'3.6.2.1-06|WHY':["1 mark: growth needs amino acids from protein to build new tissue, which energy alone does not supply.","1 mark: vitamins and minerals are also needed, because body processes such as bone growth and making haemoglobin depend on them."],
'3.6.2.1-07|FEATURE':["1 mark: names one role: supplying energy for activity and metabolism.","1 mark: names a second role: supplying materials for maintenance and repair of tissues."],
'3.6.2.1-07|WHY':["1 mark: the manual worker's muscles do more work, so they respire more.","1 mark: more food is used as fuel, which is the reason this worker's energy requirement is higher."],
'3.6.2.1-08|FEATURE':["1 mark: names one need: extra energy for making milk.","1 mark: names a second need: protein, calcium or water, which pass to the baby in the milk."],
'3.6.2.1-08|WHY':["1 mark: nutrients and water leave her body in the milk, so they must be replaced.","1 mark: because making milk also uses energy, her needs are greater than for maintenance alone."],
'3.6.2.1-09|FEATURE':["1 mark: names one feature, for example enough carbohydrate to supply energy for training.","1 mark: names a second, different feature, for example enough protein to repair muscle tissue. Enough water, or mineral salts to replace those lost in sweat, are also accepted."],
'3.6.2.1-09|WHY':["1 mark: carbohydrate is the fuel for repeated muscle respiration, so it must be replaced.","1 mark: water replaces the water lost in sweat, so that circulation and temperature control keep working."],
'3.6.2.1-10|FEATURE':["1 mark: names one way: providing energy for daily metabolism.","1 mark: names a second way: providing protein, vitamins and minerals for tissue maintenance and the immune system."],
'3.6.2.1-10|WHY':["1 mark: reduced appetite or diarrhoea can reduce nutrient intake or absorption.","1 mark: because illness also raises the body's need for repair, the gap between needs and supply is larger."],
'3.6.2.1-11|CHAIN':["1 mark: when the body grows quickly, more new tissue is made, so more building materials are needed.","1 mark: so the need for protein (amino acids) and for energy increases."],
'3.6.2.1-11|APP':["1 mark: this teenager is making new tissue, so needs amino acids for growth as well as repair.","1 mark: the adult only maintains existing tissue, so being heavier does not mean needing more protein for each kilogram of body mass."],
'3.6.2.1-12|CHAIN':["1 mark: when blood is lost, the iron in its haemoglobin is lost with it.","1 mark: so the need for dietary iron increases, because new haemoglobin must be made to replace it."],
'3.6.2.1-12|APP':["1 mark: energy comes mainly from carbohydrate and fat, whereas iron is a separate mineral need, so matching energy needs says nothing about iron.","1 mark: only the person with menstrual blood loss loses iron each month, so this person needs extra iron to replace the haemoglobin lost."],
'3.6.2.1-13|CHAIN':["1 mark: when activity increases, the muscles contract more and respire faster.","1 mark: more food is used as fuel, so the energy needed from the diet increases."],
'3.6.2.1-13|APP':["1 mark: seated duties use less energy than carrying sacks, because the muscles do less work.","1 mark: food intake stays the same, so energy intake now exceeds use and this surplus is stored as fat."],
'3.6.2.1-14|CHAIN':["1 mark: when a fetus grows, protein is needed for amino acids to build new fetal and maternal tissue.","1 mark: the mother's blood volume increases, so the need for iron to make haemoglobin rises."],
'3.6.2.1-14|APP':["1 mark: oil supplies energy but almost no iron.","1 mark: extra haemoglobin is made in pregnancy, so an iron-rich food such as meat or beans is still needed; oil alone cannot meet this need."],
'3.6.2.1-15|CHAIN':["1 mark: when a mother breastfeeds, nutrients and water leave her body in the milk, so they must be replaced.","1 mark: making milk also uses energy, so the total need rises above her maintenance needs."],
'3.6.2.1-15|APP':["1 mark: sugar in the drinks gives energy but no amino acids.","1 mark: protein is still needed to make milk proteins and to maintain her own tissues, so this diet stays inadequate."],
'3.6.2.1-16|FEATURE':["1 mark: names a cause: a prolonged shortage of food, for example after a drought.","1 mark: names an effect: loss of body mass and weakness."],
'3.6.2.1-16|WHY':["1 mark: the food supplies too little energy, so the body breaks down its fat stores for fuel.","1 mark: when the fat is used up, muscle and other tissues are broken down, which is why body mass keeps falling."],
'3.6.2.1-17|FEATURE':["1 mark: names a cause: too little fibre or too little water in the diet.","1 mark: names an effect: hard faeces that are difficult to pass."],
'3.6.2.1-17|WHY':["1 mark: fibre adds bulk and holds water in the contents of the gut.","1 mark: because the faeces stay soft and bulky, the muscles of the gut wall move them along easily."],
'3.6.2.1-18|FEATURE':["1 mark: names a dietary risk factor: a diet high in saturated fat.","1 mark: names a consequence: the coronary arteries narrow, or less oxygen reaches the heart muscle. Either point is accepted."],
'3.6.2.1-18|WHY':["1 mark: a narrowed coronary artery lets less blood, and so less oxygen, reach the heart muscle.","1 mark: because aerobic respiration in the muscle is restricted, a severe shortage can kill muscle cells."],
'3.6.2.1-19|FEATURE':["1 mark: names the imbalance: energy intake greater than energy use over a long time.","1 mark: names one health risk, for example cardiovascular disease or type 2 diabetes."],
'3.6.2.1-19|WHY':["1 mark: the meals supply more energy than the body uses.","1 mark: because the surplus is not respired, it is converted to fat and stored, so fat stores increase."],
'3.6.2.1-20|FEATURE':["1 mark: names the cause: a long-term lack of vitamin C in the diet.","1 mark: names one effect: bleeding gums or poor wound healing."],
'3.6.2.1-20|WHY':["1 mark: energy comes mainly from carbohydrate and fat, which are different nutrients from vitamin C.","1 mark: because a restricted diet can supply enough energy but still lack vitamin C, connective tissue is not maintained."],
'3.6.2.1-21|SYNTH':["1 mark: the independent variable is the comparison: groups chosen by how often they drink sugary drinks, which is not changed by the investigator.","1 mark: the dependent variable is measured: a recorded indicator of tooth decay, measured in the same way for everyone.","1 mark: other factors such as age and other eating habits are recorded or matched (controlled), so the groups are comparable.","1 mark: an ethical method: volunteers give consent, or anonymous records are used.","1 mark: many volunteers are included (repeats), with the percentage or mean for each group compared."],
'3.6.2.1-21|LIM':["1 mark: one person's memory of a month's food is unreliable, or one person is not a representative sample. Either limitation is accepted.","1 mark: an improvement that matches it: food diaries kept at the time, or records from many consenting volunteers instead."],
'3.6.2.1-21|APP':["1 mark: quotes the data: decay in 12 of 30 (40%) frequent consumers compared with 4 of 30 (about 13%) infrequent consumers.","1 mark: decay is more common with frequent sugary drinks in this survey, but this does not prove the drinks caused it, because other habits were not controlled."],
'3.6.2.1-22|CHAIN':["1 mark: drought reduces crop and livestock production, so less food is available.","1 mark: flooding destroys crops and damages roads, so food is lost and cannot be moved to where it is needed.","1 mark: with unequal distribution some households cannot obtain food even when supplies exist elsewhere, so the result is hunger in those households."],
'3.6.2.1-22|APP':["1 mark: with its own store gone, this district depends entirely on food brought in from outside.","1 mark: the damaged road stops national supplies reaching the district, so an adequate national total does not mean food reaches people there."],
'3.6.2.2-01|DEF':["1 mark: the definition gives the taking in of substances into the body.","1 mark: the key words through the mouth are needed. Eating or drinking is accepted for this part."],
'3.6.2.2-02|DEF':["1 mark: the definition gives the breakdown of food into smaller pieces, for example by chewing.","1 mark: the key words without chemical change to the food molecules are needed."],
'3.6.2.2-03|DEF':["1 mark: the definition gives the breakdown of large, insoluble molecules.","1 mark: the key words into smaller, soluble molecules are needed. Mention of enzymes is accepted but not needed."],
'3.6.2.2-04|DEF':["1 mark: the definition gives the movement of small food molecules and ions through the wall of the intestine.","1 mark: the key words into the blood are needed."],
'3.6.2.2-05|DEF':["1 mark: the definition gives the passing out of food that has not been digested or absorbed.","1 mark: the key words through the anus are needed. Mention of faeces is accepted but not needed."],
'3.6.2.2-06|FEATURE':["1 mark: names the function of the oesophagus: muscle contractions (peristalsis) move swallowed food down to the stomach.","1 mark: names the function of the rectum: storing faeces before egestion through the anus."],
'3.6.2.2-06|WHY':["1 mark: the liver and pancreas release their secretions through ducts into the small intestine.","1 mark: the food mixes with these secretions inside the gut, because food stays in the alimentary canal and never enters the organs themselves."],
'3.6.2.2-07|FEATURE':["1 mark: names the type of pathogen: a bacterium.","1 mark: names one route of transmission: swallowing contaminated water or food."],
'3.6.2.2-08|CHAIN':["1 mark: when the toxin acts, chloride ions are secreted into the small intestine, which draws water into the gut by osmosis.","1 mark: the result is watery diarrhoea, which removes water and salts from the blood and dehydrates the person."],
'3.6.2.2-08|APP':["1 mark: the secreted ions make the contents of the intestine more concentrated than the body fluids, so water moves from the body fluids into the intestine by osmosis.","1 mark: this water comes from the body, not from food just eaten, so fluid loss continues even after eating very little."],
'3.6.2.3-01|FEATURE':["1 mark: names the function: speeding up (catalysing) the breakdown of large food molecules into smaller ones."],
'3.6.2.3-02|FEATURE':["1 mark: large insoluble molecules are made into small soluble ones, which can be absorbed through the gut wall. This point needs absorption."],
'3.6.2.3-03|PROC':["1 mark: first, amylase breaks starch down to maltose.","1 mark: then maltase breaks maltose down to glucose, so glucose is the sugar absorbed."],
'3.6.2.3-03|MECH':["1 mark: salivary amylase starts to break starch down to maltose in the mouth.","1 mark: stomach acid stops the salivary amylase working, so starch digestion pauses in the stomach.","1 mark: pancreatic amylase then continues breaking starch down to maltose in the small intestine.","1 mark: maltase on the intestinal lining converts maltose to glucose, which is absorbed."],
'3.6.2.3-04|FEATURE':["1 mark: names the substrate: starch.","1 mark: names the product: maltose, a smaller sugar."],
'3.6.2.3-04|WHY':["1 mark: enzymes are specific: the active site of amylase fits starch only.","1 mark: because protein does not fit this active site, amylase cannot digest it, so a protease is needed instead."],
'3.6.2.3-05|FEATURE':["1 mark: names the substrate: protein.","1 mark: names the final products: amino acids."],
'3.6.2.3-05|WHY':["1 mark: proteases break proteins into amino acids, which are small enough to be absorbed.","1 mark: food protein becomes usable because cells join the absorbed amino acids to build the body's own proteins."],
'3.6.2.3-06|FEATURE':["1 mark: names the substrate: fat (lipid).","1 mark: names the products: fatty acids and glycerol."],
'3.6.2.3-06|WHY':["1 mark: many small droplets have a larger total surface area than one large drop.","1 mark: digestion is faster because lipase has more fat surface to act on."],
'3.6.2.3-07|FEATURE':["1 mark: names the role: the acid kills many of the bacteria swallowed with food."],
'3.6.2.3-08|FEATURE':["1 mark: the acid gives the low pH at which the stomach protease works best. This point needs the link to the enzyme."],
'3.6.2.3-09|FEATURE':["1 mark: names the liver as where bile is made. Storage in the gall bladder is not needed for this point.","1 mark: names where it goes: into the small intestine through a duct.","1 mark: bile is alkaline, so it helps neutralise the acidic stomach contents."],
'3.6.2.3-09|WHY':["1 mark: intestinal enzymes work best in less acidic conditions.","1 mark: because neutralising the acid raises the pH towards their optimum, their activity increases."],
'3.6.2.3-09|MISCON':["1 mark: the error is that bile is not acidic: it is alkaline.","1 mark: bile enters the small intestine, not the stomach, and neutralises the stomach acid there instead, raising the pH."],
'3.6.2.3-10|FEATURE':["1 mark: names emulsification: bile salts break fat into small droplets.","1 mark: the droplets have a larger total surface area.","1 mark: lipase can then reach more fat, so it digests the fat faster. Bile is not an enzyme and does not digest the fat."],
'3.6.2.3-10|WHY':["1 mark: emulsification only breaks fat into smaller droplets, while the fat molecules stay unchanged.","1 mark: lipase is still needed because chemical digestion breaks the fat molecules into fatty acids and glycerol."],
'3.6.2.3-11|SYNTH':["1 mark: the independent variable is changed: bile salts are added to one tube and an equal volume of water to the other.","1 mark: the dependent variable is measured: how far the oil and water separate, or how cloudy they stay, after a set time.","1 mark: at least two of oil volume, water volume, tube size, shaking time and temperature are kept the same.","1 mark: a workable method: shake both tubes in the same way, then observe them at set times.","1 mark: repeats each treatment and compares the results, for example the mean separation time."],
'3.6.2.3-11|LIM':["1 mark: the limitation is that longer shaking could itself break the oil into finer droplets, so the difference may not be caused by the bile salts.","1 mark: an improvement: shake both tubes for the same measured time and with the same force."],
'3.6.2.3-11|APP':["1 mark: the oil stays as fine droplets with bile salts but separates in the controls, so bile salts keep the fat emulsified.","1 mark: this shows emulsification, not chemical digestion, because no lipase was added and no products were tested for."],
'3.6.2.4-01|FEATURE':["1 mark: names the main region for absorption: the small intestine.","1 mark: names the structure that increases surface area: villi."],
'3.6.2.4-02|FEATURE':["1 mark: names the structure: many finger-like projections (villi) extend into the lumen.","1 mark: together they greatly increase the internal surface area of the small intestine."],
'3.6.2.4-02|WHY':["1 mark: more absorbing surface is exposed to the digested food.","1 mark: absorption is faster because more molecules can cross into the blood at the same time."],
'3.6.2.4-03|FEATURE':["1 mark: names the blood capillaries, which take up sugars and amino acids.","1 mark: names the central lacteal, which takes up the products of fat digestion."],
'3.6.2.4-04|FEATURE':["1 mark: names the function: carrying blood rich in absorbed nutrients from the small intestine to the liver."],
'3.6.2.4-04|MISCON':["1 mark: the error is the vessel: absorbed glucose reaches the liver in the hepatic portal vein, not the hepatic artery.","1 mark: the hepatic artery instead brings oxygenated blood to the liver."],
'3.6.2.4-05|FEATURE':["1 mark: names the storage process: the liver converts excess glucose into glycogen.","1 mark: names the later change: glycogen is broken down to glucose when it is needed."],
'3.6.2.4-05|WHY':["1 mark: glycogen is a reserve built up after a meal.","1 mark: because little glucose enters from the gut between meals, glycogen is broken down to supply glucose then."],
'3.6.2.4-06|FEATURE':["1 mark: names the process: excess amino acids are deaminated in the liver.","1 mark: the nitrogen-containing part is made into urea, which is excreted."],
'3.6.2.4-06|WHY':["1 mark: excess amino acids cannot be stored, so they are broken down in the liver.","1 mark: deamination removes the nitrogen-containing amino group, which is converted into urea; this is why more urea is made."],
'3.6.2.4-07|FEATURE':["1 mark: names one function: fat is a store of chemical energy.","1 mark: names another function: fat under the skin insulates against heat loss. Cushioning of organs is also accepted."],
'3.6.2.4-07|WHY':["1 mark: fat stores a lot of energy for its mass.","1 mark: it can be respired later when food intake is too low, which is the reason it is a good long-term reserve."],
'3.6.2.4-08|FEATURE':["1 mark: names the colon (large intestine). The small intestine earns nothing because the question excludes it."],
}
def C(o,t,p,ans,hold=False):
    A.card(o,t,p,ans,GUIDE[o+'|'+t],pending=hold)
    s=next(s for s in A.wo['item_slots'] if s['objective_id']=='OBJ-6116-'+o and s['subtype']==t)
    assert len(GUIDE[o+'|'+t])==s['mark_tariff'],(o,t,s['mark_tariff'])
    if s['assessment_objectives']==['AO2']:
        A.notes['ao_demand_evidence'].append({'item_id':s['slot'],'new_input':p,'inference':ans,'classification':'B: consequential reasoning from the given constraints/results; not the scenario name alone.'})

E('3.6-01','Two ways of obtaining nutrients',[
'Autotrophic nutrition makes organic nutrients from inorganic substances, using an energy source such as light.',
'Heterotrophic nutrition obtains ready-made organic nutrients from other organisms or their products.'
],'''A green bean plant takes carbon dioxide from the air and water from its surroundings. With light energy it builds sugar: it does not obtain this sugar by absorbing it from the soil. Mineral ions absorbed from soil are necessary materials, but they are not the plant’s food or an energy supply. A person eating beans takes in organic material made by another organism and is a heterotroph.

Nutrition concerns obtaining materials for growth, repair and respiration. Autotrophs also respire: making nutrients and releasing energy from nutrients are different processes. Heterotrophs include animals, fungi and many bacteria; they need not eat living prey. A fungus absorbing soluble substances from dead leaves is also obtaining ready-made organic nutrients. Classify the mode by where the organic nutrients come from rather than by whether the organism moves. Respiration then releases the energy stored in these nutrients, and it is the same process in both kinds of organism.''','8.1 Overview of Photosynthesis')
C('3.6-01','DIST','Distinguish autotrophic nutrition from heterotrophic nutrition.','Autotrophs make organic nutrients from inorganic materials; heterotrophs obtain ready-made organic nutrients from other organisms or their products.')

E('3.6.1.1-01','Leaf structure in cross-section',[
'A typical dicotyledonous leaf has upper and lower epidermis surrounding palisade and spongy mesophyll.',
'Veins contain xylem and phloem, and stomata are pores bordered by guard cells.'
],'''In a leaf cross-section, follow the tissues from the upper surface downwards: waxy cuticle, upper epidermis, closely packed elongated palisade cells, irregular spongy cells with air spaces, and lower epidermis. A vein cuts across these layers. Within a typical vein, xylem lies towards the upper side and phloem towards the lower side. Guard cells surround an opening called a stoma, so a stoma is a pore and not a solid cell. Colours in prepared slides may come from stains, so identify tissues from their position and structure rather than their colour.''','30.4 Leaves')
C('3.6.1.1-01','FEATURE','Identify the elongated cell layer directly below the upper epidermis and the loose tissue below it in Fig. VIS-6116-3.6.1.1-01.','Palisade mesophyll; spongy mesophyll.',hold=True)
E('3.6.1.1-02','Chloroplast distribution',[
'Palisade mesophyll cells contain many chloroplasts near the illuminated upper surface of a typical leaf.',
'Chlorophyll in chloroplasts absorbs light energy for photosynthesis.'
],'''Spongy mesophyll also photosynthesises, but its looser arrangement serves gas movement. The ordinary epidermal cells are usually transparent and lack chloroplasts, allowing light to reach the mesophyll. Guard cells are an exception to this usual epidermal pattern. Location matters as well as number: chloroplast-rich cells near incoming light can absorb much of it before it passes through the leaf.''','30.4 Leaves')
C('3.6.1.1-02','FEATURE','State the significance of having many chloroplasts in palisade cells near the upper leaf surface.','They absorb light energy effectively for photosynthesis.')
E('3.6.1.1-03','Gas exchange within the leaf',[
'Open stomata allow gases to diffuse between the atmosphere and the leaf air spaces; closure reduces this exchange.',
'Air spaces and moist mesophyll surfaces provide a large internal surface for gas exchange.'
],'''Carbon dioxide entering a stoma moves through air spaces, dissolves in the moist surface film and diffuses into cells. Oxygen can move out in the opposite direction when photosynthesis produces it faster than respiration uses it. The direction of net movement depends on concentration differences, not on the pore pumping gases. Closing stomata can conserve water but also restrict carbon dioxide entry.''','30.4 Leaves')
C('3.6.1.1-03','FEATURE','State how opening stomata helps mesophyll cells obtain carbon dioxide.','When pores open, carbon dioxide can enter down its gradient and reach mesophyll surfaces through internal air spaces.')
E('3.6.1.1-04','Transport through leaf veins',[
'Xylem supplies a leaf with water and mineral ions from the roots.',
'Phloem transports sucrose and amino acids between sources and regions of demand or storage.'
],'''Water is a reactant in photosynthesis; ions support the cell structures and reactions that make it possible. Sugar made in a leaf can be converted to sucrose for transport to growing roots or storage organs. This removal also supplies parts that cannot photosynthesise. A vein is a transport bundle, not an air passage. Its xylem and phloem have different contents and functions.''','30.4 Leaves')
C('3.6.1.1-04','FEATURE','State the main substance that xylem transports into a leaf.','Water (mineral ions are also accepted).')
E('3.6.1.1-05','Structure linked to photosynthesis',[
'The thin leaf shortens diffusion paths, while transparent surface layers admit light to chloroplast-rich mesophyll.',
'Connected air spaces let carbon dioxide reach a large area of mesophyll surface, and veins supply water.'
],'''An adaptation explanation connects a visible structure to a particular need. “Many chloroplasts” needs the link “absorb light”; “air spaces” needs “permit gases to reach mesophyll cells”. A broad lamina intercepts light, but the internal arrangement distributes that light and the raw materials. Think through a damaged leaf: if air spaces become water-filled while chlorophyll remains unchanged, carbon dioxide moves through the tissue more slowly because diffusion in water is slower than in air. Green colour alone therefore does not establish a normal rate. Each feature helps with one part of the process, and photosynthesis still needs light, carbon dioxide and water together.''','30.4 Leaves')
C('3.6.1.1-05','PROC','Explain how two internal features of a typical dicot leaf assist photosynthesis.','Chloroplast-rich palisade cells absorb light; spongy air spaces let carbon dioxide diffuse to mesophyll cells.')
C('3.6.1.1-05','APP','Explain why photosynthesis may fall in a green leaf whose air spaces have become water-filled. Its chlorophyll content and illumination are unchanged; gases diffuse more slowly through water than air.','Water in the spaces slows carbon dioxide diffusion to mesophyll cells; reduced carbon dioxide supply can limit photosynthesis.')
E('3.6.1.1-06','Preparing epidermal impressions',[
'A dried clear nail-varnish impression can reproduce a leaf surface for viewing stomata with a microscope.',
'Comparing stomatal distributions requires equal sampled areas and several fields on each surface.'
],'''Apply a thin patch of clear varnish to upper and lower surfaces of a suitable leaf, away from major veins. Let it dry; lift the film with clear adhesive tape and put it flat on a labelled slide. Start with low power, focus, then choose a useful higher power. Count stomata in equal-sized fields without selecting unusually crowded areas. Use several fields and several leaves; calculate the mean count per equal area for each surface. Keep magnification and leaf type consistent. Varnish is flammable, so work with ventilation and keep it away from flames.

A worked example: counts of 18, 22 and 20 stomata in three fields on the lower surface give a mean of 20; counts of 4, 6 and 5 on the upper surface give a mean of 5. Many dicotyledonous leaves have more stomata on the lower surface, where less water is lost to the sunlit air.''')
C('3.6.1.1-06','PROC','Describe how to prepare nail-varnish impressions of both leaf surfaces and determine any difference in their stomatal density.','Dry thin varnish patches on each surface, lift them onto labelled slides with clear tape and focus under a microscope; count stomata in several equal-area fields on each surface and compare mean counts.')
C('3.6.1.1-06','WHY','Explain why a stomatal-count investigation should examine several equal-area fields on each leaf surface rather than one chosen field.','Stomata are unevenly distributed, so one field may be unrepresentative; repeated equal-area counts give a fairer estimate of the mean density.')
E('3.6.1.1-07','Drawing and interpreting a section',[
'A biological drawing records structures actually visible in the specimen with clear outlines and appropriate proportions.',
'Leaf tissues should be identified using their arrangement and cell shapes, with accurate label lines.'
],'''Begin at low magnification to orientate the whole section, then inspect detail. Draw a large view, use continuous pencil lines without decorative shading, and separate individual cells where visible. Rule label lines to the named structure without crossing them. Include upper and lower epidermis, palisade and spongy tissues, a vein and a stoma where the chosen field shows them. Draw only what the section shows. A layer of elongated cells and a region of irregular cells can be distinguished even when staining hides chlorophyll.

To find the magnification of a drawing, measure the length of a structure on the drawing and divide by its actual length, with both in the same unit. A cell drawn 30 mm long that is really 0.06 mm long is magnified 500 times.''')
C('3.6.1.1-07','APP','Draw a large labelled biological drawing of the leaf transverse section in Fig. VIS-6116-3.6.1.1-07. Include the visible epidermal layers, palisade and spongy mesophyll, and vein.','Drawing shows the actual section: upper and lower epidermis enclosing palisade above spongy mesophyll, with the visible vein in correct proportion; labels terminate on the correct tissues.',hold=True)
C('3.6.1.1-07','WHY','Explain why a drawing of a prepared leaf section should show what is visible rather than copy a memorised diagram.','Sectioning and species differences can change the visible arrangement; recording the specimen preserves evidence rather than introducing features that were not observed.')

for o,h,c,p in [
('01','Iron in plants',['Iron ions are needed for chlorophyll formation.','A plant requires iron in small amounts for healthy green growth.'],'Iron is not the central atom of chlorophyll; magnesium has that role. Availability can matter as much as the amount in soil: a root must be able to absorb the ions. Nutrient solutions allow a plant to be supplied with a known mixture.'),
('02','Magnesium in plants',['Magnesium is a constituent of chlorophyll.','A shortage of magnesium can reduce the amount of chlorophyll in leaves.'],'Magnesium is a mineral ion rather than an organic food. A plant with enough light still needs the raw materials to build its photosynthetic machinery.'),
('03','Phosphate in plants',['Phosphate ions are needed to make DNA and energy-transfer molecules such as ATP.','Phosphate supply supports cell division and growth of roots and other tissues.'],'ATP transfers energy within cells; phosphate fertiliser does not supply light energy. DNA is the genetic material that must be copied when cells divide. These roles connect phosphate supply to production of new cells.'),
('04','Nitrate in plants',['Nitrate ions provide nitrogen for making amino acids.','Amino acids are assembled into proteins needed for growth.'],'Proteins include enzymes and structural materials. Nitrate uptake and amino-acid synthesis allow a plant to turn some carbohydrate products into nitrogen-containing molecules. Nitrogen gas in the air is not directly usable by an ordinary plant root in the same way as dissolved nitrate.')]:
 E('3.6.1.2-'+o,h,c,p,r='31.1 Nutritional Requirements of Plants')
C('3.6.1.2-01','FEATURE','State why plants require iron ions.','For chlorophyll formation.')
C('3.6.1.2-02','FEATURE','State why plants require magnesium ions.','Magnesium is part of chlorophyll.')
C('3.6.1.2-03','FEATURE','State one use of phosphate ions in plants.','Making DNA.')
C('3.6.1.2-04','FEATURE','State why nitrate ions are required for plant growth.','They supply nitrogen for amino acids and hence proteins.')
E('3.6.1.2-05','Iron deficiency',[
'Iron deficiency can cause chlorosis because insufficient chlorophyll is formed.',
'Lower chlorophyll content can reduce photosynthesis and restrict growth when light capture becomes limiting.'
],'''Chlorosis means yellowing caused by a shortage of green chlorophyll. Iron-related chlorosis often shows first in young leaves. Several mineral deficiencies and other stresses can also make leaves yellow, so a controlled nutrient comparison is stronger evidence than colour alone. If adding iron restores greenness while matched untreated plants stay pale, that supports iron shortage as the cause.''','31.1 Nutritional Requirements of Plants')
C('3.6.1.2-05','CHAIN','Explain how iron deficiency can reduce plant growth.','Less chlorophyll is formed; reduced light absorption can lower photosynthesis and carbohydrate supply for growth.')
C('3.6.1.2-05','APP','Explain what these seedling results show about the cause of the pale leaves. All solutions lack iron; half receive iron at week 2 and turn green, while matched untreated plants remain pale. Other conditions are the same.','The recovery supports iron deficiency as the cause of paleness; iron addition permits chlorophyll formation, unlike the untreated comparison.')
E('3.6.1.2-06','Magnesium deficiency',[
'Magnesium deficiency can cause chlorosis because chlorophyll contains magnesium.',
'Reduced chlorophyll can restrict photosynthesis and leave less carbohydrate for growth.'
],'''Magnesium shortage often shows first in older leaves, because the plant moves magnesium from old leaves to new growth. Separate a role from an effect: “magnesium is part of chlorophyll” names the role; “less chlorophyll leads to less light capture and slower growth” explains the effect. A yellow plant still respires; it is photosynthesis that is reduced.''','31.1 Nutritional Requirements of Plants')
C('3.6.1.2-06','CHAIN','Explain how magnesium deficiency can cause slow plant growth.','Less chlorophyll can be made; reduced photosynthesis produces less carbohydrate for growth.')
C('3.6.1.2-06','APP','Explain why a shaded seedling and a magnesium-deficient seedling may both grow slowly, although moving them into bright light helps just the shaded one. Water and other nutrients are sufficient.','The shaded plant lacked light; the deficient plant lacks magnesium for chlorophyll, so extra light does not replace the missing chlorophyll constituent.')
E('3.6.1.2-07','Phosphate deficiency',[
'Phosphate deficiency can restrict growth because cells lack sufficient material for DNA and ATP.',
'Poor phosphate supply can result in weak root development and reduced overall growth.'
],'''A stunted seedling may be limited by water, temperature or another nutrient. Comparing a complete solution with a solution lacking only phosphate, while controlling everything else, links a difference to phosphate. Phosphate is needed by roots as well as shoots, so root length is a useful measurement as well as leaf colour. For example, mean root lengths of 8.2 cm with phosphate and 3.4 cm without give a difference of 4.8 cm.''','31.1 Nutritional Requirements of Plants')
C('3.6.1.2-07','CHAIN','Explain why phosphate deficiency can restrict seedling growth.','It restricts production of DNA and ATP; cell division and energy-dependent growth are therefore limited.')
C('3.6.1.2-07','APP','Seedlings grown in a complete solution have a mean root length of 8.2 cm. Matched seedlings in a solution lacking only phosphate have a mean root length of 3.4 cm. Each treatment has ten seedlings, with the same light and temperature. Explain what conclusion these results support.','The mean root length is 4.8 cm shorter without phosphate, so the results support the conclusion that phosphate shortage reduced root growth; phosphate is needed for the DNA and ATP used to make new cells.')
E('3.6.1.2-08','Nitrate deficiency',[
'Nitrate deficiency restricts amino-acid and protein production.',
'Reduced protein synthesis can cause stunted growth, often with yellowing leaves.'
],'''Nitrogen is needed for new cytoplasm and enzymes. Adding more sugar cannot replace the missing nitrogen, even though a plant needs both carbon-containing materials and nitrogen-containing materials to grow. Nitrate shortage usually shows first as yellowing of the older leaves, because the plant moves nitrogen from old leaves to new growth. Growth slows across the whole plant, and stems are often thin and weak.''','31.1 Nutritional Requirements of Plants')
C('3.6.1.2-08','CHAIN','Explain how nitrate deficiency causes stunted growth.','Less nitrogen is available for amino acids; fewer proteins can be made for cell growth and division.')
C('3.6.1.2-08','APP','Explain why supplying extra light did not restore growth in seedlings whose solution contained no nitrate, although their leaves still made carbohydrate.','Extra light cannot supply nitrogen; without nitrate the seedlings cannot make sufficient amino acids and proteins for growth.')
E('3.6.1.2-09','Investigating mineral shortage',[
'A mineral-deficiency investigation compares a complete nutrient solution with one lacking the named mineral.',
'The comparison requires similar seedlings, matched growing conditions, repeated measurements and replication.'
],'''Germinate seedlings of the same species and similar initial size. Put replicated groups into complete solution and into otherwise identical solution without nitrate, supporting the roots and shielding solution from light to discourage algae. Keep solution volume, aeration, temperature and illumination alike. Record initial and later shoot height, leaf colour and, if appropriate, final dry mass; use the same growth interval. Replace or top up solutions consistently. Label units and calculate means for each group. Differences in initial plant size, unnoticed contamination or unequal light can weaken the comparison. Random allocation and rotating positions reduce position bias. Removing only the named mineral, and keeping the rest of the solution the same, is what links a difference in growth to that mineral.''')
C('3.6.1.2-09','SYNTH','Describe a complete investigation of the effect of nitrate deficiency on seedling growth.','Change nitrate presence using complete solution and an otherwise matching nitrate-free solution; measure growth over a fixed time; keep species, starting size, light and temperature alike; grow labelled seedlings with equal solution volumes and aeration; repeat with several seedlings per treatment and compare mean growth.')
C('3.6.1.2-09','LIM','Suggest one limitation and a linked improvement when all nitrate-free seedlings stand on a dim windowsill and all complete-solution seedlings stand under a lamp.','Unequal illumination confounds nitrate treatment with light; randomise seedlings between positions under matched illumination.')
C('3.6.1.2-09','APP','Suggest a conclusion from a controlled growth investigation: mean increase in shoot height is 6.1 cm in complete solution and 2.0 cm without nitrate over 14 days, with ten seedlings per group.','Nitrate shortage reduced growth under these conditions; the complete-solution group grew 4.1 cm more on average.')

E('3.6.1.3-01','The photosynthesis word equation',[
'Photosynthesis uses light energy absorbed by chlorophyll to make glucose from carbon dioxide and water, releasing oxygen.',
'The word equation is carbon dioxide + water → glucose + oxygen, with light and chlorophyll as conditions.'
],'''Write the conditions above the arrow or alongside the equation. Light supplies energy and chlorophyll absorbs it; neither is a raw material that is turned into sugar. Carbon enters in carbon dioxide, not in soil minerals. Water comes through the xylem. The glucose stores chemical energy that can later be released in respiration. Photosynthesis and respiration can occur in the same illuminated plant.''','8.1 Overview of Photosynthesis')
C('3.6.1.3-01','FEATURE','State the word equation for photosynthesis.','Carbon dioxide + water → glucose + oxygen (in light, using chlorophyll).')
E('3.6.1.3-02','A balanced photosynthesis equation',[
'The balanced summary equation is 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.',
'The coefficients conserve carbon, hydrogen and oxygen atoms; light energy and chlorophyll are required conditions.'
],'''Count atoms to check the equation: six carbon atoms on each side, twelve hydrogen atoms on each side, and eighteen oxygen atoms on each side. A coefficient multiplies an entire molecule, so balance an equation by changing coefficients and never the formulae. This is an overall equation that summarises many separate reactions. Its glucose product contains chemical energy.''','8.1 Overview of Photosynthesis')
C('3.6.1.3-02','FEATURE','State the balanced chemical equation for photosynthesis.','6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (light and chlorophyll).')
E('3.6.1.3-03','Testing requirements for photosynthesis',[
'A destarched leaf can be tested for newly accumulated starch after a controlled light treatment.',
'Light, chlorophyll and carbon dioxide can be investigated separately by suitable comparisons.'
],'''Destarch suitable plants in darkness beforehand so old starch is less likely to confuse the result. For light, cover part of a leaf on both sides with opaque material and expose the plant to light; the uncovered region is the comparison. For chlorophyll, mark green and non-green regions of a variegated leaf before testing it. For carbon dioxide, use matched destarched plants in sealed transparent containers: one has an absorber kept away from the plant, while the comparison lacks the absorber. Match illumination, temperature and duration.

For the starch test, kill the leaf in hot water, decolourise it in ethanol warmed in a hot-water bath, rinse to soften, then add iodine solution. Blue-black indicates starch; yellow-brown indicates no detected starch. Ethanol is flammable: use teacher supervision, eye protection and no naked flame. A green illuminated region in the same leaf helps show that the starch test and treatment worked.''')
C('3.6.1.3-03','SYNTH','Describe a controlled investigation of the requirement for light in photosynthesis, including a starch test.','Change light reaching part of a destarched leaf with an opaque cover on both sides; measure starch presence with iodine after exposure; keep other leaf conditions and exposure duration the same; boil in water, decolourise in warm ethanol in a water bath away from flames, rinse and add iodine; repeat with several leaves and compare covered with uncovered regions.')
C('3.6.1.3-03','LIM','Suggest a limitation and an improvement if a leaf tests blue-black after illumination but the plant was not destarched before the investigation.','Old starch may give a positive result unrelated to the treatment; destarch plants first and test a comparable leaf to check the starting condition.')
C('3.6.1.3-03','APP','Suggest the justified conclusion: after destarching and equal illumination, green areas of a variegated leaf test blue-black, while non-green areas stay brown with iodine.','Starch accumulated in chlorophyll-containing areas; the contrast supports a requirement for chlorophyll under these test conditions.')
E('3.6.1.3-04','Light intensity and rate',[
'Increasing light intensity raises photosynthesis rate while light is the limiting factor.',
'A plateau can occur when another factor limits the rate, so further light then gives no increase.'
],'''At a constant suitable temperature and carbon dioxide supply, a dimly lit plant has little light energy available. Increasing illumination can increase sugar production. This relationship does not continue without limit: carbon dioxide supply or temperature may then constrain it. On a graph of rate against light intensity, the rising part of the curve shows light limiting the rate and the flat part shows another factor limiting it.''','8.3 Using Light Energy to Make Organic Molecules')
C('3.6.1.3-04','FEATURE','Describe the usual effect of increasing light intensity on photosynthesis when carbon dioxide and temperature are held constant.','Rate rises while light is limiting; it levels off when another factor becomes limiting.')
C('3.6.1.3-04','WHY','Explain why extra illumination can fail to raise photosynthesis at high light intensity.','Light is no longer limiting; a factor such as carbon dioxide supply now restricts the rate.')
E('3.6.1.3-05','Carbon dioxide concentration and rate',[
'Increasing carbon dioxide concentration increases photosynthesis rate while carbon dioxide is limiting.',
'At a plateau another factor, such as light intensity, prevents further increase.'
],'''Carbon dioxide is a reactant and carbon source. Its availability differs from the availability of light energy. In a closed greenhouse it may be used faster than it enters, particularly in bright conditions. Raising its concentration can help then, but cannot make up for darkness. On a graph of rate against carbon dioxide concentration, the curve rises and then flattens in the same way as for light. The units on each axis show what was measured, for example rate in cm³ of oxygen per minute.''','8.3 Using Light Energy to Make Organic Molecules')
C('3.6.1.3-05','FEATURE','Describe the effect of increasing carbon dioxide concentration on photosynthesis at fixed light intensity and temperature.','Rate increases while carbon dioxide is limiting; it plateaus when another factor limits it.')
C('3.6.1.3-05','WHY','Explain why carbon dioxide enrichment may increase photosynthesis in a well-lit greenhouse but have little effect in a very dim one.','Carbon dioxide may limit the well-lit plants; in dim light the shortage of light energy can limit the rate instead.')
E('3.6.1.3-06','Temperature and rate',[
'When temperature limits photosynthesis, warming towards an optimum can increase enzyme-controlled reaction rates.',
'Above a suitable range, photosynthesis can fall as enzymes are damaged and other heat stresses occur.'
],'''At low temperatures molecules move more slowly and enzyme reactions tend to proceed more slowly. Warming helps only if other needs are met. Beyond an enzyme’s optimum, its active site may change shape through denaturation, reducing activity. Cooling does not reverse denaturation. Colder conditions slow enzymes without killing them, and warming raises the rate only up to the optimum. The optimum depends on the plant and the conditions, so it differs between species.''','6.5 Enzymes')
C('3.6.1.3-06','FEATURE','Describe the effect of increasing temperature on the rate of photosynthesis when light and carbon dioxide are adequate.','The rate rises as temperature increases up to an optimum; above the optimum it falls as enzymes denature.')
C('3.6.1.3-06','WHY','Explain why a large temperature increase beyond the optimum can reduce photosynthesis.','Enzymes can denature and their active sites change; fewer suitable enzyme–substrate complexes form, slowing the reactions.')
E('3.6.1.3-07','Building carbohydrates',[
'Photosynthesis produces glucose, a simple carbohydrate.',
'Glucose units can be joined to make larger carbohydrates such as starch and cellulose.'
],'''Joining many simple sugar units forms a larger molecule with different properties. Starch makes a compact insoluble reserve, while cellulose forms strong cell walls. Plants also convert some sugar into sucrose for transport. These are chemical changes made by cells, not the absorption of ready-made starch from soil. A growing leaf uses its products as well as storing some.''','3.2 Carbohydrates')
C('3.6.1.3-07','PROC','Describe how a plant makes large carbohydrates from a product of photosynthesis.','Photosynthesis makes glucose; cells join many glucose units to form starch or cellulose.')
E('3.6.1.3-08','Using and storing photosynthetic products',[
'Glucose can be respired, converted to cellulose or sucrose, or stored as starch.',
'Carbohydrate products can also provide material for fats and, with nitrogen, amino acids.'
],'''Respiration transfers energy for cell processes; it does not merely occur in darkness. Cellulose supports new walls, sucrose travels in phloem, and starch reserves can later be converted back to soluble sugars. Starch is insoluble, so storing it has a smaller direct osmotic effect than storing an equivalent amount as dissolved glucose. Seeds may store oils as well as starch. The product made and stored depends on the tissue and species.''','8.1 Overview of Photosynthesis')
C('3.6.1.3-08','FEATURE','Describe two uses of glucose formed by photosynthesis.','It can be respired to release energy; it can be converted to cellulose for cell walls.')
C('3.6.1.3-08','WHY','Explain why starch is suitable for storing carbohydrate in a plant cell.','It is insoluble and has little direct osmotic effect; it can later be broken down to usable sugars.')
E('3.6.1.3-09','Limiting factors',[
'A limiting factor is something present in the environment in short supply that restricts life processes.',
'A limiting factor can change when conditions change.'
],'''A plant with insufficient carbon dioxide cannot increase its photosynthesis merely because more light is provided. To test a suspected limit, increase that factor while keeping others constant. If rate rises, the intervention supports that factor having limited the earlier rate. A plateau alone does not uniquely identify what is limiting: several possible factors require further evidence.''')
# The definition is the approved syllabus wording rather than an uncited external scientific claim.
for cl in A.claims[-2:]:
 cl['evidence']=[{'source_id':'SRC-SYL-6116','locator':'printed p.14, 3.6.1.3 Photosynthesis','support_type':'direct'}];cl['notes']=[]
C('3.6.1.3-09','DEF','Define limiting factor.','Something present in the environment in short supply that restricts life processes.')
E('3.6.1.3-10','Identifying the active limit',[
'A factor is supported as limiting when increasing it raises rate under otherwise matched conditions.',
'A lack of response to extra light alone does not distinguish carbon dioxide shortage from unsuitable temperature.'
],'''For example, at a fixed temperature a plant releases 4 cm³ oxygen per minute at both moderate and high illumination. Adding carbon dioxide at the higher illumination raises output to 7 cm³ per minute. The intervention supports carbon dioxide limiting the original plateau. Temperature was not ruled out merely by seeing a flat curve; it was the positive carbon dioxide response that supplied the extra evidence. On a graph, a curve that is flat at high light intensity and rises when carbon dioxide is added shows that carbon dioxide was limiting at the plateau.''','8.3 Using Light Energy to Make Organic Molecules')
C('3.6.1.3-10','APP','Fig. VIS-6116-3.6.1.3-10 is a graph of photosynthesis rate against light intensity at a fixed temperature. One curve rises and then levels off at high light intensity. A second curve, obtained at the same temperature but a higher carbon dioxide concentration, rises above the plateau of the first curve at high light intensity. Explain which factor limited the rate at the plateau of the first curve.','The first curve is flat at high light intensity, so more light gave no rise in rate and light was not the limit there. Raising carbon dioxide alone allowed a higher rate at the same light intensity, so carbon dioxide concentration was the limiting factor at the plateau.',hold=True)
E('3.6.1.3-11','Investigating photosynthesis rate',[
'Oxygen volume released by a submerged plant over a measured time can estimate its net photosynthetic output.',
'Light, carbon dioxide and temperature should be varied separately, with the other conditions controlled.'
],'''Place a healthy aquatic shoot in a suitable transparent vessel and collect its oxygen into a graduated system. Allow it to adjust after changing a condition, then measure gas volume over a fixed period. For light, change lamp distance or use measured illumination while a water bath prevents heating. For carbon dioxide, use defined hydrogencarbonate concentrations at constant temperature and illumination. For temperature, use water baths, keeping light and solution conditions fixed. Repeat each level and compare mean volume per minute. Bubble counts are less reliable because bubbles vary in size. Gas may dissolve before collection, and leaking joints lose gas; these limit the estimate. Respiration also consumes oxygen, so the collected amount represents net output.''')
C('3.6.1.3-11','SYNTH','Describe a complete investigation of the effect of light intensity on photosynthesis in a submerged plant.','Change measured light intensity at a fixed aquatic shoot; measure oxygen volume collected in a set time; control temperature, shoot size and carbon dioxide supply; allow adjustment then collect gas with a sealed graduated apparatus at several light levels; repeat each level and compare mean output per minute.')
C('3.6.1.3-11','LIM','Suggest a limitation of estimating photosynthesis by counting bubbles and a linked improvement.','Bubbles have unequal volumes; collect and measure oxygen volume over the same interval instead.')
C('3.6.1.3-11','APP','Suggest a conclusion from an aquatic-shoot experiment. At 20 cm from a lamp, mean oxygen output is 0.8 cm³/min; at 10 cm it is 1.4 cm³/min. Temperature and carbon dioxide were controlled and five repeats were used.','Closer illumination increased net oxygen output under these conditions; the rise from 0.8 to 1.4 cm³/min supports light having limited the earlier rate.')
E('3.6.1.3-12','Greenhouse productivity',[
'Carbon dioxide enrichment, suitable illumination and suitable temperature can increase photosynthesis when they remove a limiting factor.',
'Productivity depends on growth over time, not on maintaining the maximum level of each input.'
],'''Enrichment supplies a reactant; lamps provide energy; heating helps enzyme reactions in cold weather, while ventilation can avoid excessive heat. Increasing one input may shift the limitation to another, so there is no guarantee that doubling an input doubles growth. A greenhouse can waste energy by heating beyond a useful temperature or adding carbon dioxide when light is inadequate. Adequate water and minerals are still needed to turn the products of photosynthesis into new tissue.''','8.3 Using Light Energy to Make Organic Molecules')
C('3.6.1.3-12','FEATURE','Describe two ways a greenhouse can improve conditions for photosynthesis.','Enrich carbon dioxide to supply a reactant; maintain a suitable temperature for enzyme-controlled reactions.')
C('3.6.1.3-12','WHY','Explain why greenhouse growers consider light, carbon dioxide and temperature together rather than maximising just one.','Removing one limit can leave another factor limiting; excessive temperature can also damage enzymes rather than improve productivity.')
E('3.6.1.3-13','Gas exchange in light and darkness',[
'Hydrogencarbonate indicator changes colour with carbon dioxide concentration: yellow at high levels, red/orange near atmospheric levels and purple at low levels.',
'An illuminated aquatic plant can remove carbon dioxide faster than respiration releases it, whereas in darkness respiration releases carbon dioxide without photosynthetic uptake.'
],'''Use equal masses of similar aquatic plant in equal volumes of indicator in sealed tubes. Illuminate one, wrap another fully in opaque material, and include a no-plant tube under each condition. Keep temperature, starting indicator colour and duration matched; use cool lighting to avoid warming one treatment. Repeat tubes. A purple light tube supports net uptake and a yellow dark tube supports net release, compared with stable no-plant controls. Light does not stop respiration: the colour indicates the balance of two processes. An unchanged colour can mean little net change rather than no reactions. Air leakage, handling with exhaled breath near the indicator or unsuitable plant material can alter the outcome.''')
C('3.6.1.3-13','SYNTH','Describe a complete investigation of aquatic-plant gas exchange in light and darkness with hydrogencarbonate indicator.','Change illumination using clear and opaque-wrapped sealed tubes; measure indicator colour after a fixed time; keep plant mass, indicator volume, starting colour and temperature alike; set up plant and no-plant tubes in both conditions and compare final colours; repeat each treatment.')
C('3.6.1.3-13','LIM','Suggest a limitation and an improvement when a light/dark indicator investigation puts the illuminated tubes beside a hot lamp.','Lamp heating changes temperature as well as light; use cool illumination or a controlled water bath to match temperatures.')
C('3.6.1.3-13','APP','Suggest what these indicator results show. Equal plant masses in sealed tubes turn the indicator purple in light and yellow in darkness; no-plant controls remain orange. Purple indicates low carbon dioxide and yellow high carbon dioxide.','In light the plant has net carbon dioxide uptake; in darkness it has net release through respiration.')

# Human nutrition. Sources support the science; curriculum-specific dietary examples remain subject to teacher verification.
E('3.6.2.1-01','Vitamin A deficiency',[
'Insufficient vitamin A can impair vision in dim light and damage healthy epithelial surfaces.',
'Animal foods such as eggs and liver supply vitamin A; orange vegetables and dark green leaves supply precursors the body can convert.'
],'''A deficiency is an inadequate supply for the body’s needs, not necessarily complete absence. A restricted diet without suitable vitamin A sources can lead to night blindness. Variety matters: a filling meal may still lack a micronutrient. Night blindness has other possible causes, so a doctor confirms a deficiency with tests. Eating a variety of foods prevents shortage; very large doses of vitamin A supplements can be harmful.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-01','FEATURE','Describe a dietary cause and an effect of vitamin A deficiency.','Too little vitamin-A-rich food can cause deficiency; an effect is impaired vision in dim light.')
C('3.6.2.1-01','WHY','Explain why a long-term diet lacking vitamin A may make seeing at dusk difficult.','Vitamin A is needed for normal light-sensitive processes in the retina; a shortage impairs vision in dim light.')
E('3.6.2.1-02','Vitamin D deficiency',[
'Vitamin D supports calcium absorption and healthy bone mineralisation.',
'Insufficient vitamin D can cause rickets in children, with soft or deformed bones.'
],'''Vitamin D can come from foods such as oily fish and fortified foods and can be formed in skin exposed to sunlight. A shortage may arise from insufficient dietary supply together with limited skin production. Calcium is needed as well: vitamin D does not replace the mineral. In growing children, poor mineralisation may cause bowed legs under body weight. Calcium is found in milk, small fish eaten with their bones, and green leafy vegetables, so a child needs a diet that supplies both calcium and vitamin D.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-02','FEATURE','Describe a cause and a skeletal effect of vitamin D deficiency in a child.','Insufficient dietary vitamin D with limited skin production can cause shortage; bones may become soft and bowed in rickets.')
C('3.6.2.1-02','WHY','Explain why vitamin D deficiency may cause bowed legs during growth.','Reduced calcium absorption impairs bone mineralisation; the softened bones can bend under body weight.')
E('3.6.2.1-03','Vitamin C deficiency',[
'Vitamin C supports formation and maintenance of connective tissues.',
'Long-term deficiency can cause scurvy, including bleeding gums and poor wound healing.'
],'''Fresh fruits and vegetables provide vitamin C. A very restricted diet with little of these foods can supply insufficient vitamin C even if energy intake is adequate. Heating and long storage can reduce the vitamin content of some foods. A mixed diet with suitable fruit or vegetables supports tissue maintenance; vitamin C is not itself an energy source.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-03','FEATURE','Describe the dietary cause of vitamin C deficiency and one effect.','Long-term lack of vitamin-C-rich fruit and vegetables; scurvy with bleeding gums or poor wound healing.')
C('3.6.2.1-03','WHY','Explain why wounds may heal poorly in severe vitamin C deficiency.','Vitamin C is needed for normal connective-tissue formation; insufficient supply weakens tissue repair.')
E('3.6.2.1-04','Iodine deficiency',[
'Iodine is required for thyroid hormone production.',
'Iodine deficiency can cause enlargement of the thyroid gland, called goitre.'
],'''Iodised salt can supply iodine, but this does not justify consuming large quantities of salt. Seafood is another possible dietary source. Goitre is an enlargement in the neck associated with the thyroid, not an enlargement of red blood cells. Keep iodine and iron separate: iodine is linked to thyroid function; iron is linked to haemoglobin.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-04','FEATURE','Describe a cause and an effect of iodine deficiency.','Insufficient dietary iodine can reduce thyroid hormone production; the thyroid gland may enlarge into a goitre.')
C('3.6.2.1-04','WHY','Explain why iodine is needed in a balanced diet.','It is used to make thyroid hormones; these help regulate the body’s metabolic activity.')
C('3.6.2.1-04','MISCON','Explain the error in saying that iodine shortage causes anaemia by preventing haemoglobin production. Give the correct mineral–condition pairings.','Iron shortage can impair haemoglobin production and cause anaemia; iodine shortage is associated with thyroid enlargement or goitre.')
E('3.6.2.1-05','Iron deficiency in people',[
'Iron is needed to make haemoglobin, which carries oxygen in red blood cells.',
'Iron deficiency can cause anaemia, with tiredness and reduced capacity for activity.'
],'''Meat, pulses and some green vegetables can contribute dietary iron. Insufficient intake or increased losses may lead to shortage. Less haemoglobin reduces oxygen-carrying capacity, so aerobic respiration during activity can become more difficult to support. Tiredness alone does not identify iron deficiency because it has many possible causes. Iron in food is not the same as the whole red blood cell; cells also require other materials.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-05','FEATURE','Describe an iron-deficiency cause and its effect on the blood.','Insufficient available dietary iron can cause shortage; haemoglobin production falls, causing iron-deficiency anaemia.')
C('3.6.2.1-05','WHY','Explain why a person with iron-deficiency anaemia may tire easily during activity.','Less haemoglobin reduces oxygen delivery; this restricts support for aerobic respiration in active tissues.')
E('3.6.2.1-06','A balanced diet for children',[
'A balanced diet provides adequate energy and appropriate amounts of carbohydrate, protein, fats, vitamins, minerals, fibre and water.',
'Children need protein for growth and calcium with vitamin D for developing bones and teeth.'
],'''Balanced means suited to needs, not equal masses of each nutrient. A meal of pearl-millet porridge, beans, vegetables and a suitable calcium source can combine energy, protein and micronutrients; no one dish guarantees the complete daily balance. A growing child may need less total energy than a large active adult but more growth materials relative to body size. Fibre supports bowel function and water supports transport and reactions. Variety across meals helps avoid shortages.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-06','FEATURE','Describe two dietary requirements especially relevant to a growing child.','Adequate protein for new tissue; calcium with vitamin D for developing bones and teeth.')
C('3.6.2.1-06','WHY','Explain why enough energy alone does not make a child’s diet balanced.','Growth also requires materials such as amino acids from protein; vitamins and minerals are needed for processes that energy-rich foods alone may not support.')
E('3.6.2.1-07','Adults and workers',[
'Adults require nutrients for maintenance and repair as well as energy for metabolism and activity.',
'Physically demanding work generally increases energy needs compared with sedentary work in otherwise similar adults.'
],'''A road worker carrying materials may respire more fuel during the working day than a worker seated at a desk. The comparison depends on body size, duration and actual effort; a job title alone does not determine an exact energy requirement. Adults still need protein, micronutrients, fibre and water even after height growth has ended. Persistent excess energy intake can lead to increased fat stores, while insufficient intake forces use of reserves.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-07','FEATURE','Describe two roles of a balanced diet in an adult worker.','It supplies energy for activity and metabolism; it supplies materials for tissue maintenance and repair.')
C('3.6.2.1-07','WHY','Explain why two adults of similar size may need different energy intakes when one does heavy manual work and the other is sedentary.','The manual worker’s muscles do more work; increased respiration uses more fuel, raising the energy requirement.')
E('3.6.2.1-08','Nutrition during nursing',[
'Producing breast milk requires energy and materials such as protein, calcium and water.',
'A nursing mother needs an adequate varied diet to support her own tissues as well as milk production.'
],'''Milk transfers nutrients to an infant, so ongoing supply matters as well as the mother’s existing reserves. Foods providing protein and calcium, sufficient energy and adequate drinking water can support these demands. Eating a varied diet with enough energy helps more than eating much more of one food. Requirements vary with the amount of milk produced and other individual factors. Family access to sufficient food can therefore affect two people at once.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-08','FEATURE','Describe two nutritional needs associated with producing breast milk.','Energy for milk synthesis; protein and calcium as materials supplied in milk.')
C('3.6.2.1-08','WHY','Explain why a nursing mother needs adequate food and water even if her own body size is not increasing.','Nutrients and water leave her body in milk; replacement and energy for milk production are needed as well as her maintenance needs.')
E('3.6.2.1-09','Athletes and training',[
'Sustained physical training increases energy use through muscle respiration.',
'Athletes also require water, mineral replacement and protein for tissue repair as part of a balanced diet.'
],'''Carbohydrate is a useful fuel source during demanding activity; some is stored as glycogen before use. Protein supports repair and adaptation but is not a substitute for sufficient overall energy. Sweating increases water loss; replacement requirements depend on weather, duration and intensity. An athlete’s diet still includes fruit, vegetables and other micronutrient sources. More protein by itself does not guarantee better performance.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-09','FEATURE','Describe two features of a balanced diet supporting an athlete’s training.','Adequate carbohydrate for energy; adequate protein for tissue repair.')
C('3.6.2.1-09','WHY','Explain why an endurance athlete needs adequate carbohydrate and water during a demanding training programme.','Carbohydrate supplies respiratory fuel for repeated muscle work; water replaces losses and supports circulation and temperature control.')
E('3.6.2.1-10','Nutrition for people living with HIV',[
'Adequate nutrition supports tissue maintenance and immune function in people living with HIV.',
'Illness, reduced appetite or diarrhoea can make adequate nutrient intake and absorption more difficult.'
],'''A varied diet with enough energy and protein, and safe food and water, supports health. Needs vary with the person’s health and treatment. Good nutrition supports general health and recovery; it does not remove HIV, and antiretroviral treatment is still needed.

Difficulty getting enough food can come from illness, household resources or access to food. Careful food hygiene matters because infections are more dangerous when immunity is reduced. People living with HIV can safely share meals and normal social contact.''','34.2 Nutrition and Energy Production')
# Specific HIV clinical advice is not established by the general nutrition chapter.
for cl in A.claims[-2:]:
 cl['evidence']=[];cl['notes']=['General nutrition principles applied to syllabus group; specific HIV nutrition support needs qualified teacher/source verification. No clinical treatment advice authored.']
C('3.6.2.1-10','FEATURE','Describe two ways an adequate balanced diet supports a person living with HIV.','It provides energy for daily metabolism; it provides protein and micronutrients for tissue maintenance and immune function.')
C('3.6.2.1-10','WHY','Explain why nutrition may need particular attention during illness in a person living with HIV.','Reduced appetite or diarrhoea may reduce nutrient intake or absorption; illness can increase demands for maintenance and repair.')
E('3.6.2.1-11','Age and dietary needs',[
'Growth raises requirements for building materials relative to body size.',
'Energy requirements depend on body size and activity as well as age.'
],'''A rapidly growing adolescent may require substantial energy and protein, while an older sedentary adult may need less energy but still needs adequate micronutrients. A shorter person does not necessarily need less of every nutrient, and older people still need protein to maintain their muscles.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-11','CHAIN','Explain why rapid growth changes dietary requirements.','New tissue must be made; extra building materials such as amino acids and adequate energy are needed.')
C('3.6.2.1-11','APP','Explain why a growing teenager may need more protein relative to body mass than a non-growing adult of similar activity, even though the adult is heavier.','The teenager needs amino acids for new tissue as well as repair; the adult mainly maintains existing tissue, so body mass alone does not settle the relative requirement.')
E('3.6.2.1-12','Sex-related needs and individual variation',[
'Average differences in body size and muscle mass can contribute to different average energy requirements between sexes.',
'Menstrual blood loss can increase iron requirements, while pregnancy and lactation add other demands.'
],'''On average, males and females differ in body size and muscle mass, and the biological reasons concern body composition and reproduction. An average does not decide one person’s exact need. Two people with the same activity and body size can have similar energy demands, while menstrual blood loss may still change iron needs. When comparing the needs of two people, say which need differs: energy, protein or a particular mineral such as iron.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-12','CHAIN','Explain how menstrual blood loss can affect dietary iron needs.','Blood loss removes iron in haemoglobin; additional dietary iron is needed to replace it.')
C('3.6.2.1-12','APP','Explain why equal energy needs do not imply equal iron needs for two adults of the same mass and activity when one has regular menstrual blood loss and the other does not.','Energy and iron are separate needs, so similar energy needs say nothing about iron; the person losing blood must replace the iron lost in haemoglobin and so needs more iron.')
E('3.6.2.1-13','Activity and energy demand',[
'Working muscles increase respiration to supply energy for contraction.',
'Greater duration or intensity of activity usually increases energy requirements.'
],'''Compare actual activity rather than labels such as “busy”. Walking a long distance, carrying loads or repeated vigorous exercise consumes energy, whereas concentrated mental work does not necessarily require a similar increase. If energy expenditure falls but intake stays high for a long time, surplus energy can be stored as fat. A single meal or day does not establish a long-term imbalance.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-13','CHAIN','Explain why greater physical activity can increase dietary energy needs.','Muscle contraction requires energy; increased respiration uses more nutrient fuel.')
C('3.6.2.1-13','APP','Explain why a worker who changes from carrying sacks all day to seated duties may gain fat if food intake remains unchanged for months. Assume other conditions remain similar.','The new duties reduce energy expenditure; continued intake above expenditure supplies surplus energy stored as fat.')
E('3.6.2.1-14','Pregnancy and dietary needs',[
'Pregnancy requires materials and energy for fetal development and maternal tissue changes.',
'Protein, iron and calcium are among the nutrients needed in adequate amounts during pregnancy.'
],'''A developing fetus produces new cells, while the pregnant person also develops tissues and a larger blood supply. Protein supports new tissue, calcium supports developing bones and iron supports haemoglobin. The extra energy needed is much less than double, and specific requirements vary during pregnancy and with the person’s existing diet.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-14','CHAIN','Explain why pregnancy increases the need for adequate protein and iron.','Protein supplies amino acids for new fetal and maternal tissue; iron supports haemoglobin for the increased blood supply.')
C('3.6.2.1-14','APP','Explain why simply adding more cooking oil would not correct both extra energy needs and low iron intake during pregnancy.','Oil supplies energy but little iron; the extra haemoglobin requirement still needs an appropriate iron source.')
E('3.6.2.1-15','Breastfeeding changes nutrient balance',[
'Lactation transfers water and nutrients from mother to infant through milk.',
'Milk production can increase energy and material requirements beyond maintenance.'
],'''Milk contains fat, sugar, protein, mineral ions and water. The mother’s body must obtain these materials or draw on reserves, and synthesis also costs energy. Extra energy alone does not replace calcium or protein. The needs of a person producing milk differ from those of the same person after lactation ends, although activity and body size also influence the comparison.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-15','CHAIN','Explain why breastfeeding increases dietary requirements even without further maternal growth.','Milk exports nutrients to the infant; its production also requires energy, so these needs are added to maintenance.')
C('3.6.2.1-15','APP','Explain why extra sweetened drinks alone would not make a low-protein diet adequate for a breastfeeding mother, even if the drinks supplied the extra energy.','Sugar can supply energy but not amino acids; protein is still needed to make milk proteins and maintain maternal tissues.')
E('3.6.2.1-16','Starvation',[
'Starvation occurs when food supplies insufficient energy and nutrients for a prolonged period.',
'The body uses stored materials and eventually body tissues, causing loss of mass, weakness and impaired function.'
],'''Malnutrition includes too little, too much or an unsuitable balance of nutrients. Starvation is a severe shortage, not a label for missing one meal. Fat reserves can provide fuel, but continued shortage also leads to protein breakdown and tissue loss. Children may stop growing normally, and resistance to infection can fall. Drought can reduce food production, while poverty or disrupted distribution may prevent access even where food exists elsewhere.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-16','FEATURE','Describe a cause and an effect of starvation.','Prolonged insufficient food supply; loss of body mass and weakness as reserves and tissues are used.')
C('3.6.2.1-16','WHY','Explain why prolonged starvation causes loss of body mass.','Food supplies too little energy; the body breaks down stored fat and later other tissues to provide fuel.')
E('3.6.2.1-17','Constipation',[
'Insufficient fibre or water intake can contribute to constipation.',
'Hard stools that are difficult or infrequent to pass are characteristic of constipation.'
],'''Fibre is not digested by human digestive enzymes but helps retain water and adds bulk to bowel contents. Water intake supports softer stools. The colon absorbs water, so contents that remain there longer may become harder. Whole grains, pulses, fruit and vegetables contribute fibre. Some cases of constipation have other causes, such as illness or medicines.''','34.3 Digestive System Processes')
C('3.6.2.1-17','FEATURE','Describe a dietary cause and an effect of constipation.','Too little fibre or water can contribute; stools become hard and difficult to pass.')
C('3.6.2.1-17','WHY','Explain how adequate fibre helps prevent constipation.','Fibre adds bulk and retains water in bowel contents; softer bulky stools are easier to move and pass.')
E('3.6.2.1-18','Diet and coronary heart disease',[
'A diet high in saturated fat can increase the risk of fatty deposits narrowing coronary arteries.',
'Narrowed coronary arteries can restrict oxygen supply to heart muscle and contribute to coronary heart disease.'
],'''Risk is not certainty. Smoking, inherited susceptibility, activity and other factors also affect coronary disease. If heart muscle receives insufficient oxygen, its aerobic respiration is restricted; severe blockage may kill part of the muscle. Excess salt can contribute to raised blood pressure, adding cardiovascular strain. Distinguish the artery supplying the heart muscle from the cavities through which the heart pumps blood.''','40.4 Blood Flow and Blood Pressure Regulation')
C('3.6.2.1-18','FEATURE','Describe a dietary risk factor and a consequence of coronary heart disease.','High saturated-fat intake can increase risk of narrowed coronary arteries; reduced blood flow limits oxygen supply to heart muscle.')
C('3.6.2.1-18','WHY','Explain why narrowing a coronary artery can harm heart muscle.','Less oxygenated blood reaches the muscle; aerobic respiration is restricted and severe shortage can damage cells.')
E('3.6.2.1-19','Obesity and energy balance',[
'Long-term energy intake exceeding energy expenditure can increase fat stores and lead to obesity.',
'Obesity is associated with increased risks of conditions including cardiovascular disease and type 2 diabetes.'
],'''Both intake and expenditure matter. High-energy foods can make surplus intake easier, but body mass is influenced by several factors, and judging a person’s habits from appearance is unreliable. Health investigations need sensitive, voluntary participation and protection of personal information. A change in a few days can reflect water as well as fat, so a sustained pattern is more informative about energy imbalance.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-19','FEATURE','Describe the energy imbalance that can lead to obesity and one associated health risk.','Energy intake persistently exceeds expenditure; cardiovascular disease risk can increase.')
C('3.6.2.1-19','WHY','Explain why frequent high-energy meals may cause increased fat storage if activity and other expenditure do not increase.','The meals can create an energy surplus; energy-rich materials not immediately used can be converted to or stored as fat.')
E('3.6.2.1-20','Scurvy as malnutrition',[
'Scurvy results from a sustained shortage of vitamin C.',
'Bleeding gums and poor wound healing reflect impaired connective-tissue maintenance.'
],'''A person can consume adequate energy yet develop scurvy if the diet lacks vitamin C. This distinguishes a specific micronutrient deficiency from starvation. Treating a deficiency needs the missing nutrient itself, not just a larger serving of the same foods. Scurvy is treated by supplying vitamin C, for example through fresh fruit and vegetables.''','34.2 Nutrition and Energy Production')
C('3.6.2.1-20','FEATURE','Describe the cause of scurvy and one characteristic effect.','Prolonged vitamin C deficiency; bleeding gums or poor wound healing.')
C('3.6.2.1-20','WHY','Explain why a person receiving enough food energy may still develop scurvy.','Energy sufficiency does not guarantee vitamin C sufficiency; a restricted diet can lack the vitamin needed for connective-tissue maintenance.')
E('3.6.2.1-21','Investigating dietary health locally',[
'A dietary survey can investigate associations between food intake and health indicators but does not by itself establish causation.',
'Health data collection requires voluntary consent, confidentiality and consistent non-judgemental questions.'
],'''For a school investigation in Namibia, use anonymous volunteer records or an anonymised dataset prepared by the teacher. The aim is to look for patterns in groups, not to diagnose individuals. Define a focused question, for example whether frequency of sugary drinks is associated with a recorded dental-decay indicator. Record portions consistently over the same interval. Investigate fat, meat and salt through separate defined measures: frequent fatty meat may raise saturated-fat intake, while processed salty foods can raise salt intake. Meat also provides useful protein and iron, so “meat is harmful” is not a sound conclusion. Sugar frequency is relevant to tooth decay and surplus energy; high salt intake can contribute to high blood pressure. Match or record age, activity and other confounders where feasible. Self-report can be inaccurate, samples may be unrepresentative, and an association cannot distinguish all alternative explanations.''')
C('3.6.2.1-21','SYNTH','Describe an ethical investigation of an association between sugary-drink intake and a health indicator in a Namibian community, without asking people to increase intake.','Group consenting anonymous volunteer records by reported sugary-drink frequency; measure a consistently recorded dental-decay indicator; record comparable age and relevant habits; use the same questionnaire and approved anonymous health records without diagnosing participants; include many volunteers and compare group summaries.')
C('3.6.2.1-21','LIM','Suggest one limitation and an improvement for a survey relying on one person’s memory of everything eaten in the last month.','Recall and one-person sampling can misrepresent usual intake; collect prospective short food diaries from many consenting volunteers.')
C('3.6.2.1-21','APP','Suggest the justified conclusion from an anonymous survey: 12 of 30 frequent sugary-drink consumers and 4 of 30 infrequent consumers have recorded tooth decay. Other dietary habits were not controlled.','Tooth decay is more frequent in the high-intake group; this association does not prove sugary drinks alone caused it because other habits may differ.')
E('3.6.2.1-22','Why famine occurs',[
'Drought and flooding can reduce harvests or damage food stores and transport routes.',
'Unequal access and distribution can prevent people obtaining food even when supplies exist elsewhere.',
'Population growth can increase demand faster than food production and distribution expand.'
],'''Famine is a severe widespread shortage of accessible food. It is not explained by a single event in every place. Drought reduces water available for crops and livestock, while flooding may destroy crops and roads at the same time. Damaged roads can prevent remaining supplies reaching households. Low income or disrupted trade can also limit access to food. Increasing demand adds pressure when land, water, harvests or infrastructure cannot keep pace. A district with a reasonable total grain supply may still have hungry households if supplies and purchasing power are uneven. Both production and access matter, because a national total does not guarantee food for every family.''')
C('3.6.2.1-22','CHAIN','Discuss how drought, flooding and unequal food distribution can each contribute to famine.','Drought reduces crop and livestock production; floods can destroy crops and transport routes; unequal distribution leaves some households without access despite supplies elsewhere.')
C('3.6.2.1-22','APP','Suggest why famine risk may rise in an isolated district after flooding even when the country’s total grain supply is adequate. The district’s main road and stored harvest have been destroyed.','The flood removed local food reserves; damaged transport prevents national supplies reaching the district, so total availability does not guarantee local access.')

# Syllabus definitions are quoted exactly in their approved senses.
for o,h,d,extra in [
('01','Ingestion','The taking in of substances into the body through the mouth.','Food is ingested before digestion. The term describes entry, not the breakdown of a molecule. Drinking water is also ingestion, even though water does not need enzyme digestion.'),
('02','Mechanical digestion','The breakdown of food into smaller pieces without chemical change to the food molecules.','Chewing breaks a piece of food into smaller pieces. Its starch molecules remain starch molecules at this stage. The increased exposed surface lets enzymes act more readily; mechanical processing and enzyme action therefore complement one another.'),
('03','Chemical digestion','The breakdown of large, insoluble molecules into smaller, soluble molecules.','Enzymes catalyse the chemical change. Small soluble products can cross the intestinal lining more readily than the large food molecules. Dissolving a substance or grinding it finely is not itself the same as breaking its molecules into smaller ones.'),
('04','Absorption','The movement of small food molecules and ions through the wall of the intestine into the blood.','Absorption follows digestion for nutrients that began as large insoluble molecules. It is a movement into the body’s transport system, not the conversion of starch to sugar. Water, ions and some nutrients already small enough can be absorbed without prior digestion.'),
('05','Egestion','The passing out of food that has not been digested or absorbed through the anus.','The rectum stores faeces before egestion. Egestion differs from excretion: undigested food has not become a waste product of cell metabolism. Urine and carbon dioxide are examples of excretory outputs, whereas undigested fibre leaves in faeces.')]:
 oid='3.6.2.2-'+o
 A.entry(oid,h,[d,extra.split('. ')[0]+'.'],extra.split('. ',1)[1] if '. ' in extra else '',source=('SRC-SYL-6116','printed p.15, 3.6.2.2 Alimentary canal','direct'))
 C(oid,'DEF','Define '+h.lower()+'.',d)
E('3.6.2.2-06','The alimentary canal as a sequence',[
'The mouth ingests and mechanically processes food, while the stomach and small intestine carry out further digestion.',
'The small intestine absorbs digested nutrients; the colon absorbs water and the rectum stores faeces before egestion.'
],'''Trace a meal through the alimentary canal, a continuous tube from mouth to anus. Waves of muscle contraction called peristalsis push food along it.

| Part | Main functions here |
|---|---|
| Mouth and salivary glands | Teeth break food; saliva moistens it and supplies amylase |
| Oesophagus | Muscular contractions move the swallowed bolus towards the stomach |
| Stomach | Mixes food with acid and protease-containing gastric juice |
| Duodenum | Receives bile and pancreatic digestive juice; chemical digestion continues |
| Ileum and remaining small intestine | Completes digestion and absorbs products through villi |
| Colon | Absorbs water from remaining contents |
| Rectum and anus | Store faeces and control their release |

The liver makes bile, the gall bladder stores and releases it, and the pancreas supplies digestive enzymes. Food passes along the gut and does not pass through the liver or pancreas.''','34.1 Digestive Systems')
C('3.6.2.2-06','FEATURE','Describe the functions of the oesophagus and rectum during passage of a meal.','The oesophagus moves swallowed food towards the stomach by muscular contractions; the rectum stores faeces before egestion.')
C('3.6.2.2-06','WHY','Explain why food does not need to enter the pancreas or liver to receive their digestive secretions.','Their secretions travel through ducts into the small intestine; food mixes with them there while staying within the alimentary canal.')
E('3.6.2.2-07','Cholera',[
'Cholera is an infectious disease caused by a bacterium.',
'Contaminated water or food can carry the bacterium into the alimentary canal.'
],'''The bacterium affects the intestine; the resulting severe watery diarrhoea can rapidly remove water and salts. Clean drinking water, sanitation and hygienic food preparation reduce transmission. A pathogen causes the disease, while poor sanitation increases the chance of exposure. Cholera is an infection and not an inherited condition. Treatment replaces the lost water and salts, using a drinking solution of water, salts and sugar.''')
C('3.6.2.2-07','FEATURE','Describe the type of pathogen causing cholera and one route of transmission.','A bacterium causes cholera; it can be swallowed in contaminated water or food.')
E('3.6.2.2-08','How cholera causes fluid loss',[
'Cholera bacteria produce a toxin that stimulates chloride-ion secretion into the small intestine.',
'The increased gut solute concentration draws water into the intestine by osmosis, causing diarrhoea and losses of water and salts.'
],'''Follow the direction: ions move into the gut lumen, then water follows from body fluids across the intestinal lining. Severe diarrhoea therefore dehydrates the person rather than washing excess body water away harmlessly. Fluid can continue entering the intestine even if the person has drunk little, because body fluids supply it. Treatment therefore has to replace both the water and the salts that were lost. Osmotic reasoning connects this to the movement of water across membranes taught in 3.3.2.''')
C('3.6.2.2-08','CHAIN','Explain the sequence from cholera toxin to dehydration.','The toxin causes chloride secretion into the gut, drawing water in by osmosis; watery diarrhoea then removes water and salts from the body.')
C('3.6.2.2-08','APP','Explain why a person with cholera may continue losing large volumes of watery stool after eating very little. The toxin causes chloride ions to enter the small intestine.','Water follows the secreted ions from body fluids into the intestine by osmosis; the fluid loss therefore need not come from food just eaten.')

E('3.6.2.3-01','Digestive enzymes and their conditions',[
'Digestive enzymes catalyse breakdown of large food molecules into smaller products.',
'Each enzyme works best within a suitable pH and temperature range; excessive heat can denature it.'
],'''An enzyme’s substrate must fit its active site. Unsuitable pH can alter the interactions needed for activity; excessive temperature changes the protein’s shape. Below an optimum, cooling generally slows reactions without the same permanent damage as denaturation. Different enzymes work in different parts of the canal: an acidic stomach suits its protease, while intestinal enzymes operate in less acidic conditions. Each enzyme has its own optimum pH.''','6.5 Enzymes')
C('3.6.2.3-01','FEATURE','State the role of digestive enzymes in the alimentary canal.','They speed up (catalyse) the breakdown of large food molecules into smaller ones.')
E('3.6.2.3-02','Why chemical digestion is needed',[
'Large insoluble food molecules cannot readily be absorbed through the intestinal wall.',
'Chemical digestion produces smaller soluble molecules suitable for absorption.'
],'''Ingesting protein does not mean whole protein molecules normally move straight into blood. Proteases break them into smaller products, ultimately amino acids, which can cross the lining and be used to build the body’s own proteins. A body therefore digests food and then constructs its own tissues, rather than directly inserting pieces of a meal into a muscle. Nutrients such as water and ions do not need this molecular breakdown.''','34.3 Digestive System Processes')
C('3.6.2.3-02','FEATURE','State the importance of chemical digestion before nutrient absorption.','It converts large insoluble food molecules into smaller soluble products that can be absorbed.')
E('3.6.2.3-03','The digestion of starch',[
'Salivary amylase begins converting starch to maltose in the mouth.',
'Pancreatic amylase continues starch digestion in the small intestine, and maltase converts maltose to glucose.'
],'''Chewing exposes more food surface to saliva. Swallowed starch may continue to meet salivary amylase briefly, but acid conditions in the stomach inhibit its action. In the small intestine, pancreatic juice supplies more amylase in suitable conditions. Maltase associated with the intestinal lining acts on maltose, producing glucose for absorption. Starch → maltose → glucose separates the two steps and enzymes. Stomach acid is not an enzyme: it only changes the pH.

In a simple test, starch solution mixed with saliva at body temperature stops giving a blue-black colour with iodine after a few minutes, while a control made with boiled saliva still does. Boiling denatures amylase, so the boiled-saliva tube shows that the starch disappeared in the first tube because of active enzyme, not because of anything else in saliva or the conditions.''','34.3 Digestive System Processes')
C('3.6.2.3-03','PROC','Describe the two main enzyme steps converting starch into an absorbable sugar.','Amylase breaks starch to maltose; maltase breaks maltose to glucose.')
C('3.6.2.3-03','MECH','Describe the complete sequence of starch digestion from the mouth to an absorbable product in the small intestine.','Salivary amylase starts starch-to-maltose digestion in the mouth; stomach acid inhibits salivary amylase; pancreatic amylase continues starch-to-maltose digestion in the small intestine; intestinal maltase converts maltose to glucose for absorption.')
E('3.6.2.3-04','Amylase',[
'Amylase acts on starch, producing maltose.',
'The smaller soluble sugar product differs chemically from its starch substrate.'
],'''Substrate names identify what an enzyme acts on; product names identify what leaves the reaction. A typical amylase does not digest protein because its active site is suited to a different substrate. In digestion, amylase is one stage rather than the complete pathway to glucose. The mouth and pancreas provide amylase, but the reaction depends on local conditions.''','34.3 Digestive System Processes')
C('3.6.2.3-04','FEATURE','Describe a typical amylase reaction, naming substrate and product.','Starch is the substrate; amylase breaks it down to maltose.')
C('3.6.2.3-04','WHY','Explain why amylase does not replace protease in protein digestion.','Its active site is specific to a different substrate; protein does not fit appropriately for the amylase reaction.')
E('3.6.2.3-05','Proteases',[
'Proteases break down proteins, with amino acids as the eventual products of complete protein digestion.',
'Different proteases can act in the stomach and small intestine under different suitable conditions.'
],'''Some protein digestion passes through shorter chains before free amino acids are produced. Give protein as the substrate and amino acids as the overall end-products. The stomach’s acid provides a suitable environment for its protease, whereas intestinal proteases have different conditions.''','34.3 Digestive System Processes')
C('3.6.2.3-05','FEATURE','Describe the overall role of proteases in digestion, naming substrate and eventual products.','They digest protein; complete digestion produces amino acids.')
C('3.6.2.3-05','WHY','Explain why proteases help make food protein usable for building body tissues.','They release small amino-acid products suitable for absorption; cells can then use those amino acids to make their own proteins.')
E('3.6.2.3-06','Lipase',[
'Lipase digests fats to fatty acids and glycerol.',
'Emulsification increases the fat surface accessible to lipase without itself chemically digesting the fat.'
],'''A large oil drop has less exposed surface than the same amount divided into many small drops. Since lipase acts where fat meets the watery contents, division into droplets can increase reaction rate under suitable conditions.''','34.3 Digestive System Processes')
C('3.6.2.3-06','FEATURE','Describe the digestion of fat by lipase, naming substrate and products.','Lipase acts on fat, producing fatty acids and glycerol.')
C('3.6.2.3-06','WHY','Explain why forming small fat droplets can help lipase digestion.','The droplets provide a larger total surface area; more fat surface is available for lipase to act on.')
E('3.6.2.3-07','Stomach acid and bacteria',[
'Hydrochloric acid in gastric juice helps kill many bacteria swallowed in food.',
'The stomach’s acid is a defence but does not make contaminated food harmless.'
],'''Acidic conditions damage many microorganisms. Some pathogens or their effects can survive this barrier, so food hygiene remains necessary. Acid is not an enzyme: it changes conditions and can affect bacteria without being a biological catalyst. Distinguish this protective role from the separate effect on the pH needed by stomach protease.''','34.1 Digestive Systems')
C('3.6.2.3-07','FEATURE','State one protective role of hydrochloric acid in gastric juice.','It kills many bacteria swallowed with food.')
E('3.6.2.3-08','Stomach acid and protease activity',[
'Hydrochloric acid creates an acidic environment in the stomach.',
'This acidic environment is suitable for the stomach’s protease activity.'
],'''An enzyme’s suitable pH is linked to the structure and interactions of its active site. Acid helps create the right conditions for stomach protease; other digestive enzymes work best at a higher pH. When acidic stomach contents enter the small intestine, their pH must be adjusted for intestinal enzyme activity. That is a different stage of digestion.''','34.1 Digestive Systems')
C('3.6.2.3-08','FEATURE','State how hydrochloric acid supports enzyme activity in the stomach.','It provides the acidic pH suitable for stomach protease.')
E('3.6.2.3-09','Bile and acidity',[
'Bile is produced by the liver, stored in the gall bladder and released into the small intestine.',
'Its alkaline components help neutralise acidic material arriving from the stomach.'
],'''Pancreatic secretions also contribute to neutralising the mixture. The resulting less acidic environment suits intestinal enzymes better. Bile is not hydrochloric acid and does not make the stomach more acidic. Keep the locations straight: stomach acid lowers pH before the material reaches the intestine; alkaline secretions then raise pH. Food stays in the gut while bile arrives through a duct.''','34.1 Digestive Systems')
C('3.6.2.3-09','FEATURE','Outline the origin, destination and pH role of bile.','The liver makes bile; it is released into the small intestine; it helps neutralise acidic stomach contents.')
C('3.6.2.3-09','WHY','Explain why neutralising acidic stomach contents helps digestion in the small intestine.','Intestinal enzymes need a less acidic environment; raising pH towards their suitable range supports their activity.')
C('3.6.2.3-09','MISCON','A student says that bile is an acid that adds to the acidity of the food in the stomach. Explain the error in this statement.','Bile is made in the liver and enters the small intestine, not the stomach; it is alkaline and helps neutralise the acid from the stomach, so it raises the pH instead of lowering it.')
E('3.6.2.3-10','Bile and fat droplets',[
'Bile salts emulsify fat, dividing it into small droplets.',
'Emulsification increases total surface area for lipase and is not chemical digestion of fat molecules.'
],'''The molecules remain fat molecules after emulsification. Lipase subsequently catalyses their chemical breakdown. Shaking oil with water may briefly disperse it, but droplets tend to join again; bile salts help maintain a finer dispersion. Thus bile helps enzyme action without being a digestive enzyme itself. Think “droplet size” for emulsification and “molecular products” for lipase.''','34.3 Digestive System Processes')
C('3.6.2.3-10','FEATURE','Outline how bile helps fat digestion without itself being an enzyme.','Bile emulsifies fat into small droplets; this increases surface area; lipase then has more surface on which to digest fat.')
C('3.6.2.3-10','WHY','Explain why emulsification is not the same as chemical digestion.','Droplets become smaller without fat molecules being chemically broken down; lipase is still needed to produce digestion products.')
E('3.6.2.3-11','Investigating bile salts',[
'A matched oil-and-water comparison with and without bile salts can demonstrate emulsification.',
'To isolate emulsification, keep oil amount, water volume, shaking and observation time the same.'
],'''Put equal oil and water volumes into identical transparent tubes. Add a measured bile-salt solution to one and an equal volume of water to the comparison; shake both for the same time and leave them together. Observe separation or the persistence of a cloudy dispersion at fixed times. Use replicated tubes. Without lipase, this tests physical dispersion rather than digestion; cloudiness is not evidence that fatty acids have formed. A separate lipase investigation could test rate, but pH needs careful control because bile’s alkalinity can itself change an indicator. Keep tubes stoppered for shaking, avoid contact with reagents and follow teacher instructions.''')
C('3.6.2.3-11','SYNTH','Describe a complete investigation of the emulsifying effect of bile salts on oil.','Change bile-salt presence using equal added solution volumes; measure separation after a fixed time; keep oil/water volumes, tube type and shaking the same; shake matched tubes with and without bile salts then observe separation at set times; repeat each treatment and compare results.')
C('3.6.2.3-11','LIM','Suggest a limitation and an improvement if one bile-salt tube is shaken for 60 s but the no-bile tube for 10 s.','Different shaking can itself change dispersion; shake both for the same measured duration and intensity.')
C('3.6.2.3-11','APP','Suggest what is supported when replicated tubes containing oil, water and bile salts remain dispersed after 5 min, while matched oil-and-water controls separate. No lipase was added.','Bile salts help maintain small dispersed oil droplets; the result supports emulsification, not chemical digestion because lipase and product tests are absent.')

E('3.6.2.4-01','Where digested nutrients enter the body',[
'The small intestine is the main region for absorption of digested food.',
'Absorption moves products across the intestinal lining into transport fluids.'
],'''The folded lining bears villi, increasing the area through which materials can pass. Most sugars and amino acids enter blood capillaries; absorbed lipid products take a different route through lacteals after processing within the lining cells. The stomach mainly stores, mixes and begins digestion of a meal rather than carrying out most nutrient absorption. The colon absorbs water, not the bulk of digested food.''','34.3 Digestive System Processes')
C('3.6.2.4-01','FEATURE','Identify the main region for absorption of digested food and the structure on its lining that increases surface area.','Small intestine; villi.')
E('3.6.2.4-02','Why villi increase absorption',[
'Villi are numerous projections of the small-intestinal lining that increase its internal surface area.',
'A larger surface permits more nutrient transfer at the same time under suitable conditions.'
],'''A long tube gains still more area from folds and projections. Surface area is different from the volume of food inside it: a lining can have many more absorbing cells without a proportionate increase in tube volume. A villus has a thin epithelial covering and a transport supply beneath it, so the enlarged surface is connected to routes that carry absorbed nutrients away. Damaged villi can therefore impair absorption even when digestion has produced normal small molecules.''','34.3 Digestive System Processes')
C('3.6.2.4-02','FEATURE','Describe how villi change the absorbing surface of the small intestine.','Numerous projections extend into the lumen; together they greatly increase the internal surface area.')
C('3.6.2.4-02','WHY','Explain why many villi make absorption more effective than a smooth lining of the same tube length.','They expose more epithelial surface to digested food; more nutrient molecules can cross at the same time.')
E('3.6.2.4-03','Structure of a villus',[
'A villus has a thin epithelial covering, blood capillaries and a central lymph vessel called a lacteal.',
'Blood capillaries take up sugars and amino acids, while lacteals receive absorbed lipid material.'
],'''The thin covering shortens the transfer distance. Flowing blood carries absorbed products away, helping maintain concentration differences. The lacteal leads into the lymphatic system, which later returns material to the blood circulation. A villus is not a single cell, and its blood capillaries are not the same tube as its lacteal. In a drawing of a villus, label the epithelium, the blood capillaries and the lacteal separately.''','34.3 Digestive System Processes')
C('3.6.2.4-03','FEATURE','Describe the transport structures inside a villus and their different roles.','Blood capillaries receive sugars and amino acids; the central lacteal receives absorbed lipid material.')
E('3.6.2.4-04','The hepatic portal route',[
'The hepatic portal vein carries nutrient-rich blood from the intestines to the liver.',
'The liver processes absorbed nutrients before much of this blood returns to the general circulation.'
],'''“Hepatic” refers to the liver. The portal vein links intestinal capillaries to the liver and does not carry absorbed food straight to the heart. The hepatic artery supplies oxygenated blood to the liver; blood leaving the liver enters hepatic veins and then the vena cava. These are different directions and functions. Most absorbed lipids enter the lymph in the lacteals first, not the intestinal blood capillaries.''','34.3 Digestive System Processes')
C('3.6.2.4-04','FEATURE','State the role of the hepatic portal vein after nutrient absorption.','It carries nutrient-rich blood from the intestines to the liver.')
C('3.6.2.4-04','MISCON','Explain the error in naming the hepatic artery as the vessel carrying recently absorbed glucose from the small intestine directly to the liver.','That route is the hepatic portal vein; the hepatic artery supplies the liver with oxygenated blood from the arterial circulation.')
E('3.6.2.4-05','Excess glucose in the liver',[
'The liver can convert excess absorbed glucose into glycogen for storage.',
'Glycogen can later be broken down to glucose when blood glucose supply needs support.'
],'''After a carbohydrate-rich meal, absorption raises glucose supply. Storing some as glycogen helps prevent an excessive rise and provides a reserve between meals. The reverse change makes glucose available when it is needed. Glycogen is an animal storage carbohydrate; it is not the plant reserve starch. The hormones insulin and glucagon control this storage and release.''','34.2 Nutrition and Energy Production')
C('3.6.2.4-05','FEATURE','Describe how the liver stores excess glucose and later makes it available.','It converts glucose into glycogen; glycogen can later be broken down to release glucose.')
C('3.6.2.4-05','WHY','Explain why storing excess glucose as glycogen is useful between meals.','Storage builds a reserve after absorption; later breakdown supplies glucose when little is entering from the intestine.')
E('3.6.2.4-06','Excess amino acids',[
'Excess amino acids are deaminated in the liver rather than stored as a separate amino-acid reserve.',
'The nitrogen-containing portion is converted into urea for excretion, while the remaining material can be used as fuel or converted for storage.'
],'''Deamination means the removal of the nitrogen-containing part of amino acids to form urea. Blood carries urea to the kidneys, which remove it in urine. The liver forms it; the kidneys excrete it. The process differs from protein digestion: digestion produces amino acids in the gut, whereas deamination processes surplus amino acids already absorbed into the body. A diet containing protein therefore does not simply fill a store of unchanged amino acids.''','34.2 Nutrition and Energy Production')
C('3.6.2.4-06','FEATURE','Describe how the liver handles excess amino acids.','It deaminates them; the nitrogen-containing part is converted to urea for excretion.')
C('3.6.2.4-06','WHY','Explain why excess absorbed amino acids lead to increased urea production.','Excess amino acids cannot be stored, so in the liver deamination removes the amino group (the nitrogen-containing part) and this is converted into urea.')
E('3.6.2.4-07','Fat as a reserve',[
'Fat stores a concentrated supply of chemical energy for later respiration.',
'Stored body fat also contributes insulation and cushioning.'
],'''A long-term energy surplus can increase fat storage; a sustained deficit can mobilise reserves. Lipids store much energy relative to mass and are largely insoluble, making them useful reserves rather than dissolved solutes. Too much stored fat increases the risk of conditions such as heart disease.''','34.2 Nutrition and Energy Production')
C('3.6.2.4-07','FEATURE','Describe two functions of stored body fat.','It provides a chemical-energy reserve; it contributes thermal insulation.')
C('3.6.2.4-07','WHY','Explain why fat is useful as a longer-term energy reserve.','It stores much chemical energy relative to its mass; it can be broken down to supply respiratory fuel when intake is insufficient.')
E('3.6.2.4-08','Water absorption',[
'Water is absorbed in both the small intestine and the colon.',
'Normally, as digested food and ions are absorbed, the gut contents become more dilute than the blood, so water follows by osmosis; if solutes build up in the gut, as in cholera, water moves the other way.'
],'''Much water is absorbed in the small intestine, including water from drinks and digestive secretions. The colon recovers additional water from the remaining contents, helping form faeces. It is therefore wrong to give the colon as the sole site of water absorption. Excessive fluid loss in diarrhoea can disrupt this recovery and deplete body water and salts. The amount of water in the gut is not simply the amount just drunk because secretions add further fluid.''','34.3 Digestive System Processes')
C('3.6.2.4-08','FEATURE','State the region of the alimentary canal, other than the small intestine, in which water is absorbed.','The colon (large intestine).')

summaries={
'3.6':'''| Mode | Source of organic nutrients | Example |
|---|---|---|
| Autotrophic | Made from inorganic materials using an energy source | A green plant photosynthesising |
| Heterotrophic | Obtained ready-made from other organisms or their products | A person eating beans |

Mineral uptake is not feeding on organic nutrients. Plants photosynthesise and also respire.''',
'3.6.1':'''A leaf is the main organ of photosynthesis. This unit follows the process from leaf structure, through the mineral ions a plant needs, to the photosynthesis equation, the factors that limit its rate and the investigations used to study it.

| Topic | Essential connection |
|---|---|
| Leaf tissues | Epidermis admits light; palisade absorbs it; air spaces and stomata permit gas exchange; veins transport materials |
| Minerals | Iron supports chlorophyll formation; magnesium is in chlorophyll; phosphate supports DNA and ATP; nitrate supplies nitrogen for amino acids |
| Photosynthesis | Carbon dioxide + water → glucose + oxygen, using light and chlorophyll |
| Products | Sugar is respired, transported as sucrose, or converted into cellulose, starch and other materials |
| Limiting conditions | Raising an input helps while that factor is limiting; a plateau does not uniquely identify the next limit |
| Investigation | Change one factor, measure an appropriate response, control others, repeat and evaluate error |
| Indicator | Light can give net carbon dioxide uptake; darkness gives respiratory release; respiration occurs in both |
''',
'3.6.2':'''Nutrition is how an organism takes in food and uses it. For people, a balanced diet supplies energy and the materials the body needs. This unit covers what happens when a nutrient is lacking, how needs change with age, activity and pregnancy, what happens to food in the alimentary canal, and how digested nutrients are absorbed and used.

| Process or need | Essential knowledge |
|---|---|
| Balanced diet | Suitable energy plus protein, fat, carbohydrate, vitamins, minerals, fibre and water |
| Deficiencies | Vitamin A: dim-light vision; D: rickets; C: scurvy; iodine: goitre; iron: anaemia |
| Changing needs | Growth, activity, pregnancy and milk production change requirements; averages do not determine individuals |
| Malnutrition | Includes shortage, excess and imbalance; energy sufficiency does not guarantee micronutrient sufficiency |
| Ingestion to egestion | Mouth entry → food breakdown → absorption → passing undigested remains through anus |
| Enzymes | Amylase: starch to maltose; maltase: maltose to glucose; proteases: proteins ultimately to amino acids; lipase: fat to fatty acids and glycerol |
| Bile | Helps neutralise acidic contents and emulsifies fat; not an enzyme |
| Absorption | Small-intestinal villi provide large area; capillaries carry sugars/amino acids, lacteals carry lipid material |
| Liver | Portal blood delivers absorbed nutrients; excess glucose forms glycogen; excess amino acids are deaminated to form urea |
| Water | Absorbed in small intestine and colon |'''
}
links={}
# Holds on whole visual needs, distinct from the subset of cards that require an unseen figure.
A.notes['visual_requirements_pending']=[
 {'requirement_id':'VIS-6116-'+o,'reason':reason} for o,reason in [
 ('3.6.1.1-01','Full leaf-section teaching/question/unfamiliar variants need scientific review; LEAF-001 omits vascular tissue.'),
 ('3.6.1.1-06','Stomatal impression images and surface identities need review; written method is not a completed practical.'),
 ('3.6.1.1-07','Reviewed specimen and matching model drawing/criteria outstanding; drawing cannot be assessed as complete.'),
 ('3.6.1.3-04','Graph acceptance and delivery remain pending; text relationship is not image interpretation.'),
 ('3.6.1.3-05','Graph acceptance and delivery remain pending.'),
 ('3.6.1.3-10','The bound graph must show a second curve, at higher carbon dioxide and the same temperature, above the first plateau; the item states this as the figure content and its key assumes it. Select and review a question variant that shows exactly this before release.'),
 ('3.6.2.2-06','Alimentary-canal diagram must correctly show accessory-gland ducts; anatomical review and delivery pending.'),
 ('3.6.2.4-01','Small-intestine anatomical teaching diagram review/delivery pending.'),
 ('3.6.2.4-03','Villus diagram must separate capillaries and lacteal; review/delivery pending.')]]
A.notes['deviations'].append({'from':'3.6.2.1-21 investigation of dietary health','to':'Ethical observational survey using anonymous consenting records; no imposed excessive intake and no diagnosis','why':'The syllabus investigation can examine associations without a harmful intervention; explicitly limited causal claims.'})
A.notes['pending_teacher_decisions']=[
 'The graph-reading APP for 3.6.1.3-10 now states the figure content it needs (second curve above the first plateau at higher carbon dioxide); the bound figure must show exactly that. No curve labels or numbers invented.',
 'Confirm curriculum conventions for iron/phosphate plant-deficiency effects and school practical methods against the named textbook when supplied.',
 'Nutrition requirements for people living with HIV require an appropriate specific health source and qualified verification; no general chapter falsely claimed to establish that clinical application.',
 'Plant practical methods, cholera mechanism, famine discussion and indicator colours without a suitable approved source locator retain empty evidence for teacher verification.'
]
# The syllabus supplies definitions, not scientific evidence for their teaching examples.
for n in ['01','02','03','04','05']:
    claims=[cl for cl in A.claims if cl['objective_ids']==['OBJ-6116-3.6.2.2-'+n]]
    for cl in claims[1:]:
        cl['evidence']=[{'source_id':OS,'locator':'34.3 Digestive System Processes','support_type':'corroboration'}]
# Move unsupported secondary limiting-factor claim off the verbatim-definition citation.
cl=next(c for c in A.claims if c['text']=='A limiting factor can change when conditions change.')
cl['evidence']=[];cl['notes']=['Explanatory scientific claim; specific approved support awaits teacher verification.']
A.write(summaries,links)
# Unit titles come from the first objective heading; make them describe the whole unit.
import json
for uid,t in {'CU-6116-3.6':'3.6 Autotrophic and heterotrophic nutrition','CU-6116-3.6.1':'3.6.1 Photosynthesis and plant nutrition','CU-6116-3.6.2':'3.6.2 Human nutrition'}.items():
    p=A.base/'content-units'/(uid+'.json')
    u=json.loads(p.read_text());u['title']=t
    p.write_text(json.dumps(u,indent=1,ensure_ascii=False)+'\n')
