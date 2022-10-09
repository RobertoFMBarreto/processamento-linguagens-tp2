# logic_lexer.py
import ply.lex as plex


class LogicLexer:
    tokens = ("LOAD", "DISCARD", "SAVE", "SHOW", "TABLE", "FROM", "SELECT", "CREATE", "USING", "JOIN", "LIMIT",
              "PROCEDURE", "DO", "END", "WHERE", "AS", "AND", "str", "comparator", "nr", "string", "CALL", "ATTRIBUTES",
              "INSERT", "INTO")
    literals = [',', '(', ')', ';']
    t_ignore = " \"\n\t"

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def t_command(self, t):
        r"""LOAD|DISCARD|SAVE|SHOW|TABLE|FROM|AS|SELECT|WHERE|AND|CREATE|USING|JOIN
        |LIMIT|PROCEDURE|DO|END|CALL|ATTRIBUTES|INSERT|INTO"""
        t.type = t.value
        return t

    def t_comments(self, t):
        r"--.*\n"
        pass

    def t_string(self, t):
        r'"[^\.]+\.[^"]+"'
        t.value = {"str": t.value[1:-1]}
        return t

    def t_nr(self, t):
        r"""[0-9]+(.[0-9]+)?"""
        try:
            t.value = float(t.value)
        except ValueError:
            pass
        return t

    def t_str(self, t):
        r"""[a-zA-Z0-9\._]+|\*"""
        return t

    def t_comparator(self, t):
        r"""<=|>=|!=|<>|<|>|="""
        return t

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
