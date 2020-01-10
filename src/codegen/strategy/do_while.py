from src.ast import *
from src.codegen.conditions import *
from src.codegen.constant import get_id


class DoWhileCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, DoWhileCommand)

    def apply(self, visitor, node, codegen):
        id = get_id()
        code = ""
        code += start_loop_label(id)
        code += visitor.visit(node.commands)
        code += evaluate_condition(codegen, node, id)
        code += f"JUMP {start_loop_label(id)}"
        code += end_loop_label(id)
        return code

    # def apply(self, visitor, node, codegen):
    #     id = get_id()
    #     code = ""
    #     code += evaluate_condition(codegen, node, id)
    #     code += start_loop_label(id)
    #     code += visitor.visit_children(node.commands)
    #     code += f"JUMP {cond_eval_start_label(id)}"
    #     code += end_loop_label(id)
    #     return code
