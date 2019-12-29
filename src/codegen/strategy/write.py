from src.ast import *


class WriteCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, WriteCommand)

    @staticmethod
    def apply(visitor, node, codeg):
        return ""
