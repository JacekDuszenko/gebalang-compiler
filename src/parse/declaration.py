from src.ast.declaration import *


def create_declarations_with_variable(p):
    decs = Declarations()
    decs.add_declaration(VariableDeclaration(id=p[1]))
    p[0] = decs


def append_variable_declaration(p):
    decs = p[1]
    decs.add_declaration(VariableDeclaration(id=p[3]))
    p[0] = decs


def create_declarations_with_array(p):
    decs = Declarations()
    decs.add_declaration(ArrayDeclaration(p[1], p[3], p[5]))
    p[0] = decs


def append_array_declaration(p):
    decs = p[1]
    decs.add_declaration(ArrayDeclaration(p[3], p[5], p[7]))
    p[0] = decs
