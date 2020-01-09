from src.ast import *
from src.codegen.value_storage import store_value_in_register
from src.codegen.labels import *

EQUAL = 'EQ'
NOT_EQUAL = 'NEQ'
LESS_THAN = 'LE'
GREATER_THAN = 'GE'
LESS_OR_EQUAL_THAN = 'LEQ'
GREATER_OR_EQUAL_THAN = 'GEQ'


def evaluate_condition(codegen, command, node_id):
    code = ""
    condition_node = command.condition
    code += cond_eval_start_label(node_id)
    left = condition_node.left
    right = condition_node.right
    code += store_value_in_register(codegen, left, storage_addr=4)
    code += store_value_in_register(codegen, right, storage_addr=5)
    t = condition_node.type
    code += execute_evaluation(codegen, t, node_id, command)
    return code


def execute_evaluation(codegen, cond_type, node_id, command):  # ADJUST LABEL NAMES TO NODE( IF - EXEC START,
    # ELSE - EXEC ELSE, WHILE _REPEAT ETC)
    passed_label = create_passed_label(command)
    failed_label = create_failed_label(command)
    code = ""
    code += "LOAD 4\n"
    code += "SUB 5\n"
    if cond_type == EQUAL:
        code += f"JZERO {passed_label(node_id)}"  # jump to commands execution (skip next jump)
        code += f"JUMP {failed_label(node_id)}"  # exit execution (jump to everything that is after the commands)
    if cond_type == NOT_EQUAL:
        code += f"JZERO {failed_label(node_id)}"  # exit execution (jump to everything that is after)
        # else just continue executing commands inside the block
    if cond_type == GREATER_THAN:
        code += f"JPOS {passed_label(node_id)}"  # jump to commands exec (skip next jump)
        code += f"JUMP {failed_label(node_id)}"  # jump to escape execution
    if cond_type == LESS_THAN:
        code += f"JNEG {passed_label(node_id)}"  # jump to commands exec (skip next jump)
        code += f"JUMP {failed_label(node_id)}"  # jump out of exec
    if cond_type == GREATER_OR_EQUAL_THAN:
        code += f"JNEG {failed_label(node_id)}"  # skip execution (jump out of exec)
    if cond_type == LESS_OR_EQUAL_THAN:
        code += f"JPOS {failed_label(node_id)}"  # skip execution
    return code


def create_passed_label(cmd):
    if isinstance(cmd, IfThenElseCommand):
        return lambda id: exec_start_label(id)
    if isinstance(cmd, IfThenCommand):
        return lambda id: exec_start_label(id)
    if isinstance(cmd, WhileCommand):
        pass
    if isinstance(cmd, DoWhileCommand):
        pass
    if isinstance(cmd, ForDownToCommand):
        pass
    if isinstance(cmd, ForUpToCommand):
        pass


def create_failed_label(cmd):
    if isinstance(cmd, IfThenElseCommand):
        return lambda id: exec_else_label(id)
    if isinstance(cmd, IfThenCommand):
        return lambda id: exec_end_label(id)
    if isinstance(cmd, WhileCommand):
        pass
    if isinstance(cmd, DoWhileCommand):
        pass
    if isinstance(cmd, ForDownToCommand):
        pass
    if isinstance(cmd, ForUpToCommand):
        pass
