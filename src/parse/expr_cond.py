from src.ast.expr_cond import *


def create_binary_expression(p):
    expr = BinaryExpression(p[1], p[2], p[3])
    p[0] = expr


def create_unary_expression(p):
    expr = UnaryExpression(p[1])
    p[0] = expr


def create_binary_conditon(p):
    cond = BinaryCondition(p[1], p[2], p[3])
    p[0] = cond
