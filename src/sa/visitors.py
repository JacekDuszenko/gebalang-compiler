from src.ast import *
from src.sa.visit_strategy import create_visit_strats
from src.util import error
import copy


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


class RecVariableVisitor(Visitor):
    def __init__(self, scope):
        self.scope = scope
        self.visit_strategies = create_visit_strats()

    def visit(self, node):
        old_scope = copy.deepcopy(self.scope)
        for strat in self.visit_strategies:
            if strat.is_applicable(node):
                self.scope = strat.apply(self, node)
                break
        self.visit_children(node)
        self.scope = old_scope

    def visit_children(self, node):
        children = [] if node.is_leaf() else node.get_children()
        for child in children:
            self.visit(child)

