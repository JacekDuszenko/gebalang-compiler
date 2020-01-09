from src.ast import *


class DoWhileCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, DoWhileCommand)


    def apply(self, visitor, node, codegen):
        return ""
