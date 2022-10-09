# logic.py
from logic_grammar import LogicGrammar
from logic_eval import LogicEval
from pprint import PrettyPrinter
import sys

pp = PrettyPrinter()

lg = LogicGrammar()
eval = LogicEval()
lg.build()

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            ans = lg.parse(contents)
            answer = eval.evaluate(ans)
            if answer is not None and type(answer) is str:
                print(f"<< {answer}")

        except Exception as e:
            print(e, file=sys.stderr)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ans = lg.parse(expr)
            # pp.pprint(ans)
            answer = eval.evaluate(ans)
            if answer is not None:
                print(f"<< {answer}")
        except Exception as e:
            print(f'\033[91m-> {e}\033[0m')





