from src.codegen.strategy_factory import create_visit_strats
from src.sa.visitors import Visitor


class CodeGenVisitor(Visitor):
    def __init__(self, cgen):
        self.visit_strategies = create_visit_strats()
        self.cgen = cgen

    def visit(self, node):
        code = ""
        for strat in self.visit_strategies:
            if strat.is_applicable(node):
                code += strat.apply(self, node, self.cgen)
                break
        children_code = self.visit_children(node)
        return code + children_code

    def visit_children(self, node):
        children_code = ""
        children = [] if node.is_leaf() else node.get_children()
        for child in children:
            children_code += self.visit(child)
        return children_code
