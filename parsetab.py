
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND AS ATTRIBUTES CALL CREATE DISCARD DO END FROM INSERT INTO JOIN LIMIT LOAD PROCEDURE SAVE SELECT SHOW TABLE USING WHERE comparator nr str string code : S ';'\n                 | S  code : code S ';'  S : command\n              | sel_queries  command : PROCEDURE str DO code END  command : LOAD TABLE A FROM A\n              | CREATE TABLE A FROM A\n              | SAVE TABLE A AS A  command : DISCARD TABLE A\n              | SHOW TABLE A  command : CREATE TABLE A FROM sel_queries  command : CREATE TABLE A FROM A JOIN J  command : CALL str  command : CREATE TABLE A ATTRIBUTES a_list  command : INSERT a_list INTO A sel_queries : SELECT a_list FROM A lim  sel_queries : SELECT a_list FROM A WHERE cond_list lim  A : str\n              | nr\n              | string  E : A comparator A  cond_list : E\n                      | cond_list AND E  lim :\n                | LIMIT nr a_list : A\n                    | a_list ',' A  J : A USING '(' A ')' "
    
_lr_action_items = {'PROCEDURE':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[5,5,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,5,-10,-11,5,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'LOAD':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[6,6,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,6,-10,-11,6,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'CREATE':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[7,7,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,7,-10,-11,7,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'SAVE':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[8,8,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,8,-10,-11,8,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'DISCARD':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[9,9,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,9,-10,-11,9,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'SHOW':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[10,10,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,10,-10,-11,10,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'CALL':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[11,11,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,11,-10,-11,11,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'INSERT':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[12,12,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,12,-10,-11,12,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'SELECT':([0,1,2,3,4,15,22,24,25,26,27,29,30,34,35,39,41,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[13,13,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,13,-10,-11,13,13,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'$end':([1,2,3,4,15,22,24,25,26,27,29,34,35,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[0,-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,-10,-11,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),';':([2,3,4,14,22,24,25,26,27,34,35,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[15,-4,-5,29,-14,-27,-19,-20,-21,-10,-11,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'END':([2,3,4,15,22,24,25,26,27,29,34,35,39,44,45,46,47,48,49,50,51,52,53,58,59,60,62,64,67,68,71,],[-2,-4,-5,-1,-14,-27,-19,-20,-21,-3,-10,-11,47,-16,-28,-25,-6,-7,-8,-12,-15,-9,-17,-25,-23,-26,-13,-18,-22,-24,-29,]),'str':([5,11,12,13,17,18,19,20,21,36,37,38,40,41,42,43,54,56,63,65,69,],[16,22,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'TABLE':([6,7,8,9,10,],[17,18,19,20,21,]),'nr':([12,13,17,18,19,20,21,36,37,38,40,41,42,43,54,55,56,63,65,69,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,60,26,26,26,26,]),'string':([12,13,17,18,19,20,21,36,37,38,40,41,42,43,54,56,63,65,69,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DO':([16,],[30,]),'INTO':([23,24,25,26,27,45,],[36,-27,-19,-20,-21,-28,]),',':([23,24,25,26,27,28,45,51,],[37,-27,-19,-20,-21,37,-28,37,]),'FROM':([24,25,26,27,28,31,32,45,],[-27,-19,-20,-21,38,40,41,-28,]),'ATTRIBUTES':([25,26,27,32,],[-19,-20,-21,42,]),'AS':([25,26,27,33,],[-19,-20,-21,43,]),'WHERE':([25,26,27,46,],[-19,-20,-21,54,]),'LIMIT':([25,26,27,46,58,59,67,68,],[-19,-20,-21,55,55,-23,-22,-24,]),'JOIN':([25,26,27,49,],[-19,-20,-21,56,]),'comparator':([25,26,27,57,],[-19,-20,-21,63,]),'USING':([25,26,27,61,],[-19,-20,-21,66,]),'AND':([25,26,27,58,59,67,68,],[-19,-20,-21,65,-23,-22,-24,]),')':([25,26,27,70,],[-19,-20,-21,71,]),'(':([66,],[69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,30,],[1,39,]),'S':([0,1,30,39,],[2,14,2,14,]),'command':([0,1,30,39,],[3,3,3,3,]),'sel_queries':([0,1,30,39,41,],[4,4,4,4,50,]),'a_list':([12,13,42,],[23,28,51,]),'A':([12,13,17,18,19,20,21,36,37,38,40,41,42,43,54,56,63,65,69,],[24,24,31,32,33,34,35,44,45,46,48,49,24,52,57,61,67,57,70,]),'lim':([46,58,],[53,64,]),'cond_list':([54,],[58,]),'E':([54,65,],[59,68,]),'J':([56,],[62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> S ;','code',2,'p_code0','logic_grammar.py',24),
  ('code -> S','code',1,'p_code0','logic_grammar.py',25),
  ('code -> code S ;','code',3,'p_code1','logic_grammar.py',29),
  ('S -> command','S',1,'p_s0','logic_grammar.py',34),
  ('S -> sel_queries','S',1,'p_s0','logic_grammar.py',35),
  ('command -> PROCEDURE str DO code END','command',5,'p_command0','logic_grammar.py',39),
  ('command -> LOAD TABLE A FROM A','command',5,'p_command1','logic_grammar.py',43),
  ('command -> CREATE TABLE A FROM A','command',5,'p_command1','logic_grammar.py',44),
  ('command -> SAVE TABLE A AS A','command',5,'p_command1','logic_grammar.py',45),
  ('command -> DISCARD TABLE A','command',3,'p_command2','logic_grammar.py',49),
  ('command -> SHOW TABLE A','command',3,'p_command2','logic_grammar.py',50),
  ('command -> CREATE TABLE A FROM sel_queries','command',5,'p_command3','logic_grammar.py',54),
  ('command -> CREATE TABLE A FROM A JOIN J','command',7,'p_command4','logic_grammar.py',58),
  ('command -> CALL str','command',2,'p_command5','logic_grammar.py',63),
  ('command -> CREATE TABLE A ATTRIBUTES a_list','command',5,'p_command6','logic_grammar.py',67),
  ('command -> INSERT a_list INTO A','command',4,'p_command7','logic_grammar.py',71),
  ('sel_queries -> SELECT a_list FROM A lim','sel_queries',5,'p_sel_queries0','logic_grammar.py',75),
  ('sel_queries -> SELECT a_list FROM A WHERE cond_list lim','sel_queries',7,'p_sel_queries1','logic_grammar.py',79),
  ('A -> str','A',1,'p_a','logic_grammar.py',84),
  ('A -> nr','A',1,'p_a','logic_grammar.py',85),
  ('A -> string','A',1,'p_a','logic_grammar.py',86),
  ('E -> A comparator A','E',3,'p_e','logic_grammar.py',90),
  ('cond_list -> E','cond_list',1,'p_cond_list','logic_grammar.py',94),
  ('cond_list -> cond_list AND E','cond_list',3,'p_cond_list','logic_grammar.py',95),
  ('lim -> <empty>','lim',0,'p_lim','logic_grammar.py',103),
  ('lim -> LIMIT nr','lim',2,'p_lim','logic_grammar.py',104),
  ('a_list -> A','a_list',1,'p_a_list','logic_grammar.py',111),
  ('a_list -> a_list , A','a_list',3,'p_a_list','logic_grammar.py',112),
  ('J -> A USING ( A )','J',5,'p_j','logic_grammar.py',120),
]
