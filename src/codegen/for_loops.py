from src.codegen.labels import *
from src.codegen.value_storage import store_value_in_register


def initialize_local_variables(codegen, variable_name, node):
    code = ""
    term_cond_name = f'{variable_name}_term_cond'
    variable_addr = codegen.get_address_by_variable_name(variable_name)
    variable_term_cond_addr = codegen.get_address_by_variable_name(term_cond_name)
    value_from = node.value_from
    value_to = node.value_to
    code += store_value_in_register(codegen, value_from, variable_addr)
    code += store_value_in_register(codegen, value_to, variable_term_cond_addr)
    return variable_addr, variable_term_cond_addr, code


FOR_UP_TO = 'FOR_UP_TO'
FOR_DOWN_TO = 'FOR_DOWN_TO'


def evaluate_condition(codegen, var_addr, var_term_addr, id, for_type):
    code = ""
    code += cond_eval_start_label(id)
    code += f"LOAD {var_addr}\n"
    code += f"SUB {var_term_addr}\n"
    if for_type == FOR_UP_TO:
        code += f"JPOS {end_loop_label(id)}"
    elif for_type == FOR_DOWN_TO:
        code += f"JNEG {end_loop_label(id)}"
    return code


def increment_iterator(var_addr):
    code = ""
    code += f"LOAD {var_addr}\n"
    code += f"INC\n"
    code += f"STORE {var_addr}\n"
    return code


def decrement_iterator(var_addr):
    code = ""
    code += f"LOAD {var_addr}\n"
    code += f"DEC\n"
    code += f"STORE {var_addr}\n"
    return code
