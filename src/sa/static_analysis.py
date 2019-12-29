from src.sa.util import create_global_scope_from_decs
from src.sa.validation import validate_and_get_declarations, validate_variables
from src.util import *


def execute_static_analysis(parse_tree):
    decs = validate_and_get_declarations(parse_tree.declarations)
    scope = create_global_scope_from_decs(decs)
    validate_variables(scope, parse_tree.commands)
    return scope
