class BinaryExpression:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.left] + [self.right]


class UnaryExpression:
    def __init__(self, value_or_identifier):
        self.expression = value_or_identifier

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.expression]


class BinaryCondition:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.left] + [self.right]
