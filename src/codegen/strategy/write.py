from src.ast import *
from src.codegen.create_constant import create_constant_number


class WriteCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, WriteCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        if node.value.is_leaf():
            return WriteCgStrat.handle_constant_case(node)
        else:
            identifier = node.value.value
            if isinstance(identifier, IdentifierVariable):
                return WriteCgStrat.handle_variable(codegen, identifier)
            if isinstance(identifier, IdentifierArrayNumber):
                return WriteCgStrat.handle_array_with_const_index(codegen, identifier)
            if isinstance(identifier, IdentifierVariable):
                return "XDDDDDD TODO"

    @staticmethod
    def handle_array_with_const_index(codegen, identifier):
        variable_name = identifier.variable
        dec = codegen.get_declaration_by_variable_name(variable_name)
        shifted_index = calculate_shifted_index(dec, identifier)
        addr = codegen.get_address_by_variable_name(variable_name, shifted_index)
        return f""" LOAD {addr}
                PUT \n"""

    @staticmethod
    def handle_variable(codegen, identifier):
        variable_name = identifier.variable
        return f"""LOAD {codegen.get_address_by_variable_name(variable_name)}
                PUT \n"""

    @staticmethod
    def handle_constant_case(node):
        result = ""
        result += create_constant_number(node.value.value)
        result = put(result)
        return result


def put(result):
    result += "PUT"
    return result


def calculate_shifted_index(declaration_node, variable_node):
    start_index = declaration_node.start_index
    return abs(start_index - variable_node.accessor)
