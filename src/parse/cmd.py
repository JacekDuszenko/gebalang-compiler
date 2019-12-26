from src.ast_model.command import AssignCommand, IfThenCommand, IfThenElseCommand, WhileCommand


def create_assign_command(p):
    cmd = AssignCommand(p[1], [3])
    p[0] = cmd


def create_if_then_command(p):
    cmd = IfThenCommand(p[2], p[4])
    p[0] = cmd


def create_if_then_else_command(p):
    cmd = IfThenElseCommand(p[2], p[4], p[6])
    p[0] = cmd


def create_while_command(p):
    cmd = WhileCommand(p[2], p[4])
    p[0] = cmd
