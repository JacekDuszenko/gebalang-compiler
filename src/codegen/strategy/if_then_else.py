from src.ast import *


class IfThenElseCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, IfThenElseCommand)

    def apply(self, visitor, node, codegen):
        return ""