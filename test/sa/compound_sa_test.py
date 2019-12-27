import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestCompoundSa:
    def test_undeclared_variable(self):
        simple_program_string = """
                             DECLARE a BEGIN
                             READ a;
                             b ASSIGN a;
                             END
                             """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_assignment_of_not_initialized_variable(self):
        simple_program_string = """
                                DECLARE a, b BEGIN
                                b ASSIGN a;
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)
