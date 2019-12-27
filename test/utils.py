from src.error.GebalangException import GebalangException
from src.lexer import lexer
from src.parser import parser


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

