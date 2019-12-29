from src.ast import *


class DoWhileCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, DoWhileCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return ""
