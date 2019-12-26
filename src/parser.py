import ply.yacc as yacc
from src.tokrules import tokens

# ordered from lowest to highest precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left, TIMES', 'DIV', 'MOD')
)


def p_plus(p):
    """expression : value PLUS value"""
    p[0] = 10
    pass

