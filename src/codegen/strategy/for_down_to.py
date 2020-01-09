from src.ast import *


class ForDownToCgStrat:

    @staticmethod
    def is_applicable(node):
        return isinstance(node, ForDownToCommand)


    def apply(self,visitor, node, codegen):
        return ""
