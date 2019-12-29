from src.ast import *


class ForUpToCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ForUpToCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return ""
