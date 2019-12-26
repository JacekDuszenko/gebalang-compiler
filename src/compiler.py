import sys

import ply.yacc as yacc

import src.parser as parser
from src.lexer import lexer
from src.util import *

parser = yacc.yacc(module=parser)
lex = lexer

if __name__ == "__main__":
    handle_wrong_input(sys.argv)
    debug = is_debug(sys.argv)
    with open(sys.argv[1]) as in_file:
        machine_code = parser.parse(lexer=lex)
        print_generated_code_to_file(machine_code, sys.argv[2])
