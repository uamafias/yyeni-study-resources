"""Numbers and Operations fixed-example presentation; no live Recall answers."""
from . import number_properties_content as properties
from . import number_fractions_content as fractions
from . import number_finance_content as finance
from . import number_scale_content as scale
from . import number_bounds_content as bounds

LESSONS={
 'nssco_number_classifications_properties':(15792,'Number Classifications and Properties',properties.classification,properties.CLASS_LABELS),
 'nssco_directed_numbers_in_action':(15793,'Directed Numbers in Action',properties.directed,properties.DIRECTED_LABELS),
 'nssco_fractions_decimals_percentages':(15794,'Fractions, Decimals, Percentages and Ordering',fractions.content,fractions.LABELS),
 'nssco_advanced_percentages':(15795,'Advanced Percentage Calculations',finance.percentages,finance.PERCENT_LABELS),
 'nssco_standard_form_estimates_approximations':(15796,'Standard Form, Estimates and Approximations',scale.standard,scale.STANDARD_LABELS),
 'nssco_limits_of_accuracy':(15797,'Limits of Accuracy',bounds.content,bounds.LABELS),
 'nssco_ratios_scales_rates':(15798,'Ratios, Scales and Rates',scale.rates,scale.RATIO_LABELS),
 'nssco_personal_finance_currency':(15799,'Personal Finance and Currency',finance.finance,finance.FINANCE_LABELS),
 'nssco_income_taxes_bills':(15800,'Income, Taxes and Bills',finance.income,finance.INCOME_LABELS),
}
LEVEL_LABELS={gid:row[3] for gid,row in LESSONS.items()}


def number_content(problem):
    row=LESSONS.get(problem.generator_id)
    return row[2](problem) if row else None
