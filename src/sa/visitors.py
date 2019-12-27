from src.ast import *
from src.sa.validation import detect_redeclaration, detect_wrong_array_range


class Visitor:
    def visit(self, node):
        yield Exception("implement me")


class DeclarationVisitor(Visitor):
    list_of_declarations = []

    def visit(self, node):
        if isinstance(node, VariableDeclaration):
            detect_redeclaration(node, self.list_of_declarations)
            self.list_of_declarations.append(node)
        elif isinstance(node, ArrayDeclaration):
            detect_redeclaration(node, self.list_of_declarations)
            detect_wrong_array_range(node)
            self.list_of_declarations.append(node)
