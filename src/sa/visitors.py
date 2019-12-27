from src.ast import *
from src.util import error


class Visitor:
    def visit(self, node):
        yield Exception("implement me")


class DeclarationVisitor(Visitor):
    def __init__(self):
        self.list_of_declarations = []

    def visit(self, node):
        if isinstance(node, VariableDeclaration):
            detect_redeclaration(node, self.list_of_declarations)
            self.list_of_declarations.append(node)
        elif isinstance(node, ArrayDeclaration):
            detect_redeclaration(node, self.list_of_declarations)
            detect_wrong_array_range(node)
            self.list_of_declarations.append(node)


def detect_redeclaration(node, list_of_declarations):
    list_of_ids = map(lambda n: n.id, list_of_declarations)
    if node.id in list_of_ids:
        error(node.line, "Second declaration of variable {}".format(node.id))


def detect_wrong_array_range(node):
    if node.start_index > node.end_index:
        error(node.line, "Invalid range of array with id {}.".format(node.id))
