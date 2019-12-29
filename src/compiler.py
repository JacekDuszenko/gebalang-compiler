import sys

from src.codegen.codegen_factory import create_code_generator
from src.lexer import lexer
from src.parser import parser
from src.sa.static_analysis import execute_static_analysis
from src.util import *

lex = lexer
yacc = parser


def compile_gebalang(code, debug=False):
    ptree = yacc.parse(input=code, lexer=lex)
    execute_static_analysis(ptree)
    codegen = create_code_generator(ptree)
    code = codegen.generate_vm_code()
    print(code)


if __name__ == "__main__":
    handle_wrong_input(sys.argv)
    debug = is_debug(sys.argv)
    with open(sys.argv[1]) as in_file:
        gebalang_code = in_file.read()
        try:
            compile_gebalang(gebalang_code, debug)
        except GebalangException:
            exit(1)
