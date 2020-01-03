from src.ast import *
from src.codegen.create_constant import create_constant_number
from src.codegen.util import calculate_shifted_index, get_array_const_index_address


class AssignCgStrat:
    @staticmethod
    def is_applicable(node):
        return isinstance(node, AssignCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        code = ""
        expr = node.expression
        if isinstance(node.identifier, IdentifierArrayVariable):
            return "TODO IMPLEMENT"  # TODO
        else:
            receiver_addr = get_receiver_addr(codegen, node.identifier)
            if isinstance(expr, UnaryExpression):
                code += load_unary_expression_to_register(codegen, expr)
                code += f"STORE {receiver_addr}\n"
                return code
            if isinstance(expr, BinaryExpression):
                return """IMPLEMENT THIS""" #TODO


def load_unary_expression_to_register(codegen, expr):
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
            """balbal"""  # TODO implement this


def get_receiver_addr(codegen, identifier):
    variable_name = identifier.variable
    if isinstance(identifier, IdentifierVariable):
        return codegen.get_address_by_variable_name(variable_name)
    if isinstance(identifier, IdentifierArrayNumber):
        dec = codegen.get_declaration_by_variable_name(variable_name)
        shifted_index = calculate_shifted_index(dec, identifier)
        return codegen.get_address_by_variable_name(variable_name, index=shifted_index)
