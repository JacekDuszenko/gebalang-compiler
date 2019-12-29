class Value:
    def __init__(self, value, line):
        self.value = value
        self.line = line

    def is_leaf(self): return isinstance(self.value, int) or isinstance(self.value, str)

    def get_children(self):
        if self.is_leaf():
            raise Exception("this shouldn't have happened")
        return [self.value]


class IdentifierVariable:
    def __init__(self, variable='', line=0, local=False):
        self.variable = variable
        self.line = line
        self.local = local

    @staticmethod
    def is_leaf(): return True


class IdentifierArrayVariable:
    def __init__(self, variable='', accessor='', line=0):
        self.variable = variable
        self.accessor = accessor
        self.line = line

    @staticmethod
    def is_leaf(): return True


class IdentifierArrayNumber:
    def __init__(self, variable='', accessor='', line=0):
        self.variable = variable
        self.accessor = accessor
        self.line = line

    @staticmethod
    def is_leaf(): return True
