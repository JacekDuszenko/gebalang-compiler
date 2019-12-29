from src.ast import *


class WhileCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, WhileCommand)

    @staticmethod
    def apply(visitor, node, codeg):
        return ""
