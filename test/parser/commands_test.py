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

    def test_valid_for_up(self):
        simple_program_string = """
                             DECLARE a BEGIN
                                READ a;
                               FOR i FROM 10 TO 50 DO 
                               a ASSIGN a PLUS 1;
                               ENDFOR
                               
                               END
                                 """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_valid_for_down_to(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                   READ a;
                                  FOR i FROM 10 DOWNTO 0 DO 
                                  a ASSIGN a PLUS 1;
                                  ENDFOR
                                    WRITE a;
                                  END
                                    """
        ptree = parse(simple_program_string)
        pretty_print(ptree)


    def test_large_embedding_for_to(self):
        simple_program_string = """
                                DECLARE a BEGIN
                                    READ a;
                                  FOR i FROM 0 TO 100 DO 
                                    FOR j FROM 0 TO 100 DO
                                        FOR k FROM 0 TO 100 DO
                                            FOR l FROM 0 TO 100 DO
                                                FOR m FROM 0 TO 100 DO
                                                    FOR n FROM 0 TO 100 DO
                                                        FOR o FROM 0 TO 100 DO
                                                            WRITE 123;
                                                        ENDFOR
                                                    ENDFOR
                                                ENDFOR
                                            ENDFOR
                                        ENDFOR
                                    ENDFOR
                                  ENDFOR
                                  END
                                    """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_large_embedding_for_down_to(self):
        simple_program_string = """
                                   DECLARE a BEGIN
                                       READ a;
                                     FOR i FROM 100 DOWNTO 0 DO 
                                       FOR j FROM 100 DOWNTO 0 DO
                                           FOR k FROM 100 DOWNTO 0 DO
                                               FOR l FROM 100 DOWNTO 0 DO
                                                   FOR m FROM 100 DOWNTO 0 DO
                                                       FOR n FROM 100 DOWNTO 0 DO
                                                           FOR o FROM 100 DOWNTO 0 DO
                                                               WRITE 123;
                                                           ENDFOR
                                                       ENDFOR
                                                   ENDFOR
                                               ENDFOR
                                           ENDFOR
                                       ENDFOR
                                     ENDFOR
                                     END
                                       """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_large_embedding_while(self):
        simple_program_string = """
                                           DECLARE a, i,j,k,l,m,n,o BEGIN
                                               READ a; READ i; READ j; READ k; READ l; READ m; READ n; READ o;
                                             WHILE i GE 100 DO 
                                               WHILE j LE 0  DO
                                                   WHILE k GEQ -500  DO
                                                       WHILE l LEQ -1024 DO
                                                           WHILE m EQ 500   DO
                                                               WHILE n NEQ 15  DO
                                                                   WHILE o EQ 0 DO
                                                                       WRITE 123;
                                                                   ENDWHILE
                                                               ENDWHILE
                                                           ENDWHILE
                                                       ENDWHILE
                                                   ENDWHILE
                                               ENDWHILE
                                             ENDWHILE
                                             END
                                               """
        ptree = parse(simple_program_string)
        pretty_print(ptree)

    def test_large_embedding_do_while(self):
        simple_program_string = """
                              DECLARE a BEGIN
                                 READ a;
                                DO DO DO DO DO
                                READ a;
                                WHILE a GEQ 150  ENDDO
                                 WHILE a GEQ 150 ENDDO
                                  WHILE a GEQ 150 ENDDO
                                   WHILE a GEQ 150 ENDDO
                                    WHILE a GEQ 150 ENDDO
                                END
                                  """
        ptree = parse(simple_program_string)
        pretty_print(ptree)
