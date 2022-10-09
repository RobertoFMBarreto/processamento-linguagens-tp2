# logic_grammar.py
from logic_lexer import LogicLexer
import ply.yacc as pyacc


class LogicGrammar:

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

    def p_code0(self, p):
        """ code : S ';'
                 | S """
        p[0] = [p[1]]

    def p_code1(self, p):
        """ code : code S ';' """
        p[0] = p[1]
        p[0].append(p[2])

    def p_s0(self, p):
        """ S : command
              | sel_queries """
        p[0] = p[1]

    def p_command0(self, p):
        """ command : PROCEDURE str DO code END """
        p[0] = {'command': p[1], 'args': [{'str': p[2]}], 'code': p[4]}

    def p_command1(self, p):
        """ command : LOAD TABLE A FROM A
              | CREATE TABLE A FROM A
              | SAVE TABLE A AS A """
        p[0] = {'command': p[1], 'args': [p[3], p[5]]}

    def p_command2(self, p):
        """ command : DISCARD TABLE A
              | SHOW TABLE A """
        p[0] = {'command': p[1], 'args': [p[3]]}

    def p_command3(self, p):
        """ command : CREATE TABLE A FROM sel_queries """
        p[0] = {'command': p[1], 'args': [p[3], p[5]]}

    def p_command4(self, p):
        """ command : CREATE TABLE A FROM A JOIN J """
        p[7].append(p[5])
        p[0] = {'command': p[1], 'args': [p[3], {'join': p[7]}]}

    def p_command5(self, p):
        """ command : CALL str """
        p[0] = {'command': 'CALL', 'args': [{'str': p[2]}]}

    def p_command6(self, p):
        """ command : CREATE TABLE A ATTRIBUTES a_list """
        p[0] = {'command': p[1], 'args': [p[3], {'list': p[5]}]}

    def p_command7(self, p):
        """ command : INSERT a_list INTO A"""
        p[0] = {'command': p[1], 'args': [{'list': p[2]}, p[4]]}

    def p_sel_queries0(self, p):
        """ sel_queries : SELECT a_list FROM A lim """
        p[0] = {'command': p[1], 'args': [{'str': p[2]}, p[4]], 'lim': p[5]}

    def p_sel_queries1(self, p):
        """ sel_queries : SELECT a_list FROM A WHERE cond_list lim """
        p[0] = {'command': p[1], 'args': [
            {'str': p[2]}, p[4], {'list': p[6]}], 'lim': p[7]}

    def p_a(self, p):
        """ A : str
              | nr
              | string """
        p[0] = p[1]

    def p_e(self, p):
        """ E : A comparator A """
        p[0] = [p[1], p[2], p[3]]

    def p_cond_list(self, p):
        """ cond_list : E
                      | cond_list AND E """
        if len(p) == 4:
            p[0] = p[1]
            p[0].append(p[3])
        else:
            p[0] = [p[1]]

    def p_lim(self, p):
        """ lim :
                | LIMIT nr"""
        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = ''

    def p_a_list(self, p):
        """ a_list : A
                    | a_list ',' A """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[3])

    def p_j(self, p):
        """ J : A USING '(' A ')' """
        p[0] = [p[1], p[4]]

    def p_error(self, p):
        if p:
            raise Exception(f"Syntax error: unexpected '{p.type}' -> {p}")
        else:
            raise Exception("Syntax error: unexpected end of file")
