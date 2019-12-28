import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestSaArrays:
    def test_assignment_of_array_without_braces(self):
        simple_program_string = """
                                     DECLARE a(2:10) BEGIN
                                     a ASSIGN 20;
                                     END
                                     """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_for_to_loop_in_FROM_clause(self):
        simple_program_string = """
                                        DECLARE a(2:10) BEGIN
                                        a(0) ASSIGN 5;
                                        FOR i FROM a TO 10 DO 
                                            WRITE 5;
                                        ENDFOR
                                        END
                                        """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_for_to_loop_in_TO_clause(self):
        simple_program_string = """
                                           DECLARE a(2:10) BEGIN
                                           a(0) ASSIGN 5;
                                           FOR i FROM 10 TO a DO 
                                               WRITE 5;
                                           ENDFOR
                                           END
                                           """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_for_downto_loop_in_FROM_clause(self):
        simple_program_string = """
                                              DECLARE a(2:10) BEGIN
                                              a(0) ASSIGN 5;
                                              FOR i FROM a DOWNTO 10 DO 
                                                  WRITE 5;
                                              ENDFOR
                                              END
                                              """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_for_downto_loop_in_DOWNTO_clause(self):
        simple_program_string = """
                                                 DECLARE a(2:10) BEGIN
                                                 a(0) ASSIGN 5;
                                                 FOR i FROM 0 DOWNTO a DO 
                                                     WRITE 5;
                                                 ENDFOR
                                                 END
                                                 """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_if_condition(self):
        simple_program_string = """
                                    DECLARE a(2:10) BEGIN
                                        READ a(0);
                                        IF a EQ 50 THEN
                                        WRITE 20;
                                        ENDIF
                                    END
                                                 """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_if_else_condition(self):
        simple_program_string = """
                                      DECLARE a(2:10) BEGIN
                                          READ a(0);
                                          IF a NEQ 50 THEN
                                          WRITE 20;
                                          ELSE
                                          WRITE 30;
                                          ENDIF
                                      END
                                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_expression(self):
        simple_program_string = """
                                         DECLARE a(2:10), b, c BEGIN
                                             READ b;
                                             READ c;
                                             b ASSIGN b PLUS a;
                                         END
                                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_array_without_braces_in_expression_other_combination(self):
        simple_program_string = """
                                          DECLARE a(2:10), b, c BEGIN
                                              READ b;
                                              READ c;
                                              a ASSIGN b PLUS a;
                                          END
                                                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_read_of_array_without_braces(self):
        simple_program_string = """
                                       DECLARE a(2:10) BEGIN
                                       READ a;
                                       END
                                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_write_of_array_without_braces(self):
        simple_program_string = """
                                       DECLARE a(0:1) BEGIN
                                       READ a(0);
                                       READ a(1);
                                       WRITE a;
                                       END
                                       """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_assignment_of_array_without_braces_right_side(self):
        simple_program_string = """
                                    DECLARE a(2:10), b BEGIN
                                    READ b;
                                    b ASSIGN a;
                                    END
                                    """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_accessing_invalid_array_range_positive(self):
        simple_program_string = """
                                DECLARE a(3:4), b BEGIN
                                    READ a(5);
                                    END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_accessing_invalid_array_range_negative(self):
        simple_program_string = """
                                  DECLARE a(-5:-3), b BEGIN
                                      READ a(-6);
                                      END
                                  """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_accessing_uninitialized_array_element(self):
        simple_program_string = """
                                  DECLARE a(0:10), b BEGIN
                                      READ a(0);
                                      READ a(1);
                                      WRITE a(0);
                                      WRITE a(1);

                                      WRITE a(3); [error here]
                                      END
                                  """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)
