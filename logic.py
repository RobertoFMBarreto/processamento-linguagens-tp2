# logic.py
from logic_grammar import LogicGrammar
from logic_eval import LogicEval
from pprint import PrettyPrinter

pp = PrettyPrinter()

lg = LogicGrammar()
lg.build()

for expr in iter(lambda: input(">> "), ""):
    try:
        ans = lg.parse(expr)
        pp.pprint(ans)
        answer = LogicEval.evaluate(ans)
        if answer is not None:
            print(f"<< {answer}")
    except Exception as e:
        print(f'\033[91m-> {e}\033[0m')


