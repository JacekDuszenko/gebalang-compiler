from src.sa.validation import validate_and_get_declarations
from src.util import *


def execute_static_analysis(parse_tree):
    decs = validate_and_get_declarations(parse_tree.declarations)
    pp(decs)
