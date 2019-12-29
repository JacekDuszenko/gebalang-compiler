from src.ast import *


class AssignCgStrat:
    @staticmethod
    def is_applicable(node):
        return isinstance(node, AssignCommand)

    @staticmethod
    def apply(visitor, node, codegen):
        return ""
