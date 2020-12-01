domain_a = 0
domain_b = 120
positive_middle_value = 70


def positive(value):
    if value < positive_middle_value - 10:
        return 0
    if domain_b > value:
        return 1
    return (value - (positive_middle_value - 10)) / (domain_b - (positive_middle_value - 10))


def negative(value):
    if value > positive_middle_value:
        return 0
    if domain_a < value < positive_middle_value:
        return (positive_middle_value - value) / positive_middle_value
    return 1
