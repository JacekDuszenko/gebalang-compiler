import ply.yacc as yacc

import src.parserules as parserules

parser = yacc.yacc(module=parserules)
