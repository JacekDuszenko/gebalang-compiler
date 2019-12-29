from src.codegen.strategy_factory import create_visit_strats
from src.sa.visitors import Visitor


class CodeGenVisitor(Visitor):
    def __init__(self, cgen):
        self.visit_strategies = create_visit_strats()
        self.cgen = cgen
        self.code = ""

    def visit(self, node):
        for strat in self.visit_strategies:
            if strat.is_applicable(node):
                self.code += strat.apply(self, node, self.cgen)
                break
        self.visit_children(node)

    def visit_children(self, node):
        children = [] if node.is_leaf() else node.get_children()
        for child in children:
            self.visit(child)
