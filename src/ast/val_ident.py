class Value:
    def __init__(self, value):
        self.value = value


class IdentifierVariable:
    def __init__(self, variable):
        self.variable = variable


class IdentifierArrayVariable:
    def __init__(self, array, variable):
        self.array = array
        self.variable = variable


class IdentifierArrayNumber:
    def __init__(self, array, number):
        self.array = array
        self.number = number
