from src.ast import *


class Visitor:
    def visit(self, node):
        yield Exception("implement me")


class DeclarationVisitor(Visitor):
    list_of_declarations = []

    def visit(self, node):
        if isinstance(node, ArrayDeclaration) or isinstance(node, VariableDeclaration):
            self.list_of_declarations.append(node)