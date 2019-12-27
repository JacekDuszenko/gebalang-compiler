import pytest

from src.error.GebalangException import GebalangException
from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestDeclarations:
    def test_varvar_redeclaration(self):
        simple_program_string = """
                       DECLARE a, b, a BEGIN
                       READ a;
                       END
                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_vararr_redeclaration(self):
        simple_program_string = """
                       DECLARE a, b, a(2:10) BEGIN
                       READ a;
                       END
                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_arrarr_redeclaration(self):
        simple_program_string = """
                       DECLARE a(3:4), b, a(2:10) BEGIN
                       READ a;
                       END
                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_arrvar_redeclaration(self):
        simple_program_string = """
                       DECLARE a(3:4), b, a BEGIN
                       READ a;
                       END
                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_arr_invalid_range_positive(self):
        simple_program_string = """
                       DECLARE a(4:3) BEGIN
                       READ a(1);
                       END
                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_arr_invalid_range_negative(self):
        simple_program_string = """
                          DECLARE a(-3:-4) BEGIN
                          READ a(1);
                          END
                          """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

