import pytest

from src.error.GebalangException import GebalangException
from src.lexer import lexer
from test.utils import *


class TestNumberRanges:
    def test_number_range_ok(self):
        simple_program_string = """
        DECLARE a BEGIN
        a ASSIGN 500;
        END
        """
        token_list = lex_to_token_list(lexer, simple_program_string)
        valid = ['DECLARE', 'ID', 'BEGIN', 'ID', 'ASSIGN', 'NUM', 'SEMICOLON', 'END']
        valid_string = remove_whitespace("DECLAREaBEGINaASSIGN500;END")
        for i, t in enumerate(token_list):
            assert t.type == valid[i]
        assert valid_string == lex_to_string(lexer, simple_program_string)

    def test_number_range_too_large(self):
        max_number = 2 ** 63 - 1
        overflow_number = max_number + 1
        simple_program_string = """
               DECLARE a BEGIN
               a ASSIGN {};
               END
               """.format(overflow_number)
        with pytest.raises(GebalangException):
            lex_to_token_list(lexer, simple_program_string)

    def test_number_range_too_small(self):
        min_number = -2 ** 63
        underflow_number = min_number -1
        simple_program_string = """
                  DECLARE a BEGIN
                  a ASSIGN {};
                  END
                  """.format(underflow_number)
        with pytest.raises(GebalangException):
            lex_to_token_list(lexer, simple_program_string)