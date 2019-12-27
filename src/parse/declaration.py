from src.ast.declaration import *


def create_declarations_with_variable(p):
    decs = Declarations()
    var_dec = VariableDeclaration(id=p[1], line=p.lineno(1))
    decs.add_declaration(var_dec)
    p[0] = decs


def append_variable_declaration(p):
    decs = p[1]
    var_dec = VariableDeclaration(id=p[3], line=p.lineno(3))
    decs.add_declaration(var_dec)
    p[0] = decs


def create_declarations_with_array(p):
    decs = Declarations()
    array_dec = ArrayDeclaration(p[1], p[3], p[5], line=p.lineno(1))
    decs.add_declaration(array_dec)
    p[0] = decs


def append_array_declaration(p):
    decs = p[1]
    array_dec = ArrayDeclaration(p[3], p[5], p[7], line=p.lineno(3))
    decs.add_declaration(array_dec)
    p[0] = decs
