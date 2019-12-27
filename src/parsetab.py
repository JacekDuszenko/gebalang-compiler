
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVMODASSIGN BEGIN COLON COMMA DECLARE DIV DO DOWNTO ELSE END ENDDO ENDFOR ENDIF ENDWHILE EQ FOR FROM GE GEQ ID IF LE LEQ LP MINUS MOD NEQ NUM PLUS READ RP SEMICOLON THEN TIMES TO WHILE WRITE\n    program : DECLARE declarations BEGIN commands END\n            | BEGIN commands END\n    \n    declarations : declarations COMMA ID\n                 | ID\n    \n    declarations : declarations COMMA ID LP NUM COLON NUM RP\n                 | ID LP NUM COLON NUM RP\n    \n    commands : commands command\n             | command\n    \n    command : identifier ASSIGN expression SEMICOLON\n    \n    command : IF condition THEN commands ENDIF\n    \n    command : IF condition THEN commands ELSE commands ENDIF\n    \n    command : WHILE condition DO commands ENDWHILE\n    \n    command : DO commands WHILE condition ENDDO\n    \n    command : FOR ID FROM value TO value DO commands ENDFOR\n    \n    command : FOR ID FROM value DOWNTO value DO commands ENDFOR\n    \n    command : READ identifier SEMICOLON\n    \n    command : WRITE value SEMICOLON\n    \n    expression : value\n               | value PLUS value\n               | value MINUS value\n               | value TIMES value\n               | value DIV value\n               | value MOD value\n    \n    condition : value EQ value\n              | value NEQ value\n              | value LE value\n              | value GE value\n              | value LEQ value\n              | value GEQ value\n    \n    value : NUM\n          | identifier\n    \n    identifier : ID\n    \n    identifier : ID LP ID RP\n    \n    identifier : ID LP NUM RP\n    '
    
_lr_action_items = {'DECLARE':([0,],[2,]),'BEGIN':([0,4,5,33,86,94,],[3,16,-4,-3,-6,-5,]),'$end':([1,19,51,],[0,-2,-1,]),'ID':([2,3,6,7,9,10,11,12,14,15,16,17,20,21,27,29,32,37,38,39,40,41,42,43,44,45,46,49,50,54,55,56,57,58,59,60,67,79,80,81,82,83,84,87,91,92,93,95,96,97,98,],[5,13,13,-8,13,13,13,28,13,13,13,33,-7,13,13,47,13,13,13,13,13,13,13,13,13,13,13,-16,-17,-9,13,13,13,13,13,13,13,-10,13,-12,-13,13,13,13,-11,13,13,13,13,-14,-15,]),'IF':([3,6,7,11,16,20,27,32,37,44,49,50,54,60,67,79,80,81,82,87,91,92,93,95,96,97,98,],[9,9,-8,9,9,-7,9,9,9,9,-16,-17,-9,9,9,-10,9,-12,-13,9,-11,9,9,9,9,-14,-15,]),'WHILE':([3,6,7,11,16,20,27,32,37,44,49,50,54,60,67,79,80,81,82,87,91,92,93,95,96,97,98,],[10,10,-8,10,10,-7,45,10,10,10,-16,-17,-9,10,10,-10,10,-12,-13,10,-11,10,10,10,10,-14,-15,]),'DO':([3,6,7,11,13,16,20,24,25,26,27,32,37,44,49,50,54,60,61,62,63,64,65,66,67,68,70,71,79,80,81,82,87,88,89,91,92,93,95,96,97,98,],[11,11,-8,11,-32,11,-7,-30,-31,44,11,11,11,11,-16,-17,-9,11,-24,-25,-26,-27,-28,-29,11,44,-33,-34,-10,11,-12,-13,11,92,93,-11,11,11,11,11,-14,-15,]),'FOR':([3,6,7,11,16,20,27,32,37,44,49,50,54,60,67,79,80,81,82,87,91,92,93,95,96,97,98,],[12,12,-8,12,12,-7,12,12,12,12,-16,-17,-9,12,12,-10,12,-12,-13,12,-11,12,12,12,12,-14,-15,]),'READ':([3,6,7,11,16,20,27,32,37,44,49,50,54,60,67,79,80,81,82,87,91,92,93,95,96,97,98,],[14,14,-8,14,14,-7,14,14,14,14,-16,-17,-9,14,14,-10,14,-12,-13,14,-11,14,14,14,14,-14,-15,]),'WRITE':([3,6,7,11,16,20,27,32,37,44,49,50,54,60,67,79,80,81,82,87,91,92,93,95,96,97,98,],[15,15,-8,15,15,-7,15,15,15,15,-16,-17,-9,15,15,-10,15,-12,-13,15,-11,15,15,15,15,-14,-15,]),'COMMA':([4,5,33,86,94,],[17,-4,-3,-6,-5,]),'LP':([5,13,33,],[18,29,52,]),'END':([6,7,20,32,49,50,54,79,81,82,91,97,98,],[19,-8,-7,51,-16,-17,-9,-10,-12,-13,-11,-14,-15,]),'ENDIF':([7,20,49,50,54,60,79,81,82,87,91,97,98,],[-8,-7,-16,-17,-9,79,-10,-12,-13,91,-11,-14,-15,]),'ELSE':([7,20,49,50,54,60,79,81,82,91,97,98,],[-8,-7,-16,-17,-9,80,-10,-12,-13,-11,-14,-15,]),'ENDWHILE':([7,20,49,50,54,67,79,81,82,91,97,98,],[-8,-7,-16,-17,-9,81,-10,-12,-13,-11,-14,-15,]),'ENDFOR':([7,20,49,50,54,79,81,82,91,95,96,97,98,],[-8,-7,-16,-17,-9,-10,-12,-13,-11,97,98,-14,-15,]),'ASSIGN':([8,13,70,71,],[21,-32,-33,-34,]),'NUM':([9,10,15,18,21,29,38,39,40,41,42,43,45,46,52,53,55,56,57,58,59,83,84,85,],[24,24,24,34,24,48,24,24,24,24,24,24,24,24,72,73,24,24,24,24,24,24,24,90,]),'EQ':([13,23,24,25,70,71,],[-32,38,-30,-31,-33,-34,]),'NEQ':([13,23,24,25,70,71,],[-32,39,-30,-31,-33,-34,]),'LE':([13,23,24,25,70,71,],[-32,40,-30,-31,-33,-34,]),'GE':([13,23,24,25,70,71,],[-32,41,-30,-31,-33,-34,]),'LEQ':([13,23,24,25,70,71,],[-32,42,-30,-31,-33,-34,]),'GEQ':([13,23,24,25,70,71,],[-32,43,-30,-31,-33,-34,]),'SEMICOLON':([13,24,25,30,31,35,36,70,71,74,75,76,77,78,],[-32,-30,-31,49,50,54,-18,-33,-34,-19,-20,-21,-22,-23,]),'PLUS':([13,24,25,36,70,71,],[-32,-30,-31,55,-33,-34,]),'MINUS':([13,24,25,36,70,71,],[-32,-30,-31,56,-33,-34,]),'TIMES':([13,24,25,36,70,71,],[-32,-30,-31,57,-33,-34,]),'DIV':([13,24,25,36,70,71,],[-32,-30,-31,58,-33,-34,]),'MOD':([13,24,25,36,70,71,],[-32,-30,-31,59,-33,-34,]),'THEN':([13,22,24,25,61,62,63,64,65,66,70,71,],[-32,37,-30,-31,-24,-25,-26,-27,-28,-29,-33,-34,]),'ENDDO':([13,24,25,61,62,63,64,65,66,68,70,71,],[-32,-30,-31,-24,-25,-26,-27,-28,-29,82,-33,-34,]),'TO':([13,24,25,69,70,71,],[-32,-30,-31,83,-33,-34,]),'DOWNTO':([13,24,25,69,70,71,],[-32,-30,-31,84,-33,-34,]),'FROM':([28,],[46,]),'COLON':([34,72,],[53,85,]),'RP':([47,48,73,90,],[70,71,86,94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([2,],[4,]),'commands':([3,11,16,37,44,80,92,93,],[6,27,32,60,67,87,95,96,]),'command':([3,6,11,16,27,32,37,44,60,67,80,87,92,93,95,96,],[7,20,7,7,20,20,7,7,20,20,7,20,7,7,20,20,]),'identifier':([3,6,9,10,11,14,15,16,21,27,32,37,38,39,40,41,42,43,44,45,46,55,56,57,58,59,60,67,80,83,84,87,92,93,95,96,],[8,8,25,25,8,30,25,8,25,8,8,8,25,25,25,25,25,25,8,25,25,25,25,25,25,25,8,8,8,25,25,8,8,8,8,8,]),'condition':([9,10,45,],[22,26,68,]),'value':([9,10,15,21,38,39,40,41,42,43,45,46,55,56,57,58,59,83,84,],[23,23,31,36,61,62,63,64,65,66,23,69,74,75,76,77,78,88,89,]),'expression':([21,],[35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> DECLARE declarations BEGIN commands END','program',5,'p_program','parserules.py',18),
  ('program -> BEGIN commands END','program',3,'p_program','parserules.py',19),
  ('declarations -> declarations COMMA ID','declarations',3,'p_declarations_variables','parserules.py',29),
  ('declarations -> ID','declarations',1,'p_declarations_variables','parserules.py',30),
  ('declarations -> declarations COMMA ID LP NUM COLON NUM RP','declarations',8,'p_declarations_arrays','parserules.py',40),
  ('declarations -> ID LP NUM COLON NUM RP','declarations',6,'p_declarations_arrays','parserules.py',41),
  ('commands -> commands command','commands',2,'p_commands','parserules.py',51),
  ('commands -> command','commands',1,'p_commands','parserules.py',52),
  ('command -> identifier ASSIGN expression SEMICOLON','command',4,'p_command_assign','parserules.py',62),
  ('command -> IF condition THEN commands ENDIF','command',5,'p_command_if_then','parserules.py',69),
  ('command -> IF condition THEN commands ELSE commands ENDIF','command',7,'p_command_if_then_else','parserules.py',76),
  ('command -> WHILE condition DO commands ENDWHILE','command',5,'p_command_while','parserules.py',83),
  ('command -> DO commands WHILE condition ENDDO','command',5,'p_command_do_while','parserules.py',90),
  ('command -> FOR ID FROM value TO value DO commands ENDFOR','command',9,'p_command_for_up_to','parserules.py',97),
  ('command -> FOR ID FROM value DOWNTO value DO commands ENDFOR','command',9,'p_command_for_down_to','parserules.py',104),
  ('command -> READ identifier SEMICOLON','command',3,'p_command_read','parserules.py',111),
  ('command -> WRITE value SEMICOLON','command',3,'p_command_write','parserules.py',118),
  ('expression -> value','expression',1,'p_expression','parserules.py',125),
  ('expression -> value PLUS value','expression',3,'p_expression','parserules.py',126),
  ('expression -> value MINUS value','expression',3,'p_expression','parserules.py',127),
  ('expression -> value TIMES value','expression',3,'p_expression','parserules.py',128),
  ('expression -> value DIV value','expression',3,'p_expression','parserules.py',129),
  ('expression -> value MOD value','expression',3,'p_expression','parserules.py',130),
  ('condition -> value EQ value','condition',3,'p_condition','parserules.py',140),
  ('condition -> value NEQ value','condition',3,'p_condition','parserules.py',141),
  ('condition -> value LE value','condition',3,'p_condition','parserules.py',142),
  ('condition -> value GE value','condition',3,'p_condition','parserules.py',143),
  ('condition -> value LEQ value','condition',3,'p_condition','parserules.py',144),
  ('condition -> value GEQ value','condition',3,'p_condition','parserules.py',145),
  ('value -> NUM','value',1,'p_number','parserules.py',152),
  ('value -> identifier','value',1,'p_number','parserules.py',153),
  ('identifier -> ID','identifier',1,'p_identifier_variable','parserules.py',160),
  ('identifier -> ID LP ID RP','identifier',4,'p_identifier_array_variable','parserules.py',167),
  ('identifier -> ID LP NUM RP','identifier',4,'p_identifier_array_num','parserules.py',174),
]
