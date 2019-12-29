from src.ast.val_ident import IdentifierVariable, IdentifierArrayNumber, IdentifierArrayVariable


def create_variable_typearr():
    return [type(IdentifierVariable())]


def create_array_typearr():
    return [type(IdentifierArrayVariable()), type(IdentifierArrayNumber())]


class Declarations:
    def __init__(self, ):
        self.declarations = []

    def add_declaration(self, declaration):
        self.declarations.append(declaration)

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return self.declarations


class VariableDeclaration:
    def __init__(self, id, line, initialized=False, local=False, addr=False):
        self.id = id
        self.line = line
        self.initialized = initialized
        self.local = local
        self.addr = addr

    @staticmethod
    def is_leaf(): return True

    @staticmethod
    def variable_types():
        return create_variable_typearr()

    @staticmethod
    def type_info():
        return "int variable"


class ArrayDeclaration:
    def __init__(self, id, start, end, line, local=False, addr=[]):
        self.id = id
        self.start_index = start
        self.end_index = end
        self.line = line
        self.local = local
        self.initialized = [False for _ in range(start, end + 1)]
        self.addr = []

    @staticmethod
    def is_leaf(): return True

    @staticmethod
    def variable_types():
        return create_array_typearr()

    @staticmethod
    def type_info():
        return "int array"
