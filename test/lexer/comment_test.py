import pytest

from src.error.GebalangLexException import GebalangLexException
from src.lexer import lexer
from test.utils import *


class TestComments:
    def test_removing_comments(self):
        simple_program_string = """
         [this is a fun comment]
         [this is a fun comment]BEGIN[this is a fun comment]
        [this is a fun comment]
         [this is a fun comment]END[this is a fun comment]
         [this is a fun comment] [this is a fun comment] [this is a fun comment]
        """
        token_list = lex_to_token_list(lexer, simple_program_string)
        valid = ['BEGIN', 'END']
        valid_string = remove_whitespace("BEGINEND")
        for i, t in enumerate(token_list):
            assert t.type == valid[i]
        assert valid_string == lex_to_string(lexer, simple_program_string)

    def test_error_when_comments_embedded(self):
        simple_program_string = """
        BEGIN
        [ comment starts [ embedded stuff ] ]
        END
        """
        with pytest.raises(GebalangLexException):
            lex_to_token_list(lexer, simple_program_string)
