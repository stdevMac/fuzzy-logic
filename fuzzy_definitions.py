from problem import acceleration, consumption, efficiency
from utils import LinguisticVar, FuzzySet, Antecedent, Consequence, Rule
from operators import Or, And


def acceleration_definitions():
    acceleration_functions = {
        'positive': acceleration.positive,
        'negative': acceleration.negative,
    }

    domain = (acceleration.domain_a, acceleration.domain_b)
    acceleration_l_var = LinguisticVar('acceleration', domain, acceleration_functions)
    fuzzy_sets = []
    for item in acceleration_functions.keys():
        fuzzy_sets.append(FuzzySet(item, domain, acceleration_functions[item], 'acceleration'))
    return acceleration_l_var, fuzzy_sets


def consumption_definitions():
    consumption_functions = {
        'high': consumption.high,
        'low': consumption.low,
    }

    domain = (consumption.domain_a, consumption.domain_b)
    consumption_l_var = LinguisticVar('consumption', domain, consumption_functions)
    fuzzy_sets = []
    for item in consumption_functions.keys():
        fuzzy_sets.append(FuzzySet(item, domain, consumption_functions[item], 'consumption'))
    return consumption_l_var, fuzzy_sets


def efficiency_definitions():
    efficiency_functions = {
        'high': efficiency.high,
        'low': efficiency.low,
    }

    domain = (efficiency.domain_a, efficiency.domain_b)
    efficiency_l_var = LinguisticVar('consumption', domain, efficiency_functions)
    fuzzy_sets = []
    for item in efficiency_functions.keys():
        fuzzy_sets.append(FuzzySet(item, domain, efficiency_functions[item], 'efficiency'))
    return efficiency_l_var, fuzzy_sets


def get_rules(sets, acceleration_values, consumption_values):
    new_rules = []

    # 1. if consumption is low => efficiency high
    antecedent = Antecedent(sets['consumption']['low'], consumption_values)
    consequence = Consequence(sets['efficiency']['high'])
    new_rules.append(Rule(antecedent, consequence))

    # 2. if consumption is high => efficiency low
    antecedent = Antecedent(sets['consumption']['high'], consumption_values)
    consequence = Consequence(sets['efficiency']['low'])
    new_rules.append(Rule(antecedent, consequence))

    # 3. if acceleration is negative and consumption low => efficiency high
    antecedent_acceleration = Antecedent(sets['acceleration']['negative'], acceleration_values)
    antecedent_consumption = Antecedent(sets['consumption']['low'], consumption_values)
    consequence = Consequence(sets['efficiency']['high'])
    new_rules.append(Rule(And(antecedent_acceleration, antecedent_consumption), consequence))

    # 4. if acceleration is positive or consumption high => efficiency low
    antecedent_acceleration = Antecedent(sets['acceleration']['positive'], acceleration_values)
    antecedent_consumption = Antecedent(sets['consumption']['high'], consumption_values)
    consequence = Consequence(sets['efficiency']['low'])
    new_rules.append(Rule(Or(antecedent_acceleration, antecedent_consumption), consequence))

    return new_rules
