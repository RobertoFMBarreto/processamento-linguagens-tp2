# logic_grammar.py
from logic_lexer import LogicLexer
import ply.yacc as pyacc


class LogicGrammar:

    precedence = (
        ("left", "or", "xor"),
        ("left", "and"),
        ("left", "+", "-"),
        ("left", "*", "/")
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = LogicLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_s0(self, p):
        """S : A
             | E
             | C"""
        p[0] = p[1]

    def p_c(self, p):
        """C : print E"""
        p[0] = {'op': p[1], 'args': [p[2]]}

    def p_n1(self, p):
        """N : nr """
        p[0] = p[1]

    def p_n2(self, p):
        """N : E '+' E
             | E '-' E
             | E '*' E
             | E '/' E """
        p[0] = {"op": p[2], "args": [p[1], p[3]]}

    def p_b1(self, p):
        """ B : F """
        p[0] = p[1]

    def p_b2(self, p):
        """ B : E or E
              | E and E
              | E xor E """
        p[0] = {"op": p[2], "args": [p[1], p[3]]}

    def p_f1(self, p):
        """ F : true """
        p[0] = True

    def p_f2(self, p):
        """ F : false """
        p[0] = False

    def p_f3(self, p):
        """ F : not F
              | not var """
        p[0] = {"op": 'not', "args": [p[2]]}

    def p_a1(self, p):
        """A : var '=' B
             | var '=' N"""
        p[0] = {'op': 'attrib', 'args': [{'var': p[1]}, p[3]]}

    def p_e(self, p):
        """E : N
             | B
             | var
             | '(' E ')'"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_error(self, p):
        if p:
            raise Exception(f"Syntax error: unexpected '{p.type}'")
        else:
            raise Exception("Syntax error: unexpected end of file")
