from src.ast.val_ident import *


def create_value(p):
    p[0] = Value(p[1])


def create_identifier_variable(p):
    p[0] = IdentifierVariable(p[1])


def create_identifier_array_variable(p):
    p[0] = IdentifierArrayVariable(p[1], p[3])


def create_identifier_array_number(p):
    p[0] = IdentifierArrayNumber(p[1], p[3])
