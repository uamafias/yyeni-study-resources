"""Settled economic senses; original teaching definitions, with homonym guards."""
import json
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
DEFINITIONS='''scarcity|Resources are limited relative to the wants that could be satisfied with them.
opportunity cost|The value of the next-best alternative forgone when a choice is made.
economic good|A good that uses scarce resources and therefore has an opportunity cost.
free good|A good available without sacrificing scarce resources in the relevant situation; it has no opportunity cost there.
land|Natural resources used in production.
labour|Human physical and mental effort used in production.
capital|Produced resources used to produce other goods and services.
entrepreneurship|Organising the other factors of production and bearing business risk.
market economic system|Resources are allocated mainly through private decisions and prices determined in markets.
planned economic system|A central authority makes the main resource-allocation decisions.
mixed economic system|Both market decisions and government decisions influence resource allocation.
specialisation|Concentrating productive effort on a narrower range of tasks or products.
division of labour|Separating a production process into tasks performed by different workers.
private sector|Economic activity owned and controlled by private individuals or organisations.
public sector|Economic activity owned or controlled by government.
sole proprietor|An individual who owns and operates an unincorporated business.
partnership|A business owned by people who agree to operate it together and share its results.
private company|An incorporated business whose shares are not offered freely to the general public.
public limited company|An incorporated company that can offer shares to the public; public in its name does not establish government ownership.
public corporation|An enterprise established or owned by the state to undertake economic activity.
close corporation|An incorporated business owned by members, with a legal identity separate from them; statutory restrictions require a current Namibian legal source.
co-operative|A business owned and controlled by members to serve their shared interests.
multinational business|A business controlling production or operations in more than one country.
limited liability|Owners' financial liability for business debts is limited by the legal form; it does not remove risk to the lender.
trade union|An organisation representing workers in matters such as pay and working conditions.
employer association|An organisation representing the interests of employers, often within an industry.
collective bargaining|Negotiation between employers or their representatives and worker representatives over employment conditions.
white-collar union|A union representing workers mainly in office, administrative or professional occupations.
blue-collar union|A union representing workers mainly in manual or industrial occupations.
craft union|A union representing workers sharing a particular skilled trade.
money|An asset generally accepted as payment for goods, services and debts.
central bank|The institution responsible for central monetary functions such as monetary policy and oversight of the banking system.
commercial bank|An institution accepting deposits, providing payment services and supplying credit.
stock exchange|An organised market for buying and selling financial securities such as shares.
exchange rate|The price of one currency expressed in another currency; state the quotation convention.
appreciation|A rise in a currency's value in terms of another currency under a floating exchange-rate system.
depreciation|A fall in a currency's value in terms of another currency under a floating exchange-rate system.
market|An arrangement through which buyers and sellers interact to exchange a product or resource.
demand|The quantities consumers are willing and able to buy at different prices over a specified period, other things equal.
supply|The quantities producers are willing and able to offer at different prices over a specified period, other things equal.
equilibrium price|The price at which quantity demanded equals quantity supplied in the specified market.
movement along a curve|A change in quantity demanded or supplied caused by a change in the product's own price, other determinants unchanged.
shift of a curve|A change in demand or supply caused by a determinant other than the product's own price.
shortage|Excess demand: quantity demanded exceeds quantity supplied at the stated price.
surplus|Excess supply: quantity supplied exceeds quantity demanded at the stated price.
price elasticity of demand|The responsiveness of quantity demanded to a price change, measured by percentage change in quantity demanded divided by percentage change in price.
price elasticity of supply|The responsiveness of quantity supplied to a price change, measured by percentage change in quantity supplied divided by percentage change in price.
perfectly inelastic demand|Quantity demanded does not change when price changes over the relevant range; PED is zero.
advertising|Paid communication intended to inform or influence potential buyers about a product or organisation.
perfect competition|A model with many price-taking firms selling an identical product, with free entry and exit and adequate information.
monopoly|A market structure with a single supplier in the defined market and barriers that restrict entry.
nominal income|Income measured in current money units before adjusting for changes in prices.
real income|The purchasing power of money income after allowing for changes in prices.
disposable income|Income remaining after direct taxes and other required deductions, available for spending or saving.
transfer earnings|The minimum reward required to keep a factor in its present use.
economic rent|The reward received by a factor above its transfer earnings.
transfer payment|A payment made without receiving a current good or service in exchange.
saving|The part of disposable income not spent on current consumption.
borrowing|Obtaining funds on terms that require repayment, usually with interest.
production|The creation of goods and services that satisfy wants.
productivity|Output per unit of input over a specified period.
capital intensive|Using a relatively high proportion of capital compared with labour in production.
labour intensive|Using a relatively high proportion of labour compared with capital in production.
total cost|The full cost of producing a specified output; total fixed cost plus total variable cost.
fixed cost|Cost that does not vary with output over the stated short-run range.
variable cost|Cost that changes as output changes over the stated range.
average cost|Total cost divided by the quantity produced.
total revenue|Income from sales; for a single uniform price, price multiplied by quantity sold.
average revenue|Total revenue divided by quantity sold.
marginal revenue|The change in total revenue from selling an additional unit.
marginal cost|The change in total cost from producing an additional unit.
profit|Total revenue minus total cost over the stated period.
profit maximisation|Choosing the feasible output that gives the greatest difference between total revenue and total cost; appropriate marginal conditions must describe a maximum.
economies of scale|Reductions in long-run average cost as the scale of production increases.
diseconomies of scale|Increases in long-run average cost as the scale of production increases.
horizontal integration|Combining businesses operating at the same stage in the same industry.
forward vertical integration|Combining with a business at a later stage of the production or distribution chain.
backward vertical integration|Combining with a business at an earlier stage of the production chain.
fiscal policy|Government decisions about taxation and public spending used to influence economic activity.
monetary policy|Actions influencing money, credit and interest conditions to pursue economic objectives.
direct tax|A tax imposed directly on an income, profit or wealth base.
indirect tax|A tax imposed on expenditure or transactions involving goods and services.
progressive taxation|The average tax rate rises as the taxable base or income rises.
proportional taxation|The average tax rate stays constant as the taxable base or income rises.
regressive taxation|The average tax burden falls as a share of income as income rises.
budget deficit|Government expenditure exceeds government revenue over the stated period.
budget surplus|Government revenue exceeds government expenditure over the stated period.
public good|A good that is non-rival and non-excludable in consumption; provision still uses scarce resources.
merit good|A good considered socially beneficial and liable to underconsumption in a market, for example through external benefits or imperfect information.
investment|Spending that adds to or replaces productive capital; it differs from merely depositing savings or transferring existing assets.
inflation|A sustained increase in the general price level over time.
retail price index|A weighted index tracking prices of a representative household-consumption basket relative to a base period.
unemployment|People willing and able to work who are seeking work but cannot find employment under the specified statistical definition.
cyclical unemployment|Unemployment associated with a fall in aggregate demand during an economic downturn.
structural unemployment|Unemployment caused by a mismatch between available workers and the skills, locations or occupations demanded.
seasonal unemployment|Unemployment arising from predictable seasonal changes in demand for labour.
frictional unemployment|Temporary unemployment while people move between jobs or search for suitable work.
Gross Domestic Product|The value of final goods and services produced within a country's territory over a specified period, avoiding double counting.
Gross National Product|Domestic product adjusted for net income earned from abroad by the country's residents, using the course's stated accounting convention.
National Income|Income earned by a country's factors of production over a stated period; specify the accounting measure when making numerical comparisons.
GDP per capita|Gross Domestic Product divided by population; use a consistent period and population measure.
balance of trade|The value of goods exports minus goods imports over a stated period.
balance of payments|A record of economic transactions between residents and the rest of the world over a stated period.
current account|The balance-of-payments account covering trade in goods and services, primary income and current transfers.
absolute advantage|The ability to produce more output from the same resources, or the same output with fewer resources.
comparative advantage|The ability to produce a good at a lower opportunity cost than another producer.
protection|Measures restricting imports or favouring domestic producers against foreign competition.
free trade|International trade without government-imposed barriers intended to restrict trade.
birth rate|Live births per thousand people in a population over a stated period, usually a year.
death rate|Deaths per thousand people in a population over a stated period, usually a year.
fertility rate|A measure of births per woman; distinguish a general fertility rate from the expected lifetime total fertility rate when using figures.
net migration|Immigration minus emigration over the stated period.
natural population increase|Births minus deaths; it excludes migration.
living standards|Material welfare and wider conditions affecting people's quality of life.
economic growth|An increase in real output over time; it is distinct from population growth.
private cost|A cost borne by the individual or organisation undertaking an activity.
external cost|A cost imposed on a third party that is not included in the decision-maker's private cost.
social cost|Private cost plus external cost for the stated activity and period.
private benefit|A benefit received by the individual or organisation undertaking an activity.
external benefit|A benefit received by third parties outside the decision-maker's private benefit.
social benefit|Private benefit plus external benefit for the stated activity and period.
conservation|Managing resource use to maintain resources or their benefits over time.
exploitation of resources|Using resources for economic purposes; it is not necessarily unsustainable overuse.'''
DEFINITIONS += """
complementary goods|Goods used together, so a rise in the price of one tends to reduce demand for the other, other things equal.
substitute goods|Goods serving similar wants, so a rise in the price of one tends to increase demand for the other, other things equal.
production possibility frontier|The combinations of two outputs obtainable when available resources are fully and efficiently used with given technology; moving along it illustrates opportunity cost.
short run|A production period in which at least one factor input is fixed.
long run|A production period in which all factor inputs can be varied.
law of diminishing returns|With technology and at least one input fixed, successive equal additions of a variable input eventually add less extra output.
normal profit|The minimum reward needed to retain entrepreneurship in its current use; it is included in economic cost.
abnormal profit|Revenue in excess of economic cost including normal profit, for the specified period.
law of increasing opportunity cost|Along a bowed-out production possibility frontier, successive equal additions of one output require increasingly large sacrifices of the other, with given resources and technology.
"""
terms=[]
for line in DEFINITIONS.splitlines():
    term,sense=line.split('|',1)
    terms.append({'term':term,'sense':sense,'provenance':'original teaching restatement within the syllabus; clarify with source before making a jurisdiction-specific claim',
                  'homonym_warning':'Use the specified quantity, sector, time horizon and population; consult the misconception register for the relevant boundary.'})
(WS/'curriculum/glossary.json').write_text(json.dumps({'glossary_id':'GLOSSARY-NAM-6145-NSSCO-2026',
    'status':'settled_for_authoring','note':'Definitions are original teaching restatements, not copied mark-scheme answers. No null senses. Legal numerical limits and current statistics remain outside these definitions.', 'terms':terms},indent=2,ensure_ascii=False)+'\n')
(WS/'curriculum/definition-rulings.json').write_text(json.dumps({'rule':'Syllabus determines scope; settled economic definitions govern learner wording. These clarifications do not add independent advanced units.','rulings':[
 {'term':'demand','ruling':'Include willingness AND ability to buy, a price range, period and other things equal; the syllabus shorthand omits conditions.'},
 {'term':'diseconomies of scale','ruling':'Use rising LONG-RUN average cost as scale rises; distinguish it from diminishing returns with a fixed input.'},
 {'term':'law of increasing opportunity cost','ruling':'Explain an increasing sacrifice along a bowed-out PPF with fixed resources and technology. A straight-line schedule has constant opportunity cost and is not evidence of increasing opportunity cost.'},
 {'term':'normal and abnormal profit','ruling':'Teach only the meanings necessary for the specified market structures; no extra welfare or oligopoly unit.'}
]},indent=2)+'\n')
print(len(terms),'settled glossary entries')
