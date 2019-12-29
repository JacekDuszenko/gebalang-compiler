from src.ast import *


def find_variable_addr(variable_node, codegen):
    if isinstance(variable_node, IdentifierVariable):
        variable_name = variable_node.variable
        declaration = codegen.vpool.pool[variable_name]
        return declaration.addr


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
