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
    def __init__(self, id):
        self.id = id

    @staticmethod
    def is_leaf(): return True


class ArrayDeclaration:
    def __init__(self, id, start, end):
        self.id = id
        self.start_index = start
        self.end_index = end

    @staticmethod
    def is_leaf(): return True