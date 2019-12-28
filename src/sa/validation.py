from src.sa.visitors import DeclarationVisitor, RecVariableVisitor


def preorder(node, visitor):
    visitor.visit(node)
    children = [] if node.is_leaf() else node.get_children()
    for c in children:
        preorder(c, visitor)


def validate_and_get_declarations(declarations_node):
    visitor = DeclarationVisitor()
    preorder(declarations_node, visitor)
    decs = visitor.list_of_declarations
    return decs


def validate_variables(scope, cmds):
    recursive_visitor = RecVariableVisitor(scope)
    recursive_visitor.visit(cmds)
