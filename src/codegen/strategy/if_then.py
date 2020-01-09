from src.ast import *
from src.codegen.conditions import evaluate_condition
from src.codegen.labels import *
from src.codegen.constant import get_id


class IfThenCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, IfThenCommand)

    def apply(self, visitor, node, codegen):
        id = get_id()
        code = ""
        code += evaluate_condition(codegen, node, id)
        code += exec_start_label(id)
        code += visitor.visit_children(node.commands)
        code += exec_end_label(id)
        return code
