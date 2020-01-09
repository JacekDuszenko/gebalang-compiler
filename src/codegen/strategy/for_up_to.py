from src.ast import *


class ForUpToCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ForUpToCommand)


    def apply(self, visitor, node, codegen):
        return ""
