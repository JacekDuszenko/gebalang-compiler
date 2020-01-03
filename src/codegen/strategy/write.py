from src.ast import *
from src.codegen.create_constant import create_constant_number
from src.codegen.util import calculate_shifted_index, get_array_const_index_address


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
                return "TODO IMPLEMENT THIS" #TODO

    @staticmethod
    def handle_array_with_const_index(codegen, identifier):
        addr = get_array_const_index_address(codegen, identifier)
        return f"""LOAD {addr}
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



