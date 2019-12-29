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

    def test_local_iterator_the_same_name_as_global(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                FOR a FROM 0 TO 100 DO
                                    WRITE 10;
                                ENDFOR
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_MUST_ASSIGN_assignment_of_local_scope_variable_nested(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                FOR b FROM 0 TO 100 DO
                                    FOR a FROM 0 TO 100 DO
                                        WRITE 10;
                                    ENDFOR
                                ENDFOR
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_local_variable_out_of_scope(self):
        simple_program_string = """
                                BEGIN
                                FOR a FROM 0 TO 100 DO
                                    FOR b FROM 0 TO 100 DO
                                        WRITE 10;
                                    ENDFOR
                                    WRITE b; [this should fail]
                                ENDFOR
                                END
                                """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_usage_of_local_variable_out_of_scope_because_in_global(self):
        simple_program_string = """
                                   BEGIN
                                   FOR a FROM 0 TO 100 DO
                                       FOR b FROM 0 TO 100 DO
                                           WRITE 10;
                                       ENDFOR
                                   ENDFOR
                                   b ASSIGN 10; [this should fail]
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_write_of_not_initialized_variable(self):
        simple_program_string = """
                                   DECLARE a BEGIN
                                   WRITE a;
                                   END
                                   """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

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
                                        DECLARE a(0:10) BEGIN
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
                                           DECLARE a(0:10) BEGIN
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
                                              DECLARE a(0:10) BEGIN
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
                                                 DECLARE a(0:10) BEGIN
                                                 a(0) ASSIGN 5;
                                                 FOR i FROM 0 DOWNTO a DO 
                                                     WRITE 5;
                                                 ENDFOR
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

    def test_analysis_should_pass_when_literals_in_assignment_conditon_expression(self):
        simple_program_string = """
                                  DECLARE a BEGIN
                                      a ASSIGN 10;
                                      FOR i FROM 0 TO 10 DO
                                      a ASSIGN 5;
                                      ENDFOR
                                      IF 2 GEQ 3 THEN
                                      a ASSIGN 5;
                                      ELSE
                                      a ASSIGN 10;
                                      ENDIF
                                      a ASSIGN 5 MOD 10;
                                      END
                                  """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)