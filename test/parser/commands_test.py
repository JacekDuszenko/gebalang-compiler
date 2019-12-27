from src.util import pretty_print
from test.utils import *


class TestCommands:
    def test_valid_ifelse(self):
        simple_program_string = """
                       DECLARE a BEGIN
                        READ a;
                        IF a GE 10 THEN
                        WRITE 5;
                        ELSE
                        WRITE 10;
                        ENDIF
                       END
                       """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_valid_if(self):
        simple_program_string = """
                          DECLARE a BEGIN
                           READ a;
                           IF a GE 10 THEN
                           WRITE 5;
                           ENDIF
                          END
                          """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_valid_while(self):
        simple_program_string = """
                             DECLARE a BEGIN
                              READ a;
                              WHILE a GEQ 50 
                              
                              DO
                              
                              WRITE 5;
                              WRITE 10;
                              WRITE 30;
                                    ENDWHILE
                             END
                             """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_valid_do_while(self):
        simple_program_string = """
                             DECLARE a BEGIN
                                READ a;
                               DO
                               READ a;
                               READ a;
                               READ a;
                               a ASSIGN a MINUS 1;
                               
                               WHILE a GEQ 150
                               ENDDO
                               END
                                 """
        ptree = parse(simple_program_string)
        pretty_print(ptree)
