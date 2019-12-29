import pytest

from src.sa.static_analysis import execute_static_analysis
from test.utils import *


class TestPositive:
    def test_p1(self):
        simple_program_string = """
                                      DECLARE a BEGIN
                                      FOR i FROM 0 TO 20 DO
                                      WRITE 10;
                                      ENDFOR
                                      
                                      FOR i FROM 0 TO 20 DO
                                      READ a;
                                      ENDFOR
                                  
                                      WRITE a;
                                      END
                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p2(self):
        simple_program_string = """
                                     DECLARE a(0:5) BEGIN
                                     READ a(0);
                                     READ a(1);
                                     READ a(2);
                                     READ a(3);
                                     READ a(4);
                                     READ a(5);
                                     WRITE a(5);
                                     WRITE a(4);
                                     WRITE a(3);
                                     WRITE a(2);
                                     WRITE a(1);
                                     WRITE a(0);
                                      END
                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p3(self):
        simple_program_string = """
                                     DECLARE a(0:3) BEGIN
                                      READ a(0);
                                      READ a(3);
                                      FOR i FROM a(0) TO a(3) DO
                                      WRITE 2;
                                      ENDFOR
                                      END
                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p4(self):
        simple_program_string = """
                                     DECLARE a(0:3) BEGIN
                                      
                                      FOR i FROM 0 TO 10 DO
                                      READ a(i);
                                      ENDFOR
                                      WRITE a(0);
                                      WRITE a(1);
                                      WRITE a(2);
                                      WRITE a(3);
                                      END
                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p5(self):
        simple_program_string = """
                                           DECLARE
                                            a, b
                                        BEGIN
                                            READ a;
                                            IF a GEQ 0 THEN
                                            WHILE a GE 0 DO
                                                b ASSIGN a DIV 2;
                                                b ASSIGN 2 TIMES b;
                                                IF a GE b THEN 
                                                        WRITE 1;
                                                ELSE 
                                                        WRITE 0;
                                                ENDIF
                                                a ASSIGN a DIV 2;
                                            ENDWHILE
                                            ENDIF
                                        END

                                             """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p6(self):
        simple_program_string = """
                                                                         [ sito Eratostenesa ]
                                    DECLARE
                                        n, j, sito(2:100)
                                    BEGIN
                                        n ASSIGN 100;
                                        FOR i FROM n DOWNTO 2 DO
                                            sito(i) ASSIGN 1;
                                        ENDFOR
                                        FOR i FROM 2 TO n DO
                                            IF sito(i) NEQ 0 THEN
                                                j ASSIGN i PLUS i;
                                                WHILE j LEQ n DO
                                                    sito(j) ASSIGN 0;
                                                    j ASSIGN j PLUS i;
                                                ENDWHILE
                                                WRITE i;
                                            ENDIF
                                        ENDFOR
                                    END

                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_p7(self):
        simple_program_string = """
                                   [ Rozklad liczby na czynniki pierwsze ]
                                    DECLARE
                                        n, m, reszta, potega, dzielnik
                                    BEGIN
                                        READ n;
                                        dzielnik ASSIGN 2;
                                        m ASSIGN dzielnik TIMES dzielnik;
                                        WHILE n GEQ m DO
                                            potega ASSIGN 0;
                                            reszta ASSIGN n MOD dzielnik;
                                            WHILE reszta EQ 0 DO
                                                n ASSIGN n DIV dzielnik;
                                                potega ASSIGN potega PLUS 1;
                                                reszta ASSIGN n MOD dzielnik;
                                            ENDWHILE
                                            IF potega GE 0 THEN [ czy znaleziono dzielnik ]
                                                WRITE dzielnik;
                                                WRITE potega;
                                            ELSE
                                                dzielnik ASSIGN dzielnik PLUS 1;
                                                m ASSIGN dzielnik TIMES dzielnik;
                                            ENDIF
                                        ENDWHILE
                                        IF n NEQ 1 THEN [ ostatni dzielnik ]
                                            WRITE n;
                                            WRITE 1;
                                        ENDIF
                                    END
                                      """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)