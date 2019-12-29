from src.ast import *


class ForDownToCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ForDownToCommand)

    @staticmethod
    def apply(visitor, node, codeg):
        return ""
