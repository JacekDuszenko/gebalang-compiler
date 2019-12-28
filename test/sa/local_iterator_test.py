import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestLocalIterator:
    def test_local_iterator_name_same_as_global(self):
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

    def test_local_iterator_name_same_as_global_downto(self):
        simple_program_string = """
                                         DECLARE a BEGIN
                                             FOR a FROM 100 DOWNTO a DO
                                             WRITE 10;
                                             ENDFOR
                                         END
                                         """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_local_variable_double_declaration(self):
        simple_program_string = """
                                      DECLARE a BEGIN
                                          FOR i FROM 0 TO 100 DO
                                           FOR i FROM 0 TO 100 DO
                                           WRITE 20;
                                               ENDFOR
                                          ENDFOR
                                      END
                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_local_variable_double_declaration_nested(self):
        simple_program_string = """
                                         DECLARE a BEGIN
                                             FOR i FROM 0 TO 100 DO
                                              FOR j FROM 0 TO 100 DO
                                                FOR k FROM 0 TO 100 DO
                                                    FOR i FROM 0 TO 100 DO
                                                        WRITE 10;
                                                    ENDFOR
                                                   ENDFOR
                                                  ENDFOR
                                                 ENDFOR
                                         END
                                         """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)