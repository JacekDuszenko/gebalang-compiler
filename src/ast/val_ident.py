class Value:
    def __init__(self, value):
        self.value = value

    def is_leaf(self): return isinstance(self.value, int) or isinstance(self.value, str)

    def get_children(self):
        if self.is_leaf():
            raise Exception("this shouldn't have happened")
        return [self.value]


class IdentifierVariable:
    def __init__(self, variable):
        self.variable = variable

    @staticmethod
    def is_leaf(): return True


class IdentifierArrayVariable:
    def __init__(self, array, variable):
        self.array = array
        self.variable = variable

    @staticmethod
    def is_leaf(): return True


class IdentifierArrayNumber:
    def __init__(self, array, number):
        self.array = array
        self.number = number

    @staticmethod
    def is_leaf(): return True
