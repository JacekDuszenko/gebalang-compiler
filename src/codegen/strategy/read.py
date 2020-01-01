from src.ast import *


def find_variable_addr(variable_node, codegen):
    variable_name = variable_node.variable
    dec = codegen.vpool.pool[variable_name]
    if isinstance(variable_node, IdentifierVariable):
        return dec.addr
    if isinstance(variable_node, IdentifierArrayNumber):
        return dec.addr[variable_node.accessor]
    else:
        return ""


class ReadCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ReadCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return f"""
                GET
                STORE {find_variable_addr(node.identifier, codegen)}
               """
