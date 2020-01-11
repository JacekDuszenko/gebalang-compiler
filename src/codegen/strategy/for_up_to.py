from src.ast import *
from src.codegen.constant import get_id
from src.codegen.for_loops import *


class ForUpToCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ForUpToCommand)

    def apply(self, visitor, node, codegen):
        variable_name = node.local_iterator.variable
        codegen.allocate_local_variable_with_term_cond(variable_name)
        id = get_id()
        var_addr, var_term_addr, code = initialize_local_variables(codegen, variable_name, node)

        code += evaluate_condition(codegen, var_addr, var_term_addr, id, for_type=FOR_UP_TO)
        code += visitor.visit_children(node.commands)
        code += increment_iterator(var_addr)
        code += f"JUMP {cond_eval_start_label(id)}"
        code += end_loop_label(id)
        codegen.deallocate_local_variable_with_term_cond(variable_name)
        return code
