from src.ast import *
from src.codegen.binary_expr import execute_and_load_binary_expression
from src.codegen.create_constant import create_constant_number
from src.codegen.util import calculate_shifted_index, get_array_const_index_address
from src.codegen.array_variable_access import load_array_variable_accessed_value, load_array_variable_addr

"""
USED REGISTERS:
0, 1, 2, 3, 4, 5
"""


class AssignCgStrat:
    @staticmethod
    def is_applicable(node):
        return isinstance(node, AssignCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        code = ""
        expr = node.expression
        if isinstance(node.identifier, IdentifierArrayVariable):
            code += load_array_variable_addr_to_three(codegen, node.identifier)
            if isinstance(expr, UnaryExpression):
                code += load_unary_expression(codegen, expr)
                code += store_under_addr_in_three()
                return code
            if isinstance(expr, BinaryExpression):
                code += execute_and_load_binary_expression(codegen, expr)
                code += store_under_addr_in_three()
                return code
        else:
            receiver_addr = get_receiver_addr(codegen, node.identifier)
            if isinstance(expr, UnaryExpression):
                code += load_unary_expression(codegen, expr)
                code += f"STORE {receiver_addr}\n"
                return code
            if isinstance(expr, BinaryExpression):
                code += execute_and_load_binary_expression(codegen, expr)
                code += f"STORE {receiver_addr}\n"
                return code


def load_array_variable_addr_to_three(codegen, identifier):
    code = ""
    code += load_array_variable_addr(codegen, identifier)
    code += "STORE 3\n"
    return code


def load_unary_expression(codegen, expr):
    value = expr.expression
    if value.is_leaf():
        number = value.value
        return create_constant_number(number)
    else:
        identifier = value.value
        variable_name = identifier.variable
        if isinstance(identifier, IdentifierVariable):
            variable_addr = codegen.get_address_by_variable_name(variable_name)
            return f"LOAD {variable_addr}\n"
        if isinstance(identifier, IdentifierArrayNumber):
            array_index_addr = get_array_const_index_address(codegen, identifier)
            return f"LOAD {array_index_addr}\n"
        if isinstance(identifier, IdentifierArrayVariable):
            return load_array_variable_accessed_value(codegen, identifier)


def get_receiver_addr(codegen, identifier):
    variable_name = identifier.variable
    if isinstance(identifier, IdentifierVariable):
        return codegen.get_address_by_variable_name(variable_name)
    if isinstance(identifier, IdentifierArrayNumber):
        dec = codegen.get_declaration_by_variable_name(variable_name)
        shifted_index = calculate_shifted_index(dec, identifier)
        return codegen.get_address_by_variable_name(variable_name, index=shifted_index)


def store_under_addr_in_three():
    return "STOREI 3\n"
