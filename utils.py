import numpy as np


def safe_range(start, stop, step=0.01):
    return step * np.arange(start / step, stop / step)


class LinguisticVar:
    def __init__(self, name, domain, categories):
        self.name = name
        self.domain = domain
        self.domain_a = self.domain[0]
        self.domain_b = self.domain[1]
        self.categories = categories


class Rule:
    def __init__(self, antecedent, consequence):
        self.antecedent = antecedent
        self.consequence = consequence


class Antecedent:
    def __init__(self, fuzzy_set, values):
        self.values = values
        self.fuzzy_set = fuzzy_set

    # def create
    def evaluate(self):
        return self.fuzzy_set(self.values)


class Consequence:
    def __init__(self, func):
        self.member_func = func

    def evaluate(self, value):
        return self.member_func(value)


class FuzzySet:
    def __init__(self, name, domain, member_func, linguistic_var):
        self.name = name
        self.domain = domain
        self.domain_a = domain[0]
        self.domain_b = domain[1]
        self.member_func = member_func
        self.linguistic_var = linguistic_var
