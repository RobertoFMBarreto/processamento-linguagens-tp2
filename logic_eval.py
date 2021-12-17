# logic_eval

def xor(a, b):
    return (a or b) and not (a and b)


class LogicEval:
    symbols = {}

    # Design Pattern: Dispatch Table
    operators = {
        "or": lambda args: args[0] or args[1],
        "not": lambda args: not args[0],
        "xor": lambda args: xor(args[0],args[1]),
        "and": lambda args: args[0] and args[1],
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "attrib": lambda args: LogicEval._attrib(args),
        "print": lambda args: print(args[0])
    }

    @staticmethod
    def _attrib(args):
        value = args[1]
        LogicEval.symbols[args[0]] = value
        return None

    @staticmethod
    def evaluate(ast):
        if type(ast) in (bool, float):
            return ast
        if type(ast) is dict:
            return LogicEval._eval_operator(ast)
        if type(ast) is str:
            var = ast
            if var in LogicEval.symbols:
                return LogicEval.symbols[ast]
            raise Exception(f"Undefined variable: {var}")

        raise Exception("Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = [LogicEval.evaluate(a) for a in ast['args']]
            if op in LogicEval.operators:
                func = LogicEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")
        if 'var' in ast:
            return ast['var']
        raise Exception('Invalid AST')
