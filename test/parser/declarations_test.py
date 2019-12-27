from test.utils import *
from src.util import pretty_print


class TestDeclarations:
    def test_no_declarations(self):
        simple_program_string = """
                 BEGIN
                 WRITE 50;
                 END
                 """
        parse(simple_program_string)

    def test_valid_variable_declaration(self):
        simple_program_string = """
                 DECLARE a,b,c,d,e,f,g,h,i,j,k,l,m,n,b,v,c,x,z BEGIN
                 WRITE 50;
                 END
                 """
        parse(simple_program_string)

    def test_valid_array_declaration(self):
        simple_program_string = """
                    DECLARE a(2:5) BEGIN
                    WRITE 50;
                    END
                    """
        parse(simple_program_string)

    def test_valid_array_declaration_with_vars(self):
        simple_program_string = """
                    DECLARE c, a(2:5), b BEGIN
                    WRITE 50;
                    END
                    """
        parse(simple_program_string)

    def test_alternating_array_declaration(self):
        simple_program_string = """
                       DECLARE a, b(2:10), c, d(3:4), e(-10:20) BEGIN
                       WRITE 50;
                       END
                       """
        ptree = parse(simple_program_string)
        pretty_print(ptree)
