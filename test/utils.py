import os
import random
import string
import subprocess
import time

from src.codegen.codegen_factory import create_code_generator
from src.lexer import lexer
from src.parser import parser
from src.sa.static_analysis import execute_static_analysis

ptaszek_with_space = '> '


def lex_to_token_list(lex, code):
    reset_and_start_lexer(lex, code)
    return [t for t in lex]


def lex_to_string(lex, code):
    s = ""
    reset_and_start_lexer(lex, code)
    for t in lex:
        s += str(t.value)
    return s


def reset_and_start_lexer(lex, code):
    lex.input(code)


def remove_whitespace(simple_program_string):
    return "".join(simple_program_string.split())


def parse(string_to_parse):
    return parser.parse(input=string_to_parse, lexer=lexer)


def write_vm_code_to_file(vm_code):
    def random_name():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))

    d = '../'
    filename = d + random_name()
    with open(filename, 'w') as file:
        file.write(vm_code)

    while not os.path.exists(filename):
        time.sleep(0.1)
    return filename


def run_vm(simple_program_string, input=None, delete_assembly=True):
    ptree = parse(simple_program_string)
    globals = execute_static_analysis(ptree)
    codegen = create_code_generator(ptree, globals)
    vm_code = codegen.generate_vm_code()
    filename = write_vm_code_to_file(vm_code)
    ps = subprocess.run(['../maszyna-wirtualna', filename], capture_output=True, input=input)
    if delete_assembly:
        os.remove(filename)
    lines = [l.decode('utf-8') for l in ps.stdout.split(b'\n')]
    output_lines = []
    for l in lines:
        extract_output(l, output_lines)

    return output_lines, ps.stderr, vm_code


def extract_output(line, result_list):
    after_pt = line.split(ptaszek_with_space, 1)
    if len(after_pt) >= 2:
        sub = after_pt[1].split('\n', 1)
        if len(sub) >= 1:
            result_list.append(sub[0])

