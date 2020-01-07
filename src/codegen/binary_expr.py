import math

from src.ast import *
from src.codegen.array_variable_access import load_array_variable_accessed_value
from src.codegen.create_constant import create_constant_number

from src.codegen.util import get_array_const_index_address

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


def execute_multiplication(codegen):  # TODO lg(n) complexity in those guys, how to :( ?
    pass


def execute_division(codegen):
    pass


def execute_modulus(codegen):
    pass


def store_variable_in_reg(codegen, identifier, storage_addr=0):
    variable_name = identifier.variable
    if isinstance(identifier, IdentifierVariable):
        variable_addr = codegen.get_address_by_variable_name(variable_name)
        return f"LOAD {variable_addr}\nSTORE {storage_addr}\n"
    if isinstance(identifier, IdentifierArrayNumber):
        array_index_addr = get_array_const_index_address(codegen, identifier)
        return f"LOAD {array_index_addr}\nSTORE {storage_addr}\n"
    if isinstance(identifier, IdentifierArrayVariable):
        code = load_array_variable_accessed_value(codegen, identifier)
        code += f"STORE {storage_addr}\n"
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
