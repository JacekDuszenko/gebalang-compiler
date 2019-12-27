import pytest

from src.error.GebalangException import GebalangException
from src.lexer import lexer
from test.utils import *


class TestSanityCheck:
    def test_lex_positive_number(self):
        simple_program_string = """
        DECLARE a,b BEGIN
        a ASSIGN 5
        b ASSIGN a
        END
        """
        token_list = lex_to_token_list(lexer, simple_program_string)
        valid = ['DECLARE', 'ID', 'COMMA', 'ID', 'BEGIN', 'ID', 'ASSIGN', 'NUM', 'ID', 'ASSIGN', 'ID', 'END']
        valid_string = remove_whitespace(simple_program_string)
        for i, t in enumerate(token_list):
            assert t.type == valid[i]
        assert valid_string == lex_to_string(lexer, simple_program_string)

    def test_lex_negative_number(self):
        simple_program_string = """
            DECLARE a,b BEGIN
            a ASSIGN -5;
            b ASSIGN a;
            END
            """
        token_list = lex_to_token_list(lexer, simple_program_string)
        valid = ['DECLARE', 'ID', 'COMMA', 'ID', 'BEGIN', 'ID', 'ASSIGN', 'NUM', 'SEMICOLON', 'ID', 'ASSIGN', 'ID',
                 'SEMICOLON', 'END']
        valid_string = remove_whitespace(simple_program_string)
        for i, t in enumerate(token_list):
            assert t.type == valid[i]
        assert valid_string == lex_to_string(lexer, simple_program_string)

    def test_wrong_value(self):
        simple_program_string = """
        DECLARE a BEGIN
        aAAA ASSIGN 5
        
        END
        """
        with pytest.raises(GebalangException):
            lex_to_token_list(lexer, simple_program_string)
