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


RIGHT_COPY_REG = 6
SUM_REG = 7
TWO_POW_REG = 8
ONE_CONST_REG = 9
TEMP_VAL_REG = 10
IS_NEG_REG = 11
IS_REM_NEG = 12


def execute_division(codegen):
    """
    R4 - left value
    R5 - right value
    R6 - r copy = rcp
    R7 - total quotient sum = sum
    R8 - current 2 pow - two_pow
    R9 - number one constant value
    R10 - temp value
    R11 - is negative flag
    """

    id = get_id()
    code = ""

    code += detect_division_by_zero(id)
    code += initialize_constant_one_and_clear_sum(id)
    code += determine_isneg(id)
    code += div_outer_loop(id)
    code += div_zero_label(id)
    return code


def determine_isneg(id):
    code = ""
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"JNEG {div_isneg_lneg_label(id)}"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JNEG {div_isneg_rneg_label(id)}"
    code += mark_as_positive(id)

    code += div_isneg_lneg_label(id)
    code += "SUB 0\n"
    code += f"SUB {LEFT_VALUE_REG}\n"
    code += f"STORE {LEFT_VALUE_REG}\n"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JNEG {div_isneg_both_neg_label(id)}"
    code += mark_as_negative(id)  # left is negative, right is positive

    code += div_isneg_rneg_label(id)
    code += f"SUB 0\n"
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += f"STORE {RIGHT_VALUE_REG}\n"
    code += mark_as_negative(id)  # left is positive, right is negative

    code += div_isneg_both_neg_label(id)
    code += "SUB 0\n"
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += f"STORE {RIGHT_VALUE_REG}\n"
    code += mark_as_positive(id)

    code += f"{div_isneg_end_label(id)}"
    return code


def mark_as_positive(id):
    code = ""
    code += "SUB 0\n"
    code += f"STORE {IS_NEG_REG}\n"
    code += f"JUMP {div_isneg_end_label(id)}"
    return code


def mark_as_negative(id):
    code = ""
    code += "SUB 0\n"
    code += "INC\n"
    code += f"STORE {IS_NEG_REG}\n"
    code += f"JUMP {div_isneg_end_label(id)}"
    return code


def initialize_constant_one_and_clear_sum(id):
    code = ""
    code += "SUB 0\n"
    code += f"STORE {SUM_REG}\n"
    code += "INC \n"
    code += f"STORE {ONE_CONST_REG}\n"
    return code


def div_outer_loop(id, is_modulus=False):
    code = ""
    code += f"{div_outer_loop_label(id)}"
    code += evaluate_exit_outer_loop_condition(id)
    code += initialize_max_twopow_loop(id)
    code += max_twopow_loop(id)
    if is_modulus:
        code += outer_loop_finalize_eval_mod(id)
    else:
        code += outer_loop_finalize_eval_div(id)
    return code


def outer_loop_finalize_eval_mod(id):
    code = ""
    code += f"{div_finalize_label(id)}"
    code += f"LOAD {IS_NEG_REG}\n"  # if is neg, we need to do complement

    code += f"JZERO {mod_do_not_complement_label(id)}"
    code += f"LOAD {LEFT_VALUE_REG}\n"  # complement the remainder
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += f"STORE {LEFT_VALUE_REG}\n"

    code += mod_do_not_complement_label(id)
    code += f"LOAD {IS_REM_NEG}\n"  # fix the sign
    code += f"JPOS {rem_must_be_neg_label(id)}"
    code += f"LOAD {LEFT_VALUE_REG}\n"  # remainder must be positive
    code += f"JPOS {rem_fixing_end_label(id)}"  # end if it is

    code += f"SUB 0\n"  # if it is not flip its sign
    code += f"SUB {LEFT_VALUE_REG}\n"
    code += f"JUMP {rem_fixing_end_label(id)}"

    code += rem_must_be_neg_label(id)
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"JNEG {rem_fixing_end_label(id)}"  # if it is neg its okay
    code += f"SUB 0\n"  # else flip its sign
    code += f"SUB {LEFT_VALUE_REG}\n"
    code += rem_fixing_end_label(id)
    return code


def outer_loop_finalize_eval_div(id):
    code = ""
    code += f"{div_finalize_label(id)}"
    code += f"LOAD {LEFT_VALUE_REG}\n"  # remainder
    code += f"STORE {TEMP_VAL_REG}\n"
    code += f"LOAD {IS_NEG_REG}\n"
    code += f"JZERO {div_nothing_to_be_done_in_finalize_label(id)}"
    code += f"SUB 0\n"
    code += f"SUB {SUM_REG}\n"
    code += f"STORE {SUM_REG}\n"
    code += f"LOAD {TEMP_VAL_REG}\n"
    code += f"JZERO {div_nothing_to_be_done_in_finalize_label(id)}"
    code += f"LOAD {SUM_REG}\n"
    code += f"DEC\n"
    code += f"STORE {SUM_REG}\n"
    code += div_nothing_to_be_done_in_finalize_label(id)
    code += f"LOAD {SUM_REG}\n"
    return code


def max_twopow_loop(id):
    code = ""
    code += div_max_two_pow_label(id)
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"SUB {RIGHT_COPY_REG}\n"
    code += f"JPOS {div_max_two_pow_reloop_label(id)}"
    code += f"JZERO {div_max_two_pow_reloop_label(id)}"
    code += f"JUMP {div_max_two_pow_exit_label(id)}"
    code += f"{div_max_two_pow_reloop_label(id)}"
    code += max_twopow_post_eval_execution(id)
    code += f"JUMP {div_max_two_pow_label(id)}"

    code += f"{div_max_two_pow_exit_label(id)}"
    code += twopow_exit_eval_execution(id)
    return code


def twopow_exit_eval_execution(id):
    code = ""
    code += f"LOAD {TWO_POW_REG}\n"
    code += f"DEC \n"
    code += f"STORE {TWO_POW_REG}\n"
    code += f"LOAD {ONE_CONST_REG}\n"
    code += f"SHIFT {TWO_POW_REG}\n"
    code += f"ADD {SUM_REG}\n"
    code += f"STORE {SUM_REG}\n"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"SHIFT {TWO_POW_REG}\n"
    code += f"STORE {TEMP_VAL_REG}\n"
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"SUB {TEMP_VAL_REG}\n"
    code += f"STORE {LEFT_VALUE_REG}\n"
    code += f"JUMP {div_outer_loop_label(id)}"
    return code


def max_twopow_post_eval_execution(id):
    code = ""
    code += f"LOAD {RIGHT_COPY_REG}\n"
    code += f"SHIFT {ONE_CONST_REG}\n"
    code += f"STORE {RIGHT_COPY_REG}\n"
    code += f"LOAD {TWO_POW_REG}\n"
    code += f"INC\n"
    code += f"STORE {TWO_POW_REG}\n"
    return code


def initialize_max_twopow_loop(id):
    code = ""
    code += f"SUB 0\n"
    code += f"STORE {TWO_POW_REG}\n"
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"STORE {RIGHT_COPY_REG}\n"
    return code


def evaluate_exit_outer_loop_condition(id):
    code = ""
    code += f"LOAD {LEFT_VALUE_REG}\n"
    code += f"SUB {RIGHT_VALUE_REG}\n"
    code += f"JNEG {div_finalize_label(id)}"
    return code


def detect_division_by_zero(id):
    code = ""
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JZERO {div_zero_label(id)}"
    return code


def execute_modulus(codegen):
    """
       R4 - left value
       R5 - right value
       R6 - r copy = rcp
       R7 - total quotient sum = sum
       R8 - current 2 pow - two_pow
       R9 - number one constant value
       R10 - temp value
       R11 - is negative flag
       R12 - rem negative flag
       """

    id = get_id()
    code = ""
    code += detect_division_by_zero(id)
    code += initialize_constant_one_and_clear_sum(id)

    code += check_remainder_negative(id)

    code += determine_isneg(id)
    code += div_outer_loop(id, is_modulus=True)
    code += div_zero_label(id)
    return code


def check_remainder_negative(id):
    code = ""
    code += f"LOAD {RIGHT_VALUE_REG}\n"
    code += f"JPOS {mod_rem_positive_label(id)}"
    code += f"SUB 0\n"
    code += f"INC\n"
    code += f"STORE {IS_REM_NEG}\n"
    code += f"JUMP {mod_end_remainder_negative_check_label(id)}"
    code += mod_rem_positive_label(id)
    code += f"SUB 0 \n"
    code += f"STORE {IS_REM_NEG}\n"
    code += mod_end_remainder_negative_check_label(id)

    return code


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
