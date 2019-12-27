class BinaryExpression:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right


class UnaryExpression:
    def __init__(self, value_or_identifier):
        self.expression = value_or_identifier


class BinaryCondition:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right
