from operators import Min, Max, Product
from utils import safe_range


class FuzzyInferenceSystem:
    def __init__(self, output_vars, rules):
        self.output_vars = output_vars
        self.rules = rules

    def mamdani(self):
        fuzzy_sets = []

        for rule in self.rules:
            ancestor_evaluation = rule.antecedent.evaluate()
            func = rule.consequence.member_func
            fuzzy_sets.append(Min(ancestor_evaluation, func))

        return Max(fuzzy_sets)

    def larsen(self):
        fuzzy_sets = []

        for rule in self.rules:
            ancestor_evaluation = rule.antecedent.evaluate()
            func = rule.consequence.member_func
            fuzzy_sets.append(Product(ancestor_evaluation, func))

        return Max(fuzzy_sets)

    def centroid(self, fuzzy_set):
        val_num = sum([x * fuzzy_set.evaluate(x)
                       for x in safe_range(self.output_vars.domain_a, self.output_vars.domain_b)])
        val_dem = sum([fuzzy_set.evaluate(x)
                       for x in safe_range(self.output_vars.domain_a, self.output_vars.domain_b)])
        return val_num / val_dem if val_dem != 0 else 0

    def bisection(self, fuzzy_set):
        area_sum = []
        last_val = 0
        for x in safe_range(self.output_vars.domain_a, self.output_vars.domain_b):
            new_val = fuzzy_set.evaluate(x)
            area_sum.append(new_val + last_val)
            last_val = new_val
        last_val = area_sum[len(area_sum) - 1]
        index = 0
        for i, sub_sum in enumerate(area_sum):
            if last_val / 2 < sub_sum:
                index = i
                break
        return self.output_vars.domain_a + index

    def mean_of_maxim(self, fuzzy_set):
        max_value = max([x for x in safe_range(self.output_vars.domain_a, self.output_vars.domain_b)])

        sol = [fuzzy_set.evaluate(x) for x in safe_range(self.output_vars.domain_a, self.output_vars.domain_b) if x == max_value]
        return sum(sol) / len(sol)
