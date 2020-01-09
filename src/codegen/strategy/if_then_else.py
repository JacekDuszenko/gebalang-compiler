from src.ast import *
from src.codegen.conditions import *
from src.codegen.constant import get_id


class IfThenElseCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, IfThenElseCommand)

    def apply(self, visitor, node, codegen):
        id = get_id()
        code = ""
        code += evaluate_condition(codegen, node, id)
        code += exec_start_label(id)
        code += visitor.visit_children(node.commands_if)
        code += f"JUMP {exec_end_label(id)}"
        code += exec_else_label(id)
        code += visitor.visit_children(node.commands_else)
        code += exec_end_label(id)
        return code
