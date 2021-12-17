
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftorxorleftandleft+-left*/and false for not nr or print true var xorS : A\n             | E\n             | CC : print EN : nr N : E '+' E\n             | E '-' E\n             | E '*' E\n             | E '/' E  B : F  B : E or E\n              | E and E\n              | E xor E  F : true  F : false  F : not F\n              | not var A : var '=' B\n             | var '=' NE : N\n             | B\n             | var\n             | '(' E ')'"
    
_lr_action_items = {'var':([0,8,9,14,15,16,17,18,19,20,21,22,],[5,24,24,27,24,24,24,24,24,24,24,24,]),'(':([0,8,9,15,16,17,18,19,20,21,22,],[8,8,8,8,8,8,8,8,8,8,8,]),'print':([0,],[9,]),'nr':([0,8,9,15,16,17,18,19,20,21,22,],[10,10,10,10,10,10,10,10,10,10,10,]),'true':([0,8,9,14,15,16,17,18,19,20,21,22,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'false':([0,8,9,14,15,16,17,18,19,20,21,22,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'not':([0,8,9,14,15,16,17,18,19,20,21,22,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,2,3,4,5,6,7,10,11,12,13,24,25,26,27,28,29,30,31,32,33,34,35,36,38,],[0,-1,-2,-3,-22,-21,-20,-5,-10,-14,-15,-22,-4,-16,-17,-6,-7,-8,-9,-11,-12,-13,-18,-19,-23,]),'+':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[15,-22,-21,-20,-5,-10,-14,-15,15,-22,15,-16,-17,-6,-7,-8,-9,15,15,15,-21,-20,15,-23,]),'-':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[16,-22,-21,-20,-5,-10,-14,-15,16,-22,16,-16,-17,-6,-7,-8,-9,16,16,16,-21,-20,16,-23,]),'*':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[17,-22,-21,-20,-5,-10,-14,-15,17,-22,17,-16,-17,17,17,-8,-9,17,17,17,-21,-20,17,-23,]),'/':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[18,-22,-21,-20,-5,-10,-14,-15,18,-22,18,-16,-17,18,18,-8,-9,18,18,18,-21,-20,18,-23,]),'or':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[19,-22,-21,-20,-5,-10,-14,-15,19,-22,19,-16,-17,-6,-7,-8,-9,-11,-12,-13,-21,-20,19,-23,]),'and':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[20,-22,-21,-20,-5,-10,-14,-15,20,-22,20,-16,-17,-6,-7,-8,-9,20,-12,20,-21,-20,20,-23,]),'xor':([3,5,6,7,10,11,12,13,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[21,-22,-21,-20,-5,-10,-14,-15,21,-22,21,-16,-17,-6,-7,-8,-9,-11,-12,-13,-21,-20,21,-23,]),'=':([5,],[22,]),')':([6,7,10,11,12,13,23,24,26,27,28,29,30,31,32,33,34,38,],[-21,-20,-5,-10,-14,-15,38,-22,-16,-17,-6,-7,-8,-9,-11,-12,-13,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'A':([0,],[2,]),'E':([0,8,9,15,16,17,18,19,20,21,22,],[3,23,25,28,29,30,31,32,33,34,37,]),'C':([0,],[4,]),'B':([0,8,9,15,16,17,18,19,20,21,22,],[6,6,6,6,6,6,6,6,6,6,35,]),'N':([0,8,9,15,16,17,18,19,20,21,22,],[7,7,7,7,7,7,7,7,7,7,36,]),'F':([0,8,9,14,15,16,17,18,19,20,21,22,],[11,11,11,26,11,11,11,11,11,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> A','S',1,'p_s0','logic_grammar.py',31),
  ('S -> E','S',1,'p_s0','logic_grammar.py',32),
  ('S -> C','S',1,'p_s0','logic_grammar.py',33),
  ('C -> print E','C',2,'p_c','logic_grammar.py',37),
  ('N -> nr','N',1,'p_n1','logic_grammar.py',41),
  ('N -> E + E','N',3,'p_n2','logic_grammar.py',45),
  ('N -> E - E','N',3,'p_n2','logic_grammar.py',46),
  ('N -> E * E','N',3,'p_n2','logic_grammar.py',47),
  ('N -> E / E','N',3,'p_n2','logic_grammar.py',48),
  ('B -> F','B',1,'p_b1','logic_grammar.py',52),
  ('B -> E or E','B',3,'p_b2','logic_grammar.py',56),
  ('B -> E and E','B',3,'p_b2','logic_grammar.py',57),
  ('B -> E xor E','B',3,'p_b2','logic_grammar.py',58),
  ('F -> true','F',1,'p_f1','logic_grammar.py',62),
  ('F -> false','F',1,'p_f2','logic_grammar.py',66),
  ('F -> not F','F',2,'p_f3','logic_grammar.py',70),
  ('F -> not var','F',2,'p_f3','logic_grammar.py',71),
  ('A -> var = B','A',3,'p_a1','logic_grammar.py',75),
  ('A -> var = N','A',3,'p_a1','logic_grammar.py',76),
  ('E -> N','E',1,'p_e','logic_grammar.py',80),
  ('E -> B','E',1,'p_e','logic_grammar.py',81),
  ('E -> var','E',1,'p_e','logic_grammar.py',82),
  ('E -> ( E )','E',3,'p_e','logic_grammar.py',83),
]