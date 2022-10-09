# logic.py
from logic_grammar import LogicGrammar
from logic_eval import LogicEval
from pprint import PrettyPrinter
import sys

pp = PrettyPrinter()

lg = LogicGrammar()
eval = LogicEval()
lg.build()
tests = ['LOAD TABLE produtos FROM "produtos.csv" ;',
         'LOAD TABLE vendas FROM "vendas.csv" ;',
         'SAVE TABLE produtos AS "produtos2.csv" ;',
         'SHOW TABLE produtos ;',
         'SELECT * FROM produtos ;',
         '-- selecionar produtos\n SELECT * FROM produtos ;',
         'SELECT * FROM vendas WHERE Qt >= 10 AND Qt < 11 ;',
         'SELECT ID,Descricao FROM produtos ;',
         'SELECT ID,Descricao FROM produtos WHERE Descricao="Pipocas" ;',
         'SELECT ID,Preco FROM produtos WHERE Descricao="Pipocas" ;',
         '-- teste erro where sem condições\nSELECT * FROM vendas WHERE ;',
         '-- teste erro nada no select\nSELECT  FROM vendas ;',
         'CREATE TABLE prod2 FROM produtos ;',
         '-- teste erro criar tabela existente\nCREATE TABLE prod2 FROM produtos ;',
         'SELECT * FROM prod2 ;',
         '-- teste erro col não existente\nCREATE TABLE tudo FROM vendas JOIN produtos USING(IDsds) ;',
         'PROCEDURE atualizar_vendas DO CREATE TABLE mais_vendidos FROM SELECT * FROM vendas WHERE Qt > 50 ; CREATE TABLE tudo FROM vendas JOIN produtos USING(ID) ; END',
         'CALL atualizar_vendas',
         'SELECT * FROM tudo ;',
         'SELECT * FROM tudo LIMIT 1;',
         'SELECT * FROM mais_vendidos ;',
         'CREATE TABLE teste ATTRIBUTES testeCol1, testeCol2',
         'SELECT * FROM teste',
         'INSERT atum, atum2 INTO teste',
         'SELECT * FROM teste',
         '-- teste erro tabela não existente\nINSERT atum, atum2 INTO teste2',
         '-- teste erro poucos valores\nINSERT atum INTO teste',
         '-- teste erro muitos valores\nINSERT atum, atum2, atum3 INTO teste',
         'DISCARD TABLE produtos ;',
         ]


for expr in tests:
    try:
        print(f'>>\033[96m {expr}\033[0m')
        ans = lg.parse(expr)
        answer = eval.evaluate(ans)
        if answer is not None and type(answer) is str:
            print(f"<< {answer}")
    except Exception as e:
        print(f'\033[91m-> {e}\033[0m')
