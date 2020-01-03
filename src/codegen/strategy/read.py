from src.ast import *


def find_variable_addr(variable_node, codegen):
    variable_name = variable_node.variable
    dec = codegen.vpool.pool[variable_name]
    if isinstance(variable_node, IdentifierVariable):
        return str(dec.addr)
    if isinstance(variable_node, IdentifierArrayNumber):
        shifted_index = abs(dec.start_index - variable_node.accessor)
        return dec.addr[shifted_index]
    else:
        return "TODO IMPLEMENT THIS" #TODO


class ReadCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ReadCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return f"""GET
STORE {find_variable_addr(node.identifier, codegen)}\n"""
