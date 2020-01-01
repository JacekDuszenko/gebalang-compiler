from src.ast import *
from src.codegen.create_constant import create_constant_number


class WriteCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, WriteCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        if node.value.is_leaf():
            result = ""
            result += create_constant_number(node.value.value)
            result = put(result)
            return result


def put(result):
    result += "PUT"
    return result
