from src.ast import *


class ReadCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ReadCommand)

    @staticmethod
    def apply(visitor, node, codeg):
        return ""
