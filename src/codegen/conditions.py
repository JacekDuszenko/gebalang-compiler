from src.codegen.create_constant import create_constant_number
from src.codegen.value_storage import store_value_in_register
from src.codegen.labels import *

EQUAL = 'EQ'
NOT_EQUAL = 'NEQ'
LESS_THAN = 'LE'
GREATER_THAN = 'GE'
LESS_OR_EQUAL_THAN = 'LEQ'
GREATER_OR_EQUAL_THAN = 'GEQ'


def evaluate_condition(codegen, condition_node, node_id):
    code = ""
    code += cond_eval_start_label(node_id)
    left = condition_node.left
    right = condition_node.right
    code += store_value_in_register(codegen, left, storage_addr=4)
    code += store_value_in_register(codegen, right, storage_addr=5)
    t = condition_node.type
    code += execute_evaluation(codegen, t, node_id)
    return code


def execute_evaluation(codegen, cond_type, node_id): #ADJUST LABEL NAMES TO NODE( IF - EXEC START, ELSE - EXEC ELSE, WHILE _REPEAT ETC)
    code = ""
    code += "LOAD 4\n"
    code += "SUB 5\n"
    if cond_type == EQUAL:
        code += f"JZERO #{node_id}_PASSED\n"  # jump to commands execution (skip next jump)
        code += f"JUMP #{node_id}_FAILED\n"  # exit execution (jump to everything that is after the commands)
    if cond_type == NOT_EQUAL:
        code += f"JZERO #{node_id}_FAILED\n"  # exit execution (jump to everything that is after)
        # else just continue executing commands inside the block
    if cond_type == GREATER_THAN:
        code += f"JPOS #{node_id}_PASSED"  # jump to commands exec (skip next jump)
        code += f"JUMP #{node_id}_FAILED"  # jump to escape execution
    if cond_type == LESS_THAN:
        code += f"JNEG #{node_id}_PASSED"  # jump to commands exec (skip next jump)
        code += f"JUMP #{node_id}_FAILED"  # jump out of exec
    if cond_type == GREATER_OR_EQUAL_THAN:
        code += f"JNEG #{node_id}_FAILED"  # skip execution (jump out of exec)
    if cond_type == LESS_OR_EQUAL_THAN:
        code += f"JPOS #{node_id}_FAILED"  # skip execution
    return code
