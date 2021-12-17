# logic_lexer.py
import ply.lex as plex


class LogicLexer:
    tokens = ("not", "and", "or", "true", "false", "xor", "var", "nr", "print", "for")
    literals = ['(', ')', '=', '+', '-', '*', '/', '[', ']', '{','}',',']
    t_ignore = " "

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def t_str(self, t):
        r"not|true|false|and|or|xor|print|for"
        t.type = t.value
        return t

    def t_var(self, t):
        r"[a-z_]+"
        return t

    def t_nr(self, t):
        r"[0-9]+(\.[0-9]+)?"
        t.value = float(t.value)
        return t

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type

    def t_error(self, t):
        print(t)
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)

