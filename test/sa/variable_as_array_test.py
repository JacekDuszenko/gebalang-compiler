import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestVariableAsArray:
    def test_variable_as_array_in_read(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    READ a(0);
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_as_array_write(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    WRITE a(3);
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_assign_as_array(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    a(5) ASSIGN 10;
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_assign_with_variable_accessor_as_array(self):
        simple_program_string = """
                                   DECLARE a, b BEGIN
                                       READ b;
                                       a(b) ASSIGN 10;
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_if_condition_as_array(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                READ a;
                                IF a(4) GE 10 THEN
                                    WRITE 100;
                                ENDIF
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_if_else_condition_as_array(self):
        simple_program_string = """
                                   DECLARE a BEGIN
                                   READ a;
                                   IF a(4) EQ 10 THEN
                                        WRITE 100;
                                   ELSE
                                        WRITE 200;
                                   ENDIF
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_while_condition_as_array(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                READ a;
                                WHILE a(-10) NEQ 10 DO
                                    WRITE 100;
                                ENDWHILE
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_do_while_condition_as_array(self):
        simple_program_string = """
                                   DECLARE a BEGIN
                                   READ a;
                                   DO
                                       WRITE 100;
                                   WHILE a(-10) LEQ 10 
                                   ENDDO
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_for_loop_from_as_array(self):
        simple_program_string = """
                                      DECLARE a BEGIN
                                      READ a;
                                      FOR i FROM a(5) TO 10 DO 
                                      WRITE 50;
                                      ENDFOR
                                      END
                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_for_loop_to_as_array(self):
        simple_program_string = """
                                      DECLARE a BEGIN
                                      READ a;
                                      FOR i FROM 0 TO a(5) DO 
                                      WRITE 50;
                                      ENDFOR
                                      END
                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_for_downto_loop_from_as_array(self):
        simple_program_string = """
                                      DECLARE a BEGIN
                                      READ a;
                                      FOR i FROM a(5) DOWNTO 0 DO 
                                      WRITE 50;
                                      ENDFOR
                                      END
                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_for_downto_loop_to_as_array(self):
        simple_program_string = """
                                         DECLARE a BEGIN
                                         READ a;
                                         FOR i FROM 0 DOWNTO a(13) DO 
                                         WRITE 50;
                                         ENDFOR
                                         END
                                         """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_expression_as_array(self):
        simple_program_string = """
                                           DECLARE a, b BEGIN
                                           READ a;
                                           b ASSIGN 35 DIV a(3);
                                           END
                                           """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_variable_expression_as_array_2nd(self):
        simple_program_string = """
                                    DECLARE a,b BEGIN
                                    READ a;
                                    b ASSIGN 35 MOD  a(4);
                                    END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)
