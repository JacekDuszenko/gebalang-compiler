class BinaryExpression:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right


class BinaryCondition:
    def __init__(self, left, type, right):
        self.left = left
        self.type = type
        self.right = right
