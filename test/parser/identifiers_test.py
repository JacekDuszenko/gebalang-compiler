from src.util import pretty_print
from test.utils import *


class TestIdentifiers:
    def test_valid_identifiers(self):
        simple_program_string = """
                       DECLARE a,b,c(-11:30) BEGIN
                       READ b;
                       READ a;
                       c(5) ASSIGN 10;
                       c(b) ASSIGN a;
                       c(-10) ASSIGN 10;
                       END
                       """
        ptree = parse(simple_program_string)
        pretty_print(ptree)
