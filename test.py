import fuzzy_definitions
from fuzzy_system import FuzzyInferenceSystem
from problem import acceleration, consumption
import random


def mamdani_centroid(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.centroid(fuzzy_system.mamdani())


def mamdani_bisection(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.bisection(fuzzy_system.mamdani())


def mamdani_mean_of_maxim(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.mean_of_maxim(fuzzy_system.mamdani())


def larsen_centroid(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.centroid(fuzzy_system.larsen())


def larsen_bisection(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.bisection(fuzzy_system.larsen())


def larsen_mean_of_maxim(rules, output_var):
    fuzzy_system = FuzzyInferenceSystem(output_var, rules)
    return fuzzy_system.mean_of_maxim(fuzzy_system.larsen())


def run_test(sets_defined, acceleration_value, consumption_value, output_vars, test_type):
    print(test_type)
    new_rules = fuzzy_definitions.get_rules(sets_defined, acceleration_value, consumption_value)

    tests = {'Mamdani using Centroid': mamdani_centroid,
             'Mamdani using Bisection': mamdani_bisection,
             'Mamdani using Mean of Maxim': mamdani_mean_of_maxim,
             'Larsen using Centroid': larsen_centroid,
             'Larsen using Bisection': larsen_bisection,
             'Larsen using Mean of Maxim': larsen_mean_of_maxim
             }
    for test in tests:
        print(test)
        print(tests[test](new_rules, output_vars))


def tests_generator(sets_defined, output_vars):
    # Example a lot of acceleration
    rnd_acceleration = random.randint(acceleration.positive_middle_value, acceleration.domain_b)
    rnd_consumption = random.randint(consumption.middle_value, consumption.domain_b)

    run_test(sets_defined, rnd_acceleration, rnd_consumption, output_vars,
             'Test high acceleration and high consumption')
    # Example a lot of acceleration
    rnd_acceleration = random.randint(acceleration.domain_a, acceleration.positive_middle_value)
    rnd_consumption = random.randint(consumption.domain_a, consumption.middle_value)

    run_test(sets_defined, rnd_acceleration, rnd_consumption, output_vars,
             f'\nTest low acceleration and low consumption with {rnd_acceleration} '
             f'of acceleration and {rnd_consumption} of consumption')
