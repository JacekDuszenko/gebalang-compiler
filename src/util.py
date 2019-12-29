import logging

from src.error.GebalangException import GebalangException

LLMAX = 2 ** 63 - 1
LLMIN = - 2 ** 63


def print_usage():
    print("""
        Usage: compiler.py INPUT_FILE OUTPUT_FILE [ -d ]
    """)


def is_debug(argv):
    return len(argv) == 4 and argv[3] is '-d'


def handle_wrong_input(argv):
    if len(argv) < 3:
        print_usage()
        exit(1)


def print_generated_code_to_file(code, filename):
    with open(filename, mode='w') as out_file:
        for line in code:
            out_file.write(line + '\n')


def error(line_number, error_message):
    print(format_error(line_number, error_message))
    raise GebalangException()


def format_error(line_number, error_message):
    return "Error in line: {}. Message: {}".format(line_number, error_message)


def is_in_range(number):
    return LLMIN <= number <= LLMAX


def create_not_in_range_message(number):
    return 'Number {} is not in range. It must be between LLMAX(2^63 - 1) and LLMIN(-2^63)'.format(number)


def pp(clas, indent=0):
    print(' ' * indent + type(clas).__name__ + ':')
    indent += 4
    if isinstance(clas, list):
        for i, elem in enumerate(clas):
            execute_printing(indent, i, elem)
    else:
        for k, v in clas.__dict__.items():
            execute_printing(indent, k, v)


def execute_printing(indent, k, v):
    if isinstance(v, list) and not isinstance(v[0], bool):
        for elem in v:
            pp(elem, indent)
    elif '__dict__' in dir(v):
        pp(v, indent)
    else:
        print(' ' * indent + k + ': ' + str(v))

