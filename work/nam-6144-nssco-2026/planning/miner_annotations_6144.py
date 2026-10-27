"""Human-readable miner annotations, in printed question-part order.

These are Codex's semantic readings, not a keyword classifier. Each selected
number refers to a specific syllabus bullet transcribed in Step 2. M=conceptual
misconception, O=omission, C=command/demand miss, S=shallow development,
P=positive observation, N=no substantive performance comment found.
"""
ANNOTATIONS = {
'QP-2020-P1': '''
1.1:03|65|M:Business activity types were confused with legal ownership forms.
1.1:04|65|M:Purposes of ownership forms were substituted for purposes of business activity types.
1.1:08|66|P:Most candidates identified the levels successfully.
1.1:10|66|O:Definitions supporting the relationship were missing; unsupported analysis could not earn credit.
1.1:09|66,67|O:One-sided discussion and missing business impact prevented a supported recommendation.
2.2:01|67|M:Organisational structure was confused with hierarchy; incomplete definitions omitted responsibility division.
2.2:01|68|P:The advantage was generally identified successfully.
2.2:06|68|O:The product-based structure was often not recognised.
2.2:02,2.2:03|68|M:Span of control was not restricted to direct reports; answers also failed to identify which manager was being counted.
2.5:05|68,69|O:Decision levels and contextual examples were missing.
2.2:02,2.2:03|69|M:Delegation was confused with decentralisation. C:Some benefits concerned subordinates when the director was the required beneficiary. O:Justification and contextual examples were missing.
3.3:01|69,70|M:Informal workplace groups were confused with unions, pressure groups or groups outside the business.
3.3:02|70|C:Candidates described group formation rather than why workers form the group.
3.5:01|70|O:Definitions repeated the word recruitment rather than stating what happens.
3.5:01|70,71|M:Recruitment methods were confused with training methods. C:Chosen recruitment channels did not fit the farm-worker context.
3.5:02|71|S:Training methods were named without analysing their suitability. O:The recommendation lacked a justified choice and farm-specific application.
4.1:01|71,72|M:Marketing was confused with market research. O:Definitions of market omitted the exchange element.
4.1:03|72|C:Generic business aims or an inappropriate market-entry objective replaced marketing objectives for an established product.
4.4:05|72|C:Answers supplied promotion methods instead of features/actions making the product successful.
4.4:04|72,73|O:Axes, shape and the current stage were misrepresented. C:Candidates extended the curve beyond the stage supported by the case.
4.4:17,4.4:16|73|M:Promotion types and sales-promotion methods were confused. S:The effect and comparative choice were missing.
3.4:12|74|M:Redundancy was confused with dismissal; examples alone did not provide a full definition.
5.3:01|74|O:Definitions omitted government enforcement of the minimum wage.
3.1:01|74|M:Job-security needs were confused with social-security benefits.
3.1:02|74,75|O:Theory names were not attached to the correct explanation; analysis and application were missing.
5.3:01,5.3:03|75|O:One-sided accounts and missing contextual impact prevented evaluation of employee protection.
''',
'QP-2020-P2': '''
2.1:02|77,78|S:Ownership characteristics were identified without developing their impact on the business.
2.4:05|78|O:Ratios were not both calculated and compared. M:Ratio notation was confused with a bare decimal.
1.2:06|79|S:Small-firm survival needed developed reasons linked to the technical-product business.
1.2:02|79,80|M:Nationalisation was confused with international trade or private-sector public limited companies. O:Alternatives and a justified decision were missing.
4.2:01|80|C:Research methods were given instead of the importance of research. S:Reasons were not developed into business effects.
4.5:05,4.5:06|80,81|O:Candidates discussed one production method rather than comparing both. S:Evaluation repeated the body without weighing suitability.
3.1:02|81,82|M:Herzberg's framework was replaced by Maslow or Taylor; hygiene factors and motivators were not distinguished.
3.4:14,3.4:16|82|C:Communication or leadership in general replaced the requested decision about worker participation.
5.2:02|83|O:Answers omitted either the reason for intervention or the means used. S:Application and causal development were weak.
5.1:05,5.1:06|83,84|O:Social costs and benefits were discussed without a reasoned planning decision.
''',
'QP-2021-P1': '''
1.1:11|65|M:Stakeholder groups were confused with informal/formal groups or production sectors.
2.5:01|65|O:The definition omitted achieving objectives.
2.5:03|65|P:Functions of management were generally identified correctly.
3.4:02|65,66|M:Cooperation and joint responsibility were confused with ownership forms. O:Explanations were not labelled clearly enough to distinguish the two ideas.
5.3:02|66|S:Protection measures were named without explaining impact. O:Government agency and evaluative judgement were missing.
2.3:01|66|M:Needs for finance were confused with sources of finance. O:Equivalent expansion examples were repeated as distinct answers.
4.3:01|67|C:Components were listed instead of defining the business plan fully.
4.3:02|67|M:The production-plan component was confused with the whole business plan.
4.4:06|67|O:Definitions lacked the distinctive brand-name and repeated-brand-purchase elements; contextual analysis was missing.
4.5:09,4.5:11|67,68|S:Location factors were listed without effects. O:The remain-versus-relocate judgement was missing.
4.1:01|68|M:Marketing was confused with advertising or market research. O:Definitions were incomplete.
4.1:03|68|C:General private-business aims replaced marketing objectives.
3.5:01|68|O:Training definitions omitted skill/knowledge acquisition or its purpose.
4.1:05|68,69|O:Definitions of the two orientations were not applied to the supplied business.
3.5:02|69|O:On-the-job training was discussed one-sidedly. S:The conclusion repeated the discussion instead of justifying suitability.
4.4:08|70|O:The monetary value was not linked to a product.
4.4:07|70|M:Packaging functions were confused with branding, the marketing mix or AIDA.
5.3:01|70|M:Social security was confused with job security or trade-union benefits.
5.4:01|70,71|M:Consumer protection was confused with employee protection. O:Specific protection knowledge and application were missing.
5.3:01,5.3:03|71|M:Employee health-and-safety protection was confused with consumer protection. O:One-sided answers prevented evaluation.
4.4:15|71,72|M:AIDA requirements were confused with marketing-mix elements. O:The acronym alone was not expanded into requirements.
4.2:01|72|O:Research definitions omitted the information-gathering purpose/timing required by the guide.
4.4:09|72|P:Pricing strategies were generally identified correctly.
4.4:13|72|O:Definitions repeated the terms rather than explaining them. S:Analysis and application were weak.
4.4:16,4.4:17|72,73|O:The same contextual detail was reused for separate application credit. O:The best method was not chosen and justified.
''',
'QP-2021-P2': '''
1.2:03|74|M:Activity sectors were confused with forms of ownership.
2.1:05,2.1:02|74,75|O:The ownership alternatives were not compared and no reasoned decision was reached.
2.6:05|75,76|O:Barriers were generic rather than case-specific. C:Solutions did not address the barriers identified.
4.5:05,4.5:06|76,77|M:Job, batch and flow production were confused. O:Comparison, application and a justified choice were missing.
3.4:11|77|S:Conflict-resolution methods were named without a developed business-specific explanation.
3.4:15|77,78|C:General participation replaced comparison of the named mechanisms. O:A comparative choice was missing.
4.5:08|78,79|M:Economies of scale were confused with economic systems. O:Specific economies and contextual consequences were missing.
4.1:04|79|C:Segmentation bases did not fit the products and customers. O:The best segmentation choice was not justified.
2.4:01|79,80|M:Accounting functions were confused with general management functions.
2.4:05|80|O:Some answers omitted calculations; others calculated without evaluating the two years.
''',
'QP-2022-P1': '''
1.2:03,1.1:03|75|M:Activity type was confused with ownership form.
1.1:11|75|P:Stakeholder groups were generally identified correctly.
2.1:02|75,76|O:Identification of the ownership form needed a supporting characteristic for full credit.
1.1:02|76|P:Two knowledge points followed by relevant application and analysis were generally recognised.
5.4:02,5.4:03|76|O:Knowledge of protection of capital providers and evaluation were weak.
2.3:02|77|M:Public-sector finance was confused with private-sector finance.
2.3:04|77|M:Internal funds were confused with unrelated external sources.
2.4:04|77|M:Profit and immediately available cash were not distinguished accurately.
2.3:05|77|C:Borrower preferences replaced the finance provider's lending/investment criteria.
5.3:01,5.3:03|78|N:The report supplies employee-protection guidance despite the paper wording employers; meaning is uncertain without resolving that source discrepancy.
4.4:01|78|O:The definition repeated product and omitted satisfying consumer wants.
4.4:02|78|O:Product types were poorly known.
4.4:19|78|C:Candidates copied sales routes without translating them into distribution channels.
4.4:10|79|O:Some stopped at unit cost or markup instead of completing the selling-price calculation.
3.5:02|79|C:Training had to suit the workforce; induction alone did not answer the requested choice.
2.1:02|80|O:Cooperative characteristics were unfamiliar; narrow teaching of ownership forms left a gap.
5.2:04|80|O:Barriers to international trade were poorly known.
3.4:11|80|C:Responses gave ways to avoid conflict rather than methods accepted for resolving the dispute in this guide.
4.4:21|80|C:Transport methods needed to fit the actual cross-border journey.
5.1:08|80,81|O:Environmental strategies lacked specific knowledge and case relevance.
2.4:05|81|M:Profitability ratios were confused with liquidity, turnover or solvency ratios.
2.4:02|81|M:Unit cost was confused with marginal cost.
2.6:01|81|O:The definition needed message receipt, understanding and feedback, not merely people talking.
2.6:02|81,82|O:Answers repeated inside/outside without identifying who communicates with whom.
2.4:05|82,83|O:Percentage conversion, interpretation of the actual figures and an evidence-based judgement were missing.
''',
'QP-2022-P2': '''
3.4:04|84|M:Craft and industrial unions were confused. S:Union names needed explanations of the workers represented.
2.1:05,2.1:02|84,85|M:Franchisor and franchisee were reversed. C:The task concerned selling the business idea rather than a generic comparison with sole trading.
4.5:07|85|C:Business effects replaced effects on workers. O:Both positive and negative worker effects needed consideration.
4.5:05,4.5:06|86|M:Batch and flow production were confused. O:Definitions alone did not support the production choice.
4.3:03|87|S:Uses of the plan were stated without explaining why they help this business.
4.1:04|87,88|C:Segmentation choices did not fit the product or customers. O:A justified decision was missing.
3.4:10|88|S:Conflict causes were named without business effects. O:Closely related pay/condition points were double-counted and case application was missing.
2.4:05|88,89|M:Liquidity was confused with profitability or solvency. O:Calculated ratios lacked interpretation against the guide's reference levels.
5.1:02|89|C:Intervention was restricted to workers despite other relevant affected groups. S:Reasons lacked developed case-specific consequences.
5.2:06|89,90|O:Negative effects and the final judgement were missing. C:The factory made containers rather than the food inside them.
''',
'QP-2023-P1': '''
2.6:04|79|M:Communication-process elements were confused with communication types or ways.
2.5:04|79|M:Managerial qualities were confused with management functions or entrepreneur characteristics.
1.1:02|79,80|O:Community contributions were stated incompletely or too vaguely.
1.1:01|80|O:Case phrases were copied without earning distinct knowledge or contextual development.
3.5:02|80|C:Off-the-job training replaced assessment of the named on-the-job method. O:Both advantages and disadvantages were needed before judgement.
3.4:03|81|O:The definition omitted that a union consists of workers.
3.4:08|81|C:Benefits of union membership replaced the requested categories of reasons for joining.
2.3:01|81|P:Finance needs were generally identified; profit maximisation was not a financing need in this task.
4.5:02|81|S:Productivity factors lacked contextual causal development. C:Some proposed factors were not accepted in this particular guide.
4.5:06|81,82|C:The method had to fit individually specified products. O:Suitability lacked a balanced justification.
4.4:03|82|O:Definitions omitted the idea of stages/phases through which the product passes.
4.4:11|82|M:Marketing promotion was confused with employee promotion. C:Methods were listed instead of defining the concept.
1.1:08|82|M:Levels of specialisation were confused with management levels.
2.3:02,2.3:03|83|C:Finance did not fit the asset, time horizon or ownership form. S:Named sources were not developed.
5.3:02|83,84|C:General HIV discussion or generic safety replaced government protection at work. O:The final judgement was missing.
2.2:02|84|O:The definition omitted the expected standard of carrying out the duty.
2.2:02|84|O:Delegation definitions omitted the manager's continuing accountability.
1.1:12|84|O:Consumer objectives needed the precise intended meaning rather than vague low-price wording.
5.2:02|84,85|C:How exporters are assisted replaced why assistance is given; imports were substituted for exports.
5.2:06|85|O:Answers omitted negative implications and a choice supported by reasons.
3.4:09|86|M:Organisational conflict was confused with organisational structure. O:The definition repeated conflict instead of explaining it.
3.4:16|86|C:Generic benefits were not tied to participation in decision making.
3.2:01|86|M:Non-financial rewards were confused with cash allowances. C:Selected benefits did not fit the workforce context.
3.2:02,3.2:03|86,87|C:Candidates discussed business benefits or other theories rather than how this payment system motivates workers; some supplied disadvantages when benefits were requested.
3.4:15|87|O:Knowledge of democratic participation was weak and unsupported generalities replaced a reasoned assessment.
''',
'QP-2023-P2': '''
2.2:05|88|C:Features of structure replaced reasons why expansion requires a change. S:Identified reasons were not developed.
5.2:01,5.2:03|88,89|M:Costs and benefits of government intervention were confused with a generic social-cost-benefit exercise.
2.2:04,2.2:01|89|O:The chart did not reflect the expanded organisation; explanations of its usefulness were missing.
2.1:05,2.1:02|90,91|M:Close-corporation members were called shareholders. C:Social costs and benefits replaced the owners' advantages/disadvantages. O:The decision was missing.
4.4:09|91|C:Pricing strategies did not fit entry into a competitive market. S:Definitions replaced explanations of business impact.
2.4:05|91|O:Correct ratio formulas, two-year comparisons and interpretation against reference levels were missing; some substituted remedies for an assessment of improvement.
5.4:02|92|M:Loan security was interpreted as physical protection. C:Other protected groups replaced capital providers.
4.5:09,4.5:10,4.5:11|92,93|M:Location factors were confused with factors of production.
4.2:04|93|M:A time-series line graph was confused with a product life cycle or bar chart. O:Axes were unlabelled.
5.3:01,5.3:03|93|C:Cost cutting or definitions of costs and benefits replaced assessing the effects of a minimum wage. O:The judgement was missing.
''',
'QP-2024-P1': '''
2.4:02|79|M:Unit cost was confused with marginal cost.
2.4:03|79|M:Income and expenses were confused with net profit and net loss.
2.4:02|79|M:Fixed/variable costs were confused with income/expenses. O:Definitions failed to relate cost behaviour to output.
2.4:07|80|C:Stakeholder aims replaced how users actually use financial statements. O:Case application was missing.
4.5:06|81|M:Job production was confused with on-the-job training. O:A one-sided answer could not support evaluation.
4.2:02|81|O:Definitions omitted existing information/data and repeated the term research.
4.2:02|82|M:External secondary sources were confused with primary research or internal sources.
4.1:03|82|P:Marketing objectives were generally identified correctly.
4.1:05|82,83|M:Definitions of market and product orientation were sometimes reversed; overall contextual performance improved.
4.1:04|83|C:Advantages of segmentation replaced identification and analysis of suitable segmentation bases. O:The judgement was weak.
3.4:05|84|M:Shop stewards were confused with trade-union officials. O:The unpaid/voluntary characteristic was omitted.
3.4:13|84|P:Industrial action types were generally identified correctly.
3.4:12|84|M:Redundancy was confused with dismissal.
3.2:02,3.2:01|85|C:Effects on the business replaced how rewards motivate the employee. O:Application and causal explanation were missing.
5.3:01,5.3:03|86|S:Measures lacked effects on the relevant parties. O:Application and evaluation of protection were missing; choosing a method alone did not answer the report's wider judgement.
1.1:06|87|O:Most identified a mixed economy, but the guide rejected an imprecise label.
1.1:06|87|C:Characteristics were supplied instead of advantages of a market economy.
1.2:04|87|O:Equivalent size measures were repeated as separate answers.
1.1:05|88|M:Fiscal and monetary-policy mechanisms were mixed up. O:Contextual effects were missing.
4.5:10,4.5:11|89|S:Location factors were restated rather than traced to effects on this business. O:Choices were not supported.
4.4:18|89|M:Distribution was confused with transport methods.
4.4:12|89|M:Product was confused with production in the marketing mix. C:The guide required the mix's category labels rather than a related term.
4.5:02|90|O:Generic management/communication terms lacked the improvement qualifier; availability of labour alone was not accepted.
4.4:13|90|O:Definitions repeated inform/persuade instead of explaining the distinction. S:Analysis and contextual application were missing.
5.1:08|91|C:Environmental proposals did not fit the sport-service context. O:Specific knowledge and a justified decision were weak.
''',
'QP-2024-P2': '''
2.6:01|92|C:Definitions, methods or barriers replaced reasons for effective communication. O:Copied case phrases did not form an applied explanation.
2.6:03|93,94|M:Communication ways were confused with one/two-way or internal/external categories.
3.1:02|94|M:Maslow was substituted for Herzberg; hygiene and maintenance were counted as separate factors. O:Worker-focused causal application was missing.
2.1:05,2.1:02|95,96|M:Partnership was incorrectly assigned limited liability or shareholders. O:Repeated shared features, missing case application and unsupported choices lost marks.
4.5:08,2.1:04,2.2:05|97|C:Positive growth effects replaced the requested negative effects. S:Listed effects were not developed into business impact.
3.4:15|98,99|M:Quality circles and worker councils were confused. O:The choice lacked impact analysis and contextual support.
1.1:09|100|P:Most candidates explained the effects of specialisation successfully.
4.4:17,4.4:12|101|P:Many candidates made a suitable justified promotional choice. C:The guide distinguished promotion types from advertising media.
2.4:05|102|M:Solvency was confused with liquidity, inverted formulas or percentages. O:Comparison with the prior year and the guide's reference point was missing.
5.4:01,5.4:03|103|C:Consumer rights or economic policies replaced protection mechanisms; some switched to workers. O:Case application and a justified comparative choice were missing.
''',
}
