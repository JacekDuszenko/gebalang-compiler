import sys

from src.codegen.codegen_factory import create_code_generator
from src.lexer import lexer
from src.parser import parser
from src.sa.static_analysis import execute_static_analysis
from src.util import *

lex = lexer
yacc = parser


def compile_gebalang(code):
    ptree = yacc.parse(input=code, lexer=lex)
    declarations = execute_static_analysis(ptree)
    codegen = create_code_generator(ptree, declarations)
    vm_code = codegen.generate_vm_code()
    print(vm_code)
    return vm_code


if __name__ == "__main__":
    handle_wrong_input(sys.argv)
    with open(sys.argv[1]) as in_file:
        code = in_file.read()
        try:
            compile_gebalang(code)
        except GebalangException:
            exit(1)
