import math

from src.ast import *
from src.codegen.constant import get_id
from src.codegen.create_constant import create_constant_number
from src.codegen.value_storage import store_variable_in_reg
from src.codegen.labels import *

"""USED REGISTERS: 0, 1, 2, 3, 4, 5"""


def execute_and_load_binary_expression(codegen, expr):
    code = ""
    left = expr.left
    right = expr.right
    operator = expr.type
    if left.is_leaf() and right.is_leaf():
        code += compute_and_store_constant_in_memory(left.value, right.value, operator)
        return code
    else:
        if left.is_leaf():
            lval = left.value
            code += create_constant_number(lval, storage_addr=4)
            code += store_variable_in_reg(codegen, right.value, storage_addr=5)
        if right.is_leaf():
            rval = right.value
            code += create_constant_number(rval, storage_addr=5)
            code += store_variable_in_reg(codegen, left.value, storage_addr=4)
        if not left.is_leaf() and not right.is_leaf():
            code += store_variable_in_reg(codegen, left.value, 4)
            code += store_variable_in_reg(codegen, right.value, 5)
        code += execute_operation(codegen, operator)
        return code


def execute_operation(codegen, operator):
    if operator == 'PLUS':
        return execute_addition(codegen)
    if operator == 'MINUS':
        return execute_subtraction(codegen)
    if operator == 'TIMES':
        return execute_multiplication(codegen)
    if operator == 'DIV':
        return execute_division(codegen)
    if operator == 'MOD':
        return execute_modulus(codegen)


def execute_addition(codegen):
    return "LOAD 4\nADD 5\n"


def execute_subtraction(codegen):
    return "LOAD 4\nSUB 5\n"


"""
R4 - left value
R5 - right value
R7 - negative one value
R8 - positive one value
R9 - temp swap variable AND left absolute value
"""
LEFT_VALUE_REG = 4
RIGHT_VALUE_REG = 5
PARTIAL_RESULT_REG = 6
NEGATIVE_ONE_VALUE_REG = 7
POSITIVE_ONE_VALUE_REG = 8
TEMP_VAL = 9


def execute_multiplication(codegen):
    id = get_id()
    code = ""
    code += detect_multiply_by_zero(id)
    code += initialize_multiplication_registers()
    code += place_smaller_on_left(id)  # optimization for big and small number (abs val)

    code += check_l_eq_one(id)
    code += check_l_even(id)
    code += execute_l_odd_logic(id)
    code += mul_l_even_label(id)
    code += execute_l_even_logic(id)

    code += mul_done_label(id)
    code += finalize_computation_result_positive(id)

    code += mul_done_neg_result_label(id)
    code += finalize_computation_result_negative(id)

    code += mul_zero_label(id)

    return code


def place_smaller_on_left(id):
    code = ""
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"JPOS {mul_left_positive_label(id)}"
    code += "SUB 0\n"
    code += f"SUB {LEFT_VALUE_REG}\n"
    code += mul_left_positive_label(id)
    code += f"STORE {TEMP_VAL}\n"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JPOS {mul_right_positive_label(id)}"
    code += "SUB 0\n"
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += mul_right_positive_label(id)
    code += f"SUB {TEMP_VAL}\n"
    code += f"JPOS {mul_do_not_swap_label(id)}"
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"STORE {TEMP_VAL}\n"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"STORE {LEFT_VALUE_REG}\n"
    code += f"LOAD {TEMP_VAL}\n"
    code += f"STORE {RIGHT_VALUE_REG}\n"
    code += f"{mul_do_not_swap_label(id)}"
    return code


def execute_l_even_logic(id):
    code = ""
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"SHIFT {POSITIVE_ONE_VALUE_REG}\n"  # r = 2r
    code += f"STORE {RIGHT_VALUE_REG}\n"
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"SHIFT {NEGATIVE_ONE_VALUE_REG}\n"  # l = l / 2
    code += f"STORE {LEFT_VALUE_REG}\n"
    code += f"JUMP {mul_start_label(id)}"
    return code


def execute_l_odd_logic(id):
    code = ""
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"ADD {PARTIAL_RESULT_REG}\n"
    code += f"STORE {PARTIAL_RESULT_REG}\n"
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"DEC\n"
    code += f"STORE {LEFT_VALUE_REG}\n"
    return code


def check_l_even(id):
    code = ""
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"SHIFT {NEGATIVE_ONE_VALUE_REG}\n"
    code += f"ADD 0\n"
    code += f"SUB {LEFT_VALUE_REG}\n"
    code += f"JZERO {mul_l_even_label(id)}"  # even
    return code


def check_l_eq_one(id):
    code = ""
    code += f"{mul_start_label(id)}"
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += "DEC\n"
    code += f"JZERO {mul_done_label(id)}"
    code += f"INC\n"
    code += f"INC\n"
    code += f"JZERO {mul_done_neg_result_label(id)}"
    return code


def finalize_computation_result_negative(id):
    code = ""
    code += "SUB 0\n"
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += f"ADD {PARTIAL_RESULT_REG}\n"
    return code


def finalize_computation_result_positive(id):
    code = ""
    code += f"LOAD {PARTIAL_RESULT_REG}\n"
    code += f"ADD {RIGHT_VALUE_REG}\n"
    code += f"JUMP {mul_zero_label(id)}"
    return code


def initialize_multiplication_registers():
    """
    initializes partial_result register and minus_one_value register and positive_one_value register
    :return:
    """
    code = ""
    code += "SUB 0\n"
    code += f"STORE {PARTIAL_RESULT_REG}\n"
    code += "DEC\n"
    code += f"STORE {NEGATIVE_ONE_VALUE_REG}\n"
    code += "INC\n"
    code += "INC \n"
    code += f"STORE {POSITIVE_ONE_VALUE_REG}\n"
    return code


def detect_multiply_by_zero(id):
    code = ""
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"JZERO {mul_zero_label(id)}"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JZERO {mul_zero_label(id)}"
    return code


def execute_division(codegen):
    pass


def execute_modulus(codegen):
    pass


def compute_and_store_constant_in_memory(l, r, operator):
    result = 0
    if operator == 'PLUS':
        result = l + r
    if operator == 'MINUS':
        result = l - r
    if operator == 'TIMES':
        result = l * r
    if operator == 'DIV':
        if r == 0:
            result = 0
        else:
            result = math.floor(l / r)
    if operator == 'MOD':
        if r == 0:
            result = 0
        else:
            result = l - (r * math.floor(l / r))
    return create_constant_number(result)
