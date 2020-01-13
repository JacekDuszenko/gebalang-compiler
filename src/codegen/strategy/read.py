from src.ast import *
from src.codegen.array_variable_access import load_array_variable_addr


class ReadCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ReadCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        identifier = node.identifier
        if isinstance(identifier, IdentifierArrayVariable):
            return ReadCgStrat.handle_array_variable_case(codegen, identifier)
        if isinstance(identifier, IdentifierArrayNumber) or isinstance(identifier, IdentifierVariable):
            return f"""GET
STORE {find_variable_addr(node.identifier, codegen)}\n"""

    @staticmethod
    def handle_array_variable_case(codegen, identifier):
        code = ""
        code += load_array_variable_addr(codegen, identifier)
        code += store_variable_addr_to_one()
        code += read_input_and_store_under_address_in_one()
        return code


def find_variable_addr(variable_node, codegen):
    variable_name = variable_node.variable
    dec = codegen.vpool.pool[variable_name]
    if isinstance(variable_node, IdentifierVariable):
        return str(dec.addr)
    if isinstance(variable_node, IdentifierArrayNumber):
        shifted_index = abs(dec.start_index - variable_node.accessor)
        return dec.addr + shifted_index


def store_variable_addr_to_one():
    return "STORE 1\n"


def read_input_and_store_under_address_in_one():
    return "GET\nSTOREI 1\n"
