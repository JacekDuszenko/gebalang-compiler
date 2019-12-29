from src.ast import *


class IfThenElseCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, IfThenElseCommand)

    @staticmethod
    def apply(visitor, node, codeg):
        return ""