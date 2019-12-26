class Declarations:
    def __init__(self, ):
        self.declarations = []

    def add_declaration(self, declaration):
        self.declarations.append(declaration)


class VariableDeclaration:
    def __init__(self, id):
        self.id = id


class ArrayDeclaration:
    def __init__(self, id, start, end):
        self.id = id
        self.start_index = start
        self.end_index = end
