class Max:
    def __init__(self, functions):
        self.functions = functions

    def evaluate(self, value):
        l = []
        for function in self.functions:
            l.append(function.evaluate(value))
        return max(l)


class Min:
    def __init__(self, ancestor_evaluation, function):
        self.ancestor_evaluation = ancestor_evaluation
        self.function = function

    def evaluate(self, eval_value):
        return min(self.ancestor_evaluation, self.function(eval_value))


class Product:
    def __init__(self, ancestor_evaluation, function):
        self.ancestor_evaluation = ancestor_evaluation
        self.function = function

    def evaluate(self, eval_value):
        return self.ancestor_evaluation * self.function(eval_value)


class And:
    def __init__(self, func_a, func_b):
        self.left_node = func_a
        self.right_node = func_b

    def evaluate(self):
        return min(self.left_node.evaluate(),self.right_node.evaluate())


class Or:
    def __init__(self, func_a, func_b):
        self.left_node = func_a
        self.right_node = func_b

    def evaluate(self, ):
        return max(self.left_node.evaluate(), self.right_node.evaluate())
