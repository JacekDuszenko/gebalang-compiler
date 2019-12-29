from src.ast import *


class IfThenCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, IfThenCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return ""
