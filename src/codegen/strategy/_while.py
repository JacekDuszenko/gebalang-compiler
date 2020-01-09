from src.ast import *


class WhileCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, WhileCommand)


    def apply(self, visitor, node, codegen):
        return ""
