import pytest

from src.error.GebalangException import GebalangException
from test.utils import *


class TestParseErrors:
    def test_capital_letters(self):
        simple_program_string = """
        DECLARE aA BEGIN
        aA ASSIGN 5;
        END
        """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_numbers(self):
        simple_program_string = """
                          DECLARE a1 BEGIN
                          WRITE 10;
                          END
                          """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_numbers_array(self):
        simple_program_string = """
                             DECLARE a(2:10), b, c, d, a1(2:10), e BEGIN
                             WRITE 10;
                             END
                             """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_no_semic_after_assign(self):
        simple_program_string = """
           DECLARE a BEGIN
           a ASSIGN 123
           END
           """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_no_coma_after_decl(self):
        simple_program_string = """
              DECLARE a b BEGIN
              a ASSIGN 123;
              END
              """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_no_coma_after_decl_2(self):
        simple_program_string = """
                    DECLARE a,b,c,d,e,f,g,h,i,j,k,l m,n,b,v,c,x,z BEGIN
                    WRITE 50;
                    END
                    """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_no_sc_after_read(self):
        simple_program_string = """
              DECLARE a BEGIN
              READ a
              END
              """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_no_sc_after_write(self):
        simple_program_string = """
                 DECLARE a BEGIN
                 a ASSIGN 10;
                 WRITE a
                 END
                 """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_number_too_large_in_array_decl(self):
        simple_program_string = """
                    DECLARE a(2:500000000000000000000000000000000) BEGIN
                    WRITE 50;
                    END
                    """
        with pytest.raises(GebalangException):
            parse(simple_program_string)

    def test_number_too_small_in_array_decl(self):
        simple_program_string = """
                       DECLARE a(-99999999999999999999999999999999:0) BEGIN
                       WRITE 50;
                       END
                       """
        with pytest.raises(GebalangException):
            parse(simple_program_string)