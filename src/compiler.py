import sys

from src.lexer import lexer
from src.parser import parser
from src.util import *

lex = lexer
yacc = parser


def compile():
    program = yacc.parse(input=gebalang_code, lexer=lex)
    pretty_print(program)


if __name__ == "__main__":
    handle_wrong_input(sys.argv)
    debug = is_debug(sys.argv)
    with open(sys.argv[1]) as in_file:
        gebalang_code = in_file.read()
        try:
            compile()
        except GebalangException:
            exit(1)