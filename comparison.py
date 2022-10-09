def greater(a, b):
    a = try_convert(a)
    if type(b) is not float:
        raise Exception('Cannot do these type of comparissons without numbers')
    else:
        return a > b


def less(a, b):
    a = try_convert(a)
    if type(b) is not float:
        raise Exception('Cannot do these type of comparissons without numbers')
    else:
        return a < b


def greater_equal(a, b):
    a = try_convert(a)
    if type(b) is not float:
        raise Exception('Cannot do these type of comparissons without numbers')
    else:
        return a >= b


def less_equal(a, b):
    a = try_convert(a)
    if type(b) is not float:
        raise Exception('Cannot do these type of comparissons without numbers')
    else:
        return a <= b


def try_convert(num):
    try:
        _num = float(num)
        return _num
    except ValueError:
        raise Exception('Cannot do these type of comparissons without numbers')


class Comparison:
    def __init__(self):
        self.comparators = {
            '>': lambda a, b: greater(a, b),
            '<': lambda a, b: less(a, b),
            '>=': lambda a, b: greater_equal(a, b),
            '<=': lambda a, b: less_equal(a, b),
            '!=': lambda a, b: a != b,
            '<>': lambda a, b: a != b,
            '=': lambda a, b: a == b,
        }

    def switch(self, signal, a, b):
        func = self.comparators.get(signal)
        return func(a, b)
