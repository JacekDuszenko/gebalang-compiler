import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestUninitializedVariable:
    def test_uninitialized_variable_simple(self):
        simple_program_string = """
                            DECLARE a, b BEGIN
                                READ b;
                                b ASSIGN a;
                            END
                        """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_uninitialized_write_variable(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    WRITE a;
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_uninitialized_variable_in_loop_cond(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    WHILE a NEQ 2 DO
                                        WRITE 50;
                                    ENDWHILE
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_uninitialized_variable_in_loop_body(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    FOR i FROM 0 TO 100 DO
                                        WRITE a;
                                    ENDFOR
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_uninitialized_variable_in_nested_loop_body(self):
        simple_program_string = """
                                   DECLARE a BEGIN
                                       FOR i FROM 0 TO 100 DO
                                        FOR j FROM 0 TO 100 DO
                                            FOR k FROM 0 TO 100 DO
                                                WRITE a;
                                            ENDFOR
                                        ENDFOR
                                       ENDFOR
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)
