import fuzzy_definitions
from test import tests_generator


def main():
    acceleration_l_val, acceleration_sets = fuzzy_definitions.acceleration_definitions()
    consumption_l_val, consumption_sets = fuzzy_definitions.consumption_definitions()
    efficiency_l_val, efficiency_sets = fuzzy_definitions.efficiency_definitions()

    full_sets = {
        'acceleration': {},
        'consumption': {},
        'efficiency': {}}
    for set_defined in acceleration_sets + consumption_sets + efficiency_sets:
        full_sets[set_defined.linguistic_var][set_defined.name] = set_defined.member_func

    tests_generator(full_sets, efficiency_l_val)


if __name__ == '__main__':
    main()
