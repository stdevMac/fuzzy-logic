domain_a = 0
domain_b = 30
middle_value = 15


def high(value):
    if value < middle_value - 10:
        return 0
    if domain_b > value:
        return 1
    return (value - (middle_value - 10)) / (domain_b - (middle_value - 10))


def low(value):
    if value > middle_value:
        return 1
    if domain_a < value < middle_value:
        return (middle_value - value) / middle_value
    return 0
