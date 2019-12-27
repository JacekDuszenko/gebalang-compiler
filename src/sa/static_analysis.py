from src.sa.visitors import *
from src.util import *


def preorder(node, visitor):
    visitor.visit(node)
    children = [] if node.is_leaf() else node.get_children()
    for c in children:
        preorder(c, visitor)


def visit_declarations(declarations_node):
    visitor = DeclarationVisitor()
    preorder(declarations_node, visitor)
    decs = visitor.list_of_declarations
    for d in decs:
        pretty_print(d)


def execute_static_analysis(parse_tree):
    visit_declarations(parse_tree.declarations)
